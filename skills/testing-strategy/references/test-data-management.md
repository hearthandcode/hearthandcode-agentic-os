# Test Data Management — Fixtures, Factories, Anonymization, Seeds

Test data is the part of a test suite that rots fastest and leaks loudest. Bad fixtures
make tests lie (stale shape, missing required fields) or fail mysteriously (shared state,
order dependence); production data in a test environment is a compliance incident with
a timestamp. The patterns here keep data honest, minimal, and safe.

## The four sources, and when each is legitimate

| Source | Legitimate when | Risk |
|---|---|---|
| Factories / builders | Almost always — the default | Default values drifting from reality |
| Hand-written fixtures | A few named, documented scenarios | Rot; over-broad "god fixtures" |
| Synthetic generators | Volume, shape variety, property/fuzz testing | Unrealistic distributions hiding perf bugs |
| Production copies | Rarely, and only anonymized + access-controlled | **PII leaks, compliance violations** |

Default to factories. A factory is code: `makeOrder(status="pending", items=1)` — every
field has a sensible default the test overrides explicitly. The override *is* the test's
specification: reading `makeOrder(paid=True, refunded=False)` tells you what the test
is about in one line.

## The builder/factory pattern

- One builder per aggregate, living next to the test suite, typed like production.
- Defaults must be *valid* values from the current schema — if a field becomes
  required, the factory fails to compile or fails a schema-check test, and every test
  using it is flagged for review rather than silently producing garbage.
- Never share mutable instances: builders return fresh objects; helpers never reach
  into module-level state a previous test mutated.
- Grow builders by parameter, not by subclass zoo: `makeOrder(items=[makeItem(qty=2)])`
  beats `makeOrderWithTwoItemsAndACouponAndAGiftCard()`.

## Anonymization — production-shaped, not production

When realistic data is genuinely needed (schema migrations, performance, search
relevance), the rule is: **shape from production, values synthetic**.

- Never copy PII into test environments, ever — not "temporarily," not "just my
  machine." A database dump in a test environment is a breach, not a convenience.
- Anonymize with care: hashing identifiers preserves joins but can be reversed for
  low-entropy fields (phone numbers, ZIPs, birthdates). Substitute from realistic
  synthetic distributions instead of hashing, or hash with a keyed process and treat
  the mapping as sensitive.
- Keep referential integrity: the anonymized dataset must still satisfy foreign keys,
  or migration tests will pass on garbage that production would reject.
- Record lineage: which snapshot, which transformation, which version of the tool.
  An anonymization step nobody can reproduce is an unanonymized step waiting to be
  rerun wrong.

The anonymization pipeline is itself tested: run it on a synthetic dataset with
plant-item PII, assert nothing planted survives.

## Fixtures and lifecycle

- **Minimal scope.** A fixture creates exactly what its tests assert on. Fixture files
  that start with 3 records and end with 40 across a year are a rot graph; prune on
  sight and split by aggregate.
- **Set up per test, not per class/module**, unless setup is provably read-only. The
  cheap insurance against order dependence: randomize test order in CI; any failure
  that appears only in a fixed order is a coupling bug.
- **Cleanup ownership.** Prefer transactional rollback or per-run containers (data
  dies with the environment) to manual deletes. If cleanup is a script someone runs
  by hand, it is already not being run.
- **Identifiers, never positions.** Assert on `orders["ORD-7001"]`, never "the first
  order" — row order is an implementation detail of the database.

## Snapshot and golden files

Golden files (recorded responses, rendered output, serialized documents) are legitimate
for large stable outputs — a rendered PDF, a generated report — with three rules:

1. **Review the golden on creation**, like any diff; a snapshot update merged without
   reading is a regression merged with approval.
2. **Normalize the volatile fields** (timestamps, request IDs) before comparing, or the
   suite trains people to `--update-all` blindly.
3. **Cap the count.** More than a handful of goldens means a real assertion layer is
   missing; goldens detect *change*, not *correctness*.

## Test-data budget and realism trade-off

Data realism is a dial, and the dial is per suite level:

- Unit: pure fabricated values; realism irrelevant, speed everything.
- Integration: schema-valid, referentially sound, small — realism limited to shape.
- Performance: synthetic at production scale with production-shaped distributions
  (check the 99th percentile of values, not just means); anonymized if derived.
- E2E: the few named accounts the flows need, in a dedicated environment with seeded,
  versioned state.

Buying full realism at unit level wastes time; buying none at performance level makes
the benchmarks fiction.

## Anti-patterns

- **The god fixture**: one shared setup everything depends on and nothing dares change.
- **Copy-paste JSON blobs**: duplicated data across dozens of files with drifting
  shapes; if it appears twice, it becomes a factory.
- **Live third-party calls in setup**: test data preparation must not depend on a
  vendor being up; stub or record it.
- **Test data in production databases**: polluting real data with `TEST-` prefixes is
  a data-hygiene debt that always gets paid back with interest — keep test environments
  separate, or isolate test tenants rigorously.
- **Secrets in fixtures**: any credential found in a fixture file is an incident; use
  dummy values and inject real ones only via environment in E2E stages.