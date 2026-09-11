---
name: game-economy-balancing
description: >-
  Use when designing, auditing, or tuning a game economy — setting up currencies,
  modeling faucet/sink flows, defining player progression curves, verifying
  economic health across player personas, and monitoring live economies.
  Produces a complete economy model with validated constraints, Monte Carlo
  results, and a live dashboard specification.
---

# game-economy-balancing

## 01 — Purpose

Game economy balancing governs how currencies, items, and resources flow
between systems, players, and monetization interfaces. A well-tuned economy
gives the player agency: earned currency feels rewarding, purchases feel
meaningful, and progression climbs steadily toward a reachable endgame. An
unbalanced economy causes players to quit from grind fatigue, frustration, or
boredom — when currency has no meaningful outlet, nothing matters.

This skill provides the complete toolchain for designing and modeling a game
economy: currency architecture, faucet and sink engineering, progression curve
design, spreadsheet and Monte Carlo modeling, monetization ethics review, and
live operations monitoring. The output is a validated economy model in both
markdown and JSON formats plus a live dashboard specification.

**Three outcomes this skill owns:**
1. A documented economy model where every faucet and sink is intentional,
   every conversion rate is chosen, and every parameter has a rationale.
2. A verified constraints set — sink ratios in range, wealth gaps controlled,
   deadlock risk below 5%, premium purity maintained.
3. A monitoring plan that detects imbalance before it erodes player trust.

The skill targets game-industry practitioners: designers, producers, live-ops
managers, and analysts. Free-to-play, premium, subscription, and hybrid models
are all supported. The philosophy: game economies are fully under designer
control. Every inequality is the result of a design decision, not a market
force. With sufficient modeling and discipline, the worst failure modes can be
prevented before they reach players.

The skill also recognizes that economies are never finished. Live tuning,
seasonal drift, content expansion, and player behavior evolution all mean the
model is a living document. The sixteen-step workflow is designed to be
repeated in full or in part whenever conditions change. The monitoring layer
(step 14) is what triggers each revisitation.

## 02 — When to Use / When Not to Use

### Triggers: Use This Skill When

1. **Your game needs a new currency system.** You are designing fresh currency
   architecture from scratch or adding a new currency into an existing game.
   Each currency needs defined faucets and sinks, and the cross-currency system
   must be simulated before implementation. `references/currencies-and-resources.md`
   provides the currency classification patterns.

2. **You suspect a live economy is misbehaving.** Players amass resources with
   nothing to spend on, skip progression through daily-login wealth, hit a
   content wall, or show fatigue curves that suggest imminent burnout. The
   diagnostics in section 05 and the monitoring guide at
   `references/live-economy-monitoring.md` give you structured detection.

3. **You are building a first-playable prototype with formal economics.**
   Revenue targets, loop growth goals, and time-to-satisfaction ratios need a
   quantitative spec from day one rather than feel-based design that collapses
   under testing.

4. **You are launching a season, major expansion, or game-defining content
   gate.** Especially when it introduces a new currency type that shifts
   existing sink patterns and alters the equilibrium of the economy.

5. **You are reviewing someone else's economy design.** The quality dimensions
   defined in section 05 — sink ratio, wealth gap, progression per persona,
   premium purity, F2P path viability — allow concrete analysis of any game
   economy.

6. **You need pre-launch live-ops readiness.** A dashboard plan does not build
   itself. Having monitoring thresholds defined before players arrive means
   there is data from day one and no guessing about what normal looks like.

7. **The game has a player-driven economy or market.** Player-to-player trades
   create supply-and-demand outside designer control, making monitoring even
   more critical. The case studies in `references/economy-case-studies.md` show
   how player-driven economies fail.

### When NOT to Use This Skill

- **Single-resource single-player linear game.** If the game has one currency
  with no multi-path spend decisions, a plain cost-to-progression spreadsheet
  suffices. Use the **game-mechanics-design** skill for balancing.

