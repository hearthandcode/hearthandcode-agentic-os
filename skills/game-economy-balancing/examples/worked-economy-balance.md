# Worked Example: Forge & Anvil Economy Model

Complete run of the game-economy-balancing workflow on a two-currency economy
for a midcore crafting RPG called **Forge & Anvil**. This document shows the
full 28-day simulation, intermediate artifacts (faucet/sink tables, tuning
decisions, diagnostic tables), and the amendment sequence that brought the
economy into compliance. Use this as a pattern for your own economy work.

## Game Profile

| Field | Value |
|-------|-------|
| Title | Forge & Anvil |
| Genre | Midcore crafting RPG (fantasy smithy) |
| Platform | PC |
| Target player | Midcore |
| Monetization | F2P, cosmetic battle pass ($4.99/month) |
| Hours to endgame (median) | 45 hours |
| Currencies | Anvil Coin (AC, primary soft), Flame Token (FT, secondary soft) |

No premium-to-power conversion exists. The battle pass grants three exclusive
cosmetic items, a +5 FT weekly bonus, and two extra daily quest slots.

## Persona Definitions

| Persona | Hours/Day | Sessions | Active Ratio | Spend Ratio | Skip Day Corr. |
|---------|-----------|----------|-------------|-------------|---------------|
| Casual | 1.0 | 1 | 70% | 50% | 1.4 |
| Midcore | 2.5 | 2 | 80% | 70% | 1.15 |
| Hardcore | 5.0 | 3 | 85% | 90% | 1.0 |

The active ratio converts total play time into earning time (menus, inventory,
and idle are discounted). Spend ratio is the fraction of available income
actually spent on sinks — casual players spend less aggressively.

## Faucet Inventory

| Activity | Currency | Type | Rate/Hour | Bound | Conditions |
|----------|----------|------|-----------|-------|------------|
| Forge items | AC | Unbounded | 60 AC | — | Core loop, skill-scaled |
| Complete quests | AC, FT | Bounded | 90 AC, 10 FT | 3 per session | Story quests |
| Sell surplus loot | AC | Bounded | 50 AC | Account supply | Inventory-limited |
| Daily login | AC, FT | Bounded | 24 AC, 4 FT | Once/day | Streak bonus |
| Daily challenge | FT | Bounded | 6 FT | Once/day | Rotating objectives |
| Perfect-craft bonus | FT | Skill | 5 FT | 24h cooldown | 100% quality only |

**Effective per-hour rates (after active ratio and persona efficiency):**

| Persona | AC/hour effective | FT/hour effective |
|---------|------------------|-------------------|
| Casual | 145 AC | 14 FT |
| Midcore | 200 AC | 19 FT |
| Hardcore | 240 AC | 22 FT |

## Sink Inventory

| Activity | Currency | Type | Cost | Frequency |
|----------|----------|------|------|-----------|
| Gear repair | AC | Friction | 15 AC | Per forging session |
| Crafting materials | AC | Procedural | 10 AC | Per recipe |
| Anvil fee | AC | Friction | 5 AC | Per session |
| Weapon upgrade | AC | Procedural | 300 AC | Every ~5 sessions |
| Armor upgrade | AC | Procedural | 150 AC | Every ~5 sessions |
| Tool slot unlock | AC | Procedural | 500 AC | One-time per slot |
| Skill unlock | AC | Procedural | 300 AC | Uncommon |
| Forge upgrade | AC + FT | Aspirational | 400 AC + 100 FT | Once per 2 weeks |

**Initial problem:** FT has only one sink (forge upgrade at 100 FT). This is
well below the minimum of three sinks per currency.

## 28-Day Balance Sheet (First Pass)

### Casual Persona (AC)

| Day | Faucet | Sink | Net | Balance | Sink Ratio |
|-----|--------|------|-----|---------|------------|
| 1 | 145 | 70 | +75 | 75 | 0.48 |
| 7 | 1015 | 490 | +525 | 625 | 0.48 |
| 14 | 2030 | 1020 | +1010 | 1610 | 0.50 |
| 21 | 3045 | 1570 | +1475 | 2885 | 0.52 |
| 28 | 4060 | 2250 | +1810 | 4220 | 0.55 |

