---
title: BSDL Canon
owner: CEO
status: Active
last_updated: 2026-07-22
---

# BSDL — Britx Software Design Language

> The canonical text of BSDL. Everything in this directory is the single source of truth for the design language; the wiki and the website are derived views and must never contradict it.

BSDL is a **design–development–software-lifecycle language**: a constitution plus a body of standards, patterns, and practices that tell any collaborator — human or AI — how Pedro (britx) builds software. It exists so that AI copilots can build software that carries his essence without re-deriving it every session.

## Reading order

| # | Section | File(s) | What it settles |
|---|---|---|---|
| 1 | **Constitution** | [`constitution/`](constitution/README.md) | Worldview, values, principles, engineering laws — the non-negotiables everything else derives from |
| 2 | Knowledge Base | [`knowledge-base.md`](knowledge-base.md) | How knowledge is captured: atomic, connected, one concept = one definition |
| 3a | Architecture, Design & Modeling | [`architecture-design-modeling.md`](architecture-design-modeling.md) | How systems are structured and modeled |
| 3b | Artificial Intelligence | [`artificial-intelligence.md`](artificial-intelligence.md) | Human–AI collaboration, prompt/context engineering, AI governance |
| 4 | Standards | [`standards.md`](standards.md) | Conventions that make work consistent |
| 5 | Development | [`development.md`](development.md) | Engineering practice: quality, testing, documentation, automation |
| 6 | Operations | [`operations.md`](operations.md) | Running, observing, and maintaining systems |
| 7 | Patterns | [`patterns.md`](patterns.md) | Named solutions and anti-patterns, with a pattern template |
| 8 | Resources | [`resources.md`](resources.md) | Curated external references |
| 9 | Glossary | [`glossary.md`](glossary.md) | Shared vocabulary |
| 10 | Community | [`community.md`](community.md) | How others participate |
| 11 | About | [`about.md`](about.md) | Provenance and intent |

## How AI should use this directory

1. Onboard through the repository's `START_HERE.md` first (BSF operating rules).
2. Read `constitution/` in full before making or proposing any significant decision.
3. Cite the specific principle or law that justifies a recommendation ("per the Law of Reversibility…"). If no principle applies, say so — per the working rule, the practice may not belong in BSDL.
4. Never edit files here on your own initiative: the canon changes only through a human-approved ADR (Level 0).

## Provenance

Imported 2026-07-22 from the Notion workspace "Britx Software Design Language" (authored by Pedro with AI assistance). Notion remains a drafting space; **this directory is the ratified text**. See ADR-001.
