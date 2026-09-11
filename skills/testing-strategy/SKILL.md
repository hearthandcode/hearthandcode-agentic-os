---
name: testing-strategy
description: >
  Load this skill when you are planning what tests a module or system needs —
  designing a test plan from zero, rescuing a suite that has grown slow, flaky,
  or inverted, allocating tests across the pyramid, choosing test-design
  techniques, or designing CI test stages and merge gates. It produces a
  risk-based test plan with a level allocation, technique-derived case catalog,
  test-data decisions, and a staged CI design. It does not review individual
  diffs (use code-review) or design component architecture (use
  software-architecture-design), though it consumes seam decisions from both.
---

# testing-strategy

## 01 — Purpose

A test suite is not a pile of tests; it is a budget spent against risk. Every test
costs something to write, to keep passing, and to wait for in CI — and every test pays
something back only if it catches a bug you would otherwise have shipped. Most suites
fail economically before they fail technically: they spend heavily on slow, redundant
end-to-end journeys that catch little, while the behavior classes that actually cause
incidents — edges, illegal state transitions, contract drift, duplicate submissions —
have no test at all.

This skill turns test planning from an instinct ("we should have more coverage") into a
repeatable procedure with a quality floor. It walks one complete strategy pass over a
module or system: establish the risk profile, measure what exists, inventory the
behaviors, allocate tests across levels, derive cases from design techniques rather than
from reading the code, decide the test-data policy, and design the CI stages that will
run the suite — ending with a plan a reviewer can check and a team can execute.

The pass is designed to be honest about cost. A plan that demands more effort than the
risk justifies will be ignored; a plan that under-tests a money path is malpractice. The
allocation, techniques, and gates exist to make that trade explicit, recorded, and
reviewable — so that what is *not* tested is a decision, never an accident.

**Three outcomes this skill owns:**

1. **A test plan that survives review.**
   - Every high-risk behavior has a named technique, a level, and derived cases; every
     gap in the plan is listed as a deferred decision with an owner, not left silent.
   - The allocation matches the module's actual shape — rule-dense cores get pyramids,
     gluing-heavy services get honeycombs — and deviations are justified in one line.
   - A reviewer can verify coverage of behavior classes, not eyeball a coverage
     percentage and hope.
2. **A case catalog with provenance.**
   - Cases come from equivalence partitioning, boundary analysis, decision tables,
     state machines, and properties — so review means "which class is missing?", not
     "do these feel like enough?"
   - The catalog is small enough to maintain: every case names the class it covers, so
     deletions are honest and redundancy is visible.
3. **A CI design people trust.**
   - Stage budgets, gate strengths, and a flake policy with an owner, so green means
     mergeable and red means stopped — not re-run-and-hope.
   - Feedback time is treated as the product it is: the commit stage stays fast enough
     that developers never context-switch waiting.

- The skill assumes a practitioner who writes tests but may never have designed a suite.
- It teaches the craft: how to read a module's shape, which technique fits which
  behavior, where a stub crosses the line into a lie, and why the merge gate is a
  contract that dies the first time you hit retry on a flake.
- It is stack-agnostic: pytest, JUnit, vitest, go test, testcontainers, Pact are named
  as examples of patterns, not requirements.
- It works for a greenfield module with zero tests, for a feature slice in a mature
  suite, and for a legacy rescue where the existing suite is the problem.
- The artifacts interlock: the behavior inventory justifies the allocation, the
  allocation constrains the case catalog, the catalog determines CI stage contents, and
  the data policy underwrites all of it — skip a layer and the later layers inherit the
  gap.
- What you should NOT expect: a tool that generates your tests. The skill structures
  judgment; the judgment stays yours. What you SHOULD expect: the module-analysis step
  to find real spec bugs before you write a single test — that is the pass working.

## 02 — When to Use / When Not to Use

### Use this skill when:

1. **You are starting a module or feature with no tests.**
   - Greenfield code is the cheapest moment to design the suite; the plan costs a day
     and repays it the first week.
   - Typical first artifacts: the behavior inventory, the allocation table, and the
     seam list that makes the plan possible at all.
