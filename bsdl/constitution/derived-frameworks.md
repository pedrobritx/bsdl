---
title: Derived Frameworks
owner: CEO
status: Active
last_updated: 2026-07-22
---

# Derived Frameworks

## 1. Lifecycle selection

BSDL does not enforce a single lifecycle. It selects a lifecycle from context.

### Primary drivers

- Regulation and domain risk
- Cost of failure
- Technical and market uncertainty
- Team maturity
- Budget constraints
- User expectations
- AI capability

### Rule of thumb

- High risk and high regulatory burden favor linear or heavily verified lifecycles.
- High uncertainty and fast learning favor iterative or evolutionary lifecycles.
- Many projects should combine both: discovery first, hardening later.

### Lifecycle selection workflow

1. Identify the domain.
2. Classify the failure cost.
3. Measure uncertainty.
4. Estimate reversibility.
5. Choose the lifecycle.
6. Re-evaluate at each major milestone.

### Example

A medical billing platform may need strict verification and auditability.

A startup MVP may need rapid discovery, user learning, and frequent reprioritization.

## 2. Architecture selection

Architecture should be designed just enough upfront to establish costly boundaries, then allowed to emerge within those boundaries.

### One-way doors

- Data model
- Security boundary
- Hosting and compliance constraints
- Major deployment topology

### Two-way doors

- Folder structure
- Module boundaries
- Naming conventions
- UI composition details

### Architecture workflow

1. Define the irreversible parts.
2. Protect them with explicit design decisions.
3. Leave the reversible parts open for learning.
4. Review the structure after evidence arrives.
5. Refactor only with traceable reason.

### Example

A monorepo can evolve into several deployable units later, but a bad database boundary can become very expensive to undo.

## 3. Decision heuristics

When in doubt, ask:

1. What is the actual context?
2. What is the least harmful option?
3. What is the most reversible choice?
4. What must be documented immediately?
5. What does the evidence say?

### Example decision record

**Question:** Should we split the backend into microservices?

**Context:** The team is small, the domain is still unstable, and deployment risk is manageable.

**Heuristic result:** Keep a modular monolith for now.

**Reason:** The split would increase coordination cost and obscure behavior before the system has earned that complexity.

## 4. AI collaboration model

AI may act as apprentice, specialist, reviewer, or architect surrogate depending on the task, but never as final moral authority.

### Roles

- **Apprentice**: drafts, summarizes, restates, and explores
- **Specialist**: fills a narrow technical gap
- **Reviewer**: critiques code, docs, or architecture
- **Architect surrogate**: proposes structure under explicit human supervision

### Guardrails

- AI must not silently substitute its judgment for human accountability.
- AI proposals must be reviewable.
- AI should expose uncertainty instead of pretending certainty.

### Example workflow

1. Human states intent.
2. AI proposes alternatives.
3. Human selects a direction.
4. AI drafts implementation.
5. Human verifies and approves.

## 5. Documentation model

Documentation is not a side product. It is part of the system.

### Documentation layers

- **Intent docs**: why
- **Design docs**: how
- **Runbooks**: how to operate
- **ADRs**: why this, not that
- **Living notes**: what changed

### Documentation workflow

1. Record the problem.
2. Record the constraints.
3. Record the decision.
4. Record the rejected alternatives.
5. Record the expected consequences.
6. Update the record when reality changes.

### Example

If a team changes database strategy, the ADR should explain:

- why the old choice failed
- what evidence triggered the change
- what costs the new choice introduces
- what remains reversible

## 6. Failure model

BSDL treats failure as informative rather than shameful.

### Good failure

A good failure is:

- visible
- bounded
- recoverable
- observable
- documented

### Bad failure

A bad failure is:

- silent
- cascading
- ambiguous
- hard to reproduce
- hidden by poor observability

### Example

A feature flag that fails closed with a clear error is preferable to a hidden corruption that appears days later.

## 7. Sustainability model

Sustainability has three dimensions:

- **Environmental**: lower unnecessary compute, storage, and transfer costs
- **Economic**: reduce long-term maintenance burden
- **Human**: preserve team health and cognitive clarity

### Example

A simpler architecture that uses fewer servers, requires less debugging, and lowers burnout is more sustainable than a flashy one.