- **Narrative-only economy with no mechanical effect.** If resource choices
  impact story but not player power, access, or speed, use a simple comparison
  table within the narrative design skill, not this full toolchain.

- **Existing balanced game with zero new content.** The ship is stable. This
  skill is for change, not for documentation. Opening a full modeling cycle
  on a healthy economy adds process without value.

- **Short-run events only.** One-week seasonal events with no secondary
  currency or lasting effect can be balanced with quick arithmetic. Save the
  full 16-step workflow for systems that persist beyond a single season.

## 03 — Inputs and Outputs

### Inputs Required

- **Game genre and core structure.** Progression type (linear, branching,
  skill-gated), session length distribution, daily recurrence patterns,
  multiplayer or single-player mode, persistent-world components.

- **Full resource list.** Every currency (primary soft, premium, reputation,
  seasonal) and every resource item (raw materials, consumables, key items).
  Partial lists produce partial models.

- **Progression milestones.** Expected level or power bands, narrative gates,
  and checkpoints that define early, mid, and endgame. These anchor the cost
  curves.

- **Monetization model.** F2P, premium, subscription, battle pass, or hybrid,
  with constraints. The business model shapes the entire architecture.

- **Player persona set.** At least three archetypes — Casual (1h/day), Midcore
  (2.5h/day), Hardcore (5h/day). Add a Whale persona when monetization relies
  on high-dollar purchases. Each needs a time budget, play style, and spending
  tolerance.

- **Target endgame time.** The number of hours to reach endgame for the median
  persona anchors all cost curves.

### Outputs Produced

- **Economy model in markdown**, populated from `templates/economy-model-template.md`.
  The template provides sections for game profile, currencies, personas, faucets,
  sinks, progression, balance sheet, diagnostics, Monte Carlo, ethics review,
  tuning history, dashboard spec, and risk register.

- **Economy model in JSON**, valid against `schemas/economy-model.schema.json`.
  The schema enforces required fields, data types, metric ranges, and persona
  completeness. Validate before distribution.

- **Faucet and sink tables** per currency per persona with net flow over a
  28-day simulation window. Produced during workflow steps 1-3.

- **28-day projection per persona** showing daily opening supply, total faucets,
  total sinks, and closing balance for every currency.

- **Verified constraints checklist**: sink ratio compliance, premium purity,
  wealth gap, reachable endgame, Monte Carlo deadlock rate.

- **Live dashboard specification** with metric names, alert thresholds, and
  response plans per `references/live-economy-monitoring.md`.

- **Risk register** mapping each failure mode from
  `references/economy-case-studies.md` to a projected scenario in the current
  design.

## 04 — Workflow

### Step 1: Define Resource Architecture

Read `references/economy-design-fundamentals.md` fully — the sink/faucet model
introduced there is the backbone of the entire workflow. Pay attention to the
three design phases (acquisition, equilibrium, prestige) and how faucet and
sink types shift between them. Output a catalog of every currency and resource:
name, role classification, functional purpose, and whether it is consumable or
accumulative.

**Check:** Does each resource have a clearly distinct role? If removing it
would not change the game, it is redundant.

### Step 2: Categorize Faucets and Sinks

Read `references/currencies-and-resources.md` — the faucet and sink
classification tables provide the taxonomy for the rest of the workflow. For
each currency, produce parallel lists: faucets tagged as Unbounded, Bounded, or
Skill; sinks tagged as Procedural, Aspirational, Social, or Friction. Every
unbounded faucet must have a measured rate and a cap.

**Check:** Does every currency have at least three sinks across at least two
different sink types?

### Step 3: Design Progression Curve

Read `references/progression-systems.md` — the four curve models (linear,
quadratic, exponential, logarithmic) and the pacing table. Choose one cost
function per currency based on design goal. Compute time-to-milestone for each
persona by dividing cumulative cost by the persona's expected daily faucet rate.
Apply the skip-day correction (1.4x casual, 1.15x midcore, 1.0x hardcore).

