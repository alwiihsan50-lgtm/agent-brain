#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unified Obsidian x Graphify Synchronization Suite
==================================================
Builds a persistent Master Obsidian Vault at /media/cuker/Data/ObsidianVault/
combining agent-brain long-term memory with micro-level Graphify knowledge graphs
for all active projects in Drive D:.
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

# Use graphify python environment
PYTHON_BIN = "/home/cuker/.local/share/uv/tools/graphifyy/bin/python"

from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html, to_obsidian
from graphify.extract import collect_files, extract
from graphify.detect import detect

VAULT_DIR = Path("/media/cuker/Data/ObsidianVault")
PROJECTS_ROOT = Path("/media/cuker/Data/Projects")
AGENT_BRAIN_DIR = Path("/home/cuker/agent-brain")


def setup_vault_structure():
    """Create clean folder hierarchy in the master Obsidian Vault."""
    print("======================================================")
    print(" 🧠🕸️ Sinkronisasi Master Obsidian x Graphify Vault  ")
    print("======================================================")
    print(f"-> Lokasi Master Vault: {VAULT_DIR}")
    
    (VAULT_DIR / "00 - Agent Brain" / "docs").mkdir(parents=True, exist_ok=True)
    (VAULT_DIR / "00 - Agent Brain" / "docs" / "history").mkdir(parents=True, exist_ok=True)
    (VAULT_DIR / "01 - Projects").mkdir(parents=True, exist_ok=True)
    (VAULT_DIR / "02 - Knowledge Base").mkdir(parents=True, exist_ok=True)


def sync_agent_brain_docs():
    """Sync central agent-brain markdown docs into Obsidian Vault."""
    print("\n[1/4] Menyinkronkan Agent Brain central docs...")
    target_ab = VAULT_DIR / "00 - Agent Brain"
    
    # Copy main README and AGENTS.md
    for f in ["README.md", "AGENTS.md", "CLAUDE.md"]:
        src = AGENT_BRAIN_DIR / f
        if src.is_file():
            shutil.copy2(src, target_ab / f)
            
    # Copy docs folder
    src_docs = AGENT_BRAIN_DIR / "docs"
    if src_docs.is_dir():
        for doc in src_docs.glob("*.md"):
            shutil.copy2(doc, target_ab / "docs" / doc.name)
        hist_dir = src_docs / "history"
        if hist_dir.is_dir():
            for h in hist_dir.glob("*.md"):
                shutil.copy2(h, target_ab / "docs" / "history" / h.name)
                
    print("    ✓ Agent Brain docs tersinkronisasi ke vault.")


def process_single_project(p_path):
    """Run Graphify extraction and export to Obsidian for a single project."""
    p_path = Path(p_path).resolve()
    p_name = p_path.name
    
    # Ignore build/dist/git folders
    if p_name.startswith(".") or p_name in ["_migration-report", "test folder"]:
        return None

    try:
        det_res = detect(p_path)
    except Exception as e:
        print(f"    [!] Error detecting {p_name}: {e}")
        return None

    if det_res.get('total_files', 0) == 0:
        return None

    code_files = []
    for f in det_res.get('files', {}).get('code', []):
        code_files.extend(collect_files(Path(f)) if Path(f).is_dir() else [Path(f)])

    ast_res = {'nodes': [], 'edges': []}
    if code_files:
        try:
            ast_res = extract(code_files, cache_root=p_path)
        except Exception as e:
            print(f"    [!] AST extract error in {p_name}: {e}")

    # Build graph
    extraction = {
        'nodes': ast_res.get('nodes', []),
        'edges': ast_res.get('edges', []),
        'hyperedges': [],
        'input_tokens': 0,
        'output_tokens': 0
    }

    if not extraction['nodes']:
        return None

    try:
        G = build_from_json(extraction, root=str(p_path), directed=False)
        if G.number_of_nodes() == 0:
            return None

        communities = cluster(G)
        cohesion = score_all(G, communities)
        gods = god_nodes(G)
        surprises = surprising_connections(G, communities)
        labels = {cid: f"{p_name} Modul {cid}" for cid in communities}
        questions = suggest_questions(G, communities, labels)

        # 1. Local graphify-out in project
        local_out = p_path / "graphify-out"
        local_out.mkdir(parents=True, exist_ok=True)
        to_json(G, communities, str(local_out / "graph.json"), force=True)
        to_html(G, communities, str(local_out / "graph.html"), community_labels=labels)
        report = generate(G, communities, cohesion, labels, gods, surprises, det_res, {'input':0,'output':0}, str(p_path), suggested_questions=questions)
        (local_out / "GRAPH_REPORT.md").write_text(report, encoding='utf-8')

        # 2. Obsidian Export in Master Vault
        dest_obsidian = VAULT_DIR / "01 - Projects" / p_name
        # Clean old generated notes in destination
        if dest_obsidian.is_dir():
            shutil.rmtree(dest_obsidian)
        dest_obsidian.mkdir(parents=True, exist_ok=True)
        note_count = to_obsidian(G, communities, str(dest_obsidian), community_labels=labels, cohesion=cohesion)

        # 3. Install Git Hook
        git_dir = p_path / ".git"
        if git_dir.is_dir():
            hook_path = git_dir / "hooks" / "post-commit"
            hook_path.parent.mkdir(parents=True, exist_ok=True)
            hook_content = """#!/bin/bash
# Auto-update graphify knowledge graph on new commit
if command -v graphify >/dev/null 2>&1; then
    if [ -d "graphify-out" ]; then
        (graphify update . >/dev/null 2>&1 &)
    fi
fi
"""
            hook_path.write_text(hook_content, encoding='utf-8')
            try:
                os.chmod(hook_path, 0o755)
            except Exception:
                pass

        print(f"    ✓ {p_name:<32} -> {G.number_of_nodes():>3} nodes, {G.number_of_edges():>3} edges | {note_count} Obsidian notes")
        return {
            'name': p_name,
            'path': str(p_path),
            'nodes': G.number_of_nodes(),
            'edges': G.number_of_edges(),
            'communities': len(communities),
            'notes': note_count,
            'god_nodes': [g.get('label', g.get('id', '')) for g in gods[:3]] if gods else []
        }
    except Exception as e:
        print(f"    [!] Failed to build graph for {p_name}: {e}")
        return None


