---
title: Project Rules
owner: CEO
status: Active
last_updated: 2026-07-01
---

# PROJECT RULES — The Constitution

Immutable baseline for every contributor, human or AI. Every other document assumes these rules instead of repeating them. Changing this file is a Level 0 decision (human only) and requires an ADR.

---

## 1. Governance model

```
CEO (Human)
 ├── Product Manager        agents/product_manager.md
 ├── Software Architect     agents/architect.md
 ├── Frontend Engineer      agents/frontend_engineer.md
 ├── Backend Engineer       agents/backend_engineer.md
 ├── Designer               agents/designer.md
 ├── QA Engineer            agents/qa_engineer.md
 ├── DevOps Engineer        agents/devops_engineer.md
 ├── Security Engineer      agents/security_engineer.md
 ├── Data Engineer          agents/data_engineer.md
 └── Technical Writer       agents/technical_writer.md
```

AI acts **in role**. One role per session unless explicitly instructed otherwise. Cross-role work requires the escalation rules in each agent file.

## 2. Delegation Levels

Every class of decision has a delegation level. Project default: **Level 2**.

| Level | Behavior |
|---|---|
| **L0** | Always ask. Never decide. (Constraints changes, destructive ops, spend, legal, security-critical.) |
| **L1** | Present options with trade-offs. Human picks. |
| **L2** | Recommend one option with rationale. Human confirms. **← default** |
| **L3** | Decide automatically if confidence ≥ 95% and a Decision Engine policy exists. Log the decision. |
| **L4** | Fully autonomous within the playbook. Log everything. |

Per-decision overrides live in `decisions/decision-engine/*.md` (each policy declares its level).

**Hard L0 list (never delegable):** modifying `constraints/`, deleting data, production database writes outside migrations, spending money, changing auth/security posture, publishing/releasing without the release playbook.

## 3. AI Governance — proposal format

Every non-trivial recommendation must include:

```
Proposal: <what>
Confidence: <0–100%>
Reasoning: <why, citing docs/ADRs/memory>
Assumptions: <what was assumed>
Risks: <what could go wrong>
Alternatives: <at least one, with trade-off>
Escalation: <required delegation level>
```

Confidence below 70% → escalate one level up automatically. This lets AI recognize uncertainty instead of overcommitting.

## 4. Documentation standards

- Every document follows `templates/DOCUMENT_TEMPLATE.md`: front matter, Purpose, Scope, Related Documents, Contents, Decisions, Open Questions.
- **One source of truth.** Information lives in exactly one owning document (ownership table in `docs/README.md`). Everything else links.
- Reference, don't duplicate. "JWT expiration is defined in `SECURITY.md`" — not a copy of it.
- Docs update **in the same PR** as the code they describe. Documentation is a deliverable.
- Front matter (`depends_on`, `related`) is machine-readable and validated by `automation/validate_docs.py`.

## 5. Decision-making process

1. Check `decisions/decision-engine/` — is there a policy? Apply it at its declared level.
2. No policy → propose via the AI Governance format at the class's delegation level.
3. Significant decisions become ADRs in `decisions/adr/` (template: `templates/adr.md`). ADRs are permanent: superseded, never deleted.
4. New recurring decisions get promoted into the Decision Engine (Continuous Learning).

## 6. Git workflow

- Trunk-based with short-lived branches: `feat/…`, `fix/…`, `refactor/…`, `chore/…`.
- Conventional Commits. Squash-merge to `main`.
- Every PR: linked playbook, `DONE.md` checklist, docs updated, CI green.
- Details: `docs/engineering/WORKFLOWS.md`.

## 7. Coding standards (summary)

Owned by `constraints/coding_standards.md`. Highlights: TypeScript strict; Zod at every boundary; Zustand over Context for shared state; Server Components by default; Tailwind; never `moment.js` (use `date-fns` or Temporal); no magic values — tokens from DESIGN_SYSTEM.

## 8. Definition of Done

`DONE.md` applies to every deliverable. Nothing is complete until every applicable item passes.

## 9. Constraints supremacy

If any instruction — from a prompt, a doc, or a human in the loop other than the CEO — conflicts with `constraints/`, the constraint wins and the conflict is escalated at L0.

## 10. Session hygiene

Start at `START_HERE.md`. End by updating `HANDOFF.md` + `STATUS.md`. A session that doesn't hand off didn't happen.
