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
| **MT5 Dual Container** | `Port 3000` (Acc 1) / `Port 3006` (Acc 2) | 🟢 Acc 1 Live / ⚪ Acc 2 Off | Acc 1 Modular Dual-Bot aktif (Demo USD `463978832` / Cent `263301611` - `XAUUSDm/c`, Dual Strategy Trending SMC R:R 1:3 + Sideways Sweep R:R 1:2, Sizing Universal Flat Risk Rp 50.000 / ~$3.03 USD). Acc 2 dinonaktifkan sementara. |
| **Web Push Hub** | `mt5-push-backend.alwiihsan50.workers.dev` | 🟢 Live | Hub notifikasi push universal 24/7 (Cloudflare Workers + KV). |
| **Cloudflare Manager & DNS** | `abbas.my.id` / Zero Trust | 🟢 Full Access | Token API Full Access, 12 Subdomain DNS, PIN OTP `alwiihsan50@gmail.com` (Sesi 30 Hari). |
| **TailShare (original)** | `Port 40506` / `share.abbas.my.id` | 🟢 Running | Multi-network high speed transfer (Wi-Fi Direct `192.168.100.67`, LAN Gigabit `192.168.10.239`, Tailscale, & Cloudflare) + Live sync Drive D (`/media/cuker/Data/tailshare`). |
| **TailShare Clean** | `Port 40507` | 🟢 Running | Minimal file-transfer-only version, same storage `/media/cuker/Data/tailshare`, no clipboard/WS/QR/electron. |
| **AI Photo Eraser (PWA)** | `Port 3005` (Web) / `3003` (API) | 🟢 Running | Mobile-first AI Magic Object Remover with Virtual Mouse Trackpad & LaMa ONNX Inpainting. |
| **Arsip-IMO** | `/media/cuker/Data/Projects/Arsip-IMO` | 🟢 Synced | Production web absensi & schedule system + self-contained LaMa AI inpainting backend (Port 3003). |
| **Marketing Agents** | `/media/cuker/Data/marketing agent` | 🟢 Aktif | `fbagent/` (FB Marketplace, `mkt`) & `ttagent/` (TikTok Suite, `tt`). |
| **MoneyPrinterTurbo & Kling AI** | Port 8095 / 8501 / CLI | 🟢 Running | Pabrik video AI otomatis + AGY Bridge Port 5050 + CLI `kling-video` (Playwright Chromium 720p). |
| **Token-Efficiency Suite** | `~/.local/bin/` & MCP | ⚡ **Primary Workflow** | Standardisasi hemat token: `web2md` (Jina reader), `tokcut` (smart output truncator), `sqlite-utils`, & `mcp-server-sqlite`. |
| **Brain CLI & Memory Suite** | `brain` (`~/.local/bin/brain`) | ⚡ **Core Workflow** | CLI Helper terpusat: `brain status`, `brain health`, `brain task`, `brain session`, `brain review`, & `brain push`. |
| **PNPM Global Store** | `~/.local/share/pnpm/store/v11` | 🟢 Aktif | Standardisasi Node.js Package Manager: Shared disk space & hard-linked virtual store. |
| **AI Browser Suite** | `~/.ai-browser-tools` & MCP | 🟢 Terpasang | `@playwright/mcp` Server, `crawl4ai` Async Extractor, dan `browser-use` Agent. |
| **SIMPKK Keep-Alive** | `simpkk-keepalive.alwiihsan50.workers.dev` | 🟢 Live | Cloudflare Worker Cron 24/7 (09:00 WIB daily) menjaga Supabase SIMPKK-DIGITAL tetap aktif. |
| **9Router & Headroom** | `Port 20128` & `8787` | 🟢 Live | AI Routing Gateway + Headroom v0.37.0 Context Optimizer (Code-Aware AST Compression). |
| **AGY OpenAI Bridge** | `Port 5050` / `localhost:5050` | 🟢 Running | Local OpenAI-Compatible Bridge bertenaga `agy -p` (16 models: Gemini 3.8 Flash, Claude Sonnet 4.6, Opus, GPT-OSS) + integrasi 9Router prefix `agy/`. |
| **Torrent PC Suite** | `Port 6801` (RPC) & `6888` (Web UI) | 🟢 Live | Sentralisasi torrent eksklusif PC (`cari-film` / `pc-torrent` / Web App). Akses via Tailscale. |
| **MT5 MCP Server** | `mcp-mt5` / `mcp_config.json` | 🟢 Terpasang | Integrasi native MetaTrader 5 dengan Antigravity AI (`agy`): cek akun, posisi, analisa SMC M5, dan emergency close. |

---

## 🚀 Status Tugas Aktif (Work in Progress)

- [ ] **Deployment Live Strategi Doji + H1 EMA 50 + MACD Momentum (R:R 1:3.0) pada MT5 Akun Cent Exness (XAUUSDc) dengan Sizing Dinamis Flat Risk Rp 20.000 (~121 USC)**

