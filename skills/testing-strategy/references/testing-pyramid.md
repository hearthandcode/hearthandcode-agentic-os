# The Test Pyramid — Allocation and Economics

The pyramid is an allocation policy, not a moral ranking. It says: given a fixed testing
budget, put most tests at the level where they run fastest, fail most precisely, and lie
least — and pay for expensive realism only where the cheap levels structurally cannot
express the behavior. Teams that invert this spend hours in slow suites chasing failures
a unit test could have named in seconds.

## What each level actually buys you

| Level | What is real | Typical runtime | Failure diagnosis | Flakiness risk |
|---|---|---|---|---|
| Unit | One behavior; collaborators are stubbed, faked, or in-memory | 1–50 ms | Exact — names the function and the expectation | Near zero if kept deterministic |
| Integration | Owned boundaries are real: database, queue, HTTP client against a controlled peer | 0.1–5 s | Good — names the seam that broke | Low–moderate; grows with environment complexity |
| End-to-end | The whole deployed system: real network, real UI or public API surface | 10 s–10 min | Poor — "checkout failed"; now find where | High — every dependency is a failure source |
| Manual / exploratory | Everything, unscripted | Hours | Human judgment | Not applicable |

Two facts drive the shape:

- Cost per test rises with realism while information per failure falls, because more
  components could have caused it.
- Speed determines whether the suite runs on every commit. A suite that runs nightly
  protects nothing: the commit that broke it is buried under a day of work by the time
  anyone sees red.

So the pyramid maximizes (tests per minute) × (diagnosis precision) and buys realism
only when cheaper levels cannot express the behavior at all.

## The default shape

For a typical web backend or CLI product, allocate roughly:

- **70% unit** — pure logic: pricing, validation, state machines, formatting, parsers.
- **20% integration** — one real boundary per test: repository against a real database,
  event handler against a real broker, client against a contract stub.
- **10% end-to-end** — the money paths only: signup, login, checkout, the top support-ticket
  flows. Single digits to low dozens, never hundreds.

The percentages are by test count, not by runtime or value. The five E2E tests in a
mature suite are the most expensive five percent and the last line of defense — treat
them as production telemetry for the happy path, not as the primary safety net.

## Allocation by module type

The right shape depends on where behavior lives:

| Module type | Recommended shape | Why |
|---|---|---|
| Pure logic core (rules engines, math, parsing) | Heavier unit layer, ~80/15/5 | Behavior is fully expressible in-process |
| CRUD service behind a database | Thick middle, ~50/40/10 | Most defects are schema, query, and transaction bugs unit tests cannot see |
| Event-driven pipeline | Integration-weighted, ~40/50/10 | The contract between stages *is* the behavior |
| UI-heavy frontend | Unit for logic + a small E2E happy-path set, ~60/30/10 | Component tests cover rendering logic; E2E covers composition |
| Library / SDK shipped to others | Unit + conformance suite, E2E only as release checks | Your users' integrations are your E2E |

Do not copy a ratio from another team. Derive the shape from the module's defect history:
look at the last ten bugs and ask at which level each could have been caught cheapest.

## The ice-cream cone — the anti-pattern

Symptoms: a thin or absent unit layer, hundreds of UI/E2E tests, CI measured in hours,
red builds that stay red for days, and a team habit of retrying until green.

Causes, in order of frequency:

1. **No seams.** Dependencies are hardwired, so the only way to exercise code is through
   the whole system. Fix seams first (see `software-architecture-design`); no test plan
   survives untestable structure.
2. **Distrust of unit tests.** Usually earned — the existing unit suite mocked everything,
   passed, and let a real bug through. The fix is better unit tests at real boundaries,
   not abandonment of the level.
3. **Coverage metrics punished the wrong thing.** "90% coverage" measured on E2E runs
   produces E2E tests. Measure coverage per level instead.

Recovery is downward migration: for each E2E test, find the earliest seam where its
assertion could live and add tests there, then delete the E2E original when the new ones
catch an equivalent bug. Do it at five tests per sprint, not big-bang.

## Deviations that are correct

- **Honeycomb / integration-weighted.** Services whose logic is gluing collaborators
  (typical microservice) get a fat middle: few pure-unit behaviors, many integration
  tests against real dependencies in containers, minimal E2E.
- **Thick middle for I/O-heavy systems.** If most past bugs were data and concurrency
  bugs, fund the level that exercises those for real.
- **Testing trophy.** If most behavior is orchestration, static types plus a dominant
  integration layer beat a pyramid. The shape follows the code's actual behavior
  distribution, always.

What is never correct: inverting to E2E-dominant. If you find yourself there, the plan
is seam work plus downward migration, not more E2E.

## Reading the shape of an existing suite

Before planning new tests, measure what exists:

- Count tests per level (by directory convention or marker). Percentages, not vibes.
- Measure per-level wall-clock runtime. The unit layer over ~10 minutes total is a finding.
- Count mock/stub declarations per test on average. Averages above ~5 suggest the unit
  layer is testing mocks, not behavior.
- Count skips, retries, and known-flaky markers. High counts mean the suite is lying
  about its own health; fix trust before adding tests.

## Rules of thumb

- Every E2E test must trace to a specific revenue- or safety-critical flow, named in
  the plan. An E2E test you cannot justify in one sentence is a liability.
- When a bug escapes to production, the postmortem must answer: which level *should*
  have caught it, and what change makes the next one land there. That answer, applied,
  is how a pyramid keeps its shape.
- Adding a level's tests without a seam for it produces integration tests that mock the
  thing under test. Do the seam work first.