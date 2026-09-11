---
name: business-planning
description: Load this skill when a founder, freelancer, or small-business owner needs to plan a business — validating an idea, pricing services, sizing a market, building a 12-month financial sketch, or deciding whether a venture is worth starting at all. It produces decision-ready planning artifacts: a one-page plan, a quarterly financial sketch with break-even and cash-runway math, a tested assumption log, and a risk register. Use it for new ventures, pivots, or annual plan refreshes; skip it for execution-level work like marketing calendars or visual design. The method favors tested assumptions and honest arithmetic over polished projections.
---

# business-planning

## 01 — Purpose

This skill turns "I think I have a business" into a plan you can act on, be corrected by, and show to
the people it affects. It exists because most early business documents fail in predictable ways:
revenue lines with no named buyer, prices that ignore the cost floor, plans that are profitable on
paper and out of cash in month four, and risk sections that catalog annoyances while the actual kill
risks go unwritten. Every step of the workflow exists to prevent one of those named failures, not to
fill pages.

The craft being taught is deciding, not documenting. A strong plan is short, arithmetic-forward, and
revisable; a weak one is long, adjective-forward, and defended. When you finish a run, the test is
whether a stranger could read the summary and repeat back what the business does, who buys, and why it
wins — and whether every number in it can show its work.

This skill owns three outcomes and is judged on them:

1. **A bottom-up revenue basis and market size.** Arithmetic you can show — reachable buyers through
   channels you actually operate, a justified close rate, priced offers, expected volume per quarter —
   so the year-one number is derived rather than wished. If the arithmetic cannot be shown in one line,
   the number does not belong in the plan.
2. **A 12-month financial sketch that names its own danger.** Quarterly revenue by line with one-time
   and recurring separated, a cost structure with the founder's wage priced as a cost, a founder-level
   break-even, cash timing with deposits and payment windows mapped, the trough month identified, and
   runway stated in months with a triggered response attached.
3. **A tested core and a priced risk surface.** The three to five assumptions the plan stands on, each
   with the cheapest honest real-world test and a falsification condition written before the test runs;
   plus a risk register where every severe risk carries a present, tested, owned mitigation with an
   observable trigger.

The financial sketch is deliberately a sketch: quarterly granularity, order-of-magnitude confidence,
built so monthly actuals can be dropped beside it and the variance will say which assumption to fix.
Expect to revise it monthly in the first six months. A plan that cannot survive being wrong is not a
plan; this skill builds documents designed to be corrected.

What this skill deliberately does not own: running marketing channels, writing the words, designing the
product surfaces, or building the delivery process. It decides what the business sells, at what price,
to whom, at what margin, and at what risk — and hands clean inputs to the sibling skills that execute.
If a session drifts into those territories, close the drift and route it: the planning artifacts stay
arithmetic-forward, and the execution work gets its own skill.

## 02 — When to Use / When Not to Use

Use this skill when any of the following is true. These are the triggers practitioners actually bring;
each names the situation, not just the topic.

- **A venture is being decided.** Someone is weighing leaving a job, signing a lease, or spending
  savings, and needs the plan that settles the go/no-go question with named assumptions, a runway
  figure, and a resignation rule they can bind themselves to.
- **A service business is being priced.** A freelancer or studio has an offer but no prices — or prices
  set by feel and defended by mood. The cost-floor, market-range, and value-anchor work in step 6
  belongs here, as does the unit logic beneath it.
- **A plan must survive contact with a stakeholder.** The document will be shown to a partner or spouse
  sharing financial risk, a lender, a co-founder, or a first client, and it needs honest numbers,
  visible derivation, and a defensible logic trail.
- **An existing business is pivoting or expanding.** The model worked and now something changes — a new
  service line, a shift from projects to retainers, a second segment, a move to productized offers —
  and the change deserves the same derive-test-schedule treatment as a fresh start.
- **An annual plan refresh is due.** Last year's plan exists and actuals exist; the gap between them is
  the planning input. This skill runs the refresh as a revision with forecasting error visible, not a
  rewrite from a blank page.
- **A lean validation loop is wanted.** The idea is early and cheap tests should run before any full
  plan exists. The one-page plan, the assumption map, and the commitment-test toolkit are the right
  weight — and they are in this skill.

Do not reach for this skill in the following cases. Each non-trigger names the better route.

- **The marketing motions are the subject** — channel calendars, campaign structure, launch sequencing,
  social cadence. Use `marketing-strategy` for channel and positioning strategy,
  `social-media-strategy` for platform cadence, or `content-calendar-planning` for the publishing
  schedule. This skill only sizes demand enough to price and plan; it does not run the channels.
- **The words are the subject** — naming, taglines, website copy, proposal language, pitch narrative.
  Use `copywriting-and-messaging`. Planning decides what the offer is and what it costs; that skill
  decides how it is said.
