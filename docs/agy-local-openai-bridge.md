# 🚀 AGY Local OpenAI Bridge & 9Router Integration

Panduan integrasi resmi lokal yang mengubah sesi aktif Antigravity CLI (`agy -p`) menjadi endpoint universal **OpenAI-Compatible API** (`/v1/chat/completions`) yang aman, legal, dan terintegrasi langsung dengan **9Router** (Port `20128`) dan **Headroom Token Saver** (Port `8787`).

---

## 📌 1. Informasi Arsitektur & Lingkungan

| Parameter | Nilai / Konfigurasi |
| :--- | :--- |
| **Service Name** | `agy-bridge` |
| **Executable Binary** | `/home/cuker/.local/bin/agy-bridge` |
| **Systemd Service** | `~/.config/systemd/user/agy-bridge.service` (`systemctl --user`) |
| **Port Bridge Lokal** | `Port 5050` (`http://localhost:5050`) |
| **Direct OpenAI Endpoint** | `http://localhost:5050/v1` |
| **9Router Gateway Endpoint** | `http://localhost:20128/v1` |
| **9Router Provider ID** | `openai-compatible-chat-agy-local` (Prefix: `agy/`) |
| **Default Model** | `gemini-3.8-flash-high` |

---

## 🔒 2. Mengapa Arsitektur Ini Aman bagi Akun Google?

Berbeda dengan reverse-engineering OAuth langsung di aplikasi pihak ketiga yang berisiko terkena *flagging* / *ban*, bridge ini:
1. Berjalan di layer lokal internal.
2. Setiap kali ada request masuk dari Cursor / Cline / NextChat / 9Router, bridge mengeksekusi binary resmi `agy -p "<prompt>" --model "<model>" --output-format stream-json`.
3. Dari sudut pandang Google, seluruh trafik keluar murni dihasilkan oleh aplikasi resmi Google Antigravity CLI di workstation Anda sendiri.

---

## 🤖 3. Model yang Didukung (16 Models)

Dapat dipanggil via 9Router dengan format `agy/<model_id>`:

| Model ID di 9Router | Nama Asli di AGY | Tipe / Karakteristik |
| :--- | :--- | :--- |
| `agy/gemini-3.8-flash-high` | Gemini 3.8 Flash (High) | Super Cepat, Reasoning Tinggi (Default) |
| `agy/gemini-3.8-flash` | Gemini 3.8 Flash | Alias cepat untuk 3.8 Flash |
| `agy/gemini-3.7-flash-high` | Gemini 3.7 Flash (High) | Flagship Flash generasi sebelumnya |
| `agy/gemini-3.6-flash-high` | Gemini 3.6 Flash (High) | Model stabil hemat token |
| `agy/gemini-3.1-pro-high` | Gemini 3.1 Pro (High) | Heavy Reasoning Pro |
| `agy/claude-sonnet-4-6` | Claude Sonnet 4.6 | Claude Thinking untuk coding berat |
| `agy/claude-opus-4-6-thinking` | Claude Opus 4.6 (Thinking) | Model penalaran tertinggi |
| `agy/gpt-oss-120b-medium` | GPT-OSS 120B (Medium) | Model open source performa tinggi |

---

## ⚙️ 4. Cara Penggunaan di Aplikasi Eksternal

### A. Melalui 9Router Gateway (Port 20128) — *Direkomendasikan*
Mendapatkan kompresi context token otomatis dari Headroom (Port 8787) dan logging terpusat:
* **Provider:** `OpenAI-Compatible`
* **Base URL:** `http://localhost:20128/v1`
* **API Key:** `sk-2c5c0b1b0dac27df-vdt1g2-7d225d4d` *(atau key 9Router Anda)*
* **Model Name:** `agy/gemini-3.8-flash-high` atau `agy/claude-sonnet-4-6`

### B. Direct ke AGY Bridge (Port 5050)
Jika ingin bypass 9Router langsung ke bridge lokal:
* **Provider:** `OpenAI-Compatible`
* **Base URL:** `http://localhost:5050/v1`
* **API Key:** sembarang teks (misal `sk-agy-local`)
* **Model Name:** `gemini-3.8-flash-high` atau `claude-sonnet-4-6`

---

## 🛠️ 5. Manajemen Service Systemd

```bash
# Cek status bridge
systemctl --user status agy-bridge.service

# Restart service
systemctl --user restart agy-bridge.service

# Stop service
systemctl --user stop agy-bridge.service

# Lihat log real-time
journalctl --user -u agy-bridge -f
```

---

## 🧪 6. Contoh Verifikasi cURL

### Non-Streaming:
```bash
curl -s -X POST http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer sk-2c5c0b1b0dac27df-vdt1g2-7d225d4d" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agy/gemini-3.8-flash-high",
    "messages": [{"role": "user", "content": "Hai, siapa kamu?"}]
  }'
```

### Streaming SSE:
```bash
curl -s -N -X POST http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer sk-2c5c0b1b0dac27df-vdt1g2-7d225d4d" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "agy/claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "Tulis 1 baris pantun"}],
    "stream": true
  }'
```
