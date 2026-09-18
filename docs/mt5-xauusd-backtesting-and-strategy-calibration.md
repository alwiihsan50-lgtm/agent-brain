# 📈 Dokumentasi Strategi & Toolkit Backtest XAUUSD M5 (Gold Engine 2026)

Dokumentasi komprehensif mengenai arsitektur strategi, temuan empiris kalibrasi 9 bulan (50.248 bar M5 YTD 2026), perbandingan parameter, dan toolkit CLI `xau-backtest` untuk eksekusi simulasi instan.

---

## 🏆 1. Konfigurasi Bot Terbaik (*The Optimal Golden Stack*)

Setup ini diterapkan pada [`/home/cuker/mt5_storage/mt5_config/bot_trending.py`](file:///home/cuker/mt5_storage/mt5_config/bot_trending.py) dan berjalan live di kontainer `exness-mt5`:

| Layer / Komponen | Parameter Optimal | Rasional & Bukti Backtest |
| :--- | :--- | :--- |
| **Timeframe Dual-Engine** | **H1** (Arah Tren & Kekuatan) + **M5** (Entri & Timing) | H1 membaca arah arus modal institusi; M5 memberi entri presisi dengan SL rapat. |
| **Filter Tren Makro** | **H1 Golden Cross (Opsi 2):**<br>• BUY: `EMA 50 > EMA 200` & `Harga >= EMA 50`<br>• SELL: `EMA 50 < EMA 200` & `Harga < EMA 50` | Memangkas trade lawan arus saat terjadi *crash/pullback* dalam. Mengeliminasi *knife-catching*. |
| **Filter Kekuatan Tren** | **H1 ADX ≥ 20.0** | Mematikan bot saat pasar tidur (*dead drift* / sideways Asia tanpa volume). |
| **Siklus Momentum** | **Gold MACD (16, 38, 9)** pada M5 | Disesuaikan dengan ritme siklus 80–190 menit sesi London & New York, menggantikan MACD default (12, 26, 9) yang terlalu bising. |
| **Trigger Entry** | **Doji Stalemate Compression:**<br>• `MIN_DOJI_RANGE = $0.50`<br>• `MAX_DOJI_BODY_RATIO = 0.30`<br>• `Lookback = 5 candle (range 3-8 live / 2-7 backtest)` | Menangkap kompresi volatilitas sebelum ekspansi harga. Body ratio 30% terbukti paling pas dengan volatilitas intraday Gold. |
| **Stop Loss Boundary** | **SL Dinamis ($1.50 – $4.50)** | Mengikuti ekor Doji + buffer spread + $0.20. Batas bawah $1.50 mencegah *stop hunt*, batas atas $4.50 membatasi risiko saat ada *spike*. |
| **Target Profit** | **R:R Murni 1:3.0 (TANPA BEP)** | **Aturan Paling Krusial:** Menyalakan BEP memotong profit sebesar **-60%**. R:R murni 1:3.0 adalah *mathematical sweet spot* di pasar Gold. |
| **Money Management** | **Flat Risk Rp 20.000 / trade** (~121 USC / ~$1.21 USD) | Lot dinamis: `Lot = Risk / (SL * 100)`. Max DD hanya Rp 300k–340k, sangat aman untuk modal Rp 552k. |
| **Batas Risiko Harian** | **Rem 3x SL Harian (Aktif)** (`MAX_DAILY_CONSEC_LOSSES = 3`) | Membatasi kerugian harian terburuk maksimal **Rp 60.000 / hari** (10.8% modal). |

---

## 📊 2. Rangkuman Temuan Empiris Kunci

### A. Komparasi Target Risk-to-Reward: R:R 1:3.0 vs R:R 1:2.5
* **Target R:R 1:3.0 (Dipilih & Aktif):**
  * Win Rate: **35.8%** | Profit Factor: **1.66**
  * Net Profit: **+45.779 USC (+Rp 7.553.248)**
  * Max Drawdown: **15.1 R (Rp 303.615 / 55.0% modal)**
  * Karakter: Efisiensi matematika tertinggi, pemulihan drawdown lebih cepat.
* **Target R:R 1:2.5 (Alternatif):**
  * Win Rate: **39.0%** | Profit Factor: **1.58**
  * Net Profit: **+41.844 USC (+Rp 6.904.100)** *(Turun -Rp 650rb)*
  * Max Drawdown: **18.6 R (Rp 372.336 / 67.4% modal)**
  * Karakter: Win rate lebih tinggi (+59 trade menang), cocok jika trader menginginkan frekuensi kemenangan lebih sering.

### B. Komparasi Rem SL Harian (Circuit Breaker)
* **Rem 3x SL (Konservatif / Aktif):** Net +Rp 7.55M, Max DD Rp 303k (15.1 R), Max Streak 11 SL, Worst day -Rp 60k.
* **Rem 5x SL (Maksimalis):** Net +Rp 8.63M (+Rp 1.07M), Max DD Rp 341k (17.0 R), Max Streak 14 SL, Worst day -Rp 100k.
* **Tanpa Rem (0x / Unlimited):** Net +Rp 10.95M, Max DD Rp 427k (21.3 R), Max Streak 18 SL, berisiko terbakar >30% modal di hari crash.

### C. Anatomi SL Beruntun (Streak)
* **42.4% SL Streak** terjadi di **Hari Sideways / Choppy / Konsolidasi Sempit** (harga bolak-balik $2–$4 tanpa volume untuk berekspansi ke target 1:3 R).
* **57.6% SL Streak** terjadi di **Hari Reversal / Tren Liar / Whipsaw M5** (misal saat Gold crash -$65, H1 EMA50 masih lagging di atas EMA200, membuat bot mencari BUY di tengah sell-off institusi).
* **70% TP** terjadi di hari **Trending Impulsif Murni** (pergerakan searah tanpa pullback agresif).

---

## ⚡ 3. Toolkit Backtest Cepat (`xau-backtest` / `backtest-gold`)

Toolkit ini berada di `/home/cuker/mt5_storage/mt5_backtest/` dan di-link ke `/home/cuker/.local/bin/`.

### Perintah Utama:
```bash
# 1. Jalankan backtest konfigurasi live aktif (< 200 ms)
xau-backtest live
# atau cukup:
xau-backtest

# 2. Komparasi instan berbagai skenario
xau-backtest compare                  # Rem 3x vs Rem 5x vs Tanpa Rem
xau-backtest compare --daily-sl-sweep # Sapuan Rem 1x s/d Tanpa Rem
xau-backtest compare --rr-sweep       # Sapuan R:R 1.5 s/d 3.5
xau-backtest compare --doji-sweep     # Sapuan toleransi body Doji
xau-backtest compare --custom "3,5"   # Custom list

# 3. Uji parameter kustom
xau-backtest run --rr 3.5 --monthly   # Uji RR 3.5 dengan rincian bulanan
xau-backtest run --daily-sl 5 --chart /path/chart.html # Uji Rem 5x + Plotly HTML
```
