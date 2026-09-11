---
name: game-mechanics-design
description: >
  Use when designing, specifying, prototyping, balancing, or playtesting game
  mechanics — from the core loop down to a single buildable mechanic spec.
  Triggers include: designing a core loop or "one more run" structure, drafting
  a mechanic spec for engineers, choosing what a new mechanic should reward,
  prototyping a rule set cheaply, balancing progress curves or loadout
  options, or triaging playtest feedback into changes. Produces mechanic
  specs, GDD sections, prototype plans, balance passes, and playtest reports.
---

# game-mechanics-design

## 01 — Purpose

Game mechanics are the rules and systems that create player experience. A
well-designed mechanic is learnable, expressive, and aligned with the
experience you want the player to have. This skill gives you the tools to
design, specify, and iterate on mechanics with discipline — from the first
napkin sketch to the playtest-informed revision.

The skill covers the full arc: understanding what makes a mechanic work (core
loops, player motivation), specifying it precisely enough to build or prototype
(mechanic specs, documentation), and validating it through playtesting and
balancing. It does not cover level layout, narrative design, or art direction —
those are separate domains with their own skills.

**Three outcomes this skill owns:**
1. A mechanic that is specified clearly enough for a developer to implement or a designer to test.
2. A playtest plan that surfaces the mechanic's strengths and weaknesses before full production.
3. A balance rationale that explains why the numbers are what they are, so the next change is a decision rather than a guess.

Design here means decisions, not decoration. Every artifact this skill
produces is judged by one question: can the team make the next correct
decision from it without asking the author?

**Scope boundary.** This skill stops at the boundary named in section 02: it
produces the rule, the number, and the test, and hands the space, the
sentence, and the screen to their own disciplines. The boundary is a handoff
with artifacts, not a wall — level design receives the decision goals a space
must serve, narrative receives the experience intent, engineering receives
the spec — and every handoff names the open questions the receiving
discipline must answer before the mechanic ships.

**Operating stance.** Three habits run through everything this skill does:

- **Diagnose before designing.** Find the decision the loop is missing before
  generating candidates; a mechanic that answers a real diagnosis survives
  contact with players, and one that decorates an undiagnosed loop does not.
- **Cheapest signal first.** A paper grid that changes a decision beats a
  polished build that flatters a hope. Cost follows the question, never leads it.
- **Evidence over seniority.** Playtest behavior outranks opinion — including
  the designer's. Opinions generate hypotheses; sessions decide them.

**Vocabulary used throughout.** These terms are used with these meanings in
every file in this skill:

- *Mechanic* — one rule system the player interacts with, small enough for one
  spec file.
- *Core loop* — the repeating structure of verb, decision, resolution, and
  reward that defines play.
- *Decision point* — the moment in a loop where two or more options are live
  and the choice is not free.
- *Parameter* — a tunable number, named in a table with default, range, owner.
- *Lever* — a category of change used to rebalance (availability, conditional,
  frequency, magnitude, friction, rule).
- *Run* — one attempt through the game's fail-and-retry structure; a *session*
  is one sitting, possibly containing several runs.
- *Bank phase* — the end-of-session minutes where rewards tally, purchases
  happen, and the next loop is teased.

## 02 — When to Use / When Not to Use

**Use this skill when any of these are true:**

1. **Designing a core loop.** You are defining what the player does every 30
   seconds or every 30 minutes — the verb, the decision point, the resolution,
   the reward. Use when a game is new, when a loop is not landing, or when a
   publisher asks "what does the player actually do?"
2. **Specifying a mechanic for implementation.** You need a document an
   engineer can build from, with rules, parameters, edge cases, and a test
   plan. Use for anything entering a sprint.
3. **Choosing what a mechanic should reward.** You are deciding the
   motivational job — autonomy, competence, which player archetype, which fun
   category — before deciding the rules. Use when a design argues with itself
   about who it is for.