2. **You are planning tests for an existing system about to change.**
   - New payment flows, a pricing engine, a migration, a new integration partner —
     anything where the change carries consequence and the current suite is thin or
     absent in exactly that area.
3. **Your suite is slow, flaky, or inverted.**
   - Hours-long CI, ice-cream-cone test shapes, red builds everyone retries: the plan
     includes a rescue path — measurement, seam work, downward migration, and a flake
     policy.
4. **You are designing or repairing CI test stages.**
   - What blocks a merge, what runs nightly, what budgets each stage gets, how flaky
     tests are quarantined and re-entered.
5. **You are deciding what NOT to test.**
   - Budgets are finite; the plan makes the sacrifice list explicit and reviewable,
     which is the difference between a decision and a hole.
6. **You need to review someone else's test plan.**
   - §05 and the template's review checklist give the reviewer a mechanical check
     instead of a taste argument.

### Do NOT use this skill when:

1. **You are reviewing a specific diff or pull request.**
   - Review asks "is this behavior tested?"; it does not design the suite. That is
     `code-review`, which hands test-plan gaps back to this skill.
2. **You are deciding how code should be structured so it can be tested.**
   - Seams, boundaries, and dependency injection belong to `software-architecture-design`.
     This skill names the seams a plan requires; it does not design them.
3. **You are writing an individual test.**
   - The unit and integration references supply patterns for that; the strategy pass is
     for the suite and its pipeline, not the next assertion.
4. **You are doing performance or load testing.**
   - Benchmarks, soak tests, and capacity planning are a separate discipline with
     separate budgets. This skill sets the boundary (slow integration tests are failing
     tests, not benchmarks) and stops there.
5. **You are setting up exploratory or manual QA processes.**
   - Exploratory testing deserves its own charter discipline; this skill only reserves
     a line in the plan for it and says when it runs.

## 03 — Inputs and Outputs

### Inputs

You should have at least ONE of these before starting:

- **A module or feature boundary.** The code, its owner, and its scope. A plan without
  a boundary becomes a manifesto; pick the repo path and stick to it.
- **The consequence statement.** What happens when this code is wrong — money, data,
  safety, trust, or support tickets. This single fact drives the entire allocation.
- **Requirement sources.** Specs, API contracts, tickets, the actual code. Techniques
  operate on specified behavior; where the spec is silent, the plan records the gap.
- **The current test state.** Existing suites and their levels, runtime, flake history,
  CI configuration. Planning greenfield when brownfield exists produces a fantasy.
- **Constraints.** CI budget, sandbox availability, compliance rules on data use,
  team conventions for runners and layout.

### What good inputs look like

- A module small enough to hold in one head: a service, a package, a feature slice.
  An empire-wide test strategy is a program, not a pass; start with the riskiest module.
- A consequence statement with a named stakeholder: "a wrong total settles against the
  PSP's books and finance notices within a day" beats "bugs would be bad."
- A spec with at least one worked example per rule — decision tables and boundaries
  need concrete numbers to derive from.
- CI history: last month's runs, their durations, their flake rate. If CI does not
  exist, that is the first finding.

### Outputs

1. **A test plan** (`templates/test-plan-template.md`) — the durable artifact: context
   and quality goals, module analysis with behavior inventory, level allocation, case
   catalog with provenance, data policy, CI stage design, exit criteria.
2. **A behavior inventory** — the table of behaviors with risk, technique, and level.
   It doubles as the spec-review artifact: ambiguities found here are requirements bugs
   found at their cheapest.
3. **A CI stage design** — which stages exist, what each contains, budgets, and gate
   strength, with the flake policy attached.
4. **A seam list** — the injectable dependencies the plan requires, handed to
   `software-architecture-design` if they do not yet exist.
5. **Handoffs:** structural findings go to `software-architecture-design`; per-diff
   test questions stay with `code-review`; the plan is the boundary between them.

## 04 — Workflow

A complete pass has ten steps. Steps 1-4 are analysis and shape the whole plan; 5-7
produce the plan's substance; 8 reviews it; 9-10 execute and keep it alive. Skipping
steps 1-4 to write tests directly is how suites grow big and blind.

