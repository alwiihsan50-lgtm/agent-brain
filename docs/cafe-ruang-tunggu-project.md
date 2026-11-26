# Dokumentasi Proyek: Cafe Ruang Tunggu (POS & Antrean)

## 1. Metadata Repositori & Lingkungan

- **Nama Proyek:** Cafe Ruang Tunggu — POS & Antrean
- **Lokasi Lokal:** `D:\Projects\cafe-ruang-tunggu` (`/media/cuker/Data/Projects/cafe-ruang-tunggu`)
- **Remote Git:** belum ada (repo lokal, branch `main`)
- **Produksi:** https://cafe-ruang-tunggu.vercel.app
- **Vercel Project:** `cafe-ruang-tunggu` (scope `alwi-ikhsan-s-projects`)
- **Supabase Project:** `cafe ruang tunggu` — ref `svgbotpzgukqurwcrdqd`, region `ap-southeast-1`, Postgres 17.12
- **Tipe Aplikasi:** Web statis (HTML + CSS + JS) + Supabase Auth/PostgREST/Realtime
- **Status:** Live; redesign **Warm Specialty** selesai sebagai prototipe, **belum di-deploy**

## 2. Tech Stack

- **Frontend produksi:** satu file HTML dengan CSS & JS inline, supabase-js v2 via CDN.
- **Frontend prototipe:** `app/index.html` + `styles.css` + `app.js` (vanilla JS, data dummy).
- **Auth:** Supabase Auth `signInWithPassword`, sesi disimpan client.
- **Database:** tabel `menu`, `orders`, `order_items`, `profiles`; RPC `buat_order`, `my_role`.
- **Realtime:** subscribe `postgres_changes` pada tabel `orders`.
- **Font:** Plus Jakarta Sans + Fraunces (Google Fonts).

## 3. Struktur Folder Proyek

```
app/          prototipe redesign (3 file, data dummy)
legacy/       snapshot persis HTML produksi 26 Nov 2026
docs/         DESIGN-SYSTEM.md, SUPABASE.md, ROADMAP.md
screenshots/  bukti visual desktop & mobile
scripts/      serve.sh
```

## 4. Peran & Navigasi

| Role | Tab | Catatan |
| --- | --- | --- |
| `owner` | Closing, Pesanan | Read-only di daftar pesanan |
| `kasir` | Order, Pesanan, Closing | Membuat order & pembayaran |
| `waiter` | Order, Pesanan | Dapat meminta struk |
| `dapur` | Antrean | Kanban Baru → Diproses → Siap |

Akun Auth (sandi **tidak** disimpan di repo): `owner@`, `kasir@`, `waiter@`,
`dapur@ruangtunggu.com`.

## 5. Status Data Saat Arsip

- `menu`: 6 baris aktif.
- `orders` / `order_items`: 0 baris.
- `profiles` / `auth.users`: 4 baris hasil setup sesi ini.
- Deploy Vercel: Ready, HTTP 200, tanpa env var, Git belum terhubung.
- Realtime & login diverifikasi; tidak ada order nyata yang dibuat saat audit.

## 6. Arah Desain (Warm Specialty)

- Krem `#F7F5F0`, hijau tua `#1F3D33`, terracotta `#C4703C`.
- UI Plus Jakarta Sans; judul Fraunces.
- Layout: sidebar + topbar di desktop, bottom nav + cart sheet di mobile.
- Antrean dapur memakai kanban 3 kolom dengan timer; status >10 menit berwarna merah.
- Token lengkap & keputusan per layar: `docs/DESIGN-SYSTEM.md` di repo proyek.

## 7. Batasan & Keamanan (Constraints)

1. **Jangan simpan service role key** atau sandi akun di repo/dokumen.
2. Anon key memang publik dan tertanam di HTML produksi; tetap patuhi RLS.
3. Skema Supabase tidak boleh diubah saat porting desain.
4. Prototipe `app/` memakai data dummy — jangan diklaim sebagai produksi.
5. Ganti sandi demo sebelum aplikasi dipakai publik.
6. Deploy produksi hanya setelah approval USER.

## 8. Verifikasi yang Sudah Dilakukan

- **Login API:** 4/4 role → 200 OK; profil sesuai role.
- **Login UI produksi:** Chromium headless, 4/4 berhasil, 0 error console.
- **Prototipe:** 4/4 role, alur tambah order → antrean → selesai, 0 error console.
- **Responsif:** tanpa horizontal overflow pada 360/390/768/1024/1180/1280/1440px.
- **Salinan arsip:** checksum `app/` identik dengan workspace asal; server lokal HTTP 200.

## 9. Perintah Cepat

```bash
# Prototipe
cd /media/cuker/Data/Projects/cafe-ruang-tunggu
./scripts/serve.sh                     # http://localhost:8901

# Git proyek
git -C /media/cuker/Data/Projects/cafe-ruang-tunggu log --oneline

# Supabase read-only
supabase projects list
supabase projects api-keys --project-ref svgbotpzgukqurwcrdqd
```

## 10. Pekerjaan Berikutnya

1. Port desain ke produksi tanpa mengubah skema (lihat `docs/ROADMAP.md`).
2. Hardening: ganti sandi, audit RLS, env var Vercel, integrasi Git.
3. Peningkatan: foto menu, export CSV nyata, cetak struk, PWA.

> Catatan protokol: porting ke produksi **belum** dikerjakan. Tugas arsip progres
> ini menunggu konfirmasi USER sebelum ditandai selesai di `README.md`.