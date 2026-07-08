---
title: Start Here
owner: All
status: Active
last_updated: 2026-07-01
---

# START HERE

**You are an employee of this repository.** Before doing anything, onboard yourself. No AI begins coding before understanding context.

## Onboarding sequence (mandatory, in order)

| # | Read | You now understand |
|---|---|---|
| 1 | `PROJECT_RULES.md` | The constitution: principles, governance, delegation |
| 2 | `docs/product/VISION.md` | Why this product exists |
| 3 | `docs/product/PRODUCT.md` | What it does and for whom |
| 4 | `docs/engineering/ARCHITECTURE.md` | How it is structured |
| 5 | `docs/product/ROADMAP.md` | Where it is going |
| 6 | `STATUS.md` | Where it is right now |
| 7 | `HANDOFF.md` | What the last session left for you |

## Then, before acting

1. **Identify your role.** Read your file in `agents/`. It defines your responsibilities, required reading, and what you must never do.
2. **Pick the playbook.** Feature? Bug? Release? `playbooks/` has the workflow. Follow it.
3. **Check the Decision Engine.** Before asking "which library/provider/pattern?", check `decisions/decision-engine/`. The answer likely exists.
4. **Check memory.** `memory/preferences.md` and `memory/mistakes.md` encode what this company has already learned. Do not relearn it the hard way.
5. **Respect constraints.** Everything in `constraints/` is non-negotiable. Violations are never acceptable, regardless of delegation level.

## Session contract

- **During work:** follow your playbook's checklist; record significant decisions as ADRs (`templates/adr.md` → `decisions/adr/`).
- **Before proposing:** apply the AI Governance format from `PROJECT_RULES.md` (confidence, reasoning, risks, alternatives).
- **At session end:** update `HANDOFF.md` and `STATUS.md`. This is not optional — it is how the company remembers.

## If information is missing

Do not guess. Use the Question Engine pattern: the relevant recipe (`recipes/`) and decision policy (`decisions/decision-engine/`) contain "Before implementing" checklists. Surface unanswered items to the human at the appropriate delegation level.
