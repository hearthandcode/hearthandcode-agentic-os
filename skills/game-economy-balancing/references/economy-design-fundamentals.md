# Economy Design Fundamentals

Methodology for the sink/faucet model that underlies every game economy. Use this
file when laying out the architecture of a new economy, auditing an existing one
for inflation or deflation, or explaining to stakeholders why a given number
matters. The concepts here are the foundation — every other reference in this
skill package builds on them.

## 1. The Faucet/Sink Model

Every game economy is a closed or semi-closed system of resource production and
consumption. Two forces govern it:

- **Faucets (sources / injection points).** Any action or system that creates
  *new* currency or resources. Killing a monster for gold, completing a daily
  quest, selling loot to an NPC, harvesting a node — these add units that did
  not exist before. Faucets increase total supply.
- **Sinks (drains / removal points).** Any action or system that permanently
  removes currency or resources from circulation. Repair bills, vendor
  purchases, crafting costs, upgrade fees, auction-house listing fees — these
  destroy units. Sinks decrease total supply.

The single most important rule in economy design: **sinks must collectively
exceed faucets over the intended play period, or the economy inflates and
progression erodes.** An economy where more units enter than leave is a
ticking time bomb — players accumulate faster than the game can give them
reasons to spend, prices feel meaningless, and every new player faces a
mountain of pre-inflated costs.

## 2. Faucet Types

**Unbounded faucets.** Repeatable with no hard cap. Dangerous on their own: a
mob that drops gold with no daily limit is an unbounded faucet. Every unbounded
faucet must carry either a diminishing-returns curve or an explicit per-player
cap. Without one, a single dedicated player or bot can inject arbitrary
currency.

**Bounded faucets.** Limited per unit of time, account lifetime, or content
availability. Daily login rewards, first-clear bonuses, quest chains — these
are predictable and safe. The designer knows exactly how much enters the
system per player per day.

**Skill-based faucets.** Awards that scale with player competence. A high-skill
player extracts more currency per minute from the same activity. This creates
the persona efficiency gap — the hardcore player earns more per hour than the
casual, even doing the same things. Skill faucets must be modeled with a
distribution, not a point value.

## 3. Sink Types

**Procedural sinks.** Required for normal progression. Every player encounters
them: level-up costs, skill purchases, gear repair. These are predictable and
form the backbone of the sink inventory. Without enough procedural sinks, the
game lacks a spending floor.

**Aspirational sinks.** Entirely optional but visible to the player. Cosmetic
skins, titles, mount colors, housing decorations. These are the designer's best
tool — they pull currency out of the economy without punishing the player or
blocking progression. A healthy economy has more aspirational than procedural
sink volume.

**Social sinks.** Guild fees, gift giving, PvP entry fees, marketplace listing
taxes. Community-driven consumption that scales with the number of engaged
players. These are harder to model because they depend on social dynamics, but
they are also more resilient to farming and botting.

**Friction sinks.** Costs that punish failure or inefficient play: death
penalties, gear durability loss on death, market fees on failed listings. Use
sparingly — friction sinks feel bad even when they are fair. Their purpose is
not revenue extraction but behavioral steering.

## 4. The Three Economic Phases

Every game economy passes through three phases that correspond to the player's
relationship with the game:

**Phase 1 — Acquisition (first session to week 2).** Faucets are generous,
sinks are light. The player is learning and needs to feel rewarded for every
action. Sink ratio should be in the 0.60-0.80 range, meaning players accumulate
more than they spend. First upgrade costs under 60 minutes of casual play.

**Phase 2 — Equilibrium (week 2 to month 2).** Faucets and sinks converge.
Sink ratio targets 0.85-1.10. The player understands the system and begins
making meaningful spending decisions. This phase is where good economies feel
satisfying and bad economies reveal their cracks.

**Phase 3 — Prestige (month 2+).** Sinks begin to exceed faucets (ratio
1.00-1.20). Aspirational and social sinks dominate. The player is spending
to express identity, not to progress. Without enough Phase 3 sinks, the
economy plateaus and endgame feels empty.

## 5. Metastability

A well-designed economy is self-correcting without designer intervention.
Build in ambient sinks (always-on minimum leakage like repair), variable sinks
(costs that rise with total supply), and value intermediaries that cap
concentration. The economy should bend toward health when left alone — if it
bends toward runaway inflation or deflation without active tuning, the
architecture is wrong.

## 6. Key Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| Sink ratio | Sinks consumed / Faucets generated (per period) | Is the economy inflating or deflating? |
| Liquid supply | Total unspent currency across all players | How much purchasing power is sitting idle? |
| Velocity | Transaction volume / Total supply | How actively is currency circulating? |
| Wealth gap | Top 10% avg / Median wealth | Is wealth concentrating unsustainably? |

Calculate these per currency, not aggregated. A single aggregate number hides
crises in individual currencies.