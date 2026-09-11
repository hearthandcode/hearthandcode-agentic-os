# Integration Testing Patterns — Real Boundaries, One at a Time

An integration test verifies that your code and a real collaborator agree: the schema
matches the query, the serialization matches the parser, the client matches the server's
actual contract. Unit tests with stubs cannot find these bugs — the stub encodes the
assumption being tested. Integration tests exist to break that assumption in CI, not in
production.

## What counts as an integration test

One real boundary per test: database, message broker, cache, filesystem, HTTP client
against a controlled peer, or the composition root that wires modules together. Two
rules keep diagnosis sharp:

- **One boundary per test.** A test that touches database + broker + external API +
  clock is an E2E test wearing an integration costume; when it fails you cannot say
  which seam broke.
- **Test through the seam your code actually uses.** Exercise the real repository
  method the handler calls, not a parallel test-only copy that drifts.

## Databases: the patterns that matter

**Schema-first tests.** Migrations are code; test them. Every migration gets a
forward-and-back test against a fresh database seeded with representative data. A
migration suite that has never run against production-shaped data is a production
incident on a timer.

**Repository tests against a real engine.** Spin up the actual database (testcontainers
or an ephemeral instance) — not a SQLite stand-in for Postgres, and not an in-memory
emulation. SQLite tolerates SQL Postgres rejects, and the difference always surfaces in
production. Assert on read-back state, not on "the insert didn't throw."

**Transaction discipline.** Decide once, team-wide:

- Wrap each test in a transaction and roll back (fast, but hides commit-time behavior), or
- Truncate between tests (slower, more honest), or
- One schema per test class with unique-tenant isolation.

Document the choice; mixing modes produces order-dependent flakes.

**Concurrency and constraint bugs live here.** The double-submit race, the unique
constraint race, the lost-update on read-modify-write — these are integration tests with
real threads or two concurrent transactions. They are flaky by nature, so gate them
behind a marker and give them retry-free deterministic structure (barriers, not sleeps).

## HTTP boundaries

**Your API, from the outside.** Contract tests hit the running app in-process (or a
container) and assert request/response contracts: status codes, error shapes, headers,
auth required where specified. This is where "the API returns 500 for a declined card"
gets caught, because the controller's error mapping is exactly the kind of code unit
stubs erase.

**Your outbound clients, against a stub peer.** Run a controlled HTTP stub (WireMock,
httptest, a local fixture server) that answers canned and fault responses. The point is
not to test the vendor — it is to test *your client's* handling of the vendor's
documented and undocumented behaviors: timeouts, 5xx, malformed bodies, rate-limit
responses, TLS handshake delays.

**Contract testing between your own services.** When you own both ends, record the
provider's contract and replay it against the consumer (Pact-style or a shared schema
snapshot). The provider's pipeline fails when it breaks a consumer — no joint
environment needed. This replaces the majority of cross-service E2E tests.

## Message brokers and queues

- Publish-consume roundtrip on a real broker instance (container or ephemeral cloud
  namespace), asserting delivery and ordering guarantees you actually rely on.
- Poison-pill handling: a message that fails processing goes to the DLQ, not into a
  restart loop.
- At-least-once reality: handlers must be idempotent; test duplicate delivery
  explicitly, because the broker *will* deliver twice someday.
- Schema evolution: a message produced by the old schema must deserialize under the
  new one where compatibility is promised.

## The composition root

One test (or a handful) that boots the real wiring — real DI graph, real config
loading, real feature flags resolved — and proves the system starts and answers a
health check. Cheap, and it catches the "missing binding" class of failure that
individual seam tests never see.

## Environment management

- Ephemeral per run, not shared: containers (Testcontainers, compose) or per-CI-job
  instances. Shared staging databases under CI are the source of most cross-run flakes.
- Pin versions. Integration tests must run against the *same major versions* as
  production; testing against "whatever the image was this week" is uncontrolled.
- Seed data is part of the test: fixtures state exactly what they create and assert on
  identifiers, never on "the first row."
- Startup readiness: poll health endpoints with a bounded timeout; never sleep a fixed
  number of seconds and hope.

## Speed and hygiene budget

- The integration layer's total wall-clock budget: ~10 minutes in CI. Above that,
  parallelize by boundary or shard by module.
- Every integration test must clean up what it creates, or the suite degrades into
  mysterious cross-test coupling. Prefer teardown-by-rollback to teardown-by-scrubbing.
- Flakiness protocol: a test that fails twice in a month without a code cause gets
  quarantined within a day (marked, moved out of the merge gate, ticketed with an
  owner) — never left red, never silently retried forever.

## The contract test, in one paragraph

The most valuable integration test in a microservice fleet is the recorded contract:
consumer captures what it needs from the provider; provider replays those expectations
on every build. It converts "we think the orders service still returns `total_cents`"
from a production incident into a red build in the provider's CI. Where you own both
sides, contract tests should outnumber cross-service E2E tests by ten to one.

## What integration tests are not for

- Business-rule coverage — that is the unit layer's job; duplicating every rule here
  doubles maintenance for nothing.
- Full user journeys — that is E2E, and the pyramid caps it deliberately.
- Performance — load tests are a separate discipline with separate budgets; a slow
  integration test is a failing test, not a benchmark.