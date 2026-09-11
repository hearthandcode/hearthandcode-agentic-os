# Property-Based and Fuzz Testing — Testing Invariants, Not Examples

Example tests check what you thought of. Property-based tests check what you couldn't
have thought of: they generate hundreds of inputs from a specification, assert an
invariant holds for *every* one, and when it fails, shrink the input to a minimal
reproducible case. Fuzzing applies the same idea to hostile inputs — malformed, adversarial,
resource-exhausting data — where the invariant is "does not crash, hang, or corrupt state."

These techniques are not replacements for the example-based layers; they are the
high-yield specialty for behaviors whose correctness is an *invariant over unbounded
inputs*.

## When to reach for properties

Choose a property when you can state a rule that must hold for all inputs, even though
the input space is too large to enumerate:

| Property shape | Statement | Classic bugs found |
|---|---|---|
| Roundtrip | `decode(encode(x)) == x` for all x | Charset bugs, lossy normalization, key collisions |
| Oracle | `f(x) == slowCorrectF(x)` | Optimizations that changed behavior |
| Invariant | total = sum(items) − discount; never negative | Arithmetic drift, negative quantities |
| Idempotence | `retry(f(x)) == f(x)`, `migrate(migrate(db)) == migrate(db)` | Double-charge, non-idempotent handlers |
| Metamorphic | same query, shuffled input order → same result | Order-dependent logic, unstable sorts |
| Stateful | any sequence of legal commands leaves the model consistent | State-machine gaps, race conditions |

If you cannot state such a rule, property testing degenerates to "random inputs don't
crash" — useful only as fuzzing.

## Writing a good property

1. **State the invariant precisely before writing the property.** "Serialization
   roundtrips any invoice" — including which fields are preserved exactly, which are
   normalized, and which may degrade.
2. **Constrain the generator to meaningful inputs, then widen.** Start with the
   documented domain (positive quantities, known currencies), get green, then remove
   constraints one at a time — each removal that survives is knowledge; each that fails
   is a real bug with a shrinking repro.
3. **Expect shrinking to be the whole payoff.** A failing property that shrinks to
   "quantity = -1, currency = '€£'" is a bug report no example test would have written.
4. **Reproduce failures deterministically.** Record the seed and the case; replay it as
   a pinned example test so the fix is verifiable forever.

## The model-based pattern for stateful systems

For lifecycle-heavy code (a payment state machine, a session store):

1. Build a trivial *model* — a dict, a list, plain code with no cleverness.
2. Generate random legal (and some illegal) command sequences.
3. After each command, run it against both the real system and the model; assert the
   observable state matches.
4. On mismatch, shrink the *sequence* — the minimal command list is the failing
   scenario.

The model is the test's oracle; its simplicity is the point. If your model needs
mocks, it is not a model, it is a second implementation.

## Fuzzing for hostile inputs

Where properties assert correctness, fuzzing asserts robustness under attack-shaped
input:

- **Structured fuzzing**: generate malformed inputs from the format's grammar —
  truncated files, wrong magic bytes, deep nesting, length-field lies, duplicate keys.
- **Coverage-guided fuzzing** (AFL++, libFuzzer, Jazzer, go-fuzz): let the fuzzer run
  unattended against parsers, deserializers, and anything reading untrusted bytes.
  Seed the corpus with real captured traffic.
- **API fuzzing**: send malformed JSON, absurd sizes, unicode confusables, duplicate
  fields, wrong content types, and slow-loris-style pacing at your endpoints; assert
  graceful errors, not stack traces.
- **Resource exhaustion**: inputs sized at the documented maximum × 10 and the maximum
  ÷ 1 — both must behave.

Run fuzzing campaigns in batch (nightly, or before releases on changed parsers), not
on every commit — minutes-long budgets per target per run, with findings triaged like
bugs, not logged like noise.

## Cost and placement in the pyramid

Property and fuzz tests sit at the unit/integration boundary: fast generators run in
the commit suite; slow campaigns run nightly. Budgets:

- Commit-stage properties: seconds to a low minute per property, capped iterations.
- Nightly campaigns: 5–30 minutes per target, unattended, findings to a triage queue.
- Any property that flakes gets its seed pinned — a property test must never be
  "randomly failing," because then it is randomly believed.

## Properties as executable specification

The durable value: a property file is a spec that runs. "Every state transition leaves
an audit event" or "no sequence of legal API calls can leave an order both captured and
voided" is exactly the sentence you would write in a design doc — except it is checked
on every build. For money- and safety-adjacent modules, one stateful property per
critical invariant is the highest-value hour of test writing in the codebase.

## Common failures

- **Testing the generator instead of the code.** If the property only ever feeds the
  function values it trivially handles, it proves nothing; widen deliberately.
- **Weak oracles.** "Doesn't throw" for a parser is a fuzz check, not a property; pair
  it with roundtrip or an oracle.
- **Non-deterministic tests in the merge gate.** Unseeded generators or real time
  inside properties produce the worst kind of flake: intermittent, unshrinkable,
  unbelieved.
- **Property sprawl.** Five properties per trivial function is ceremony. Reserve
  properties for genuine invariants over genuinely unbounded spaces.

## Quick selection guide

- Parsers, codecs, serializers → roundtrip property + structured fuzz.
- Pricing, totals, accounting → invariant + oracle properties.
- Handlers, jobs, migrations → idempotence properties.
- State machines, sessions, carts → model-based stateful property.
- Anything reading untrusted bytes → coverage-guided fuzz campaign, batch-run.