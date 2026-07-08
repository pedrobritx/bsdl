---
title: Automation
owner: DevOps Engineer
status: Active
last_updated: 2026-07-01
---

# Automation

Scripts that keep the framework honest (Automation Over Repetition).

| Script | Does |
|---|---|
| `validate_docs.py` | Enforces front matter + checks relative links. Runs in CI on every PR. |

## Planned
- Dependency-graph builder from front matter (`depends_on`/`related` → visual graph)
- Stale-doc detector (`last_updated` vs git history of owned code)
- HANDOFF/STATUS freshness check at PR time
