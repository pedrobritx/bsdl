---
title: "ADR-002 (Proposed): Polaris, Axis, Meridian, and Sentinel"
owner: CEO
status: Proposed
last_updated: 2026-10-14
---

# ADR-002 (Proposed): Four independent products under Polaris governance

## Purpose
Propose the Polaris/Axis transition without renaming, extracting, deleting or publishing anything until ratified by the human owner.

## Scope
Governance, engineering, design, security, AI orchestration, interoperability and repository ownership. This ADR does not approve a new brand, changes to the Polaris constitution, nor any production mutation.

## Context

Historical proposal; current terminology is normalized under ADR-005. Extraction authority is separately recorded in ADR-004.
The current repository combines the Polaris canon in `polaris/` with the Axis operating framework at the root. Meridian is a separate working product with its own Figma integration, tests and deployment. The desired future allows standalone adoption of Axis, Meridian and Security (Sentinel) as well as complete Polaris-governed adoption.

## Proposed decision
1. **Polaris**: constitutional governance identity, accountable for ratified principles, cross-product contracts, policy selection, orchestration, project adoption, agent delegation and approval gates. Preserve Polaris canon and ADR history during migration.
2. **Axis**: engineering capability, independently distributable reference architectures, engineering playbooks, project profiles, scaffolds, development workflows, data and deployment adapters. Do not require Meridian.
3. **Meridian**: independent visual and interaction design system. Preserve the existing Figma file, 0.5 stable baseline, versioned evidence, bridge workflow and 0.6 experimental isolation. Do not require Axis.
4. **Sentinel**: independent security engineering discipline: threat modeling, identity/access requirements, application security, supply chain, security checks, secure agent/tool boundaries and security evidence. Do not become a home-grown authentication provider.
5. Each product owns its implementation and release. Polaris describes *composition*, not compulsory runtime imports; no cyclic dependencies.
6. Security, accessibility, product quality, and observability remain cross-cutting obligations. Sentinel owns security verification, Axis functional/performance verification, Meridian visual/interaction/accessibility evidence, and Polaris gates policy and evidence aggregation.
7. Risk-proportionate oversight follows existing delegation: L0 human-only for constitutional, security-critical, destructive, financial and production-sensitive decisions; L2 default for major proposed changes.

## Candidate ownership
| Existing asset | Proposed owner | Migration treatment |
| --- | --- | --- |
| `polaris/` and ratified constitution | Polaris | Preserve unchanged first; rename terminology only through separate approved ADR |
| `PROJECT_RULES.md` constraints/delegation | Polaris | Preserve human-only decisions; reconcile project-specific engineering policy later |
| `agents/CEO.md`, project-level coordination | Polaris | Keep orchestration role, link specialist implementations |
| `agents/architect.md`, engineering roles and implementation recipes | Axis | Extract with provenance, review duplicates before removing from Polaris |
| `agents/designer.md` | Meridian subject matter; Polaris registry | Move specialist instruction only after agreed adoption contract |
| `agents/security_engineer.md` | Sentinel subject matter; Polaris registry | Move specialist instruction only after security repo is initialized |
| `playbooks/`, `recipes/`, `templates/`, `automation/` | Mixed | Inventory and classify individually; do not bulk move blindly |
| `.github/workflows/docs-validate.yml` | Polaris initially | Retain canon validation; Axis gets its own project-specific validation later |
| `.github/workflows/wiki-sync.yml` and `.wiki/` | Polaris | Preserve with wiki backup and post-rename smoke test |
| Meridian's four `.github/workflows/` | Meridian | Keep running locally; update only deliberate integration references |

## Distribution and contracts
- Each capability remains usable without the other three products.
- Polaris supplies an opt-in, versioned composition manifest, with explicit capability ownership and support matrix.
- Prefer reviewed pull requests and versioned artifacts to unreviewed cross-repository writes.
- Lock reusable workflow references by commit SHA where feasible and grant least privilege.
- Source-specific secrets remain in their respective systems, not a Polaris-wide secret store.
- Every cross-product integration must be tested *both* with and without Polaris.

## Alternatives
- Keep one monorepo: simplest initially, but weak independent distribution and ownership boundaries.
- Split by frontend/backend/mobile/DevOps: excessive coordination, code reuse friction and duplicated cross-cutting responsibilities.
- Split Polaris/Axis immediately before inventory: high risk of broken docs, workflows, agents and historical references.

## Consequences and risks
Positive: independent adoption, clearer ownership, smaller tool interfaces, separate versions, less cross-product coupling.
Negative: extra release and contract maintenance, cross-repository compatibility tests, migration of old references, and name-collision risk.
Guardrails: no forced rename, branch deletion, credential migration, forced push, production modification or automatic merge under this proposal.

## Related documents
- Existing ADR-001: `decisions/adr/001-polaris-canon-three-surfaces.md`
- Existing constitution: `polaris/constitution/README.md`
- Transition inventory and runbook: `docs/proposals/2026-10-14-polaris-transition.md`

## Open questions for owner approval
1. Ratify the four product names and final spelling of the umbrella name.
2. Canonical identity and path naming were subsequently authorised in ADR-005.
3. Confirm repository visibility/licensing and how public/shared workflows will be distributed.
4. Approve the extraction strategy and exact first consumer project.

**State:** PROPOSED. No implementation or governance decision has been ratified by this document.
