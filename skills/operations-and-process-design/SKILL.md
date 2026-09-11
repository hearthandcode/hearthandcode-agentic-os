---
name: operations-and-process-design
description: Use when a team, project, or business function lacks reliable workflows, loses steps in handoffs, has no documented process, or needs a delivery pipeline diagnosed and redesigned. This skill produces process maps, SOPs, capacity plans, quality checkpoints, and a continuous improvement cadence that together turn irregular operations into predictable, measurable work.
---

# operations-and-process-design

## 01 — Purpose

Every team of any size runs on processes. Some are explicit and reliable. Most are implicit, inconsistent, and frayed at the handoff boundaries between people, tools, and stages. This skill provides a structured method for finding, fixing, and sustaining processes that consistently deliver output.

The skill does three things.

First, it surfaces the gap between the documented process and the actual behavior. When two people describe the same workflow differently, a reliable process does not exist. The mapping and interview techniques in this skill expose the real pattern, including shadow systems, workarounds, and errors that someone absorbs silently. The practitioner learns to observe instead of ask, and to track instead of speculate. The gap between what the team says they do and what they actually do is where the most valuable design insight lives — every undocumented shortcut is a candidate for formalizing, and every unacknowledged error is a design target.

Second, it produces a process that outlasts the person who designed it. The reference files encode proven craft patterns:

- Swimlane maps that show who does what at a glance. The map becomes the single source of truth for who owns each step — ending the "I thought you were doing that" conversations.
- State models that make bottlenecks and wait states visible. Every wait state is drawn and named, so the team can see where time is lost between steps.
- SOPs that produce correct results from a newcomer on the first attempt. The SOP is validated by the newcomer test from `references/sop-authoring.md`, which guarantees that any competent person can execute the handoff without asking for help.
- Capacity planning that prevents overload before it occurs. The capacity note from Step 8 ensures the team knows whether the process fits their bandwidth before they commit to it.
- Quality management that catches escapes at the handoff, not the client. Inspection points at the highest-risk handoffs prevent defects from reaching the client, where they become expensive to fix.

The output is a package of maps, procedures, and checklists — not a suggestion memo. Every artifact in the package has a testable quality criterion: the map must include exception paths, the SOP must pass the newcomer test, the capacity note must be numeric, the risk register must have named owners, and the transition plan must have calendar dates. If any artifact fails its quality criterion, the package is not complete.

Third, it installs a lightweight improvement mechanism that runs without the designer present. Every process degrades under normal use. The skill encodes:

- A cadence for retrospectives defined in `references/continuous-improvement.md`.
- The discipline of one change at a time: precisely one structural change between measurement periods, so the effect is attributable.
- A measurement habit tied to the process metrics — cycle time, handoff latency, and escape count — defined in `references/quality-management-basics.md`.
- The transition plan in the skill's deliverable includes a named first retrospective date so improvement is not deferred.

The team acquires a process plus a habit of maintaining it.

Process design operates at three levels of maturity. At level one, the work sees consistent output: the same steps in the same order, every time. At level two, the process is measured: cycle time, handoff latency, and escape count are tracked, and their trends are visible. At level three, the process improves: each retrospective changes exactly one thing, and the measurement system confirms whether the change moved the needle in the right direction. This skill delivers level one for a single process and leaves the measurement hooks for level two and three. The reference files provide the method for each step up the maturity ladder.

Teams that have never had a written process will often skip directly to level two — they want metrics to prove the process works — but the skill's workflow is designed to build level one first. A process that is not consistent cannot be measured meaningfully, because the variance across cycles masks any signal in the metrics. The skill's nine-step workflow produces the consistency artifacts (maps, SOP, capacity note) before it installs the measurement system, ensuring the team has something stable to measure.

This skill addresses teams from a solo practitioner up to about twenty people. The same handoff analysis, state guards, and SOP review apply across that range. Beyond twenty, add dedicated operations staff before adding more process.

The skill's workflow is designed to be self-contained: the practitioner does not need external tools beyond the templates provided. A process map can be drawn on a whiteboard, an SOP can be written in a text editor, and a capacity note fits on one page. The method works before the automation is in place. This is deliberate — the method must survive the gap between the design phase and the tool-implementation phase.

The skill assumes nothing about your industry. The scenarios in `examples/worked-process-design.md` are fictional composites, but the mechanics — observing work, defining handoffs, gating state transitions, sizing capacity — transfer unchanged between a design studio, a clinic's front office, a construction firm's estimating team, and a software support desk.

The boundary of this skill is intentionally narrow. It covers linear and lightly branching workflows: an order is placed, an intake is processed, a ticket is resolved, a design is delivered. It does not cover recursive decision-making (policy drafting, strategic planning), open-ended discovery (creative ideation), or high-variance processes where each work item follows a different path (incident response, emergency medicine where each case is unique). For those domains, the mapping technique still applies, but the target design must account for the fact that the trigger and end state may be the only common elements across work items. The skill's workflow can still produce a current-state map and a dropped-step analysis for high-variance processes, but the target design will have fewer prescriptive paths and more decision points guiding the operator through each branching case.

What this skill is not: it does not manage the work for you, does not pick your tools, and does not contain every judgment in checklists. It produces the things that make judgment possible — shared maps, written procedures, and honest arithmetic about what the team can actually carry. The skill gives you the framework to make better decisions about how work flows; it does not take the decisions away from the people who do the work.

**The specific outcomes this skill owns:**

1. **A current-state and target-state swimlane map** showing roles, functions, decisions, handoffs, and wait states. The map is the shared reference the team negotiates from. Notation follows `templates/process-map-template.md` and the quality checklist in `references/process-mapping.md`.

2. **A documented list of dropped steps** with root causes drawn from a controlled list: missing trigger, missing handoff element, misordered step, missing acceptance criteria, unassigned ownership, capacity gap. Each row includes severity and traces to a specific fix in the target design.

3. **At least one SOP for the most critical handoff**, guaranteeing that the designated part of the process is performed consistently, with defined start and end conditions, and validated by the newcomer test from `references/sop-authoring.md`.

4. **A documented process package** containing pending SOPs, a definition of done for each state, and a capacity note stating whether the process fits the team's current bandwidth.

5. **A lightweight operations cadence** including inspection points at handoffs, defect feedback loops, retrospective timing, and an owner for every process state.

6. **A written transition plan** that schedules the switch from old process to new process across four weeks, with a test run, a parallel-run phase, a full-switch date, and a first retrospective date.

7. **A risk register** specific to the redesigned process, with likelihood-impact scores, mitigations, and named risk owners for each identified category.

## 02 — When to Use / When Not to Use

Apply the skill when you recognize one of these patterns in the team's operations.

### Use this skill when:

1. **A critical task was missed at least once in the past month, and the cause was not workload.** The task is known, but no control prevents its omission. The design intent is to add that control: a checkpoint that must be acknowledged, a handoff that must be accepted before work proceeds, or a state that enforces the step before exit.

2. **Work crosses more than two people before the final state.** Every handoff consumes information, reorders priorities, and drops detail. The skill formalizes handoff analysis around the six-part model: sender, receiver, token, acceptance criteria, trigger, feedback. Each missing element is a named gap with a named fix. For example, if a client brief crosses from CD to PD with no acceptance criteria (what "good" looks like), PD designs from guesswork. The fix is adding a confirmation step at the handoff.

3. **Someone asks "is it done?" and the answer is "I thought you were handling that."** The receiver never learned the token was passed. This is the most common handoff defect in small teams. The skill forces explicit notification at transfer, and receiver confirmation before the work is considered handed over. The trigger for the receiver's next step is not "sender said so" but "receiver confirmed the artifact."

4. **A precondition document arrives after the step it enables has already started.** The deposit invoice arrives after work begins. The brief is written after the prototype ships. The skill imposes state guards: the next step does not trigger until the prior condition is verified true, and the guard is a named state, not a good intention. A state guard replaces "we will remember to check" with "the system checks before the step activates."

5. **Work is accepted without a shared written statement of the deliverable.** A verbal scoping conversation plus a "looks good" reply is not scope. The skill forces a written artifact produced at scoping, and explicit confirmation from both sides before design work starts. Without a written scope, revision cycles are unbounded because there is no reference point for what was agreed.

6. **The same type of defect appears across two projects.** One incident is a mistake. Two identical incidents mean an inspection point is missing or ineffective. The skill traces the path backward through the map, finds where the inspection should have caught it, then makes that inspection effective. Repeat defects are the strongest signal for a process design intervention.

7. **A new team member needs weeks to become productive because the process lives in someone's head.** The skill converts tacit knowledge into written form: maps that show the flow, SOPs a newcomer can execute, definitions of done that remove guesswork. A process that cannot be learned from documents alone is a single point of failure.

8. **The team's tools changed but the process did not adapt.** A new billing system, a new project tracker, or a new shared drive changed the tool surface while the workflow still follows the old path. The skill maps which functions the tool is performing, which old steps are no longer needed, and which handoffs need to change shape around the new tool.

### Do NOT use this skill when:

