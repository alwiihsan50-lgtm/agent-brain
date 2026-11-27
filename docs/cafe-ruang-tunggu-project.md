# Dokumentasi Proyek: Cafe Ruang Tunggu (POS, Antrean & Menu)

## 1. Metadata Repositori & Lingkungan

- **Nama Proyek:** Cafe Ruang Tunggu — POS, Antrean & Menu
- **Lokasi Lokal:** `D:\Projects\cafe-ruang-tunggu` (`/media/cuker/Data/Projects/cafe-ruang-tunggu`)
- **GitHub Repo:** `alwiihsan50-lgtm/cafe-ruang-tunggu` (private, branch `main`)
- **Produksi:** https://cafe-ruang-tunggu.vercel.app
- **Halaman install:** https://cafe-ruang-tunggu.vercel.app/install
- **Vercel Project:** `cafe-ruang-tunggu` (scope `alwi-ikhsan-s-projects`), Git-connected, production branch `main`
- **Supabase Project:** `cafe ruang tunggu` — ref `svgbotpzgukqurwcrdqd`, region `ap-southeast-1`, Postgres 17.12
- **Firebase:** project `project-998f2`, package Android `com.ruangtunggu.cafe`
- **Tipe Aplikasi:** Web statis (HTML + CSS + JS) + Supabase; PWA; APK Android via Capacitor
- **Status:** Web live (Warm Specialty). Menu owner, PWA, APK 1.1.0, push FCM, dan abstraksi printer sudah aktif. Tugas ditutup atas konfirmasi USER 26 Nov 2026; uji perangkat fisik dilakukan mandiri oleh USER.

## 2. Tech Stack

- **Frontend:** `public/index.html`, `styles.css`, `app.js` (vanilla JS), `config.js` publik.
- **Auth:** Supabase Auth `signInWithPassword`; sesi dipulihkan otomatis.
- **Database:** `menu`, `orders`, `order_items`, `profiles`, `device_tokens`; RPC `buat_order`, `my_role`.
- **Realtime:** publikasi `orders` + `menu`.
- **PWA:** `manifest.webmanifest`, service worker `sw.js` (cache shell), `offline.html`.
- **Android:** Capacitor 8, `@capacitor/push-notifications`, browser, app, status-bar, splash-screen.
- **Push:** Firebase FCM v1 + Edge Function `push-notify` + trigger Postgres `pg_net`.
- **Printer:** ESC/POS via helper HTTP localhost (APK terpisah).
- **Hosting:** Vercel static `public/`; APK di Supabase Storage bucket `apk`.
- **Build CI:** GitHub Actions (`.github/workflows/android.yml`), JDK 21, Android SDK 36.

## 3. Struktur Folder Proyek

```
public/       aplikasi web produksi (+ manifest, sw, ikon, install, version.json)
android/      proyek Capacitor (izin, ikon, signing config, google-services.json)
supabase/     migrations SQL + functions/push-notify
.github/      workflow build APK
prototype/    mockup desain awal (data dummy)
legacy/       snapshot sebelum redesign
docs/         DESIGN-SYSTEM, SUPABASE, DEPLOYMENT, ANDROID, PUSH-NOTIFICATIONS, PRINTER, ROADMAP
screenshots/  bukti visual
scripts/      serve.sh, update-version.mjs
vercel.json   output public/, cleanUrls, header cache/keamanan
```

Folder `prototype/`, `legacy/`, `docs/`, `android/`, `supabase/`, `screenshots/`
tidak ikut ter-publish ke web.

## 4. Peran & Navigasi

| Role | Tab | Catatan |
| --- | --- | --- |
| `owner` | Closing, Pesanan, Menu | Kelola menu (CRUD + soft delete) |
| `kasir` | Order, Pesanan, Closing | Order, cetak struk, export CSV |
| `waiter` | Order, Pesanan | Order + minta struk |
| `dapur` | Antrean | Kanban Baru → Diproses → Siap |

Akun Auth (sandi **tidak** disimpan di repo/dokumen): `owner@`, `kasir@`,
`waiter@`, `dapur@ruangtunggu.com`. Sandi demo masih perlu diganti.
Sejak web 1.8.0: signup publik **ditutup**; akun baru hanya dibuat owner
lewat **Kelola Staf** (`staff-admin`); staf bisa ganti sandi mandiri.

## 5. Status Data Saat Update

- `menu`: 6 baris (aktif), dikelola lewat tab Menu owner.
- `orders`: 2 baris; `id=1` adalah order produksi nyata (`12/aji sumanto`,
  Rp40.000, status `siap`) — **jangan dihapus/diubah**. `id=6` adalah sisa uji
  meja 7 (perlu keputusan user sebelum dibersihkan).
- `order_items`: 6 baris.
- `profiles` / `auth.users`: 4 akun role.
- `device_tokens`: 0 (menunggu APK terpasang).
- Order uji `A7`, `TEST-DEPLOY`, dan `QA-TABLET` sebelumnya sudah dihapus.

## 6. Arah Desain (Warm Specialty)

