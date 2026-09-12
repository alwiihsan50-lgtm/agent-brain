# SOP & PROTOKOL MEMORI AGENT (PERMANENT & IMMUTABLE)

> 🔒 **ATURAN KEKEBALAN PROTOKOL (MODEL-AGNOSTIC IMMUTABILITY CONSTRAINT):**
> File ini adalah aturan wajib dan permanen bagi SELURUH AI Agent dan Model LLM (Claude, Gemini, GPT, DeepSeek, Antigravity, OpenCode, Aider, dll.) yang beroperasi di workspace ini.
> **DILARANG KERAS** memodifikasi, menghapus, melonggarkan, atau merusak protokol inti ini, **KECUALI** ada instruksi perubahan yang diminta secara eksplisit dan spesifik oleh USER (pemilik sistem).

---

### 1. PHASE READ (BOOTING)
- Sebelum memulai pekerjaan apa pun, WAJIB membaca [`README.md`](README.md) untuk memahami konteks, riwayat pekerjaan, dan status proyek terkini.
- Bacalah indeks dokumentasi di [`docs/`](docs/):
  - [`docs/system-environment-and-ports.md`](docs/system-environment-and-ports.md) untuk batasan port dan lingkungan sistem.
  - [`docs/token-efficiency-and-mcp-tooling.md`](docs/token-efficiency-and-mcp-tooling.md) untuk standarisasi utility penghemat token (`web2md`, `tokcut`, `sqlite-utils`, MCP SQLite).
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
  2. Apakah pekerjaan tersebut sudah divalidasi tuntas oleh USER sehingga boleh dicentang (`[x]`) dan dipindahkan/diarsip ke [`docs/history/completed-milestones-archive.md`](docs/history/completed-milestones-archive.md). (*Ingat: DILARANG mengasumsikan atau mencentang selesai tanpa persetujuan langsung USER*).

---

### 2. PHASE CODE INTELLIGENCE (GRAPHIFY INTEGRATION)
- **Auto-Init Fallback:** Jika repositori belum memiliki `graphify-out/graph.json`, jalankan `graphify .` (atau `/graphify .`) satu kali untuk membangun graf AST lokal secara gratis (0 API cost).
- Gunakan perintah `graphify query "<tanya>"`, `graphify explain "<konsep>"`, atau `graphify path` untuk menavigasi struktur kode secara hemat token. Hindari membaca ribuan baris kode mentah sekaligus.
- Setelah mengedit kode di repositori lokal, jalankan `graphify update .` untuk menyinkronkan knowledge graph.

---

### 3. PHASE WRITE (HANDOFF, VERIFIKASI & ATURAN MUTLAK PENYELESAIAN TUGAS)
- ⚠️ **ATURAN MUTLAK PENYELESAIAN TUGAS (NO AUTO-COMPLETION):**
  * AI Agent **DILARANG KERAS** menganggap selesai atau mencentang checklist (`[x]`) secara mandiri/sepihak, baik untuk **pekerjaan baru** maupun **pekerjaan lama yang belum selesai**.
  * Seluruh pekerjaan baru atau pekerjaan yang sedang berjalan **WAJIB tetap berstatus belum selesai (`- [ ]`)** sampai USER secara langsung dan eksplisit mengonfirmasi bahwa pekerjaan tersebut benar-benar tuntas.
  * Hanya setelah mendapatkan konfirmasi eksplisit dari USER:
    1. Item pekerjaan boleh diubah menjadi dicentang (`[x]`).
    2. Milestone yang selesai dipindahkan/diarsipkan ke [`docs/history/completed-milestones-archive.md`](docs/history/completed-milestones-archive.md) agar `README.md` tetap ringkas (<100 baris).

- 🔍 **PROTOKOL STANDAR "READY FOR REVIEW" (VERIFIABLE HANDOFF):**
  Ketika AI Agent selesai mengimplementasikan tugas dan siap diverifikasi USER, AI Agent **WAJIB** menyajikan laporan dengan format:
  1. **Perubahan yang Dilakukan (What Changed):** Ringkasan file, endpoint, atau fungsi yang dimodifikasi.
  2. **Bukti Pengujian (Proof of Work):** Output eksekusi test terminal, respon status curl HTTP 200, atau verifikasi browser/screenshot.
  3. **Cara Verifikasi Cepat (One-Liner Verification):** Perintah CLI 1 baris atau URL yang bisa langsung diuji oleh USER dalam hitungan detik.
  4. **Call to Action Konfirmasi:** Meminta persetujuan eksplisit dari USER: *"Mohon review hasil di atas. Jika sudah sesuai, beri tahu saya agar status tugas dapat saya tandai selesai (`[x]`) di agent-brain."*

- 🛠️ **STANDARISASI CLI HELPER (`brain`):**
  Tersedia utility terpusat `brain` di `~/.local/bin/brain` untuk menjaga integritas memori:
  * `brain status` : Cek daftar tugas aktif, active session, dan status port real-time.
  * `brain health` : Healthcheck konektivitas seluruh reserved ports & endpoints.
  * `brain task add "<deskripsi>"` : Tambah tugas baru berstatus `- [ ]` ke `README.md`.
  * `brain task done <id> --confirm-user` : Tandai tugas selesai `[x]` hanya jika USER telah konfirmasi.
  * `brain session set ...` & `brain session clear` : Kelola [`ACTIVE_SESSION.md`](ACTIVE_SESSION.md).
  * `brain push "<pesan-commit>"` : Validasi batas baris `README.md`, update timestamp, commit, dan push otomatis ke GitHub.

