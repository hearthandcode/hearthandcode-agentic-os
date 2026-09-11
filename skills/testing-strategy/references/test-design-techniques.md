# Test Design Techniques — Choosing Cases That Earn Their Keep

Random test-writing finds random bugs. Design techniques find the *classes* of bugs that
live in a behavior's structure: at edges, in combinations, and in illegal states. This
reference is the selection guide: given a behavior's shape, which technique produces the
smallest case set with the highest defect yield.

## The technique table

| Technique | Behavior shape it fits | What it finds |
|---|---|---|
| Equivalence partitioning | Any input with natural classes (types, ranges, formats) | One representative per class covers the whole class |
| Boundary value analysis | Ranges, limits, off-by-one territory | The ±1 bugs at edges of valid ranges |
| Decision tables | Rules that combine conditions (discounts, permissions, pricing) | Wrong combinations and missed condition pairs |
| State-transition testing | Objects with a lifecycle (order, session, subscription) | Illegal transitions, unreachable states, missing guards |
| Pairwise / combinatorial | Many independent options (config matrices, feature flags) | Interaction bugs without exponential case counts |
| Error guessing | Everything, applied by the experienced | The nulls, empties, duplicates, timeouts nobody specified |
| Property-based testing | Invariants over unbounded inputs (roundtrip, idempotence) | The weird input no human would have typed |

Selection is mechanical: classify each behavior, apply its technique, and only hand-fill
cases that no technique generates.

## Equivalence partitioning

Split the input domain into classes the program treats identically; test one member of
each. Cover the invalid classes too — the negative space is where most defects live.

For `parseQuantity(text) -> int`:

- Valid classes: `1`–`999` (max stock), leading/trailing whitespace variants.
- Invalid classes: empty, non-numeric, negative, zero, `1000+`, `3.5`, unicode digits,
  `1e3`, embedded NUL, a 10,000-character digit string.

Twelve classes, twelve tests, and every future regression in any class is caught by its
representative. Two common mistakes: testing three examples of the same class (wasted
budget) and forgetting that *invalid* classes need expected outputs specified, not just
"should fail."

## Boundary value analysis

Defects cluster at edges: `>=` vs `>`, off-by-one in slices, limits in binary-adjacent
values. For each numeric or size range, test the boundary itself and both neighbors:
`min-1, min, min+1, max-1, max, max+1`. Add the structural extremes: `0`, `1`, empty,
`MAX_INT`, `MAX_INT+1`, and for money, cents not dollars (see the ShopPay example —
`0.07` vs `0.08` rounding is a boundary case in disguise).

Pair boundaries: a window is `(start-1,start)`, `(start,start)`, `(start,end)`,
`(end,end+1)`, and the zero-width window.

## Decision tables

For behavior driven by combinations of conditions, build the table explicitly:

| Rule | cart ≥ $50 | member | coupon valid | → discount |
|---|---|---|---|---|
| 1 | N | – | – | none |
| 2 | Y | N | N | 5% |
| 3 | Y | Y | N | 10% |
| 4 | Y | – | Y | best-of(10%, coupon) |
| 5 | Y | Y | Y | best-of(10%, coupon) — state the tie-break |

Rules with "–" are don't-care columns that collapse case counts. The table is also the
spec review: a rule nobody can explain is a requirements bug found before a line of test
code exists.

## State-transition testing

For lifecycle-bearing objects, draw states and legal transitions, then test three things:

1. **Every legal transition** fires correctly and produces the documented side effects.
2. **Every illegal transition** is rejected with the specified error, not silently
   accepted. (The transition matrix's empty cells are the test list.)
3. **Idempotence and re-entry**: replaying an event twice, events arriving out of order,
   and resume-after-crash at each state.

A payment order (`draft → authorized → captured → refunded`) with a `void` path is a
five-state machine with ~20 legal transitions and dozens of illegal ones — this is where
double-refund and capture-after-void bugs live, and no amount of happy-path testing
touches them.

## Pairwise testing

When N independent axes multiply into thousands of combinations (browsers × locales ×
tiers × flags), pairwise covers every *pair* of values in a fraction of the full product.
Use it when the full cross product exceeds ~50 cases and you have no defect history
pointing at specific interactions. Do not use it where three-way interactions are known
to matter — pairwise is a budget tool, not a completeness claim.

## Error guessing and the defect-history list

Maintain the team's list of recurring bug shapes: null, empty string, empty collection,
duplicate submit, unicode confusables, timezone edges (DST, midnight, leap year),
concurrent double-click, clock skew, disk full, and cancelled-mid-request. Each release,
sweep the changed surface against the list. This is unglamorous and consistently
high-yield.

## Risk-based weighting

You will not have budget for every technique everywhere. Weight behaviors by
(consequence of failure) × (likelihood of change):

- Consequence: money, personal data, safety, data-destroying operations get full
  technique treatment; cosmetic surfaces get partitioning plus error guessing.
- Likelihood: complex conditionals, new code, and historically buggy files get more
  cases; simple pass-through code gets the minimum.

Record the weighting in the plan so skipping a technique is a decision, not an accident.

## Documenting provenance in the plan

Each planned case group should carry its origin: `EP` (partitioning), `BVA`, `DT`
(decision table), `ST` (state machine), `PW`, `EG`, or `PROP`. Provenance turns review
into checking — a reviewer asks "which classes did EP produce, and which are missing?"
instead of "do these tests feel like enough?" It also makes deletions honest: removing a
case must name the class it covered or the class is now untested.

## Anti-patterns

- **Line-coverage-driven cases.** Cases reverse-engineered from code find code bugs the
  code's author already suspected; techniques find spec gaps.
- **Copying the last production bug once.** One regression test per incident, without
  generalizing to its class, is how suites grow to thousands of tests while staying blind.
- **Technique theater.** Applying decision tables to a one-condition boolean is ceremony.
  Match the effort of the technique to the structure of the behavior.