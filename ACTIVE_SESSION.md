# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** Mode review sementara: login pilih peran sekali klik (web 1.7.0) + fitur pengantaran menunggu validasi
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** Web 1.7.0 live (9a34694). Layar login = panel pilih 5 peran (owner/kasir/waiter/dapur_makanan/barista) sekali klik tanpa sandi; form email tetap ada via tautan. Edge function demo-login deployed; sandi demo HANYA di secret Supabase DEMO_PASSWORD (tidak di repo/docs). Kill switch: supabase secrets unset DEMO_PASSWORD --project-ref svgbotpzgukqurwcrdqd dan/atau demoLogin:false di config.js. REST 5 peran 200 + peran ngawur 400; E2E browser 7/7 (picker, masuk waiter/owner, logout balik picker, toggle form). PENTING: jangan aktif saat operasional nyata — siapa pun tahu URL bisa masuk tanpa sandi; matikan setelah review user. Fitur pengantaran (1.6.1, E2E 12/12) masih menunggu validasi user.
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-27 15:43 WIB
