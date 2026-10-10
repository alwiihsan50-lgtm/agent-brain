# Agent Brain - Central Context & Workspace

Repositori ini adalah sistem memori terpusat (*Shared Memory System*) dan tempat penyimpanan dokumentasi bersama untuk seluruh AI Agent lintas platform.

> 🔒 **ATURAN KEKEBALAN PROTOKOL (IMMUTABILITY CONSTRAINT):**
> Seluruh aturan arsitektur, batasan port (`40506`, `3000`, `8080`), dan sinergi `agent-brain` + `graphify` bersifat **PERMANEN**.
> Model AI Agent apa pun (Gemini, Claude, GPT, DeepSeek, Antigravity, dll.) **DILARANG KERAS** mengubah atau merusak protokol ini kecuali diminta secara spesifik oleh USER.
> ⚠️ **ATURAN MUTLAK PENYELESAIAN TUGAS & AUTO-ARCHIVAL:** Pekerjaan baru maupun lama yang belum selesai **DILARANG KERAS** dianggap selesai atau dicentang (`[x]`) sebelum mendapatkan konfirmasi langsung dan validasi dari USER. Tugas yang telah divalidasi selesai (`[x]`) secara otomatis diarsipkan ke `docs/history/completed-milestones-archive.md` dengan HANYA menyisakan 2 catatan pekerjaan terakhir yang telah selesai di `README.md`.

---

## 📌 Status Sistem & Lingkungan Aktif

