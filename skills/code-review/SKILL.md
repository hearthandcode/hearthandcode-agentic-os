---
name: code-review
description: >
  Load this skill when you are reviewing a pull request, diff, or changeset for
  correctness, security, performance, and readability — or when you need to give
  structured, actionable review feedback and handle disagreement professionally.
  Also load it when preparing code you authored for review, or when triaging a
  review queue. It produces a prioritized review report with severity-graded
  findings, concrete suggested fixes, and a disposition log. It does not do
  architecture design (use software-architecture-design) or test planning (use
  testing-strategy), though it hands findings to both.
---

# code-review

## 01 — Purpose

A code review is the last cheap place to find a bug. After merge, the same defect costs a
revert, an incident, or a customer report — each an order of magnitude more expensive than
the comment that would have caught it. That cost asymmetry is the whole economic argument
for review, and it only holds when reviews actually find things: an approval that misses
an injection is worse than no review, because it carries the team's stamp. But review is
also where teams burn trust: hostile nitpicks, unexplained demands, and rubber-stamp
approvals all damage the code and the people.

This skill turns review from an instinct into a repeatable procedure with a quality floor.
It walks one complete review pass over a changeset: understand the change's intent, trace
the data through it, check it against correctness, security, performance, and readability
criteria, then deliver findings as a prioritized report with suggested fixes.

The pass is designed to be deep where it matters and fast where it does not: a 40-line
diff gets the full checklist in twenty minutes; a 400-line diff gets a structured hour.
The procedure scales by attention, not by skipping steps.

The skill treats review as teaching as much as filtering. A good review leaves the author
better at the craft, not just this diff better fixed. The tone rules in the feedback
reference exist because the difference between a review that lands and one that breeds
resentment is rarely the technical content — it is the framing.

**Three outcomes this skill owns:**

1. A findings report a reviewer can send and an author can act on: every finding has
   severity, location, evidence, and a suggested fix — none is a vague vibe.
2. Security and correctness coverage that survives a hostile diff: the checklist covers
   injection, authorization, secret handling, boundary conditions, and error paths, so
   "LGTM" means something.
3. A review conversation that stays professional under disagreement: the skill provides
   phrasing patterns, severity language, and an escalation path that respects both the
   author's judgment and the reviewer's duty.

## 02 — When to Use / When Not to Use

### Use this skill when:

1. **You are assigned a pull request to review.**
   - Any size, any language. The workflow scales its depth to the diff; the checklist
     applies to 20 lines as to 2,000.
   - You will produce findings with severities instead of a stream of chat comments.
2. **You are about to open a pull request of your own.**
   - Running the checklist against your own diff before requesting review catches the
     mechanical findings early and saves a review round-trip.
   - Author self-review also sharpens what to tell reviewers: known weaknesses and
     deliberate trade-offs should be stated, not discovered.
3. **You are reviewing a security-sensitive change.**
   - Auth flows, input handling, SQL or shell construction, file and network I/O, crypto
     use, dependency bumps.
   - The security reference gives the injection and authorization checks that generic
     review habit misses.
4. **You are triaging a review backlog or deciding what to automate.**
   - The automation reference maps finding classes to the right enforcement layer:
     formatter, linter, type checker, CI gate, or human attention.
   - Use it to stop spending human review on what a robot catches better.
5. **You disagree with an author or reviewer and need the disagreement resolved.**
   - The feedback reference has severity language, phrasing patterns, and the
     disagree-and-commit protocol for resolving stalemates.
   - This includes receiving a harsh review yourself: there is a protocol for that too.
6. **You are calibrating a team's review standards.**
   - The principles and checklist references define what "reviewed" means, so approval
     stops being a social ritual and starts being a quality bar.
   - The case studies show the standard applied to realistic diffs.

### Do NOT use this skill when:

1. **You are deciding how a system should be structured.**
   - Component boundaries, style choice, and decision records belong to
     `software-architecture-design`. Review comments can observe structural problems;
     they should not redesign the system inline.
2. **You are planning what tests to write.**
   - Test plans, coverage strategy, and flake policy belong to `testing-strategy`.
   - Review asks "is there a test for this behavior?" — the strategy skill decides what
     the test suite should look like overall.
