---
title: "Constraint: Accessibility"
owner: Design
status: Active
last_updated: 2026-07-01
---

# Constraint: Accessibility

> Constraints are **immutable during execution**. AI never violates them. Changing one requires an ADR + human approval (Level 0).

## Non-negotiables
- WCAG 2.2 AA minimum
- Full keyboard operability
- Contrast ratios enforced from DESIGN_SYSTEM tokens
- Every interactive element has an accessible name
- Never rely on color alone to convey state

## Verification
> _How compliance is checked (automated where possible)._
