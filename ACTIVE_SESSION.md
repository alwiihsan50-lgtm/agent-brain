# 📝 ACTIVE SESSION SCRATCHPAD (JEMBATAN ANTAR-AGENT)

> 💡 **Kapan Menggunakan File Ini?**
> File ini adalah **Papan Tulis Sementara (Scratchpad)** jika Anda (USER) ingin **berganti AI Agent / ganti sesi di tengah jalan** saat sebuah proyek multi-langkah belum selesai.
> - **Agent yang sedang bekerja:** Wajib menuliskan ringkasan konteks teknis saat ini sebelum sesi ditutup jika tugas belum 100% tuntas.
> - **Agent yang baru masuk:** Wajib membaca file ini pada fase *Booting* agar langsung tahu persis sampai baris kode mana pekerjaan terakhir berhenti, tanpa perlu bertanya ulang ke USER.

---

## 🔄 Status Sesi Saat Ini
- **Status:** `IDLE` *(Seluruh Tugas Sesi Ini Telah Selesai & Divalidasi User)*
- **Proyek Terakhir:** Upgrade Live [`bot_trending.py`](file:///home/cuker/mt5_storage/mt5_config/bot_trending.py) v6.2 dengan Skema **Flat Risk 2.0% + High-Water Mark (HWM) 10% Drawdown Ratchet Murni Satuan `IDC`** di Akun 1 (`443003218` - `Exness-MT5Real44`)
- **Agent Terakhir:** Antigravity (Gemini 3.8 Pro)
- **Waktu Update:** 2026-10-18 11:06 WIB

---

## 🎯 Ringkasan Handoff untuk Sesi Baru
1. **Status Live Akun 1 (`443003218` - `Exness-MT5Real44`, Container `exness-mt5`, Port `3000`, Mata Uang `IDC`):**
   - **Bot Aktif:** [`bot_trending.py`](file:///home/cuker/mt5_storage/mt5_config/bot_trending.py) v6.2 (Magic `889911`, diawasi oleh [`runner.py`](file:///home/cuker/mt5_storage/mt5_config/runner.py)).
   - **Mekanisme Sizing Baru ([`core/risk_manager.py`](file:///home/cuker/mt5_storage/mt5_config/core/risk_manager.py)):**
     - **Murni Satuan Native `IDC`** (bebas parameter `USC` / kurs statis): `HWM Balance` disimpan di [`hwm_state_443003218.json`](file:///home/cuker/mt5_storage/mt5_config/hwm_state_443003218.json) (`27.926.771,78 IDC`).
     - **Flat Risk `2.0%` per Trade:** `558.535,44 IDC` (`≈ Rp 5.585 IDR`) pada HWM saat ini.
     - **Aturan HWM 10% Drawdown Ratchet:** Selama drawdown dari `HWM` `< 10%`, basis perhitungan 2% tetap menggunakan `100% HWM` (**lot tidak dikecilkan**). Penyesuaian turun (`-10%` step) hanya dilakukan setiap kelipatan `10%` drawdown dari `HWM`.
     - **Dynamic Free-Margin Guard:** Menghapus hard-cap statis `0.50 Lot` lama dan menggantinya dengan pengecekan `mt5.order_calc_margin()` (maks 50% `free_margin` dalam `IDC`).
   - **2 Pair Aktif:**
     - `XAUUSDc`: `fixed_lot=None`, `risk_pct_equity=0.02`, `dd_step_pct=0.10`, `R:R 1:2.0`, `sl_mode="hybrid"` (`1.8x ATR14`), `use_m5_zlema_align=True` (Lot dinamis saat ini `~0.03–0.06 Lot`).
     - `USTECc`: `fixed_lot=None`, `risk_pct_equity=0.02`, `dd_step_pct=0.10`, `R:R 1:1.75`, `sl_mode="atr"` (`1.8x ATR14`), `use_m5_trend_align=True` (Lot dinamis saat ini `~0.34–0.61 Lot`).
