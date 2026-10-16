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

Sistem telah disederhanakan murni menjadi antarmuka **Quick Reply** yang cepat, bersih, dan tanpa distraksi:
- **Web UI Mobile:** `https://mt5-push-backend.alwiihsan50.workers.dev/reply`.
- **Aksi Ketuk Notifikasi:** Setiap kali notifikasi selesai di-tap di iPhone, Safari/PWA langsung membuka antarmuka balas cepat.
- **Tampilan Antarmuka:**
  - Status koneksi PC (`🟢 PC Online`).
  - **💬 Jawaban Terakhir dari Antigravity:** Menampilkan jawaban terakhir secara ringkas dan rapi dalam format Markdown (`marked.parse()`) di dalam satu kartu terfokus. Tanpa tumpukan riwayat chat masa lalu yang membebani layar HP, sehingga pengguna langsung fokus pada pesan yang ingin dibalas.
  - **✍️ Box Input Balasan Cepat:** Input box teks autofokus yang siap menerima ketikan cepat atau tombol dikte suara (*voice dictation*) bawaan keyboard iOS.
  - Quick action chips minimalis: `Lanjutkan`, `Oke terima kasih`.
  - Tombol aksi utama: `🚀 Kirim Balasan` dengan indikator progres dan umpan balik haptik.
  - **Desain Bebas Distraksi:** Seluruh tombol berlebih (`/resume`, `/status`, `/usage`, modal picker) telah dihilangkan agar fokus 100% pada pembalasan cepat.
- **Eksekusi ke Antigravity CLI:**
  - Teks balasan disimpan di antrean KV Cloudflare Workers.
  - Daemon lokal PC (`antigravity-reply-daemon.service` running 24/7) mengambil pesan dan menyuntikkannya langsung ke session `tmux` aktif menggunakan `tmux send-keys`.
  - Antigravity langsung memproses instruksi tanpa perlu menyentuh komputer atau login Google di HP.




