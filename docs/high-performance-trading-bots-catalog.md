# 🏆 KATALOG AUDIT FORENSIK BOT TRADING MT5 (12-PILAR ZERO-BIAS: PROFITABLE VS UNPROFITABLE)

> 🏛️ **Tujuan Dokumen:**
> Dokumen ini adalah catatan kanonikal hasil **Audit Forensik 12-Pilar Zero-Bias Institusional** atas seluruh kandidat bot trading MT5 di workspace ini menggunakan data riil **732.186 candle M1 (25 Bulan: Sep 2024 – Sep 2026)** dan **Data D1 Multi-Pair 6,5 Tahun (2020 – 2026)**.
> Memisahkan secara tegas antara **Bot yang Terbukti Profitable (Bebas Bias)** dan **Bot yang Terbukti Unprofitable / Cacat Metodologi Backtest**.

---

## 🟢 BAGIAN 1: BOT YANG TERBUKTI PROFITABLE (LULUS 12-PILAR ZERO-BIAS & LIVE DI AKUN 1)

| Nama Bot & Strategi | Magic Number | Pair & TF | Sizing (Risk Moderat di Saldo `1.700 USC` / `Rp 279rb`) | Trades | Win Rate & R:R | Profit Factor (Zero-Bias) | Konsistensi Bulanan | Max Drawdown | Status Produksi |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. M5 Dual-Pair Doji + H1/M5 ZLEMA 50 + MACD + SMC + Stationary ATR 1.8x v6.1** | **`889911`** | `XAUUSDc` (`0.01L`) + `USTECc` (`0.20L`) (M5) | **`0.01L` XAU (`R:R 1:2.0`, M5-ZL50) + `0.20L` USTEC (`R:R 1:1.75`, M5-Trend)** | **1.368** *(719 XAU + 649 USTEC)* | **WR 42,9% (OOS 44,3%)**<br>*(XAU 39,9% / USTEC 46,2%)* | **`1.40`**<br>*(IS: 1.40, OOS: 1.40, XAU: 1.38, USTEC: 1.42)* | **24 / 26 Bulan Hijau (`92,3%`)**<br>*(Sharpe `3.91`, Sortino `11.40`)* | **`186,6 USC` (`11,0%`)**<br>*(Ret/DD `18,08x`)* | 🟢 **LIVE AKUN 1**<br>[`bot_trending.py`](file:///home/cuker/mt5_storage/mt5_config/bot_trending.py) |

---

### 🥇 Detail Bot Profitable Tunggal: M5 Dual-Pair Doji + H1/M5 ZLEMA 50 + MACD + SMC + Stationary ATR 1.8x (`bot_trending.py` v6.1)
* **Lokasi Script Aktif:** [`/home/cuker/mt5_storage/mt5_config/bot_trending.py`](file:///home/cuker/mt5_storage/mt5_config/bot_trending.py) & [`/home/cuker/mt5_storage/mt5_config/strategies/doji_zlema_macd.py`](file:///home/cuker/mt5_storage/mt5_config/strategies/doji_zlema_macd.py)
* **Lokasi Script Audit Zero-Bias:** [`/home/cuker/mt5_storage/mt5_backtest/sweep_rr_1_0_to_2_0_champions.py`](file:///home/cuker/mt5_storage/mt5_backtest/sweep_rr_1_0_to_2_0_champions.py) & [`/home/cuker/mt5_storage/mt5_backtest/audit_full_account1_portfolio.py`](file:///home/cuker/mt5_storage/mt5_backtest/audit_full_account1_portfolio.py)
* **Arsitektur & Keunggulan Kuantitatif:**
  1. **Tanpa Martingale / Tanpa Averaging (`Single-Shot` per Pair):** Maksimal 1 posisi pada `XAUUSDc` (`0.01 Lot`, `R:R 1:2.0`) dan 1 posisi pada `USTECc` (`0.20 Lot`, `R:R 1:1.75`) dengan tracker rem harian independen (`Maks 3x SL beruntun/hari` + `Cooldown 15 Menit`).
  2. **Stationary Hybrid-ATR `1.8x` SL/TP + Filter `M5 ZLEMA 50`:**
     * **`XAUUSDc` (`R:R 1:2.0`, `use_m5_zlema_align: True`):** `SL = max(Structural_SL, 1.8x M5_ATR14)` dengan *stationary clamp* `0.12%–0.35%` dari harga Emas + wajib searah `M5 ZLEMA 50` (`PF 1.38`, `WR 39,9%`, `21/25` Bulan Hijau `84,0%`, Net `+1.500,8 USC`).
     * **`USTECc` (`R:R 1:1.75`, `use_m5_trend_align: True`):** `SL = 1.8x M5_ATR14` (`40–160 index pts`) + wajib searah `M5 ZLEMA 50 & EMA 50 > EMA 200` (`PF 1.42`, `IS: 1.49`, `OOS: 1.29`, `WR 46,2%`, `14/17` Bulan Hijau `82,4%`, Net `+1.873,5 USC`).
  3. **Sinergi Portofolio Gabungan v6.1 (1.368 Transaksi Zero-Bias):**
     * **Combined Profit Factor:** **`1.40`** (`IS: 1.40`, `OOS: 1.40` — 0% Overfitting!).
     * **Net Profit Gabungan:** **`+3.374,3 USC` (`+Rp 554.321 IDR` / `+198,5%` dari modal `1.700 USC`)**.
     * **Max Drawdown Gabungan:** Hanya **`186,6 USC` (`Rp 30.654 IDR` / `11,0%` dari modal)** — **Return/MaxDD Ratio `18,08x`**, **Annualized Sharpe `3.91`**, **Sortino `11.40`**, dan **`24 dari 26` Bulan Hijau (`92,3%`)**.

---

## 🔴 BAGIAN 2: BOT YANG TERBUKTI UNPROFITABLE / GAGAL AUDIT 12-PILAR ZERO-BIAS (DIARSIPKAN)

> ⚠️ **PERINGATAN KERAS (DO NOT DEPLOY):**
> Seluruh bot di bawah ini telah diaudit secara forensik baris demi baris dan terbukti **TIDAK PROFITABLE (Rugi)** pada rezim 2024–2026 atau **Berisiko Margin Call Tinggi** ketika bias simulasi (*Same-Bar TP Fallacy*, pengabaian *Entry-Bar SL*, beban *Overnight Swap*, ketidakcocokan parameter lot/slippage) dibersihkan. Seluruh script telah dipindahkan ke [`/home/cuker/mt5_storage/mt5_config/archived_bots/`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/).

| File Script Terarsip | Nama Bot / Strategi | Hasil Audit Forensik Zero-Bias & Penyebab Kegagalan |
| :--- | :--- | :--- |
| [`bot_daily_doji.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_daily_doji.py) | **D1 Swing Doji Pullback Reversal (2-Bar Exit Engine)** (`XAUUSDc` + `USDJPYc`, Magic `889933`) | ❌ **RUGI PADA REZIM 2024–2026 (PF `0.97`, Net `-27,3 USC`) & MENGGANGGU PORTOFOLIO M5:**<br>1. **Swap Drag Menginap 2 Malam (`48 Jam`):** Biaya inap 2 malam (`-0,80 s/d -1,60 USC/trade`) memakan profit tipis pada rezim 2024–2026 (`XAU D1 PF 0.99`, `JPY D1 PF 0.96`).<br>2. **Ketimpangan Risiko (`Risk Mismatch`):** 1x SL D1 mencapai `-50 s/d -85 USC` (`5x–8x` lebih besar dari SL M5 `8–12 USC`), sehingga saat digabung dengan M5 menurunkan bulan hijau dari `92,3% (24/26)` menjadi `73,1% (19/26)` dan memperbesar Max DD dari `11,0%` ke `14,9%`. |
| [`bot_grid_cent.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_grid_cent.py) | **Cent Grid Harvester v3.2 / v3.4** (`XAUUSDc` M5 Martingale Grid `1.25x` Max L5) | ❌ **GAGAL AUDIT (PF Riil `1.06`, Bulan Hijau `58,3%`, Max DD Melebihi Saldo):**<br>1. **6 Ketidakcocokan Parameter Backtest Lama:** Backtest lama memakai base lot `0.03` (bukan `0.01`), membebankan exit slippage 3x–8x lebih kecil dari realita, dan filter spread rollover berbeda.<br>2. **R:R Terbalik Ekstrem (`1 : 0.10`):** Rata-rata 1x panen hanya `+2,72 USC` (`Rp 446`), sedangkan 1x Cut Loss menghanguskan `-41,72 s/d -51,78 USC` (**butuh 15–19x Win berturut-turut hanya untuk menutup 1x Loss**).<br>3. **Max Drawdown `1.786 USC`:** Melebihi total modal live Akun 1 (`1.700 USC` / `Rp 279rb`) dan hanya menghasilkan `14/24` bulan hijau (`58,3%` < batas wajib `75%`). |
| [`bot_pullback_sniper.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_pullback_sniper.py) | **M5 Pullback Limit Sniper v1.0** (33.3% Fib Limit + Momentum Bar $\ge \$3.50$) | ❌ **TERBUKTI RUGI / UNPROFITABLE (PF Riil `0.86 – 0.90`, Net `-1.283 USC`):**<br>1. **Bias Fatal *Same-Bar TP Fallacy*:** Backtest lama (`run_audit_current_settings.py` & `sweep_pullback_levels.py`) mengecek `High[fill_m1] >= TP` pada **candle M1 yang sama** tempat harga baru saja turun menyentuh `Buy Limit` (`Low[fill_m1] <= limit_price`), menciptakan ratusan kemenangan fiktif.<br>2. **Distorsi Rumus `tp_rr` & `Trailing BEP`:** Saat diuji ulang dengan *Next-Bar Fill Mandate* (732.186 bar M1), strategi ini **murni merugi** (**PF `0.86`** dengan BEP, WR `23,4%`; **PF `0.90`** tanpa BEP, WR `31,6%`; hanya `8/24` bulan hijau). |
| [`bot.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot.py) | **Dual-Track Hedged Martingale v2.7** | ❌ **MARGIN CALL (`MC`) / PF `< 1.00`:**<br>Tangga martingale `[0.01 .. 0.65]` mengalami Margin Call pada modal `1.700–2.711 USC` ketika tren emas bergerak `> $100` tanpa pullback. Jika tangga dipotong pada L4/L5, Profit Factor jatuh di bawah `1.00`. |
| [`run_trending_bot_backtest.py`](file:///home/cuker/mt5_storage/mt5_backtest/run_trending_bot_backtest.py) | **Pure FVG CE 50% Pullback Engine (M5)** | ❌ **IMPASS / MARGINAL (PF `1.02 – 1.04`, Bulan Hijau `50,0%`):**<br>Hanya menghasilkan 9 dari 18 bulan hijau (`50,0%`) dengan Max Drawdown `60,7%`. Profit tipis habis tergerus spread dan slippage. |
| [`run_forex_h1_sweeps.py`](file:///home/cuker/mt5_storage/mt5_backtest/run_forex_h1_sweeps.py) | **Forex H1 Bollinger Bands + RSI Mean Reversion** | ❌ **GAGAL OUT-OF-SAMPLE (PF OOS `0.65 – 0.92`):**<br>Mengalami *overfitting* pada In-Sample dan gagal menghasilkan profit pada periode Out-of-Sample di 7 dari 8 pasangan mata uang mayor/cross. |
| [`bot_sideways.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_sideways.py) & [`bot_crypto_trending.py`](file:///home/cuker/mt5_storage/mt5_config/archived_bots/bot_crypto_trending.py) | **Asian Range Sweep & Crypto Trend M5** | ❌ **DRAWDOWN ASIMETRIS & SPREAD DRAG:**<br>Rentan terkena stop-out beruntun saat *expansion breakout* sesi Eropa dan tergerus spread mikro BTCUSD M5. |