def sync_all_projects():
    """Scan and process all projects in Drive D:."""
    print("\n[2/4] Mengekstrak AST Graphify & membangun Obsidian Notes per proyek...")
    results = []
    
    # 1. Projects root
    for entry in sorted(PROJECTS_ROOT.iterdir()):
        if entry.is_dir():
            # If subfolder has project (e.g. Monitor-Sistem-Desktop-v1.1/Monitor-Sistem-Desktop)
            sub_proj = entry / entry.name.replace("-v1.1", "")
            target_p = sub_proj if sub_proj.is_dir() else entry
            res = process_single_project(target_p)
            if res:
                results.append(res)
                
    # 2. Marketing agent workplace
    mkt_dir = Path("/media/cuker/Data/marketing agent")
    if mkt_dir.is_dir():
        for entry in sorted(mkt_dir.iterdir()):
            if entry.is_dir():
                res = process_single_project(entry)
                if res:
                    results.append(res)

    # 3. Agent-brain repo itself
    res_ab = process_single_project(AGENT_BRAIN_DIR)
    if res_ab:
        results.append(res_ab)

    return results


def generate_master_dashboard(projects_summary):
    """Generate 00 - Master Dashboard.md in Obsidian."""
    print("\n[3/4] Menghasilkan 00 - Master Dashboard.md & Peta Ekosistem...")
    
    dash_path = VAULT_DIR / "00 - Master Dashboard.md"
    
    content = [
        "# 🌌 Master Workspace Dashboard (Agent-Brain × Graphify)",
        "",
        "> 🧠 **Central Knowledge Graph & Long-Term Memory Hub**",
        "> Seluruh proyek, arsitektur sistem, port terpesan, dan grafik dependensi kode terintegrasi otomatis di sini.",
        "",
        "---",
        "",
        "## 📌 Quick Access: Sistem & Dokumen Utama",
        "",
        "- 📄 [[00 - Agent Brain/README|🚀 Central System Status & Protocol]]",
        "- 📄 [[00 - Agent Brain/AGENTS|🔒 SOP & Protokol Memori AI Agent]]",
        "- 📄 [[00 - Agent Brain/docs/system-environment-and-ports|🔌 System Environment & Reserved Ports]]",
        "- 📄 [[00 - Agent Brain/docs/stb-rockchip-web-remote-architecture|📺 STB RockChip 4-Tab Hub]]",
        "- 📄 [[00 - Agent Brain/docs/mt5-docker-forex-trading-automation|📈 MT5 Exness Forex Automation]]",
        "- 📄 [[00 - Agent Brain/docs/cloudflare-manager-architecture-and-dns-mapping|☁️ Cloudflare Zero Trust & DNS Hub]]",
        "- 📄 [[00 - Agent Brain/docs/agent-brain-and-graphify-synergy-guide|🕸️ Panduan Sinergi Agent-Brain & Graphify]]",
        "",
        "---",
        "",
        "## 📂 Katalog Proyek Aktif & Knowledge Graph",
        "",
        "| Proyek | Nodes | Relasi | Komunitas | Catatan Obsidian | God Nodes Utama |",
        "| :--- | :---: | :---: | :---: | :---: | :--- |"
    ]
    
    for p in projects_summary:
        p_name = p['name']
        god_str = ", ".join([f"`{g}`" for g in p['god_nodes']]) if p['god_nodes'] else "-"
        link_str = f"[[01 - Projects/{p_name}/index|{p_name}]]"
        content.append(f"| **{link_str}** | {p['nodes']} | {p['edges']} | {p['communities']} | {p['notes']} | {god_str} |")
        
    content.extend([
        "",
        "---",
        "",
        "## 🛠️ Panduan Alur Kerja (Workflow Guide)",
        "",
        "### 1. Navigasi Cepat di Obsidian:",
        "- **Buka Graph View**: Tekan `Ctrl + G` di Obsidian untuk melihat seluruh jaring relasi antar proyek dan modul.",
        "- **Pencarian Cepat**: Tekan `Ctrl + O` dan ketik nama fungsi/class/dokumen apa pun.",
        "- **Backlinks Panel**: Buka panel kanan untuk melihat semua file yang mereferensikan modul yang sedang dibuka.",
        "",
        "### 2. Sinergi dengan AI Agent:",
        "- Setiap commit Git akan otomatis memperbarui graf berkat **Git Post-Commit Hook**.",
        "- AI Agent dapat mengeksplorasi modul spesifik dengan perintah:",
        "  ```bash",
        "  graphify query \"<pertanyaan arsitektur>\"",
        "  graphify path \"<fungsi_A>\" \"<fungsi_B>\"",
        "  graphify explain \"<NamaClass>\"",
        "  ```",
        "",
        "---",
        "*Dashboard ini diperbarui otomatis oleh `sync-obsidian-graphify.py`.*"
    ])
    
    dash_path.write_text("\n".join(content), encoding='utf-8')
    print("    ✓ Master Dashboard berhasil dibuat di: 00 - Master Dashboard.md")


