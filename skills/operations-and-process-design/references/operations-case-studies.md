# Operations Case Studies: Pixel & Ink Delivery Pipeline Redesign

This case study follows a two-person design studio, "Pixel & Ink," through a complete operations redesign of its client-onboarding and delivery pipeline. The studio's process was losing steps at every handoff, causing delayed revenue, missed deadlines, and client frustration.

## The Situation

Pixel & Ink consists of two partners: one creative director (CD) who handles client relationships, brief gathering, and creative direction; one production designer (PD) who does the actual design and asset production. Between them: zero structured processes, one shared email inbox, and a mounting number of clients who were not paying because, it turned out, because contracts signed meant invoices had not yet been sent.

### The Data Before Redesign

The partners had taken recent weeks documenting trouble:

- 4 of last 7 projects had a kickoff meeting before the signed contract was returned.
- 3 of 7 projects were started urgently without a creative brief. The designer had a verbal brief that changed twice after first round.
- 7 of 7 projects had no scoped tasks; the designer discovered a need for photography work or custom illustration only halfway through.
- 4 of 7 projects had missing assets at kickoff: two were missing the logo pack, one did not brand guidelines, and one did not have a request for product photography.
- Deposits collected: 3 collections on 7 contracts — meaning 4 projects started work with no payment. Average collection time was 18 days after contract signature.
- 2 of 7 projects had pricing that was established after work had started.

### Initial Interview Notes

**Maya (Creative Director)**: "I bring in client who needs something, tell PD, PD starts working, I trust them to handle it. Check-in only when the client asks. The billing, I have to chase them to produce an invoice and I'm not sure what to send for each job."

**PD (Production Designer)**: "I get a message: 'New project, client is Jane.' That's it. I have no brief, no timeframe, no budget. Half the time I just guess what she meant from the email thread and start designing."

This gap is typical: the loss of information at the handoff from the client-facing person to the executor.

## The Current-State Broken Process

The process map that the pair recalled and validated over two afternoons:

1. Maya gets referral or inbound lead.
2. Maya has conversation, builds rapport, mentions rough scope.
3. Maya sends a verbal or written "we will send you" in the email.
4. No proposal appears — engagement letter is not sent for weeks.
5. Client eventually asks for a proposal again.
6. Maya bills a hasty scope estimate now with a contract.
7. Maya sends contract — sometimes through a digital signature tool, sometimes email.
8. Client says "yes" but not return the officially signed contract.
9. Maya tells PD to start work because the client said yes verbally.
10. PD asks for assets; Maya pings client; assets trickle in over days.
11. PD designs first round.
12. PD sends the design to Maya; Maya forwards to client.
13. Client feedback goes through Maya back to PD.
14. At some point Maya asks about payment; client any payment is due.
15. Billing sends invoice; sometimes pays, sometimes does not because.
16. Project closes, no folder, no scope of progress or outcome.

### The Swidelane Map (Simplified)

**Lane: Maya (CD)**

Trigger → Lead arrives → Discovery email → Scope → Send contract (late) → Tell PD to start → Receive design → Send to client → Receive feedback → Request payment late → Project done.

**Lane: PD**

Wait for assignment → Get message ("Client X") → Ask for assets → Wait → Design first round → Send to Maya → Receive feedback chan → Adjust → Iterate.

**Lane: Client**

Express interest → Wait → Get contract → Ask again for contract → Respond verbally → Get reminders about assets → Send assets slowly → Review → Give feedback → Receive work → Invoice arrives after work is done → Pay late.

**Lane: Shared/Admin**

- No admin function.
- No system to drive the process.

### Step-by-Step Dropped Summary

| Problem | Root Cause | Impact |
|---------|-------------|--------|
| Contract signs but no invoice sent | No step that fires billing as transitional event | Revenue not collected for weeks or months |
| Work starts before contract | No gate enforces the contract before start. Condition: "work started" is "client said yes" verb average, not "signed contract is achieved" | Legal risk and revenue collection delay |
| Assets always arriving late | No check-in before start to ask "Do you have all the assets?" | Re-work and timeline slip |
| Feedback routing goes through Maya | Single person is the information conduit; no direct method to share | Maya's time gets wasted on medium cross-forwarding |
| No tracker per project | Each project lives in the email thread, no single location for the ticket | History of decisions lost steps |
| No record of kickoff done | No written checklist of what to cover | Standard process not really consistent |

## Root Cause Mapping

Three themes emerged:

1. **No explicit stage boundaries**. The process had no triggered state transitions. "Start work" is not attached to a prerequisite — it fires on a word-of-mouth signal that is unreliable.
2. **No handoff structure**. Going from client to CD to PD back to CD to client: each handoff reworded, summarized, or delayed.
3. **No inherent measure** — the time-to-invoice from contract signature was not tracked, so it was not visible as a problem.

