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
> - **PORT 40506**: Dipesan untuk **TailShare** (`/home/cuker/tailshare`).
> - **PORT 3000 / 3001**: Dipesan untuk **MetaTrader 5 Web GUI VNC** (`exness-mt5` container).
> - **PORT 8080**: Dipesan untuk **MT5 Live Trading Web Dashboard** (`mt5-dashboard` container).
> *(Catatan: Backend Web Push Notification telah dimigrasikan ke **Cloudflare Workers (Serverless)**, sehingga Port 3005 kini bebas).*

Untuk server pengujian atau server pengembang sementara lainnya, **SELALU gunakan port bebas alternatif** seperti `5173`, `3002`, `3080`, `8000`, dll.

---

## 3. Remote Access Utama: Cloudflare Tunnel Multi-Subdomain

Remote access publik utama dikelola oleh **Cloudflare Tunnel (`cloudflared.service` 24/7)** pada domain **`abbas.my.id`**:

| Layanan / Aplikasi | Target Port Lokal | Subdomain Publik (HTTPS) | Status |
| :--- | :---: | :--- | :---: |
| 📊 **MT5 Live Trading Dashboard** | `http://localhost:8080` *(mentari-server)* | **`https://dashboard.abbas.my.id`** | 🟢 **Live (HTTP 200)** |
| 🖥️ **MetaTrader 5 Desktop GUI (VNC)** | `https://localhost:3001` *(mentari-server)* | **`https://mt5.abbas.my.id`** *(alias: `vnc`)* | 🟢 **Live (HTTP 200)** |
| 🏠 **CasaOS Web GUI Dashboard** | `http://localhost:80` *(mentari-server)* | **`https://server.abbas.my.id`** / **`https://casa.abbas.my.id`** | 🟢 **Live (HTTP 200)** |
| 📁 **TailShare Web UI** | `http://localhost:40506` *(Windows Workstation / Linux)* | **`https://share.abbas.my.id`** | 🟢 **Live (HTTP 200)** |

### Konfigurasi Cloudflare Tunnel:
* **Tunnel mentari-server:** `mentari-tunnel` (`6cd14b2e-12e7-44f2-b138-d8c1684690a6`) mengelola `dashboard`, `mt5`, `vnc`, `server`, dan `casa.abbas.my.id`.
* **Security Layer:** Cloudflare Zero Trust Access (PIN OTP `alwiihsan50@gmail.com`, Session 1 Bulan / 730 Jam).

---

## 4. Remote Access Privat: Tailscale MagicDNS & Direct Mesh
* **MagicDNS Tailnet Suffix:** `tail474821.ts.net` (Aktif 100%)
* **Keunggulan MagicDNS:** Resolusi nama domain otomatis antar-perangkat baik saat di rumah (LAN) maupun di luar rumah (Cellular / Public Wi-Fi) tanpa perlu menghafal atau mengubah IP address.

### 🌐 Pemetaan Domain MagicDNS & Port Aplikasi:
| Perangkat (Node) | Hostname / FQDN MagicDNS | IP Tailscale | Aplikasi / Service & URL Akses |
| :--- | :--- | :--- | :--- |
| **Linux Workstation** | `cuker-h610m-hvs-m-2-r2-0`<br>`cuker-h610m-hvs-m-2-r2-0.tail474821.ts.net` | `100.110.205.27` | - **TailShare:** `http://cuker-h610m-hvs-m-2-r2-0:40506`<br>- **MT5 Dashboard:** `http://cuker-h610m-hvs-m-2-r2-0:8080`<br>- **MT5 GUI (VNC):** `http://cuker-h610m-hvs-m-2-r2-0:3000`<br>- **STB Remote Proxy:** `http://cuker-h610m-hvs-m-2-r2-0:8085`<br>- **SSH:** `ssh cuker@cuker-h610m-hvs-m-2-r2-0` |
| **STB Android 13** | `erza`<br>`erza.tail474821.ts.net` | `100.104.214.122` | - **STB Remote Server:** `http://erza:8080`<br>- **ADB Remote:** `adb connect erza:5555` |
| **Server Debian** | `mentari-server`<br>`mentari-server.tail474821.ts.net` | `100.109.208.27` | - **CasaOS Dashboard:** `http://mentari-server`<br>- **SSH:** `ssh mentari@mentari-server` |
| **iPhone** | `ip11`<br>`ip11.tail474821.ts.net` | `100.71.123.61` | - Akses client / PWA Safari ke seluruh MagicDNS URL |
| **Windows Workstation**| `cuker`<br>`cuker.tail474821.ts.net` | `100.99.188.44` | - Dual-boot Windows node |

---

## 5. Repositori & Proyek Utama dalam Sistem
- `agent-brain`: `https://github.com/alwiihsan50-lgtm/agent-brain` (Shared Memory System)
- `Arsip-IMO`: `https://github.com/alwiihsan50-lgtm/Arsip-IMO` (Active branch: `main` di `D:\Projects\Arsip-IMO`)
- `tailshare`: `https://github.com/alwiihsan50-lgtm/tailshare` (Berada di `/home/cuker/tailshare`, Storage di `/media/cuker/Data/tailshare`)
- `MT5 Docker Bot & Dashboard`: Berada di `/home/cuker/mt5_config`, `/home/cuker/mt5_dashboard`, `/home/cuker/cf-push-backend`, dan `/home/cuker/bot_web_docs`
