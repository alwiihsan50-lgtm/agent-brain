# 🏛️ Arsitektur Reverse Martingale (Paroli) 2-Way Trading

Dokumen ini mendokumentasikan arsitektur kanonikal resmi **Reverse Martingale (Paroli) 2-Way Trading System** yang dirancang untuk mengatasi kelemahan mendasar grid martingale konvensional saat menghadapi pasar *trending* maupun *choppy*.

---

## 🎯 1. Filosofi & Paradigma Utama

Pada martingale konvensional:
* Posisi yang kalah (**losing side**) dilipat lot-nya secara eksponensial ($0.01 \rightarrow 0.02 \rightarrow 0.04 \rightarrow 0.08$). Hal ini memicu risiko kehancuran modal (*gambler's ruin / margin call*) saat tren berjalan kuat tanpa retrace.

Pada **Reverse Martingale (Paroli)**:
1. **Sisi Kalah (Loss) DILARANG KERAS Dilipat**: Sisi yang terkena cut-loss langsung di-reset ke lot dasar terkecil (**0.01L**). Risiko kerugian dibatasi kaku (*strictly flat*).
2. **Sisi Menang (Profit) Dilipat Bertahap**: Keuntungan pasar di-*compound* secara terkontrol menggunakan urutan tangga kemenangan:
   $$\text{Lot Sequence} = [0.01, 0.02, 0.03]$$
3. **Milestone Auto-Lock (3-Streak Reset)**: Begitu mencapai 3 kemenangan beruntun, bot otomatis mengunci seluruh keuntungan dan me-reset urutan kembali ke Level 0 (**0.01L**).

---

## 🛡️ 2. Penanggulangan Risiko & Anti-Whipsaw (Opsi 1)

Saat pasar mengalami *choppy* atau bolak-balik dalam rentang sempit, membuka banyak layer grid dapat memicu penumpukan posisi dua arah yang membebani margin (*whipsaw accumulation*).

**Disiplin Opsi 1 (Single Active Position Per Side):**
* Di pasar hanya boleh ada **maksimal 1 BUY dan 1 SELL** yang aktif secara bersamaan (Total maksimum 2 posisi).
* Tidak ada layer baru yang dibuka sebelum salah satu posisi aktif menyentuh TP atau SL.

---

## 🔬 3. Eliminasi Spread Asymmetry Drag (Kompensasi Spread Matematis)

Pada trading 2 arah dengan hard SL & TP simetris, terdapat fenomena jebakan spread broker:
* **BUY dibuka di harga Ask, ditutup di harga Bid**.
* **SELL dibuka di harga Bid, ditutup di harga Ask**.

Jika target TP dan SL dipasang murni berjarak $D$:
* Saat pasar naik, SELL SL terkena ketika pasar baru bergerak sejauh $D - \text{Spread}$.
* Namun BUY TP baru tersentuh ketika pasar telah bergerak sejauh $D + \text{Spread}$.
* **Celah Discrepancy**: Terjadi jurang sebesar $2 \times \text{Spread}$ di mana SELL sudah mati cut-loss, namun BUY belum sempat menyentuh TP. Jika harga berbalik arah di titik ini, kedua posisi akan terkena SL (*Double Loss*).

### Solusi Kuantitatif: Spread-Compensated TP Priority
Formula TP dikalibrasi dengan diskon sebesar $\ge 2.0 \times \text{Spread}$:
$$\text{BUY TP} = \text{Price}_{\text{Ask}} + D - (2.05 \times \text{Spread})$$
$$\text{SELL TP} = \text{Price}_{\text{Bid}} - D + (2.05 \times \text{Spread})$$

**Hasilnya**:
Saat harga menembus target, TP pihak pemenang **pasti tersentuh 1-2 tik LEBIH DULU** daripada SL pihak yang kalah. Keuntungan dijamin terkunci di broker.

---

## ⚡ 4. Atomic Synchronized Counterpart Management

Alih-alih membiarkan posisi lawan menggantung sendirian setelah pasangannya tertutup:
1. Begitu satu sisi menyentuh TP, bot secara instan mengeksekusi penutupan paksa (*atomic market close*) pada posisi lawan.
2. Sisi pemenang melipat lot ke tingkat berikutnya ($0.01 \rightarrow 0.02$).
3. Sisi yang kalah di-reset ke lot dasar ($0.01$).
4. Keduanya membuka pasangan posisi baru secara simultan di level harga pasar terkini.

---

## ⚙️ 5. Implementasi & Parameter Live (Akun 2 Demo)

| Parameter | Konfigurasi Live | Keterangan |
| :--- | :--- | :--- |
| **Simbol** | `BTCUSDm` | Pasangan crypto 24/7 (aktif di akhir pekan) |
| **Magic Number** | `667788` | Magic unik terisolasi di MT5 Akun 2 |
| **Target SL/TP** | `$25.0 USD` / `$25.0 USD` | Jarak pergerakan cepat & responsif (~0.03% BTC) |
| **Spread Comp Multiplier** | `2.05x` | Menjamin TP kena lebih dulu dari SL lawan |
| **Max Spread Filter** | `$10.0 USD` | Mencegah pembukaan saat spread melebar |
| **Lot Sequence** | `[0.01, 0.02, 0.03]` | Tangga Paroli 3-streak reset |
| **File Skrip** | `/home/cuker/mt5_storage/mt5_config_prop1/bot_reverse_martingale_crypto.py` | Berjalan di container `propfirm-mt5` (Wine Python) |
| **Telemetri JSON** | `/home/cuker/mt5_storage/mt5_config_prop1/bot_status_reverse_marti_crypto.json` | Update status real-time 1 detik |
