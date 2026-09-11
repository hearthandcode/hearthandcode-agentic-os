---
name: level-and-encounter-design
description: >
  Use when designing or revising game levels and encounters — laying out a
  level, pacing a beat sequence, designing a combat, puzzle, or boss
  encounter, planning a difficulty curve, teaching mechanics without text,
  or fixing a level that playtesting flagged. Produces a level spec with
  spatial layout, timed beat sequence, encounter blueprints, difficulty
  curve, telemetry targets, and a playtest protocol. Stops at rules and
  economy (game-mechanics-design, game-economy-balancing) and at art
  direction (ui-design-critique).
---

# level-and-encounter-design

## 01 — Purpose

A level is a promise about the player's next ten minutes: what they will
learn, what they will feel, and why they will keep going. Levels fail in
predictable ways — unreadable space, a curve that spikes, an encounter that
punishes instead of teaches, a corridor that says nothing. This skill exists
to catch those failures on paper, where a fix costs a line, instead of in
production, where a fix costs a rebuild.

The skill covers the arc from intent to verified space: turning an
experience goal into spatial composition (sightlines, landmarks, loops,
chokepoints), pacing that space into a beat sequence with an intensity arc,
designing the encounters that populate it from a pattern catalog, teaching
mechanics through placement rather than text, and validating the result with
telemetry targets and a playtest protocol. The output is a buildable,
testable level spec — not a mood board and not an essay.

**Three outcomes this skill owns:**

1. A level spec that a level builder can greybox from: zone list, beat
   sequence with timings, encounter blueprints, and the teaching plan —
   each decision recorded with its reason.
2. A difficulty curve that names intended intensity per beat, the
   player-state it assumes, and the rest beats that make the spikes
   survivable.
3. A validation plan: the telemetry events that will confirm or refute the
   design, and the playtest protocol that turns sessions into specific,
   retestable changes.

This skill treats a level as an argument the space makes to the player.
Every artifact it produces is judged by one question: could a builder and a
playtester act on this without asking the designer what they meant?

**Scope boundary.** This skill owns space, pacing, encounters, and
environmental storytelling. Adjacent work is adjacent: the rules and
systems those encounters exercise belong to game-mechanics-design; economy
tuning (drop rates, currency sinks across a game) belongs to
game-economy-balancing; the visual polish of the rendered space belongs to
ui-design-critique; narrative content beyond what the environment itself
carries belongs to story-and-narrative-design. Handoffs are explicit: this
skill hands the mechanics designer the decision goals each space must
serve, and hands the narrative designer the environmental beats the story
must land on.

**Operating stance.** Three habits run through everything here:

- **Teach by placement, not by text.** A mechanic is taught when the space
  makes the safe path require it and the layout lets failure be cheap and
  legible. Tutorial text is a confession that the teaching space failed.
- **Curve before content.** The intended intensity per beat is decided
  before encounters are placed; content that fills an unplanned curve
  produces spikes nobody can fix late.
- **Cheap space first.** Paper maps, greybox, and blockouts answer layout
  questions; production art answers taste questions. Cost follows the
  question, never leads it.

**Vocabulary used throughout.** These terms are used with these meanings in
every file in this skill:

- *Beat* — one unit of intended experience inside a level (introduce,
  pressure, rest, payoff, reveal), with a target duration.
- *Zone* — a contiguous stretch of space with one dominant beat.
- *Encounter* — a designed unit of opposition or challenge inside a zone:
  combat, puzzle, traversal hazard, or stealth set piece.
- *Pattern* — a reusable encounter structure (arena, gauntlet, puzzle-lock,
  boss) with known strengths, costs, and failure modes.
- *Gating* — a barrier that forwards progress only when the player has
  demonstrated a capability.
- *Intensity* — the designed demand on player attention and skill at a
  beat, rated 0-10 relative to the game's own baseline.
- *Rest beat* — a low-intensity stretch that lets the player consolidate
  what a preceding spike taught.
- *Sightline* — what the player can see from a position; the primary tool
  for directing attention and teaching affordance.
- *Landmark* — a memorable object used for orientation and route recall.
- *Retry loop* — the fail-learn-retry cycle a teaching encounter is built
  to run cheaply.
- *Telemetry target* — a pre-registered number (completion rate, death
  count at a beat, time-to-finish band) against which real data is read.

