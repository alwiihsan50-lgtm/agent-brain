# Panduan Instalasi & Konfigurasi TailShare di Linux Mint

Dokumen ini berisi panduan langkah demi langkah untuk menginstal dan menjalankan **TailShare** (Cloud Clipboard & File Sharing) pada sistem operasi Linux Mint, termasuk pembuatan background service via `systemd`.

---

## 1. Prasyarat Sistem
Pastikan Node.js, npm, dan Tailscale sudah terpasang di Linux Mint:

```bash
# Update sistem & install Node.js + npm
sudo apt update
sudo apt install -y nodejs npm git curl

# Verify versi Node.js (minimal Node v18+)
node -v
npm -v

# Install & Jalankan Tailscale (jika belum ada)
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

---

## 2. Clone Repositori & Install Dependensi

```bash
# Clone repositori ke direktori home
cd ~
git clone https://github.com/alwiihsan50-lgtm/claudbridge.git tailscale-share
cd tailscale-share

# Install dependensi Node.js
npm install
```

---

## 3. Menjalankan Server Secara Manual (Pengujian)

```bash
# Uji coba jalankan server
npm start
```
Akses web UI melalui browser di: **`http://localhost:40506`** atau `http://<IP-Tailscale-Linux>:40506`.

---

## 4. Konfigurasi Auto-Start (Systemd Background Service)

Agar TailShare berjalan otomatis saat Linux Mint dinyalakan (booting) tanpa perlu membuka terminal:

1. Buat file unit service `systemd`:
   ```bash
   sudo nano /etc/systemd/system/tailshare.service
   ```

2. Tempelkan (paste) konfigurasi berikut *(sesuaikan username Anda jika bukan `alwi`)*:
   ```ini
   [Unit]
   Description=TailShare Cloud Clipboard & File Sharing Service
   After=network.target tailscaled.service

   [Service]
   Type=simple
   User=alwi
   WorkingDirectory=/home/alwi/tailscale-share
   ExecStart=/usr/bin/node server.js
   Restart=always
   Environment=NODE_ENV=production
   Environment=PORT=40506

   [Install]
   WantedBy=multi-user.target
   ```

3. Simpan file (`Ctrl+O`, `Enter`, `Ctrl+X`), lalu jalankan perintah berikut untuk mengaktifkan service:
   ```bash
   # Reload daemon systemd
   sudo systemctl daemon-reload

   # Aktifkan service agar jalan saat booting
   sudo systemctl enable tailshare

   # Jalankan service sekarang
   sudo systemctl start tailshare

   # Cek status service
   sudo systemctl status tailshare
   ```

---

## 5. Membuat Desktop Shortcut di Linux Mint (.desktop)

Buat file shortcut di desktop Linux Mint agar bisa diklik 2x:

1. Buat file `TailShare.desktop`:
   ```bash
   nano ~/Desktop/TailShare.desktop
   ```

2. Isi dengan teks berikut:
   ```ini
   [Desktop Entry]
   Version=1.0
   Type=Application
   Name=Buka TailShare
   Comment=Buka TailShare Clipboard & File Sharing
   Exec=xdg-open http://localhost:40506
   Icon=web-browser
   Terminal=false
   Categories=Network;Utility;
   ```

3. Beri izin eksekusi:
   ```bash
   chmod +x ~/Desktop/TailShare.desktop
   ```

---

## 6. Menu Klik Kanan Nemo File Manager (Nemo Actions)

Integrasi menu klik kanan di Linux Mint (Nemo) agar dapat langsung membagikan file/folder ke TailShare:

1. **Helper CLI:** `~/.local/bin/tailshare-send`
   - Mengirim file via TailShare REST API (`http://127.0.0.1:40506/api/files/upload`) dengan metadata pengirim dan push notifikasi instan.
   - Fallback otomatis ke copy direktori `/media/cuker/Data/tailshare` jika offline.
   - Notifikasi desktop via `notify-send`.
2. **Nemo Actions:**
   - `~/.local/share/nemo/actions/tailshare-send.nemo_action`: Muncul saat memilih file/folder ("Kirim ke TailShare").
   - `~/.local/share/nemo/actions/tailshare-open-web.nemo_action`: Muncul saat klik kanan area kosong ("Buka TailShare Web").
   - `~/.local/share/nemo/actions/tailshare-open-folder.nemo_action`: Muncul saat klik kanan area kosong ("Buka Folder Penyimpanan TailShare").