**Check:** Does any milestone spike exceed 2.5x the prior segment duration for
any persona? A spike that large means players will feel blocked.

### Step 4: Build Spreadsheet Model

Read `references/economy-modeling.md` — the static modeling section describes
column layout, formula relationships, and validation patterns. Output a working
model (spreadsheet or script) with columns per currency per persona: starting
supply, daily faucet events, daily sink events, net flow, running balance.
Cover at least 28 days.

**Check:** Is the model fully deterministic? Changing any single input must
recalculate the entire 28-day projection.

### Step 5: Define Persona Segments

Use `templates/economy-model-template.md` to define the persona taxonomy. The
template provides a structured section for persona definitions including hours
per day, session count, active ratio, spend ratio, and skip-day correction.
Define at least three personas.

**Check:** Are all major player segments that will interact with the economy
represented?

### Step 6: Assign Per-Persona Rates and Run Simulation

For each persona, assign per-hour faucet rates reflecting the persona
efficiency gap (hardcore earns more per hour than casual due to mastery and
routing). Multiply by active hours per day, then apply spend ratio to sinks.
Run the 28-day simulation from day 0 with zero starting supply. Record ending
balance per day.

**Check:** Does day-28 wealth diverge more than 3x between casual and hardcore?
Wider divergence means the personas are playing different games.

### Step 7: Compute Sink Ratio

Formula: sink_ratio = total_sinks_consumed / total_faucets_generated, per
currency, over 28 days. Target: 0.85-1.10 for the median persona. Below 0.85
means inflation; above 1.10 means deflation. Compute per currency individually,
never aggregate.

**Check:** Are all currencies in 0.85-1.10 for at least three of the defined
personas at day 28?

### Step 8: Measure Inflation Rate

Formula: inflation_rate = (total_faucets − total_sinks) / total_liquid_supply,
computed weekly per currency. Healthy: 1-3% per week. Caution: 4-6%.
Escalation: above 6%. Negative inflation (deflation) means sinks exceed faucets
and liquidity is drying up.

**Check:** Is any currency above 6% weekly inflation for two consecutive weeks?
If so, open a tuning cycle before it accelerates.

### Step 9: Set Progression Anchors

From `templates/economy-model-template.md`, produce the milestone table: First
Upgrade (≤60 min casual play), Mid Gate (~15h casual play), Endcap (target
endgame time). Compute cost per currency and time-to-reach per persona.

**Check:** Is casual persona endgame time no more than 2x hardcore persona
endgame time?

### Step 10: Define Premium Rules

Read `references/currencies-and-resources.md` — the premium section covers
conversion rules and the trap of premium-to-soft at fair rates. Write an
explicit statement of what premium can and cannot purchase. Premium must not
convert to direct persistent power.

**Check:** Does every premium purchase path pass the three-part test (no direct
power, no indirect advantage, no stacking loophole)?

### Step 11: Run Ethics Review

Read `references/monetization-ethics.md` — the dark pattern catalog covers
obfuscated pricing, false urgency, pay-to-skip-fun, gacha opacity, burying the
free path, and exploiting vulnerability. Score every purchase flow.

**Check:** Are all purchase flows clean? Any flagged pattern must have a
redesign that preserves revenue without the dark pattern.

### Step 12: Run Monte Carlo Simulation

Read `references/economy-modeling.md` — the Monte Carlo section describes the
simulation framework and output analysis. Run 1000 iterations randomizing
persona assignment and daily activity choices. Track time-to-endgame, endgame
wealth, purchase spend, and deadlock events.

**Check:** Are all three gates passed: deadlock ≤5% at day 14, supply CV ≤15%,
and no persona with zero liquidity for more than two consecutive days?

### Step 13: Adjust Tuning Levers

Read `references/tuning-and-balancing-methods.md` — the lever table enumerates
each adjustable parameter, its effect direction, and its risk profile. For each
currency that fails any check, apply a single tuning cycle: reduce the largest
faucet by ≤10%, then increase a sink cost by ≤10%, then add a new aspirational
sink if still out of range. No lever changes by more than 10% per cycle.

