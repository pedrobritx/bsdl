---
title: "ADR-000: Adopt the Britx Software Framework"
owner: CEO
status: Accepted
last_updated: 2026-07-01
---

# ADR-000: Adopt the Britx Software Framework

## Problem
Software projects lose context across AI conversations, models, and time. Decisions vanish, preferences are relearned, and each project reinvents standards.

## Options considered
1. **Ad-hoc docs + prompts per project** — flexible; context evaporates; no reuse.
2. **Tool-specific config (e.g. CLAUDE.md only)** — works today; breaks on tool change (violates Framework Over Tooling).
3. **BSF** — model-agnostic operating system; repository holds memory, standards, decisions.

## Decision
Adopt BSF. The repository is the company; AI models are interchangeable employees.

## Consequences
+ Context, decisions, and knowledge survive any model change.
+ Every project starts from established standards.
− Documentation discipline required in every PR (mitigated by CI validation + DONE.md).

## Confidence
95% — governance model tested informally across prior projects; formalized here.

## Links
`README.md` · `PROJECT_RULES.md` · `automation/validate_docs.py`