## 02 — When to Use / When Not to Use

**Use this skill when any of these are true:**

1. **Laying out a level.** A space must be composed from nothing or from a
   brief: zones, routes, sightlines, landmarks, gating, and the beat
   sequence the player will walk. Use before any greybox is built.
2. **Designing an encounter.** A combat arena, a stealth setup, a
   puzzle-lock, a gauntlet, or a boss needs its pattern chosen, its space
   shaped, and its fail states made legible and cheap.
3. **Fixing pacing.** A level drags, spikes, or ends before it pays off;
   the intensity arc needs to be drawn and the beat sequence rebalanced.
4. **Planning a difficulty curve.** Intended intensity per beat, per
   level, or across a game's opening hours needs to be explicit before
   tuning begins.
5. **Teaching mechanics without text.** A new verb (a grapple, a stealth
   crouch, an environmental hazard) must be taught through placement,
   safe failure, and gating — the tutorial-level problem.
6. **Writing a level spec for the team.** Builders, encounter designers,
   and playtest coordinators each need their slice of one coherent,
   buildable document.
7. **Turning playtest data into changes.** Session notes, death heatmaps,
   or completion telemetry need triage into layout, encounter, pacing, or
   readability fixes with retests attached.
8. **Using environmental storytelling.** The space itself must carry
   history, foreshadowing, or mood — props, arrangement, and state —
   without cutscenes or text.

**Do not use this skill when:**

1. **The mechanic itself is the job.** Inventing, specifying, or balancing
   the grappling rule, the stealth detection model, or the barrel damage
   numbers belongs to game-mechanics-design. This skill decides where the
   mechanic is taught and exercised; the rule's content is theirs.
2. **Economy tuning is the job.** Drop rates, currency flow, and pricing
   across a game belong to game-economy-balancing. A reward chest's
   placement is this skill; its contents' economics are theirs.
3. **Art direction is the job.** Palette, lighting mood, asset style, and
   rendered visual polish belong to ui-design-critique. Greybox
   readability is this skill; the paint is not.
4. **The game's story content is the job.** Plot, dialogue, and character
   belong to story-and-narrative-design. Environmental storytelling
   technique is here; the tale being told is theirs.
5. **Core loop design is the job.** What the player does every thirty
   seconds and why it rewards belongs to game-mechanics-design. Levels
   stage a loop; they do not define it.
6. **Test automation is the job.** Harnesses, CI gates, and automated
   soak tests belong to testing-strategy. This skill writes the playtest
   protocol and the telemetry event list, not the code that collects
   them.
7. **Production scheduling is the job.** Milestone planning and estimates
   belong to operations-and-process-design; this skill emits specs and
   playtest plans, and sequencing them is theirs.
8. **A walkthrough or strategy guide is the job.** Documenting a finished
   level for players needs no design skill here — it is writing from the
   shipped artifact.

When in doubt: if the deliverable is a *zone*, a *beat*, an *encounter
blueprint*, a *curve*, or a *telemetry target*, this skill applies. If it
is a *rule*, an *economy*, a *render*, or a *plot point*, hand off at the
boundary with the artifacts the neighbor needs.

## 03 — Inputs and Outputs

**Inputs this skill consumes:**

- An experience brief: the intended feel and length ("10 minutes,
  introductory, teaches grappling, stealth, and explosive barrels without
  text"), the audience's assumed skill, and what comes before and after.
- The mechanics inventory: verbs available to the player, with their
  current spec status, and any mechanic that must be taught by this level.
- Constraints: engine or tooling limits, team capacity, art budget,
  platform performance targets, and any locked geometry or existing
  levels that continuity must respect.
- Reference material: the game's own prior levels (for escalation
  baselines), competitor levels worth learning from, and any documented
  pillars the game carries.
- For revision work: the existing level spec, playtest notes, death
  heatmaps, completion telemetry, and session recordings if they exist.

**Input readiness checklist.** Before starting the workflow, confirm:

- The experience goal is one sentence the team can argue with — not a
  theme, a verb ("stealth playground"), or a feature list.
- The mechanics to be taught are named individually; "teach the systems"
  is not teachable, "teach the grapple's swing arc" is.
- The assumed player state is stated: what the player can already do, and
  what this level may assume they know.