**Check:** Is every change documented in the tuning history with old value, new
value, delta, and measured outcome?

### Step 14: Design Live Dashboard Plan

Read `references/live-economy-monitoring.md` — the dashboard architecture
section recommends metric families, alert grouping, and response escalation
tiers. Define at least seven metrics with healthy range, caution threshold,
escalation threshold, and response action.

**Check:** Do the dashboard metrics cover all seven essential signals (currency
supply, sink ratio, wealth gap, first upgrade time, velocity, F2P path,
revenue per user)?

### Step 15: Reference Case Studies

Read `references/economy-case-studies.md` — two detailed case studies (one
healthy, one collapsed). Build a comparison table mapping analogous patterns
in your design to each failure mode. Where your design matches a failure
pattern, define a specific escalation path.

**Check:** Is every failure mode that has an analogue in your design matched
with a preventative measure and a trigger signal?

### Step 16: Finalize Output Documents

Populate `templates/economy-model-template.md` with data from steps 1-15.
Validate the resulting JSON against `schemas/economy-model.schema.json` using a
schema validator. Output: economy-model.md (human-readable) and
economy-model.json (machine-readable).

**Check:** Does the JSON pass schema validation with zero errors? Are the
markdown and JSON consistent on all key parameters?

## 05 — Rules and Quality Bar

1. **Sink Ratio Rule.** Every currency must have a sink ratio between 0.85 and
   1.20 for at least three persona-weeks at day 28. *Why:* below 0.85 causes
   hoarding and inflation; above 1.20 causes deflation and frustration.

2. **First Upgrade Doorway.** The first meaningful upgrade must cost 60
   minutes of casual play or less. *Why:* if the player cannot feel the
   economy rewarding their first session, they will not return for a second.

3. **Bounded Faucet Constraint.** Every unbounded faucet must have a daily cap
   or a diminishing-returns curve. *Why:* unbounded faucets without caps are
   the most common cause of runaway inflation in live games.

4. **Premium Purity.** Premium currency must not grant direct persistent power.
   *Why:* the moment premium buys stats, fair competition ends and the game
   becomes pay-to-win.

5. **One Role Per Currency.** No two currencies serve the same design purpose.
   *Why:* overlapping roles create confusion and make monitoring exponentially
   harder.

6. **Catch-Up Guarantee.** Casual persona endgame time must be at most 2x
   hardcore persona endgame time. *Why:* at 3x, casual players can see the
   finish line but know they will never reach it.

7. **Wealth Gap Limit.** At day 28, the top 10% average wealth must be at most
   3.5x the median. *Why:* concentration above 3.5x means the wealthy players
   are in a different economy than everyone else.

8. **No Direct Payment for Power.** No purchase flow can produce a permanent,
   irreversible stat increase from real money. *Why:* this is the universal
   dividing line between acceptable and predatory monetization.

9. **Transparent Pricing.** Every purchase interface must display the base
   value, conversion rate, and probability of random outcomes. *Why:* opaque
   pricing is the most common regulatory violation and the fastest trust
   destroyer.

10. **Bankruptcy Cap.** At most 5% of any persona may reach zero currency on
    any simulation day. *Why:* players who cannot afford the minimum required
    action do not continue playing.

11. **Model-Alignment Trigger.** Any live telemetry that diverges >25% from
    the model projection within 14 days triggers a mandatory re-review.
    *Why:* the model is wrong until proven right; ignoring divergence compounds
    the error.

12. **Content Ripple Check.** Any content update that touches a currency must
    recalculate sink ratio and liquidity curves before shipping. *Why:* a new
    item tier with no corresponding sink is a hidden inflation injection.

13. **Monte Carlo Pass.** All three Monte Carlo gates must pass: deadlock ≤5%,
    supply CV ≤15%, zero-liquidity ≤2 consecutive days. *Why:* a deterministic
    model is not enough; the stochastic simulation reveals the tails.

