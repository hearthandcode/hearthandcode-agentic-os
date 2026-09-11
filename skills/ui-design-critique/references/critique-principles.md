# Critique Principles

Methodology for every critique this skill produces: how to frame judgment, how to label severity, how to phrase criticism, and how to turn raw observations into a prioritized report. Read this before running any critique, regardless of platform or product type.

## Goals before taste

A critique answers one question: **does this interface achieve its stated goal for its intended users?** It does not answer "would I have designed it this way?" Personal preference is not evidence. If you cannot connect a finding to a goal, a user, a task, or a named principle, it is not a finding — it is a preference, and it belongs in the report's open questions or nowhere at all.

Before looking at a single screen, write the goal sentence:

> This screen exists so that [user] can [task], and success looks like [measurable outcome].

Every screen in the critique gets its own goal sentence. A checkout step's goal is "complete address entry without errors or re-entry," not "look trustworthy" — trust is a means, not a goal. If the requester cannot supply goals, eliciting them is the first act of the critique, not a courtesy.

This rule cuts both ways. A screen that is visually dated but completes its task efficiently should be praised for efficiency and flagged for polish — not torn down. A screen that is beautiful but hides the primary action is failing, no matter how good the palette is.

## The finding format

Every finding in a report uses the same four-part shape. Consistency is what makes findings comparable, rankable, and assignable across reports and teams.

1. **Severity** — P0 blocker, P1 major, P2 moderate, or P3 polish (scale below).
2. **Evidence** — what is actually on the screen: the element, its location, its state, and what a user encounters. Specific and checkable.
3. **Principle** — the violated rule, named and tied to its reference file (for example, "body text fails the 4.5:1 minimum — see `references/color-and-contrast.md`").
4. **Fix** — the concrete change to make, scoped to what the team can actually ship.

A finding missing any part is a rough note, not a finding. "The buttons look weak" is a note. "The secondary 'Save draft' button uses the same fill and weight as the primary 'Submit payment' button, so risk-free and irreversible actions look identical (P2, emphasis budget — see `references/visual-hierarchy.md`); make 'Submit payment' the only filled button on the step" is a finding.

## Severity scale

Severity measures impact on users and the goal — never implementation effort, and never how much you personally dislike the design.

| Label | Name | Meaning | Typical example |
| --- | --- | --- | --- |
| P0 | Blocker | Prevents or risks losing the core task; fix before ship | Primary action unreachable by keyboard; displayed total is wrong |
| P1 | Major | Causes errors, hesitation, or abandonment for many users | Errors surface only after full form submit |
| P2 | Moderate | Friction or confusion a determined user works around | Buried but findable guest-checkout link |
| P3 | Polish | Inconsistency or drift; a quality signal, not friction | Mixed corner radii across sibling buttons |

Rules for using the scale:

- P0 and P1 together should rarely exceed a third of the findings. If they do, force-rank until they do — "everything is critical" means nothing is.
- Severity is assigned per finding, then the report is ordered by it. Do not order findings by screen position; readers do not experience the report as a walkthrough.
- When unsure, downgrade rather than inflate. A wrong P0 burns the credibility the next report needs.
- A P0 that is cheap to fix is still a P0; effort is reported separately, never folded into severity.

### Severity calibration traps

- **The expert trap:** you know the product, so friction that would stop a first-time user doesn't stop you. Ask: what would someone on their first session do here?
- **The screenshot trap:** severity judged from a still image systematically overrates visual flaws and underrates behavioral ones. Behavioral probes (submit empty, double-tap, navigate back) find the P0s.
- **The loud-stakeholder trap:** whoever complained loudest about a feature pulls its severity up. Re-anchor every rating to the goal sentence.
- **The effort-inversion trap:** "but it's a two-line fix" quietly upgrades findings. Record effort in the fix line, never in the severity label.

## Evidence discipline

Findings stand on what is visible, not on what you assume happens behind the screens.

- Describe the element and its state: "the 'Continue to payment' button renders disabled on load," not "the button doesn't work."
- Use counts and measurements where possible: "11 distinct font sizes on one screen," "the order summary begins 320px below the fold on a 390px-wide viewport."
- When you cannot verify behavior — static screenshots only — mark the finding "assumed — verify in build" instead of inventing interactions.
- One concrete state reference per finding beats five paragraphs of prose. Attach the screenshot name or step where the evidence lives.

## Kind phrasing

Criticism only lands if it can be heard. Kindness here is precision plus respect — not softening until the finding is useless.

- Critique the artifact, never the person. "The form loses entered data on back-navigation," not "someone forgot to preserve state."
- Prefer observable language to judgment language: "the label disappears when the user types" instead of "lazy placeholder misuse."
- Every problem arrives with a fix. A finding without a recommended change reads as an attack; with one, it reads as a plan.
- Lead the report with two or three things that work and should survive the redesign. This is not a courtesy — it protects good decisions from being "fixed" later.
- No sarcasm, no humor at the artifact's expense, and no superlatives in either direction.

## Merging and deduplication

Raw observation lists always contain duplicates and chains of the same root cause. Clean them before rating severity:

- Merge observations that share one root cause into one finding, keeping the strongest evidence. Three notes about cramped spacing in different corners are one spacing finding with three evidence points.
- Split observations that bundle two problems ("the modal is ugly and unreachable by keyboard") into separate findings, each with its own severity.
- Keep the count honest. A 40-finding list is a backlog dump, not a critique: cap the delivered top list (12 findings for a five-screen flow is a working default) and move the remainder to a clearly labeled appendix.

## Prioritization logic

Order findings by severity first. Within one severity, order by breadth of user impact, then by how cheap the fix is relative to its gain — a P2 fixed with one line of CSS that removes a daily annoyance can justifiably outrank a P2 requiring a step redesign.

State the distribution in the report ("3 P0, 5 P1, 3 P2, 1 P3") so the reader sees the shape of the problem at a glance before reading a single finding.

## Working with disagreement

Critiques get challenged. That is the method working, not failing.

- When a stakeholder rejects a finding, ask which of the four parts they dispute: the evidence (checkable), the principle (citable), the severity (re-rankable against the goal), or the fix (negotiable). Most disputes are about the fix, which is fine — the finding stands.
- Offer to downgrade rather than to defend a label. A finding moved from P1 to P2 still exists and still ships in priority order.
- If disagreement persists about facts, it converts into an open question with a verification plan, not an argument.

## Report voice

- Declarative and specific: "the ZIP field opens an alphabet keyboard" — not "it might be worth looking at the keyboard situation at some point."
- Present tense for what is on screen, future tense for what the fix does.
- No hedging stacks ("perhaps possibly sort of"), no intensifiers ("absolutely terrible"), no passive constructions that hide the actor ("mistakes were made in the flow").
- The report speaks for the method; sign it with the review's date and inputs, not with opinions about the team.
