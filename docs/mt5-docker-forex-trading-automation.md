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
  - `exness-mt5` (Akun Utama: `263301611` Exness-MT5Real37 Cent USC, KasmVNC Port `3000` / `3001` - **AKTIF / RUNNING: Pure SMC Solo Gold v5.2-PURE-RR3 (XAUUSDc)**)
  - `propfirm-mt5` (Akun ke-2: `463880423` Exness, KasmVNC Port `3006` / `3007` - **STANDBY / OFF**: Dinonaktifkan sementara)
- **Volume Persisten:** `./mt5_config` -> `/config` (Akun 1) dan `./mt5_config_prop1` -> `/config` (Akun 2)
- **Environment:** `PUID=1000`, `PGID=1000`, `TZ=Asia/Jakarta`
- **Web UI GUI MT5:**
  - Akun 1 (M5 Cent): `https://mt5.abbas.my.id` / `http://localhost:3000`
  - Akun 2 (M1): `http://localhost:3006`

### B. Lingkungan Python di dalam Wine
- **Path Python:** `C:\Program Files (x86)\Python39-32\python.exe` (Wine environment)
- **Modul Kunci:** `MetaTrader5` (v5.0.36), `numpy` (versi `1.26.4` - wajib `numpy<2`)
- **Catatan Penting:** Library `MetaTrader5` merupakan modul C-Extension Windows, sehingga script Python **harus dieksekusi di dalam Wine** container yang sama dengan terminal MT5:
  ```bash
  docker exec --user abc exness-mt5 wine python -u /config/bot.py        # Akun 1
  docker exec --user abc propfirm-mt5 wine python -u /config/bot.py      # Akun 2
  ```

### C. Bot Python Logic Akun 1 - Modular Dual-Bot (`mt5_config/`)
- **Arsitektur Modular (Option 1):** Satu terminal MT5 menjalankan 2 bot independen dengan `magic_number` berbeda:
  1. **`bot_trending.py` (Magic `889911`):**
     - Strategi: Pure SMC M5 (BOS + FVG/OB unmitigated + H1 EMA-50 trend alignment).
     - Filter Rejim: ADX(14) M15 >= 18 (hanya aktif saat ada momentum tren sehat).
     - Target: R:R Strict 1:3.0 (+Rp 150.000 vs -Rp 50.000).
     - Log & Telemetri: `/config/bot_trending.log` & `/ram_data/bot_status_trending.json`.
  2. **`bot_sideways.py` (Magic `889922`):**
     - Strategi: Asian Range Liquidity Sweep / Turtle Soup (Fakeout Reversal).
     - Filter Rejim: ADX(14) M15 <= 25 & Box Range $3.00 - $18.00 (mencegah false sweep saat trending).
     - Setup: Sweep wick di luar box range + rejection candle >= 35% masuk kembali ke dalam range.
     - Target: R:R Strict 1:2.0 (+Rp 100.000 vs -Rp 50.000).
     - Log & Telemetri: `/config/bot_sideways.log` & `/ram_data/bot_status_sideways.json`.
  3. **`bot_supervisor.py` (Process Manager & Aggregator):**
     - Mengawasi lifecycle kedua bot (auto-restart jika salah satu crash).
     - Menggabungkan telemetri kedua bot ke `/ram_data/bot_status.json` dan `/config/bot_status.json`.
- **Sizing:** Dinamis Flat Risk Rp 50.000 per posisi (~303 USC pada Cent account / Rp 50.000 Standard).
- **Service:** `mt5-trading-bot.service` (Runner: `/home/cuker/start-bot.sh`).
- **CLI Helper:** `bot-control` (`status`, `logs`, `restart`, `test`).

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

## 🎯 4. Strategi Pure SMC Solo Gold Dual-Direction (v4.5-SOLO-GOLD-OPTIMIZED) & Integrasi Antigravity MCP

### A. Strategi Pure SMC Solo Gold Focus (BUY & SELL)
* **Timeframe:** 5-Menit (M5) untuk identifikasi *Order Block (OB)* & *Break of Structure (BOS)* dua arah + H1 Trend Filter (EMA-50).
* **Multi-OB Lookback & Front-Running Touch Buffer Engine (v4.5):**
  - Lookback aktif 60 candle M5 (5 jam riil pasar) unmitigated.
  - **Front-Running Touch Buffer:** Toleransi mitigasi `0.5 * spread` (~$0.12 - $0.15) di bibir Order Block agar entri terpicu presisi saat likuiditas institusional berbalik tipis.
  - Telemetri live `setup_reason` menampilkan zona Supply/Demand terdekat beserta jarak poin real-time (contoh: `Nearest Supply: 4286.496 (+0.345)`).
