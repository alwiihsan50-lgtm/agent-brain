# Kebijakan Sentralisasi Unduhan Torrent (PC-Only Policy)

Dokumen ini menetapkan aturan permanen mengenai manajemen pengunduhan torrent di seluruh ekosistem workstation.

---

## 🔒 1. Mandat & Aturan Mutlak
> ⚠️ **ATURAN MUTLAK USER:**  
> **SELURUH TASK PENGUNDUHAN TORRENT HANYA BOLEH DILAKUKAN DI PC WORKSTATION INI.**  
> Seluruh AI Agent (Gemini, Claude, GPT, Antigravity, OpenCode, dll.) **DILARANG KERAS** mendelegasikan, mengonfigurasi, atau menjalankan daemon/proses torrent downloader di perangkat lain seperti **STB Android (`erza`)** atau **`mentari-server` (CasaOS)**.

---

## 🎯 2. Rationale & Alasan Arsitektur
1. **Penyimpanan Berkapasitas Besar:**
   - PC Workstation memiliki Drive Data (`/media/cuker/Data`) dengan bandwidth disk tinggi dan ruang penyimpanan besar khusus untuk unduhan (`/media/cuker/Data/Downloads/`).
2. **Integritas Perangkat Edge / STB:**
   - STB Android (`erza`) memiliki memori flash internal terbatas (NAND eMMC). Menjalankan torrent di STB menyebabkan keausan flash disk (*disk wear*), storage cepat penuh (*insufficient storage*), dan membebani RAM yang dibutuhkan untuk daemon uinput Remote Hub dan video playback.
3. **Stabilitas Server (`mentari-server`):**
   - `mentari-server` didedikasikan untuk perekaman CCTV 24/7, CasaOS, dan Cloudflare Tunnel. Aktivitas P2P torrent dapat menghabiskan koneksi routing LAN / bandwidth upload-download yang mengganggu transmisi stream CCTV.

---

## 🛠️ 3. Tooling & Standard Execution di PC Workstation
- **Direktori Unduhan Resmi:**
  ```bash
  /media/cuker/Data/Downloads/
  ```
- **Engine Unduhan PC:**
  - **Aria2 CLI / Daemon (Port 6801):**
    - Binary: `~/.local/bin/aria2c`
    - RPC Endpoint: `http://127.0.0.1:6801/jsonrpc`
    - CLI Monitor: `pc-torrent` (`~/.local/bin/pc-torrent`)
  - **Transmission (GUI / Daemon):**
    - Konfigurasi: `~/.config/transmission/`
- **Streaming Internal:**
  - Serial/media yang telah terunduh dapat di-stream ke perangkat lain (termasuk STB & ponsel) melalui `loki_stream_server.py` (Port `8888`) atau TailShare (Port `40506`).

---

## 📋 4. Checklist Kepatuhan AI Agent
- [x] Pastikan path tujuan unduhan selalu mengarah ke `/media/cuker/Data/Downloads/`.
- [x] Tidak memasang `aria2` atau torrent client di STB via ADB.
- [x] Tidak memasang container torrent downloader di `mentari-server` via CasaOS/Docker tanpa izin eksplisit.
- [x] Monitor status berkala menggunakan `pc-torrent` atau `brain health`.
