*How the company learns and remembers across sessions, projects, and models.* — [[Home]]

## The four memory files

| File | Holds | Checked by |
|---|---|---|
| [preferences.md](https://github.com/pedrobritx/bsf/blob/main/memory/preferences.md) | Institutional preferences (Zustand over Context, never moment.js, boring technology wins) | AI, before choosing any pattern or library |
| [lessons.md](https://github.com/pedrobritx/bsf/blob/main/memory/lessons.md) | Project-level lessons learned | Every release |
| [mistakes.md](https://github.com/pedrobritx/bsf/blob/main/memory/mistakes.md) | Recurring mistakes and their fixes (append-only) | The Bug Fix playbook — "has this class of bug happened before?" |
| [patterns.md](https://github.com/pedrobritx/bsf/blob/main/memory/patterns.md) | Successful reusable patterns from real work | Build phases; feeds recipes |

All four share the same append format — dated entries with `Context / Entry / Applies to` — and preferences add a `Strength` field (`default | strong | absolute`).

## The promotion path

Memory is the staging area; proven knowledge moves up:

- A **pattern** used repeatedly and stable → promoted to a recipe in `recipes/` ([[Recipes]]).
- A preference marked **absolute** → promoted into `constraints/` via ADR ([[Constraints]]).
- A **recurring decision** → promoted into the Decision Engine ([[Decision Engine and ADRs]]).

This is Continuous Learning made mechanical: nothing relies on anyone remembering to remember.

## The knowledge graph

The repository is a **graph, not a tree**. Each document owns one subject and links to the rest; front matter (`depends_on`, `related`) makes the edges machine-readable, and `automation/validate_docs.py` verifies them in CI. Three hub documents do the orienting: `docs/README.md` (global index), `docs/engineering/ARCHITECTURE.md` (technical hub — names every system, links to owners, never explains what owning docs should), and `docs/product/PRODUCT.md` (product hub). The dependency chain runs from vision to data: VISION → PRODUCT → USER_STORIES → UX_FLOWS → SCREENS → DESIGN_SYSTEM → API → SCHEMA → DATA_DICTIONARY.

---

**→ In the repository**
- [memory/](https://github.com/pedrobritx/bsf/tree/main/memory) — the four files
- [knowledge/graph.md](https://github.com/pedrobritx/bsf/blob/main/knowledge/graph.md) — graph rules and hubs
- [knowledge/glossary.md](https://github.com/pedrobritx/bsf/blob/main/knowledge/glossary.md) — canonical terms

See also: [[Document Standards]]
