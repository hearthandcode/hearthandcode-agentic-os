# Progression Systems

Methodology for designing the cost curves and pacing schedules that define how
players advance through a game. Every progression system is an economy in
miniature — players earn resources and spend them on advancement. If the
economy is the circulatory system, progression is the skeleton. Use this file
when choosing a curve shape, setting milestone costs, or validating that a
progression path is fair across player personas.

## 1. The Four Curve Models

**Linear.** `Cost = base + level * rate`. Every level costs the same increment.
Predictable, easy to balance, easy for players to understand. Best for:
secondary currencies, cosmetic items, consumables, any progression where the
designer wants transparent pricing. The player never hits a surprise wall, but
also never gets scaling satisfaction.

**Quadratic.** `Cost = base * level^2`. Mild acceleration. Costs grow noticeably
but not punishingly. Best for: primary progression currency, gear upgrade costs,
skill tree unlocks. The standard choice for most games because it creates a
gentle difficulty ramp without sharp gates.

**Exponential.** `Cost = base * r^level` (r > 1). Steep acceleration. Best for:
prestige layers, endgame mastery, content that should feel aspirational rather
than expected. Use sparingly — a 0.1 error in the rate factor makes the curve
either trivial or impassable. Always simulate with Monte Carlo before shipping
an exponential curve.

**Logarithmic.** `Cost = base * log(level + 1)`. Diminishing per-level cost.
Early levels come fast, later levels slow naturally. Best for: reputation
tracks, achievement-based rewards, catch-up mechanics. Players feel fast early
progress which builds momentum; the natural slowdown provides content
longevity without sharp gates.

## 2. Pacing Anchors

Every economy needs three milestone anchors regardless of curve shape:

**First Upgrade (Doorway).** Cost must be reachable within 60 minutes of casual
play. This is the first moment a player feels the effect of the economy. If the
first upgrade takes longer than one session, the player leaves before learning
the spending loop. Overrides all other pacing considerations.

**Mid Gate.** Cost at approximately 15 hours of casual play. The player has
learned the systems and is now making meaningful spending decisions. This gate
validates that the progression curve is not flattening too early or spiking too
sharply. Time-to-midgate between personas should not diverge by more than 2x.

**Endcap.** Target time-to-endgame for the median persona. This number anchors
all downstream cost calculations. If endgame is 40 hours away and casual
players are projected at 60 hours, while hardcore players hit it at 25 hours,
the 2.4x gap exceeds the 2x safety limit.

## 3. Curve Selection Heuristic

| Purpose | Recommended Curve | Why |
|---------|-------------------|-----|
| Primary progression currency | Quadratic | Balanced difficulty ramp |
| Cosmetic / vanity items | Linear | Transparent, fair pricing |
| Endgame prestige gate | Exponential | Clear aspirational cap |
| Crafting material cost | Logarithmic | Early gating eases off |
| Reputation / faction track | Logarithmic | Fast early progress builds momentum |

## 4. Phase Pacing

The five phases of player progression map to distinct economic behaviors:

| Phase | Hours Played | Faucet Sentiment | Sink Sentiment |
|-------|-------------|-------------------|----------------|
| Onboarding | 0-2 | Generous (learning) | Minimal (no friction) |
| Early game | 2-10 | Growing with skill | First procedural sinks |
| Mid game | 10-30 | Stable | Balanced (sink ratio ~1.0) |
| Late game | 30-80 | Efficiency-focused | Aspirational sinks dominate |
| Endgame | 80+ | Prestige and social | Luxury and expression |

## 5. Gates and Spikes

A gate is any progression segment whose duration exceeds the average of the two
adjacent segments by more than 60%. Gates are not inherently bad — they create
dramatic structure. But a gate exceeding 2.5x the prior segment duration for
any persona is a spike that will cause measurable player dropoff.

Detect spikes by computing time-per-segment per persona, then flagging segments
that break the 2.5x rule. Run this detection before any progression curve ships.

## 6. Catch-Up Guarantee

The casual persona's time-to-endgame must be at most 2x the hardcore persona's
time-to-endgame. At 3x, the gap is unbridgeable — casual players can see the
finish line but know they will never reach it. Catch-up mechanics (daily bonus
acceleration, rested XP, mentor bonuses) should exist in the design from day
one, not added as an apology after launch.