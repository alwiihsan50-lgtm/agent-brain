# Agent Brain - Central Context & Workspace

Repositori ini adalah sistem memori terpusat (*Shared Memory System*) dan tempat penyimpanan dokumentasi bersama untuk seluruh AI Agent lintas platform.

---

## 📌 Status Proyek & Lingkungan Saat Ini
- **Project Scope:** Multi-project Context & Shared Memory (`Arsip-IMO`, `SmartHome`, `SaveBuddy`, `SIMPKK-DIGITAL`, `Mentari Ecosystem`, `TailShare`, `Web Push Safari iOS`, `MT5 Docker Bot`, `Cloudflare Zero Trust`, `Infisical`, `agent-brain`)
- **Status:** Active / Production Ready
- **Last Updated By:** Antigravity AI Agent (Google DeepMind)
- **Last Updated At:** 2026-08-15 13:00 WIB

---

## 🚀 Progress & Checklist Pekerjaan

- [x] Inisialisasi repositori `agent-brain` dan SOP `AGENTS.md`
- [x] Migrasi seluruh memori & konteks proyek `Arsip-IMO` dari sesi terdahulu ke `docs/arsip-imo-project.md`
- [x] Pendokumentasian batasan lingkungan sistem & reserved port di `docs/system-environment-and-ports.md`
- [x] Pemetaan seluruh repositori dan proyek di Drive `D:\` ke `docs/drive-d-projects-catalog.md`
- [x] Tambahkan panduan instalasi & auto-start TailShare untuk **Linux Mint** di `docs/tailshare-linux-mint-installation.md`
- [x] Implementasi dan deployment penuh aplikasi **TailShare** versi lintas platform (**Windows & Linux**) dengan auto-start background 24/7, installer 1-klik Windows, live auto-sync folder **Drive D: `D:\tailshare`**, preview streaming langsung di web tanpa perlu download manual, dan perbaikan Electron Linux Native GUI.
- [x] Sinkronisasi & pembaruan versi lokal TailShare di Windows dengan versi GitHub (`alwiihsan50-lgtm/tailshare`, Port 53317, auto-start startup Windows, shortcut Desktop, dan optimasi background process)
- [x] Implementasi, pengujian live, dan pendokumentasian arsitektur **Web Push Notification untuk Safari iOS (iPhone)** tanpa bot Telegram/WhatsApp (PWA Standalone, Service Worker, VAPID Keys, Express backend dengan library `web-push`, dan Cloudflare Pages) di `docs/safari-ios-web-push-notification.md`.
- [x] Implementasi dan deployment live **Automasi Trading MetaTrader 5 (Docker + Exness + Wine Python)** yang terhubung langsung ke **Serverless Cloudflare Workers Web Push Notification** (`https://mt5-push-backend.alwiihsan50.workers.dev`) dengan Cloudflare KV dan Web Crypto API di `docs/mt5-docker-forex-trading-automation.md`.
- [x] Implementasi dan aktivasi strategi trading otomatis **Multi-Pair Scanner (6 Pairs: EURUSDm, GBPUSDm, USDJPYm, AUDUSDm, USDCADm, XAUUSDm)** dengan **EMA Crossover (9/21) + RSI (14)**, proteksi SL/TP per pair, dan Push Notification real-time ke iPhone di `mt5_config/bot.py`.
- [x] Pembuatan dan containerisasi **MT5 Live Trading Web Dashboard (Docker container `mt5-dashboard` di Port `8080`)** untuk monitoring real-time balance, equity, floating P/L, scanner pair, open trades, dan log aktivitas via browser.
- [x] Optimasi **Zero-Flicker in-place DOM sync**, antarmuka **Mobile-Friendly iOS Segmented Tab**, integrasi **Riwayat Transaksi Selesai (Closed Deals History & Win Rate Metrik)**, serta dukungan **PWA Standalone Safari iOS (iPhone)** dengan Service Worker, safe-area insets, dan web manifest di `mt5-dashboard`.
- [x] Standardisasi protokol **Dual-Engine Synergy (`agent-brain` + `graphify`)** untuk seluruh AI Agent di `.agents/rules/agent-brain-and-graphify-synergy.md` dan `docs/agent-brain-and-graphify-synergy-guide.md`.
- [x] Implementasi **Dynamic Flexible Pips Risk Engine berdasarkan Nilai Rupiah (Max Loss SL: Rp 25.000 / Target Win TP: Rp 50.000, 1:2 RRR)** yang secara dinamis menghitung jarak pip sesuai karakteristik setiap pair dan ukuran volume lot.
- [x] Setup & Tuning Lingkungan **Linux Mint Developer Workflow Suite** (Starship prompt, Zoxide smart jumping, FZF fuzzy search, LazyDocker TUI, Btop system monitor, Bat, Eza, smart aliases di `~/.bash_aliases`, Desktop guide, dan symlinks Drive D) di `docs/linux-mint-developer-workflow-customizations.md`.
- [x] Pembersihan seluruh branch lama di remote GitHub `alwiihsan50-lgtm/Arsip-IMO` (`feat/mobile-first-ui`, `beta`, `agent/fix-repo-audit-findings`), penghapusan repositori lokal lama, dan kloning fresh tunggal `main` stabil ke `D:\Projects\Arsip-IMO` (`/media/cuker/Data/Projects/Arsip-IMO`) lengkap dengan verifikasi build & dependency.
- [x] Implementasi dan aktivasi penuh **Cloudflare Tunnel (`cloudflared.service` 24/7)** pada domain **`abbas.my.id`** untuk akses remote publik tak terbatas tanpa batas port (`https://dashboard.abbas.my.id`, `https://share.abbas.my.id`, `https://vnc.abbas.my.id`) lengkap dengan SSL resmi di `docs/system-environment-and-ports.md`.
- [x] Implementasi dan aktivasi penuh **Cloudflare Zero Trust Access Application & Policy** untuk domain `*.abbas.my.id` dengan proteksi One-Time PIN email eksklusif untuk `alwiihsan50@gmail.com` dan masa aktif sesi persisten **30 Hari (730 Jam / 1x login per bulan)**.
- [x] Instalasi dan konfigurasi **Infisical CLI (`infisical` v0.38.0)** di Linux Mint sebagai pusat Secret Management & Vault terenkripsi lintas perangkat (Mobile & Desktop).