Sink ratio at 0.55 is well below the 0.85 floor — AC is inflating rapidly for
the casual persona. The skip-day correction (1.4x) means the casual effectively
plays 20 days out of 28, not 28.

### Midcore Persona (AC)

| Day | Faucet | Sink | Net | Balance | Sink Ratio |
|-----|--------|------|-----|---------|------------|
| 1 | 500 | 250 | +250 | 250 | 0.50 |
| 7 | 3500 | 1850 | +1650 | 2350 | 0.53 |
| 14 | 7000 | 4200 | +2800 | 5600 | 0.60 |
| 21 | 10500 | 7000 | +3500 | 9100 | 0.67 |
| 28 | 14000 | 10500 | +3500 | 12600 | 0.75 |

AC sink ratio improves over time as more expensive upgrade sinks unlock, but
even at day 28 it is only 0.75 — still below the 0.85 floor.

### Hardcore Persona (AC)

| Day | Faucet | Sink | Net | Balance | Sink Ratio |
|-----|--------|------|-----|---------|------------|
| 1 | 1020 | 500 | +520 | 520 | 0.49 |
| 7 | 7140 | 3800 | +3340 | 4600 | 0.53 |
| 14 | 14280 | 8700 | +5580 | 10780 | 0.61 |
| 21 | 21420 | 14000 | +7420 | 18200 | 0.65 |
| 28 | 28560 | 20000 | +8560 | 26760 | 0.70 |

### Flame Token (All Personas, First Pass)

The FT balance sheet reveals a clear problem:

| Persona | Day 7 FT | Day 14 FT | Day 21 FT | Day 28 FT | Sink Ratio |
|---------|----------|-----------|-----------|-----------|------------|
| Casual | 78 FT | 168 FT | 252 FT | 378 FT | 0.15 |
| Midcore | 343 FT | 721 FT | 1085 FT | 1435 FT | 0.22 |
| Hardcore | 672 FT | 1428 FT | 2184 FT | 2940 FT | 0.18 |

FT sink ratio across all personas is 0.15-0.22 — critical deficiency. The
forge upgrade (100 FT) is the only sink, but it is purchased infrequently
(once per 2 weeks). All personas accumulate FT with no meaningful outlet.

## Diagnostics (First Pass)

| Metric | Target | Casual | Midcore | Hardcore | Status |
|--------|--------|--------|---------|----------|--------|
| AC sink ratio (28d) | 0.85-1.20 | 0.55 | 0.75 | 0.70 | **FAIL** |
| FT sink ratio (28d) | 0.85-1.20 | 0.15 | 0.22 | 0.18 | **FAIL** |
| Wealth gap | <3.5x | — | — | 2.1x | Pass |
| Endgame time ratio | <2.0x | — | — | 1.7x | Pass |
| First upgrade time | <60 min | 28 min | — | — | Pass |
| Premium purity | No power | — | — | — | Pass |

The AC sink ratio is failing across all personas — too much currency is
entering and not enough is leaving. The FT sink ratio is critically failing.

## Tuning Cycle 1: AC Inflation

**Problem:** AC sink ratio is 0.55-0.75 across personas. The economy is
strongly inflationary.

**Step 1 (mildest lever):** Reduce the forge-items faucet rate from 60 AC/hour
to 54 AC/hour (10% reduction).

**Result after step 1:** AC sink ratio moves to 0.62 (Casual), 0.82 (Midcore),
0.77 (Hardcore). Midcore is now within range; Casual and Hardcore still fail.

**Step 2:** Increase weapon upgrade cost from 300 AC to 330 AC (10% increase).
Increase armor upgrade cost from 150 AC to 165 AC.

**Result after step 2:** Sink ratios: Casual 0.68, Midcore 0.88, Hardcore 0.83.
Casual still failing but trending up.

**Step 3:** Add a new aspirational AC sink — a pet cosmetic vendor (500 AC per
pet, monthly rotation).

**Result after step 3:** Sink ratios: Casual 0.82, Midcore 0.93, Hardcore 0.88.
Casual still slightly below 0.85 but within 5% — acceptable for the first-month
acquisition phase. Midcore and Hardcore pass.

