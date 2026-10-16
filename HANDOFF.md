---
title: Polaris handoff
owner: Maintainer
status: Active
last_updated: 2026-10-16
---

# Current handoff

The 2026-10-16 owner request establishes Polaris as the usual coordinator and keeps each discipline independently usable. Composition changes are prepared for coordinated review on refactor/constellation-composition. The shared contract and audit record live in Polaris; local discipline manifests describe reusable ownership and evidence outputs. Product-specific artifacts remain in their product repository.

Run the documented local checks. Review the coordinated changes before merge; no release, deployment, provider configuration or automatic merge is included. Source revisions and local modifications are recorded by the planner; its output is a plan, not completed specialist work.

## Previous record (historical)

---
title: Polaris extraction handoff
owner: Maintainer
status: Active
last_updated: 2026-10-15
---

# Current handoff

2026-10-15: the owner explicitly authorised moving capability files to their corresponding repositories and committing. Original file provenance is recorded in migration/provenance.json. The reviewed operating directions are applied. ADR-005 subsequently authorises editorial product naming and current paths; philosophical commitments and historical decision states remain unchanged. Original historical wording/paths remain recoverable from Git.

## Remaining review gates

Axis #1, Meridian #32 and Sentinel #1 are merged. Polaris #8 remains draft; naming follow-ups are separate reviewed changes. The current canon directory is `polaris/`. Native Figma label edits are separately authorised and evidenced; they do not publish a library or create a named version.
Review destination branches before Polaris removal; inspect licence/distribution separately before any release. No automatic merge, deployment or auth posture changes are authorised.

## Preserved previous handoff

---
title: Handoff
owner: All
status: Active
last_updated: 2026-07-22
---

# HANDOFF — Session Continuity

> Every session ends by overwriting the **Current handoff** section. Another AI — or a human — can continue immediately. Previous handoffs are appended to the log below (newest first, keep last 10).

## Current handoff

**Session:** 2026-07-22 · Polaris canon import (Notion → repo)
**Role:** Software Architect + Technical Writer

### Completed
- Imported the full Polaris text from the Notion export ("Polaris", 11 sections + Constitution) into `polaris/`: `constitution/` (README, preamble, foundations, principles, engineering-laws, derived-frameworks, reference-implementations) + 11 section files, all with Axis front matter.
- AI consumption layer: root `CLAUDE.md` / `AGENTS.md` (session entry points) and `llms.txt` (retrieval index).
- ADR-001 (Proposed, L2): repo `polaris/` is the canon; wiki and future website are derived surfaces; Notion demoted to drafting space.
- README reframed: repo = Polaris (constitution) + Axis (derived framework), two-layer table + AI/human entry pointers.
- Wiki: new `.wiki/Polaris-Constitution.md` page; sidebar + Home navigation updated.
- STATUS: added milestone M0.7 (Polaris canon imported, in review).

### Files modified
- New: `polaris/**` (19 files), `CLAUDE.md`, `AGENTS.md`, `llms.txt`, `decisions/adr/001-polaris-canon-three-surfaces.md`, `.wiki/Polaris-Constitution.md`. Edited: `README.md`, `.wiki/_Sidebar.md`, `.wiki/Home.md`, `STATUS.md`, `HANDOFF.md`.

### Pending
- Website surface: enable GitHub Pages in repo settings, then add a static-site workflow that renders `polaris/` (toolchain deliberately not chosen yet — see ADR-001).
- Constitution gaps: Governance / Evolution / Compliance procedures exist only as an empty Notion stub — draft and ratify them.
- Notion "Untitled" constitution page was empty and was not imported.
- Earlier pending items (repo settings, labels, branch protection, project boards) still open from 2026-07-08 handoff.

### Known issues
- All `status: Draft` documents are stubs awaiting content.
- Wiki links in `.wiki/Home.md` (repo-file links) still point at `pedrobritx/axis`; repo is `pedrobritx/polaris` — sweep and fix.

### Recommended next step
Review + merge the Polaris import PR, ratify ADR-001, then decide the website toolchain (recommendation: GitHub Pages from `polaris/` markdown) and wire the Pages workflow.

---

## Handoff log

### 2026-07-08 · Publication (DevOps Engineer)
Completed: Axis v0.1.0 scaffold (119 files) adopted; validator green; SECURITY.md rewritten; README "Beyond the repo"; CI `docs-validate.yml`; wiki authored in-repo under `.wiki/` (16 pages) synced by `wiki-sync.yml`. Pending: repo settings (template flag, topics), 27-label taxonomy, branch protection, five master Projects.

### 2026-07-01 · Framework bootstrap (Software Architect)
Completed: Axis skeleton generated — full directory tree, all core documents, agents, playbooks, recipes, decision engine, constraints, memory, templates, prompts, automation. Pending: fill VISION/PRODUCT, delegation defaults, seed decision-engine policies. Recommended: dry-run the New Feature playbook.
