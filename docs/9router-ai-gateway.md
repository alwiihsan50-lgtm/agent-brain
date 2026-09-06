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

---

## ⚡ 4. Token Saver: Integrasi Headroom (Context Optimization)

Headroom (`headroom-ai`) adalah layer kompresi context pintar untuk LLM. Bekerja dengan cara mengompresi pesan/prompt via endpoint `/v1/compress` sebelum dialihkan ke provider model:

- **Versi Terpasang:** `headroom-ai v0.37.0` (Extras: `[proxy,code]`)
- **Binary Path:** `/home/cuker/.local/bin/headroom`
- **Proxy Port:** `8787` (`http://localhost:8787`)
- **Headroom Dashboard:** `http://localhost:8787/dashboard` atau via 9Router proxy: `http://localhost:20128/api/headroom/proxy/dashboard`
- **9Router Token Saver Settings:** `http://localhost:20128/dashboard/token-saver`
- **Fitur Aktif:**
  - `SmartCrusher`: Kompresi struktur JSON, tool outputs, dan whitespace tanpa menghilangkan makna semantik.
  - `Code-Aware (Tree-Sitter)`: AST-based compression untuk bahasa pemrograman (Python, JS, TS, Go, Rust, Java, C, C++, dll.).
- **Pengaturan Environment:**
  - File `~/.config/pip/pip.conf` dikonfigurasi `break-system-packages = true` agar 9Router UI dapat mengelola extras pip secara seamless di Linux Mint 22 (PEP 668).
- **Process Management:**
  - PID file: `~/.9router/headroom/proxy.pid`
  - Log file: `~/.9router/headroom/proxy.log`
  - Kontrol via 9Router: tombol **Start/Stop/Manage Headroom** di tab `Token Saver`.

