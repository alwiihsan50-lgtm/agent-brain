# Agent Brain - Central Context & Workspace

Repositori ini adalah sistem memori terpusat (*Shared Memory System*) dan tempat penyimpanan dokumentasi bersama untuk seluruh AI Agent lintas platform.

---

## 📌 Status Proyek & Lingkungan Saat Ini
- **Project Scope:** Multi-project Context & Shared Memory (`Arsip-IMO`, `SmartHome`, `SaveBuddy`, `SIMPKK-DIGITAL`, `Mentari Ecosystem`, `TailShare`, `agent-brain`)
- **Status:** Active / Production Ready
- **Last Updated By:** Antigravity AI Agent (Google DeepMind)
- **Last Updated At:** 2026-08-14 02:31 WIB

---

## 🚀 Progress & Checklist Pekerjaan

- [x] Inisialisasi repositori `agent-brain` dan SOP `AGENTS.md`
- [x] Migrasi seluruh memori & konteks proyek `Arsip-IMO` dari sesi terdahulu ke `docs/arsip-imo-project.md`
- [x] Pendokumentasian batasan lingkungan sistem & reserved port di `docs/system-environment-and-ports.md`
- [x] Pemetaan seluruh repositori dan proyek di Drive `D:\` ke `docs/drive-d-projects-catalog.md`
- [x] Tambahkan panduan instalasi & auto-start TailShare untuk **Linux Mint** di `docs/tailshare-linux-mint-installation.md`
- [x] Implementasi dan deployment penuh aplikasi **TailShare** versi lintas platform (**Windows & Linux**) dengan auto-start background 24/7, installer 1-klik Windows, live auto-sync folder **Drive D: `D:\tailshare`**, preview streaming langsung di web tanpa perlu download manual, dan push update ke `https://github.com/alwiihsan50-lgtm/tailshare`.
- [ ] Implementasi fitur baru atau pemeliharaan berkala sesuai instruksi pengguna selanjutnya.

---

## 📝 Ringkasan Konteks Terakhir
1. **TailShare Live Folder Sync (Drive D):** Terkoneksi langsung ke folder **Drive D `D:\tailshare`** (`/media/cuker/Data/tailshare`). Mendukung real-time directory watcher (file apa pun yang dimasukkan ke folder ini langsung muncul di web secara instan), streaming/preview foto & media langsung di browser tanpa perlu download ulang, auto-sync clipboard Windows & Linux, dan berjalan di port `53317`. Salinan Windows berada di `C:\Users\alwii\Desktop\tailshare-suite`.
2. **Arsip-IMO Project:** Berada di branch `Beta2-redesign` (`D:\Documents\GitHub\Arsip-IMO`). Aplikasi karyawan React 19 + Supabase + Zustand. Layout kontrol kalender menggunakan grid 2x2 dengan font `12px`.
3. **Katalog Proyek Drive D (`D:\Projects`):** Terdiri dari 18 repositori Git aktif termasuk ekosistem IMO, SmartHome, SaveBuddy, SIMPKK Digital, PRD Generator, dan Ekosistem LPKP Mentari.

---

## 📚 Indeks Dokumentasi (`docs/`)
- 📄 [Panduan Instalasi TailShare di Linux Mint](docs/tailshare-linux-mint-installation.md) - Langkah-langkah instalasi Node.js, Tailscale, setup systemd auto-start, dan shortcut desktop di Linux Mint.
- 📄 [Katalog Proyek Drive D](docs/drive-d-projects-catalog.md) - Pemetaan lengkap 18 repositori Git, remote URL, branch aktif, dan direktori di Drive `D:\`.
- 📄 [Arsip-IMO Project Specification & Memory](docs/arsip-imo-project.md) - Dokumentasi lengkap proyek Arsip-IMO, batasan, arsitektur, navigasi, dan workflow delivery.
- 📄 [System Environment & Reserved Ports](docs/system-environment-and-ports.md) - Informasi spesifikasi sistem Windows, konfigurasi GitHub CLI, dan aturan Port 40506 (TailShare).
