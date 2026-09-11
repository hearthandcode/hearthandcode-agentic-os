# Review Checklist — Correctness, Edge Cases, Error Handling

Work this checklist over the changed lines and their context. Not every item applies to
every diff; apply judgment, but a skipped item should be a decision, not an accident.
Items are grouped so a pass can be split across sittings. Severity suggestions are
defaults — raise them when data, money, or security is involved.

## A. Intent and scope

1. [ ] The diff does what its description says — every claim in the PR description is
      verifiable in the code. *(Unverifiable claims: ask before approving.)*
2. [ ] The diff does nothing the description does not mention — no smuggled refactors,
      no unrelated fixes riding along. *(Ride-alongs are review-opacity bugs; ask for a
      split.)*
3. [ ] The change's blast radius matches its description — touched callers, endpoints,
      jobs, and tests are the ones you would expect. *(Surprise radius is a Major.)*
4. [ ] Refactors preserve behavior and are verified by tests that pin the behavior.
5. [ ] Dead code, commented-out code, and debug scaffolding are absent from the diff.
6. [ ] Feature flags or config gates exist for changes that need staged rollout, and
      their default states are correct for every environment.

## B. Correctness

7. [ ] Loop bounds are right at every edge: first iteration, last iteration, zero
      iterations. *(Off-by-one here is the classic; do the boundary math in writing.)*
8. [ ] Off-by-one checks on all index arithmetic: `<=` vs `<`, 0-based vs 1-based
      conversions, slice and range ends. *(The single most common shipped bug class.)*
9. [ ] Null/None/nil handling: every dereference of a nullable value has a guard, and
      the guard's failure path is defined (not a silent swallow).
10. [ ] Empty collections: aggregation over nothing returns a defined value, not an
     exception or a meaningless default like `0` for an average.
11. [ ] Integer edge cases: overflow on accumulation, division by zero, negative
     inputs where the code assumes positive, integer vs float division semantics.
12. [ ] Operator precedence and short-circuit logic match the intent; parenthesize
     anything non-obvious. *(Readers misparse mixed `and`/`or` constantly.)*
13. [ ] State mutation is safe: shared/global state is not mutated on paths that can
     run concurrently; iteration does not mutate the collection being iterated.
14. [ ] Async/concurrency code: race conditions considered, locks held no longer than
     needed, awaits not forgotten in a branch.
15. [ ] Time and timezone handling: timestamps stored UTC, converted only at display
     boundaries, DST transitions and leap handling not hand-rolled.
16. [ ] Float comparisons use tolerance, not `==`; money is integer cents or decimal
     types, never binary floats.
17. [ ] Encoding and normalization: strings compared after agreed normalization; UTF-8
     boundaries handled at I/O edges.
18. [ ] Resource cleanup: every open file, connection, lock, or transaction is closed
     on all paths, including exceptions (try/finally, defer, context manager, RAII).
19. [ ] Error paths match happy-path rigor: failures produce correct state, useful
     errors, and no half-applied writes (transactions or idempotency where needed).
20. [ ] Return values on every branch are coherent: no path returns success-shaped
     garbage or error-shaped success.

## C. Boundary conditions (apply to every input the code accepts)

21. [ ] Zero/empty input.
22. [ ] One element (the `> 1` assumption bug).
23. [ ] Many elements — what is the behavior at 10x expected volume?
24. [ ] Maximum-size input: strings at field limits, payloads at message limits,
     pages at max size. *(Unbounded is a Major.)*
25. [ ] Weird-but-legal input: unicode, negative numbers where sign is meaningless,
     duplicate keys, whitespace-only strings.
26. [ ] Illegal input: rejected explicitly with the right error, not by crashing or
     by silently coercing.
27. [ ] Concurrent duplicates: the same request twice, the same resource edited by two
     actors — double-submit, lost-update, and idempotency considered.
28. [ ] Clock and ordering assumptions: does anything break if events arrive out of
     order or a clock steps backward?

## D. Error handling

29. [ ] Errors are handled, not swallowed: no empty catch blocks; swallowed exceptions
     carry a comment with the reason and the risk accepted.
30. [ ] Error messages carry context (what failed, with what key values) without
     leaking secrets or user data into logs.
31. [ ] Retries exist only where the operation is idempotent or made idempotent; retry
     storms on non-idempotent endpoints are a Blocker.
32. [ ] Failure of a dependency degrades sensibly: timeout set, fallback defined, and
     the user-visible behavior on failure is specified.
33. [ ] Partial failure leaves consistent state: multi-step writes have a rollback or
     compensating action, and "half-done" is impossible or detectable.

## E. Tests

34. [ ] Behavior changes come with tests that fail without the change.
35. [ ] Tests assert behavior, not implementation details (no pinning of call order
     where order is incidental).
36. [ ] Boundary conditions from section C appear as test cases — at minimum empty,
     one, many, and the specific edge the change touches.
37. [ ] Tests are deterministic: no sleeps, no dependence on wall-clock ordering, no
     real network without a harness designed for it.
38. [ ] Test names say what behavior they pin, so a future failure reads as a sentence.

## F. Security and data (see the security reference for depth)

39. [ ] Every new input path is checked against the injection classes relevant to its
     sinks (SQL, shell, HTML/JS, path, URL).
40. [ ] Every new data-access path carries the authorization check the old path had —
     and the check is at the enforcement layer, not the UI.
41. [ ] No secrets in the diff, the logs, or the fixtures.
42. [ ] PII handling: new fields or logs that carry personal data are minimized,
     justified, and documented.

## Using the checklist

- **Depth scales with risk.** Auth/payments/data-deletion code gets every item read
  against the code; docs and formatting get section A and the tooling gates.
- **Do the math in writing** for any bounds or pagination arithmetic — write the small
  case down (`n=3, pageSize=2, page=2 → ?`) before believing the code.
- **N/A is a valid mark; silence is not.** Mark items N/A with a reason so a second
  reviewer can verify the *marks* rather than redo the whole pass.
- **Recurring misses become automation.** Any item that three consecutive reviews flag
  belongs to a linter or CI gate, per `references/review-automation.md`.
- **The checklist is a floor, not a ceiling.** Domain-specific items (HIPAA fields,
  financial rounding, GPU memory) belong in the team's extension of this list.