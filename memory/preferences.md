---
title: "Memory: Preferences"
owner: CEO
status: Active
last_updated: 2026-07-01
---

# Memory: Preferences

> Institutional preferences that survive individual conversations. AI checks this before choosing any pattern or library. Conflicts with `constraints/` are impossible by construction — constraints win.

## Code
- Prefer **Zustand** over Context API for shared state.
- Prefer **React Server Components** and **Server Actions**.
- Prefer **Tailwind**.
- Always **Zod** at boundaries.
- Never **moment.js** — `date-fns` / Temporal.

## Architecture
- Simplicity over cleverness; boring technology wins.
- pgvector before dedicated vector DBs.
- One vendor doing two jobs beats two vendors doing one each.

## Process
- Dry-run before destructive or infra changes.
- Terminal co-engineer mode for ops: command → output → analysis → refined command.
- Explanations outside code blocks, never as inline annotations.

## Format
```
### [YYYY-MM-DD] Preference
Context:
Preference:
Strength: (default | strong | absolute)
```

## Entries
_Add as they emerge. Promote "absolute" entries into `constraints/` via ADR._