- Art budget is known, because beat count without budget is fiction.
- For revisions: the complaint is sourced (telemetry, sessions, reviews),
  because a fix aimed at a rumor misfires.

**Outputs this skill produces:**

- `templates/level-spec-template.md` — the master artifact: experience
  goal, zone list, beat sequence with timings, encounter blueprints,
  teaching plan, difficulty curve, telemetry targets, and playtest plan.
- `schemas/level-spec.schema.json` — the machine-checkable shape of that
  spec for teams that pipeline level data into tools.
- Spatial map: ASCII or diagrammed zone layout with sightline notes,
  landmarks, loops, and chokepoints.
- Encounter blueprints: one per designed encounter — pattern chosen and
  why, space shape, player options, fail states, and retry cost.
- Teaching plan: per mechanic — where introduced, where safely failed,
  where combined, where gated, and what text was deliberately avoided.
- Difficulty curve: beat-by-beat intensity ratings with rest beats
  marked, plus the escalation rationale against the game's baseline.
- Telemetry and playtest plan: events to log, targets per event, test
  protocol, sample size, and the triage rubric for results.

**Acceptance criteria per output.** An output is done when:

- A *beat sequence* covers the level end to end, each beat names its
  zone, target duration, intensity, and job, and durations sum to the
  level's target length.
- An *encounter blueprint* names its pattern, the option space the player
  has, every fail state, and the cost of failing — and the space shape
  can be greyboxed from the description.
- A *teaching plan* introduces each mechanic in a space where failure is
  cheap and legible, exercises it in combination, and gates progress on
  it — with zero reliance on tutorial text.
- A *difficulty curve* states intended intensity per beat, marks rest
  beats, and stays inside the game's escalation baseline with reasons
  where it deliberately departs.
- A *telemetry plan* registers events, targets, and cadence before the
  level ships to testers, so data arrives against a pre-agreed reading.

**Artifact conventions.** How outputs are named, stored, and linked:

- One spec file per level; encounter blueprints are sections of it, or
  separate files named `level-<name>-<encounter>.md` when large.
- Zone IDs are stable strings (`z01_collapse`, `z04_stealth`) that never
  change across revisions; telemetry keys on them, so renaming them
  breaks the data line.
- Beats carry IDs (`b02`) that stay fixed through revisions; "beat 2
  kills too many players" must mean the same beat in every meeting.
- Revisions append, not overwrite: each spec version notes date, playtest
  input, and the changes made in response.
- The ASCII map lives in the spec file itself so it travels with the
  document; rendered screenshots link outward but never replace the map.

Everything the skill produces is a markdown file (plus the JSON schema);
nothing requires a special toolchain, and a builder who has never seen
this repository can greybox from the spec without asking questions.

## 04 — Workflow

The steps below are the full arc from experience brief to playtest-verified
level. A narrow job (one encounter, a pacing fix) enters at the step that
matches the symptom and exits at step 12. Greenfield levels run the whole
list. Each step names its reference file; load the reference before doing
the step's work.

1. **Fix the experience goal and player state.** Write the one-sentence
   goal, the target duration, the assumed player skills, and the list of
   mechanics this level must teach or exercise. Read
   `references/level-design-principles.md` first — readability,
   affordance, flow, and gating govern every later step.
2. **Choose the pacing shape.** Decide the intensity arc: where the
   spikes are, where the rests are, what the level's climax beat is, and
   how it escalates against the game's baseline. Read
   `references/pacing-and-difficulty-curves.md`; draw the curve before
   drawing the map.
3. **Compose the space.** Draft the zone list and the map: sightlines,
   landmarks, route loops, chokepoints, and gating positions. Read
   `references/spatial-composition.md`. Check every zone against the
   readability and affordance principles from step 1.
4. **Sequence the beats.** Turn the map and curve into a timed beat
   sequence: each beat gets a zone, a duration, an intensity, and a job.
   Verify durations sum to the target length and the curve from step 2
   survives contact with the map.
5. **Design the encounters.** For each high-intensity beat, choose an
   encounter pattern and blueprint it. Read
   `references/encounter-design-patterns.md` for the pattern catalog —
   arena, gauntlet, puzzle-lock, boss — with each pattern's strengths,
   costs, and failure modes. Blueprints name space shape, player options,
   fail states, and retry cost.
