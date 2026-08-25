# 📺 STB RockChip Android 13 Web Remote & Input Architecture

Dokumentasi ini merangkum arsitektur teknis, daemon kontrol backend, virtual input emulation, dan antarmuka web untuk STB RockChip V8_Max (Android 13).

---

## 🏛️ 1. Ikhtisar Arsitektur

```
┌─────────────────────────────────────────────────────────────┐
│                      PENGGUNA (HP / Web Browser)            │
│  - Virtual Cursor 60 FPS (Relative Trackpad Mode)           │
│  - Draggable & Auto-Dismiss 4-Way Scroll Pad                │
│  - True Focal-Point Pinch-to-Zoom & Pan (hingga 4x)         │
│  - Fullscreen HUD & Direct Keyboard Typing                  │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTP REST / WebSocket (Port 8085)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│           LINUX WORKSTATION PROXY (PC Mint)                 │
│  - Service: `stb-remote-proxy.service` (Port 8085)          │
│  - Tailscale Subnet Routing: `192.168.100.0/24`             │
│  - URL Akses Remote: `http://100.110.205.27:8085`           │
└──────────────────────────────┬──────────────────────────────┘
                               │ LAN HTTP (Port 8085 -> STB:8085)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│          STB ROCKCHIP V8_MAX (Android 13 ARM64)             │
│  - Binary: `/vendor/bin/stb_server` & `/data/local/tmp/`    │
│  - Kernel Emulation: Linux `/dev/uinput` (Mouse & Wheel)    │
│  - Screen Capture: Zero-overhead optimized capture loop     │
│  - RAM Cleaner: `am kill-all` + kernel `drop_caches`        │
│  - Tailscale IP: `100.104.214.122` (node: `erza`)           │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚙️ 2. Spesifikasi Daemon Backend (`stb_server`)

Daemon ditulis dalam **Go (Golang)** dan dikompilasi secara cross-compile untuk arsitektur Linux ARM64 (`aarch64`):

- **Lokasi Eksekusi:** `/vendor/bin/stb_server` & `/data/local/tmp/stb_server`
- **Port Layanan:** `8080` (HTTP REST API + Static 4-Tab Web Assets)
- **Persistensi Autostart:** Diinisialisasi secara native via `/vendor/etc/init/stb_server.rc`, `/vendor/etc/init/stb_autostart.rc`, dan skrip `/data/local/tmp/stb_autostart.sh` saat `sys.boot_completed=1`.

### Endpoint API Utama:

| Endpoint | Method | Fungsi |
| :--- | :--- | :--- |
| `/api/screen/frame` | `GET` | Mengambil snapshot layar tunggal beresolusi tinggi (JPEG non-cache). |
| `/api/screen/stream` | `GET` | Streaming snapshot ringan (~2 FPS eco-mode). |
| `/api/mouse/move` | `POST` | Mengirim pergerakan kursor mouse relatif `(dx, dy)` via `/dev/uinput`. |
| `/api/mouse/click` | `POST` | Eksekusi klik kiri (`BTN_LEFT`) pada posisi kursor saat ini. |
| `/api/mouse/scroll`| `POST` | Eksekusi scroll wheel (`REL_WHEEL` / `REL_HWHEEL`) 4 arah. |
| `/api/key` | `POST` | Mengirim keycode Android (Home, Back, D-Pad, Vol+, Vol-, Power). |
| `/api/text` | `POST` | Mengirim teks langsung ke input box yang aktif di TV via `input text`. |
| `/api/app/launch` | `POST` | Membuka aplikasi via *Native Component Launcher* (`cmd package resolve-activity`). |
| `/api/system/clean-ram` | `POST` | Membersihkan memori RAM, `am kill-all`, dan flush pagecache kernel (`drop_caches: 3`). |

---

## 🖱️ 3. Kontrol Kursor Mouse & Gesture (Web UI)

### A. Trackpad-Style Virtual Cursor (60 FPS)
- Elemen kursor visual (`#virtual-mouse-cursor`) dirender langsung di atas canvas/gambar TV di browser pengguna.
- Geseran 1 jari di layar HP bertindak sebagai *touchpad delta*, menggerakkan kursor secara instan tanpa perlu me-refresh snapshot TV saat jari bergerak.
- Refresh frame TV hanya dipicu 1 kali setelah ketukan/klik selesai dieksekusi.

### B. Gestur Interaktif
1. **Ketukan 1 Jari (<12px delta):** Klik Kiri (`BTN_LEFT`) pada posisi kursor di TV dengan animasi gelombang (*ripple*) biru.
2. **Tahan 1 Jari (0.5 detik):** Tombol Kembali / Klik Kanan (`Android BACK keyevent 4`) dengan animasi gelombang amber dan haptic feedback.
3. **Cubit 2 Jari (Pinch to Zoom):** Memperbesar viewport hingga 4x dengan perhitungan *focal-point* `(midX, midY)` tepat di antara dua jari.

