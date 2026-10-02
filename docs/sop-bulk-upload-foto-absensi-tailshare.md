# SOP: Bulk Upload Foto Absensi dari TailShare ke Web Arsip-IMO

> 📌 **Tujuan Dokumen:**
> Panduan operasional standar (SOP) untuk AI Agent ketika diminta mengunggah foto absensi bulanan karyawan (seperti Arif atau karyawan lainnya) yang dikirimkan via file ZIP di TailShare ke dalam sistem aplikasi web **Arsip-IMO**.

---

## 🏛️ 1. Identifikasi Sistem & Sumber File

| Komponen | Lokasi / Nilai | Keterangan |
| :--- | :--- | :--- |
| **Folder File TailShare** | `/media/cuker/Data/tailshare/` | Lokasi penerimaan file ZIP dari HP / TailShare PC (Port 40506). |
| **Repositori Web Arsip-IMO** | `/media/cuker/Data/Projects/Arsip-IMO` | Web absensi utama (React 19 + Supabase, Port 3004). |
| **Supabase Project Ref** | `tfrkmgqwxkydpnccgkhr` | Project Supabase aktif: `web-absensi`. |
| **Bucket Storage** | `foto-absensi` | Bucket publik untuk foto absensi karyawan. |
| **Tabel Database** | `absensi` & `karyawan` | Tabel relasional utama data absensi. |

---

## 👥 2. Kamus Master Karyawan (Database ID & Pos)

| ID | Nama Karyawan | Pos | NIPPM | User ID Supabase Auth |
| :---: | :--- | :---: | :---: | :--- |
| **1** | ALWI IKHSAN | Pos 61 | `2610020061` | `1085a6c8-2711-4ad8-9b2d-2509acce8250` |
| **2** | RAMA WAHYUDI | Pos 61 | `2610020066` | `22a9ee6d-d43f-47b6-b5bf-655b85b15350` |
| **3** | IPAN ABDI WITOKO | Pos 61 | `2610020064` | `fc39525b-78d9-488c-b789-29b941d39a51` |
| **4** | M. HUSNI RAHIM | Pos 61 | `2610020065` | `231fa3e4-70d9-458c-afff-6c3cdb214978` |
| **5** | RIAN ANDRIKO | Pos 60 | `2610020068` | `d64db8b4-c6dc-413c-8016-2508c7833617` |
| **6** | REKSI MAILAKI SIBUEA | Pos 60 | `2610020067` | `8a09fc28-667e-4f7e-a602-8bed21c35b28` |
| **7** | **ARIF** | **Pos 60** | `2610020062` | `f208c314-2382-4579-bc35-fa453bf0aa1a` |
| **8** | BUDI KUSUMA | Pos 60 | `2610020063` | `f26e80d2-092c-4028-9cd4-9756dd8c5c34` |

---

## 🔑 3. Akses Database Langsung Tanpa Login Karyawan

Tidak perlu meminta kata sandi karyawan atau login melalui form UI web browser. PC ini telah terautentikasi ke akun Supabase Admin (`alwiihsan50@gmail.com`).

### Cara Mendapatkan `service_role` Key:
Jalankan perintah CLI:
```bash
supabase projects api-keys --project-ref tfrkmgqwxkydpnccgkhr
```
Salin kunci bertipe `service_role`. Kunci ini memiliki hak akses *bypass* Row Level Security (RLS) sehingga skrip lokal dapat mengunggah file ke Storage bucket `foto-absensi` dan melakukan upsert langsung ke tabel `absensi`.

---

## 🔄 4. Siklus Pola Shift & Jadwal Dinas

Pola shift berputar dalam siklus 8 hari (`src/features/JadwalDinas/jadwalDinas.js`):
- **Titik Nol:** `2026-06-01`
- **Pola Shift (8 Hari):** `['malam', 'siang', 'pagi', 'malam', 'siang', 'pagi', 'rest', 'libur']` (Kode: 17, 16, 15, 17, 16, 15, R, L)
- **Offset Karyawan:**
  - **Pos 60:** Arif (offset: 0), Bado (offset: 2), Budi (offset: 4), Reksi (offset: 6)
  - **Pos 61:** Husni (offset: 0), Alwi (offset: 2), Yudi (offset: 4), Ipan (offset: 6)

### Rumus Kalkulasi Shift:
```python
diff_days = (target_date - date(2026, 6, 1)).days
index_hari = ((diff_days % 8) + 8) % 8
shift_index = (index_hari + offset) % 8
shift = POLA[shift_index]
```

---

## 🖼️ 5. Standar Pemrosesan & Kompresi Foto

1. **Format Timemark:** Foto kamera Timemark biasanya berukuran `1200x1600` dengan stempel waktu, tanggal, dan alamat di margin bawah.
2. **Batas Ukuran Web:** Foto wajib dikompresi agar berukuran **`<= 150 KB`** (target ideal 130–145 KB) menggunakan Pillow:
   ```python
   # Kualitas 70-80 pada resolusi asli atau proporsional 927x1236 jika diperlukan
   im.save(buf, format='JPEG', quality=q, optimize=True)
   ```
3. **Format Nama File Storage:**
   `${tanggal}_${karyawan_id}_${uploadId}_1.jpg`
   `${tanggal}_${karyawan_id}_${uploadId}_2.jpg`
4. **Format Kolom `foto_url`:**
   Dua URL publik dipisahkan dengan koma: `url1,url2`.

---

## 🚀 6. Alur Kerja Eksekusi Cepat (Workflow)

```
[File ZIP di TailShare]
          │
          ▼
1. Ekstrak ZIP ke folder scratch/
          │
          ▼
2. Baca Timestamp Timemark & Petakan Tanggal/Shift (Cocokkan dengan Jadwal)
          │
          ▼
3. Kompresi seluruh foto ke target <= 150 KB
          │
          ▼
4. Upload ke Supabase Storage (foto-absensi) & Upsert tabel absensi via service_role key
          │
          ▼
5. Upsert hari Rest & Libur (shift: 'rest'/'libur', foto_url: '')
          │
          ▼
6. Verifikasi rekap 30/30 hari di database & cek web http://localhost:3004
```

---

## 🧪 7. Perintah Verifikasi Cepat (One-Liner)

Untuk memverifikasi kelengkapan absensi bulan tertentu:
```bash
node -e '
const { createClient } = require("@supabase/supabase-js");
const supabase = createClient("https://tfrkmgqwxkydpnccgkhr.supabase.co", "<SERVICE_ROLE_KEY>");
async function check() {
  const { data } = await supabase.from("absensi").select("karyawan_id, tanggal, shift, foto_url").gte("tanggal", "2026-10-01").lte("tanggal", "2026-10-31");
  console.log("Total baris terdata:", data.length);
}
check();
'
```
