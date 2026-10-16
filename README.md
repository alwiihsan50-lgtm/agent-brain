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
| **MT5 Dual Container & Autonomous Sentinel** | `Port 3000` (Acc 1) / `Port 3006` (Acc 2) | 🟢 Acc 1 & 2 Live | **Acc 1 (Port 3000):** Cent `263301611`: **M5 Pullback Sniper v1.0 Live** (`bot_pullback_sniper.py`, Magic `881100`, XAUUSDc, Sesi 06:00-23:00 WIB). Setup Momentum M5 Range $\ge \$3.50$ (Toleransi Ekor Close 8.0%) + Order Limit Diskon 33.3% (Expiry 3 Bar / 15 Mnt) + Split-Ticket Twin Orders (Hard TP1 70% di halfway + Hard TP2 30% di puncak + True Structural SL pangkal lilin). Sizing: **Pure Geometric Compounding 2.0% Risk of Balance Per Trade (Max 3 Posisi, Capped by Broker Max 200L)** + **Filter Berita Dinamis ForexFactory Red Folder USD**. **Saldo: 2.676,54 USC**. **Acc 2 (Port 3006):** IDR `463880423`: **3 Bot Running Paralel**: 1) **M5 Dual-Engine Reversal Marubozu & Pullback Sniper v2.0** (`bot.py`, Magic `889911`, Engine 1 Market Order Marubozu 1.2x TP + EMA 50, Engine 2 Pullback 50% Limit, XAUUSDm). 2) **Dual-Track Harvester v1.0** (`bot_dual_track.py`, Magic `992200` & `992201`, 19x wins). 3) **Reverse Martingale Paroli 2-Way Crypto v1.2** (`bot_reverse_martingale_crypto.py`, Magic `667788`, BTCUSDm, Tangga [0.01, 0.02, 0.03], Target $25 USD, Spread-Compensated TP, Atomic Sync Close). Saldo bersih: Rp 74,10+ Juta IDR. |
| **Web Push Hub** | `mt5-push-backend.alwiihsan50.workers.dev` | 🟢 Live | Hub notifikasi push universal 24/7 (Cloudflare Workers + KV). |
| **Cloudflare Manager & DNS** | `abbas.my.id` & `lpkpmentari.id` | 🟢 Full Access | Manajemen DNS terpusat 2 zona aktif (`abbas.my.id` & `lpkpmentari.id` Vercel/Hostinger), Zero Trust OTP `alwiihsan50@gmail.com`. |
| **TailShare (original)** | `Port 40506` / `share.abbas.my.id` | 🟢 Running | Multi-network high speed transfer (Wi-Fi Direct `192.168.100.67`, LAN Gigabit `192.168.10.239`, Tailscale, & Cloudflare) + Live sync Drive D (`/media/cuker/Data/tailshare`). |
| **TailShare Clean** | `Port 40507` | 🟢 Running | Minimal file-transfer-only version, same storage `/media/cuker/Data/tailshare`, no clipboard/WS/QR/electron. |
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

---

## 🚀 Status Tugas Aktif (Work in Progress)

- [ ] **Implementasi Tombol /new, Pemilih Ganti Sesi Terfokus (Hanya Chat Terakhir), & Optimasi Kuota Cloudflare Workers (<25% Free Tier) pada Quick Reply Antigravity**

- [x] **Pembaruan Label Kurikulum 'Materi Kompetensi 1 - Materi Kompetensi 5' & Pemisahan Tab Vokasi di LPKPMentariWebsite (Live di lpkpmentari.id)**
- [x] **Penautan Kartu Akreditasi BAN-PDM & Identitas VIN Kemnaker ke Portal Resmi di Profil Lembaga (Live di lpkpmentari.id)**
- 📂 *Seluruh milestone dan riwayat tugas terdahulu telah diselesaikan dan diarsipkan ke [docs/history/completed-milestones-archive.md](docs/history/completed-milestones-archive.md).*

---

## 📚 Indeks Dokumentasi (`docs/`)

- 📝 [**Active Session Scratchpad**](ACTIVE_SESSION.md) — Jembatan memori real-time antar agent saat pengerjaan tugas aktif.
- 📑 [**Indeks Master Dokumentasi Terpusat (`docs/README.md`)**](docs/README.md) — Katalog terstruktur seluruh 34 dokumen sistem lintas kategori:
  - 📈 [**Trading Kuantitatif & Algoritmik MT5**](docs/README.md#-1-trading-kuantitatif--algoritmik-mt5) (8 Dokumen: Cent Grid v3.2, Paroli 2-Way, Triad, 12 Pilar Anti-Bias, Hall of Fame)
  - 🌐 [**Infrastruktur, Server & Jaringan Remote**](docs/README.md#-2-infrastruktur-server--jaringan-remote) (9 Dokumen: Ports, STB Remote, Web Push, Zero Trust, TailShare, Torrent)
  - ⚡ [**AI Tooling, Context Efficiency & Workflow**](docs/README.md#-3-ai-tooling-context-efficiency--developer-workflow) (9 Dokumen: `web2md`, `tokcut`, Graphify Hook, 9Router, Headroom, AGY Bridge)
  - 🏢 [**Ekosistem Platform Web Lembaga & Database**](docs/README.md#-4-ekosistem-platform-web-lembaga--database) (4 Dokumen: LPKP Mentari, Arsip-IMO, Supabase Keepalive)
  - 🎬 [**Creative Media, AI Video & Marketing**](docs/README.md#-5-creative-media-ai-video--marketing-automation) (3 Dokumen: MoneyPrinterTurbo, TikTok Suite, Kling AI Automation)
- 📜 [**Arsip Milestone Terdahulu**](docs/history/completed-milestones-archive.md) — Log lengkap 200+ riwayat pekerjaan selesai terverifikasi.

---

**Last Updated By:** Antigravity (Gemini 3.8 Flash)
**Last Updated At:** 2026-10-17 04:46 WIB


