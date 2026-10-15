---
title: "Polaris Transition: Inventory, Migration Plan and Release Gates"
owner: Software Architect
status: Proposed
last_updated: 2026-10-14
---

# Polaris transition — safe start

## Purpose
Operational roadmap for evolving `pedrobritx/bsdl` into Polaris governance, separating Axis engineering, retaining Meridian design, and creating Sentinel security. This is a proposal, not authorization to rename or extract repositories.

## Verified baseline (14 October 2026)
- `pedrobritx/bsdl` is the current live repository. `pedrobritx/bsf` resolves via GitHub redirect to **the same repository ID**, not an independent BSF repository.
- BSDL canon lives in `bsdl/`. Root-level `AGENTS.md`, `PROJECT_RULES.md`, `START_HERE.md`, `agents/`, `playbooks/`, `recipes/`, `templates/`, `automation/`, `constraints/`, `decisions/` and `docs/` are mixed-purpose.
- BSDL workflows: `.github/workflows/docs-validate.yml` (checks front matter and links), `.github/workflows/wiki-sync.yml` (syncs `.wiki/` with wiki; uses `GITHUB_REPOSITORY`).
- Several BSDL README/wiki/status references point to obsolete `pedrobritx/bsf` locations.
- Meridian workflows: `figma-sync.yml`, `figma-bridge-check.yml`, `forest-figma-handoff.yml`, `pages.yml`.
- Meridian's Figma sync has hardcoded `github.repository == 'pedrobritx/meridian'`, which is fine **so long as Meridian is not renamed**.
- Meridian package `@pedrobritx/meridian` is version 0.5.0 with `private: true`; it is not yet a independently published npm package.
- Existing Meridian 0.6 Living Matter roadmap is explicitly experimental. Do not promote it or migrate consuming apps as part of this restructure.
- Repository `pedrobritx/polaris`, `pedrobritx/axis`, `pedrobritx/sentinel` did not resolve during a connected-account inspection; this is not a trademark or namespace reservation.

## Foundational principle
Polaris is the **governance/control plane**, not a required runtime dependency for Axis, Meridian or Sentinel. Each child has its own source of truth and capabilities. Independent installation and composition are both acceptance criteria.

## Phase 0 — Review and inventory (no breaking mutations)
- [ ] Ratify ADR-002 under existing L0 constitution/governance rules.
- [ ] Take a baseline SHA/release or tag and back up the current wiki before any rename.
- [ ] Enumerate all tracked files by owner: Polaris / Axis / Meridian / Sentinel / shared contract / historical.
- [ ] Audit cross-repo references: `pedrobritx/bsdl`, `pedrobritx/bsf`, absolute URLs, GitHub Actions `uses:`, package names, Figma bridges, callbacks, webhooks, site URLs and local remotes.
- [ ] Snapshot workflow schedules, secrets *names* (not secret values), repo variables, environments, permissions, protection rules, Pages, releases and deploy hooks. GitHub repo content API alone does not verify every repository setting.
- [ ] Define stable export surfaces, version scheme and smoke tests before file movement.

## Phase 1 — Create Axis (extract first)
- [ ] Create `pedrobritx/axis` with README, independent `AGENTS.md`, source provenance, LICENSE decision, changelog, version policy and test CI.
- [ ] Curate engineering-specific material from the current BSF root, preserving authorship/provenance and links to original BSDL commit; audit mixed directories one file at a time.
- [ ] Axis owns reusable engineering workflows and technology *profiles* (web, mobile, desktop), not a repo per discipline.
- [ ] Test standalone Axis adoption in a scratch project **without** Polaris or Meridian.
- [ ] In Polaris, replace extracted canonical copies with slim pointers after Axis passes tests; avoid two independently edited sources of truth.

## Phase 2 — Create Sentinel (minimal useful slice)
- [ ] Create `pedrobritx/sentinel` with threat-model template, security baseline, identity/access checklist, secret policy, supply-chain check and security change gate.
- [ ] Port specialist security knowledge without moving the root `SECURITY.md` reporting contact/policy blindly.
- [ ] Add automated checks only where they produce meaningful evidence; avoid excessive false positives and blanket approvals.
- [ ] Verify standalone Sentinel use with a scratch repository and secure, least-privilege GitHub permissions.

