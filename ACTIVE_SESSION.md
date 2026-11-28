# Active Session Scratchpad

> ℹ️ File ini berfungsi sebagai jembatan memori real-time antar AI Agent lintas sesi ketika ada pekerjaan yang sedang berjalan.
> Update file ini saat beralih tugas atau sebelum handoff. Ketika tugas selesai dan telah divalidasi oleh USER, kembalikan status ke IDLE.

- **Status:** IN_PROGRESS
- **Active Project:** Cafe Ruang Tunggu
- **Current Task:** 1.18.0 foto menu + ganti foto owner live — menunggu review USER; dummy tetap; launch-removal terbuka
- **Modified Files:** -
- **Verification Command / URL:** -
- **Next Steps / Notes:** 28 Nov malam: rilis 1.18.0 (3bea046) satu rilis sesuai pilihan USER (foto + upload owner sekalian). Foto diambil dari Wikimedia Commons (CC0/CC BY/CC BY-SA/PD) via skrip berburu 4 round + QA visual montase sendiri: buang kandidat salah (bendera kota Sanger, lukisan LACMA, penyanyi band Butterscotch, muffin, donat, es krim, kemasan, botol, poster, fries McDonald's). 49 webp 600px total 1,7MB di public/menu/<id>.webp; fallback ikon via onerror remove; menu baru id>49 tanpa foto statis. Override: menu.foto text + bucket menu-foto publik baca, tulis owner penuh/owner_makanan folder makanan (storage.foldername); upload path kategori/id-timestamp.webp; kompres createImageBitmap+canvas webp q0.76; saveMenu upload dulu lalu satu update (audit satu tindakan); objek lama remove best-effort. fn_audit direproduksi penuh + elsif menu.foto (v_chat false). SW: cache-first murni /menu/ + /storage/v1/object/public/menu-foto/ (immutable). Verifikasi lokal+produksi: 49 img loaded kasir/owner/mobile, override owner tampil lintas perangkat ke kasir, audit menu.foto ada chat 0, penetrasi kasir upload/update DITOLAK, owner_makanan lintas kategori DITOLAK (makanan OK), hapus override kembali null + objek terbuang, regresi 1.16/1.17 lulus, 0 console error. PELAJARAN: (1) skrip uji harus idempoten — run gagal setengah meninggalkan menu uji yang menggeser assertion jumlah; (2) cleanup bucket JANGAN sapu semua objek di produksi (foto asli owner!) — filter pola uji (uji- / id-menu-uji-); (3) f-string Python bocorkan kurawal JS object {count:...} → escape ganda; (4) assertion img harus tunggu complete+naturalWidth (lazy-load). Cleanup: 491 order (482 dummy+9 asli), 49 menu, 0 override, 87 audit asli, 0 objek bucket, 0 sisa uji. Bukti screenshots/foto-1.18.0-*.png; folder review USER /media/cuker/Data/tailshare/foto-menu-review/ (kontak.html).
- **Last Updated By:** AI Agent
- **Last Updated At:** 2026-11-28 13:58 WIB
