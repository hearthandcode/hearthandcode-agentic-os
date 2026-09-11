# ADRs: Architecture Decision Records — Format, Lifecycle, Linking

An ADR is a short document that captures one consequential architecture decision: the context that forced it, the options considered, the choice made, and its consequences. ADRs exist because decisions decay faster than code — six months later nobody remembers why the search index was a materialized view instead of a service, and the cost of finding out the hard way is a rewrite. ADRs are written by whoever made the decision, at decision time, and are immutable once accepted.

## When a decision deserves an ADR

Not every choice needs a record. Write an ADR when the decision is:

- **Hard to reverse** — data ownership, a persistence engine, a public interface contract, a message topology.
- **Visible to more than one person** — anyone else will build against it or operate it.
- **Costly to relitigate** — teams waste the most time re-arguing settled choices with no record of the original argument.

A library choice that can be swapped in an afternoon does not need an ADR; a *policy* about when to choose libraries might.

## Format

Use a fixed structure so readers can skim. The canonical sections:

```markdown
# ADR-NNNN: <imperative title, e.g. "Use Postgres full-text search over a dedicated engine">

## Status
accepted | proposed | superseded-by-ADR-XXXX | rejected

## Date
YYYY-MM-DD

## Context
What forces are in play: requirements, constraints, current state. Written so a
reader with no memory of the project understands why a decision was needed at all.

## Options Considered
Each option gets: a name, a one-paragraph description, and the strongest argument
for it. Include the option you rejected for political reasons — that is exactly
the argument worth preserving.

## Decision
One sentence, imperative. "We will X." If this cannot be one sentence, it is
several decisions — split the ADR.

## Consequences
What becomes easier, what becomes harder, what new obligations appear. Include
the revisit trigger: the observable condition under which this decision should
be re-examined ("if search p95 exceeds 500 ms..."). A decision without a revisit
trigger reads as eternal, and no architectural decision is eternal.

## Links
supersedes: ADR-NNNN | amends: ADR-NNNN | relates-to: ADR-NNNN, doc/path.md
```

Keep ADRs to one page. If it needs two, you are recording a design document, not a decision — link the design doc instead.

## The title discipline

Titles are imperative and specific: "Use Postgres full-text search over a dedicated engine," not "Search." Readers scanning a list of forty ADRs will see only titles. A title that states the choice lets a reader decide relevance without opening the file.

## Numbering

Sequential, zero-padded, never reused: ADR-0001, ADR-0002. Rejected or superseded numbers are retired, not recycled — the number is the permanent address of the argument. Gaps in the sequence are acceptable (an ADR withdrawn before acceptance); duplicates and reused numbers are not.

## Lifecycle

1. **Proposed** — the ADR is drafted; anyone may add options or attack arguments. The proposed state is where contention belongs.
2. **Accepted** — the deciding authority (team consensus, tech lead, architect — pick one and be consistent) accepts it. Accepted ADRs are immutable: edits go to a new ADR.
3. **Superseded** — a new ADR replaces this one. The old ADR's status line changes *only* to point at its successor; nothing else in the body is touched.
4. **Rejected** — the decision went the other way. Keep the document: rejected ADRs are the cheapest way to prevent re-proposing a settled question, and sometimes the context changes and the rejection becomes the seed of the new ADR.
5. **Amended (via new ADR)** — a small change to an accepted decision does not edit it; a new ADR states "amends ADR-NNNN: [the delta]."

## Linking

Links are what turn a folder of ADRs into a decision graph:

- **supersedes** — this ADR replaces that one. Every superseded ADR gets the reverse link in its status.
- **amends** — this ADR modifies part of that one without replacing it.
- **relates-to** — shared context, shared trade-off, or a decision that constrains this one.
- **requires** — this ADR is only valid if that one is accepted.

When you write an ADR, always search existing ADRs for related decisions. Linking is how a reader follows a thread ("what did we decide about data ownership overall?") instead of reading the folder alphabetically.

## Where ADRs live

Next to the code they govern, in version control, reviewed like code. A wiki page outside review flow will drift; a file in the repository gets updated in the same pull request that changes the architecture. A common layout: `docs/adr/0001-use-postgres-fts.md` with an index table (`adr/index.md`) listing number, title, status.

## Writing quality bar

- **Context before conclusion.** The reader must be able to disagree with the decision but still understand it. If the context section only supports the chosen option, it is advocacy, not context.
- **Steel-man the rejected options.** "Option B was bad" is worthless. "Option B was better for Q4 modifiability, but failed our one-engineer operations constraint" is a record that survives.
- **Consequences include costs.** An ADR whose consequences section lists only benefits will be distrusted — correctly.
- **Revisit triggers are measurable.** "If it gets slow" is a trigger nobody will pull. "If p95 exceeds 500 ms for two consecutive weeks" is.
- **One decision per ADR.** "Use Postgres and adopt FTS" is two ADRs; splitting them means one can be superseded without touching the other.

## Anti-patterns

- **The eternal ADR.** No revisit trigger, no supersession ever. Architecture decisions have shelf lives; the record should say what the shelf life is.
- **The journal ADR.** Entries written months after the fact, reconstructing arguments nobody remembers. Record at decision time; if backfilling, say so in the context and mark the arguments as reconstructed.
- **The essay ADR.** Two thousand words of system context with the actual decision in paragraph nine. If the reader cannot find the decision in fifteen seconds, restructure.
- **The unlinked ADR.** No supersession, amendment, or relation links — a folder of disconnected monoliths. When writing a new ADR, link it to its neighbors.
- **The rewritten ADR.** An accepted ADR edited in place to reflect a changed decision. This destroys the decision history, which was the point. Supersede instead.
- **The ADR that records the outcome, not the argument.** "We chose X" with no options considered. The argument is the asset; the outcome is the easy part.