14. **F2P Path Guarantee.** Every premium item must have a visible free
    alternative path at ≤2x the paid time cost. *Why:* the free path protects
    the premium economy by keeping non-spenders engaged.

15. **Step Limit on Levers.** No single lever may change by more than 10% per
    tuning cycle. *Why:* larger changes over-correct and make it impossible to
    tell which adjustment worked.

16. **Every Sink Needs a Reason.** Every sink must answer: "why does this sink
    exist, and why does it cost this much?" *Why:* a sink without a rationale
    is a number that will be wrong for unknown reasons.

## 06 — Worked Example: Forge & Anvil

The full model for this worked example lives in
`examples/worked-economy-balance.md`. That file shows every intermediate
artifact — the complete 28-day balance sheets per persona, faucet/sink tables,
tuning history, Monte Carlo results, and ethics review. The material below is a
summary that runs the 16-step workflow on Forge & Anvil and shows the key
decisions and intermediate artifacts.

**Game:** Forge & Anvil, a free-to-play midcore crafting RPG. The player forges
weapons and armor in a fantasy smithy, sells them, levels up, unlocks
blueprints, and competes weekly. The economy has two currencies: Anvil Coin
(AC, primary soft) and Flame Token (FT, secondary soft). Monetized through a
cosmetic battle pass at $4.99/month. No premium-to-power conversion.

**Personas:** Casual (1h/day), Midcore (2.5h/day), Hardcore (5h/day).

**Step 1-2 intermediate artifacts — Faucet and sink catalog:**

| Resource | Faucets | Sink Types | Faucet Count | Sink Count |
|----------|---------|------------|-------------|-----------|
| AC | forge, quest, sell, login | repair, materials, anvil fee, weapon upgrade, armor upgrade, tool unlock, skill unlock, forge upgrade | 4 | 8 |
| FT | quest, daily challenge, perfect-craft | forge upgrade, (later) Flame Enchant, Tempering Station | 3 | 1 (initial) |

**Diagnosis:** FT needs more sinks — only one initial sink. This deficiency is
flagged in step 2 and tracked into step 13 for correction.

**Step 3-4 intermediate artifacts — Cost curve selection:**
AC uses a quadratic curve (cost = base × level²) because the game has a
natural ceiling at level 50 and the quadratic profile creates a satisfying
power feeling. FT uses linear (cost = base + level × rate) because FT is a
bonus currency, not a primary progression path.

**Pre-tuning 28-day balance sheet (AC, Midcore persona, excerpt):**

| Day | Opening AC | Daily Faucet | Daily Sink | Closing AC |
|-----|-----------|-------------|-----------|-----------|
| 1 | 0 | 200 | 50 | 150 |
| 7 | 950 | 250 | 180 | 1,020 |
| 14 | 2,100 | 310 | 450 | 1,960 |
| 21 | 3,800 | 370 | 620 | 3,550 |
| 28 | 5,600 | 420 | 810 | 5,210 |

**Pre-tuning diagnostics:** AC sink ratio: Casual 0.55, Midcore 0.72, Hardcore
0.68 — all failing the 0.85 floor. FT sink ratio: Casual 0.15, Midcore 0.22,
Hardcore 0.18 — critically failing. AC inflation at 4.5% weekly (caution zone).
FT inflation at 12% weekly (escalation zone — immediate tuning required).

**Step 5-6 persona analysis:** Per-persona rates set with an efficiency gap:
Hardcore earns 240 AC/h effective vs. Casual at 145 AC/h. Spend ratios vary:
Casual 50% (spends half of earned, hoards the rest), Midcore 75%, Hardcore 90%.
Day-28 wealth divergence: 2.1x — within the 3x limit.

**Step 9 milestone anchors:** First Upgrade (28 min casual — passes rule 2).
Mid Gate (18h casual). Endcap (45h midcore, 60h casual — ratio 1.33x, passes
the 2x limit of rule 6).

