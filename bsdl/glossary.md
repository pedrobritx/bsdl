---
title: Glossary
owner: CEO
status: Active
last_updated: 2026-07-22
---

# 9. Glossary

---

> **The Glossary is the canonical dictionary of the Britx Software Design Language (BSDL). It defines the official meaning of every term, concept, acronym, and abbreviation used throughout the framework.**
> 

The Glossary establishes a shared vocabulary that ensures consistent communication between engineers, teams, organizations, and AI systems.

Each term has a single authoritative definition, preventing ambiguity and enabling interoperability across the entire BSDL knowledge base.

---

# Purpose

The Glossary exists to provide precise, consistent, and authoritative definitions for every concept used within BSDL.

It serves as the semantic foundation upon which all other disciplines are built.

---

# Objectives

- Establish a common engineering vocabulary.
- Eliminate ambiguity.
- Standardize terminology.
- Support machine-readable knowledge.
- Improve communication.
- Enable semantic search.
- Connect related concepts across BSDL.
- Preserve conceptual consistency as BSDL evolves.

---

# Principles

- One concept, one canonical definition.
- Definitions should be technology-neutral whenever possible.
- Terms should be concise yet precise.
- Every definition should be understandable by humans.
- Every definition should be interpretable by machines.
- Terminology evolves through governance.
- Synonyms should reference the canonical term.
- Definitions should be linked to related concepts.

---

# Organization

```
📖 Glossary

├── Core Concepts
├── Architecture
├── Design
├── Development
├── Operations
├── Artificial Intelligence
├── Standards
├── Patterns
├── Security
├── Testing
├── Documentation
├── Project Management
├── Acronyms
├── Symbols
└── Deprecated Terms
```

---

# Core Concepts

The fundamental vocabulary of BSDL.

Examples:

- Software
- System
- Engineering
- Design
- Architecture
- Model
- Component
- Interface
- Module
- Artifact
- Pattern
- Principle
- Standard

---

# Architecture

Definitions related to software structure.

Examples:

- Layer
- Service
- Boundary
- Dependency
- Domain
- Context
- View
- Architecture Style
- Quality Attribute

---

# Design

Design-related terminology.

Examples:

- Abstraction
- Encapsulation
- Coupling
- Cohesion
- Composition
- Responsibility
- Interaction
- Constraint

---

# Development

Implementation terminology.

Examples:

- Commit
- Branch
- Merge
- Refactoring
- Build
- Compilation
- Dependency
- Framework
- Library

---

# Operations

Operational vocabulary.

Examples:

- Deployment
- Rollback
- Monitoring
- Logging
- Observability
- Availability
- Scalability
- Incident
- Runbook

---

# Artificial Intelligence

AI terminology.

Examples:

- Prompt
- Context
- Token
- Embedding
- Agent
- Tool Calling
- Hallucination
- Retrieval
- Memory
- Reasoning

---

# Standards

Normative terminology.

Examples:

- Requirement
- Recommendation
- Compliance
- Specification
- Normative
- Informative
- Guideline
- Policy

---

# Patterns

Pattern-related terminology.

Examples:

- Intent
- Context
- Applicability
- Trade-off
- Consequence
- Participant
- Collaboration

---

# Security

Security concepts.

Examples:

- Authentication
- Authorization
- Encryption
- Secret
- Threat
- Vulnerability
- Risk
- Attack Surface

---

# Testing

Testing terminology.

Examples:

- Unit Test
- Integration Test
- Regression
- Mock
- Fixture
- Assertion
- Coverage

---

# Documentation

Documentation vocabulary.

Examples:

- README
- ADR
- RFC
- Changelog
- Metadata
- Specification
- Template

---

# Project Management

Project and process terms.

Examples:

- Milestone
- Sprint
- Roadmap
- Backlog
- Requirement
- Stakeholder
- Deliverable

---

# Acronyms

Every acronym should have exactly one canonical definition.

Examples:

- ADR
- API
- CI
- CD
- CQRS
- CRUD
- DDD
- DSL
- JSON
- JWT
- MVC
- REST
- SOLID
- SQL
- UML

---

# Symbols

Engineering notation used across BSDL.

Examples:

- →
- ←
- ↔
- ⇒
- ✓
- ✗
- ∞

---

# Deprecated Terms

A historical record of terminology that has been replaced or discouraged.

Example:

| Deprecated | Replacement |
| --- | --- |
| Master Branch | Main Branch |
| Whitelist | Allowlist |
| Blacklist | Denylist |

This preserves historical context while promoting current terminology.

---

# Glossary Entry Template

Every term should follow the same structure.

```
Term

Category

Definition

Purpose

Context

Notes

Synonyms

Antonyms

Abbreviations

Related Concepts

Related Standards

Related Patterns

Examples

References

Machine-readable Metadata
```

---

# Semantic Relationships

To make the glossary useful for both humans and AI, every term should explicitly define its relationships to other terms.

Relationship types could include:

- **Is A** — hierarchical classification (e.g., *Repository* **is a** Pattern).
- **Part Of** — compositional relationship (e.g., *Module* **is part of** an Architecture).
- **Related To** — general semantic association.
- **Depends On** — prerequisite concept.
- **Opposes** — contrasting or conflicting concept.
- **Synonym Of** — alternate accepted term.
- **Deprecated In Favor Of** — historical replacement.

This effectively turns the glossary into a **semantic knowledge graph**, allowing navigation from one concept to another rather than treating definitions as isolated entries.

---

# Canonical Vocabulary Levels

One feature I'd add to distinguish BSDL is a classification that indicates the status of each term within the framework:

| Level | Meaning |
| --- | --- |
| **Core** | Fundamental term used throughout BSDL. |
| **Domain** | Specific to a particular engineering discipline (e.g., Architecture, AI, Operations). |
| **External** | Adopted from an external standard or body of knowledge (e.g., UML, HTTP, OAuth). |
| **Experimental** | New terminology under evaluation and subject to change. |
| **Deprecated** | Retained only for historical compatibility; use the recommended replacement instead. |
