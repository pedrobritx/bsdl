---
title: "Constraint: Performance"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Constraint: Performance

> Constraints are **immutable during execution**. AI never violates them. Changing one requires an ADR + human approval (Level 0).

## Non-negotiables
- LCP < 2.5s, INP < 200ms, CLS < 0.1 on production
- API p95 < 400ms for standard reads
- No unbounded client-side lists — paginate or virtualize
- Bundle budget per route defined in PERFORMANCE.md

## Verification
> _How compliance is checked (automated where possible)._
