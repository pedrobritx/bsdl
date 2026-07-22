---
title: Reference Implementations
owner: CEO
status: Active
last_updated: 2026-07-22
---

# Reference Implementations

## Document stack

- Constitution
- Manifesto
- Principles
- Laws
- Lifecycle models
- Architecture standards
- Project templates
- AI prompt templates
- ADR template
- Runbook template

## BSDL decision record template

```markdown
# Decision

## Context

## Problem

## Constraints

## Options considered

## Decision

## Consequences

## Risks

## Reversibility

## Review date
```

## BSDL lifecycle template

```
Discovery
  -> Framing
  -> De-risking
  -> Design
  -> Build
  -> Verify
  -> Release
  -> Observe
  -> Evolve
```

## BSDL architecture rule template

```
If a decision is expensive to reverse, it must be:
1. explicit
2. documented
3. reviewed
4. testable where possible
```

## BSDL AI collaboration prompt template

```
Role: [apprentice | specialist | reviewer | architect surrogate]
Task: [what the AI should do]
Context: [the real-world constraints]
Non-negotiables: [ethical / technical / organizational limits]
Output format: [table | outline | markdown | code | decision matrix]
```

## BSDL heuristic table

| Question | Default direction | Why |
| --- | --- | --- |
| Need speed with low risk? | Iterate | Learning is cheaper than overdesign |
| Need safety with high cost of failure? | Verify first | Mistakes are expensive |
| Need consistency across projects? | Standardize | Reduces cognitive load |
| Need flexibility in uncertain scope? | Keep reversible | Preserves future options |
| Need ethical restraint? | Refuse the request | Some work should not exist |

## BSDL project structure example

```
project/
  docs/
    constitution/
    adr/
    runbooks/
  app/
  tests/
  infrastructure/
  scripts/
  prompts/
```

## Example workflow: choosing a lifecycle

1. Acknowledge the domain and its failure cost.
2. Classify uncertainty.
3. Identify irreversible commitments.
4. Decide whether the project needs a linear, iterative, or hybrid lifecycle.
5. Record the rationale in an ADR.
6. Review the choice after the first evidence loop.

## Example workflow: adding a new architecture rule

1. State the problem that the rule solves.
2. State the context where it applies.
3. State the failure mode it prevents.
4. State the cost of obeying the rule.
5. State the cost of breaking the rule.
6. Add an example and a counterexample.

## Example: good vs bad abstraction

### Good abstraction

A shared validation module that removes duplication and makes the domain rules obvious.

### Bad abstraction

A universal framework layer that generalizes unrelated workflows and hides important differences.

## Example: good vs bad optimization

### Good optimization

Compress assets, reduce payloads, and eliminate redundant computation after measuring a real bottleneck.

### Bad optimization

Rewriting a clear module into a clever form before there is any evidence that it matters.
