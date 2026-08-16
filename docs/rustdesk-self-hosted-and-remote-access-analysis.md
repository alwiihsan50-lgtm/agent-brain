# Analisis & Panduan RustDesk Self-Hosted, Batasan Jaringan, & Solusi Remote

Dokumentasi ini merangkum setup infrastruktur RustDesk Server mandiri di workstation Linux Mint, hasil investigasi konektivitas (LAN, Tailscale, IPv6, Paket Data Seluler), batasan firewall modem/ISP, serta opsi solusi berikutnya.

---

## 1. Arsitektur & Konfigurasi Server RustDesk Lokal

Server RustDesk mandiri telah di-deploy dan berjalan aktif via Docker Compose di workstation Linux:

- **Direktori Project:** `/home/cuker/rustdesk-server`
- **File Konfigurasi:** `/home/cuker/rustdesk-server/docker-compose.yml`
- **Container Aktif:**
  - `rustdesk-hbbs` (ID & Rendezvous Server) — `hbbs -r rustdesk.abbas.my.id:21117 -k _`
  - `rustdesk-hbbr` (Relay Server) — `hbbr -k _`
- **Network Mode:** `host` (Binding langsung ke port IPv4 `0.0.0.0` dan IPv6 `::`)
- **Port Terpesan:**
  - `21115` (TCP) — NAT type test
  - `21116` (TCP & UDP) — ID registration, heartbeat, & P2P handshake
  - `21117` (TCP) — Data relay fallback
- **Public Key Enkripsi Server:** `+Gj77z0PhFv2c2QzF0Uc65Za+s151qsR0qxK5gVhZ4Q=`
- **ID Klien PC:** `1135152995`
- **DNS Record:** `rustdesk.abbas.my.id` (Tipe `AAAA`, DNS Only / Grey Cloud) diarahkan ke IPv6 publik workstation `2404:c0:9603:b053:96ee:52cc:fb96:b299`.

---

## 2. Hasil Pengujian Konektivitas Lintas Jaringan

| Skenario Jaringan | Hasil Koneksi | Analisis Teknis |
| :--- | :---: | :--- |
| **Wi-Fi Lokal Rumah (LAN)** | 🟢 **Sukses 100%** | HP dan PC berada dalam subnet lokal yang sama. Traffic tidak melewati firewall modem WAN. |
| **Tailscale VPN (Privat)** | 🟢 **Sukses 100%** | Menggunakan virtual network interface (`100.110.205.27`), menembus NAT lewat direct peer mesh encrypted. |
| **Paket Data Seluler (4G/5G)** | 🔴 **Dicegat Modem** | Inbound packets dari internet publik ditolak oleh **SPI Inbound Firewall** bawaan modem/router ISP (IndiHome/Biznet). |

---

## 3. Analisis Mengapa Solusi Tunnel Tertentu Tidak Bisa

1. **Cloudflare Tunnel (`cloudflared`):**
   - Cloudflare Tunnel gratis dirancang khusus untuk traffic layer web (**HTTP, HTTPS, WebSocket**).
   - Traffic native RustDesk mobile app menggunakan raw TCP & UDP socket non-HTTP, yang hanya didukung pada paket enterprise berbayar (*Cloudflare Spectrum*).
2. **Tailscale Funnel:**
   - Tailscale Funnel membatasi traffic publik hanya untuk protokol HTTPS/TLS pada port `443`, `8443`, dan `10000`.
   - Tidak mendukung UDP dan tidak mengizinkan port raw TCP custom (21115-21117).
3. **Playit.gg Tunnel:**
   - Agent `playit` berhasil terpasang di systemd (`playit.service`), namun Playit membatasi alokasi custom port TCP+UDP gratis pada versi web dashboard terbarunya.

---

## 4. Opsi Solusi Rekomendasi Selanjutnya

1. **Google WebRTC (Chrome Remote Desktop) — *Paling Direkomendasikan Tanpa Biaya***
   - Bekerja melalui protokol WebRTC Google (STUN/TURN outbound dari PC).
   - Tembus firewall modem otomatis tanpa perlu port forwarding.
   - Aplikasi resmi tersedia di iOS/Android, 60 FPS, pinch-to-zoom, dan HP 100% bebas dari VPN.
2. **Cloud Relay Server (Fly.io / VPS Singapura) — *Jika Tetap Menggunakan RustDesk***
   - Menjalankan `hbbs` dan `hbbr` di server cloud luar (Fly.io Free Tier di region `sin` Singapura / VPS mini).
   - PC rumah dan HP dua-duanya menghubungi keluar (*outbound*), sehingga firewall modem tidak memblokir.
3. **Otomasi iOS Shortcut (Tailscale + RustDesk 1-Click)**
   - Membuat tombol otomatis di iPhone yang menyalakan Tailscale hanya saat RustDesk dibuka, dan mematikannya saat selesai.