- 📝 **ACTIVE SESSION SCRATCHPAD (`ACTIVE_SESSION.md`):**
  Untuk pekerjaan multi-tahap yang belum selesai atau sebelum terjadi pergantian agent, catat konteks aktif (project, task, modified files, blockers) ke [`ACTIVE_SESSION.md`](ACTIVE_SESSION.md) menggunakan `brain session set`. Setelah tugas tuntas divalidasi USER, reset ke IDLE via `brain session clear`.

---

### 4. PROTOKOL PERSISTENSI KREDENSIAL & CLI TOKEN (INFISICAL + AGENT-BRAIN)
- **Auto-Sync ke Secret Vault:** Kapan pun USER menambahkan token baru, API key baru, atau login CLI baru (misal: Cloudflare, Turso, Vercel, Supabase, GitHub, Fly.io, HuggingFace, OpenAI, Anthropic, dll.):
  1. AI Agent **WAJIB LANGSUNG** menyimpannya ke Infisical Secret Vault untuk kedua environment (`dev` & `prod`):
     ```bash
     infisical secrets set KEY_NAME="<token_value>" --env=dev && infisical secrets set KEY_NAME="<token_value>" --env=prod
     ```
  2. AI Agent **WAJIB** memperbarui jumlah & status kredensial di tabel [`README.md`](README.md) (kolom Infisical Secret Vault) dan dokumen terkait.
  3. Lakukan `git add`, `git commit -m "..."`, dan `git push` ke repositori `agent-brain` agar memori tersinkronisasi lintas platform.

---

### 5. PROTOKOL SUITE BROWSER AUTOMATION (UNTUK SELURUH AI AGENT)
Seluruh AI Agent yang beroperasi di workstation ini memiliki akses penuh ke **AI Browser Automation Suite**:
- **Environment Python Terpusat:**
  ```bash
  /home/cuker/.ai-browser-tools/bin/python
  ```
  *(Sudah terpasang `crawl4ai`, `browser-use`, `playwright`, Chromium Headless Shell, dan library LLM).*

- **Panduan Pemilihan & Eksekusi Tool:**
  1. **Scraping / Membaca Web Modern (JS-Heavy / SPA) ➔ Gunakan `crawl4ai`:**
     Untuk membaca dokumentasi atau halaman dinamis menjadi Markdown bersih secara instan:
     ```bash
     /home/cuker/.ai-browser-tools/bin/python -c "
     import asyncio
     from crawl4ai import AsyncWebCrawler
     async def run():
         async with AsyncWebCrawler() as c:
             res = await c.arun('<TARGET_URL>')
             print(res.markdown)
     asyncio.run(run())
     "
     ```
  2. **Interaksi Native & Verifikasi UI / Screenshot ➔ Gunakan `@playwright/mcp`:**
     Konfigurasi MCP Server aktif di [`.agents/plugins/playwright-browser/mcp_config.json`](../.agents/plugins/playwright-browser/mcp_config.json). Agent dengan kapabilitas MCP dapat memanggil tools browser langsung untuk klik tombol, isi form, dan screenshot localhost.
  3. **Navigasi Otonom Multi-Langkah & Vision ➔ Gunakan `browser-use`:**
     Gunakan untuk workflow penjelajahan web mandiri. Panduan lengkap dan script template tersedia di [`docs/ai-browser-automation-tools.md`](docs/ai-browser-automation-tools.md).

---

### 6. PROTOKOL UTAMA EFISIENSI TOKEN (TOKEN EFFICIENCY FIRST WORKFLOW)
Seluruh AI Agent **WAJIB** menerapkan prinsip hemat token sebagai workflow utama dalam setiap tugas:
1. **Web & Documentation Browsing:**
   - Gunakan `web2md "<URL>"` (Jina Reader markdown converter) dibanding HTTP raw fetch / HTML dump mentah untuk menghemat 80-90% token.
   - Contoh: `web2md "https://docs.example.com" -m 50`
2. **Terminal Execution & Logs Output:**
   - Bungkus eksekusi test/build/log panjang dengan `tokcut` atau pipe `| tokcut -n 30` untuk membatasi output hanya pada header dan tail error relevan.
   - Contoh: `tokcut npm run build` atau `cat large.log | tokcut -n 40`
3. **Database & SQLite Inspection:**
   - Gunakan `sqlite-utils schema <db>` atau tool MCP SQLite (`sqlite-marketing`) untuk inspeksi struktur tabel.
   - Hindari dump SQL mentah atau query `SELECT *` tanpa filter `LIMIT`.
4. **Code Navigation & Selective Reading:**
   - Gunakan `graphify query "<tanya>"`, `graphify explain "<konsep>"`, atau `graphify path` sebelum membuka file source code mentah.
   - Gunakan pembacaan baris spesifik (slice line range `StartLine`/`EndLine`) dan hindari membaca ribuan baris kode sekaligus jika hanya membutuhkan bagian tertentu.