1. **The need is business strategy, goal-setting, or policy.** Those skills live elsewhere. Operations design assumes strategy exists — it designs how the work flows, not what work to do or why. Use `strategic-planning` for strategy work.
2. **The bottleneck is software structure, data architecture, or system design.** Use `software-architecture-design` when the problem lives in code or infrastructure, not in how people move work between each other.
3. **The need is a test plan, test infrastructure, or coverage analysis.** Use `testing-strategy`. This skill designs the workflow — how work moves between people and what quality checks exist at handoffs — not the product verification of that workflow.
4. **The need is creative exploration — a product name, a campaign concept, a visual direction.** Use `brainstorming-and-ideation`. This skill prescribes structure, which hinders divergent creative work.
5. **The process already works.** No missed steps, no recurring defects, no handoff confusion, no capacity strain. Do not add overhead to a functioning system. Process design has a cost: maintaining maps, reviewing SOPs, running retrospectives. Apply it only where the cost is lower than the defect cost.
6. **The request is to document for compliance with no intent to change behavior.** A shelf document signed off by a consultant is not an operation. Without a transition plan and a 30-day review, the deliverable produces no change.
7. **The root cause is clearly a single person's performance, not a systemic gap.** If one person consistently fails at a task that everyone else performs correctly, the fix is coaching, not process redesign. Process design addresses systemic defects that appear regardless of who holds the role.

## 03 — Inputs and Outputs

### What the User Must Supply

The practitioner gathers these before the skill produces reliable results.

**Scope sentence.** One sentence containing the trigger event and the end state.

- Trigger must be observable: "a prospect submits the intake form" not "a client is ready."
- End state must be a measurable condition: "the invoice is paid and the project folder is archived" not "it wraps up."
- If the scope needs a conjunction to hold together, narrow it. One sentence only.
- Write the scope sentence before conducting any interviews. It is the filter for what to include and what to leave out. Every step that does not fit between trigger and end belongs in an adjacent process, not this one.
- The scope sentence is also the contract with the sponsor. If the sponsor later asks why X was not covered, the sentence is the answer.

**Role access.** One representative from each role in the process.

- Interview individually. Never in a group — groups defer to the most senior person.
- Ask each person to trace a real recent work item, not an ideal.
- If a person is unavailable, examine the artifacts they produce.
- Each interview follows a consistent structure: (1) ask the person to name their first step when a new item arrives, (2) ask what they produce and who receives it, (3) ask what they wait for and from whom, (4) ask what they do when something goes wrong, (5) ask what they wish was different. The five-question structure covers the full handoff model without leading the witness.
- Record verbatim. Your own paraphrasing of someone's process loses detail.

**Observation access.** Permission to follow one real work item from trigger to end.

- Recall skips friction. Observation finds it.
- Record waits, exceptions, shortcuts, and any piece of informal handoff.
- The observer does not intervene. Capture exactly what happens, including deviations.
- Observation is more valuable than interviews. One traced work item reveals more about the actual process than three hours of conference-room discussion. The observer's role is to notice what the participants no longer see: the extra step someone takes, the workaround they do not mention, the silence when a handoff fails.

**Capacity estimate.** The team's available person-hours per week per role.

- Precision is not required. A number is required.
- Exclude meetings, admin, and lunch from the estimate.
- Example: "CD gives 25 h/wk for project work after internal overhead. PD gives 22."
- If the team cannot produce a number, ask them to track for one week. A week of honest tracking provides better data than a conference-room estimate and avoids the optimism bias that plagues capacity planning.

**Optional documentation.** Existing SOPs, checklists, templates, older maps.

- Treat these as unreliable history — not ground truth.
- The divergence between documented intent and actual practice is a design target.
- A documented process that no one follows is a liability: it creates the illusion of control. The practitioner's job is to discover why the document and the reality diverged, and to design something that works in the real environment.

### Prerequisites and Constraints

- **Time.** The full workflow takes one to three working days for a small process: roughly half a day per interview, half a day of observation, two days of design and writing. A rushed map is a wrong map. The interviews alone require scheduling with each role; observation requires an uninterrupted block with one real work item. If the practitioner has less than one uninterrupted day, defer the observation phase — it is the step that most directly prevents Failure Mode 1 (map does not match reality).
- **Authority.** Someone who can change how work flows must sponsor the redesign. If no such person exists, document the current state truthfully, but the target design will not be adopted. The sponsor does not need to be a manager — a senior individual contributor who owns the process and can make changes is sufficient. The key test: can the sponsor say "we are doing it this way now" and have the team follow?
- **Stability.** The process being mapped should be in regular use. A quarterly process cannot be observed during a single session; reconstruct from several historical work items and flag the lower confidence. For low-frequency processes, supplement observation with artifact analysis: email threads, meeting notes, and project tracking records from the last three occurrences.
- **Team buy-in.** The team must understand that the redesign is about systemic improvement, not performance review. If the team fears that mapping their process will expose individual failures, they will describe the ideal process instead of the actual one. Frame the effort as defect analysis, not personnel evaluation. Use the language of the dropped-step analysis table — paths and states, not people and mistakes.
- **Tool access.** The practitioner needs read access to the tools the team uses: project tracker, billing system, shared drive, communication platform. Every tool used in the process should be visible during observation. A tool that the practitioner cannot see is a source of hidden handoffs.

### What Good Inputs Look Like

A well-prepared client provides:

- **A clear trigger event.** "When the intake form is submitted" is a good trigger. "When we get a new lead" is vague — there may be multiple lead channels with different processes. Narrow to one channel.
- **A clear end state.** "When the invoice is marked paid and the project folder is archived" is a good end state. "When the project wraps up" is vague — wrapping up may mean different things to different roles.
- **Role clarity.** "We have Maya (CD) and Jordan (PD)" is better than "We have a team of two." Knowing each person's role and their approximate allocation (hours per week) is essential for the capacity note.
- **Artifact access.** Email threads from the last completed project, the project tracker history, the billing records. The more historical data available, the more baselines the capacity note can draw from.

If the client cannot supply any of the above, proceed anyway — every gap in the inputs is diagnostic. A client that cannot name their trigger or end state has a scope problem before they have a process problem, and that discovery is itself a useful output. The practitioner documents the missing input as a risk in the risk register and adjusts the capacity note's confidence level accordingly. A capacity note built without a capacity estimate (because the team could not provide one) is flagged as "low confidence — estimate within ±40%."

### What the Skill Produces

1. **Current-state swimlane map.** Role lanes, steps, decision diamonds with labeled outputs, exception paths, rework loops, wait states. Title, version, date on the map. Minimum 8 steps, maximum 25 per page. Notation conventions in `templates/process-map-template.md`. The map is the shared reference that the team negotiates from — disagreements about what currently happens are resolved against the map, not against memory.

2. **Dropped-step analysis table.** One row per defect. Columns: step number, expected output, actual result, gap description, root cause from the controlled list (missing trigger, missing handoff element, misordered step, missing acceptance criteria, unassigned ownership, capacity gap), and risk level (low/medium/high/critical). This table is the design agenda for everything downstream. Every row in the analysis table generates at least one change in the target design. Use `references/process-mapping.md` for the root cause taxonomy.

3. **Target-state swimlane map.** Same notation as the current-state map. Step count no more than 20% over the old map. Every handoff defines all six parts: sender, receiver, token, acceptance criteria, trigger, feedback. Each change on the map traces to a specific row in the dropped-step analysis table — no change without a defect behind it. The target map is validated against the capacity note before finalization.

4. **One SOP for the highest-risk handoff.** Covers exactly one handoff from start condition to end condition. Validated by the newcomer test described in `references/sop-authoring.md`. Format from `templates/sop-template.md`. The SOP is the most actionable deliverable — it is the only artifact that a team member follows step by step.

5. **Capacity note.** Team capacity per role per week, process demand per work unit, expected weekly volume, demand-to-capacity ratio, a buffer of 15–25%, and when the ratio exceeds 1.0, the explicit decision about which work stalls. Method from `references/capacity-planning.md`. The capacity note is numeric — no qualitative statements like "the team is busy."

6. **Risk register.** Table with risk name, likelihood (1–5), impact (1–5), mitigation strategy, and named owner. Format described in `references/quality-management-basics.md`. The risk register is a living document that the team updates at each retrospective.

7. **Transition plan.** Four-week rollout schedule: test one item in week 1, switch the highest-risk handoff in week 2, all new work in week 3, first retrospective in week 4. Written on a shared calendar with named owners and dates.

## 04 — Workflow

Proceed in order: discovery, analysis, design, implementation. Each step names the governing reference and closes with a checkpoint question.

### Step 1 — Define the process boundary

Write one sentence: "When [trigger] occurs, the process runs until [end state]." The trigger is observable. The end is a verifiable condition.

- **Reference:** `references/process-mapping.md`, scope section.
- If the sentence contains "and then," "or," or "unless," the scope is too wide.
- Make note of adjacent excluded processes so scope creep has a written boundary.
- Example for the Pixel & Ink scenario: "When a prospective client makes first contact, the process runs until the final payment is received and the archived project folder is complete." This excludes pre-sales marketing and post-hoc portfolio review.
- If the team cannot agree on the one-sentence boundary, pause and negotiate. The process design should not proceed from disagreement.
- The boundary sentence also identifies the adjacent processes that are not being redesigned. In the Pixel & Ink case, the excluded adjacent processes are lead generation (pre-trigger) and portfolio management (post-end-state). Document these adjacent processes and state explicitly that they are not in scope. This prevents the scope from creeping during Step 6 when someone suggests adding a step that properly belongs to a different process.
- **Checkpoint:** "Can you name the exact trigger and end state in one sentence with no extra clauses?"

### Step 2 — List the actors and assign lanes

Record every role that touches the process: people, systems, external parties. Each becomes a swimlane.