* **Mode Operasional:**
  - **Sinyal BUY:** Terpicu saat harga berada di atas H1 EMA-50 (BULLISH) dan memitigasi *Bullish Demand OB* setelah terjadi *Bullish BOS*.
  - **Sinyal SELL:** Terpicu saat harga berada di bawah H1 EMA-50 (BEARISH) dan memitigasi *Bearish Supply OB* setelah terjadi *Bearish BOS*.
* **Spread Buffer Calibration pada Take Profit:**
  - **SELL TP:** `Entry - (SL_dist * RR) + Spread` ➔ Mengangkat titik TP sebesar 1 spread agar harga Ask langsung menyentuh TP saat jarum candlestick (Bid) mencium target.
  - **BUY TP:** `Entry + (SL_dist * RR) - (Spread * 0.5)` ➔ Menurunkan sedikit target TP agar harga Bid mudah melibas TP tanpa terganjal spread.
* **Instrumen Aktif:** `XAUUSDm` (Gold Solo Focus) pada Akun 1.
* **Flat Risk Sizing:** Risiko per trade dipatok flat **Rp 50.000** (lot dihitung dinamis via native broker `mt5.order_calc_profit`).
* **Strict Risk-to-Reward (R:R):** **1:3.0** (+Rp 150.000 saat TP vs -Rp 50.000 saat SL).
* **Batas Toleransi SL Teknikal:** $1.50 – $3.50 (15 s/d 35 pips).
* **Auto Break-Even (BE @ +1.0R):** Begitu profit menyentuh +1.0R (+Rp 50.000), SL digeser otomatis ke titik impas (Entry +/- Spread Buffer) untuk mengunci posisi bebas risiko pada BUY maupun SELL.
* **Auto News & Spread Filter:** Membekukan entri saat spread melebar (> $0.60) atau pada jendela rilis berita US (12:25-13:15 UTC & 14:00-14:45 UTC) dan Market Rollover (20:50-22:10 UTC).

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

## 📈 5. Hasil Validasi Backtesting: Konfigurasi Bot Live (v4.8 Max SL Clamp Rp 100k)

Pengujian komprehensif dijalankan menggunakan **49.453 bar data M5 riil Exness Gold** (Full YTD) dan divalidasi silang menggunakan **100.000 candle resolusi M1 intra-bar riil**:

