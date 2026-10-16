---
title: Decisions
owner: Software Architect
status: Active
last_updated: 2026-10-15
---

# Decisions

Two complementary systems:

## `adr/` — Architectural Decision Records
Permanent, per-project records: **why** something was decided. Numbered `NNN-slug.md`, per `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/templates/adr.md`. Superseded, never deleted. Six months from now, "why are we using X?" already has an answer.

## `decision-engine/` — Reusable policies
Pre-answered recurring questions: **what** to choose by default, when to deviate, what to avoid. Instead of asking "which auth provider?" on every project, the policy already contains the preferred solution, exceptions, and rationale — with its own delegation level.

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
