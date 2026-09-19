# 🛡️ PANDUAN KUANTITATIF RESMI: STANDAR PENGEMBANGAN BOT & BACKTEST TANPA BIAS (ZERO-BIAS PROTOCOL)

Dokumen ini adalah **standar protokol permanen** bagi seluruh sesi AI Agent dalam merancang, memvalidasi, mengaudit, dan mendeploy algoritma trading MT5 dan backtest Python di sistem ini.

---

## ⚠️ Latar Belakang & Masalah Masa Lalu
Pada pengembangan terdahulu, terjadi beberapa kali ilusi performa pada bot (khususnya Crypto/Forex) di mana backtest di atas kertas tampak sangat menguntungkan (+Rp 9.9M, PF 1.39), namun saat diaudit ulang ternyata menyimpan kelemahan fatal:
1. **Lookahead Bias Tersembunyi:** Sinyal membaca `Close` lilin yang belum selesai pada bar entri.
2. **Pengabaian Spread Riil:** Keluar masuk posisi diuji tanpa memotong spread Bid-Ask broker.
3. **Parameter Tidak Proporsional:** Buffer SL disamakan $20 USD untuk Bitcoin ($81.000), padahal $20 USD bahkan lebih kecil dari spread normal.
4. **Ketiadaan Filter Rejim:** Bot dipaksa trading di hari sideways/choppy tanpa filter ADX.

Protokol ini disusun agar kesalahan tersebut **TIDAK PERNAH TERULANG KEMBALI**.

---

## 🏛️ 1. Hukum Lilin Tertutup (Closed-Bar Law & Zero Lookahead Bias)
Sinyal trading HANYA boleh dihasilkan dari lilin yang telah resmi ditutup sempurna (*Completed Candle*).

```
[Candle i-2 (Selesai)]  ──>  [Candle i-1 (Selesai)]  ──>  [Candle i (BARU TERBUKA)]
        ▲                             ▲                               ▲
        │                             │                               │
  Data Historis                Trigger Sinyal                   Titik Entri:
  Indikator Dihitung           (Doji/MACD/RSI Evaluated)       Harga Open[i]
```

* **Formula Skrip Backtest Python:**
  ```python
  # BENAR (Bebas Lookahead Bias):
  prev_c = close[i-1]
  prev_o = open[i-1]
  macd_bull = (macd_hist[i-1] > 0)
  entry_price = open[i]   # Masuk pada awal bar berikutnya
  
  # SALAH BESAR (Lookahead Bias):
  # macd_hist[i] dihitung dari close[i] yang belum terjadi saat open[i]!
  if macd_hist[i] > 0: entry = open[i]
  ```
* **Formula Bot MT5 Live:**
  * Lilin `rates[-1]` adalah lilin yang sedang berjalan (Bar 0). **DILARANG** membaca `rates[-1]['close']` sebagai konfirmasi sinyal.
  * Sinyal HANYA sah jika membaca `rates[-2]` (Bar 1 yang baru saja tutup) atau array yang di-slice `rates[:-1]`.

---

## ⚖️ 2. Realisme Friksi Transaksi (Bid-Ask & Slippage)

Setiap pengujian backtest WAJIB memperlakukan friksi pasar secara realistis:

### A. Eksekusi Berdasarkan Kuotasi Harga:
* **BUY Order:**
  * Buka di harga **Ask** (`Bid + Spread`).
  * Take Profit (TP) tertutup di harga **Bid** (`High - Spread`).
  * Stop Loss (SL) tertutup di harga **Bid** (`Low`).
* **SELL Order:**
  * Buka di harga **Bid**.
  * Take Profit (TP) tertutup di harga **Ask** (`Low + Spread`).
  * Stop Loss (SL) tertutup di harga **Ask** (`High + Spread`).

### B. Aturan Worst-Case Intra-Bar:
Jika dalam satu bar yang sama tercatat `High >= TP` DAN `Low <= SL`, sistem backtest **WAJIB MENGASUMSIKAN STOP LOSS TERKENA LEBIH DULU**. Asumsi bahwa TP terkena duluan hanya boleh digunakan jika ada data tick riil.

### C. Penalti Slippage Statis:
Tambahkan slippage minimal pada setiap exit SL:
* **Gold (XAUUSD):** $+0.10$ s/d $+0.25$ USD.
* **Bitcoin (BTCUSD):** $+5.00$ s/d $+20.00$ USD.
* **Forex:** $+0.3$ s/d $+0.5$ pip.

---