6. **Plan the teaching.** For each mechanic to be taught, place the
   introduction, the safe failure, the combination exercise, and the
   gate. Read `references/narrative-through-environment.md` for how the
   environment signals affordance and stakes without text; the teaching
   plan doubles as the environmental storytelling plan.
7. **Write the spec.** Assemble everything into the level spec using
   `templates/level-spec-template.md`, validating the structure against
   `schemas/level-spec.schema.json` when tooling will consume it. The
   spec is the handoff artifact; it must stand alone.
8. **Greybox and self-test.** Build the cheapest playable space and walk
   it: sightlines as mapped, beats as timed, fail states as legible.
   Fix layout issues here; production cost multiplies whatever survives
   greybox.
9. **Run the level playtest protocol.** Test with players who match the
   assumed player state. Read `references/playtesting-levels.md` for the
   structured protocol, focus areas, silent-mechanic-teaching test, and
   minimum sample set. Watch for where players look, hesitate, and die —
   not just where they fail.
10. **Instrument and read telemetry.** Log the events registered in the
    spec (deaths by zone, completion rate, time-to-finish, route
    choices). Read `references/level-metrics-and-telemetry.md` for the
    core metrics and heatmap reading; compare actuals to the spec's
    targets.
11. **Triage and revise.** Turn findings into prioritized changes:
    layout fixes before encounter tuning, encounter tuning before
    number tweaks. Append the revision to the spec with the input that
    prompted it. Re-run the affected playtest focus areas.
12. **Close the loop.** When targets are met (or departures are accepted
    with reasons), mark the spec verified and file the lessons. Read
    `references/level-case-studies.md` to compare the level's choices
    against annotated classics — as a checklist for what was learned,
    not as a template to copy.

Steps 1-4 are thinking work with one-page outputs. Steps 5-7 are design
work with buildable artifacts. Steps 8-12 are evidence work. Most broken
levels skipped step 2 — the curve — and discovered their spike in
playtest, where the fix costs a rework instead of an eraser.

**Emitted artifacts by step:**

| Step | Emits |
| --- | --- |
| 1 | Experience goal, player state, mechanics-to-teach list |
| 2 | Intensity arc with rest beats and climax marked |
| 3 | Zone list and spatial map with sightline notes |
| 4 | Timed beat sequence covering the level |
| 5 | Encounter blueprints for high-intensity beats |
| 6 | Teaching plan and environmental storytelling notes |
| 7 | Assembled level spec (and schema validation where used) |
| 8 | Greybox findings and spec amendments |
| 9 | Playtest session notes in protocol format |
| 10 | Telemetry readings against registered targets |
| 11 | Prioritized revision list, appended to the spec |
| 12 | Verification note and lessons filed |

**Common entry points.** Not every job starts at step 1:

- *Greenfield level:* start at 1, run all twelve.
- *Single encounter:* enter at 5 with the beat's context from the spec;
  exit at 7 with a blueprint.
- *Pacing fix:* enter at 2 with playtest notes; loop 2 → 4 → 5.
- *Readability fix:* enter at 3 with the complaint source; check
  sightlines, affordances, and gating before touching encounters.
- *Telemetry review:* enter at 10 with the spec's targets in hand; exit
  at 11 with triaged changes.

**Working rhythm.** The full arc runs in four working sessions:

- Session one: steps 1-4, ending in a sequenced, mapped beat sheet.
- Session two: steps 5-7, ending in a buildable spec.
- Session three: steps 8-9, greybox and first player sessions.
- Session four: steps 10-12, telemetry reading, triage, verification.

The rhythm assumes one designer plus a builder; a larger team parallelizes
sessions two across zones. What does not compress is the ordering: goal
before curve, curve before map, map before encounters, encounters before
teaching, teaching before testing. Reversing any of those orders is how a
level becomes a corridor with fights in it.

## 05 — Rules and Quality Bar

1. **One sentence of intent per level.** The experience goal is written,
   visible, and argued with; every later decision cites it. A level with
   no stated intent is a corridor with decoration.
2. **The curve exists before the content.** Intended intensity per beat is
   decided before encounters are placed; content that fills an unplanned
   curve produces the spike nobody can fix late.