**Step 10 premium rules:** FT cannot buy power. Premium battle pass items are
cosmetic only: skin tints, emote effects, profile frames. Passes rule 4.

**Step 11 ethics:** All four purchase flows scored against the dark pattern
catalog. Battle pass: shows base price, renewal date, and full contents before
purchase. Skip timers: show base wait time and cost-per-minute. No gacha.
Score: clean.

**Step 12 Monte Carlo (1000 runs):** Deadlock 1.8% (<5% passes rule 13). AC
supply coefficient of variation 11%, FT CV 14% (both ≤15% passes). Zero
zero-liquidity days across all runs.

**Step 13 tuning decisions and intermediate artifacts:**

| Lever | Old Value | New Value | Delta | Rationale |
|-------|----------|----------|-------|-----------|
| Forge AC faucet per action | 60 | 54 | −10% | Largest faucet, most leverage |
| Weapon upgrade cost | 300 | 330 | +10% | Primary mid-game sink |
| Armor upgrade cost | 150 | 165 | +10% | Secondary sink |
| Pet cosmetic vendor (new sink) | — | 500 AC/tier | New | Aspirational, unlimited tiers |
| Flame Enchant (new FT sink) | — | 35 FT | New | Cosmetic glow, 48h duration |
| Tempering Station (new FT sink) | — | 50 FT | New | Durability convenience, 7d |

**Post-tuning diagnostics:**

AC sink ratio: Casual 0.82 (borderline), Midcore 0.93 (pass), Hardcore 0.88
(pass). FT sink ratio: Casual 0.80 (borderline), Midcore 0.86 (pass), Hardcore
0.84 (pass). Both improve significantly. The model recommends live monitoring
of FT in the first two weeks and introducing a third FT seasonal sink if FT
balance exceeds 500 FT for the average midcore player at day 60.

See `examples/worked-economy-balance.md` for complete tables, balance sheets,
and the full tuning history.

## 07 — Failure Modes and Recovery

### 1. Sink Faucet Inversion

**Early signal:** Sink ratio exceeds 1.20 from day 1 of simulation. Players
cannot afford basic progression and the economy deflates immediately.

**Corrective move:** Add a daily login faucet boost for two weeks. Introduce
a tutorial quest chain that delivers one-time currency rewards per account.

**Prevention:** During step 1, ensure the acquisition phase (first 2 weeks
of the simulation) has a target sink ratio of 0.60-0.80 — intentionally
inflationary. Designing for equilibrium from day 1 misses the generosity
window players need to build attachment.

### 2. Wealth Chasm

**Early signal:** Top 10% median wealth exceeds 3.5x at day 28. Wealthy
players drain content faster and devalue effort for new players.

**Corrective move:** Introduce progressive friction tax on high-wealth
thresholds (storage fees, luxury item rentals). Add a vanity-only prestige
sink with large currency deposits.

**Prevention:** Monitor wealth gap weekly from day 1 of simulation. If any
persona's wealth grows faster than 2x the next persona, reduce their
skill-based faucet rate or increase their aspirational sink costs in step 13.

### 3. Premium Hyperinflation

**Early signal:** Premium currency converts to soft at a rate that makes
conversion economically efficient. Soft currency from conversion exceeds 20%
of total daily income for any persona.

**Corrective move:** Cap soft-income-from-conversion at 20% of daily income.
Reduce conversion ratio to 300:1 or add a cooldown between conversion events.

**Prevention:** During step 10, block premium-to-soft conversion entirely
unless a punitive rate (100:1 or worse) is the only option. The safest design
has no conversion path at all.

### 4. Resource Cascade

**Early signal:** A lower-tier resource has zero active sinks once the player
progresses past that tier. Old materials accumulate in inventory permanently.

**Corrective move:** Add a salvage or upcycle conversion path for every
lower-tier resource. Set conversion at 3:1 or worse so upcycling is
convenience, not a primary faucet.

