# 🔮 Master Obsidian × Graphify Unified Workspace Guide

Dokumen ini menjelaskan arsitektur, struktur, dan panduan penggunaan **Master Obsidian × Graphify Workspace** yang menyatukan seluruh memori jangka panjang (**agent-brain**), peta arsitektur micro-level (**Graphify**), dan seluruh 23 proyek kerja aktif di Drive `D:\` ke dalam satu **Master Obsidian Vault** yang persisten.

---

## 🏛️ Mengapa Master Vault Diletakkan di Drive D:?

Master Vault disimpan di:
```text
/media/cuker/Data/ObsidianVault/
```
**Keuntungan Utama:**
1. **Kebal Instal Ulang OS (*OS-Reinstall Proof*):**
   Karena berada di partisi Drive D (`/media/cuker/Data`), seluruh catatan, grafik relasi, visual canvas, dan dashboard **TIDAK AKAN HILANG** saat Anda berganti distro Linux, format partisi root, atau upgrade sistem operasi.
2. **Single Source of Truth:**
   Mengintegrasikan 23 repositori Git dan ratusan modul kode ke dalam satu jaring *backlinks* `[[wikilinks]]` yang saling terhubung.

---

## 📂 Struktur Master Obsidian Vault

```text
/media/cuker/Data/ObsidianVault/
├── 00 - Master Dashboard.md       # Pusat kendali: status proyek, tabel port, & ringkasan
├── 00 - Ecosystem Map.canvas       # Peta visual interaktif seluruh proyek mengitari agent-brain
│
├── 00 - Agent Brain/              # Memori Makro & SOP Imutable
│   ├── README.md                  # Status infrastruktur (STB, Mentari, MT5, Tailshare, dll)
│   ├── AGENTS.md                  # SOP & Protokol Wajib AI Agent
│   └── docs/                      # 20+ Panduan teknis mendalam
│
├── 01 - Projects/                 # Knowledge Graph Mikro per Proyek (23 Proyek)
│   ├── Monitor-Sistem-Desktop/    # AST notes, class, method, & community clusters
│   ├── Arsip-IMO/
│   ├── ADMIN-WEB-IMO/
│   ├── SmartHome/
│   ├── Catat-Duit-Voice/
│   ├── MoneyPrinterTurbo/
│   ├── CompAcc/
│   ├── MentariAcc/
│   ├── LPKPMentariWebsite/
│   ├── MentariOnlineCourse/
│   ├── simpkk-digital/
│   ├── timemark-photo-adjustment/
│   ├── fbagent/
│   ├── ttagent/
│   └── ... (Seluruh repositori Drive D)
│
└── 02 - Knowledge Base/           # Catatan arsitektur umum & dokumentasi pendukung
```

---

## 🚀 Cara Menggunakan Obsidian

1. **Buka Aplikasi Obsidian**:
   - Cari **Obsidian** di Menu Aplikasi Linux Mint, atau jalankan via terminal:
     ```bash
     flatpak run md.obsidian.Obsidian &
     ```
2. **Buka Master Vault**:
   - Pada layar awal Obsidian, pilih **"Open folder as vault"**.
   - Pilih direktori: `/media/cuker/Data/ObsidianVault`.
3. **Mulai Menjelajah**:
   - **Dashboard**: Buka `00 - Master Dashboard.md` untuk melihat status proyek & link cepat.
   - **Graph View (Ctrl + G)**: Buka graf interaktif raksasa untuk melihat bagaimana fungsi, modul, dan proyek saling terhubung.
   - **Canvas View**: Buka `00 - Ecosystem Map.canvas` untuk melihat tata letak visual proyek.
   - **Quick Switcher (Ctrl + O)**: Ketik nama class, fungsi, file, atau konsep untuk melompat langsung ke catatannya.

---

## 🔄 Otomatisasi & Auto-Sync Lintas Proyek

1. **Git Post-Commit Hook (Otomatis per Commit)**:
   Seluruh 23 repositori telah dipasangi post-commit hook. Setiap kali Anda atau AI Agent melakukan `git commit`, Graphify lokal akan otomatis sinkron di latar belakang tanpa biaya token.

2. **Perintah Sinkronisasi Manual Satu Baris**:
   Kapan pun Anda menambahkan proyek baru di Drive D atau ingin menyinkronkan ulang seluruh vault, jalankan di terminal:
   ```bash
   obsidian-sync
   ```
   *Perintah ini akan secara otomatis memindai seluruh folder di Drive D, mengekstrak AST kode terbaru, memperbarui catatan Obsidian, dan menyusun ulang Master Dashboard.*

---

## 🤖 Panduan untuk AI Agent
Saat AI Agent bekerja di workspace ini:
- **Tingkat Makro**: Buka `/media/cuker/Data/ObsidianVault/00 - Agent Brain/` untuk memahami arsitektur & port.
- **Tingkat Mikro**: Gunakan `graphify query`, `graphify path`, atau baca catatan modul di `01 - Projects/<nama_proyek>/`.
- **Setelah Modifikasi**: Jalankan `obsidian-sync` jika struktur arsitektur baru ingin langsung terindeks di Obsidian.
