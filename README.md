# Agent Brain - Central Context & Workspace

Repositori ini adalah sistem memori terpusat (*Shared Memory System*) dan tempat penyimpanan dokumentasi bersama untuk seluruh AI Agent lintas platform.

> 🔒 **ATURAN KEKEBALAN PROTOKOL (IMMUTABILITY CONSTRAINT):**
> Seluruh aturan arsitektur, batasan port (`53317`, `3000`, `8080`), dan sinergi `agent-brain` + `graphify` bersifat **PERMANEN**.
> Model AI Agent apa pun (Gemini, Claude, GPT, DeepSeek, Antigravity, dll.) **DILARANG KERAS** mengubah atau merusak protokol ini kecuali diminta secara spesifik oleh USER.

---

## 📌 Status Sistem & Lingkungan Aktif

| Layanan / Komponen | Port / Endpoint | Status | Deskripsi |
| :--- | :--- | :--- | :--- |
| **mentari-server (CasaOS)** | `server.abbas.my.id` / `casa.abbas.my.id` | 🟢 Live | Web GUI Dashboard (Port 80) & Debian 13 Server via Cloudflare Tunnel 24/7. |
| **Cloudflare Zero Trust** | `*.abbas.my.id` | 🟢 Aktif | Akses remote PIN OTP `alwiihsan50@gmail.com` & sesi persisten **30 Hari**. |
| **TailShare** | `Port 53317` / `share.abbas.my.id` | 🟢 Running | Live sync folder Drive D (`D:\tailshare`) & GUI Native Electron. |
| **MT5 Docker Exness** | `Port 3000` / `mt5.abbas.my.id` | 🟢 Running | Wine Python MetaTrader 5 di `mentari-server` (`/home/mentari/mt5_storage`). |
| **MT5 Web Dashboard** | `Port 8080` / `dashboard.abbas.my.id` | 🟢 Running | Zero-flicker live monitoring & PWA Standalone Safari iOS (`mentari-server`). |
| **Web Push Hub** | `mt5-push-backend.alwiihsan50.workers.dev` | 🟢 Live | Hub notifikasi push universal 24/7 (Cloudflare Workers + KV). |
| **Infisical Secret Vault** | `app.infisical.com` / `infisical` CLI | 🟢 Synced | 13 kredensial infrastruktur E2EE tersimpan di environment `dev` & `prod`. |
| **Trading Risk Engine** | `mt5_config/bot.py` | 🟢 Aktif | ATR Volatility Grid Multi-pair scanner dengan Dynamic Spacing & Circuit Breaker. |
| **Arsip-IMO** | `/media/cuker/Data/Projects/Arsip-IMO` | 🟢 Synced | Single branch `main` stabil terverifikasi. |

- **Dual-Engine Protocol:** `agent-brain` (Global Strategy) + `graphify` (Local AST Code Intelligence).
- **Global Excludes:** `graphify-out/` dan `.graphify_*` di-ignore secara global via `~/.gitignore_global`.
- **Last Updated By:** Antigravity AI Agent (Google DeepMind)
- **Last Updated At:** 2026-08-15 22:38 WIB

---

## 🚀 Progress & Task Aktif

- [x] Optimasi arsitektur **Dual-Engine (`agent-brain` + `graphify`)**:
  - Penambahan klausul **Immutability & Integrity Guardrail** (kebal dari perubahan otomatis oleh model AI yang berganti-ganti).
  - Penambahan aturan **Auto-Init Fallback** (`graphify .` otomatis jika graf belum ada).
  - Setup **Global Git Ignore** (`~/.gitignore_global`) untuk isolasi artefak `graphify-out/`.
  - Pembuatan script dan panduan **Git Post-Commit Hook** auto-sync di `docs/git-post-commit-graphify-hook.md`.
  - **Memory Token-Budgeting:** Arsip milestone lampau dipindahkan ke `docs/history/completed-milestones-archive.md`.
  - Penambahan developer shortcuts di `~/.bash_aliases` (`gf`, `gfu`, `gfq`, `gf-viz`, `brain-sync`, `brain-push`).
- [x] Onboarding & konfigurasi infrastruktur **mentari-server** (Debian 13 Trixie, Tailscale SSH, Docker v29.7.2, Passwordless Sudo, persistent auto-start).
- [x] Setup **Cloudflare Tunnel (`mentari-tunnel`)** 24/7 untuk CasaOS Web GUI di **`https://server.abbas.my.id`** dan **`https://casa.abbas.my.id`** (Auto-SSL HTTPS, systemd persistent).
- [x] **Migrasi Penuh MT5 Trading Bot & Dashboard ke `mentari-server`:**
  - Build image Docker `mt5:latest` (Wine32 + Wine64 + Openbox KasmVNC) di `mentari-server`.
  - Transfer direktori Wine, MT5, Python 3.9, bot logic, dan realtime dashboard ke `/home/mentari/mt5_storage`.
  - Konfigurasi systemd unit 24/7 `mt5-trading-bot.service` (auto-restart saat booting server).
  - Setup Cloudflare Tunnel routing untuk `https://dashboard.abbas.my.id` (Port 8080) dan `https://vnc.abbas.my.id` (Port 3000) dengan proteksi Zero Trust PIN OTP.
- [ ] *(Siap untuk task / fitur baru dari pengguna)*

---

## 📚 Indeks Dokumentasi (`docs/`)

- 📄 [**Infrastruktur mentari-server Debian**](docs/mentari-server-debian-infrastructure.md) — Spesifikasi, remote SSH key, dan manajemen container.
- 📄 [**Arsip Milestone & Riwayat Lengkap**](docs/history/completed-milestones-archive.md) — Log lengkap seluruh fitur & milestone terdahulu.
- 📄 [**System Environment, Ports & Remote Access**](docs/system-environment-and-ports.md) — Port terpesan, Cloudflare Tunnel & Zero Trust.
- 📄 [**Panduan Sinergi agent-brain & graphify**](docs/agent-brain-and-graphify-synergy-guide.md) — Integrasi memori makro dan knowledge graph mikro.
- 📄 [**Git Post-Commit Hook Graphify**](docs/git-post-commit-graphify-hook.md) — Panduan auto-sync knowledge graph saat commit.
- 📄 [**Universal Web Push Notification Service**](docs/universal-web-push-notification-service.md) — Hub notifikasi REST API (Python, JS, Go, cURL).
- 📄 [**Automasi Trading MT5 & Cloudflare Push**](docs/mt5-docker-forex-trading-automation.md) — Setup bot MT5 Docker, Wine Python, dynamic risk calculation.
- 📄 [**Web Push Notification Safari iOS**](docs/safari-ios-web-push-notification.md) — Syarat PWA Safari iOS, Service Worker, dan VAPID.
- 📄 [**TailShare Linux Mint Guide**](docs/tailshare-linux-mint-installation.md) — Panduan instalasi dan auto-start TailShare.
- 📄 [**Katalog Proyek Drive D**](docs/drive-d-projects-catalog.md) — Pemetaan 18 repositori Git aktif di Drive `D:\Projects`.
- 📄 [**Arsip-IMO Specification**](docs/arsip-imo-project.md) — Dokumentasi arsitektur dan UI/UX proyek Arsip-IMO.
- 📄 [**Kustomisasi Workflow Linux Mint**](docs/linux-mint-developer-workflow-customizations.md) — Starship, Zoxide, FZF, LazyDocker, Btop, aliases.
