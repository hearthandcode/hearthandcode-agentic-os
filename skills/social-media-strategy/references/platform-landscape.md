# platform-landscape.md — Platform catalog, roles, and effort economics

This reference backs workflow step 3 (platform scoring) and step 6 (formats). It is a catalog of durable platform mechanics, not a news feed: specific algorithms and feature sets change, but audience structure, format costs, and durability patterns move slowly.

## How to use this file

- Read the role taxonomy first; roles are the vocabulary the strategy uses.
- Use the catalog to seed the candidate shortlist, then score candidates against the user's actual segments, never against generic "best platform" advice.
- Price every kept platform in weekly hours using the effort-economics table; a platform without an hour cost cannot enter the plan.

## The role taxonomy

Every kept platform gets exactly one primary role. A platform with two roles is a platform with none.

- **Primary stage** — where the operator's main conversation and visibility happen; the account people are most likely to see first. Cost drivers: posting cadence and reply volume.
- **Community home** — where superfans and collaborators gather; slower content, faster conversation. Cost drivers: ongoing moderation and presence, not production.
- **Storefront and archive** — where the work lives and converts: product pages, devlogs, portfolios, changelogs. Cost drivers: page upkeep plus occasional long-form posts; highest durability of any role.
- **Watchlist** — a platform being mirrored to or monitored, deliberately without a cadence commitment. Cost drivers: near zero, but must carry a dated revisit trigger or it becomes silent sprawl.

Roles rank by operator value per hour differently per project: a shop with persistent pages may find the storefront role outearns the stage role at a fraction of the hours. That judgment is step 3's job; this file's job is to make the roles legible.

## Platform catalog (durable mechanics)

**Microblog feeds (short-post public timelines).**
Audience: real-time conversation, practitioners, press, curators. Formats: short text, images, short clips, threads. Economics: cheap per post, expensive in replies — the cadence is the iceberg's visible tip. Durability: hours; almost nothing posted survives the week. Best as primary stage for products with a story that unfolds in public.

**Long-form devlog and store pages (indie storefronts).**
Audience: high-intent buyers and readers who came to you. Formats: long posts, screenshots, builds, changelogs. Economics: expensive per post (an hour or more), cheap in upkeep. Durability: years; posts sit on the page where the purchase happens. Best as storefront and archive; the single highest-leverage role for products that sell themselves from a page.

**Video platforms (long-form).**
Audience: large, discovery-driven, search-persistent. Formats: edited video. Economics: brutal for a solo operator — multiple hours per asset. Durability: strong; search keeps paying. Verdict for small budgets: defer to post-launch, or convert long-form video into text-plus-clips for the primary stage.

**Vertical short video.**
Audience: very large, cold, algorithm-sorted. Formats: short vertical clips, trends. Economics: moderate per clip, but the cadence expected to compound is several per week, and results are high-variance. Durability: hours to days. Honest scoring: strong reach, weak fit for operators who dislike the format or cannot sustain the cadence; discomfort shows on camera.

**Chat communities (servers and groups).**
Audience: superfans, playtesters, collaborators. Formats: conversation, voice, events. Economics: low production cost, real moderation cost, and it never turns off. Durability: conversation is ephemeral, but relationships persist. Best as community home — usually opened deliberately (for example, when a demo ships and playtesters need a place), not before there are people to fill it.

**Professional and portfolio networks.**
Audience: industry peers, hiring, press. Formats: essays, milestones, hiring posts. Economics: one post per week is a reasonable cadence; posts reward polish over volume. Durability: days to weeks. Best as a secondary stage when the goal includes collaborators, funding, or press rather than players.

**Image-led communities (art-first feeds).**
Audience: visual-work lovers and artists. Formats: finished pieces, process shots, timelapses. Economics: driven by production of the art itself, which the operator owes anyway — often the cheapest "extra" platform for visual products. Durability: moderate; boards and tags persist. Best as a stage when the product is the image.

**Forums, subreddits, and topic boards.**
Audience: genre communities with strong norms against self-promotion. Formats: text posts, participation. Economics: reading and participating honestly is the cost; posting your own work requires existing standing. Durability: search-persistent. Best as watchlist-plus-participation; enter as a member, never as a marketer.

**Newsletters and RSS.**
Audience: the operator's own list — no algorithm between you and the reader. Formats: email, essays. Economics: one send per week or two; writing time only. Durability: the list itself is the asset. Strictly speaking not a social platform, but it is the most durable stage available and pairs naturally with a storefront role.

## Effort economics (the table that saves the strategy)

| Format family | Production cost per unit | Cadence needed to compound | Hidden cost |
|---|---|---|---|
| Short text post | minutes | daily-ish presence | replies are the real cost |
| Screenshot + caption | 10-20 min | 2-3 per week | choosing shots; none serious |
| Long-form devlog | 1-3 h | weekly or biweekly | nothing — it is the cost |
| Edited thread | 1-2 h | biweekly | research; links rot |
| Short vertical clip | 1-3 h | several per week | trend treadmill |
| Long video | 4-10 h | weekly to be seen at all | thumbnail/title craft |
| Community upkeep | 15-30 min/day | continuous | it never pauses |
| Listening pass | 15-30 min | 1-2 per week | reading time, not tooling |

Two rules fall out of this table and are worth writing into any strategy: reply time is part of platform cost, not a rounding error; and two platforms priced honestly with a listening block usually fill a solo operator's entire realistic budget.

## Format economics per role

- Primary stage formats: short text, screenshots, threads, clips — favor anything under 30 minutes per unit.
- Community home formats: conversation, events, playtest threads — favor presence over polish.
- Storefront formats: devlogs, changelogs, press kits, build notes — favor completeness over frequency.
- Watchlist formats: mirrors of the primary stage's outputs, zero incremental production.

## Durability and the compounding argument

Platforms differ in whether yesterday's work still earns tomorrow. Feed posts decay in hours; store pages, search-persistent video, and owned lists compound for months. The strategic implication: a small hour budget should keep at least one high-durability surface in the plan, because a presence made only of ephemeral posts must be rebuilt from zero every week. When scoring candidates, durability is the tiebreaker that most often changes the keep/drop call.

## Scoring rubric for step 3

Score each candidate 1-3 on:
1. **Audience fit** — do the user's ranked segments actually gather here, demonstrably?
2. **Format cost** — can the operator produce this platform's native formats at its native cadence for a price the budget survives?
3. **Durability** — does work posted here keep paying after the week it was posted?

Keep two or three platforms total, assign each exactly one role, price each in hours including replies, and cut immediately when the sum exceeds budget. Defer with a dated trigger; drop with a written reason. Both go in the decisions log.

## Anti-patterns this file exists to prevent

- The FOMO pick: adding a platform because it is discussed, not because a segment is there.
- The five-account blur: more platforms than the budget feeds, all at half effort, all reading as abandonment.
- The reply-blind budget: pricing posting time while ignoring the conversation the posts will generate.
- The permanence error: treating a defer or drop decision as final; every such call should carry its dated trigger or written reason.