- Use role names, not personal names. People leave; roles persist.
- A tool that performs a step automatically gets its own lane.
- **Reference:** `references/process-mapping.md`, actor identification section.
- **Template:** `templates/process-map-template.md`, Section 2 — Actors / Roles.
- A tool that runs unattended (an email auto-responder, a signature portal) is a lane. A tool that a human operates is not a lane; the human is.
- When the same person fills two roles, keep two lanes and merge only at the drawing stage, labeling each step with its role. The dual role is a structural risk — the design must not hide it.
- List the actors in order of their first appearance in the process. The top lane should be the role that performs the first step. This makes the map read naturally from top to bottom and left to right.
- External parties — clients, vendors, regulatory bodies — are real actors that control the flow. They get lanes. If the client is a source of waiting time, the client lane makes that waiting visible.
- **Checkpoint:** "If each person in a lane was replaced tomorrow, would the lane label still hold?"

### Step 3 — Walk the work with one real example

Follow one real work item from trigger to end state. Record each step: what the actor did, what triggered it, what it consumed, what it produced, where it crossed lanes.

- **Reference:** `references/process-mapping.md`, "Finding the Real Process" — observe first, ask after.
- Use the six-part handoff model as a live checklist: for every lane crossing, ask "who sent it, who received it, what was the token, what were the acceptance criteria, what triggered the transfer, and what feedback confirmed receipt?" If any answer is missing or vague, that handoff is a candidate for the dropped-step table.
- Record the informal side channel: chat messages, verbal agreements, anything outside the formal path. The informal channel is where work actually moves. The formal channel is where it is logged. When the two diverge, the map shows the informal path and flags the divergence.
- The walk is not done until the item reaches the end state or is abandoned. Abandonment points are still data. Record why the item was abandoned: did the client withdraw, did the scope exceed the budget, did the team decide the project was not viable? Each abandonment is a design target for a gate that should have been earlier.
- Ask each actor to reconstruct the item chronologically from the artifacts they touched, not from memory: emails sent, tickets created, files saved. Artifacts do not exaggerate. A person who insists they always send a signed contract will produce a signed contract artifact for the traced item, or the artifact will reveal the gap.
- For each step, ask one diagnostic question: "How did you know to do this, and how did you know it was done?" The first answer names the trigger; the second names the acceptance criteria. Missing answers become dropped-step rows.
- Build the handoff table in parallel: for every lane crossing, record sender, receiver, token, acceptance criteria, trigger, and feedback channel. Use `references/workflow-design.md` for the full six-part specification.
- Collect at least one wait time measurement for each wait state identified. Even an approximate duration ("about three days") is useful. If the same wait state appears in multiple items, the median wait time becomes the baseline for the redesign.
- **Checkpoint:** "Does this match what happened to a real work item or what the team says should happen?"

### Step 4 — Draw the current-state map

Place each step in the actor's lane. Connect with arrows. Add decision diamonds with two labeled paths. Note handoff lines crossing lane boundaries and wait states.

- **Reference:** `references/process-mapping.md`, swimlane layout conventions.
- **Template:** `templates/process-map-template.md`, Section 5 — Step Inventory.
- Every decision diamond must have a YES output and a NO output. A diamond with one output is not a decision. The NO path leads to a loop back, an exception handler, or a termination state. If the process does not specify what happens when the answer is no, the process is incomplete.
- At least one exception path or rework loop. If none appears, return to Step 3 and ask about the worst work item of the last month. The worst item always contains a decision that tested the process and an exception path that the team used.
- Wait states are drawn as a distinct shape or annotated explicitly: "Waiting on client assets," "Waiting on deposit." Every wait state without a named trigger to exit it is a defect waiting to become a dropped step. The trigger can be a calendar date, a notification, or a manual check — but it must be written.
- Check the map against the trace: every artifact observed in Step 3 must appear as an input or output of some step. An artifact that appears in the trace but not on the map is a hidden handoff. A hidden handoff means the trace is more accurate than the map, and the map must be adjusted to match the trace.
- Use the process map quality checklist in `references/process-mapping.md`. This checklist tests each map element against a standard: are all lanes labeled? Are all arrows directional? Are all decision diamonds binary? Is there a legend? Does the map fit on one page at readable font size?
- Number each step on the map. The step numbers become the key for the dropped-step analysis table in Step 5. A step without a number cannot be referenced in the analysis.
- Draw the map by hand or in a simple tool before polishing. The first version should be a rough sketch that communicates the flow; the polished version adds notation and labels. Most teams spend too long on the polished version and not enough on verifying that the rough version matches reality. A rough map that reveals a hidden handoff is more valuable than a polished map that confirms the documented-but-inaccurate process.
- **Checkpoint:** "Does the map show what happens when someone says no — not just the path for when they say yes?"

### Step 5 — Conduct the dropped-step analysis

For each step in the current map, ask whether it consistently produces the expected output. Every step that does not gets a row in the analysis table.

- The root cause list — a single, controlled taxonomy:
  - Missing trigger — nothing caused the step to run.
  - Missing handoff element — work crossed without notification or acceptance.
  - Misordered step — the step ran before its prerequisite was true.
  - Missing acceptance criteria — the output was produced but never confirmed.
  - Unassigned ownership — no person was accountable for the step.
  - Capacity gap — the step was skipped because the person was overloaded.
- Each row: step number, expected output, actual result, gap description, root cause, risk level.
- Severity levels: critical (revenue, legal exposure, or client trust), high (rework, delay, or overage), medium (inconsistent output that does not delay the process), low (cosmetic variance).
- Keep a count of defects per root cause. The cause with the highest count is the first design target. In the Pixel & Ink example, missing triggers outnumber every other cause, which is why the redesign leads with automated triggers instead of adding manual checks.
- Look for root cause clusters: three missing triggers in different parts of the process point to a systemic gap in how work is initiated across the board. A systemic fix (like an automated trigger system) addresses all three at once; individual fixes address them one at a time and miss the pattern.
- When two dropped steps share the same root cause, fix both with a single structural change rather than two separate ones. This keeps the process simple and the step count under the 20% limit.
- Present the table to the team before designing fixes. The team must consent to the diagnosis before accepting the prescription. If the team disagrees with a root cause assignment, investigate further — the team's lived experience is data that the table may have misinterpreted.
- **Reference:** `references/quality-management-basics.md`, defect classification.
- **Checkpoint:** "Does every dropped step carry exactly one root cause from the controlled list? If it carries two, split the step."

### Step 6 — Design the target-state process

For each recorded drop, pick one structural countermeasure from the following:

- Add a step that fills the gap (e.g., a checklist before kickoff).
- Reorder steps so preconditions run first.
- Reassign step to a different role or actor.
- Add a gate that only passes when a condition is true before work proceeds. A gate is not a person checking — it is a state that the item must pass through, verified by an artifact or tool.
- Automate a handoff (e.g., trigger an invoice when contract status changes to "signed").

- **Reference:** `references/workflow-design.md`, state design rules and queue management.
- Every handoff must define all six parts: sender, receiver, token, acceptance criteria, trigger, feedback. If one part is missing, the handoff is incomplete. For example, in the Pixel & Ink current state, the asset handoff had a sender (client) and a token (logo file), but no acceptance criteria (what format? all assets or a subset?) and no feedback channel (does CD confirm receipt?). Completing the handoff meant adding acceptance criteria and a confirmation step.
- Restraint: the new design may not exceed the current step count by more than 20%. More than that means the design is adding, not fixing. Count steps precisely: sub-steps within a single decision do not count. Each box and diamond on the map is one step.
- Trace: every new step traces to at least one row in the dropped-step table. Steps that do not have a defect behind them should be removed. If a step cannot be traced, it is process decoration — remove it before presenting to the team.
- Model the wait states explicitly in the target design. Each wait state gets three attributes: the trigger that enters it, the trigger that exits it, and the owner who notices when the exit does not happen. In the Pixel & Ink design, "Waiting on client assets" enters when the checklist is sent, exits when the asset folder is confirmed complete, and the Admin/Systems lane owns the reminder cadence that fires if assets are not received within 3 business days.
- Prefer one structural countermeasure per dropped step. Two countermeasures applied to one defect blur which change produced the effect when you measure later. If two countermeasures genuinely address two different aspects of the same step (e.g., the step needs an earlier trigger AND a clearer acceptance criteria), list both but note which is primary and which is secondary.
- Choose the handoff form for each lane crossing: push (sender pushes to receiver), pull (receiver pulls from a queue), or event-driven (a system trigger fires the handoff). Reference `references/tooling-and-automation.md` for when to automate. Push handoffs suit urgent or time-sensitive transfers; pull handoffs suit processes where the receiver controls their own capacity; event-driven handoffs suit processes where the trigger is predictable and repeatable.
- Validate the target state against the capacity note before finalizing. If the redesign adds steps that push PD capacity over 100%, the design fails regardless of its theoretical elegance. The capacity arithmetic is the closure condition for the design phase.
- **Checkpoint:** "Can each dropped step be traced to a specific change in the new map?"

### Step 7 — Write the SOP for the most critical handoff

Identify the highest-risk row from Step 5. Write a single SOP covering the handoff between that step and the next, using the SOP template and the SOP authoring reference.

