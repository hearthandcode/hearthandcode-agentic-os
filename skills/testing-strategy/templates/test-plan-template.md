# Test Plan — {{Module / Feature}}

> Fill every bracketed section. Delete guidance lines (italic) as you complete each.
> Keep the plan to the length the risk warrants: a two-page plan for a module, one page
> for a feature slice.

**Module:** {{name, owner, repo path}}
**Plan author:** {{name}} · **Date:** {{YYYY-MM-DD}} · **Status:** {{draft / in review / accepted}}

## 1. Context and quality goals

- **What this module does (2–3 sentences):** {{the behavior it owns, in product terms}}
- **Failure consequence:** {{what breaks, who notices, what it costs — money, data, trust, safety}}
- **Top quality attributes and why:**
  1. {{e.g., correctness under double submission — money}}
  2. {{e.g., contract stability — external consumers}}
  3. {{e.g., performance at P99 — user-facing latency}}
- **Explicitly traded away (sacrifice list):** {{what you are NOT testing and why — named, not omitted}}

## 2. Current state (zero or legacy)

| Question | Answer |
|---|---|
| Existing tests at this level? | {{none / count / directory}} |
| Existing seams (injectable deps, interfaces)? | {{list, or "none — seam work required first"}} |
| Test runner + layout convention | {{pytest / JUnit / vitest / go test; where tests live}} |
| CI today | {{what runs, on what trigger, how long}} |
| Known-flaky or quarantined tests | {{list or none}} |

> If there are **no seams**, list them as blocking work in §8 with an owner. Test plans
> do not survive untestable structure.

## 3. Module analysis

- **Behavior inventory** (one row per behavior — the plan's backbone):

| ID | Behavior / rule | Source (spec, code, ticket) | Risk (H/M/L) | Technique | Level |
|---|---|---|---|---|---|
| B1 | {{e.g., total = Σ items − discount − fees}} | {{spec §2.1}} | H | INV (invariant) | Unit |
| B2 | {{e.g., declined card → error shape E2}} | {{PSP contract}} | H | DT + EP | Integration |
| B3 | {{...}} | | | | |

- **State machines:** {{list lifecycles; attach the transition table if nontrivial}}
- **External dependencies:** {{name each; owned / third-party; how faked at each level}}
- **Shared mutable state:** {{databases, caches, singletons the tests must isolate}}

## 4. Level allocation

| Level | Scope here | Est. count | Runtime budget | Runs in |
|---|---|---|---|---|
| Unit | {{pure logic: pricing, validation, state}} | {{n}} | {{≤ 60 s total}} | Commit stage |
| Integration | {{boundaries: DB, PSP stub-peer, events}} | {{n}} | {{≤ 5 min total}} | Integration stage |
| Property | {{invariants: totals, idempotence, statefulness}} | {{k}} | {{≤ 1 min}} | Commit stage |
| E2E | {{money flows only, named}} | {{≤ 5}} | {{≤ 10 min}} | Nightly |
| Manual/exploratory | {{charter for the next release}} | — | — | Before release |

> The allocation must match the module type (see `references/testing-pyramid.md`).
> Justify any deviation in one line.

## 5. Case catalog (per behavior)

For each B-id above, list the cases the techniques generate:

| Case | Derives from | Input class / transition | Expected outcome | Level |
|---|---|---|---|---|
| C1 | B1 | {{cart ≥ $50, member, no coupon}} | {{10% discount}} | Unit |
| C2 | B1 | {{cart $49.99}} | {{no discount}} | Unit |
| C3 | B2 | {{PSP returns 503 twice, then 200}} | {{retry once, then surface E2}} | Integration |
| ... | | | | |

> Provenance matters: each case names the technique and class it covers (EP class, BVA
> edge, decision-table rule, illegal transition). A deleted case must name the class
> now untested.

## 6. Test data

| Concern | Decision |
|---|---|
| Builders/factories | {{module, location, defaults kept schema-valid}} |
| Named fixtures | {{which scenarios, where stored, review owner}} |
| Synthetic generation | {{needed? for what? distribution source}} |
| Production data | {{NOT USED, or anonymization pipeline + lineage reference}} |
| Secrets | {{dummy values only; real creds injected via env in E2E only}} |

## 7. CI stages and gates

| Stage | Contains | Trigger | Budget | Gate effect |
|---|---|---|---|---|
| Commit | {{unit + property + affected integration}} | Every push | {{≤ 10 min}} | Blocks merge |
| Integration | {{full integration, containers}} | Pre-merge | {{≤ 15 min}} | Blocks merge |
| Nightly | {{E2E + fuzz campaigns + mutation spot-check}} | Scheduled | {{≤ 30 min}} | Alerts |
| Release smoke | {{deploy health + top flows}} | Release RC | {{≤ 5 min}} | Blocks release |

- Flake policy: {{quarantine owner, re-entry criteria, retry policy}}
- Reporting: {{where failures surface; trend owner; escape-rate review cadence}}

## 8. Coverage and exit criteria

- **Behavior coverage:** {{n}} of {{m}} planned behaviors have cases — the exit metric
  (line coverage % is a secondary signal only).
- **Exit criteria for "tested":** all H-risk behaviors green at planned levels; all
  illegal transitions covered; {{any module-specific gates, e.g., reconciliation check live}}.
- **Deferred with owners:** {{behaviors consciously deferred — ticket, owner, date}}

## 9. Risks and open questions

| Risk / question | Impact on plan | Resolution needed from |
|---|---|---|
| {{e.g., PSP sandbox rate limits}} | {{E2E budget constrained}} | {{PSP account owner}} |
| {{e.g., no seam for clock in billing}} | {{timeout tests blocked}} | {{module owner — seam task B7}} |

## 10. Review checklist (for the reviewer of this plan)

- [ ] Every H-risk behavior has a named technique and level
- [ ] Illegal transitions enumerated, not just legal ones
- [ ] Allocation matches module type; deviations justified
- [ ] E2E tests each trace to a named flow and consequence
- [ ] Data section has no production-PII path
- [ ] Gates defined per stage; flake policy has an owner
- [ ] Sacrifice list explicit — nothing silently untested