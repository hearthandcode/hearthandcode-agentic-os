# Prototyping Playbook

Methodology for answering design questions as cheaply as possible. A
prototype is not a rough version of the game — it is an experiment whose
result changes a decision. If you cannot name the decision a prototype
informs, you are not prototyping; you are building with extra steps.

## 1. The fastest-testable-thing discipline

Every prototype starts with two sentences written down before any work:

- **The question:** "Will players <behavior> when <condition>?"
- **The decision it informs:** "If no, we <change X>; if yes, we <commit Y>."

Then find the cheapest artifact that can produce a signal on that
question. The ladder, from cheapest to most expensive:

1. **Spreadsheet:** numbers behaving as modeled. For economies, curves,
   and progression math. Hours.
2. **Paper:** rules and decisions, tested by hand. For rule sets, choice
   architecture, turn structure, card economies. Half a day.
3. **Greybox:** geometry without art, debug inputs, instant-restart
   loops. For feel, spacing, timing, readability. Days.
4. **Vertical slice with art:** one thread of the real game polished.
   For sell-ability and production risk. Weeks — use sparingly and late.
5. **Full build:** everything above, everywhere. Not a prototype; a
   milestone.

Skip rungs only when the question physically requires it (controller
feel cannot be tested on paper). Every skipped rung multiplies cost.

## 2. What each rung can and cannot answer

- **Spreadsheet:** answers "does the math do what we intend" — never
  "is it fun." Players are absent; agents are not players.
- **Paper:** answers rule clarity, decision depth, pacing of choices.
  Cannot answer real-time feel, dexterity, or UI. Playtests with 2-4
  people, roles played by hand, and iterate rules between rounds while
  enthusiasm is in the room.
- **Greybox:** answers legibility (can players read the space and the
  threat), timing, and rough feel. Cannot answer "is it fun long-term,"
  because novelty carries greyboxes further than art carries games.
- **Slice:** answers whether the promise lands for a new player. Cannot
  answer balance at scale (one slice is too little content) — resist
  reading balance conclusions from a slice.

## 3. Prototype hygiene rules

1. **One question per prototype.** A prototype testing three questions
   returns mush. Fork it if you must.
2. **Timebox before starting**, and honor the box. The timebox is part
   of the experiment: if the question needs two more weeks, the decision
   changes shape, not the box.
3. **Build the restart loop first.** Prototypes live or die on how fast
   you can get back to the moment being tested; instant restart is worth
   any ugly hack.
4. **Fake the rest.** Placeholder art, debug menus, teleport commands —
   every minute spent on polish inside a greybox is stolen from signal.
5. **Write the kill criteria before testing.** Decide in advance what
   result ends the idea ("if fewer than half the players re-enter within
   20 seconds, the death loop is broken"). Kill criteria written after
   the results are just opinions with graphs.
6. **Screenshot the build and archive it.** Prototypes get resurrected;
   without an archive, resurrection restarts from memory.

## 4. Paper prototyping, specifically

Paper works for any turn-structured or decision-structured system —
including real-time games reduced to their decision skeleton.

- Represent each player-facing state with a card; represent randomness
  with dice or a shuffled deck; represent timers with a phone.
- Design the first five minutes to teach itself; if you must explain,
  the explanation is a finding.
- Log decisions on a tally sheet; you are watching choice patterns, not
  winners.
- Rewrite rules between rounds, loudly and dated — the rule sheet's
  revision history is the prototype's most valuable output.
- Watch for players optimizing past the intended experience; that is
  the dominant-strategy check running early, for free.

## 5. Digital greybox, specifically

- Engine choice: whatever gets the question answered fastest — often the
   team's existing project forked, sometimes a throwaway scene. Never
   start a new engine for a prototype.
- Instrument early: log the events you will need for the playtest
   question (restarts, deaths, choices, session ends) before inviting
   players, not after.
- Budget the first-person hour: the designer should hit the tested
   moment within five minutes of pressing play, or the loop needs work
   before any outside eyes.
- Greyboxes decay: after ~three iterations, the team's familiarity
   poisons the feel data. Rotate fresh players or retire the box.

## 6. From prototype result to decision

End every prototype with a one-page memo: question, artifact, method,
result (with numbers or quotes), decision, and the next artifact or the
grave. Two outcomes are acceptable — the decision made, or the question
sharpened into a follow-up prototype. A third outcome — "we learned a
lot" with no decision — means the question was wrong, and the memo says
so rather than pretending.

## 7. Common prototyping failures

- **The pet demo:** polishing the greybox because it is satisfying to
  polish. Prevention: the timebox and the memo.
- **The vague question:** "is combat good?" Prevention: the two-sentence
  header rule; if it cannot be written, the prototype waits.
- **The sunk prototype:** continuing past the kill criteria because the
  artifact is done. Prevention: criteria dated before results.
- **The unplayable paper test:** paper for a dexterity question.
  Prevention: check the rung-answer table before building.
- **The designer-only signal:** testing with the four people who built
  it. Prevention: outside players at greybox stage, every time.

## 8. A worked fragment

Question: "Will players choose the risky vein over the safe vein when the
risk is visible?" Decision: if no, the risk display redesigns; if yes,
the mining loop keeps its core tension. Artifact: paper grid with token
veins and a hazard deck, half a day, two sessions with colleagues.
Result: players chose risky veins 70% of the time, but only after round
two's rule rewrite made hazard odds readable. Decision: keep the choice;
the visibility fix moved to the UI backlog. Next artifact: greybox with
the same numbers and real-time digging. One-page memo filed; the paper
rule sheet's three revisions are archived beside it.