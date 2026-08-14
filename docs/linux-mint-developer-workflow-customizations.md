# 🐧 Linux Mint Developer Workflow Customizations & Aliases

Dokumentasi standarisasi lingkungan terminal, alat produktivitas, dan konfigurasi sistem operasi Linux Mint 22.3 (Zena) untuk alur kerja fullstack development, automasi trading bot (MT5 Docker), AI pairing, dan dual-boot Windows.

---

## 🛠️ 1. Paket & Utilitas CLI yang Terpasang

- **Starship Prompt (`/usr/local/bin/starship`):** Prompt modern dengan git branch status, runtime version (Node.js, Python), docker context, dan eksekusi durasi. Konfigurasi di `~/.config/starship.toml`.
- **Zoxide (`/usr/bin/zoxide`):** Smart directory jumping (`z <query>`) yang terintegrasi di `~/.bashrc`.
- **FZF (`/usr/bin/fzf`):** Fuzzy finder interaktif untuk pencarian history (`Ctrl+R`) dan file navigation (`Ctrl+T`).
- **LazyDocker (`/usr/local/bin/lazydocker`):** Visual TUI manager untuk container Docker.
- **Btop (`/usr/bin/btop`):** TUI system & resource monitor untuk CPU, RAM, Disk, dan Network.
- **Eza (`/usr/bin/eza`):** Pengganti modern `ls` dengan ikon dan git integration.
- **Bat (`/usr/bin/batcat` -> `~/.local/bin/bat`):** Pengganti `cat` dengan syntax highlighting.

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
