---
title: Constellation repository composition audit
owner: Maintainer
status: In review
last_updated: 2026-10-16
---

# Repository audit and implementation record

The owner requested repository placement, Polaris-led coordination, independent discipline adoption and removal of legacy/redundant content. The [composition contract](../../integration/README.md) owns the resulting repository map and protocol; [ADR-006](../../decisions/adr/006-optional-discipline-composition.md) records this operational decision. No philosophical canon amendment is included.

## Inspected baseline

| Repository | Reviewed main revision | Tracked files |
|---|---|---:|
| Polaris | `2360903f6f247f38aad798e2646bd0c30d208636` | 91 |
| Axis | `9de5994ace6eb43d633e9018f44f6aa992fef67b` | 121 |
| Meridian | `e236561b2c8d20784e90a838310a67ee6b3f6c2c` | 190 |
| Sentinel | `d1e678e966c86ffe39ebf8bfbd19d9ac242a3c1b` | 17 |
| Constellation | Empty repository, no main commit | 0 |

Inspected contributor instructions, constitutional sections, operating rules, roles, documentation/template ownership, manifests, CI, build/test seams, extraction records, exact duplicate files and references to legacy design artifacts. Baseline documentation/tooling tests passed (Polaris 30, Axis 27, Sentinel 27); Meridian's 70 existing tests passed.

## Findings and changes

- The earlier capability extraction already placed engineering in Axis, the design implementation in Meridian and security methods in Sentinel. The missing connection was an explicit composition/adoption protocol, not another wholesale extraction.
- Polaris now owns a dependency-free local handoff planner. Explicit selections, missing source failures, all eight capability combinations, governance-free composition and immutable source metadata have behavioural checks. The host agent/human still analyses requests and performs/delegates work.
- Each discipline declares local entry points, reusable ownership and expected outputs in `discipline.json`. Product-specific outputs remain in their product repository. Constellation receives its initial product definition and adoption configuration rather than copied governance or a speculative application scaffold.
- Polaris's wiki contained superseded confidence-based delegation, provider defaults, obsolete branch links and a second list presented as canonical principles. Replaced policy mirrors with owner navigation, reduced the wiki from 52,590 to 7,245 bytes, and relocated useful project-tracking patterns to Axis.
- Replaced duplicated Claude instructions with the shared AGENTS entry point; consolidated three empty Polaris memory slots; corrected onboarding, decision and completion guidance that assumed local engineering playbooks or compulsory Axis documents. Historical records remain labelled as historical.
- Axis's document graph remains a catalogue of selectively adopted templates. Generic product design/security document slots are not competing Meridian/Sentinel implementations. Copying the whole empty catalogue is explicitly discouraged.
- Moved Meridian's unused 0.1 tokens and native inventory to `archive/0.1/` without changing their bytes. Preserved stable 0.5 sources, experimental 0.6 Lab isolation, native node IDs, token/copy baselines and active generated outputs.
- Corrected an existing malformed Lab footer, empty CSS import and inconsistent JSON import attributes found during build verification.
- Exact duplicate local validators/tests remain deliberately independent: removing them would make otherwise standalone repositories depend on a sibling or network service. The equal Meridian copy baseline and website content serve different conflict-detection roles and are not redundant build artifacts.

## Verification

Fresh local results on 2026-10-16:

| Check | Result |
|---|---|
| Polaris documentation validator | Passed: 65 documents |
| Polaris unit/tooling suite | Passed: 43 tests, including 13 composition cases |
| Axis documentation/tooling | Passed: 116 documents and 27 tests |
| Sentinel documentation/tooling | Passed: 12 documents and 27 tests |
| Meridian `npm test` | Passed: 70 tests |
| Meridian `npm run build` | Passed; the three identified source build warnings are resolved |
| Real manifests, all eight discipline combinations | Passed; disabled scopes remain unverified and missing enabled sources fail |
| Wiki navigation and local link targets | Passed |
| Canonical Polaris text and extraction ledgers | No changed bytes |
| Meridian 0.1 archive moves | Original bytes match exactly |
| Generated Meridian CSS/plugin bundles | Rebuild produces no tracked differences |
| Repository whitespace checks | Passed |
| Browser suite | Blocked by environment: Chromium absent; browser download returned an invalid/truncated archive. `npm run test:browser -- --workers=2 --max-failures=1` stopped before browser assertions (1 launch failure, 1 interrupted, 80 not run). |

Documentation validation establishes document health; planned handoffs are not completed product work. Native Figma editing, human accessibility studies, production security, deployments and an autonomous builder are outside this implemented verification scope. Rerun Meridian’s browser suite in CI or an environment with a working Chromium installation before approving its UI cleanup.

## Review coordination

Review the discipline manifests and Constellation definition with the Polaris contract. Cross-repository changes are not atomic; merge owning destinations before relying on their new main-branch entry points. Current navigation links aid discovery; executed requests retain exact reviewed source revisions. Preserve existing review/merge/release gates. Sentinel already has an open naming follow-up (#2); reconcile its overlapping documentation changes during coordinated review rather than discarding that work.
