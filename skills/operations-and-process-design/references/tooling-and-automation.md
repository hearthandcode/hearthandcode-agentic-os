# Tooling and Automation Checklist

## The Decision to Automate

Automation is not always the right answer. A manual process that runs three times a week is not worth automating. A manual process that runs three hundred times a day and produces predictable errors is a candidate. This reference helps you decide.

## When to Automate

### Strong signals: automate now

- The task is repeated at least once per day per person, and the steps are identical each time.
- The same error occurs in the manual execution at least 5% of the time.
- The manual process requires someone to wait for an external system to advance to the next state before proceeding to the next step.
- A handoff to another system currently requires a human being copying data from one place to another (copy-paste operations are a red flag for automatable).

### Weak signals: consider

- The task requires a decision that follows a deterministic pattern: "If X is true," "then you do." For deterministic O patterns, an automated decision is reliable.
- The manual process involves two or more record-keeping actions across a system in sequence. If the operator must enter the same piece of data into two fields in different systems, the data entry is redundant.
- The task is performed reliably by a single person who is the only person who knows the process. The hidden threat of the process is a human bus factor. Automate to reduce that risk.

### Strong signals: do not automate

- The process involves a judgment call that cannot be reduced to a set of rules.
- The process output is used by a single person or internal team in a low-frequency context.
- The process is not yet stable: it changes every two weeks. Automating a moving target will waste more time than it saves.
- Automation tools would cost more in infrastructure or subscription fees than the hourly cost of the manual work over two years.
- The process requires extracting structured data from unstructured input (free-form emails, browser screenshots) -- these often require more human repair time than the saved.

## Build vs. Buy Decision

For any proposed automation:

### Questions to answer

1. Is there an existing tool that does exactly this? Do not use build thinking when a plug-and-play solution exists.
2. If no exact tool exists, is there a short combo or two tools that would achieve what the custom tool does? The custom build's cost is not only the engineering. It is the maintenance over time.
3. If building, what is the expected workload for the tool? An automation for a two-person team is built differently than a full auto for a 50-person team. Build small, refactor when needed.
4. Does the tool need to integrate with any of the operational tools that are not web-API compatible? If the target lacks an API, building an automation is not a software project; it is a process redesign.

### The buy threshold

"Buy" the tool if any of these is true:

- The cost of the tool over 2 years is less than the cost of building and maintaining the custom tool in the same period.
- The tool is used for two months and shuts down. The ongoing subscription is less than the cost of developer time.
- The tool has a documented non-API integration with the current workflow system. A listed integration that works.

### The build threshold

Build if all of these are true:

- No suitable existing tool exists.
- The automation has a clear ongoing maintainer.
- The automation either integrates as a no-customization to an API-based tool OR reduces the cognitive load of the system by at least 30% of manual effort.
- The automation affect a high-volume, stable internal process.

## Automation Risk

| Risk | Consequence | Mitigation |
|------|-------------|------------|
| Honest errors are automated faster | The bad process becomes faster and more frequent mistakes | Run the automation in parallel with manual for 1 week, validate 100% |
| Uncritical assumption | Fallible conditions change silently, and the automation fails | Include a conspicuous manual check-in point in the workflow |
| Over-automation | The operator stops monitoring the output | Every automated steps has a periodic check point |
| Brittle external dependency | The tool breaks when external API changes lead to silent data loss | Time-box the unmantainable external dependency and replace within 6 months |
| Zombied automation | Operator stops verifying the automation's output | The automation must report is "done" and the result always seen by a human before action |
| No escape | If automation is down, there is no manual procedure to fall back on | Keep the manual SOP written when automation is created |

## The Automation Readiness Checklist

Before building a tool, complete check each of these:

- [ ] The process is standardized: there is a written SOP and it is followed.
- [ ] The process is stable: no modifications to the way the work is performed have been made in the last 30 days.
- [ ] The process is deterministic: the output for a known input is always the same.
- [ ] Automation directly saves at least 1 hour/week of human time.
- [ ] The process has an owner who will maintain the automation.
- [ ] Data entering the automated step is in machine-readable format (not human-generated free text).
- [ ] A manual alternative is both known and written in the backup SOP.
- [ ] The automation run does not require an external system that we cannot reach.
- [ ] There is a clearly documented process for the first error of the automation.
- [ ] The tool itself is cheap to buy or simple to build (under two days of effort for a two-person shop).

## Automation Maintenance Cadence

- **Weekly**: check the automation's error log if it produces one.
- **Monthly**: confirm the automation still runs against the actual production environment.
- **Quarterly**: verify that the process the automation is attached to has not changed.
- **Upon incident**: apply the post mortem to the automation itself: what went wrong, is there fallback, and what should be updated.

## Integration Checklist

Integrate automation across tools in order given:

1. **Communication**: an email to Slack notification when a work item enters a certain queue.
2. **Task management**: create a card in the project tracker when a new item arrives in a shared imap.
3. **Document management**: template generation, auto-fill from data, and file naming.
4. **Billing**: invoice generation based on project milestones and time logs.
5. **Track**: automated handoff transitions on completion of a step.

For a two-person agency, steps 1 and 2 give the biggest pain relief with the lowest setup complexity.

## Automation Stack

For a small service business:

- **Task tracker**: open-source or free-tier: Linear, Plane, or plain GitHub Issues.
- **Automation integrator**: n8n (hosted self or Bulldog) or Make (cloud).
- **Document generator**: Google Docs API. Template with placeholders. No PDF generation engine required.
- **Bot communication**: Slack webhooks. Free tier for a channel, no premium.

Any automation platform should be:

- Running on a machine you control or a vendor that provides logs and alerting.
- Adjustable without programming knowledge for the next person to support it.
- Documented: the tool's purpose, the flow, the testing steps.