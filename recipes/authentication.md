---
title: "Recipe: Authentication"
owner: Engineering
status: Active
last_updated: 2026-07-01
---

# Recipe: Authentication

How this company builds authentication. Follow it; deviate only via ADR. Policy rationale lives in `decisions/decision-engine/authentication.md`.

## Before implementing — answer these (Question Engine)
- [ ] Social login? Which providers?
- [ ] MFA required, optional, or none?
- [ ] Passwordless (magic link / passkeys)?
- [ ] Session lifetime and refresh policy?
- [ ] Account recovery flow?
- [ ] Roles/permissions model (RBAC granularity)?
- [ ] B2B needs (orgs, invites, SSO later)?

Unanswered items → escalate at L2 before writing code.

## Default stack
**Supabase Auth** (default — one less vendor, RLS-native) with email+password and OAuth providers as decided above. Sessions via Supabase SSR helpers; middleware-protected routes.

## Implementation steps
1. Enable providers in Supabase dashboard; record config in `docs/engineering/AUTH.md`.
2. Env vars added to `ENVIRONMENT.md` (never values, only purpose).
3. Server-side client + middleware session refresh (SSR helpers).
4. Route protection: everything private by default; public routes are an explicit allow-list (`constraints/security.md`).
5. RBAC: `roles` in DB, enforced by **RLS policies** — never client-side only.
6. UI: login/register/recover screens from `SCREENS.md`, all states, localized strings.
7. Zod-validate every auth-related input at the boundary.
8. Recovery flow tested end-to-end, including expired-token path.
9. Analytics: `auth_signup`, `auth_login`, `auth_recovery_start/complete` per `OBSERVABILITY.md`.

## Security notes
- Session lifetime + JWT policy is owned by `SECURITY.md` — link, don't restate.
- Auth posture changes are always **L0**.
- Never log tokens, emails in plaintext beyond need, or recovery links.

## Definition of Done additions
- [ ] RLS verified with tests (authorized AND unauthorized paths)
- [ ] Recovery + logout + session-expiry paths tested
- [ ] AUTH.md updated in the same PR
