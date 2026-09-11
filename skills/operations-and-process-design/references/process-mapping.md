# Process Mapping Methodology

## Why Map a Process

A process map is the single most valuable artifact you can create before redesigning anything. It forces you to discover what actually happens, not what people believe happens. Every serious operations design starts with one.

## Swimlane Diagrams (Cross-Functional Flowcharts)

The standard notation for any process involving multiple roles or systems. Each lane belongs to one actor — a person, a role, a system, or an external party. Steps sit in the lane of whoever does them.

### Basic Shapes and Their Meanings

| Shape | Meaning | When to Use |
|-------|---------|-------------|
| Rounded rectangle | Start / End | One start, potentially multiple end states |
| Rectangle | Activity / Step | An action someone or something performs |
| Diamond | Decision / Gateway | A branch point; exactly one output at a time |
| Parallelogram | Data / Document / Handoff | Something produced or passed between lanes |
| Cylinder | Database / Storage | A permanent or semi-permanent store |
| Arrow | Sequence flow | Direction of work; label only when ambiguous |
| Dashed arrow | Information flow | Data that doesn't move the primary work token |
| Circle with label | Off-page connector | Continue the flow on another page |

### Swimlane Layout Conventions

- Lanes go top-to-bottom or left-to-right. Left-to-right is standard for wide processes; top-to-bottom fits vertical viewports.
- The first swimlane is the initiator — the actor that triggers the process.
- When a step produces output consumed by another lane, the arrow crosses the lane boundary at a right angle.
- Avoid arrow spaghetti. If more than three arrows cross between the same two lanes in sequence, consider consolidating steps or splitting the process.

### Building a Swimlane Map: Step Sequence

1. **Determine scope**. What trigger starts this process? What condition ends it? Draw a start oval and an end oval before placing any steps.
2. **List the actors**. Every person, system, or role that touches the work. One swimlane per actor.
3. **Walk the critical path**. The main flow from start to end. Place those steps first.
4. **Add exceptions and alternatives**. Return paths, rejection flows, timeouts. These are almost always the source of dropped steps.
5. **Label each handoff**. Every time work passes between lanes, the output must be explicit: what is handed over and in what form.
6. **Check for loops**. If a step leads back to a prior step, make that arrow explicit. Loops that aren't drawn indicate process gaps that cause frustration.
7. **Add decision points**. Every diamond must account for all possible outputs. A yes/no diamond that does not cover the no path is incomplete.

## Finding the Real Process (Not the Stated One)

Every organization has three versions of any process: the documented one, the one people say they follow, and the one they actually follow. Map the third one.

### Interview Techniques

- **Walk-through**. Ask the person to do the task while you watch. Do not ask them to describe it abstractly; the abstract version smooths over friction.
- **Recurring events**. Ask "what happened the last time this went wrong?" That story reveals enforcement mechanisms, informal overrides, and workarounds more efficiently than a happy path walk-through.
- **Six honest questions.** For every transition between actors, ask: Who does the work? What gets delivered? When does it happen? Where does it happen? Why is it done this way? How is it verified right?

### Ramp-up Detection

Three signals that the real process differs from the documented one:

1. **Local terminology**. People use words for steps or states that don't appear in any document.
2. **Shadow systems**. A spreadsheet, a notebook, or a separate Slack channel that tracks what the main system is supposed to track.
3. **Error absorption**. A person who catches problems caused by a broken handoff and fixes them silently without reporting the gap.

If you find any of these, the real process diverges from the documented one. Map the real one.

## Handoff Analysis

The fundamental unit of operations is one person handing a piece of work to another. Every handoff is a risk point.

### Handoff Anatomy

A complete handoff has:

- **Sender**: the person finishing their part.
- **Receiver**: the person continuing the part.
- **Token**: the work item being passed (a ticket, a doc, a code review, an approval).
- **Acceptance criteria**: the receiver's conditions for accepting the work token.
- **Trigger:** the event that tells the sender to transfer the token.
- **Feedback channel**: the avenue for returning work that does not meet acceptance criteria.

If any of these six elements are implicit, the handoff is incomplete and will cause dropped steps.

### Handoff Defect Categories

- **Lost token**. Work passes from A to B, B does not realize it arrived. No ticket, no acknowledgment. -- Fix: assign a tracking ID and require explicit acceptance.
- **Wrong format**: The work arrives in a format the receiver cannot process. -- Fix: define acceptance criteria and templates.
- **Wrong receiver**: The work goes to a person who does not have a role to handle it. -- Fix: enforce routing based on role, not person.
- **Missing context**: The work arrives without the information the receiver needs to act. -- Fix: define a minimum information package per handoff.
- **Dead handoff**: Work stalls because the receiver does not know they are the receiver. -- Fix: require a notification and an acknowledgment.

## Finding the Real Process: A Practical Pattern

When you suspect the documented flow does not match reality, use the tracking follow:

1. Ticket one work item all the way from trigger to settled.
2. Forget everything the process document says.
3. Exhaustively note what actually happens, including waiting periods, copied people, escalations, and exceptions.
4. Compare your empirical map to whatever official document exists.
5. The disagreement is your redesign opportunity list.

## Common Process Mapping Pitfalls

| Pitfall | Why it hurts | How to avoid it |
|---------|-------------|-----------------|
| Mapping too much at once | The diagram becomes unreadable and the team loses confidence | Stay within 15-20 steps per map; split into subprocesses |
| More than 1 decision diamond created with no else path | The map is incomplete | Force yourself to add the else path even if it is a dead end |
| Using people's names in swimlanes instead of roles | The map breaks when staff changes | Use role labels everywhere |
| Omitting rework loops | The map implies first-pass quality is perfect | Walk through one instance that had to go back and document the loop |
| Combining what is and what should be | The map is unusable for diagnosis | Draw the current-state map first and the target-state map second-draw them separately |
| Relying on one person's perspective | The map reflects that person's blind spots for which they lack visibility | Interview at least two people per lane |

## Process Map Quality Checklist

- The start trigger and the end state -- both defined.
- Each lane is a single role, and lane labels do not include specific names.
- Every diamond has a labeled output path for each possible outcome.
- Handoffs are labeled with what is handed over.
- The map includes at least one rework or exception path.
- Swimlanes left-to-right or top-to-bottom; each dedicated to a role.
- The total number of steps is between 8 and 20 for a single page.
- Connector lines do not cross each other more than once in the whole diagram.
- Each actor appears in exactly one lane.
- The map has a title, version field, and a revision date.

## Escaping Analysis Paralysis

Process mapping can consume unlimited time. The rule of thumb is: follow one work item at a time. When the map has accounted for 15 to 20 steps and the team can point to the specific step where things break, you have enough detail. Stop adding steps and start redesigning. The purpose of the map is not exhaustive knowledge; it is an improvement of the map.