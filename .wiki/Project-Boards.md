*The GitHub Projects layer: live work state for the framework's workflows.* — [[Home]]

Boards hold **work state only** — specifications live in feature-spec instances in the repo, never in a card ([[Document Standards]]).

## The five master projects

| Project | Purpose | Column field |
|---|---|---|
| **BSF · Kanban** | The daily driver. Columns mirror the work lifecycle with an explicit DoD gate: Backlog → Spec → In Progress → In Review · DoD → Blocked → Done. | `Stage` |
| **BSF · Roadmap** | Now / Next / Later / Shipped horizons with Start/Target dates for the roadmap layout. | `Horizon` |
| **BSF · Product Launch** | Phase-gated launch: Foundation → Build → Hardening → Launch Prep → Launch → Post-launch, with an explicit Go/No-Go field. | `Phase` |
| **BSF · Feature Release** | Mirrors the five phases of the New Feature playbook exactly — the board *is* the playbook: 0 · Context → 1 · Design → 2 · Build → 3 · Quality → 4 · Ship & Learn → Done. | `Phase` |
| **BSF · Bug Triage** | Severity-driven pipeline: New → Reproduced → Root-caused → Fix in progress → Verifying → Closed. | `Pipeline` |

All five live at [github.com/pedrobritx?tab=projects](https://github.com/pedrobritx?tab=projects).

## The field taxonomy

Shared by all five (so copies stay faithful): `Agent Role` (PM…Writer), `Delegation` (L0–L4), `Confidence` (number). Per-board: the column field above, plus `Playbook` and `Priority` (Kanban), `Milestone`/`Start`/`Target` (Roadmap), `Go/No-Go` and `Due` (Launch), `DoD` and `Target release` (Feature Release), `Severity` and `Regression?` (Bug Triage).

**Labels ↔ fields:** repo labels mirror the board fields so issues carry their routing with them — `playbook:*` labels ↔ the `Playbook` field, `role:*` ↔ `Agent Role`, `L0`–`L4` ↔ `Delegation`, `sev:1`–`sev:4` ↔ `Severity`.

## Instantiating per product (personal accounts)

Marking Projects as reusable *templates* is an organization-only GitHub feature. On a personal account the pattern is: **keep the five masters pristine and copy them per product**:

```
gh project copy <number> --source-owner pedrobritx --target-owner pedrobritx --title "MyApp · Kanban"
```

Copies inherit fields and draft items; link the copy to the product repo with `gh project link`.

---

**→ In the repository**
- [playbooks/new_feature.md](https://github.com/pedrobritx/bsf/blob/main/playbooks/new_feature.md) — the five phases the Feature Release board mirrors
- [DONE.md](https://github.com/pedrobritx/bsf/blob/main/DONE.md) — the gate behind "In Review · DoD"
- [templates/feature_spec.md](https://github.com/pedrobritx/bsf/blob/main/templates/feature_spec.md) — where specs live (not in cards)

See also: [[Playbooks]] · [[Getting Started]]
