*The two-part decision system: reusable policies and permanent records.* — [[Home]]

## Policy vs record

- **Decision Engine** (`decisions/decision-engine/`) — pre-answered recurring questions: **what** to choose by default, when to deviate, what to avoid. Instead of asking "which auth provider?" on every project, the answer already exists — with exceptions and rationale.
- **ADRs** (`decisions/adr/`) — permanent per-project records: **why** something was decided here, including the options that lost. Numbered `NNN-slug.md`, superseded but never deleted.

The Engine saves the question from being asked twice; the ADR saves the answer from being forgotten.

## The lifecycle

```
Question arises → policy exists? ──yes→ apply at its level, log
        │no
        ▼
Propose (AI Governance format) → human decides → ADR filed
        │
        ▼
Recurring? → promote into decision-engine/   (Continuous Learning)
```

## Per-policy delegation, by example

Each policy declares its own delegation level. The authentication policy is **L3 with triggers**: the default is Supabase Auth (already in stack, RLS-native, free tier). If no trigger is present, the AI applies the default automatically at ≥95% confidence and logs it — no meeting, no interruption. But two triggers demote the decision to **L1** (present options): day-one B2B org management, or enterprise SSO on the near-term roadmap — because then Clerk becomes a serious contender and the trade-off is genuinely the human's to make. The policy also has an avoid-list with reasons (Firebase Auth: parallel ecosystem, weak Postgres/RLS story; hand-rolled auth: never — security constraint).

This is the pattern for all eleven shipped policies: analytics, authentication, background jobs, database, deployment, file storage, monitoring, payments, state management, testing, and UI framework.

---

**→ In the repository**
- [decisions/README.md](https://github.com/pedrobritx/bsf/blob/main/decisions/README.md) — the two systems and lifecycle
- [decisions/decision-engine/authentication.md](https://github.com/pedrobritx/bsf/blob/main/decisions/decision-engine/authentication.md) — the worked example
- [decisions/adr/000-adopt-bsf.md](https://github.com/pedrobritx/bsf/blob/main/decisions/adr/000-adopt-bsf.md) — the first ADR: adopting BSF itself
- [templates/adr.md](https://github.com/pedrobritx/bsf/blob/main/templates/adr.md) — the ADR template

See also: [[Governance and Delegation]] · [[Memory and Knowledge]]
