# 🅿️ Tugas Disisihkan (Parked Tasks)

> Disisihkan atas instruksi USER pada **27 November 2026** ("sisihkan dulu semua tugas yang belum live — ada list prioritas baru").
> Seluruh tugas di bawah **TIDAK dihapus dan TIDAK dianggap selesai** — status tetap `- [ ]`.
> Untuk mengaktifkan kembali: pindahkan baris tugas ke bagian `## 🚀 Status Tugas Aktif` di `README.md` (atau minta agent mengembalikannya).

## Cafe Ruang Tunggu (8 tugas — belum live penuh per verifikasi 27 Nov 2026)

- [ ] **Cafe: perluas ketahanan offline (cache antrean dapur baca-saja, rencana jaringan cadangan)**

- [ ] **Cafe: laporan mingguan/bulanan owner + nomor urut harian di struk**

- [ ] **Cafe: monitoring error ringan (Sentry/log) + smoke test CI web**

- [ ] **Cafe: helper printer thermal APK dan uji printer fisik sebelum buka**

- [ ] **Cafe: fitur batal/void order dengan izin per-role + alasan + notifikasi + tampilan closing**

- [ ] **Cafe: backup otomatis Supabase schema+data dan uji restore berkala**

- [ ] **Cafe: audit & ketatkan RLS orders/profiles (pembatasan per-role/per-kolom + jejak audit perubahan)**

- [ ] **Cafe Ruang Tunggu — hardening: ganti sandi 4 akun demo, audit RLS, & evaluasi env var Vercel**
  - Catatan: sebagian tercover web 1.8.0 (kelola staf + ganti sandi mandiri, dikonfirmasi USER 27 Nov). Ganti sandi demo ditunda atas instruksi USER — owner reset mandiri via Kelola Staf. Sisa terbuka: audit RLS & evaluasi env var Vercel.

## Non-Cafe (4 tugas)

- [ ] **Implementasi Proteksi Re-entry Pasca-TP (10m Cooldown), Anti-Same-Bar M5, & State Persistence Cooldown Pasca-SL di bot_trending.py v6.2 (Akun 1 443003218)**

- [ ] **Uji Coba Live Bot Continuous SAR Trailing v2.0 (Jarak Stop $0.50 USD, Trailing Trigger $1.50 USD, XAUUSDm Lot 0.01) di MT5 Akun 2 Demo (463880423)**

- [ ] **Penyusunan Modul Pembelajaran Lengkap Klaster 1 (Dasar Komputer & Sistem Operasi) Format PDF di TailShare**

- [ ] **Review Audit Paritas Live bot_trending.py v6.2 (PF riil 1.24 vs klaim 1.40, bias re-entry Open-bar di engine lama, DD 2% HWM ~46%) & putuskan penurunan risiko 2%→1% di Akun 1 (443003218)**

---

## Pengingat terkait (bukan tugas parkir)

- ⚠️ **Mode review login sekali klik (web 1.7.0) masih LIVE** (`demoLogin: true` di `public/config.js`). Setelah USER selesai review, matikan kill switch: `supabase secrets unset DEMO_PASSWORD --project-ref svgbotpzgukqurwcrdqd` dan/atau `demoLogin: false` lalu deploy.
