# Economy Case Studies

Two detailed case studies — one of a healthy economy and one of a collapsed
economy — drawn from professional experience. Use this file when stress-testing
a design against real-world failure modes, or when explaining to stakeholders
why a specific tuning decision matters. Names and details have been changed;
the dynamics are real.

## Case Study 1: Ember Realm (Healthy Economy)

**Game type:** Midcore fantasy MMO, three currencies (gold, reputation tokens,
premium gems). Free-to-play with cosmetic battle pass. Launched 2022.

**What went right.** The design team built a four-persona model (casual 1h/day,
midcore 3h/day, hardcore 6h/day, whale) before writing any code. The model
predicted a gold sink ratio of 0.88 at day 30 for the casual persona — slightly
inflationary, which is intentional to make the first month feel generous. The
hardcore persona showed 1.02 — nearly perfect equilibrium. Both were within
tolerance.

**The tuning story.** At launch, telemetry showed the casual gold sink ratio at
0.92 (model: 0.88, delta: 4.5%). Within spec, but trending the wrong way.
The team chose to add a small aspirational sink — a pet skin vendor — costing
500 gold. After the patch, casual sink ratio settled at 0.90. The move was
preventive, not reactive. The change was 8 lines of configuration and shipped
in a routine patch.

**The midgame test.** At month 4, a new zone introduced a secondary reputation
currency with its own shop. The team followed the one-currency-per-axis rule:
reputation buys horizontal expression only (cosmetics, titles, emotes), not
power. The gold economy was unaffected. The reputation economy was isolated and
easy to monitor.

**Long-term health.** At month 18, the sink ratio remained within 0.82-1.05
across all currencies. Wealth gap: 2.8x. No emergency tuning ever required.

**Why it worked.** The model was built and verified before the game shipped.
When reality diverged from the model, the team knew which lever to pull and by
how much. They never changed a lever by more than 10% in a single patch. They
added sinks before players felt the inflation, not after.

## Case Study 2: Void Engine (Collapsed Economy)

**Game type:** Sci-fi F2P looter-shooter, three currencies (credits, crafting
parts, premium tokens). Hybrid monetization with loot boxes. Launched 2023.

**What went wrong.** The team shipped without an economic model. The design
lead estimated progression curves from feel, adjusted numbers during alpha based
on forum complaints, and declared the economy ready. The first two weeks of
launch looked fine because new players were earning and spending freely. By week
4, the first warning signs appeared.

**The collapse sequence.**

Week 3: credit sink ratio hit 0.55. Players were earning faster than they could
spend. The team's response: added a new weapon tier that cost 50,000 credits to
upgrade — a single, large procedural sink. This was a mistake: a single sink
accounting for more than 60% of total spending creates a feast-or-famine cycle.

Week 6: the premium currency — purchasable with real money — could convert to
credits at a 1:100 rate. Whales began converting heavily. Credit supply
increased 300% in two weeks. Crafting part prices in the player market doubled.
Non-spending players could no longer afford basic crafting.

Week 10: the wealth gap hit 8.2x. The top 1% of players held 40% of total
credit supply. Casual players reported that the game had become unplayable
without spending. Forum sentiment shifted from "fun game" to "pay-to-win
garbage."

Week 16: monthly active users dropped 60% from peak. Revenue per user was
actually up — the remaining players were whales — but total revenue was down
because the player base had collapsed.

**Why it failed.** Six compounding errors: (1) no pre-launch model, (2) reactive
tuning that made things worse, (3) premium-to-soft conversion at a non-punitive
rate, (4) no sink ratio monitoring, (5) no wealth gap tracking, (6) the "add a
bigger sink" approach that concentrated spending rather than distributing it.

**Recovery attempt.** The team introduced a credit sink tax (5% on all market
transactions) and capped premium-to-soft conversion at 1:500. It was too late.
The player trust was gone. The game was sunset 14 months after launch with
under 5% of its peak player count.

**Lesson.** An economy that does not have a model before launch is not a
designed economy. It is a bet that every intuitive tuning decision will be
correct. Void Engine proved that the bet has a 90% chance of failing.