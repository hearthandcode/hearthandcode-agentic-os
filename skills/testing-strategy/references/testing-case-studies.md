# Testing Case Studies — Four Strategies Applied to Real Shapes

Four miniature case studies, each showing the strategy decision, not just the test
list: what the module is, what the constraints forced, where the budget went, and what
the plan got wrong first. Read them as calibrations for the workflow's judgment calls.

## Case 1 — Legacy CRUD service: the ice-cream cone recovery

**Shape:** A five-year-old order-management service, 40k lines, no unit tests, 900+
Selenium E2E tests, CI measured in hours, three flakes per green build. The team's
instinct: "delete the E2E tests, write unit tests."

**What the strategy actually did:**

- Measured first: the 900 E2E tests covered 11 user flows with heavy overlap; the top
  20 tests covered ~80% of the exercised surface. They were not 900 units of safety,
  they were 11 flows recorded redundantly.
- Freed a seam per sprint: extracted the repository interface, injected a clock, broke
  the config singleton. No test plan can precede this work; it *is* this work.
- Downward migration: each E2E test was mapped to the earliest seam that could hold its
  assertions. Business rules moved to unit tests; persistence moved to repository tests
  against a containerized database; the cross-flow 20 stayed E2E.
- Deleted aggressively: 900 → 32 E2E tests over three quarters. Every deletion was
  paired with the lower-level tests that replaced it, checked by keeping a
  migration ledger.

**Result:** CI 3.5 h → 11 min; escaped-defect rate unchanged (the safety was real);
flakes from three per build to one per fortnight.

**The mistake in the first draft of the plan:** targeting 80% line coverage as the
goal. It produced assertion-free tests of getters. The revised plan targeted *behavior
coverage*: every rule in the discount module named and tested. Coverage was a symptom
metric, not the goal.

**Lesson:** legacy suites are migrated by seam-and-migrate, not by parity. And a
numeric coverage target optimizes for the number.

## Case 2 — Payments module (the ShopPay shape): zero tests, high stakes

**Shape:** A checkout module — cart, pricing, payment authorization, capture, refund
— with zero tests, one integration partner (a PSP), and direct money consequences.

**What the strategy actually did:**

- Started from the state machine, not from the code: `draft → authorized → captured →
  refunded/voided`. Illegal transitions (double capture, refund after void) got state
  tests before any happy path was written, because those are the incidents with
  financial liability attached.
- Decision table for pricing before cases: card fees × member tier × coupon ×
  rounding. The table itself exposed a spec ambiguity (coupon vs member discount
  tie-break) — a requirements bug found before a test existed.
- Boundaries in cents everywhere; a boundary-value sweep at rounding edges found the
  classic 0.005 rounding disagreement between the service and the PSP sandbox.
- The PSP client got a stub-peer suite (timeout, 5xx, malformed body, double-charge
  retry) plus one contract test replaying the PSP's recorded sandbox responses.
- One stateful property: "no sequence of legal commands leaves an order both captured
  and voided." It found a race on the first night.
- E2E capped at the five money flows, run nightly against a PSP sandbox with seeded
  test accounts, never against production keys.

**The mistake:** the first plan had no reconciliation story. It tested the module's
behavior in isolation and nothing verified the module's totals against the PSP's
settlement report — a daily compare job became part of the plan (an integration test
plus a production telemetry check, not more E2E).

**Lesson:** for money, the highest-value artifacts are the state machine's illegal
transitions and one reconciliation check — not broader happy-path coverage.

## Case 3 — Event-driven pipeline: integration-weighted by design

**Shape:** Order events flow: ingest → validate → enrich → publish. Little pure logic;
the behavior is the contracts between stages and delivery guarantees.

**What the strategy actually did:**

- Honeycomb allocation: ~40/50/10. Unit tests only for validation rules and the enrich
  transforms; the fat middle tested each stage against real containers (broker,
  datastore); a handful of E2E for the full order flow.
- Contract tests dominated: each stage's consumed schema recorded and replayed against
  producers. A producer-side red build blocks when it would break a downstream consumer.
- At-least-once reality made idempotence the most-tested property: duplicate delivery,
  out-of-order arrival, replay after consumer crash — each a named scenario.
- Poison-pill and DLQ behavior tested explicitly; the "message that fails forever"
  case had zero coverage before and caused the worst production week in the team's
  history.

**The mistake:** early stage tests asserted on message *count* after a fixed sleep —
classic timing flake. Replaced with broker-backed assertions (read-until-seen with
bounded deadline); flakes went to zero and the tests got faster.

**Lesson:** in pipelines, the schema and delivery semantics are the product; test
duplicates and poison pills first, throughput never (that is a load-test concern).

## Case 4 — Frontend checkout flow: thin E2E, component middle

**Shape:** A React checkout with heavy client-side logic (address validation, promo
codes, 3DS redirects) and a backend API.

**What the strategy actually did:**

- Client logic (promo eligibility, address normalization, price display math) moved
  out of components into pure modules — tested at unit level, ~65% of the suite.
- Component tests (rendering library's testing tools) for each checkout step: states,
  error display, disabled-button logic — ~30%.
- E2E capped at five journeys (guest checkout, member checkout, declined card,
  3DS challenge, promo-apply) — ~5%. They run in the nightly, not the merge gate, and
  each traces to a named support-ticket class.
- Network layer mocked at the API client boundary for component tests; the real API
  contract is covered by the backend's contract tests, not duplicated here.

**The mistake:** the first version mocked the API at the `fetch` level, which made
component tests both brittle and lying (they encoded URL and response-shape guesses).
Moving the mock to the API client module — the seam the code owns — fixed both, and is
the general rule: mock at the seam you own, nearest to the consumer.

**Lesson:** frontends deserve pyramids too; the "E2E-only" instinct for UI comes from
logic that has not yet been extracted to testable modules.

## Cross-case patterns

- Every strategy began with **measurement or modeling**, not test-writing: defect
  history, flow overlap, state machines, contract surfaces.
- Every first-draft mistake was a **metric or a shortcut**: coverage numbers, count
  assertions, fetch-level mocks — all of them optimized the visible number instead of
  the behavior.
- The durable wins were **seams and contracts**: repository interfaces, injected
  clocks, recorded schemas, client-boundary mocks. Tests decay; seams keep the next
  decade of tests writable.
- Money and delivery semantics got the specialty techniques (stateful properties,
  idempotence cases, reconciliation checks) — the techniques with the highest yield
  per line in exactly the places where failure costs real money.