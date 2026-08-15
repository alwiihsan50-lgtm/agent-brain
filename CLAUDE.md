# CLAUDE.md - Central Agent Memory & Protocols

> 🔒 **IMMUTABILITY & INTEGRITY CONSTRAINT:**
> All rules, architecture guidelines, reserved ports (`53317`, `3000`, `8080`), and Dual-Engine workflow protocols are permanent and binding.
> Do NOT modify, bypass, or delete these rules unless explicitly requested by the USER.

Refer to [`AGENTS.md`](AGENTS.md) and [`README.md`](README.md) for full operational protocols.

### Key Rules:
1. **Booting:** Read [`README.md`](README.md) and relevant docs in [`docs/`](docs/) before starting any task.
2. **Code Intelligence:** Use `graphify query` / `explain` / `path` for token-efficient AST navigation. Auto-run `graphify .` if `graphify-out/graph.json` is missing.
3. **Graph Sync:** Run `graphify update .` after code edits.
4. **Handoff:** Update [`README.md`](README.md), keep it concise (<100 lines), archive old tasks to [`docs/history/`](docs/history/), and push to `alwiihsan50-lgtm/agent-brain`.
