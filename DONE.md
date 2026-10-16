---
title: Polaris definition of done
owner: Maintainer
status: Active
last_updated: 2026-10-16
---

# Completion evidence

Apply checks to the actual deliverable; state material limitations and reasons for inapplicable checks.

- The approved objective and acceptance criteria are met, with observable evidence.
- The [composition contract](integration/README.md) places reusable and product-specific changes in their owners. Selected disciplines return artifacts and evidence; excluded required scopes remain visible until alternative coverage is verified.
- Required guidance and consequential decisions are traceable to the reviewed revisions. Draft policies grant no authority. Canon changes retain their separate human/ADR gate.
- Run relevant checks in each changed repository and verify the integrated result. Documentation checks alone do not prove product functionality, accessibility or security. Preserve independent review requirements where applicable.
- Inspect diffs for accidental public-contract changes, secrets, copied policy, generated noise and unrelated edits. Product-facing behaviour receives appropriate functional, accessibility, privacy and security checks in its own repository.
- Update owning documentation and the local CHANGELOG. Update STATUS/HANDOFF for changed state or unfinished work; preserve historical records.
- Keep unresolved decisions, residual risk and deployment/publication/merge gates explicit. A plan, passing test or completed discipline task does not grant external authority.
