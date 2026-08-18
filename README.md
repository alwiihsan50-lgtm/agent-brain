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
| **TailShare** | `Port 40506` / `share.abbas.my.id` | 🟢 Running | Live sync folder Drive D (`/media/cuker/Data/tailshare`) & GUI Native Electron. |
| **MT5 Docker Exness** | `Port 3000` / `mt5.abbas.my.id` | 🟢 Running | Wine Python MetaTrader 5 di `mentari-server` (`/home/mentari/mt5_storage`). |
| **MT5 Web Dashboard** | `Port 8080` / `dashboard.abbas.my.id` | 🟢 Running | Zero-flicker live monitoring & PWA Standalone Safari iOS (`mentari-server`). |
| **Web Push Hub** | `mt5-push-backend.alwiihsan50.workers.dev` | 🟢 Live | Hub notifikasi push universal 24/7 (Cloudflare Workers + KV). |
| **Infisical Secret Vault** | `app.infisical.com` / `infisical` CLI | 🟢 Synced | 10 kredensial infrastruktur E2EE tersimpan di `dev` & `prod` (Cloudflare Full Access, Turso, Vercel, dll.). |
| **Trading Risk Engine** | `mt5_config/bot.py` | 🟢 Aktif | ATR Volatility Grid Multi-pair scanner dengan Dynamic Spacing & Circuit Breaker. |
| **RustDesk Direct Access** | `Port 21112` / `100.110.205.27` | 🟢 Ready | Direct IP & Tailscale remote access (`100.110.205.27:21112` / LAN `192.168.100.61`). |
| **Arsip-IMO** | `/media/cuker/Data/Projects/Arsip-IMO` | 🟢 Synced | Single branch `main` stabil terverifikasi. |

- **Dual-Engine Protocol:** `agent-brain` (Global Strategy) + `graphify` (Local AST Code Intelligence).
- **Global Excludes:** `graphify-out/` dan `.graphify_*` di-ignore secara global via `~/.gitignore_global`.
- **Last Updated By:** Antigravity AI Agent (Google DeepMind)
- **Last Updated At:** 2026-08-19 03:35 WIB

---

## 🚀 Progress & Task Aktif

- [x] **Fitur Fullscreen Mouse Mode, Pinch-to-Zoom & Floating Keyboard:**
  - Menambahkan tombol **⛶ Layar Penuh** yang memaksimalkan tampilan TV ke 100% layar HP.
  - **Mouse Mode Terintegrasi**:
    1. **Klik Kiri**: Ketuk 1 jari untuk klik kiri seketika dengan riak animasi biru.
    2. **Klik Kanan / Long-Press**: Tahan layar (0.5s) untuk membuka menu konteks Android / klik kanan dengan riak animasi amber + haptic vibration.
    3. **Pinch-to-Zoom & Pan**: Cubit 2 jari untuk zoom in hingga 4x dan geser (pan) area yang diperbesar.
    4. **Floating Keyboard HUD**: Tombol keyboard melayang di mode fullscreen untuk mengetik langsung ke TV, tombol hapus, dan tombol navigasi instan.
- [x] **Fitur Toggle Switch Auto-Refresh 0.5s (2 FPS Eco-Mode):**
  - Menambahkan switch toggle `⚡ Auto 0.5s` di Tab **Cuplikan Layar TV** Web Remote.
  - Memakai resolusi ringan (640x360) dan non-blocking recursive loop yang otomatis me-refresh snapshot setiap 500ms saat tab aktif.
  - Dilengkapi *Smart Auto-Pause*: otomatis berhenti total (CPU 0%) saat berpindah ke tab Remote/Aplikasi atau saat layar HP terkunci/background.
- [x] **Penerapan Penuh Opsi 1 (Smart Snapshot on Action) & Opsi 3 (App Launcher Hub):**
  - Melepas streaming kontinu Opsi 2 untuk menjaga STB 100% bebas beban dan hemat kuota HP.
  - Mengoptimalkan Tab **📸 Cuplikan Layar TV (Smart Snapshot)**: Pengambilan foto layar beresolusi tinggi hanya saat diminta atau saat layar diklik dengan overlay loading halus dan 0% CPU idle.
  - Mengoptimalkan Tab **🎮 Remote**: Navigasi D-Pad, Volume, Back, Home, Power, Keyboard Teks dengan latensi instan (<2ms).
  - Mengoptimalkan Tab **⭐ Aplikasi**: Grid aplikasi favorit (SmartTube, TV Bro, Settings, Tailscale, dll.) dan pencarian aplikasi dengan peluncuran 1-klik.