| Metrik Kinerja | 🟡 v4.6 (Cap SL $2.85 / Max Rp 50rb) | 🔴 v4.7 Proper SL (Uncapped / Max $10) | 🟢 v4.8 MAX SL CLAMP RP 100K LIVE ($5.68) |
| :--- | :--- | :--- | :--- |
| **Metode & Eksekusi** | Intrabar Worst-Case + Rejection Filter | Proper Structural SL + Rejection Filter | **Proper SL + Clamp Max $5.68 + Rejection Filter** |
| **Resolusi Validasi M1** | 100.000 Candle M1 Intra-Bar | 100.000 Candle M1 Intra-Bar | **100.000 Candle M1 Intra-Bar (3.5 Bulan)** |
| **Total Trade (M1 Resolusi)**| 103 Trade | 210 Trade | **210 Trade** |
| **Menang Penuh (Win / TP 1:3)**| 67 Trade (65.0%) | 133 Trade (63.3%) | **135 Trade (64.3%)** 🚀 |
| **Impas (Break-Even / BEP)** | 0 Trade (0.0%) | 0 Trade (0.0%) | **0 Trade (0.0%)** 🚫 *(Murni R:R 1:3)* |
| **Kalah (Loss / SL)** | 36 Trade (35.0%) | 77 Trade (36.7%) | **75 Trade (35.7%)** |
| **Profit Factor (PF)** | 5.03 | 5.22 | **5.27** 🏆 |
| **Profit Bersih (Net Profit)** | +Rp 5.860.584 | +Rp 18.494.812 | **+Rp 18.250.395 (+211% dibanding v4.6)** 💰 |
| **Max Drawdown Terburuk** | Rp 203.619 | Rp 352.513 | **Rp 352.513** |
| **Kerugian Terburuk 1 Trade** | **Rp 51.226** ($2.81) | Rp 113.776 ($6.37) ⚠️ | **Rp 101.759** ($5.69) 🛡️ *(Strictly capped)* |
| **Rata-rata Kerugian SL** | Rp 40.445 | Rp 56.857 | **Rp 56.940** |
| **Laporan Visual Interaktif** | [`ytd_bep_vs_no_bep_report.html`](file:///media/cuker/Data/Projects/trading-backtest/ytd_bep_vs_no_bep_report.html) | [`proper_sl_fixed_lot_report.html`](file:///media/cuker/Data/Projects/trading-backtest/proper_sl_fixed_lot_report.html) | [`m5_analysis_m1_execution_report.html`](file:///media/cuker/Data/Projects/trading-backtest/m5_analysis_m1_execution_report.html) |

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

---

## 🔬 8. Audit Validasi Backtest YTD 2026 & Evolusi ke v5.2 Pure R:R

Pada 17 September 2026, dilakukan evaluasi kritis menyeluruh terhadap klaim backtest historis (+Rp 14.25M) vs pengujian riil YTD 2026 menggunakan dataset 50.247 bar M5 XAUUSDc (1 Jan s/d 16 Sep 2026).

### A. Temuan Bias Metodologis Backtest Lama
1. **Bias Periode (Cherry-Picked):** Data 100k M1 lama hanya mencakup Juni–September 2026 (fase trending naik kencang). Melewatkan Januari 2026 yang choppy dan menyumbang drawdown terbesar.
2. **Lookahead Leak pada Resampling H1:** Resampling Pandas `1h` membocorkan penutupan jam ke bar menit awal melalui default left-edge indexing.
3. **M1 vs M5 Rejection:** Konfirmasi rejection dievaluasi di candle 1 menit (terpicu 210x), sedangkan bot live menunggu candle 5 menit (hanya 76 trade riil).

### B. Komparasi 4 Model Proteksi Modal (50k Bar M5 YTD 2026)
| Variant | Konfigurasi | Net Profit | PF | Win Rate | Keterangan |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **v5.1 (Two-Stage)** | Lock +0.3R @ +1.5R | -Rp 206.327 | 0.88 | 46.1% | ❌ Guard memotong 77% pemenang di +0.3R (Rp 15rb) vs SL penuh (-Rp 50rb). |
| **Variant A** | Lock +1.0R @ +1.5R | -Rp 25.005 | 0.99 | 46.1% | ⚪ Breakeven marginal. |
| **v5.2 (Pure R:R)** | **Murni 1:3 (Tanpa Guard)** | **+Rp 383.726** | **1.14** | **28.0%** | 🏆 **PEMENANG**: 21 trade menyentuh full TP (+Rp 150rb). Asymmetric reward 3:1. |
| **Variant D** | Murni 1:2 (Tanpa Guard) | +Rp 222.111 | 1.09 | 36.0% | ✅ Profit positif tapi net lebih rendah dari 1:3. |

### C. Konfigurasi Aktif Live (v5.2-PURE-RR3)
- **Engine:** `STAGE1_TRIGGER_RR = 0.0`, `STAGE2_TRIGGER_RR = 0.0`, `AUTO_BE_TRIGGER_RR = 0.0`.
- **Target R:R:** Strict 1:3.0 (+Rp 150.000 vs Flat Risk Rp 50.000).
- **Akun:** Exness Cent `263301611` (`XAUUSDc`) / Demo USD `463978832` (`XAUUSDm`).

### D. Validasi Backtest Dual-Bot Modular (Trending SMC + Sideways Sweep YTD 2026)
Pengujian komprehensif pada dataset riil 50.248 bar M5 (1 Jan - 16 Sep 2026) dengan flat risk $3.03 USD (~Rp 50.000) per trade:
- **Laporan Visual Interaktif:** [`dual_modular_gold_backtest_report.html`](file:///media/cuker/Data/Projects/trading-backtest/dual_modular_gold_backtest_report.html)
- **Script Backtest:** [`backtest_dual_modular_gold.py`](file:///media/cuker/Data/Projects/trading-backtest/backtest_dual_modular_gold.py)

| Strategi / Modul | Target R:R | Total Trade | Win Rate | Net Profit (USD) | Net Profit (IDR) | Profit Factor | Max Drawdown |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Module 1: Trending SMC** | 1:3.0 | 1,533 | 31.7% | +$347.41 | +Rp 5,732,232 | 1.07 | -$236.37 (~Rp 3.9M) |
| **Module 2: Sideways Sweep** | 1:2.0 | 390 | **37.2%** | +$77.21 | +Rp 1,273,948 | **1.09** | **-$77.38** (~Rp 1.2M) |
| **Combined Portfolio** | **Hybrid** | **1,923** | **32.8%** | **+$424.62** | **+Rp 7,006,180** | **1.07** | **-$254.84** (~Rp 4.2M) |

**Temuan Kunci Sinergi Dual-Regime:**
1. **Stabilizer Alami:** Pada bulan-bulan di mana pasar emas berkonsolidasi dan tren gagal berlanjut (Februari +$18, Juni +$50, Agustus +$43), Bot Sideways menghasilkan profit positif yang menambal penurunan (*cushioning drawdown*) Bot Trending.
2. **Booster Pertumbuhan:** Saat emas mengalami fase trending kuat (April +$176, Mei +$58, September +$117), Bot Trending menjadi mesin pencetak profit utama dengan asymmetric R:R 1:3.0.
3. **Proyeksi pada Saldo $2,822 USD:** Akumulasi profit +$424.62 USD setara dengan **+15.0% return** dalam 8.5 bulan, dengan maximum drawdown portofolio hanya **9.0%** (-$254 USD).

### E. Integrasi Filosofi Candle Doji (Indecision Equilibrium & Reversal Confirmation Engine)

Berdasarkan saran USER untuk meningkatkan performa Profit Factor dan Win Rate sistem Dual-Bot, dilakukan riset dan implementasi matematis **Filosofi Candlestick Doji (Munehisa Homma / Steve Nison)**:

1. **Prinsip Dasar & Logika Pasar:**
   * **Doji Stalemate (Ekuilibrium / Kehabisan Momentum):** Sebuah candle dengan rasio badan tipis (`abs(Close - Open) / (High - Low) <= 0.25`) merepresentasikan keraguan dan kehabisan tenaga dorongan agresif lawan saat harga masuk ke Order Block / Range Boundary.
   * **Prinsip Konfirmasi Reversal (Breakout Confirmation):** Doji adalah netral. Pembukaan posisi HANYA sah jika bar berikutnya ditutup membuktikan kemenangan salah satu pihak:
     * *BUY*: Bar tertutup bullish (`Close > Open`) dan menembus ke atas *High* dari Doji (`Close > Doji_High`).
     * *SELL*: Bar tertutup bearish (`Close < Open`) dan menembus ke bawah *Low* dari Doji (`Close < Doji_Low`).
   * *Sideways Sweep*: Serapan likuiditas ekstrem diakomodasi via **Dragonfly Doji** pada Range Low (`lower_wick >= 50%`, `body <= 20%`) dan **Gravestone Doji** pada Range High (`upper_wick >= 50%`, `body <= 20%`).

2. **Perbandingan Komparatif Backtest (50.248 Bar M5 YTD 2026, Akun $2,822 USD):**

| Metrik Kinerja | Baseline (Sebelum Doji) | Doji Philosophy Enhanced | Peningkatan / Koreksi |
| :--- | :---: | :---: | :--- |
| **Total Trades** | 1,923 trades | 1,705 trades | -218 false trades tereliminasi |
| **Win Rate** | 32.8% | **35.5%** | **+2.7%** |
| **Trending Net Profit** | +$347.41 USD | **+$1,168.10 USD** | **+236%** (Naik 3.3x lipat) |
| **Trending Profit Factor** | 1.07 | **1.30** | **+0.23** |
| **Sideways Net Profit** | +$77.21 USD | **+$98.17 USD** | **+27%** |
| **Combined Net Profit (USD)** | +$424.62 USD | **+$1,266.27 USD** | **+198.2%** (+Rp 13.88 Juta) |
| **Combined Net Profit (IDR)** | +Rp 7.006.180 | **+Rp 20.893.504** | **+Rp 20.89 Juta** (+44.9% Return) |
| **Combined Profit Factor** | 1.07 | **1.26** | **+0.19** |
| **Max Portfolio Drawdown** | -$254.84 USD (~9.0%) | **-$100.22 USD (~3.5%)** | **-60.7%** (Drawdown terpangkas 61%) |

3. **Konsistensi Bulanan Portofolio Doji Enhanced (YTD 2026):**
   * **8 dari 9 Bulan Profit Konsisten:** Jan (+$78), Mar (+$189), Apr (+$181), Mei (+$96), Jun (+$229), Jul (+$187), Agu (+$178), Sep (+$171).
   * **Hanya 1 Bulan Drawdown Ringan:** Feb (-$42 USD / -Rp 700rb).
   * **Laporan HTML Interaktif:** Disajikan lengkap di [`dual_modular_gold_backtest_report.html`](file:///media/cuker/Data/Projects/trading-backtest/dual_modular_gold_backtest_report.html).




