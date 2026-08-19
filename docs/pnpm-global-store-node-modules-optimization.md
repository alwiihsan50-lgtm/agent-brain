# Standardisasi PNPM & Optimasi Shared node_modules Global Store

## 1. Ringkasan & Tujuan Arsitektur
Sebelumnya, setiap proyek JavaScript/TypeScript (Node.js) mengunduh dan menyimpan duplikat folder `node_modules` secara mandiri menggunakan `npm`. Hal ini menghabiskan ruang penyimpanan (*disk space*) ratusan megabyte hingga puluhan gigabyte di workstation lokal.

Untuk menghemat disk secara drastis, meningkatkan kecepatan instalasi, dan mencegah duplikasi paket antar-repositori, seluruh ekosistem workstation telah distandardisasi menggunakan **`pnpm` (Performant npm)** dengan **Content-addressable Global Store**.

---

## 2. Spesifikasi Teknis Global Store

- **Package Manager Utama:** `pnpm` (Versi: `11.22.0`+)
- **Lokasi Node Binary:** `/home/cuker/.local/bin/node` (v22.23.2)
- **Lokasi PNPM Binary:** `/home/cuker/.local/bin/pnpm`
- **Lokasi Global Content-Addressable Store:**
  ```bash
  /home/cuker/.local/share/pnpm/store/v11
  ```
- **Mekanisme Tautan:** *Hard link* & *Symlink* dari virtual store (`node_modules/.pnpm`) ke content-addressable store.
- **Efisiensi:** Jika 10 proyek menggunakan dependensi versi yang sama (misal: `react@18.2.0`, `express@5.2.1`, `hono@4.13.3`, `typescript@5.9.3`), file fisik hanya tersimpan **1 kali** di disk.

---

## 3. Repositori yang Telah Dimigrasikan

| Repositori / Direktori Proyek | Framework / Stack | Status Migrasi |
| :--- | :--- | :---: |
| `/home/cuker/tailshare` | Electron, Express, Multer | 🟢 Migrated to `pnpm` |
| `/home/cuker/SIMPKK-DIGITAL` | React / Next.js Stack | 🟢 Migrated to `pnpm` |
| `/home/cuker/push-backend` | Cloudflare Workers, Vitest, Wrangler | 🟢 Migrated to `pnpm` |
| `/home/cuker/mt5_storage/cf-push-backend` | Hono, Web Push | 🟢 Migrated to `pnpm` |
| `/home/cuker/bot_push_server/backend` | Express, Web Push, CORS | 🟢 Migrated to `pnpm` |
| `/home/cuker/cf-push-backend` | Hono, WebCrypto Web Push | 🟢 Migrated to `pnpm` |

---

## 4. SOP & Aturan Kerja AI Agent (Wajib)

Seluruh AI Agent dan developer di workstation ini **WAJIB** mematuhi aturan berikut saat berurusan dengan proyek Node.js:

1. **Gunakan `pnpm` Sebagai Default:**
   - DILARANG menjalankan `npm install` atau `yarn install` secara sembarangan di repositori lokal.
   - Selalu gunakan `pnpm install` (atau `pnpm i`).
2. **Menambah / Menghapus Package:**
   - Tambah dependensi produksi: `pnpm add <package>`
   - Tambah dependensi development: `pnpm add -D <package>`
   - Hapus dependensi: `pnpm remove <package>`
3. **Menjalankan Script Proyek:**
   - `pnpm dev`, `pnpm build`, `pnpm start`, `pnpm test`
4. **Membersihkan Unused Packages Global Store:**
   - Jalankan `pnpm store prune` sewaktu-waktu untuk membuang paket yang sudah tidak dirujuk oleh proyek mana pun di sistem.
