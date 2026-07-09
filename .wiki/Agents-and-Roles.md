*One section per role: what it does, and the one thing it must never do.* — [[Home]]

Every agent file shares six sections — Responsibilities, Priorities, Required reading, Never do, Definition of Done, Escalation rules. Usage: *"Act as `agents/frontend_engineer.md`"* — the AI loads the role and its boundaries, no repetition needed.

### CEO (Human)
Owns vision, final approval, and everything on the hard L0 list; sets delegation defaults and arbitrates conflicts between roles. **Never:** delegate the hard L0 list. → [agents/CEO.md](https://github.com/pedrobritx/bsf/blob/main/agents/CEO.md)

### Product Manager
Owns `docs/product/` and translates vision into specs via the feature-spec template; runs the Question Engine before any spec is "ready". **Never:** mark a spec ready with unanswered Question Engine items. → [agents/product_manager.md](https://github.com/pedrobritx/bsf/blob/main/agents/product_manager.md)

### Software Architect
Owns `ARCHITECTURE.md` (the hub) and the Decision Engine; reviews structural changes and curates ADRs. **Never:** approve violations of `constraints/` at any confidence level. → [agents/architect.md](https://github.com/pedrobritx/bsf/blob/main/agents/architect.md)

### Frontend Engineer
Implements UI from screen and design-system specs; owns client state, data-fetching patterns, and error/loading/empty states. **Never:** invent visual design or API contracts — those belong to Designer and Backend. → [agents/frontend_engineer.md](https://github.com/pedrobritx/bsf/blob/main/agents/frontend_engineer.md)

### Backend Engineer
Implements endpoints, business logic, and integrations; owns boundary validation (Zod) and migrations with rollbacks. **Never:** expose an endpoint without an explicit auth decision. → [agents/backend_engineer.md](https://github.com/pedrobritx/bsf/blob/main/agents/backend_engineer.md)

### Designer
Owns `docs/design/` and produces specs complete enough that engineers never invent UI; guards accessibility at design time. **Never:** ship a screen spec without all states (default/loading/empty/error). → [agents/designer.md](https://github.com/pedrobritx/bsf/blob/main/agents/designer.md)

### QA Engineer
Owns the testing strategy and enforces the Definition of Done on every PR; hunts edge cases. **Never:** accept "not applicable" without written justification. → [agents/qa_engineer.md](https://github.com/pedrobritx/bsf/blob/main/agents/qa_engineer.md)

### DevOps Engineer
Owns CI/CD, environments, and monitoring; executes the Release playbook. **Never:** deploy outside the Release playbook. → [agents/devops_engineer.md](https://github.com/pedrobritx/bsf/blob/main/agents/devops_engineer.md)

### Security Engineer
Owns security verification, the Security Review playbook, and all auth/permission reviews. **Never:** approve auth posture changes autonomously — always L0. → [agents/security_engineer.md](https://github.com/pedrobritx/bsf/blob/main/agents/security_engineer.md)

### Data Engineer
Owns schema, data dictionary, seed data, and migrations; designs tables and RLS with Backend. **Never:** ship a schema change without dictionary + migration + rollback in the same PR. → [agents/data_engineer.md](https://github.com/pedrobritx/bsf/blob/main/agents/data_engineer.md)

### Technical Writer
Owns the docs index, template compliance, and changelog quality; audits for duplication and broken links. **Never:** duplicate content to "make a doc more complete" — link instead. → [agents/technical_writer.md](https://github.com/pedrobritx/bsf/blob/main/agents/technical_writer.md)

---

**→ In the repository**
- [agents/README.md](https://github.com/pedrobritx/bsf/blob/main/agents/README.md) — the org chart and the six-section format

See also: [[Playbooks]] · [[Governance and Delegation]]
