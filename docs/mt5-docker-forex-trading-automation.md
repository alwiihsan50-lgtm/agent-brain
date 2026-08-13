# Setup & Arsitektur Automasi Trading MT5 (Docker + Exness + Push Notification iOS)

Dokumentasi komprehensif mengenai implementasi sistem trading bot otomatis yang berjalan di lingkungan terisolasi (Docker), terintegrasi dengan MetaTrader 5 Exness, serta terhubung ke sistem Push Notification mandiri (Apple Safari iOS) via Cloudflare Tunnel.

---

## 🏗️ 1. Arsitektur Keseluruhan

Sistem automasi trading ini mengombinasikan 4 layer utama:

```
+-------------------------------------------------------------------------------+
|                                Linux Host System                              |
|                                                                               |
|  +-----------------------------+         +---------------------------------+  |
|  |     Docker Container        |         |        Host Services            |  |
|  |       (exness-mt5)          |         |                                 |  |
|  |                             |         |  +---------------------------+  |  |
|  |  [MetaTrader 5 GUI (Wine)]  |         |  | Node.js Push Server       |  |  |
|  |          |                  |  HTTP   |  | (Port 3005)               |  |  |
|  |  [Python 3.9 (Wine)]        |-------->|  | (/home/cuker/bot_push_...) |  |  |
|  |  - Script: /config/bot.py   | 172.17.0.1|  +-------------+-------------+  |  |
|  |  - Package: MetaTrader5     |  :3005  |                |                |  |
|  |  - Downgrade: numpy<2       |         |                v                |  |
|  +--------------+--------------+         |  +---------------------------+  |  |
|                 |                        |  | Cloudflare Tunnel         |  |  |
|                 | Port 3000              |  | (mt5-push via cloudflared)|  |  |
|                 v                        |  +-------------+-------------+  |  |
|          Web VNC Interface               |                |                |  |
|          (http://localhost:3000)         +----------------|----------------+  |
+-----------------------------------------------------------|-------------------+
                                                            | HTTPS / SSL
                                                            v
                                                  +-------------------+
                                                  |   iPhone Safari   |
                                                  |  (PWA Subscribed) |
                                                  | Push Notification |
                                                  +-------------------+
```

---

## 📦 2. Komponen & Detail Konfigurasi

### A. Container Docker MT5 (`docker-compose.yml`)
- **Lokasi Compose:** `/home/cuker/docker-compose.yml`
- **Container Name:** `exness-mt5`
- **Image:** `mt5:latest` (berbasis `gmag11/MetaTrader5-Docker` dengan KasmVNC)
- **Port:** `3000` (Web VNC HTTP), `3001` (HTTPS)
- **Volume:** `/home/cuker/mt5_config` -> `/config`
- **Environment:** `PUID=1000`, `PGID=1000`, `TZ=Asia/Jakarta`
- **Web UI GUI:** `http://localhost:3000`

### B. Lingkungan Python di dalam Wine
- **Path Python:** `C:\Program Files (x86)\Python39-32\python.exe` (Wine environment)
- **Modul Kunci:** `MetaTrader5` (v5.0.36), `numpy` (versi `1.26.4` - wajib `numpy<2`)
- **Catatan Penting:** Library `MetaTrader5` merupakan modul C-Extension Windows, sehingga script Python **harus dieksekusi di dalam Wine** container yang sama dengan terminal MT5:
  ```bash
  docker exec --user abc exness-mt5 wine python -u /config/bot.py
  ```
- **Network Bridge:** Container mengakses push server host menggunakan IP default Docker bridge `http://172.17.0.1:3005`.

### C. Bot Python Logic (`mt5_config/bot.py`)
- Terletak di `/home/cuker/mt5_config/bot.py` (tersinkronisasi langsung ke `/config/bot.py` dalam container).
- Inisialisasi koneksi IPC ke terminal MT5 (`mt5.initialize()`).
- Mengambil info akun (Login ID, Saldo, Currency, Equity, Free Margin).
- Berlangganan ke symbol Market Watch (contoh: `EURUSDm` di akun Exness).
- Fungsi `send_push_notification(title, message)` yang mem-POST payload JSON ke server push lokal.

### D. Push Notification Server (Node.js)
- **Lokasi:** `/home/cuker/bot_push_server/backend/`
- **Port:** `3005` (diubah dari `3000` untuk mencegah konflik dengan MT5 Web GUI)
- **Framework:** Express.js + `web-push` library
- **Endpoint Utama:**
  - `POST /subscribe`: Menerima & menyimpan objek `subscription` dari client browser / iPhone PWA.
  - `POST /trigger-notification`: Menerima `{ title, message }` dan mem-broadcast web push ke seluruh perangkat terdaftar.

### E. Cloudflare Tunnel (`cloudflared`)
- **Nama Tunnel:** `mt5-push`
- **CLI:** `cloudflared` (native linux-amd64 package)
- **Rute DNS:** Dihubungkan ke custom subdomain di Cloudflare DNS user.
- **Eksekusi:**
  ```bash
  cloudflared tunnel run --url http://localhost:3005 mt5-push
  ```

### F. Web Dokumentasi & PWA Client
- **Dokumentasi Statis:** `/home/cuker/bot_web_docs/index.html`
- **Client PWA Pendaftaran:** `/home/cuker/bot_push_server/backend/public/` (`index.html`, `sw.js`, `manifest.json`)

---

## ⚡ 3. Cara Menjalankan & Mengelola Layanan

### 1. Menjalankan Container MT5
```bash
cd /home/cuker
docker compose up -d
```
Akses `http://localhost:3000` untuk login akun Exness (pilih server sesuai akun demo/real).

### 2. Menjalankan Backend Push Notification
```bash
cd /home/cuker/bot_push_server/backend
npm start
```

### 3. Menjalankan Cloudflare Tunnel
```bash
cloudflared tunnel run --url http://localhost:3005 mt5-push
```

### 4. Menjalankan Bot Trading Python
```bash
docker exec --user abc exness-mt5 wine python -u /config/bot.py
```

---

## ⚠️ 4. Troubleshooting & Gotchas

1. **Error NumPy `_ARRAY_API not found`:**
   Pustaka `MetaTrader5` tidak kompatibel dengan NumPy 2.x. Jika diinstall ulang, pastikan downgrade:
   ```bash
   docker exec --user abc exness-mt5 wine python -m pip install "numpy<2"
   ```
2. **Koneksi Container ke Host (`Connection Refused` di localhost:3005):**
   Di dalam Docker container, `localhost` merujuk ke container itu sendiri. Untuk mengakses port 3005 di host Linux, gunakan IP `172.17.0.1:3005`.
3. **Encoding Karakter / Emoji di Terminal Windows (Wine):**
   Standard output di Wine dapat memunculkan warning `charmap codec can't encode character` jika terdapat emoji non-ASCII pada `print()`, namun transmisi HTTP Push Notification tetap berhasil terkirim utuh ke iPhone.