def create_ecosystem_canvas(projects_summary):
    """Generate an Obsidian Canvas linking all projects visually."""
    print("\n[4/4] Membuat 00 - Ecosystem Map.canvas...")
    canvas_path = VAULT_DIR / "00 - Ecosystem Map.canvas"
    
    nodes = []
    edges = []
    
    # Center Node: Agent-Brain
    nodes.append({
        "id": "agent-brain-center",
        "type": "file",
        "file": "00 - Agent Brain/README.md",
        "x": 0,
        "y": 0,
        "width": 380,
        "height": 240
    })
    
    # Project Nodes arranged around center
    import math
    n_proj = len(projects_summary)
    radius_x = 900
    radius_y = 650
    
    for i, p in enumerate(projects_summary):
        angle = (2 * math.pi * i) / max(n_proj, 1)
        px = int(math.cos(angle) * radius_x)
        py = int(math.sin(angle) * radius_y)
        p_name = p['name']
        node_id = f"proj-{p_name}"
        
        index_file = f"01 - Projects/{p_name}/index.md"
        
        nodes.append({
            "id": node_id,
            "type": "file",
            "file": index_file,
            "x": px,
            "y": py,
            "width": 300,
            "height": 180
        })
        
        edges.append({
            "id": f"edge-ab-{p_name}",
            "fromNode": "agent-brain-center",
            "fromSide": "bottom" if py > 0 else "top",
            "toNode": node_id,
            "toSide": "top" if py > 0 else "bottom",
            "label": f"{p['nodes']} nodes"
        })
        
    canvas_data = {
        "nodes": nodes,
        "edges": edges
    }
    
    canvas_path.write_text(json.dumps(canvas_data, indent=2), encoding='utf-8')
    print("    ✓ Obsidian Canvas visual dibuat: 00 - Ecosystem Map.canvas")


def main():
    setup_vault_structure()
    sync_agent_brain_docs()
    projects_summary = sync_all_projects()
    generate_master_dashboard(projects_summary)
    create_ecosystem_canvas(projects_summary)
    
    print("\n======================================================")
    print(" 🎉 [SELESAI] Master Obsidian x Graphify Vault Siap! ")
    print("======================================================")
    print(f" • Folder Vault: {VAULT_DIR}")
    print(" • Total Proyek Terindeks:", len(projects_summary))
    print(" • Buka Obsidian lalu pilih 'Open folder as vault' -> pilih:")
    print(f"   {VAULT_DIR}")
    print("======================================================")


if __name__ == "__main__":
    main()
