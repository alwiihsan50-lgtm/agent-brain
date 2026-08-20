# Agent Brain - Central Context & Workspace

Repositori ini adalah sistem memori terpusat (*Shared Memory System*) dan tempat penyimpanan dokumentasi bersama untuk seluruh AI Agent lintas platform.

> 🔒 **ATURAN KEKEBALAN PROTOKOL (IMMUTABILITY CONSTRAINT):**
> Seluruh aturan arsitektur, batasan port (`40506`, `3000`, `8080`), dan sinergi `agent-brain` + `graphify` bersifat **PERMANEN**.
> Model AI Agent apa pun (Gemini, Claude, GPT, DeepSeek, Antigravity, dll.) **DILARANG KERAS** mengubah atau merusak protokol ini kecuali diminta secara spesifik oleh USER.

---

## 📌 Status Sistem & Lingkungan Aktif

| Layanan / Komponen | Port / Endpoint | Status | Deskripsi |
| :--- | :--- | :--- | :--- |
| **Cloudflare Manager & DNS** | `abbas.my.id` / Infisical | 🟢 Full Access | Token API Full Access terverifikasi (DNS, Zone, SSL, WAF, Tunnels, Zero Trust, Workers). |
| **mentari-server (CasaOS)** | `server.abbas.my.id` / `casa.abbas.my.id` | 🟢 Live | Web GUI Dashboard (Port 80) & Debian 13 Server via Cloudflare Tunnel 24/7. |
| **Cloudflare Zero Trust** | `*.abbas.my.id` | 🟢 Aktif | Akses remote PIN OTP `alwiihsan50@gmail.com` & sesi persisten **30 Hari**. |
| **PNPM Global Store** | `~/.local/share/pnpm/store/v11` | 🟢 Aktif | Standardisasi Node.js Package Manager: Shared disk space & hard-linked virtual store. |
| **TailShare** | `Port 40506` / `share.abbas.my.id` | 🟢 Running | Live sync folder Drive D (`/media/cuker/Data/tailshare`) & GUI Native Electron. |
| **MT5 Docker Exness** | `Port 3000` / `mt5.abbas.my.id` | 🟢 Running | Wine Python MetaTrader 5 di `mentari-server` (`/home/mentari/mt5_storage`). |
| **MT5 Web Dashboard** | `Port 8080` / `dashboard.abbas.my.id` | 🟢 Running | Zero-flicker live monitoring & PWA Standalone Safari iOS (`mentari-server`). |
| **Web Push Hub** | `mt5-push-backend.alwiihsan50.workers.dev` | 🟢 Live | Hub notifikasi push universal 24/7 (Cloudflare Workers + KV). |
| **STB Web Remote** | `Port 8085` / Tailscale `erza` | 🟢 Running | Remote TV: Virtual cursor 60 FPS, draggable 4-way scroll, focal zoom, clean RAM daemon. |
| **Infisical Secret Vault** | `app.infisical.com` / `infisical` CLI | 🟢 Synced | 10 kredensial infrastruktur E2EE tersimpan di `dev` & `prod`. |
| **Trading Risk Engine** | `mt5_config/bot.py` | 🟢 Aktif | ATR Volatility Grid Multi-pair scanner dengan Dynamic Spacing & Circuit Breaker. |
| **AI Browser Suite** | `~/.ai-browser-tools` & MCP | 🟢 Terpasang | `@playwright/mcp` Server, `crawl4ai` Async Extractor, dan `browser-use` Agent. |
| **Arsip-IMO** | `/media/cuker/Data/Projects/Arsip-IMO` | 🟢 Synced | Single branch `main` stabil terverifikasi. |

- **Dual-Engine Protocol:** `agent-brain` (Global Strategy) + `graphify` (Local AST Code Intelligence).
- **Global Excludes:** `graphify-out/` dan `.graphify_*` di-ignore secara global via `~/.gitignore_global`.
- **Last Updated By:** Antigravity AI Agent (Google DeepMind)
- **Last Updated At:** 2026-08-20 11:24 WIB

---

## 🚀 Progress & Task Aktif

