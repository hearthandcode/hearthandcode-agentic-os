# Review Case Studies — Three Realistic Diffs, Three Reviews

Three composite cases shaped from common industry experience — a small clean-looking
diff with a hidden logic bug, a feature diff with an authorization hole, and a refactor
that quietly changed behavior. Each shows the workflow applied and the report produced.
Names and code are illustrative; the failure patterns are real.

## Case 1 — The tidy helper (hidden off-by-one)

**The diff:** 35 lines adding `getActiveSubscriptions(userId, cutoff)`, filtering a
cached list by a renewal date. Tests included. Formatting clean. CI green.

**Intent:** return subscriptions that have not expired as of `cutoff`.

**The review pass:**

- Steps 1-2: intent clear; blast radius small (one caller). The reviewer reads the full
  function including its context — the cache is a module-level list shared across
  requests.
- Step 3 correctness pass finds it with boundary math: the filter is
  `sub.renewsAt <= cutoff`, but the domain rule (stated in the caller) is "active
  through the end of the renewal day." A subscription renewing at `2026-05-01T00:00Z`
  is dead by `2026-05-01T00:00Z` under this code — the customer's last day is gone.
  The fix is `<` ... wait, no: the *intent* is "active through the renewal date," so
  the comparison belongs at day granularity, not instant granularity.
- The reviewer writes the failing case into the comment: `renewsAt = 2026-05-01T00:00Z`,
  `cutoff = 2026-05-01T12:00Z` → returned expired, customer overcharged on a renewal
  check.
- Step 4 security pass: clean. Step 5 performance: the function re-filters the whole
  cache per call — fine at current scale, Nit with a named volume.
- Step 7 tests: the new test's `cutoff` sidesteps the boundary (uses noon, renewal at
  midnight) — the test passes on buggy code. Finding: Major.

**The verdict:** request changes. Blocker? Debatable — the reviewer grades Major with a
note that if the caller feeds midnight-ish cutoffs it is a Blocker; the author
confirms the caller can, and it becomes a Blocker in round two. Honest severity
updating in action.

**The lessons:**

- Small, clean diffs hide boundary bugs as well as large ones do; size is not risk.
- The bug was found by doing the arithmetic in writing, not by vibes — the checklist's
  boundary-condition section exists for exactly this.
- Severity can update as facts arrive; the protocol (state uncertainty, update on
  evidence) handled it without drama.

## Case 2 — The admin endpoint (authorization hole)

**The diff:** 140 lines adding `GET /admin/metrics` plus a metrics service. The
description: "ops wants usage stats; internal only."

**The review pass:**

- Steps 1-2: intent clear. The diff registers the route with a comment "internal only
  for now." The reviewer's security pass (Step 4) asks the operational question: how
  is "internal" enforced?
- Finding (Blocker): the route has no authentication middleware and no role check —
  "internal" is enforced by the URL being unlisted. The metrics service returns
  customer names, counts, and revenue figures.
- Second finding (Major): the metrics service queries all tenants in one connection
  with no read-replica routing — fine today, flagged with the volume that changes it.
- Third finding (Minor): response includes raw SQL timing histograms — useful, but
  should exclude statement text (leaks schema details).
- The author's pushback: "nobody outside the VPN can reach it." The reply: the
  security reference's rule — checks live at the enforcement layer, and perimeter
  assumptions ("it's internal") have a documented failure rate; the fix is three
  lines of middleware. Disagree-and-commit would have applied if the author still
  disagreed after the evidence; the author did not.

**The verdict:** request changes. The fix lands: middleware added, plus a test that
asserts the endpoint 403s without the ops role.

**The lessons:**

- "Internal only" is not an authorization system; the checklist's authorization items
  exist because this exact hole ships constantly.
- The finding offered the fix (middleware + test), which converted a two-day debate
  into a same-day change.
- The test asserting the 403 is the institutional memory: future refactors that drop
  the middleware fail CI, not an audit.

## Case 3 — The behavior-changing refactor (silent semantic drift)

**The diff:** 400 lines, "refactor: extract shared validation into a service." No
behavior changes claimed. Tests updated to match new signatures.

**The review pass:**

- Steps 1-2: refactor claim makes behavior-preservation the review's central question.
  The checklist item: is there a test that pins the behavior? The updated tests changed
  assertions in three places — the reviewer compares old vs new test expectations and
  finds the drift.
- Finding (Blocker): the extracted validator now treats empty-string input as "missing
  field" (raising the missing-field error) where the old inline code treated it as a
  provided-but-invalid value (different error code, different user message). Two
  downstream API consumers branch on that error code; the refactor would have changed
  their behavior silently.
- Second finding (Major): the refactor hoisted validation before authorization —
  invalid requests from unauthorized callers now get validation errors instead of 403,
  leaking field requirements to unauthenticated probes. Information disclosure, low
  severity but real; the fix reorders the middleware chain.
- Third finding (Minor): the "shared service" gained a config dependency, coupling it
  to app startup — noted as a design smell with a handoff suggestion.
- The author's question: "isn't any behavior change acceptable in a refactor?" Answer:
  the principles reference's rule — refactors preserve observable behavior; intentional
  changes are new diffs with their own intent statements.

**The verdict:** request changes. After fixes: approve.

**The lessons:**

- Refactors are the highest-risk category for silent drift because nothing "fails" —
  the review's job is to diff semantics, not just syntax. Old-vs-new test assertions
  are the reviewer's best tool.
- Error-code semantics are API contract; changes to them are behavior changes even
  when the type system is happy.
- The middleware-order finding shows how refactors move security properties without
  touching "security code" — the security pass is not skippable on refactors.

## Cross-case patterns

- **All three bugs were found by procedure, not intuition:** boundary math, the
  authorization checklist, the semantic diff of refactor behavior. The checklist
  catches what impression misses.
- **All three authors were competent and cooperative.** The defects were ordinary
  engineering — which is why review runs on every diff, not just suspicious ones.
- **Severity moved as evidence moved** (Case 1) and pushback was answered with
  evidence (Case 2) — the severity scale and the disagreement protocol are what make
  honesty cheap.
- **Every case ended in follow-ups that outlived the review:** a boundary test, an
  auth-middleware test, an error-code contract note. Reviews compound when their
  dispositions are recorded; otherwise they are conversations that evaporate.

## A note on using these cases

Run your first real review against the checklist, then read these cases and compare
your findings list against each case's findings. The gap is your calibration signal:
missed classes become checklist items you personally re-read; over-flagged taste
becomes restraint. The case studies are mirrors, not just examples.