# 🎬 MoneyPrinterTurbo — Automated AI Video Production Factory

Dokumentasi implementasi, konfigurasi, arsitektur hybrid "Naik Kelas", dan panduan operasional MoneyPrinterTurbo.

---

## 📂 Lokasi Workspace & Virtual Environment
- **Direktori Proyek:** `/media/cuker/Data/Projects/MoneyPrinterTurbo`
- **Virtual Environment:** `/home/cuker/.virtualenvs/moneyprinterturbo`
- **Konfigurasi Utama:** `/media/cuker/Data/Projects/MoneyPrinterTurbo/config.toml`
- **Folder Aset Video Lokal:** `/media/cuker/Data/Projects/MoneyPrinterTurbo/storage/local_videos`
- **Folder Font Tambahan:** `/media/cuker/Data/Projects/MoneyPrinterTurbo/resource/fonts` (Impact, BeVietnamPro-Bold, dll.)

---

## 🌐 Port Mapping & Services
Untuk menjaga kepatuhan terhadap aturan sistem dan mencegah tabrakan dengan reserved ports:

| Service | Port | Endpoint / URL | Keterangan |
| :--- | :--- | :--- | :--- |
| **Streamlit WebUI** | `8501` | `http://127.0.0.1:8501` | Dashboard interaktif visual pembuatan video & pengaturan subtitle. |
| **FastAPI REST Server** | `8095` | `http://127.0.0.1:8095/docs` | REST API backend untuk automasi batch/remote (Menggantikan port 8080 default). |

---

## ⚡ Cara Menjalankan Service

### 1. Menjalankan Streamlit WebUI (Visual Dashboard)
```bash
cd /media/cuker/Data/Projects/MoneyPrinterTurbo
./webui.sh
```
Buka browser di `http://127.0.0.1:8501`.

### 2. Menjalankan REST API Server
```bash
cd /media/cuker/Data/Projects/MoneyPrinterTurbo
./run_api.sh
```
Akses dokumentasi Swagger interaktif di `http://127.0.0.1:8095/docs`.

---

## 🚀 Pendekatan Hybrid "Naik Kelas"

Untuk menghindari konten bernuansa *spam / low-effort stock video*, konfigurasi default telah dioptimalkan:
1. **Rasio Format 9:16 Vertikal:** Format native video TikTok/Reels/Shorts (`1080x1920`).
2. **Audio & Narasi Indonesia Dinamis:** Default suara diset ke `id-ID-ArdiNeural` via Edge-TTS dengan speed multiplier `1.08x` untuk pacing cepat dan retensi tinggi.
3. **High-Visibility Viral Subtitles:**
   * **Font:** `impact.ttf` / `BeVietnamPro-Bold.ttf` (tebal, tegas, dan mudah terbaca).
   * **Warna:** Kuning Kontras (`#FFFF00`) dengan stroke hitam tebal (`2.5px`).
   * **Posisi Aman (Safe Zone):** `68%` dari atas layar (menghindari tumpang tindih dengan caption bawah dan tombol interaksi TikTok di sebelah kanan).
4. **Local Asset Bank Priority:** Memanfaatkan `storage/local_videos` untuk memasukkan footage produk real dan b-roll autentik.