- One SOP covers one handoff. If the purpose statement contains "and," split it. A handoff is a single transfer of a single work item from one role to another. When the purpose statement reads "collect deposit and notify the team," it covers two handoffs — split into two SOPs.
- Every step is a single verb phrase and is its own line. "Send the deposit invoice and update the tracker" is two lines: "Send the deposit invoice" and "Update the project tracker to 'invoice sent'."
- Start condition: the exact state that must be true before any step can begin. Written as a binary test. Example for ONB-02: "The signed contract PDF exists in the project folder and the project status is 'Contract Signed.'"
- End condition: the exact state that proves the handoff is complete. Written as a binary test. Example: "The billing system shows a 'Deposit Received' entry for this project and the project status is 'Deposit Received.'"
- Run the newcomer test: hand it to someone who has never done the task and watch. Every question they ask is a gap in the prose. Fix the SOP, not the person. The newcomer test is not a formality — it is the only reliable way to check if an SOP is complete. An SOP that passes the newcomer test with zero questions has a quality ceiling that no amount of editing from the author can achieve.
- **Reference:** `references/sop-authoring.md`, "The Newcomer Test."
- **Template:** `templates/sop-template.md`.
- The SOP must survive the worst-case operator stress: someone interrupted mid-step. Write each step so it can be resumed without re-reading the entire document. Numbered steps, explicit preconditions, and a clear checkpoint at the end make this possible. An interrupted operator should be able to look at the last completed step and resume from there without guessing.
- Write for the second reading, not the first. The first read is orientation. The second read is execution. Steps that require the operator to scroll back to the top to find a reference are broken. If a step references a template name, include the file path in the step itself: "Open `templates/deposit-invoice-template.md`" not "Open the template."
- Include the exception path: what the operator does if a step cannot be completed. "If the billing system returns an error, contact the CD and log the error in the project tracker with the error message." Without exception handling, the operator fills the gap with their own invention, which varies by person.
- Every SOP has a version number and a review date on the first page. The version number changes when any step is added, removed, or reordered. The review date is 90 days from the current date, regardless of whether the SOP is expected to change. A date triggers action; an absence of a date means the SOP drifts until it no longer matches reality.
- When the same information appears in the SOP body and in a reference document, the SOP body wins. Do not make the operator cross-reference. If the billing system's invoice template changes, update the SOP body with the new template path — the cross-reference to a shared resource is brittle and will be the first thing that breaks.
- No SOP runs longer than 15 steps at body font size. If the handoff requires more than 15 steps, it is either too granular (combine two related steps) or too broad (split into two SOPs). The 15-step limit is a forcing function for clarity.
- **Checkpoint:** "Could a competent new person follow this and get the correct output on the first try without asking any questions?"

### Step 8 — Build the capacity note

Using `references/capacity-planning.md`, compute the arithmetic of whether the redesigned process fits the team.

- Team capacity: person-hours per week per role, excluding meetings and admin.
- Demand per work unit: sum the per-step effort from the target-state map.
- Weekly volume: how many work units the team expects to process.
- Ratio: demand ÷ capacity. Below 0.8 is comfortable. 0.8 to 1.0 is sustainable. Above 1.0 is overcommitted.
- Buffer: 15–25% of capacity for outliers and incidents. Include buffer explicitly in the ratio calculation. A ratio of 1.0 without buffer is already overcommitted.
- Bottleneck: identify the step or role with the least slack. State what happens when it saturates. When the bottleneck saturates, work piles up before it, and the steps after it starve. The bottleneck determines the throughput of the entire process.
- Include a specific note about which tool or resource has capacity that is not accounted: an automated billing system has infinite throughput for invoicing; an individual person has none. Do not treat tool capacity the same as human capacity. A tool's throughput is limited only by its design; a human's throughput is limited by time, attention, and energy.
- If ratio exceeds 1.0, state explicitly which work will be deferred, reduced in scope, or rejected. This is part of the note, not a follow-up. The decision to defer work is not a process failure — it is a capacity signal.
- Define the three process metrics: cycle time (trigger to end state), handoff latency (sender delivery to receiver start), and escape count (defects caught by the client). Record baseline measurements before the transition begins. These three metrics cover speed (cycle time), flow (handoff latency), and quality (escape count). A process that improves only one metric without degrading the others is a genuine improvement.
- **Reference:** `references/quality-management-basics.md`, measurement section.
- **Checkpoint:** "If the team's next four commitments are placed on one calendar alongside the process map, does any week exceed capacity? If so, what is the plan?"

### Step 9 — Write and execute the transition plan

A four-week schedule switching the team from current process to target process.

- Week 1: run the new process on one test work item alongside the current process. The team runs both tracks for this one item and compares results. The purpose is discovery, not switching — find the rough edges while the old safety net is still active. Record what broke, what confused someone, and what was slower than expected.
- Week 2: switch the highest-risk handoff across all items. Every project entering the pipeline uses the new handoff structure for one specific crossing (e.g., the contract-to-invoice handoff). Everything else still follows the old pattern. This limits the blast radius of any missed defect and allows the team to build confidence in one change at a time.
- Week 3: run all new work fully using the new process. Existing in-flight projects remain on the old process to avoid mid-stream disruption. The team should be prepared to roll back any specific handoff that fails the confidence test during this week.
- Week 4: hold the first retrospective using `references/continuous-improvement.md` and change exactly one thing. The one change may be a process adjustment, a missing SOP, or an observation about a tool that does not fit — but exactly one. The retrospective asks four questions: what worked, what did not, what did we learn about the process that the design phase missed, and what is our single change for the next two weeks.
- The transition plan is part of the skill's deliverables. If the transition schedule is not written, the new process does not get adopted. The plan should be written on a shared calendar with owner names and dates for each phase.
- A pre-mortem on the transition itself: before starting week 1, the team spends 15 minutes answering "it is now six weeks later and the transition failed — what went wrong?" The answers become mitigations that go into the risk register.
- Rollback plan: specify the conditions under which the team reverts to the old process. Typically, if a critical defect appears that blocks revenue or client delivery, roll back the affected handoff immediately. If the defect is non-critical (e.g., a minor delay in invoice generation), note it for the retrospective but do not roll back. The rollback plan prevents the team from overreacting to small problems.
- **Checkpoint:** "Is the 30-day review date on the calendar with a named owner?"

## 05 — Rules and Quality Bar

These rules separate professional process design from generic advice. Each carries its rationale, because a rule without a why gets ignored under pressure.

1. **Every process map shows at least one exception path.** If the map contains only the happy path, the team has no plan for where things go wrong. Rationale: systems fail at their exceptions; an undrawn exception is an undesigned one.

2. **Every handoff defines six parts.** Sender, receiver, token, acceptance criteria, trigger, feedback. A handoff missing any part forces someone to guess. Rationale: the six-part definition is what makes a handoff self-enforcing and observable.

3. **Every SOP step is one imperative verb phrase on its own line.** If a step needs more than one sentence or two actions, it is two steps. Rationale: the newcomer test fails the moment the reader must mentally unpack a compound step. A step that reads "Verify the deposit percentage and create the invoice" breaks the operator's flow between the two actions. Split it.

4. **Every handoff has a written definition of done with 3 to 7 binary criteria.** Each criterion is verifiable by someone other than the performer. Rationale: without a DoD, "done" reflects mood, and rework becomes the de facto quality process. Example DoD for asset collection: (1) all logo files in vector and raster format, (2) brand style guide attached, (3) sample content uploaded, (4) competitor references linked, (5) copy text in editable format.

5. **The capacity note contains numbers, not words.** Capacity, demand, ratio, and buffer are always numeric. "We are busy" is not a capacity note. Rationale: a design that cannot fit on a calendar fails regardless of its theoretical quality. A numeric capacity note enables the sponsor to make trade-off decisions: "if we accept this project, the bottleneck saturates and the existing project delays by 3 days."

6. **At least one root cause in the analysis is not personal.** If the table says "X forgot," replace it with the systemic condition that permitted the forgetting. Rationale: a process that demands perfect people fails on the first distraction. A system that prevents forgetting — by adding a trigger, a checklist, or a gate — succeeds regardless of who operates it.

7. **Every redesign adds at least one inspection point that did not exist before.** The inspection verifies output against acceptance criteria at the highest-risk handoff. Rationale: adding steps without adding verification increases throughput of defects, not quality. The inspection point is the only step that directly reduces escapes.

8. **Escapes are documented by path, not by person.** "The invoice escaped because no step triggers invoicing after contract signature" — not "Maya forgot." Rationale: blocking the path prevents the next incident; naming the person prevents nothing.

9. **Every state in the process has a named owner.** If a state has no owner, stalled work is invisible. Rationale: the owner is the person who will notice when a wait state exceeds its expected duration.

10. **The process survives one key person being unavailable.** Define the degraded mode: where work waits, what alert fires, who covers. Rationale: a process that stops when one person is out is a person, not a process. If CD is out sick, the asset checklist reminder should still fire, and the contract-to-invoice trigger should still work. The degraded mode lists what continues and what pauses.

11. **Design for the least experienced possible operator.** The SOP assumes no context outside the document; the map uses roles, not individuals. Rationale: a process that works only for the veteran is a knowledge silo, not a process. A new team member should be able to read the SOP and execute the handoff without asking anyone for clarification.

12. **One change per improvement cycle.** Multiple fixes may be drafted, but they go live one at a time with baseline measurements between. Rationale: two simultaneous changes make the effect impossible to attribute.

13. **The process is the actual observable behavior, not the document.** If the map is accurate but the team does not follow it, the design is incomplete. Rationale: a process that lives in a folder produces no value.

14. **Every design carries a 30-day review date, and that review happens.** Compare the actual operation against the target map: count defects, measure cycle time, decide what to adjust. The review is the first step of the continuous improvement cadence from `references/continuous-improvement.md`. A review that does not change anything is a missed opportunity — there is always something to improve in a process that has been running for 30 days.

