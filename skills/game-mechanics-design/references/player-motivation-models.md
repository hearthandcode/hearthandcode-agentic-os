# Player Motivation Models

A reference of the motivation frameworks working designers actually use, with
the failure modes each model explains best. Use it when choosing what a
mechanic should reward, when a shipped mechanic lands with players in ways
you did not expect, or when a design argues with itself about who the game
is for. Models are lenses, not laws — each one earns its keep by predicting
a failure you can then avoid or a fix you can then apply.

## 1. Intrinsic vs. extrinsic motivation

Intrinsic motivation comes from the activity itself (mastery, curiosity,
the joy of a clean execution); extrinsic motivation from external rewards
(points, loot, rank). The overjustification effect is the working
designer's key fact: attaching strong external rewards to an already
enjoyed activity can *displace* the intrinsic motivation — players start
playing for the reward, and when the reward dries up or is nerfed, the
activity is dropped with it.

Design consequences:

- Reward the activity players already enjoy, never instead of it. If the
  loot chase is the only reason to run the dungeon, the combat had
  better be excellent anyway — otherwise you have built a slot machine
  that patches poorly.
- Extrinsic rewards are best as *recognition* of intrinsic play (style
  bonuses for creative kills) rather than as the price of participation.
- When you must use extrinsic rewards, prefer uncertain, cosmetic, or
  informational rewards over guaranteed, mechanical ones; they displace
  less and stay exciting longer.
- Watch for displacement symptoms: players skipping content without
  rewards, doing the daily chore and logging off, calling the fun part
  "the grind."

## 2. Self-determination theory (SDT)

SDT names three needs whose satisfaction produces durable, intrinsic
engagement. It is the most actionable lens for mechanic design because
each need maps to designable properties:

- **Autonomy** — the player chooses meaningfully. Served by real options
  (builds, routes, dialogue), menus that do not punish experimentation,
  and objectives that can be pursued in different orders. Broken by
  single-solution design, forced tutorials, and FOMO clocks.
- **Competence** — the player gets better and can see it. Served by
  legible failure, skill-expressive mechanics, difficulty that scales
  with visible mastery, and feedback that names what improved. Broken
  by opaque failure, rubber-banding, and rewards for participation
  rather than play.
- **Relatedness** — the player matters to others. Served by co-op
  interdependence, shared achievements, mentoring, and worlds that
  remember the player's actions. Broken by pure competition ladders
  for casual audiences and by social features that require scheduling.

Mechanic audit pattern: for any mechanic, ask which need it feeds, how
strongly, and which need it taxes. A guild-mandated daily quest feeds
relatedness weakly and taxes autonomy strongly — the audit predicts its
resentment. The strongest loops feed two needs at once: a build-crafting
mechanic feeding autonomy and competence; a duo mechanic feeding
relatedness and competence.

SDT also explains why punishment-heavy design feels controlling:
deaths that confiscate progress feed competence only if the failure was
legible and the retry fast. Confiscation without legibility is a tax,
and players experience taxes as external control.

## 3. Player archetypes: Bartle and successors

The classic four-type model, built from two axes (acting on the world vs.
interacting with players; acting vs. interacting):

- **Achievers** — accumulate status through in-world achievement.
  Want: goals, completions, visible progress bars, set collections.
- **Explorers** — know the world. Want: hidden systems, recipes, map
  edges, mechanics with discoverable depth (a parry window shorter than
  the tutorial says).
- **Socializers** — use the game as a medium for people. Want: shared
  spaces, co-op verbs, communication tools, mutual projects.
- **Killers** — act on other players. Want: asymmetric PvP, dominance,
  and reputations. (In single-player games their analog is mastery
  bragging — leaderboard chasing, no-hit runs.)

Working extensions worth knowing: the demographics of these mix across
genres (a crafting sandbox is Explorer/Socializer heavy; a ladder shooter
is Killer/Achiever heavy), and most real players are mixtures that shift
by mood and session length. Design consequences:

- A game should feed its *core* archetype deeply and at least one
  adjacent archetype lightly. Feeding all four equally produces a
  shallow theme park.
- Mechanics have archetype affinity: crafting feeds Explorers and
  Achievers; ranked ladders feed Killers and Achievers; housing feeds
  Socializers and Achievers. Check that your game's promised experience
  and its reward structure point at the same archetype.
- Content aimed at an absent archetype is dead content: a trading post
  in a four-player co-op game with no economy will rot.

## 4. The motivations-for-play lens (fun categories)

A complementary catalog of what players say they want: sensation (the
controller-shaking feel), narrative (the story), fantasy (being the
thing), discovery (finding out), challenge (the test), submission
(letting the system wash over you — farming sims, idle games), expression
(leaving a mark — bases, characters), and spectating/watching. Use it in
playtest debriefs: ask which two or three of these the player came for,
then check whether the mechanic under test serves any of them. A
mechanic serving none of the player's stated motivations is dead weight,
however elegant.

## 5. Applying the lenses in order

1. **Who is the player?** Name the primary and secondary archetypes for
   your game (one sentence each, from audience research or from the GDD).
2. **What motivation does the mechanic serve?** One sentence: which SDT
   need, which fun category, which archetype.
3. **What does it tax?** Every mechanic costs attention, autonomy, or
   mastery elsewhere. Name the tax; if you cannot, you have not
   understood the mechanic.
4. **Check displacement:** does the reward replace or recognize the fun?
5. **Predict the failure mode** from the model's own failure list
   (grind resentment, chore loops, achievement-only play), then decide
   the telemetry or playtest question that would catch it.

## 6. Failure modes each model predicts

- Overjustification: rewards cannibalize intrinsic fun → retention dies
  when the season ends.
- SDT-autonomy starvation: single-solution builds → the community
  optimizes one path and calls the game solved.
- SDT-competence starvation: opaque death → blame, not mastery.
- Archetype mismatch: Killer-heavy design shipped to Socializer
  audience → hostile chat, churn.
- Fun-category mismatch: challenge framing for a submission-framed
  audience → "why is this so stressful?"

## 7. Worked fragment

A hypothetical co-op mining game adds a shared "overburden" mechanic:
both players carry one haul pack; dropping your half slows the partner.
SDT audit: feeds relatedness strongly (interdependence), competence
moderately (packing order matters), taxes autonomy (route choices now
need agreement). Archetype check: Socializer primary, Achiever
secondary — a fit for the stated audience, with a killer-side risk (a
partner who drops their half repeatedly becomes griefing; needs a
consent toggle). Fun categories: expression and challenge, not
sensation. The prediction: affection from duos, resentment from solo-
with-matchmaking; the playtest question is accordingly "do matched
randoms disable the pack?" — behavioral, observable, and dated.