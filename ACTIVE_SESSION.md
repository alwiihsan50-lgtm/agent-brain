# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** 1.17.1 koneksi jujur + refresh live — menunggu review USER; dummy tetap; launch-removal terbuka
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov malam: rilis 1.17.1 (a0c8521 + e52d7c0) atas pertanyaan USER 'apa perlu tombol refresh & indikator online' + 'apa buat berat? kalo engga kerjakan'. JAWABAN BERAT: tidak — event-driven (status channel, online/offline, klik), nol polling, nol DB change. Implementasi: state.conn/rtHealthy/rtDown/rtReplacing; setConn() pill+sidebar (sideLive/sideLiveText); mobile pill dot-only (text display:none); subscribeRealtime status SUBSCRIBED→live+kompensasi loadTab bila rtDown; CHANNEL_ERROR/TIMED_OUT/CLOSED→connecting; online listener & visibilitychange resubscribe bila !rtHealthy; subscribeRealtime buang SEMUA channel via db.getChannels() (cegah yatim/dobel pasca flap); refreshAll() = loadMenu silent + loadTab + refreshBadge + syncOrderQueue + resubscribe bila perlu, ikon spinning. PELAJARAN UJI: (1) supabase-js tidak selalu resubscribe sendiri pasca offline→online → resubscribe eksplisit di online event; (2) assertion 'order belum masuk' false-positive karena NAMA uji run sebelumnya masih ada di daftar hari ini → pakai suffix unik per run; (3) probe instrumentasi loadTab + stack membuktikan app bersih sebelum menyalahkan app. Verifikasi lokal+produksi: boot Live, offline pill+sidebar merah, order konteks lain muncul tanpa pindah tab setelah pulih, connecting 'Menyambung…', tanpa channel order tidak masuk sampai klik refresh, refresh memulihkan channel+data, mobile dot+refresh muat 390px, regresi 1.16/1.17 penuh lulus, 0 console error. Cleanup: 0 sisa uji; data asli + 482 dummy utuh. Bukti screenshots/conn-1.17.1-*.png.
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 12:59 WIB
