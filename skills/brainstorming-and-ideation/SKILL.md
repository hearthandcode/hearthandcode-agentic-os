---
name: brainstorming-and-ideation
description: >
  Load this skill when you need structured ideation: building a genuine pool
  of options and narrowing it to a defensible shortlist — for a product
  concept, a name, a show format, a strategy move, or any problem where the
  obvious first answer is not good enough. It covers framing the prompt,
  choosing divergence techniques, judgment-free capture, clustering,
  dot-voting, rubric scoring, and the decision record. It does not execute
  the winning idea (hand off to the relevant domain skill) and does not
  deep-evaluate one already-chosen option (score it directly with
  `references/idea-evaluation-rubrics.md` instead).
---

# brainstorming-and-ideation

## 01 — Purpose

An ideation session fails in one of two predictable directions. It converges
before it diverges — the first workable idea wins because it arrived first, and
the team never learns what the second-best looked like. Or it diverges forever —
the wall fills with sticky notes, everyone feels productive, and no decision
gets made. Both failures share one root cause: generation and judgment are
different mental modes, and running them together damages both.

This skill turns an open-ended problem into a timed, quota-driven session that
produces a real pool of options, then narrows that pool through named
convergence gates until three to five candidates remain — each carrying its
survival reasoning, its biggest risk, and a next step. It replaces "let's
brainstorm" with a procedure whose output can be audited.

**Three outcomes this skill owns:**

1. **A pool of 30+ raw ideas** produced by at least two different divergence
   techniques, with volume enforced by quota rather than left to mood — because
   the last third of any quota is where the novel work lives.
2. **A shortlist of 3-5 candidates** that survived clustering, dot-voting, a
   priority matrix, and weighted rubric scoring, with every rejected idea
   archived alongside a one-line reason and a resurface condition.
3. **A decision record** an absent stakeholder can reconstruct: what was
   selected, what is on hold and under what condition, what was archived, and
   what happens next, with owners and dates.

The skill is operational, not inspirational: it names the techniques, the
timeboxes, the vote budgets, the score weights, and the failure signals. A solo
practitioner and a facilitator work from the same 14-step procedure; only the
timings scale. The domain is any problem where new options are needed — product
concepts, names, formats, business directions, research angles. This skill does
not execute the winner; the decision record is the exit point, and the selected
idea moves from there to whichever domain skill owns execution.

## 02 — When to Use / When Not to Use

### Use this skill when:

1. **You need options and have none, or only one obvious candidate.**
   - Breadth before depth is the whole game; the framing and quota steps exist
     to defeat the blank page and the first-idea trap. Example: "I need a name
     for the newsletter and the only one I have is generic and taken."
2. **You have plenty of ideas and no disciplined way to narrow them.**
   - A pool of 20-50 undifferentiated items is a convergence problem; the
     clustering, dot-vote, matrix, and rubric gates exist for exactly this.
     Example: fifty feature requests, three prototype slots.
3. **You are running a solo session and want output instead of wandering.**
   - Timeboxes, quotas, and forced lens-switches beat an unstructured hour, and
     the solo break protocol keeps you honest when scoring your own ideas.
4. **A team keeps circling the same two ideas, and the loudest voice wins.**
   - Silent brainwriting strips authorship from generation; blind dot-voting
     strips it from ranking. Both are in `references/divergence-techniques.md`
     and `references/convergence-techniques.md`.
5. **A real decision is coming and you have no evidence to compare options.**
   - The rubric and its anti-pattern flags surface feasibility risk and
     champion bias before the decision, not after it.
6. **You are facilitating and the session has to survive a hard room.**
   - Energy management, trap scripts, and remote adaptations live in
     `references/facilitation-guide.md`; `references/ideation-case-studies.md`
     shows two realistic sessions, including one that nearly derailed.

### Do NOT use this skill when:

1. **The problem is narrative craft — story, character, dialogue.**
   - Use `story-and-narrative-design`. Selecting among concepts is this skill's
     job; inventing a coherent narrative world is a craft discipline with its
     own methodology.
2. **The idea is already chosen and needs execution.**
   - Use the downstream domain skill: `marketing-strategy`,
     `copywriting-and-messaging`, `content-calendar-planning`,
     `ui-design-critique`, or `software-architecture-design` — or no skill at
     all for straightforward action.
