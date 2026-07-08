---
title: "Playbook: Migration"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Playbook: Migration

## When to use
Schema or data must change shape.

## Required reading
1. `docs/engineering/MIGRATION_GUIDE.md`
2. `docs/engineering/SCHEMA.md`
3. `docs/engineering/DATA_DICTIONARY.md`

## Steps
1. Write the migration and its rollback together
2. Dry-run on a copy of production-like data
3. Verify SEED_DATA still loads
4. Apply in staging; validate; then production
5. Update SCHEMA and DATA_DICTIONARY in the same PR

## Validation
Rollback tested; data integrity checks pass; docs updated atomically.

## Documentation updates
SCHEMA, DATA_DICTIONARY, MIGRATION_GUIDE if the process itself changed.

## Completion checklist
- [ ] All steps executed
- [ ] Validation passed
- [ ] Documentation updated
- [ ] `docs/oss/CHANGELOG.md` updated
- [ ] `STATUS.md` and `HANDOFF.md` updated
- [ ] `DONE.md` criteria satisfied