4. **Prototyping a rule set cheaply.** You have a question and need the
   fastest artifact that can answer it: spreadsheet, paper, greybox, slice.
   Use before any production engineering on an unproven mechanic.
5. **Balancing numbers or strategies.** You are tuning cost curves, checking
   for dominant strategies, or re-pricing a choice players avoid or overpick.
   Use whenever a parameter table exists or a strategy is dominant.
6. **Turning playtest data into changes.** You have session notes, telemetry,
   or community feedback threads and need triage into blocked, distorted, and
   polish buckets with retests attached.
7. **Writing or revising a design doc section.** You need the GDD skeleton
   filled with the loop, pillars, mechanics table, and risks — not a novel.
8. **Auditing a shipped mechanic.** Players overpick, avoid, or misunderstand
   something; you need a structured diagnosis and a lever-based fix.
9. **Tearing down a proven mechanic.** You admire another game's mechanic and
   need its anatomy extracted and re-derived for your genre — deliberately,
   not copied blind. Use the case-study method before borrowing.
10. **Choosing between candidate mechanics.** You have several plausible
    designs and need a decision pass that weighs goal fit, prototype cost, and
    blast radius — the workflow's step 4 exists for exactly this fork.

**Do not use this skill when:**

1. **Layout and space are the job.** Encounter arenas, level flow, pacing
   across physical space, and cover placement are level-and-encounter-design
   territory. Mechanics and levels meet at "what decisions does this space
   offer," but the space itself is not this skill.
2. **The story is the job.** Plot, dialogue, character, narrative structure,
   and lore delivery belong to story-and-narrative-design. A mechanic that
   expresses theme is in scope; the theme's content is not.
3. **Economy deep-modeling is the job.** Sink/source audits, inflation
   modeling, and market simulation at scale belong to game-economy-balancing.
   This skill handles first-pass levers and hands off the deep model.
4. **The software architecture is the job.** ECS structure, netcode, save
   systems, and frame budgets belong to software-architecture-design. Specs
   here state *what* the mechanic does; the code's shape is theirs.
5. **The marketing copy is the job.** Store pages, patch notes as
   communication, and community messaging belong to copywriting-and-messaging
   and social-media-strategy. Balance rationale feeds them; writing them does
   not belong here.
6. **The aesthetic judgment is the job.** Art direction, palette, readability
   of final renders, and UI visual polish belong to ui-design-critique and
   design-system-foundations. Greybox legibility questions are in scope here;
   the paint is not.
7. **Test automation is the job.** Test frameworks, coverage targets, and CI
   gates belong to testing-strategy. This skill writes the behavioral
   questions those tests eventually encode, not the harness.
8. **Monetization pricing is the job.** IAP structure, price ladders, and
   store economy design belong to game-economy-balancing. A mechanic that
   serves monetization is still specced here, but the price is theirs.
9. **Production scheduling is the job.** Estimation, sprint planning, and
   milestone negotiation belong to operations-and-process-design. This skill
   emits specs and playtest plans; sequencing them is theirs.

When in doubt: if the deliverable is a *rule*, a *number*, or a *test*, this
skill applies. If it is a *space*, a *sentence*, or a *screen*, hand off.

## 03 — Inputs and Outputs

**Inputs this skill consumes:**

- A brief or prompt: the game's premise, constraints, and the question to
  answer. A one-paragraph brief is enough to start; a GDD is enough to align.
- An existing design doc or its equivalent — pillars, audience, session
  length. If none exists, workflow steps 1-2 produce the minimum.
- Playtest notes, session recordings, telemetry exports, or community
  feedback threads when the work is iterative rather than greenfield.
- Existing parameter tables, economy sheets, or spec files for the systems a
  new mechanic will touch.
- Platform and scope constraints: session length targets, team size, engine,
  input methods, co-op or solo structure.

**Input readiness checklist.** Before starting the workflow, confirm:

- The brief states a question, not just a feature ("make mining feel fresh"
  is a wish; "players abandon sessions before the first bank" is a question).
