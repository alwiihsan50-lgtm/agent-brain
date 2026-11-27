# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IDLE
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** Wipe database selesai (menunggu konfirmasi USER) — langkah berikut: isi data real (menu via Kelola Menu owner)
- **Modified Files:** docs/SUPABASE.md (repo cafe), backup: /media/cuker/Data/backups/cafe-ruang-tunggu/2026-11-27-pre-wipe/
- **Verification Command / URL:** supabase db query --remote=svgbotpzgukqurwcrdqd --read-only 'SELECT count(*) FROM orders'
- **Next Steps / Notes:** 27 Nov 2026: USER instruksikan hapus semua data kecuali akun, lalu konfirmasi eksplisit via pertanyaan. TRUNCATE order_items/orders/messages/device_tokens/menu RESTART IDENTITY — terverifikasi 0 baris; profiles 5 & auth.users 5 utuh; sequence reset ke 1. Backup 139 baris + metadata 5 akun di /media/cuker/Data/backups/cafe-ruang-tunggu/2026-11-27-pre-wipe/. Repo cafe: commit c36dd79 (docs). Task wipe di agent-brain masih unchecked menunggu konfirmasi USER. 12 tugas lama tetap parkir di docs/parked-tasks.md. PENTING: mode review 1.7.0 masih LIVE (demoLogin:true) — matikan sebelum operasional nyata: supabase secrets unset DEMO_PASSWORD --project-ref svgbotpzgukqurwcrdqd dan/atau demoLogin:false di public/config.js. Sandi demo belum diganti (owner reset via Kelola Staf).
- **Last Updated By:** OpenCode (Qwen4 Max)
- **Last Updated At:** 2026-11-27 23:51 WIB
