# Currencies and Resources

Pattern catalog for classifying and designing in-game currencies and resources.
Use this file when deciding how many currencies your game needs, what role each
plays, what sinks each supports, and how they convert between one another. A
game with clean currency architecture is easier to balance, easier for players
to understand, and easier to extend with new content.

## 1. Currency Types

**Primary soft currency.** The main currency of the game, earned through normal
play, spent on nearly everything. Gold, credits, coins. Every player engages
with it every session. Must have the most sinks, the most faucets, and the
healthiest sink ratio. Primary soft currency is the circulatory system of the
economy — when it fails, the whole game fails.

**Secondary soft currency.** Earnable through specific content or activities.
Dungeon tokens, raid seals, faction badges. Tied to a subset of sinks. Purpose:
create content-specific progression without devaluing the primary currency. A
secondary currency that overlaps in sinks with the primary currency is clutter,
not design.

**Premium currency.** Obtainable through real-money purchase or very limited
in-game achievement. Gems, diamonds, star coins. Central to free-to-play
monetization. The hard rule: premium currency must not convert to direct
persistent power. It buys cosmetics, time-saves, convenience, and access — it
does not buy stats.

**Reputation / faction currency.** Tied to a specific vendor or faction.
Spent in that faction's shop only. Purpose: gate content by investment in a
specific system. Effective for horizontal progression but creates inventory
bloat if too many factions exist simultaneously.

**Limited / seasonal currency.** Valid only during a specific event or season.
Purpose: drive engagement during a window, then expire. Must have an explicit
end-of-life plan: salvage rate to primary currency, conversion to XP, or
automatic deletion with advance warning.

## 2. Resource Types

**Consumable resources.** Used once and destroyed. Potions, arrows, fuel,
repair kits. Design rule: affordable at the tier they are earned, expensive
enough that stockpiling has a ceiling. A consumable that is cheaper than the
time cost to make it becomes infinite free value.

**Accumulative resources.** Build up over time and persist. XP, reputation,
energy. Design rule: capped or soft-capped to prevent infinite hoarding. An
uncapped accumulative resource that generates forever will eventually make
every sink irrelevant.

**Constant-value resources.** Each unit is worth the same as every other unit.
Gold is constant-value: one gold coin is one gold coin. Easy to model, easy
for players to understand. Risk: players treat them as interchangeable and
stop caring about individual units once the numbers get large.

**Scalar resources.** Each instance has its own value spectrum. A unique sword
has stats, durability, and rarity that determine its worth. Harder to model —
you need a valuation function, not just a count. But scalar resources create
the emotional attachment that constant-value resources cannot.

## 3. The One-Axis Rule

Each currency occupies exactly one axis from this set:

- **Vertical progression** — the currency buys power (levels, stats, gear tiers)
- **Horizontal expression** — the currency buys variety (builds, cosmetics,
  side activities)
- **Content gating** — the currency buys access (zones, bosses, dungeons)
- **Friction recovery** — the currency bypasses punishment (repair, resurrection)

A currency that occupies two axes is two currencies merged in error. When a
single currency buys both power and cosmetics, players optimize for power and
ignore cosmetics — then wonder why they have nothing to spend on.

## 4. Conversion Rules

Soft-to-premium conversion should be one-directional (soft → premium at
punitive rates, or blocked entirely). Premium-to-soft at a fair rate is the
most common design mistake in F2P economies: it lets whales flood the soft
economy with real-money purchases, inflating prices for everyone.

When conversion is necessary, use either a punitive rate (100:1 or worse) or
a one-way gate (premium → time-save items only, never → soft currency).

## 5. Currency Proliferation Warning

More than four active currencies simultaneously causes measurable player
frustration. Each new currency adds cognitive load, complicates monitoring, and
creates a coordination problem (the player must track which currency is needed
for which purchase). Before adding a new currency, ask: can an existing
currency be repurposed or split? If the answer is truly no, schedule the
retirement of the oldest active currency in the same release.

## 6. Storage Patterns

| Pattern | Behavior | Example |
|---------|----------|---------|
| Uncapped | No limit. Watch for hoarding. | Gold, primary soft |
| Hard cap | Absolute limit. Built-in pacing. | Energy, action points |
| Soft cap with depreciation | Value decays per season or event. | Prestige tokens, seasonal currency |