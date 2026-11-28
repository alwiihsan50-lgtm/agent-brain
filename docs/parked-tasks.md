# 🅿️ Tugas Disisihkan (Parked Tasks)

> Disisihkan atas instruksi USER pada **27 November 2026** ("sisihkan dulu semua tugas yang belum live — ada list prioritas baru").
> Seluruh tugas di bawah **TIDAK dihapus dan TIDAK dianggap selesai** — status tetap `- [ ]`.
> Untuk mengaktifkan kembali: pindahkan baris tugas ke bagian `## 🚀 Status Tugas Aktif` di `README.md` (atau minta agent mengembalikannya).

## Cafe Ruang Tunggu (6 tugas — belum live penuh per verifikasi 27 Nov 2026)

- [ ] **Cafe: perluas ketahanan offline (cache antrean dapur baca-saja, rencana jaringan cadangan)**

- [ ] **Cafe: laporan mingguan/bulanan owner + nomor urut harian di struk**

- [ ] **Cafe: monitoring error ringan (Sentry/log) + smoke test CI web**

- [ ] **Cafe: fitur batal/void order dengan izin per-role + alasan + notifikasi + tampilan closing**

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

- ⚠️ **Mode review login sekali klik (web 1.7.0, diperluas 1.15.0 jadi 6 peran) masih LIVE** (`demoLogin: true` di `public/config.js`). Saat launch: `supabase secrets unset DEMO_PASSWORD DEMO_PASSWORD_MAKANAN --project-ref svgbotpzgukqurwcrdqd` dan `demoLogin: false` lalu deploy + bersihkan akun demo.
- ⚠️ **SAAT LAUNCH: login ulang relay RT Print Helper dengan akun staf asli** (ditambahkan 28 Nov atas konfirmasi USER). Relay helper login memakai akun staf; bila akun demo dihapus atau sandinya direset saat launch, refresh token helper invalid → cetak dari jauh (waiter/PWA/iOS) mati diam-diam. Langkah: buka helper di tablet kasir → kartu Relay cloud → login akun kasir/owner asli → pastikan status ONLINE → uji satu cetak dari perangkat waiter.
- ⚠️ **Data dummy (482 order per 28 Nov) TETAP di produksi atas pilihan USER 28 Nov** ("centang task, dummy tetap") sampai permintaan hapus atau launch. Cleanup: SQL header `seed-dummy-20261128.sql` + sequence `setval(max(id)+1)` (bukan restart 1 — order asli id 15 ada).
