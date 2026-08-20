# 🎵 TikTok Marketing Agent Suite (`ttagent`)

Dokumentasi arsitektur, CLI command `tt`, automasi produksi video pendek 9:16, TikTok Shop, Live Streaming, dan sistem CRM Leads / Affiliate.

---

## 📂 Lokasi Workspace
- **Direktori:** `/media/cuker/Data/marketing agent/ttagent`
- **Global Launcher CLI:** `/home/cuker/.local/bin/tt`
- **Runtime Environment:** Python 3.11 (`/home/cuker/.ai-browser-tools/bin/python`)
- **Browser Profile:** `/home/cuker/.ai-browser-tools/tiktok_profile`

---

## 🏗️ Modul & Komponen Utama

| Modul | File | Fungsi Utama |
| :--- | :--- | :--- |
| **CLI App** | `tt.py` | Command center antarmuka terminal interaktif berbasis Typer & Rich. |
| **Media Engine** | `tools/video_optimizer.py` | FFmpeg 9:16 scaler, EXIF/metadata stripper, cover generator with high-CTR headline. |
| **Script Engine** | `tools/script_generator.py` | Generator naskah video 15s/30s/60s, 100+ bank viral hook, spintax SEO captions. |
| **Live Engine** | `tools/live_script_generator.py` | Generator rundown 60 menit TikTok Live selling, cue cards, & flash sale drops. |
| **Hashtag Matrix** | `tools/hashtag_researcher.py` | Generator bundle tagar 4-8 tags terstruktur (Mega, Niche, Commercial, Local). |
| **Closing Helper** | `tools/closing_helper.py` | Bank script respon cepat DM TikTok, WhatsApp Bio Link, dan affiliate pitch. |
| **Database CRM** | `tools/tracker.py` | SQLite DB (`database/tiktok_tracker.db`): Video pipeline, FYP metrics, Leads & Creator CRM. |
| **Browser Worker** | `tools/tt_worker.py` | Automasi Playwright dengan persistent session untuk TikTok Studio. |

---

## ⚡ Perintah Cepat CLI `tt`

```bash
tt dashboard        # Ringkasan workspace, video pipeline, FYP metrics, dan CRM
tt script           # Wizard interaktif pembuat naskah video TikTok (15s/30s/60s)
tt hooks            # Jelajahi 100+ bank formula viral hooks (Curiosity, Negative, FOMO, dll.)
tt media            # Olah video/foto mentah menjadi 9:16 vertikal (1080x1920)
tt cover            # Buat cover/thumbnail 9:16 dengan headline tebal & badge
tt live             # Buat rundown live selling 60 menit & cue cards
tt hashtags         # Racik tagar SEO TikTok optimal
tt scripts          # Bank script chat respon cepat & template outreach affiliate
tt add-video        # Catat video baru ke pipeline konten
tt videos           # Tampilkan daftar pipeline konten
tt update-metrics   # Catat metrik performa video (views, likes, comments, orders, GMV)
tt add-lead         # Catat leads masuk dari TikTok Bio Link
tt leads            # Daftar prospek CRM
tt add-creator      # Catat creator affiliate untuk kirim sample produk
tt creators         # Daftar creator affiliate & status sample
tt login            # Login & simpan sesi browser TikTok persisten
tt check-login      # Cek status login akun TikTok
tt studio           # Buka TikTok Creator Studio di browser
```