### Step 1 — Establish context and risk
**Reference:** `references/testing-pyramid.md`

- Write the consequence statement first: what breaks when this module is wrong, who
  notices, how fast, at what cost. Money and personal data get the full treatment;
  cosmetic surfaces get a fraction of the budget.
- Identify the stakeholders and their sharpest concern: finance settles daily; support
  dreads the double-refund; the on-call dreads the flaky suite itself.
- Name the quality attributes in priority order — correctness, state integrity,
  contract stability, latency, throughput. The plan optimizes the top two.
- Set the explicit sacrifice list now, at draft: what you will not test and why. A plan
  without a sacrifice list is a wish, not a budget.
- Checkpoint question: "Could I defend this plan's budget from the consequence statement
  alone? If not, the consequence statement is too vague — sharpen it before proceeding."

### Step 2 — Baseline the existing suite
**Reference:** `references/testing-pyramid.md`

- Count tests per level (unit / integration / E2E) by directory or marker. Percentages,
  not vibes.
- Measure per-level wall-clock runtime from CI history. A unit layer over ~10 minutes
  total is a finding, not a fact of life.
- Count skips, retries, and quarantined tests. High counts mean the suite is lying
  about its own health; fix trust before adding tests.
- Read the last ten escaped bugs and note at which level each could have been caught
  cheapest. This defect history is the strongest allocation evidence you will get.
- If the suite is E2E-heavy with no seams, expect the rescue path (§07) rather than a
  plain plan.
- Checkpoint question: "Do I know what exists, what it costs, and what it misses?"

### Step 3 — Inventory behaviors and dependencies
**Reference:** `references/test-design-techniques.md`

- List the behaviors the module owns, one row per rule: source (spec, code, ticket),
  risk, and — later — technique and level. Twenty to forty rows is typical for a
  module; if you have hundreds, your rows are functions, not behaviors.
- Draw state machines for anything with a lifecycle: orders, sessions, subscriptions.
  The empty cells of the transition matrix are your illegal-transition test list.
- Build decision tables where conditions combine: discounts, permissions, pricing,
  feature flags. A rule nobody can explain is a spec bug found before any test exists.
- List external dependencies and mark each owned or third-party — this determines how
  each is faked at each level.
- Note every place behavior depends on time, randomness, or environment; these become
  seam requirements.
- Checkpoint question: "Which spec ambiguities did this inventory expose? Raise them
  now — before any test is written."

### Step 4 — Choose the allocation
**Reference:** `references/testing-pyramid.md`

- Pick the default shape (roughly 70/20/10) and adjust by module type: rule-dense cores
  hold the pyramid; glue-heavy services go honeycomb; pipelines go integration-heavy.
- Cap E2E deliberately: single digits to low dozens, each tracing to a named flow with
  a named consequence. An E2E test you cannot justify in one sentence is a liability.
- Assign each behavior inventory row a level. Money and safety rules get the level
  where they can fail most precisely, which is usually unit — plus one integration
  witness so the wiring is proven, not assumed.
- Budget runtime per level and check the sum against the CI stage budgets in Step 7.
  An allocation that cannot run in the pipeline it needs is a fiction.
- Justify every deviation from the default in one line in the plan.
- Checkpoint question: "Does the shape follow the module's defect history, or the
  team's habit?"

### Step 5 — Derive cases from techniques
**Reference:** `references/test-design-techniques.md`

- For each behavior, apply its technique mechanically: equivalence classes, boundary
  values (±1, empty, max), decision-table rules, state transitions legal and illegal,
  pairwise where combinations multiply, error-guessing sweeps against the team's bug
  list.
- Derive properties where invariants exist: roundtrips for codecs, oracles for
  optimizations, idempotence for handlers, stateful models for state machines.
- Prefer the smallest case set that covers every class; redundancy is maintenance debt,
  not safety.
- Record provenance on every case group: EP, BVA, DT, ST, PW, EG, PROP. Deletion of a
  case must name the class it covered or the class is now untested.