### C. Floating 4-Way Scroll Pad
- Widget pop-up kompas navigasi 4 arah:
  - ⬆️ **Atas:** `REL_WHEEL +3`
  - ⬇️ **Bawah:** `REL_WHEEL -3`
  - ⬅️ **Kiri:** `REL_HWHEEL -3`
  - ➡️ **Kanan:** `REL_HWHEEL +3`
- **Fitur Draggable:** Dapat disentuh pada header dan digeser bebas ke posisi mana pun di layar.
- **Auto-Dismiss:** Otomatis tertutup saat pengguna menyentuh/klik area di luar kotak scroll pad.

---

## 🚀 4. Optimalisasi Sistem & Kernel STB (Android 13)

1. **Deep Debloat & Background Services Cleaning:**
   - Pencopotan/Penonaktifan paket Google: GSF (`com.google.android.gsf`), GMS (`com.google.android.gms`), Play Store (`com.android.vending`), AdServices, & Telemetri.
   - Penonaktifan layanan non-TV: CTS Testing Shim (`cts.ctsshim`), Sinkronisasi Kontak/Kalender (`providers.contacts`, `providers.calendar`), Companion Manager (`companiondevicemanager`), Cloud Backup (`sharedstoragebackup`, `backupconfirm`, `wallpaperbackup`), SIM/NFC Secure Element (`com.android.se`), Hotspot OSU (`hotspot2.osulogin`), dan Stock MediaCenter.
   - Sisa penyimpanan internal lega **~6.8 GB** (sebelumnya 3.2 GB).
   - RAM bebas melonjak stabil menjadi **~900 MB – 1.1 GB** (Suhu idle dingin: **~46°C**).
   - **Mekanisme Rollback/Restore:** Skrip pemulihan instan tersedia di STB (`/data/local/tmp/restore_bloatware.sh`) dan di PC Mint (`/home/cuker/.local/bin/stb-restore.sh`). Menjalankan perintah `stb-restore.sh` akan mengembalikan seluruh paket ke status aktif seketika tanpa perlu restart.

2. **Network & Display Tuning:**
   - Wi-Fi Power Save: `disabled` (mencegah spike latency saat streaming bitrate tinggi).
   - GPU Renderer: Menggunakan native `opengl` (kompatibel penuh Mali-450 GPU).
   - Kernel memory swappiness di-tune untuk low memory footprint.

3. **Systemless DNS Filter (Blokir Iklan, Pornografi, & Judi Online):**
   - **Database Domain:** StevenBlack Unified + Porn + Gambling + Fake News (~174.264 baris / 167.388 domain di `/vendor/etc/hosts_family.txt` & `/data/local/tmp/hosts_family.txt`).
   - **Mekanisme:** Bind mount langsung ke `/system/etc/hosts` yang diinisialisasi secara otomatis oleh fungsi `initDNSFilter()` di dalam daemon Go `stb_server` dan `/vendor/bin/stb_autostart.sh`.
   - **Keunggulan:** Zero latency (0.2 ms), 0% CPU/RAM overhead, memblokir iklan & konten dewasa di seluruh aplikasi/browser tanpa merusak koneksi Tailscale VPN (Private DNS diset `off`).

---

## 🌐 5. Akses Remote Jarak Jauh & Arsitektur Keamanan

- **Tailscale Node:** `erza-1` (`100.122.66.85`) — Enkripsi *End-to-End* WireGuard (ChaCha20-Poly1305).
- **Web Remote URL:**
  - Jaringan Lokal: `http://192.168.100.75:8080`
  - Tailscale Global: `http://100.122.66.85:8080`
- **Keamanan & Isolasi Akses:**
  - **Zero Trust Mesh:** Hanya perangkat yang login di tailnet privat `alwiihsan50@gmail.com` yang dapat mengakses STB.
  - **No Public Exposure:** Port 8080 dan port 5555 berada di balik NAT router lokal tanpa *port forwarding*, kebal dari serangan internet publik.
  - **Privileged Management:** Akses kontrol ADB Wireless root terkunci hanya pada PC Mint (`100.110.205.27` / `192.168.100.x`).

---

## 🛠️ 6. Hardware Unbrick, PCB Test Points & UART Console (`RK3528_DDR3_8X4_V12`)

### A. Spesifikasi Hardware PCB
- **Motherboard:** Round Blue PCB bertuliskan `RK3528_DDR3_8X4_V12`
- **SoC:** RockChip RK3528 Quad-Core ARM64
- **eMMC:** Samsung 16 GB eMMC 5.1 BGA-153 (`KLMAG1JENB-B031`)
- **RAM:** 4x DDR3 BGA chips (`SEC`)
- **Wi-Fi:** `LB800D-S HCY Wifi6`

