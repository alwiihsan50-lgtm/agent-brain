# Cloudflare Manager: Arsitektur, Kredensial & Pemetaan DNS

Dokumentasi ini mencatat arsitektur terpadu manajemen Cloudflare pada domain **`abbas.my.id`** dan akun `alwiihsan50@gmail.com`.

---

## 1. Kredensial & Autentikasi API

Seluruh kredensial Cloudflare disimpan terenkripsi End-to-End (E2EE) di **Infisical Secret Vault** pada environment `dev` dan `prod`:

| Kunci Rahasia | Nilai / ID Terverifikasi | Deskripsi |
| :--- | :--- | :--- |
| **`CLOUDFLARE_API_TOKEN`** | `cfut_...` (`id: c9e67abad20a8345d209c28f1879efa3`) | Token API kustom dengan **Full Access (100%)** tanpa batasan IP. |
| **`CLOUDFLARE_ACCOUNT_ID`** | `186a8cf86076dbb4201bbc22b0236e7c` | Akun Cloudflare utama `Alwiihsan50@gmail.com`. |
| **`CLOUDFLARE_ZONE_ID`** | `d258eb92742b2f14fe9aa53d92e07791` | Zone ID domain `abbas.my.id`. |
| **`CLOUDFLARE_ACCESS_APP_ID`** | `b37ecff4-01f8-4deb-80b9-b9f0b4bd9b53` | Cloudflare Zero Trust Access Application ID. |

---

## 2. Cakupan Hak Akses Terverifikasi (*Full Scope Audit*)

Berdasarkan audit live probing API, token memiliki hak akses berikut:

- 🟢 **DNS & Zone Management:** Read & Edit (Tambah, Ubah, Hapus DNS Records).
- 🟢 **Zone Settings:** Read & Edit (56 konfigurasi zone aktif).
- 🟢 **SSL/TLS & Edge Certificates:** Read & Edit (Full/Strict Encryption).
- 🟢 **WAF & Security Rulesets:** Read & Edit (Firewall, Bot Fight Mode, Rate Limiting).
- 🟢 **Cloudflare Tunnels (`cloudflared`):** Read & Edit (5 Tunnel terdaftar).
- 🟢 **Zero Trust Access:** Read & Edit (Aplikasi, Kebijakan OTP Email, Durasi Sesi).
- 🟢 **Workers & Serverless:** Read & Edit (Scripts, Routes, Workers AI, Vectorize).
- 🟢 **Workers KV & D1 Storage:** Read & Edit (Key-Value CRUD & SQL Database).
- 🟢 **Page Rules & Transform Rules:** Read & Edit (Redirects & Cache Rules).

---

## 3. Pemetaan DNS Records Aktif (`abbas.my.id`)

| Subdomain / Host | Tipe | Target Tujuan | Proxy (CDN/WAF) | Layanan / Perangkat Terkait |
| :--- | :---: | :--- | :---: | :--- |
| `dashboard.abbas.my.id` | CNAME | `6cd14b2e-...cfargotunnel.com` | 🟠 True | **MT5 Live Trading Dashboard** (`mentari-server` Port 8080) |
| `mt5.abbas.my.id` | CNAME | `6cd14b2e-...cfargotunnel.com` | 🟠 True | **MetaTrader 5 GUI VNC** (`mentari-server` Port 3001) |
| `vnc.abbas.my.id` | CNAME | `6cd14b2e-...cfargotunnel.com` | 🟠 True | **Alias VNC MT5** (`mentari-server` Port 3001) |
| `server.abbas.my.id` | CNAME | `6cd14b2e-...cfargotunnel.com` | 🟠 True | **CasaOS Web GUI** (`mentari-server` Port 80) |
| `casa.abbas.my.id` | CNAME | `6cd14b2e-...cfargotunnel.com` | 🟠 True | **Alias CasaOS Dashboard** (`mentari-server` Port 80) |
| `share.abbas.my.id` | CNAME | `38aa36f2-...cfargotunnel.com` | 🟠 True | **TailShare File Transfer** (`workstation` Port 40506) |
| `desk.abbas.my.id` | CNAME | `38aa36f2-...cfargotunnel.com` | 🟠 True | **RustDesk Web Client** (`workstation`) |
| `relay.abbas.my.id` | CNAME | `38aa36f2-...cfargotunnel.com` | 🟠 True | **RustDesk Relay Server** |
| `relay.rustdesk.abbas.my.id` | CNAME | `38aa36f2-...cfargotunnel.com` | 🟠 True | **RustDesk Relay Subdomain** |
| `rustdesk.abbas.my.id` | CNAME | `38aa36f2-...cfargotunnel.com` | 🟠 True | **RustDesk ID/Rendezvous Server** |
| `push.abbas.my.id` | CNAME | `97adeb5f-...cfargotunnel.com` | 🟠 True | **Push Gateway Legacy** |
| `api.abbas.my.id` | CNAME | `061290b2-...cfargotunnel.com` | 🟠 True | **API Gateway Endpoint** |

---

## 4. Keamanan Zero Trust & Sesi

- **Metode Autentikasi:** One-Time PIN (OTP) dikirim ke email `alwiihsan50@gmail.com`.
- **Durasi Sesi Aktif:** 730 Jam (**30 Hari**) persisten agar user tidak perlu login berulang kali saat membuka PWA / Web Dashboard di smartphone atau laptop.
- **Bypass Rule:** Diterapkan khusus untuk webhook / callback API tertentu tanpa mengurangi proteksi antarmuka pengguna web.

---

## 5. Tooling & Perintah Eksekusi Otomatis

Untuk melakukan perubahan konfigurasi Cloudflare dari terminal Linux Mint:

```bash
# Menjalankan script dengan token Cloudflare dari Infisical:
infisical run --env=prod -- python3 script_cf.py

# Manajemen Workers & KV via Wrangler:
npx wrangler whoami
npx wrangler deploy

# Pengecekan status Cloudflare Tunnel:
cloudflared tunnel list
```
