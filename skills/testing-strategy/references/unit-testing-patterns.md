# Unit Testing Patterns — Tests That Name a Behavior and Keep Their Word

A unit test proves one behavior of one unit of code in isolation, in milliseconds, with
zero I/O. Most suites fail not from missing tests but from tests that assert too little,
mock too much, or couple to implementation details — so they pass while the product is
wrong, or break on harmless refactors. These patterns are the quality bar.

## One test, one behavior, one reason to fail

The naming convention carries the spec: `subject_condition_expected_result` in the
domain's language — `charge_declined_when_card_expired_reports_declined_with_reason`.
A name containing "and", "or", or "correctly" is usually two tests or zero specification.

Structure every test in three moves:

1. **Arrange** — build the minimal world: inputs, stubs, state. Anything the test does
   not read or assert on is noise; delete it.
2. **Act** — exactly one call to the subject, extracted to one line. If acting takes
   five calls, you are testing a scenario, not a unit — move it to integration.
3. **Assert** — on observable outcomes: return value, state change, outbound message
   to a collaborator. Asserting on internal calls (a private method ran, a mock got
   three calls in an order nobody specified) is implementation coupling.

## The Verify Principle — test through the public seam

Test the subject through the interface its callers actually use. This keeps tests valid
through refactors: rename a private helper, twenty tests stay green because none of them
knew it existed. The trade-off, handled honestly:

- Testing only the top public API of a deep module makes failure diagnosis slow, so
  extract the *next* public seam as behavior grows rather than reaching into privates.
- A behavior with no observable external effect does not deserve a test — if nothing
  can detect its absence, its absence changes nothing.

## Test doubles: choose by the collaborator's role

| Double | Use when | The trap |
|---|---|---|
| Stub | The test needs the collaborator to *return* data | Stubbing values that don't match the real thing |
| Fake | The collaborator has real logic worth exercising (in-memory DB, in-process queue) | Fakes drifting from the real implementation |
| Mock | You must verify an *outbound* interaction (an email was sent, an event published) | Mocking *inbound* calls — that's re-implementing the subject |
| Spy | You need interaction history without pre-scripted replies | Over-asserting: checking every call, not the meaningful one |

The dividing rule: mock what you *own*, stub what you merely *consume*. A mock of a
third-party API encodes your guess about its behavior; when the vendor changes, your
green tests lie. Mock your repository interface (you own it and its failure modes);
stub the payment provider's HTTP layer at your anti-corruption boundary, and cover the
real vendor with a thin contract test.

Only assert interactions that would break the user if they broke: "the refund event was
published once" is load-bearing; "the logger was called with exactly these fields" is not.

## The shared-setup trap

One god fixture with twenty fields, mutated by every test, is how suites become
unmaintainable: change one field, 400 tests fail, nobody knows which behavior changed.

- Build setup per test: helper functions (`makeOrder(paid=true)`) with explicit
  arguments, not shared mutable state.
- Shared *unchanging* constants are fine; shared *mutable* state is a bug factory —
  including module-level caches and class attributes.
- If ObjectMother-style builders grow unwieldy, split them by aggregate, not by test file.

## Parameterization and the case catalog

Any test whose body repeats with different data is a parameterized test over a case list.
Keep the list in a table with an ID and the expected outcome, so a failure reads
"case 7: zero-quantity cart is rejected" — not a stack trace and a guess. This is also
where the design techniques' output lands: each equivalence class becomes one row.

## Testing error paths with the same rigor as happy paths

For every failure mode the subject can produce, assert three things: the error is the
*specified* one, the message is actionable (contains the identifier an on-call human
needs), and no partial side effect leaked (the charge was not captured, the event was
not half-published). Testing that "it throws" without asserting which error is how
systems end up returning 500 for a declined card.

## Time, randomness, and environment — the determinism contract

A unit test that fails sometimes is worse than no test: it trains the team to re-run.
Every source of nondeterminism gets a seam:

- **Time**: inject a clock. Never `Thread.sleep` in a unit test; advance the fake clock.
- **Randomness**: inject a seed or a source; test the distribution separately if needed.
- **Filesystem/network**: never in unit tests — those are integration tests by definition.
- **Locale, timezone, threading**: set explicitly; do not depend on the CI machine's
  defaults, which differ from laptops.

## What not to unit test

- Plain data classes and constants — nothing to verify.
- Thin configuration wiring — one integration test that the wiring resolves beats fifty
  reflection tests.
- Generated code and vendor SDK internals — contract-test the boundary instead.
- Private methods — unless a behavior is genuinely too intricate to express through any
  public seam, in which case the fix is an extraction, not an exemption.

## The mutation-testing sanity check

Coverage says lines ran; mutation testing says the assertions would notice a change.
Run a mutation tool occasionally on critical modules (pricing, auth): if it reports
surviving mutants in code you believed well-tested, the tests assert proximity, not
behavior. Budget note: mutation testing is minutes-to-hours per module; use it as a
quarterly audit of the critical 10%, not a CI gate.

## Quality bar checklist

- Runtime: the whole unit layer stays under ~10 minutes; single tests under ~100 ms.
- Failure precision: any red test names the behavior that broke within seconds.
- Refactor tolerance: a pure rename/refactor turns zero tests red.
- No test reads another test's leftovers; order randomization passes.
- Every test's name states behavior, not method name.