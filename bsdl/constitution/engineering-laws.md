---
title: Engineering Laws
owner: CEO
status: Active
last_updated: 2026-07-22
---

# Engineering Laws

## Law of Context

Every architecture, workflow, and process is local to a situation. Reuse the principle, not the dogma.

### Practical meaning

The same policy should not be copied into different projects unchanged. It should be translated to the project’s risk profile, budget, team maturity, regulatory burden, and product stage.

## Law of Human Primacy

If a system is technically elegant but socially harmful, it is not successful.

### Practical meaning

A solution does not become good merely because it is performant, maintainable, or clever.

## Law of Collective Knowledge

Every useful system is an inheritance. It must preserve and amplify the knowledge that made it possible.

### Practical meaning

Good software leaves behind durable explanatory artifacts: architecture notes, ADRs, test suites, and operational guidance.

## Law of Evidence

Claims about software must be testable, observable, or otherwise falsifiable.

### Practical meaning

Every major claim should answer at least one of the following:

- What test proves this?
- What metric observes this?
- What failure would falsify this claim?

## Law of Adaptability

Change should be cheap where possible. High-cost decisions must be made consciously and documented.

### Practical meaning

Irreversible choices require extra scrutiny. Cheap-to-reverse choices should be favored during uncertainty.

## Law of Explicit Ethics

Ethical constraints belong in the architecture, not as afterthoughts.

### Practical meaning

Accessibility, privacy, security, environmental cost, and power asymmetry should be discussed during design—not only during review or incident response.

## Law of Architectural Memory

Important decisions must be recorded as durable context, not left as tribal memory.

### Practical meaning

If the team cannot explain why a major decision was made, the system is already weaker than it appears.

## Law of Consistency

Consistency is usually more valuable than local optimization. Abstraction is useful only when it reduces cognitive load without hiding meaning.

### Practical meaning

Prefer boring clarity over clever condensation.

## Law of Boundaries

A system is never isolated. Every design choice affects and is affected by surrounding systems.

### Practical meaning

Software architecture includes the team, the deployment environment, the organization, and the users.

## Law of Reversibility

The more expensive a decision is to reverse, the earlier it must be made explicit and the more carefully it must be documented.

### Practical meaning

Data model changes, security decisions, and hosting choices deserve more caution than internal naming.
