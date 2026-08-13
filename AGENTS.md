# SOP & PROTOKOL MEMORI AGENT

File ini adalah aturan wajib bagi SELURUH AI Agent yang mengakses repositori ini.

### 1. PHASE READ (BOOTING)
- Sebelum memulai pekerjaan apa pun, WAJIB membaca `README.md` untuk memahami konteks, riwayat pekerjaan, dan status proyek terkini.
- Bacalah indeks dokumentasi di `docs/`:
  - [`docs/tailshare-linux-mint-installation.md`](docs/tailshare-linux-mint-installation.md) untuk instruksi setup TailShare di Linux Mint.
  - [`docs/drive-d-projects-catalog.md`](docs/drive-d-projects-catalog.md) untuk melihat daftar seluruh repositori dan proyek di Drive `D:\`.
  - [`docs/arsip-imo-project.md`](docs/arsip-imo-project.md) untuk proyek **Arsip-IMO**.
  - [`docs/system-environment-and-ports.md`](docs/system-environment-and-ports.md) untuk batasan port dan lingkungan sistem.
  - [`docs/safari-ios-web-push-notification.md`](docs/safari-ios-web-push-notification.md) untuk panduan & spesifikasi implementasi Web Push Notification (Safari iOS & Browser).
- Jangan mengulang pekerjaan yang sudah dicentang selesai di `README.md`.

### 2. PHASE WRITE (HANDOFF / COMPLETION)
- Setelah selesai mengerjakan tugas, WAJIB memperbarui `README.md`:
  * Centang checklist tugas yang selesai (`[x]`).
  * Tambahkan tugas baru di daftar jika ada.
  * Update kolom `Last Updated By` (nama/platform kamu) dan `Last Updated At` (tanggal & waktu UTC/WIB saat ini).
  * Tuliskan ringkasan singkat perubahan/konteks terbaru di bagian "Ringkasan Konteks".
- Jika membuat dokumentasi teknis, kode, atau skema baru, simpan file-nya di dalam direktori `docs/` (contoh: `docs/api-spec.md`) lalu tautkan/link file tersebut di `README.md`.
