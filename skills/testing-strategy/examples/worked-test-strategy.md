# Worked Test Strategy — ShopPay Checkout Module, Zero Existing Tests

Companion to §06 of SKILL.md. Shows the full strategy pass on a payment-checkout
module with no tests, following `templates/test-plan-template.md` section by section.
The interesting decisions are called out in **bold decision notes**.

## 1. Context

**Module:** ShopPay — checkout module in the `shop` monorepo (`shop/packages/shoppay`).
Owns cart totals, pricing rules, payment authorization via the Stripe-like PSP
"PayCo", capture, void, and refund. Written by two engineers over eight months.
**Zero existing tests.** No CI beyond lint.

- **Failure consequence:** money. A double capture, a missed refund, or a silently
  wrong total is a support incident, a settlement discrepancy, and in aggregate a
  trust problem. This is the highest-consequence module in the product.
- **Top quality attributes:**
  1. Correctness of totals under every pricing combination (money).
  2. State-machine integrity: no capture-after-void, no double refund (money + audit).
  3. Contract stability with PayCo and with the storefront API (external consumers).
- **Traded away (explicit):** no performance suite this pass (traffic is small; revisit
  at 10× load); no browser-level E2E for the storefront UI in this plan (frontend team
  owns theirs); PSP production keys never used in tests — sandbox only.

**Decision note:** the consequence statement drives everything later. "Money" is why
the state machine gets property tests and why E2E exists at all. For a settings page,
the same workflow would produce a much smaller plan.

## 2. Current state

| Question | Answer |
|---|---|
| Existing tests | None. Not even a runner configured. |
| Seams | Almost none: PSP client hardwired via `new PayCoClient(apiKey)`; clock via `Date.now()` scattered; repository is a thin class over SQL — injectable but nobody injects it |
| Runner | Team standard is pytest (Python service); layout convention `tests/unit`, `tests/integration` exists in sibling modules |
| CI | Lint only, on push, ~40 s |
| Flaky tests | None (nothing exists to flake) |

**Decision note:** seam work is the first work item, not a test item. The plan lists
three seams as tasks with the module owner assigned: PSP client interface, clock
interface, and (already fine) repository interface. Roughly a day of work total. This
is the moment to say it out loud: without it, the entire plan below is unwritable.

## 3. Module analysis

Behavior inventory (abridged to representative rows; the real table had 26 behaviors):

| ID | Behavior | Source | Risk | Technique | Level |
|---|---|---|---|---|---|
| B1 | Total = Σ(items) − discounts − fees; rounding half-even to cents | Pricing spec §2 | H | BVA + INV | Unit |
| B2 | Member 10% vs coupon: best-of applies, never stacks | Pricing spec §2.3 | H | DT | Unit |
| B3 | Zero/negative quantity cart rejected with error E1 | API spec | M | EP | Unit |
| B4 | `draft → authorized` on PayCo success | Payment spec §1 | H | ST | Integration |
| B5 | `authorized → captured` exactly once (idempotent) | Payment spec §1 | H | ST + idempotence | Integration |
| B6 | Capture after void rejected with error E3 | Payment spec §1 | H | ST (illegal) | Unit |
| B7 | Refund ≤ captured amount; partial refunds accumulate | Payment spec §2 | H | BVA + ST | Integration |
| B8 | PayCo timeout → order stays `draft`, retry allowed | Ops runbook | H | fault injection | Integration |
| B9 | PayCo 5xx → user-visible error E2, no partial state | API contract | H | fault injection | Integration |
| B10 | Webhook replay of `payment.succeeded` is a no-op | Payment spec §3 | H | idempotence | Integration |

**State machine** (drawn before any test written):

```
draft ──authorize──▶ authorized ──capture──▶ captured ──refund──▶ refunded
  │                     │                                        ▲
  └─void─▶ voided ◀──void──┘              captured ──partial refund──▶ partially_refunded
```

Illegal transitions worth naming: capture from `draft`/`voided`/`refunded`, authorize
twice, refund > captured, refund after full refund, void after capture. **Decision
note:** the illegal-transition list was generated mechanically from the matrix's empty
cells — 19 of them — and became the case list directly.