- **The visuals or product surfaces are the subject** — interface quality, design critique, brand
  look-and-feel, or in-game economy tuning. Use `ui-design-critique` for interface review,
  `design-system-foundations` for system-level visual structure, or `game-economy-balancing` when the
  economy is a game economy.
- **You need raw idea generation**, not a decision about an idea. Use `brainstorming-and-ideation`
  first; when a shortlist exists, bring it here and the workflow will size, test, and price the
  survivors.
- **The operational machine is the subject** — workflows, SOPs, delivery process, tooling, hiring
  mechanics. Use `operations-and-process-design`. Planning sets what must be delivered and at what
  margin; that skill designs how delivery runs day to day.
- **No decision is pending.** If someone wants background reading on "how businesses work" with nothing
  to plan, no skill is needed — a conversation or general reference material serves better, and running
  a full planning workflow would produce an unused artifact. Ask whether a decision is pending before
  building anything.

A useful boundary test: if the next concrete output is a number with arithmetic behind it — a price, a
break-even, a runway figure, a market size, a quarterly target — this skill fits. If it is a calendar,
a sentence, or a screen, one of the siblings above fits better. When several could apply, plan for the
artifact the user acts on next week, then hand off the rest.

## 03 — Inputs and Outputs

### What the user must supply

The workflow degrades gracefully, but every missing input below becomes an explicit assumption in the
plan rather than silently ignored. Ask in this order; stop when resistance appears and record the gap
with a test date instead of pressing.

- **Cash on hand and monthly personal burn** — the two numbers that turn runway into calendar math. One
  figure each. Estimates are acceptable and get marked as such in the sketch.
- **The personal income floor** — what the business must pay the founder monthly, and by when. Usually
  a household commitment. This number drives founder-level break-even and the tax provision line.
- **Delivery capacity** — realistic weekly hours for client or production work, ideally already tested
  against a normal week. Untested estimates are flagged for a capacity test in step 9.
- **The network and channel inventory** — who is reachable and how: contacts, communities, referral
  sources, audiences, past clients. This inventory bounds the bottom-up market size in step 5.
- **The offer as currently imagined** — service lines or products, any existing prices, and evidence
  already collected: past projects, quotes made and their outcomes, pre-orders, signed pilots.
- **Known constraints and commitments** — non-negotiables such as a resignation date, a savings floor,
  an exclusivity clause, a planned absence, or a no-subcontracting rule.
- **The decision the plan must settle** — one sentence. "Can I resign by March?" produces a different
  plan than "What should the studio sell?" or "Should we take the retail account?"

### What the skill hands back

- **A one-page plan** — roughly ten short sections on one page: identity line, customer and wedge,
  offers with prices and unit math, the win reason with proof, a bottom-up revenue goal, 90-day dated
  outcomes, key assumptions with tests, top risks with triggers, metrics, and commitment rules. Built
  from `templates/one-page-plan-template.md`.
- **A full business plan (optional, when stakes warrant)** — the ten-section scaffold in
  `templates/business-plan-template.md`: summary, customer and wedge, offer and pricing table, market
  evidence, business model, the 12-month financial sketch as a quarterly table, metrics and cadence,
  milestones, assumption tests, and the risk register. Six to twelve pages when filled honestly; longer
  means sections 1–3 are undecided.
- **A 12-month financial sketch** — a quarterly table: revenue by line (one-time and recurring
  separated), variable and fixed costs, founder draw, tax provision, net cash flow, and running cash
  balance, with founder-level break-even and the trough month marked, plus a 60-percent-of-plan
  downside case.
- **An assumption log** — the plan's foundations as rows: assumption, why it matters, test,
  falsification condition, result, action taken. This is the artifact that makes the plan correctable.
- **A risk register** — kill risks and friction separated, each row carrying likelihood, impact, early
  signal, mitigation, trigger, and review date; plus the commitment rules list with triggers.
- **A metrics starter** — one North Star, three to five input metrics with derived targets, and two or
  three health metrics with safe ranges, plus the monthly and quarterly review rhythm on the calendar.
- **A worked example to calibrate against** — the Aurora Creative run in
  `examples/worked-business-plan.md`, with the completed plan, financial sketch, scorecard start, and
  full risk register at final-artifact depth.

Reference depth lives in `references/`: methodology in `business-model-design.md`,
`market-analysis.md`, `financial-planning-basics.md`, `goal-setting-and-metrics.md`, and
`lean-planning-methods.md`; working instruments in `risk-assessment.md` and
`stakeholder-communication.md`; calibration in `planning-case-studies.md`. First-time runners should
read `lean-planning-methods.md` and `financial-planning-basics.md` before step 1.

## 04 — Workflow

Twelve steps, run in order. Each step names the reference file that governs it and a checkpoint
question to put to the user before moving on, and leaves behind a named artifact. The sequence is
deliberately front-loaded with evidence and back-loaded with documents: no plan section is drafted
before steps 1–9 have produced its inputs. A full run is a working session of several hours; steps 7–12
are commonly a second session.

