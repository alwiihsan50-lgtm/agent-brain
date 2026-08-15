# Spesifikasi Lingkungan Sistem, Reserved Ports, & Remote Access

## 1. Lingkungan Sistem (Environment)
- **Sistem Operasi:** Linux Mint 22.3 (Primary Active Workstation) & Windows 11 (Dual-boot)
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

## 3. Remote Access: Tailscale Funnel Mapping (Public HTTPS)

> [!NOTE]
> Tailscale Funnel secara teknis **hanya mendukung 3 port publik resmi**: `443`, `8443`, dan `10000`. Akses di luar port tersebut tidak dapat diterima oleh edge server Tailscale global.

Aplikasi lokal diekspos melalui **Tailscale Funnel** pada node `cuker-h610m-hvs-m-2-r2-0` (Domain: `cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net`):

| Tipe | Port Publik | Target App Lokal | URL Akses Remote (HTTPS) | Keterangan |
| :--- | :---: | :---: | :--- | :--- |
| **Funnel (Public HTTPS)** | **`443`** (Default) | `http://127.0.0.1:8080` | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net` | **MT5 Live Trading Dashboard** (PWA Ready) |
| **Funnel (Public HTTPS)** | **`8443`** | `http://127.0.0.1:3000` | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net:8443` | **MetaTrader 5 Web GUI (VNC)** |
| **Funnel (Public HTTPS)** | **`10000`** | `http://127.0.0.1:53317` | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net:10000` | **TailShare Web UI** |

### Akses Privat via Tailscale VPN (Direct IP):
Jika Tailscale VPN aktif di HP/laptop:
- MT5 Dashboard: `http://100.110.205.27:8080`
- MT5 Web GUI: `http://100.110.205.27:3000`
- TailShare: `http://100.110.205.27:53317`

---

## 4. Repositori & Proyek Utama dalam Sistem
- `agent-brain`: `https://github.com/alwiihsan50-lgtm/agent-brain` (Shared Memory System)
- `Arsip-IMO`: `https://github.com/alwiihsan50-lgtm/Arsip-IMO` (Active branch: `main` di `D:\Projects\Arsip-IMO`)
- `tailshare`: `https://github.com/alwiihsan50-lgtm/tailshare` (Berada di `/home/cuker/tailshare`, Storage di `/media/cuker/Data/tailshare`)
- `MT5 Docker Bot & Dashboard`: Berada di `/home/cuker/mt5_config`, `/home/cuker/mt5_dashboard`, `/home/cuker/cf-push-backend`, dan `/home/cuker/bot_web_docs`
