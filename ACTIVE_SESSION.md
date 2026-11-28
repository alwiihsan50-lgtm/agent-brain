# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** 1.18.1 chat berjendela live + audit free tier selesai — menunggu review USER; dummy tetap; launch-removal terbuka
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov malam: rilis 1.18.1 (8afb38b) atas pertanyaan USER 'riwayat chat tampil seluruhnya?' → temuan limit 200 gabungan; USER pilih paket penuh lalu perjelas: maks 200 di layar, halaman lama mengganti jendela (terbaru tidak dimuat). Desain: loadChatWindow(older) keyset cursor (dibuat_pada,id) + scope eq tipe per chip; state.chatLive/chatCursor; renderChat oldbar+chat-older; onChatMessage hanya sisip bila live&scope&tab chat; loadTab chat skip reload bila !chatLive; index messages_tipe_waktu_idx + messages_waktu_id_idx (migrasi 20261128060000). Verifikasi banjir terkendali 205 manusia+205 audit (toggle habis menu uji): semua terbaru=200 audit, scope chat=200 manusia, older ganti jendela (sisa dinamis!), realtime lama stabil, kembali live, mobile oldbar 390px, 0 error; regresi 1.16/1.17/1.18 lulus lokal+produksi. PELAJARAN UJI: (1) assertion sisa halaman harus dinamis (data asli ikut terhitung); (2) race: realtime push ke jendela kosong SAAT load memenuhi wait prematur → settle 600ms pasca klik chip; (3) wait ganti scope harus membedakan scope (filter+isi), bukan hanya live+length; (4) pesan tidak bisa dihapus klien (append-only) → cleanup banjir via SQL service-role. AUDIT FREE TIER (permintaan USER): DB 15MB/500MB (3%); storage 4,5MB/1GB (0,45%, apk 4,46MB + menu-foto 0); aset inti 277KB + foto 1,79MB + ikon 355KB ≈ 2,4MB unduh sekali per perangkat (SW cache); 1 channel realtime/klien (4 tabel publikasi); 3 edge functions; 2 cron jobs; estimasi egress API <1GB/bln dari 5GB; realtime <200rb pesan/bln dari 2M; pertumbuhan audit+messages dibatasi retensi 12 bulan (proyeksi DB <100MB setahun). Kesimpulan: TIDAK berat, semua kuota terpakai single-digit %. Rekomendasi: cleanup dummy saat launch, pantau egress dashboard bulanan, apk bucket bisa pindah GitHub Releases bila storage menyempit (belum perlu).
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 16:50 WIB
