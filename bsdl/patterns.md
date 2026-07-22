---
title: Patterns
owner: CEO
status: Active
last_updated: 2026-07-22
---

# 7. Patterns

---

> **Patterns are documented, reusable solutions to recurring engineering problems within a specific context.**
> 

They capture proven knowledge acquired through experience and provide a common language for discussing software solutions without prescribing a single implementation.

Within BSDL, patterns describe *why* a solution exists, *when* it should be used, *how* it works, and *what trade-offs it introduces*.

Patterns are descriptive rather than prescriptive. Their suitability always depends on context, constraints, and engineering goals.

---

# Purpose

The Patterns section exists to preserve reusable engineering knowledge.

Rather than rediscovering solutions for recurring problems, engineers can apply established patterns, understand their consequences, and adapt them to the needs of each project.

Patterns accelerate learning, improve communication, and provide a shared vocabulary for humans and AI.

---

# Objectives

- Capture proven engineering knowledge.
- Standardize recurring solutions.
- Improve architectural consistency.
- Reduce accidental complexity.
- Document trade-offs explicitly.
- Connect related patterns into an engineering knowledge graph.
- Enable AI to recommend appropriate solutions based on context.

---

# Principles

- Patterns solve recurring problems.
- Every pattern exists because of a context.
- Every pattern has consequences.
- Patterns should describe trade-offs, not perfection.
- Patterns communicate intent.
- Patterns evolve through experience.
- No pattern is universally applicable.
- Context determines appropriateness.

---

# Organization

```
🧩 Patterns

├── Architectural Patterns
├── Design Patterns
├── Enterprise Patterns
├── Integration Patterns
├── Data Patterns
├── Distributed Systems Patterns
├── Cloud Patterns
├── AI Patterns
├── DevOps Patterns
├── User Experience Patterns
├── Workflow Patterns
├── Organizational Patterns
├── Pattern Languages
└── Pattern Catalog
```

---

# Architectural Patterns

Large-scale system organization.

Examples:

- Layered Architecture
- Clean Architecture
- Hexagonal Architecture
- Onion Architecture
- Pipes and Filters
- Event-Driven Architecture
- Microkernel
- Microservices
- Modular Monolith
- Service-Oriented Architecture (SOA)

---

# Design Patterns

Object-oriented and general software design.

Examples:

### Creational

- Factory Method
- Abstract Factory
- Builder
- Prototype
- Singleton

### Structural

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

### Behavioral

- Strategy
- Observer
- State
- Command
- Iterator
- Mediator
- Memento
- Chain of Responsibility
- Template Method
- Visitor

---

# Enterprise Patterns

Business application architecture.

Examples:

- Repository
- Unit of Work
- Specification
- Service Layer
- Domain Model
- Transaction Script
- Active Record
- Data Mapper
- Identity Map

---

# Integration Patterns

Communication between systems.

Examples:

- Publish–Subscribe
- Message Broker
- Event Bus
- API Gateway
- Backend for Frontend (BFF)
- Saga
- Outbox
- CQRS
- Event Sourcing

---

# Data Patterns

Data organization and persistence.

Examples:

- Entity–Attribute–Value
- Materialized View
- Cache Aside
- Write Through Cache
- Read Replica
- Sharding
- Partitioning

---

# Distributed Systems Patterns

Engineering reliable distributed software.

Examples:

- Circuit Breaker
- Bulkhead
- Retry
- Timeout
- Leader Election
- Consensus
- Idempotency
- Health Check

---

# Cloud Patterns

Cloud-native engineering.

Examples:

- Sidecar
- Ambassador
- Strangler Fig
- Blue–Green Deployment
- Canary Release
- Auto Scaling
- Immutable Infrastructure

---

# AI Patterns

This is where BSDL can contribute something original.

Examples:

- Retrieval-Augmented Generation (RAG)
- Multi-Agent Collaboration
- Tool Calling
- Prompt Chaining
- Reflection
- Self-Consistency
- Context Routing
- Human-in-the-Loop
- AI Pair Programming
- Knowledge-Augmented Generation

---

# DevOps Patterns

Engineering workflow.

Examples:

- GitOps
- Trunk-Based Development
- Infrastructure as Code
- Progressive Delivery
- Continuous Deployment

---

# User Experience Patterns

Recurring interaction solutions.

Examples:

- Wizard
- Infinite Scroll
- Progressive Disclosure
- Master–Detail
- Dashboard
- Empty States
- Undo

---

# Workflow Patterns

Software engineering processes.

Examples:

- RFC Process
- ADR Workflow
- Feature Branch Workflow
- Release Train
- Incident Lifecycle

---

# Organizational Patterns

Engineering at scale.

Examples:

- Conway's Law Applications
- Team Topologies
- Platform Teams
- Stream-Aligned Teams
- Enabling Teams

---

# Pattern Languages

One of the most interesting ideas inherited from Christopher Alexander.

Instead of isolated patterns, BSDL should show **how patterns work together**.

For example:

```
Requirements

↓

DDD

↓

Hexagonal Architecture

↓

Repository

↓

Specification

↓

Unit of Work

↓

CQRS

↓

Event Sourcing
```

This is far more valuable than a flat catalog because it teaches engineers to compose solutions.

---

# Pattern Catalog

A searchable index of every pattern documented in BSDL.

Suggested database properties:

- Name
- Category
- Problem
- Context
- Complexity
- Domain
- Maturity
- Related Patterns
- Related Standards
- Related Principles
- Related Anti-patterns

---

# Pattern Template

Every pattern should follow the same structure.

```
Name

Category

Intent

Problem

Context

Motivation

Applicability

Structure

Participants

Workflow

Advantages

Disadvantages

Trade-offs

Consequences

Known Uses

Related Patterns

Related Anti-patterns

Related Standards

References

Machine-readable Metadata
```

---

# BSDL Pattern Relationships

One original feature I'd introduce is that **patterns are explicitly connected** rather than documented in isolation.

Each pattern would define relationships such as:

- **Requires** — patterns that should already be in place.
- **Complements** — patterns commonly used together.
- **Conflicts With** — patterns that solve the same problem differently or are generally incompatible.
- **Alternative To** — interchangeable approaches for similar contexts.
- **Refines** — a more specialized version of another pattern.
- **Replaced By** — successor patterns that supersede older approaches.
