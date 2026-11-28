# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** Web 1.12.0 (format K jutaan + logo minimal) live — menunggu review USER; 1.10.0/1.11.0 juga masih menunggu konfirmasi
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov: rilis 1.12.0 commit bbe6559 live produksi. (1) fmt(): semua kelipatan 1000 -> K termasuk jutaan (1.554.000->1.554K, 12.000.000->12.000K); tidak-bulat tetap penuh; rp() struk&CSV tetap penuh; assert produksi lulus. (2) Logo beringin dari TailShare (5b4c1ec7 jpeg): latar putih dihapus jadi PNG transparan; tree-mark.png aspek alami; placement minimal boot/login-desktop(plate krem)/login-mobile/sidebar; favicon tree-32, apple tree-180, PWA tree-192/512/maskable (nama baru karena /icons/* immutable 1 th); ikon lama dihapus (404); SW CORE+notif icon pindah; cache cafe-v1.12.0. Bukti screenshots/logo-1.12.0-*.png. Task baru 1.12.0 x2 status - [ ]; task 1.10.0/1.11.0 tetap - [ ]; DATA DUMMY TETAP. Setelah USER konfirmasi: centang task terkait, kembalikan parkir #6, hapus dummy (SQL header seed-dummy-20261128.sql). Mode review LIVE + sandi demo belum direset.
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 07:48 WIB
