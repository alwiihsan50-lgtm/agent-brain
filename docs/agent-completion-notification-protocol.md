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

## 📱 4. Direct Tunnel Webhook & Quick Reply Interface (0% Quota Waste, Zero-Auth)

Sistem mengadopsi arsitektur **Direct Webhook via Cloudflare Tunnel** yang mengeliminasi 100% beban polling Cloudflare:
- **Web UI & Direct Webhook:** `https://reply.abbas.my.id` (Port lokal `40508` via Cloudflare Tunnel `cuker-apps`).
- **Aksi Ketuk Notifikasi:** Notifikasi push iPhone langsung membuka `https://reply.abbas.my.id` secara instan tanpa login (Zero-Auth) dengan edge SSL Cloudflare otomatis.
- **Tampilan Antarmuka (Minimalist Quick Reply):**
  - Status koneksi PC (`🟢 PC Direct Tunnel (0% Quota)`).
  - **💬 Jawaban Terakhir Saja:** Mengambil langsung jawaban terakhir dari `transcript.jsonl` lokal PC secara SSR (Server-Side Rendered), bebas riwayat chat panjang masa lalu yang membebani layar.
  - **✍️ Box Input Balasan Cepat:** Input box autofokus siap menerima teks atau mikrofon dikte suara (*voice dictation*) bawaan iOS.
  - Quick action chips minimalis: `Lanjutkan`, `Oke terima kasih`.
  - Tombol aksi utama: `🚀 Kirim Balasan` dengan indikator progres dan getaran haptik.
- **⚡ Efisiensi Kuota Cloudflare (100% Zero-Quota Polling):**
  - **Zero Polling Loop:** PC Daemon tidak lagi melakukan polling ke Cloudflare Worker setiap 3,5 detik.
  - **Zero KV Reads:** Pemborosan 49.370 KV Reads/hari dari loop polling dieliminasi **100% (turun menjadi 0)**.
  - Cloudflare Worker murni hanya bertindak sebagai push gateway notifikasi ke Apple APNs saat tugas selesai (~10-20 request/hari = <0,02% kuota harian).
- **Eksekusi ke Antigravity CLI:**
  - Server daemon lokal PC (`agent-reply-daemon` pada port `40508`) menerima POST dari browser HP via Cloudflare Tunnel secara instan (<50ms).
  - Teks disuntikkan langsung ke sesi `tmux` aktif menggunakan `tmux send-keys` tanpa delay antrean.

---

## ⚡ 5. Single Notification Guarantee (Auto-Deduplication & Cooldown)

Untuk menjamin kenyamanan pengguna dan mencegah notifikasi ganda pada setiap kali pergantian turn/tugas:
- **Penyebab Duplikasi Lampau:** Pemanggilan manual `agent-notify` oleh AI Agent dan pemicuan otomatis lifecycle hook `Stop` di Antigravity (`~/.local/bin/agent-notify-hook`) berjalan bersusulan (selisih ~1-2 detik).
- **Mekanisme Auto-Deduplication (Smart Cooldown 12s):**
  - Utilitas `~/.local/bin/agent-notify` menyimpan timestamp pengiriman terakhir di `/tmp/agent_notify_last_sent`.
  - Jika AI Agent telah memanggil `agent-notify` secara manual, panggilan berikutnya dari lifecycle hook (`--from-hook`) otomatis di-skip.
  - Jika AI Agent tidak memanggil secara manual, lifecycle hook bertindak sebagai jaring pengaman (*safety net*) dengan mengekstrak baris pertama respons AI dari transcript dan mengirimkannya secara otomatis.
- **Hasil:** Pengguna dijamin **HANYA menerima tepat 1 notifikasi** per penyelesaian tugas di smartphone.




