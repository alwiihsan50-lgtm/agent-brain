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
| **MT5 Dual Container & Autonomous Sentinel** | `Port 3000` (Acc 1) / `Port 3006` (Acc 2) | 🟢 Acc 1 & 2 Live | **Acc 1 (Port 3000):** Cent `443003218` (`Exness-MT5Real44`, Saldo `27.926.772 IDC` / `Rp 279.268 IDR` / `~1.700 USC`): **M5 Dual-Pair Sniper v6.1 (Stationary Hybrid-ATR + M5 ZLEMA 50 Champion)**: `bot_trending.py` (Magic `889911`: `XAUUSDc` `0.01 Lot` `R:R 1:2.0` + `M5 ZLEMA 50` PF `1.38` WR `39.9%` + `USTECc` `0.20 Lot` `R:R 1:1.75` + `M5 ZLEMA/EMA` PF `1.42` WR `46.2%` -> **Combined PF `1.40` (IS `1.40`, OOS `1.40`), `24/26` Bulan Hijau (`92.3%`), Sharpe `3.91`, Sortino `11.40`, Max DD `11.0%`**). *(Seluruh bot tidak profitable pada rezim 2024–2026 termasuk `bot_daily_doji.py` PF `0.97` diarsipkan ke `archived_bots/`)*. **Acc 2 (Port 3006):** IDR `463880423`: **3 Bot Running Paralel** (`bot.py`, `bot_dual_track.py`, `bot_reverse_martingale_crypto.py`). Saldo bersih: Rp 74,10+ Juta IDR. |
| **Web Push Hub** | `mt5-push-backend.alwiihsan50.workers.dev` | 🟢 Live | Hub notifikasi push universal 24/7 (Cloudflare Workers + KV). |
| **Cloudflare Manager & DNS** | `abbas.my.id` & `lpkpmentari.id` | 🟢 Full Access | Manajemen DNS terpusat 2 zona aktif (`abbas.my.id` & `lpkpmentari.id` Vercel/Hostinger), Zero Trust OTP `alwiihsan50@gmail.com`. |
| **TailShare (original)** | `Port 40506` / `share.abbas.my.id` | 🟢 Running | Multi-network high speed transfer (Wi-Fi Direct `192.168.100.67`, LAN Gigabit `192.168.10.239`, Tailscale, & Cloudflare) + Live sync Drive D (`/media/cuker/Data/tailshare`). |
| **TailShare Clean** | `Port 40507` | 🟢 Running | Minimal file-transfer-only version, same storage `/media/cuker/Data/tailshare`, no clipboard/WS/QR/electron. |
| **Antigravity Direct Hub** | `Port 40508` / `reply.abbas.my.id` | 🟢 Live (Tunnel) | Direct HTTP Webhook & Quick Reply Server (0% Quota, Zero Polling Loop). |
| **Arsip IMO 2025** | `arsip.abbas.my.id` | 🟢 Live (Cloudflare) | Web mandiri arsip presensi IMO 2025 (Bulan 1-4) 100% Cloudflare (Pages + D1 + KV), 24/7 uptime tanpa PC. PC workstation hanya digunakan saat generate file Excel resmi. |
| **Marketing Agents** | `/media/cuker/Data/marketing agent` | 🟢 Aktif | `fbagent/` (FB Marketplace, `mkt`) & `ttagent/` (TikTok Suite, `tt`). |
| **MoneyPrinterTurbo & Kling AI** | Port 8095 / 8501 / CLI | 🟢 Running | Pabrik video AI otomatis + AGY Bridge Port 5050 + CLI `kling-video` (Playwright Chromium 720p). |
| **Token-Efficiency Suite** | `~/.local/bin/` & MCP | ⚡ **Primary Workflow** | Standardisasi hemat token: `web2md` (Jina reader), `tokcut` (smart output truncator), `sqlite-utils`, & `mcp-server-sqlite`. |
| **Brain CLI & Memory Suite** | `brain` (`~/.local/bin/brain`) | ⚡ **Core Workflow** | CLI Helper terpusat: `brain status`, `brain health`, `brain task`, `brain session`, `brain review`, & `brain push`. |
| **Agent Notification Suite** | `agent-notify` / Hook | 🔔 **Always-On** | Notifikasi otomatis setiap tugas/prompt selesai: Push Web Cloudflare ke iPhone + Linux Desktop `notify-send`. |
| **XAU Backtest Toolkit** | `xau-backtest` / `backtest-gold` | ⚡ **Lightning Engine** | Toolkit backtest XAUUSD M5 super cepat (<200ms) berbasis binary cache 50k bar YTD 2026. Mendukung comparative sweeps, monthly breakdown, Plotly chart HTML, & 1:1 live bot simulation. |
| **PNPM Global Store** | `~/.local/share/pnpm/store/v11` | 🟢 Aktif | Standardisasi Node.js Package Manager: Shared disk space & hard-linked virtual store. |
| **AI Browser Suite** | `~/.ai-browser-tools` & MCP | 🟢 Terpasang | `@playwright/mcp` Server, `crawl4ai` Async Extractor, dan `browser-use` Agent. |
| **SIMPKK Keep-Alive** | `simpkk-keepalive.alwiihsan50.workers.dev` | 🟢 Live | Cloudflare Worker Cron 24/7 (09:00 WIB daily) menjaga Supabase SIMPKK-DIGITAL tetap aktif. |
| **9Router & Headroom** | `Port 20128` & `8787` | 🟢 Live | AI Routing Gateway + Headroom v0.37.0 Context Optimizer (Code-Aware AST Compression). |
| **AGY OpenAI Bridge** | `Port 5050` / `localhost:5050` | 🟢 Running | Local OpenAI-Compatible Bridge bertenaga `agy -p` (16 models: Gemini 3.8 Flash, Claude Sonnet 4.6, Opus, GPT-OSS) + integrasi 9Router prefix `agy/`. |
| **Torrent PC Suite** | `Port 6801` (RPC) & `6888` (Web UI) | 🟢 Live | Sentralisasi torrent eksklusif PC (`cari-film` / `pc-torrent` / Web App). Akses via Tailscale. |
| **MT5 MCP Server** | `mcp-mt5` / `mcp_config.json` | 🟢 Terpasang | Integrasi native MetaTrader 5 dengan Antigravity AI (`agy`): cek akun, posisi, analisa SMC M5, dan emergency close. |
| **Vibe-Trading AI Workspace** | `Port 8899` / `localhost:8899` | 🟢 Live (Systemd) | Quantitative financial research & multi-agent trading workspace (HKUDS): 306 QuantLib math functions, 478 Alpha Zoo, 29 data loaders, React 19 UI, terintegrasi AGY Bridge Port 5050. |

