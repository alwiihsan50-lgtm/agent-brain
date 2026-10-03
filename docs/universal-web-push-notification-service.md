# Universal Web Push Notification Service (Cloudflare Workers 24/7)

Dokumentasi standar integrasi sistem **Universal Web Push Notification** terpusat untuk seluruh aplikasi dan bot dalam ekosistem (MT5, Arsip-IMO, SaveBuddy, Server Monitoring, cron jobs, dll).

---

## 🌐 1. Arsitektur Terpusat (Central Notification Hub)

Semua aplikasi pengirim (baik yang berjalan di Docker, server lokal, VM, maupun Cloud) hanya perlu memanggil 1 REST API endpoint yang sama di Cloudflare Workers:

```
[Aplikasi 1: MT5 Bot (Docker)] ------+
[Aplikasi 2: Arsip-IMO Backend] ----+
[Aplikasi 3: TailShare / PC Suite] -+---> [Cloudflare Workers Hub] ---> [Apple Push Service] ---> [iPhone User]
[Aplikasi 4: Server Cron/Monitor] --+      (https://mt5-push-backend...       (web.push.apple.com)
[Aplikasi N: Custom App] -----------+           .alwiihsan50.workers.dev)
```

### Detail Endpoint:
* **Service URL:** `https://mt5-push-backend.alwiihsan50.workers.dev`
* **Trigger Endpoint:** `POST https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification` (Payload: `{ "topic": "mt5_trading" | "system_boot" | "general_alerts", "title": "...", "message": "..." }`)
* **Registration Endpoint:** `POST https://mt5-push-backend.alwiihsan50.workers.dev/subscribe`
* **Preferences Endpoint:** `GET /preferences?endpoint=...` & `POST /preferences`
* **PWA Web UI (Client & Toggle Settings):** `GET https://mt5-push-backend.alwiihsan50.workers.dev/`
* **Database Subscription:** Cloudflare KV Namespace `SUBSCRIPTIONS` (ID: `0217d87236964fb796f7988e77f29de0`)
* **VAPID Public Key:** `BDrLwaIpW32cMuH3t3CSr_rxSirYALcj9BOepAeFtSi9mHtO1IsNgU0hfvgCVJXQO7l6xQKTwsXEuTpU5JS2oXs`

---

## 💻 2. Snippet Integrasi Pengirim (Trigger Notification)

Untuk menambahkan fitur notifikasi ke aplikasi baru, cukup salin salah satu snippet berikut:

### A. Python (requests / urllib standar)
```python
import json
import urllib.request

def send_push_alert(title: str, message: str):
    """Kirim notifikasi push instan ke iPhone pengguna via Cloudflare Workers."""
    url = "https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification"
    payload = json.dumps({"title": title, "message": message}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "UniversalPushClient/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"[Push Notification Error]: {e}")
        return False

# Contoh Pemanggilan:
send_push_alert("🚀 Server Alert", "Pekerjaan backup database telah selesai sukses.")
```

### B. JavaScript / TypeScript / Node.js
```javascript
async function sendPushAlert(title, message) {
  try {
    const res = await fetch('https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, message })
    });
    return res.ok;
  } catch (err) {
    console.error('Failed to send push:', err);
    return false;
  }
}

// Contoh Pemanggilan:
await sendPushAlert('💼 Arsip-IMO', 'Ada dokumen baru yang membutuhkan tanda tangan.');
```

### C. PHP / Laravel
```php
use Illuminate\Support\Facades\Http;

function sendPushAlert(string $title, string $message): bool {
    $response = Http::timeout(10)->post('https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification', [
        'title' => $title,
        'message' => $message,
    ]);
    return $response->successful();
}

// Contoh Pemanggilan:
sendPushAlert('⚡ Workstation Monitor', 'Penyimpanan Drive D mencapai 85% pada pukul ' . date('H:i:s'));
```

### D. Golang
```go
package main

import (
	"bytes"
	"encoding/json"
	"net/http"
	"time"
)

func SendPushAlert(title, message string) error {
	payload, _ := json.Marshal(map[string]string{
		"title":   title,
		"message": message,
	})
	client := &http.Client{Timeout: 10 * time.Second}
	_, err := client.Post("https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification", "application/json", bytes.NewBuffer(payload))
	return err
}
```

### E. Shell / Bash (cURL / Cron Job)
```bash
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"title": "🔔 Cron Alert", "message": "Proses sinkronisasi data selesai."}' \
  https://mt5-push-backend.alwiihsan50.workers.dev/trigger-notification
```

---

## 📱 3. Pendaftaran & Kebijakan Single-Device (1 HP Eksklusif)

Sistem ini menerapkan **Strict Single-Device Architecture** (hanya 1 smartphone aktif terdaftar):
1. Setiap kali user menghubungkan perangkat baru atau menginstal ulang PWA di HP:
   - Endpoint baru akan **menggantikan (*overwrite*)** seluruh data langganan lama di Cloudflare KV (`SUBSCRIPTIONS`).
   - Tidak akan terjadi penumpukan token atau duplikasi notifikasi.
2. Status di header PWA akan menampilkan **"● Terhubung (1 HP Aktif)"**.

---

## 🛡️ 4. Maintenance & Operasional
- **Biaya:** $0 / Bulan (Free Tier Cloudflare Workers mencakup 100.000 request/hari).
- **Single-Device Retention:** Cloudflare KV selalu menahan tepat 1 objek langganan aktif pengguna.
- **Auto Cleanup:** Cloudflare Worker secara otomatis mendeteksi status `410 Gone` atau `404 Not Found` dari Apple/Google Push Service saat user meng-uninstall PWA atau mencabut izin notifikasi, dan menghapus subscription tersebut dari KV database tanpa intervensi manual.

---

## 💻 5. Notifikasi Startup/Boot & Idle PC Linux Mint
Tersedia skrip daemon `boot-ready-notify.py` di `~/.local/bin/` yang dijalankan otomatis via `systemd --user` (`boot-ready-notify.service`):
- **Deteksi:** Menunggu jaringan online & load CPU stabil (idle < 35%).
- **Info Payload:** Waktu boot (`systemd-analyze`), penggunaan RAM, IP LAN & Tailscale, serta status container Docker (MT5 Bot/Dashboard).
- **Service Status:** `systemctl --user status boot-ready-notify.service`.

