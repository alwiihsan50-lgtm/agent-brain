# Spesifikasi Lingkungan Sistem, Reserved Ports, & Remote Access

## 1. Lingkungan Sistem (Environment)
- **Sistem Operasi:** Linux Mint 22.3 (Primary Active Workstation) & Windows 11 (Dual-boot)
- **Domain Utama Cloudflare:** `abbas.my.id`
- **Akun GitHub Utama:** `alwiihsan50-lgtm`
- **Metode Autentikasi Git:** GitHub CLI (`gh`) via HTTPS protocol
- **Root Workspace Linux:** `/home/cuker`
- **Workspace Proyek Drive D:** `/media/cuker/Data/Projects` (Symlink: `~/Projects`)
- **Storage Drive D:** `/media/cuker/Data` (Symlink: `~/Data`)
- **Virtual Storage ext4 Image:** `/media/cuker/Data/mt5-storage.img` (Mount: `/home/cuker/mt5_storage`)
- **Root Workspace Windows:** `C:\Users\alwii\Desktop` & `D:\Projects`

---

## 2. Port Sistem Terpesan Lokal (Local Reserved Ports)
> [!IMPORTANT]
> - **PORT 53317**: Dipesan untuk **TailShare** (`/home/cuker/tailshare`).
> - **PORT 3000 / 3001**: Dipesan untuk **MetaTrader 5 Web GUI VNC** (`exness-mt5` container).
> - **PORT 8080**: Dipesan untuk **MT5 Live Trading Web Dashboard** (`mt5-dashboard` container).
> *(Catatan: Backend Web Push Notification telah dimigrasikan ke **Cloudflare Workers (Serverless)**, sehingga Port 3005 kini bebas).*

Untuk server pengujian atau server pengembang sementara lainnya, **SELALU gunakan port bebas alternatif** seperti `5173`, `3002`, `3080`, `8000`, dll.

---

## 3. Remote Access Multi-Domain: Cloudflare Tunnel (Tanpa Batas Port)

Remote access utama dikonfigurasikan menggunakan **Cloudflare Tunnel (`cloudflared`)** pada domain **`abbas.my.id`**. Setiap aplikasi berjalan pada root subdomain independen tanpa batasan port, tanpa modifikasi path, dan dengan SSL Cloudflare otomatis.

| Layanan / Aplikasi | Target Port Lokal | Subdomain Publik (HTTPS) | Status |
| :--- | :---: | :--- | :---: |
| 📊 **MT5 Live Trading Dashboard** | `http://localhost:8080` | **`https://dashboard.abbas.my.id`** | 🟢 **Live (HTTP 200)** |
| 📂 **TailShare Web UI** | `http://localhost:53317` | **`https://share.abbas.my.id`** | 🟢 **Live (HTTP 200)** |
| 🖥️ **MetaTrader 5 Desktop GUI (VNC)** | `http://localhost:3000` | **`https://vnc.abbas.my.id`** | 🟢 **Live (HTTP 200)** |

### Konfigurasi Cloudflare Tunnel:
* **Service:** `cloudflared.service` (Systemd 24/7 background)
* **Config File:** `/etc/cloudflared/config.yml` & `/home/cuker/.cloudflared/config.yml`
* **Tunnel Name:** `cuker-apps` (`38aa36f2-8898-4c7a-9f75-add2d18513ce`)

---

## 4. Remote Access Cadangan: Tailscale Serve & Funnel

| Metode | URL / Host | Target |
| :--- | :--- | :--- |
| **Tailscale Funnel** | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net` | MT5 Dashboard (`:8080`) |
| **Tailscale Funnel** | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net:8443` | MT5 Web GUI (`:3000`) |
| **Tailscale Funnel** | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net:10000` | TailShare (`:53317`) |
| **Tailscale Private IP** | `http://100.110.205.27:<PORT>` | Akses privat langsung saat Tailscale VPN aktif di HP/Laptop |

---

## 5. Repositori & Proyek Utama dalam Sistem
- `agent-brain`: `https://github.com/alwiihsan50-lgtm/agent-brain` (Shared Memory System)
- `Arsip-IMO`: `https://github.com/alwiihsan50-lgtm/Arsip-IMO` (Active branch: `main` di `D:\Projects\Arsip-IMO`)
- `tailshare`: `https://github.com/alwiihsan50-lgtm/tailshare` (Berada di `/home/cuker/tailshare`, Storage di `/media/cuker/Data/tailshare`)
- `MT5 Docker Bot & Dashboard`: Berada di `/home/cuker/mt5_config`, `/home/cuker/mt5_dashboard`, `/home/cuker/cf-push-backend`, dan `/home/cuker/bot_web_docs`
