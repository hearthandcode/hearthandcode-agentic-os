---
name: game-mechanics-design
description: >
  Load this skill when you need to design, specify, and iterate on game mechanics
  — from core loop to individual mechanic specification with playtesting built
  in from the start. Produces mechanic specs, design doc sections, and
  playtest plans.
---

# game-mechanics-design

## 01 — Purpose

Game mechanics are the rules and systems that create player experience. A well-designed mechanic is learnable, expressive, and aligned with the experience you want the player to have. This skill gives you the tools to design, specify, and iterate on mechanics with discipline — from the first napkin sketch to the playtest-informed revision.

The skill covers the full arc: understanding what makes a mechanic work (core loops, player motivation), specifying it precisely enough to build or prototype (mechanic specs, documentation), and validating it through playtesting and balancing. It does not cover level layout, narrative design, or art direction — those are separate domains with their own skills.

**Three outcomes this skill owns:**
1. A mechanic that is specified clearly enough for a developer to implement or a designer to test.
2. A playtest plan that surfaces the mechanic's strengths and weaknesses before full production.
3. A balanced set of mechanics where no single strategy dominates and player choices feel meaningful.

---

## 02 — When to Use / When Not to Use

### Use this skill when:

1. **Designing a new game's core loop.** You need to define what the player does moment-to-moment, what keeps them going, and how the loop escalates. This is the highest-leverage application of this skill.

2. **Specifying a single mechanic rigorously.** You have an idea for a mechanic — a crafting system, a combo system, a movement ability — and you need to write it up so someone else can prototype it.

3. **Diagnosing why a mechanic feels bad.** Players report that a mechanic is frustrating, boring, or confusing. You need structured analysis to find the root cause.

4. **Preparing a mechanic for prototyping.** You want to answer "what's the simplest thing I can build to test whether this works?" before committing to full implementation.

5. **Reviewing an existing mechanic for balance.** A mechanic has one dominant strategy, or an ability is never chosen, or a resource is always abundant. You need systematic tools to find and fix these issues.

6. **Communicating a mechanic to a team or client.** You need to write a spec that another designer, developer, or stakeholder can understand and act on.

### Do NOT use this skill when:

1. **You need narrative or story work.** Use `story-and-narrative-design` for plot, character, and worldbuilding. Mechanics and narrative intersect (mechanics can tell stories), but this skill does not cover narrative craft.

2. **You are doing math-only economy tuning.** Use `game-economy-balancing` for currency systems, progression pacing, and spreadsheet-driven balance passes. This skill covers the feel and player-experience side of mechanics; the economy skill covers the math.

3. **You need visual feedback on a UI element or screen.** Use `ui-design-critique` for visual hierarchy, layout, and accessibility. A mechanic's UI matters, but this skill focuses on the underlying rule system.

4. **You are brainstorming general creative ideas without a game context.** Use `brainstorming-and-ideation` for divergent thinking sessions. This skill assumes you're working within a game design context with mechanics intent.

---

## 03 — Inputs and Outputs

### Inputs

You should supply at least ONE of these before starting:

- **A design brief:** What kind of game is this? What audience? What feeling should the mechanic create? A half-page description is enough to start.
- **A mechanic idea:** Even a rough "I want the player to combine items to make new ones" is enough — the skill helps you develop it.
- **A pain point:** "Players are not using the shield ability" or "progression feels flat after level 5" gives the skill a diagnostic starting point.
- **A constraint set:** Platform (mobile/PC/console), genre (RPG/puzzle/action), player count (single/multi), development budget (small/medium/large) — these shape which solutions are viable.
- **An existing mechanic spec or design doc:** For revision or review, the skill can analyze and suggest improvements.

### Outputs

The skill produces documents and plans. Each output uses the templates in `references/` and `templates/`:

1. **A mechanic specification** (`templates/mechanic-spec-template.md`) — one mechanic defined precisely: trigger, resolution, edge cases, failure states, and player-facing description. Implementable from this document alone.

2. **A game design document section** (`templates/game-design-doc-template.md`) — a larger document covering the core loop, progression arc, and how mechanics relate.

3. **A playtest plan** — who to test with, what to watch for, what metrics to capture, and how to triage results. Uses `references/playtesting-methods.md`.