**Prevention:** During step 2, audit every resource's sinks at every tier. A
resource that is still generated but not consumed at endgame is a cascade
victim before it ships.

### 5. Dead Currency

**Early signal:** A seasonal or event currency has no end-of-life plan at
creation. It sits permanently in player inventory after the event ends.

**Corrective move:** Define at creation time: salvage at 2:1 to primary
currency, convert to XP at a set rate, or auto-delete on expiration with
advance warning.

**Prevention:** Add an End-of-Life field to every currency entry in
`templates/economy-model-template.md` during step 1. If the field is empty,
the currency cannot ship.

### 6. Login Overinflation

**Early signal:** Login rewards account for more than 50% of total monthly
earnings for the casual persona. Players progress by logging in, not playing.

**Corrective move:** Redistribute login rewards away from raw currency toward
skip-accumulator items — things that reduce grind time rather than providing
currency directly.

**Prevention:** During step 6, include login rewards in the faucet inventory
and compare against active earnings. If login exceeds 30% of active earnings,
redesign before the model passes.

### 7. Over-Levered Changes

**Early signal:** The team changes multiple economy levers in a single patch
without isolating each effect. Patch notes have no old and new values.

**Corrective move:** Revert all changes from the patch. Re-apply one lever at
a time, waiting 72 hours between each to measure the effect. Never ship more
than one lever change in a single patch during live operations.

**Prevention:** Enforce the 10%-per-lever cap during step 13. Use the tuning
history table in `templates/economy-model-template.md` to track every change.
If the table has no entries, the changes have not been documented.

## 08 — Supporting Files Index

| File | Role | Read / Use when |
|------|------|-----------------|
| SKILL.md | Master charter — this file | Navigating the skill; starting any economy workflow |
| references/economy-design-fundamentals.md | Methodology — sink/faucet model, economic phases, metastability | Steps 1, 7-8, 13; understanding core architecture |
| references/currencies-and-resources.md | Pattern catalog — currency types, resource classification, conversion rules | Steps 2, 10; classifying currencies and designing sinks |
| references/progression-systems.md | Methodology — curve models, pacing anchors, phase pacing | Steps 3, 9; choosing cost functions and setting milestones |
| references/monetization-ethics.md | Rubric — dark pattern checklist, premium purity rule, regulatory landscape | Step 11; auditing purchase flows before launch |
| references/economy-modeling.md | Methodology — spreadsheet modeling, Monte Carlo simulation, metrics | Steps 4, 12; building and stress-testing the model |
| references/tuning-and-balancing-methods.md | Checklist — lever table, delta method, 10% rule, tuning sequence | Step 13; adjusting parameters when quality gates fail |
| references/live-economy-monitoring.md | Metrics guide — essential metrics, dashboard architecture, alert thresholds | Step 14; designing live ops monitoring before launch |
| references/economy-case-studies.md | Case study — healthy (Ember Realm) and collapsed (Void Engine) economies | Step 15; stress-testing design against known failure modes |
| templates/economy-model-template.md | Template — fill-in markdown skeleton with guidance blocks | Steps 5, 9, 16; structuring the output document |
| schemas/economy-model.schema.json | Schema — JSON Schema (draft 2020-12) model validator | Step 16; validating the output before distribution |
| examples/worked-economy-balance.md | Example — complete Forge & Anvil 28-day model with tuning history | Section 06; seeing the full workflow on a real scenario |

### Common economy archetypes and when they fit

| Archetype | Description | Best for | Examples |
|-----------|-------------|----------|----------|
| Single linear | One currency, one purpose — earned through play, spent on gates | Casual mobile, premium one-time games | Super Mario Run, Monument Valley |
| Dual parallel | Hard currency (premium, slow) + soft currency (earned, fast) with conversion gates | F2P mobile, GaaS | Clash Royale, Brawl Stars |
| Multi-resource | 3+ resources with complementary roles, each sunk at different rates | RPGs, crafting games, 4X | Factorio, Stardew Valley, Satisfactory |
| Token economy | One fungible token as universal exchange with multiple simultaneous sink types | Social platforms, UGC | Roblox, Second Life |

