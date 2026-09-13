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
  - `exness-mt5` (Akun Utama: `434073017` Exness, KasmVNC Port `3000` / `3001` - **AKTIF / RUNNING**)
  - `propfirm-mt5` (Akun ke-2: `463880423` Exness, KasmVNC Port `3006` / `3007` - **NONAKTIF / STOPPED**)
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
  - **Strict Risk Controls:** Wajib Stop Loss di luar batas Order Block / Swing Rejection, Risk FLAT Rp 50.000 per trade, batas SL terukur per instrumen (`XAUUSDm`: 1.50 - 3.50; `EURUSDm`: 3 - 12 pips; `GBPUSDm`: 4 - 15 pips untuk mencegah kerugian melebihi ~Rp 50rb-60rb pada minimal lot 0.01), konfirmasi Break of Structure (BOS menembus Swing High) sebelum mitigasi OB, Risk-to-Reward 1:3.0 (Target +Rp 150.000), Auto Break-Even (BE) otomatis saat trade mencapai +1.0R (Risk-Free), hard equity drawdown cap 25%, dan max 1 order per pair (No Averaging / Single Order).
- **Proteksi Anti-Spam Notifikasi:** Fungsi `send_push_notification(title, message, cooldown_seconds=30)` dilengkapi deduplication & 30-second cooldown timer untuk mencegah loop pesan ke Cloudflare Workers:
  `https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification`

### D. Bot Martingale Logic Akun 2 (`mt5_config_prop1/bot.py`)
- Terletak di `/home/cuker/mt5_storage/mt5_config_prop1/bot.py` (tersinkronisasi ke `/config/bot.py` container `propfirm-mt5`).
- **Adaptive Trend Martingale Engine:**
  - **Filter Tren & Entry Trigger:** RSI(14) M15 + EMA(50/200) Pullback.
  - **Averaging Step:** ATR(14) M15 * 1.2x (menyesuaikan volatilitas).
  - **Multiplier:** Progressive 1.5x (Level 1: 0.01, L2: 0.01, L3: 0.02, L4: 0.03, L5: 0.05, L6: 0.08) — jauh lebih aman dari 2.0x konvensional.
  - **Basket Take Profit:** Seluruh posisi dalam keranjang ditutup simultan saat Total Net Profit mencapai target (Rp 20.000 IDR / dinamis).
  - **Circuit Breaker:** Hard Equity Drawdown Cap 25% untuk mengamankan sisa modal.

### E. Cloudflare Worker Push Backend (`cf-push-backend`)
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

---

## 🎯 4. Strategi Pure SMC (5M) & Integrasi Antigravity MCP

### A. Strategi Pure SMC Sniper (Non-Martingale)
* **Timeframe:** 5-Menit (M5) untuk identifikasi *Bullish Order Block (OB)* & *Break of Structure (BOS)* + H1 Trend Filter (EMA-50).
* **Flat Risk Sizing:** Risiko per trade dipatok flat **Rp 50.000** (lot dihitung otomatis dari jarak SL ke bawah OB).
* **Target Risk-to-Reward:** **1:2.0** (+Rp 100.000 saat TP vs -Rp 50.000 saat SL).
* **Auto Break-Even (BE):** Begitu profit menyentuh +1.0R (+Rp 50.000), SL digeser ke titik impas (Entry + Spread) untuk mengunci posisi bebas risiko.
* **Auto News & Spread Filter:** Membekukan entri jika spread XAUUSDm > 60 pips atau jam berita US (NFP/CPI/FOMC).

### B. MT5 MCP Server untuk Antigravity (`agy`)
* **Executable Wrapper:** `/home/cuker/.local/bin/mcp-mt5`
* **Server Script:** `/home/cuker/mt5_storage/mt5_mcp_server.py`
* **Konfigurasi Global:** Terdaftar di `~/.gemini/config/mcp_config.json` di bawah key `"mt5"`.
* **Tools Tersedia:**
  - `mt5_get_account_status`: Saldo, equity, margin, floating PnL real-time.
  - `mt5_get_open_positions`: Melihat tiket posisi aktif, lot, SL, TP, profit berjalan.
  - `mt5_get_smc_analysis`: Meminta AI menganalisis kondisi pasar M5 saat ini (OB, BOS, Discount, Sinyal).
  - `mt5_get_trade_history`: Riwayat transaksi tertutup dan statistik win rate.
  - `mt5_emergency_close_all`: Perintah darurat untuk menutup seluruh posisi trading terbuka sekaligus.

