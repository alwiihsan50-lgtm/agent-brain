# 📚 INDEKS DOKUMENTASI TERPUSAT AGENT-BRAIN (`docs/`)

> 🏛️ **Tujuan Direktori:**
> Direktori ini menyimpan seluruh arsitektur kanonikal, spesifikasi teknis, protokol kuantitatif, dan panduan sistem lintas AI Agent di komputer ini.
> Gunakan indeks terstruktur per kategori di bawah ini untuk menavigasi dokumen tanpa membebani *context window* utama.

---

## 📑 Daftar Kategori Dokumentasi

- 📈 [1. Trading Kuantitatif & Algoritmik (MT5)](#-1-trading-kuantitatif--algoritmik-mt5)
- 🌐 [2. Infrastruktur, Server & Jaringan Remote](#-2-infrastruktur-server--jaringan-remote)
- ⚡ [3. AI Tooling, Context Efficiency & Developer Workflow](#-3-ai-tooling-context-efficiency--developer-workflow)
- 🏢 [4. Ekosistem Platform Web Lembaga & Database](#-4-ekosistem-platform-web-lembaga--database)
- 🎬 [5. Creative Media, AI Video & Marketing Automation](#-5-creative-media-ai-video--marketing-automation)
- 📜 [6. Riwayat Milestone & Arsip Tugas Selesai](#-6-riwayat-milestone--arsip-tugas-selesai)

---

### 📈 1. Trading Kuantitatif & Algoritmik (MT5)

| Dokumen | Deskripsi Inti & Fokus Arsitektur |
| :--- | :--- |
| [**Katalog Bot Berperforma Unggul (Hall of Fame)**](high-performance-trading-bots-catalog.md) | Etalase terpusat seluruh bot trading kuantitatif teruji (Cent Grid v3.2, Engulfing, D1 Doji, SMC) & Lemari Arsip Substandard. |
| [**Arsitektur Cent Grid Harvester (Anti-MC & Anti-Mati Lampu)**](optimal-xauusd-cent-grid-harvester-architecture.md) | Panduan kanonikal bot grid Akun 1 Cent v2.2/v3.2 (Mandatory Cut-Loss L4, Hard SL Broker, Closed-Bar Law). |
| [**Arsitektur Reverse Martingale Paroli 2-Way Trading**](reverse-martingale-paroli-2way-architecture.md) | Sistem Paroli 2 arah anti-martingale, kalibrasi spread asymmetry drag, dan atomic sync counterpart reset. |
| [**Arsitektur Triad Hedged Martingale Non-Stop**](triad-hedged-martingale-nonstop-architecture.md) | 3 solusi cerdas non-stop (Tail Pruning via Siphon Pool, Dynamic Decay Escape, Trend Booster, & Sizing Anti-Duplicate). |
| [**Kerangka Trading Makro-Kuantitatif Institusional**](institutional-macro-quant-trading-framework.md) | Alur kerja Top-Down Tri-Pillar (Makro/Fundamental + Sentimen Intermarket + Struktur SMC + R:R Asimetris 1:3). |
| [**Protokol Bot & Backtest Anti-Bias (12 Pilar)**](quantitative-bot-development-and-zero-bias-backtesting-protocol.md) | Standar wajib institusional eliminasi lookahead bias, intra-bar blindspot, spread drag, & validasi out-of-sample. |
| [**Automasi Trading MT5 & Cloudflare Push**](mt5-docker-forex-trading-automation.md) | Panduan lingkungan Docker MT5, Wine Python, dynamic risk calculation, dan push telemetry. |
| [**Dokumentasi Kalibrasi Strategi XAUUSD M5**](mt5-xauusd-backtesting-and-strategy-calibration.md) | Catatan kalibrasi historis sweep parameter XAUUSD M5. |

---

### 🌐 2. Infrastruktur, Server & Jaringan Remote

| Dokumen | Deskripsi Inti & Fokus Arsitektur |
| :--- | :--- |
| [**System Environment, Ports & Remote Access**](system-environment-and-ports.md) | Pemetaan port terpesan (40506, 3000, 8080), Cloudflare Tunnel, Zero Trust OTP, dan endpoint cloud. |
| [**STB RockChip Web Remote Architecture**](stb-rockchip-web-remote-architecture.md) | Arsitektur daemon uinput, 4-Tab Hub, tuner resolusi HDMI 1080p, dan optimasi kernel headless STB. |
| [**Infrastruktur mentari-server Debian**](mentari-server-debian-infrastructure.md) | Spesifikasi hardware/OS server Debian, otentikasi SSH public key, dan tata kelola container Docker. |
| [**Universal Web Push Notification Service**](universal-web-push-notification-service.md) | Hub notifikasi REST API 24/7 terpusat bertenaga Cloudflare Workers + KV Namespace. |
| [**Protokol Notifikasi Selesai Tugas AI**](agent-completion-notification-protocol.md) | Mandat dual-channel notification otomatis (`notify-send` desktop + Apple Push iPhone) setiap prompt selesai. |
| [**Safari iOS Web Push Notification Guide**](safari-ios-web-push-notification.md) | Panduan teknis Web Push Safari iOS, manifest PWA standalone, dan penanganan VAPID Apple Push. |
| [**Cloudflare Manager & DNS Mapping**](cloudflare-manager-architecture-and-dns-mapping.md) | Manajemen 12 DNS subdomain terpusat untuk domain `abbas.my.id` dan `lpkpmentari.id`. |
| [**TailShare Linux Mint Guide**](tailshare-linux-mint-installation.md) | Panduan instalasi, auto-start systemd, dan transfer gigabit LAN/Wi-Fi Direct TailShare Port 40506. |
| [**Kebijakan Sentralisasi Torrent PC Workstation**](torrent-download-centralization-policy.md) | Aturan mutlak larangan download torrent di STB/Server; sentralisasi eksklusif ke PC Workstation Port 6801/6888. |

---

### ⚡ 3. AI Tooling, Context Efficiency & Developer Workflow

| Dokumen | Deskripsi Inti & Fokus Arsitektur |
| :--- | :--- |
| [**Tooling Efisiensi Token & MCP Server**](token-efficiency-and-mcp-tooling.md) | Panduan praktis zero-token waste: `web2md` (Jina reader), `tokcut`, `sqlite-utils`, dan MCP SQLite. |
| [**Panduan Sinergi agent-brain & graphify**](agent-brain-and-graphify-synergy-guide.md) | SOP integrasi memori makro lintas platform (`agent-brain`) dan pemetaan AST mikro lokal (`graphify`). |
| [**AI Browser Automation Tools Guide**](ai-browser-automation-tools.md) | Integrasi `@playwright/mcp`, `crawl4ai` asynchronous extractor, dan `browser-use` autonomous agent. |
| [**Git Post-Commit Graphify Hook**](git-post-commit-graphify-hook.md) | Otomasi pembaruan AST graphify otomatis saat commit tanpa biaya token API. |
| [**Standardisasi PNPM & Shared node_modules**](pnpm-global-store-node-modules-optimization.md) | Optimalisasi virtual store global dan hard-links deduplikasi penyimpanan Node.js. |
| [**Kustomisasi Workflow Linux Mint**](linux-mint-developer-workflow-customizations.md) | Starship prompt, Zoxide smart jump, FZF fuzzy search, LazyDocker, Btop, dan alias terminal. |
| [**Katalog Proyek Drive D**](drive-d-projects-catalog.md) | Pemetaan struktur 18 repositori Git aktif di `D:\Projects`. |
| [**9Router AI Gateway**](9router-ai-gateway.md) | Integrasi gateway proxy Port 20128 dan kompresor AST Headroom Port 8787. |
| [**AGY Local OpenAI Bridge**](agy-local-openai-bridge.md) | Bridge API lokal Port 5050 bertenaga Antigravity CLI untuk aplikasi pihak ketiga. |

---

### 🏢 4. Ekosistem Platform Web Lembaga & Database

| Dokumen | Deskripsi Inti & Fokus Arsitektur |
| :--- | :--- |
| [**LPKP Mentari Ecosystem**](lpkp-mentari-ecosystem.md) | Struktur arsitektur portal `lpkpmentari.id`, sistem kursus online, dan integrasi Supabase DB. |
| [**Arsip-IMO 2025 Architecture Specification**](arsip-imo-project.md) | Dokumentasi web mandiri Cloudflare (Pages + D1 + KV) presensi IMO 2025 tanpa beban PC. |
| [**SOP Bulk Upload Foto Absensi TailShare**](sop-bulk-upload-foto-absensi-tailshare.md) | Prosedur otomasi ekstraksi ZIP foto TailShare, kompresi <=150KB, dan upload langsung database Supabase. |
| [**SIMPKK-DIGITAL Supabase Keep-Alive**](simpkk-digital-supabase-keepalive.md) | Solusi dual-layer keepalive Supabase Free Tier (GitHub Actions + local crontab) anti-pause. |

---

### 🎬 5. Creative Media, AI Video & Marketing Automation

| Dokumen | Deskripsi Inti & Fokus Arsitektur |
| :--- | :--- |
| [**MoneyPrinterTurbo Hybrid Architecture**](moneyprinterturbo-hybrid-architecture.md) | Pabrik video AI otomatis, port 8095/8501, local asset bank, dan kinetic subtitles. |
| [**TikTok Marketing Agent Suite**](tiktok-marketing-agent-suite.md) | Panduan arsitektur ttagent, CLI `tt`, format video 9:16 vertikal, dan CRM SQLite. |
| [**Kling AI Browser Automation & Video Pipeline**](kling-ai-browser-automation-and-moneyprinter-pipeline.md) | Otomasi Playwright browser untuk utilisasi kuota harian Kling AI dan integrasi pipeline video. |

---

### 📜 6. Riwayat Milestone & Arsip Tugas Selesai

* [**Arsip Milestone Terdahulu (Completed Milestones Archive)**](history/completed-milestones-archive.md) — Log historis lengkap 200+ pekerjaan selesai yang telah divalidasi oleh USER.
