# Giving and Receiving Feedback — Phrasing, Severity, Disagreement

The technical half of review is finding defects; the human half is saying so in a way
that gets them fixed without burning the relationship. Most review failures are human
failures: phrasing that reads as attack, severity that reads as power play, disagreement
that escalates because nobody had a protocol. This reference supplies the language and
the protocols.

## Severity language

Use a fixed scale and mean it. Invented or implicit scales ("this is pretty bad") force
authors to guess the stakes.

| Severity | Meaning | Merge rule |
|---|---|---|
| **Blocker** | Security, data loss/corruption, correctness defect on the main path, legal/compliance violation | Must fix before merge. No exceptions; "we'll fix it tomorrow" after merge is an incident template |
| **Major** | Significant defect on an edge path, missing required test, unbounded resource use, misleading name on load-bearing code | Fix in this PR or a same-week tracked follow-up with an owner |
| **Minor** | Small correctness/robustness gap, clarity issue with a real but limited cost | Fix now if trivial; otherwise ticket it. Never blocks |
| **Nit** | Taste, alternative phrasing, preference | Take it or leave it. Reviewer says "nit" explicitly and does not re-raise if declined |

Calibration rules:

- Severity describes the code's risk, not the reviewer's confidence in their own taste.
  A reviewer who marks three Nits as Majors trains authors to skim their reviews.
- If you are unsure between two levels, say so: "Major (possibly Blocker if X can be
  empty) — can you confirm X's domain?" Uncertainty stated is credibility preserved.
- Blocker is not a synonym for "I feel strongly." It has a specific meaning; borrowing
  it for emphasis is severity inflation and it devalues the scale for everyone.

## Phrasing patterns

The goal of every comment: the author knows what to do, why it matters, and feels
respected. Patterns that survive contact with real teams:

**Observation + impact + suggestion.** The workhorse.

- Weak: "This is wrong."
- Better: "This uses string concatenation to build the ORDER BY clause. Since `sort`
  comes from the request, a crafted value can execute arbitrary SQL. Suggest an
  allow-list: `{name: 'name', date: 'created_at'}`."

**Ask before asserting, when you might be missing context.**

- "Does the caller guarantee this list is non-empty? If not, `items[0]` throws on the
  empty case." — a question that becomes a finding only if the answer is no.
- Questions cost the author ten seconds; false assertions cost the author an argument.

**Anchor to the code, not the person.**

- Never: "you forgot the tenant check."
- Always: "this path skips the tenant check that `listInvoices` applies — was that
  deliberate?"
- The "was that deliberate?" close is not decoration: it is how you learn the author
  had a reason, and it makes being wrong painless.

**Praise specifically, sparingly, honestly.**

- "Nice — extracting the pagination helper made the controller readable" teaches what
  was good and costs one line. Generic "nice work" teaches nothing. Invented praise is
  worse than none; authors can tell.

**Bundle Nits; never let them lead.**

- One grouped comment: "Nits (ignore any): comment restates the code; `pageSize`
  could be a named constant; two blank lines at EOF." Nits listed first make the
  author hunt for the real findings among them.

**State your uncertainty and your review depth.**

- "Standard pass — I did not line-check the migration SQL."
- "I think this is a bug but I am not certain about the framework's null handling here."

**Write findings that teach.**

- The best review comments transfer the principle, not just the fix: one sentence on
  why the pattern matters ("allow-listing survives new columns; sanitizing does not")
  turns this fix into every future diff being better.

## Receiving a harsh review (for authors)

- Extract findings from tone: read the diff comments as a checklist and fix what is
  real; the venom is the reviewer's problem, not a reason to reject valid findings.
- Name tone violations once, plainly, in meta-language: "the findings stand, but
  please keep comments about the code." Escalate only if it repeats.
- Never rebut in bulk; answer findings individually with evidence. Bulk replies read
  as dismissal and extend the thread.
- If a review is unactionable (all verdict, no evidence), ask for specifics once:
  "which case does this break? I cannot fix a summary."

## Disagreement protocol

Technical disagreement is normal and healthy; unresolved escalation is not. The
protocol, in order:

1. **Restate the other side.** Each party states the other's argument to their
   satisfaction before rebutting. Half the disagreements dissolve here — they were
   talking past each other.
2. **Find the factual question under the value question.** "Should we validate here or
   at the boundary?" is a design value; "does the ORM escape this?" is a fact. Resolve
   facts with a test or the docs, immediately.
3. **Timebox the thread.** Three rounds of comments without convergence means the
   disagreement is about values or context, not code. Move to step 4.
4. **Talk synchronously.** Ten minutes of conversation resolves what thirty comments
   cannot. Chat is the worst medium for disagreement; tone disappears.
5. **Escalate to a named third party.** The team's tech lead or a senior neutral
   reviewer reads both arguments and decides. Their decision is recorded in the review
   thread; the losing side commits.
6. **Disagree and commit.** The losing side states their position once for the record
   ("I believe the allow-list belongs in config, not code — noted for the next
   revisit"), then implements the decision fully. Re-litigating in future reviews
   without new information is the protocol violation.

What the protocol prevents: the slow poison of "fine, whatever" implementations —
resentful compliance that ships the original plan's defects plus new ones.

## Review-related anti-patterns and their counters

- **The drive-by nitpick** (one comment, no context, "why is this here?"): the author
  cannot tell finding from curiosity. Counter: classify your comments; questions say
  "genuine question."
- **The wall of text** (40 comments on a 60-line diff): the signal drowns. Counter:
  severity-sorted findings; if everything matters, ask for a pairing session instead.
- **The re-review ambush** (new Major findings appear in round four): reviews that
  keep growing erode trust. Counter: declare the review complete each round; new
  findings after approval go through a fresh, explicit pass — usually a sign the first
  pass was shallow.
- **The style vendetta** (same preference, every review): counter: promote it to a
  linter rule or drop it. Human review is for what tools cannot see.
- **The silent approval** (LGTM with zero engagement on a risky diff): counter: the
  report template's summary line makes the reviewer state what they checked.
- **The public humiliation** (detailed findings pasted into a team channel): counter:
  review in the review tool; the channel gets the summary, never the anatomy.

## The meta-rule

Every phrasing choice reduces to one test: *after this comment, is the author smarter
and the code better — or just the author smaller?* Reviews are read by people who will
write the next diff too. Write for that person.