### Step 1 — Frame the engagement

- **Action.** Write down the decision this plan must settle, the planning horizon, and the hard
  constraints: dates, floors, non-negotiables. Agree on scope — one-page plan first, full plan if the
  stakes or audience warrant it — and decide what is out of scope for this run. Leaves behind the
  engagement frame: decision, horizon, constraints.
- **Governing reference:** `references/lean-planning-methods.md` — the plan-versus-experiment
  distinction and the one-page discipline.
- **Checkpoint question:** "If this plan goes well, what decision gets made in the next 90 days — and
  by whom?"

### Step 2 — Establish the raw numbers

- **Action.** Collect cash on hand, monthly personal burn, the founder income floor, and tested
  delivery capacity. Compute the preliminary cost floor for the founder's time: (target annual income +
  taxes at an effective rate + fixed business costs) ÷ realistic annual billable hours. Utilization for
  a service business is 55–70 percent of a standard week, not 100. Leaves behind the raw-numbers block:
  cash, burn, income floor, capacity, cost floor per hour.
- **Governing reference:** `references/financial-planning-basics.md` — cost structure, the precision
  level, and the cost-floor calculation.
- **Checkpoint question:** "Which of these four numbers are measured facts, and which are estimates we
  should mark for testing?"

### Step 3 — Define the customer and the wedge

- **Action.** Name one primary segment specifically: role, organization type, budget owner. Choose the
  wedge — the narrow entry point that is underserved, reachable, winnable, and expandable. Write down
  the adjacent segment you are not taking yet and the trigger that would reopen the choice. Leaves
  behind the segment, wedge, expansion path, declined alternative, and channel statement.
- **Governing reference:** `references/market-analysis.md` — sizing philosophy, competitor mapping, and
  wedge criteria.
- **Checkpoint question:** "What repeatable channel reaches your first ten buyers — and have you used
  it yet?"

### Step 4 — Design the business model

- **Action.** Answer the five model questions: who pays, what they get, why you instead of every
  alternative, how they pay (the payment shape, which drives cash timing), and what is left over per
  unit. State the unit logic explicitly — for the main unit, its price, direct cost, and contribution —
  and decide the recurring-versus-one-time mix with a year-end recurring target. Leaves behind the
  model summary: five answers, the unit-economics line, the recurring mix.
- **Governing reference:** `references/business-model-design.md` — the five questions, the nine
  building blocks, value capture, and unit logic.
- **Checkpoint question:** "Can you state price, direct cost, and contribution for one unit — and would
  the model survive losing your largest relationship tomorrow?"

### Step 5 — Size the market bottom-up

- **Action.** Derive year-one obtainable market: reachable buyers through channels you can operate ×
  realistic close rate × average first-year value. Show the arithmetic; cite the source of the close
  rate even if the source is thin evidence honestly labeled. Collect demand signals with dates and
  sources; map direct, indirect, and do-nothing competition, stating what you must prove to win each.
  Leaves behind the bottom-up arithmetic, the signal log, and the competitor map with the do-nothing
  row filled.
- **Governing reference:** `references/market-analysis.md` — bottom-up arithmetic, TAM honesty red
  flags, and the competitor table including the status quo row.
- **Checkpoint question:** "How many buyers can you actually reach this year through channels you
  already operate — and what evidence supports the close rate?"

### Step 6 — Price the offer from three anchors

- **Action.** For each service line or product, set price against three anchors: the cost floor from
  step 2, the market range (from real quotes and rate cards, not surveys), and the value anchor — the
  buyer's economics. Choose the pricing structure per line — hourly, per project, per day, retainer,
  value-based — and state payment terms, since they drive cash timing in step
7. Leaves behind the pricing table: line, price, pricing basis, payment terms.
- **Governing reference:** `references/financial-planning-basics.md` for the three anchors and
  structures; `references/business-model-design.md` for the value-capture check.
- **Checkpoint question:** "Does the price clear your cost floor with margin at realistic utilization —
  and if the floor is above the market range, which do we fix?"

### Step 7 — Build the 12-month financial sketch

- **Action.** Lay out four quarters: revenue by line from price × expected volume, variable costs as
  per-unit rules, fixed costs by month, founder draw, tax provision, net cash flow, and running
  balance. Map cash timing per revenue line — deposits at signature, balances on delivery, payment
  windows. Mark founder-level break-even and the trough month, then run the downside case at 60 percent
  of plan and check it against the minimum-cash rule. Leaves behind the quarterly financial table plus
  break-even, the trough, and the triggered downside response.
- **Governing reference:** `references/financial-planning-basics.md` — the 12-month sketch procedure,
  break-even, and runway math.
- **Checkpoint question:** "Which month is the cash trough, does it clear your floor, and what is the
  pre-agreed response if it does not?"