- [x] **Pembersihan RustDesk & Optimasi Penuh Web Remote:**
  - Menghapus total **RustDesk** (`com.carriez.flutter_hbb`) dan seluruh residu konfigurasinya dari STB sesuai permintaan user.
  - Suhu STB tetap dingin (**~46°C**) dan RAM bebas **~1.0 GB**.
- [x] **Fitur Tombol Bersihkan RAM & Tutup Semua Aplikasi (Web Remote):**
  - Menambahkan endpoint `POST /api/system/clean-ram` di backend daemon STB (`stb_server`).
  - Menjalankan `am kill-all`, mematikan proses background non-esensial dengan tetap mempertahankan layanan kritis (RustDesk, Tailscale, TV Launcher, system server), dan membersihkan filesystem drop_caches (`echo 3 > /proc/sys/vm/drop_caches`).
  - Menambahkan tombol **🧹 Bersihkan RAM** di Top Header Bar dan di baris tombol navigasi utama (Trio: Kembali, Bersihkan, Menu) lengkap dengan haptic feedback & floating toast notification.
- [x] **Perbaikan Error Pemutaran Video SmartTube (Resolusi DNS & GPU Renderer):**
  - Menguji status Google Services: SmartTube **tidak memerlukan Google Play Services**, namun layanan GMS telah diaktifkan kembali untuk pengujian penuh.
  - Menemukan akar penyebab error pemutaran video:
    1. Konflik `Private DNS` dengan VPN Tailscale -> Diperbaiki dengan `private_dns_mode: off`.
    2. Properti `debug.hwui.renderer skiagl` tidak kompatibel dengan GPU Mali-450 -> Dikembalikan ke renderer native `opengl`.
  - SmartTube berjalan lancar dan video teruji diputar normal.
- [x] **Instalasi & Koneksi RustDesk + Tailscale di STB (Remote Desktop 60 FPS Native):**
  - Memasang **RustDesk v1.4.9 ARM64** (`com.carriez.flutter_hbb`) dan **Tailscale v1.102.2** (`com.tailscale.ipn`).
  - STB terhubung penuh ke jaringan Tailscale dengan IP: **`100.104.214.122`** (node name: `erza`).
  - RustDesk ID: **`1811189838`**, Direct Access Port: **`21118`**, Kata Sandi Permanen: **`Cuker1234`**.
  - Opsi: `verification-method = 'use-permanent-password'` dan Direct IP Access aktif.
  - Ping latency langsung via Tailscale: **4.4 ms**, Sisa RAM Bebas STB: **> 1.02 GB**, Suhu: **46°C**.