3. **The code is not yet written and you are evaluating a design proposal.**
   - Reviewing pseudocode or a design doc is architecture review, not code review; the
     altitude and artifacts are different.
4. **You need a merge decision on business or product grounds.**
   - Whether a feature should ship is a product question; review can flag scope creep
     but does not own the yes/no on the feature itself.
5. **You are doing a post-incident forensic audit of merged code.**
   - Incident analysis has its own discipline (timeline, contributing factors, blameless
     framing). Review technique informs it, but this skill's workflow presumes a
     pre-merge diff.

## 03 — Inputs and Outputs

### Inputs

You should have at least ONE of these before starting:

- **A diff or pull request.** The changeset itself, with enough context to see the
  surrounding code. A diff without its function's full body hides boundary bugs.
- **The stated intent.** A PR description, ticket link, or one sentence: "add CSV export
  to the orders API." Review checks intent against implementation; no intent, no review.
- **Constraints and conventions.** Team style guide, security requirements for the touched
  area, known performance budgets.
- **Prior review history.** Earlier comments on the same PR, so you do not relitigate
  resolved threads.
- **For author self-review:** your own diff and five minutes of honesty about which parts
  you are least sure of.

### What good inputs look like

- A diff under ~400 lines reviews deeply in one sitting; larger diffs review better split,
  and the workflow says when to ask for a split.
- An intent statement with acceptance criteria turns the review from taste-checking into
  verification.
- A failing CI run attached to the PR converts half the mechanical checklist into a
  five-second check.
- Access to the running system or a staging environment lets you verify claims the diff
  makes; some reviews are settled by clicking, not reading.

### Outputs

1. **A review report** (`templates/review-report-template.md`) — the durable artifact:
   summary, findings table with severity and location, suggested fixes, disposition log.
   Sendable as a PR comment or a document.
2. **Inline comments** for the author's context: each one anchored to a line, phrased per
   the feedback reference, with severity marked.
3. **A verdict** with an explicit category: approve, approve-with-comments, request
   changes, or block (security/data-loss only). Ambiguous verdicts are a defect.
4. **Handoffs:** findings that belong to another skill — an architectural concern to
   `software-architecture-design`, a test-plan gap to `testing-strategy` — recorded as
   handoff notes rather than smuggled into style nitpicks.

## 04 — Workflow

A complete pass has twelve steps. Steps 1-5 build the mental model; 6-10 are the checks;
11-12 deliver the verdict. Skimming steps 1-5 to jump to comments is the most common way
reviews go wrong.

### Step 1 — Read the intent before the code
**Reference:** `references/review-principles.md`

- Read the PR description, ticket, or commit message first. What is this change trying to
  do, and what should NOT change?
- Read the diff at skim depth once without commenting: get the shape, the files touched,
  the size.
- Check the size against your attention budget: over ~400 lines, ask the author to split
  it or book a walkthrough; reviewing a 2,000-line diff in one pass produces vibes, not
  findings.
- Skim the PR's CI status and existing comments so you do not duplicate answered questions.
- Note the change type: feature, fix, refactor, config, dependency, generated code — each
  shifts which checks matter.
- Checkpoint question: "Could I state this change's purpose in one sentence? If not, ask
  the author before proceeding."

### Step 2 — Understand the change in context
**Reference:** `references/review-principles.md`

- Open the full files for the changed hunks: the diff shows lines; bugs live in context.
- Trace the main path end to end: where does the input enter, where does the result land?
- Identify the blast radius: which callers, endpoints, jobs, or tests does this touch?
- For refactors, verify behavior preservation is actually the goal and check for a test
  that pins it.
- Note anything that surprised you — surprise is where findings live.
- Checkpoint question: "If this change does what its author says, what would I expect to
  see — and do I see it?"

### Step 3 — Run the correctness pass
**Reference:** `references/review-checklist.md`

- Work the checklist's correctness section line by line on logic changes: loop bounds,
  off-by-one conditions, null and empty handling, operator precedence, mutation of shared
  state, integer overflow, time and timezone handling, float equality.
- For each branch in changed code, ask what makes it taken; untaken branches are where
  bugs hide.
- Check error paths with the same care as happy paths: what happens when the call fails,
  the list is empty, the lock is held?
