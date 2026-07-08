# Britx Software Framework (BSF)

**An AI-native operating system for designing, building, shipping, and maintaining software products.**

> The repository is the company. Humans and AI are just different kinds of employees.

BSF is **model-agnostic**. It works with Claude Code, Codex, Gemini CLI, Cursor, Amp, or any future AI development tool. The framework — not the model — holds the company's memory, standards, and decision process.

---

## What this is

Not a template. Not a prompt collection. An **operating system** for software projects:

- Every project starts from established standards.
- Every decision is traceable (ADRs).
- Every AI knows its role (agents) and its autonomy (delegation levels).
- Every contributor — human or artificial — works from the same source of truth.
- Context survives conversations, sessions, and model changes.

## Core Principles

1. **AI-First** — every project is understandable by humans and AI.
2. **Single Source of Truth** — information exists in one authoritative location.
3. **Context Before Code** — AI must understand the project before writing code.
4. **Documentation Is Code** — documentation evolves with the codebase.
5. **Decisions Are Permanent** — architectural decisions are recorded and traceable.
6. **Everything Has an Owner** — every document, decision, and component has clear responsibility.
7. **Automation Over Repetition** — repeatable work becomes playbooks, recipes, or templates.
8. **Human Oversight by Default** — AI proposes, humans approve, unless delegation allows otherwise.
9. **Continuous Learning** — every project contributes patterns, lessons, and reusable knowledge.
10. **Framework Over Tooling** — replace AI tools without replacing the process.

## Repository map

| Path | What it is |
|---|---|
| `START_HERE.md` | Universal entry point. Every AI session begins here. |
| `PROJECT_RULES.md` | The constitution. Immutable principles and governance. |
| `STATUS.md` | Live project dashboard. |
| `HANDOFF.md` | Session-to-session continuity. |
| `DONE.md` | Definition of Done for every deliverable. |
| `docs/` | Human-readable reference (product, design, engineering, business, oss). |
| `agents/` | AI role definitions — the org chart. |
| `playbooks/` | Repeatable workflows (feature, bug fix, release…). |
| `recipes/` | Standard implementation patterns (auth, payments…). |
| `templates/` | Reusable specification formats. |
| `prompts/` | Reusable prompt library. |
| `decisions/` | ADRs + the Decision Engine (pre-made policy answers). |
| `constraints/` | Non-negotiable rules. AI never violates these. |
| `memory/` | Long-term preferences, lessons, mistakes, patterns. |
| `knowledge/` | The graph — how everything connects. |
| `automation/` | Scripts that keep the framework honest. |

## Beyond the repo

The repository is the single source of truth; these surfaces orient and operate around it:

| Surface | Purpose |
|---|---|
| [Wiki](https://github.com/pedrobritx/bsf/wiki) | **Start here if you're human** — narrative onboarding; every page links back to the authoritative repo files. |
| [Projects](https://github.com/pedrobritx?tab=projects) | Five master boards — Kanban (daily driver), Roadmap (Now/Next/Later), Product Launch (phase gates), Feature Release (mirrors `playbooks/new_feature.md`), Bug Triage (severity pipeline). |
| [Discussions](https://github.com/pedrobritx/bsf/discussions) | Questions, ideas, and RFCs before they become issues or ADRs. |
| [Releases](https://github.com/pedrobritx/bsf/releases) | Versioned snapshots of the framework. |

**Adopt BSF:** click **Use this template** on this repo, or:

```bash
gh repo create myapp --template pedrobritx/bsf --private --clone
```

**Instantiate the boards** (personal accounts copy the masters — Projects can't be templated outside orgs):

```bash
gh project copy <number> --source-owner pedrobritx --target-owner pedrobritx --title "MyApp · Kanban"
```

## Quick start (new project)

1. Copy this skeleton (or `git clone` and re-init).
2. Fill `docs/product/VISION.md` and `docs/product/PRODUCT.md`.
3. Set delegation defaults in `PROJECT_RULES.md`.
4. Point your AI tool at `START_HERE.md`.
5. Build.

## Framework layers

```
Vision → Strategy → Planning → Design → Engineering
      → Quality → Deployment → Operations → Learning
```

Each layer owns specific documents, workflows, and AI responsibilities. See `docs/README.md`.

---
*BSF v0.1.0 · Maintained by Pedro Henrique Bahia Brito (britx)*
