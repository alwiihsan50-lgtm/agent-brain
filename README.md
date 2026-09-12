# Agent Brain - Central Context & Workspace

Repositori ini adalah sistem memori terpusat (*Shared Memory System*) dan tempat penyimpanan dokumentasi bersama untuk seluruh AI Agent lintas platform.

> 🔒 **ATURAN KEKEBALAN PROTOKOL (IMMUTABILITY CONSTRAINT):**
> Seluruh aturan arsitektur, batasan port (`40506`, `3000`, `8080`), dan sinergi `agent-brain` + `graphify` bersifat **PERMANEN**.
> Model AI Agent apa pun (Gemini, Claude, GPT, DeepSeek, Antigravity, dll.) **DILARANG KERAS** mengubah atau merusak protokol ini kecuali diminta secara spesifik oleh USER.
> ⚠️ **ATURAN MUTLAK PENYELESAIAN TUGAS:** Pekerjaan baru maupun lama yang belum selesai **DILARANG KERAS** dianggap selesai atau dicentang (`[x]`) sebelum mendapatkan konfirmasi langsung dan validasi dari USER.

---

## 📌 Status Sistem & Lingkungan Aktif

| Layanan / Komponen | Port / Endpoint | Status | Deskripsi |
| :--- | :--- | :--- | :--- |
| **STB Web Remote Hub** | `Port 8080` / `100.122.66.85:8080` | 🟢 Live | Streamlined 3-Tab Hub: Remote, Apps (Official YouTube TV, TV Bro, Tailscale), Settings, Ad & Adult Filter 167k+ domains, HDMI 1080p. |
| **mentari-server (CasaOS)** | `server.abbas.my.id` / `casa.abbas.my.id` | 🟢 Live | Dashboard Web GUI (Port 80) & Debian 13 Server via Cloudflare Tunnel 24/7. |
| **MT5 Dual Container** | `Port 3000` (Acc 1) / `Port 3002` (Acc 2) | 🟢 Running | Dual-instance trading bots: SMC & Liquidity Sweep (Akun 1) + Adaptive Martingale & Basket TP (Akun 2). |
| **Web Push Hub** | `mt5-push-backend.alwiihsan50.workers.dev` | 🟢 Live | Hub notifikasi push universal 24/7 (Cloudflare Workers + KV). |
| **Cloudflare Manager & DNS** | `abbas.my.id` / Zero Trust | 🟢 Full Access | Token API Full Access, 12 Subdomain DNS, PIN OTP `alwiihsan50@gmail.com` (Sesi 30 Hari). |
| **TailShare (original)** | `Port 40506` / `share.abbas.my.id` | 🟢 Running | Multi-network high speed transfer (Wi-Fi Direct `192.168.100.67`, LAN Gigabit `192.168.10.239`, Tailscale, & Cloudflare) + Live sync Drive D (`/media/cuker/Data/tailshare`). |
| **TailShare Clean** | `Port 40507` | 🟢 Running | Minimal file-transfer-only version, same storage `/media/cuker/Data/tailshare`, no clipboard/WS/QR/electron. |
| **AI Photo Eraser (PWA)** | `Port 3005` (Web) / `3003` (API) | 🟢 Running | Mobile-first AI Magic Object Remover with Virtual Mouse Trackpad & LaMa ONNX Inpainting. |
| **Arsip-IMO** | `/media/cuker/Data/Projects/Arsip-IMO` | 🟢 Synced | Production web absensi & schedule system (branch `main`). |
| **Marketing Agents** | `/media/cuker/Data/marketing agent` | 🟢 Aktif | `fbagent/` (FB Marketplace, `mkt`) & `ttagent/` (TikTok Suite, `tt`). |
| **MoneyPrinterTurbo** | `Port 8095` (API) / `8501` (WebUI) | 🟢 Running | AI Video Factory 9:16 vertikal, Edge-TTS Ardi, & subtitle kuning. |
| **Token-Efficiency Suite** | `~/.local/bin/` & MCP | ⚡ **Primary Workflow** | Standardisasi hemat token: `web2md` (Jina reader), `tokcut` (smart output truncator), `sqlite-utils`, & `mcp-server-sqlite`. |
| **Brain CLI & Memory Suite** | `brain` (`~/.local/bin/brain`) | ⚡ **Core Workflow** | CLI Helper terpusat: `brain status`, `brain health`, `brain task`, `brain session`, `brain review`, & `brain push`. |
| **PNPM Global Store** | `~/.local/share/pnpm/store/v11` | 🟢 Aktif | Standardisasi Node.js Package Manager: Shared disk space & hard-linked virtual store. |
| **AI Browser Suite** | `~/.ai-browser-tools` & MCP | 🟢 Terpasang | `@playwright/mcp` Server, `crawl4ai` Async Extractor, dan `browser-use` Agent. |
| **SIMPKK Keep-Alive** | `simpkk-keepalive.alwiihsan50.workers.dev` | 🟢 Live | Cloudflare Worker Cron 24/7 (09:00 WIB daily) menjaga Supabase SIMPKK-DIGITAL tetap aktif. |
| **9Router & Headroom** | `Port 20128` & `8787` | 🟢 Live | AI Routing Gateway + Headroom v0.37.0 Context Optimizer (Code-Aware AST Compression). |
| **Torrent PC Suite** | `Port 6801` / `/media/cuker/Data/Downloads` | 🟢 Standby | Sentralisasi unduhan torrent eksklusif PC (`pc-torrent` / Aria2 / Transmission). Dilarang di STB / mentari-server. |