- Krem `#F7F5F0`, hijau tua `#1F3D33`, terracotta `#C4703C`.
- UI Plus Jakarta Sans; judul Fraunces.
- Layout: sidebar + topbar di desktop, bottom nav + cart sheet di mobile.
- Antrean kanban 3 kolom dengan timer; status >10 menit merah.
- Token lengkap & keputusan per layar: `docs/DESIGN-SYSTEM.md` di repo proyek.

## 7. Fitur Baru (26 Nov 2026)

### 7.1 Kelola menu owner
- Tab `menu` dengan pencarian + filter (Semua/Makanan/Minuman/Nonaktif).
- Tambah/edit lewat bottom sheet; validasi nama 2–80 karakter, harga 0–10 jt.
- Nonaktifkan = soft delete (`aktif=false`); hilang dari kasir/waiter, riwayat aman.
- Hapus permanen hanya bila `order_items` belum pernah memakai menu tersebut.
- Realtime `menu` → kasir/waiter langsung ter-update; item nonaktif dibuang dari
  keranjang dengan notifikasi.
- `buat_order` menolak item nonaktif/tidak ada (bukan lagi silent drop).

### 7.2 PWA & versi
- `manifest.webmanifest` (standalone, ikon 192/512/maskable/apple).
- Service worker cache-first untuk shell, network-first untuk navigasi; halaman
  `offline.html`.
- `/install` berisi unduhan APK + panduan Add to Home Screen iOS.
- `version.json` + banner update: web reload via service worker, APK buka URL
  unduhan bila `versionCode` lebih baru.

### 7.3 APK Android
- Package `com.ruangtunggu.cafe`, minSdk 24 (Android 7), target 36.
- `server.url` memuat web produksi → update web tanpa rebuild.
- Ikon adaptive + splash brand; izin `POST_NOTIFICATIONS`, `VIBRATE`.
- Network security config: cleartext hanya untuk `127.0.0.1`/`localhost` (helper printer).
- Build CI menandatangani dengan PKCS12, unggah ke Storage, update `version.json`.

### 7.4 Push FCM
- Tabel `device_tokens` + RLS per user.
- Edge Function memetakan event → role: order baru (dapur+owner), minta struk
  (kasir+owner), siap (waiter+owner).
- Channel Android `orders`, `receipt`, `ready`; tap notifikasi membuka tab terkait.
- Token invalid dihapus otomatis; logout menghapus token user.

### 7.5 Printer thermal
- Pengaturan di sidebar APK: enabled, port 9123, PIN, lebar 58/80, tes koneksi.
- `buildEscPos()` mengirim struk sebagai base64 ke `POST /print` helper.
- Helper APK terpisah belum dibuat (menunggu printer dibeli); fallback dialog
  print Android tetap aktif. Kontrak lengkap: `docs/PRINTER.md`.

### 7.6 Kelola staf & akun (web 1.8.0, 27 Nov 2026 — menunggu validasi USER)
- **Kelola staf (owner)**: sheet baru dari sidebar/topbar — daftar staf
  (email, peran, status, masuk terakhir), tambah staf (email/nama/peran/
  sandi awal + generator acak), edit nama/peran, reset sandi,
  nonaktifkan/aktifkan (ban). Edge function `staff-admin` (JWT + cek role
  owner di server; anti-lockout: owner tak bisa ban/menurunkan peran diri).
- **Ganti sandi mandiri** (semua peran): sheet "Akun saya" dari chip user
  topbar / sidebar; min 8 karakter + konfirmasi ulang (`auth.updateUser`).
- **Signup publik ditutup**: `disable_signup=true`, `password_min_length=8`
  (Management API). Akun baru hanya via owner.
- **Sandi 5 akun demo TIDAK diubah** (instruksi USER); secret `DEMO_PASSWORD`
  tetap → mode review sekali klik tetap jalan. Reset sandi suatu akun oleh
  owner otomatis menghentikan login sekali klik untuk peran itu.
- E2E produksi 20/20 (buat/login/ganti sandi/reset/ban/unban/403 non-owner/
  anti-lockout/mobile 360px/demo-login 5 peran 200/cleanup cascade).
  Screenshot: `screenshots/staff-*.png`. Commit `6bd28b4` + `61d7ab0`.

## 8. Deployment

- **Web:** push `main` → Vercel build (output `public/`). `vercel.json` mengatur
  cleanUrls, no-cache untuk `config.js`/`version.json`/`sw.js`, cache ikon.
- **APK:** Actions → Build Android APK. Workflow menaikkan `versionCode`,
  build, unggah ke bucket `apk`, lalu commit `public/version.json` ke `main`.
- **Secrets GitHub:** `ANDROID_KEYSTORE_BASE64`, `ANDROID_KEYSTORE_PASSWORD`,
  `ANDROID_KEY_ALIAS`, `ANDROID_KEY_PASSWORD`, `SUPABASE_URL`,
  `SUPABASE_SERVICE_ROLE_KEY`.
