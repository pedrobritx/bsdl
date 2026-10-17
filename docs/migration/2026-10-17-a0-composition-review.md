---
title: A0 coordinated composition review
owner: Polaris maintainer
status: In review
last_updated: 2026-10-17
---

# A0 — Composition PR review and safe merge preparation

**Tracking:** [A0-001](https://github.com/pedrobritx/polaris/issues/10) · [A0 goal](https://github.com/pedrobritx/constellation/issues/2)  
**Authority:** review-only; no merge, deployment, Figma publication, spending or constitutional amendment is authorized by this document.

## Inspected review heads and reported CI (17 October 2026)

| Repository | PR | Revision | Relevant GitHub Actions |
| --- | --- | --- | --- |
| Polaris | [#9](https://github.com/pedrobritx/polaris/pull/9) | `ca31751fa91508428fc72b9f46545056650975f8` | Validate docs: **success** ([run](https://github.com/pedrobritx/polaris/actions/runs/38867978015)) |
| Axis | [#3](https://github.com/pedrobritx/axis/pull/3) | `1414aed324bd010bbfaa56f002a57198b0674473` | Validate documentation: **success** ([run](https://github.com/pedrobritx/axis/actions/runs/38867926281)) |
| Meridian | [#37](https://github.com/pedrobritx/meridian/pull/37) | `2b9b5c42a2ad154ac929b63d1b50b7280c0c9f74` | Figma Bridge Checks and Validate and deploy Meridian: **success** ([runs](https://github.com/pedrobritx/meridian/actions/runs/38868051460)); deployment job may be skipped—this is not a release claim |
| Sentinel | [#3](https://github.com/pedrobritx/sentinel/pull/3) | `e7a17cec987eeff377fbd73c530c4156c25815b3` | Validate documentation: **success** ([run](https://github.com/pedrobritx/sentinel/actions/runs/38867930135)) |
| Constellation | [#1](https://github.com/pedrobritx/constellation/pull/1) | `a5d554f1575d57d474b312b8ce46ad25ae066052` | No workflow run returned for this head; product-definition review still necessary |
| Sentinel naming follow-up | [#2](https://github.com/pedrobritx/sentinel/pull/2) | `97d76efebd54e20d0fdc258726ea2dc79302695f` | Validate documentation: **success** ([run](https://github.com/pedrobritx/sentinel/actions/runs/38829225087)) |

These are CI observations for those commits, not independent assurance of product behavior or security. Neither automatic merging nor actual pilot execution has occurred.

## Concrete conflicts and review tasks

- **Sentinel #2 and #3 overlap** on `README.md`, `CHANGELOG.md` and `HANDOFF.md`. The README's canonical origin sentence appears in *both* proposed branches; #3 also introduces optional composition guidance. The CHANGELOG includes complementary naming and composition entries. HANDOFF records diverge (naming-only follow-up versus post-composition session). **Recommended resolution:** preserve the exact name-normalization ledger from #2, the distinct naming CHANGLELOG entry and original lineage, while keeping #3's newer composition handoff. Re-run Sentinel tests after integration, then separately close/supersede #2 only upon owner review. Do not silently discard provenance.
- **Meridian #37** also alters three Lab source files and archives old 0.1 assets beyond creating `discipline.json`; review native Figma/stable 0.5 boundaries and regenerated output drift, not just its green validation badge. No Figma publish authorized.
- **Polaris #9** touches extensive wiki/navigation, duplicated process text and a new planner. Confirm no philosophical canon or extraction ledgers changed and all project/discipline modes still validate. An ADR labeled `Accepted` in an unmerged draft branch must not be treated as merged main authority.
- **Constellation #1** has no application runtime yet; verify its `constellation.json` with actual manifests at selected revisions and ensure it doesn't duplicate Polaris authority.
- **Independence:** Axis, Meridian and Sentinel must remain usable without a Polaris checkout; no implicit runtime dependencies or provider selections.

## Proposed safe review/merge order (not executed)

1. Resolve Sentinel #2/#3 overlapping edits with a dedicated reviewable reconciliation; verify exact provenance.
2. Review/merge authorized **Axis #3, Meridian #37 and reconciled Sentinel #3**; inspect changes and rerun owning tests at the final review heads.
3. Review Polaris #9 against those immutable reviewed revisions, especially opt-outs, missing-source behavior and the governance contract; merge only upon explicit authorization.
4. Review Constellation #1 adoption against the accepted composition contract; merge only upon explicit authorization.
5. Retarget stacked implementation PRs [Polaris #19](https://github.com/pedrobritx/polaris/pull/19) and [Constellation #8](https://github.com/pedrobritx/constellation/pull/8) once their bases merge, then rerun exact-head checks.

## Follow-up evidence required

- CI on **final** reconciled heads; stale checks aren't proof for later commits.
- Standalone no-Polaris tests, explicit all-eight-opt-out combination tests, project-specific ownership and cross-repo reference verification.
- Human approval for any merges or security posture/constitutional changes; no silent release or license selection.
- A0 pilot remains unverified until real host execution with the six gates.
