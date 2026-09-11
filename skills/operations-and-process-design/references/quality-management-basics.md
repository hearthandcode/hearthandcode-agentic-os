# Quality Management Basics

## What Quality Means in Operations

Quality in an operations context is one thing: conformance to requirements. If the steps in the process match the SOP, and the SOP defines the correct way to do the work, the work is quality. This is a pragmatic definition that separates what operations can control from what it cannot.

### Requirements Triangle

Every piece of output has three dimensions of quality:

- **Output correctness**: the thing is right. The briefing matches the brand guidelines. The figure adds up correctly. The deliverable matches the brief.
- **Timeliness**: the thing is delivered at the time expected or earlier. Timeliness of a product is a separate property of quality, not a trade-off.
- **Format conformance**: the thing is in the expected form. Naming conventions, folder location, file type, header usage.

Any of these three can fail independently. A perfectly designed output delivered three days late is a defect. A document in the right folder with the wrong orientation is a defect.

## Definitions of Done

A definition of done is a list of criteria that must be true for a work item to be considered complete and movemout of the current step. Without a definition of done, quality is whatever the operator thinks it is, which varies from person to person and from morning to afternoon.

### Writing a Definition of Done

- Contains 3-7 criteria. More than that and it will not be checked.
- Each criterion must be binary — it is true or it is false. No "maybe" or "pretty much checked."
- Each criterion is independently verifiable by someone other than the performer.
- Examples: "The file is named according to the agreement in the client naming guide." "The deposit invoice says the correct amount."

The Definition of Done is reviewed by the person who receives the work, not the person who produces the work. The receiver has the exact perspective on what ready means.

## Inspection Points

An inspection point is a pre-defined gate in the process at which the output from the previous step is checked before the current step is allowed to proceed.

### Selecting Inspection Points

Inspect at these natural points:

- Before a handoff to someone else.
- Before a cost accrues (hours still billable, materials already bought).
- Before a deadline-bound output is released to an external party.
- Before an output is the foundation for other work.

### Types of Inspection

- **Complete inspection**: the recipient checks everything, step by step. Expensive but appropriate for high-cost or high-risk outputs.
- **Sampling inspection**: The recipient samples randomly from the output. OK for high-volume low-risk work.
- **Peer review**: an independent person checks the output against the definition of done. The standard for SOP clarity.

### What to Document in an Inspection

For each defect found:

- What step produced it.
- What was wrong specifically.
- The root cause, determined by briefly probing the cause (it is the act of producing the step, the step's instructions, or something missing upstream).
- Whether it's an opening-and-return or a fix-in-place.

Fixed-in-place items are fast on the critical path. Opening-and-return items require the work to loop back to an earlier process. They are the ones to address from a redesign perspective.

## Escape Analysis

An escape is a defect that passed through all the inspection points and was caught by an external entity (the client, the customer, the end user). Escapes are the most important defects to analyze because they reveal a gap in your inspections.

### Escape Pathway

For each escape:

1. Where was the defect introduced in the process?
2. Where should it have been caught? (Which inspection point was supposed to catch it.)
3. Why did the inspection point not catch it? (Not executed? Executed incorrectly? Not powerful enough?
)

Once you trace these three steps, you fix the missing inspection. Not the SOP in the original step always — the inspection step. The original step still might be faulty, but the escape implies the inspection point is what let the defect out.

## Quality Baselines

A quality baseline is a measurement taken before a change to establish the current defect rate.

### Useful Baselines

- Defects per 100 outputs.
- Defects per handoff.
- Elapsed time spent on rework per output as a percentage of total production time for that output.
- Number of non-critical defects caught by the client.
- Cycle time for a defect to be caught, starting from when it was introduced (days).

Set a baseline before you change anything. After the change, measure the same metric. The difference is the effect of the change. Without a pre-change baseline, you have no signal.

## Quality Management Checklist

- Each step in the process has a Definition of Done that is written down and known to the performer.
- Each Definition of Done has 3-7 concrete, binary, verifiable criteria.
- Each handoff includes a check against the receiving side's criteria before acceptance.
- Each inspection point is explicitly identified by text point in the workflow and which agent does it.
- Escapes are tracked: each one has a record of what escaped, when, and which inspection point failed.
- The quality process includes at least one baseline metric measured before changes are made.
- Quality performance is reviewed at regular intervals (weekly or the rhythm of the process).
- The quality manager is an explicit role, not a standby.
- Quality improvements are tied to specific changes in the process, not a general exhortation.
- The quality of output in a process is measured as a function of upstream conditions, not only downstream effort.

## Common Quality Management Mistakes

- **Adding inspection before fixing root causes**. Defect from poor training will not be caught by a review; the review then becomes a crutch that slows the process without improving.
- **Making the definition of Done too long**. The operator cannot handle 35 criteria. They will check 35 into a list of repeating checklists.
- **Over inspection**: every step is blocked by an inspector's queue. The workflow slows and the team ignores inspections on critical steps.
- **Punishing escapes punitively**. If people are blamed for escapes, they will hide them. Track defects without personal attribution.
- **Mixing project mgt quality and process quality**. The project manager's quality target (keep the schedule) is different from process quality (do it right). Do not re-define the process quality to get schedule relief.