---

## 📝 Ringkasan Konteks Terakhir
1. **Dual-Engine AI Synergy:** Sistem menggabungkan `agent-brain` sebagai memori strategis jangka panjang lintas proyek (Single Source of Truth) dan `graphify` sebagai knowledge graph AST kode lokal per-repositori.
2. **Cloudflare Zero Trust & Tunnel (Production Grade Security):**
   - Seluruh subdomain di `*.abbas.my.id` (`dashboard.abbas.my.id`, `share.abbas.my.id`, `vnc.abbas.my.id`) telah diproteksi penuh oleh **Cloudflare Zero Trust Access**.
   - Otentikasi eksklusif hanya untuk email pemilik (`alwiihsan50@gmail.com`) via kode PIN 6-digit.
   - **Sesi Persisten 30 Hari (730 jam):** Pengguna hanya perlu login 1 kali di browser HP/PC, dan selama 30 hari ke depan semua aplikasi langsung terbuka otomatis tanpa meminta login lagi.
   - Tailscale Funnel publik telah ditutup permanen untuk menghilangkan backdoor, sementara Tailscale VPN privat tetap aktif untuk koneksi direct IP.
3. **Pusat Secret Management Terpusat (Infisical):**
   - Tool `infisical` CLI v0.38.0 telah terpasang di Linux Mint (`/usr/bin/infisical`).
   - Digunakan untuk mengelola token & kredensial terenkripsi E2EE yang dapat diakses via web, mobile iPhone, dan CLI injection.