- Audience and session length are named, or step 1 will invent them.
- The systems the mechanic will touch have named owners, so the interaction
  map has someone to negotiate with.
- Any playtest data being reacted to is dated and sourced; undated feedback
  is rumor and gets treated as such.

**Outputs this skill produces:**

- `mechanic-spec-template.md` — the per-mechanic specification: frontmatter,
  rules, parameters, interaction map, edge cases, experience intent, open
  questions, playtest plan. The primary artifact; one per mechanic.
- `game-design-doc-template.md` — the GDD section template: elevator pitch,
  experience goals, core loop, pillars, mechanics overview, risks.
- `schemas/mechanic-spec.schema.json` — the validation contract a finished
  spec must satisfy before review.
- Balance passes: parameter changes with stated ranges, owners, and the
  reasoning, ready to merge into the spec's parameter table.
- Playtest plans and triage reports: questions, protocols, signals, buckets,
  decisions, retests.
- Decision records: one page per significant choice — evidence, options,
  decision, retest owed.

**Acceptance criteria per output.** An output is done when:

- A *mechanic spec* validates against the schema, every rule is testable as
  written, every parameter has an owner, and a stranger could implement it.
- A *GDD section* answers the stranger test for its own scope and links every
  row of its mechanics table to a real spec.
- A *balance pass* names its lever, its one-axis comparison, and the
  dominant-strategy check it ran — a number with no reason is not shipped.
- A *playtest report* cites behavioral evidence with counts, states its triage
  buckets, and attaches a retest to every fix.
- A *decision record* would let a newcomer reconstruct the choice without
  interviewing anyone.

**Artifact conventions.** How outputs are named, stored, and linked:

- Spec files take the mechanic's name (`rune-upgrades.md`) and live beside
  the systems they govern; the GDD links, the spec defines.
- Every output carries its template's frontmatter — version, status, owner,
  date — because those fields are what other systems and readers key off.
- Decision records are appended to the artifact they decided; context travels with it.
- Parameter tables are the single source for tunable numbers: builds read
  the table, not the prose, and tuning passes edit the table with reasons.
- Retest schedules live in the spec's playtest section, visible to the next reader.
- Retired artifacts (paper prototypes, spreadsheets) are archived beside the
  memo that cites them; a broken citation gets restored or re-cited.

Everything the skill produces is a markdown file or a table that lives beside
the code it governs. Nothing here requires a special toolchain.

## 04 — Workflow

The steps below are the full arc. Short jobs (a balance tweak, a spec touch-up)
enter at the step that matches the change and exit at step 12. Greenfield
mechanics run the whole list. Each step names its reference file; load the
reference before doing the step's work.