### Implementation estimate

A first economy model for a medium-complexity dual-currency game takes:
- **Design + doc:** 5-10 hours
- **Spreadsheet model:** 3-5 hours to build and sanity-check
- **Monte Carlo simulation:** 2-4 hours to script 10K player-lifecycle runs
- **Playtune pass:** 4-8 hours across 3-5 closed sessions
- **Finalization:** 2-3 hours to validate schema and write dashboard spec

Budget 2-3 calendar weeks. The model lives in version control beside the game design doc; never tune from memory.

### Key economy terms

| Term | Definition |
|------|-----------|
| Faucet | Any system that generates currency or resources for the player — quests, drops, daily bonuses, selling |
| Sink | Any system that removes currency or resources — repair, crafting fees, upgrade costs, consumables |
| Soft currency | Freely earned through play, abundant, routine purchases |
| Hard currency | Earned slowly or purchased, scarce, premium items |
| Conversion gate | Rate-limited exchange between currencies at a fixed ratio |
| Sink ratio | Total faucet volume / total sink volume over a reference period. 1.0 = metastable equilibrium |
| Inflation | Currency devaluation as more enters than is removed, making prices feel meaningless |
| Wealth chasm | Growing gap between top and bottom player segments that devalues effort for new players |
| Progression curve | Rate of content unlock as a function of playtime or level |

### Reading Paths

**New to economy design:** Start with `references/economy-design-fundamentals.md`,
then `references/currencies-and-resources.md`. Read the worked example at
`examples/worked-economy-balance.md`. Return to SKILL.md for the workflow.

**Building a model:** Follow steps 1-16 in order. Each step names the reference
file to read first. Use `templates/economy-model-template.md` as the output
scaffold.

**Validating an existing model:** Jump to section 05 (Rules and Quality Bar).
For each rule you suspect is failing, read the associated reference and the
relevant workflow step.

**Diagnosing a live economy:** Start with `references/live-economy-monitoring.md`
to set up metrics. Then `references/economy-case-studies.md` to match symptoms
to known failure modes. Use section 07 (Failure Modes) for corrective moves.

### Related skills in this repository

| Skill | Relationship |
|-------|-------------|
| game-mechanics-design | Economy balancing feeds mechanic specs with cost data; mechanics create the faucets and sinks the economy tunes |
| level-and-encounter-design | Level pacing determines how fast players accumulate resources — coordinate progression curves across both |
| business-planning | Monetization strategy lives here; the business plan references the economy model's pricing assumptions |
### Tuning sequence quick-reference

When a specific rule fails in testing, apply fixes in this order:
1. Adjust sink depth (how much currency a single sink removes)
2. Adjust faucet rate (how fast currency enters)
3. Adjust conversion rate (soft-to-hard exchange ratios)
4. Add or remove a sink (structural change — highest impact, highest risk)
5. Adjust progression curve (shift when each sink becomes available)

Change one variable between playtests. Mark the baseline, change one lever, run three tests, compare.

### Reading Paths

**New to economy design:** Start with `references/economy-design-fundamentals.md`,
then `references/currencies-and-resources.md`. Read the worked example at
`examples/worked-economy-balance.md`. Return to SKILL.md for the workflow.

**Building a model:** Follow steps 1-16 in order. Each step names the reference
file to read first. Use `templates/economy-model-template.md` as the output
scaffold.

**Validating an existing model:** Jump to section 05 (Rules and Quality Bar).
For each rule you suspect is failing, read the associated reference and the
relevant workflow step.

**Diagnosing a live economy:** Start with `references/live-economy-monitoring.md`
to set up metrics. Then `references/economy-case-studies.md` to match symptoms
to known failure modes. Use section 07 (Failure Modes) for corrective moves.