- **Supabase secrets:** `FIREBASE_SERVICE_ACCOUNT`, `PUSH_WEBHOOK_SECRET`.
- Detail: `docs/DEPLOYMENT.md`, `docs/ANDROID.md`, `docs/PUSH-NOTIFICATIONS.md`.

## 9. Batasan & Keamanan (Constraints)

1. **Jangan simpan service role key**, service account Firebase, keystore, atau
   sandi akun di repo/dokumen.
2. Anon key memang publik di frontend; tetap patuhi RLS.
3. Skema Supabase hanya diubah lewat migration yang dibahas; `buat_order` sudah
   di-hardening.
4. Hanya isi `public/` yang boleh dipublikasikan.
5. Ganti sandi demo sebelum aplikasi dipakai lebih luas.
6. Jangan hapus/ubah order produksi `id=1`.
7. `minta_struk` harus direset `false` setelah struk dicetak agar permintaan
   berikutnya memicu notifikasi.
8. Keystore APK wajib dicadangkan; kehilangan = tidak bisa update menimpa.

## 10. Verifikasi yang Sudah Dilakukan

- **Login UI produksi:** 4/4 role berhasil, 0 error console.
- **Alur order live:** kasir → dapur → siap → minta struk → closing.
- **Menu owner (Playwright):** tambah, edit, nonaktifkan, filter nonaktif, hapus
  permanen, dan kasir tidak melihat tab Menu — semua lulus.
- **Layout menu:** 320–1440px tanpa overflow (filter membungkus di 320px).
- **PWA:** manifest terpasang, service worker aktif, 11 aset ter-cache, reload
  offline menampilkan shell login.
- **Install page:** 320–1280px tanpa overflow; tombol APK menunggu version.json.
- **Database:** RLS `device_tokens` 4 policy; publikasi realtime `menu` aktif;
  fungsi `buat_order` sudah memuat validasi baru.
- **APK 1.1.0 (versionCode 1):** build CI sukses, terunggah ke Storage,
  `version.json` produksi menunjuk ke berkas itu; SHA-256 cocok dan sertifikat
  v2 sama dengan keystore rilis (`44:E3:40:5C…`). Halaman `/install` live
  menampilkan tombol unduh.
- **FCM backend:** Edge Function `push-notify` ter-deploy; smoke test 401
  (secret salah), token palsu dihapus otomatis (`dropped:1`); trigger
  `orders_push_webhook` + `pg_net` aktif.
- **Belum diverifikasi:** pemasangan APK di perangkat, push end-to-end 3 role,
  banner update, dan helper printer.

## 11. Perintah Cepat

```bash
# Lokal
cd /media/cuker/Data/Projects/cafe-ruang-tunggu
python3 -m http.server 8901 --directory public

# Web deploy
git add -A && git commit -m "..." && git push origin main
vercel ls cafe-ruang-tunggu

# Capacitor
npm run cap:sync
npm run android:build        # butuh JDK 21 + Android SDK

# Build APK via CI
gh workflow run android.yml -f notes="Rilis ..."
gh run watch

# Supabase
supabase functions deploy push-notify --project-ref svgbotpzgukqurwcrdqd --no-verify-jwt
supabase secrets list --project-ref svgbotpzgukqurwcrdqd
```

## 12. Breakpoint Penting

| Rentang | Shell | Keranjang | Grid menu |
| --- | --- | --- | --- |
| ≥1181px | Sidebar | Rail sticky | 3–6 kolom |
| 901–1180px | Sidebar | Cart bar (setelah sidebar) | 2–4 kolom |
| ≤900px | Bottom nav | Cart bar di atas nav | 2–4 kolom |
| ≤340px | Bottom nav | Cart bar | 1 kolom |

Login satu kolom jika lebar ≤800px **atau** tinggi ≤520px.
Screenshot acuan: `screenshots/tablet-768-order.png`,
`tablet-1024-order.png`, `phone-360-order.png`, `tablet-768-cart-sheet.png`,
`phone-landscape-login.png`.

## 13. Pekerjaan Berikutnya

1. USER memasang APK 1.1.0 dan menguji push 3 role pada perangkat fisik.
2. Bila ada laporan notifikasi: periksa `device_tokens`, log `push-notify`, dan
   `net._http_response`; pastikan secret Vault = secret function.
3. Putuskan order uji `id=6` (meja 7) — hapus atau biarkan.
4. Beli printer → bangun APK helper sesuai `docs/PRINTER.md`.
5. Hardening: ganti sandi akun demo **oleh owner sendiri** lewat Kelola Staf
   → Reset sandi (ditunda atas instruksi USER 27 Nov; jangan diubah agent),
   audit RLS, backup schema/data. Signup publik sudah ditutup (web 1.8.0).
6. Peningkatan: foto menu asli, nomor urut harian, custom domain.

> Catatan protokol: seluruh task proyek ini **sudah ditandai selesai** atas
> konfirmasi eksplisit USER pada 26 Nov 2026. Yang tersisa bersifat opsional
> lanjutan (uji perangkat, printer fisik, hardening).