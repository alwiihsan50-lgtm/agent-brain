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

## 📜 3. Aturan Token Efficiency untuk AI Agent

1. **Browsing Dokumen:** Gunakan `web2md` dibanding HTTP raw scrape biasa.
2. **Log & Testing Output:** Bungkus eksekusi test/build panjang dengan `tokcut` atau tail parameter.
3. **Database Inspection:** Gunakan `sqlite-utils schema` atau tool MCP SQLite daripada membaca seluruh baris data.
4. **Code Navigation:** Selalu gunakan `graphify query` / AST parser sebelum membaca file source code secara utuh.
