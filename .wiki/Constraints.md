*The non-negotiables: rules AI never violates, at any delegation level.* — [[Home]]

## Constraint ≠ preference

A **preference** (`memory/preferences.md`) is a default the AI should follow but can argue with. A **constraint** is **immutable during execution**: no confidence level, no delegation level, and no instruction from anyone but the CEO can override it. Changing a constraint is a Level 0 decision requiring an ADR and human approval. The distinction is what makes L3/L4 autonomy safe — you can hand the AI the keys precisely because some doors don't open.

## The seven constraint files

| File | Most representative rule |
|---|---|
| [security.md](https://github.com/pedrobritx/bsf/blob/main/constraints/security.md) | No secrets in code, logs, or prompts — ever. |
| [coding_standards.md](https://github.com/pedrobritx/bsf/blob/main/constraints/coding_standards.md) | TypeScript strict everywhere; Zod validates every external boundary. |
| [cost.md](https://github.com/pedrobritx/bsf/blob/main/constraints/cost.md) | Any new recurring cost is L0 — no exceptions, no trials that auto-convert. |
| [performance.md](https://github.com/pedrobritx/bsf/blob/main/constraints/performance.md) | LCP < 2.5s, INP < 200ms, CLS < 0.1 in production. |
| [accessibility.md](https://github.com/pedrobritx/bsf/blob/main/constraints/accessibility.md) | WCAG 2.2 AA minimum; never rely on color alone to convey state. |
| [privacy.md](https://github.com/pedrobritx/bsf/blob/main/constraints/privacy.md) | PII flagged in the data dictionary and encrypted at rest; GDPR + LGPD by default. |
| [legal.md](https://github.com/pedrobritx/bsf/blob/main/constraints/legal.md) | Every dependency must have a compatible license. |

## Constraints supremacy

`PROJECT_RULES.md` §9: if **any** instruction — from a prompt, a document, or a human in the loop other than the CEO — conflicts with `constraints/`, **the constraint wins** and the conflict escalates at L0. This makes constraints robust against prompt injection, well-meaning shortcuts, and drift: the framework's answer to "just this once" is a structural *no*.

---

**→ In the repository**
- [constraints/](https://github.com/pedrobritx/bsf/tree/main/constraints) — all seven files
- [PROJECT_RULES.md](https://github.com/pedrobritx/bsf/blob/main/PROJECT_RULES.md) — §9, constraints supremacy

See also: [[Governance and Delegation]]
