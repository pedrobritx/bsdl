---
title: "Playbook: Security Review"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Playbook: Security Review

## When to use
Periodic review, new sensitive surface, or pre-release audit.

## Required reading
1. `docs/engineering/SECURITY.md`
2. `constraints/security.md`
3. `docs/engineering/AUTH.md`

## Steps
1. Enumerate the attack surface of the change/area
2. Check auth, input validation, secrets, dependencies, RLS
3. Run dependency audit
4. File findings by severity; Level 0 escalation for critical findings
5. Verify fixes; re-test

## Validation
No critical/high findings open; audit output attached to PR.

## Documentation updates
SECURITY if the threat model changed; INCIDENT_RESPONSE if a live issue was found.

## Completion checklist
- [ ] All steps executed
- [ ] Validation passed
- [ ] Documentation updated
- [ ] `docs/oss/CHANGELOG.md` updated
- [ ] `STATUS.md` and `HANDOFF.md` updated
- [ ] `DONE.md` criteria satisfied
