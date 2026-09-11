# Capacity Planning Methodology

## What Capacity Planning Is

Capacity planning is the disciplined answer to the question: "Given the work we have coming in and the resources we currently have, can we deliver on schedule without overloading the people?" It is a routine practice, not a one-time exercise. Calendars, budgets, and staffing decisions emerge from it.

## Estimating Capacity

Capacity is not a fixed number. It is the number of hours available per week multiplied by the kind of work done and the utilization rate that the organization can sustain.

### Formula

**Available capacity per person = Total available hours per week × Utilization target × Skill-specific efficiency**

Total available hours -- The contractual hours, minus meetings, administrative overhead, and any mandatory company time.

Utilization target is the sustainable fraction of total hours spent on productive work. For knowledge work settings, 60 to 75 percent is real; above 85% leads to burnout and degradation.

Skill-specific efficiency: a learning-and-practice factor that reflects whether the person has done similar work before. A first-time task yields 0.5 or 0.6 of full efficiency. The second time yields 0.8, and from the third on it's nearly 1.0.

### Team-Level Capacity

Sum capacity across the team for the same work type category. If the team splits across disciplinary boundaries (design, development, ops), calculate each category separately. Do not sum across categories for planning purposes; it produces the bus that says "we have 40 hours" for a two-person design team.

### Demand Estimation

The counterpart to capacity is demand. For each work item type, estimate:

- **Volume**: how many items of this type arrive per time unit? (Watch for seasonality: past-month averages can mask a 2x spike at month end.)
- **Effort**: how many person-hours does one unit of this work type consume? Use historical data over estimates. If no historical data exists, the first three occurrences are tracked manually to calibrate.
- **Due dates**: which items have hard deadlines? Hard deadlines consume capacity early because the slack is at the front of the schedule, not the back.
- **Recurring overhead**: maintenance, triage, internal requests, and other non-project work. Estimate this if you use this type; if you don't, you are double-booking the team.

## Demand-to-Capacity Ratio

The summary statistic: billable hours on the calendar / realistic hours available.

If the ratio is below 0.8: you have unused capacity that could be directed to improvement, learning, or proactive work. If between 0.8 and 1.0: tight but sustainable with moderate buffers. If above 1.0: the system is overbooked, lead times will stretch, and quality will degrade.

## Capacity Buffers

A buffer is capacity intentionally left unbooked to absorb variability.

### Types of Buffers

- **Demand buffer**: capacity held because demand has inherent variability. A team handling 10 unplanned items per week that expects 10 holds 15 hours of buffer.
- **Switch buffer**: capacity set aside to allow a team member to transition between disparate task types without disrupting flow.
- **Emergency buffer**: capacity held for organizational fires. This is explicitly authorized by the team and sometimes the account's project sponsors.

### Buffer Sizing

A buffer that is too large invites organizational slack. A buffer that is too small guarantees delay. The right size is:

Identify the variation. If historical arrivals vary by 20% around the mean, set the buffer to at least 20% of capacity.

Explicit rules for the buffer in drawings: You may burn buffer time only when specific exceptions occur: unplanned work, a team member is sick, a critical client change. Buffer is not overflow for all planning errors.

## Saying No

The hardest part of capacity planning is declining work. Without a structured way to say no, a team takes on everything and delivers nothing well.

### Structuring the No

- **State the capacity**: "We have capped at 40 hours of capacity per design sprint, and the entire sprint is already full of existing engagements."
- **Show the impact**: "Taking this work would push the delivery on the Storrs project by 10 days."
- **Offer an alternative**: "We can start this work when the Harris report is delivered, which opens a slot on October 10."
- **Accept trade-offs**: If the client needs the work regardless, then a triage choice must be made: delay the existing work, reduce the scope of the existing work, or add capacity. No invisible deferrals.

### No as a Service

The "no" is not personal. It is a professional assessment of capacity. People who routinely skip this decision are the people who deliver late, quality-degraded output consistently. Routine no is a discipline, not a negativity.

## Planning Horizon Pyramid

- **Strategic (quarterly)**: rolling 12-week forecast of incoming work, capacity adjustments, and resourcing decisions.
- **Tactical (bi-weekly)**: the next two sprints or similar cycle: What is committed, what is forecast, and what buffer to create?
- **Operational (daily)**: standup or daily review: what moves today, which blockers are notable, and are the effective queues drifting toward burnout?

## Forward-Looking Capacity Indicators

Before the crash: a set of metrics to watch. Any of these going in the wrong direction means a capacity mismatch will occur in the next 2 to 4 weeks:

- Queues are increasing but not being reduced every week.
- Unplanned work percentage of total hours is above 30%.
- Overtime is being used consistently beyond 2 consecutive weeks.
- The number of items that reach the "stalled" state due to person overloading increases.

## Capacity Planning Checklist

- The work period (week, month, quarter) has a defined capacity in hours.
- Demand for the period is estimated for each work type.
- The capacity-demand ratio is below 1.0. If not, exceeding the capacity aligns with the bound on the maximum week.
- A buffer of 15-25% is held per person per week.
- Inbound unplanned work acceptance has a process: is it ticketed, evaluated for fit, and does the capacity for it exist?
- Buffer consumption is tracked: how much was used and for what reason.
- Hard deadlines are flagged on the calendar ahead of than they happen.
- The plan includes at least one appropriate "no" if the ratio is above 1.0.
- The checkpoint: if all existing work proceeds at normal velocity, what workload looks like after adding this to capacity.
- Recurring overhead and maintenance have a line item hours.