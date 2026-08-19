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

- **Lokasi Eksekusi:** `/vendor/bin/stb_server` (dengan symlink/fallback di `/data/local/tmp/stb_server`)
- **Port Layanan:** `8085` (HTTP REST API + Static Web Assets)
- **Persistensi Autostart:** Dijalankan saat booting via `/data/local/tmp/stb_autostart.sh` dan init daemon.

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

1. **Deep Debloat:**
   - Pencopotan 23 paket streaming berat, Google Play Services (`com.google.android.gms`), dan framework telemetri.
   - Sisa penyimpanan internal lega **~6.8 GB** (sebelumnya 3.2 GB).
   - RAM bebas meningkat stabil menjadi **~1.0 GB – 1.1 GB** (Suhu idle dingin: **~46°C**).

2. **Network & Display Tuning:**
   - Wi-Fi Power Save: `disabled` (mencegah spike latency saat streaming bitrate tinggi).
   - GPU Renderer: Menggunakan native `opengl` (kompatibel penuh Mali-450 GPU).
   - Kernel memory swappiness di-tune untuk low memory footprint.

---

## 🌐 5. Akses Remote Jarak Jauh (Tailscale)

- **Node Name:** `erza` (`100.104.214.122`)
- **Proxy Endpoint Linux Mint:** `http://100.110.205.27:8085`
- **Local LAN STB:** `http://192.168.100.61:8085`
