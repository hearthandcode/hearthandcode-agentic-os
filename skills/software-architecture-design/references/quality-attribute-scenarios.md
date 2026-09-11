# Quality Attribute Scenarios — Performance, Modifiability, Security

A quality attribute scenario converts a vague requirement ("it must be fast") into a testable statement about the system. Scenarios are the load-bearing input to architecture: every boundary, style choice, and mechanism should trace to one. Without them, architecture debates are aesthetics; with them, they are engineering.

## The six-part scenario form

Every scenario has six parts. The first four come from the requirement; the last two are what you can verify:

| Part | Question it answers | Example |
|---|---|---|
| **Source** | Who or what generates the stimulus? | A signed-in user's web client |
| **Stimulus** | What happens? | Requests the note list |
| **Environment** | Under what conditions? | Normal weekday load, warm cache miss |
| **Artifact** | What part of the system is exercised? | The Notes component's read path |
| **Response** | What should the system do? | Return the list |
| **Response measure** | How is success measured? | p95 ≤ 300 ms server-side; ≤ 0.1% error rate |

A scenario missing the response measure is a wish. A scenario missing the environment will be relitigated under load conditions nobody agreed to. Write the full six parts for every scenario that will constrain the design.

## Performance scenarios

Performance is response time, throughput, or resource consumption under stated load. Common forms:

- **Latency:** "On checkout submit (source: shopper), during a sale with 3x normal traffic (environment), the payment path (artifact) confirms within 2 s p95 / 5 s p99 (measure)."
- **Throughput:** "The ingestion pipeline processes 10,000 events/s sustained with ≤ 2 s average lag."
- **Capacity:** "The system supports 5,000 concurrent sessions with the deployed instance count staying within budget; headroom is measured, not assumed."

Crafting guidance:

1. **Choose the percentiles deliberately.** p50 hides tail pain; p99.9 forces architecture changes. Median-only scenarios systematically hide the queueing behavior that breaks systems. Use p95 as the default contract, p99 where user-visible stalls are costly (payment, login).
2. **State the load the measure assumes.** "p95 under 300 ms" means nothing without the rps, data volume, and concurrency in force.
3. **Distinguish server time from perceived time.** A 300 ms server response can still be a 1.2 s page. If the scenario is about users, measure the user experience.
4. **Include a degradation scenario.** What happens at 2x the load? Graceful degradation (slower but stable) and collapse (errors, cascading failure) are different architectures.

## Modifiability scenarios

Modifiability is the cost of change — and the risk of the change breaking something else. The stimulus is always a change request; the measure is effort or blast radius:

- **Localized change:** "Product adds note-level ACL rules (source: product owner), changing only the Access module (artifact), with no changes to Notes or clients, in ≤ 1 day of work, verified by existing tests (measure)."
- **Extension:** "A new export format is added as a new module implementing the exporter port, touching no existing files (open-closed), shippable behind its own feature flag."
- **Portability:** "The primary data store moves from vendor A to vendor B by reimplementing the repository port; core logic untouched; a dual-write verification period proves parity."
- **Deletion:** "Feature X is removed by deleting its module and its rows in the feature registry — no dead references remain."

Crafting guidance:

1. **Name the change, not the quality.** "Maintainable" is untestable; "ACL rules change in one module in a day" is a design requirement you can check in review.
2. **The measure is where it hits the fan.** "≤ 1 day, no client changes" forces the boundary design. "Reasonable effort" forces nothing.
3. **Include the change you fear most.** The most probable future change should be the cheapest. List the three most likely changes for this system in the next year and write scenarios for them.
4. **Beware speculative flexibility.** Every extension point is a permanent tax. A modifiability scenario with no identified near-term change behind it should be challenged in review.

## Security scenarios

Security scenarios pair an attacker (source) with a protection the design must provide. The response measure is usually detection, resistance, or recovery:

- **Resistance:** "An authenticated user (source) submits a note ID belonging to another user (stimulus) via the API (environment); the system (artifact) denies with 404-equivalent semantics, writes an audit event, and never leaks existence (measure: no cross-tenant reads in the test suite's authz matrix)."
- **Detection:** "A credential-stuffing attempt (100 failed logins from one source in 5 minutes) triggers rate limiting and an alert within 1 minute."
- **Recovery / audit:** "For any note, the system can answer who modified it and when, for 7 years, in a query that returns in < 2 s."
- **Data protection:** "Note bodies are encrypted at rest with keys rotated quarterly; a snapshot of the database alone yields nothing readable."

Crafting guidance:

1. **Attack the boundaries.** Most security scenarios live at trust transitions: client→server, user→other-user's-data, component→component. Enumerate the trust boundaries first, then write one scenario per boundary.
2. **Authorization deserves per-resource scenarios.** "We do authz" is not a scenario. "A user cannot read a note they are not shared on, tested by an explicit matrix" is.
3. **Write the abuse case for every feature.** For each feature the product adds, ask "how would this be abused?" and make the answer a scenario — this is cheaper than retrofitting.
4. **Recovery is a security attribute too.** Detect, resist, *and* recover. An audit trail you cannot query is a decorative trail.

## Prioritizing scenarios

You cannot design for ten equally weighted scenarios. Prioritize by **cost of failure**, not by enthusiasm of the stakeholder:

1. **Grade each scenario:** what happens if this fails? Data loss or security breach (critical) > visible user pain (high) > internal friction (medium) > hypothetical futures (low).
2. **Keep 6-10.** More than ten scenarios in active conflict is a symptom you are designing a platform when you are building a product.
3. **Name the sacrifices explicitly.** For any quality not in the table, write one line: "we are not optimizing for X; revisit trigger Y." An unnamed sacrifice is a future incident.
4. **Re-derive on major changes.** When the product shifts (new client type, tenfold user growth, new compliance regime), the scenario table changes first, and the architecture follows or gets an ADR explaining why not.

## From scenario to mechanism

Every scenario in the final table needs a named design mechanism and a verification method:

| Scenario (abbrev.) | Mechanism | Verification |
|---|---|---|
| p95 < 300 ms note list | Read path indexes; pagination; cache | Load test at stated rps |
| ACL change in ≤ 1 day, one module | ACL isolated in Access module; policy port | Module dependency check + tests |
| Cross-user read impossible | Ownership check at read path; authz matrix tests | Suite with attacker-shaped cases |
| DB failover < 5 min, ≤ 5 min loss | Managed HA Postgres, synchronous standby | Failover drill, twice a year |

If the mechanism column is empty, the scenario is aspirational. If the verification column is empty, the scenario is a rumor. The architecture review (see `architecture-review-checklist.md`) checks both columns for every row.
