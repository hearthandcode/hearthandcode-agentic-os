# Critique Report — [Flow or Screen Name]

Metadata block: product, screens covered, date, reviewer, source of screens (design file / build / screenshots), viewport(s) reviewed.

## Goal capture

Goal sentence per screen (from the intake conversation):

- Screen 1: This screen exists so that [user] can [task], and success looks like [outcome].
- Screen 2: ...
- Screen 3: ...

Scope guard: what was explicitly in and out of scope for this critique.

## What works

Two or three things that work, with the same evidence discipline as failures. Name the pattern and why it works, so a redesign preserves it deliberately. A critique that finds nothing good is incomplete, not thorough.

## Severity scale

| Label | Name | Meaning |
| --- | --- | --- |
| P0 | Blocker | Prevents or risks losing the core task; fix before ship |
| P1 | Major | Causes errors, hesitation, or abandonment for many users |
| P2 | Moderate | Friction a determined user works around |
| P3 | Polish | Inconsistency or drift; quality signal, not friction |

Severity measures user impact, never implementation effort. Distribution: [n] P0, [n] P1, [n] P2, [n] P3.

## Finding format

Every finding uses this shape:

> **[P#] Title.** *Evidence:* what is on screen, where, in what state — specific and checkable. *Principle:* the violated rule, tied to its reference file. *Fix:* the concrete change, scoped to what the team can ship.

## Findings

[Ordered P0 → P3. Within one severity, order by breadth of impact, then by fix cheapness relative to gain.]

### [P0] Finding title
- **Evidence:** ...
- **Principle:** ... (see `references/[file].md`)
- **Fix:** ...

### [P1] Finding title
- **Evidence:** ...
- **Principle:** ... (see `references/[file].md`)
- **Fix:** ...

## Open questions

Unknowns and verification gaps — no severity, prompts for the team:

- [Behavior that could not be verified from static screens — "verify in build"]
- [Missing context — analytics, platform constraints, prior research]
- [Decisions the team must make — e.g., whether a promo stays on a task screen]

## Assumptions

What you had to assume because the requester did not specify it: intended audience, devices, whether a dark theme exists, whether the flow is live or a prototype. Assumptions stated are revisable; unstated ones become silent errors.

## Appendix

Additional findings below the delivered top list (keep the delivered list honest — 12 findings for a five-screen flow is a working default). Each entry in the same finding format, labeled by severity.