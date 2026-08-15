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

## 3. Remote Access: Tailscale Serve & Funnel Mapping

Aplikasi lokal diekspos melalui **Tailscale Serve & Funnel** pada node `cuker-h610m-hvs-m-2-r2-0` (Domain: `cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net`).

| Tipe | Port Publik / Tailnet | Target App Lokal | URL Akses | Keterangan |
| :--- | :---: | :---: | :--- | :--- |
| **Funnel + Serve** | **`40506`** | `http://127.0.0.1:53317` | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net:40506` | **TailShare Web UI** |
| **Funnel + Serve** | **`40507`** | `http://127.0.0.1:8080` | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net:40507` | **MT5 Live Trading Dashboard** |
| **Funnel + Serve** | **`40508`** | `http://127.0.0.1:3000` | `https://cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net:40508` | **MetaTrader 5 Web GUI (VNC)** |
| **Root (443)** | *Kosong* | - | - | *Dikosongkan sesuai konfigurasi pengguna* |

---

## 4. Repositori & Proyek Utama dalam Sistem
- `agent-brain`: `https://github.com/alwiihsan50-lgtm/agent-brain` (Shared Memory System)
- `Arsip-IMO`: `https://github.com/alwiihsan50-lgtm/Arsip-IMO` (Active branch: `main` di `D:\Projects\Arsip-IMO`)
- `tailshare`: `https://github.com/alwiihsan50-lgtm/tailshare` (Berada di `/home/cuker/tailshare`, Storage di `/media/cuker/Data/tailshare`)
- `MT5 Docker Bot & Dashboard`: Berada di `/home/cuker/mt5_config`, `/home/cuker/mt5_dashboard`, `/home/cuker/cf-push-backend`, dan `/home/cuker/bot_web_docs`