3. **Teach by placement; budget text to zero.** Every mechanic gets an
   introduction space, a safe failure space, a combination space, and a
   gate. If the teaching needs a paragraph, the spaces failed — fix the
   spaces.
4. **Failure is cheap, legible, and fast to retry.** A teaching encounter
   that costs two minutes of walking before the next attempt is a
   churn machine. Death must show the player what killed them.
5. **Every encounter names its pattern and its alternative.** The blueprint
   records why the pattern fits this beat and what was rejected —
   unrecorded choices get relitigated every time the encounter is tuned.
6. **Sightlines are designed, not inherited.** What the player can see
   from every decision point is checked against what the beat needs them
   to see; accidental sightlines leak the level's secrets and kill
   stealth setups.
7. **Gates prove capability.** A barrier forwards progress only after the
   player has demonstrated the mechanic it exists to verify; a gate that
   opens on proximity teaches nothing and wastes the space.
8. **Rest beats are scheduled, not accidental.** Consolidation stretches
   follow spikes by design, with something worth looking at; a curve of
   all spikes reads as grind, and a curve of all rests reads as filler.
9. **Landmarks orient.** Every route decision point has a memorable object
   the player can navigate by; a player who cannot rebuild the level's
   map in their head after one run will not find the optional content.
10. **Telemetry targets are pre-registered.** Death counts, completion
    bands, and route splits are written into the spec before testing;
    targets invented after the data are excuses wearing a lab coat.
11. **Playtest notes name behaviors, not verdicts.** "Player stopped at
    the collapsed pillar for 40 seconds, then quit" beats "confusing" —
    the behavior is actionable, the adjective is not.
12. **Fix order: layout, encounters, numbers.** A death heatmap cluster
    is treated as a readability or layout problem first; tuning damage
    values on a misread space hides the problem and doubles the retest.
13. **Zone and beat IDs never change.** Telemetry and meeting notes key
    on them; renaming them breaks the data line and rewrites history.
14. **Escalation is argued against a baseline.** Every difficulty
    departure from the game's opening baseline is recorded with its
    reason, because unrecorded spikes are indistinguishable from
    mistakes by the next level's designer.
15. **Greybox decides; production confirms.** Layout questions are settled
    at the cheapest artifact; no production art is spent on a space
    whose beat timing has not survived a greybox walk.
16. **Hand off at the boundary, with the artifact.** The mechanics
    designer receives the decision goals each space must serve; art
    receives the beat moods and sightline requirements; narrative
    receives the environmental beats. Every handoff names the open
    questions the receiver must answer.

## 06 — Worked Example

Scenario: **Cavern Run**, an action-platformer, needs its introductory
level: **10 minutes for a first-time player**, teaching **grappling**,
**stealth**, and **explosive barrels** — with no tutorial text. The full
run is expanded zone-by-zone in `examples/worked-level-design.md`; this
section shows the intermediate artifacts and the reasoning between them.

**Steps 1-2 artifacts (goal and curve).** Experience goal: "a first-time
player leaves able to grapple under pressure, move unseen, and weaponize
the environment — without reading a word." Player state: can run, jump,
and attack; nothing else. Mechanics to teach: grapple (swing arc and
release timing), stealth (sightline avoidance, patrol rhythm), barrel
(positional damage, chain reactions). Intensity arc drawn first: 3
(landing) → 2 (first grapple, safe) → 5 (first barrel combat) → 1 (rest,
story beat) → 6 (stealth corridor) → 4 (decompression) → 8 (barrel gauntlet
climax) → 3 (exit vista). Rest beats at beats 4 and 6 are deliberate; the
climax is the only 8.

**Steps 3-4 artifacts (space and beats).** Six zones mapped in ASCII with
sightline notes: `z01_landing` (straight path, one readable landmark — a
broken lift frame), `z02_ravine` (the grapple gap: too wide to jump, hook
point rendered at eye level on the far wall), `z03_quarry` (barrel
introduction: scattered barrels, three dim-witted grunts), `z04_barracks`
(rest beat: environmental storytelling — abandoned bunks, a tally wall,
foreshadowing graffiti of the patrol captain), `z05_galleries` (stealth:
dark corridor, two patrols on readable loops, shadow pockets at eye
height), `z06_collapse` (climax gauntlet: barrels, grappling swings over
gap sequences, one locked gate the player must open by luring a patrol
into the barrel stack). Beats timed to sum to 10:00 with first-run
drift noted (+15% observed on comparable levels).

