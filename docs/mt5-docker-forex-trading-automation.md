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
  - `exness-mt5` (Akun Utama: `434073017` Exness, KasmVNC Port `3000` / `3001` - **AKTIF / RUNNING: Pure SMC M5 v4.1-HYBRID-SMC**)
  - `propfirm-mt5` (Akun ke-2: `463880423` Exness, KasmVNC Port `3006` / `3007` - **AKTIF / RUNNING: Pure SMC M1 Scalper Experiment**)
- **Volume Persisten:** `./mt5_config` -> `/config` (Akun 1) dan `./mt5_config_prop1` -> `/config` (Akun 2)
- **Environment:** `PUID=1000`, `PGID=1000`, `TZ=Asia/Jakarta`
- **Web UI GUI MT5:**
  - Akun 1 (M5): `https://mt5.abbas.my.id` / `http://localhost:3000`
  - Akun 2 (M1): `http://localhost:3006`

### B. Lingkungan Python di dalam Wine
- **Path Python:** `C:\Program Files (x86)\Python39-32\python.exe` (Wine environment)
- **Modul Kunci:** `MetaTrader5` (v5.0.36), `numpy` (versi `1.26.4` - wajib `numpy<2`)
- **Catatan Penting:** Library `MetaTrader5` merupakan modul C-Extension Windows, sehingga script Python **harus dieksekusi di dalam Wine** container yang sama dengan terminal MT5:
  ```bash
  docker exec --user abc exness-mt5 wine python -u /config/bot.py        # Akun 1
  docker exec --user abc propfirm-mt5 wine python -u /config/bot.py      # Akun 2
  ```

### C. Bot Python Logic Akun 1 - M5 Timeframe (`mt5_config/bot.py`)
- Terletak di `/home/cuker/mt5_storage/mt5_config/bot.py` (tersinkronisasi langsung ke `/config/bot.py` container `exness-mt5`).
- Multi-Pair SMC M5 Engine: XAUUSDm (Gold 1:3.0), EURUSDm (1:2.0), GBPUSDm (1:2.0).
- Auto Break-Even @ +1.0R, H1 EMA-50 Trend Bias, Flat Risk Rp 50.000.
- Service: `mt5-trading-bot.service` (Runner: `/home/cuker/start-bot.sh`).

### D. Bot Python Logic Akun 2 - M1 Timeframe (`mt5_config_prop1/bot.py`)
- Terletak di `/home/cuker/mt5_storage/mt5_config_prop1/bot.py` (tersinkronisasi ke `/config/bot.py` container `propfirm-mt5`).
- **Pure SMC M1 Scalper Engine (Khusus XAUUSDm / Gold Only - Dual-Direction v4.3-M1-GOLD-DUAL):**
  - **Pair:** Khusus `XAUUSDm` (Gold Only).
  - **Arah Trading:** Dual-Direction (BUY & SELL) dengan filter bias HTF M15 EMA-50.
  - **Timeframe Eksekusi:** M1 (1-Menit) untuk fractal swings, BOS, unmitigated Order Blocks (Bullish OB & Bearish OB).
  - **Higher Timeframe Bias:** M15 EMA-50 (15x rasio terhadap M1) untuk menentukan arah Bullish vs Bearish.
  - **Kalibrasi Jarak SL M1 Gold:** Min SL $0.80, Max SL $2.50.
  - **Target Rasio R:R:** 1:3.0 (+Rp 150.000 target profit vs Rp 50.000 max risk).
  - **Spread Buffer Take Profit:**
    - BUY TP: `Ask + (SL_dist * 3.0) - (Spread * 0.5)`
    - SELL TP: `Bid - (SL_dist * 3.0) + Spread` (mengatasi Ask spread gap).
  - **Auto Break-Even (BE @ +1.0R):** Geser SL otomatis ke Entry +/- Spread Buffer saat floating profit mencapai +1.0R (+Rp 50.000).
  - **Flat Risk Sizing:** Tetap flat Rp 50.000 per posisi (lot dihitung dinamis via `order_calc_profit`).
  - **Service Systemd:** `mt5-trading-bot-prop1.service` (Runner: `/home/cuker/start-bot-prop1.sh`).
  - **Audit Logging & Status:** `/config/bot_activity_m1.log`, `/config/bot_trades_m1.csv`, dan `/ram_data/bot_status_prop1.json`.

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

## 🎯 4. Strategi Pure SMC Multi-Pair Dual-Direction (v4.3-DUAL-SPREAD-BUFFER) & Integrasi Antigravity MCP

