# Setup & Arsitektur Automasi Trading MT5 (Docker + Exness + Cloudflare Workers Push Notification)

Dokumentasi komprehensif mengenai implementasi sistem trading bot otomatis yang berjalan di lingkungan terisolasi (Docker), terintegrasi dengan MetaTrader 5 Exness, serta terhubung ke sistem Push Notification mandiri (Apple Safari iOS) via **Cloudflare Workers (Serverless 24/7 Gratis)**.

---

## 🏗️ 1. Arsitektur Keseluruhan

Sistem automasi trading ini menggunakan arsitektur hybrid modern:

```
+-------------------------------------------------------------+
|                      Linux Host System                      |
|                                                             |
|  +-------------------------------------------------------+  |
|  |     Docker Container (exness-mt5)                     |  |
|  |                                                       |  |
|  |  [MetaTrader 5 GUI (Wine)] ---> Web VNC (Port 3000)   |  |
|  |          |                                            |  |
|  |  [Python 3.9 (Wine)]                                  |  |
|  |  - Script: /config/bot.py                             |  |
|  |  - Package: MetaTrader5 5.0.36                        |  |
|  |  - Downgrade: numpy==1.26.4 (numpy<2)                 |  |
|  +--------------------------+----------------------------+  |
|                             | HTTPS POST                    |
+-----------------------------|-------------------------------+
                              | (/trigger-notification)
                              v
             +----------------------------------+
             |   Cloudflare Workers (Serverless)|
             |   https://mt5-push-backend.      |
             |   alwiihsan50.workers.dev        |
             |                                  |
             |  - Library: webcrypto-web-push   |
             |  - Storage: Cloudflare KV (subs) |
             |  - Web UI: PWA Subscribe Page    |
             +----------------+-----------------+
                              | Web Push Protocol (Apple/Google)
                              v
                    +-------------------+
                    |   iPhone Safari   |
                    |  (PWA Standalone) |
                    | Push Notification |
                    +-------------------+
```

---

## 📦 2. Komponen & Detail Konfigurasi

### A. Container Docker MT5 & Dashboard (`docker-compose.yml`)
- **Lokasi Fisik (Drive D):** `/media/cuker/Data/mt5-storage.img` (Format ext4 30GB sparse image loop-mounted ke `/home/cuker/mt5_storage`)
- **Lokasi Compose:** `/home/cuker/mt5_storage/docker-compose.yml`
- **Containers:**
  - `exness-mt5` (Image: `mt5:latest` KasmVNC Port `3000` / `3001`)
  - `mt5-dashboard` (Python HTTP Realtime Web Dashboard Port `8080`)
- **Volume:** `/home/cuker/mt5_storage/mt5_config` -> `/config`
- **Environment:** `PUID=1000`, `PGID=1000`, `TZ=Asia/Jakarta`
- **Web UI GUI MT5:** `http://localhost:3000`
- **Web Dashboard Bot:** `http://localhost:8080`

### B. Lingkungan Python di dalam Wine
- **Path Python:** `C:\Program Files (x86)\Python39-32\python.exe` (Wine environment)
- **Modul Kunci:** `MetaTrader5` (v5.0.36), `numpy` (versi `1.26.4` - wajib `numpy<2`)
- **Catatan Penting:** Library `MetaTrader5` merupakan modul C-Extension Windows, sehingga script Python **harus dieksekusi di dalam Wine** container yang sama dengan terminal MT5:
  ```bash
  docker exec --user abc exness-mt5 wine python -u /config/bot.py
  ```

### C. Bot Python Logic (`mt5_config/bot.py`)
- Terletak di `/home/cuker/mt5_config/bot.py` (tersinkronisasi langsung ke `/config/bot.py` dalam container).
- Inisialisasi koneksi IPC ke terminal MT5 (`mt5.initialize()`).
- Mengambil info akun (Login ID, Saldo, Currency, Equity, Free Margin).
- Berlangganan ke symbol Market Watch (contoh: `EURUSDm` di akun Exness).
- Fungsi `send_push_notification(title, message)` yang mem-POST payload JSON ke endpoint Cloudflare Workers:
  `https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification`

### D. Cloudflare Worker Push Backend (`cf-push-backend`)
- **Lokasi Source:** `/home/cuker/cf-push-backend/`
- **URL Publik:** `https://mt5-push-backend.alwiihsan50.workers.dev`
- **Engine:** Cloudflare Worker (Hono + `@block65/webcrypto-web-push` + Web Crypto API)
- **Storage:** Cloudflare KV Namespace `SUBSCRIPTIONS` (ID: `0217d87236964fb796f7988e77f29de0`)
- **Fitur All-in-One:**
  - `GET /`: Menyajikan Web PWA Interface untuk tombol "Hubungkan ke Server" di iPhone.
  - `GET /sw.js`: Menyajikan Service Worker untuk menangkap background push event.
  - `GET /manifest.json`: Web App Manifest untuk PWA Standalone di Safari iOS.
  - `POST /subscribe`: Menyimpan objek langganan ke Cloudflare KV.
  - `POST /trigger-notification`: Mengirim notifikasi ke semua perangkat terdaftar.

---

## ⚡ 3. Cara Menjalankan & Menguji

### 1. Menjalankan Container MT5
```bash
cd /home/cuker
docker compose up -d
```
Akses `http://localhost:3000` di browser untuk login akun Exness.

### 2. Mendaftarkan iPhone (PWA Push)
1. Buka `https://mt5-push-backend.alwiihsan50.workers.dev` di Safari iPhone.
2. Tekan tombol **Share** -> **Add to Home Screen**.
3. Buka ikon aplikasi di Home Screen, lalu tekan **Hubungkan ke Cloudflare Server** (izinkan notifikasi).

### 3. Layanan Auto-Start 24/7 (Systemd Service)
Bot trading dan container MT5 telah dikonfigurasi untuk otomatis berjalan sendiri saat PC dihidupkan (*boot*):
* **Service Unit:** `/etc/systemd/system/mt5-trading-bot.service` (`systemctl status mt5-trading-bot.service`)
* **Runner Script:** `/home/cuker/start-bot.sh`
* **Log Realtime:** `journalctl -u mt5-trading-bot.service -f`

Perintah kontrol service:
```bash
sudo systemctl restart mt5-trading-bot.service   # Restart bot
sudo systemctl stop mt5-trading-bot.service      # Hentikan bot
sudo systemctl status mt5-trading-bot.service    # Cek status
```

### 4. Deploy / Update Worker (Bila ada perubahan)
```bash
cd /home/cuker/cf-push-backend
npx wrangler deploy
```

---

## 💡 Keuntungan Menggunakan Cloudflare Workers
1. **100% Gratis & Serverless:** Tidak memerlukan port lokal di host Linux dan tidak memakan RAM.
2. **24/7 Siap Sedia:** Backend selalu aktif di jaringan edge global Cloudflare.
3. **Bebas Tunnel:** Tidak perlu lagi menjalankan proses tunneling `cloudflared` atau `pinggy` untuk push notification.