4. **Multi-Pair Algorithmic Trading Bot & Web Dashboard (Docker):** Berjalan aktif melalui Docker (`exness-mt5` di Port `3000` dan `mt5-dashboard` di Port `8080`) dan systemd service (`mt5-trading-bot.service`). Storage virtual ext4 berada di `/media/cuker/Data/mt5-storage.img` yang melegakan ruang SSD sistem.
5. **Universal Web Push Notification Hub (Cloudflare Workers 24/7):** Dibangun sebagai hub notifikasi terpusat (`https://mt5-push-backend.alwiihsan50.workers.dev`) menggunakan Cloudflare KV (`SUBSCRIPTIONS`) dan `@block65/webcrypto-web-push`. Siap dipanggil oleh aplikasi mana pun cukup via 1 panggilan HTTP POST (`/trigger-notification`).
6. **Linux Mint Developer Workflow Customization:** Sistem terminal dan shell Linux Mint 22.3 telah dioptimasi dengan Starship prompt, Zoxide smart directory jumping, FZF fuzzy finder history (`Ctrl+R`) & file (`Ctrl+T`), LazyDocker (`ld`), Btop system monitor (`top`), Bat syntax highlighter, Eza modern tree/icons, smart aliases harian (Docker, systemd bot, port checking), symlinks Drive D (`~/Data`, `~/Projects`), dan file instruksi di Desktop.
7. **Web Push Notification Safari iOS (iPhone & Local Server):** Menggunakan Web Push API standar, Service Worker (`sw.js`), `manifest.json` PWA Standalone, VAPID Keys, dan backend Node.js (`web-push`). Repo lokal: `safari-push-test`, Cloudflare Pages: `https://safari-push-test.pages.dev`.
8. **TailShare Universal Suite (Windows & Linux Native GUI):** Terkoneksi langsung ke folder **Drive D `D:\tailshare`** (`/media/cuker/Data/tailshare`). Mendukung GUI Native Electron (`bin/tailshare` dengan CommonJS preload & X11 sandbox flags), auto-attach ke daemon background systemd tanpa konflik port `53317`, live folder watcher, dan web UI. Repo: `https://github.com/alwiihsan50-lgtm/tailshare`.
9. **Pembaruan TailShare di Windows:** Repositori GitHub `alwiihsan50-lgtm/tailshare` telah dikloning dan diinstal di `C:\Users\alwii\Desktop\tailshare`. Port default telah dialihkan ke **53317**, script auto-start Startup Windows terpasang, file sharing terintegrasi ke `D:\tailshare`, dan shortcut Desktop diperbarui.
10. **Konsolidasi Repositori Arsip-IMO (Fresh Clone Single Main):**
   - Branch selain `main` di GitHub (`feat/mobile-first-ui`, `beta`, `agent/fix-repo-audit-findings`) telah dihapus secara permanen.
   - Branch `main` di GitHub tetap utuh dan stabil di commit **`9c63a0e`**.
   - Folder repositori lama di `D:\Documents\GitHub\Arsip-IMO` dan salinan lama telah dibersihkan.
   - Fresh clone tunggal telah ditempatkan di `D:\Projects\Arsip-IMO` (`/media/cuker/Data/Projects/Arsip-IMO`), `npm install` dan `npm run build` berhasil 100% tanpa error.
11. **Katalog Proyek Drive D (`D:\Projects`):** Terdiri dari 18 repositori Git aktif termasuk ekosistem IMO, SmartHome, SaveBuddy, SIMPKK Digital, PRD Generator, dan Ekosistem LPKP Mentari.
12. **Lingkungan & Reserved Ports:** Port **`53317`** (TailShare), Port **`3000`** (MT5 Web VNC GUI), Port **`8080`** (MT5 Web Dashboard). Port `3005` telah dilepas.

---

## 📚 Indeks Dokumentasi (`docs/`)
- 📄 [Panduan Kustomisasi Workflow & Aliases Linux Mint](docs/linux-mint-developer-workflow-customizations.md) - Panduan alat produktivitas, aliases, shortcuts, dan konfigurasi terminal Linux Mint.
- 📄 [Panduan Sinergi agent-brain & graphify](docs/agent-brain-and-graphify-synergy-guide.md) - Protokol kolaborasi memori makro lintas proyek dan knowledge graph kode mikro.
- 📄 [Panduan Universal Web Push Notification Service](docs/universal-web-push-notification-service.md) - Dokumentasi hub notifikasi terpusat, endpoint REST API, dan template kode integrasi untuk aplikasi lain (Python, JS, PHP, Go, cURL).
- 📄 [Panduan Automasi Trading MT5 & Cloudflare Workers Push](docs/mt5-docker-forex-trading-automation.md) - Arsitektur Docker MT5, Wine Python MetaTrader5, Cloudflare Workers push backend, Cloudflare KV, dan integrasi bot.
- 📄 [Panduan Web Push Notification Safari iOS](docs/safari-ios-web-push-notification.md) - Arsitektur, syarat Apple Safari iOS PWA, spesifikasi Service Worker, VAPID keys, dan backend Node.js.
- 📄 [Panduan Instalasi TailShare di Linux Mint](docs/tailshare-linux-mint-installation.md) - Langkah-langkah instalasi Node.js, Tailscale, setup systemd auto-start, dan shortcut desktop di Linux Mint.
- 📄 [Katalog Proyek Drive D](docs/drive-d-projects-catalog.md) - Pemetaan lengkap 18 repositori Git, remote URL, branch aktif, dan direktori di Drive `D:\`.
- 📄 [Arsip-IMO Project Specification & Memory](docs/arsip-imo-project.md) - Dokumentasi lengkap proyek Arsip-IMO, batasan, arsitektur, navigasi, dan workflow delivery.
- 📄 [System Environment, Ports & Remote Access](docs/system-environment-and-ports.md) - Informasi spesifikasi sistem Windows/Linux, aturan port terpesan, serta mapping Cloudflare Tunnel & Zero Trust.
