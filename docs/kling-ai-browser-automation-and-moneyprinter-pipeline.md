# Kling AI Browser Automation & MoneyPrinterTurbo Pipeline

Dokumentasi implementasi otomasi browser nyata (*Real Browser Automation*) untuk **Kling AI** menggunakan Playwright Chromium, sinkronisasi sesi Firefox, pemanfaatan kuota harian gratis web (66 kredit/hari), CLI `kling-video`, dan integrasinya ke **MoneyPrinterTurbo** (Port 8501) serta **TailShare** (Port 40506).

---

## 🏛️ 1. Latar Belakang & Analisis Masalah

1. **Pemisahan Saldo Kling AI Developer API vs Web Portal:**
   - Kling AI menyediakan **66 kredit gratis setiap hari** di web portal (`kling.ai`), namun API Developer resminya (`app.klingai.com/global/dev/api-key`) memisahkan saldo dan membutuhkan top-up berbayar.
   - Pemanggilan via API Developer resmi tanpa saldo menghasilkan error: `RuntimeError: Kling API error (429): Account balance not enough`.
2. **Reverse Engineering Web API (`klingCreator`) Telah Usang:**
   - Proyek reverse-engineering berbasis cookie HTTP (`yihong0618/klingCreator`) telah didepresiasi karena sistem keamanan Kuaishou/Kling AI menerapkan enkripsi tanda tangan JavaScript dinamis (`kwscode`/`kwfv1`) dan proteksi WAF (Issue #32: `status 500 / MID.S4B`).
3. **Solusi: Otomasi Browser Nyata (*Real Browser Automation*):**
   - Menjalankan engine Chromium headless resmi Playwright dengan menginjeksi seluruh sesi autentikasi dari browser Firefox lokal pengguna (`cookies.sqlite` dan 63 item `localStorage`).
   - Eksekusi JavaScript resmi Kling AI berjalan di dalam browser sehingga tanda tangan keamanan sah dan bypass proteksi anti-bot WAF.

---

## ⚙️ 2. Komponen & Arsitektur Solusi

```
[Profil Firefox Pengguna]
  ├── cookies.sqlite (passToken, did, kwscode, dll.)
  └── ls/data.sqlite (klingai_user, userId, dll.)
          │
          ▼  (Auto-injeksi)
[Playwright Chromium Headless]
  ├── Buka https://kling.ai/app/video/new
  ├── Pilih Model: VIDEO 1.5
  ├── Konfigurasi Resolusi: 720p (Free-tier, 20 kredit/video)
  ├── Isi Prompt Storytelling
  └── Klik Generate & Pantau Render Cloud
          │
          ▼  (Auto-download via IconDownload)
[Penyimpanan Lokal & Integrasi Ekosistem]
  ├── MoneyPrinterTurbo: /media/cuker/Data/Projects/MoneyPrinterTurbo/storage/local_videos/
  └── TailShare: /media/cuker/Data/tailshare/ (Port 40506 / share.abbas.my.id)
```

---

## 📋 3. Tabel Biaya Kredit Kling AI (Web 720p)

| Model | Resolusi | Biaya Kredit | Kapasitas Harian (66 Kredit) |
| :--- | :--- | :--- | :--- |
| **VIDEO 1.0 (Standard)** | 720p | **10 kredit** | 6 video klip / hari |
| **VIDEO 1.5 (High Quality)** | 720p | **20 kredit** | 3 video klip / hari |
| **VIDEO 3.0 (Tercanggih, No Audio)** | 720p | **40 kredit** | 1 video klip / hari |
| **VIDEO 3.0 (Native Audio)** | 720p | **60 kredit** | 1 video klip / hari |

> ⚠️ *Catatan: Resolusi 1080p dan 4K eksklusif untuk pelanggan berbayar (Subscription).*

---

## 🚀 4. Penggunaan CLI `kling-video`

Tool CLI global telah dipasang di `/home/cuker/.local/bin/kling-video`.

```bash
# Generate video dari mana saja di terminal
kling-video -p "Cinematic shot of a cozy rustic coffee shop on a rainy afternoon, steam rising, warm lighting, 4k"

# Atau dengan nama file output spesifik
kling-video -p "A warrior walking in rain" -o "warrior_rain.mp4"
```

### Karakteristik File Hasil Uji Coba:
* **File:** `kling_coffee_rain.mp4` (5.5 MB)
* **Resolusi:** 1280x720, 30 fps (H.264), durasi 5.11 detik.
* **Audio:** Stereo AAC ambient rain & cafe.
* **Tersedia di TailShare:** `http://localhost:40506` dan `https://share.abbas.my.id`.

---

## 🎬 5. Pipeline MoneyPrinterTurbo

1. Video hasil generate otomatis masuk ke `/media/cuker/Data/Projects/MoneyPrinterTurbo/storage/local_videos/`.
2. Buka WebUI MoneyPrinterTurbo di [http://localhost:8501](http://localhost:8501).
3. Pilih **Video Source:** `Local Video` -> Pilih video hasil render Kling.
4. MoneyPrinterTurbo + model AI lokal AGY (Port 5050) merakit narasi suara TTS, background music, dan subtitle dinamis menjadi video konten siap upload.
