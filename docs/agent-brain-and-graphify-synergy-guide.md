# 🧠🕸️ Panduan Sinergi: agent-brain & graphify

Dokumen ini menjelaskan integrasi sinergi antara **`agent-brain`** (Penyimpanan Memori & Strategi Lintas Repositori) dan **`graphify`** (Knowledge Graph & Analisis AST Kode Lokal) untuk seluruh AI Agent di lingkungan kerja ini.

---

## 🎯 Mengapa Keduanya Diperlukan Bersama?

* **`agent-brain` (The Strategist & Long-Term Memory):**
  Menjawab pertanyaan tingkat makro / lintas sistem:
  - *"Apa saja proyek di komputer ini?"*
  - *"Mengapa kita memilih Cloudflare Workers daripada Telegram?"*
  - *"Port berapa saja yang sudah dipesan agar tidak bentrok?"*
  - *"Apa yang telah kita capai pada sesi sebelumnya?"*

* **`graphify` (The Code Cartographer & Deep Explorer):**
  Menjawab pertanyaan tingkat mikro / per-repositori:
  - *"Fungsi mana yang memanggil fungsi X?"*
  - *"Bagaimana alur dependency dari file index ke worker?"*
  - *"Tampilkan subgraph relasi antar modul tanpa membaca ribuan baris kode secara mentah."*

---

## 🔄 Siklus Alur Kerja Sinergis (The Synergy Lifecycle)

1. **Phase 1: Orientasi Konteks Makro (`agent-brain`)**
   Agent membuka `agent-brain/README.md` dan dokumen terkait di `agent-brain/docs/` untuk memahami batasan, aturan port (`docs/system-environment-and-ports.md`), dan riwayat pekerjaan. Jika terdapat item pekerjaan yang belum selesai (`- [ ]`), Agent wajib meminta konfirmasi ke user apakah ingin dilanjutkan atau diarsip.

2. **Phase 2: Eksplorasi Kode Mikro (`graphify`)**
   - **Auto-Init:** Jika `graphify-out/graph.json` belum ada di repositori target, jalankan `graphify .` (0 token API cost, AST engine).
   - Agent menanyakan arsitektur kode secara terfokus:
     ```bash
     graphify query "<pertanyaan arsitektur atau alur kode>"
     graphify explain "<nama fungsi / konsep>"
     graphify path "<modul_A>" "<modul_B>"
     ```
   - Membaca `graphify-out/wiki/index.md` untuk menjelajahi struktur kode dengan hemat token.

3. **Phase 3: Eksekusi & Pembaruan Kode**
   Agent memodifikasi atau membangun fitur pada repositori yang bersangkutan.

4. **Phase 4: Sinkronisasi Graph Lokal (`graphify`)**
   Setelah kode dimodifikasi, perbarui graf AST:
   ```bash
   graphify update .
   ```
   *(Opsional: pasang Git Post-Commit Hook agar langkah ini berjalan otomatis di background).*

5. **Phase 5: Pencatatan Memori Permanen (`agent-brain`)**
   Agent memperbarui `agent-brain/README.md` (checklist, status aktif), mengarsipkan riwayat lama ke `docs/history/`, mencatat dokumen baru jika ada, lalu melakukan `git commit` dan `git push` ke repositori `alwiihsan50-lgtm/agent-brain`.

---

## 🛡️ Best Practices & Git Management
- `graphify-out/` dan `.graphify_*` secara global telah di-ignore melalui `~/.gitignore_global` sehingga tidak akan mencemari commit kode aplikasi.
- `agent-brain/README.md` dijaga ringkas (<100 baris) agar fase Booting AI Agent selalu cepat dan hemat token.
