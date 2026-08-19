# 🌐 Panduan Tools Automasi & Navigasi Browser AI

Dokumen ini mencatat instalasi, konfigurasi, dan cara penggunaan 3 tools automasi browser yang dipasang di sistem Linux Mint untuk kebutuhan AI Agent lintas platform.

---

## 🛠️ 1. Tiga Pilar Automasi Browser

| Tool | Tipe / Engine | Lokasi / Konfigurasi | Kapan Digunakan |
| :--- | :--- | :--- | :--- |
| **`@playwright/mcp`** | **MCP Server (Native Tool)** | `/home/cuker/.agents/plugins/playwright-browser/` | **Interaksi Langsung di Sesi Chat:** Navigasi web, klik tombol, isi form, dan tangkap screenshot tanpa perlu membuat file script perantara. |
| **`crawl4ai`** | **Python Library / Async Crawler** | `/home/cuker/.ai-browser-tools` | **Riset & Scraping Cepat:** Mengambil konten website dinamis (JavaScript-heavy/SPA) dan langsung mengubahnya menjadi Markdown bersih siap baca dengan token minimal. |
| **`browser-use`** | **Python Autonomous Agent** | `/home/cuker/.ai-browser-tools` | **Tugas Otonom Multi-Step:** Alur kerja panjang berbasis visi komputer (misal: mencari produk, membandingkan harga di banyak tab, mengisi form berulang). |

---

## 📂 2. Struktur Instalasi & Environment

* **Python Virtualenv Terisolasi:**
  ```bash
  /home/cuker/.ai-browser-tools/
  ```
  Berisi `crawl4ai`, `browser-use`, `playwright`, `patchright`, `pydantic`, dan dependensi terkait.

* **Playwright Browser Binaries:**
  Tersedia Chromium di direktori cache sistem (`~/.cache/ms-playwright/`).

* **Konfigurasi MCP Server (`.agents/plugins/playwright-browser/`):**
  - Manifest: `plugin.json`
  - Konfigurasi: `mcp_config.json` (menjalankan `@playwright/mcp` via npx headless mode).

---

## 💻 3. Contoh Penggunaan Singkat

### A. Ekstraksi Web Cepat dengan `crawl4ai` (Python)
```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com")
        print(result.markdown)  # Markdown bersih siap olah LLM

if __name__ == "__main__":
    asyncio.run(main())
```
*Eksekusi:* `/home/cuker/.ai-browser-tools/bin/python script.py`

### B. Automasi Tugas Otonom dengan `browser-use` (Python)
```python
import asyncio
from browser_use import Agent
from langchain_openai import ChatOpenAI  # atau provider LLM lainnya

async def main():
    agent = Agent(
        task="Buka halaman Wikipedia tentang Linux dan cari versi kernel pertama.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🔒 4. Keamanan & Best Practices
- Seluruh browser dijalankan secara aman di lingkungan lokal.
- Sesi Playwright MCP secara default menggunakan mode `--headless` untuk menjaga efisiensi RAM dan CPU.
- Direktori `.ai-browser-tools` berada di home user dan tidak mengganggu paket sistem APT Debian/Mint.
