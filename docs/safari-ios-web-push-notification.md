# Spesifikasi & Panduan Implementasi Web Push Notification (Safari iOS & Browser)

Dokumentasi ini merangkum arsitektur, syarat khusus sistem Apple iOS (Safari 16.4+), dan implementasi teknis Web Push Notification untuk integrasi ke sistem backend/server lokal tanpa menggunakan Telegram/WhatsApp bot.

---

## 1. Persyaratan Khusus iOS Safari (Apple Web Push)
1. **HTTPS Wajib:** Web Push API dan Service Worker hanya bisa berjalan di lingkungan aman (*Secure Context* - HTTPS). Akses via IP lokal mentah (`http://192.168.x.x`) akan diblokir oleh Safari.
2. **Mode PWA / Add to Home Screen:** Di iOS (16.4+), notifikasi web **hanya** diizinkan jika web di-install/ditambahkan ke Layar Utama (*Home Screen*) via Safari (`Share` -> `Add to Home Screen`). Web harus memiliki `manifest.json` dengan `"display": "standalone"`.
3. **User Gesture Permission:** Permintaan izin `Notification.requestPermission()` harus dipicu oleh aksi langsung pengguna (misal: klik tombol), bukan otomatis saat halaman dimuat.

---

## 2. Arsitektur Komponen

```
[ Local Server / App Backend ] 
            │
            ▼ (VAPID Private Key + Subscription Endpoint)
   [ Apple Push Service (APNs) ]
            │
            ▼
      [ iPhone / Safari PWA ] ──> [ Service Worker (sw.js) ] ──> [ Banner Notifikasi ]
```

### A. Client / Frontend (`public/`)
- **`manifest.json`**: Konfigurasi PWA (nama aplikasi, icon 192x192, start_url, display standalone).
- **`sw.js` (Service Worker)**: Mendengarkan event `push` dan memanggil `self.registration.showNotification(title, options)`. Menangani event `notificationclick` untuk navigasi.
- **`index.html`**:
  - Mengonversi VAPID Public Key base64 ke `Uint8Array`.
  - Mendaftarkan Service Worker (`navigator.serviceWorker.register('sw.js')`).
  - Meminta izin (`Notification.requestPermission()`).
  - Mendaftarkan subscription via `registration.pushManager.subscribe({ userVisibleOnly: true, applicationServerKey })`.
  - Mengirim payload `PushSubscription` JSON ke backend via endpoint `/subscribe`.

### B. Server / Backend (`server.js`)
- Menggunakan library **`web-push`** (`npm install web-push express cors`).
- Menyimpan konfigurasi **VAPID Keys**:
  - **Public Key**: Dibagikan ke frontend untuk `pushManager.subscribe`.
  - **Private Key**: Disimpan rahasia di backend untuk enkripsi payload saat menembak notifikasi.
- Endpoint:
  - `POST /subscribe`: Menerima dan menyimpan data langganan (endpoint URL APNs + kunci `p256dh` & `auth`) ke database/memori.
  - `POST /trigger-notification`: Menerima payload pesan (`title`, `message`), lalu memanggil `webpush.sendNotification(subscription, payload)`.

---

## 3. Contoh Implementasi Kode

### `sw.js`
```javascript
self.addEventListener('push', function(event) {
    let data = { title: 'Notifikasi Baru', body: 'Pesan dari server.' };
    if (event.data) {
        try {
            data = event.data.json();
        } catch (e) {
            data.body = event.data.text();
        }
    }
    
    let options = {
        body: data.body,
        icon: 'icon-192.png',
        vibrate: [200, 100, 200, 100, 200]
    };
    
    event.waitUntil(
        self.registration.showNotification(data.title, options)
    );
});

self.addEventListener('notificationclick', function(event) {
    event.notification.close();
    event.waitUntil(
        clients.matchAll({ type: 'window' }).then(windowClients => {
            if (windowClients.length > 0) return windowClients[0].focus();
            return clients.openWindow('/');
        })
    );
});
```

### `server.js` (Node.js Backend)
```javascript
const express = require('express');
const webpush = require('web-push');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const publicVapidKey = 'PUBLIC_VAPID_KEY';
const privateVapidKey = 'PRIVATE_VAPID_KEY';

webpush.setVapidDetails(
  'mailto:admin@domain.com',
  publicVapidKey,
  privateVapidKey
);

let subscriptions = []; // Simpan ke database pada aplikasi riil

app.post('/subscribe', (req, res) => {
  const sub = req.body;
  if (!subscriptions.find(s => s.endpoint === sub.endpoint)) {
    subscriptions.push(sub);
  }
  res.status(201).json({ success: true });
});

app.post('/trigger-notification', async (req, res) => {
  const { title, message } = req.body;
  const payload = JSON.stringify({ title, body: message });

  try {
    const promises = subscriptions.map(sub => webpush.sendNotification(sub, payload));
    await Promise.all(promises);
    res.status(200).json({ success: true, message: 'Notifikasi terkirim' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(3000, () => console.log('Backend berjalan di port 3000'));
```

---

## 4. Lokasi Prototype & Pengujian
- **Direktori Proyek Lokal:** `safari-push-test` (`/media/cuker/Data/Projects/test folder/safari-push-test/` atau `D:\Projects\test folder\safari-push-test\`)
- **Cloudflare Pages:** `https://safari-push-test.pages.dev`
- **Tunnel Pengujian HTTPS Lokal:** `ssh -p 443 -R0:localhost:3000 a.pinggy.io`
