# 🛡️ PANDUAN KUANTITATIF RESMI: STANDAR PENGEMBANGAN BOT & BACKTEST TANPA BIAS (12 PILAR INSTITUSIONAL)

Dokumen ini adalah **standar protokol permanen** bagi seluruh sesi AI Agent dalam merancang, memvalidasi, mengaudit, dan mendeploy algoritma trading MT5 dan backtest Python di sistem ini.

---

## ⚠️ Latar Belakang Masalah
Pada pengembangan terdahulu, terjadi beberapa kali ilusi performa pada bot (khususnya Crypto/Forex) di mana backtest di atas kertas tampak sangat menguntungkan, namun saat diaudit ulang ternyata menyimpan kelemahan fatal:
1. **Lookahead Bias Tersembunyi:** Sinyal membaca `Close` lilin yang belum selesai pada bar entri.
2. **Pengabaian Spread Riil:** Keluar masuk posisi diuji tanpa memotong spread Bid-Ask broker.
3. **Parameter Tidak Proporsional:** Buffer SL disamakan $20 USD untuk Bitcoin ($81.000), padahal $20 USD bahkan lebih kecil dari spread normal.
4. **Warm-up Horizon Tidak Memadai:** Indikator dihitung dari data bar yang terlalu pendek sehingga menghasilkan nilai yang berbeda dengan live terminal.
5. **Ketiadaan Filter Rejim:** Bot dipaksa trading di hari sideways/choppy tanpa filter ADX.

Protokol ini disusun agar kesalahan tersebut **TIDAK PERNAH TERULANG KEMBALI**.

---

## 🏛️ 12 PILAR STANDAR KUANTITATIF ANTI-BIAS

### 1. Hukum Lilin Tertutup (Closed-Bar Law & Zero Lookahead Bias)
Sinyal trading HANYA boleh dihasilkan dari lilin yang telah resmi ditutup sempurna (*Completed Candle*).
* **Di Backtest Python:** Jika entri dieksekusi pada `Open[i]`, seluruh indikator penentu (MACD, EMA, RSI, ADX, Doji) **WAJIB dibaca pada indeks `[i-1]`** atau di-`.shift(1)`. Dilarang keras mengevaluasi indikator berbasis `Close[i]` saat bar `i` baru dibuka!
* **Di Bot MT5 Live:** Lilin indeks 0 (`rates[-1]`) adalah lilin berjalan yang belum selesai. Pemicu sinyal hanya boleh membaca lilin indeks 1 (`rates[-2]`) atau array yang telah di-slice `rates[:-1]`.

### 2. Realisme Friksi Transaksi (Bid-Ask Kuotasi & Worst-Case Execution)
Mengabaikan spread dan selisih kuotasi adalah penipuan statistik:
* **BUY:** Buka di harga **Ask** (`Bid + Spread`), TP tertutup di **Bid** (`High - Spread`), SL tertutup di **Bid** (`Low`).
* **SELL:** Buka di harga **Bid**, TP tertutup di **Ask** (`Low + Spread`), SL tertutup di **Ask** (`High + Spread`).
* **Prinsip Worst-Case Intra-Bar:** Jika dalam 1 candle yang sama tercatat `High >= TP` DAN `Low <= SL`, sistem backtest **WAJIB MENGASUMSIKAN STOP LOSS TERKENA LEBIH DULU**.

### 3. Execution Latency & Tick Slippage (Friksi Jeda Eksekusi)
* Lilin ditutup pada `14:00:00`. Order terkirim dan terisi di server broker pada `14:00:01` s/d `14:00:02`.
* **Kewajiban Slippage Penalti:** Wajib menambahkan penalti slippage minimal pada setiap exit SL:
  * Gold (XAUUSD): Minimal $-0.10$ USD s/d $-0.25$ USD.
  * Bitcoin (BTCUSD): Minimal $-5.00$ USD s/d $-20.00$ USD.
  * Forex: Minimal $-0.3$ pip s/d $-0.5$ pip.

### 4. Skala Parameter Proporsional (Anti-Angka Statis Acak)
Parameter jarak SL, buffer, dan batas Doji tidak boleh disalin mentah-mentah antar instrumen:
* **Buffer SL Relatif Terhadap Harga & Spread:**
  * Emas ($2,600 USD, spread $0.20): Buffer SL $0.20 USD adalah wajar (~1x spread, ~0.007% harga).
  * Bitcoin ($80,000 USD, spread $10–$45): Buffer SL $20 USD adalah **KESALAHAN FATAL** (lebih kecil dari spread!). Buffer minimal harus 2x–3x spread ($60–$100 USD) atau berbasis persentase ATR.
* **Uji Serapan Biaya (Spread Drag Test):**
  $$\text{Spread Drag Ratio} = \frac{\text{Spread Broker}}{\text{Target Profit (TP)}} \times 100\%$$
  * Jika rasio $> 15\%$, sistem **DITOLAK**. Biaya transaksi memakan porsi profit terlalu besar.

