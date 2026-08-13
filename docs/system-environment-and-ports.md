# Spesifikasi Lingkungan Sistem & Port Terpesan

## 1. Lingkungan Sistem (Environment)
- **OS:** Windows
- **Akun GitHub Utama:** `alwiihsan50-lgtm`
- **Metode Autentikasi Git:** GitHub CLI (`gh`) via HTTPS protocol
- **Root Workspace:** `C:\Users\alwii\Desktop`

## 2. Port Sistem Terpesan (Reserved Ports)
> [!IMPORTANT]
> - **PORT 53317**: Dipesan secara khusus untuk **TailShare** (`/home/cuker/tailshare` / `C:\Users\alwii\Desktop\tailshare`).
> - **PORT 3000**: Dipesan untuk **MetaTrader 5 Web VNC GUI** (`exness-mt5` container).
> - **PORT 3005**: Dipesan untuk **Web Push Notification Backend Server** (`/home/cuker/bot_push_server`).
> **DILARANG keras** menghentikan, mematikan, atau mengikat (bind) aplikasi web / dev server lain ke port-port di atas tanpa penyesuaian.

Untuk server pengujian atau server pengembang sementara lainnya, **SELALU gunakan port bebas alternatif** seperti `3001`, `5173`, `8080`, `8000`, dll.

## 3. Repositori & Proyek Utama dalam Sistem
- `agent-brain`: `https://github.com/alwiihsan50-lgtm/agent-brain` (Shared Memory System)
- `Arsip-IMO`: `https://github.com/alwiihsan50-lgtm/Arsip-IMO` (Active branch: `Beta2-redesign`)
- `tailshare`: `https://github.com/alwiihsan50-lgtm/tailshare` (Berada di `/home/cuker/tailshare`, Storage di `/media/cuker/Data/tailshare`)
- `MT5 Docker Bot & Push Notification`: Berada di `/home/cuker/mt5_config`, `/home/cuker/bot_push_server`, dan `/home/cuker/bot_web_docs`