3. **You have a single option and need a quick verdict on it.**
   - Score it directly with `references/idea-evaluation-rubrics.md` in about
     ten minutes; running the full divergence machinery to evaluate one idea is
     process theater.
4. **The problem is operational optimization — scheduling, routing, triage.**
   - Use `operations-and-process-design`; these problems usually have a
     computable answer that ideation technique would obscure.
5. **The question is technical architecture or test strategy.**
   - Use `software-architecture-design` or `testing-strategy`; engineering
     trade-offs are analysis problems with stated constraints, not pools to
     broaden.

## 03 — Inputs and Outputs

### Inputs

You need at least the first two before starting; the rest raise fidelity:

- **A problem statement with a real constraint in it.** Context, audience, and
  the one limit that actually binds. "We need ideas" is not an input; "weekly
  content ideas a solo producer can ship" is.
- **Session type and headcount.** Solo, or a team of 3-8 in person / 2-6
  remote-synchronous. Technique selection and vote budgets depend on it.
- **A time budget.** 45 minutes minimum solo, 90 minimum for a team session —
  shorter and convergence gets cut, which is the worst place to cut.
- **Non-negotiable boundaries.** Budget, legal, brand, platform limits. These
  are framing inputs, not ideation challenges.
- **A baseline concept (optional but common).** Required for SCAMPER; if none
  exists, the warm-up or the constraint top-up will produce one.

### What good inputs look like

- The constraint is stated as a limit, not a solution: "no paid media budget"
  beats "we should do partnerships." The audience is a specific someone, not
  "everyone." Someone can say what would make the session a failure — that
  sentence becomes a success criterion in Step 2.

### Outputs

The session produces eight artifacts, packaged in
`templates/ideation-session-template.md`:

1. **A framing prompt** — a "How might we…" question that passes the
   three-prompt test in `references/facilitation-guide.md`.
2. **The raw idea pool** — 30+ ideas, each with an ID, the technique that
   produced it, and a one-line description.
3. **A cluster map** — named themes covering the whole pool, misc cluster under
   20%.
4. **A dot-vote ranking** — weighted votes per idea; top 8-10 advance.
5. **A priority-matrix placement** — feasibility against impact, four sectors,
   with research-quadrant residents named.
6. **Weighted rubric scores** for the finalists — Novelty, Feasibility, Fit,
   optional Impact, per `references/idea-evaluation-rubrics.md`.
7. **A shortlist of 3-5** — ranked, each with a one-line rationale and its
   biggest risk.
8. **A decision record** — selected / hold / archive per idea, with next steps
   and owners, formatted per `references/ideation-capture-and-triage.md`.

### What good outputs look like

- An absent stakeholder can reconstruct the decision path from the record
  alone. The archived pool survives intact — rejected ideas keep their reasons,
  so a constraint change next quarter can resurface them cheaply.
- The shortlist differs in kind, not degree: three variations of one idea means
  divergence underproduced, and that is a session defect worth recording.

## 04 — Workflow

Fourteen steps. Steps 1-4 are preparation; 5-9 are divergence; 10-14 are
convergence. Times are the 45-minute solo baseline with team timings noted — a
team session runs 90-120 minutes. Open a reference when a step names it; do not
read them all up front.

### Step 1 — Frame the prompt
**Reference:** `references/facilitation-guide.md`

- Tighten the raw problem into one "How might we…" question, then apply the
  three-prompt test: a 12-year-old understands it; it does not prescribe a
  solution; it is broad enough for 30 genuinely different directions.
- Fold in one or two real constraints — more than three active constraints
  collapses the space (`references/constraint-based-creativity.md`).
- Write the prompt where every participant can see it for the entire session.
- Checkpoint: "Could someone generate 30 ideas from this sentence without
  asking me a single clarification question?"

### Step 2 — Set the quota and success criteria
**Reference:** `references/ideation-principles.md`

- Fix the numbers before generating: pool minimum (30), shortlist size (3-5),
  and what a failed session would look like. Record them at the top of
  `templates/ideation-session-template.md`.
- The quota binds per round, not retroactively at the end — a round that
  underproduces is a signal, not a debt to settle later.
- Checkpoint: "Is the pool target reachable with the techniques I plan to
  run?"

