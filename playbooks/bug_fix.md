---
title: "Playbook: Bug Fix"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Playbook: Bug Fix

## When to use
A defect in shipped behavior needs correction.

## Required reading
1. `STATUS.md` (known bugs)
2. `docs/engineering/ERROR_HANDLING.md`
3. `docs/engineering/TESTING.md`

## Steps
1. Reproduce the bug and write a failing test first
2. Locate root cause (not symptom)
3. Check `memory/mistakes.md` — has this class of bug happened before?
4. Fix with the smallest correct change
5. Run full test suite
6. Record the lesson in `memory/mistakes.md` if it is a recurring class

## Validation
Failing test now passes; no regressions; error taxonomy respected.

## Documentation updates
ERROR_HANDLING if a new error class was introduced; CHANGELOG under *Fixed*.

## Completion checklist
- [ ] All steps executed
- [ ] Validation passed
- [ ] Documentation updated
- [ ] `docs/oss/CHANGELOG.md` updated
- [ ] `STATUS.md` and `HANDOFF.md` updated
- [ ] `DONE.md` criteria satisfied