**Steps 5-6 artifacts (encounters and teaching).** Grapple introduction:
a gap-jump attempt is allowed first — the geometry makes the jump visibly
fail with no damage (cheap, legible failure), and the hook point's visual
affordance (glow-free silhouette against the light shaft) does the
teaching. Stealth corridor: patrol sightcones are readable via floor
lighting, failure means a reset to corridor start (8 seconds, cheap), and
the checkpoint sits *before* the sightline, not inside it. Barrel: the
first barrel is fired on by an enemy grunt at a scripted safe distance —
the player learns positional damage by watching, then uses it one beat
later. Gauntlet climax: pattern is a hybrid gauntlet-arena; player options
grapple-skips versus barrel lures; fail states all reset to 20 seconds
prior. Teaching plan registered: zero text, zero UI popups; all affordance
through light, silhouette, and patrol rhythm.

**Steps 7-8 artifacts (spec and greybox).** Spec assembled in the level
spec template and validated against the JSON schema for the build
pipeline. Greybox walk found two issues: the `z02` hook point read as
background geometry (fixed by moving it one meter into the light shaft),
and `z05`'s second patrol overlapped the first's route at 40 seconds
(making stealth trivially timed) — patrol offset retuned before player
testing.

**Steps 9-11 artifacts (playtest and triage).** Protocol from the
playtesting reference: five first-time players, silent-mechanic-teaching
test enabled (no text ever shown), focus areas pre-marked. Results:
grapple taught to 5/5 without text (target met); stealth corridor killed
the run for 2/5 — deaths clustered at the second patrol's turn (telemetry
heatmap confirmed the cluster); both misread the barrel chain-reaction in
the gauntlet as a hazard rather than a tool until their third attempt.
Triage, in fix order: layout first — the corridor's shadow pocket before
the second patrol was half a beat too shallow (deepened); encounter
second — the gauntlet's barrel stack was moved off the main path so the
chain reaction reads as chosen, not suffered; numbers last — no damage
tuning was touched. Revision appended to the spec with the input noted.

**Step 12 artifact (verification).** Second test round: completion 5/5,
deaths at the former cluster down from 11 to 2, all five players used a
barrel offensively at least once. Departures accepted with reasons:
average time-to-finish 11:40 against the 10:00 target — accepted
because the drift sits in the rest beat, and cutting rest beats to hit a
number was the wrong trade. Spec marked verified; lessons filed
(affordance needs light contrast, not decoration; patrol routes need
offset verification on paper before build).

**What the example demonstrates.** The curve was drawn before the map; the
teaching plan is entirely placement; every teaching moment allowed cheap,
legible failure; telemetry targets existed before the first test; the
triage respected the layout → encounter → numbers order; and a target
departure (11:40 vs 10:00) was accepted with a recorded reason rather
than silently missed.

**Adapting the example to another level.** The transferable skeleton, with
the Cavern Run specifics stripped:

- Teach one mechanic per introduction beat, with its safe failure adjacent
  — never two firsts at once.
- Rest beats are where environmental storytelling lands; the player who
  is not being tested is the player who has time to read the world.
- Stealth only works when the patrol's logic is readable on sight and the
  reset is cheaper than the failure was instructive.
- Set-piece climaxes pay off only the mechanics the level already taught;
  a climax that requires an untaught trick is a checkpoint-eater.

## 07 — Failure Modes and Recovery

1. **Map before curve.** Signal: zones are drawn and populated before any
   intensity arc exists; the level's spike is discovered in playtest.
   Correction: stop populating, draw the curve from the experience goal,
   then re-sequence beats against the existing zones — usually a
   rest beat moves and one encounter demotes. Prevention: step 2 precedes
   step 3 by rule.
2. **Teaching by text or popup.** Signal: the teaching plan contains a
   control hint, an objective banner, or an NPC info-dump; playtesters
   read instead of learn. Correction: redesign the introduction space so
   the safe path requires the mechanic and failure is cheap; keep the
   text only if the mechanic is genuinely invisible (rare). Prevention:
   rule 3 — budget text to zero and treat any need for it as a space
   defect.