### Step 8 — Choose the metrics and targets

- **Action.** Pick one North Star that reflects delivered value and can be steered monthly or
  quarterly. Derive three to five input metrics from the arithmetic of the North Star target: proposals
  needed, win rate to maintain, average value, retainers live. Add two or three health metrics with
  safe ranges — utilization, collection days, minimum cash — and apply the retire-one rule: any new
  metric retires an old one. Leaves behind the metric tree: North Star, inputs with derived targets,
  health ranges.
- **Governing reference:** `references/goal-setting-and-metrics.md` — North Star tests, the
  input-metric tree, and target derivation.
- **Checkpoint question:** "If this number moves next quarter, what action could you have taken this
  month — and if none, is it the wrong North Star?"

### Step 9 — Map and test the load-bearing assumptions

- **Action.** List the plan's dependencies; score each on impact-of-being-wrong and uncertainty. For
  the high-impact, high-uncertainty few, run the cheapest honest test — problem interviews, live
  quotes, smoke tests with real commitment, pilots, time-boxed capacity trials — with the falsification
  condition written before the test runs. Record results and actions in the assumption log, and update
  earlier steps when a test contradicts them. Leaves behind the assumption log with the top assumptions
  tested or test-dated.
- **Governing reference:** `references/lean-planning-methods.md` — assumption mapping, test types,
  falsification conditions, and the log.
- **Checkpoint question:** "Which two or three assumptions, if wrong, kill this plan — and what
  evidence, gathered before launch, would tell us?"

### Step 10 — Build the risk register

- **Action.** Walk the kill-risk checklist: concentration, cash, founder health and dependence,
  compliance and tax, reputation, demand shift, legal exposure, key-asset loss. Sort kill risks from
  friction and spend register space accordingly. Score likelihood and impact honestly on a three-point
  scale; give every severe row an early signal and a mitigation that is present, tested, and owned,
  with a trigger. Write the commitment rules — spending caps, concentration caps, minimum cash,
  resignation conditions — as triggered rules, not intentions. Leaves behind the risk register (8–12
  rows) and the commitment-rules list.
- **Governing reference:** `references/risk-assessment.md` — the kill-risk checklist, scoring
  discipline, pre-mortem, and mitigation standards.
- **Checkpoint question:** "For each severe-and-likely risk: what control exists today, has it been
  exercised, and who owns it?"

### Step 11 — Draft the plan documents

- **Action.** Fill `templates/one-page-plan-template.md` — always; it forces the decisions onto one
  page and exposes unfinished thinking. When the stakes or audience warrant, extend into
  `templates/business-plan-template.md`, writing the summary section last. Replace every placeholder,
  keep every number traceable to a step above, and cut all instructional comments before delivery.
  Leaves behind the one-page plan (v1) and, where in scope, the full plan draft.
- **Governing reference:** the two templates; for audience and framing,
  `references/stakeholder-communication.md` — the stakeholder map and update formats.
- **Checkpoint question:** "Could a stranger read the summary and repeat back what this business does,
  who buys, and why it wins?"

### Step 12 — Set the operating cadence

- **Action.** Put the monthly scorecard review and the quarterly half-day on the calendar before the
  session ends. Decide who receives which update at what cadence — the partner or family numbers
  conversation, lender or client updates — and fix the formats now so drift is visible later. Define
  what would trigger graduating from lean planning to full planning, and write it down. Leaves behind
  calendar dates, the stakeholder update map, and the graduation test.
- **Governing reference:** `references/goal-setting-and-metrics.md` for the cadence rules;
  `references/stakeholder-communication.md` for update formats and the quarterly numbers conversation.
- **Checkpoint question:** "What is the date of the first review, and who hears the numbers first?"

### Execution notes

- Steps 1–3 rarely need a second session; steps 5–7 are where sessions most often split. When resuming,
  re-read the assumption log before continuing — it is the memory of the run.
- If the user cannot supply cash, burn, or an income floor, mark those as assumptions with test dates
  in step 9 rather than stalling; the plan must still name what is unknown and when it will be known.
- If the cost floor exceeds the market range in step 6, do not average the problem away: change the
  offer shape — productize, raise value, change segment — and rerun steps 4–
6. This is the most common mid-run correction, and it is a feature of the method, not a failure of the
   business.
- Treat capacity stated as availability ("I have 40 hours") as untested. Sustained delivery at
  realistic utilization is the planning number; an untested estimate goes to step 9 as a capacity test
  with a date.
- Never blend prices across lines to flatter the math, and never let "one percent of a big market"
  substitute for the reachable-buyers calculation.
- Keep all intermediate artifacts: the assumption log, first-pass tables, rejected drafts. They are the
  audit trail that makes the final plan correctable, and they are what section 06 demonstrates in
  condensed form.

## 05 — Rules and Quality Bar

