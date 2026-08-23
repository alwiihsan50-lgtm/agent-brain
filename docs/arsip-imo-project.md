# Dokumentasi Proyek: Arsip-IMO

## 1. Metadata Repositori & Cabang
- **GitHub Repo:** `alwiihsan50-lgtm/Arsip-IMO`
- **Active / Primary Branch:** `main` (branch tunggal stabil, seluruh branch lama telah dibersihkan)
- **Lokasi Lokal:** `D:\Projects\Arsip-IMO` (`/media/cuker/Data/Projects/Arsip-IMO`)
- **Tipe Aplikasi:** Aplikasi presensi / absensi karyawan utama (`src/App.jsx`)
- **Aplikasi Web Admin:** Jangan diubah kecuali ada permintaan eksplisit dari pengguna.

## 2. Tech Stack
- **Frontend Framework:** React 19, Vite
- **Styling:** Tailwind CSS
- **State Management:** Zustand (`src/store/useAppStore.js`)
- **Database & Backend:** Supabase

## 3. Aturan & Batasan Permanen (Constraints)
1. **Database Schema:** DILARANG mengubah skema atau struktur database.
2. **Format URL Foto (`foto_url`):** Tetap gunakan format *comma-separated string* untuk menyimpan dan membaca multiple photo URL.
3. **Absensi (`absensi`):** Pertahankan fungsi dan logika absensi yang sudah berjalan lancar.
4. **Scoping:** Perubahan kode harus tetap fokus pada fitur yang diminta.
5. **Kredensial:** DILARANG melakukan commit file `.env`, nilai token, atau rahasia lainnya.

## 4. Arsitektur Navigasi Aplikasi
- State navigasi global dikelola oleh Zustand di `src/store/useAppStore.js`.
- `currentView: 'main'` -> Menampilkan kalender absensi utama.
- `currentView: 'serah-terima'` -> Menampilkan tampilan Serah Terima (`src/features/SerahTerima/SerahTerimaView.jsx`).
- `src/App.jsx` membuka Serah Terima via `handleOpenSerahTerima` (memastikan karyawan terisi sesuai karyawan yang sedang login).
- Tombol **Kembali** pada `SerahTerimaView` harus selalu memanggil `setCurrentView('main')`.

## 5. Tata Letak Grid Kontrol Kalender (2x2 Grid)
Kontrol navigasi kalender menggunakan layout 2 baris x 2 kolom:

| Posisi | Kontrol / Fungsi |
| --- | --- |
| Top Left (Atas Kiri) | Bulan Sebelumnya (Previous month) |
| Bottom Left (Bawah Kiri) | Bulan Sekarang (Current month) |
| Top Right (Atas Kanan) | Jadwal Dinas |
| Bottom Right (Bawah Kanan) | Serah Terima |

- Ukuran teks untuk keempat tombol grid diset eksplisit sebesar `12px`.
- Tombol Password dan Logout tetap berada di header atas.

## 6. Verifikasi & Prosedur Pengujian
- **Build Verification:** Selalu jalankan `npm run build` setelah perubahan kode.
- **Linting:** Jalankan `npm run lint` jika relevan (catatan: branch saat ini memiliki temuan lint bawaan lama yang tidak mengganggu).
- **Dependency Lock:** `npm ci` bisa gagal jika `package.json` dan `package-lock.json` belum tersinkronisasi. Jangan mengupdate lockfile kecuali diminta.
- **Git Diff:** Periksa `git diff` untuk memastikan tidak ada file yang tidak relevan ikut ter-commit.

## 7. Workflow Pengiriman (Delivery)
- Commit perubahan yang telah diverifikasi dengan pesan commit format *Conventional Commits*.
- Push commit langsung ke `origin/main` (kecuali pengguna minta sebaliknya).
- Laporkan hasil build dan Commit SHA yang telah dipush ke pengguna.

## 8. Riwayat Commit Terkait
- `cdbc759` - Restore pure in-browser Timemark date adjustment (HTML5 Canvas + EXIF piexifjs) without PC backend dependency.
- `9c63a0e` - Add graphify knowledge graph and automated GitHub Actions workflow.
- `853dde9` - Restored Serah Terima navigation.
- `4ceb0d6` - Reorganized calendar navigation into a 2x2 grid.
- `a7adc4f` - Set navigation grid text to `12px`.
