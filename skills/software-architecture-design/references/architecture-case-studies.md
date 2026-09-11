# Architecture Case Studies — One Monolith, One Modular, Compared Over Time

Two designs, both realistic composites drawn from common industry experience: a ticketing system that began as a layered monolith and accreted until its seams dissolved, and a workforce-scheduling platform that began modular and kept its seams only through enforced ownership. Neither is a horror story; both are normal outcomes of normal pressures. The value is in watching *which specific decisions* produced each trajectory.

## Case 1 — Meridian: the monolith that dissolved its own seams

**Context.** A 2019-era ticketing system for live events: events, seat maps, orders, payments, refunds. Two developers, deadline-driven, Spring Boot, one Postgres, rendered server-side. Initial design: textbook layered monolith — controllers / services / repositories per feature area. Sound choice at the time; nobody should second-guess it.

**Years 0-1: the layers worked.** Features shipped weekly. The service layer held the rules; repositories held SQL. Tests covered pricing and refunds. The discipline held because two people can hold a whole system in their heads.

**Year 2: the shortcuts.** Under a deadline (a viral event, 40x signups), a controller called a repository directly "just this once" for seat availability. The next developer, reading that code, learned the real rule: the layers were a convention, not a boundary. Within a year: SQL in controllers, business rules in repositories (query-shaped rules: "if the seat map row says X, the order is Y"), and a shared `UtilService` that everything imported. Seat-availability logic — the hottest, most correctness-critical logic in the system — existed in four places with subtly different rules.

**Year 3: the data model became the architecture.** The `orders` table accreted columns for every feature: `promo_code_snapshot`, `resale_flag`, `refund_state_v2`, eleven nullable columns whose semantics lived in comments. Nobody could change `orders` without a full-system regression sweep, because reads of those columns happened everywhere — the table had become the integration point between all features. Adding a resale flow took a quarter; the original estimate was two weeks.

**Year 4: the extraction attempt.** Leadership commissioned a microservices split. The team carved along the only visible lines — the technical layers — producing a "payments service" that contained payment *and* refund *and* promo logic, because the domain boundaries had never existed in the code. The split added network hops and distributed transactions to the existing tangle. It was partially rolled back; the durable fix was the boring one: re-draw domain boundaries *inside* the monolith first, move behavior behind interfaces, then extract only what failure-isolation demanded (payments).

**The causal chain, stated plainly:**

1. One unenforced dependency violation → the boundary's authority collapsed (boundaries are conventions only while someone enforces them).
2. The shared table became the real interface → every feature coupled to a mutable schema.
3. No ADRs existed → the extraction repeated the same mistake at higher cost, because there was no record of which boundaries were load-bearing.

**What would have changed the trajectory.** Not microservices in 2019. Three cheap things: (a) an enforced dependency rule — even a test that fails the build when a controller imports a repository; (b) ownership discipline on `orders` — a single `Ordering` module that all order writes pass through; (c) ADRs for the two or three truly costly decisions (seat-map consistency, order schema evolution). The failure was never "monolith"; it was "monolith with no boundaries and no memory."

## Case 2 — Lattice: the modular design that kept its seams

**Context.** A workforce-scheduling platform (shifts, availability, compliance rules, payroll export) built 2020 by four engineers who had lived through a Meridian. Design: **modular monolith, hexagonal inside.** Five modules — Scheduling, Availability, Compliance, PayrollExport, Accounts — each with a declared interface; module-to-module calls only through those interfaces; one module per domain, enforced by an architectural test that fails the build on cross-module internal imports.

**The decisions that mattered:**

1. **Interfaces before implementation, per module.** Each module's interface was designed and reviewed before its internals were written. When Scheduling's internals were rewritten in year 2 (from a rule-engine to a solver), no caller changed. The rewrite took three weeks; the Meridian equivalent took a quarter.
2. **Data ownership from day one.** Each module owned its tables; cross-module reads went through interfaces. When PayrollExport needed shift data, it called Scheduling's export port — and when volumes grew, Scheduling added a batch-friendly read model without PayrollExport noticing. No shared mutable tables anywhere.
3. **ADRs with revisit triggers.** Eleven ADRs by year 2. The load-bearing one: "scheduling engine is in-process; extract only if solver CPU time starves request threads." The trigger (p99 solver time > 2 s) fired in year 3; extraction of the solver to a worker process took ten days because the module already had an interface and no shared tables. The extraction was a mechanical consequence of an earlier decision, not a project.
4. **The test that enforced the architecture.** A module-boundary test (static analysis over imports) ran in CI. It failed eight times in two years — eight dead boundary violations caught before accretion. This is the single highest-leverage artifact in the case: the architecture existed in the build, not in the slide deck.

**What it cost.** Honest accounting, because modular designs are marketed as free: interfaces were designed twice (the first versions guessed wrong about batching and were revised); the boundary test took a week to build and maintain; some call paths have mapping boilerplate that a tangled design would not need; and for the first six months the five-module structure was over-engineered for a product with forty users — Scheduling and Availability could have been one module until collaboration features landed. Modularity delayed features by weeks, once, at the start.

**Where Lattice nearly failed.** Year 3: a "quick" cross-module table read was merged during an incident weekend (the boundary test was skipped in a hotfix path). It was found in the next quarterly review — the checklist's data-ownership points (17-18 in the 40-point review) — and removed within a sprint. The lesson is not "never break the rule"; it is *the review existed to catch the break, and the fix was cheap because the drift was one commit old*. Seam-keeping is a maintenance activity, not a launch event.

## Side-by-side

| Dimension | Meridian | Lattice |
|---|---|---|
| Initial style | Layered monolith | Modular monolith (hexagonal inside) |
| Boundary authority | Convention; eroded in year 2 | Enforced by CI test; survived 3 years |
| Data model | Shared `orders` table = real interface | Per-module ownership; reads via ports |
| Decision record | None | 11 ADRs with measurable revisit triggers |
| Cost of a major rewrite | A quarter, high risk | Three weeks, low risk |
| Cost of extraction | Rolled back; wrong seams | Ten days along a prepared seam |
| Total overhead paid | Late, compounding, unpriced | Early, visible, bounded |
| Failure mode | Boundaries as folders | One drifted commit, caught by review |

## What transfers to your design

1. **Enforcement is the boundary.** A seam that nothing enforces (test, review, module system) is a folder with ambitions. Decide the enforcement mechanism in the same ADR that draws the boundary.
2. **Data ownership is the deepest seam.** Both cases turn on who writes which tables. Get ownership right and later restructuring is cheap; get it wrong and every later change is surgery.
3. **ADRs made Lattice's extraction boring.** The revisit trigger converted a potential "should we split?" debate into an execution of a recorded plan. Write triggers for the decisions whose reversal you can foresee.
4. **Modularity has an entry cost; Meridian's costs were deferred and compounding.** Neither is free. The honest comparison is not "cost now vs. cost never" but "cost now vs. cost later with interest."
5. **Scale the ceremony to the team and the stakes.** Lattice's five modules were one too many at forty users. Boundaries should arrive with the pressures that justify them — but the *mechanism* (interfaces, ownership rules, the CI test) is cheap to establish early and expensive to retrofit.

6. **Read failures as information about boundaries.** Meridian's rollback taught the team where the real seams were — none. When a change escapes its expected blast radius, treat it as a boundary report and write down which seam failed to contain it. Both case studies' final architectures were shaped less by their initial designs than by their teams' honesty about these reports.