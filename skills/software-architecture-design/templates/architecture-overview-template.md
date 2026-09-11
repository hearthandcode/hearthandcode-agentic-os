# {{System Name}} — Architecture Overview

> One document a new engineer reads in twenty minutes to understand what the
> system is, why it is shaped the way it is, and where the decisions live.
> Replace every `{{placeholder}}`; delete instruction blocks before publishing.
> Keep it current: this document is wrong the day the code contradicts it.

## 1. System Brief

{{One paragraph: what the system does, for whom, and what "working" means.
Written so a stranger can repeat it back in one sentence.}}

- **Users:** {{who uses it, at what scale today}}
- **Clients:** {{web / mobile / CLI / partner integrations}}
- **Operating team:** {{who builds it, who is on call}}

## 2. Stakeholders and What They Need

| Stakeholder | Cares about | Design implication |
|---|---|---|
| {{end users}} | {{speed, reliability}} | {{scenario Q1, Q3}} |
| {{operators / on-call}} | {{legible failures, low alert load}} | {{failure-mode section}} |
| {{the business}} | {{cost ceiling, optionality to grow}} | {{constraint row, revisit triggers}} |

## 3. Quality-Attribute Scenarios

{{The 6-10 scenarios the design must satisfy, in six-part form. Full guidance:
references/quality-attribute-scenarios.md. Every row needs a mechanism and a
verification — a scenario without both is a wish.}}

| # | Stimulus | Environment | Response measure | Mechanism | Verification |
|---|---|---|---|---|---|
| Q1 | {{user requests note list}} | {{weekday load}} | {{p95 < 300 ms}} | {{indexes, pagination}} | {{load test}} |
| Q2 | {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

**Explicitly sacrificed (for honesty):** {{quality not optimized, e.g. "no
horizontal write scaling; single-writer Postgres"}} — **revisit trigger:**
{{measurable condition}}.

## 4. Context and Constraints

- **Non-negotiable:** {{mandated stack, compliance, existing data with no
  migration window, budget caps}} — mark each as verified mandate or soft
  preference.
- **External actors:** {{email provider, payment gateway, SSO}} — what crosses
  the boundary, in which direction.
- **Operational maturity:** {{what the team can operate today — no machinery
  beyond this without an operator plan}}.

## 5. Component Map

{{One component per row. A reader must be able to draw this as a diagram in
ten minutes: components as boxes, dependencies as arrows pointing the declared
direction.}}

| Component | Owns (data + behavior) | May ask (via ports) | Never does |
|---|---|---|---|
| {{Notes}} | {{notes tables, CRUD, tagging}} | {{ask Access about permissions}} | {{decide permissions itself}} |
| {{Access}} | {{ACL rules, shares}} | {{read note existence from Notes}} | {{write notes}} |
| {{Search}} | {{derived search index}} | {{consume note events}} | {{hold source-of-truth data}} |

**Architecture style:** {{e.g. hexagonal modular monolith}} — rationale in
ADR-{{number}}; rejected alternatives recorded there.

## 6. Interfaces

{{For each boundary, the contract summary. Full rules: references/api-design-principles.md.}}

- **Public API:** {{e.g. REST /v1/notes, /v1/search — auth via {{scheme}}; versioning in path; error contract with stable codes and retryable flag}}
- **Internal ports:** {{e.g. NoteRepository, AccessPolicy, NoteEvents}} — in-process today; designed so {{extraction candidate}} can be extracted without caller changes.
- **Events:** {{name, payload contract, delivery guarantee, lag tolerance}}.

## 7. Data Model and Ownership

{{Entities, relationships, one owner each. Full guidance: references/data-modeling-basics.md.}}

| Entity | Owner | Notes |
|---|---|---|
| {{notes}} | {{Notes}} | {{FKs, constraints, soft-delete policy}} |
| {{note_shares}} | {{Access}} | {{unique (note_id, user_id)}} |
| {{search index}} | {{Search}} | {{derived; rebuild path: <stated>; refresh: <mechanism>}} |

**Consistency model:** {{strong within {{store}}; eventual for {{index}}, lag
tolerated up to {{N}} seconds per scenario {{Q#}}}}.

## 8. Failure Behavior

| Component failure | User-visible effect | System behavior | Recovery |
|---|---|---|---|
| {{Search down}} | {{search shows "unavailable"}} | {{notes CRUD unaffected}} | {{restart; index rebuild path}} |
| {{database failover}} | {{< 5 min errors}} | {{ standby promotion}} | {{drill twice a year}} |

## 9. Decision Index

| ADR | Title | Status | Revisit trigger |
|---|---|---|---|
| ADR-{{0001}} | {{single deployable, hexagonal modules}} | {{accepted}} | {{trigger + measure}} |
| ADR-{{0002}} | {{Postgres FTS}} | {{accepted}} | {{trigger + measure}} |

Full ADRs live in {{docs/adr/}}; format per templates/adr-template.md.

## 10. Review Record

- **Last 40-point review:** {{date}} — findings and dispositions: {{fixed /
  accepted / tracked, with one line each}}.
- **Next scheduled review:** {{date or trigger}}.

## 11. Revisit Triggers (the living part of this document)

| Decision | Trigger (measurable) | Action if fired |
|---|---|---|
| {{single-writer Postgres}} | {{write p95 > 200 ms sustained}} | {{open ADR for read replicas or queue offload}} |
| {{monolith shape}} | {{onboarding a second team}} | {{re-evaluate module extraction (ADR-0001)}} |

---

*This overview is governed by the architecture-review-checklist; update it in
the same PR as any change it describes.*
