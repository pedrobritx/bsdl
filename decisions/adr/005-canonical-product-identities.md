---
title: ADR-005 canonical product identities
owner: Maintainer
status: Accepted
last_updated: 2026-10-15
---

# Canonical product identities

The owner explicitly requested complete current-tree naming cleanup for Polaris and Axis, including paths, links, hooks and mentions, then extended it to native Figma labels and the ai/Ambientis consumers. This supersedes the earlier instruction to preserve legacy spellings and paths in current files.

Polaris owns the Constitution and governance; Axis owns engineering capability. Rename the canon directory to `polaris/`, the wiki Constitution page and the two historical ADR filenames. Update entry points, documentation and ownership-aware links together. Editorial changes to the Constitution replace product identity only; they do not amend its philosophical commitments. The protective-intervention amendment remains Proposed.

Historical records in the current tree use current terminology for retrieval. Their original wording remains recoverable from immutable parent commits. ADR numbers, decisions, dates and ratification state remain unchanged. Old extraction hashes describe the recorded extraction snapshot, not every later editorial revision. The normalization ledger records each source path as UTF-8 hex, original bytes' SHA-256 and resulting path/hash without keeping obsolete names as active aliases.

Cross-repository canon links pin the naming commit before source cutover. Publish the wiki through the existing reviewed workflow after merge. Do not recreate previous repository addresses, rewrite Git history, force-push, merge automatically, advance Figma named-version/token baselines, or publish a Figma library in this cleanup.

Verify current tracked paths/text, local and cross-repository link targets, wiki navigation, source hash preservation and existing repository checks. Naming-only consumer PRs preserve their existing product and architecture semantics.
