# Readability and Style — Naming, Function Shape, Comments

Readable code is code the next person can change confidently. In review, readability is
the highest-leverage non-correctness concern: a readability fix saves every future
reader time, and unclear code is where bugs hide. This reference covers the three
readability levers — naming, structure, and comments — and the discipline of keeping
style out of human review.

## Naming

Names are the densest documentation the code will ever have. Review them as promises:

- **Say what, not how or type.** `remainingRetryCount` beats `count` and
  `intRemaining`; `isEligibleForRenewal` beats `flag2`. A name that only restates the
  type (`userString`) is usually a missing domain concept (`displayUserName`).
- **Booleans read as predicates.** `isActive`, `hasChildren`, `canEdit` — the name
  should complete "if ..." naturally in a conditional. `status` where a boolean is
  expected forces readers into the implementation.
- **Functions are verbs with objects.** `computeInvoiceTotal`, not `invoiceTotal` (that
  is a getter) or `doWork`. The name should survive being read aloud in a sentence:
  "we computeInvoiceTotal for each unpaid order."
- **Consistency is a feature.** One concept, one word: `fetch` vs `retrieve` vs `get`
  for the same operation trains readers to expect differences that do not exist. Pick
  the team's verb and note drift as a finding.
- **Scope calibrates length.** Loop index `i` is fine; a three-line-lived variable can
  be terse; anything crossing a function boundary owes the reader a full name.
- **No lies.** The worst names are the ones that are almost right: `getUser` that
  creates users, `list` that filters, `update` that deletes and recreates. A misleading
  name is a correctness finding, not a style one.
- **Avoid encodings and negations.** `notReady` forces double-negative reading
  (`if !notReady`); prefer the positive form. Hungarian prefixes and type suffixes age
  badly; say what the thing is for.

## Function shape

Structure decisions are readability decisions. The review checks the shape, not the
line count:

- **One job per function, stated in the name.** If describing the function needs
  "and," it is two functions (or a pipeline the call site should show).
- **One level of abstraction per function.** A function that orchestrates (parse
  request → validate → call service → map response) should not also contain bit-mask
  arithmetic. Mixed levels are where readers lose the thread; extract the low-level
  chunk under a name.
- **Guard clauses over nesting.** Early returns for invalid cases let the main path
  read top-to-bottom at zero indentation. Deep nesting (`if` inside `if` inside loop
  inside `try`) is a refactor signal: invert the conditions, return early, or extract.
- **Parameters are few and ordered sanely.** Four-plus parameters or same-typed
  neighbors (`update(from, to, amount, currency)` — which is which?) want an options
  object or a named type. Boolean parameters at call sites (`process(order, true)`)
  hide meaning; a named flag type or two functions beat it.
- **Side effects are visible from the signature.** A function named `getX` that writes
  is a lie with a compile-passing alibi. Mutating methods announce it; queries do not
  mutate.
- **Return shape is predictable.** Mixed return types (object on success, `false` on
  failure) push checking onto every caller. Exceptions or result types with one shape
  keep the caller's code flat.
- **Length is a smell only via nesting and jobs.** A 60-line function with one level of
  abstraction and clear sections can be fine; a 12-line function with three jobs is
  not. Read the shape; do not count lines.

## Comments

The test for every comment: *does it carry information the code cannot?*

- **Why-comments earn their line.** Rationale, constraints, links to decisions:
  "hashing here, not on write, because the digest must include the tenant prefix" —
  the code cannot say this. These are the comments review protects.
- **What-comments are deletions.** `// increment counter` above `counter += 1` is
  noise that will drift out of sync and mislead someone. The reference term is a
  "label": restates the code, adds nothing.
- **Doc comments are contracts.** Public functions document contract, not
  implementation: parameters, return, failure modes, and any non-obvious preconditions
  ("caller must hold the lock"). If the contract is unstateable in a few lines, the
  design is the finding, not the doc.
- **TODOs carry owners.** `// TODO: batch these` without a name or ticket is a wish.
  The review converts TODOs into tracked items or deletes them. Date the TODO; a
  two-year-old TODO with no owner is tech debt wearing a costume.
- **Commented-out code is deletion, not documentation.** Version control remembers;
  the working tree should tell the truth.
- **Warning comments state the trap.** "Order matters here: X must run before Y or the
  index build deadlocks" — that is a comment with a job. Add the test that pins the
  ordering if it can be pinned.

## Style: the part tools should own

Everything mechanical is not review material. The dividing line:

- **Tools own:** formatting, import order, line length, quoting, semicolons, trailing
  commas, many naming conventions, unused imports, common dead-code patterns.
  Enforced by formatter and linter, ideally in CI, before review starts.
- **Humans own:** domain-fit names, function shape, comment quality, abstraction
  level, API ergonomics — judgment calls where the tool has no opinion.

In review, style comments follow one rule: **if a formatter or linter could catch it,
it should never reach the author from a human.** Repeated style findings across
reviews are an automation backlog item, not reviewer persistence (see
`references/review-automation.md`).

When a diff violates a *team* convention (documented, agreed), the comment cites the
convention: "team style: services return Result, not raw exceptions — see the style
guide, section 3." Convention enforcement is different from taste expression: it is
consistent, citable, and cheap to automate.

## Review phrasing for readability findings

Readability findings are the easiest to state as taste and the hardest to defend as
need — so state them with their consequence:

- Weak: "this is confusing." (Whose confusion? What cost?)
- Strong: "this reads as updating the order, but it also cancels the payment intent —
  a reader fixing the pagination bug next quarter will not expect that. Suggest
  renaming to `cancelAndUpdateOrder` or splitting."
- The pattern: **name what the reader will misread, and the concrete cost of that
  misread.** If you cannot name the misread, it is a preference — mark it a Nit or
  let it go.

## The readability review pass, in order

1. Read the diff cold, as a stranger. Note every place you reread, backtracked, or
   guessed — each is a candidate finding.
2. Check names against promises (lies first, vagueness second).
3. Check function shape: jobs per function, abstraction levels, nesting depth.
4. Check comments: why-comments protected, labels deleted, TODOs owned.
5. Filter: what is left that a tool could have caught? Move those to the automation
   note; they are not comments for the author.
6. Whatever survives gets severity and the misread-cost phrasing — or gets dropped.
   Restraint is part of the craft.