These rules separate professional plans from decorated hopes. Each is a checkable property of the
output, not a style preference. When reviewing any artifact from this skill, test it against these
numbered rules before anything else.

1. **Every number is derived, and the arithmetic is shown.** A revenue figure with no visible price ×
   volume (or buyers × close rate × value) behind it is disqualified. *Why:* untraceable numbers cannot
   be corrected when actuals arrive — they can only be abandoned, and abandonment is how plans die
   quietly.
2. **One primary segment per plan.** Two segments produce two plans stapled together, with diluted
   wedges and blended math. *Why:* the wedge, the channel, and the capacity math all stop being
   derivable when the buyer is plural.
3. **Price from the cost floor first, then test against market and value.** The floor is where service
   businesses fail first, and it is knowable before the first sale. *Why:* polishing a price that
   cannot pay the founder is negotiation preparation for a losing position.
4. **Founder time is a cost, never a residual.** "Profit" that is actually unpaid wages hides the true
   viability of the business. *Why:* the cost-floor and founder-level break-even calculations exist
   precisely to expose this, and they only work if applied at step 2.
5. **Separate one-time from recurring revenue in every table.** They carry different risk, different
   cash timing, and different growth logic. *Why:* a blended revenue line makes both the runway math
   and the capacity math quietly wrong, and the error surfaces at the worst time.
6. **Cash timing is part of every revenue line.** Deposits, payment windows, and delivery dates convert
   revenue into cash on specific months; the sketch shows cash, not bookings. *Why:* businesses die of
   calendar math, not profit math — the trough month must be findable in the document.
7. **Assumptions are tested before they are bet on, and the falsification condition is written before
   the test.** Commitment evidence — deposits paid, quotes accepted, signed pilots — outweighs stated
   intent. *Why:* deciding afterward what would have counted is how people talk themselves out of
   evidence.
8. **Kill risks outrank friction in the register, and every severe row has a present, tested, owned
   mitigation with a trigger.** "Be careful" is not a control. *Why:* plans fail from unmanaged kill
   risks, and registers fail from unreviewed rows; both failures are prevented by the column
   discipline.
9. **The plan carries written commitment rules with triggers** — concentration caps, minimum cash,
   spending gates, resignation conditions. *Why:* future-you under pressure is a different
   decision-maker, and triggers are the only reliable way to bind them.
10. **One North Star, three to five inputs, and the retire-one rule for any new metric.** Every target
    carries a one-line "why this number." *Why:* metric soup feels like rigor and produces no
    decisions; unexplained targets get gamed or ignored.
11. **Precision stays proportional to stakes.** Quarterly granularity, order-of-magnitude confidence,
    three-point risk scores, ranges with reasons. *Why:* invented decimals create false confidence and
    hide the assumptions that actually matter.
12. **The wedge you declined is written down next to the wedge you chose**, with the condition that
    would reopen it. *Why:* without a recorded alternative, every attractive distraction reopens the
    strategy monthly.
13. **The plan names what would make it wrong.** The graduation test from lean to full planning, the
    pipeline-collapse trigger, the downside case at 60 percent of plan. *Why:* a plan with no stated
    failure conditions is a belief, and beliefs do not get revised on schedule.
14. **Capacity is a tested delivery rate, not an availability estimate.** "I have 40 hours" is not a
    planning number; sustained billable output at realistic utilization is. *Why:* revenue lines sized
    to availability fail at delivery, and the failure surfaces mid-quarter when it is most expensive.

The rubric instruments behind these rules, for review passes: the model interrogation checklist and
unit-logic traps in `business-model-design.md`; the TAM honesty red flags and demand-signal weighting
in `market-analysis.md`; the cost-floor, break-even, and runway diagnostics in
`financial-planning-basics.md`; the North Star tests and scorecard format in
`goal-setting-and-metrics.md`; the kill-risk checklist and mitigation standards in
`risk-assessment.md`; the falsification-condition discipline in `lean-planning-methods.md`; and the
update-format consistency rule in `stakeholder-communication.md`. A plan that passes rules 1–9 is
decision-ready; a plan that also passes 10–14 is an operating document.

## 06 — Worked Example

Aurora Creative: a one-person brand-and-web design studio founded by a designer leaving a full-time
job. The deliverable agreed in step 1: a one-page plan plus a 12-month financial sketch — revenue by
service line, cost structure, pricing logic, break-even, cash runway, quarterly milestones, and a risk
register. This section shows the run in condensed form with the intermediate artifacts visible,
including one rejected first pass; the completed final artifacts live in
`examples/worked-business-plan.md`.

**Step 1 — Frame.** Decision to settle: can the designer resign next month and reach a $4,800/month
income floor within the year? Horizon: 12 months. Constraints: $16,500 cash reserve; household income
floor fixed; no subcontracted brand work in year one — craft quality is the win reason.

