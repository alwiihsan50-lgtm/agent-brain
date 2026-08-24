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
| **Marketing Agents** | `/media/cuker/Data/marketing agent` | 🟢 Aktif | `fbagent/` (FB Suite, `mkt`) & `ttagent/` (TikTok Suite, `tt`). |
| **TikTok Web Dashboard** | `Port 8090` / `192.168.101.2:8090` | 🟢 Running | Mobile-First Web Studio: Script generator, AI Voiceover, 9:16 Video render, CRM. |
| **Timemark Lab Studio** | `Port 3005` (Web) / `3003` (API) | 🟢 Running | SOTA AI Inpainting (LaMa ONNX 198 MB), dynamic anchor, and pixel-perfect Roboto font. |
| **Arsip-IMO** | `/media/cuker/Data/Projects/Arsip-IMO` | 🟢 Synced | Single branch `main` stabil terverifikasi. |

- **Dual-Engine Protocol:** `agent-brain` (Global Strategy) + `graphify` (Local AST Code Intelligence).
- **Global Excludes:** `graphify-out/` dan `.graphify_*` di-ignore secara global via `~/.gitignore_global`.
- **Last Updated By:** Antigravity AI Agent (Google DeepMind)
- **Last Updated At:** 2026-08-24 16:45 WIB

---

## 🚀 Progress & Task Aktif

