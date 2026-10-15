---
title: "Constraint: Cost"
owner: CEO
status: Active
last_updated: 2026-10-15
---

# Constraint: Cost

> Prevents AI from suggesting overengineered solutions. Immutable during execution.

## Non-negotiables
- **Any new recurring cost is L0.** No exceptions, no trials that auto-convert.
- Prefer free tiers and services already in the stack before adding vendors.

## Infrastructure and vendor decisions
- New recurring spend, paid trials and per-seat services require explicit L0 approval.
- Introduce infrastructure only with a concrete need, maintenance/exit costs and rollback plan.
- Reuse services actually present and suitable in the project; do not assume a vendor is installed.
- Historical vendor preferences and infrastructure avoid-list are retained in `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/profiles/web-typescript.md`. Adopting that profile does not approve spend or provisioning.

## Verification
- PR reviewer checks new dependencies/services against this list.
- `STATUS.md` risk section flags any cost-bearing proposal awaiting L0.
