# Risk Assessment

A plan is a set of bets; a risk register is the acknowledgment of the bets, priced. This document is a working checklist for finding the risks that actually kill small businesses, running a pre-mortem, and writing mitigations that exist outside the plan document — because a mitigation that lives only in the plan is a wish, not a control.

## Kill risk versus friction

Sort every risk into one of two classes first; they get different treatments.

- **Kill risk:** can end the business or its founder's ability to continue — a client concentration collapse, a legal or tax failure, burnout, cash-out, a health event, a reputational breach.
- **Friction:** costs time, money, or morale but does not end the business — a lost proposal, a late payment, a slow tool.

Planning time follows the 80/20: most effort on kill risks, one line each for friction. Businesses die from the first class, not the second, and yet plans spend their risk sections on the second because it is more comfortable to write.

## The kill-risk checklist

Walk this list explicitly for every plan. Each item is a question with a yes/no/unknown answer; every "unknown" becomes an action.

1. **Concentration.** Does any client, channel, or supplier exceed 40 percent of revenue? What happens in the 30 days after losing it — name the actions, not the feelings.
2. **Cash.** What is minimum projected cash, in which month, and what is the agreed cut list if actual cash touches it? A cut list written in advance is a decision made calmly; unwritten, it is a panic made later.
3. **Founder dependence and health.** What stops if the founder is out for three weeks? Which deliverables stall, which income stops, which client notices first?
4. **Compliance and tax.** Registration, licensing, insurance coverage, sales tax or VAT obligations, estimated tax provisioning. Failures here are slow, silent, and terminal; "unknown" answers are unacceptable on this line.
5. **Reputation.** What single public failure would most damage the business — a botched flagship deliverable, a missed deadline with a visible client, a data or confidentiality lapse?
6. **Demand shift.** What change in buyer behavior or tools would halve demand for the core offer within a year — a platform change, a cheaper substitute, an economic contraction in the segment?
7. **Legal exposure.** Contracts without limitation-of-liability terms, work done without written agreement, IP ownership ambiguity in deliverables.
8. **Key-person or key-asset loss.** The single laptop, the single proprietary process, the one subcontractor who actually holds the client relationship.

The output is not prose — it is the first column of a table. Prose hides risks; a table makes them comparable.

## Likelihood, impact, and honest scoring

Score each risk on likelihood and impact over the plan horizon, on a three-point scale where:

- Likelihood: **likely** (more than half of scenarios), **possible** (roughly 5–50 percent), **unlikely** (under 5 percent).
- Impact: **severe** (kills or maims the plan), **moderate** (derails a quarter), **minor** (annoying, absorbable).

Resist two scoring temptations. First, optimism discounting: risks you personally fear feel "unlikely" because feeling them is unpleasant — score from evidence and base rates, not comfort. Second, precision theater: "possible" is more honest than "23 percent" invented from nothing. A three-by-three grid (severe/likely in the corner) beats a heat map with invented decimals.

Anything scoring severe-and-likely must leave the register with either a funded mitigation or an explicit written acceptance naming what the plan does differently. Severe-and-likely risks that get neither are the defining marker of an amateur plan.

## The pre-mortem

Run a pre-mortem before committing to any major plan or big bet: assume it is twelve months later and the business failed; write the story of why.

Procedure:

1. Set a timer for 15 minutes. Write the failure narrative: "It's [month/year]. The business is dead. Here's what happened..." Be specific — dates, decisions, the moment it went wrong.
2. List every cause the narrative produced; cluster them.
3. For each cluster, ask: was this knowable in advance, and is it preventable, reducible, or unavoidable?
4. Preventable risks get actions scheduled this month. Reducible ones get contingency plans with triggers. Unavoidable ones get acceptance and, sometimes, a plan redesign.

What pre-mortems find that checklists miss: the slow slide (revenue "fine" for months because one client quietly absorbed 70 percent), the silent dependency (the only person who knows how the invoices get paid), the hero assumption (the plan only works if you never get sick), the drift into a market that was shrinking the whole time. Narratives surface mechanism; checklists surface category.

## Mitigations that actually work

A mitigation is a control that exists outside the document. Test each one against three properties:

- **Present:** it exists today, not "once things stabilize."
- **Tested:** it has been used or exercised at least once — you know it works.
- **Owned:** someone is named and a date exists.

Mitigation vocabulary, in ascending order of robustness:

1. **Prevention:** stop the cause — contracts signed before work starts, deposits before calendars fill.
2. **Reduction:** shrink likelihood or impact — a second client channel, a subcontractor bench, a tax account funded monthly.
3. **Contingency with a trigger:** a prepared response that fires on an observable condition — "if cash < 1.5 months of burn, cancel all discretionary spend and open collection conversations the same week."
4. **Transfer:** insurance, fixed-fee contracts with liability caps, escrow arrangements.
5. **Acceptance, written:** the risk stays, the plan says so, the review date exists.

The order matters for honesty: "acceptance" written for a severe risk you merely dislike is a rationalization. Acceptance is for minor risks and for severe ones you cannot affect at acceptable cost — and those deserve a trigger-based contingency anyway.

## The risk register table

Columns: risk | category (kill/friction) | likelihood | impact | early signal | mitigation | trigger | review date. The early-signal column is the one beginners omit and practitioners prize: it converts the register from an annual document into a monthly instrument, because each signal is a checkable condition. Keep the register to 8–12 rows; a 40-row register is a filing system, not a management tool, and unreviewed rows are worse than absent ones.

### Example rows (fictional solo studio)

- Risk: largest client (45 percent of revenue) departs. Category: kill. Likelihood: possible. Impact: severe. Early signal: slower email replies; invoicing contact changes. Mitigation: cap any client at 35 percent; keep two prospect channels active. Trigger: concentration > 40 percent for two consecutive months. Review: quarterly.
- Risk: tax under-provisioning. Category: kill. Likelihood: possible. Impact: severe. Early signal: tax account balance below 25 percent of quarter revenue. Mitigation: transfer 30 percent of every payment to the tax account same day. Trigger: any missed transfer. Review: monthly.
- Risk: founder burnout. Category: kill. Likelihood: possible. Impact: severe. Early signal: two consecutive months under 50 percent utilization with full calendars. Mitigation: capacity buffer; a named subcontractor for overflow. Trigger: second consecutive below-buffer month. Review: monthly.

## Review cadence

Monthly: read the early-signal column only — five minutes. Quarterly: rescore likelihood and impact; add risks the quarter produced; retire ones that evaporated; verify each "present" mitigation is still present. Annually: rebuild the register from the pre-mortem rather than editing last year's — editing accumulates stale rows the way attics accumulate boxes.

## Failure modes

- **The register that no one reads.** Prevented by the early-signal column and the monthly five-minute pass.
- **Friction inflation.** Spending register space on annoyances while kill risks get one line — prevented by the two-class sort before writing anything.
- **Mitigation-in-a-document.** "We will be careful" as a control — prevented by the present/tested/owned test.
- **Optimism discounting.** Scoring by comfort — prevented by scoring from base rates and evidence, and by the pre-mortem narrative, which bypasses comfort entirely.