## Tuning Cycle 2: FT Sink Ratio

**Problem:** FT sink ratio is 0.15-0.22. The currency has only one sink.

**Step 1:** Add Flame Enchant — cosmetic weapon glow effect, costs 35 FT,
48-hour duration. Classified as aspirational sink.

**Step 2:** Add Tempering Station — reduces gear durability wear on one
equipped slot by 15% for 7 days, costs 50 FT. Classified as light convenience
sink (not power).

**Result after steps 1-2:** Sink ratios: Casual 0.72, Midcore 0.80, Hardcore
0.78. Still below 0.85 but dramatically improved.

**Step 3:** Reduce Tempering Station cost from 50 FT to 45 FT (10% reduction)
to increase consumption.

**Result after step 3:** Sink ratios: Casual 0.80, Midcore 0.86, Hardcore 0.84.
Near-pass. Monitor.

## Final Diagnostics (Post-Tuning)

| Metric | Target | Casual | Midcore | Hardcore | Status |
|--------|--------|--------|---------|----------|--------|
| AC sink ratio (28d) | 0.85-1.20 | 0.82 | 0.93 | 0.88 | Near-pass (Casual 4% low) |
| FT sink ratio (28d) | 0.85-1.20 | 0.80 | 0.86 | 0.84 | Near-pass, monitor |
| Wealth gap | <3.5x | — | — | 2.0x | Pass |
| Endgame time ratio | <2.0x | — | — | 1.7x | Pass |
| First upgrade time | <60 min | 28 min | — | — | Pass |
| Premium purity | No power | — | — | — | Pass |

## Monte Carlo Results

1000-iteration simulation (post-tuning):

| Gate | Threshold | Result | Status |
|------|-----------|--------|--------|
| Deadlock rate at day 14 | ≤5% | 1.8% | Pass |
| AC supply CV | ≤15% | 11% | Pass |
| FT supply CV | ≤15% | 14% | Pass |
| Max zero-liquidity days | ≤2 | 0 | Pass |

## Ethics Review

| Purchase Flow | Dark Patterns | Status |
|--------------|--------------|--------|
| Battle pass purchase | None found | Clean |
| Premium shop (cosmetic) | None found — free path visible without scrolling | Clean |
| FT purchase with real money | None found — FT cannot buy power | Clean |
| Seasonal pet vendor | None found — deterministic pricing, no gacha | Clean |

## Tuning Summary

| Date | Lever | Old Value | New Value | Delta | Reason |
|------|-------|-----------|-----------|-------|--------|
| Pre-launch | Forge-items AC faucet rate | 60 AC/h | 54 AC/h | −10% | AC inflation |
| Pre-launch | Weapon upgrade cost | 300 AC | 330 AC | +10% | AC inflation |
| Pre-launch | Armor upgrade cost | 150 AC | 165 AC | +10% | AC inflation |
| Pre-launch | Pet cosmetic sink | — | 500 AC/tier | New | AC aspirational sink |
| Pre-launch | Flame Enchant sink | — | 35 FT/48h | New | FT sink deficiency |
| Pre-launch | Tempering Station sink | — | 50 FT/7d | New | FT sink deficiency |
| Pre-launch | Tempering Station cost | 50 FT | 45 FT | −10% | Increase FT consumption |

## Launch Recommendations

1. **Day 0:** Monitor AC and FT sink ratios daily for first two weeks.
2. **Week 2:** If FT sink ratio remains below 0.85, introduce a third FT sink
   (seasonal cosmetic, time-limited, 120 FT).
3. **Week 4:** If AC sink ratio for casual persona has not reached 0.85,
   add a daily-login AC sink (small gear durability loss that costs 5 AC to
   repair — 3 line config change).
4. **Month 2:** First content update should add new sinks before it adds new
   faucets. Prioritize aspirational sinks over procedural ones.

The FT economy is the primary risk. Continue monitoring FT liquid supply and
introduce a third sink (seasonal timed event) if FT balance exceeds 500 FT
for the average midcore player at day 60.