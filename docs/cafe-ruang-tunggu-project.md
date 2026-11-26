# Dokumentasi Proyek: Cafe Ruang Tunggu (POS & Antrean)

## 1. Metadata Repositori & Lingkungan

- **Nama Proyek:** Cafe Ruang Tunggu — POS & Antrean
- **Lokasi Lokal:** `D:\Projects\cafe-ruang-tunggu` (`/media/cuker/Data/Projects/cafe-ruang-tunggu`)
- **GitHub Repo:** `alwiihsan50-lgtm/cafe-ruang-tunggu` (private, branch `main`)
- **Produksi:** https://cafe-ruang-tunggu.vercel.app
- **Vercel Project:** `cafe-ruang-tunggu` (scope `alwi-ikhsan-s-projects`), Git-connected, production branch `main`
- **Supabase Project:** `cafe ruang tunggu` — ref `svgbotpzgukqurwcrdqd`, region `ap-southeast-1`, Postgres 17.12
- **Tipe Aplikasi:** Web statis (HTML + CSS + JS) + Supabase Auth/PostgREST/Realtime
- **Status:** Live dengan desain **Warm Specialty**; push ke `main` = deploy otomatis

## 2. Tech Stack

- **Frontend:** `public/index.html` + `public/styles.css` + `public/app.js` (vanilla JS), config publik di `public/config.js`.
- **Auth:** Supabase Auth `signInWithPassword`, sesi dipulihkan otomatis.
- **Database:** tabel `menu`, `orders`, `order_items`, `profiles`; RPC `buat_order`, `my_role`.
- **Realtime:** subscribe `postgres_changes` pada `orders` (order baru, minta struk, perubahan status).
- **Font:** Plus Jakarta Sans + Fraunces (Google Fonts).
- **Hosting:** Vercel static, output directory `public/` lewat `vercel.json`.

## 3. Struktur Folder Proyek

```
public/       aplikasi produksi (satu-satunya folder yang di-deploy)
prototype/    mockup desain awal, data dummy (referensi)
legacy/       snapshot persis HTML produksi sebelum redesign (26 Nov 2026)
docs/         DESIGN-SYSTEM.md, SUPABASE.md, DEPLOYMENT.md, ROADMAP.md
screenshots/  bukti visual prototipe & produksi
scripts/      serve.sh (menyajikan public/)
vercel.json   output public/, cleanUrls, header keamanan
```

Folder `prototype/`, `legacy/`, `docs/`, dan `screenshots/` **tidak** ikut
ter-publish; sudah diverifikasi 404 di domain produksi.

## 4. Peran & Navigasi

| Role | Tab | Catatan |
| --- | --- | --- |
| `owner` | Closing, Pesanan | Read-only di daftar pesanan |
| `kasir` | Order, Pesanan, Closing | Membuat order, cetak struk, export CSV |
| `waiter` | Order, Pesanan | Dapat meminta struk |
| `dapur` | Antrean | Kanban Baru → Diproses → Siap, bunyi saat order baru |

Akun Auth (sandi **tidak** disimpan di repo): `owner@`, `kasir@`, `waiter@`,
`dapur@ruangtunggu.com`.

## 5. Status Data Saat Update

- `menu`: 6 baris aktif.
- `orders`: 1 order produksi nyata (`12/aji sumanto`, Rp40.000, status `siap`) —
  **jangan dihapus**.
- `profiles` / `auth.users`: 4 akun role.
- Order uji `A7` dan `TEST-DEPLOY` sudah dihapus setelah verifikasi.
- Deploy terakhir: build statis 2 detik dari commit Git, status Ready.

## 6. Arah Desain (Warm Specialty)

- Krem `#F7F5F0`, hijau tua `#1F3D33`, terracotta `#C4703C`.
- UI Plus Jakarta Sans; judul Fraunces.
- Layout: sidebar + topbar di desktop, bottom nav + cart sheet di mobile.
- Antrean dapur kanban 3 kolom dengan timer; status >10 menit berwarna merah.
- Token lengkap & keputusan per layar: `docs/DESIGN-SYSTEM.md` di repo proyek.

## 7. Deployment

- Repo GitHub terhubung ke Vercel via GitHub App; branch produksi `main`.
- `vercel.json`: `outputDirectory: public`, `cleanUrls`, header keamanan,
  `config.js` no-cache.
- Tanpa environment variable; URL + anon key ada di `public/config.js`.
- Rollback: promote deployment sehat di dashboard Vercel atau `git revert`.
- Detail: `docs/DEPLOYMENT.md` di repo proyek.

## 8. Batasan & Keamanan (Constraints)

1. **Jangan simpan service role key** atau sandi akun di repo/dokumen.
2. Anon key memang publik dan tertanam di frontend; tetap patuhi RLS.
3. Skema Supabase tidak boleh diubah tanpa pembahasan terpisah.
4. Hanya isi `public/` yang boleh dipublikasikan; folder internal jangan
   dipindah ke `public/`.
5. Ganti sandi demo sebelum aplikasi dipakai lebih luas.
6. Jangan hapus atau ubah order produksi nyata saat pengujian.

## 9. Verifikasi yang Sudah Dilakukan

- **Login UI produksi:** 4/4 role berhasil, 0 error console.
- **Alur order live:** kasir submit → tiket muncul realtime di dapur → diproses
  → siap → waiter minta struk → badge muncul realtime di kasir → closing.
- **Responsif:** tanpa horizontal overflow pada 360/390/768/1024/1180/1280/1440px.
- **Mobile:** cart bar tidak menutupi bottom nav; bottom sheet bisa dibuka dan
  ditutup via Escape.
- **Deploy:** push `main` memicu build Vercel otomatis; halaman live HTTP 200;
  aset `styles.css`, `app.js`, `config.js` HTTP 200; folder internal 404.
- **Data:** order uji dibersihkan; order produksi tidak tersentuh.

## 10. Perintah Cepat

```bash
# Lokal
cd /media/cuker/Data/Projects/cafe-ruang-tunggu
./scripts/serve.sh                     # http://localhost:8901 (data Supabase live)

# Deploy
git add -A && git commit -m "..." && git push origin main
vercel ls cafe-ruang-tunggu            # cek status build

# Git proyek
git -C /media/cuker/Data/Projects/cafe-ruang-tunggu log --oneline

# Supabase read-only
supabase projects list
supabase projects api-keys --project-ref svgbotpzgukqurwcrdqd
```

## 11. Pekerjaan Berikutnya

1. Hardening: ganti sandi 4 akun demo, audit RLS, pertimbangkan env var.
2. Peningkatan: foto menu asli, nomor urut harian, PWA/offline, custom domain.
3. Backup berkala schema + data menu.

> Catatan protokol: pekerjaan porting & integrasi Git **sudah selesai dan
> diverifikasi**, tetapi task di `README.md` agent-brain masih `[ ]` sampai
> USER memberi konfirmasi eksplisit.