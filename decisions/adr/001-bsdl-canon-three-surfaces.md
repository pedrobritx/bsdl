---
title: "ADR-001: BSDL canon lives in-repo; wiki and website are derived surfaces"
owner: Software Architect
status: Accepted
last_updated: 2026-07-22
---

# ADR-001: BSDL canon lives in-repo; wiki and website are derived surfaces

## Problem

BSDL (the Britx Software Design Language — constitution, standards, patterns) was drafted in Notion; this repository held only BSF (the operating framework). The project's purpose is to serve as guardrails and retrieval context for AI copilots building future britx projects, which requires the text to be (a) canonical in one place, (b) version-controlled and reviewable, (c) directly readable by AI tools, and (d) presentable to humans. Three surfaces were proposed: repo, website, GitHub wiki. The risk to avoid is three diverging copies of the truth.

## Options considered

1. **Repo as single canon; wiki and website generated/derived from it** — one source of truth, PR-reviewed changes, AI reads raw markdown; costs a sync step for the derived surfaces.
2. **Notion as canon, repo as export target** — comfortable editing, but exports are lossy, un-reviewable, and the repo (what AI actually reads) lags the truth.
3. **Wiki as canon** — easy editing, but wikis bypass PR review, CI validation, and are awkward for RAG ingestion.

## Decision

Option 1, at delegation level L2 — recommended by AI, ratified by the CEO via merge of PR #5 (2026-07-22).

- `bsdl/` holds the ratified BSDL text (constitution + numbered sections), imported 2026-07-22 from the Notion export. Notion remains a drafting space only.
- AI consumption layer: `CLAUDE.md` / `AGENTS.md` (session entry points) and `llms.txt` (retrieval index) at the repo root.
- **Wiki** stays authored in-repo under `.wiki/` and published by the existing `wiki-sync.yml` workflow — narrative onboarding for humans, always linking back to `bsdl/`.
- **Website** will be a static site generated from `bsdl/` markdown via GitHub Pages (workflow to be added once Pages is enabled in repo settings); it never carries content that is not in `bsdl/`.
- Changing anything in `bsdl/` is a Level 0 decision requiring an ADR, per `PROJECT_RULES.md`.

## Consequences

Positive: one reviewable truth; AI copilots in any tool can be pointed at one URL/clone; CI (`docs-validate.yml`) now guards the canon's front matter and links. Negative: editing loses Notion's comfort — changes go through git; the website and any Notion mirror require discipline (or automation) to stay derived rather than drift into forks. Governance/Evolution/Compliance sections of the constitution are not yet ratified and remain an open gap.

## Confidence

85% — the structure follows BSDL's own Law of Architectural Memory and BSF's Single Source of Truth principle; the main uncertainty is the website toolchain choice, deliberately deferred.

## Links

`bsdl/README.md` · `CLAUDE.md` · `llms.txt` · `README.md` (three-surfaces table) · `.github/workflows/wiki-sync.yml`