---


## 🚀 Status Tugas Aktif (Work in Progress)

- [ ] **Pembuatan CLI tool pencari torrent film (cari-film & pc-torrent search) otomatis terintegrasi Aria2 RPC Port 6801 (Drive Data)**

- [x] **Implementasi 5 Pilar Peningkatan Workflow Agent Brain: Strict User Confirmation, Ready for Review Protocol, brain CLI Helper, Live Healthcheck, dan ACTIVE_SESSION.md.**
- [x] **Setup & integrasi Headroom (v0.37.0) context compression di 9Router (Port 8787 & 20128).**
- 📂 *Riwayat lengkap seluruh milestone terdahulu telah diarsipkan ke [docs/history/completed-milestones-archive.md](docs/history/completed-milestones-archive.md).*

---

## 📚 Indeks Dokumentasi (`docs/`)

- 📝 [**Active Session Scratchpad**](ACTIVE_SESSION.md) — Jembatan memori real-time antar agent saat pengerjaan tugas aktif.
- 📄 [**Tooling Efisiensi Token & MCP Server**](docs/token-efficiency-and-mcp-tooling.md) — Panduan `web2md`, `tokcut`, `sqlite-utils`, dan MCP SQLite.
- 📄 [**STB RockChip Web Remote Architecture**](docs/stb-rockchip-web-remote-architecture.md) — Arsitektur daemon uinput, 4-Tab Hub, HDMI resolution tuner, Tailscale IP, dan optimasi kernel.
- 📄 [**System Environment, Ports & Remote Access**](docs/system-environment-and-ports.md) — Port terpesan, Cloudflare Tunnel & Zero Trust.
- 📄 [**Panduan Sinergi agent-brain & graphify**](docs/agent-brain-and-graphify-synergy-guide.md) — Integrasi memori makro dan knowledge graph mikro.
- 📄 [**MoneyPrinterTurbo Hybrid Architecture**](docs/moneyprinterturbo-hybrid-architecture.md) — Setup pabrik video AI, port 8095/8501, local asset bank, & kinetic subtitle.
- 📄 [**TikTok Marketing Agent Suite**](docs/tiktok-marketing-agent-suite.md) — Panduan arsitektur ttagent, CLI `tt`, video 9:16, live selling, & CRM SQLite.
- 📄 [**Automasi Trading MT5 & Cloudflare Push**](docs/mt5-docker-forex-trading-automation.md) — Setup bot MT5 Docker, Wine Python, dynamic risk calculation.
- 📄 [**Infrastruktur mentari-server Debian**](docs/mentari-server-debian-infrastructure.md) — Spesifikasi, remote SSH key, dan manajemen container.
- 📄 [**Universal Web Push Notification Service**](docs/universal-web-push-notification-service.md) — Hub notifikasi REST API (Python, JS, Go, cURL).
- 📄 [**Arsip-IMO Specification**](docs/arsip-imo-project.md) — Dokumentasi arsitektur dan UI/UX proyek Arsip-IMO.
- 📄 [**Cloudflare Manager & DNS Mapping**](docs/cloudflare-manager-architecture-and-dns-mapping.md) — Manajemen 12 DNS subdomain dan akses Zero Trust.
- 📄 [**Safari iOS Web Push Notification**](docs/safari-ios-web-push-notification.md) — Panduan integrasi Web Push Safari iOS & PWA standalone.
- 📄 [**LPKP Mentari Ecosystem**](docs/lpkp-mentari-ecosystem.md) — Struktur ekosistem platform web LPKP Mentari.
- 📄 [**AI Browser Automation Tools**](docs/ai-browser-automation-tools.md) — Panduan Playwright MCP, Crawl4AI, dan Browser-Use.
- 📄 [**Git Post-Commit Graphify Hook**](docs/git-post-commit-graphify-hook.md) — Panduan auto-sync graphify via Git Hook.
- 📄 [**TailShare Linux Mint Guide**](docs/tailshare-linux-mint-installation.md) — Panduan instalasi dan auto-start TailShare.
- 📄 [**Standardisasi PNPM & Shared node_modules**](docs/pnpm-global-store-node-modules-optimization.md) — Konfigurasi global store, hard links, dan panduan dependensi Node.js.
- 📄 [**Kustomisasi Workflow Linux Mint**](docs/linux-mint-developer-workflow-customizations.md) — Starship, Zoxide, FZF, LazyDocker, Btop, aliases.
- 📄 [**Katalog Proyek Drive D**](docs/drive-d-projects-catalog.md) — Pemetaan 18 repositori Git aktif di Drive `D:\Projects`.
- 📄 [**Kebijakan Sentralisasi Torrent PC**](docs/torrent-download-centralization-policy.md) — Aturan mutlak seluruh task torrent hanya berjalan di PC workstation.
- 📄 [**SIMPKK-DIGITAL Supabase Keep-Alive**](docs/simpkk-digital-supabase-keepalive.md) — Solusi dual-layer keepalive Supabase Free Tier (GitHub Actions + local crontab).
- 📄 [**9Router AI Gateway**](docs/9router-ai-gateway.md) — Panduan integrasi AI proxy gateway & token saver (Port 20128).
- 📄 [**Arsip Milestone & Riwayat Lengkap**](docs/history/completed-milestones-archive.md) — Log lengkap seluruh fitur & milestone terdahulu.

---

**Last Updated By:** Antigravity (Gemini 3.8 Flash)
**Last Updated At:** 2026-09-12 19:00 WIB




