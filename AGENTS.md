---
title: AI Entry Point (Agents)
owner: CEO
status: Active
last_updated: 2026-10-15
---

# AI onboarding — read this first

Polaris holds the Polaris Constitution (canonical in `polaris/`) and the governance registry. The owner-authorised Axis extraction to Axis and specialist relocation are recorded in ADR-004; this entry point does not grant release or merge authority.

## Mandatory sequence

1. Read `START_HERE.md` and follow its onboarding order.
2. Read `polaris/constitution/README.md` and its six subpages — these are the non-negotiables every recommendation must trace back to.
3. Pick your role from `agents/` and the matching playbook from `playbooks/`.

## Standing rules (summary — authoritative text in `PROJECT_RULES.md`)

- Apply L2 to unresolved consequential decisions. Proceed with reversible work already authorised within the task scope; preserve explicit human gates.
- The Constitution governs derived rules; adopted hard constraints require explicit recorded amendment. Operational defaults must fit the project context. Apply the authority and conflict rules in `PROJECT_RULES.md` without claiming precedence over host instructions or permissions.
- Significant decisions become ADRs (`https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/templates/adr.md` → `decisions/adr/`). The canon in `polaris/` changes only via human-approved ADR (L0).
- Trace consequential recommendations to the relevant Polaris constitutional principle or law, with concrete evidence.
- Update continuity records when state changes or work remains; deliver read-only evidence without artificial repository writes.

## When building *other* projects from this repo

A project explicitly records adoption of Polaris governance and its applicable profiles. Standalone use of Axis, Meridian or Sentinel does not silently adopt the full Polaris process; each capability retains its own essential quality and safety guarantees. For governed projects, translate the constitutional principles and operating framework to the project's risk profile — reuse the principle, not the dogma.