---

## 🚀 Status Tugas Aktif (Work in Progress)

- [x] **Riset Sweep R:R `1:1.0` s/d `1:2.0` (12-Pilar Zero-Bias), Penghentian `bot_daily_doji.py` (`889933`, PF 2024–2026 `0.97`), & Upgrade Live `bot_trending.py` v6.1 Dual-Pair Optimized (`XAUUSDc` `0.01 Lot` `R:R 1:2.0` + `M5 ZLEMA 50` PF `1.38` + `USTECc` `0.20 Lot` `R:R 1:1.75` PF `1.42` -> Combined PF `1.40`, `24/26` Bulan Hijau `92.3%`, Sharpe `3.91`) di Akun 1 (`443003218`)**
- [x] **Audit Forensik 12-Pilar Zero-Bias Seluruh Kandidat Bot MT5, Pencatatan Bot Unprofitable (`bot_grid_cent.py` PF 1.06, `bot_pullback_sniper.py` PF 0.86-0.90) vs Profitable, & Deployment Dual Sniper Mode Moderat (`bot_trending.py` Magic `889911` + `bot_daily_doji.py` Magic `889933`) di Akun 1 (`443003218`)**
- 📂 *Seluruh milestone dan riwayat tugas terdahulu telah diselesaikan dan diarsipkan ke [docs/history/completed-milestones-archive.md](docs/history/completed-milestones-archive.md).*

---

## 📚 Indeks Dokumentasi (`docs/`)

- 📝 [**Active Session Scratchpad**](ACTIVE_SESSION.md) — Jembatan memori real-time antar agent saat pengerjaan tugas aktif.
- 📑 [**Indeks Master Dokumentasi Terpusat (`docs/README.md`)**](docs/README.md) — Katalog terstruktur seluruh 34 dokumen sistem lintas kategori:
  - 📈 [**Trading Kuantitatif & Algoritmik MT5**](docs/README.md#-1-trading-kuantitatif--algoritmik-mt5) (8 Dokumen: Katalog Audit Bot Profitable vs Unprofitable, Paroli 2-Way, Triad, 12 Pilar Anti-Bias)
  - 🌐 [**Infrastruktur, Server & Jaringan Remote**](docs/README.md#-2-infrastruktur-server--jaringan-remote) (9 Dokumen: Ports, STB Remote, Web Push, Zero Trust, TailShare, Torrent)
  - ⚡ [**AI Tooling, Context Efficiency & Workflow**](docs/README.md#-3-ai-tooling-context-efficiency--developer-workflow) (9 Dokumen: `web2md`, `tokcut`, Graphify Hook, 9Router, Headroom, AGY Bridge)
  - 🏢 [**Ekosistem Platform Web Lembaga & Database**](docs/README.md#-4-ekosistem-platform-web-lembaga--database) (4 Dokumen: LPKP Mentari, Arsip-IMO, Supabase Keepalive)
  - 🎬 [**Creative Media, AI Video & Marketing**](docs/README.md#-5-creative-media-ai-video--marketing-automation) (3 Dokumen: MoneyPrinterTurbo, TikTok Suite, Kling AI Automation)
- 📜 [**Arsip Milestone Terdahulu**](docs/history/completed-milestones-archive.md) — Log lengkap 200+ riwayat pekerjaan selesai terverifikasi.

---

**Last Updated By:** Antigravity (Gemini 3.8 Flash)
**Last Updated At:** 2026-10-18 10:09 WIB


