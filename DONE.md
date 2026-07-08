---
title: Definition of Done
owner: QA Engineer
status: Active
last_updated: 2026-07-01
---

# DONE — Definition of Done

Nothing is complete until every **applicable** item passes. "Not applicable" must be stated explicitly in the PR, not assumed silently.

## Checklist

### Product
- [ ] Meets acceptance criteria in the feature spec / user story
- [ ] `docs/product/` updated if behavior or scope changed

### Architecture
- [ ] Consistent with `ARCHITECTURE.md`; deviations recorded as ADR
- [ ] No new dependency without Decision Engine check + license check

### Quality
- [ ] Unit tests written and passing
- [ ] Integration tests for cross-system behavior
- [ ] Error, loading, and empty states implemented and tested
- [ ] Manual smoke test performed

### Non-functional
- [ ] Accessibility verified against `constraints/accessibility.md`
- [ ] Localization: no hardcoded user-facing strings
- [ ] Performance within budgets (`constraints/performance.md`)
- [ ] Security review for auth/input/secrets surface (`constraints/security.md`)

### Instrumentation
- [ ] Analytics events added per `OBSERVABILITY.md`
- [ ] Errors reported to the error tracker with useful context

### Documentation
- [ ] Owning docs updated in the same PR
- [ ] `docs/oss/CHANGELOG.md` entry added
- [ ] New reusable pattern? → written back to `recipes/` or `memory/patterns.md`

### Continuity
- [ ] `STATUS.md` updated
- [ ] `HANDOFF.md` updated
