# 🏛️ Arsitektur Triad Hedged Martingale Non-Stop (Anti-Slow-Bleed & Anti-MC)

> **Status:** Production / Active Architecture  
> **Target Implements:** MT5 Akun 2 Demo Trial 17 (`propfirm-mt5`, XAUUSDm) & Protokol Graceful Wind-Down Akun 1 Real Cent (`exness-mt5`, XAUUSDc)  
> **Magic Numbers:** `556677` (Akun 2) | `778899` (Akun 1)  
> **Tanggal Rilis:** 8 Oktober 2026  

---

## 📌 1. Latar Belakang & Masalah Martingale Tradisional

Pada strategi grid/martingale tradisional di pasar Gold (XAUUSD), terdapat dilema struktural klasik:
1. **Jika Menggunakan Hard Stop Layer (misal Max 5 Layer):** Begitu harga terus trending melawan arah tanpa retrace, bot membeku dan membiarkan floating loss diam. Akun mengalami *slow bleed* (mati perlahan) akibat beban swap atau pemotongan cut-loss paksa yang merusak modal.
2. **Jika Tanpa Stop Layer Sama Sekali:** Jumlah lot membengkak secara eksponensial di layer 8+, memicu Margin Call (MC) jika terjadi reli ekstrem tanpa koreksi.

Sistem **Triad Hedged Martingale Non-Stop** dirancang untuk menghapus konsep *Stop Layer* kaku dengan menggantinya menggunakan **3 Solusi Dinamis Berkelanjutan** yang saling menopang secara organik.

---

## ⚡ 2. Tiga Pilar Solusi Cerdas Institusional (Triad Solutions)

```
       ┌────────────────────────────────────────────────────────┐
       │                   PASAR EMAS TRENDING                  │
       └───────────────────────────┬────────────────────────────┘
                                   │
            ┌──────────────────────┴──────────────────────┐
            ▼                                             ▼
  [SISI MENANG / TREN]                          [SISI KALAH / TERTEKAN]
  • Trend Booster Lot (0.03L-0.05L)             • Tertekan >= 3 Layer
  • Panen TP 10 Pips Berkali-kali               • Floating Drawdown Bertambah
            │                                             │
            ▼                                             │
   [SIPHON HARVEST POOL]                                  │
   (Akumulasi Cuan Tunai)                                 │
            │                                             │
            ├────────────── ✂️ GUNTING EKOR ───────────────┤
            │         (Solusi 1: Tail Pruning)            │
            │  L1 Terburuk Ditutup Disubsidi Cuan         │
            │  BEP Keranjang Melompat Dekat Running       │
            │                                             ▼
            │                                📉 TARGET MELURUH
            │                             (Solusi 2: Dynamic Decay)
            │                            L4: Rp 2.000 | L6: Rp 250 BEP
            │                                             │
            │                                             ▼
            └───────────────────────────────────► [Lolos Keranjang (Close All)]
                                                  Reset Sisi Kalah ke 0.01L!
```

### ✂️ Solusi 1: Gunting Ekor (Tail Pruning via Profit Siphon Pool)
* **Konsep:** Sisi yang menang (searah tren) terus mencetak profit terealisasi dari TP 10 pips. Keuntungan ini dialokasikan ke `siphon_pool_idr`.
* **Eksekusi:** Ketika keranjang sisi yang kalah tertekan ($\ge 3$ layer) dan dana di pool mencukupi:
  - Bot memotong posisi L1 terburuk (posisi paling jauh dari harga saat ini yang menyumbang kerugian terbesar).
  - Kerugian L1 tersebut disubsidi 100% oleh dana `siphon_pool_idr` **tanpa mengurangi saldo modal akun**.
* **Dampak:** Margin langsung lega, beban keranjang berkurang drastis, dan rata-rata titik impas (BEP) keranjang langsung melonjak mendekati harga pasar.
* **Persistensi State:** Dana pool dan histori pemotongan dipersist secara atomik ke disk (`siphon_state.json`) agar tahan terhadap restart container atau crash.

