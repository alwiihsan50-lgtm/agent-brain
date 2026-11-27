# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IDLE
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** Tidak ada pekerjaan aktif — waiter lacak pengantaran (1.6.1) dikonfirmasi USER & dicentang 27 Nov 2026
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** Verifikasi live 27 Nov: web 1.8.0 HTTP 200, RPC tandai_diantar ada di remote (migration 20261127120000 applied), UI antar ada di app.js produksi. Tugas waiter dicentang atas instruksi USER ('yang sudah live tandai selesai'). Sisa 8 tugas cafe belum live penuh; hardening akun demo sebagian tercover 1.8.0 (sandi demo ditunda atas instruksi USER, owner reset mandiri via Kelola Staf; audit RLS & env var Vercel masih terbuka). PENTING: mode review 1.7.0 masih LIVE (demoLogin:true) — setelah user selesai review, matikan kill switch: supabase secrets unset DEMO_PASSWORD --project-ref svgbotpzgukqurwcrdqd dan/atau demoLogin:false di public/config.js. Catatan: CLI 'brain task done' memakai index berbeda dari 'brain task list' (hanya menghitung task unchecked) — verifikasi teks task setelah eksekusi.
- **Last Updated By:** OpenCode (Qwen4 Max)
- **Last Updated At:** 2026-11-27 22:20 WIB