- Verify claimed behavior against the actual code, not the description.
- Checkpoint question: "For every condition I can vary (empty, one, many, huge, weird),
  do I know what this code does?"

### Step 4 — Run the security pass
**Reference:** `references/security-review-basics.md`

- Check every place user-controlled data enters: does it reach a SQL query, shell
  command, HTML/JSON output, file path, or URL without parameterization or escaping?
- Check authorization on every new or changed endpoint and data access: is the permission
  check present, at the right layer, and does it cover indirect access (IDOR)?
- Check secret handling: no credentials in code, logs, or test fixtures; new secrets go
  to the secret manager, not the diff.
- Check dependency changes: what is this new package, who maintains it, what does it
  actually pull in?
- Check the crypto: standard library primitives only, no home-rolled schemes, randomness
  from the right source.
- Checkpoint question: "If a hostile user spent an hour on this code, what would they
  try first — and does the code survive it?"

### Step 5 — Run the performance pass
**Reference:** `references/performance-review-basics.md`

- Identify the hot paths the change touches: request handlers, per-row loops, scheduled
  jobs, hot library functions.
- Look for the classic shapes: queries inside loops (N+1), unbounded result sets,
  repeated work that could be hoisted, allocations in tight loops, synchronous calls
  where a batch exists.
- For data access, ask about indexes: does the new query match an index, or does it scan?
- Do not demand measurements for non-hot-path code; performance review is about the
  shapes that scale badly, not micro-taste.
- Checkpoint question: "If this ran at 100x today's volume, what breaks first — and is
  that acceptable?"

### Step 6 — Run the readability pass
**Reference:** `references/readability-and-style.md`

- Read the diff as the next maintainer would: does the code say what it does without a
  guide?
- Check names: do they carry meaning or just type information? Is the lie-to-truth ratio
  in comments favorable?
- Check function shape: one level of abstraction per function, early returns over nested
  conditionals where they aid reading, no function doing three jobs.
- Check dead code, commented-out code, and speculative generality.
- Apply the team's conventions; enforce them once, then automate them.
- Checkpoint question: "In six months, will the next reader understand this without
  asking the author?"

### Step 7 — Check the tests
**Reference:** `references/review-checklist.md`

- Does the change come with tests that fail without it? A fix without a regression test
  is a bug on layaway.
- Do the tests assert the right things — behavior, not implementation details?
- Are there tests for the boundary conditions the checklist found (empty, one, many,
  huge, weird)?
- Do new tests pass in isolation and are they deterministic? Flaky tests are findings.
- For security fixes: does a test demonstrate the exploit is closed?
- Checkpoint question: "If the author's fix silently regressed next month, would any
  test go red?"

### Step 8 — Assign severities and draft findings
**Reference:** `references/giving-and-receiving-feedback.md`

- Grade each finding: Blocker (must fix before merge), Major (fix now or in a tracked
  follow-up), Minor (should fix, non-urgent), Nit (take it or leave it).
- Anchor every finding to a file and line; unanchored findings are unactionable.
- For each finding, state the evidence and the suggested fix. "I think" without evidence
  is not a finding.
- Mark your confidence where you are unsure; a wrong Blocker costs more than a missing
  Minor.
- Checkpoint question: "For each finding, could the author act on it without asking me
  what I meant?"

### Step 9 — Compose the review
**Reference:** `templates/review-report-template.md`

- Write the summary: what the change does, overall assessment, the verdict category.
- Fill the findings table: severity, location, issue, suggestion, status.
- Order by severity, then by reading order; put the praise first if praise is due, and
  mean it or omit it.
- Keep the report under a page for a normal diff; a novel per diff is a review nobody
  reads.
- Use inline comments for line-level detail and the report for the overview.
- Checkpoint question: "If I were the author, would I know exactly what to do next?"

### Step 10 — Deliver and discuss
**Reference:** `references/giving-and-receiving-feedback.md`

- Deliver promptly; a review that ages a week is a review the author resents.
- Respond to author pushback on the merits: if their argument is right, update the
  finding; if the disagreement persists, use the disagree-and-commit protocol.
- Never let a review become about the author; the code is the subject.
- For unresolved Blockers, escalate per team policy rather than approving to be polite.
- Checkpoint question: "Is the disagreement about the code, or about us? If it is about
  us, resolve that directly."