- [x] **Notifikasi Otomatis Boot & Idle PC ke Smartphone:** Membuat skrip daemon `boot-ready-notify.py` dan systemd service `boot-ready-notify.service` yang otomatis mendeteksi koneksi internet dan stabilisasi idle sistem saat PC baru menyala, lalu mengirim ringkasan status boot (durasi, CPU load, RAM, IP LAN/Tailscale, status Docker MT5) via Cloudflare Web Push Hub ke iPhone.
- [x] **Optimasi Memori & Prefetching Linux Mint (16 GB RAM):** Memasang daemon `preload` untuk adaptive application prefetching, mengaktifkan `tmpfs` pada `/tmp` (~7.7 GB RAM) via `tmp.mount`, serta mengonfigurasi sysctl kernel `vm.swappiness=10` dan `vm.vfs_cache_pressure=50` di `/etc/sysctl.d/99-performance-tuning.conf`.
- [x] **Standardisasi PNPM & Optimasi Shared node_modules Global Store:** Memasang PNPM v11 global dan memigrasi seluruh repositori lokal (`tailshare`, `SIMPKK-DIGITAL`, `push-backend`, `cf-push-backend`, `mt5_storage/cf-push-backend`, `bot_push_server/backend`) ke Global Content-Addressable Store (`~/.local/share/pnpm/store/v11`) guna menghemat ratusan megabyte/gigabyte ruang penyimpanan. Dokumentasi lengkap di `docs/pnpm-global-store-node-modules-optimization.md`.
- [x] **Standarisasi Repositori LPKP Mentari (Web 1 & Web 2):** Mengonfigurasi `AGENTS.md`, Git Hook Auto-Sync Graphify (`post-commit`/`post-checkout`), AST Knowledge Graph (`graphify-out/`), runtime Linux `esbuild` global di Linux Mint, dan menyusun dokumentasi arsitektur di `docs/lpkp-mentari-ecosystem.md`.
- [x] **Pemasangan AI Browser Automation Suite Selesai:** Menginstal dan mengonfigurasi `@playwright/mcp` (MCP Server Antigravity), `crawl4ai` (AI Web Scraping & Clean Markdown Engine), dan `browser-use` (Autonomous Web Navigation Agent) di virtualenv terisolasi `/home/cuker/.ai-browser-tools`.
- [x] **Protokol Konfirmasi Task Belum Selesai (Pending Task Confirmation):** Menambahkan aturan wajib bagi seluruh AI Agent untuk meminta konfirmasi ke USER di awal sesi jika menemukan task belum selesai (`- [ ]`) di `README.md` (apakah ingin dilanjutkan atau diarsip).
- [x] **Perbaikan Bug MT5 Trading Bot & Anti-Spam Push Notification:** Memperbaiki infinite loop & spam notifikasi pada mode NEUTRAL Dual Grid di `bot.py` serta proteksi deduplication dan rate-limiting cooldown 30 detik pada `send_push_notification`.
- [x] **Pembersihan Disk & Kernel Purge (+16 GB Reclaimed) & Advanced System Tuning.**

---

## 📚 Indeks Dokumentasi (`docs/`)

- 📄 [**Standardisasi PNPM & Shared node_modules**](docs/pnpm-global-store-node-modules-optimization.md) — Konfigurasi global store, hard links, dan panduan dependensi Node.js.
- 📄 [**Ekosistem Digital LPKP Mentari**](docs/lpkp-mentari-ecosystem.md) — Arsitektur Web 1 (Astro 7), Web 2 (Next.js 16 LMS), Supabase, & kurikulum pelatihan.
- 📄 [**AI Browser Automation Tools**](docs/ai-browser-automation-tools.md) — Panduan Playwright MCP Server, Crawl4AI, dan Browser-Use.
- 📄 [**STB RockChip Web Remote Architecture**](docs/stb-rockchip-web-remote-architecture.md) — Arsitektur daemon uinput, virtual cursor 60 FPS, draggable scroll pad, and system tuning.
- 📄 [**Cloudflare Manager & DNS Mapping**](docs/cloudflare-manager-architecture-and-dns-mapping.md) — Kredensial Full Access, pemetaan 12 subdomain DNS, dan arsitektur Zero Trust.
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