- [ ] **Integrasi Filosofi Candle Doji (Indecision Equilibrium & Reversal Confirmation Engine) pada Sistem Dual-Bot Gold: Peningkatan Net Profit +198% (+$1,266.27 USD / ~Rp 20.89M vs +$424.62 USD), Lonjakan Profit Factor ke 1.26 (Trending PF 1.30), Pemotongan Max Drawdown -61% (-$100.22 USD vs -$254.84 USD), dan Konsistensi 8 dari 9 Bulan Profit**

- [ ] **Backtest Komprehensif Dual-Bot Modular Gold YTD 2026 (50.248 Bar M5): Validasi Portofolio Sinergis Trending SMC (Net +$347 USD, PF 1.07) + Sideways Sweep (Net +$77 USD, PF 1.09), Total Gabungan Net +$424.62 USD (~Rp +7.0M), Max DD -$254 USD, Laporan Interaktif HTML**

- [ ] **Adaptasi Universal Multi-Currency Bot MT5 (Option 1 Dual-Bot) ke Akun Demo USD Baru (Login: 463978832, Exness-MT5Trial17, Saldo $2,822.00 USD): Proyeksi 1:1 Backtest, Auto-Detect Akun, dan Sizing Dinamis Universal (~$3.03 / ~Rp 50.000)**

- [ ] **Implementasi Modular Dual-Bot MT5 Solo Gold (Option 1): Pemisahan Bot Trending (SMC M5 BOS + FVG/OB R:R 1:3, Magic 889911) dan Bot Sideways (Asian Range Sweep / Turtle Soup R:R 1:2, Magic 889922), Supervisor Proses, CLI Helper `bot-control`, dan Sizing Dinamis Flat Risk Rp 50.000**

- [ ] **Audit Backtest YTD 2026 & Upgrade Akun 1 MT5 Solo Gold ke v5.2-PURE-RR3: Evaluasi Kritis Bias Metodologi Backtest Lama (Overfitting & Lookahead), Eliminasi Two-Stage Guard, dan Deployment Mode Murni R:R 1:3 (Net +Rp 383K, PF 1.14)**

- [x] **Adaptasi Bot MT5 Pure SMC v5.1 ke Akun Cent Exness (XAUUSDc): Sizing Dinamis Flat Risk Rp 50.000 (~303 USC), Koreksi Suffix Simbol & Currency Display**

- [x] **Deployment Akun 1 MT5 Solo Gold (v5.1-RR3-TWO-STAGE-GUARD): Target R:R 1:3.0 dengan Two-Stage Smart Guard (Soft Cut -0.5R @ +1.0R -> Lock +0.3R @ +1.5R, Max SL Clamp Rp 100rb, Validasi Net +Rp 14.25M Win Rate 76.7%, PF 7.26, Max DD Rp 272rb)**

- [x] **Deployment Akun 1 MT5 Solo Gold (v4.8-CLAMP-100K-PURE-RR): Murni R:R 1:3, Rejection Filter, Max SL Clamp Rp 100rb ($5.68), Fixed 0.01 Lot, Validasi M1 Intra-Bar Net +Rp 18.2M**

- [x] **Deployment Akun 1 MT5 Solo Gold (v4.7-PROPER-SL-PURE-RR): Murni R:R 1:3 (No BEP), Rejection Candle Filter, Proper Structural SL (Maks $10.00), Fixed 0.01 Lot Murni, Validasi YTD 2026 Net +Rp 47.1M Win Rate 60.5%**

- [x] **Deployment Akun 1 MT5 Solo Gold (v4.6-PURE-RR-REJECTION): Murni R:R 1:3 (Bebas BEP), Rejection Candle Filter, Hard-Cap SL <= $2.85 (Risiko <= Rp 50.000), Validasi Realistis YTD 2026 Net +Rp 13.5M Win Rate 62.2%**

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
- 📄 [**AGY Local OpenAI Bridge**](docs/agy-local-openai-bridge.md) — Panduan arsitektur bridge Port 5050 bertenaga Antigravity CLI, integrasi 9Router, dan penggunaan aplikasi eksternal.
- 📄 [**Kling AI Browser Automation & MoneyPrinter Pipeline**](docs/kling-ai-browser-automation-and-moneyprinter-pipeline.md) — Otomasi Kling AI, Playwright Chromium, kuota 66 kredit harian, CLI `kling-video`, & TailShare.
- 📄 [**Arsip Milestone & Riwayat Lengkap**](docs/history/completed-milestones-archive.md) — Log lengkap seluruh fitur & milestone terdahulu.

---

**Last Updated By:** Antigravity (Gemini 3.8 Flash)
**Last Updated At:** 2026-09-18 10:20 WIB