### Step 11 — Record dispositions and follow-ups
**Reference:** `templates/review-report-template.md`

- For each finding, record the outcome: fixed, accepted-with-rationale, or follow-up
  ticket with an owner.
- Follow-ups without owners and dates are how accepted risks silently become incidents.
- Note any systemic finding for the automation discussion: if three PRs miss the same
  thing, that thing is now a linter rule.
- Checkpoint question: "Will someone be able to see, in a month, why each finding was
  resolved the way it was?"

### Step 12 — Close the loop and improve the process
**Reference:** `references/review-automation.md`

- Move every repeatable finding class into automation: formatter, linter, type checker,
  or CI gate, per the automation reference's mapping.
- Retire checklist items that automation now covers; keep human attention for judgment
  calls.
- Sample your own reviews monthly: are severities consistent? Are findings actionable?
  Is approval latency within team norms?
- Checkpoint question: "Which of today's findings should no human ever have to find
  again?"

## 05 — Rules and Quality Bar

How to use these rules: run any review against them before sending. A violated rule with
no rationale is a defect in the review itself.

1. **Review the code, not the coder.** Every comment addresses the diff, never the person.
   - Craft: `references/giving-and-receiving-feedback.md`.
   - Why: reviews that judge authors end; reviews that improve code continue.
   - Corollary: "you always do this" is never a review finding.
2. **Understand before you judge.** No finding is issued until you can state what the
   change intends and how the changed code flows.
   - Craft: `references/review-principles.md`.
   - Why: most false-positive reviews come from reviewing the diff in imagination rather
     than in context.
3. **Every finding is specific, evidenced, and actionable.**
   - File, line, what is wrong, why it matters, suggested fix — or an honest "I might be
     missing context here."
   - Why: vague findings teach nothing and resolve nothing.
4. **Severity is about the code, not the reviewer's mood.**
   - Blockers are defects that damage users, data, or security. Taste is a Nit.
   - Craft: `references/giving-and-receiving-feedback.md`.
   - Why: inflated severity trains authors to ignore reviews entirely.
5. **Security findings are never waived for convenience.**
   - An injection, a missing authorization check, or a logged credential is a Blocker
     regardless of deadline.
   - Craft: `references/security-review-basics.md`.
   - Why: the cost asymmetry is extreme — a fix now is minutes; a breach later is the
     company's problem.
6. **A fix without a test is a finding.**
   - Regression coverage accompanies behavior changes; the review asks which test fails
     without this change.
   - Craft: `references/review-checklist.md`.
   - Why: untested fixes are bugs waiting for their next production debut.
7. **Style is enforced by tools, not by humans.**
   - Formatting and naming conventions belong to formatters and linters; human review
     spends attention on what tools cannot see.
   - Craft: `references/review-automation.md`.
   - Why: style debates in review are the most expensive way to have them.
8. **Review in the author's interest.** The goal is their growth and the code's safety,
   in that order.
   - Craft: `references/review-principles.md`.
   - Why: authors who feel attacked hide; authors who feel taught iterate faster.
9. **Uncertainty is stated, not hidden.** "I think this is wrong because X" beats a
   confident wrong call.
   - Why: reviewers trade credibility for confidence at exactly the wrong moments.
10. **Approve nothing you cannot explain.** Approval means you understood the change and
    checked the checklist; rubber stamps are unreviewed merges with extra steps.
    - Craft: `references/review-checklist.md`.
    - Why: the merge button is the team's last quality gate; passing it through
      unexamined defeats the whole practice.
11. **Hand off what belongs elsewhere.** Architectural redesign and test-strategy gaps are
    recorded as handoffs, not inline redesign lectures.
    - Handoff targets: `software-architecture-design`, `testing-strategy`.
    - Why: scope discipline keeps reviews fast and findings actionable.
12. **Follow up or the review did not happen.** Every finding ends in fixed,
    accepted-with-rationale, or an owned ticket.
    - Craft: `templates/review-report-template.md`.
    - Why: untracked "should fix later" is how known vulnerabilities ship.
13. **Small diffs get deep reviews; big diffs get split.** The reviewer's attention is
    the scarcest resource in the process; spend it where it resolves.
    - Why: a 2,000-line diff reviewed in an hour was not reviewed; it was blessed.
