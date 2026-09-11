# Review Principles — Review for the Author, the Reader, and the Future

Code review is three jobs wearing one badge: a quality gate that catches defects, a
teaching exchange that raises the whole team's craft, and a record that explains the code
to the person who reads it in two years. Reviews that do only the first job produce
grudging compliance; reviews that ignore the first produce admiration and outages. This
reference covers the principles that make all three work.

## The three audiences

Every review decision serves three readers at once. When they conflict, the order of
precedence is: correctness of the shipped system, then the future maintainer, then the
author's comfort — but a review that tramples the author stops being able to serve the
first two, because authors stop listening.

**The author.** The person in the review is usually competent, always busy, and frequently
operating on partial context about the surrounding system. They wrote the code they
wrote for reasons that made sense from where they sat. A review that assumes bad faith or
carelessness produces defensiveness; a review that assumes competence but sees something
they could not see from their seat produces gratitude.

- Assume the author knew things you do not; ask before asserting.
- Phrase findings against the code, never the coder: "this line drops the tenant check"
  not "you forgot the tenant check."
- When you find something good, say so specifically. Generic praise reads as filler; the
  author learns nothing from "LGTM."

**The reader.** The next person to touch this code — who may be the author in six
months with no memory of it. The review is the only moment when someone outside the
author's head reads the code closely before it ships. Their questions are the questions
the future reader will have.

- If you had to reread a function three times to follow it, the next reader will too —
  that is a finding, even if the code is correct.
- If a comment explains *what* the code does, the code should say it instead. If a
  comment explains *why*, it is usually the most valuable line in the diff.
- Naming is the review's highest-leverage readability lever: a rename costs seconds and
  saves the reader minutes forever.

**The future.** Review is the checkpoint where the team's standards are actually
enforced — or revealed to be fiction. Every approved diff teaches the team what is
acceptable. An approval with a known Blocker teaches that Blockers are negotiable.

- Ask what this diff makes normal: if it adds the third copy-pasted query builder, the
  finding is not about this diff alone.
- Consider the revert path: would this change be easy to undo if it goes wrong? Reversible
  changes can ship with less ceremony; irreversible ones cannot.
- Note drift: if the code contradicts the team's written conventions, either the code or
  the conventions need updating — silent drift poisons both.

## What review is for — and what it is not for

**Review is for:**

- Catching defects the author cannot see: blind spots, tunnel vision, unknown unknowns.
  This is the highest-value function and it works only with fresh eyes.
- Spreading knowledge: the reviewer now knows this subsystem; the author learns the
  team's standards. Rotation of reviewers is a feature, not an inefficiency.
- Enforcing the shared bar: tests exist, security checks are in place, the change does
  what it says.
- Recording intent: the review conversation and its report become documentation of why
  the code is the way it is.

**Review is not for:**

- Enforcing personal style. Formatters exist; the human reviewer who argues about tabs is
  spending team attention on a solved problem.
- Displaying status. Reviews full of archaic jargon and preference-nits teach the team
  that review is a hazing ritual.
- Blocking on taste. If a finding has no correctness, security, performance, or
  maintainability consequence, it is a Nit and says so.
- Re-litigating settled decisions. If the architecture was chosen in a recorded decision,
  the review does not reopen it on taste; it flags drift with evidence.

## The economics of review attention

Review attention is the scarcest resource in the process. A reviewer who spends an hour
on formatting spends an hour not spent on the loop bounds. The allocation rules:

1. **Severity first.** Read for Blockers (security, data loss, correctness) before
   anything else. A review that found two Blockers and missed a naming quibble succeeded;
   one that found five nits and missed the injection failed.
2. **Depth follows risk.** Auth, payments, data deletion, concurrency, and migration code
   get line-by-line reading. Formatting-only changes get a skim and the tooling gate.
3. **Timebox honestly.** A review that would take two hours and gets twenty minutes
   produces nothing useful. Say so and re-schedule or split the diff rather than
   pretending.
4. **Approve nothing unreviewed.** If you cannot honestly say you checked the checklist,
   say "I need more time" — an honest delay beats a dishonest approval.

## Findings, questions, and preferences — three different speech acts

Most review confusion comes from collapsing these three into one stream:

- **Findings** claim the code is wrong: "this drops records when count is not a multiple
  of the page size." They carry severity and evidence.
- **Questions** probe understanding: "does this helper handle an empty list?" They may
  resolve into findings or vanish; the author can answer, and answers are cheap.
- **Preferences** express taste: "I would have used a switch here." They are Nits, they
  never block, and stating them costs the author attention. Spend preference-budget
  sparingly; a reviewer who expresses ten preferences per review trains authors to skim
  their findings.

Before posting a comment, classify it. A surprising number of "findings" are preferences
in costume, and a surprising number of "questions" are findings afraid to commit.

## The three review modes

The depth of review should match the diff's risk, and the reviewer should say which mode
they ran:

- **Full pass:** intent, context, correctness, security, performance, readability, tests,
  report. For anything touching auth, data handling, money, or concurrency.
- **Standard pass:** intent, correctness on the changed logic, tests, readability skim,
  security scan of new inputs and endpoints. For ordinary feature and fix work.
- **Light pass:** intent, diff sanity, tooling gates, no logic deep-read. For
  formatting, docs, generated code, and version bumps. Even this pass reads the diff —
  "LGTM" without reading is not a mode.

State the mode in the review when it is below full. A reviewer who says "standard pass —
I did not line-check the migration" has given the team accurate information; one who
approved silently has not.

## When you are the author

Receiving review well is half the practice:

- Read the whole review before replying to any of it. Line-one anger at finding one
  ruins the reading of findings two through nine.
- Assume competence in the reviewer as you want it assumed in you. If a finding seems
  wrong, engage the evidence, not the tone.
- Answer questions explicitly; push back with evidence when the finding is wrong —
  reviewers update, that is the system working.
- Push your own "I am not sure about X" into the review conversation deliberately;
  disclosed uncertainty gets help, undisclosed uncertainty ships bugs.
- If a review is harsh in tone, address the substance and note the tone separately —
  "the finding about X stands, but please phrase findings against the code" is a fair
  meta-comment, delivered once, without heat.

## The review's contract with the team

A review that follows these principles makes four promises:

1. **I read your diff in context, not just the hunks.**
2. **My findings are specific, evidenced, and severity-graded — and I say when I am
   unsure.**
3. **My severity reflects the code's risk, not my mood or our history.**
4. **My approval means I checked the checklist, not that I skimmed and felt fine.**

Teams that keep these promises get reviews that catch real defects and grow engineers.
Teams that break them get approval theater — the expensive simulation of quality.