- Sweep the changed surface against the recurring-bug list each release: nulls,
  empties, duplicates, unicode, DST, clock skew.
- Checkpoint question: "For each high-risk behavior, which classes does the catalog
  cover — and which are missing?"

### Step 6 — Decide the test data policy
**Reference:** `references/test-data-management.md`

- Default to builders and factories with schema-valid defaults; tests override
  explicitly, and the override is the test's specification.
- Fix fixture lifecycle: per-test setup, randomizable order, cleanup by rollback or
  ephemeral environments — never by hand-run scripts.
- Golden files only for large stable outputs, reviewed on creation, volatile fields
  normalized; goldens detect change, not correctness.
- The rule on production data is absolute: shape from production, values synthetic.
  Production PII in a test environment is a breach, not a convenience.
- Match realism to level: unit wants none, integration wants schema-valid, performance
  wants production-shaped distributions.
- Checkpoint question: "Where does every byte of test data come from, and could any of
  it embarrass us in an audit?"

### Step 7 — Design the CI stages
**Reference:** `references/ci-test-pipelines.md`

- Lay out the stage ladder: commit stage (unit + affected integration, ≤10 min,
  blocks merge), integration stage (full integration, pre-merge, blocks), nightly
  (E2E, properties, fuzz campaigns — alerts), release smoke (blocks release),
  production synthetics (pages).
- One decision per stage: what does it block? A nightly that blocks merges is
  misplaced; a commit stage that merely alerts does not exist.
- Parallelize and cache deliberately: timing-aware sharding, ephemeral per-worker
  dependencies, cache keys that include lockfile hashes.
- Write the flake policy with the plan: detection, one-day quarantine with owner and
  due date, root-cause fixes, evidence-based re-entry, no blanket retries.
- Define reporting: failures first, trends monthly, escape-rate review — every
  production bug names the level that should have caught it.
- Checkpoint question: "Does green mean mergeable and red mean stopped? If anyone
  remembers the last time they hit retry, the policy is not real."

### Step 8 — Write and review the plan
**Reference:** `templates/test-plan-template.md`

- Fill the template in order; its sections mirror Steps 1-7, and the review checklist
  at the end is the quality bar.
- Review the plan before implementing it: the reviewer checks classes against the
  inventory, not test counts against a feeling.
- Verify every H-risk behavior has a technique, a level, and cases; verify illegal
  transitions are enumerated; verify the data policy has no production-PII path.
- Confirm the sacrifice list is explicit and owned — silent omissions are findings.
- Confirm the seam list: every dependency the plan requires that does not exist yet
  becomes a blocking task with an owner, ahead of test-writing.
- Checkpoint question: "Could a new engineer execute this plan without asking what to
  do first?"

### Step 9 — Implement in slices
**Reference:** `references/unit-testing-patterns.md` · `references/integration-testing-patterns.md`

- Implement by behavior slice, not by level: one behavior's unit cases, its
  integration witness, its property if any — red to green together.
- Start with the highest-risk behaviors; the plan must deliver value if the sprint ends
  early, so order by risk, not by file layout.
- Keep the unit layer's quality bar: one behavior per test, observable-outcome
  assertions, doubles chosen by role, determinism seams everywhere.
- Keep the integration layer honest: one boundary per test, real engines in containers,
  contract tests for owned service pairs, fault injection for every third-party client.
- Wire stages as suites land: the commit stage blocks from the first slice, so the
  gate's contract exists from day one.
- Checkpoint question: "If the sprint stopped right now, what would this slice have
  proven?"

### Step 10 — Keep the plan alive
**Reference:** `references/ci-test-pipelines.md`

- New behaviors enter the inventory and get technique-derived cases before the code
  that implements them merges; the plan is a living table, not a document.
- Run the escape-rate review monthly: every production bug names the level that should
  have caught it, and the fix lands in the plan.
- Audit the plan quarterly: allocation versus defect history, quarantine count, stage
  budgets, sacrifice list still true.
- Retire tests on purpose: when a flow dies, its tests die with it. Untended suites
  grow, slow, and lie.
