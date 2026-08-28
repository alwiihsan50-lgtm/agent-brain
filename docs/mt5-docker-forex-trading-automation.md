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

### A. Container Docker MT5 (`docker-compose.yml`)
- **Host Server:** `mentari-server` / Local Linux Mint
- **Lokasi Direktori:** `/home/mentari/mt5_storage` (`/home/cuker/mt5_storage`)
- **Lokasi Compose:** `/home/mentari/mt5_storage/docker-compose.yml`
- **In-Memory RAM Architecture:**
  - **Shared RAM Volume (`ram_buffer`):** Driver `tmpfs` berukuran 64 MB di-mount ke `/ram_data` di container MT5.
  - **Container tmpfs Mounts:** `/tmp` (512M) dan `/dev/shm` (512M) berjalan di RAM.
- **Containers:**
  - `exness-mt5` (Akun Utama: `434073017` Exness, KasmVNC Port `3000` / `3001`)
  - `propfirm-mt5` (Akun ke-2: `463880423` Exness, KasmVNC Port `3002` / `3003`)
- **Volume Persisten:** `./mt5_config` -> `/config` (Akun 1) dan `./mt5_config_prop1` -> `/config` (Akun 2)
- **Environment:** `PUID=1000`, `PGID=1000`, `TZ=Asia/Jakarta`
- **Web UI GUI MT5:**
  - Akun 1: `https://mt5.abbas.my.id` / `http://localhost:3000`
  - Akun 2: `http://localhost:3002` *(HTTPS: `3003`)*

### B. Lingkungan Python di dalam Wine
- **Path Python:** `C:\Program Files (x86)\Python39-32\python.exe` (Wine environment)
- **Modul Kunci:** `MetaTrader5` (v5.0.36), `numpy` (versi `1.26.4` - wajib `numpy<2`)
- **Catatan Penting:** Library `MetaTrader5` merupakan modul C-Extension Windows, sehingga script Python **harus dieksekusi di dalam Wine** container yang sama dengan terminal MT5:
  ```bash
  docker exec --user abc exness-mt5 wine python -u /config/bot.py
  ```

### C. Bot Python Logic (`mt5_config/bot.py`)
- Terletak di `/home/cuker/mt5_storage/mt5_config/bot.py` (tersinkronisasi langsung ke `/config/bot.py` dalam container).
- Inisialisasi koneksi IPC ke terminal MT5 (`mt5.initialize()`).
- Mengambil info akun (Login ID, Saldo, Currency, Equity, Free Margin).
- **Smart Money Concepts (SMC) & Multi-Pair Engine:**
  - **Market Structure Mapping:** 5-Bar Fractal Swings pada M15 & H1, mendeteksi Break of Structure (BOS) dan Change of Character (CHoCH).
  - **Liquidity Sweep Detection (BSL & SSL):** Mengidentifikasi manipulasi likuiditas institusional (wick rejection di atas swing high / di bawah swing low).
  - **Institutional Order Block (OB) & Fair Value Gap (FVG):** Memetakan area supply & demand terdekat serta imbalance harga.
  - **Equilibrium 50% Filter:** Mengharuskan BUY hanya pada zona Discount (< 50% swing range) dan SELL hanya pada zona Premium (> 50% swing range).
  - **Strict Risk Controls:** Wajib Stop Loss di luar batas Order Block / Swing Rejection, minimal Risk-to-Reward 1:2.0, Auto Break-Even (BE) otomatis saat trade mencapai 1.0x R:R, hard equity drawdown cap 10%, dan max 3 open positions total.
- **Proteksi Anti-Spam Notifikasi:** Fungsi `send_push_notification(title, message, cooldown_seconds=30)` dilengkapi deduplication & 30-second cooldown timer untuk mencegah loop pesan ke Cloudflare Workers:
  `https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification`

### D. Cloudflare Worker Push Backend (`cf-push-backend`)
- **Lokasi Source:** `/home/mentari/mt5_storage/cf-push-backend/`
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
cd /home/mentari/mt5_storage
docker compose up -d
```
Akses `https://vnc.abbas.my.id` atau `http://100.109.208.27:3000` di browser untuk login akun Exness.

### 2. Mendaftarkan iPhone (PWA Push)
1. Buka `https://mt5-push-backend.alwiihsan50.workers.dev` di Safari iPhone.
2. Tekan tombol **Share** -> **Add to Home Screen**.
3. Buka ikon aplikasi di Home Screen, lalu tekan **Hubungkan ke Cloudflare Server** (izinkan notifikasi).

### 3. Layanan Auto-Start 24/7 (Systemd Service)
Bot trading dan container MT5 telah dikonfigurasi untuk otomatis berjalan sendiri saat server dihidupkan (*boot*):
* **Service Unit:** `/etc/systemd/system/mt5-trading-bot.service` (`systemctl status mt5-trading-bot.service`)
* **Runner Script:** `/home/mentari/mt5_storage/start-bot.sh`
* **Log Realtime:** `journalctl -u mt5-trading-bot.service -f`

Perintah kontrol service di `mentari-server`:
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