4. **A balance analysis** — identifying dominant strategies, dead options, and tuning recommendations. Uses `references/balancing-fundamentals.md`.

5. **A mechanic case study comparison** — when learning from existing games, the skill produces annotated analyses using `references/mechanics-case-studies.md`.

---

## 04 — Workflow

### Step 1 — Frame the design space
Reference: `references/core-loop-design.md`

Before designing anything, establish the context: What is the game's core loop? What does the player do in a 30-second loop? A 30-minute loop? What motivates them to continue? Write these down — even a paragraph each.

Checkpoint question: "Can I state the core loop in one sentence? If not, I need to narrow the scope before designing mechanics."

### Step 2 — Identify the mechanic's job
Reference: `references/mechanics-taxonomy.md`

Place your mechanic in one of the taxonomy categories: action mechanic (what the player directly does), system mechanic (rules that govern behavior), progression mechanic (how the player grows), or social mechanic (how players interact). Each category has different design expectations and failure modes.

Checkpoint question: "What job is this mechanic doing for the player experience? If it's doing more than one job, should it be split?"

### Step 3 — Map the player motivation
Reference: `references/player-motivation-models.md`

Map the mechanic to player motivation. Does it satisfy intrinsic motivation (competence, autonomy, relatedness — SDT)? Does it rely on extrinsic rewards (points, unlocks)? Mechanics that only use extrinsic motivation often feel hollow after the novelty wears off.

Checkpoint question: "If the extrinsic rewards were removed, would players still engage with this mechanic?"

### Step 4 — Specify the mechanic
Reference: `templates/mechanic-spec-template.md`, `schemas/mechanic-spec.schema.json`

Write the mechanic spec. Include: trigger condition, resolution steps, inputs/outputs, edge cases (what happens at zero, maximum, or unexpected states), failure states (what does a player mistake look like and how is it communicated), and the player-facing description (what the player sees and understands).

The schema at `schemas/mechanic-spec.schema.json` encodes the required fields. Validate your spec against it before proceeding.

Checkpoint question: "Could a developer implement this mechanic from the spec alone? If not, what's missing?"

### Step 5 — Build a prototype plan
Reference: `references/prototyping-playbook.md`

Design the fastest testable version of your mechanic. Paper prototype? Digital with basic shapes? Existing game mod? The playbook helps you match the prototype fidelity to the question you need answered.

Checkpoint question: "What is the smallest thing I can build that will tell me whether this mechanic works?"

### Step 6 — Design the playtest
Reference: `references/playtesting-methods.md`

Design a playtest that will actually surface the mechanic's problems. Who should test (target audience or general)? What will you watch for? How will you capture feedback without leading the player? How many sessions before you have confidence?

Checkpoint question: "If the mechanic has a fatal flaw, will this playtest design catch it?"

### Step 7 — Run the playtest and triage feedback
Reference: `references/playtesting-methods.md`, `references/mechanics-documentation.md`