### Step 3 — Choose two to four divergence techniques
**Reference:** `references/divergence-techniques.md`

Match techniques to the session's situation:

| Situation | Technique |
|---|---|
| A baseline concept exists | SCAMPER |
| Stuck circling one domain | Forced analogy |
| Judgment anxiety, cold room | Worst idea first |
| Loud-voice dominance | Brainwriting (635) |
| The pool is stale and safe | Constraint flips |
| No starting point at all | Random entry, analogous worlds |

- Pair at least one generative technique with one lens-breaking technique
  (worst-first or constraint flips). Never exceed four techniques; switching
  cost exceeds marginal novelty after that.
- Checkpoint: "If technique one stalls, what is technique two — and is it
  actually a different lens, or the same lens with a new name?"

### Step 4 — Prepare the capture space
**Reference:** `references/ideation-capture-and-triage.md`

- One idea per unit: one sticky, one row, one card — movable without rewriting.
  The ten-second rule: if recording an idea takes longer, fix the setup before
  the session, not during it.
- Physical: sticky notes, markers, visible timer, bare wall. Digital: shared
  document with a row per idea, a voice timer, a dedicated parking-lot section.
- Remote: six participants maximum, shared document mandatory, two-minute
  buffers on every transition.
- Checkpoint: "Can I capture an idea without stopping the person mid-sentence
  — and can everyone see the timer?"

### Step 5 — Warm-up
**Reference:** `references/facilitation-guide.md`

- Three minutes, one prompt, no evaluation: "List ten everyday frictions you
  noticed this week in this domain." The output is never used in the session;
  the warm-up exists to start the generative engine and to prove capture works.
- Solo: write, then physically set the list aside unread.
- Checkpoint: "At least one item per minute? If not, the prompt is too big —
  shrink it and run once more."

### Step 6 — Divergence round 1
**Reference:** `references/divergence-techniques.md`

- Timer on, capture only. In team sessions the facilitator records and does not
  generate (Rule 11).
- Run the technique's own procedure exactly: SCAMPER means five ideas per move;
  brainwriting means passing sheets at five minutes. The procedures carry the
  quota.
- No "but", no "we tried that", no "the client will hate it" — objections go to
  the parking lot in five seconds and generation continues.
- At the timer, stop. Read the round back once, without comment.
- Checkpoint: "Twelve or more ideas this round? If not, note it — do not
  extend the round; that rewards slowness."

### Step 7 — Divergence round 2
**Reference:** `references/divergence-techniques.md`

- Switch techniques immediately; no break, previous ideas stay visible. Round
  two must be a different lens, not more of round one: after SCAMPER,
  worst-first or constraint flips — not more modification moves.
- Solo adaptation: same two rounds, but change seat or surface between them and
  treat round one as written by a stranger.
- Checkpoint: "Are round-two ideas visibly different in kind? Same themes
  means the techniques were too similar — swap one and add a short round
  three."

### Step 8 — Constraint top-up (contingent)
**Reference:** `references/constraint-based-creativity.md`

- Run only if the pool is under quota after round two; otherwise the time goes
  to the break. List the session's live constraints, invert or exaggerate one
  or two, and generate against the new frame for three minutes.
- Tag every idea born here as constraint-born — Rule 10 needs one of these to
  survive into the shortlist as the wildcard.
- Checkpoint: "Pool at 30 now? If still short, the prompt was narrower than it
  looked — say so in the decision record."

### Step 9 — The mandatory break
**Reference:** `references/ideation-principles.md`

- Three minutes solo, fifteen for a team session. Physically leave the
  workspace; do not look at the pool. The break is the boundary between the
  modes: without it, judgment leaks into generation and generation leaks into
  scoring, corrupting both.
- Checkpoint: "Can I look at this pool as if a stranger wrote it?"

### Step 10 — Cluster the pool
**Reference:** `references/convergence-techniques.md`

- Classify, do not evaluate: ten seconds per idea, move it, next. Name every
  cluster by the theme that holds it; merge clusters that share a theme.
- Misc over 20% of the pool means the clustering failed — split it and re-run;
  do not proceed with a junk drawer.
- One dominant cluster is information: the problem is well-trodden there and
  starved elsewhere — note it for the decision record.
- Checkpoint: "Every idea in a named cluster, misc under 20%?"

