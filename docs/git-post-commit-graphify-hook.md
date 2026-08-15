# 🪝 Panduan Git Post-Commit Hook: Auto-Sync Graphify

Dokumen ini menjelaskan cara memasang dan memanfaatkan **Git Post-Commit Hook** untuk memastikan Knowledge Graph (`graphify-out/`) pada repositori kode Anda otomatis ter-update setiap kali ada commit baru, tanpa perlu dijalankan secara manual oleh developer maupun AI Agent.

---

## 🎯 Mengapa Memakai Hook Ini?

1. **Otomatis & Silent:** Berjalan di latar belakang setiap kali `git commit` selesai dieksekusi.
2. **0 Biaya API Token:** Menggunakan AST deterministic parser (`graphify update .`).
3. **Mencegah Graf Usang (*Stale Graph*):** Peta arsitektur kode selalu sinkron dengan baris kode terbaru di branch Git.

---

## 🛠️ Isi Script Hook (`.git/hooks/post-commit`)

```bash
#!/bin/bash
# Auto-update graphify knowledge graph on new commit
if command -v graphify >/dev/null 2>&1; then
    if [ -d "graphify-out" ]; then
        echo "🕸️ [Graphify] Mengupdate knowledge graph lokal..."
        (graphify update . >/dev/null 2>&1 &)
    fi
fi
```

---

## 🚀 Cara Pemasangan Otomatis

Jalankan perintah berikut di dalam direktori repositori Git target:

```bash
# Buat file hook dan beri izin eksekusi
cat << 'EOF' > .git/hooks/post-commit
#!/bin/bash
if command -v graphify >/dev/null 2>&1; then
    if [ -d "graphify-out" ]; then
        (graphify update . >/dev/null 2>&1 &)
    fi
fi
EOF
chmod +x .git/hooks/post-commit
```

Atau gunakan helper script yang tersedia di `scripts/install-graphify-hook.sh`.
