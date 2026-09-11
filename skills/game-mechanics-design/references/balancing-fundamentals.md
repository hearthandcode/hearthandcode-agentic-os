# Balancing Fundamentals

Methodology for making mechanical choices deliberate and defensible.
Balancing is not making everything equal — it is making the intended
strategies dominant over the unintended ones, keeping failures fair, and
knowing which number to turn when evidence says something is off.

## 1. What balance actually means

A game is balanced when:

1. **Intended strategies are viable.** Every strategy the design promises
   (stealth, brute force, trading, tech-rush) can win in the right hands.
2. **No unintended strategy dominates.** Degenerate strategies may exist;
   they must not be the best answer to everything.
3. **Losses are legible.** When players lose, they can name a cause and a
   counterplay. Balance failures usually present first as blame-shifting:
   "the game cheated."
4. **Comeback is possible but not guaranteed.** Trailing players need a
   path back; leading players need protection from pure catch-up curses.

Note what is *not* on the list: equal win rates, equal pick rates, or
equal usage. Some content should be situational; some strategies should be
harder. Balance is a means to fairness and expressiveness, not symmetry.

## 2. The lever inventory

Every game exposes a limited set of tuning levers. Enumerate them once and
you will stop reaching for the same three:

- **Magnitude levers:** damage, health, cost, yield, range, duration.
  The blunt instruments; they move everything downstream.
- **Frequency levers:** cooldowns, spawn rates, resource ticks, drop rates.
  Change the texture of play without changing single moments.
- **Friction levers:** input difficulty, wind-up times, animation locks,
  UI steps. Nerfs that skilled players feel as clunkiness — use with care.
- **Availability levers:** what appears when — pool composition, shop
  rotation, unlock order, drop tables. Powerful for fixing degenerate
  combos without touching the pieces.
- **Conditional levers:** bonuses and penalties that apply only in stated
  contexts (vs. bosses, in shadows, while low health). Surgical but
  additive; five conditionals deep, players can no longer model the rule.
- **Rule levers:** change the decision structure itself (stun immunity,
  no-hit shields, limit one legendary per run). Expensive to reason about,
  reserved for confirmed structural problems.

Order of preference when responding to a problem: availability →
conditional → frequency → magnitude → friction → rule. The early levers
reshape strategy space; the late ones rewrite player expectations.

## 3. Cost curves and power curves

Most progression content is a curve; getting the family right matters more
than any single point on it.

- **Linear:** each purchase adds a flat increment. Predictable, keeps
  choices comparable, dulls over time as absolute numbers grow.
- **Quadratic / polynomial:** late purchases scale faster. Creates
  climax builds but bends the midgame; keep exponents low (2, never 4)
  or the endgame owns the game.
- **Exponential:** each step multiplies. Use only for things meant to
  explode (idle-game multipliers), because exponential curves cannot be
  nerfed gracefully — the balance cliff is always one step away.
- **Diminishing returns (sub-linear):** each step adds less. Correct
  default for defensive stats and for anything players stack.
- **Soft-capped:** linear until a knee, then flat. Communicates "enough"
  without a hard rule; make the knee visible to players.

Practical rules of thumb:

- Price curves should rise faster than power curves, or late purchases
  become auto-includes.
- Multiplicative bonuses stack explosively. Either sum them instead, or
  hold the number of multipliers on one character low enough to model.
- Cost in *time* (cooldown, wind-up) is often a better nerf than cost in
  *power*, because it changes decisions rather than erase them.
- Square-root damage scaling on stat stacking keeps accumulation
  meaningful without letting one stat own the game.

## 4. Marginal value per resource

The core economic instrument of balance: what does the *next* point of a
resource buy? If the 10th point of strength buys more than the 10th point
of armor, players stack strength until something changes. Two fixes: equal
the marginal value across competing stats, or make the exchange explicit
(one point of armor = 0.8 points of effective health against the common
damage band) and let players optimize a solved system. Hidden unequal
marginal values are the most common root cause of "everyone takes the same
perk."

## 5. Dominant-strategy checks

Run this check on every mechanic and every balance pass:

1. **Enumerate the strategies** the mechanic permits (for a card: aggro,
   control, combo; for a loadout slot: each fill).
2. **Find the answer key:** which single strategy wins most often against
   the field? Use data where it exists; use expert play where it does not.
3. **Ask the dominance question:** is the best strategy also the easiest
   and the most available? That triple is the degenerate signature.
4. **Break it deliberately:** buff a rival strategy until the dominant one
   must answer it, rather than nerfing the dominant one into the ground.
   Players forgive buffs; they remember nerfs.
5. **Recheck after each patch** — dominance migrates; killing one degenerate
   strategy crowns another.

A healthy metagame has answered strategies, not one answer: rock-paper-
scissors structure, situational tech, and a cost to every default.

## 6. Simple quantitative tools

- **Effective health:** health × (1 + armor/100). Lets you compare armor
  and health buffs on one axis; most armor formula debates are this curve
  in a costume.
- **DPS with uptime:** damage per activation × activations per minute ×
  uptime%. Kills most "this weapon feels stronger" arguments.
- **Expected value with real distributions:** mean drop value × rate per
  minute; but check variance separately — two options with equal EV and
  different variance serve different players, and variance is a design
  tool (risk appetite), not an error.
- **Simulation for volume:** encode the rules and play 1,000 rounds with a
  scripted strategy to get distributions for win rate, session length,
  and resource curves. Naive-agent caveat: results describe the agent's
  strategy, not good players'.
- **Change-one-variable testing:** when playtests disagree with the model,
  trust the playtest, change one number, and retest. The model explains;
  the playtest decides.

## 7. Pre-ship balance checklist

- Every parameter in the spec has a stated range and a default chosen by
  reasoning, not by later regret.
- The top three intended strategies each beat at least one dominant
  strategy in expert play.
- The known degenerate combos are either fixed or consciously accepted in
  writing (with a monitoring plan).
- Loss replays are legible: a new player can say what killed them.
- Progression content still competes with the base kit (no dead items).
- A rollback plan exists for the riskiest change (ship a config flag).

## 8. Case fragment: nerfing without breaking hearts

A co-op survival game's "adrenaline surge" perk (25% attack speed for 10s
after a dodge) dominated every loadout. The first nerf drafted was a flat
reduction to 15%, which the community would read as "you broke our favorite
thing." The shipped fix instead moved availability: the perk now shares a
slot with the two other dodge-synergy perks, keeping its identity but
pricing the *combination* rather than the power. Pick-rate fell from 71% to
38% without forum protests — and the two sibling perks became real choices.
The lesson: when one option dominates, first try repricing the choice, not
weakening the toy.