### Step 11 — Dot-vote to coarsen
**Reference:** `references/convergence-techniques.md`

- Weighted budget per person: one strong dot (3 points), two medium (2), three
  weak (1). Solo: one ten-point budget spent the same way. Votes land on
  ideas, not clusters; hide authorship where possible.
- Top 8-10 advance; record full tallies in the template.
- Checkpoint: "Is one idea far ahead of the field? Flag it for the champion
  check in Step 13 rather than crowning it here."

### Step 12 — Place survivors on the priority matrix
**Reference:** `references/convergence-techniques.md`

- Two axes: feasibility and impact. Thirty seconds per idea, no debate.
- High/high advances to scoring. High impact with low feasibility becomes a
  research candidate, not a reject. Low/low archives with a one-line reason.
  The matrix is a sorting gate, not a verdict — record placements and reasons.
- Checkpoint: "Did anything land in research? An empty research quadrant means
  the pool was safe, and Rule 10's wildcard is at risk."

### Step 13 — Score the finalists
**Reference:** `references/idea-evaluation-rubrics.md`

- Score each surviving idea 1-5 on Novelty, Feasibility, and Fit; add Impact
  when a measurable change is known in advance. Default weights: Novelty 30%,
  Feasibility 35%, Fit 25%, Impact 15% — adjust per the brief, but never to
  equal weights.
- Apply the anti-pattern flags: champion problem, rebranded standard, scope
  creep, unfalsifiable idea. Flags override scores.
- Enforce the feasibility floor: below 3, the idea becomes a research question;
  at 2 with no derisking path, archive it.
- Checkpoint: "Could I defend every score to the person whose idea just lost
  to a lower scorer?"

### Step 14 — Build the shortlist and decision record
**Reference:** `references/ideation-capture-and-triage.md`

- Rank the scored survivors; the shortlist takes 3-5 and must include one
  constraint-born wildcard (Rule 10).
- Fill the decision record in `templates/ideation-session-template.md`:
  selected, held (with the condition that would activate it), archived (with
  the one-line reason and resurface condition). Every next step gets an owner
  and a date, even in a solo session — "me, by Friday" counts.
- Checkpoint: "Could someone who missed the session reconstruct what was
  decided, and why, from this record alone?"

## 05 — Rules and Quality Bar

Run any session against these before declaring it done. A violated rule with no
recorded reason is a defect in the session itself.

1. **Set the quota before you start and enforce it per round.**
   - Craft: `references/ideation-principles.md`.
   - Why: the first twenty ideas are the ones everyone would produce anyway;
     the quota is what pushes past them.
2. **Keep divergence and convergence physically separated.**
   - Craft: `references/ideation-principles.md`.
   - Why: judgment suppresses generation, and generation during scoring
     corrupts the scores.
3. **No critique during divergence — every objection goes to the parking lot.**
   - Craft: `references/ideation-capture-and-triage.md`.
   - Why: one early "that won't work" taxes every idea that comes after it.
4. **Capture every idea as a discrete movable unit in ten seconds.**
   - Craft: `references/ideation-capture-and-triage.md`.
   - Why: capture friction is a silent quota killer.
5. **Two to four techniques, timeboxed — never one lens for the whole pool.**
   - Craft: `references/divergence-techniques.md`.
   - Why: each technique forces a different cognitive pathway; one lens
     produces one shape of idea.
6. **The misc cluster stays under 20% of the pool.**
   - Craft: `references/convergence-techniques.md`.
   - Why: a large misc cluster means the taxonomy failed, not the ideas.
7. **Dot-voting screens; rubric scoring decides.**
   - Craft: `references/convergence-techniques.md`.
   - Why: popularity and quality are different measurements, and only one of
     them is scoreable.
8. **Weights differ per criterion and are fixed before scoring begins.**
   - Craft: `references/idea-evaluation-rubrics.md`.
   - Why: equal weights are unexamined weights; late weights invite gaming.
9. **The feasibility floor is 3 — below it, derisk or archive.**
   - Craft: `references/idea-evaluation-rubrics.md`.
   - Why: unbuildable is not selectable; it is a research project wearing an
     idea's clothes.
