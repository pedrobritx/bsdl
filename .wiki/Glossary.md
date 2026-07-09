*Every BSF term, each linking to its owner.* — [[Home]]

The canonical project glossary lives in [`knowledge/glossary.md`](https://github.com/pedrobritx/bsf/blob/main/knowledge/glossary.md); this page mirrors it and adds wiki-navigation terms.

| Term | Definition | Where it lives |
|---|---|---|
| **ADR** | Architectural Decision Record — permanent record of a significant decision; superseded, never deleted. | [decisions/adr/](https://github.com/pedrobritx/bsf/tree/main/decisions/adr) · [[Decision Engine and ADRs]] |
| **Agent** | A role an AI can assume, defined by responsibilities, required reading, and boundaries. | [agents/](https://github.com/pedrobritx/bsf/tree/main/agents) · [[Agents and Roles]] |
| **AI Governance block** | The mandatory proposal format: confidence, reasoning, assumptions, risks, alternatives, escalation. | [PROJECT_RULES.md](https://github.com/pedrobritx/bsf/blob/main/PROJECT_RULES.md) §3 · [[Governance and Delegation]] |
| **Constraint** | A non-negotiable rule, immutable during execution; changing one is L0 + ADR. | [constraints/](https://github.com/pedrobritx/bsf/tree/main/constraints) · [[Constraints]] |
| **Decision Engine** | Pre-answered recurring decisions: default, exceptions, avoid-list, own delegation level. | [decisions/decision-engine/](https://github.com/pedrobritx/bsf/tree/main/decisions/decision-engine) · [[Decision Engine and ADRs]] |
| **Delegation Level (L0–L4)** | How much autonomy AI has for a class of decision, from "always ask" to "autonomous within playbook". | [PROJECT_RULES.md](https://github.com/pedrobritx/bsf/blob/main/PROJECT_RULES.md) §2 · [[Governance and Delegation]] |
| **DoD / DONE.md** | The Definition of Done checklist applied to every deliverable; N/A must be explicit. | [DONE.md](https://github.com/pedrobritx/bsf/blob/main/DONE.md) |
| **Handoff** | The session-continuity record every session overwrites at its end. | [HANDOFF.md](https://github.com/pedrobritx/bsf/blob/main/HANDOFF.md) |
| **Hard L0 list** | Decisions never delegable to AI: constraints changes, data deletion, spend, auth posture, unplaybooked releases. | [PROJECT_RULES.md](https://github.com/pedrobritx/bsf/blob/main/PROJECT_RULES.md) §2 · [[Governance and Delegation]] |
| **Master project** | One of the five pristine BSF boards, copied per product (never worked in directly). | [[Project Boards]] |
| **Memory** | The four append-only learning files: preferences, lessons, mistakes, patterns. | [memory/](https://github.com/pedrobritx/bsf/tree/main/memory) · [[Memory and Knowledge]] |
| **Playbook** | A repeatable workflow with required reading, steps, validation, and a completion checklist. | [playbooks/](https://github.com/pedrobritx/bsf/tree/main/playbooks) · [[Playbooks]] |
| **Question Engine** | The "Before implementing" checklist pattern that surfaces unknowns before code. | [recipes/](https://github.com/pedrobritx/bsf/tree/main/recipes) · [[Recipes]] |
| **Recipe** | The company-standard implementation of a common feature; deviation requires an ADR. | [recipes/](https://github.com/pedrobritx/bsf/tree/main/recipes) · [[Recipes]] |
| **Session hygiene** | Start at START_HERE, end by updating HANDOFF + STATUS. A session that doesn't hand off didn't happen. | [PROJECT_RULES.md](https://github.com/pedrobritx/bsf/blob/main/PROJECT_RULES.md) §10 |
| **Single Source of Truth** | Information lives in exactly one owning document; everything else links. | [docs/README.md](https://github.com/pedrobritx/bsf/blob/main/docs/README.md) · [[Document Standards]] |

---

**→ In the repository**
- [knowledge/glossary.md](https://github.com/pedrobritx/bsf/blob/main/knowledge/glossary.md) — the canonical glossary
