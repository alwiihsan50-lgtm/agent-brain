# Agent Brain - Central Context & Workspace

Repositori ini adalah sistem memori terpusat (*Shared Memory System*) dan tempat penyimpanan dokumentasi bersama untuk seluruh AI Agent lintas platform.

---

## 📌 Status Proyek & Lingkungan Saat Ini
- **Project Scope:** Multi-project Context & Shared Memory (`Arsip-IMO`, `SmartHome`, `SaveBuddy`, `SIMPKK-DIGITAL`, `Mentari Ecosystem`, `TailShare`, `Web Push Safari iOS`, `MT5 Docker Bot`, `agent-brain`)
- **Status:** Active / Production Ready
- **Last Updated By:** Antigravity AI Agent (Google DeepMind)
- **Last Updated At:** 2026-08-14 04:08 WIB

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
- [ ] Implementasi strategi & indikator algoritma trading lanjutan (RSI, MA crossover, risk management) di `bot.py`.

---

## 📝 Ringkasan Konteks Terakhir
1. **Automasi Trading MetaTrader 5 (Docker + Wine Python + Exness):** Berjalan di container Docker `exness-mt5` (Image `mt5:latest` KasmVNC port `3000`). Script `bot.py` dieksekusi di lingkungan Wine Python 3.9 (dengan `numpy==1.26.4` & package `MetaTrader5` 5.0.36) terhubung ke akun Exness Demo (`Exness-MT5Trial7`).
2. **Serverless Cloudflare Workers Push Notification Backend:** Backend notifikasi telah dimigrasi 100% ke **Cloudflare Workers** (`https://mt5-push-backend.alwiihsan50.workers.dev`), didukung oleh Cloudflare KV (`SUBSCRIPTIONS`) dan `@block65/webcrypto-web-push`. Layanan ini berjalan 24/7 gratis, menyajikan PWA registration UI + Service Worker + Push Trigger API, dan tidak lagi membebani proses/port lokal.
3. **Web Dokumentasi Lokal:** Dokumentasi interaktif disimpan di `/home/cuker/bot_web_docs/index.html`.
4. **Web Push Notification Safari iOS (iPhone & Local Server):** Menggunakan Web Push API standar, Service Worker (`sw.js`), `manifest.json` PWA Standalone, VAPID Keys, dan backend Node.js (`web-push`). Repo lokal: `safari-push-test`, Cloudflare Pages: `https://safari-push-test.pages.dev`.
5. **TailShare Universal Suite (Windows & Linux Native GUI):** Terkoneksi langsung ke folder **Drive D `D:\tailshare`** (`/media/cuker/Data/tailshare`). Mendukung GUI Native Electron (`bin/tailshare` dengan CommonJS preload & X11 sandbox flags), auto-attach ke daemon background systemd tanpa konflik port `53317`, live folder watcher, dan web UI. Repo: `https://github.com/alwiihsan50-lgtm/tailshare`.
6. **Pembaruan TailShare di Windows:** Repositori GitHub `alwiihsan50-lgtm/tailshare` telah dikloning dan diinstal di `C:\Users\alwii\Desktop\tailshare`. Port default telah dialihkan ke **53317**, script auto-start Startup Windows terpasang, file sharing terintegrasi ke `D:\tailshare`, dan shortcut Desktop diperbarui.
7. **Arsip-IMO Project:** Berada di branch `Beta2-redesign` (`D:\Documents\GitHub\Arsip-IMO`). Aplikasi karyawan React 19 + Supabase + Zustand. Layout kontrol kalender menggunakan grid 2x2 dengan font `12px`.
8. **Katalog Proyek Drive D (`D:\Projects`):** Terdiri dari 18 repositori Git aktif termasuk ekosistem IMO, SmartHome, SaveBuddy, SIMPKK Digital, PRD Generator, dan Ekosistem LPKP Mentari.
9. **Lingkungan & Reserved Ports:** Port **`53317`** (TailShare), Port **`3000`** (MT5 Web VNC GUI). Port `3005` telah dilepas.

---

## 📚 Indeks Dokumentasi (`docs/`)
- 📄 [Panduan Automasi Trading MT5 & Cloudflare Workers Push](docs/mt5-docker-forex-trading-automation.md) - Arsitektur Docker MT5, Wine Python MetaTrader5, Cloudflare Workers push backend, Cloudflare KV, dan integrasi bot.
- 📄 [Panduan Web Push Notification Safari iOS](docs/safari-ios-web-push-notification.md) - Arsitektur, syarat Apple Safari iOS PWA, spesifikasi Service Worker, VAPID keys, dan backend Node.js.
- 📄 [Panduan Instalasi TailShare di Linux Mint](docs/tailshare-linux-mint-installation.md) - Langkah-langkah instalasi Node.js, Tailscale, setup systemd auto-start, dan shortcut desktop di Linux Mint.
- 📄 [Katalog Proyek Drive D](docs/drive-d-projects-catalog.md) - Pemetaan lengkap 18 repositori Git, remote URL, branch aktif, dan direktori di Drive `D:\`.
- 📄 [Arsip-IMO Project Specification & Memory](docs/arsip-imo-project.md) - Dokumentasi lengkap proyek Arsip-IMO, batasan, arsitektur, navigasi, dan workflow delivery.
- 📄 [System Environment & Reserved Ports](docs/system-environment-and-ports.md) - Informasi spesifikasi sistem Windows/Linux, konfigurasi GitHub CLI, dan aturan Port terpesan (53317, 3000).

