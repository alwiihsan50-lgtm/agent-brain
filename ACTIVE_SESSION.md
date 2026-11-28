# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** 1.17.0 Jejak owner-only live — menunggu review USER; dummy tetap; launch-removal terbuka
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov malam: rilis 1.17.0 (17ae865) atas usul USER 'tab jejak gak perlu di semua staff'. Keputusan: Jejak (arsip+filter+CSV) untuk owner & owner_makanan; RLS audit_baca dibatasi my_role() in ('owner','owner_makanan') — pembatasan SERVER bukan hanya UI; subscribeRealtime audit_log hanya owner (hindari channel error RLS); TABS staff tanpa jejak; deep-link ?tab=jejak staff sudah guarded TABS.includes. Chat messages tetap semua peran (transparansi situasional) & pencatatan trigger tidak berubah (akuntabilitas penuh). Verifikasi lokal+produksi: kasir 4 tab tanpa jejak, select audit 0 baris DITOLAK, update/delete/insert DITOLAK (403 revoke), uji silang pada baris asli: DITOLAK + arsip UTUH; owner jejak penuh + toggle 1.16.2 + CSV; realtime chat ke staff tetap (87 kartu); mobile owner 6 tab; 0 error. Cleanup uji: 0 sisa; data asli utuh incl. pembatalan asli #498/520/525/526 'Terlalu lama' (cafe aktif). PELAJARAN: skrip penetrasi lama mengasumsikan staff bisa SELECT audit utk ambil id target → setelah RLS owner-only harus uji silang (owner baca id, staff coba, owner verifikasi utuh); id 1 tidak ada lagi (sequence maju) → assertion integritas pakai baris pertama yang ada.
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 12:23 WIB
