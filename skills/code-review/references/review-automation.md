# Review Automation — What to Automate, What Stays Human

Every finding class that a machine can catch should be caught by a machine: cheaper,
faster, perfectly consistent, and free of social cost. Human review attention is the
scarce resource; this reference maps finding classes to their proper enforcement layer
so humans spend attention on judgment, not on typing "missing semicolon."

## The division of labor

| Finding class | Right layer | Why |
|---|---|---|
| Formatting, import order, whitespace | Formatter on save + pre-commit | Deterministic; zero-debate; instant |
| Syntax-level smells, unused vars/imports | Linter in CI | Fast; catches before review starts |
| Type errors, null-deref classes | Type checker as CI gate | Machines out-judge humans here |
| Known-vulnerable dependencies | Dependency audit bot in CI | Database lookup, not judgment |
| Banned patterns (string-built SQL, eval) | Custom lint rule / CI grep gate | One rule buys back hundreds of reviews |
| Secrets committed | Secret scanner in CI + repo hook | Must run before push lands, not after |
| Coverage drop on changed lines | Coverage gate in CI | Mechanical; configure thresholds honestly |
| Complexity/size gates (function length, file size) | Lint metrics with thresholds | Keeps diffs reviewable at all |
| Logic bugs, race conditions | **Human review** | Requires understanding intent and context |
| Security reasoning (authz design, crypto choices) | **Human review** + security pass | Pattern rules help; judgment decides |
| API ergonomics, naming meaning, function shape | **Human review** | Taste with consequences; not mechanizable |
| Test quality (asserts the right thing) | **Human review** | Coverage numbers cannot read assertions |
| Design fit, "should this exist" | **Human review** / architecture skill | Out of scope for diff-level review |

The rule that falls out: **if a class of finding appears three times in three reviews,
it graduates to automation.** Review findings are a bug report against the process.

## Building the automation ladder

1. **Formatter first.** Language-standard formatter, applied on save and in CI.
   Formatting comments in review drop to zero immediately. The formatter's opinion
   becomes the team's; the debate is closed by fiat, which is the point.
2. **Linter second.** The language's mainstream lint config, then team additions.
   Start with the recommended set; add custom rules only when review history shows a
   recurring class.
3. **Type checking third (where applicable).** Strictness pays for itself in the
   null-deref and shape-mismatch classes; adopt strict mode early when possible,
   gradually on legacy code.
4. **CI gates fourth.** Tests, coverage on changed lines, dependency audit, secret
   scan. The gate blocks merge; review verifies judgment calls on top.
5. **Custom rules last and surgically.** Each custom rule should trace to a real
   finding history: "we shipped two N+1s from lazy relations" → a lint that bans
   relation dereference in serializers. Rules without history are hunches; revisit
   and delete rules that never fire.

## Custom rules worth writing (found in real review histories)

- **No string-built queries:** flag string concatenation/interpolation adjacent to SQL
  keywords; force the parameterized helper. (Catches the injection class review keeps
  re-finding.)
- **No secrets by pattern:** known credential shapes (long base64, `AKIA` prefixes,
  `BEGIN PRIVATE KEY`) blocked at commit time.
- **No new endpoints without explicit auth declaration:** framework-specific rule that
  fails when a route lacks its authorization annotation/middleware.
- **Banned sinks:** `eval`, `exec`, dynamic `innerHTML` assignment, shell-string
  invocation — configured per language, logged with file/line.
- **Mandatory fields on new public API models:** e.g., every new response model
  carries the tenant scope field; every new date field names its timezone.

Each of these exists because a human reviewer kept catching the same thing. When a
rule fires rarely, delete it — rule rot is real.

## What stays stubbornly human

- **Intent checking.** Does the code do what the change claims? Only a human with the
  intent statement can say. (Step 1-2 of the workflow; no linter knows the intent.)
- **Context-dependent correctness.** The loop bound is wrong *for this* domain rule.
  The checklist catches it because the reviewer read the ticket; a linter cannot.
- **Security reasoning above pattern level.** The query is parameterized (lint passed)
  but the check runs before the authz check completes (race) — judgment.
- **Meaning of names and shape of abstractions.** Tools flag style; they cannot tell
  `processData` is hiding a transaction boundary.
- **Test adequacy.** Coverage measures execution, not assertion quality; only a reader
  can say the test pins the bug or just executes the code.
- **The meta-review.** "Is this diff the third copy of the same pattern? Is this the
  moment to hand off to architecture?" — systems thinking, human only.

## Measuring the review process itself

What to track, per team and per reviewer:

- **Approval latency by diff size.** Under-two-minute approvals on large diffs are
  rubber stamps; multi-day latencies are process rot. Both are findings against the
  process.
- **Defect escape rate.** Bugs found post-merge that review should have caught,
  sampled from incident reports: which finding class escaped, and was it mechanizable?
  Every escape feeds the automation ladder or the checklist.
- **Comment-to-fix conversion.** Findings that end up fixed vs dropped. Dropped
  findings without recorded rationale are review energy leaking out of the system.
- **Severity consistency.** Sample reviews quarterly; compare severity assignments
  across reviewers against the scale's definitions. Drift means recalibration training,
  not blame.
- **Review load distribution.** One reviewer carrying the team burns out and
  rubber-stamps; rotate and cap per-reviewer load.

## The feedback loop with the checklist

The review checklist (`references/review-checklist.md`) and the automation set evolve
together:

- Item escaped three times → build the lint/gate; mark the item "automated" so
  reviewers stop checking it by eye.
- Item never fires in a quarter of reviews → demote to the light-pass skim or drop it.
- New incident class appears → add the checklist item before the lint rule exists;
  humans check first, tools catch it forever after.

The checklist is not sacred; it is the cache of the team's scarred experience, and
automation is how the team stops re-bleeding from old wounds.

## Anti-patterns in review automation

- **The 10,000-warning bootstrap.** Enabling a strict linter on a legacy codebase and
  demanding authors fix unrelated warnings. Counter: baseline file or suppress-with-
  ticket, new code clean, migrate opportunistically.
- **The flaky gate.** A CI check that fails randomly trains everyone to hit "re-run"
  and eventually to ignore the gate entirely. Counter: quarantine flaky checks the
  same day; a gate's credibility is its value.
- **The style tribunal.** Automation that blocks merges on taste-level rules nobody
  agreed to. Counter: rules require team sign-off; the default is advisory until
  ratified.
- **Automation as review replacement.** "The linter passed" is not a review. Gates
  catch classes; the human pass covers what gates cannot — keep the distinction
  explicit in team policy.
- **Rules that fight the formatter.** Lint rules that conflict with the formatter
  produce noise on every run. Counter: resolve the conflict in config the week it
  appears; do not let teams develop workarounds.