**Dependencies:** PayCo (third-party — stub/contract), Postgres (owned — real in
integration), clock (seam), storefront API consumers (owned — contract).

## 4. Allocation

Payments logic is rule-dense with a thin I/O shell, and the one heavyweight dependency
(PayCo) is vendor-owned: **pyramid, roughly 70/20/10, with E2E capped hard.**

| Level | Scope | Count | Budget | Runs in |
|---|---|---|---|---|
| Unit | pricing, validation, transition guards, error mapping | ~90 | ≤ 60 s | Commit |
| Integration | Postgres repository; PayCo stub-peer incl. faults; webhooks; composition root | ~45 | ≤ 5 min | Integration stage |
| Property | totals invariant; stateful "never captured+voided"; idempotence of capture/refund | 4 | ≤ 2 min | Commit (nightly wide) |
| E2E | 5 flows, sandbox PayCo, seeded accounts | 5 | ≤ 10 min | Nightly |

**Decision note:** the stub-peer suite for PayCo covers *our client's* behavior under
PayCo's documented failures (timeout, 5xx, malformed body, retry-after-partial) — the
vendor is not being tested, our handling is. One contract test replays recorded
sandbox responses to catch drift.

## 5. Cases (representative, from the techniques)

Decision table for B2 (discounts), four rules → four unit cases + the tie-break case
the table exposed as ambiguous — raised to the product owner before writing tests;
answer: best-of, coupon wins ties. Boundary sweep for B1: `0.005` rounding at
cart totals `x.005/x.015` against PayCo's rounding — found the two disagree; spec
amended to "half-even, computed by ShopPay, never by the client." State cases for
B4–B7: 8 legal transitions as integration tests, 19 illegal transitions as unit tests
on the guard layer. Fault matrix for B8/B9: timeout, 503-twice-then-200, malformed
JSON, rate-limit 429 — four stub-peer scenarios each with asserted end-state and
error mapping.

Every case row carries provenance (`DT rule 4`, `ST illegal c→v`, `BVA x.005`) so
review checks classes, not vibes.

## 6. Data

- `factories.py` builders: `make_cart()`, `make_order(status=...)`, `make_payment_event()`;
  defaults schema-valid, tests override explicitly.
- Postgres via ephemeral container per CI run; schema migrations applied as part of
  setup — migrations tested as part of the plan.
- PayCo sandbox accounts: three seeded test accounts (basic, member, member+coupon),
  credentials from CI secret store, never committed.
- **No production data. Anywhere. The anonymization pipeline does not exist for this
  module and was not needed; builders cover it.**

## 7. Stages and gates

| Stage | Contains | Trigger | Budget | Gate |
|---|---|---|---|---|
| Commit | unit ~90 + property 4 + affected integration | every push | ≤ 10 min | blocks merge |
| Integration | full integration ~45, containers | pre-merge | ≤ 15 min | blocks merge |
| Nightly | E2E 5 + wide property seeds + PayCo contract replay | scheduled | ≤ 20 min | alerts |
| Release smoke | deploy health + guest checkout sandbox flow | release RC | ≤ 5 min | blocks release |

Flake policy: named owner (test-infra rotation), 1-day quarantine SLA, re-entry after
100 clean nightly runs, zero blanket retries. Reporting: escape-rate review monthly —
every production payment bug must name the level that should have caught it.

## 8. Exit criteria

All 26 behaviors case-covered (B1–B26); all 19 illegal transitions green; stateful
property live in the commit stage; reconciliation check (ShopPay totals vs PayCo
settlement report) running as a daily job — **added after the first plan review
flagged that nothing verified module totals against the PSP's own books.** Deferred:
performance suite (ticket PERF-14, revisit at 10× load), 3DS challenge E2E (frontend
team's flow; contract only).

## What the pass caught before any test was written

1. The discount tie-break ambiguity (decision table review).
2. The rounding-policy disagreement with PayCo (boundary sweep).
3. The missing reconciliation story (plan review).
4. Three required seams that didn't exist (current-state analysis).

Four defects and three structural gaps found by planning alone — the cheapest point
in the entire exercise, and the reason the workflow insists on analysis before cases.