After the playtest, triage feedback into: critical issues (the mechanic is broken or un-fun), major issues (the mechanic needs significant revision), minor issues (tuning and polish), and non-issues (one player's preference). Update the spec with findings.

Checkpoint question: "For each critical issue, can I name the specific change I'll make and how I'll test it?"

### Step 8 — Balance pass
Reference: `references/balancing-fundamentals.md`

Check for dominant strategies, dead options, and resource imbalances. Identify the levers you can tune (cost, cooldown, range, duration, power) and change one variable at a time. Re-test the minimum viable change.

Checkpoint question: "Have I confirmed that my attempted fix actually resolved the balance issue, or did it just shift the problem to a different mechanic?"

### Step 9 — Document and archive
Reference: `references/mechanics-documentation.md`

Write the final mechanic spec with all revisions incorporated. If working on a larger project, update the relevant section of the game design doc using `templates/game-design-doc-template.md`.

Checkpoint question: "If I come back to this mechanic in six months, will this documentation be enough to understand why the mechanic works the way it does?"

### Step 10 — Learn from existing designs
Reference: `references/mechanics-case-studies.md`

Before finalizing, review how similar mechanics work in published games. Use the case studies to check whether you've encountered known pitfalls. This is not about copying — it's about not rediscovering known failure modes.

Checkpoint question: "Are there known failure modes for this type of mechanic that I haven't addressed?"

---

## 05 — Rules and Quality Bar

1. **One mechanic, clear core.** A mechanic should do one thing well. If you can't describe it in one sentence, it's doing too much.

2. **Specify the edge cases first.** What happens at zero, at max, during interruption, with invalid input? Edge cases reveal 80% of design problems before the first prototype.

3. **Test the riskiest assumption first.** Identify the single assumption your mechanic depends on — then build the cheapest test for it. If that assumption fails, the rest doesn't matter.

4. **Prefer simple resolution over realistic simulation.** A mechanic that resolves in one step is more learnable than one with a multi-step calculation, even if the latter is "more realistic."

5. **Playtest with silence.** Don't explain the mechanic. Watch what players do. Their behavior will tell you more than their feedback.

6. **One variable at a time in balance passes.** Changing cost AND cooldown AND damage simultaneously means you won't know which change caused the result.

7. **Document the failure.** When a mechanic fails in testing, document why. That knowledge is as valuable as the working mechanic.

8. **Match mechanic complexity to player skill.** A mechanic that requires 100 hours of practice to master is fine for a core audience game. For a casual game, that's a design failure.

9. **Every mechanic communicates theme.** The rules you choose tell the player what kind of world this is. A combo system says "this world rewards mastery." A crafting system says "this world rewards preparation."

10. **If a playtester asks "what should I do?", the mechanic has failed.** The best mechanics are understood through play, not instruction.

11. **One playtest session is anecdote. Three is data. Ten is a pattern.** Don't balance based on one player's feedback.

12. **The mechanic must be fun without its rewards.** If the core interaction isn't satisfying, adding more rewards will not fix it long-term.

13. **You cannot design a mechanic in isolation.** Every mechanic exists in relation to every other mechanic in the game. A buff that costs nothing affects every other resource system.

14. **When a mechanic is cut, save the spec.** You may reuse the concept in a different context, or the post-mortem may reference why it was cut.

15. **The player does not need to understand how the mechanic works. They need to understand what it DOES.** The internal logic can be complex; the output must be legible.

16. **Iteration is the design process, not a correction.** Every mechanic goes through multiple versions. The first version is a hypothesis, not a failure.

---

## 06 — Worked Example

**Scenario:** Design a roguelite "one more run" upgrade mechanic for a game called "Deep Delve" — a turn-based dungeon crawler where the player descends through procedurally generated caverns. The core loop: move, discover, fight, loot, descend. The upgrade mechanic should give the player meaningful choices between runs that change how the next run plays.

### Step 1 — Frame the design space

The core loop in one sentence: "The player moves to an adjacent cavern tile, discovers what's there (enemy, treasure, trap, or event), resolves the encounter, and chooses whether to descend further or retreat."

The "one more run" feeling comes from: (a) the run was short and left the player wanting more, (b) the player unlocked something new that they want to try, (c) the player believes they can do better next time. Our upgrade mechanic needs to support (b) — give the player something to look forward to after a failed or completed run.

### Step 2 — Identify the mechanic's job

This is a **progression mechanic** — it governs how the player grows between runs. It also has a social element (share your build with other players), but primarily it's about progression.

The job: After each run, the player chooses one upgrade from a small set (3 choices). The upgrade changes how their next run plays — a new ability, a stat modifier, or a rule-breaking exception. This creates anticipation for the next run.

### Step 3 — Map the player motivation

Intrinsic: The upgrade gives the player a new way to play (autonomy). Mastering the upgrade improves their performance (competence). The upgrade system connects each run to the next (relatedness to the meta-game).

Extrinsic: No points or unlocks beyond the upgrade itself. This is important — the upgrade IS the reward.

Riskiest assumption: "Players will find the upgrades exciting enough to want another run." Test this with a paper prototype showing the upgrade choices and asking "which one do you choose and why?"

### Step 4 — Specify the mechanic

Using `templates/mechanic-spec-template.md`:

**Mechanic Name:** Rune Upgrades (run-altering meta-progression)

**Trigger:** Run ends (player dies, retreats, or reaches the bottom).

**Resolution:** Player is shown 3 randomly-selected rune stones from a pool of 12. Each rune stone modifies the next run. The player picks one. The unchosen runes are shuffled back into the pool.

**Rune examples:**
- Ember Rune: All damage dealt by the player is increased by 25%, but the player cannot heal.
- Echo Rune: The player sees the contents of the next 3 tiles before moving.
- Roots Rune: The player cannot skip encounters — must resolve every enemy tile, but gains double loot.
- Flux Rune: All numerical values in the run are randomized between 50% and 150% of their normal value.

**Edge cases:**
- Pool exhaustion: If the player has seen every rune in the last 3 runs, the pool reshuffles fully.
- Rune stacking: Multiple runs with the same rune stack effects with diminishing returns (e.g., two Ember runes = +40% damage, not +50%).
- First run: The player starts with no rune. The first run is "pure" to establish a baseline.

**Failure states:**
- If a rune would make the run impossible (e.g., Roots Rune on a level with a required trap-skip), the rune is not offered.
- If the player doesn't pick within 60 seconds, a random rune is assigned.

**Player-facing description:** "After every run, three rune stones glow on the altar. Choose one. Each changes how your next descent works — new powers, new risks, new strategies."

### Step 5 — Build a prototype plan

Fastest test: Index cards. Create 12 cards with one rune each. Play a minimal version of Deep Delve: 10 cards for dungeon tiles (monster, treasure, trap, empty, boss). Run through a few turns, then die on purpose. Show the rune selection. Note: (1) does the player want to play again? (2) which rune did they choose and why? (3) does the choice feel meaningful?

### Step 6 — Design the playtest

Testers: 3-5 people familiar with roguelike games (core audience). Protocol:
1. Play one run without runes (baseline — 5 minutes).
2. Die, choose a rune.
3. Play a second run with the chosen rune (5 minutes).
4. Short interview: "How did the rune change the experience? Would you want to see other rune options?"
5. Repeat with a different rune.

### Step 7 — Run the playtest and triage

Results from beta testing (simulated for this example):
- **Critical issue:** Players ignored the choice entirely on their first death — they wanted to "just play again" without reading rune descriptions.
  - Fix: Runes are not offered on the first death. Only after the second run, giving the player a baseline.
- **Major issue:** The Echo Rune was always chosen when offered — it's too useful.
  - Fix: Reduce Echo to showing 1 tile ahead instead of 3. Re-test.
- **Minor issue:** Some rune names were confusing ("Flux Rune" — what does flux mean here?).
  - Fix: Rename to descriptive names ("Chaos Rune").
- **Non-issue:** One player wanted to keep two runes.
  - Noted but not acted on — the one-per-run constraint creates meaningful choices.

### Step 8 — Balance pass

After fixes: Ember Rune's +25% damage is strong but the no-healing penalty is severe enough that players only pick it on high-risk runs. Echo Rune (now 1 tile) is useful but not mandatory. Roots Rune creates interesting decisions (players weave through the dungeon to minimize compulsory encounters). Flux Rune is a chaos option for experienced players.

Dominant strategy check: No single rune is picked >40% of the time in the player tracking. Dead option check: All 12 runes are picked at least once across a 50-run simulation.

### Step 9 — Document

The Rune Upgrade mechanic is now documented in the game design doc at `gdd/mechanics/rune-upgrades.md`. Key decisions recorded: one-rune-per-run (prevents runaway power), no rune on first death (gives baseline), descriptive names (reduces confusion), pool reshuffle (prevents stale choices).

### Step 10 — Learn from existing designs

Case studies (from `references/mechanics-case-studies.md`):
- **Slay the Spire's card rewards:** Similar three-choice system, but the choices are immediate (you pick during the run, not between runs). The pool exhaustion mechanic (reshuffle after seeing everything) is taken from StS's card pool management.
- **Hades' boons:** Boons change how the same weapons play. Our runes serve a similar function but at the meta-level rather than in-run.

---

## 07 — Failure Modes and Recovery

1. **The mechanic is fun once, but not repeatable.**
   - *Early signal:* Playtesters say "that was cool" once but don't want to do it again.
   - *Corrective:* Add emergent depth — rules that interact differently each time. A mechanic that plays out identically every time has no replay value.
   - *Prevention:* Before prototyping, ask "what would make me want to do this 50 times?"

2. **The mechanic is too complex to learn.**
   - *Early signal:* Testers ask "what should I do?" or make the same mistake repeatedly.
   - *Corrective:* Reduce the number of rules. Aim for one input, one outcome. If you need complexity, layer it — introduce the basic version first, add nuance as the player progresses.
   - *Prevention:* The 30-second test — can a new player understand the mechanic in 30 seconds of play?

3. **The mechanic has a dominant strategy.**
   - *Early signal:* All playtesters make the same choice or use the same approach.
   - *Corrective:* Remove the dominant option or give other options a reason to be chosen. Make the dominant strategy situationally good, not universally best.
   - *Prevention:* After first playtest, check: "would any rational player ever choose differently?"

4. **The mechanic conflicts with other mechanics.**
   - *Early signal:* Two mechanics cancel each other out or create an unintended synergy that breaks the game.
   - *Corrective:* Decide which mechanic's intent is stronger and revise the other. Document the interaction so future designers know about it.
   - *Prevention:* After specifying each new mechanic, review it against every existing mechanic for interaction effects.

5. **The mechanic relies on the player understanding probability.**
   - *Early signal:* Players are frustrated that a 30% chance "never procs" or a 70% chance "always fails."
   - *Corrective:* Remove randomness or make it transparent (show the odds, use predictable patterns instead of pure random).
   - *Prevention:* Assume players cannot intuitively estimate probability. If the mechanic's success depends on probability comprehension, the mechanic is flawed.

6. **The mechanic creates analysis paralysis.**
   - *Early signal:* Players pause for too long before acting, or express anxiety about making the wrong choice.
   - *Corrective:* Reduce the number of options, or make options more clearly distinct so the choice is obvious.
   - *Prevention:* Set a time limit in testing. If players routinely need more than 5 seconds to choose, the mechanic has too many branches.

7. **The mechanic is balanced by guesswork rather than iteration.**
   - *Early signal:* Numbers keep changing but the feel doesn't improve.
   - *Corrective:* Run a dedicated balance playtest focused on one variable. Strip everything else away and tune that one lever against a known baseline.
   - *Prevention:* Each balance pass should answer one specific question, not "let's see if this feels better."

8. **The mechanic is documented for the designer, not the implementer.**
   - *Early signal:* A developer reads the spec and asks clarifying questions about basic behavior.
   - *Corrective:* Rewrite the spec from the implementer's perspective. Add pseudocode, flowcharts, or example play sequences.
   - *Prevention:* Before delivering, ask "could I implement this myself with only this document?"

---

## 08 — Supporting Files Index

| File | Purpose | Used In |
|---|---|---|
| `references/core-loop-design.md` | Core loop anatomy and 30-second/30-minute loops | Section 04, Step 1 |
| `references/mechanics-taxonomy.md` | Pattern catalog for action, system, progression, social mechanics | Section 04, Step 2 |
| `references/player-motivation-models.md` | Intrinsic/extrinsic motivation, player archetypes | Section 04, Step 3 |
| `references/prototyping-playbook.md` | Paper and digital prototyping methods | Section 04, Step 5 |
| `references/mechanics-documentation.md` | How to write a mechanic spec others can build | Section 04, Step 9 |
| `references/balancing-fundamentals.md` | Levers, cost curves, dominant-strategy checks | Section 04, Step 8; Section 05 |
| `references/playtesting-methods.md` | Recruitment, protocols, observation, feedback triage | Section 04, Steps 6-7 |
| `references/mechanics-case-studies.md` | 4 well-known mechanics dissected and re-derived | Section 04, Step 10 |
| `templates/mechanic-spec-template.md` | One-page mechanic specification template | Section 04, Step 4 |
| `templates/game-design-doc-template.md` | Game design document section template | Section 04, Step 9 |
| `schemas/mechanic-spec.schema.json` | JSON schema for mechanic spec validation | Section 04, Step 4 |
| `examples/worked-mechanic-design.md` | Full worked example from brief to playtest plan | Section 06 (companion) |