# Worked Example — QuickNotes: Complete Architecture Design Run

This file carries the extended artifacts for the worked example in SKILL.md §06: the full architecture overview content, both finished ADRs, and the review findings log. The workflow steps are in SKILL.md; this document shows what the outputs look like when filled in.

**Scenario recap.** QuickNotes: a small multi-user notes service for a 40-person startup. Web + mobile clients; users create notes, tag them, share individual notes, and full-text search everything they can read. ~200 daily active users, growth hoped for but unproven. One full-stack engineer builds it; a second joins in six months. Constraints: managed Postgres (existing account), no Kubernetes, budget for at most one additional managed service.

---

## Artifact 1 — Scenario table (filled)

| # | Source | Stimulus | Environment | Artifact | Response measure |
|---|---|---|---|---|---|
| Q1 | Signed-in web user | Opens note list | Weekday, 10 rps, warm cache miss | Notes read path | p95 < 300 ms server-side |
| Q2 | Signed-in user | Full-text search own notes | Up to 50k notes/user | Search module | p95 < 500 ms; lag ≤ 10 s behind writes |
| Q3 | Infrastructure | Primary DB fails | Any time | Postgres HA | Recovery < 5 min; ≤ 5 min data loss |
| Q4 | Product owner | Change note-level ACL rules | Any time | Access module | ≤ 1 day, one module, no client changes |
| Q5 | Malicious/buggy client | Store malformed note body | Any time | Notes write path | Reject or quarantine; other notes unaffected |
| Q6 | Signed-in mobile user | Read shared note | Any time | Notes + Access | p95 < 300 ms; revocation effective ≤ 1 read |

Prioritization by cost of failure: Q3 > Q5 > Q1 > Q6 > Q2 > Q4.
Named sacrifice: no horizontal write scaling (single-writer Postgres); revisit trigger: write p95 > 200 ms sustained for a week.
Constraint check: "managed Postgres" is a verified mandate (company account, billing already approved); "no Kubernetes" is a soft constraint — the real constraint is "nothing that needs a dedicated operator."

---

## Artifact 2 — Component map (filled)

| Component | Owns (data + behavior) | May ask (via ports) | Never does |
|---|---|---|---|
| Notes | `notes`, `note_tags` tables; CRUD; tagging; malformed-body validation | Ask Access via `AccessPolicy`; publish via `NoteEvents` | Decide permissions; touch search index |
| Access | `note_shares` table; ACL rules; share lifecycle | Read note existence via `NoteReader` port | Write notes |
| Search | Derived `notes_search` index | Consume `NoteEvents`; read `notes` snapshot for rebuild | Hold source-of-truth data |

Style: hexagonal modular monolith (ADR-0001). All module-to-module calls go through interfaces defined by the consuming side.

---

## Artifact 3 — ADR-0001 (full text)

```markdown
# ADR-0001: Single deployable with hexagonal module boundaries

## Status
accepted

## Date
2026-09-11

## Context
QuickNotes must serve 200 DAU (growing, unproven) with one engineer today and
a second in six months. Scenario pressure: Q4 (ACL changes confined to one
module in ≤ 1 day) demands real boundaries; the ops constraint (one engineer,
no Kubernetes) forbids multi-service overhead. Q3/Q1 are satisfied comfortably
by a single well-indexed Postgres instance.

## Options Considered
### Option A — Layered monolith (controllers/services/repositories)
Fastest to first feature; every developer knows the shape.
- Pros: minimal ceremony; simplest debugging (call stacks); fastest onboarding.
- Cons: the layer convention erodes without enforcement (see Meridian case);
  ACL logic tends to leak into handlers, directly threatening Q4.
- Rejected because: Q4's one-day/one-module guarantee depends on a boundary
  that layering does not structurally protect.

### Option B — Two services (Notes API + Search service)
Cleanest failure isolation for Search; independent scaling.
- Pros: search indexing cannot starve request threads; clean blast radius.
- Cons: second deployment pipeline, second on-call surface, network contract
  to maintain — all for a component that is *survivable* when it fails (Q5/Q2
  semantics). Violates the one-extra-service budget before any real scale.
- Rejected because: operational cost exceeds the benefit at 200 DAU; the
  extraction path stays open (see Decision).

### Option C — Hexagonal modular monolith (chosen)
One deployable; Notes/Access/Search as in-process modules behind interfaces.
- Pros: real boundaries (module-boundary test in CI); testing without
  infrastructure via ports; Search extraction later is bounded.
- Cons: interface + mapping boilerplate up front; boundary discipline must be
  enforced by a test, not convention.

## Decision
We will build QuickNotes as a single deployable with three modules (Notes,
Access, Search) communicating only through interfaces, with a CI
module-boundary test enforcing import rules.

## Consequences
Becomes easier: one pipeline, one datastore, one on-call surface; unit testing
through in-memory port doubles.
Becomes harder: up-front interface design; in-process event dispatch must be
replaced by a broker if extraction happens.
New obligations: maintain the module-boundary test; keep Search's port free of
Postgres-FTS-specific types.
Revisit trigger: extract Search to its own process if indexing CPU starves
request threads (p99 request latency > 800 ms attributable to indexing) or a
second team forms.

## Links
- relates-to: ADR-0002 (Search port must stay implementation-agnostic)
```