- Checkpoint question: "Does the plan still describe the suite that exists?"

## 05 — Rules and Quality Bar

1. **The plan tests behaviors, not lines.** Coverage percentage is a secondary signal;
   the exit metric is behaviors-with-cases. Line-coverage targets produce
   assertion-free tests of getters.
2. **Every E2E test traces to a named flow and a named consequence.** If you cannot
   justify it in one sentence, it is a liability you maintain nightly.
3. **Illegal transitions before happy paths.** For anything with a lifecycle, the
   empty cells of the state matrix are the first tests written — that is where
   money-losing bugs live.
4. **Mock what you own; stub what you consume.** A mock of a third-party API encodes
   your guess and lies when the vendor changes; cover real vendors with thin contract
   tests against recorded responses.
5. **One boundary per integration test.** A test that touches database, broker, API,
   and clock is an E2E test in disguise; when it fails you cannot say which seam broke.
6. **Nondeterminism gets a seam or the test does not ship.** Injected clocks, seeded
   randomness, no sleeps in waits. A test that fails sometimes trains the team to
   re-run instead of believe.
7. **Cases carry provenance.** EP, BVA, DT, ST, PW, EG, PROP on every group — review
   checks classes, deletions name the class they orphan.
8. **Production data never enters test environments.** Shape from production, values
   synthetic. This rule has no exceptions, no "temporarily," and no personal laptops.
9. **The commit stage stays under ten minutes.** Fix latency with selection and
   sharding, never by deleting the gate or by routing around it.
10. **Flakes quarantine within a day, with an owner and a re-entry criterion.** Left
    red, trust dies; blanket-retried, lies live. Never neither.
11. **Every stage has one gate decision and one owner.** Unowned stages decay into
    folklore nobody dares change.
12. **The sacrifice list is explicit.** What is not tested is a recorded decision with
    a reason; silent omissions are how "fully tested" stops meaning anything.
13. **Seams come first.** A plan that requires dependencies no code provides is a
    fiction; seam work is scheduled ahead of test-writing, with owners.
14. **The suite's shape is audited against defect history quarterly.** The pyramid is
    a policy, not a religion — but deviations are derived from evidence, re-derived
    regularly.

## 06 — Worked Example

The full example lives in `examples/worked-test-strategy.md`; this section shows the
shape of the reasoning on its central decisions. The subject: **ShopPay**, a
payment-checkout module — cart totals, pricing rules, authorization, capture, void,
refund via a PSP ("PayCo") — with zero existing tests and money on every line.

**Step 1-2 set the stakes.** The consequence statement: a wrong total settles against
the PSP's books, a double capture or missed refund is a support incident with financial
liability. Money risk means the state machine gets property tests and E2E exists at
all; the same workflow on a settings page would produce a much smaller plan. The
baseline: zero tests, no CI beyond lint, three missing seams (PSP client, clock,
repository injection) — recorded as blocking tasks before any test work.

**Pyramid breakdown (Step 4):** rule-dense core with a thin I/O shell and one
vendor-owned heavyweight dependency, so a near-default pyramid:

| Level | Scope | Count | Budget | Stage |
|---|---|---|---|---|
| Unit (~90) | pricing, validation, transition guards, error mapping | 90 | ≤ 60 s | commit |
| Integration (~45) | Postgres repo, PayCo stub-peer with faults, webhooks, composition root | 45 | ≤ 5 min | integration |
| Property (4) | totals invariant; stateful "never captured+voided"; capture/refund idempotence | 4 | ≤ 2 min | commit |
| E2E (5) | the five money flows, sandbox PayCo, seeded accounts | 5 | ≤ 10 min | nightly |

**Technique selection (Step 5):** the decision table for discounts (member 10% vs
coupon, best-of never stacks) exposed a tie-break ambiguity — a requirements bug
raised before a test existed. The boundary sweep at rounding edges found the service
and the PSP disagreeing on half-even at `x.005` — the spec got amended before code.
The state matrix produced 8 legal transitions (integration) and 19 illegal ones (unit
guards): capture-after-void, double refund, refund-above-captured. The fault matrix
for the PayCo client: timeout, 503-twice-then-200, malformed body, rate-limit — four
scenarios each asserting end-state and error mapping, testing *our client's* handling,
never the vendor. One stateful property — "no sequence of legal commands leaves an
order both captured and voided" — found a race on its first nightly run.