15. **Design for the typical work item, not the outlier.** If eight of ten projects flow smoothly and the design is built around the two difficult ones, the team will reject the overhead for the majority case. Rationale: the outlier gets an exception path; the main path serves the typical flow. Tag exception paths clearly so operators know when to deviate.

16. **Do not design a step that cannot be observed.** If a step produces no artifact and no observable output, decompose it into sub-steps until each produces something measurable. Rationale: an invisible step cannot be verified, inspected, or improved. A "thinking" step is not a process step — "write the scope document" is.

17. **The first week of the transition is for discovery, not for proving the design works.** If the team reports that the new process broke something, that is data, not failure. The design must be adjusted, and the adjustment is the purpose of the test run. Rationale: a design that is fragile under the first real test would have failed eventually — better to find it in week 1 than in week 3 when three projects are in flight.

18. **A process map without a legend is not a process map.** Every shape used (rectangle for step, diamond for decision, rounded rectangle for terminal, parallel lines for wait state) must be defined in a legend on the same page. Rationale: the map is a communication tool; a reader who must guess what a shape means will misinterpret the process.

19. **Every decision diamond has an explicit question written inside it.** "Client signs contract?" not just "Sign?" The question must be binary (yes/no) and must be the exact question the operator answers. Rationale: vague questions produce vague branches, and vague branches are indistinguishable from guesses.

20. **SOPs list the materials, tools, or system access needed before the first step.** A newcomer who reaches step 3 and realizes they need access to a tool they do not have will stop the process. The materials section prevents that stop. Rationale: a process that requires a tool the operator cannot use is a process that will not run.

**Anti-patterns to avoid:**

- **Process as punishment.** If the process exists because one person failed once, it feels like collective attribution and is rejected immediately. Design from systemic need, not from a specific incident.
- **The process design is an add-on to existing work.** New steps are added to a process that is already full. Every process design should also remove at least one old step, freeing capacity for the new controls.
- **Writing the process as figures of speech.** Terms like "escalate," "align," "deep dive," and "circle back" are not process steps. A step must be an observable behavior — something you can see a person doing. Replace "escalate to leadership" with "send the summary report to the director with a yes/no recommendation."
- **Documenting before observing.** Writing the process from a conference room without watching the actual work creates a map that is wrong from the start. The team will reject it because it does not match reality.
- **Process design as a one-time event.** If the document is never reviewed and never adjusted, it is an archive copy, not a process. The 30-day review is not optional. A process that is not reviewed may as well not exist.
- **Assigning process ownership to someone who does not execute it.** The process needs co-design with the people who will execute it. A process designed by a consultant and handed to a team is owned by no one.
- **Perfection before launch.** Waiting until the design is flawless before the team begins to follow it delays the first delivery and the first improvement cycle. Bring a "good enough" design to test in week 1, then improve from actual use data rather than from theory.
- **Treating every exception as a process failure.** Some steps are deliberately gated by human judgment. A process that tries to encode every decision removes the human judgment it needs. Distinguish between process failure (a step that should have run but did not) and deliberate exception (a step that was skipped because the operator judged it unnecessary and documented the reason).
- **Over-measuring before stable operation.** Do not install metrics until the process has run for two weeks. Early metrics reflect transition friction, not process quality. Baseline after two weeks, then measure.

Delivery requires passing the reference checklists:

- Process map checklist: `references/process-mapping.md`, "Process map quality checklist."
- SOP checklist: `references/sop-authoring.md`, "Quality check the deliverable."
- Quality management checklist: `references/quality-management-basics.md`, "Quality management checklist."

If any checklist item fails, the artifact is not done. Fix it and re-run.

**How to present the redesigned process to a sponsor or team.**

The presentation should follow this structure, which mirrors the workflow order and builds trust at each step:

1. Start with the current-state map. Read it aloud with the team following along. When they see their own work reflected accurately, they trust that the design is grounded in reality. If they correct the map, incorporate the correction before moving on.
2. Present the dropped-step analysis table. Lead with the root cause distribution, not the individual rows. Say "We found three missing triggers" before listing each one. The distribution tells the story faster than the table.
3. State the principle behind each target design change before showing the target map. "We are adding automated triggers because missing triggers are our most common defect" sets up the target map as a response to a problem, not an arbitrary redesign.
4. Show the target map directly overlaid on the current map (a side-by-side or diff format). Highlight what changed and why each change traces to a dropped-step row.
- Read the capacity note aloud. Lead with the bottleneck and the limit. "PD design time is the constraint, and we can only do one project at a time" is an honest statement that earns more trust than "we think we can handle it."
6. Present the risk register before the transition plan. Acknowledging risks upfront signals maturity. If the sponsor pushes back on a risk, update the register — don't defend it.
7. Close with the transition plan in calendar format. Name the week-1 date and the week-4 retrospective date. The team leaves knowing exactly when the changes begin.

Each presentation step consumes no more than 5 minutes. The entire meeting lasts 35 minutes. If the meeting runs longer, the designer has lost the room with detail that belongs in the supporting documentation.

**Final delivery format.** The complete package is a single PDF or markdown document with the following sections in order: (1) scope sentence and adjacent processes not in scope, (2) current-state swimlane map, (3) dropped-step analysis table, (4) target-state swimlane map, (5) SOP for the highest-risk handoff, (6) capacity note with baseline metrics, (7) risk register, (8) transition plan with calendar dates and named owners. The document is no longer than 15 pages at 11pt body font. Extra detail lives in the `examples/` and `references/` directories and is linked from the document but not included inline.

**Process maturity after the first cycle.** After the four-week transition plan completes, the team can assess where their process stands on the three-level maturity scale defined in §01. A level-one process produces consistent output: the same steps in the same order, every time, with documented exceptions. Level two adds measurement: the team knows their cycle time, handoff latency, and escape count, and can see week-over-week trends. Level three adds improvement: each retrospective changes exactly one thing, and the measurement system confirms the effect. Most teams reach level one after the first four-week cycle. Level two takes two to three cycles (8-12 weeks). Level three is the ongoing operating state. The skill's reference files — particularly `references/continuous-improvement.md` and `references/quality-management-basics.md` — provide the method for each advancement.

## 06 — Worked Example: Pixel & Ink

This section runs the full workflow on a representative scenario: a two-person design studio called Pixel & Ink. Their client onboarding process drops steps at every handoff. The full extended artifact — maps, SOP, capacity worksheet, and decision log — is in `examples/worked-process-design.md`. This section presents the intermediate artifacts in condensed form.

### The Studio and the Problem

Pixel & Ink has two people. Maya is the creative director (CD) handling client relationships, scoping, and billing. A production designer (PD) does the design work and handles client feedback. There is no administrative role.

Maya's description of the current state: "A new client emails us. I send a contract, sometimes not. When they confirm, I tell the PD to start, maybe. He asks for brand assets, but the client may send them days later. I design, send, the client replies with feedback that I pass to the PD. I send the invoice at the end. If I remember."

Known symptoms: contracts are not signed before work starts, deposits are not collected, kickoffs happen before design assets arrive, no brief is written, and the project folder is missing.

### Step 1: Process Boundary

Sentence: "When a prospective client makes first contact, the process runs until the final payment is received and the project folder is archived."

Adjacent excluded processes: lead generation (pre-trigger) and portfolio management (post-end-state). The scope sentence explicitly excludes marketing activities that generate leads before first contact, and post-project activities like portfolio review and case study development. This is documented on the scope card shared with all stakeholders.

### Step 2: Actors and Lanes

- Creative Director (CD) — Maya
- Production Designer (PD)
- Client
- Admin/Systems — new lane added during design

The process has four lanes. The Admin/Systems lane is new — it did not exist in the current state. Adding it was the first structural change, because without a dedicated lane for tool-based automations, the team had no way to assign ownership to the automated triggers that the target design requires.

### Step 3: Walk a Real Work Item

Tracing the last actual project:

1. Client sends inquiry.
2. CD holds a discovery call; notes are not recorded outside a notebook.
3. CD sends a summary email with a rough scope. No brief document exists.
4. CD sends contract. Client responds "sounds good" but does not actually sign.
5. CD verbally authorizes PD to start work.
6. PD asks for brand assets. Client sends a logo in the wrong format. Three additional back-and-forth exchanges follow.
7. PD begins designing from an email thread and guesswork about aesthetic direction.
8. PD sends first round to CD. CD forwards to the client.
9. Client feedback goes back through CD to PD — delayed by up to 2 days. The feedback is rephrased by CD.
10. Two revision rounds. The second round reveals that the client expected a different color palette.
11. CD sends an invoice after final delivery.
12. Payment arrives after 5 weeks and 2 CD reminders.

Observation: no step in this trace verified anything — not the contract signature, assets, brief, direction, or payment terms. Every handoff was verbal or email-based with no acceptance criteria. The process relied entirely on CD's memory and goodwill. When CD was busy (which was most of the time), steps were skipped. The trace demonstrates the classic "good intentions" process: everyone believes the steps are happening, but no artifact confirms that any transfer actually completed.

Key observation from the artifact trace: the email thread for this project contained 47 messages over 9 weeks. Of those 47, 29 were requests for information that should have been collected in the first contact. The ratio of request messages to production messages is a proxy for process health: a well-designed process produces a low ratio; Pixel & Ink's ratio of 29:47 (62%) indicates a severe information-asymmetry problem where most of the communication time is spent collecting what should have been gathered upfront.

