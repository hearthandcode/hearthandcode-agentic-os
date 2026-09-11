# CI Test Pipelines — Stage Design, Gates, and Flake Control

The test suite's value is realized only where it runs. A well-designed suite bolted to
a badly designed pipeline still delivers: hours-long feedback, red builds nobody trusts,
and a merge gate people route around. This reference covers the pipeline half of the
strategy: which tests run where, what blocks a merge, and how flakiness is kept from
destroying trust.

## The stage model

A pipeline is a sequence of progressively more expensive, progressively more realistic
stages. Each stage's job: kill the build fast enough that the next stage's cost is only
paid for builds that earned it.

| Stage | Runs | When | Budget | Gate strength |
|---|---|---|---|---|
| Pre-commit / editor | Lint, types, affected unit tests | On save | Seconds | None — convenience |
| Commit stage (PR) | All unit + affected integration + compile | On every push | **≤ 10 min** | Blocks merge |
| Integration stage | Full integration suite, containers | Before merge or on merge to main | ≤ 20 min | Blocks merge |
| Nightly | E2E, properties, fuzz campaigns, mutation spot-audits | Scheduled | 1–4 h | Alerts, not blocking |
| Release | Full E2E, smoke on the release candidate, migration dress rehearsal | On release branch | ≤ 1 h | Blocks release |
| Production | Smoke checks, synthetic transactions | Continuous | Seconds | Pages |

Design rules that fall out of the table:

- **Feedback time is the product.** The commit stage over ~10 minutes trains developers
  to context-switch; the fix is parallelization and affected-test selection, never
  deleting the gate.
- **Every stage has one owner decision: what does this stage block?** A nightly stage
  that blocks merges is a stage misplaced; a commit stage that alerts without blocking
  is a gate that does not exist.
- **Fail the stage on the first red signal**; do not let later stages run against a
  build already known broken.

## The merge gate — what "green" means

The merge gate is the contract: green means safe to merge, red means not. Enforce it:

- Branch protection: merges require the gate; no admin overrides except a recorded,
  time-boxed break-glass process with a follow-up ticket.
- Required checks are the *minimal* set that must pass: compile, lint, unit, affected
  integration. Everything else alerts.
- A red main is an all-hands signal with a default clock: revert or fix within the
  hour. The person who broke it owns the fix; "someone will look at it" is how red
  mains become red weeks.
- Flaky tests never sit in the required set. A flake in the gate converts every merge
  into a dice roll and every engineer into a re-run clicker — quarantine policy below.

## Parallelization and sharding

- Shard by test file/module with per-shard timing awareness; naive round-robin sharding
  produces one 20-minute shard and three 3-minute ones.
- Parallelize integration tests by giving each worker its own ephemeral dependencies
  (containers with distinct ports/networks or separate schemas). If tests cannot run
  in parallel, that is a data-coupling finding — fix the tests, not just the pipeline.
- Cache the world: dependency downloads, compiled artifacts, container image layers.
  Cache misses should be rare events, and the cache key must include the lockfile
  hashes.

## Affected-test selection

For monorepos and large suites, run the tests that the change *could* affect:

- Map directories to owning test suites; run the union of maps touched by the diff.
- Under-selecting is dangerous, so the mapping errs inclusive, and the nightly full
  suite backstops it. Selection is an optimization for the commit stage; the merge and
  nightly stages eventually see everything.

## Flake control — the trust policy

Flakiness is not an annoyance; it is the mechanism by which a team learns to ignore
red. Run it as a numbered policy:

1. **Detect**: CI records per-test pass/fail history. Any test with ≥2 spurious fails
   in a rolling month is flagged automatically.
2. **Quarantine within a day**: flagged tests are marked (`@flaky`) and removed from
   the required gate while keeping them visible in a non-gating job. Quarantine has an
   owner and a due date; it is a hospital, not a retirement home.
3. **Fix at the root**: nondeterminism sources (time, sleep-based waits, shared state,
   network races, unordered collections) are the checklist; most flakes die with an
   injected clock and deterministic waits.
4. **Re-enter through evidence**: a quarantined test returns to the gate only after a
   green streak in the non-gating job (e.g., 100 consecutive nightly runs).
5. **Never** blanket-retry to green. One automatic retry with reporting is tolerable
   during quarantine triage; retries as a permanent policy are how flakes hide.
6. **Budget**: if quarantined tests exceed ~1% of the suite, stop adding tests and
   spend the sprint on the quarantine backlog — a growing quarantine is a failing suite
  with better PR.

## Reporting that people read

- Failures first: the pipeline report leads with what failed, at which stage, with the
  first failing step — not 4,000 lines of scroll.
- Trends: suite runtime, flake rate, quarantine count, and escape rate (bugs found in
  production that tests should have caught) reported monthly; trends are how the plan
  gets re-budgeted.
- Test quality signals: skipped tests and quarantined tests are surfaced on every PR
  touching their module — invisible skips are how coverage quietly dies.
- Artifacts on failure only: logs, container states, database dumps from the ephemeral
  environment. Always-on artifact collection is where build minutes go to die.

## Release and post-deploy stages

- **Migration dress rehearsal**: before a release with schema migrations, replay the
  migrations against a production-shaped copy and measure the lock window. A migration
  that has never run against production-shaped data in CI will run its first such pass
  in production.
- **Release smoke**: on the release candidate, a minute-scale suite covering deploy
  health, auth, and the top revenue flows. It blocks the release; it does not replace
  the nightly E2E.
- **Synthetic monitoring**: after deploy, the smallest set of synthetic transactions
  (login, search, checkout) runs continuously against production. This is the last
  stage of the pipeline and the first detector of environment-specific failures no
  test environment replicates.

## Anti-patterns

- **The 90-minute merge gate**: unbounded suite growth in the required set; fix with
  selection and sharding, and move slow non-critical tests to nightly.
- **Retry-as-strategy**: `retries: 5` globally hides real nondeterminism; use it only
  for known-flaky marked tests, and count the retries in reporting.
- **Green-meaningless**: required checks that only lint, or that skip on empty-diff
  paths, give false confidence. Audit the required set quarterly against the actual
  defect escapes.
- **Pipeline sprawl without owners**: every stage has a named owner; an unowned stage
  decays into folklore nobody dares change.