### 📉 Solusi 2: Target BEP Meluruh (Dynamic Decay Escape)
* **Konsep:** Semakin dalam layer terbentuk, semakin tidak realistis menuntut target profit besar karena membutuhkan jarak retrace yang terlalu jauh.
* **Tabel Peluruhan Target:**
  - **Layer 2:** Rp 5.000 IDR (Target normal penuh)
  - **Layer 3:** Rp 3.500 IDR
  - **Layer 4:** Rp 2.000 IDR
  - **Layer 5:** Rp 1.000 IDR
  - **Layer 6:** Rp 250 IDR *(BEP modal kembali)*
  - **Layer 7+:** Rp 0.0 IDR *(Release cepat di titik impas tanpa serakah)*
* **Dampak:** Pada layer 4-6, sedikit sentuhan pantulan harga sudah cukup untuk meloloskan dan menutup bersih seluruh keranjang (*Close All Basket Exit*).

### 🚀 Solusi 3: Trend-Riding Booster (Lot Booster Sisi Menang)
* **Konsep:** Ketika satu sisi tertekan $\ge 3$ layer, hal ini adalah konfirmasi teknikal bahwa pasar sedang bergerak dalam tren searah sisi pemenang.
* **Dinamika Lot Booster:**
  - Lawan layer 1–2: Base Lot normal `0.01L`
  - Lawan layer 3: Boosted Lot `0.02L`
  - Lawan layer 4: Boosted Lot `0.03L`
  - Lawan layer 5+: Boosted Lot `0.05L`
* **Dampak:** Sisi pemenang memanen profit 2x hingga 5x lebih deras. Cuan ekstra ini langsung disedot untuk mengisi Siphon Pool guna mempercepat gunting ekor sisi yang kalah.

---

## 🧮 3. Algoritma Penentuan Lot (Volume-Max Relative Ladder)

Untuk mencegah cacat logika penentuan lot saat berinteraksi dengan Tail Pruning dan Trend Booster:
1. **Anti-Lot Kembar (Anti-Duplicate):** Alih-alih mengandalkan `len(positions)` yang berubah mundur saat ekor dipotong, penentuan lot berikutnya menggunakan rumus:
   $$\text{Next Lot} = \min(\{L \in \text{LOT\_LADDER} \mid L > \max(\text{Active Volume})\}).$$
   Menjamin jika posisi terbesar saat ini $0.05\text{L}$, layer berikutnya pasti $0.08\text{L}$ (tidak pernah mendatar atau mengulang $0.05\text{L}$).
2. **Anti-Lot Terbalik (Anti-Inverted):** Jika L1 dibuka dengan Trend Booster $0.03\text{L}$, Layer 2 otomatis melompat ke $0.05\text{L}$ (tidak mengecil ke $0.02\text{L}$).
3. **Kondisi Reset ke 0.01L:**
   - Saat seluruh keranjang tertutup bersih (*Close All*).
   - Saat sisi lawan telah lepas dari tekanan layer tinggi ($\le 2$ layer).
   - Siklus normal TP 10 pips.

---

## 🛡️ 4. Protokol Graceful Wind-Down (Akun 1 Real Cent)

Protokol ini diterapkan ketika pengguna ingin menghentikan operasional bot di akun live secara aman tanpa *cut-loss* paksa:
1. `GRACEFUL_WIND_DOWN = True` diaktifkan di konfigurasi.
2. Bot **menolak pembukaan siklus/posisi awal baru** (`num_positions == 0` langsung return).
3. Keranjang posisi yang sedang aktif **tetap dikawal** dengan expanding 1.5x step hingga menyentuh target keranjang (+2.5 USC) dan di-*Close All*.
4. **Hasil Implementasi Live (Akun 1 Cent `263301611`):**
   - Modal Awal: `2.353,55 USC`
   - Saldo Akhir Pasca Wind-Down: `2.491,05 USC`
   - **Realized Profit Bersih Tunai:** **+137,50 USC (~Rp 22.000 IDR)**
   - Open Positions: `0` (Bersih total, zero floating drawdown).
