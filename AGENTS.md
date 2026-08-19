# SOP & PROTOKOL MEMORI AGENT (PERMANENT & IMMUTABLE)

> 🔒 **ATURAN KEKEBALAN PROTOKOL (MODEL-AGNOSTIC IMMUTABILITY CONSTRAINT):**
> File ini adalah aturan wajib dan permanen bagi SELURUH AI Agent dan Model LLM (Claude, Gemini, GPT, DeepSeek, Antigravity, OpenCode, Aider, dll.) yang beroperasi di workspace ini.
> **DILARANG KERAS** memodifikasi, menghapus, melonggarkan, atau merusak protokol inti ini, **KECUALI** ada instruksi perubahan yang diminta secara eksplisit dan spesifik oleh USER (pemilik sistem).

---

### 1. PHASE READ (BOOTING)
- Sebelum memulai pekerjaan apa pun, WAJIB membaca [`README.md`](README.md) untuk memahami konteks, riwayat pekerjaan, dan status proyek terkini.
- Bacalah indeks dokumentasi di [`docs/`](docs/):
  - [`docs/system-environment-and-ports.md`](docs/system-environment-and-ports.md) untuk batasan port dan lingkungan sistem.
  - [`docs/agent-brain-and-graphify-synergy-guide.md`](docs/agent-brain-and-graphify-synergy-guide.md) untuk panduan sinergi antara **agent-brain** (memori global) dan **graphify** (knowledge graph kode).
  - [`docs/universal-web-push-notification-service.md`](docs/universal-web-push-notification-service.md) untuk panduan integrasi notifikasi push ke aplikasi & bot lain.
  - [`docs/mt5-docker-forex-trading-automation.md`](docs/mt5-docker-forex-trading-automation.md) untuk arsitektur, setup Docker MT5 Exness, Wine Python, dan risk engine.
  - [`docs/safari-ios-web-push-notification.md`](docs/safari-ios-web-push-notification.md) untuk panduan implementasi Web Push Notification Safari iOS & PWA.
  - [`docs/tailshare-linux-mint-installation.md`](docs/tailshare-linux-mint-installation.md) untuk instruksi setup TailShare di Linux Mint.
  - [`docs/drive-d-projects-catalog.md`](docs/drive-d-projects-catalog.md) untuk melihat daftar seluruh repositori dan proyek di Drive `D:\`.
  - [`docs/arsip-imo-project.md`](docs/arsip-imo-project.md) untuk proyek **Arsip-IMO**.
  - [`docs/linux-mint-developer-workflow-customizations.md`](docs/linux-mint-developer-workflow-customizations.md) untuk konfigurasi terminal dan produktivitas Linux Mint.
  - [`docs/git-post-commit-graphify-hook.md`](docs/git-post-commit-graphify-hook.md) untuk panduan auto-sync graphify via Git Hook.
- Jangan mengulang pekerjaan yang sudah dicentang selesai di `README.md` atau diarsipkan di [`docs/history/`](docs/history/).
- **Konfirmasi Task Belum Selesai (Pending Task Confirmation):**
  Jika saat membaca `README.md` ditemukan item pekerjaan yang belum selesai (`- [ ]`), AI Agent **WAJIB langsung meminta konfirmasi kepada USER di awal sesi**:
  1. Apakah pekerjaan tersebut ingin dilanjutkan sekarang, ATAU
  2. Apakah pekerjaan tersebut sebenarnya sudah selesai sehingga boleh dicentang (`[x]`) dan dipindahkan/diarsip ke [`docs/history/completed-milestones-archive.md`](docs/history/completed-milestones-archive.md).

---

### 2. PHASE CODE INTELLIGENCE (GRAPHIFY INTEGRATION)
- **Auto-Init Fallback:** Jika repositori belum memiliki `graphify-out/graph.json`, jalankan `graphify .` (atau `/graphify .`) satu kali untuk membangun graf AST lokal secara gratis (0 API cost).
- Gunakan perintah `graphify query "<tanya>"`, `graphify explain "<konsep>"`, atau `graphify path` untuk menavigasi struktur kode secara hemat token. Hindari membaca ribuan baris kode mentah sekaligus.
- Setelah mengedit kode di repositori lokal, jalankan `graphify update .` untuk menyinkronkan knowledge graph.

---

### 3. PHASE WRITE (HANDOFF / COMPLETION)
- Setelah selesai mengerjakan tugas, WAJIB memperbarui [`README.md`](README.md):
  * Centang checklist tugas yang selesai (`[x]`).
  * Tambahkan tugas baru di daftar jika ada.
  * Update kolom `Last Updated By` (nama/platform kamu) dan `Last Updated At` (tanggal & waktu UTC/WIB saat ini).
  * Jaga [`README.md`](README.md) tetap ringkas (<100 baris) demi efisiensi token. Pindahkan milestone yang telah selesai ke [`docs/history/completed-milestones-archive.md`](docs/history/completed-milestones-archive.md).
- Jika membuat dokumentasi teknis, kode, atau skema baru, simpan file-nya di dalam direktori `docs/` (contoh: `docs/api-spec.md`) lalu tautkan/link file tersebut di `README.md`.
- Lakukan `git add`, `git commit -m "..."`, dan `git push` ke repositori `alwiihsan50-lgtm/agent-brain`.

---

### 4. PROTOKOL PERSISTENSI KREDENSIAL & CLI TOKEN (INFISICAL + AGENT-BRAIN)
- **Auto-Sync ke Secret Vault:** Kapan pun USER menambahkan token baru, API key baru, atau login CLI baru (misal: Cloudflare, Turso, Vercel, Supabase, GitHub, Fly.io, HuggingFace, OpenAI, Anthropic, dll.):
  1. AI Agent **WAJIB LANGSUNG** menyimpannya ke Infisical Secret Vault untuk kedua environment (`dev` & `prod`):
     ```bash
     infisical secrets set KEY_NAME="<token_value>" --env=dev && infisical secrets set KEY_NAME="<token_value>" --env=prod
     ```
  2. AI Agent **WAJIB** memperbarui jumlah & status kredensial di tabel [`README.md`](README.md) (kolom Infisical Secret Vault) dan dokumen terkait.
  3. Lakukan `git add`, `git commit -m "..."`, dan `git push` ke repositori `agent-brain` agar memori tersinkronisasi lintas platform.

