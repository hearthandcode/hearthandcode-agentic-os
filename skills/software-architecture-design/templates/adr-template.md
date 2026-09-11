# ADR-{{number}}: {{imperative title stating the decision}}

> Copy this template to `docs/adr/NNNN-<slug>.md` and replace every `{{placeholder}}`.
> One decision per ADR. Delete this instruction block before saving.

## Status

`proposed` | `accepted` | `superseded-by-ADR-{{number}}` | `rejected`

## Date

{{YYYY-MM-DD}}

## Context

{{What forces are in play? Requirements, constraints, current state. Write for a
reader with no memory of the project: they should understand why a decision was
needed at all. Name the quality-attribute scenarios that put pressure on this
decision (e.g. "Q3: database failover under 5 minutes"). 2-6 sentences.}}

{{If this ADR backfills a decision made earlier, say so here and mark the
arguments as reconstructed.}}

## Options Considered

### Option A — {{name}}

{{One-paragraph description, then the strongest argument FOR it. Steel-man it;
the record is worthless if rejected options are strawmen.}}

- **Pros:** {{concrete benefits, tied to scenarios}}
- **Cons:** {{concrete costs, tied to scenarios or operations}}
- **Rejected because:** {{the argument that actually killed it — be specific
  enough that a reader could re-run this decision if the cons stop applying}}

### Option B — {{name}}

{{Same shape as Option A.}}

### Option C — {{name}} *(optional)*

{{Same shape. Include any option rejected for non-technical reasons (politics,
budget, mandate) — those arguments are the ones future teams will need.}}

## Decision

{{One imperative sentence: "We will X." If this cannot be one sentence, split
the ADR.}}

## Consequences

**Becomes easier:** {{what this unlocks or simplifies}}

**Becomes harder:** {{what this costs — every decision has a cost; an ADR that
lists only benefits will be distrusted}}

**New obligations:** {{what must now be maintained, measured, or documented}}

**Revisit trigger:** {{the observable, measurable condition under which this
decision should be re-examined — e.g. "if search p95 exceeds 500 ms for two
consecutive weeks" or "if a second team starts writing to notes tables." A
decision without a trigger reads as eternal, and none are.}}

## Links

- `supersedes:` ADR-{{number}} *(or remove)*
- `amends:` ADR-{{number}} *(or remove)*
- `relates-to:` ADR-{{number}}, {{doc path}} *(or remove)*

---

### Completed example (content sketch — full text lives in examples/worked-architecture-design.md)

```markdown
# ADR-0002: Use Postgres full-text search instead of a dedicated search engine

## Status
accepted

## Date
2026-09-11

## Context
QuickNotes needs full-text search across note bodies a user can access
(scenario Q2: p95 < 500 ms up to 50k notes/user). Constraints: one engineer,
budget for at most one additional managed service, no Kubernetes. Search is
survivable if briefly unavailable (scenario Q5 semantics).

## Options Considered
### Option A — Managed dedicated search service (e.g. hosted Elasticsearch)
Excellent relevance tuning and scale headroom.
- Pros: battle-tested FTS, faceting, worst-case scale covered.
- Cons: second managed dependency to operate and pay for; another failure
  mode; API surface to learn — exceeds our budget cap of one extra service.
- Rejected because: operational cost for a one-engineer team at 200 DAU.

### Option B — Postgres FTS over a materialized `notes_search` view
Native to our existing primary datastore; tsvector ranking adequate for
keyword search over prose notes.
- Pros: zero new infrastructure; transactional refresh; backup/recovery
  inherited from Postgres.
- Cons: ranking quality below a purpose-built engine at scale; index build
  time grows with corpus.
- Rejected: (not rejected — chosen).

## Decision
We will implement search as Postgres full-text search over a materialized
view maintained inside the same database, behind the Search module's port.

## Consequences
Becomes easier: operations (one datastore); consistency (view refresh is
transactional).
Becomes harder: relevance tuning limited; extraction to a dedicated engine
later requires a backfill.
New obligations: monitor index build time and search p95.
Revisit trigger: search p95 > 500 ms at p95 load, or index build > 5 minutes,
for two consecutive weeks → extract Search behind its existing port.

## Links
- relates-to: ADR-0001 (module boundaries define the Search port)
```
