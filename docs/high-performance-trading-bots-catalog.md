# 🏆 KATALOG AUDIT FORENSIK BOT TRADING MT5 (12-PILAR ZERO-BIAS: PROFITABLE VS UNPROFITABLE)

> 🏛️ **Tujuan Dokumen:**
> Dokumen ini adalah catatan kanonikal hasil **Audit Forensik 12-Pilar Zero-Bias Institusional** atas seluruh kandidat bot trading MT5 di workspace ini menggunakan data riil **732.186 candle M1 (25 Bulan: Sep 2024 – Sep 2026)** dan **Data D1 Multi-Pair 6,5 Tahun (2020 – 2026)**.
> Memisahkan secara tegas antara **Bot yang Terbukti Profitable (Bebas Bias)** dan **Bot yang Terbukti Unprofitable / Cacat Metodologi Backtest**.

---

## 🟢 BAGIAN 1: BOT YANG TERBUKTI PROFITABLE (LULUS 12-PILAR ZERO-BIAS & LIVE DI AKUN 1)

| Nama Bot & Strategi | Magic Number | Pair & TF | Sizing (Risk Moderat di Saldo `1.700 USC` / `Rp 279rb`) | Trades | Win Rate & R:R | Profit Factor (Zero-Bias) | Konsistensi Bulanan | Max Drawdown | Status Produksi |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. M5 Doji Breakout + H1 ZLEMA 50/200 + MACD + SMC v5.1** | **`889911`** | `XAUUSDc` (M5) | **Flat `0.02 Lot`**<br>*(Risk Rp 820–1.640/SL, TP Rp 2.460–4.920)* | **1.198** *(25 Bln)* | **WR 29,4%**<br>**R:R `1 : 3.0`** *(1x Win tutup 3x Loss)* | **`1.24`**<br>*(IS: 1.28, OOS: 1.16, 1.5x Spd: 1.16)* | **20 / 25 Bulan Hijau (`80,0%`)** | **`396,6 USC` (`23,3%`)** *(atau `11,7%` di 0.01L)* | 🟢 **LIVE AKUN 1**<br>[`bot_trending.py`](file:///home/cuker/mt5_storage/mt5_config/bot_trending.py) |
| **2. D1 Swing Doji Pullback Reversal (2-Bar Exit Engine)** | **`889933`** | `XAUUSDc`, `USDJPYc` (D1) | **Dinamis `0.01–0.02 Lot`**<br>*(Target Risk Rp 8.500, Max Cap Rp 15.000)* | **190–242** *(6,5 Thn)* | **WR 41,1%–47,9%**<br>**R:R `~1 : 1.35`** | **`1.22 – 1.28`** | **Stabil Tahunan (2020–2026)** | **`463 – 490 USC`** | 🟢 **LIVE AKUN 1**<br>[`bot_daily_doji.py`](file:///home/cuker/mt5_storage/mt5_config/bot_daily_doji.py) |

---

### 🥇 Detail Bot Profitable #1: M5 Doji Breakout + H1 ZLEMA 50/200 + MACD + SMC (`bot_trending.py` v5.1)
* **Lokasi Script Aktif:** [`/home/cuker/mt5_storage/mt5_config/bot_trending.py`](file:///home/cuker/mt5_storage/mt5_config/bot_trending.py) & [`/home/cuker/mt5_storage/mt5_config/strategies/doji_zlema_macd.py`](file:///home/cuker/mt5_storage/mt5_config/strategies/doji_zlema_macd.py)
* **Lokasi Script Audit Zero-Bias:** [`/home/cuker/mt5_storage/mt5_backtest/test_stationary_and_multipair_trending.py`](file:///home/cuker/mt5_storage/mt5_backtest/test_stationary_and_multipair_trending.py)
* **Arsitektur & Keunggulan Kuantitatif:**
  1. **Tanpa Martingale / Tanpa Averaging:** Hanya membuka maksimal 1 posisi (`Single-Shot`) dengan Stop Loss keras (`$2.50 – $5.00` di Gold) dan Take Profit `3.0x SL` (`$7.50 – $15.00`).
  2. **Asymmetric R:R `1 : 3.0`:** Titik impas (*Break-Even Win Rate*) hanya **25,0%**. Cukup **1x Win langsung menutup 3x Loss berturut-turut**.
  3. **Kalibrasi Volatilitas Stasioner (`D1 ATR >= 0.90% dari harga Gold`):** Menggantikan angka dolar statis (`$30/$40`) yang mengalami *price-scale drift* saat emas naik dari `$2.500` (2024) ke `$4.400+` (2026). Dikombinasikan dengan filter `H1 ADX 22.0 – 50.0` dan `Doji Body <= 22%`.
  4. **Lulus Audit 12-Pilar Penuh (Setelah Perbaikan Bug Entry-Bar SL & Ask Spread SELL):**
     * **Net Profit (25 Bulan di `0.02 Lot`):** **`+1.931,8 USC` (`+Rp 317.353 IDR` / `+113,6%` dari modal `1.700 USC`)**.
     * **Max Drawdown (25 Bulan di `0.02 Lot`):** **`396,6 USC` (`Rp 65.150 IDR` / `23,3%` dari modal)** — atau hanya **`11,7%`** pada `0.01 Lot`.
     * **Konsistensi Bulanan:** **20 dari 25 Bulan Hijau (`80,0%`)**, termasuk **12 bulan hijau berturut-turut (Sep 2025 – Agu 2026)**.

### 🥈 Detail Bot Profitable #2: D1 Swing Doji Pullback Reversal (`bot_daily_doji.py`)
* **Lokasi Script Aktif:** [`/home/cuker/mt5_storage/mt5_config/bot_daily_doji.py`](file:///home/cuker/mt5_storage/mt5_config/bot_daily_doji.py)
* **Lokasi Script Audit Zero-Bias:** [`/home/cuker/mt5_storage/mt5_backtest/audit_all_candidates_zero_bias.py`](file:///home/cuker/mt5_storage/mt5_backtest/audit_all_candidates_zero_bias.py)
* **Arsitektur & Perbaikan Produksi:**
  1. **Logika Setup:** Mengambil koreksi *pullback* harian (candle Doji D1 dengan ekor penolakan $\ge 25\%$ dan koridor `RSI 14` di `40–65` untuk Bullish / `35–60` untuk Bearish) searah tren makro `D1 EMA 50 > EMA 200`. Posisi ditutup otomatis setelah **2 candle D1 selesai (`48 Jam`)**.
  2. **Perbaikan Bug Mata Uang `IDC`:** Menambahkan dukungan eksplisit `acc_currency == "IDC"` (`100 IDC = Rp 1 IDR`) pada `calculate_flat_risk_lot()`, `execute_daily_trade()`, dan `format_currency_values()` agar tidak salah dikalikan kurs USD (`16.500x`).
  3. **Kalibrasi Risk Moderat:** Target risiko `FLAT_RISK_IDR = Rp 8.500` (`~51 USC`), batas maksimal `MAX_RISK_IDR = Rp 15.000`, dan *hard cap* volume maksimal `0.02 Lot`.

---

## 🔴 BAGIAN 2: BOT YANG TERBUKTI UNPROFITABLE / GAGAL AUDIT 12-PILAR ZERO-BIAS (DIARSIPKAN)

> ⚠️ **PERINGATAN KERAS (DO NOT DEPLOY):**
> Seluruh bot di bawah ini telah diaudit secara forensik baris demi baris dan terbukti **TIDAK PROFITABLE (Rugi)** atau **Berisiko Margin Call Tinggi** ketika bias simulasi (*Same-Bar TP Fallacy*, pengabaian *Entry-Bar SL*, ketidakcocokan parameter lot/slippage) dibersihkan. Seluruh script telah dipindahkan ke [`/home/cuker/mt5_storage/mt5_config/archived_bots/`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/).

| File Script Terarsip | Nama Bot / Strategi | Hasil Audit Forensik Zero-Bias & Penyebab Kegagalan |
| :--- | :--- | :--- |
| [`bot_grid_cent.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_grid_cent.py) | **Cent Grid Harvester v3.2 / v3.4** (`XAUUSDc` M5 Martingale Grid `1.25x` Max L5) | ❌ **GAGAL AUDIT (PF Riil `1.06`, Bulan Hijau `58,3%`, Max DD Melebihi Saldo):**<br>1. **6 Ketidakcocokan Parameter Backtest Lama:** Backtest lama memakai base lot `0.03` (bukan `0.01`), membebankan exit slippage 3x–8x lebih kecil dari realita, dan filter spread rollover berbeda.<br>2. **R:R Terbalik Ekstrem (`1 : 0.10`):** Rata-rata 1x panen hanya `+2,72 USC` (`Rp 446`), sedangkan 1x Cut Loss menghanguskan `-41,72 s/d -51,78 USC` (**butuh 15–19x Win berturut-turut hanya untuk menutup 1x Loss**).<br>3. **Max Drawdown `1.786 USC`:** Melebihi total modal live Akun 1 (`1.700 USC` / `Rp 279rb`) dan hanya menghasilkan `14/24` bulan hijau (`58,3%` < batas wajib `75%`). |
| [`bot_pullback_sniper.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_pullback_sniper.py) | **M5 Pullback Limit Sniper v1.0** (33.3% Fib Limit + Momentum Bar $\ge \$3.50$) | ❌ **TERBUKTI RUGI / UNPROFITABLE (PF Riil `0.86 – 0.90`, Net `-1.283 USC`):**<br>1. **Bias Fatal *Same-Bar TP Fallacy*:** Backtest lama (`run_audit_current_settings.py` & `sweep_pullback_levels.py`) mengecek `High[fill_m1] >= TP` pada **candle M1 yang sama** tempat harga baru saja turun menyentuh `Buy Limit` (`Low[fill_m1] <= limit_price`), menciptakan ratusan kemenangan fiktif.<br>2. **Distorsi Rumus `tp_rr` & `Trailing BEP`:** Saat diuji ulang dengan *Next-Bar Fill Mandate* (732.186 bar M1), strategi ini **murni merugi** (**PF `0.86`** dengan BEP, WR `23,4%`; **PF `0.90`** tanpa BEP, WR `31,6%`; hanya `8/24` bulan hijau). |
| [`bot.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot.py) | **Dual-Track Hedged Martingale v2.7** | ❌ **MARGIN CALL (`MC`) / PF `< 1.00`:**<br>Tangga martingale `[0.01 .. 0.65]` mengalami Margin Call pada modal `1.700–2.711 USC` ketika tren emas bergerak `> $100` tanpa pullback. Jika tangga dipotong pada L4/L5, Profit Factor jatuh di bawah `1.00`. |
| [`run_trending_bot_backtest.py`](file:///home/cuker/mt5_storage/mt5_backtest/run_trending_bot_backtest.py) | **Pure FVG CE 50% Pullback Engine (M5)** | ❌ **IMPASS / MARGINAL (PF `1.02 – 1.04`, Bulan Hijau `50,0%`):**<br>Hanya menghasilkan 9 dari 18 bulan hijau (`50,0%`) dengan Max Drawdown `60,7%`. Profit tipis habis tergerus spread dan slippage. |
| [`run_forex_h1_sweeps.py`](file:///home/cuker/mt5_storage/mt5_backtest/run_forex_h1_sweeps.py) | **Forex H1 Bollinger Bands + RSI Mean Reversion** | ❌ **GAGAL OUT-OF-SAMPLE (PF OOS `0.65 – 0.92`):**<br>Mengalami *overfitting* pada In-Sample dan gagal menghasilkan profit pada periode Out-of-Sample di 7 dari 8 pasangan mata uang mayor/cross. |
| [`bot_sideways.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_sideways.py) & [`bot_crypto_trending.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_crypto_trending.py) | **Asian Range Sweep & Crypto Trend M5** | ❌ **DRAWDOWN ASIMETRIS & SPREAD DRAG:**<br>Rentan terkena stop-out beruntun saat *expansion breakout* sesi Eropa dan tergerus spread mikro BTCUSD M5. |
