# Mechanics Case Studies

Four well-known mechanics dissected and re-derived. The point of a case
study is not trivia — it is to extract the design decision under the
surface, then show the derivation so it can be borrowed deliberately
rather than copied blindly. Each study ends with transferable rules.

## 1. Slay the Spire's deckbuilding — progression as per-run decisions

**The mechanic.** You begin each run with a weak, fixed deck. Combat wins
offer a choice of three cards; relics modify rules; shops and events bend
the pool. The deck you end a run with shares almost no cards with the deck
you started.

**Why it works.** Deckbuilding converts progression — normally a slow,
between-session currency — into the *core decision space*. Every reward is
a build question ("does this fit my engine?"), which feeds both competence
(sharper deck, better play) and autonomy (the run is yours). The per-run
reset also caps balance damage: a degenerate combo lives for one run, then
shuffles back into the pool.

**The anatomy, stated generically:**
1. A fixed, weak starting state.
2. Rewards that are *choices among alternatives*, never fixed payouts —
   choice is what converts reward into decision.
3. Synergy surfaces (relics, events, shops) that recontextualize old
   pieces so early picks stay live late.
4. A run structure short enough that a broken attempt costs one session.

**Failure modes if you borrow it:** thin pools (choice collapses into
picking the biggest number), dead picks (cards no build wants — audit pool
weekly), and removal friction (players who cannot prune a deck cannot
execute a plan).

**Re-derive it for another genre:** a farming sim where the "deck" is a set
of field leases drafted each season, rewards offered as three-lease
choices, and permanent relics in the form of irrigation tech that changes
which leases are worth taking.

## 2. Minecraft's crafting — knowledge as progression

**The mechanic.** Raw materials combine through recipes into tools, which
gather better materials, which craft better tools. The recipe book is the
game's tech tree, and for years it lived entirely in the player's head and
the wiki.

**Why it works.** The loop (punch wood → craft table → tools → stone →
iron → diamond) is a textbook 30-minute arc: each tier is a session peak
with a banking ritual at the end. But the deeper design is that **crafting
converts knowledge into power**: learning a recipe is a level-up the game
did not gate. Progression by knowledge is the cheapest progression that
still feels earned, and it explains why players voluntarily watch tutorials
— the wiki is part of the intended difficulty curve (a choice modern
in-game recipe books have re-priced).

**Anatomy, generically:**
1. Inputs gatherable in tiers, gated by the *output* of the previous tier
   (iron needs a stone pick — the gate is a crafted object, not a wall).
2. Recipes that combine at most a handful of ingredient types, arranged in
   a grid so shape itself is a puzzle.
3. Crafting output that is also an input-gathering tool — the loop closes.

**Failure modes:** recipe discoverability (progress halts without external
knowledge — the in-game book is the fix), ingredient soup (too many
interchangeable materials), and dead recipes nobody crafts after the tier
is passed.

**Re-derive it:** a cooking-forward RPG where recipes are learned from NPC
dialogue and failed dishes, gates are kitchen tools you craft, and each new
tool re-opens the cheapest ingredient tier with better yields.

## 3. Portal's portal gun — one verb, total depth

**The mechanic.** Two linked holes in surfaces; walk through one, exit the
other, preserving momentum. That is the entire kit, and it carries a
six-hour game.

**Why it works.** Portal strips the shooter to a single mechanic and then
spends all its content budget teaching, combining, and escalating *that
mechanic* rather than adding verbs. Each chamber introduces one twist on
the rule (momentum, weighted cubes, turrets, gel) and immediately demands
the previous lessons. The teaching is diegetic — the level is the tutorial,
which is why the game has no text.

**Anatomy, generically (this is the one-mechanic-game template):**
1. One verb with a strict rule set (what surfaces accept portals, what
   carries through).
2. Content as a sequence of *twists on the verb*, each twist introduced in
   a safe space and immediately tested in a dangerous one.
3. Failure cheap and instant (a pit, a reset button), so experimentation
   stays cheaper than comprehension.
4. An escalation of *constraints*, not of controls — the gun never
   changes; the situations do.

**Failure modes:** a single-verb game must pace its twists perfectly — one
under-taught twist stalls players harder than any boss — and the verb
must tolerate experimentation (physics players will break every chamber;
build for it). Also: content hunger. A one-verb game consumes twist ideas
faster than a multi-verb game; budget the sequel for the verb, not the
sequel's marketing.

**Re-derive it:** a climbing game whose only verb is planting a magnetic
anchor (walls accept one, ceilings another); every level is a new rule
about what the anchor sticks to.

## 4. Hades' boons — random rewards that respect player intent

**The mechanic.** Each chamber offers a choice of three boons (god
powers); boons come in builds (one god's sets synergize), rarity varies,
and duos/legendaries are rare lock-ins. The run's power arrives randomly
but the *shape* of the build is chosen.

**Why it works.** Randomness supplies variety; choice supplies agency. The
offered trio is filtered (compatible slots, your recent gods weighted), so
the player is never offered a dead pick — variance acts inside a design
corridor. Failure converts to meta-progression (darkness, keepsakes,
contracts) so a lost run still banks something, which is what makes the
roguelite loop sustainable rather than punishing. Finally, boon rarity is
genuinely exciting because the ceiling is real: legendaries change plans.

**Anatomy, generically (the "random choice" template):**
1. A reward pool with internal synergy families, so any single pick
   implies future picks.
2. Offer filtering that respects build state (never offer a fourth armor
   piece to a dodge build).
3. Rarity as a real ceiling, with rarity rates tuned so the dream pick
   appears every few runs — not every run, or rarity stops mattering.
4. A meta layer that converts failure into permanent, honest progress.

**Failure modes:** offer pools that ignore build state (dead choices),
rarity inflation (everything legendary), and meta progression so strong
the run's choices stop mattering (the meta plays itself).

**Re-derive it:** an expedition roguelite where ore veins grant "prospector
tricks" (scanning pulses, loadout mods) drafted in threes from families —
seismic, pyrotechnic, logistical — with rare "mother lode" tricks that
reshape the run.

## 5. Cross-study patterns

Four mechanics, four genres, and the same three laws underneath:

1. **Decisions, not content, carry depth.** Deck drafts, recipe knowledge,
   chamber twists, boon trios — none add verbs; they multiply choices.
2. **Teaching is content.** All four games spend their best design on the
   first exposure and the first test of each rule, and their worst sin is
   an under-taught twist.
3. **Failure must bank something.** A dead run that teaches deck synergies,
   reveals a recipe, shows a chamber rule, or pays meta currency keeps the
   loop honest; a run that banks nothing is pure loss.

## 6. How to run your own dissection

1. Pick a mechanic you envy. Play it for two hours with the question
   "what decision am I actually making?" running.
2. Write its anatomy in 3-5 numbered rules, stated generically (no
   proper nouns allowed in the anatomy).
3. List its dependency: what else in that game has to be true for the
   mechanic to work (economy, pacing, failure cost)?
4. Re-derive it in your genre with your constraints — new nouns, same
   skeleton.
5. Note what you changed and why; the delta between the original and your
   version is where your design actually lives.