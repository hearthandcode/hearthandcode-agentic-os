# Worked Example: Pixel & Ink Client Onboarding Redesign

## Background

This is the worked example for the operations-and-process-design skill. It uses the same scenario as the case study in `references/operations-case-studies.md` but surfaces full intermediate artifacts: the broken process map as discovered, the dropped-step analysis table, the redesign decision log, and the revised swimlane.

---

## Artifact 1: Current-State Swimlane Map — "As-Is: Client Onboarding"

**Swimlanes:**
- Maya (Creative Director / Client Contact)
- PD (Production Designer)
- Client
- Shared / Admin (nonexistent)

| Step | Actor | Action | Output | Handoff | Defect? |
|------|-------|--------|--------|---------|---------|
| 1 | Maya | Receives lead email | Lead info stored in-person | — | — |
| 2 | Maya | Discovery call (verbal) | Notes mental-only | → nothing formal | No brief |
| 3 | Maya | Sends rough email | Scope text | → PD? not shared | Not shared with PD |
| 4 | Maya | Drafts contract | ea. contract | → Client | Delayed by weeks |
| 5 | Client | Says "yes" | Verbal verbal | ↑ Maya | No record |
| 6 | Maya | Tells PD "start" | Slack message | → PD | No trigger condition |
| 7 | PD | Asks "What's the client?" | Confused chain | — | Assets not listed |
| 8 | Client | Responds to request with assets | Zip / Google Drive link | → PD | Assets arrive late |
| 9 | PD | Designs first round | Design output | → Maya | No brief boundary |
| 10 | Maya | Forwards to client | Email | | Bottleneck |
| 11 | Client | Feedback | Email chain | → Maya | |
| 12 | Maya | Forwards feedback to PD | Rephrased | PD | Loss of detail |
| 13 | PD | Revisions | Design | → Maya | Loops past |
| 14 | Maya | Thinks about billing | Invoice | — | No schedule |
| 15 | Client | Pay — or not | | | |
| 16 | — | Close | Nothing | | No folder or review |

### Key Observations from Map

- Process has 16 steps but only 2 are executed by the receiver.
- Work sequentially has 2 serial handoffs: Maya → PD (4), PD → Maya (9), Maya → Client (10), Client → Maya (11), then back to PD (12).
- The performative of "contract signed" is on step 5, but step 6 triggers before the contract is fully executed.
- Step 7 is a bottle-neck: PD cannot begin until assets are held, but the asset man is not part of the process.
- Billing is step 14, in step 16. That is the largest gap.

---

## Artifact 2: Dropped-Step Analysis

| Step # | Step | Dropped Element | Root Cause | Impact |
|--------|------|----------------|------------|---------|
| 3 → 6 | Handoff: email to PD | No scope document, no timeline, no budget | The work order process is not defined; the contract is sent before the scoping step | PD cannot start without context |
| 5 → 6 | Verbal yes → started | Contract signature | No trigger-boundary between "pre-sales" and "revenue capture" | Projects start without signed contract |
| 5 → 14 | Contract signed → invoice | All invoicing steps missing | Process does not attach resources to step | Revenue delayed between 18 days |
| 6 → 7 | Kickoff | Asset list, brief, and schedule | Kickoff is not defined as a step | Re-work and delay |
| 10 → 12 | Review | Feedback format standardized | No agreed-upon feedback delivery mechanism | Maya becomes a rephrasing bottleneck |
| 14 | Billing event | No billing events | No step model of the process that triggers bill creation | Collection is random |

---

## Artifact 3: Target-State Process Map — "To-Be" Design

