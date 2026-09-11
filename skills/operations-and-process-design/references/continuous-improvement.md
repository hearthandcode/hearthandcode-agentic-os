# Continuous Improvement Methodology

## What Continuous Improvement Is

Continuous improvement is a systematic practice of making a process better a little bit at a time, based on real data, not gut feeling. It is not about big transformations. It is about the rhythm of observation and adjustment.

## The Kaizen Cycle

The simplest continuous improvement cycle is Plan-Do-Check-Act (PDCA):

- **Plan**: identify a change you believe will improve something measurable. Define how you will measure it.
- **Do**: make the change. Do it on a small scale; an hour, one batch, one day.
- **Check**: measure the result. Did it produce the expected outcome? What else changed?
- **Act**: if it worked, standardize the change so it stays, or try a different change from step 1 if it did not work.

Cycle duration: on a team that meets daily, one cycle, one proposed change. On a weekly meeting, one change. At a monthly meeting, it's also one change.

## One Change at a Time

The rule is that at any time, the team is testing exactly one process change. If multiple changes happen simultaneously, the isolating cause of cause and effect becomes impossible.

### Why one change matters

- **Attribution**: When only one thing changed, the result of that change can be attributed directly.
- **Cognitive load**: Two changes at once introduces variable interactions that people cannot easily reason about.
- **Revert simplicity**: If a change is harmful, reverting one change is easy. Reverting the interaction of two changes is not.

The only exception is a pre-planned change package that has been tested in a separate environment first.

## The Three Horizons of Improvement

- **Horizon 1 — Eliminate Known Pain**: obvious trouble steps: repeated handoffs, manual data entry, confusing forms, repeated questions. These are quickest to fix.
- **Horizon 2 — Increase Predictability**: the horizon of the system itself performs reliably. Simple jobs: define operating parameters, set schedules, clarify owner decisions.
- **Horizon 3 — Increase Resilience**: the system degrades gracefully under load. The horizon is the turning of the ou of process from a set of prescribed steps to a flexible practice that handles variance.

## Structuring a Retrospective

A retrospective is a structured meeting that produces improvements. Without structure, it becomes a complaint session.

### The Retrospective Template

1. **Gather Data**: What happened in the last period? List facts, not feelings. Use data from the process itself.
2. **Generate Insights**: Ask "What went well?" and "What did not go well?" Each person categorizes items individually. Then the group discusses.
3. **Decide on Improvements** : The group picks the main thing to change for the next period. Not everything, not the top three, but exactly one.

### The Countermeasure Format

Every improvement decision is recorded as:

| Problem | Root cause (not symptom) | Proposed countermeasure | Owner | Deadline |
|---------|---------------------------|-------------------------|-------|----------|

The countermeasure is recorded as a change to the workflow or an SOP. Decisions without also changing the workflow are not implemented.

### Retrospective Rhythm

- **After every delivery cycle**: the team reviews where improvements were made.
- **After a significant failure**: a blameless postmortem. The focus is the process, not the person.
- **After a significant success**: a success-reflect. Why did it go well? What does that tell you about the process?

For a two-person team like Pixel & Ink, the retrospective is 30 minutes every two weeks taped to an actual work delivery or calendar event. The medium is conversation, but the recording must be written. The one decision each cycle is the one countermeasure.

## Change One Thing

In a process, change intervention is limited to "change one thing" every improvement cycle. This prevents:

- Over-improvement that destabilizes the process.
- Skipping on monitoring the effect.
- Biasing conclusions by confounding variables.

### Doing "Change One Thing"

1. After the retrospective, pick the one item that has the largest impact on the most common problem.
2. The single improvement IS the change. It is made to the SOP, or the workflow, or the queue structure.
3. The improvement must be measurable. "Better communication" is not an improvement; "Add one Slack post at 9AM is."
4. The change takes effect immediately. Everyone knows the improvement has started.
5. The next cycle reviews the effect of last improvement before the next improvement.

## Standardize Before You Improve

This principle stands above all others: You cannot improve a process that is not standard. If each operator performs the work differently, the variations are different every time you change it.

First, standardize the process (SOP, step definitions, check)...Then, collect data on the standard process...Then, change to measure the effect. If the process changes from non-standard to improvement, the improvement has no baseline.

## The Improvement Velocity Metric

Traces the right metric to calibrate improvement: the lead time for identified improvement to reach standard process.

If a good idea from a retrospective takes six months to become part of the standard, the improvement speed is too low. Something in the governance layer (approval process, deployment pipeline, organizational culture) is blocking.

The metric: from the retrospective decision to the SOP being effective.

## Continuous Improvement Checklist

- The team has a defined improvement cycle (daily, weekly, bi-weekly) and holds the meeting.
- Exactly one improvement is active at a time.
- Each improvement is measured: what was the  metric level before, what was the metric level after.
- The improvement is recorded in the SOP or the workflow definition.
- A method exists to revert a change if it does not achieve the intended effect.
- The "after" measurement was conducted.
- The improvement was first implemented as a trial (small, time-boxed) and then standardized.
- The standard for the previous version of the process preceded the change.