**Step 2 — Raw numbers.** Cash $16,500; personal burn $4,000/month; income floor $4,800/month net.
Capacity tested during the final employed month: 6 focused delivery hours/day, 4 client days/week — 24
billable hours/week planned, 22 as the floor. Preliminary cost floor: ($57,600 target income + ~$17,400
tax provision + ~$9,300 fixed costs) ÷ 1,248 annual billable hours ≈ $67/hour.

**Step 3 — Customer and wedge.** Segment: founder-led consumer brands, 2–20 employees, rebranding or
building a first serious site. Wedge: local food-and-beverage founders, reachable through two past
side-project references (a brewery rebrand, a café site) and a regional founders' meetup. Expansion:
adjacent consumer segments once two non-F&B case studies exist. Declined for now: enterprise and agency
overflow work; reopen if the referral sources run dry.

**Step 4 — Model.** The five answers: founders pay; they get a brand and site that make them look
established; why Aurora — senior work at studio speed, fixed fee, one accountable designer; how they
pay — 40 percent deposit, balance net-15 on delivery, retainers monthly; what is left over — the unit
line below. Unit logic: brand project $6,500 − ~$350 direct = $6,150 contribution; brand+web $10,800 −
~$600 = $10,200; site-care retainer $950 − ~$40 = $910/month. Recurring mix: 0 percent today, 25
percent of monthly revenue by Q4.

**Step 5 — Market, bottom-up.** 180 reachable contacts × 28 percent conversation rate ≈ 50
conversations/year → 40 percent produce proposals ≈ 20 proposals → 45 percent win rate ≈ 9 projects. At
$8,200 average first-year project value: ~$73,800, plus retainers ramping to four live ≈ $25,600 →
~$99,000; planning basis set at $92,000 as a ramp haircut. Competitor map: cheaper freelancers (weak on
seniority), full agencies (weak on price and speed), DIY templates — the do-nothing row (tolerable pain
until a launch or rebrand forces the question). Signals logged with dates: two inbound asks from the
meetup within three weeks; a local competitor raising prices.

**Step 6 — Pricing table (draft that survived, after the A2 test below).**

| Line | Price | Basis | Terms |
| --- | --- | --- | --- |
| Brand identity project | $6,500 (band $6,000–6,800) | Floor $67/h × ~65 h + margin; market test | 40% deposit, net-15 |
| Brand + web project | $10,800 (band $10,000–11,500) | Floor × ~110 h; value anchor (launch economics) | 40% deposit, net-15 |
| Site-care retainer | $950/month, 4 h included | Cost floor + responsiveness value | Monthly, 3-month initial term |

**Steps 7–8 — Sketch and metrics, first pass (rejected, then revised).** The first draft booked two
projects per quarter. Capacity math killed it: at 24 billable hours/week, one brand project ≈ 65 hours
and one brand+web ≈ 110 hours — roughly 1.5 projects/quarter, not two. Revised revenue: Q1 $6,950, Q2
$19,850, Q3 $22,050, Q4 $26,350; year $75,200 — deliberately under the $92,000 basis, so pipeline
targets must beat the sketch rather than match it. Cash timing (deposits at signature, balances net-15
after delivery) puts the trough at Q2: $4,500 closing, below the $5,800 floor (1.5 months burn).
Metrics chosen: North Star — monthly billable revenue, $7,700/month by Q4; inputs — 8
conversations/week, 2 proposals/month by Q2, ≥45 percent win rate, 4 retainers live by Q4; health —
utilization 55–70 percent, collection < 35 days, cash ≥ $5,800.

**Step 9 — Assumption log (as tested).**

| # | Assumption | Test | Wrong if | Result | Action |
| --- | --- | --- | --- | --- | --- |
| A1 | Warm network yields ≥ 6 Q1 proposals | 12 outreach conversations, weeks 1–3 | < 3 produce proposal requests | 9 conversations → 5 requests | Proceed; second channel for Q3 |
| A2 | $6,500 brand price clears | Quote in 3 live proposals | 0 accept and 2+ counter below $5,500 | 1 accept, 1 accept at $6,000, 1 lost | Band $6,000–6,800 |
| A3 | $950 retainer sells | Pitch 4 past/prospective clients | 0 of 4 accept | 2 accept | Line confirmed at $950 |
| A4 | 24 billable h/week sustainable | Final-month trial at pace | < 20 h or quality drop | Sustained 22–24 | Keep 24 with 22 floor |
| A5 | No client exceeds 40% of revenue | Structural cap, monitored quarterly | First two projects from one client | First two clients differ | Cap holds; quarterly check |

**Quarterly milestones (as planned in the one-page plan).**

| Quarter | Milestone | Definition of done |
| --- | --- | --- |
| Q1 | Studio open for business | 12 outreach conversations done; site live with two case studies; first project signed at $6,000+; first retainer live |
| Q2 | Recurring floor forming | Second retainer live; two projects delivered on schedule; collection days under 35 |
| Q3 | Second channel active | 2+ proposals/month sourced outside the warm network; first brand+web case study published |
| Q4 | Recurring mix target met | Retainers at 25 percent+ of monthly revenue; year-two pricing review scheduled |

