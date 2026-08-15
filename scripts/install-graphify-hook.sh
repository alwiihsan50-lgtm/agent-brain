#!/bin/bash
# ==============================================================================
# 🪝 Helper Script: Pasang Git Post-Commit Hook untuk Graphify
# Penggunaan: ./install-graphify-hook.sh [path-ke-repo]
# ==============================================================================

REPO_DIR="${1:-.}"

if [ ! -d "$REPO_DIR/.git" ]; then
    echo "❌ Error: Direktori '$REPO_DIR' bukan repositori Git!"
    exit 1
fi

HOOK_FILE="$REPO_DIR/.git/hooks/post-commit"

cat << 'EOF' > "$HOOK_FILE"
#!/bin/bash
# Auto-update graphify knowledge graph on new commit
if command -v graphify >/dev/null 2>&1; then
    if [ -d "graphify-out" ]; then
        (graphify update . >/dev/null 2>&1 &)
    fi
fi
EOF

chmod +x "$HOOK_FILE"
echo "✅ Git Post-Commit Hook berhasil dipasang di: $HOOK_FILE"