1. **Restate the brief as a measurable goal.** Convert the request into an
   observable target the mechanic must move ("players re-enter within 20 s of
   a death"; "players pick the risky vein 40%+ of the time"). If the goal
   cannot be observed, it cannot be tested, and the mechanic will be argued
   about forever. Read `references/player-motivation-models.md` to pick the
   motivational target — which need the mechanic feeds, which archetype it
   serves, and what it taxes.
2. **Analyze the loops the mechanic will live in.** Write the 30-second loop
   and the 30-minute loop as four parts each (verb, decision, resolution,
   reward), and find the decision point the new mechanic attaches to. Read
   `references/core-loop-design.md` first; a mechanic with no loop to live in
   is a gimmick. Diagnose the loop before designing anything: the fix the
   loop needs dictates the mechanic family.
3. **Generate candidates across families.** Produce three or more one-line
   candidates, at least one from a family you did not first think of. For each
   candidate write the decision it creates and the state it adds. Read
   `references/mechanics-taxonomy.md` and walk its catalog as a matrix; kill
   any candidate whose decision sentence is "the player gets stronger."
4. **Choose the candidate and state the bet.** Pick by fit to the goal from
   step 1, cost to prototype, and blast radius on existing systems. Write one
   paragraph: what you expect to happen, what would prove it wrong. This is
   the bet the playtest will cash.
5. **Write the mechanic spec.** Fill `templates/mechanic-spec-template.md`:
   rules as numbered testable statements, parameters with defaults and ranges,
   interaction map in both directions, edge cases with stated behaviors,
   experience intent, open questions with owners. Read
   `references/mechanics-documentation.md` for the bar each section must
   clear; validate the result against `schemas/mechanic-spec.schema.json`.
6. **Prototype the riskiest assumption.** Find the fastest artifact that can
   produce a signal: spreadsheet, paper, greybox, slice. Write the question
   and the kill criteria before building; timebox; instrument restarts and
   events before inviting players. Read `references/prototyping-playbook.md`.
   A prototype result that changes no decision was the wrong prototype.
7. **Run the first balance pass.** Price the mechanic against its neighbors
   on one axis (marginal value per resource), check for dominant strategies,
   and choose levers in preference order (availability → conditional →
   frequency → magnitude → friction → rule). Read
   `references/balancing-fundamentals.md`. Record every parameter change in
   the spec's parameter table with its reasoning — numbers without reasons
   rot within one patch cycle.
8. **Plan and run the playtest.** Write the behavioral question, choose the
   protocol (think-aloud, quiet observation, A/B, unmoderated, paper),
   recruit the right segment, and run the session without rescuing players.
   Read `references/playtesting-methods.md`. Five players of the right
   segment beats fifteen of the wrong one.
9. **Triage the evidence.** Sort signals into blocked (cannot proceed),
   distorted (proceeds while avoiding the mechanic), and polish (works but
   drags). Translate complaints into needs before translating them into
   tasks. Fix in bucket order; attach a retest to every fix.
10. **Decide and record.** Revise the spec, bump its version, and write the
    decision record: evidence, options considered, decision, retest owed.
    Compare the result against the step-4 bet and say which won. Read
    `references/mechanics-case-studies.md` if the result suggests the
    mechanic's pattern needs re-derivation rather than tuning.
11. **Update the design doc.** Add or revise the mechanics-table row, the
    core-loop sentence if the loop changed, and the risks section. Use
    `templates/game-design-doc-template.md`. Superseded content moves to a
    dated appendix; it does not vanish.
12. **Close the loop with a retest.** Every fix from step 9 names the next
    session that will verify it. A fix without a scheduled retest is a
    hypothesis wearing a green checkmark.

Steps 1-4 are thinking work with one-page outputs. Steps 5-7 are writing work
with artifact outputs. Steps 8-12 are evidence work with decision outputs.
Most failed mechanic projects skipped 1-2 and paid for it in 8-10.

**Emitted artifacts by step:**

| Step | Emits |
| --- | --- |
| 1 | Goal statement with observable targets and the motivational alignment note |
| 2 | Loop diagnosis: 30-second and 30-minute loops, four parts each |
| 3 | Candidate list, one line each, with decision sentences |
| 4 | The bet: chosen candidate, expectation, falsifier |
| 5 | Mechanic spec (validated against the schema) |
| 6 | Prototype memo: question, artifact, result, decision |
| 7 | Balance pass: lever choices and parameter-table changes with reasons |
| 8 | Playtest plan and session logs |
| 9 | Triage report: signals, buckets, fixes, retests |
| 10 | Revised spec (version bumped) and decision record |
| 11 | Updated GDD rows and risks section |
| 12 | Retest schedule attached to the spec |

**Common entry points.** Not every job starts at step 1:

- *Greenfield mechanic:* start at 1, run all twelve.
- *Balance patch:* start at 7 with the spec's parameter table; loop 7 → 8 →
  12 if the change is behavioral rather than numeric.
- *Playtest triage:* start at 9 with the session evidence; return to 7 only
  if the fix is a pricing problem.
- *GDD authoring:* start at 11 with the spec set finished; if specs are
  missing, drop to 5 for each mechanic the doc must link.

**Working rhythm.** The full arc is designed to be run in four working
sessions, and the artifacts mark the seams:

- Session one: steps 1-4, ending in the bet. Outputs are one page each, and
  the candidate choice happens with all options on the table.
- Session two: steps 5-7, ending in a testable build or artifact; the spec
  review and the prototype memo share one meeting when the prototype is paper.
- Session three: steps 8-9, the playtest and its triage. Book the retest
  before leaving the room.
- Session four: steps 10-12, the decision record and doc updates; if the
  evidence contradicts the bet, session three repeats before session four runs.

The rhythm assumes a small team; a solo designer compresses sessions one and
two into an afternoon. What does not compress is the ordering: a bet written
before evidence, evidence gathered before decisions, decisions recorded
before doc updates. Reversing any of those orders is how mechanic work
becomes opinion work.

## 05 — Rules and Quality Bar

1. **Diagnose the loop before designing the mechanic.** No mechanic leaves
   this skill without a named loop, a named decision point, and a one-sentence
   reason it improves that decision. Mechanics bolted onto undiagnosed loops
   add content, not depth.
2. **Every rule in a spec is testable as written.** No "some," "often,"
   "reasonable," or "feels." QA turns each rule into a test case without
   interpretation; if they cannot, the rule is not done. Vague quantifiers in
   a spec are defects, not style.
3. **Every parameter has a default, a range, and an owner.** Numbers without
   ranges are untested; tables without owners are unmaintained. Tunable
   numbers appear in the parameter table and nowhere else — no magic
   constants in prose or code.
4. **Name the decision a mechanic creates.** If the honest answer is "the
   player gets a bigger number," it is a reward, not a mechanic — treat it as
   a parameter change and price it accordingly.
5. **Prototype at the cheapest rung that can answer the question.** Paper
   before greybox, greybox before slice. Write the question and the kill
   criteria before building; a prototype that cannot fail is not an
   experiment.
6. **Balance by repricing choices before weakening toys.** When one option
   dominates, first try availability and conditional levers on its rivals.
   Players forgive buffs; they remember nerfs.
7. **No dominant strategy ships unacknowledged.** Every balance pass names
   the current best strategy, why it is acceptable or not, and what would
   dethrone it. Degenerate combos are either fixed or accepted in writing
   with a monitoring plan.
8. **Playtests answer written questions.** No session without a behavioral
   question and a success criterion decided in advance. Never rescue players
   mid-test; a test that dies found something.
9. **Feedback is translated before it becomes tasks.** Difficulty complaints
   are checked against legibility first; suggestions are mined for the need
   underneath; feature requests are weighed by the source's expertise. A
   complaint without a named need is not yet a task.
10. **Failure must bank something.** Any mechanic governing repeated
    attempts (runs, raids, seasons) must convert a loss into money, insight,
    knowledge, or position. A loop that only punishes is a slot machine with
    bad odds.
11. **Teaching is content.** Every new rule budgets for its introduction and
    its first safe test. Under-taught mechanics are indistinguishable from
    broken ones in playtests — and get "fixed" the wrong way.
12. **Decisions get records.** Significant choices produce a one-page record:
    evidence, options, decision, retest owed. Unrecorded decisions get
    relitigated; recorded ones get improved.
13. **Specs stay one page.** If a spec cannot fit a page, it is usually two
    mechanics — split into a parent and children before writing more.
    Documentation beyond a page belongs in the GDD, not the spec.
14. **Interactions are mapped in both directions.** Every spec lists what it
    reads, what it writes, what triggers it, what interrupts it — with
    "none" written explicitly where a list is empty. Empty is a claim and a
    testable one.
15. **Version and status are load-bearing.** Every content change bumps the
    version and touches the date; status changes are loud. Docs whose version
    drifted from their text are distrusted on sight, and rightly so.
16. **Hand off at the boundary, with the artifact.** When work crosses into
    level, story, economy, or architecture territory, this skill's job ends
    at a written handoff — the spec, the numbers, the open questions — not
    with a hallway agreement.

## 06 — Worked Example

Scenario: **Deep Delve**, a mining roguelite, needs a "one more run" upgrade
mechanic. Playtesters finish sessions and stop; the surface shop's linear
purchases give no build identity; delves are 15-25 minutes, solo or duo. The
full run below is expanded artifact-by-artifact in
`examples/worked-mechanic-design.md`; this section shows the intermediate
artifacts and the reasoning between them.

**Step 1-2 artifacts (goal and loop diagnosis).** The brief is restated as a
measurable goal: 60% of sessions end with immediate re-entry, players can
describe their build in one sentence, and no re-entry stalls longer than 20
seconds. The motivational target is set from the motivation models: feed
competence (builds reward skill) and autonomy (player-chosen shapes), and —
critically — displace the existing beeline incentive, because the ore shop
already rewards straight-to-the-vein play and a new mechanic that also rewards
beelining doubles the problem.

The loop diagnosis (from the core-loop reference): the 30-second loop
(scan, choose shaft or vein, dig, resolve) is fine; the 30-minute loop's bank
phase is flat — purchases are linear stat bumps, so the post-escape minutes
have no build story and no peak. The missing "one more run" energy lives in
the bank phase. Diagnosis: a progression-family mechanic, not a new verb.

**Step 3-4 artifacts (candidates and the bet).** Three candidates plus one
family flip, each with its decision sentence:

1. *Rune Upgrades* — ore glyphs socketed mid-run into a 3-slot harness, each
   granting a build-defining mod; family set bonuses reward commitment.
   Decision: which shape of miner am I this run?
2. Talent tree at the surface shop. Decision: what to buy next. Rejected —
   doubles the existing shop; slow; no in-run identity.
3. Prestige depth multiplier. Decision: whether to chase depth. Rejected —
   no per-run decisions; feels like a tax.
4. Duo rune-sharing (social flip). Kept as a slice of candidate 1, not a
   standalone.

The bet, written down: "Rune Upgrades will make players commit to a build by
mid-delve and convert death into next-run ambition; if fewer than 2 of 5
playtesters re-enter within 20 s of death, the conversion value or the
post-death loop is wrong."

**Step 5 artifact (the spec, abridged).** Written with the mechanic-spec
template and validated against the schema:

- Rules (abridged to four of eight): runes drop only from clusters 8 m or
  deeper; socketing takes 2 s and can be interrupted by damage; same-family
  runes grant set bonuses at 2 and 3 of a family; on death, socketed runes
  convert to insight at 40% of value, and insight buys next-run rune quality
  — nothing else.
- Parameters: `socket_time 2.0s (1.0-3.0)`, `death_insight_rate 0.40
  (0.25-0.60)`, `drop_min_depth 8 (5-14)`, `set_bonus_value 25% (15-40%)`,
  each with an owner.
- Interaction map: reads hazard-band depth gating and duo range checks;
  writes shop credit and run loadout. Edge cases cover harness-full
  overwrites, simultaneous cache grabs, death mid-socket, and escape with
  zero runes.
- Experience intent: by mid-delve the player can say "I'm going pyro this
  run"; death stings but funds the next attempt's ambition, so re-entry is a
  plan, not a reset.

**Step 6-7 artifacts (prototype and balance).** Paper first (half a day: a
tile grid, rune cards, two colleague sessions) surfaced that three slots and
three families made players lock a family by the second socket and treat
slot three as filler — so set bonuses were placed at 2 *and* 3, making slot
three a real choice. Greybox followed (three days, debug mods, telemetry on
socket/escape/death) with kill criteria written before outside players saw
it. The balance pass chose the availability lever for the beeline problem
(depth-gated drops reshape strategy space without taxing the existing verb),
re-expressed the shop's flat damage line as rune-credit pricing so both
compete on one axis, and answered the all-pyro dominance found on paper by
buffing logistic cache yield at 3-family rather than nerfing pyro.

**Step 8-10 artifacts (playtest, triage, decision).** Five players, quiet
observation, telemetry on, question: "Will players re-enter a delve within
20 s of a death at least once per session?" Result: 4 of 5 re-entered —
target met. Triage:

| Signal | Bucket | Fix |
| --- | --- | --- |
| Two players destroyed a rune by accidental overwrite, then quit | Blocked | Confirm-to-destroy with mod comparison |
| One player socketed nothing, saving slots for something better | Distorted | Slot one's set bonus counts only when non-empty |
| Death felt bad with no behavioral drop | Polish | Death-conversion sting plus a next-run preview card |

The decision record appended to the spec reads, in full: "v0.3 — re-entry
target met (4/5 within 20 s). Shipped: confirm-to-destroy, empty-slot
incentive, death sting. Evidence: five-session greybox round, telemetry
socket/escape/death, debrief quotes. Options considered: harness expansion
(rejected — no evidence slots were the problem), rarity rework (deferred).
Owed retests: destroy-confirm usability, empty-slot socket timing, death
sting sentiment at next round." The GDD mechanics table gained a row linking
to `rune-upgrades`.

**What the example demonstrates.** The diagnosis preceded the mechanic (flat
bank phase → progression family). Motivation analysis produced a working
constraint (reward depth commitment, not veins) that shaped the drop rules.
Paper prototyping saved slot three for half a day's cost. Kill criteria were
written before contact with results and survived. The fix that shipped was
priced in levers, not lectures. Each artifact exists because a later decision
needed it — nothing was written for the binder.

**Adapting the example to another game.** The transferable skeleton, with
the Deep Delve specifics stripped:

- A flat *bank phase* in the session arc is the usual root cause of missing
  "one more run" energy — diagnose the 30-minute loop before inventing
  upgrades.
- A motivation audit yields a *constraint* (here: reward depth commitment,
  not veins) that the rules must honor; write it next to the goal first.
- Mid-run upgrade mechanics need: a socket/choice structure, family or set
  bonuses that make early picks live late, and a death conversion that
  keeps failure honest. The numbers are yours; the structure is the pattern.
- Replace the surface nouns, keep the shape: a fishing game's "lures," a
  space hauler's "rig modules," a heist game's "crew contracts" — each is
  the same anatomy with a new fantasy. What must be re-derived per game is
  the *conversion economy* (what death pays) and the *commitment pricing*
  (what family lock-in costs).

## 07 — Failure Modes and Recovery

1. **The mechanic with no loop.** Signal: the spec is finished but nobody can
   say which decision it improves; playtesters call it "fine" and never touch
   it. Correction: return to workflow step 2, name the decision point, and
   either attach the mechanic to it or cut the mechanic. Adding content to an
   undiagnosed loop makes the loop worse, not richer.
2. **The spec nobody can build from.** Signal: engineers ask what a rule
   means; QA writes three different test cases for one rule; "reasonable"
   appears in the rules section. Correction: rewrite rules as numbered,
   falsifiable statements; move feelings into the experience-intent section;
   validate against the schema before the next review.
3. **The dominant strategy discovered late.** Signal: one loadout, build, or
   route wins everywhere; community guides converge; variety metrics collapse.
   Correction: run the dominant-strategy check from the balancing reference;
   prefer repricing rivals (availability, conditional levers) over nerfing the
   dominant option; recheck after each patch, because dominance migrates.
4. **The playtest that proves nothing.** Signal: findings are opinions, the
   team argues instead of deciding, or the only note is "needs polish."
   Correction: the test lacked a written behavioral question and success
   criterion — re-run with the question, the protocol, and the no-rescue rule
   from the playtesting reference. Never rescue players mid-session.
5. **Reward displacement.** Signal: players do the rewarded chore and quit,
   skip unrewarded content they used to enjoy, or call the fun part "grind."
   Correction: check the motivation reference's overjustification section;
   convert the reward from participation price to recognition of play, or
   shrink it until intrinsic fun carries the activity again.
6. **The prototype that grew.** Signal: the greybox has a title screen, the
   paper test has custom-printed cards, the timebox expired twice. Correction:
   stop; restate the one question; ship the ugliest artifact that can answer
   it. Prototyping cost past the question's value is design debt.
7. **Balance by patch regret.** Signal: numbers change every build with no
   recorded reason; players learn nothing is stable; tuning debates restart
   weekly. Correction: parameters return to the spec table with ranges,
   owners, and one-line rationales; changes ship with change records; a
   rollback flag ships with the riskiest value.
8. **The untested fix.** Signal: a triage item is marked done but the next
   session's notes complain about the original behavior. Correction: every
   fix names its retest and its session; workflow step 12 is not optional. A
   fix without a scheduled retest is a hypothesis wearing a green checkmark.
10. **The ownerless spec.** Signal: the owner field says a team name, the
    parameter table's owners say three different people, and nobody answers
    for the last tuning change. Correction: one accountable owner per spec,
    re-assigned before the next merge; ownerless parameters are frozen
    until claimed.

## 08 — Supporting Files Index

| File | Role | Read/Use when |
| --- | --- | --- |
| `references/core-loop-design.md` | Methodology: loop anatomy, 30-second and 30-minute loops, escalation patterns, loop diagnosis | Designing or diagnosing what the player repeatedly does |
| `references/mechanics-taxonomy.md` | Pattern catalog: action, system, progression, and social mechanic families with generation matrix | Naming, generating, or coverage-checking mechanic candidates |
| `references/player-motivation-models.md` | Reference: intrinsic/extrinsic motivation, SDT needs, Bartle archetypes, fun categories | Choosing what a mechanic should reward and predicting who it serves |
| `references/prototyping-playbook.md` | Methodology: fastest-testable-thing ladder, paper and greybox practice, kill criteria | Answering a design question as cheaply as possible |
| `references/mechanics-documentation.md` | Template guide: the bar a spec must clear, section guidance, hygiene checklist | Writing or reviewing a mechanic spec others can build from |
| `references/balancing-fundamentals.md` | Methodology: lever inventory, cost curves, marginal value, dominant-strategy checks | Pricing a mechanic, tuning numbers, or responding to dominance |
| `references/playtesting-methods.md` | Methodology: recruitment, protocols, observation signals, feedback triage | Planning sessions, observing players, converting feedback into decisions |
| `references/mechanics-case-studies.md` | Case study: four well-known mechanics dissected with transferable rules | Borrowing a proven pattern deliberately rather than copying blindly |
| `templates/mechanic-spec-template.md` | Template: one-page mechanic spec with YAML frontmatter and fill-in checklist | Starting a new mechanic spec (workflow step 5) |
| `templates/game-design-doc-template.md` | Template: GDD section guidance plus skeleton with maintenance rules | Writing or revising the design doc (workflow step 11) |
| `schemas/mechanic-spec.schema.json` | Schema: validation contract for mechanic specs before review | Gating a spec at the end of workflow step 5 |
| `examples/worked-mechanic-design.md` | Example: the full Deep Delve run — brief to signed-off spec with all intermediate artifacts | Seeing the workflow applied end-to-end (companion to section 06) |

**Reading paths.** How to load this skill's files for common jobs:

- *Greenfield mechanic:* read core-loop-design and mechanics-taxonomy first,
  then player-motivation-models; write with mechanic-spec-template.
- *Balance patch:* read balancing-fundamentals; consult
  playtesting-methods if the change is behavioral.
- *Spec review:* read mechanics-documentation and validate against the
  schema; skim mechanics-case-studies if the pattern itself is in question.
- *First time here:* read section 06 above, then the worked example — the
  workflow makes more sense with its artifacts visible.