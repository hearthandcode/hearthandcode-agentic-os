# Architecture Review Checklist — 40 Points

Run this checklist against a design (an architecture overview plus its ADRs) before code is written against it, and against a running system when reviewing its evolution. Check every point; a skipped point is where findings hide. Mark each ✓ (met), ✗ (violated), or N/A (with one-line justification — "N/A" without a reason is a finding).

## A. Scenario coverage (points 1-8)

1. ✓/✗ — Every quality requirement exists as a six-part scenario with a response measure.
2. — The top 6-10 scenarios are prioritized by cost of failure, and the ranking is written down.
3. — Every scenario maps to at least one named design mechanism (the "mechanism" column is filled).
4. — Every scenario names a verification method (test, load run, drill) — nothing is verified by hope.
5. — Sacrificed qualities are listed explicitly with a revisit trigger for each.
6. — Percentiles and load assumptions are stated for performance scenarios (no bare "fast").
7. — Modifiability scenarios name the actual near-term change they protect ("ACL change in one module in a day").
8. — The scenario table was re-derived after the latest major product shift (new client, growth, compliance).

## B. Structure and boundaries (points 9-16)

9. — Every component passes the one-sentence purpose test (no "and" in the purpose).
10. — Every component passes the tell-nothing test (interns can be rewritten without caller changes).
11. — Component names are responsibility nouns, not grab-bags ("NoteManager" is a finding).
12. — Dependencies between components point one direction and are drawn as they really exist in code.
13. — No content coupling: no component reaches into another's tables or internal structs.
14. — No temporal coupling without an explicit, documented tolerance (ordering/lag assumptions stated).
15. — The style choice (layered / hexagonal / event-driven / microkernel) is recorded with rejected options.
16. — Each boundary change is justified by a scenario, and speculative extension points are flagged.

## C. Data and consistency (points 17-24)

17. — Every entity has exactly one owning component; a table lists entity → owner.
18. — Two-writer cases are resolved: commands-through-owner or events, not shared write access.
19. — Cardinality and uniqueness constraints are enforced in the schema, not only application code.
20. — Every derived copy (cache, index, materialized view) names its refresh mechanism and rebuild path.
21. — Denormalizations list the read they serve, the refresh mechanism, and the drift check.
22. — The consistency model per boundary is stated (strong / eventual) and matches what users are promised.
23. — Retention, soft-delete, and audit columns exist where deletion is undoable or auditable.
24. — The migration story exists for the riskiest schema change on the roadmap (not for the ideal future — the next one).

## D. Interfaces (points 25-30)

25. — Every operation has a named actor and an authorization rule.
26. — Every list operation paginates with a documented maximum page size.
27. — Idempotency is defined per mutating operation (retry behavior stated).
28. — The error contract is uniform: stable codes, retryable flag, no internal details leaked.
29. — The 404-vs-403 information-disclosure policy is decided and applied uniformly.
30. — The versioning policy and deprecation workflow are recorded (an ADR, not a convention).

## E. Risk and failure (points 31-35)

31. — For each component: "what does its failure look like?" has a written answer (timeout, retry, degrade, halt).
32. — Failure of survivable components does not take down the core paths (stated per component).
33. — Retry/queue behavior cannot form a retry storm (backoff, caps, idempotency).
34. — The worst realistic failure (data loss, security breach) has a recovery and audit path.
35. — Operational maturity constraints are honored (no machinery the team cannot operate).

## F. Decisions and review hygiene (points 36-40)

36. — Every consequential decision is an ADR with options considered and consequences.
37. — Every ADR has a revisit trigger that is measurable and dated.
38. — ADRs link to each other (supersedes / amends / relates-to); no orphan decisions.
39. — The overview can be turned into a diagram in ten minutes by a reader who has never seen the system.
40. — Prior review findings each have a disposition: fixed, accepted-with-rationale, or tracked as a decision.

## Scoring and disposition

- **Blockers:** any ✗ on points 17, 18, 21, 22, 31, 34 (data ownership, drift, consistency, failure shape, recovery). These unblock nothing until resolved.
- **Majors:** any ✗ on points 1-8, 9-16, 25-30 — unmet scenarios and broken boundaries.
- **Minors:** N/A without justification, missing links, stale tables.

For each finding record: the point number, the evidence (quote the overview/ADR section), and one of three dispositions — **fixed** (change made before sign-off), **accepted** (rationale recorded in the relevant ADR), or **tracked** (converted to an ADR or issue with an owner). A review with dispositions recorded is complete; a review with a score and no dispositions is a formality.

## Running it well

- Run the full list yourself first; a second reviewer then only checks the points you marked ✓ or N/A — fresh eyes on your blind spots, not a duplicate pass.
- Review the *documents against each other* (scenarios vs. mechanisms vs. ADRs) before questioning the design itself; most findings are inconsistencies, not errors.
- Timebox to one pass: 90 minutes for a system of moderate size. Findings degrade past that; note "second pass" items instead of exhausting yourself.
- Re-run points 17-24 and 36-40 quarterly on live systems — data ownership and decision-record drift are the slow leaks that turn architectures into accidents.