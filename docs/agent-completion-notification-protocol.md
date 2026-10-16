# 🔔 Protokol Mandat Notifikasi Penyelesaian Tugas (Agent Completion Notification)

> 🔒 **Status: MANDAT SISTEM PERMANEN**
> Aturan ini berlaku untuk **seluruh sesi chat AI Agent (Antigravity CLI / IDE / Web) saat ini dan seluruh sesi di masa depan**.
> Setiap model AI Agent yang menjalankan sesi di komputer ini **WAJIB** mengirimkan notifikasi kepada USER setiap kali menyelesaikan 1 tugas atau 1 prompt.

---

## 🏛️ 1. Arsitektur Jalur Ganda (Dual-Channel Notification)

Ketika perintah `agent-notify "<judul>" "<pesan>"` dieksekusi, sistem secara otomatis mendistribusikan sinyal melalui dua jalur:

```
[AI Agent Selesai Tugas/Prompt]
              │
              ▼
   [CLI Helper: agent-notify]
        ┌─────┴────────────────────────────────┐
        ▼                                      ▼
[Desktop Popup Linux Mint]        [Cloudflare Web Push Hub]
 (notify-send via D-Bus)         (mt5-push-backend...workers.dev)
        │                                      │
        ▼                                      ▼
[Layar Monitor PC Workstation]       [Apple Push Service]
                                               │
                                               ▼
                                      [Smartphone / iPhone User]
```

---

## 🛠️ 2. Komponen & Lokasi File Sistem

| Komponen | Lokasi File | Fungsi & Peran |
| :--- | :--- | :--- |
| **CLI Executable** | [`~/.local/bin/agent-notify`](file:///home/cuker/.local/bin/agent-notify) | Utilitas utama pengirim notifikasi desktop + Cloudflare Web Push. |
| **Lifecycle Hook Script**| [`~/.local/bin/agent-notify-hook`](file:///home/cuker/.local/bin/agent-notify-hook) | Handler perantara untuk event `Stop` Antigravity. |
| **Antigravity Hook Config**| [`~/.agents/hooks.json`](file:///home/cuker/.agents/hooks.json) | Konfigurasi lifecycle hook event `Stop` otomatis. |
| **Permanent Agent Rule** | [`~/.agents/rules/agent-completion-notification.md`](file:///home/cuker/.agents/rules/agent-completion-notification.md) | Aturan sistem wajib (injected system prompt) untuk seluruh model AI Agent. |

---

## 📋 3. Standar Format Pemanggilan

```bash
agent-notify "<Judul Ringkas>" "<Penjelasan Singkat Pekerjaan Selesai>"
```
*Contoh:*
```bash
agent-notify "✅ Update Selesai" "Sinkronisasi agent-brain dan pengarsipan bot telah rampung."
```

---

## 📱 4. Minimalist Quick Reply Interface via iPhone (Zero-Auth)

Sistem mengadopsi antarmuka **Quick Reply Terfokus** yang cepat, bersih, dan hemat kuota:
- **Web UI Mobile:** `https://mt5-push-backend.alwiihsan50.workers.dev/reply`.
- **Aksi Ketuk Notifikasi:** Setiap kali notifikasi selesai di-tap di iPhone, Safari/PWA langsung membuka antarmuka balas cepat.
- **Tampilan Antarmuka:**
  - Status koneksi PC (`🟢 PC Online`).
  - **✨ Tombol `/new` (Popup Box Prompt Pertama & Auto-Switch):** Saat ditekan, muncul pop-up dialog yang meminta pengguna mengisikan instruksi atau prompt pertama untuk sesi baru. Begitu tombol 'Mulai & Buka Sesi' diklik, antarmuka web langsung otomatis beralih ke sesi baru tersebut dengan status tunggu respons awal, sementara PC Workstation langsung mengeksekusi `agy --dangerously-skip-permissions -i '<prompt>'`.
  - **📂 Tombol Ganti Sesi (Header & Chips):** Membuka bottom-sheet modal berisi 10 daftar sesi percakapan terbaru dengan waktu dan jumlah pesan.
  - **💬 Jawaban Terakhir Saja (Zero-History Distraction):** Sesuai arahan efisiensi, saat pengguna beralih sesi atau membuka pesan, sistem **HANYA menampilkan chat terakhir dari sesi tersebut** (bukan seluruh tumpukan riwayat masa lalu). Layar HP tetap 100% ringan, terfokus, dan hemat memori.
  - **✍️ Box Input Balasan Cepat:** Input box teks autofokus siap ketik atau tombol dikte suara (*voice-to-text*) bawaan iOS.
  - Quick action chips: `✨ /new`, `📂 Ganti Sesi`, `Lanjutkan`, `Oke terima kasih`.
  - Tombol aksi utama: `🚀 Kirim Balasan` dengan umpan balik visual dan haptik.
- **⚡ Efisiensi Kuota Cloudflare (100% Aman):**
  - Menggunakan endpoint terpadu (`/api/daemon-poll`) yang memeriksa prompt baru dan permintaan ganti sesi dalam satu request atomic.
  - Polling interval diatur ke **3,5 detik** ($86.400 / 3,5 = \sim 24.685\text{ request/hari}$), hanya memakan **~24,7% kuota harian Cloudflare Free Tier (100k request/hari)**.
  - Menyisakan lebih dari 75.000 request bebas per hari, menjamin arsitektur Cloudflare Workers tetap berjalan lancar 24/7 tanpa risiko terblokir atau over-quota.
- **Eksekusi ke Antigravity CLI:**
  - Daemon lokal PC (`antigravity-reply-daemon.service` running 24/7) menyuntikkan instruksi langsung ke session `tmux` aktif menggunakan `tmux send-keys`.

---

## ⚡ 5. Single Notification Guarantee (Auto-Deduplication & Cooldown)

Untuk menjamin kenyamanan pengguna dan mencegah notifikasi ganda pada setiap kali pergantian turn/tugas:
- **Penyebab Duplikasi Lampau:** Pemanggilan manual `agent-notify` oleh AI Agent dan pemicuan otomatis lifecycle hook `Stop` di Antigravity (`~/.local/bin/agent-notify-hook`) berjalan bersusulan (selisih ~1-2 detik).
- **Mekanisme Auto-Deduplication (Smart Cooldown 12s):**
  - Utilitas `~/.local/bin/agent-notify` menyimpan timestamp pengiriman terakhir di `/tmp/agent_notify_last_sent`.
  - Jika AI Agent telah memanggil `agent-notify` secara manual, panggilan berikutnya dari lifecycle hook (`--from-hook`) otomatis di-skip.
  - Jika AI Agent tidak memanggil secara manual, lifecycle hook bertindak sebagai jaring pengaman (*safety net*) dengan mengekstrak baris pertama respons AI dari transcript dan mengirimkannya secara otomatis.
- **Hasil:** Pengguna dijamin **HANYA menerima tepat 1 notifikasi** per penyelesaian tugas di smartphone.