### Step 4: Current-State Swimlane Map (Condensed)

**CD lane:** Receive inquiry → Discovery call (unrecorded) → Send scope email → Send contract (sometimes days later) → Verbally authorize start → Notify PD → Relay assets piecemeal → Receive design → Forward to client → Receive feedback → Forward to PD → Send invoice (if remembered) → Chase payment.

**PD lane:** Wait for start signal → Ask for assets and brief → Wait for assets → Design from guesswork → Send to CD → Receive feedback (rephrased) → Revise → Repeat.

**Client lane:** Express interest → Agree verbally → Receive asset request → Send partial assets → Receive design draft → Send feedback to CD → Wait for invoice → Pay late.

**Admin/Systems lane:** (Empty — no existing tooling.)

Zero decision diamonds because no step has a conditional path. The process is linear even though evidence shows it skips several steps. The complete map uses the notation conventions from `templates/process-map-template.md`.

Structural analysis of the current map: 29 steps across 3 lanes (12 in CD, 8 in PD, 9 in Client). No wait states are drawn, but the trace shows at least 3 wait states (waiting for contract signature, waiting for assets, waiting for payment). The absence of drawn wait states is diagnostic: the team treats waiting as a normal part of the process rather than a deviation to be measured and reduced. A well-designed process draws wait states explicitly so the team can see where time is lost.

Handoff count: 12 lane crossings. Of these, 7 are missing at least one of the six handoff elements. The most common missing element is acceptance criteria (missing in 6 of 7 incomplete handoffs). The second most common is feedback confirmation (missing in 4 of 7). This is the primary structural defect: work moves between lanes without any verification that the right thing was received.

### Step 5: Dropped-Step Analysis

| # | Step | Expected | Actual | Root Cause | Risk |
|---|------|----------|--------|------------|------|
| 1 | Contract | Signed PDF | Verbal agreement | Missing acceptance criteria | Critical |
| 2 | Deposit | 50% collected before start | Never collected | Missing trigger | Critical |
| 3 | Kickoff | Assets + brief confirmed | Start before both ready | Misordered step — no gate | Critical |
| 4 | Brief | Written brief in folder | Notebook notes only | Unassigned ownership | High |
| 5 | Assets | Complete checklist in folder | Partial, wrong format | Missing handoff acceptance | High |
| 6 | Feedback | Direct PD–client loop | Rephrased via CD | Capacity gap — CD is blocking | High |
| 7 | Invoice | Triggered at milestone | At end if remembered | Missing trigger | High |

Root cause distribution: Missing trigger = 3 (deposit, asset checklist trigger, invoice). Missing handoff element = 2 (contract acceptance criteria, asset acceptance criteria). Misordered step = 1 (kickoff before deposit cleared). Unassigned ownership = 1 (no one owned brief creation). Capacity gap = 1 (CD as feedback bottleneck). The distribution drives the design priorities: add triggers first because they affect three defects; fix handoff completeness second because it affects two; the remaining defects are addressed as individual adjustments. The capacity gap on feedback is unique — CD is blocking because CD is the only channel to the client. The redesign removes CD from the feedback loop entirely, which resolves the capacity gap without adding headcount.

Three clusters: missing triggers (deposit, invoice), no gate on preconditions (kickoff), and unstructured handoffs (assets, feedback, contract). The complete analysis with full detail is in `examples/worked-process-design.md`.

### Step 6: Target-State Redesign

Updated lanes: CD, PD, Client, Admin/Systems.

Changes applied:

- CD scopes project with a brief template and creates a project folder at the scope step. During the scope call, CD follows the brief template to capture project goals, audience, deliverables, timeline, and budget in a structured document. The template ensures nothing is forgotten and provides a shared reference for kickoff.
- Contract is sent for digital signature via an e-sign tool. The tool replaces the "send contract PDF by email and hope" pattern with a standard process that creates a signed artifact and fires an event when complete.
- When signature completes, the Admin/Systems lane automatically sends a deposit invoice for 50%. This replaces CD's memory-based invoice trigger with an event-driven handoff. The trigger is "e-sign status = complete"; the action is "generate and send deposit invoice."
- Kickoff does not start until the deposit has cleared. This fixes dropped step 2 (missing deposit). The gate is a status check on the billing system; the kickoff step reads "project status = Deposit Received" before proceeding. This is the single most impactful change in the redesign.
- A standing asset checklist is sent with the contract. Admin/Systems tracks the checklist and reminds the client every 3 days. Kickoff occurs only when the checklist shows complete. This fixes dropped step 3 (incomplete assets). The checklist includes: logo files (vector and raster), brand style guide, sample content/images, copy text, competitor references, and technical specifications. Each item has a "received" checkbox with a date stamp.
- CD, PD, and client hold a kickoff meeting together; the brief is confirmed on the call. This fixes dropped step 4 (missing brief). The meeting agenda is: review the brief point by point, confirm design direction, set revision expectations, and agree on the communication channel (tool, not CD). All three parties sign off on the brief document during the call.
- PD sends drafts directly to client for review; feedback flows directly to PD. CD sees only project milestones. This fixes dropped step 6 (CD as bottleneck). PD and client share a review tool with inline commenting, eliminating the rephrasing delay.
- Final approval triggers the balance invoice automatically. Fixes dropped step 7 (missing invoice trigger). When the client marks "approved" in the review tool, the system generates the final invoice.

Handoff count drops from 12 to 7. Step count rises from 29 to 33 — within the 20% margin. The complete target-state map uses the notation in `templates/process-map-template.md`. The six-part handoff specification for every lane crossing is documented following `references/workflow-design.md`.

### Step 7: SOP for the Highest-Risk Handoff (Overview)

The full SOP is ONB-02: Collect deposit after contract signature. This handoff was selected because it has the highest risk score in the dropped-step table (critical severity, two root causes: missing trigger and missing acceptance criteria).

Start condition: the e-sign system reports the contract signed.
End condition: bank shows the deposit received, and project status is "Deposit Received."

Procedure:
1. Open the signed contract PDF and read the deposit amount.
2. Create the deposit invoice in the billing system for 50% of the contract value.
3. Send the invoice with the payment-terms template.
4. Record the invoice date and due date in the project tracker.
5. Check for payment every 2 business days.
6. If payment is 5 business days late, send the overdue reminder template.
7. When payment arrives, update project status to "Deposit received."
8. Notify CD and PD the project is cleared for asset-collection phase.

Exception path for step 6: if the billing system returns an error when creating the invoice, contact CD and log the error in the project tracker with the exact error message. Do not proceed until CD confirms the billing issue is resolved. If the overdue reminder from step 6 generates no response within 3 additional business days, escalate to CD who contacts the client directly.

Materials needed before starting: access to the e-sign system (reporting view), access to the billing system (invoice creation), access to the project tracker, deposit invoice template (`templates/deposit-invoice-template.md`), and the overdue reminder template (`templates/overdue-reminder-template.md`).

Acceptance criteria: the billing tool shows deposit as received, and the tracker status is "Deposit received." The complete SOP document is in `examples/worked-process-design.md` following the `templates/sop-template.md` format.

Validation result: the SOP passed the newcomer test with one question ("What if the contract deposit percentage is different from 50%?"). The SOP was updated to add step 1.5: "Verify the deposit percentage in the signed contract terms; if different from the default 50%, adjust the invoice amount." After this change, the SOP passed the test with zero questions.

### Step 8: Capacity Note

- CD capacity: 25 hours/week for project work.
- PD capacity: 22 hours/week for design and feedback.
- Admin/Systems time: negligible once templates are set up. The e-sign tool and billing automation run without human attention. The only human-admin overhead is the reminder cadence for asset collection (setting a timer when checklist is sent, checking in every 3 days). Estimated at 0.5 hours per project.

Per-project demand: scoping (3h CD), contract (0.5h CD), asset collection (0.5h automated admin), kickoff (1h CD + 0.5h PD), design (16h PD), revisions (2h PD), review/approval (2h CD). Total: 8h CD, 18.5h PD, 0.5h admin.

At 1 project per week: CD ratio = 32% utilization; PD ratio = 84%. Sustainable with some buffer remaining.
At 2 concurrent projects: PD ratio = 168%, not feasible. The capacity note states that only 1 project may be in the design phase at a time. The second project must wait in the asset collection queue. This means the sales pipeline must be managed to not exceed one project per week entering the design phase.

Demand composition: PD design time makes up 86% of PD's total per-project effort. If revision time increases (e.g., a difficult client or an unclear brief), the design phase extends, and the one-project-per-week constraint tightens. The capacity note flags this as the highest-risk assumption and recommends tracking actual design hours against the 16-hour estimate in the first three projects.

Buffer: 15% of PD time (3.3 hours/week) reserved for urgent revision work.
Bottleneck: PD design time. Sales must be based on PD capacity, not CD enthusiasm. CD has 68% slack after one project, which means CD can take on additional sales and scoping work as long as that does not increase the number of projects entering the design pipeline.

Choke point analysis: the deposit-collection step now has an automated trigger (contract→invoice), which reduces handoff latency from CD's variable availability to the e-sign tool's constant availability. This is the single improvement that had the highest impact on the overall cycle time because it removed CD from the critical path for that handoff.

Baseline metrics before transition: cycle time = 42 days (median), handoff latency at the asset step = 3–5 days, escapes = 2 per project (missing direction, wrong palette). Method from `references/capacity-planning.md`. These baselines are recorded before any changes are made, so the improvement from the redesign is measurable against a known starting point.