- [x] **Unbrick Sukses 100% STB RockChip RK3528 (V8_Max Android 13):** Berhasil memulihkan STB yang bootloop/rusak partisi recovery ke kondisi normal pabrik menggunakan metode RockChip MaskROM hardware trigger (Short Pad AV ke Ground pada saat USB dicolokkan). Menulis ulang seluruh partisi asli (`recovery.img` 96MB & `boot.img` 50MB) via `rkdeveloptool` dan `fast_flash_maskrom.py`. STB berhasil booting normal ke tampilan utama Android TV. Dokumentasi lengkap di `docs/stb-rockchip-web-remote-architecture.md`.
- [x] **Isolasi Microservice AI & Hosting Murni Vercel:** Menghapus fungsi serverless proxy Vercel dan membatasi fitur rahasia edit tanggal AI otomatis hanya pada *local development* (`localhost`). Web online di Vercel kini menjadi static SPA murni yang 100% independen tanpa ketergantungan pada PC lokal.
- [x] **Auto-Generate Jadwal Dinas Bulanan Otomatis (Pre-Populated Schedule):** Menambahkan sistem auto-provisioning baris jadwal bulanan di `src/features/absensi/absensiService.js` (`ensureMonthlyAbsensiRows`). Setiap bulan aktif yang dibuka langsung membuat baris jadwal dinas untuk seluruh karyawan secara instan via bulk upsert `ignoreDuplicates: true` (aman tanpa menimpa data yang sudah ada), sehingga alur database menjadi sangat sederhana (pure `UPDATE`).
- [x] **Upload Foto Serah Terima Mandiri (Tanpa Wajib Absensi):** Mengizinkan user mengunggah foto serah terima pada tanggal lampau dan hari ini secara mandiri meski belum mengisi data/foto absensi utama (menggunakan database upsert otomatis). Hanya tanggal di masa depan yang terkunci (`abu-abu`). Serta memastikan absensi utama tetap akurat dan tidak terpengaruh jika hanya foto serah terima yang diunggah.
- [x] **Fleksibilitas Upload Foto Kerja Arsip-IMO (1 atau 2 Foto):** Mengizinkan user mengunggah foto kerja secara bertahap (minimal 1 foto tersimpan dulu, foto kedua bisa disusulkan kemudian) dengan manajemen slot mandiri (Tersimpan/Ganti/Hapus/Batal), smart delta upload tanpa re-upload foto lama, pembersihan otomatis storage tak terpakai, dan indikator visual status kalender (`(1 FOTO)` vs `Lengkap ✅`).
- [x] **Desktop Launcher Timemark AI Backend:** Membuat pintasan desktop interaktif [`Timemark-AI-Backend.desktop`](file:///home/cuker/Desktop/Timemark-AI-Backend.desktop) dan runner script [`timemark-backend-launcher.sh`](file:///home/cuker/.local/bin/timemark-backend-launcher.sh) di Linux Mint. Menyediakan live terminal logs, auto-detect IP Tailscale, notifikasi desktop `notify-send`, auto-restart port 3003 jika ada konflik PID, serta auto-start Web Arsip-IMO (Port 3004) dalam sekali klik.
- [x] **Integrasi AI Inpainting LaMa SOTA ke Web Arsip-IMO:** Berhasil menghubungkan alur kerja upload foto absensi di [`Arsip-IMO`](file:///media/cuker/Data/Projects/Arsip-IMO) langsung ke backend microservice **FastAPI LaMa ONNX (Port 3003)**. Modul `src/lib/timemarkAdjuster.js` di-upgrade menggunakan deteksi anchor dinamis garis kuning, tipografi Roboto Bold asli, fallback 2D Laplacian inpainting, dan update EXIF timestamp digital sebelum upload ke Supabase Storage.
- [x] **Release Stable: Integrasi SOTA LaMa ONNX Neural Inpainting di Timemark Photo Adjustment:** Model AI deep inpainting **LaMa (Fast Fourier Convolutions, 198 MB)** resmi dijadikan rilis stabil di backend FastAPI (`backend/app.py`) dan frontend Vite React Studio (`port 3005`). Menyediakan penghapusan tanggal 100% fotorealistis dan seamless, deteksi kolom anchor dinamis, multi-engine switcher, dan lolos seluruh unit test backend.
- [x] **Integrasi Shortcut Klik Kanan TailShare di Nemo File Manager (Linux Mint):** Memasang aksi menu konteks Nemo (`tailshare-send.nemo_action`, `tailshare-open-web.nemo_action`, `tailshare-open-folder.nemo_action`), helper CLI `tailshare-send` untuk pengiriman instan multi-file/folder via REST API (Port 40506) / storage sync Drive D (`/media/cuker/Data/tailshare`), ikon sistem hicolor TailShare, dan desktop notification `notify-send`.
- [x] **Setup Partisi VM_Storage (127 GB ext4) & KVM/Virt-Manager Virtualization Hub:** Berhasil membuat partisi baru `/dev/sda2` (127.5 GB ext4, label `VM_Storage`) di `/media/cuker/VM_Storage` dengan fstab automount, mengonfigurasi KVM, QEMU, Virt-Manager, OVMF UEFI, virtual network default, dan storage pool (`vm-images` & `vm-iso`) dengan data partisi NTFS (`sda1`) 100% aman dan utuh.
- [x] **Setup Workspace & Suite Marketing Agent TikTok (ttagent):** Membangun workplace lengkap di `/media/cuker/Data/marketing agent/ttagent`, engine olah video/foto 9:16 vertikal (1080x1920, EXIF/metadata stripper, cover high-CTR headline), generator naskah video 15s/30s/60s dengan bank 100+ viral hooks psikologis, generator rundown TikTok Live Selling 60 menit, riset tagar SEO, CRM leads & affiliate creator tracker SQLite, SOP algoritma FYP, dan perintah global CLI `tt`.
- [x] **Setup Workspace & Suite Marketing Agent Facebook Marketplace:** Membangun workplace lengkap di `/media/cuker/Data/marketing agent`, virtual environment Python dengan dependencies (`pillow`, `rich`, `typer`, `jinja2`, `pandas`, `openpyxl`, `playwright`), tool optimizer foto 1:1 square + clean EXIF + trust badge, generator listing SEO spintax, CRM leads & renewals SQLite, script closing chat, dan perintah global CLI `mkt`.
- [x] **Notifikasi Otomatis Boot & Idle PC ke Smartphone:** Membuat skrip daemon `boot-ready-notify.py` dan systemd service `boot-ready-notify.service` yang otomatis mendeteksi koneksi internet dan stabilisasi idle sistem saat PC baru menyala, lalu mengirim ringkasan status boot (durasi, CPU load, RAM, IP LAN/Tailscale, status Docker MT5) via Cloudflare Web Push Hub ke iPhone.
- [x] **Optimasi Memori & Prefetching Linux Mint (16 GB RAM):** Memasang daemon `preload` untuk adaptive application prefetching, mengaktifkan `tmpfs` pada `/tmp` (~7.7 GB RAM) via `tmp.mount`, serta mengonfigurasi sysctl kernel `vm.swappiness=10` dan `vm.vfs_cache_pressure=50` di `/etc/sysctl.d/99-performance-tuning.conf`.
- [x] **Standardisasi PNPM & Optimasi Shared node_modules Global Store:** Memasang PNPM v11 global dan memigrasi seluruh repositori lokal (`tailshare`, `SIMPKK-DIGITAL`, `push-backend`, `cf-push-backend`, `mt5_storage/cf-push-backend`, `bot_push_server/backend`) ke Global Content-Addressable Store (`~/.local/share/pnpm/store/v11`) guna menghemat ratusan megabyte/gigabyte ruang penyimpanan. Dokumentasi lengkap di `docs/pnpm-global-store-node-modules-optimization.md`.
- [x] **Standarisasi Repositori LPKP Mentari (Web 1 & Web 2):** Mengonfigurasi `AGENTS.md`, Git Hook Auto-Sync Graphify (`post-commit`/`post-checkout`), AST Knowledge Graph (`graphify-out/`), runtime Linux `esbuild` global di Linux Mint, dan menyusun dokumentasi arsitektur di `docs/lpkp-mentari-ecosystem.md`.
- [x] **Pemasangan AI Browser Automation Suite Selesai:** Menginstal dan mengonfigurasi `@playwright/mcp` (MCP Server Antigravity), `crawl4ai` (AI Web Scraping & Clean Markdown Engine), dan `browser-use` (Autonomous Web Navigation Agent) di virtualenv terisolasi `/home/cuker/.ai-browser-tools`.
- [x] **Protokol Konfirmasi Task Belum Selesai (Pending Task Confirmation):** Menambahkan aturan wajib bagi seluruh AI Agent untuk meminta konfirmasi ke USER di awal sesi jika menemukan task belum selesai (`- [ ]`) di `README.md` (apakah ingin dilanjutkan atau diarsip).
- [x] **Arsitektur In-Memory RAM MT5, AI Browser & Media Engine:**
  - MT5 & Web Dashboard: Shared volume `tmpfs` (`ram_buffer` 64 MB) lintas container Docker untuk Zero Disk I/O status 6s.
  - AI Browser Suite: Mengarahkan `TMPDIR` & `PLAYWRIGHT_TMPDIR` ke `/tmp/playwright-ram` (`tmpfs` RAM) untuk zero-wear fast scraping.
  - Media Engine (`ttagent`/`fbagent`): Staging frame extraction & video transcode di `/tmp/media-staging/` serta SQLite In-Memory PRAGMA tuning (WAL, MEMORY temp_store, 64 MB RAM cache, 256 MB MMAP).
- [x] **Monetisasi Otomatis: Multi-Account MT5 Scaling & TikTok Affiliate Factory:**
  - Multi-Account MT5: Dukungan agregasi portofolio multi-akun di RAM (`/api/accounts`), template container Prop Firm di `docker-compose.yml`, dan dynamic status routing.
  - Content Factory CLI (`tt factory`): Generator batch video 9:16 otomatis (Script Hook Psikologis, Edge-TTS AI Voiceover, In-Memory FFmpeg render, SQLite auto-tracking, dan Apple Web Push).
- [x] **Setup & Kustomisasi MoneyPrinterTurbo "Naik Kelas":** Memasang MoneyPrinterTurbo di `/media/cuker/Data/Projects/MoneyPrinterTurbo` dengan virtual environment Linux `/home/cuker/.virtualenvs/moneyprinterturbo`, mengonfigurasi Port aman `8095` (REST API) & `8501` (WebUI), default rasio 9:16 vertikal, font viral `impact.ttf`, subtitle kuning kontras (`#FFFF00`), Edge-TTS `id-ID-ArdiNeural` (1.08x rate), serta integrasi folder aset lokal `storage/local_videos`. Dokumentasi lengkap di `docs/moneyprinterturbo-hybrid-architecture.md`.
- [x] **Pembersihan Disk & Kernel Purge (+16 GB Reclaimed) & Advanced System Tuning.**

---

## 📚 Indeks Dokumentasi (`docs/`)

- 📄 [**MoneyPrinterTurbo Hybrid Architecture**](docs/moneyprinterturbo-hybrid-architecture.md) — Setup pabrik video AI, port 8095/8501, local asset bank, & kinetic subtitle.
- 📄 [**TikTok Marketing Agent Suite**](docs/tiktok-marketing-agent-suite.md) — Panduan arsitektur ttagent, CLI `tt`, video 9:16, live selling, & CRM SQLite.
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
