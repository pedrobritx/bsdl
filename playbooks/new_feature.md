---
title: "Playbook: New Feature"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Playbook: New Feature

The canonical loop: idea → shipped. Every feature follows this; skipping steps requires an ADR.

## When to use
New user-facing capability or significant behavior change. (Small corrections → Bug Fix; structure-only → Refactor.)

## Phase 0 — Context (Product Manager role)
1. Read `docs/product/PRODUCT.md`, `USER_STORIES.md`, `ROADMAP.md`.
2. Write the spec from `templates/feature_spec.md`.
3. **Question Engine pass:** open the relevant `recipes/*.md` — every "Before implementing" item is answered or escalated. A spec with open questions is not ready.
4. Human approves the spec (L2 default: recommend, confirm).

## Phase 1 — Design (Designer + Architect roles)
5. Designer: UX flow + screen spec, all states, from Design System components. Update `UX_FLOWS.md` / `SCREENS.md`.
6. Architect: check the Decision Engine for every technical choice; new significant decisions → ADR via `templates/adr.md`.
7. Data Engineer: schema delta per `templates/database_table.md` — migration and rollback drafted now, not later.

## Phase 2 — Build (Backend + Frontend roles)
8. Backend: endpoints per `templates/api_endpoint.md`; Zod validation; error taxonomy from `ERROR_HANDLING.md`.
9. Frontend: implement from the screen spec; tokens only; loading/empty/error states are part of the feature, not polish.
10. Both: check `memory/preferences.md` and `memory/patterns.md` before choosing any pattern.

## Phase 3 — Quality (QA role)
11. Full test set per `TESTING.md` checklist.
12. Accessibility + localization verification.
13. QA verdict against `DONE.md` — every item passed or explicitly N/A with justification.

## Phase 4 — Ship & Learn
14. Merge per `WORKFLOWS.md`; release per the Release playbook if applicable.
15. `CHANGELOG.md` entry (*Added*).
16. New reusable pattern discovered? Write it back: `recipes/` (if a standard) or `memory/patterns.md` (if a technique).
17. Update `STATUS.md` + `HANDOFF.md`.

## Validation
Acceptance criteria demonstrably met; DONE.md green; analytics events firing.

## Completion checklist
- [ ] Spec approved before code
- [ ] Question Engine items closed
- [ ] ADRs filed for significant decisions
- [ ] DONE.md fully satisfied
- [ ] Learning written back (recipe/pattern/lesson)
- [ ] STATUS + HANDOFF updated