---

## Artifact 4 — ADR-0002 (full text)

```markdown
# ADR-0002: Use Postgres full-text search instead of a dedicated search engine

## Status
accepted

## Date
2026-09-11

## Context
Q2 requires full-text search over note bodies with p95 < 500 ms at up to
50k notes/user, and index lag ≤ 10 s. Q3-style survivability: search may be
briefly unavailable without harming notes CRUD. Constraints: budget for at
most one additional managed service (preferred: zero), one engineer.

## Options Considered
### Option A — Managed dedicated search service
Purpose-built relevance, faceting, scale headroom.
- Pros: proven at large corpus; rich ranking features.
- Cons: second managed dependency (exceeds budget), another failure mode and
  auth surface, eventual-consistency plumbing to build by hand.
- Rejected because: operational and budget cost for a corpus that Postgres
  FTS demonstrably covers at our scale.

### Option B — Postgres FTS over a maintained tsvector column + GIN index
(chosen)
- Pros: zero new infrastructure; refresh is transactional with the note write;
  backups, failover, and auth inherited from Postgres.
- Cons: ranking quality below a dedicated engine; tsvector triggers add write
  latency (~measured: negligible at our write volume); corpus growth beyond
  ~1M notes will need re-evaluation.

## Decision
We will implement search as Postgres full-text search (tsvector column,
GIN index, trigger-maintained) inside the Notes module's database, exposed
through the Search module's `NoteSearch` port.

## Consequences
Becomes easier: operations (one datastore); consistency (same-transaction
refresh); recovery (index is derivable, no separate rebuild pipeline).
Becomes harder: advanced relevance (faceting, typo tolerance) is out of reach;
the tsvector trigger couples write latency to index maintenance.
New obligations: monitor search p95 and index build time; keep the
`NoteSearch` port contract free of Postgres types.
Revisit trigger: search p95 > 500 ms at p95 load, or query planning time >
50 ms, for two consecutive weeks → extract Search (per ADR-0001) onto a
dedicated engine, backfilling from `notes`.

## Links
- relates-to: ADR-0001 (module boundaries define the extraction path)
```

---

## Artifact 5 — Review findings log (40-point checklist)

| Point | Severity | Finding | Disposition |
|---|---|---|---|
| R-22 | Major | Consistency model was implied, never stated: does share revocation take effect immediately? | **Fixed:** ACL checked at read time via `AccessPolicy`; revocation effective on next read (Q6). Recorded in overview §7. |
| R-31 | Major | Search module's failure behavior undefined. | **Fixed:** search requests return 503-with-retryable during index unavailability; notes CRUD unaffected. Recorded in overview §8 and ADR-0002 consequences. |
| R-26 | Major | `GET /v1/notes` had no stated page size cap. | **Fixed:** default 50, max 200, cursor pagination. Recorded in interface section. |
| R-36 | Minor | ADR-0001 claimed "easier testing" without naming a mechanism. | **Fixed:** rewritten to name in-memory port doubles as the mechanism. |
| R-30 | Minor | Versioning policy existed as a convention, not a record. | **Tracked:** one-line policy added to overview §6 (path versioning, additive-only within a major); full ADR deferred until a breaking change forces the question. |
| R-33 | Minor | In-process event dispatch had no backpressure note (fan-out to Search could queue unboundedly under write bursts). | **Accepted:** write volume is human-scale; bounded in-memory queue with drop-oldest + lag alarm. Rationale recorded in ADR-0002 consequences. |

Blockers: none. Review completed in one 75-minute pass; two findings were found only when checking documents against each other (scenario Q6 vs. the interface section), which is why the cross-check comes before design critique.

---

## What this example demonstrates

1. **The scenario table did the arguing.** Every contested point (services vs. modules, dedicated search vs. FTS) resolved by pointing at a scenario row — not by seniority.
2. **Two ADRs were enough.** The style choice and the search choice are the decisions with real reversal costs; everything else (pagination caps, error shape) is contract detail that does not need a record.
3. **The review found real holes** — revocation timing, search failure behavior, page caps — none of which the design's author could see, because authors cannot read their own documents as a stranger does.
4. **The revisit triggers make the design honest.** Every acceptance includes the condition under which it stops being right; that is what makes the ADRs living rather than memorial.