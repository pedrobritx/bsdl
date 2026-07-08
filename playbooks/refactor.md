---
title: "Playbook: Refactor"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Playbook: Refactor

## When to use
Structure needs improvement without behavior change.

## Required reading
1. `docs/engineering/ARCHITECTURE.md`
2. `constraints/coding_standards.md`
3. `memory/patterns.md`

## Steps
1. Confirm test coverage of the target area BEFORE touching it
2. State the target structure and why (1 paragraph in the PR)
3. Refactor in small, reviewable commits
4. Behavior must be identical — no feature changes smuggled in
5. Update `memory/patterns.md` if a reusable pattern emerged

## Validation
All tests green; no public contract changed; diff reviewed against ARCHITECTURE.

## Documentation updates
ARCHITECTURE if structure map changed; ADR if a structural decision was made.

## Completion checklist
- [ ] All steps executed
- [ ] Validation passed
- [ ] Documentation updated
- [ ] `docs/oss/CHANGELOG.md` updated
- [ ] `STATUS.md` and `HANDOFF.md` updated
- [ ] `DONE.md` criteria satisfied
