---
title: Definition of Done
owner: QA Engineer
status: Active
last_updated: 2026-10-15
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
- [ ] Evidence of the intended outcome recorded. Analytics is optional and requires a justified purpose, minimal collection and explicit approval; follow `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/engineering/OBSERVABILITY.md` if adopted.
- [ ] Errors reported to the error tracker with useful context

### Documentation
- [ ] Owning docs updated in the same PR
- [ ] `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/oss/CHANGELOG.md` entry added
- [ ] New reusable pattern? → written back to `recipes/` or `memory/patterns.md`

### Continuity
- [ ] `STATUS.md` updated
- [ ] `HANDOFF.md` updated