| Layanan / Komponen | Port / Endpoint | Status | Deskripsi |
| :--- | :--- | :--- | :--- |
| **STB Web Remote Hub** | `Port 8080` / `100.122.66.85:8080` | 🟢 Live | Streamlined 3-Tab Hub: Remote, Apps (Official YouTube TV, TV Bro, Tailscale), Settings, Ad & Adult Filter 167k+ domains, HDMI 1080p. |
| **MT5 Dual Container & Autonomous Sentinel** | `Port 3000` (Acc 1) / `Port 3006` (Acc 2) | 🟢 Acc 1 & 2 Live | **Acc 1 (Port 3000):** Cent `263301611`: **v2.7 Dual-Track Hedged Harvester Live** (`bot.py`, Magic `778899` [Scalper] & `778898` [Runner], XAUUSDc). Track A: Grid Step $3.50 x 1.5, Hard TP $1.80, Direct Force-Prune $\ge$L5. Track B: Unshakable Trend Runner 0.02L (No-BEP Backup Mode) saat lawan $\ge$L3, Hard SL $4.00, Anti-Cannibalization Safeguard. Session Filter 07:00-19:00 WIB (**Soft Sleep Aktif**). **Saldo: 2.711,74 USC, Equity 100% Utuh (0 active pos)**. **Acc 2 (Port 3006):** IDR `463880423`: **3 Bot Running Paralel**: 1) **M5 Dual-Engine Reversal Marubozu & Pullback Sniper v2.0** (`bot.py`, Magic `889911`, Engine 1 Market Order Marubozu 1.2x TP + EMA 50, Engine 2 Pullback 50% Limit, XAUUSDm). 2) **Dual-Track Harvester v1.0** (`bot_dual_track.py`, Magic `992200` & `992201`, 19x wins). 3) **Reverse Martingale Paroli 2-Way Crypto v1.2** (`bot_reverse_martingale_crypto.py`, Magic `667788`, BTCUSDm, Tangga [0.01, 0.02, 0.03], Target $25 USD, Spread-Compensated TP, Atomic Sync Close). Saldo bersih: Rp 74,10+ Juta IDR. |
| **Web Push Hub** | `mt5-push-backend.alwiihsan50.workers.dev` | 🟢 Live | Hub notifikasi push universal 24/7 (Cloudflare Workers + KV). |
| **Cloudflare Manager & DNS** | `abbas.my.id` & `lpkpmentari.id` | 🟢 Full Access | Manajemen DNS terpusat 2 zona aktif (`abbas.my.id` & `lpkpmentari.id` Vercel/Hostinger), Zero Trust OTP `alwiihsan50@gmail.com`. |
| **TailShare (original)** | `Port 40506` / `share.abbas.my.id` | 🟢 Running | Multi-network high speed transfer (Wi-Fi Direct `192.168.100.67`, LAN Gigabit `192.168.10.239`, Tailscale, & Cloudflare) + Live sync Drive D (`/media/cuker/Data/tailshare`). |
| **TailShare Clean** | `Port 40507` | 🟢 Running | Minimal file-transfer-only version, same storage `/media/cuker/Data/tailshare`, no clipboard/WS/QR/electron. |
| **Arsip IMO 2025** | `arsip.abbas.my.id` | 🟢 Live (Cloudflare) | Web mandiri arsip presensi IMO 2025 (Bulan 1-4) 100% Cloudflare (Pages + D1 + KV), 24/7 uptime tanpa PC. PC workstation hanya digunakan saat generate file Excel resmi. |
| **Marketing Agents** | `/media/cuker/Data/marketing agent` | 🟢 Aktif | `fbagent/` (FB Marketplace, `mkt`) & `ttagent/` (TikTok Suite, `tt`). |
| **MoneyPrinterTurbo & Kling AI** | Port 8095 / 8501 / CLI | 🟢 Running | Pabrik video AI otomatis + AGY Bridge Port 5050 + CLI `kling-video` (Playwright Chromium 720p). |
| **Token-Efficiency Suite** | `~/.local/bin/` & MCP | ⚡ **Primary Workflow** | Standardisasi hemat token: `web2md` (Jina reader), `tokcut` (smart output truncator), `sqlite-utils`, & `mcp-server-sqlite`. |
| **Brain CLI & Memory Suite** | `brain` (`~/.local/bin/brain`) | ⚡ **Core Workflow** | CLI Helper terpusat: `brain status`, `brain health`, `brain task`, `brain session`, `brain review`, & `brain push`. |
| **XAU Backtest Toolkit** | `xau-backtest` / `backtest-gold` | ⚡ **Lightning Engine** | Toolkit backtest XAUUSD M5 super cepat (<200ms) berbasis binary cache 50k bar YTD 2026. Mendukung comparative sweeps, monthly breakdown, Plotly chart HTML, & 1:1 live bot simulation. |
| **PNPM Global Store** | `~/.local/share/pnpm/store/v11` | 🟢 Aktif | Standardisasi Node.js Package Manager: Shared disk space & hard-linked virtual store. |
| **AI Browser Suite** | `~/.ai-browser-tools` & MCP | 🟢 Terpasang | `@playwright/mcp` Server, `crawl4ai` Async Extractor, dan `browser-use` Agent. |
| **SIMPKK Keep-Alive** | `simpkk-keepalive.alwiihsan50.workers.dev` | 🟢 Live | Cloudflare Worker Cron 24/7 (09:00 WIB daily) menjaga Supabase SIMPKK-DIGITAL tetap aktif. |
| **9Router & Headroom** | `Port 20128` & `8787` | 🟢 Live | AI Routing Gateway + Headroom v0.37.0 Context Optimizer (Code-Aware AST Compression). |
| **AGY OpenAI Bridge** | `Port 5050` / `localhost:5050` | 🟢 Running | Local OpenAI-Compatible Bridge bertenaga `agy -p` (16 models: Gemini 3.8 Flash, Claude Sonnet 4.6, Opus, GPT-OSS) + integrasi 9Router prefix `agy/`. |
| **Torrent PC Suite** | `Port 6801` (RPC) & `6888` (Web UI) | 🟢 Live | Sentralisasi torrent eksklusif PC (`cari-film` / `pc-torrent` / Web App). Akses via Tailscale. |
| **MT5 MCP Server** | `mcp-mt5` / `mcp_config.json` | 🟢 Terpasang | Integrasi native MetaTrader 5 dengan Antigravity AI (`agy`): cek akun, posisi, analisa SMC M5, dan emergency close. |

---

## 🚀 Status Tugas Aktif (Work in Progress)

