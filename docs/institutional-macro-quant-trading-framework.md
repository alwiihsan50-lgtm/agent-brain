# 🏛️ KERANGKA KERJA TRADING MAKRO-KUANTITATIF INSTITUSIONAL (THE GREAT TRADER BLUEPRINT)

> 💡 **FILOSOFI UTAMA:**
> *"Trader amatir mencari pola grafik secara terisolasi. Trader hebat membaca peta makroekonomi global, mengidentifikasi arus pasang modal institusional, dan hanya menggunakan teknikal untuk menentukan waktu dan presisi titik eksekusi."*
> — Mandat Resmi: **Capital Preservation First, Profit Sedikit Konsisten > Win Besar Lalu MC.**

---

## 🧭 1. Piramida 4 Pilar Analisis Institusional

```
                    ┌───────────────────────────────┐
                    │    1. MAKRO & FUNDAMENTAL     │ ➔ The "Why"
                    │  (Suku Bunga, Yield, Inflasi) │   (Arah Arus Modal Global)
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │   2. SENTIMEN & INTERMARKET   │ ➔ The "Context"
                    │ (Risk-On/Off, DXY, News Risk) │   (Iklim Pasar & Rejim)
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │   3. STRUKTUR PASAR (SMC)     │ ➔ The "Where"
                    │ (Order Block, FVG, Liquidity) │   (Zona Harga Institusi)
                    └───────────────┬───────────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │  4. EKSEKUSI & RISK ASYMMETRY │ ➔ The "When & How"
                    │  (M5 Timing, R:R 1:3, Hard SL)│   (Presisi & Proteksi Akun)
                    └───────────────────────────────┘
```

---

## 🌍 PILAR 1: Fondasi Makro & Fundamental (The "Why")

Sebelum grafik dibuka, tentukan kompas fundamental global:
1. **Divergensi Kebijakan Bank Sentral (*Central Bank Divergence*):**
   * Pasangan mata uang selalu merupakan rasio dua ekonomi (A vs B).
   * **Mata Uang Kuat:** Bank sentral dengan suku bunga riil tinggi, ekonomi tangguh, inflasi persisten (contoh: USD didukung Fed rate tinggi dan ekonomi tangguh).
   * **Mata Uang Lemah:** Bank sentral dengan pertumbuhan ekonomi lesu, risiko stagflasi, atau pemangkasan suku bunga lebih cepat (contoh: EUR tertekan stagflasi zona Eropa).
2. **Imbal Hasil Obligasi Pemerintah (*US Treasury Yields*):**
   * Yield 10Y AS yang tinggi (> 5.0%) adalah magnet modal global, mendorong penguatan Dolar AS (DXY) dan menekan mata uang lawan (EUR/USD, GBP/USD).
3. **Sentimen Struktural Komoditas (Emas / XAUUSD):**
   * Emas tidak hanya dipengaruhi oleh suku bunga AS, melainkan oleh faktor dedolarisasi, pembelian cadangan emas fisik oleh Bank Sentral Global (PBoC, BRICS), dan eskalasi risiko geopolitik dunia.

---

## ⚡ PILAR 2: Sentimen & Analisis Lintas Pasar (*Intermarket Context*)

1. **Rejim Pasar: Risk-On vs Risk-Off:**
   * **Risk-On (Optimisme):** Saham menguat, modal mengalir ke mata uang berimbal hasil tinggi.
   * **Risk-Off (Kekhawatiran / Defensif):** Modal mengalir ke instrumen *safe-haven* (USD, Emas, Obligasi).
2. **Protokol Perlindungan Berita Berdampak Tinggi (*Event Risk Shield*):**
   * Kalender ekonomi (NFP, CPI, PCE, FOMC Rate Decision) memicu *liquidity vacuum* dan *spread widening*.
   * **Aturan Mutlak:** Membekukan entri baru 30 menit sebelum dan sesudah rilis data *High-Impact*, membiarkan volatilitas liar mereda sebelum menyaring setup kembali.

---

## 🎯 PILAR 3: Struktur Pasar Cerdas (*Smart Money Concepts / The "Where"*)

Gunakan timeframe makro (D1, H4, H1) untuk memetakan level di mana institusi besar meninggalkan jejak likuiditas:
1. **Order Block (OB) & Fair Value Gap (FVG):** Menemukan ketidakseimbangan harga (*imbalance*) tempat harga berpotensi memantul (*mitigation*).
2. **Zona Premium vs Discount:**
   * Dilarang membeli di zona Premium (kemahalan).
   * Dilarang menjual di zona Discount (terlalu murah).
3. **Liquidity Sweep (Pembersihan Likuiditas):** Menunggu pasar menyapu level puncak/lembah sebelumnya (*Stop Hunt*) sebelum mengonfirmasi pembalikan arah sejati.

---

## 🏹 PILAR 4: Waktu Eksekusi & Tata Kelola Risiko (The "When & How")

### 📜 Hukum Keselarasan Ganda (The Confluence Law):
> ⚖️ **Sebuah transaksi HANYA SAH dieksekusi jika:**
> $$\text{Arah Makro Fundamental} == \text{Arah Struktur Pasar Teknikal}$$
> * **Fundamental Bearish + Teknikal Bearish:** 🟢 **High-Conviction SELL** (Searah arus modal).
> * **Fundamental Bullish + Teknikal Bullish:** 🟢 **High-Conviction BUY** (Searah arus modal).
> * **Fundamental & Teknikal Bertolak Belakang:** ⚪ **HOLD / STANDBY** (Dilarang melawan arus makro dan dilarang mendahului grafik).

### 🛡️ Parameter Risiko Ketat (Mandat Manager):
* **Ukuran Lot:** Flat `0.01 Lot` mikro cent per transaksi.
* **Risiko per Transaksi:** Terkunci di bawah **1.0% Equity** (nominal rata-rata 2.5 – 5.0 USC).
* **Rasio Keuntungan Asimetris:** Strict **Risk-to-Reward 1:2.5 s/d 1:3.0**.
* **Hard Stop Loss di Broker:** Tidak ada posisi tanpa SL di server Exness.
* **Maksimal Eksposur Portofolio:** Maksimal 2 posisi terbuka simultan.

---

## 🤖 Integrasi AI Macro Supervisor (Gemini 3.8 Flash via Port 5050)

Daemon `mt5-ai-supervisor.service` bertindak sebagai Pengawas Makro:
1. **Audit Tiap 30 Menit:** Membaca telemetri akun, floating profit, pergerakan 4 pair, dan kalender berita.
2. **Evaluasi Rejim:** Menggunakan kemampuan penalaran LLM untuk memastikan transaksi aktif selaras dengan dinamika makro.
3. **Push Digest ke HP:** Melaporkan intisari situasi pasar dan pertumbuhan akun langsung ke smartphone pemilik modal.
