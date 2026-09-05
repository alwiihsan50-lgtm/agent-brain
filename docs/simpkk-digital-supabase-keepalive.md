# SIMPKK-DIGITAL: Supabase Keep-Alive Architecture

## 📌 Ringkasan Masalah & Solusi

Project **SIMPKK-DIGITAL** menggunakan Supabase Free Tier yang memiliki kebijakan otomatisasi pause setelah 7 hari tidak ada aktivitas kueri database (PostgreSQL). Karena website ini tidak diakses setiap hari, database rawan ter-pause.

### Masalah Terdahulu:
1. **Repository Secrets Belum Diset:** Workflow GitHub Action sebelumnya gagal 100% pada step `Validate Secrets` karena secret `SUPABASE_URL` dan `SUPABASE_ANON_KEY` kosong di GitHub.
2. **Endpoint Tidak Menyentuh PostgreSQL:** Workflow sebelumnya memanggil root `/rest/v1/` dan `/auth/v1/health` yang di-cache gateway dan tidak memicu transaksi kueri PostgreSQL nyata.

---

## 🛡️ Dual-Layer Keep-Alive System

Untuk menjamin Supabase tidak pernah ter-pause meski ditinggal lama:

### 1. Cloud Layer (GitHub Actions Workflow)
- **File:** `.github/workflows/supabase-keep-alive.yml`
- **Jadwal:** Berjalan setiap 2 hari (`0 2 */2 * *` pada pukul 09:00 WIB).
- **Target Kueri:**
  1. **PostgreSQL Database Engine:** `GET /rest/v1/dusuns?select=id&limit=1` (memaksa PostgREST mengeksekusi engine kueri PostgreSQL).
  2. **Supabase Auth Service:** `GET /auth/v1/settings` (memastikan service auth 200 OK).
  3. **Supabase Storage Service:** `GET /storage/v1/bucket` (memastikan service bucket aktif).
- **Secrets:** `SUPABASE_URL` & `SUPABASE_ANON_KEY` diset via GitHub Actions Secrets.

### 2. Local Fallback Layer (Dihapus atas permintaan User)
- Script lokal dan entri crontab di sistem Linux Mint telah dibersihkan/dihapus agar tidak membebani sistem lokal.
- Pengawasan keep-alive difokuskan pada Cloud Layer (GitHub Actions) dan layanan cloud independen (cron-job.org).

---

## 🔍 Cara Verifikasi Manual
1. **GitHub Actions:**
   ```bash
   gh workflow run "supabase-keep-alive.yml" --repo alwiihsan50-lgtm/SIMPKK-DIGITAL
   gh run list --workflow=supabase-keep-alive.yml --repo alwiihsan50-lgtm/SIMPKK-DIGITAL
   ```

