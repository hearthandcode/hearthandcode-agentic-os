# Performance Review Basics — Hot Paths, Allocations, N+1

Performance review is not about making code fast in general; it is about finding the
shapes that scale badly and the unbounded behaviors that become outages. A reviewer
cannot profile a diff, but a reviewer can recognize the structures that profile poorly —
and demand bounds where bounds are missing.

## First: is this even a hot path?

Spend performance attention where it can matter. Classify the changed code:

- **Hot paths** — executed per-request, per-row, per-message, or in loops: request
  handlers, ORM hooks, serializers, validation on large inputs, scheduled jobs at
  frequency, library functions used everywhere.
- **Cold paths** — startup, config load, admin actions, error reporting, one-time
  migrations. Correctness matters; performance rarely does. Do not spend review capital
  on cold-path micro-efficiency.
- **Amplified paths** — code whose cost multiplies: a helper called in a loop, a
  per-row callback, an N+1-shaped query. These are the dangerous middle: individually
  cheap, collectively fatal.

The review question for each changed path: *what is the cost model as volume grows?*
Constant, linear, or worse — and is "worse" reachable by ordinary use?

## The shapes that scale badly

### Database access

- **N+1 queries.** The classic: fetch a list, then per-item fetch for a relation.
  Signal: a query inside a loop or a lazy-loaded relation dereferenced during
  serialization. Fix: batched fetch, join, or eager-loading — and the review can point
  at the exact line where the loop dereferences.
- **Unbounded reads.** `SELECT *` without LIMIT, list endpoints without page caps,
  exports without streaming. Any read whose size is controlled by the data is a finding
  waiting for the day the table grows. Bound it: page size caps, streaming, cursors.
- **Missing index match.** A new query filtered or sorted on columns with no covering
  index forces a scan. Reviewer check: does the WHERE/ORDER BY match an existing index?
  If not, the diff needs the migration too.
- **Count-heavy pagination.** `COUNT(*)` over large tables per request is a slow
  default; cursor pagination or cached counts are the standard alternatives.
- **Chatty transactions.** Many tiny transactions in a loop, or a transaction held
  across a network call (user think-time inside a transaction is a Blocker — it pins
  locks and connection pool slots).

### Allocations and CPU

- **Allocation in tight loops.** Building intermediate objects, strings, or arrays
  per-iteration where a hoisted buffer or generator would do. Meaningful in per-row
  serialization and hot library code; invisible in cold paths.
- **Repeated invariant work.** Parsing config, compiling a regex, building a lookup
  table, or reconnecting inside a per-request or per-row function. Hoist it. Regex
  compilation in a loop is the perennial example.
- **Quadratic accidents.** List concatenation or membership checks inside loops
  (`x in list` instead of a set), string += building, repeated slicing. The signal is
  nested iteration over the same data without a memo.
- **Copies of large data.** Passing big structures by value through layers, deep-
  cloning objects that were read-only. A reference, a view, or an immutable-by-convention
  pass is usually free.
- **Synchronous work that has an async or batch alternative.** Per-item network calls
  where a batch endpoint exists; per-row HTTP where a bulk API exists; sequential
  independent I/O that could run concurrently.

### Concurrency and I/O

- **Serial I/O in parallelizable work.** Independent calls awaited one at a time in a
  fan-out context; the review marks it Minor-to-Major depending on depth of the fan.
- **Connection/transaction pinning.** Holding a pool connection across slow operations
  starves the pool; the failure shows up as mysterious timeouts under load.
- **Fire-and-forget without bounds.** Unbounded task spawning (one task per item, no
  semaphore) converts a burst into an outage; bounded concurrency is the fix.
- **Cache misuse.** Caching without a key that includes all inputs (wrong data served),
  without TTL or invalidation (stale forever), or caching at the wrong layer (caching a
  cheap computation and paying serialization for it).

## Reviewing performance findings honestly

- **Name the growth, not the gadget.** "This is O(n²) in list size — with 10k invoices
  it is 100M comparisons" is a finding; "this could be faster" is noise. Do the
  arithmetic in the comment; numbers are what survive pushback.
- **Respect the scale budget.** A 5ms function called once a minute is not a finding.
  Ask "what volume makes this hurt?" — if the answer is beyond the product's horizon,
  note it as Nit or leave it out entirely.
- **Benchmarks beat opinions, estimates beat benchmarks-for-small-stuff.** If the
  reviewer cannot estimate the cost with arithmetic, and the path is genuinely hot,
  the finding asks for a measurement before merge, not a rewrite.
- **Suggest the minimal fix.** The batch query, the hoisted parse, the page cap — not an
  architecture migration. Performance review is the wrong venue for redesign; structural
  findings are handoffs (see the SKILL's cross-skill boundaries).
- **Watch the memory shape, not just time.** Unbounded buffers, whole-file reads into
  memory, per-connection caches that never evict — these are the outages that latency
  dashboards miss until the OOM kill.

## Performance smells table

| Smell in the diff | Likely cost shape | First-line fix |
|---|---|---|
| Query or RPC inside a loop | N+1, linear-plus-latency | Batch, join, or eager-load |
| List endpoint with no page cap | Unbounded read | Cap page size; cursor pagination |
| `COUNT(*)` per request on big table | Linear scan per page | Cache count; cursor pagination |
| Regex/config/lookup built per call | Constant waste per request | Hoist to module or app scope |
| `x in list` inside loop over list | Quadratic | Set/dict membership |
| String concatenation in loop | Quadratic in bytes | Join or builder |
| Whole file/body read into memory | Memory proportional to input | Stream; chunk; bound size |
| Transaction held across network call | Pool/lock starvation | Narrow the transaction |
| Unbounded task fan-out | Burst overload | Semaphore/bounded concurrency |
| Cache with input-incomplete key | Wrong data served | Fix the key; test the collision |
| Cache with no TTL/invalidation | Stale forever | TTL plus explicit invalidation |

## What stays out of performance review

- Micro-taste that measurement cannot distinguish at the product's scale (`i++` vs
  `+= 1`, this-or-that array method): out.
- Rewrites of working cold-path code for elegance-as-performance: out.
- Premature machinery (a cache layer, a queue, a read replica) demanded by the reviewer
  without a named scenario: out — that is architecture, and it needs an ADR, not a
  review comment.

The performance reviewer's oath: *every finding names a growth curve, a reachable
volume, and a minimal fix — or it stays silent.*