### 5. Warm-Up Horizon & Indicator Stabilization (Stabilitas Indikator)
* Indikator lagging berbasis eksponensial (EMA, MACD, ATR, ADX) membutuhkan masa pemanasan riwayat data agar nilai matematisnya konvergen dan identik dengan terminal MT5 live.
* **Syarat Minimal Riwayat Bar:** Minimal **$3\times$ s/d $5\times$ periode terpanjang**.
  * Contoh: Menghitung EMA 200 atau H1 Trend Filter wajib memuat minimal **1.000 bar masa lalu** sebelum mengevaluasi sinyal pertama.

### 6. Swap Fee & Overnight Financing Drag (Biaya Inap Semalam)
* Transaksi yang tertahan melewati jam rollover harian (pukul 04:00/05:00 WIB) terkena bunga inap (*swap fee*).
* **Triple Swap Hari Rabu:** Khusus hari Rabu malam, swap dikalikan $3\times$ lipat.
* Pada backtest strategi yang menahan posisi $>24$ jam, perhitungan PnL wajib memperhitungkan tabel swap harian broker.

### 7. Weekend Gap & Session Rollover Protection (Risiko Akhir Pekan)
* Pasar Forex dan Emas tutup Jumat malam dan buka Senin subuh.
* Jika ada peristiwa geopolitik akhir pekan, harga buka Senin dapat melompat jauh melewati batas Stop Loss (*Gap Risk*).
* Bot wajib memiliki parameter: apakah posisi intraday wajib ditutup sebelum penutupan pasar hari Jumat malam.

### 8. Dynamic Broker Contract & Currency Sizing
Sebelum menghitung lot, bot wajib memeriksa spesifikasi terminal:
* `BTCUSDc` di Exness Cent adalah **0.01 BTC per lot** (bukan 1.0 BTC).
* Emas (`XAUUSDc` / `XAUUSDm`): 100 oz per lot.
* Mata uang akun Cent adalah `USC` ($1 USD = 100 USC). Fungsi `mt5.order_calc_profit()` mengembalikan nilai dalam mata uang akun.

### 9. Multi-Stage Validation (In-Sample, Out-of-Sample, & WFA)
1. **Split Test (70% In-Sample vs 30% Out-of-Sample):** Parameter dioptimasi pada data In-Sample, lalu diuji pada data Out-of-Sample yang belum pernah dilihat model. Jika Profit Factor turun $>25\%$, parameter tersebut mengalami *overfitting*.
2. **Uji Konsistensi Bulanan (Monthly Breakdown):** Minimal **75% bulan harus profit hijau**.
3. **Stress Test 2x Spread:** Naikkan spread menjadi 2x lipat normal. Jika strategi langsung bangkrut, sistem terlalu rapuh.

### 10. Anti-Overfitting & P-Hacking Trap (Kebetulan Statistik)
* **Aturan Parsimoni (Prinsip Occam's Razor):** Model dengan 2–3 parameter inti yang logis selalu mengalahkan model dengan banyak indikator rumit yang di-tweak berlebihan.
* Jika melakukan parameter sweep: Jangan memilih titik puncak kurva terisolasi (*isolated peak*). Pilih rentang nilai yang stabil di sekitarnya (*broad plateau*).

### 11. Proteksi Portofolio Wajib (Circuit Breaker & Sizing)
* **Universal Flat Risk Sizing:** Risiko per trade dibatasi secara flat (misal Rp 20.000), bukan lot statis.
* **Rem Harian Berturut-turut (Daily Circuit Breaker):** Maksimal 3x–5x Stop Loss berturut-turut dalam 1 hari kalender.
* **Filter Rejim Wajib:** Bot trending wajib memakai filter kekuatan tren (misal H1 ADX $\ge 20.0$). Bot sideways wajib memakai batas maksimal tren (misal M15 ADX $\le 22.0$).

### 12. Checklist Audit Baris-demi-Baris Sebelum Live Deployment
- [ ] Indikator dihitung murni pada `[i-1]` (lilin tertutup).
- [ ] Entri dieksekusi pada harga `Open[i]` dengan penalti slippage realistis.
- [ ] Buffer SL proporsional terhadap harga aset dan minimal 2x–3x spread broker.
- [ ] Slicing array indikator bebas off-by-one error (`[-k]` vs `[:-1][-k]`).
- [ ] Indikator memiliki warm-up minimal $3\times$ periode terpanjang (misal $\ge 1.000$ bar untuk EMA 200).
- [ ] Efek swap dan jam rollover diakomodasi.
- [ ] Telah lolos pengujian out-of-sample dan stress test spread.
- [ ] Circuit breaker rem harian aktif dan teruji di kode.
- [ ] Status diekspor ke RAM tmpfs untuk melindungi storage SSD.

---
*Protokol ini tersimpan di `agent-brain/docs/` dan dipetakan sebagai skill Antigravity `quant-backtest-integrity`.*