**Decisions the intermediates forced.** The retainer line exists because the cash-timing map showed the
trough and A3 proved the offer; without the map, the original all-projects draft would have shipped.
The brand+web band was cut from a first-pass $12,500 after the A2 counters — the market test cost three
proposals and saved a quarter of mispriced selling. The Q2 trough — found in step 7, before it happened
— became a triggered rule rather than a worry: bridge contract, 3 weeks, only if the pipeline is under
2 proposals at end of month 4; otherwise pull retainers forward. The concentration cap shaped selling
behavior from month one: two channels, not one, because the risk table made the dependency visible —
and A1's result (5 of 9 conversations converting to requests) confirmed the warm channel while still
triggering the second-channel plan for Q3.

**Step 12 — Cadence (as set, before resigning).** First monthly scorecard review on the first Friday
after launch; quarterly half-day scheduled before each quarter begins. Stakeholder map fixed: the
partner gets the quarterly numbers conversation — cash position, runway, revenue versus plan, biggest
risk, next quarter's one goal; no lender yet; the two retainer clients get the monthly four-block
update (headline, shipped, numbers, asks) in the same format every month, so a missing number reads as
loudly as a wrong one. Graduation test written down: three consecutive months of operational misses —
capacity, delivery, collections — rather than existential ones moves planning from one page to full.

**Step 10 — Risk register (condensed to the kill-class rows).** Concentration above 40 percent —
mitigation: cap plus 2 new conversations/week; trigger: any quarter over cap. Pipeline collapse — two
consecutive months under 2 proposals; mitigation: second-channel activation. Cash below floor — monthly
check against $5,800; mitigation: the bridge rule. Non-payment — 10+ days late; mitigation: deposit
plus signed agreement plus net-15. Tax under-provision — tax account under 25 percent of quarter
billings; mitigation: same-day 30 percent transfer. Commitment rules written with triggers: deposit and
signed agreement before any engagement; 30 percent of every payment to the tax account same day; no
project below $6,000 without written rationale; concentration cap 40 percent; no subcontracted brand
work in year one.

**Final artifacts.** The completed one-page plan (v3), the full quarterly financial and cash tables,
the scorecard start for month 1, and the seven-row risk register are in
`examples/worked-business-plan.md`, with a closing list of what the planning run changed and why. In
one line each: the run invented the retainer line, set the brand+web price band from tested counters,
converted the Q2 cash trough into a triggered decision rule, and shaped selling behavior from month one
via the concentration cap.

**What the run kept unchanged.** The wedge, the win reason, and the no-subcontracting rule all survived
testing intact, and the declined enterprise segment stayed declined. That is what a defensible plan
looks like after evidence: most of it still standing, the changed parts changed for named reasons, and
the reasoning visible in the artifacts rather than asserted in prose. A plan that changes everything
after testing was never a plan — only a guess with formatting.

## 07 — Failure Modes and Recovery

Each failure mode below lists the early signal to watch for, the corrective move when caught, and the
prevention habit that stops recurrence. Signals are observable in the artifacts; none requires guessing
at intent.

1. **Hope-based projection.** Revenue lines that "grow" with no price × volume or buyers × rate behind
   them. *Early signal:* a year-one number whose derivation cannot be shown in one line of arithmetic.
   *Corrective move:* rebuild every revenue line bottom-up per step 5 and re-price per step 6; expect
   the number to fall, and let it. *Prevention:* rule 1 and the bottom-up arithmetic — no revenue
   figure enters the sketch without its factors attached.
2. **The unpaid founder.** A plan that shows "profit" while ignoring the founder's wage, making a loss
   look like a living. *Early signal:* no cost-floor calculation anywhere in the artifacts. *Corrective
   move:* recompute the cost floor and founder-level break-even; re-price or reshape the offer until
   contribution clears them. If the floor sits above the market range, fix the offer shape —
   productize, raise value, or change segment — rather than averaging the problem away. *Prevention:*
   rule 4 — founder time is priced into every sketch at step 2, before any revenue optimism exists to
   defend.
3. **Cash blindness.** Profitable on paper, broke in month four because deposits are thin, terms are
   long, and the trough was never located. *Early signal:* the sketch shows revenue by quarter but no
   cash balance by month, or no deposit terms on any line. *Corrective move:* map cash timing per
   revenue line, mark the trough month, and attach the pre-agreed response to the minimum-cash trigger.
   *Prevention:* rule 6 — cash timing is mandatory in step 7, and the trough must clear the floor or
   carry a triggered fix.