14. **Write the report, not just the chat.** Verbal or chat-only reviews leave no record;
    the report is the institutional memory of what was found and decided.
    - Craft: `templates/review-report-template.md`.
    - Why: next quarter's auditor, or next month's incident review, reads artifacts —
      not Slack scrollback.

## 06 — Worked Example

The scenario: you are reviewing a 120-line diff — "Add pagination to invoice list" — from
a competent, trusted author. Two serious defects hide in it: a SQL injection through a
sort parameter, and an off-by-one in the page-boundary logic that silently drops a record.
The full annotated diff and the finished report are in
`examples/worked-code-review.md`; this section walks the reasoning.

### Steps 1-2 — Intent and context

- PR description: "Adds page and sort parameters to GET /invoices; customers asked to
  jump to a page instead of scrolling."
- Skim: 3 files, 120 lines changed — a controller, a repository, one test file. Small
  enough for a deep single pass.
- Intent stated for the check: users can fetch invoices by page number with a sort
  choice; existing API behavior for unpaginated callers must not change.
- CI green, no prior comments; review proceeds from a clean slate.
- Context read: the repository has an existing `paginate()` helper this diff bypasses —
  noted as a question for the author (later resolved: the helper lacks sort support, and
  extending it would have changed its other callers; the bypass was deliberate and is
  fine, but the diff never said so).
- Surprise noted early: the sort parameter is interpolated directly into the query
  string-building code — flagged for the security pass before the deep read even starts.

### Steps 3-4 — Correctness and security pass findings

- Off-by-one found by boundary math, not intuition: `page` is 1-based from the API but
  the offset math is `page * pageSize`, so page 1 returns rows `pageSize`..`2*pageSize-1`
  — the first row never appears, and the last page silently drops records whenever
  `count % pageSize != 0`.
- Verified against the test in the diff: the new test uses `page=1, pageSize=50` against
  120 rows and asserts "50 returned" — it passes on the buggy code, which is exactly how
  the bug ships.
- Second correctness finding: `totalPages` computed from a stale count fetched before the
  insert-happy window — minor, with a follow-up ticket.
- The sort parameter reaches SQL as string concatenation: `ORDER BY " + sortColumn`.
  Column names cannot be bind parameters, so the fix is allow-listing, and the reference
  has the pattern.
- Exploit demonstrated in the finding: `sort=name; DROP TABLE invoices; --` (or more
  subtly, `name; SELECT pg_sleep(10)`) — proof this is a Blocker, not a nit.
- Second security finding: the pagination endpoint skips the tenant check the old path
  had; cross-tenant page fetches work if you guess IDs — IDOR, also a Blocker.
- Secrets check clean; dependency check clean (no new packages).

### Steps 5-6 — Performance and readability

- The count query runs on every page load with no caching and no cap on `pageSize` — a
  client can request `pageSize=1000000` and melt the database; Major, with a suggested
  cap of 200.
- The sort path bypasses the existing helper, so the new query shape will not pick up
  any future index tuning applied there — Minor, folded into the stale-count follow-up.
- Readability is genuinely good: names are clear, the pagination helper is extracted and
  reusable, the controller stays thin. Two Nits only — praise where due, per the
  principles reference.
- Comment check: the one comment in the diff ("// paginate") restates the code and should
  go; the reference calls this a label, not a comment.

### Steps 7-8 — Tests and severity assignment

- Test finding (Major): the new test asserts the buggy behavior's symptom (50 rows from
  page 1) but pins it wrongly — after the fix it must assert rows 1..50 on page 1 and
  20 rows on page 3 for 120 rows. A test that fails without the fix AND with it is
  worthless; this one passes with the bug, which is the quiet scandal of the diff.
- Severity table assembled: 2 Blockers (injection, IDOR), 2 Majors (off-by-one, missing
  tenant check was folded into the IDOR blocker; pageSize cap and test-pinning are the
  Majors), 1 Minor (stale count), 2 Nits.
- Confidence stated on the injection finding: certain — the exploit string is included.

### Steps 9-10 — Report and verdict

- Verdict: **request changes** — two Blockers make approval impossible; the report says
  so in one line, then details.
- The report leads with what is good (clean structure, good helper extraction) because
  the feedback reference is explicit about it, then the findings table.