10. **Every shortlist carries one constraint-born wildcard.**
    - Craft: `references/constraint-based-creativity.md`.
    - Why: constraints manufacture the novelty that safe rounds never reach,
      and a shortlist of near-identical safe ideas is a failed session.
11. **The facilitator hosts and records; they do not generate.**
    - Craft: `references/facilitation-guide.md`.
    - Why: a facilitator who generates cannot simultaneously protect the flow.
12. **Solo sessions still separate the two voices.**
    - Craft: `references/facilitation-guide.md`.
    - Why: the generator and the scorer share one skull; the physical break is
      the only thing keeping them distinct.
13. **The session ends with a written decision record — no exceptions.**
    - Craft: `references/ideation-capture-and-triage.md`.
    - Why: a session with no artifact is conversation, not ideation.
14. **Archive the unselected pool with reasons; never purge it.**
    - Craft: `references/ideation-case-studies.md`.
    - Why: the 80% rule says most of the pool goes unused by design — the
      archive is where its deferred value waits.

## 06 — Worked Example

The scenario: a 45-minute solo session to design the concept for a podcast
called **Urban Field Guide** — a show that helps city dwellers notice and
understand the nature they walk past daily, engaging enough to recommend and
practical enough to change how listeners walk. The fully annotated session,
with every idea, vote, and score, is in `examples/worked-ideation-session.md`;
this section walks the reasoning at workflow altitude.

### Steps 1-2 — Prompt, quota, setup, warm-up

- Prompt, passing all three tests: "How might we design a podcast that helps
  city dwellers notice and understand the nature they encounter daily — birds,
  plants, weather, sidewalk ecology — and is engaging enough to recommend and
  practical enough to change how people walk?"
- Constraints folded into the frame: audio-first, one person must be able to
  produce it, no budget for original field recordings. Success criteria: pool
  of 30+, shortlist of exactly 3, recorded at the top of the session template.
- Capture in a shared document, one numbered row per idea, timer visible,
  parking-lot section at the bottom. Warm-up produced eleven frictions in
  three minutes — capture verified at better than one idea per minute — then
  set aside unread.

### Step 3 — Techniques chosen

