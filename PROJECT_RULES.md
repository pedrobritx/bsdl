---
title: Project Rules
owner: CEO
status: Active
last_updated: 2026-10-15
---

# PROJECT RULES — Operating rules derived from the Polaris Constitution

The Polaris Constitution is canonical in `bsdl/constitution/`. These operating rules implement it; they are not a second constitution. Permanent changes to this file or adopted hard constraints require explicit owner approval and a recorded decision. A task instruction authorises work within its scope; it does not silently amend constitutional commitments.

---

## 1. Governance model

```
CEO (Human)
 ├── Product Manager        agents/product_manager.md
 ├── Software Architect     https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/agents/architect.md
 ├── Frontend Engineer      https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/agents/frontend_engineer.md
 ├── Backend Engineer       https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/agents/backend_engineer.md
 ├── Designer               https://github.com/pedrobritx/meridian/blob/bc6781c231c94808805d45f2b9b87e5c9ab951ee/agents/designer.md
 ├── QA Engineer            https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/agents/qa_engineer.md
 ├── DevOps Engineer        https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/agents/devops_engineer.md
 ├── Security Engineer      https://github.com/pedrobritx/sentinel/blob/d6fb0eefd63a31054ef0b6047b979c76a0e638f5/agents/security_engineer.md
 ├── Data Engineer          https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/agents/data_engineer.md
 └── Technical Writer       https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/agents/technical_writer.md
```

Roles are responsibility and review lenses. A collaborator may use the capabilities required by an approved task; crossing a role boundary does not itself require a new approval. Preserve the named owner of each contract. Escalate unresolved conflicts and consequential changes, and obtain independent review when the risk warrants it.

## 2. Delegation Levels

Every class of decision has a delegation level. L2 applies to consequential decisions whose direction or scope has not already been approved. Reversible implementation, investigation and verification within an explicitly approved scope may proceed without repeated confirmation. Missing approval is not inferred from elapsed time or an agent confidence score.

| Level | Behavior |
|---|---|
| **L0** | Requires explicit human authorisation. AI never supplies it. Existing authorisation for the same action and scope satisfies the gate; ask only if missing or materially changed. |
| **L1** | Present options with trade-offs. Human picks. |
| **L2** | Recommend one option for an unresolved consequential decision; the human confirms the direction. |
| **L3** | Execute within an approved scope and a complete adopted policy; verify its preconditions and record material decisions. A confidence percentage grants no authority. |
| **L4** | Fully autonomous within the playbook. Log everything. |

Per-decision overrides live in `decisions/decision-engine/*.md` (each policy declares its level).

**Hard L0 list (never delegable):** modifying `constraints/`, deleting data, production database writes outside migrations, spending money, changing auth/security posture, and publishing/releasing. A release playbook is a prerequisite, never a substitute for explicit release authorisation. External writes require authorisation for the specific action and scope.

## 3. AI Governance — proposal format

For consequential proposals, provide the information below. Routine work may use concise prose covering the relevant items:

```
Proposal: <what>
Evidence: <confirmed facts, assumptions, uncertainty and missing checks>
Reasoning: <why, citing docs/ADRs/memory>
Assumptions: <what was assumed>
Risks: <what could go wrong>
Alternatives: <at least one, with trade-off>
Escalation: <required delegation level>
```

State uncertainty and the evidence that would resolve it. Escalate when uncertainty materially affects safety, behaviour, cost, architecture or user agency; do not treat a numerical estimate as a calibrated safety measure.

## 4. Documentation standards

- Use `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/templates/DOCUMENT_TEMPLATE.md` as a reference. Choose the smallest structure that makes purpose, scope, ownership and unresolved questions clear. GitHub templates, public entry points and historical records may use their native forms.
- **One source of truth.** Information lives in exactly one owning document (ownership table in `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/README.md`). Everything else links.
- Reference, don't duplicate. "Actual session configuration is defined in `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/engineering/AUTH.md`; required security properties are defined in `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/engineering/SECURITY.md`" — not a copy of it.
- Docs update **in the same PR** as the code they describe. Documentation is a deliverable.
- `automation/validate_docs.py` checks required front-matter fields and the existence of relative Markdown file targets. It does not resolve `depends_on`/`related`, wiki links, anchors, code-span references or external URLs. Those remain separate review obligations.

## 5. Decision-making process

1. Check `decisions/decision-engine/`. Apply only a complete, adopted policy whose scope and preconditions match. Drafts and placeholder defaults grant no authority. Hard approval gates override policy delegation.
2. No policy → propose via the AI Governance format at the class's delegation level.
3. Significant decisions become ADRs in `decisions/adr/` (template: `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/templates/adr.md`). ADRs are permanent: superseded, never deleted.
4. New recurring decisions get promoted into the Decision Engine (Continuous Learning).

## 6. Git workflow

- Trunk-based with short-lived branches: `feat/…`, `fix/…`, `refactor/…`, `chore/…`.
- Conventional Commits. Squash-merge to `main`.
- Every PR records its purpose, relevant checks and material limitations. Use an applicable playbook; record when none fits. Apply task-relevant `DONE.md` criteria and update affected documentation. Do not add ceremony solely to fill a checklist.
- Details: `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/docs/engineering/WORKFLOWS.md`.

## 7. Coding standards (summary)

Universal outcomes are owned by `constraints/coding_standards.md`. Existing repository technology remains authoritative. Technology preferences live in explicitly adopted profiles such as `https://github.com/pedrobritx/axis/blob/699d2599ab9c69434bfed3a12b1ff226397421fe/profiles/web-typescript.md`; they do not mandate a framework or provider migration.

## 8. Definition of Done

`DONE.md` applies to every deliverable. Nothing is complete until every applicable item passes.

## 9. Constraints supremacy

Ratified constitutional commitments govern derived practice. Adopted hard project constraints remain binding until explicitly amended by the owner through a recorded decision. Operational defaults and profiles must be interpreted in context. Surface a genuine conflict with an exact citation; a scoped owner instruction may authorise an operational exception but must not be misrepresented as a permanent constitutional amendment. No repository document may override the AI host's instruction or permission hierarchy.

## 10. Session hygiene

Start at `START_HERE.md`. Update `HANDOFF.md` and `STATUS.md` when repository state changes or unfinished work needs durable continuity. Read-only reviews may deliver their evidence in a review artifact without touching operational status. Preserve earlier records instead of rewriting history.