- Suggested fixes are concrete: the allow-list map is written out in the example file,
  the offset math corrected, the tenant check restored with a test.
- The report's summary states the review depth honestly: full checklist, ~50 minutes,
  including writing the exploit proof — so the author knows the Blockers were earned.
- Inline comments kept to the four substantive findings; the Nits ride in one grouped
  comment so they cannot masquerade as blockers.
- Author response simulated in the example: author asks "why not just sanitize the sort
  string?" — the reply cites the reference's rule that deny-list sanitization fails on
  unknown surfaces and shows the allow-list as strictly simpler.
- Second author question: "isn't the off-by-one just a doc fix?" — answered with the
  boundary math written out: 120 rows, page 3, pageSize 50 must return rows 101..120;
  the shipped math returns rows 151..170, i.e. nothing. A doc fix cannot return rows
  that do not exist.
- The disagreement resolves on evidence, not authority — which is the point of writing
  the math into the finding.

### Steps 11-12 — Dispositions and automation

- Dispositions: both Blockers fixed in the follow-up push; off-by-one fixed with the
  corrected test; pageSize cap added; stale-count follow-up ticketed with an owner.
- Automation lesson recorded: the injection class (string-built SQL) is now caught by a
  repository-lint rule banning non-parameterized query construction; the off-by-one got
  a property test idea handed to `testing-strategy`.
- The tenant-check miss prompted a checklist addition: "does every new data-access path
  carry the authorization check the old path had?"
- Outcome verified by the example file: the fixed diff's tests fail without the fix —
  the property the original diff's tests lacked.
- What the review cost, honestly: about 50 minutes including writing the exploit proof
  and the corrected test. What it prevented: silent data loss on every odd-sized last
  page, a cross-tenant read, and an injection reachable by every customer with a URL.
- The lesson for the team: the diff was small, well-formatted, and green in CI — none of
  which correlates with correctness. Only the checklist found what mattered.

### What the example proves

- Reading the test first is not enough: the diff's own test pinned the bug. Boundary
  math beats test greenness.
- Security findings need proofs, not vibes: the exploit string converted a debatable
  comment into an unarguable Blocker.
- Severity discipline kept the review short: two Blockers and two Majors carried the
  verdict; the Nits were grouped and marked as taste.
- The follow-ups outlived the review: a lint rule, a checklist line, and a handoff —
  the review's value compounds only if the dispositions are recorded.

## 07 — Failure Modes and Recovery

1. **Rubber-stamp review under time pressure.**
   - Early signal: approvals arriving in under two minutes on large diffs.
   - Corrective move: rerun the checklist on the diff; retrain attention on Steps 3-5.
   - Prevention: size limits in team policy; big diffs get split or get a dedicated hour.
   - Detection: review-latency metrics by diff size; an inverse correlation is the tell.
2. **Style war drowns the real findings.**
   - Early signal: twenty comments on formatting, none on logic.
   - Corrective move: move style to tooling per the automation reference; re-issue the
     review with severity-ranked findings only.
   - Prevention: team rule — style comments only for what tools cannot check.
   - Detection: comment-tag ratio (style vs. substance) per reviewer, reviewed monthly.
3. **The security flaw everyone saw and nobody flagged.**
   - Early signal: a review thread where someone says "hmm" about input handling and
     moves on.
   - Corrective move: reopen the review; file the Blocker late but file it.
   - Prevention: the security pass is a separate, named step — never folded into
     "general reading."
   - Detection: post-merge security greps on high-risk patterns (`+ "` near SQL, string
     interpolation into queries).
4. **Nitpicking as status display.**
   - Early signal: reviews full of personal-preference comments with no severity.
   - Corrective move: enforce the severity scale; nits must say "nit" and carry no
     blocking weight.
   - Prevention: reviewer training on the feedback reference's phrasing patterns.
   - Detection: comment severity distribution per reviewer; pure-Nit reviewers get
     coaching, not silence.
5. **The author "fixes" findings without understanding them.**
   - Early signal: follow-up pushes that appease comments without addressing causes.
   - Corrective move: re-review the fix's substance; if the cause persists, say so
     plainly and point at the reference that explains it.
   - Prevention: findings written to teach — evidence plus suggested fix, not verdicts.
   - Detection: same-file, same-class findings recurring across three consecutive PRs
     from one author pair.
