# 🏢 Ekosistem Digital LPKP Mentari

Dokumen ini memuat arsitektur lengkap, pemetaan repositori, basis data, alur bisnis, dan integrasi Dual-Engine Protocol untuk seluruh platform digital **LPKP Mentari** (`github.com/lpkpmentaribussiness`).

---

## 🏛️ 1. Profil & Legalitas Lembaga

- **Nama Resmi:** Lembaga Kursus dan Pelatihan Kerja LPKP Mentari
- **Tahun Berdiri:** 2001
- **Legalitas & Akreditasi:**
  - **NPSN:** `K5666768`
  - **Akreditasi:** Terakreditasi B (BAN-PNF 2017)
- **Alamat Lembaga:** Jl. Kutilang No. 5, Lingkungan 06, Kelurahan Bulian, Kecamatan Bajenis, Kota Tebing Tinggi, Sumatera Utara
- **Kontak & CS:** `0813-7000-7002` (`https://wa.me/6281370007002`) / `lpkp.mentari@gmail.com`

---

## 🌐 2. Repositori Utama & Peran Platform

| Nama Proyek | Direktori Lokal | Remote GitHub | Tech Stack | Keterangan / Peran |
| :--- | :--- | :--- | :--- | :--- |
| **Web 1: LPKPMentariWebsite** | `/media/cuker/Data/Projects/LPKPMentariWebsite` | `lpkpmentaribussiness/LPKPMentariWebsite` | Astro 7 + TypeScript + Vercel | Website profil resmi, legalitas, galeri prestasi, & katalog 6 program luring. |
| **Web 2: MentariOnlineCourse** | `/media/cuker/Data/Projects/MentariOnlineCourse` | `lpkpmentaribussiness/MentariOnlineCourse` | Next.js 16 + React 19 + Tailwind 4 + Supabase | Platform LMS daring, pemutar video, upload 6 ujian, grading instruktur, & verifikasi sertifikat digital. |
| **CompAcc** | `/media/cuker/Data/Projects/CompAcc` | `lpkpmentaribussiness/CompAcc` | Vite + React + TypeScript + Supabase | Platform aplikasi komputer akuntansi Mentari. |
| **MentariAcc** | `/media/cuker/Data/Projects/MentariAcc` | `lpkpmentaribussiness/MentariAcc` | Vite + React + Supabase | Aplikasi manajemen keuangan & akuntansi internal. |

---

## 📚 3. Katalog Program Pelatihan

### A. Program Pelatihan Vokasi Lembaga (Web 1 - Luring)
1. **Komputer Office:** Keterampilan aplikasi perkantoran (Word, Excel, PowerPoint) untuk administrasi kerja.
2. **Teknisi Komputer:** Perawatan, instalasi, perakitan, dan troubleshooting hardware/software.
3. **Desain Grafis:** Komunikasi visual, manipulasi grafis, dan aset promosi digital.
4. **Akuntansi MYOB:** Pembukuan dan penyusunan laporan keuangan terkomputerisasi.
5. **Tata Boga:** Pengolahan kuliner dan wirausaha makanan.
6. **Menjahit:** Pembuatan pola dan teknik menjahit garmen.

### B. Paket Kursus Online Bersertifikat (Web 2 - Daring / LMS)
1. **Microsoft Office Dasar (Rp 500.000):** 18 materi video fondasi + 6 ujian praktik Word, Excel, PowerPoint + sertifikat resmi.
2. **Microsoft Office Lanjutan (Rp 500.000):** 18 materi video tingkat lanjut + 6 ujian praktik Word, Excel, PowerPoint + sertifikat resmi.

---

## 🗄️ 4. Infrastruktur Database & Layanan Terhubung

- **Supabase Project:** `MentariOnlineCourse` (`zzfkzlvjqskyffmmierh`)
- **Tabel Utama:**
  - `profiles`: Akun pengguna dan pemisahan role (`participant`, `instructor`, `admin`).
  - `courses`: Master kursus online (`office-dasar`, `office-lanjutan`).
  - `lessons`: Modul video materi dan ujian per aplikasi.
  - `enrollments`: Pendaftaran kursus dan status verifikasi pembayaran.
  - `submissions`: File tugas & ujian praktik yang diupload siswa beserta nilai & catatan pengajar.
  - `certificates`: Metadata nomor sertifikat dan link dokumen verifikasi resmi.
- **Storage Buckets:** `materials`, `submissions`, `certificates`
- **Video Delivery:** Bunny Stream / Tus upload client.

---

## 🔄 5. Standar Alur Kerja (Dual-Engine Protocol)

1. **AST Code Navigation:** Setiap repositori dilengkapi `graphify-out/` untuk penelusuran arsitektur kode instan tanpa membebani context token.
2. **Auto-Sync Git Hook:** File `.git/hooks/post-commit` terpasang di setiap repo untuk memicu `graphify update .` otomatis saat ada commit baru.
3. **Project Memory:** Setiap repo memiliki `AGENTS.md` yang memuat batasan teknis, routing, dan skrip validasi.