### B. Pemetaan Test Point PCB & Akses Root Hardware
1. **Header `DEBUG` (UART Serial Console):**
   - **Lokasi:** Di samping slot kartu MicroSD (TF).
   - **Pinout (3 Pin):** `GND` | `TX` | `RX` (Tegangan logika: **`3.3V`**).
   - **Koneksi USB-to-TTL (CH340):** `GND` ➡️ `GND`, `RX` Dongle ➡️ `TX` STB, `TX` Dongle ➡️ `RX` STB *(VCC tidak dihubungkan)*.
   - **Baudrate:** **`1500000` (1.5 Mbps)** & fallback **`115200`**.
   - **Skrip Pemantau:** [`/home/cuker/Desktop/stb-remote/rockchip_robust_serial.py`](file:///home/cuker/Desktop/stb-remote/rockchip_robust_serial.py).
2. **Titik Pad `AV` (Recovery Key):**
   - **Lokasi:** Di antara colokan `SPDIF` dan `DCIN`, tepat di samping elco `100 10V VT`.
   - **Fungsi:** Short ke Ground (bodi seng DCIN/USB) saat colok adaptor daya untuk memicu mode Android Recovery.
3. **Titik eMMC Test Point (MaskROM Hardware Override):**
   - **Lokasi:** Deretan titik solder bundar (via) di bawah chip Samsung `KLMAG1JENB` bertuliskan angka `1-14`.
   - **Fungsi:** Menghubungkan pinset di baris titik eMMC saat power masuk memblokir boot eMMC dan memaksa SoC RK3528 masuk ke **Mode MaskROM USB 2.0 (Port Hitam)**.
4. **Alat Otomasi Flasher PC:**
   - Skrip 1-Klik: [`/home/cuker/Desktop/stb-remote/flash-maskrom.sh`](file:///home/cuker/Desktop/stb-remote/flash-maskrom.sh) (Flash otomatis via `rkdeveloptool` untuk partisi asli `recovery.img`, `boot.img`, `dtbo.img`, `vbmeta.img`).
   - Panduan Visual PCB: [`/media/cuker/Data/tailshare/testpoint_guide.jpg`](file:///media/cuker/Data/tailshare/testpoint_guide.jpg) & [`emmc_testpoints_zoom.jpg`](file:///media/cuker/Data/tailshare/emmc_testpoints_zoom.jpg).

### C. Jalur MicroSD Bootable Rescue (SD_Firmware_Tool Method)
1. **Prioritas Boot Silikon RK3528:**
   - Slot Kartu MicroSD (TF) adalah **Prioritas #1** pada silikon BootROM SoC RK3528.
   - Kerusakan partisi `recovery` di eMMC diabaikan saat MicroSD bootable terpasang.
2. **Binari Bootloader Resmi RK3528 Terkompilasi:**
   - Direktori Perkakas: [`/home/cuker/Desktop/stb-remote/rk3528_binaries/`](file:///home/cuker/Desktop/stb-remote/rk3528_binaries/)
   - `idblock.img` (317 KB) — Dibuat via `boot_merger` resmi RockChip dengan DDR3 memory training `rk3528_ddr_1056MHz_D3_LP3_eyescan_v1.13.bin` & `rk3528_spl_v1.06.bin`.
   - `rk3528_loader.bin` (471 KB) — USB download miniloader untuk `rkdeveloptool db` / `upgrade_tool DB`.
   - `upgrade_tool` (Linux x86_64) — Utilitas resmi pabrik RockChip untuk flashing tingkat rendah.
3. **Format Layout MicroSD:**
   - Sektor 64 (Offset 32 KB): `idblock.img` (disuntikkan via `dd if=idblock.img of=/dev/sdX seek=64`).
   - Partisi 1: MBR FAT32 (Offset 16 MB) berisi paket firmware / partisi asli.

### D. Resolusi Akhir & Prosedur Unbrick Teruji (100% Verified)
1. **Pemicu MaskROM Tercepat:**
   - Sambungkan kabel USB Male-to-Male dari PC ke STB (Port Hitam/Biru).
   - Tempelkan pinset dari **Pad `AV` ke Ground (bodi seng)** saat kabel USB dicolokkan ke STB (tahan 2 detik lalu lepas).
2. **Proses Penulisan Otomatis:**
   - Terdeteksi sebagai `Vid=0x2207, Pid=0x350c Loader`.
   - Menggunakan skrip [`fast_flash_maskrom.py`](file:///home/cuker/Desktop/stb-remote/fast_flash_maskrom.py) untuk menulis partisi asli `recovery.img` (96 MB) dan `boot.img` (50 MB) via `rkdeveloptool write-partition`.
   - STB me-reboot normal dan 100% pulih ke menu desktop Android 13 bawaan pabrik.



