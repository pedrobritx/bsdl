---
title: "Template: Feature Specification"
owner: Product Manager
status: Active
last_updated: 2026-07-01
---

# Template: Feature Specification

Every feature starts identically. Copy this, fill it, link it from the PR.

```markdown
# Feature: <name>

## Problem
What user/business problem this solves. Link USER_STORIES.

## Users
Who is affected and how.

## Acceptance criteria
- [ ] Given / when / then …

## Database changes
Tables/columns touched. Link SCHEMA + DATA_DICTIONARY. Migration + rollback plan.

## API changes
New/modified endpoints per templates/api_endpoint.md.

## UI changes
Screens/components per SCREENS + DESIGN_SYSTEM. All states: loading/empty/error.

## Analytics
Events to add per OBSERVABILITY.md.

## Tests
Required set per TESTING.md.

## Documentation
Which owning docs update in the same PR.

## Migration & rollback
How existing users/data are affected; how we back out.

## Delegation
Decision classes touched + their levels. Open questions for the human.
```
