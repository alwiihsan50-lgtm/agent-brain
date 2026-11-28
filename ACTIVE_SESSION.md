# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** Evaluasi menu (1.13.0) + dummy 30 hari live — menunggu review USER; 1.10.0–1.13.0 semua masih - [ ]
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov: (1) web 1.13.0 fe0d83a: tab Evaluasi owner (periode hari ini/7/30/custom, tren vs periode lalu, badge Laris>=10%/Sepi<2%/mati, KPI, CSV). (2) seed dummy 30 hari 69f55d7: 468 order lampau (total 483 = 482 dummy + 1 asli 'Rosiana' id 15), 40 batal; eksekusi supabase db query --remote --yes -f; pelajaran: order batal wajib status kategori non-null ('batal') else trigger init_order_kategori_status+guard_order_batal menolak; DO atomik jadi gagal pertama tanpa data parsial. Verifikasi produksi: Evaluasi 7hr 6.295K/113 trx tren nyata (CSV Nasi Ayam Penyet +94,1%), 30hr 25.883K/443 trx, dead 7, Closing 21 Nov 25 trx/1.549K, 0 console error, nav 5 tombol muat 390. Bukti screenshots/eval-1.13.0-*.png + dummy30d-closing-1121.png. DATA DUMMY (14 hari ini + 468 lampau) TETAP sampai USER konfirmasi; cleanup satu SQL header seed-dummy-20261128.sql (LIKE 'Dummy%' mencakup semua). Setelah konfirmasi: centang task 1.10.0/1.11.0/1.12.0x2/1.13.0/dummy30d, kembalikan parkir #6, hapus dummy. Mode review LIVE + sandi demo belum direset.
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 09:02 WIB
