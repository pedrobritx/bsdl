---
title: ADR-006 optional discipline composition
owner: Maintainer
status: Accepted
last_updated: 2026-10-16
---

# Polaris intake and independent disciplines

## Context and authority

On 2026-10-16 the owner requested a repository ownership audit, cleanup and seamless delegation through Polaris while retaining the ability to opt out of disciplines. This authorises this scoped operational implementation. It does not amend the philosophical canon or grant merge/release/provider authority.

## Decision

The [composition contract](../../integration/README.md) owns repository boundaries, adoption, intake and handoff semantics. Each discipline supplies a local manifest and remains usable without Polaris or the other disciplines. A dependency-free local planner validates explicit human/agent selections, verifies required guidance exists and records immutable source revisions plus local modification state. It never claims to interpret requests or execute agents.

Project implementation, designs and security findings belong in the adopting product. Reusable methods/components belong in the owning discipline. The previously empty Constellation repository receives product definition and contribution boundaries for the future hybrid application; it does not acquire duplicate governance or discipline implementations.

Replace obsolete wiki policy copies with navigation to their owners; consolidate empty Polaris memory slots and remove duplicated onboarding. Retain historical ADRs, extraction ledgers, canonical text, Meridian's stable/experimental boundaries and the standalone documentation validators. Blank Axis adopter templates remain an opt-in catalogue, not mandatory project files.

## Alternatives and consequences

A single runtime/monorepo would make independent adoption harder. A distributed autonomous agent service would introduce credentials, hosting, failure recovery and coordination costs before an actual execution need. The selected manifest/handoff seam is small and reversible, can later be consumed by the Constellation application, and works in an ordinary AI coding session now. It still requires a host agent or human to read context, choose disciplines, perform work and verify the integrated result.

An excluded requested discipline stays an unverified coverage gap. No automatic pass, fallback provider, deployment, merge or security-posture change is implied. This operational decision derives from laws of Context, Evidence, Boundaries, Consistency, Adaptability and Architectural Memory.
