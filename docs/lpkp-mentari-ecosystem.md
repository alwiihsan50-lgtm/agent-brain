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

| Nama Proyek | Direktori Lokal | Remote GitHub | Tech Stack & DNS | Keterangan / Peran |
| :--- | :--- | :--- | :--- | :--- |
| **Web 1: LPKPMentariWebsite** | `/media/cuker/Data/Projects/LPKPMentariWebsite` | `lpkpmentaribussiness/LPKPMentariWebsite` | Astro 7 + TS + Vercel (DNS: Cloudflare `76.76.21.21`) | Website profil resmi (`lpkpmentari.id`), legalitas, galeri prestasi, & katalog 12 program vokasi. |
| **Web 2: MentariOnlineCourse** | `/media/cuker/Data/Projects/MentariOnlineCourse` | `lpkpmentaribussiness/MentariOnlineCourse` | Next.js 16 + React 19 + Tailwind 4 + Supabase | Platform LMS daring, pemutar video, upload 6 ujian, grading instruktur, & verifikasi sertifikat digital. |
| **CompAcc** | `/media/cuker/Data/Projects/CompAcc` | `lpkpmentaribussiness/CompAcc` | Vite + React + TypeScript + Supabase | Platform aplikasi komputer akuntansi Mentari. |
| **MentariAcc** | `/media/cuker/Data/Projects/MentariAcc` | `lpkpmentaribussiness/MentariAcc` | Vite + React + Supabase | Aplikasi manajemen keuangan & akuntansi internal. |
| **LMS & Shop Legacy** | Hostinger hPanel | - | PHP 8.4 / LiteSpeed (`153.92.9.143`) | Subdomain `lms.lpkpmentari.id` & `marketplace.lpkpmentari.id` (routed via Cloudflare DNS-Only). |

---

## 📚 3. Katalog Program Pelatihan

### A. Program Pelatihan Vokasi Lembaga (Web 1 - Luring)
1. **Komputer Office:** Keterampilan aplikasi perkantoran (Word, Excel, PowerPoint) untuk administrasi kerja.
2. **Teknisi Komputer:** Perawatan, instalasi, perakitan, dan troubleshooting hardware/software.
3. **Teknik Jaringan:** Instalasi, konfigurasi jaringan komputer LAN/WLAN, dan infrastruktur konektivitas.
4. **Desain Grafis:** Komunikasi visual, manipulasi grafis, dan aset promosi digital kreatif.
5. **Multimedia:** Produksi konten audio-visual, video, fotografi, dan media interaktif.
6. **Programer Web Desain:** Perancangan tampilan website responsif, antarmuka UX/UI, dan dasar web coding.
7. **Akuntansi Myob-Accurate:** Pencatatan dan pembukuan terkomputerisasi sistem MYOB & Accurate.
8. **Tata Boga:** Pengolahan kuliner komersial dan wirausaha makanan mandiri.
9. **Tata Busana:** Pembuatan pola pakaian, teknik menjahit, dan produksi garmen siap pakai.
10. **Salon Tata Rias:** Tata rias wajah, perawatan kecantikan, dan penataan rambut profesional.
11. **Pengelasan:** Teknik las listrik/SMAW, keselamatan kerja bengkel, dan fabrikasi logam.
12. **Barista Kopi:** Seni racik kopi, teknik manual brewing, mesin espresso, dan manajemen coffee bar.

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
- **Domain & DNS Routing (`lpkpmentari.id`):**
  - **Registrar:** Niagahoster / Hostinger (Valid s/d 11 Juni 2027)
  - **DNS Manager:** Cloudflare (`love.ns.cloudflare.com`, `ricardo.ns.cloudflare.com`)
  - **Apex (`@`) & `www`:** Vercel Edge (`76.76.21.21` & `cname.vercel-dns.com`, DNS-Only)
  - **Subdomain `lms` & `marketplace`:** Hostinger Shared Hosting (`153.92.9.143`, DNS-Only)

---

## 🔄 5. Standar Alur Kerja (Dual-Engine Protocol)

1. **AST Code Navigation:** Setiap repositori dilengkapi `graphify-out/` untuk penelusuran arsitektur kode instan tanpa membebani context token.
2. **Auto-Sync Git Hook:** File `.git/hooks/post-commit` terpasang di setiap repo untuk memicu `graphify update .` otomatis saat ada commit baru.
3. **Project Memory:** Setiap repo memiliki `AGENTS.md` yang memuat batasan teknis, routing, dan skrip validasi.
