*How the company decides: the org model and the autonomy system.* — [[Home]]

## The org chart

A human CEO sits at the top; ten AI-assumable roles report to them:

```
CEO (Human)
 ├── Product Manager      ├── QA Engineer
 ├── Software Architect   ├── DevOps Engineer
 ├── Frontend Engineer    ├── Security Engineer
 ├── Backend Engineer     ├── Data Engineer
 ├── Designer             └── Technical Writer
```

AI acts **in role** — one role per session unless instructed otherwise. Each role's file defines its responsibilities, required reading, and hard boundaries: [[Agents and Roles]].

## Delegation levels L0–L4

Every *class* of decision has a level. The project default is **L2**.

| Level | Behavior | Realistic example |
|---|---|---|
| **L0** | Always ask; never decide. | "Should we soften the RLS requirement in `constraints/security.md`?" — AI refuses to even draft it without the human. |
| **L1** | Present options with trade-offs; human picks. | "Clerk-trigger present (B2B orgs are day-one): here are Supabase Auth vs Clerk, with costs and trade-offs." |
| **L2** | Recommend one option with rationale; human confirms. *(default)* | "For this form I recommend a Server Action with Zod validation — confirm?" |
| **L3** | Auto-decide at ≥95% confidence **when a Decision Engine policy exists**; log it. | Auth needed, no B2B triggers → applies Supabase Auth per the policy, logs the decision, keeps moving. |
| **L4** | Fully autonomous within a playbook; log everything. | Executing the Bug Fix playbook end-to-end on a reproduced, root-caused defect. |

Confidence below 70% escalates one level up automatically — the system is designed so AI recognizes uncertainty instead of overcommitting.

## The hard L0 list

Never delegable, at any confidence: modifying `constraints/`, deleting data, production database writes outside migrations, spending money, changing auth/security posture, publishing/releasing outside the release playbook. These are the decisions where a wrong autonomous call is irreversible, costly, or a security event — so they are constitutionally human.

## The proposal format

Every non-trivial recommendation uses the AI Governance block from `PROJECT_RULES.md` §3. A worked example:

```
Proposal: Use pgvector on Supabase for semantic search over documents
Confidence: 92%
Reasoning: decision-engine/database.md prefers existing stack; constraints/cost.md
  lists dedicated vector DBs as L0; corpus is <1M vectors, well within pgvector range
Assumptions: query latency budget of 200ms holds at current scale
Risks: index rebuild time grows with corpus; revisit if >5M vectors
Alternatives: Pinecone — better at extreme scale, but new vendor + recurring cost (L0)
Escalation: L2 — recommend and confirm
```

---

**→ In the repository**
- [PROJECT_RULES.md](https://github.com/pedrobritx/bsf/blob/main/PROJECT_RULES.md) — governance model, levels, hard L0 list, proposal format (§1–§3)
- [agents/](https://github.com/pedrobritx/bsf/tree/main/agents) — the org chart as files

See also: [[Agents and Roles]] · [[Decision Engine and ADRs]]
