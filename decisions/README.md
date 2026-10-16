---
title: Decisions
owner: Software Architect
status: Active
last_updated: 2026-10-16
---

# Decisions

Two complementary systems:

## `adr/` — Architectural Decision Records
Permanent, per-project records: **why** something was decided. Numbered `NNN-slug.md`; use the project’s format or constitutional decision record. Axis’s ADR template is optional. Superseded, never deleted. Six months from now, "why are we using X?" already has an answer.

## Adopted project policies
Reusable policy templates live in Axis; adopted policy instances live in the project. Polaris does not contain a local `decision-engine/` directory. Pre-answered recurring questions: **what** to choose by default, when to deviate, what to avoid. Instead of asking "which auth provider?" on every project, the policy already contains the preferred solution, exceptions, and rationale — with its own delegation level.

## Policy readiness
Only a complete adopted policy is operative. It must state scope, prerequisites, decision/default, rationale, exceptions, approval level and review trigger. A Draft or placeholder is treated as no policy. Never invent missing policy contents or treat a confidence score as authority.

## Lifecycle
```
Question arises → complete adopted policy fits? ──yes→ check hard gates, apply, record
        │no
        ▼
Propose (AI Governance format) → human decides → ADR filed
        │
        ▼
Recurring? → promote into decision-engine/  (Continuous Learning)
```
