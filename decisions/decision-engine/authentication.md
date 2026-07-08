---
title: "Decision: Authentication"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Decision Policy: Authentication

## Default
**Supabase Auth.** Already in the stack, RLS-native, no extra vendor, generous free tier (cost constraint).

## Use Clerk instead only if
- Complex B2B org management (orgs, invitations, per-org roles) is a day-one requirement, or
- Enterprise SSO (SAML/OIDC) is on the near-term roadmap.

## Avoid
- **Firebase Auth** — locks into a parallel ecosystem we don't use; weaker Postgres/RLS story.
- **Hand-rolled auth** — never. Security constraint.

## Rationale
See `recipes/authentication.md` for the how. First ADR applying this policy should be filed as `decisions/adr/00X-auth-provider.md` per project.

## Delegation level
**Level 3** — apply the default automatically if no "use Clerk instead" trigger is present; log the decision. Triggers present → L1 (present options).
