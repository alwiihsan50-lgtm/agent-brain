# Spesifikasi Infrastruktur Server: `mentari-server`

Dokumentasi terpusat untuk PC Server mandiri (`mentari-server`) yang terhubung dalam ekosistem workstation melalui jaringan privat Tailscale dan SSH terenkripsi.

---

## 1. Spesifikasi Hardware & Sistem Operasi
- **Hostname:** `mentari-server`
- **Sistem Operasi:** Debian GNU/Linux 13 (*trixie*) - Kernel `6.12.101+deb13-amd64`
- **User Utama:** `mentari`
- **Kapasitas RAM:** ~4.0 GiB (Total: 3.7 GiB, Available: ~2.9 GiB)
- **Konfigurasi Penyimpanan (Total: ~1.1 TB):**
  - ⚡ **SSD Sistem (`/dev/sdb` - 128 GB `PREMIUM-128GB`):**
    - `/` (Root OS): 113 GB (*Terpakai: 3.0 GB, Sisa: 104 GB*)
    - `/boot/efi`: 976 MB
    - `[SWAP]`: 3.9 GB
  - 💽 **HDD Storage (`/dev/sda` - 1 TB `TOSHIBA DT01ABA100V`):**
    - `/cctv` (Label: `CCTV_STORAGE`): 916 GB (*Sisa: 907 GB*)
    - Folder: `/cctv/recordings`, `/cctv/data`, `/cctv/config` (Owner: `mentari`)
    - Persisten di `/etc/fstab` (`noatime,nodiratime,nofail`)
- **Docker Engine:** `v29.7.2` (User `mentari` terdaftar di grup `docker` non-root)
- **Manajemen Agent:** Full-access via passwordless SSH dari workstation AI Agent (`ssh mentari-server`).

---

## 2. Jaringan & Akses Remote
- **Tailscale Mesh IP:** `100.109.208.27`
- **Subnet IP LAN:** `192.168.101.243` (Routing via MikroTik `192.168.100.7`, latensi <0.5ms)
- **Ethernet Interface & MAC:** `enp2s0` ➔ `00:e0:4c:bf:02:e1` (Realtek RTL8111 Gigabit)
- **SSH Port:** `22` (OpenSSH Server)
- **Host Alias Lokal (Workstation):** `mentari-server`
- **Autentikasi Kunci:** Public key `id_termius_rsa.pub` terpasang di `~/.ssh/authorized_keys`

### Konfigurasi SSH Client (`~/.ssh/config`):
```ssh-config
Host mentari-server
    HostName 192.168.101.243
    User mentari
    IdentityFile ~/.ssh/id_termius_rsa
    ServerAliveInterval 60
    ServerAliveCountMax 3
    StrictHostKeyChecking accept-new

Host mentari-tailscale
    HostName 100.109.208.27
    User mentari
    IdentityFile ~/.ssh/id_termius_rsa
    ServerAliveInterval 60
    ServerAliveCountMax 3
    StrictHostKeyChecking accept-new
```

---

## 3. Web GUI & Cloudflare Tunnel (Akses Global 24/7)
- **Aplikasi Web GUI:** CasaOS v0.4.15 (Port 80)
- **Domain Publik HTTPS:**
  - 🌐 **`https://server.abbas.my.id`** (HTTP 200 Live)
  - 🌐 **`https://casa.abbas.my.id`** (HTTP 200 Live)
- **Cloudflare Tunnel ID:** `6cd14b2e-12e7-44f2-b138-d8c1684690a6` (`mentari-tunnel`)
- **File Konfigurasi Tunnel:** `/etc/cloudflared/config.yml`
- **Service Systemd:** `cloudflared.service` ➔ `enabled` (Active 24/7)

---

## 4. Hak Akses & Persistensi Layanan
1. **Passwordless Sudo:**
   - Konfigurasi: `/etc/sudoers.d/mentari` (`mentari ALL=(ALL) NOPASSWD:ALL`)
   - Memungkinkan otomatisasi pemeliharaan dan deploy oleh AI Agent tanpa prompt password.
2. **Auto-Start Saat Booting:**
   - `ssh.service` ➔ `enabled` (Active)
   - `tailscaled.service` ➔ `enabled` (Active)
   - `cloudflared.service` ➔ `enabled` (Active)
   - Server otomatis pulih dan dapat diakses publik maupun privat segera setelah restart / mati listrik.
3. **Tailscale Key Expiry:** Dinonaktifkan (*Disabled*) di konsol admin Tailscale untuk menjaga koneksi permanen.
4. **Wake-on-LAN (WoL) Persistence:**
   - Service: `wol-enable.service` (`/etc/systemd/system/wol-enable.service`)
   - Command: `/sbin/ethtool -s enp2s0 wol g`
   - Status: `enabled` & `active`

---

## 5. Cara Akses, Wake-on-LAN & Eksekusi Perintah
```bash
# Nyalakan mentari-server dari PC lokal via Wake-on-LAN (Magic Packet)
wake-mentari
# Atau kirim packet sekaligus cek status ping otomatis
wake-mentari-check

# Akses remote langsung via alias
ssh mentari-server

# Eksekusi perintah administratif
ssh mentari-server "docker ps"
ssh mentari-server "sudo systemctl status <service>"
ssh mentari-server "df -h"
```