### A. Strategi Pure SMC Multi-Pair Dual-Direction (BUY & SELL)
* **Timeframe:** 5-Menit (M5) untuk identifikasi *Order Block (OB)* & *Break of Structure (BOS)* dua arah + H1 Trend Filter (EMA-50).
* **Mode Operasional:**
  - **Sinyal BUY:** Terpicu saat harga berada di atas H1 EMA-50 (BULLISH) dan memitigasi *Bullish Order Block* (Demand) setelah terjadi *Bullish BOS*.
  - **Sinyal SELL:** Terpicu saat harga berada di bawah H1 EMA-50 (BEARISH) dan memitigasi *Bearish Order Block* (Supply) setelah terjadi *Bearish BOS*.
* **Spread Buffer Calibration pada Take Profit:**
  - **SELL TP:** `Entry - (SL_dist * RR) + Spread` ➔ Mengangkat titik TP sebesar 1 spread agar harga Ask langsung menyentuh TP saat jarum candlestick (Bid) mencium target.
  - **BUY TP:** `Entry + (SL_dist * RR) - (Spread * 0.5)` ➔ Menurunkan sedikit target TP agar harga Bid mudah melibas TP tanpa terganjal spread.
* **Instrumen Aktif:** `XAUUSDm` (Gold), `EURUSDm`, dan `GBPUSDm` (Exness Raw/Standard).
* **Flat Risk Sizing:** Risiko per trade dipatok flat **Rp 50.000** (lot dihitung dinamis via native broker `mt5.order_calc_profit`).
* **Hybrid Risk-to-Reward (R:R):**
  - **`XAUUSDm` (Gold):** **1:3.0** (+Rp 150.000 saat TP vs -Rp 50.000 saat SL).
  - **`EURUSDm` & `GBPUSDm`:** **1:2.0** (+Rp 100.000 saat TP vs -Rp 50.000 saat SL).
* **Batas Toleransi SL Teknikal:**
  - `XAUUSDm`: 1.50 – 3.50 ($1.50 - $3.50).
  - `EURUSDm`: 3 – 12 pips (0.0003 – 0.0012).
  - `GBPUSDm`: 4 – 15 pips (0.0004 – 0.0015).
* **Auto Break-Even (BE @ +1.0R):** Begitu profit menyentuh +1.0R (+Rp 50.000), SL digeser otomatis ke titik impas (Entry +/- Spread Buffer) untuk mengunci posisi bebas risiko pada BUY maupun SELL.
* **Auto News & Spread Filter:** Membekukan entri saat spread melebar atau pada jendela rilis berita US (12:25-13:15 UTC & 14:00-14:45 UTC) dan Market Rollover (20:50-22:10 UTC).

### B. MT5 MCP Server untuk Antigravity (`agy`)
* **Executable Wrapper:** `/home/cuker/.local/bin/mcp-mt5`
* **Server Script:** `/home/cuker/mt5_storage/mt5_mcp_server.py`
* **Konfigurasi Global:** Terdaftar di `~/.gemini/config/mcp_config.json` di bawah key `"mt5"`.
* **Tools Tersedia:**
  - `mt5_get_account_status`: Saldo, equity, margin, floating PnL real-time.
  - `mt5_get_open_positions`: Melihat tiket posisi aktif, lot, SL, TP, profit berjalan.
  - `mt5_get_smc_analysis`: Meminta AI menganalisis kondisi pasar M5 saat ini (OB, BOS, Trend H1, Sinyal).
  - `mt5_get_trade_history`: Riwayat transaksi tertutup dan statistik win rate.
  - `mt5_emergency_close_all`: Perintah darurat untuk menutup seluruh posisi trading terbuka sekaligus.

---

## 📈 5. Hasil Validasi Backtesting Penuh YTD 2026: BUY-ONLY vs DUAL-DIRECTION (BUY & SELL)

Pengujian komprehensif dijalankan menggunakan **153.536 bar data M5 riil Exness** dari 1 Januari s/d 11 September 2026:

