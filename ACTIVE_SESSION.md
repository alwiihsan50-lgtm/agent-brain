# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** 1.14.0 kunci menu per owner live — menunggu review USER; 1.10.0–1.14.0 + dummy30d semua - [ ]
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov: rilis 1.14.0 commit 11b4106 live. Migrasi 20261128020000_owner_per_kategori: profiles_role_check + owner_makanan; menu_kelola = owner full OR owner_makanan makanan (using+with check); set_menu_habis + owner_makanan. staff-admin ROLES + owner_makanan (deploy). App: menuScope() owner->minuman, owner_makanan->makanan; menuFiltered/renderMenuManager/openMenuForm/saveMenu scoped; chip wewenang; TABS+ROLELBL+opsi staf. PENTING: RLS UPDATE/DELETE menolak SENYAP (0 baris, tanpa error) — uji harus ukur efek, bukan error; insert menolak 403. Override admin owner tetap full di server (UI hide saja, keputusan USER varian B). Verifikasi lokal+produksi: owner 29 kartu minuman + Kelola staf; owner_makanan 20 kartu makanan tanpa Kelola staf; tembus RLS update/insert/delete minuman DITOLAK, update makanan OK; override owner OK; Evaluasi/Closing kedua role penuh; kasir 2 kategori; 0 console error. Akun uji uji.owner.makanan@ruangtunggu.com DIHAPUS (cascade profiles); data utuh 49 menu/483 order/5 staf. Bukti screenshots/owner-scoped-1.14.0-*.png. db push ternyata juga apply 2 migrasi lama yg belum tercatat history (idempoten, data aman). DATA DUMMY TETAP sampai konfirmasi USER; cleanup SQL header seed-dummy-20261128.sql. Setelah konfirmasi: centang semua task, parkir #6, hapus dummy. Mode review LIVE + sandi demo belum direset.
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 09:45 WIB
