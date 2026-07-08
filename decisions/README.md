---
title: Decisions
owner: Software Architect
status: Active
last_updated: 2026-07-01
---

# Decisions

Two complementary systems:

## `adr/` — Architectural Decision Records
Permanent, per-project records: **why** something was decided. Numbered `NNN-slug.md`, per `templates/adr.md`. Superseded, never deleted. Six months from now, "why are we using X?" already has an answer.

## `decision-engine/` — Reusable policies
Pre-answered recurring questions: **what** to choose by default, when to deviate, what to avoid. Instead of asking "which auth provider?" on every project, the policy already contains the preferred solution, exceptions, and rationale — with its own delegation level.

## Lifecycle
```
Question arises → policy exists? ──yes→ apply at its level, log
        │no
        ▼
Propose (AI Governance format) → human decides → ADR filed
        │
        ▼
Recurring? → promote into decision-engine/  (Continuous Learning)
```