| Metrik Kinerja | 🟡 BUY-ONLY (Versi Lama) | 🟢 DUAL-DIRECTION (BUY & SELL v4.2) |
| :--- | :--- | :--- |
| **Periode Data** | 1 Januari 2026 – 11 September 2026 | 1 Januari 2026 – 11 September 2026 |
| **Total Trade Dieksekusi** | 835 Trade | **1.708 Trade** |
| **Menang Penuh (Win / TP)** | 460 Trade (55.1%) | **963 Trade (56.4%)** |
| **Impas (Break-Even @ 1R)** | 186 Trade (22.3%) | **417 Trade (24.4%)** |
| **Kalah (Loss / SL)** | 189 Trade (22.6%) | **328 Trade (19.2%)** |
| **Tingkat Bebas Rugi (Win + BE)**| 77.4% | **80.8%** |
| **Profit Factor (PF)** | 5.87 | **7.06** |
| **Profit dari Posisi BUY** | +Rp 40.510.783 | **+Rp 40.510.783** |
| **Profit dari Posisi SELL** | Rp 0 | **+Rp 47.191.862** |
| **Profit Bersih (Net Profit)** | **+Rp 40.510.783 (+8.102% ROI)** | **+Rp 87.702.645 (+17.540% ROI)** |
| **Kontribusi per Pair (Dual)** | - | Gold: +Rp 50.4M (PF 7.37) \| EUR/USD: +Rp 18.9M (PF 6.26) \| GBP/USD: +Rp 18.3M (PF 7.55) |
| **Laporan Visual Interaktif** | [`ytd_2026_backtest_report.html`](file:///media/cuker/Data/Projects/trading-backtest/ytd_2026_backtest_report.html) | [`dual_direction_smc_report.html`](file:///media/cuker/Data/Projects/trading-backtest/dual_direction_smc_report.html) |

---

## 📝 6. Sistem Audit Logging & Monitoring Real-Time

Bot dilengkapi sistem pencatatan persisten berlapis untuk debugging dan monitoring jangka panjang:

1. **Log Aktivitas Persisten (`/config/bot_activity.log`):**
   * Lokasi di Host: `/home/cuker/mt5_storage/mt5_config/bot_activity.log`
   * Format: `[YYYY-MM-DD HH:MM:SS] [LEVEL] <Pesan>` dengan immediate auto-flush ke disk.
   * Auto-rotation otomatis saat ukuran file melebihi 20 MB.
2. **Jurnal Transaksi CSV (`/config/bot_trades.csv`):**
   * Lokasi di Host: `/home/cuker/mt5_storage/mt5_config/bot_trades.csv`
   * Mencatat setiap lifecycle order: `OPEN`, `AUTO_BE`, `CLOSE`, `REJECT`, dan `CIRCUIT_BREAKER`.
3. **Pelacakan Penutupan Deal & Push Notification:**
   * Mendeteksi deal penutupan secara real-time via `mt5.history_deals_get()`.
   * Otomatis mengklasifikasikan hasil (`🎯 TP`, `🛑 SL`, `🛡️ BE`) dan memicu Web Push Notification ke iPhone.
4. **Heartbeat Bersih (Bebas Binary Blob Systemd):**
   * Menghilangkan karakter `\r` stdout agar tidak terbaca sebagai `[blob data]` oleh `journald`.
   * Heartbeat status bersih dicatat setiap 60 detik (Saldo, Equity, Posisi Aktif, Status Scan Pair).
   * Perubahan status sinyal dicatat seketika saat terdeteksi.
5. **Telemetri RAM Dashboard (Port 3000):**
   * Streaming RAM tmpfs pada `/ram_data/bot_status.json` tetap berjalan setiap 4 detik untuk Web Dashboard ultra-cepat tanpa disk wear.

---

## 🖥️ 7. Analisis Spesifikasi Cloud / VPS untuk Deployment Mandiri

Berdasarkan audit telemetri riil container `exness-mt5` (Wine 64-bit, MetaTrader 5, Python bot runtime, dan KasmVNC Web GUI):

| Komponen | Konsumsi Riil Sistem | Kebutuhan Minimum VPS | Analisis Paket Rendah (1 vCPU / 1 GB RAM / 10 GB SSD) |
| :--- | :--- | :--- | :--- |
| **Penyimpanan (SSD)** | **~13 – 15 GB** (OS ~3GB, Docker Image `mt5:latest` ~6.7GB, `/config` volume ~3.9GB) | **20 GB – 25 GB SSD** | ❌ **10 GB SSD Pasti Gagal (`Disk Full`)** saat ekstraksi layer docker atau pull image. |
| **Memori (RAM)** | **~840 MB Idle** (`exness-mt5` ~637 MB + OS ~200 MB) | **2 GB RAM** (+ Swap 2 GB) | ⚠️ **1 GB RAM Sangat Berisiko OOM Killer** saat lonjakan tick pasar padat atau pembukaan Web VNC. |
| **Processor (CPU)** | **~5% – 10%** saat scanning M5 rutin | **1 Core – 2 Cores** | 🟡 **1 vCPU Cukup**, tetapi akan spike 100% saat initial chart sync / Wine boot. |

**Rekomendasi Paket VPS Ekonomis Terbaik:**
- **Spesifikasi Standar:** 1–2 vCPU, 2 GB RAM (+ 2 GB Swap File), 25–30 GB NVMe/SSD.
- **Provider Acuan (~$3 – $4/bulan):** Hetzner Cloud (CX22), Contabo (Cloud VPS 1), atau DigitalOcean / Vultr.


