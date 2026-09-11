# Profiles

The eight profiles are the active layer of the system — the ones you load
into your agent harness when you have work to do. Each profile is a charter
(PROFILE.md) that defines exactly what it accepts, produces, and how it
operates.

---

## When to use each profile

### pathfinder (L1 — Orientation)

**Use when:** You have a vague idea, a messy directory, or a multi-part
request and need to figure out what you're actually asking. The pathfinder
scopes the work, maps what exists, and recommends which layer (and which
profile) should handle each piece.

**Example triggers:**
- "I have a bunch of notes from last week — what should I do with them?"
- "I need to start the Q3 project but don't know where to begin."
- "Can you look at ~/agentic-hub/ and tell me what's there?"

### steward (L2 — Stewardship)

**Use when:** You're about to do something with side effects (write a file,
modify a configuration, reorganize a directory) and want the agent to name
every effect before it happens. The steward enforces the consent-and-effects
principle for the whole system.

**Example triggers:**
- "Take today's meeting notes and save them in the project folder."
- "Rename all the files in the drafts directory to use YYYY-MM-DD prefixes."
- "I'm about to run a script that modifies several files — check the plan
  first."

### librarian (L3 — Knowledge)

**Use when:** You need to capture information, take notes, organize sources,
or get an answer from material you've stored. The librarian labels every
factual claim as source, evidence, guess, or unknown.

**Example triggers:**
- "I found a useful article about async Rust patterns — save it to my notes."
- "What does my notes directory say about deployment strategies?"
- "I need a citation for the claim that PostgreSQL handles 2000 writes/sec."

### waymaker (L4 — Planning)

**Use when:** You have a goal that needs decomposition into ordered steps
with clear done-criteria. The waymaker produces a plan, not a pile of work.

**Example triggers:**
- "I want to release a new version of my game's demo by November 1. What's
  the plan?"
- "I have a week to set up the analytics pipeline — break this into steps."
- "This project feels too big to start. Help me figure out what to do first."

### maker (L5 — Craft)

**Use when:** You have a clear, bounded piece of build work — prose, code,
designs, assets — and you want it executed within scope. The maker drafts,
iterates, and self-checks against acceptance criteria.

**Example triggers:**
- "Write a blog post about the new site launch — 1200 words, technical but
  accessible."
- "Implement the file upload component per the spec in
  `docs/upload-spec.md`."
- "Draft the investor update email for this month."

### critic (L6 — Review)

**Use when:** You have a finished unit of work (draft, code, design) and
want it verified against its criteria before calling it done. The critic
finds problems; it does not silently fix them.

**Example triggers:**
- "Review this pull request before I ship it."
- "Check this blog post against the quality checklist."
- "Is the maker's implementation of the upload component complete per the
  acceptance criteria?"

### herald (L7 — Delivery)

**Use when:** You have reviewed, passing work and need to prepare it for its
audience — format it, package it, add handoff notes. The herald prepares
publication but never publishes.

**Example triggers:**
- "Turn this reviewed report into a PDF with a cover page and table of
  contents."
- "Package this design system as a shareable ZIP with a README."
- "Format these release notes for the community blog."

### archivist (L8 — Continuity)

**Use when:** You're resuming a session, archiving a finished effort, or
need a status update on what's in progress. The archivist keeps work
resumable.

**Example triggers:**
- "I was working on the database migration last week — where was I?"
- "Archive the Q2 project — it's done and I want the notes preserved."
- "What's the status of everything in the hub scope right now?"

---

## How to switch profiles

Switch by loading the desired profile in your harness. The profile's PROFILE.md
(installed as SOUL.md in Hermes or as an agent file in Pi) defines everything
the profile needs to operate.

Do not switch profiles mid-task. Finish or explicitly cancel the current task
before loading a different profile. Profiles are designed for single-layer
work; switching mid-stream confuses the context.

## How to customize a profile

Each PROFILE.md has a Customization section (section 08) that tells you what
you can safely edit. Generally:

- **You may edit:** Voice examples, template preferences, custom failure
  mode additions.
- **Do not edit without understanding the whole fleet:** Layer binding,
  operating principles, input/output contracts, seam definitions.

If you change a profile's templates or voice examples, keep the changes
within the profile's charter — do not edit the contracts in `spec/`.

## Profile cross-reference

Profiles collaborate via named handoffs. No profile references another by
its internal directory structure; they use the eight public profile names:

| Reference name | Layer | Directory |
|---|---|---|
| pathfinder | L1 Orientation | profiles/pathfinder/ |
| steward | L2 Stewardship | profiles/steward/ |
| librarian | L3 Knowledge | profiles/librarian/ |
| waymaker | L4 Planning | profiles/waymaker/ |
| maker | L5 Craft | profiles/maker/ |
| critic | L6 Review | profiles/critic/ |
| herald | L7 Delivery | profiles/herald/ |
| archivist | L8 Continuity | profiles/archivist/ |

You can read any profile's full PROFILE.md to understand its contracts in
detail. The spec directory has the template (0004) that governs every
profile charter.