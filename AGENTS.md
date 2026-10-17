---
title: AI Entry Point (Agents)
owner: CEO
status: Active
last_updated: 2026-10-16
---

# AI onboarding — read this first

Polaris holds the Polaris Constitution (canonical in `polaris/`) and the governance registry. The owner-authorised Axis extraction to Axis and specialist relocation are recorded in ADR-004; this entry point does not grant release or merge authority.

## Mandatory sequence

1. Read `START_HERE.md` and follow its onboarding order.
2. Read `polaris/constitution/README.md` and its six subpages — these are the non-negotiables every recommendation must trace back to.
3. Read `integration/README.md`. Inspect the adopting project, select only its enabled/requested disciplines and read their entry points. Polaris has no local engineering `playbooks/` directory.

4. For experimental A0 contextual routing, read `integration/a0.md` and the optional repo-local `.agents/skills/constellation-a0/SKILL.md`. They are advisory extensions to the v1 planner and cannot authorize execution.

## Standing rules (summary — authoritative text in `PROJECT_RULES.md`)

- Apply L2 to unresolved consequential decisions. Proceed with reversible work already authorised within the task scope; preserve explicit human gates.
- The Constitution governs derived rules; adopted hard constraints require explicit recorded amendment. Operational defaults must fit the project context. Apply the authority and conflict rules in `PROJECT_RULES.md` without claiming precedence over host instructions or permissions.
- Significant decisions become ADRs in `decisions/adr/`; Axis’s ADR template is optional. The canon in `polaris/` changes only via human-approved ADR (L0).
- Trace consequential recommendations to the relevant Polaris constitutional principle or law, with concrete evidence.
- Update continuity records when state changes or work remains; deliver read-only evidence without artificial repository writes.

## When building *other* projects from this repo

A project explicitly records adoption of Polaris governance and its applicable profiles. Standalone use of Axis, Meridian or Sentinel does not silently adopt the full Polaris process; each capability retains its own essential quality and safety guarantees. For governed projects, translate the constitutional principles and operating framework to the project's risk profile — reuse the principle, not the dogma.