**CI stage design (Step 7):** commit stage blocks merge (unit + property + affected
integration, ≤10 min); integration stage blocks pre-merge (full suite in containers,
≤15 min); nightly runs E2E plus wide property seeds plus PayCo contract replay
(alerts only); release smoke (health + guest-checkout sandbox flow, ≤5 min) blocks the
release. Flake policy: named owner, one-day quarantine, re-entry after 100 clean
nightlies, zero blanket retries. Escape-rate review monthly.

**What the pass caught before any test was written:** the discount tie-break
ambiguity, the rounding disagreement, three missing seams, and — from plan review —
the absent reconciliation story (module totals vs PayCo's settlement report, now a
daily check). Four defects and three structural gaps from analysis alone: the cheapest
work in the entire exercise, and the reason Steps 1-4 precede any test-writing.

## 07 — Failure Modes and Recovery

### The suite is an ice-cream cone (E2E-heavy, no unit layer)
- **Symptom:** hours of CI, three flakes per green build, red builds stay red for days.
- **Recovery:** measure first — the E2E tests are usually eleven flows recorded
  redundantly, not eleven hundred units of safety. Free one seam per sprint, migrate
  each E2E test's assertions to the earliest seam that can hold them, delete the
  original when the replacement catches an equivalent bug. Five tests per sprint, with
  a migration ledger; never big-bang. (See Case 1 in `references/testing-case-studies.md`.)

### The plan assumed seams that do not exist
- **Symptom:** "just unit-test the pricing logic" — except the PSP client, clock, and
  repository are hardwired.
- **Recovery:** the seam list is a work item, scheduled ahead of tests with owners.
  Do not mock your way around it; mocks of hardwired structure test the mock.

### Flakiness has destroyed trust in the gate
- **Symptom:** engineers hit retry as a reflex; red means nothing.
- **Recovery:** enforce the numbered policy — detect from CI history, quarantine
  within a day with owner and due date, root-cause the nondeterminism (injected clock,
  deterministic waits, per-worker data), re-enter on evidence. If quarantined tests
  exceed ~1% of the suite, stop adding tests and spend the sprint on the backlog.

### A production escape the suite should have caught
- **Symptom:** a bug ships; some test passed where a behavior test would have failed.
- **Recovery:** the postmortem answers one question in writing — which level *should*
  have caught it, and what change makes the next one land there. The answer updates
  the plan (new behavior row, new class, new property). Escape-rate review monthly.

### Tests assert proximity, not behavior
- **Symptom:** high coverage, green suite, real defects — mutation testing would show
  survivors everywhere.
- **Recovery:** rewrite the assertions of the affected module's tests against
  observable outcomes; use mutation testing as a quarterly audit on the critical 10%,
  not a gate.

### The plan became a shelf document
- **Symptom:** the plan describes a suite that stopped matching reality two quarters ago.
- **Recovery:** Step 10's audits are the maintenance contract — inventory updates on
  merge, quarterly shape audit, retirement of dead flows' tests. If the plan cannot
  be maintained, shrink it to the behavior inventory and the gate table, which are the
  two parts that must stay true.

### The vendor (PSP, API, service) changed and tests went red en masse
- **Symptom:** forty failures overnight, all in one boundary's tests.
- **Recovery:** this is the contract-test investment paying off — the red build is the
  *drift signal*. Update the stub-peer fixtures and the recorded contract against the
  vendor's changelog, then review which behavioral assertions changed meaning.

### Nobody knows what "done" means for testing this feature
- **Symptom:** "more tests" as an endless ask; arguments about sufficiency with no
  arbiter.
- **Recovery:** the plan's exit criteria — behaviors covered, illegal transitions
  green, properties live, reconciliation running. Sufficiency is checked against the
  inventory, not felt in a standup.

