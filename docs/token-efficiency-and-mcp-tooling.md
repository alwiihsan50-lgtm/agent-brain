# ⚡ Panduan Tooling Efisiensi Token & MCP Server

Dokumen ini mencatat standarisasi utility dan MCP Server penghemat token yang terpasang di host Linux Mint (`/home/cuker/.local/bin/` & `~/.gemini/config/mcp_config.json`).

---

## 🎯 1. Daftar Tool yang Dipasang

| Tool | Tipe / Bin Path | Fungsi Utama | Cara Pakai Singkat |
| :--- | :--- | :--- | :--- |
| **`web2md`** | Python CLI (`~/.local/bin/web2md`) | Mengonversi halaman dokumentasi/web menjadi clean markdown via Jina Reader (`r.jina.ai`) dengan fallback lokal. Menghemat 80-90% token dari raw HTML. | `web2md "https://docs.example.com" -m 50` |
| **`tokcut`** | Python CLI (`~/.local/bin/tokcut`) | Smart output truncator untuk terminal. Membatasi output command besar (build/test/log) agar hanya mengambil header dan error tail. | `tokcut <perintah>` atau `cmd \| tokcut -n 30` |
| **`sqlite-utils`** | UV Tool (`~/.local/bin/sqlite-utils`) | Inspeksi skema & query database SQLite tanpa perlu load dump SQL besar. | `sqlite-utils schema database.db` |
| **`mcp-server-sqlite`** | UV Tool MCP Server | Server MCP resmi untuk query dan inspeksi skema database via protokol Model Context Protocol. | Terdaftar di `~/.gemini/config/mcp_config.json` |
| **`sqlite3`** | Native Linux CLI (`/usr/bin/sqlite3`) | Utility command-line native SQLite3 untuk manajemen database lokal. | `sqlite3 database.db ".schema"` |

---

## ⚙️ 2. Konfigurasi MCP Global (`~/.gemini/config/mcp_config.json`)

```json
{
  "mcpServers": {
    "sqlite-marketing": {
      "command": "/home/cuker/.local/bin/mcp-server-sqlite",
      "args": ["--db-path", "/media/cuker/Data/marketing agent/ttagent/database/tiktok_tracker.db"]
    }
  }
}
```

---

## 📜 3. Aturan Standar Token Efficiency (Primary Workflow)

Seluruh AI Agent yang bekerja di workstation ini **WAJIB** mematuhi 5 pilar efisiensi token berikut sebagai workflow utama:

### 1. Web & Documentation Browsing (Hemat 80–90% Token)
- **Aturan:** Dilarang melakukan fetch mentah (raw HTML/dump) yang menghabiskan ribuan baris token tidak perlu.
- **Workflow:**
  * Dokumen standar / artikel / web umum: Gunakan `web2md "<URL>" -m 50`
  * Halaman dinamis / JS-heavy / SPA: Gunakan `crawl4ai` via environment Python terpusat (`/home/cuker/.ai-browser-tools/bin/python`).

### 2. Terminal Execution & Build Output
- **Aturan:** Dilarang membiarkan command dengan output ratusan/ribuan baris mencemari context window.
- **Workflow:**
  * Bungkus command berisiko output panjang dengan `tokcut`:
    ```bash
    tokcut npm run build
    tokcut cargo test
    cat large_file.log | tokcut -n 30
    ```
  * Hanya header, error tail, dan ringkasan penting yang disajikan ke LLM.

### 3. Database & Schema Inspection
- **Aturan:** Dilarang melakukan dump SQL atau query `SELECT *` tanpa batas pada database besar.
- **Workflow:**
  * Inspeksi struktur: `sqlite-utils schema <path_to_db>` atau gunakan MCP `sqlite-marketing`.
  * Query terarah: `sqlite-utils tables <path_to_db> --counts` atau `sqlite3 <db> "SELECT ... LIMIT 10;"`.

### 4. Code Intelligence & Navigation
- **Aturan:** Hindari membaca seluruh file kode berukuran ratusan/ribuan baris sekaligus.
- **Workflow:**
  * Navigasi arsitektur: `graphify query "<pertanyaan>"`, `graphify explain "<simbol>"`, atau `graphify path <source> <target>`.
  * Pembacaan file: Selalu gunakan pembacaan range baris spesifik (`StartLine`, `EndLine`).

### 5. Shared Memory & Status Preservation
- **Aturan:** Simpan konteks yang selesai di `docs/history/` dan jaga `README.md` tetap ringkas (<100 baris) agar booting agent tetap instan dan hemat token.