6. **Review as gatekeeping theater.**
   - Early signal: approvals depend on who the author is, not what the diff does.
   - Corrective move: apply the checklist uniformly; make the report template the
     artifact of record for every approval.
   - Prevention: the checklist defines "reviewed"; approval without findings is suspect.
   - Detection: audit sampled approvals — could the approver explain the change?
7. **The disagreement that poisons the working relationship.**
   - Early signal: threads growing from technical points to "as I already said."
   - Corrective move: invoke disagree-and-commit; escalate to a third reviewer or the
     team's tech lead as a neutral reader.
   - Prevention: timebox comment threads; three rounds without convergence escalates.
   - Detection: thread length and tone shift; a mediator costs less than a rift.
8. **Findings without follow-through.**
   - Early signal: "should fix" comments that nobody ever tracks.
   - Corrective move: convert open findings to tickets with owners in the same session.
   - Prevention: the disposition step is mandatory before approval-with-comments.
   - Detection: quarterly sample of review findings — were they resolved or dropped?

### How the failure modes connect

- Modes 1 and 6 are attention failures at opposite ends: too little scrutiny and
  misdirected scrutiny. The checklist and severity scale are the shared fix.
- Modes 3 and 5 are teaching failures: the reviewer saw the problem and did not
  communicate it effectively. The feedback reference's phrasing patterns target these.
- Modes 2 and 7 are relationship failures wearing technical clothing; both resolve by
  moving taste out of human review and disagreement into protocol.
- Mode 8 is the system failing silently: reviews happened, nothing changed. The
  automation reference exists to convert review energy into permanent fixes.

## 08 — Supporting Files Index

Reading order: run §04 top to bottom; open a reference when a step names it; use the
report template when composing findings; read the worked example after your first real
review, not before.

Why the file set is shaped this way: the eight references each carry one body of craft —
principles, checks, security, performance, readability, human dynamics, automation, and
applied cases — so SKILL.md stays procedural rather than encyclopedic. The template
defines the one output shape (the report). The example shows the full pass on a diff with
hidden defects at realistic depth. If you read only one file before your first review,
make it `references/review-checklist.md`.

| File | Purpose | Used In |
|---|---|---|
| `references/review-principles.md` | Review for the author, reader, and future; what review is for | §04 Steps 1-2; §05 Rule 2 |
| `references/review-checklist.md` | Correctness, edge cases, error handling checklist | §04 Step 3, Step 7; §05 Rule 10 |
| `references/security-review-basics.md` | Injection, authz, secrets, dependencies | §04 Step 4; §05 Rule 5 |
| `references/performance-review-basics.md` | Hot paths, allocations, N+1 | §04 Step 5 |
| `references/readability-and-style.md` | Naming, function shape, comments | §04 Step 6; §05 Rule 7 |
| `references/giving-and-receiving-feedback.md` | Phrasing, severity, disagreement protocol | §04 Steps 8, 10; §05 Rules 1, 4 |
| `references/review-automation.md` | What to automate, what stays human | §04 Step 12; §05 Rule 7 |
| `references/review-case-studies.md` | Three realistic diffs with full reviews | §06 Worked Example context |
| `templates/review-report-template.md` | Findings report shape | §04 Steps 9, 11; §05 Rule 14 |
| `examples/worked-code-review.md` | Full 120-line diff review with the two hidden defects | §06 Worked Example |

Maintenance contract:

- This table must match the directory exactly — the verification suite diffs it against
  reality.
- If you add a file, add a row and cite it at its point of use in §04.
- If a file is no longer used, remove both the file and the row; dead rows are findings.

Cross-skill boundaries:

- Findings that reveal structural problems (a boundary that should not exist, a module
  growing grab-bag tendencies) are recorded here and handed to
  `software-architecture-design`; review flags, architecture decides.
- Test-suite design gaps surfaced by review (missing coverage strategy, no flake policy)
  belong to `testing-strategy`; review asks whether the behavior is tested, strategy owns
  the suite design.
- If a review surfaces the third "temporary" exception to a boundary in a month, stop
  reviewing diffs and start an architecture conversation — the pattern is the finding.