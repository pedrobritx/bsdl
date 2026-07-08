---
title: "Constraint: Security"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Constraint: Security

> Constraints are **immutable during execution**. AI never violates them. Changing one requires an ADR + human approval (Level 0).

## Non-negotiables
- No secrets in code, logs, or prompts — ever
- All inputs validated at the boundary (Zod)
- Auth required by default; public endpoints are explicit allow-list
- Dependencies audited before adding; no unmaintained packages
- RLS enabled on all Supabase tables

## Verification
> _How compliance is checked (automated where possible)._