3. **The illegible death.** Signal: playtesters die and cannot say what
   killed them; death heatmap clusters form at the same spot. Correction:
   fix readability first (sightline to the threat, affordance of the
   hazard), then encounter tuning, then numbers — in that order, per
   rule 12. Prevention: every encounter blueprint's fail states are
   legibility-checked at greybox.
4. **The stealth corridor nobody can read.** Signal: players fail the
   corridor repeatedly without adjusting behavior — they cannot see the
   patrol logic. Correction: make sightcones visible through floor
   lighting or patrol rhythm, shorten the reset, and move the checkpoint
   before the sightline, not inside it.
5. **The gauntlet that punishes.** Signal: the climax combines two
   untaught demands at once; completion collapses and retries feel
   random. Correction: decompose — the climax may require mastery of
   taught mechanics in combination, never a first. Insert a combination
   practice beat two beats earlier.
6. **Metrics read without targets.** Signal: telemetry arrives and every
   reading is debated from taste; "feels too hard" arguments replace
   data. Correction: re-register targets in the spec, then reread the
   existing data against them; departures get accepted or fixed with
   reasons, not vibes.
7. **Playtest notes as verdicts.** Signal: feedback reads "level is
   boring/confusing/hard" with no behaviors attached. Correction: rerun
   the protocol's observation pass — record where players stop, look,
   hesitate, and retry; convert each verdict question into a behavior
   question for the next round.
8. **ID churn.** Signal: zone names drift between spec versions
   (`z03_quarry` becomes `z03_mines`); telemetry dashboards split, and
   meeting notes refer to different beats. Correction: freeze the ID
   table, map old to new once, and key all future data on the frozen
   IDs. Prevention: rule 13 — IDs never change; display names do.

## 08 — Supporting Files Index

| File | Role | Read/Use when |
| --- | --- | --- |
| `references/level-design-principles.md` | Methodology: readability, affordance, flow, gating | Framing the level (workflow step 1; check at every layout decision) |
| `references/pacing-and-difficulty-curves.md` | Methodology: intensity arcs, rest beats, ramp design, difficulty measurement | Drawing the curve (workflow step 2; fixes entering at 2) |
| `references/spatial-composition.md` | Methodology: sightlines, landmarks, loops, chokepoints | Composing the map (workflow step 3) |
| `references/encounter-design-patterns.md` | Pattern catalog: arena, gauntlet, puzzle-lock, boss structures with costs and failure modes | Blueprinting encounters (workflow step 5) |
| `references/narrative-through-environment.md` | Methodology: environmental storytelling — props, state, foreshadowing, pacing | Planning teaching and world-through-space (workflow step 6) |
| `references/level-metrics-and-telemetry.md` | Metrics guide: completion, death heatmaps, time-to-finish, event design | Registering and reading telemetry (workflow step 10) |
| `references/playtesting-levels.md` | Methodology: level-specific test protocol, silent-teaching test, sample sizes, iteration discipline | Running playtests (workflow step 9; triage at 11) |
| `references/level-case-studies.md` | Case study: SMB 1-1, Ravenholm, Undead Burg annotated beat by beat | Closing the loop against annotated classics (workflow step 12) |
| `templates/level-spec-template.md` | Template: the full level spec from goal through playtest plan | Producing the spec artifact (workflow step 7) |
| `schemas/level-spec.schema.json` | Schema: machine-checkable level spec shape for tooling pipelines | Validating spec structure when tools consume it (workflow step 7) |
| `examples/worked-level-design.md` | Example: the full Cavern Run intro level with zones, timings, and encounter blueprints | Seeing the workflow applied end-to-end (companion to section 06) |

**Reading paths.** How to load this skill's files for common jobs:

- *Greenfield level:* read level-design-principles, then
  pacing-and-difficulty-curves; write with level-spec-template.
- *Encounter work:* read encounter-design-patterns; check the beat's
  context in spatial-composition before shaping the space.
- *Stealth or teaching fix:* read narrative-through-environment and the
  silent-teaching section of playtesting-levels.
- *Telemetry review:* read level-metrics-and-telemetry first; consult
  pacing-and-difficulty-curves if the fix moves beats.
- *First time here:* read section 06 above, then the worked example — the
  workflow makes more sense with its zones visible.