## 08 — Supporting Files Index

Reading order: run §04 top to bottom; open a reference when a step names it; use the
template to write the plan; read the worked example before your first real pass — it
shows the judgment calls the steps compress.

Why the file set is shaped this way: the eight references each carry one body of craft
— allocation economics, case derivation, the two main levels' patterns, the specialty
techniques, data policy, pipeline design, and applied cases — so SKILL.md stays
procedural rather than encyclopedic. The template defines the one output shape (the
plan). The example shows the full pass on a zero-test money module at realistic depth.
If you read only one file before planning, make it `references/testing-pyramid.md`.

| File | Purpose | Used In |
|---|---|---|
| `references/testing-pyramid.md` | Level allocation, economics, anti-patterns, rescue shape | §04 Steps 1-2, 4; §05 Rule 9 |
| `references/test-design-techniques.md` | EP, BVA, decision tables, state machines, pairwise, risk weighting | §04 Steps 3, 5; §05 Rule 7 |
| `references/unit-testing-patterns.md` | Structure, doubles, determinism, the quality bar for unit tests | §04 Step 9; §05 Rules 1, 6 |
| `references/integration-testing-patterns.md` | Real boundaries, contracts, fault injection, environment hygiene | §04 Step 9; §05 Rule 5 |
| `references/property-and-fuzz-testing.md` | Invariants, oracles, stateful models, fuzz campaigns | §04 Step 5; §05 Rule 3 |
| `references/test-data-management.md` | Builders, fixtures, anonymization, goldens, realism dial | §04 Step 6; §05 Rule 8 |
| `references/ci-test-pipelines.md` | Stage ladder, gates, sharding, flake policy, reporting | §04 Steps 7, 10; §05 Rules 9-11 |
| `references/testing-case-studies.md` | Four realistic strategies with their first-draft mistakes | §06, §07 context |
| `templates/test-plan-template.md` | The plan's shape, with reviewer checklist | §04 Step 8; §05 Rule 12 |
| `examples/worked-test-strategy.md` | ShopPay full pass: pyramid, techniques, stages, decisions | §06 Worked Example |

Maintenance contract:

- This table must match the directory exactly — the verification suite diffs it
  against reality.
- If you add a file, add a row and cite it at its point of use in §04.
- If a file is no longer used, remove both the file and the row; dead rows are findings.

Cross-skill boundaries:

- Seams and boundaries the plan requires are designed in `software-architecture-design`;
  this skill names them and hands structural work over. The strategy plans around the
  architecture; it does not redesign it.
- Per-diff questions ("is this behavior tested?") belong to `code-review`; that skill
  flags test-plan gaps and hands them back here. Review asks, strategy owns.
- Performance, load, and capacity work is a separate discipline; this skill sets the
  boundary (slow integration tests are failures, not benchmarks) and defines the
  handoff point (a named performance ticket with its own budget).
- Exploratory testing gets a reserved line in the plan (charter, owner, timing) but its
  own craft is out of scope here.

### Common testing archetypes

| Archetype | Pyramid shape | Key techniques | CI posture | Best for |
|-----------|--------------|----------------|------------|----------|
| Greenfield | 70/20/10 unit/integration/e2e | EP, BVA, property-based | All stages block merge | New services with clean slate |
| Brownfield rescue | 40/40/20 — elevate integration coverage | Characterization tests, seam injection | Integration stage blocks; unit stage is aspirational | Legacy code with high defect rate |
| Microservice | 80/15/5 — test your service, mock others | Contract tests, fault injection, stateful properties | Commit: unit + contract; Nightly: full + fuzz | Distributed systems with many dependencies |
| Data/BI | 30/20/50 — ETL validation is the critical path | Golden datasets, schema assertions, row-count diffs | Integration blocks merge; e2e runs on schedule | Reporting, analytics, ML pipelines |

### Skill maintenance contract

This skill targets an active codebase. Revisit the archetype selection every 3-6 months or after a major architectural change. When the system evolves, re-run the risk inventory (Step 1) and technique selection (Step 4) before updating individual test suites. The template and worked example should be revised when the team's CI pipeline or test tooling changes materially.

