*Honest answers to the questions everyone asks first.* — [[Home]]

### Is this tied to Claude?

No. **Framework Over Tooling** is principle #10: BSF is plain Markdown in a git repo, and the framework — not the model — holds the memory, standards, and decision process. It works with Claude Code, Codex, Gemini CLI, Cursor, Amp, or whatever ships next.

### Why not just a CLAUDE.md?

A tool-specific config file works today and breaks on tool change — that's option 2 in [ADR-000](https://github.com/pedrobritx/bsf/blob/main/decisions/adr/000-adopt-bsf.md), considered and rejected. A single file also can't carry an org model, delegation levels, per-decision policies, append-only memory, and CI-enforced structure. BSF is what a CLAUDE.md wants to be when it grows up — and your AI tool's config file can simply say "read `START_HERE.md`".

### How is this different from Scrum / Shape Up?

Those are methodologies for coordinating *humans*: ceremonies, cadences, estimation. BSF is an operating system for a *hybrid* company where most execution is AI and the scarce resource is context and judgment, not standup time. The overlapping concerns (what to build next, definition of done) exist in BSF as documents and checklists rather than meetings. You can run Scrum on top of BSF if your humans need it — the two don't compete.

### What happens when I switch AI tools mid-project?

Nothing, structurally. The new tool reads `START_HERE.md`, walks the same onboarding sequence, loads the same role file, and inherits the same memory, decisions, and handoff. That's the point: context survives conversations, sessions, *and models*. Your only real work is wiring the new tool's entry point to `START_HERE.md`.

### Do I need all 119 files for a weekend prototype?

Honestly: no. Set your delegation defaults to L3/L4, ignore `docs/business/` and most of `docs/` until they matter, and let the AI run playbooks autonomously. What you still want even on a weekend: `constraints/` (the guardrails), the Decision Engine (instant answers to stack questions), and `HANDOFF.md` (so Sunday-you remembers what Saturday-you did). The framework scales down — empty docs cost nothing, and they're there when the prototype graduates.

---

**→ In the repository**
- [decisions/adr/000-adopt-bsf.md](https://github.com/pedrobritx/bsf/blob/main/decisions/adr/000-adopt-bsf.md) — the options considered
- [README.md](https://github.com/pedrobritx/bsf/blob/main/README.md) — what BSF is and is not

See also: [[Core Principles]] · [[Getting Started]]
