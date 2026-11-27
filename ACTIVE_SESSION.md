# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IDLE
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** Tidak ada pekerjaan aktif — wipe DB, menu real 49 item, QRIS 1.9.0 semuanya dikonfirmasi USER 28 Nov 2026
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov 2026: USER konfirmasi 3 task selesai (wipe database sisakan 5 akun; isi menu real 49 item; QRIS web 1.9.0 dengan cache 1x unduh). Ketiganya dicentang + diarsipkan otomatis. App siap diisi data operasional real. 12 tugas lama tetap parkir di docs/parked-tasks.md menunggu prioritas baru USER. PENTING sebelum operasional nyata: (1) matikan mode review sekali klik — supabase secrets unset DEMO_PASSWORD --project-ref svgbotpzgukqurwcrdqd dan/atau demoLogin:false di public/config.js lalu deploy; (2) owner reset sandi 5 akun via Kelola Staf. Backup pre-wipe: /media/cuker/Data/backups/cafe-ruang-tunggu/2026-11-27-pre-wipe/; QRIS asli: .../qris/qris-asli-IMG_6747.jpeg.
- **Last Updated By:** OpenCode (Qwen4 Max)
- **Last Updated At:** 2026-11-28 00:33 WIB