### Swimlanes (New)
- **Maya** — Client relationship, account strategy, scoping partnership, billing review.
- **PD** — Scoping partner (shared), design, schedule.
- **Admin** — (new role, provided by an automated tool or by Maya's Finance day) contracts, invoicing, deposit capture.
- **Client** — as before, but with clearer handoffs.

### New Flow

| # | Actor | Step | Type | Handoff | Control |
|---|-------|------|------|---------|---------|
| 1 | Maya | Lead → Discovery call | Activity | — | — |
| 2 | Maya + PD | Brief scoping session | Activity | Output → brief document | Template |
| 3 | Maya | Cost and timeline estimate | Decision | YES → Maya sends proposal; NO → Loop back to 2 | |
| 4 | Maya | Send proposal + contract | Handoff | Proposal → Client | Template |
| 5 | Client | Accept proposal | Decision | YES → step 6; NO → dead client | |
| 6 | Admin tool (auto) | Send deposit invoice (50%) | Auto | Invoice → Client | Triggered by Docusign |
| 7 | Client | Pay deposit | Event | Bank → Admin | Verify |
| 8 | Maya | Shop: send asset checklist | Handoff | Asset list → Client | Template |
| 9 | Client | Provide assets | Event | Files → Admin folder | |
| 10 | Maya | Confirm assets complete | Decision | YES → step 11; NO → delay | |
| 11 | Maya + PD | Internal Kickoff | Activity | Shared → portal | Checklist |
| 12 | PD | Design | Activity | — | WIP visible |
| 13 | PD | Send design for feedback | Handoff (direct to Client) | Design → Client feedback tool | |
| 14 | Client | Feedback via tool | Handoff | Feedback → PD | Asynchronous |
| 15 | PD | Final | Handoff | Final assets | — |
| 16 | Admin | Send final invoice | Handoff | Invoice → Client | |
| 17 | Client | Pay final | Event | Payment → Admin | |
| 18 | Maya / PD | Project close | Activity | Review, archive | Checklist |

### Change Highlights from Old to New

| Gone in New Process | Why |
|--------------------|--------------------|
| Verbal only "yes" triggers | Replaced by Docusign + deposit triggers |
| Maya forwards all feedback | PD and client communicate in shared feedback tool |
| Invoice sent after the project | Deposit now collected first; the final invoice is triggered at step 15 |
| No assets before start | Asset list enforces step 10; a "waiting on client" state tracks delay |
| No project folder | Shared project folder created before step 11 |

---

## Artifact 4: Revised SOP — Handoff from Contract to Kickoff (Risk Step)

**SOP ID**: `ONB-02`: Handoff from Signed Contract to Kickoff

**Purpose**: This procedure covers the phase between contract acceptance and the first design sprint. It ensures the deposit is collected, assets are availability, and scope is clear before any hands-on design work is started.

**Prerequisites**:
- Sheet created in the tool.
- Layout payment has been set up in QuickBooks.

**Inputs**:
- Signed contract via Docusign.
- Brief that was incorporated in the proposal.

**Procedure**:
1. When you get the Docusign notification "Contract completed," open the project in the CRM.
2. Label the project status as "Signed, Deposit Pending."
3. Notify to Admin tool (automation: triggers invoice for 50% deposit deposit).
4. Wait until the bank shows the deposit completed, or a manual account of the payment has been received.
5. If deposit has been 5 business days, send the reminder and ping the client.
6. When deposit is confirmed, send the asset checklist and then wait for the client to complete.
7. When assets are received (files in the project folder), confirm the assets are complete per the checklist from the folder name. If complete, mark the project ready for kickoff.
8. Move the project to the next stage of scheduling: a kickoff meeting call on the schedule.

---

## The Capacity Note for the Team

At launch, the team's available Weekly Free:

- Maya: 25 usable hours (40 less 5 for meetings, 10 hours context switching between client communication, billing, scoping).
- PD: 22 usable hours (12 full hours blocked for focused design on and a day divided with 2 projects at a time).

**Demand**: Each new project consumes 18 design hours plus 8 CDR hours which spread over 2 weeks.

**Capacity**: At 30 total hours of client work per week, the team can handle three projects at WIP simultaneously if interleaved.

**Booking Rule**: The third project does not start pending the closure of one of the current WIP. This is tracked on the shared view.

Now, the 21 target: team reserves 1 day a week of admin time every week (buffer = 5 HD Maya, 0.8 hours a week for PD) for "fine in the process" and responding to any accidental complexity.

---

## Decision Log

| # | Decision | Options Considered | Outcome | Rationale |
|---|----------|-------------------|---------|-----------|
| D1 | Enforce deposit BEFORE work | No deposit, Decouple from kickoff | Deposit before work | Remove billing risk at the end of the process |
| D2 | Use a tool for feedback | Maya relaying, shared feedback tool | Shared feedback tool (client portal) | Reduce cycling through intermediate person |
| D3 | Add scoping stage | Skip (add to Maya's call), charge for scoping, scoping is included | CD + CS session | Short is a data collection step, not a billable; blind deliver without a scope is wasteful |
| D4 | Create explicit "wait" state | Active work, no concept of queuing | Wait queue | Let the team know the client is not moving forward with an asset for a week |

---

## Post-Migration Baseline Check

After the changes were adopted for 4 weeks:

- 6 projects processed.
- 5 of 6 had all assets at kickoff.
- 5 of 6 had deposit collected before design work.
- 6 of 6 used the new SOP consistently.
- Average contract-to-invoice gap: 3 days.
- PD report: "Now reading the brief before starting means I have confidence about their overall expectation within the design sprint rather than guessing at the big picture."

This is the full worked example that the skill's Workflow section covers at a high-level. Use this document to understand the density of intermediate artifacts and pace from the broken current state to a clarified future state.