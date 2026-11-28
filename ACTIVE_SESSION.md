# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** 1.15.0 review 6 peran live — menunggu review USER; task launch-removal tercatat; 1.10.0–1.15.0 + dummy30d - [ ]
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov: rilis 1.15.0 commit 82ad807 live. (1) demo-login: ACCOUNTS + owner_makanan (ownermakanan@ruangtunggu.com); provision otomatis ensureDemoAccount (service role env) bila grant gagal; PELAJARAN: secret lama DEMO_PASSWORD < 8 karakter sedangkan GoTrue kini min 8 → akun baru weak_password 422; solusi secret BARU DEMO_PASSWORD_MAKANAN (openssl rand -hex 12, tidak di repo); sandi demo lain TIDAK disentuh. (2) Rename: profiles.nama owner → 'Owner Minuman' (SQL), ROLELBL.owner 'Owner Minuman', topbar userRole pakai ROLELBL, opsi staf 'Owner Minuman (Admin)', tombol demo owner label baru + tombol owner_makanan baru (6 peran). Verifikasi lokal+produksi: 6 tombol, sekali klik owner_makanan → 20 kartu makanan, owner → 29 minuman + Kelola staf, daftar staf 6 termasuk kedua owner, 0 console error; race uji topbar diperbaiki dengan wait_for_function. Bukti screenshots/review-1.15.0-*.png. SAAT LAUNCH (task terpisah): unset kedua secret + demoLogin false + bersihkan akun demo. DATA DUMMY TETAP sampai konfirmasi USER; setelah konfirmasi: centang task, parkir #6, cleanup dummy SQL header seed-dummy-20261128.sql.
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 10:00 WIB
