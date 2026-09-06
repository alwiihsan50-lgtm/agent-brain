# 🌐 9Router - AI Routing Gateway & Token Saver

9Router adalah smart AI proxy gateway lokal untuk me-route request coding assistant (Claude Code, Cursor, Antigravity, OpenCode, Cline, Codex, dll.) ke 40+ AI providers dengan fitur auto-fallback dan RTK (Request Token Keeper).

---

## 📌 1. Informasi Instalasi & Lingkungan

| Parameter | Nilai / Konfigurasi |
| :--- | :--- |
| **Versi Terpasang** | `0.5.69` |
| **Binary Path** | `/home/cuker/.local/bin/9router` |
| **Node Module Path** | `/home/cuker/.local/lib/node_modules/9router` |
| **Data & SQLite DB** | `/home/cuker/.9router/db/data.sqlite` |
| **Runtime Dependencies** | `~/.9router/runtime/node_modules` (`better-sqlite3`, `systray2`) |
| **Default Port** | `20128` (Dashboard & API) |
| **OpenAI-Compatible API** | `http://localhost:20128/v1` |
| **Web Dashboard** | `http://localhost:20128/dashboard` |

---

## 🚀 2. Cara Menjalankan & Perintah CLI

```bash
# 1. Jalankan interaktif (akan menampilkan pilihan Web UI, CLI, atau Background)
9router

# 2. Jalankan di background (Tray Mode)
9router -t

# 3. Jalankan tanpa membuka browser otomatis & tampilkan log
9router -n -l

# 4. Cek bantuan dan opsi lengkap
9router --help
```

---

## ⚙️ 3. Integrasi dengan AI Coding Tools

Untuk menyambungkan tool (Cursor, Claude Code, Cline, RooCode, dll.) ke 9Router:

- **Base URL / Endpoint:** `http://localhost:20128/v1`
- **API Key:** Dapatkan dari Web Dashboard (`http://localhost:20128/dashboard`)
- **Model:** Sesuaikan dengan provider yang diaktifkan (misal: `kr/claude-sonnet-4.5`, Kiro AI, OpenCode Free, dll.)