4. **Survey validation.** Intent treated as commitment — "would you buy this?" answered politely and
   recorded as demand. *Early signal:* an assumption log whose tests are all questionnaires or
   compliments. *Corrective move:* re-run the load-bearing assumptions as commitment tests: live
   quotes, deposits, paid pilots, dated pre-orders. Re-run the capacity assumption against a calendar,
   too — sustained delivery hours are commitment evidence about the founder. *Prevention:* the
   test-type table in `lean-planning-methods.md` — interest metrics are context; only money and
   scheduled time are results.
5. **Mitigation-in-a-document.** A risk register whose responses are intentions — "we will be careful,"
   "monitor closely" — with no owner, trigger, or existence outside the file. *Early signal:* no
   trigger column, or triggers that name feelings instead of observable conditions. *Corrective move:*
   run the present/tested/owned test per row; demote anything that fails to "accepted, written," with a
   review date. *Prevention:* the register columns in `risk-assessment.md` and the step 10 checkpoint
   question.
6. **Metric soup and review theater.** Twelve tracked numbers, reviews that report and decide nothing,
   targets nobody can explain. *Early signal:* the scorecard grows while corrective actions per month
   approach zero. *Corrective move:* apply the retire-one rule, cut to one North Star plus inputs, and
   cap monthly reviews at two corrective actions with owners and dates. *Prevention:* the scorecard
   format and cadence rules in `goal-setting-and-metrics.md`.
7. **Plan sprawl.** The document grows past a dozen pages while the load-bearing decisions stay unmade
   — usually because customer, offer, or pricing is unsettled. *Early signal:* page count rising faster
   than the number of decisions closed. *Corrective move:* drop to the one-page plan, run steps 9–10 on
   the two or three assumptions that matter, and rebuild the full document only after they survive.
   *Prevention:* the graduation test in `lean-planning-methods.md` — full plans are earned by surviving
   tests, not by writing stamina.
8. **The silence spiral.** Updates go out only when there is good news; stakeholders — especially
   partners sharing financial risk — fill the silence with worse-than-real assumptions. *Early signal:*
   the last update predates a known miss, or the update format changes to bury one. *Corrective move:*
   reinstate the fixed cadence and format, lead with the headline including the miss, and hold the
   quarterly numbers conversation with the real runway figure. *Prevention:* the update formats and
   bad-news sequence in `stakeholder-communication.md`, agreed in step 12 while nothing is wrong.

Recovery posture, across all of these: almost no failure is fatal if the intermediate artifacts exist —
the assumption log, the sketch, the register. Fix the artifact that lied, re-run the affected steps,
and version the plan forward. Hiding a failed assumption inside a polished document is the only
unrecoverable version.

## 08 — Supporting Files Index

Every file in this skill directory, with its purpose and where this document uses it. Paths are
relative to the skill root; the table matches the directory exactly.

| Path | Purpose | Used by |
| --- | --- | --- |
| `SKILL.md` | This file: purpose, workflow, rules, worked example, index | All sections |
| `references/business-model-design.md` | Methodology: canvas, value capture, unit logic, recurring mix | 04 (steps 4, 6), 05 |
| `references/market-analysis.md` | Methodology: bottom-up sizing, competitor map, wedge selection | 04 (steps 3, 5), 05 |
| `references/financial-planning-basics.md` | Methodology: cost floor, pricing anchors, break-even, runway | 04 (steps 2, 6, 7), 05 |
| `references/goal-setting-and-metrics.md` | Methodology: North Star, input metrics, quarterly cadence | 04 (steps 8, 12), 05 |
| `references/risk-assessment.md` | Checklist: kill risks, pre-mortem, register columns, triggers | 04 (step 10), 05, 07 |
| `references/lean-planning-methods.md` | Methodology: one-page plan, assumption tests, pivots | 04 (steps 1, 9), 05, 07 |
| `references/stakeholder-communication.md` | Methodology: updates, asks, expectation and bad-news handling | 04 (steps 11, 12), 07 |
| `references/planning-case-studies.md` | Case study: a service and a product business planned end to end | 02, 06 |
| `templates/business-plan-template.md` | Full plan scaffold with instructional comments | 03, 04 (step 11) |
| `templates/one-page-plan-template.md` | One-page plan scaffold, fill-in-order sections | 03, 04 (step 11) |
| `examples/worked-business-plan.md` | Extended Aurora Creative artifacts: complete plan, sketch, register | 03, 06 |

File conventions: references contain no YAML frontmatter and are practitioner documents, not summaries;
templates contain instructional blockquotes meant to be deleted on use; the example carries finished
artifacts with every number traceable to a step in section 04. Read the reference named in a workflow
step before executing that step for the first time; the templates are fill-ready as they stand; and
read the example before a first run — it is the calibration target for what finished artifacts look
like. This index is part of the contract: a file on disk but missing from the table is a defect of this
document, and a name in the table without a file is a broken pointer — verify against a directory
listing after any edit to this skill.
