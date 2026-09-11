# Process Map Template

Use this template to create a swimlane process map. Fill in the fields below and draw the map according to the process-mapping reference. A good map is 8-20 steps, uses explicit handoffs, and captures both the happy path and at least one exception.

---

## 1. Map Metadata

| Field | Value |
|-------|-------|
| Process name | |
| Version | |
| Author | |
| Date created | |
| Date last updated | |
| Process scope (trigger → end state) | |
| Favored tool for rendering | [Lucid, Miro, Excalidraw, pen+paper, yEd] |

---

## 2. Actors / Swimlanes

Define one swimlane for each distinct role. Do NOT list people's real names — use role labels.

| Lane # | Role Name | Role Description | Replaces (previous process actor names) |
|--------|-----------|-----------------|----------------------------------------|
| 1 | [role] | [what this role does in this process] | |
| 2 | [role] | [what this role does in this process] | |
| 3 | [role] | [what this role does in this process] | |
| 4 | [role] | [what this role does in this process] | |
| 5 | [role] | [what this role does in this process] | |

## 3. Trigger

What event causes this process to begin?

> **Start**: [e.g., "Client interest is received via email/contact form."]

## 4. End State(s)

What condition(s) must be true for the process to conclude?

> **End**: [e.g., "Project is complete and all invoices have been paid."]

| Alternate End State | Triggering Condition |
|---------------------|----------------------|
| [e.g., "Canceled"] | [e.g., "Client withdraws before contract."] |
| [e.g., "Stalled"] | [e.g., "Assets not received after 14 days, zombie status."] |

---

## 5. Step Inventory

List process steps sequentially. One row per box on the map (each rectangle or diamond). For each step, provide:

| # | Step Name | Actor (Lane) | Step Type | Input(s) | Output(s) / Handoff | Verifiable Check |
|---|-----------|-------------|-----------|----------|-------------------|-------------------|
| 1 | | | [Activity / Decision / Handoff] | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |
| 13 | | | | | | |
| 14 | | | | | | |
| 15 | | | | | | |

**Step type guidelines:** Activity (action step), Decision (branch point — must have both YES and NO paths labeled on the map — fill in the Decision Paths section below), Handoff (output goes to another lane), Wait (time-based pause), Storage (DB/file — cylinder notation only when the work item is stored permanently).

---

## 6. Decision Paths

For every Decision row in the inventory:

**Decision step #___: [Step name]**

| Condition | Outcome / Next Step | Notes |
|-----------|--------------------|-------|
| YES / PASS | → Step # | |
| NO / FAIL | → Step # | |
| [Third condition] | → Step # | |

---

## 7. Handoff Table

For every time work crosses from one swimlane to another, complete the following table.

| Step # | Sender Role | Receiver Role | Token / Deliverable | Acceptance Criteria | Trigger | Feedback Channel |
|--------|------------|--------------|--------------------|--------------------|---------|------------------|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |

---

## 8. Exceptions / Loops

| Return loop from step | Back to step | Reason for loop (condition) | Owner |
|-----------------------|-------------|---------------------------|-------|
| | | | |
| | | | |

---

## 9. Map Quality Check

After the map is complete, run through the checklist from reference/process-mapping.md:

- [ ] The map has a title, version, and date.
- [ ] Start trigger and end states are defined.
- [ ] Each lane represents exactly one role.
- [ ] Every decision diamond has labeled YES and NO paths.
- [ ] Handoffs are labeled with the token being handed over.
- [ ] At least one exception or rework loop is documented.
- [ ] The total number of steps is between  8 and 20.
- [ ] Connector lines cross each other at most once.
- [ ] Each actor appears in exactly one lane.

---

## 10. Map Output Notes

The final map should be a visual (diagram) in whatever tool the team uses, attached to this template. The template captures the structured data for the map so that you can re-generate the diagram later.

The table at section 8 (Exceptions/Loops) is used as a starting point for the Dropped-Step Analysis. The analysis will take entries 8 and match them to root causes in the process. Then during the redesign, the points they reveal are the main change indicators.