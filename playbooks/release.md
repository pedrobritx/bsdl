---
title: "Playbook: Release"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Playbook: Release

## When to use
A version is ready to ship.

## Required reading
1. `docs/engineering/RELEASE.md`
2. `docs/engineering/WORKFLOWS.md`
3. `STATUS.md`

## Steps
1. Verify `DONE.md` for every item in the release
2. Update version per SemVer and tag
3. Update `docs/oss/CHANGELOG.md`
4. Deploy per RELEASE procedure
5. Smoke-test production
6. Monitor OBSERVABILITY dashboards for 30 min
7. Update `STATUS.md` deployment status

## Validation
Smoke tests pass; error rate stable; rollback plan confirmed available.

## Documentation updates
CHANGELOG finalized; ROADMAP milestone marked shipped.

## Completion checklist
- [ ] All steps executed
- [ ] Validation passed
- [ ] Documentation updated
- [ ] `docs/oss/CHANGELOG.md` updated
- [ ] `STATUS.md` and `HANDOFF.md` updated
- [ ] `DONE.md` criteria satisfied
