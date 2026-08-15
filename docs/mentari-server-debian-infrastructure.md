# Spesifikasi Infrastruktur Server: `mentari-server`

Dokumentasi terpusat untuk PC Server mandiri (`mentari-server`) yang terhubung dalam ekosistem workstation melalui jaringan privat Tailscale dan SSH terenkripsi.

---

## 1. Spesifikasi Hardware & Sistem Operasi
- **Hostname:** `mentari-server`
- **Sistem Operasi:** Debian GNU/Linux 13 (*trixie*) - Kernel `6.12.101+deb13-amd64`
- **User Utama:** `mentari`
- **Kapasitas RAM:** ~4.0 GiB (Total: 3.7 GiB, Available: ~2.9 GiB)
- **Kapasitas Disk:** 113 GB (Available: ~104 GB pada partisi `/dev/sdb2`)
- **Docker Engine:** `v29.7.2` (User `mentari` terdaftar di grup `docker` non-root)

---

## 2. Jaringan & Akses Remote
- **Tailscale Mesh IP:** `100.109.208.27`
- **Subnet IP LAN:** `192.168.100.7` / `192.168.101.243`
- **SSH Port:** `22` (OpenSSH Server)
- **Host Alias Lokal (Windows & Linux):** `mentari-server`
- **Autentikasi Kunci:** Public key `id_termius_rsa.pub` terpasang di `~/.ssh/authorized_keys`

### Konfigurasi SSH Client (`~/.ssh/config`):
```ssh-config
Host mentari-server
    HostName 100.109.208.27
    User mentari
    IdentityFile ~/.ssh/id_termius_rsa
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

---

## 3. Hak Akses & Persistensi Layanan
1. **Passwordless Sudo:**
   - Konfigurasi: `/etc/sudoers.d/mentari` (`mentari ALL=(ALL) NOPASSWD:ALL`)
   - Memungkinkan otomatisasi pemeliharaan dan deploy oleh AI Agent tanpa prompt password.
2. **Auto-Start Saat Booting:**
   - `ssh.service` ➔ `enabled` (Active)
   - `tailscaled.service` ➔ `enabled` (Active)
   - Server otomatis pulih dan dapat di-SSH segera setelah restart / mati listrik.
3. **Tailscale Key Expiry:** Dinonaktifkan (*Disabled*) di konsol admin Tailscale untuk menjaga koneksi permanen.

---

## 4. Cara Akses & Eksekusi Perintah
```bash
# Akses remote langsung via alias
ssh mentari-server

# Eksekusi perintah administratif
ssh mentari-server "docker ps"
ssh mentari-server "sudo systemctl status <service>"
ssh mentari-server "df -h"
```