- [x] **Remote Desktop Visual & Tailscale Proxy STB (Zero-Overhead di STB):**
  - Mengimplementasikan endpoint `/api/screen/frame`, `/api/screen/stream` (MJPEG ~3 FPS), `/api/screen/tap`, dan `/api/screen/swipe` di [`Desktop/stb-remote`](file:///home/cuker/Desktop/stb-remote).
  - Menambahkan Tab **Layar TV** di Web Remote dengan viewport interaktif (klik langsung di layar untuk navigasi, swipe untuk scroll) dan quick control bar.
  - Memasang service proxy background di PC Linux ini (`stb_proxy_x86_64` di port `8085` via `stb-remote-proxy.service`) dan meng-advertise Tailscale Subnet Router `192.168.100.0/24`.
  - Akses remote visual dari luar rumah via Tailscale: `http://100.110.205.27:8085`.
- [x] **Pembuatan Shortcut Pengaturan Lengkap (Full Android Settings):**
  - Mengintegrasikan package **SettingsShortcut** (`com.basti564.settingsshortcut`) agar menu Pengaturan Lengkap AOSP Android 13 (`com.android.settings/.Settings`) dapat diakses langsung dari beranda TV dan App Drawer.
  - Memperbarui susunan slot shortcut beranda pada `HCY Launcher` (`spUtils.xml`) dan tombol Pengaturan pada Web Remote UI ([`Desktop/stb-remote`](file:///home/cuker/Desktop/stb-remote)).
- [x] **Tuning Kernel & Jaringan Tingkat Lanjut STB (Low-Latency 4K Streaming):**
  - Menonaktifkan mode hemat daya Wi-Fi (`power_save off`) untuk menghilangkan latency spike & micro-buffering saat streaming video bit-rate tinggi.
  - Optimalisasi GPU Rendering Pipeline via `SkiaGL` dan SurfaceFlinger `latch_unsignaled=1` untuk animasi UI bebas stutter.
  - Penataan parameter kernel Linux `vm.swappiness: 60`, `vfs_cache_pressure: 50`, dan persistensi autostart di `/data/local/tmp/stb_autostart.sh`.
- [x] **De-Google Total STB (Nonaktifkan GMS & GSF):**
  - Menonaktifkan penuh `com.google.android.gms` (Google Play Services) dan `com.google.android.gsf` (Google Services Framework).
  - Verifikasi mandiri: SmartTube, TV Bro, Aurora Store, dan UI TV berjalan 100% lancar dengan 0 crash & 0 beban background Google.
- [x] **Instalasi TV Bro (Browser Android TV Bebas Iklan) & Penggantian Chrome:**
  - Pemasangan versi terbaru **TV Bro v2.1.6** (`com.phlox.tvwebbrowser`) yang dioptimasi khusus remote TV, built-in AdBlocker, dan video player native.
  - Pencopotan Google Chrome (`com.android.chrome`) untuk menghemat ~150 MB penyimpanan dan RAM background.
  - Pembaruan Web Remote UI ([`Desktop/stb-remote`](file:///home/cuker/Desktop/stb-remote)): Shortcut browser otomatis mengarah ke **TV Bro**.
- [x] **Deep Debloat & Minimalist Setup STB RockChip V8_Max (Android 13):**
  - Pembersihan menyeluruh 23 paket streaming yang tidak digunakan, telemetri Google, dan layanan non-TV (Amazon Prime, Netflix, Vidio, Spotify, TikTok, WeTV, iQIYI, Viki, HBO GO, Hotstar, Viu, Perfect Player, YouTube Official, Katniss Assistant, Android System Intelligence, Google TTS, Restore, Cell Broadcast, Calculator, Sound Picker, Shortcut Maker).
  - Pembersihan cache sisa: Storage internal `/data` bertambah lega **3.6 GB** (Free storage dari 3.2 GB menjadi **6.8 GB**).
  - Lonjakan performa memori: Free RAM meningkat drastis menjadi **~830 MB** (*Used RAM terpangkas dari 1.9 GB menjadi 1.1 GB*).
  - Refresh Web Remote UI ([`Desktop/stb-remote`](file:///home/cuker/Desktop/stb-remote)): Tab Aplikasi Favorit disederhanakan khusus untuk **SmartTube, TV Bro, Aurora Store, Pengaturan TV, Miracast, dan Media Center**.
- [x] **Perbaikan Peluncur Aplikasi STB Web Remote (RockChip Android 13):**
  - Identifikasi akar masalah: Perintah `monkey` gagal mengeksekusi launcher pada daemon background Android 13 tanpa TTY dan gagal membedakan intent `LEANBACK_LAUNCHER` vs `LAUNCHER` (contohnya Spotify).
  - Implementasi Native Component Launcher di [`main.go`](file:///home/cuker/Desktop/stb-remote/main.go) menggunakan `cmd package resolve-activity` dan `cmd activity start -n <component>` dengan multi-fallback intent.
  - Penambahan parameter `data-act` pada aplikasi favorit di [`public/index.html`](file:///home/cuker/Desktop/stb-remote/public/index.html) dan pembaruan fungsi `launchApp()` di [`public/app.js`](file:///home/cuker/Desktop/stb-remote/public/app.js).
  - Build binary ARM64 (`stb_server_arm64`) dan deployment langsung ke STB (`/vendor/bin/stb_server` & `/data/local/tmp/stb_server`). Verifikasi live berhasil 100%.
- [x] **Migrasi Data Keuangan SaveBuddy -> Catat Uang Bersama:**
  - Ekstraksi 120 transaksi dari `DompetPapaMamaAbbasTsaqiy` (Turso `savebuddy`).
  - Pembuatan file backup arsip di SaveBuddy (`backup_*.json`, `backup_*.csv`, `backup_*.sql`).
  - Impor dan sinkronisasi 120 transaksi lengkap dengan 18 kategori ke database `catat-uang-bersama` pada **Buku Keuangan Mama** (`https://catat-uang-bersama.vercel.app`).
- [x] **Cloudflare Manager Role & Full API Access Onboarding:**
  - Audit hak akses API Cloudflare di seluruh modul (DNS, Zone, Tunnels, Access, Workers, KV, WAF, SSL).
  - Pembaruan token API Full Access tanpa batasan IP ke Infisical Secret Vault (`dev` & `prod`).
  - Pemetaan 12 DNS records aktif domain `abbas.my.id` dan dokumentasi arsitektur di `docs/cloudflare-manager-architecture-and-dns-mapping.md`.
- [x] **TailShare Port Migration & Storage Mount Fix:**
  - Migrasi port default TailShare dari `53317` ke `40506` (Server, Client UI, QR Code, dan Cloudflare Tunnel `share.abbas.my.id`).
  - Pemulihan & perbaikan mount NTFS Drive D (`/dev/sda1` -> `/media/cuker/Data`) dari kondisi *read-only* (lock Windows Fast Startup) menjadi *read-write* (`ntfs-3g rw`).
  - Persistensi entri mount di `/etc/fstab` dan pembuatan symlink `/media/cuker/Data1 -> /media/cuker/Data`.
- [x] Onboarding & konfigurasi infrastruktur **mentari-server** (Debian 13 Trixie, Tailscale SSH, Docker v29.7.2, Passwordless Sudo, persistent auto-start).
- [x] Setup **Cloudflare Tunnel (`mentari-tunnel`)** 24/7 untuk CasaOS Web GUI di **`https://server.abbas.my.id`** dan **`https://casa.abbas.my.id`** (Auto-SSL HTTPS, systemd persistent).
- [x] **Migrasi Penuh MT5 Trading Bot & Dashboard ke `mentari-server`:**
  - Build image Docker `mt5:latest` (Wine32 + Wine64 + Openbox KasmVNC) di `mentari-server`.
  - Transfer direktori Wine, MT5, Python 3.9, bot logic, dan realtime dashboard ke `/home/mentari/mt5_storage`.
  - Konfigurasi systemd unit 24/7 `mt5-trading-bot.service` (auto-restart saat booting server).
  - Setup Cloudflare Tunnel routing untuk `https://dashboard.abbas.my.id` (Port 8080) dan `https://vnc.abbas.my.id` (Port 3000) dengan proteksi Zero Trust PIN OTP.
- [x] **Konfigurasi Wake-on-LAN (WoL) `mentari-server`:**
  - Identifikasi MAC LAN `00:e0:4c:bf:02:e1` (Realtek RTL8111 `enp2s0`) pada subnet LAN `192.168.101.243`.
  - Instalasi `ethtool` & pembuatan systemd unit persisten `wol-enable.service` di Debian 13 (`wol g` MagicPacket).
  - Instalasi `wakeonlan` & penambahan fungsi shortcut `wake-mentari` serta `wake-mentari-check` di Linux Mint workstation.
- [x] Optimasi arsitektur **Dual-Engine (`agent-brain` + `graphify`)**:
  - Penambahan klausul **Immutability & Integrity Guardrail** (kebal dari perubahan otomatis oleh model AI yang berganti-ganti).
  - Penambahan aturan **Auto-Init Fallback** (`graphify .` otomatis jika graf belum ada).
  - Setup **Global Git Ignore** (`~/.gitignore_global`) untuk isolasi artefak `graphify-out/`.
  - Pembuatan script dan panduan **Git Post-Commit Hook** auto-sync di `docs/git-post-commit-graphify-hook.md`.
  - **Memory Token-Budgeting:** Arsip milestone lampau dipindahkan ke `docs/history/completed-milestones-archive.md`.
  - Penambahan developer shortcuts di `~/.bash_aliases` (`gf`, `gfu`, `gfq`, `gf-viz`, `brain-sync`, `brain-push`, `wake-mentari`).
- [ ] *(Siap untuk task / konfigurasi baru dari pengguna)*

---

## 📚 Indeks Dokumentasi (`docs/`)

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