## Phase 3 — Align Meridian (conservative)
- [ ] Keep Figma file and four existing workflows where they are.
- [ ] Update BSDL/Polaris reference links and document product boundary; do not rewrite unrelated design semantics.
- [ ] Expose a versioned adoption contract or package entry points only after independent build/CI checks.
- [ ] Keep stable 0.5 intact; handle 0.6 experimental milestones independently.
- [ ] Test consumption by an app not built with Axis.

## Phase 4 — Rename BSDL to Polaris (only after gates)
- [ ] Verify candidate names and ecosystem/umbrella brand separately. Do not conflate brand name with GitHub organization or a fifth repository.
- [ ] Check every caller of the current repo's actions/reusable workflows; **GitHub does not redirect those references after rename**.
- [ ] Ensure consumers reference the new `pedrobritx/polaris` location with explicit versions; prepare cutover in pull requests before rename.
- [ ] Confirm wiki backup, project Pages URLs, webhook endpoint assumptions, repo integrations, linked branch protections and git remote URLs.
- [ ] Rename using GitHub repository Settings, with the original repository still retained (history/issues/wiki).
- [ ] Update local remotes, docs and consumers; then run wiki sync, docs validation, agent retrieval, integration and rollback smoke tests.
- [ ] **Do not create a new repo at the previous `pedrobritx/bsdl` name**: doing so breaks redirects.
- [ ] Decide deliberately whether historical `pedrobritx/bsf` redirects must remain or can be retired; do not repurpose this path during cutover.

## Phase 5 — Minimal composition (no centralized secrets)
- [ ] Define `ecosystem.schema.json` and `ecosystem.yaml` contract within Polaris.
- [ ] Declare optional Axis/Meridian/Sentinel capabilities and version compatibility; no implied source copying.
- [ ] Provide project-level adapters for GitHub / Figma / Supabase / Vercel (only applicable adapters run).
- [ ] CI validates a standalone Axis consumer, standalone Meridian consumer, standalone Sentinel consumer and one integrated project.
- [ ] Require a reviewed PR for cross-repo changes; no blanket bot write token; production/deletion/security-policy alterations remain human-approved.

## Workflow ownership after cutover
| Workflow | New home | Cutover requirement |
| --- | --- | --- |
| `docs-validate.yml` | Polaris | Keep; add Axis/Sentinel independent validators rather than transplant blindly |
| `wiki-sync.yml` | Polaris | Preserve; verify wiki destination after rename with backup |
| `figma-sync.yml` | Meridian | Preserve scheduled and dispatch jobs; verify Figma token and repository dispatch only, without exposing values |
| `figma-bridge-check.yml` | Meridian | Preserve existing pull-request verification |
| `forest-figma-handoff.yml` | Meridian | Preserve issue-based review protocol; Figma editable frames are not automatically updated by this workflow |
| `pages.yml` | Meridian | Preserve current Pages deployment and base path `/meridian/` |
| New `engineering-validate.yml` | Axis | Add when Axis implementation is extracted |
| New `security-baseline.yml` | Sentinel | Add after review of supply-chain and least-privilege baseline |

## Definition of done
- No history or approved ADR lost.
- Polaris canon remains discoverable and CI valid.
- Axis independently useful without Meridian or Polaris runtime.
- Meridian builds, tests, syncs and publishes as before, with existing Figma file intact.
- Sentinel security controls work without proprietary dependency.
- At least one opt-in project composes the three modules under Polaris through reviewed, versioned contracts.
- Integration failures are visible; no silent destructive action or credential leak.

## Naming
Polaris · Axis · Meridian · Sentinel are accepted *candidate* product labels for planning. Final product naming and a potential umbrella name are distinct branding decisions; verify collisions/trademarks before external launch. No new fifth repo is necessary to have an umbrella brand.

## Rollback strategy
Before rename/extraction, snapshot commits, wiki and CI settings. Extraction happens in separate repositories/PRs. If a gate fails, leave `bsdl` authoritative and unrenamed, and revert proposed integration PRs. A rename rollback requires updating integrations and re-testing: redirects alone do not repair reusable workflow calls.

## Links to source of truth
- https://github.com/pedrobritx/bsdl
- https://github.com/pedrobritx/meridian
- https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository
- https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations
