---
title: "Playbook: Performance Optimization"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Playbook: Performance Optimization

## When to use
A performance budget is exceeded or at risk.

## Required reading
1. `docs/engineering/PERFORMANCE.md`
2. `constraints/performance.md`
3. `docs/engineering/OBSERVABILITY.md`

## Steps
1. Measure first — capture a baseline with real numbers
2. Identify the single biggest bottleneck
3. Propose the fix with expected gain (Delegation Level applies)
4. Implement and re-measure against baseline
5. Record the technique in `memory/patterns.md`

## Validation
Post-change measurement meets budget; no functional regressions.

## Documentation updates
PERFORMANCE with new numbers; ADR if an architectural trade-off was made.

## Completion checklist
- [ ] All steps executed
- [ ] Validation passed
- [ ] Documentation updated
- [ ] `docs/oss/CHANGELOG.md` updated
- [ ] `STATUS.md` and `HANDOFF.md` updated
- [ ] `DONE.md` criteria satisfied
