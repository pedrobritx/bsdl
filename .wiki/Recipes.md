*Standard implementations: how this company builds common features.* — [[Home]]

## The philosophy

A recipe is the company-standard way to implement a recurring feature — authentication, payments, file uploads. Follow it; **deviate only via ADR**. This isn't rigidity for its own sake: the recipe encodes decisions already made (and paid for), so every project doesn't re-litigate them. The *why* behind each recipe's defaults lives in the matching [[Decision Engine and ADRs]] policy.

## The Question Engine

Every recipe opens with a **"Before implementing"** checklist — the questions that must be answered before code is written. This is the Question Engine pattern: surface the unknowns up front, at the right delegation level, instead of discovering them as rework.

The authentication recipe is the worked example. Before implementing auth, seven boxes: social login and which providers? MFA required, optional, none? Passwordless? Session lifetime and refresh policy? Account recovery flow? Roles/permissions granularity? B2B needs (orgs, invites, SSO later)? *Unanswered items escalate at L2 before any code.* Then the recipe prescribes the default stack (Supabase Auth, RLS-native), nine implementation steps from provider config through analytics events, security notes (auth posture changes are always L0), and recipe-specific additions to the Definition of Done — RLS verified with tests on both the authorized and unauthorized paths.

## The recipe shelf

| Recipe | File |
|---|---|
| Authentication | [authentication.md](https://github.com/pedrobritx/bsf/blob/main/recipes/authentication.md) |
| AI Chat | [ai_chat.md](https://github.com/pedrobritx/bsf/blob/main/recipes/ai_chat.md) |
| Background Jobs | [background_jobs.md](https://github.com/pedrobritx/bsf/blob/main/recipes/background_jobs.md) |
| CRUD | [crud.md](https://github.com/pedrobritx/bsf/blob/main/recipes/crud.md) |
| File Uploads | [file_uploads.md](https://github.com/pedrobritx/bsf/blob/main/recipes/file_uploads.md) |
| Notifications | [notifications.md](https://github.com/pedrobritx/bsf/blob/main/recipes/notifications.md) |
| Payments | [payments.md](https://github.com/pedrobritx/bsf/blob/main/recipes/payments.md) |
| Search | [search.md](https://github.com/pedrobritx/bsf/blob/main/recipes/search.md) |

New patterns earn their way onto this shelf: a technique proven in real work goes to `memory/patterns.md` first, and gets promoted to a recipe when it becomes a standard ([[Memory and Knowledge]]).

---

**→ In the repository**
- [recipes/](https://github.com/pedrobritx/bsf/tree/main/recipes) — all recipes

See also: [[Decision Engine and ADRs]]