### Transition and Results

After 2 months of running the target design (the full transition plan is in `examples/worked-process-design.md`):

- Deposit collection time: 18 days → 4 days. The automated trigger from e-sign to invoicing removed CD's memory as the gating factor. The first invoice now goes out within hours of contract signature, not days or weeks.
- Projects starting before contract signed: 0 of 6 (vs. previous where all started before signing). The gate on deposit cleared is enforced by the tool, not by CD's oversight. Work cannot begin until the system shows "Deposit Received."
- Projects with all assets at kickoff: 5 of 6 (vs. 3 of 7 previously). The asset checklist and Admin/Systems reminder cadence reduced the incomplete-asset handoff from the most common delay to a near miss.
- PD reported 70% less surprise work in the design loop. Direct feedback from client to PD eliminated the rephrasing delay and the misinterpretation that CD's rephrasing introduced. PD now receives the client's actual words, not CD's interpretation.
- CD reported: "I have one hour a week to track pipeline instead of emergency triage." CD's time was freed from being the handoff bottleneck for contract, assets, feedback, and invoicing. That time now goes to project strategy and client relationships.
- Cycle time reduced from 42 days to 18 days (median). The 57% reduction comes from parallelizing the asset collection phase with the design phase: assets are collected during contract signing rather than after kickoff.
- Escapes reduced from 2 per project to 0.3 per project. The brief confirmation during the kickoff call eliminated the "wrong palette" escape. The direct feedback loop eliminated the "misunderstood direction" escape.
- The pre-mortem (conducted before week 1) identified two risks that materialized during the transition: (1) the automated invoice firing for a contract with changed scope, and (2) the client not understanding the asset checklist format. Both had mitigations in the risk register, which reduced their impact from process-stopping to process-slowing.

The transition was not perfectly smooth. In week 2 of the transition, the automated deposit invoice fired for a project where the scope had changed after the contract was signed, producing an invoice that did not match the revised scope. The SOP was updated in week 3 to add a step: "Before sending the automatic deposit invoice, verify that the signed contract is the current version." The one weekly change rule (from continuous improvement) meant fixing this one gap in week 2 and living with any other rough edges until week 4's retrospective.

The full narrative case study with before/after metrics appears in `references/operations-case-studies.md`. The complete transition plan, maps, and decision log are in `examples/worked-process-design.md`.

## 07 — Failure Modes and Recovery

Process design fails in predictable ways. Each mode names the early signal, the corrective action, the prevention, and the detection check.

**Failure 1 — The map describes what people said, not what they do.**

- Signal: during review, a team member reads the map and says "That's not how it really works" or "We stopped doing that months ago." Or, more tellingly, the team member who was interviewed later points to a step on the map and says "That's what I said, but actually I check another system first."
- Fix: return to Step 3 and trace two more real items end to end. Remove steps that were not observed. For each removed step, ask why the interview reported it — was it a hoped-for step that never materialized, or a historical practice that stopped but was not removed from the collective memory?
- Prevention: never build the first map from interviews alone. Observation of one work item outweighs three perfectly reported recollections. Use interviews for the cast of characters and the language of the domain, but observation for the actual sequence of events.
- Detection: the step count mismatch between interviews and observation exceeds 30%.

**Failure 2 — The map is all easy path.**

- Signal: the drawn flow is a straight line — no loops, no diamonds, no exception path.
- Fix: ask for the worst work item this month. Map that second path. The deviations are the exception paths.
- Prevention: when drawing a decision diamond, write the NO branch before the YES branch. A diamond must have two paths.
- Detection: every lane has exactly one arrow per step; there are no diamonds.

**Failure 3 — The SOP fails the newcomer test.**

- Signal: the test reader stops mid-procedure to ask about a term, a path, a tool, or a file location.
- Fix: treat every question as a defect in the document. Add a step or update a term. Re-run the test.
- Prevention: the newcomer test is a release gate. No SOP ships without passing it.
- Detection: more than 3 questions or pauses during the first read-through.

**Failure 4 — Capacity estimates are optimistic.**

- Signal: the ratio appears comfortable, but the team is drowning in the first two weeks. They are meeting the new process steps but working overtime to do so, which is not captured in the basic demand/capacity arithmetic.
- Fix: measure actual hours in the first two completed items. Recompute the ratio. If above 1.0, cut work immediately. Use the actual hours to update the demand estimate for future projects; the estimated demand was likely missing a step that only shows up during real execution.
- Prevention: the first retrospective reviews the capacity note against measured actuals. The note has a "revised on" date for its estimated parameters.
- Detection: overtime appears in the first two weeks despite a ratio below 0.8.

**Failure 5 — Ratio exceeds 1.0 with no intake gate.**

- Signal: work is accepted while the queue grows, and no one can say which commitment will be late.
- Fix: add an intake gate. New work waits in a queue until the bottleneck frees up.
- Prevention: the capacity note lists a plan for what to defer before the process goes live.
- Detection: number of in-flight projects exceeds the number that capacity arithmetic supports.

**Failure 6 — The team ignores the new process.**

- Signal: maps are filed away. Two weeks later, the old process still runs unchanged. The maps are referenced in meetings but not used between them.
- Fix: stop trying to enforce everything. Enforce the single highest-risk handoff — the one the SOP covers. One enforced gate changes behavior more than seven ignored ones. A single enforced handoff sets a precedent that other handoffs will eventually follow.
- Prevention: the team participated in the design (Step 6). Co-design creates ownership; delivery creates resistance. If the team did not participate, the resistance is expected and the transition plan must account for it with more coaching time in week 1.
- Detection: the first retrospective finds no change in behavior, or the team reports "we keep meaning to use the new process but keep falling back."

**Failure 7 — The redesign adds more complexity than it removes.**

- Signal: the new map has significantly more steps than the old one — over the 20% limit.
- Fix: delete new steps that do not trace to a dropped-step row. Merge steps with shared actors and triggers.
- Prevention: the 20% limit is the constraint. Track step count as a design metric.
- Detection: step count exceeds old count by more than 20%.

**Failure 8 — The process decays after one month.**

- Signal: after 2–3 weeks, no one privately tracks work-in-progress, and the team returns to memory-based operation.
- Fix: hold the 30-day review even if the team is busy. Find the biggest bottleneck and simplify it.
- Prevention: the 30-day review event is set during the design phase, with a named owner and calendar block.
- Detection: the capacity note is not referenced in any decision for two consecutive weeks.

**Failure 9 — Process abandonment risk.** The team invests in designing the new process but never adopts it.

- Signal: the team nods at the output, says "looks good," and goes back to the old way.
- Fix: co-design every step. Share intermediate artifacts — the current-state map at Step 4, the dropped-step table at Step 5, the target map at Step 6 — and let the team consent to each one before proceeding. Consent means "I can live with it," not "I agree with everything."
- Prevention: include the team in Step 3 walkthrough. The person who sees their own world reflected in the current-state map is invested in the new design.
- Detection: no one referencing the process artifacts in daily standups after week 1.

**Failure 10 — Cascading failure from an upstream defect.** A defect in one step propagates downstream, and each downstream actor treats it as a separate new problem.

- Signal: three different people report three different problems; investigation reveals they all trace to one upstream missing step.
- Fix: anchor every investigation at the upstream source handoff. Log all downstream symptoms as artifacts of one defect until proven otherwise.
- Prevention: build a single inspection point at the highest-risk handoff. When that handoff is enforced, cascading failures are contained.
- Detection: escape count rises without a corresponding increase in dropped-step table entries.

**Failure 11 — The design is accepted but the team does not understand it.** The target map is approved in a meeting, but when asked to explain the flow from start to finish, no one can.

- Signal: the team nods at the target map but offers no questions or concerns. Silence during a design review is not consent — it is confusion.
- Fix: run a simulation. Ask the team to walk through the target map with a hypothetical work item. Each person says what they do at each step and what they expect from the previous handoff. The simulation reveals every misunderstanding before the transition starts.
- Prevention: the target map is presented not as a final design but as a shared hypothesis. The team tests the hypothesis during week 1 (the test run) and adjusts from what they learn.
- Detection: week 1 test run reveals that two team members had different understandings of the same step.

**Failure 12 — The process is adopted but the metrics never improve.** The team follows the new map, creates SOPs, runs retrospectives, but cycle time and escapes stay the same.

