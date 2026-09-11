# Idea Evaluation Rubrics

## The Three-Axis Scoring Model

Every idea is scored on three axes that together capture its viability. Each axis uses a 1-5 scale.

| Score | Novelty | Feasibility | Fit |
|-------|---------|-------------|-----|
| 5     | The idea is genuinely novel; no good analogue exists in this domain | Can be done by the current team with current resources (expertise) within current capacity | The idea directly solves the brief's core challenge without secondary issues |
| 4     | Could be adapted, but the core is not widespread | Feasible with moderate stretch; a new partnership or tool needed | Minor adaptation needed, core fit |
| 3     | An interesting recombination of known approaches | Feasible, but requires significant effort; currently too costly or time-consuming | Fits the problem but fits poorly in brand/audience/match |
| 2     | Known approach in this domain; standard practice | Feasible only with large resources, expert support, or major process changes | The idea fits the brief but would compromise something important |
| 1     | Already exist in multiple forms; does not advance | Considered not be feasible in the current resource envelope | Does not fit the problem as briefed |

### Optional Fourth Axis: Impact

Add this when a clear measure of change is known in advance (engagement metric, cycle time, revenue):

| Score | Impact |
|-------|--------|
| 5 | Would redefined the category / create a new line of work |
| 4 | Would be a top 3 change for the organization if executed |
| 3 | Would be a material improvement (5-20%) |
| 2 | Would be a minor improvement (<5%) |
| 1 | Would not make a detectable difference |

## Weight Selection

Default weights: Novelty 30%, Feasibility 35%, Fit 25%, Impact 15%. Adjust for the session's purpose:

- If the brief is user-driven: Feasibility 40%, Fit 10%, Impact 20%.
- If the brief is exploratory: Novelty 45%, Feasibility 20%, Fit 20%, Impact 15%.
- If the brief is exploratory: Novelty 10%, Feasibility 40%, Fit 30%, Impact 40%.

Scoring: For each idea: (N + w_N) + (F + w_F) + (Fit + w_Fit) + (I + w_I).

## Anti-Pattern Flags

These flags override scoring. Any idea flagged with at least 1 is a candidate for removal or concurrent remediation.

| Anti-pattern | Signal | Action |
|---------------|--------|--------|
| Activates a known blocker | This idea will trigger compliance, legal, or approval by design | Flag as high-risk; include a desirability plan |
| The champion problem | One champion advocating for it and no one else | Score objectively; do not weight by support |
| Rebranded standard | The idea is a known practice you use every day | Apply a novelty score of 1-2; ask "is this an improvement?" |
| Too many dependencies | Team cannot ship without 3+ external partners | Requires a dependency roadmap |
| Scope creep | The idea is currently scoped in a way that prevents any other features | Must be trimmed to a smaller round |
| Surface fix | The idea addresses a symptom rather than root cause | Requires a root cause analysis first |
| Unfalsifiable | No way to test whether the idea works | Must be reframed as a testable hypothesis |

## The Score Threshold Method

1. **Score cutoff:** Apply the rubric to all ideas above the facility line. Remove those below a total weighted score of 2.5 (or adjusted to match your scale).
2. **The novelty line check:** If no idea scores > 4 in Novelty, you are in the "known solutions" zone, which may be acceptable if the brief calls for reliable, not novel. If it does not, you need to repeat divergence or use constraint flips.
3. **The feasibility floor:** If an idea scores below 3 on Feasibility, ask: "Can we reduce risk by scoping the first version to just a specific test?" If so, the idea stays. If not, and the score is ≤2, remove it.

## Documentation Template

For the shortlist, record each entry:

```
Idea name:
Novelty: X/5  Feasibility: X/5  Fit: X/5  [Impact: X/5]
Weighted score: ____
Anti-pattern flags: [none, ____]
Risk: [Low/Medium/High]
One-line summary: ____
Decision: [Select / Hold / Archive]
```