---
title: "Constraint: Performance"
owner: Engineering
status: Active
last_updated: 2026-10-15
---

# Constraint: Performance

> Constraints are **immutable during execution**. AI never violates them. Changing one requires an ADR + human approval (Level 0).

## Non-negotiables
- Set measurable budgets for the project's actual platform, user tasks and representative hardware.
- The historical web/API defaults are retained in `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/profiles/web-typescript.md`; adopting another platform does not import web-only metrics.
- No unbounded client-side lists — paginate or virtualize
- Record applicable runtime, payload, memory and response budgets in `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/engineering/PERFORMANCE.md`.

## Verification
Record the tested workload, device/environment, measurements and limits. Budget declarations are not evidence of measured performance.
