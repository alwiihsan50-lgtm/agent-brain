# 🐧 Linux Mint Developer Workflow Customizations & Aliases

Dokumentasi standarisasi lingkungan terminal, alat produktivitas, dan konfigurasi sistem operasi Linux Mint 22.3 (Zena) untuk alur kerja fullstack development, automasi trading bot (MT5 Docker), AI pairing, dan dual-boot Windows.

---

## 🛠️ 1. Paket & Utilitas CLI yang Terpasang

- **Starship Prompt (`/usr/local/bin/starship`):** Prompt modern dengan git branch status, runtime version (Node.js, Python), docker context, dan eksekusi durasi. Konfigurasi di `~/.config/starship.toml`.
- **Zoxide (`/usr/bin/zoxide`):** Smart directory jumping (`z <query>`) yang terintegrasi di `~/.bashrc`.
- **FZF (`/usr/bin/fzf`):** Fuzzy finder interaktif untuk pencarian history (`Ctrl+R`) dan file navigation (`Ctrl+T`).
- **LazyDocker (`/usr/local/bin/lazydocker`):** Visual TUI manager untuk container Docker (`ld`).
- **Btop (`/usr/bin/btop`):** TUI system & resource monitor untuk CPU, RAM, Disk, dan Network (`top`).
- **Eza (`/usr/bin/eza`):** Pengganti modern `ls` dengan ikon dan git integration (`ls`, `ll`, `lt`, `tree`).
- **Bat (`/usr/bin/batcat` -> `~/.local/bin/bat`):** Pengganti `cat` dengan syntax highlighting.
- **Graphify CLI (`~/.local/bin/graphify`):** Knowledge graph & AST engine (`gf`, `gfu`, `gfq`, `gfp`, `gfe`, `gf-status`, `gf-viz`).

---

## ⌨️ 2. Standar Aliases Sistem (`~/.bash_aliases`)

```bash
# Navigasi Cepat
alias ddata='cd /media/cuker/Data'
alias dproj='cd /media/cuker/Data/Projects'
alias dbot='cd /home/cuker/mt5_dashboard'
alias dbrain='cd /home/cuker/agent-brain'
alias dtail='cd /home/cuker/tailshare'
alias dhome='cd /home/cuker'

# Modern CLI
alias ls='eza --icons=auto'
alias ll='eza -la --icons=auto --git'
alias la='eza -a --icons=auto'
alias lt='eza --tree --level=2 --icons=auto'
alias tree='eza --tree --icons=auto'
alias cat='bat --paging=never'
alias top='btop'

# Docker & Containers
alias ld='lazydocker'
alias dps='docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'
alias dpsa='docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'
alias dlog='docker logs -f'
alias dstop='docker stop'
alias dstart='docker start'
alias drestart='docker restart'
alias dprune='docker system prune -f'

# Jaringan & Port
alias ports='sudo ss -tulpn | grep LISTEN'
alias myip='curl -s ifconfig.me && echo'
alias localip='hostname -I | awk "{print \$1}"'

# Bot & Service systemd
alias bot-status='sudo systemctl status mt5-trading-bot.service'
alias bot-restart='sudo systemctl restart mt5-trading-bot.service'
alias bot-stop='sudo systemctl stop mt5-trading-bot.service'
alias bot-start='sudo systemctl start mt5-trading-bot.service'
alias bot-logs='journalctl -u mt5-trading-bot.service -f -n 50'

# Git
alias gs='git status -sb'
alias ga='git add'
alias gc='git commit -m'
alias gp='git push'
alias gpl='git pull'
alias gd='git diff'
alias gl='git log --oneline --graph --decorate -n 15'

# 🕸️ Graphify Helpers
alias gf='graphify'
alias gfu='graphify update .'
alias gfq='graphify query'
alias gfp='graphify path'
alias gfe='graphify explain'
gf-status()   # Cek status graphify-out di direktori saat ini
gf-viz()      # Buka graphify-out/graph.html di browser

# 🧠 Agent Brain Shortcuts
alias brain='cd /home/cuker/agent-brain && git status -sb'
brain-sync()  # git pull agent-brain dari GitHub
brain-push()  # git add, commit, & push agent-brain ke GitHub

# Sistem & Dual-boot
alias win='~/reboot-to-windows.sh'
alias reload='source ~/.bashrc && echo "✅ ~/.bashrc berhasil dimuat ulang!"'
alias update='sudo apt update && sudo apt upgrade -y'
alias cls='clear'
```

---

## 🗂️ 3. Symlink & Integrasi File Manager (Nemo)

- Symlink Home:
  - `~/Data` ➔ `/media/cuker/Data`
  - `~/Projects` ➔ `/media/cuker/Data/Projects`
- GTK/Nemo Bookmarks:
  - `file:///media/cuker/Data` (Data Drive D)
  - `file:///media/cuker/Data/Projects` (Projects)
  - `file:///home/cuker/agent-brain` (Agent Brain)

---

## ⚡ 4. Optimasi Memori & Kernel Tuning (16 GB RAM)

- **`preload` Daemon:** Layanan LSB adaptive readahead yang memantau aplikasi sering dibuka dan melakukan prefetching otomatis ke RAM cache.
- **`tmpfs` untuk `/tmp` (`/etc/systemd/system/tmp.mount`):** Folder sementara berkapasitas 50% RAM (~7.7 GB) dipasang di RAM, mempercepat I/O file sementara dan mengurangi siklus tulis pada SSD.
- **Sysctl Virtual Memory (`/etc/sysctl.d/99-performance-tuning.conf`):**
  - `vm.swappiness=10`: Mengutamakan penggunaan RAM dan meminimalisir swap.
  - `vm.vfs_cache_pressure=50`: Menahan cache direktori/file di RAM lebih lama.