### Key testing terms

| Term | Definition |
|------|-----------|
| Unit test | Tests a single unit in isolation, with all collaborators replaced by doubles. Fast (~ms), deterministic, no I/O |
| Integration test | Tests across real boundaries — database, network, filesystem. Slower (~s), covers the seams |
| E2E test | Tests through the full deployed system. Slow (~min), high confidence, high maintenance |
| Property-based test | Asserts invariant properties over many generated inputs rather than specific example values |
| Characterization test | Captures current behavior as a test, used when refactoring legacy code without existing tests |
| Seam | A point in the code where behavior can be replaced without changing the code itself — the entry point for test doubles |
| Flake | A test that passes and fails without any code change. Root cause is always non-determinism in the test or its environment |
| Escape | A bug that reaches production despite the test suite. Escapes trigger a retrospective: what did the suite miss? |
| Hermetic | A test that depends on nothing outside its own process — no shared databases, no network, no wall-clock timing. Every hermetic test is reproducible on any machine |
| Coverage gap | A region of the codebase that no test exercises. Measured by line coverage but more importantly by risk coverage — are the high-risk behaviors tested? |

### Archetype quick-reference

| Archetype | Pyramid shape | Key techniques | CI posture | Best for |
|-----------|--------------|----------------|------------|----------|
| Greenfield | 70/20/10 unit/integration/e2e | EP, BVA, property-based | All stages block merge | New services with clean slate |
| Brownfield rescue | 40/40/20 — elevate integration coverage | Characterization tests, seam injection | Integration stage blocks; unit stage is aspirational | Legacy code with high defect rate |
| Microservice | 80/15/5 — test your service, mock others | Contract tests, fault injection, stateful properties | Commit: unit + contract; Nightly: full + fuzz | Distributed systems with many dependencies |
| Data/BI | 30/20/50 — ETL validation is the critical path | Golden datasets, schema assertions, row-count diffs | Integration blocks merge; e2e runs on schedule | Reporting, analytics, ML pipelines |

### Related skills in this repository

| Skill | Relationship |
|-------|-------------|
| code-review | Reviews per-diff test coverage questions; flags test-plan gaps that belong here |
| software-architecture-design | Architecture decisions determine what seams are available for testing — design for testability |
| operations-and-process-design | CI pipeline design and flake-management processes feed into the test strategy's operational layer |

### Test-strategy maintenance cadence

| Trigger | Action |
|---------|--------|
| New feature with high-risk behavior | Re-run risk inventory (Step 1), add techniques (Step 4) |
| Architecture change (new seam, new service) | Update test-level allocation (Step 2), re-run CI design (Step 7) |
| Flake rate exceeds 2% | Quarantine all flakes, run root-cause analysis, adjust hermeticity |
| Two escapes in one quarter | Retrospective every escape, update technique selection and review checklist |
| Team growth or churn | Review plan readability, update template examples |

### Related skills in this repository

| Skill | Relationship |
|-------|-------------|
| code-review | Reviews per-diff test coverage questions; flags test-plan gaps that belong here |
| software-architecture-design | Architecture decisions determine what seams are available for testing |
| operations-and-process-design | CI pipeline design and flake-management process feeds into operational layer |
### Reading Paths

**New to testing strategy:** Start with `references/testing-pyramid.md`, then
`references/test-design-techniques.md`. Read the worked example at
`examples/worked-test-strategy.md`. Return to SKILL.md for the workflow.

**Planning for a new system:** Follow steps 1-10 in order. Each step names the
reference file to read first. Use `templates/test-plan-template.md` as the
output scaffold.

**Rescuing a flaky suite:** Jump to section 07 (Failure Modes). Start with
environment non-determinism — it causes 60% of flakes — then work through
the remaining patterns.

**Diagnosing an escape:** Start with the retrospective template. Identify what
risk class the escape belongs to, what technique would have caught it, and
whether that technique should be added to the permanent plan.
A mature test strategy is a living document — review it quarterly.
