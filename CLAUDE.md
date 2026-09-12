# CLAUDE.md - Central Agent Memory & Protocols

> 🔒 **IMMUTABILITY & INTEGRITY CONSTRAINT:**
> All rules, architecture guidelines, reserved ports (`40506`, `3000`, `8080`), and Dual-Engine workflow protocols are permanent and binding.
> Do NOT modify, bypass, or delete these rules unless explicitly requested by the USER.

Refer to [`AGENTS.md`](AGENTS.md) and [`README.md`](README.md) for full operational protocols.

### Key Rules:
1. **Booting:** Read [`README.md`](README.md) and relevant docs in [`docs/`](docs/) before starting any task.
2. **Code Intelligence:** Use `graphify query` / `explain` / `path` for token-efficient AST navigation. Auto-run `graphify .` if `graphify-out/graph.json` is missing.
3. **Graph Sync:** Run `graphify update .` after code edits.
4. **Task Completion & Handoff:** **STRICT USER CONFIRMATION**: Never mark tasks as complete (`[x]`) or archive them autonomously—all new and ongoing tasks remain `- [ ]` until directly and explicitly confirmed by the USER. Present "Ready for Review" report (Changes, Proof of Work, One-liner verification) to the USER.
5. **Tooling & Sync:** Use `brain status`, `brain task add`, `brain health`, `brain session`, and `brain push "<msg>"` to maintain memory integrity and push updates to `alwiihsan50-lgtm/agent-brain`.
