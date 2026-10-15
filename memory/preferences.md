---
title: "Memory: Preferences"
owner: CEO
status: Active
last_updated: 2026-10-15
---

# Memory: Preferences

> Preferences are context, not universal law. Explicit current owner decisions and the repository's actual architecture guide their application. Surface conflicts with adopted hard constraints; do not pretend conflicts are impossible.

## Code
- Write code, code comments, code instructions and code reviews in English (explicit owner instruction, 2026-10-15).
- Historical web technology preferences are preserved in `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/profiles/web-typescript.md`; apply them only in an explicitly adopted matching context.

## Architecture
- Simplicity over cleverness; boring technology wins.
- Where an adopted PostgreSQL/Supabase profile fits, consider pgvector before adding a separate vector service; do not impose it on other architectures.
- One vendor doing two jobs beats two vendors doing one each.

## Process
- Dry-run before destructive or infra changes.
- Terminal co-engineer mode for ops: command → output → analysis → refined command.
- Explain decisions in clear prose. Keep useful code comments for constraints and non-obvious reasons; avoid comments that merely narrate the code.

## Format
```
### [YYYY-MM-DD] Preference
Context:
Preference:
Strength: (default | strong | absolute)
```

## Entries
_Add as they emerge. Promote "absolute" entries into `constraints/` via ADR._