- [ ] **Implementasi M5 Dual-Engine Reversal Marubozu & Pullback Sniper v2.0 (Market Order Marubozu 1.2x TP + EMA 50, Magic 889911) di MT5 Akun 2 Demo** ⚠️ [MENUNGGU KONFIRMASI USER]

- [ ] **Pengujian Bot Reverse Martingale Paroli 2-Way Crypto (Opsi 1: BTCUSDm, Magic 667788, v1.2 Fast-Paroli $25 USD) di MT5 Akun 2 Demo**

- [ ] **Pengujian Dual-Track Harvester v1.0 (Scalper + Trend Runner, Magic 992200 & 992201) di MT5 Akun 2 Demo**

- [ ] **Implementasi Dual-Track Harvester v2.7 di Bot MT5 Akun 1 Real Cent (Step $3.50, TP $1.80, Unshakable Backup Runner No-BEP + Direct Force-Pruning L5)**

- [x] **Implementasi Halaman & Menu Pelatihan Vokasi (11 Kejuruan), Pembaruan Teks Profil, & Tautan Resmi NPSN Kemendikdasmen di LPKPMentariWebsite (Live di lpkpmentari.id)**

- [x] **Penambahan 4 Paket Kursus Online Baru (Photoshop & CorelDraw, Web Desain Dasar, Web Desain Terampil, Komputer Akuntansi) di MentariOnlineCourse**

- 📂 *Seluruh milestone dan riwayat tugas terdahulu telah diselesaikan dan diarsipkan ke [docs/history/completed-milestones-archive.md](docs/history/completed-milestones-archive.md).*

---

## 📚 Indeks Dokumentasi (`docs/`)

- 📝 [**Active Session Scratchpad**](ACTIVE_SESSION.md) — Jembatan memori real-time antar agent saat pengerjaan tugas aktif.
- 🏛️ [**Arsitektur Reverse Martingale Paroli 2-Way Trading**](docs/reverse-martingale-paroli-2way-architecture.md) — Panduan kanonikal sistem Paroli 2 arah anti-martingale, kalibrasi eliminasi spread asymmetry drag, dan atomic sync counterpart reset.
- 🏛️ [**Arsitektur Triad Hedged Martingale Non-Stop**](docs/triad-hedged-martingale-nonstop-architecture.md) — Panduan kanonikal 3 solusi cerdas non-stop (Tail Pruning via Siphon Pool, Dynamic Decay Escape, Trend Booster, & Sizing Anti-Duplicate).
- 🏆 [**Katalog Bot Trading Berperforma Unggul (Hall of Fame)**](docs/high-performance-trading-bots-catalog.md) — Etalase terpusat seluruh bot trading kuantitatif teruji (Cent Grid v3.2, Hybrid Grid Engulfing, M5 Trend Sniper, D1 Multi-Pair Doji, Forex SMC).
- 🏛️ [**Kerangka Trading Makro-Kuantitatif Institusional**](docs/institutional-macro-quant-trading-framework.md) — Alur kerja Top-Down Tri-Pillar (Makro/Fundamental + Sentimen Intermarket + Struktur SMC + Eksekusi Asimetris R:R 1:3).
- 📄 [**Arsitektur Cent Grid Harvester (Anti-MC & Anti-Mati Lampu)**](docs/optimal-xauusd-cent-grid-harvester-architecture.md) — Panduan kanonikal resmi bot grid Akun 1 Cent v2.2 (Sizing, Mandatory Cut-Loss L4, Hard SL Broker, Pure Candle Flow).
- 📄 [**Protokol Bot & Backtest Anti-Bias**](docs/quantitative-bot-development-and-zero-bias-backtesting-protocol.md) — Standar wajib 7 pilar kuantitatif eliminasi lookahead bias, spread drag, & validasi out-of-sample.
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
- 📄 [**SOP Bulk Upload Foto Absensi TailShare**](docs/sop-bulk-upload-foto-absensi-tailshare.md) — Prosedur otomasi ekstraksi ZIP foto TailShare, kompresi <=150KB, dan upload langsung database Supabase Arsip-IMO.
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
**Last Updated At:** 2026-10-10 17:52 WIB


