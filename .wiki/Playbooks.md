*Repeatable workflows: what triggers each, and how one feature moves through the company.* — [[Home]]

## When you say… → the AI follows…

| You say | Playbook | File |
|---|---|---|
| "Add the ability to…", "Build a feature…" | New Feature | [new_feature.md](https://github.com/pedrobritx/bsf/blob/main/playbooks/new_feature.md) |
| "X is broken", "Fix this error" | Bug Fix | [bug_fix.md](https://github.com/pedrobritx/bsf/blob/main/playbooks/bug_fix.md) |
| "Clean this up", "Restructure without changing behavior" | Refactor | [refactor.md](https://github.com/pedrobritx/bsf/blob/main/playbooks/refactor.md) |
| "Ship it", "Cut a version" | Release | [release.md](https://github.com/pedrobritx/bsf/blob/main/playbooks/release.md) |
| "It's slow", "We're over budget on LCP" | Performance Optimization | [performance_optimization.md](https://github.com/pedrobritx/bsf/blob/main/playbooks/performance_optimization.md) |
| "Audit this", "New sensitive surface" | Security Review | [security_review.md](https://github.com/pedrobritx/bsf/blob/main/playbooks/security_review.md) |
| "The schema needs to change" | Migration | [migration.md](https://github.com/pedrobritx/bsf/blob/main/playbooks/migration.md) |

## Anatomy of a playbook

Every playbook has the same skeleton: **when to use** it, **required reading** (the docs that must be loaded before acting), numbered **steps**, a **validation** gate, and a **completion checklist** that always ends the same way — CHANGELOG updated, STATUS + HANDOFF updated, DONE.md satisfied. A playbook is finished when its checklist is green, not when the code compiles.

## One feature, five phases — a short story

*Someone asks for magic-link login.* **Phase 0 (Context):** the Product Manager reads the product docs, writes a spec from the template, and runs the Question Engine pass against the authentication recipe — MFA? session lifetime? recovery flow? A spec with open questions is not ready. The human approves. **Phase 1 (Design):** the Designer specs the screens in every state; the Architect checks the Decision Engine (Supabase Auth, L3 — decided and logged, no meeting needed); the Data Engineer drafts the schema delta *with its rollback, now, not later*. **Phase 2 (Build):** Backend implements endpoints with Zod at the boundary; Frontend builds from the screen spec, tokens only — loading/empty/error states are part of the feature, not polish. **Phase 3 (Quality):** QA runs the full test checklist plus accessibility and localization, and issues a verdict against DONE.md — every item passed or explicitly N/A with justification. **Phase 4 (Ship & Learn):** merge, changelog, release if applicable — and the new reusable pattern gets written back to `recipes/` or `memory/patterns.md`. The company just got smarter.

That five-phase lifecycle is also the column layout of the **Feature Release** board: [[Project Boards]].

---

**→ In the repository**
- [playbooks/](https://github.com/pedrobritx/bsf/tree/main/playbooks) — all seven playbooks

See also: [[Recipes]] · [[Project Boards]]