SCAMPER (a baseline exists — "a narrator describes urban wildlife on your
walk") plus worst idea first, with constraint flips held as the top-up round.

### Steps 4-6 — Round 1: SCAMPER, twelve minutes

Ten of the round's ideas, by SCAMPER move:

- Substitute (1-2): ambient field recordings only, the listener identifies what
  they hear; rotating local residents replace the single narrator voice.
- Combine (3-4): geotagged episodes that change with the listener's location;
  each episode paired with one build-it-yourself nature craft.
- Adapt (5-6): every episode opens with a 30-second "look up" prompt; one
  audio skill taught per episode — identify that bird by song.
- Modify (7-8): three-minute episodes, one species each; a seven-episode season
  released over seven consecutive days as a commute companion.
- Put to another use (9-10): recordings repurposed as a local-history
  soundscape; printable maps and checklists the listener carries on the walk.

### Step 7 — Round 2: worst idea first, twelve minutes

- Terrible ideas captured with enthusiasm (7): listeners clap to greet
  wildlife; a subscription squirrel-cam; animals delivering monologues;
  haiku-only episodes; AI narration from municipal waste data; thirty minutes
  of rustling leaves; a GPS sticker hunt.
- The flips produced the keepers (3): from the squirrel-cam, a five-minute
  "watch something vertical" listener assignment; from haiku-only, the
  30-second pocket guide — one species of the day; from animal monologues, the
  guest-city lens — real people (naturalist, gardener, street-sweeper) hosting
  episodes from their own block.
- One objection ("this is too niche") hit the parking lot and was resolved at
  convergence: the niche was the differentiation, not the bug.

### Steps 8-9 — Constraint top-up and break

- The pool stood at 27 after two rounds, so the top-up ran: audio-only
  inverted (add a printable field card), weekly inverted (daily), single host
  inverted (naturalist plus newcomer), polished structure inverted (start
  mid-scene, no intro). Born in the top-up: the city-layers miniseries (what's
  green / what's loud / what's on the pavement), mid-scene starts, the
  two-host pair, and the seven-day listener action arc.
- Two late captures duplicated earlier entries and were folded into their
  siblings — the pool is recorded as 30 distinct ideas.
- Three-minute break, physically out of the room, document closed.

### Steps 10-12 — Cluster, vote, matrix

- Five clusters: episode format (9), voices and participation (9), companion
  artifacts and partnerships (4), location and city-as-data (3), unflipped
  worst-case (5). Misc: zero — every idea landed in a named cluster.
- Solo dot budget spent: strong on the seven-day micro season, medium on the
  guest-city lens and the pocket guide, weak on the two-host pair, geotagged
  episodes, and the soundscape cycle. Top six advanced.
- Matrix: micro season, guest lens, pocket guide, and two-host pair placed
  high/high; geotagged episodes landed in research (needs an app partner);
  the worst-case and low/low ideas archived with one-line reasons.

### Step 13 — Scores

Default weights — Novelty 30%, Feasibility 35%, Fit 25%, Impact 15%. The
geotagged row is the floor working: a good weighted total is not a pass when a
required axis fails — deferred with a resurface condition, not deleted. The
pair and the guest lens were one idea in two shapes; dedupe happened before
scoring, so neither inflated the other.

| Idea | N | F | Fit | I | Weighted | Note |
|---|---|---|---|---|---|---|
| Seven-day micro season | 4 | 5 | 4 | 4 | 4.55 | strongest across the board |
| Guest-city lens | 4 | 4 | 4 | 3 | 4.05 | highly repeatable per season |
| 30-second pocket guide | 3 | 5 | 3 | 3 | 3.85 | constraint-born wildcard |
| Geotagged episodes | 5 | 2 | 4 | 4 | 3.80 | feasibility floor: trip |
| Naturalist + newcomer pair | 3 | 4 | 4 | 4 | 3.90 | folded into guest lens |

### Step 14 — Shortlist and decision record

1. **Seven-day micro season** — three minutes, one species, daily. Highest
   weighted score; extreme feasibility; builds a daily habit loop.
2. **Guest-city lens** — a different city-knowing resident per episode.
   Repeatable across seasons and neighborhoods.
3. **30-second pocket guide** — one species of the day, built for sharing. The
   wildcard, born from the haiku constraint flip.

- Decision record: micro season selected (pilot: record one seven-day season);
  guest lens selected (contact two naturalists and one city worker); geotagged
  held (condition: platform partnership); worst-case and city-data clusters
  archived with reasons and resurface conditions. The 80% rule held: 27 of 30
  ideas went unused — on purpose, into the archive, where their value waits
  for a constraint change.

### What the example proves

- The last third of the pool paid: all three shortlist entries were born in
  round two's flips or the constraint top-up, not in round one. Worst-first
  earned its slot: two of three winners descend from deliberately terrible
  ideas.
- The two convergence gates caught different failure shapes: the matrix parked
  geotagged as research, and the feasibility floor caught it again at scoring —
  gates overlap by design, not by accident. Dedupe before scoring, so near-twin
  ideas cannot double-count votes and scores.
- The archive is a deliverable, not a scrap heap — the unflipped worst-case
  cluster contains the seed of a plausible second series track.

## 07 — Failure Modes and Recovery

1. **Premature convergence — judgment leaks into generation.**
   - Early signal: idea rate drops right after someone says "but we tried that."
   - Corrective move: park the objection, restart the timer, restate the rule.
   - Prevention: the no-critique rule is stated in Step 1 and enforced verbatim.
   - Detection: per-minute idea counts; a cliff after the first critique.
2. **The pool stalls at fifteen safe ideas.**
   - Early signal: the last five captures are paraphrases of each other.
   - Corrective move: switch to constraint flips or worst-first mid-round; run
     the forced push ("ten more, any technique").
   - Prevention: Step 3 pairs a generative technique with a lens-breaking one.
   - Detection: one cluster absorbing most of the pool during divergence.
3. **Loud-voice dominance in team sessions.**
   - Early signal: one participant's name on most captured ideas after round one.
   - Corrective move: switch the next round to silent brainwriting.
   - Prevention: brainwriting opens sessions where hierarchy problems are known.
   - Detection: per-participant authorship counts after round one.
4. **Champion bias carries a weak idea to the shortlist.**
   - Early signal: one person defends the same idea at every convergence gate.
   - Corrective move: re-vote blind and apply the champion-problem flag before
     scoring.
   - Prevention: anonymized capture from Step 4 onward.
   - Detection: correlation between idea authorship and vote share.
5. **The all-safe shortlist.**
   - Early signal: every finalist scores 4+ on Feasibility, 2 or less on Novelty.
   - Corrective move: run one constraint-flip round; force a wildcard into scoring.
   - Prevention: the novelty-line check in `references/idea-evaluation-rubrics.md`.
   - Detection: no finalist scores above 4 on Novelty anywhere.
6. **The session that produces no residue.**
   - Early signal: "great session — so what do we do now?" and no document to open.
   - Corrective move: fill the decision record before anyone leaves, owners and
     dates included.
   - Prevention: Rule 13 makes the record the session's exit condition.
   - Detection: templates returned with an empty decision-record section.
7. **Remote-session drift.**
   - Early signal: silence between contributions, cameras off, votes arriving late.
   - Corrective move: move contributions into the shared document (brainwriting).
   - Prevention: the remote setup constraints in Step 4, capped at six people.
   - Detection: per-participant contribution counts diverging widely.

### How the failure modes connect

- Modes 1 and 2 are divergence failures at opposite ends: judgment arriving
  early, and energy never arriving at all. The parking lot and the technique
  switch are the shared fixes.
- Modes 3 and 4 are authorship failures — loud in generation, quiet in
  scoring. Anonymity is the common defense, which is why capture setup is a
  named step and not an afterthought.
- Modes 5 and 6 are convergence and closure failures; mode 7 is the remote
  amplifier that makes all six easier to fall into.

## 08 — Supporting Files Index

Reading order: run §04 top to bottom and open a reference only when a step
names it; keep `templates/ideation-session-template.md` open as the session's
live document; read `examples/worked-ideation-session.md` after your first real
session, not before.

The file set is shaped so this document stays procedural: each reference
carries one body of craft — principles, divergence catalog, convergence
methods, constraint design, evaluation, facilitation, capture and triage, and
applied cases — while the template defines the artifact shape and the example
shows one complete session at full depth. If you read only one file before your
first session, make it `references/divergence-techniques.md`.

| File | Purpose | Used In |
|---|---|---|
| `references/ideation-principles.md` | Three pillars, two-phase process, the 80% rule | §04 Steps 2, 9; §05 Rules 1-2 |
| `references/divergence-techniques.md` | Catalog of seven divergence techniques | §04 Steps 3, 6-7; §05 Rule 5 |
| `references/convergence-techniques.md` | Clustering, dot-voting, matrix, weighting | §04 Steps 10-12; §05 Rules 6-8 |
| `references/constraint-based-creativity.md` | Designing constraints that generate novelty | §04 Steps 1, 8; §05 Rule 10 |
| `references/idea-evaluation-rubrics.md` | Scoring axes, weights, anti-pattern flags, floors | §02, §04 Step 13; §05 Rules 8-9 |
| `references/facilitation-guide.md` | Session blueprint, energy, solo and remote modes | §04 Steps 1, 4-5; §05 Rule 11 |
| `references/ideation-capture-and-triage.md` | Capture formats, parking lot, decision record | §03, §04 Steps 4, 14; §05 Rules 4, 13 |
| `references/ideation-case-studies.md` | Two realistic sessions with outcomes | §02, §05 Rule 14; §06 context |
| `templates/ideation-session-template.md` | The session's live document and artifact shape | §03, §04 Steps 2, 14 |
| `examples/worked-ideation-session.md` | Full Urban Field Guide session: 30 ideas to 3 | §06 |

Maintenance contract:

- This table must match the directory exactly; a file added or removed means a
  row added or removed, plus a citation at that file's point of use in §04.
- If a file is no longer used, remove both the file and its row — dead rows are
  findings, and so are orphaned files.
- Section edits that change a step's reference must update the Used In column in
  the same change.

Cross-skill boundaries:

- Narrative craft — story, character, dialogue — belongs to
  `story-and-narrative-design`; ideation selects among concepts, it does not
  write them.
- Executing the selected idea belongs to the downstream domain skill named in
  §02; the decision record is this skill's exit artifact, and follow-on work
  starts there.
- Process and production design for the follow-on work — schedules, workflows,
  resourcing — belongs to `operations-and-process-design`; if the shortlist
  needs a plan rather than a decision, hand it off.