- Signal: three months in, the baseline metrics from Step 8 have not changed direction.
- Fix: the most common cause is that the design treated symptoms rather than root causes. Re-run the dropped-step analysis with the current-state map (which is now the previous month's actuals). Look for the root cause that was misidentified or overlooked in the first pass.
- Prevention: during Step 6, validate each countermeasure by asking "will this actually change the metric we care about?" A countermeasure that does not trace to a measurable metric outcome is a guess.
- Detection: the 30-day review and the 60-day review both show zero movement in the target metric.

**Failure 13 — The transition plan is written but not executed.** The plan exists on paper, but the team does not start the test run in week 1, and the process never leaves the old way of working.

- Signal: the week-1 test run date passes with no activity. When asked, the team says they will start next week.
- Fix: the transition plan must have a hard start date agreed upon by the sponsor and the team during Step 9. If the start date slips by more than one week, the process design is dead — repeat Steps 4-6 with the team's consent.
- Prevention: the transition plan is not a draft; it is a calendar commitment. The sponsor must confirm the week-1 start date during the final presentation meeting.
- Detection: no test run activity within the first week after the presentation meeting.

**Recovery protocol for any failure mode.** When a failure is detected, follow this sequence:

1. Name the failure mode from the list above. Do not describe symptoms; name the specific mode.
2. Identify the root cause using the same controlled taxonomy from Step 5: missing trigger, missing handoff element, misordered step, missing acceptance criteria, unassigned ownership, or capacity gap. The failure may trace to a different root cause than the original dropped steps.
3. Apply the fix listed for the failure mode.
4. Apply the prevention measure permanently so the failure does not recur in the next cycle.
5. Log the failure in the risk register as a new row if it was not already listed.
6. Proceed — do not restart the workflow from Step 1 unless the failure invalidates the current-state map. Most failures are contained within one or two steps of the workflow.

**Risk register format.** For each risk identified during design, document in a table:

| Risk | Likelihood (1–5) | Impact (1–5) | Mitigation | Owner |
|------|-----------------|-------------|------------|-------|

Complete this table at the end of Step 6 and include it in the process package. Use the defect classification from `references/quality-management-basics.md`. When presenting the redesigned process, lead with the risk section. A design that acknowledges its risks is trusted more than one that claims perfection.

**Example risk register entries for Pixel & Ink redesign:**

| Risk | Likelihood (1–5) | Impact (1–5) | Mitigation | Owner |
|------|-----------------|-------------|------------|-------|
| Automated invoice fires for wrong scope version | 4 | 3 | Add scope-verification step before invoice generation | CD |
| Client does not understand asset checklist format | 3 | 4 | Include example of each asset type in the checklist | Admin/Systems |
| PD resists direct feedback channel (loss of CD filter) | 2 | 3 | Roll feedback change out gradually; week 2 is trial only | CD |
| E-sign tool adoption friction with clients | 4 | 2 | Send one-paragraph setup guide with the contract link | CD |
| Capacity constraint (PD at 84%) blocks growth | 3 | 4 | Track PD actual hours for first 3 projects before scaling | CD |

Each risk has a named owner who is responsible for monitoring the signal and activating the mitigation. The risk register is reviewed at each retrospective (weeks 1, 4, 8, and monthly thereafter). When a risk changes (likelihood or impact shifts by 2+ points), the register is updated immediately; otherwise, it is revalidated at the next retrospective.

## 08 — Supporting Files Index

The table lists every file in this skill directory. The index must match the directory exactly: if a file exists but is not listed, or is listed but does not exist, the skill is broken.

| Path | Purpose | Used By |
|------|---------|---------|
| `references/process-mapping.md` | Swimlane methodology: scope, lanes, handoff anatomy, quality checklist | §01, §02, §03, §04 Steps 1–4, §05 |
| `references/workflow-design.md` | State models, queues, batching, bottleneck theory, WIP limits, six-part handoff | §04 Steps 3, 6; §05; §07 |
| `references/sop-authoring.md` | SOP writing standards, newcomer test, delivery checklist | §03, §04 Step 7, §05 |
| `references/capacity-planning.md` | Demand vs capacity arithmetic, buffers, bottleneck identification | §03, §04 Step 8, §05, §07 |
| `references/quality-management-basics.md` | Definitions of done, inspection points, escapes, measurement | §04 Steps 5, 8; §05; §06 |
| `references/continuous-improvement.md` | Retrospectives, one change at a time, kaizen cadence | §04 Step 9, §05, §07 |
| `references/tooling-and-automation.md` | When to automate, design vs buy, automation risk | §04 Step 6, §05, §07 Failure 10 |
| `references/operations-case-studies.md` | Full case study: Pixel & Ink and other process redesigns | §06 |
| `templates/sop-template.md` | SOP scaffold with instructional comments and format rules | §03, §04 Step 7, §06 |
| `templates/process-map-template.md` | Process-map notation scaffold with step inventory, handoff table | §03, §04 Steps 2, 4, 6; §06 |
| `examples/worked-process-design.md` | Extended worked example: full maps, SOP, capacity worksheet | §06, §07 |

**Maintenance contract:**

- This table must match the directory exactly — the verification suite diffs it against the filesystem.
- If you add a file, add a row and cite it at its point of use in §04.
- If a file is no longer used, remove both the file and the row.
- The "Used By" column lists the sections that reference the file. An uncited file must be used or removed.

**Verification:** Run a file listing of this skill directory and compare against the table. Every file on disk must appear in the table. Every file in the table must exist on disk. Every reference file is at least 40 substantive lines; every template and example is at least 30 substantive lines. If any file falls below the minimum, expand it to meet the standard.

**File-level quality standards for this skill directory:**
- Each references/ file must be 40-200 lines of substantive content. A reference that is too short does not carry enough craft knowledge to be useful; a reference that exceeds 200 lines should be split into two references.
- Each template must be at least 30 lines with instructional comments explaining how to use each section. Bare stencil files are not templates — they must carry usage guidance.
- Each example must be at least 50 lines and demonstrate the full workflow on a named scenario with intermediate artifacts.
- The SKILL.md itself must be 504-520 substantive lines (total - blank - 2 frontmatter delimiters). This ensures every skill carries comparable depth regardless of its topic.

**Maintenance cadence:** The skill directory should be reviewed every 90 days. At each review, check that every reference file is still accurate, every template still matches the current workflow steps, and every example still represents a realistic scenario. Update the review date in each file's frontmatter or first-page section. A skill that is not reviewed degrades silently.

**Cross-skill boundaries:**

- Findings that reveal tooling or automation gaps that require custom software belong to `software-architecture-design`. Process design identifies the gap; architecture designs the tool.
- Test-suite design gaps surfaced during quality management belong to `testing-strategy`. Process design defines inspection points; testing strategy defines the test suite shape.
- Strategic decisions about what work to accept, pricing, or market positioning belong to `strategic-planning`. Process design assumes strategy exists and is stable.
- If the same process defect appears in three different workflows across the organization, stop designing individual processes and start a systemic operations architecture conversation — the pattern is the finding.

This skill is part of an open-source agent skills collection. Extend it, adapt it to your context, and contribute improvements back through the project repository.

**How to extend this skill for your domain.** If your process domain (e.g., clinical intake, construction estimating, or customer support) has specific vocabulary, regulations, or tool requirements, create a domain-specific adaptation by:

1. Forking `templates/process-map-template.md` with domain-specific lane categories and step types.
2. Adding a domain-specific reference file to `references/` (e.g., `references/regulatory-requirements.md` or `references/industry-standard-workflows.md`).
3. Updating the Supporting Files Index table in §08 of the forked SKILL.md.
4. Running the verification check: every file in the directory appears in the table, and every table entry exists on disk.

The skill's core workflow (§04 Steps 1-9) is designed to be domain-independent. The domain adaptation lives in the reference files and templates, not in the workflow steps themselves. When you fork, keep the workflow steps intact — domain knowledge belongs in references, and the verification suite checks the fork's section structure against the same 0006 contract. Domain adaptations are forks, not edits to this file: this SKILL.md stays generic so every domain gets the same tested workflow.

**Final note on scope discipline.** The most common way this skill fails is not bad design — it is scope expansion. A team asks for help with client onboarding, and by week three the redesign covers project management, invoicing, time tracking, and hiring. Each addition seems reasonable in isolation. Together they produce a system nobody follows. Resist the pull: one process, one boundary sentence, one transition plan at a time. The method works because it is narrow. A second process deserves its own boundary sentence, its own dropped-step table, and its own transition plan — not a bolt-on to the first. When a sponsor pushes for "while we are at it" additions during the final presentation, record them in a parking lot with a named future date rather than absorbing them into the current scope; the parking lot is the pressure valve that keeps the boundary sentence intact. At the 30-day retrospective, every parked item is scheduled as its own bounded redesign or explicitly declined, so the list never becomes a graveyard of good intentions.

**Return triggers, enumerated.** (1) Process shape change: a new client type, service line, or staffing change that alters the number of hands a step passes through. (2) Repeat drop: the same step dropped twice in one quarter, which means the fix is structural, not behavioral. (3) Silent skip: a checklist item skipped without comment across three consecutive runs — either the item is wrong, or the training is. (4) Metrics drift: cycle time or escape count trending worse for three consecutive periods. (5) Post-incident: any client-visible failure traced to a handoff. Each trigger opens a new scoped engagement with its own boundary sentence — never a patch to the previous one's artifacts. A fresh pass reuses the same nine-step workflow, the same templates, and the same quality bar; only the boundary sentence and the cast of actors change between passes. Keep the previous artifacts archived, not edited: an archive of dated maps is the history of how the operation matured, and it prevents the next practitioner from re-deriving decisions that were already made.

**The nine-step workflow at a glance, for when you return.**

1. Scope: write the boundary sentence — what process, which actors, what is explicitly out.
2. Inventory: list every actor, tool, and artifact the process touches today.
3. Map the current state: swimlanes, steps, handoffs, decision points — observed, not remembered.
4. Analyze dropped steps: find where work falls through and classify each drop by root cause.
5. Design the target state: remove, combine, automate, or gate each failure point.
6. Draft the SOP: numbered steps with owners, triggers, and the evidence trail for each.
7. Check capacity: the bottleneck resource sets the throughput limit — state it in numbers.
8. Plan the transition: calendar dates, named owners, one pilot client, one rollback trigger.
9. Verify and hand off: checklist run, retrospective scheduled, metrics dashboard live.

This skill is part of an open-source agent skills collection. Extend it, adapt it to your context, and contribute improvements back through the project repository.