## Redesigned Process

### New Flow

1. **Acquisition Stage (Maya)** → Inbound lead: qualified in 15 min discovery call. After the call, Maya returns to the studio and records call in a template.
2. **Scoping (Maya + PD)** →
   a. Maya gets the brief into a shared template.
   b. PD does a scoping estimate (1-hour review of the brief, included assets list, check format, stack, timeline).
   c. Maya sends proposal with scope and pricing.
3. **Contract + Billing (Admin)** → The proposal turns into a contract. Contract is signed as Docusign. Invoicing is sent: 50% required before kickoff, remainder on delivery. (Invoice is sent immediately after contract signature — no explicit manual step).
4. **Asset Checkpoint** → On contract signed + deposit in — Team requires that assets are owned or have confirmed access before kickoff. Send a checklist to the client with a list of 5 things. Due date: 5 days from contract.
5. **Kickoff (PD leads)** → Maya and have a 30-minute project internal start call, PD leads that day. PD sets up final. Deliverable: assets list confirmed, shared folder set up.
6. **Design Loop** → PD designs → sends to Maya for a review (1 round) → Maya sends to Client.

### Key Decisions

- Handoff gap: Contract → Invoice is now automated via the signing tool (trigger from signature → send invoice via QuickBooks). Eliminated the gap.
- Handoff gap: Kickoff is now a single step, not a string of ambiguous emails.
- Instance difference: Maya no longer routes the client feedback — they are copied but the PD communicates detail.
- The "scoping" step is a team step; both Maya and PD spend 1 hour to price and scope the job, this avoids the situation where PD is asked to design without a boundary.

### Checkpoints Added

After contract sent, after check of assets, after first deadline. At each point, the "next action" is written on a public slay.

## New SOP Excerpt: Client Kickoff (PD)

Written per the SOP in `templates/sop-template.md`:

**ONB-03**: Client Kickoff SOP

**Purpose**: This procedure covers launching a design project that has a fully signed contract and deposit collection, from the moment of the team is ready to start hands-on work.

**Prerequisites**: Signed contract, deposit received (check the bank), Assets checklist delivered to the client, date expiration for the assets is not passed.

**Procedure**:
1. Confirm that a project folder is created in the shared drive.
2. Place the signed contract and brief into the folder.
3. Create a new project card in Linear with the project name. In the description, attach the brief document; add labels for "Kickoff."
4. Add the 5 tasks that are the project scope from the brief.
5. Add the client to the signature tool for feedback.
6. Review that all assets are present in the folder (confirm with the asset checklist in the folder).
7. If assets are not complete, insert a "waiting on client" queue. Wait.

**Checkpoint** (use references/quality-management-basics.md Definition of Done):
- The project is in the workspace with 5 tasks defined in their ticket system.
- The project folder is on the internal drive, with contracts, brief, and asset list inside.
- They have confirmed the client's content review schedule.
- The project line has a predefined estimated hours and total scope.

## Capacity Note: The Two-Person Reality

The two-person team's capacity for design work is limited to a max of 3 concurrent projects. With 2 projects in production, the third project is booked through following month.

In the old process, capacity was not tracked. Both would accept work without knowing if they could do work simultaneously. The result: one partner accepted a full-lifecycle design for a new client, while the other was neck-deep—the second week of the production stage of previous commitments. Both felt the load.

In the redesign, they have a wall board that shows WIP items (safe-by-safe). At a weekly standup, 20 minutes, they process positive and negative requests. The no-go decision is made by:

- "If we said yes to the client now, how many projects are active?"
- "Is anyone available in the next 2 weeks?"
- "What would be at risk by saying no?"

The no is immediate, polite, and usually defer: "We can start that in late December. If yes, let's book now."

## Post-Redesign Metrics (After 2 Months)

- Average deposit collection time: dropped from 18 days to 4 days.
- Projects starting without contract: 0 of 6 (target: zero).
- Projects starting with missing assets at kickoff: down from 4 of 7 to 1 of 6.
- PD reported: 70% less "surprise" work during the design loop.
- Maya reported: "I have 1 clear hour a week to track pipeline status; the rest is not chaotic."

## Lessons for the Practitioner

This case study is typical of small-studio operations: missing artifacts, single points of failure in handoffs, ambiguous triggers. The work done here was done over 4 nights in total after hours: 2 nights to learn the current process, 1 night to design the new process, and 1 night to product the SOP and the map for the first pass. The improvements were immediate because the root problems were gap doers, not system architecture.

The main lesson: the biggest improvements come from adding ONE explicit state boundary (the contract deposit before work starts) and ONE tracking artifact (the project card). Both impose a discipline that makes other work simple.