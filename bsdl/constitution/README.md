---
title: BSDL Constitution
owner: CEO
status: Active
last_updated: 2026-07-22
---

# 1. BSDL Constitution

Software is the intentional organisation of human knowledge into executable systems that transform reality in service of humanity.

**BSDL** is a constitution for software development, not a mere methodology. It defines the worldview, values, ethical limits, and engineering laws from which lifecycles, architectures, workflows, documentation standards, and AI collaboration patterns are derived.

## How to read this constitution

- [Preamble](preamble.md) explains why BSDL exists.
- [Foundations](foundations.md) define what software is, what counts as truth, and what values matter.
- [Constitutional Principles](principles.md) state the non-negotiables.
- [Engineering Laws](engineering-laws.md) translate principles into operational constraints.
- [Derived Frameworks](derived-frameworks.md) show how to build lifecycles, architectures, and decisions from those laws.
- [Reference Implementations](reference-implementations.md) provide templates, heuristics, and examples.

## Constitution Map

```markdown
Worldview
  └─ Ontology
      └─ Axiology
          └─ Ethics
              └─ Epistemology
                  └─ Systems Theory
                      └─ Engineering Theory
                          └─ Practices
```

## Working rule

Any downstream practice must trace back to at least one constitutional principle. If it cannot, it does not belong in BSDL.

## Relationship to BSF

The **Britx Software Framework** (the operational skeleton at this repository's root — `START_HERE.md`, `agents/`, `playbooks/`, `decisions/`, `constraints/`, `memory/`) is the first **derived framework** of this constitution: BSDL states *why and what must hold*; BSF encodes *how a project operates day to day*. When BSF and the constitution conflict, the constitution wins and the conflict is resolved through an ADR.

## Open sections

Governance, Evolution, Compliance amendment procedures are drafted in Notion but not yet ratified here. Until then, changes to any file in `bsdl/` are Level 0 decisions (human only, ADR required) per `PROJECT_RULES.md`.