## 📏 3. Skala Parameter Proporsional (Bukan Angka Statis)

Parameter jarak SL, batas Doji, dan buffer tidak boleh disalin mentah-mentah antar instrumen.

| Instrumen | Harga Nominal | Spread Rata-rata | Buffer SL Minimal | Jarak SL Minimal |
| :--- | :---: | :---: | :---: | :---: |
| **Gold (XAUUSD)** | ~$2,600 USD | $0.15 – $0.35 | **$0.20 – $0.30** | **$1.50 – $4.50** |
| **Bitcoin (BTCUSD)** | ~$80,000 USD | $10.00 – $45.00 | **$60.00 – $100.00** | **$300.00 – $1,200.00** |
| **EURUSD (Forex Major)**| ~1.1000 | 0.8 – 1.2 pip | **1.5 – 2.0 pips** | **8.0 – 25.0 pips** |
| **EURGBP (Cross Slow)** | ~0.8500 | 1.5 – 2.0 pips | **2.0 – 2.5 pips** | **12.0 – 35.0 pips** |

### Uji Kelayakan Biaya (Spread Drag Test):
$$\text{Spread Drag Ratio} = \frac{\text{Spread Broker}}{\text{Target Profit (TP)}} \times 100\%$$
* Jika rasio $> 15\%$, sistem dinyatakan **CACAT SECARA BIAYA**. Jangan jalankan di timeframe kecil jika spread memakan porsi profit terlalu besar.

---

## 🔬 4. Metodologi Validasi Multi-Tahap (Anti-Curve Fitting)

Sebelum sebuah strategi dinyatakan "layak pakai", wajib melalui 3 tahap pengujian:

1. **Tahap 1: In-Sample (70%) vs Out-of-Sample (30%)**
   * Optimasi parameter hanya boleh dilakukan di dataset In-Sample.
   * Kunci parameter dan uji di dataset Out-of-Sample (data yang belum pernah dilihat model).
   * **Syarat Lolos:** Penurunan Profit Factor di Out-of-Sample tidak boleh lebih dari 20%.
2. **Tahap 2: Konsistensi Bulanan (Monthly Breakdown)**
   * Minimal **75% bulan harus profit hijau**.
   * Max Drawdown bulanan tidak boleh melampaui 3x batas risiko harian.
3. **Tahap 3: Stress Test (2x Spread & Slippage)**
   * Naikkan spread menjadi 2 kali lipat spread normal.
   * **Syarat Lolos:** Profit Factor tetap $> 1.10$ dan Net Profit tetap positif.

---

## 🛡️ 5. Proteksi Portofolio Wajib (Circuit Breaker & Sizing)

1. **Universal Flat Risk Sizing:**
   * Risiko per transaksi dibatasi secara flat (misal Rp 20.000 / ~121 USC).
   * Lot dihitung dinamis: $\text{Lot} = \frac{\text{Target Risk}}{\text{Loss per 1 Lot (SL Distance)}}$.
   * Terapkan clamp `min_lot` dan `max_lot`.
2. **Rem Harian Berturut-turut (Daily Circuit Breaker):**
   * Maksimal **3x s/d 5x Stop Loss berturut-turut dalam 1 hari kalender**.
   * Jika tercapai, bot wajib berhenti secara otomatis hingga pergantian hari kalender.
3. **Filter Rejim Wajib:**
   * Bot trending wajib memiliki filter kekuatan tren (misal H1 ADX $\ge 20$).
   * Bot sideways wajib memiliki filter batas maksimal tren (misal M15 ADX $\le 22$).

---

## ✅ 6. Checklist Verifikasi Sebelum Live Deployment

Setiap perubahan atau pembuatan bot baru wajib lolos checklist berikut:
- [ ] Indikator dievaluasi murni pada `i-1` (lilin tertutup).
- [ ] Entri terjadi pada harga `Open[i]`.
- [ ] Jarak SL dan buffer proporsional terhadap harga aset dan minimal 2x–3x spread broker.
- [ ] Perhitungan profit/lot membaca spesifikasi kontrak riil MT5 (`trade_contract_size` dan `digits`).
- [ ] Telah lolos pengujian out-of-sample dan stress test spread.
- [ ] Circuit breaker rem harian aktif dan teruji di kode.
- [ ] Status diekspor ke RAM tmpfs untuk mencegah keausan storage.

---
*Dokumen ini tersimpan di `agent-brain/docs/` dan dipetakan sebagai skill Antigravity `quant-backtest-integrity`.*
