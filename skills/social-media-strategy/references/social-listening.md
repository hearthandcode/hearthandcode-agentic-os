# social-listening.md — Monitoring, sentiment, feedback into decisions

This reference backs workflow step 10. It carries the keyword method, cadence design, triage buckets with destinations, the escalation rule, and the route that turns findings into product and content decisions.

## What listening is and is not

Listening is a small, scheduled read of what people say about the product and its neighborhood, routed into decisions. It is not metrics review (dashboards own follower counts and impressions), not reputation scrolling (that is anxiety with a search box), and not a tooling purchase (free platform features — saved searches, list columns, store-page comments — are sufficient at this scale).

The budget is the constraint that keeps it healthy: fifteen to thirty minutes, once or twice a week, on the calendar as an appointment. Listening that grows past its budget is shrinkable in a defined order: keywords first, cadence last.

## The keyword list

Build the list once in step 10, review it quarterly:
1. **Product name and handle** — including the distinctive substring people will actually type (short names need the genre term attached; long names need their common misspelling).
2. **Product-adjacent terms** — genre descriptors and feature phrases a stranger might use without knowing the product exists.
3. **Peer titles and creator handles** — two or three works or voices with overlapping audiences; their comment sections are your segment's natural habitat.
4. **Exclusion terms** — the generic words that flood results (common English words, other products' names) filtered out to keep the pass inside its minutes.

Test the list by running one pass: if the first pass returns mostly noise, fix exclusions before fixing cadence — volume, not frequency, is the usual problem.

## Cadence design

- **Fixed slot**: same day and time each week (or two slots), because flexible listening becomes no listening.
- **Bounded reading**: the timer runs during the pass; unfinished items roll to next week rather than expanding the session.
- **One findings note**: a single dated document per session, appended — not scattered screenshots. Findability is what makes listening compound; an insight buried in a camera roll is lost.

## Triage buckets and destinations

Every item seen in a pass goes into one bucket, and every bucket has a named destination — feedback without a destination is entertainment:

| Bucket | Looks like | Destination |
|---|---|---|
| Praise | love for a moment, feature, or the feed itself | testimonials note; quoted (with permission) in launch materials |
| Questions | how does X work, when is Y | FAQ document; recurring questions become pillar content |
| Bugs | crashes, broken behavior, confusion | known-issues list; confirmed repro goes to the backlog owner |
| Feature asks | I wish it could... | backlog note, reviewed monthly; patterns outrank single loud requests |
| Sentiment drift | mood shifting around price, scope, direction | flagged in the findings note; surfaces at the monthly audit |
| Drama | pile-ons, call-outs, influencer conflict | escalation rule (below), then the crisis one-pager if it qualifies |

Buckets are fixed in the strategy so triage is classification, not judgment, at read speed.

## The escalation rule

Decide in peacetime what turns a listening pass into a crisis call:

- Default: an item is handled by its bucket.
- Escalate when **all** are true: the source is someone the operator does not know; the item is spreading beyond its original thread or being screenshotted; and the claim is about safety, deception, or conduct rather than taste.
- On escalation: stop, classify against the crisis one-pager's tiers, and follow its first-hour actions — the listening pass ends there.

The point of the rule is to move the decision from adrenaline to policy: drama gets classified once, in advance, instead of re-litigated every week with feelings attached.

## Feedback into product and content decisions

The route is monthly, written, and small:
1. **Collect**: the findings notes and bucket destinations accumulate during the month.
2. **Pattern**: at the monthly audit, read the month's items for patterns — the same question five times in public is a FAQ post; the same complaint three times is a known issue; the same ask twice a month is backlog evidence.
3. **Decide**: each pattern gets exactly one disposition — becomes content (a pillar post answers it), becomes backlog (routed to the product with the evidence), or becomes a written no (recorded with its reason so it does not return monthly).
4. **Close the loop publicly where cheap**: answering "this keeps being asked, so here is a post about it" is listening visibly working, and it teaches the audience that feedback lands.

## Sentiment, in honest terms

At this scale, sentiment is directional, not statistical: count the month's praise, questions, bugs, and asks; note whether the mix is shifting and why. Sentiment surprises worth flagging: affection for a feature that was almost cut (protect it), irritation with a choice the operator considers minor (investigate before defending), enthusiasm arriving from a community the strategy does not serve (a segment candidate for the next audit).

## The listening rubric (run in step 12)

- Keyword list covers product, misspellings, genre terms, and two peers, with exclusions.
- Cadence is a dated calendar appointment with bounded minutes.
- Every triage bucket has a named destination.
- The escalation rule exists and matches the crisis one-pager's tiers.
- Findings live in one dated note series, not scattered screenshots.
- The monthly route (pattern, decide, disposition) is written into the strategy.
- Metrics review is explicitly out of the listening pass.

## Anti-patterns

- **Dashboard creep**: the pass becomes an hour of impressions-refreshing; shrink the keywords, not the cadence.
- **Bucketless triage**: findings forwarded "somewhere" and lost; destinations are the deliverable.
- **Escalation by mood**: escalating because a critic was loud, while genuine spreading claims ride in the normal buckets; the rule exists to prevent exactly this inversion.
- **The orphan backlog**: feature asks collected monthly and never reviewed with the product's owner; listening that routes nothing is surveillance, not strategy.