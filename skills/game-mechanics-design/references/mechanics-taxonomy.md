# Mechanics Taxonomy

A pattern catalog for classifying and generating game mechanics. Use it three
ways: to name what you are building (naming sharpens design), to find
neighbors (mechanics that solved similar problems), and to check coverage
(a design that draws from only one family usually has a missing pillar).
Families describe what the mechanic is *for*; the patterns inside each
family describe how it works.

## 1. The four families

- **Action mechanics** — moment-to-moment play: the verbs, timing, and
  space. Lived in per second. Examples: dodge rolls, parries, grapples.
- **System mechanics** — interacting rule modules that create emergent
  situations. Lived in per encounter. Examples: weather, faction
  reputations, elemental reactions, economy inputs.
- **Progression mechanics** — how power and capability grow. Lived in
  per session or per campaign. Examples: skill trees, deckbuilding,
  crafting tiers, prestige layers.
- **Social mechanics** — structures between players. Lived in per
  relationship. Examples: trading, co-op roles, leaderboards, guild
  obligations.

Every mechanic belongs primarily to one family and borrows from others.
A crafting system (progression) that gates by zone danger (action) and
enables player markets (social) is one mechanic with three family
surfaces — spec the surfaces separately, because they break separately.

## 2. Action patterns

- **Commitment windows:** moves with wind-up and recovery, so choosing
  to act is also choosing to be vulnerable. The backbone of readable
  combat.
- **Spacing tools:** dashes, repositioning, knockback — they make space
  itself a resource.
- **Parry/counterplay:** defensive verbs with tight timing that convert
  defense into offense. High skill ceiling, high teaching cost.
- **Charge tiers:** hold-to-empower inputs; one verb, multiple depths.
- **Risk toggles:** stances or modes trading speed for power, active at
  player will rather than situationally.

Design notes: action patterns are judged by their commitment (a dodge
with no recovery teaches panic-dodging), by legibility of enemy answers
(every player verb needs a readable threat it answers), and by input
economy (more than six simultaneous verbs exceeds most players'
attention; depth comes from combining, not accumulating).

## 3. System patterns

- **Element/reaction grids:** statuses that combine (fire + oil). Depth
  scales with the square of elements — budget elements carefully, as 6
  elements means 15 potential pairs to author and balance.
- **Economy taps and sinks:** sources and drains for each currency; a
  currency with no sink inflates until progression mechanics break.
- **Faction/reputation systems:** persistent relationship state that
  changes available content. Powerful for world-feel, dangerous when
  reputation gates become chores.
- **Simulation spills:** systems that produce consequences outside their
  intended arena (fire spreads to the marketplace you wanted intact).
  Delightful when intended, expensive when accidental — audit the spill
  paths before shipping.
- **Constraint rotators:** recurring state that reshuffles decisions
  (day/night, seasons, patrols). Cheapest way to refresh a static map.

## 4. Progression patterns

- **Horizontal (breadth):** new options, not bigger numbers — new tools,
  verbs, routes. Preserves challenge; multiplies content cost.
- **Vertical (depth):** numbers grow. Cheap to produce, erodes earlier
  content and challenge; pace it or the game becomes a checklist.
- **Choice-based:** progression as decisions inside play (deckbuilding,
  talent respec, boon drafting). Strongest ownership feelings; requires
  pools deep enough that choices stay real.
- **Knowledge-based:** player skill and understanding as the unlock
  (recipe discovery, boss pattern mastery). Cheapest to produce, hardest
  to pace; cannot be patched by numbers.
- **Meta/prestige:** run-level progress that survives resets. Converts
  failure into momentum — the engine of "one more run" design.

## 5. Social patterns

- **Asymmetric co-op roles:** complementary kits that make players need
  each other (one scans, one digs). The strongest bonding pattern;
  fails when roles are optional.
- **Trading and markets:** player economies. Enormous depth, enormous
  exploit surface — do not ship without sink analysis.
- **Broadcast and compare:** leaderboards, ghosts, shareable builds.
  Cheap sociality; works even in single-player games (seeds, daily
  challenges).
- **Obligation loops:** guild tasks, shared bases, care-taking mechanics
  that create gentle duty to others. Retention through guilt is real
  but burns goodwill when abused.

## 6. Generating with the catalog

To design a mechanic for a stated job, walk the catalog as a matrix:

1. State the job and the loop it must live in (loop design first,
   always — see `core-loop-design.md`).
2. Pick the family whose timescale matches the job (per second, per
   encounter, per session, per relationship).
3. List two patterns from that family and one from an adjacent family;
   design three one-line candidates.
4. For each candidate, write: the decision it creates, what it adds to
   the loop's state change, and what existing system it might break.
5. Kill any candidate whose decision sentence is "the player gets
   stronger" — that is an outcome, not a mechanic.

## 7. Coverage check

For a whole game, audit family coverage against the experience goals:
an action game may deliberately run action-heavy, but even then a
progression pattern (weapons that change verbs) and a light social
pattern (shared runs, ghosts) usually strengthen the core. A design
drawing on exactly one family is fragile: when that family's content
thins, nothing catches the player.

## 8. Worked fragment

The same job — "make mining trips feel different each run" — through
three families: action (a pickaxe overcharge verb that risks tool
breakage, changing moment-to-moment digging), system (cave-ins that
reroute tunnels, reshuffling the encounter space), progression (per-run
relic choices that reshape the run's build). All three are legitimate;
they differ in timescale, cost, and what they make the player decide.
The worked example in `../examples/worked-mechanic-design.md` picks the
progression candidate and shows why.