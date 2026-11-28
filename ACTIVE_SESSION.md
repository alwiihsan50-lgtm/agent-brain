# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** Web 1.13.0 (tab Evaluasi menu owner) live — menunggu review USER; 1.10.0/1.11.0/1.12.0 juga masih menunggu konfirmasi
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov: rilis 1.13.0 commit fe0d83a live produksi. Tab baru owner 'Evaluasi' (TABS.owner: closing,evaluasi,pesanan,menu,chat; ikon i-trend). computeMenuEval() murni client-side (pola computeClosingSplit): periode kini+pembanding satu query orders+order_items; semua menu dinilai termasuk 0 terjual & nonaktif; item menu terhapus ditandai; order batal dikecualikan. Ambang: Laris >=10% omzet, Sepi <2%, mati qty 0. KPI: omzet+tren, best seller, menu aktif tanpa penjualan, konsentrasi top 3. Periode: hari ini/7/30/custom (tanggal terbalik dinormalisasi). Export CSV evaluasi-menu-*.csv angka penuh. Bottom nav 5 tombol muat 390px (guard <=400px). Verifikasi lokal+produksi: assert sintetis (tren 100%, batal excluded, deleted row, dead count) + data nyata (453K/11 trx — ada 1 order baru dari review USER selain 10 dummy), 0 console error. Bukti screenshots/eval-1.13.0-*.png. Task 1.13.0 - [ ]; task 1.10.0/1.11.0/1.12.0x2 tetap - [ ]; DATA DUMMY TETAP. Setelah USER konfirmasi: centang task terkait, kembalikan parkir #6, hapus dummy (SQL header seed-dummy-20261128.sql). Mode review LIVE + sandi demo belum direset.
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 08:10 WIB
