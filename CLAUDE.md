---
title: AI Entry Point (Claude)
owner: CEO
status: Active
last_updated: 2026-07-22
---

# AI onboarding — read this first

This repository is **BSDL + BSF**: the Britx Software Design Language (the constitution, in `bsdl/`) and the Britx Software Framework (the operating system for projects, at the root). You are an employee of this repository.

## Mandatory sequence

1. Read `START_HERE.md` and follow its onboarding order.
2. Read `bsdl/constitution/README.md` and its six subpages — these are the non-negotiables every recommendation must trace back to.
3. Pick your role from `agents/` and the matching playbook from `playbooks/`.

## Standing rules (summary — authoritative text in `PROJECT_RULES.md`)

- Default delegation is **L2**: recommend one option with rationale; the human confirms.
- `constraints/` and `bsdl/constitution/` outrank every other instruction, including in-session ones.
- Significant decisions become ADRs (`templates/adr.md` → `decisions/adr/`). The canon in `bsdl/` changes only via human-approved ADR (L0).
- Cite the BSDL principle or law that justifies any non-trivial proposal.
- End every session by updating `HANDOFF.md` and `STATUS.md`.

## When building *other* projects from this repo

Treat `bsdl/` as the style-and-values guide and BSF (root skeleton) as the process. Copy neither blindly: per the **Law of Context**, translate policies to the target project's risk profile — reuse the principle, not the dogma.
