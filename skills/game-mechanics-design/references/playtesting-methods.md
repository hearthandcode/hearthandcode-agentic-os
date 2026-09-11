# Playtesting Methods

Methodology for turning play sessions into design evidence. Playtesting is
not watching people have fun — it is running structured sessions, observing
behavior, and triaging feedback into decisions. This file covers
recruitment, session protocols, observation technique, and what to do with
what you hear.

## 1. What playtests are for

A playtest answers a question you wrote down beforehand. Good test
questions are behavioral and observable: "do players find the shrine within
4 minutes?", "do players use the block verb against ranged enemies?", "do
players abandon runs when the curse hits?" If the question is "do people
like it?", split it into what people do (behavior), what they say (opinion),
and what they fail at (legibility) — the three produce different fixes.

## 2. Recruitment

Who to recruit, in rough order of usefulness by project stage:

1. **The design team itself** — for gross breakage and feel at whitebox
   stage. Free, fast, and immune to nothing: designer immunity to friction
   sets in within hours of starting.
2. **Colleagues outside the project** — they owe you 30 minutes and will
   tell the truth gently. Best for first-exposure legibility.
3. **Friends-and-family** — enthusiastic, forgiving, dangerous. Their
   signals are real but exaggerated; use them for confidence checks, not
   for tuning.
4. **Target-audience strangers** — recruited for genre familiarity (or
   deliberate unfamiliarity, if testing onboarding). The gold standard
   from greybox onward; 5-8 players per round of the same segment
   surfaces the big issues.
5. **Expert players** — for balance validation, degenerate-strategy
   hunting, and difficulty ceilings. Never use them to judge difficulty
   for newcomers; they cannot remember being new.

Segment notes: mix session-length expectations (a five-minute mobile player
and a two-hour PC player break the same design differently). For
moderated tests, screen for the ability to narrate; for unmoderated
tests, screen only for the platform. Compensate strangers when the
session exceeds 45 minutes — incentives change behavior, so disclose them.

How many players: usability-style legibility problems surface by the fifth
unique player; balance problems need 15-30 plus telemetry; feel problems
need the team's own long sessions. Budget rounds, not sample sizes: three
rounds of five beats one round of fifteen.

## 3. Session protocols

Pick the protocol to match the question:

- **Think-aloud moderated (30-45 min):** player narrates decisions while
  playing; facilitator asks "what are you thinking?" and never helps.
  Best for legibility, onboarding, and confusion hunting.
- **Quiet observation (20-60 min):** no talk during play; note-taking on
  behavior, then a structured interview. Best for feel, pacing, and
  frustration — narration changes both.
- **A/B build test:** two builds differing in one variable, players
  randomly assigned. Best for parameter questions with binary answers.
- **Unmoderated remote build:** players play at home; you get telemetry
  and a feedback form. Best for volume, retention curves, and crash
  hunting; worst for understanding why.
- **Paper playtest:** at a table, rules on cards. Best for rule-set and
  economy questions before any code exists (details in the prototyping
  playbook).

Protocol ground rules for every type:

- Decide in advance what "success" is for each task; write it down.
- Never teach during the test unless the test is of the teaching.
- Log timestamps of every stumble, backtracking, and abandonment.
- The facilitator speaks last and least; silence after an answer pulls the
  real answer out.
- End every session with: what would you tell a friend? what would you cut?

## 4. Observation technique

Watch for the four signal classes; each maps to a different fix:

- **Stumbles** (hesitation, repeated deaths at one spot): friction or
  telegraph problems. Count them per player per minute.
- **Pivots** (the player changes plan mid-execution): decision points
  working — or failing, if pivots are involuntary. Mark what triggered it.
- **Skips** (content walked past without engagement): visibility or
  appeal failure, not difficulty.
- **Abandonment** (task or session quit): the strongest negative signal;
  note the moment and the state. Ten stumbles matter less than one quit.

Record behaviors, not interpretations, in the room. "Died twice at the
bridge, then quit" is evidence; "the bridge is boring" is a hypothesis.
Interpret later, against the log.

What to capture minimally per session: start/end time, build hash, player
segment, the task question, stumble/pivot/skip/abandon marks with
timestamps, verbatim quotes (the vivid ones travel), and your top-3 issues
draft. Telemetry adds the volume layer: completion rates, time-to-first-X,
death heatmaps, churn points.

## 5. Feedback triage

Player statements need translation before they become tasks. The standard
grist:

- Complaints about **difficulty** often mark legibility failures — players
  die to what they cannot read. Check telegraphs before touching numbers.
- Suggestions ("you should add a sprint button") are diagnoses in disguise;
  the underlying need ("I want to cross the safe town faster") is the task.
- Silence during failure is worse than cursing: cursing players are still
  engaged; silent ones have concluded the game is not about them.
- Requests to keep broken content ("don't change the infinite money glitch")
  mark fun discovered by players, not a defect — evaluate the fun.
- Feature requests from experts are balance data; from newcomers, they are
  onboarding data. Weigh by source.

Triage with three buckets and act in this order:

1. **Blocked:** players cannot proceed or the mechanic misfires. Fix before
   any further testing.
2. **Distorted:** players proceed but by avoiding the mechanic (never
   dodging, never selling, always blocking). Reprice or redesign.
3. **Polish:** it works; it drags. Queue for tuning, and say so in the
   notes so it is visibly triaged rather than ignored.

Every triaged item records: signal (behavior), interpretation (hypothesis),
decision (change, defer, reject), and the retest that will check it.

## 6. Reporting cadence

Same day: raw log with timestamps. Within 48 hours: one-page findings —
top issues with severity, evidence counts, and the decisions taken.
Within a week: the changes shipped, so testers see their fingerprints.
Testers who never see changes stop volunteering. Never argue with a
tester's experience; argue with your interpretation of it — privately,
afterward, in the triage doc.

## 7. Common playtest failures

- **The leading demo:** facilitator explains, rescues, and steers until the
  player succeeds. Prevention: write the no-rescue rule on the session
  script; if the test dies, the test found something.
- **The survey substitute:** 40 questionnaire answers, no observed play.
  Prevention: questionnaires report only; behavior decides.
- **The polite round:** friends praise everything; nothing changes.
  Prevention: ask "what would you cut?" — praise has no action item.
- **The flood:** 60 notes of equal weight; the big three drown.
  Prevention: triage buckets, severity labels, top-3 forcing.
- **The unverified fix:** issue marked fixed without a retest. Prevention:
  every fix names its retest in the same line.

## 8. A worked fragment

A greybox build of a vault-raiding mechanic, five colleagues, quiet
observation protocol, question: "do players choose stealth or speed, and
do they stick with the choice?" Findings: three of five players switched
to speed after the first alarm, citing (in the debrief) "the alarm cost
nothing." The alarm cost was raised (a lever, not a lecture), and the
retest showed 5 of 5 committing to one plan per vault. One-line lesson:
when players will not commit, price the commitment before adding more
stealth verbs.