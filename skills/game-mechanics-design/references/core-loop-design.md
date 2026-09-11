# Core Loop Design

Methodology for the repeating structures that make a game playable. The core
loop is what the player does so often it becomes the game: jump and stomp, draft
a card and fight a room, scan a vein and dig it. Mechanics live inside loops;
a mechanic that has no loop to live in is a gimmick. Use this file to design a
loop from scratch, to diagnose a loop that is not landing, and to size the
loops beneath and above the one you are editing.

## 1. Loop anatomy

Every loop, at any scale, has four parts:

1. **Verb** — what the player physically does (jump, draft, dig).
2. **Decision point** — the moment where two or more options are live and
   the choice is not free (which shaft, which card, which upgrade).
3. **Resolution** — the game's answer, ideally legible and immediate.
4. **Reward / state change** — what the player holds afterward that
   changes the next iteration (currency, knowledge, access, position).

Loops fail at the part you skipped. No decision point → the loop is a
chore with feedback. No legible resolution → the player cannot learn, so
mastery is impossible. No state change → the loop is a treadmill, and
players feel the belt.

A loop is *good* when its decision point is genuinely open (more than one
defensible answer), its resolution teaches (cause and effect are visible),
and its reward changes the next decision (not just a bigger number).

## 2. The 30-second loop

The smallest repeated unit. Name the verb, the decision, and the
resolution in one sentence each; if you cannot, the game's moment-to-
moment play is not designed yet. Test questions for any candidate:

- Does the decision repeat without going stale for at least 50
  repetitions (roughly 25 minutes of play)?
- Is the resolution readable without UI explanation after the third try?
- Does a skilled player resolve it measurably differently than a new one?

Escalation is the fix for staleness, not replacement: vary the inputs to
the decision (new enemy mixes, new vein compositions, new weather) rather
than adding a new verb every week. Verbs are expensive — each one needs
teaching, balancing, and UI. Escalating *parameters* inside one verb is
cheap.

## 3. The 30-minute loop

The session arc. A well-formed 30-minute loop has phases players can
feel: an **open** (a low-stakes setup phase that teaches today's state),
a **rise** (stakes and complexity climb), a **peak** (the moment the
session was for), and a **bank** (rewards tally, purchases happen, the
next loop is teased). The peak must actually peak: if every phase has the
same intensity, players cannot tell when to push or when to rest, and
sessions end at arbitrary points.

The bank phase is the most commonly skipped, and skipping it is the most
common reason a good action game has no retention: the player finishes
the peak and is dropped into the next open with nothing gained, nothing
chosen, nothing anticipated. Design the bank as deliberately as the peak.

Loop nesting: the 30-second loop runs inside the 30-minute loop; the
30-minute loop runs inside the meta loop (the campaign, the ladder
season, the collection). Each outer loop's reward must be purchasable or
expressed by the inner loop — a meta reward the moment-to-moment play
never touches is dead content on arrival.

## 4. Escalation patterns

- **Parameter escalation:** same verb, bigger/harder/faster inputs.
  Cheapest; saturates (a +10% enemy is invisible after ten levels).
- **Combination escalation:** known elements in new combinations (two
  enemy types that counter each other, forcing new decisions from old
  verbs). The workhorse of good action pacing.
- **Rule escalation:** a twist that bends a known rule (a floor that
  inverts gravity, a boss that must not be hit). Expensive per instance;
  spend rarely and teach instantly.
- **Player-power escalation:** the player's kit grows (double jump,
  new tools). Feels best, breaks balance fastest; gate it behind
  mastering the current kit or the game teaches helplessness.

Escalate at least two of the four in alternation. Escalating only
parameters yields a spreadsheet; only power yields a power fantasy with
no floor under it.

## 5. Diagnosing a loop that is not landing

Symptom → likely cause → first intervention:

- Players stop mid-session → no peak, or the peak was mispriced → re-
  structure the session arc before touching content.
- Players skip the new system → it has no decision point → attach it to
  a choice players already make daily, or cut it.
- Players grind without choosing → resolution rewards volume over
  decisions → price the smart route above the loud route.
- Sessions end at the same boring point → the bank phase is missing or
  flat → give the last minutes a tally, a choice, and a tease.
- New players quit in the open phase → the open has no hook → open with
  a decision, not an explanation.

## 6. Core loop checklist

- [ ] The loop's four parts are each writable in one sentence.
- [ ] The decision point has at least two defensible answers.
- [ ] Resolution is legible within three repetitions.
- [ ] The reward changes the next decision, not just a counter.
- [ ] The 30-second loop survives 50 repetitions in test.
- [ ] The 30-minute arc has a felt peak and a designed bank.
- [ ] Outer-loop rewards are spendable in inner loops.

## 7. Worked fragment

A hypothetical quarry-exploration game's 30-second loop, written to the
anatomy: verb — pilot the drill rig toward a glow on the scanner; decision
— spend drill heat on the deep vein (rare ore, rockfall risk) or the
shallow cluster (safe, common); resolution — the vein collapses or
yields, with the risk visibly telegraphed by cracks; reward — ore that
buys heat capacity, which widens tomorrow's deep-vein option. The
30-minute arc opens with a scan survey (cheap decisions teaching today's
map), rises through band depth, peaks at the mother lode call, and banks
at the surface depot where the haul is tallied and the next survey is
bought. The worked example in `../examples/worked-mechanic-design.md`
shows this loop receiving a new mechanic.