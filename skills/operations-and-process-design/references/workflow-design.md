# Workflow Design Methodology

## What a Workflow Is

A workflow is the sequence of states a single unit of work passes through from initiation to completion, together with the rules that govern state transitions and the queuing mechanisms that manage work items waiting at each state.

This is distinct from a process map. A process map shows who does what. A workflow design shows how work moves between states, how it queues when capacity is not infinite, and how the system behaves under load.

## Core State Model

Every workflow can be encoded in four elements:

- **States**: the named conditions a work item may be in (e.g., created, approved, in-progress, completed, canceled, rejected).
- **Transitions**: the allowed moves from one state to another (e.g., created → approved, approved → in-progress -- but not created → completed directly).
- **Actors**: the roles allowed to take each transition.
- **Guards**: the conditions that must be true before a transition is allowed.

### State Design Rules

- A work item must be in exactly one state at all times.
- No state can have overlapping transition permissions for two actors who are indifferent to each other.
- The state model must express every state in which a work item could be stalled -- if a ticket can sit untouched for a week, that waiting period must be a defined state.
- Terminal states absorb any incoming work item cleanly. The system must not produce orphaned items in a non-terminal state at the end of a business day.

### The Deadly States Problem

Most workflow designs have these implicit states:

| The caller says | The workflow says | The truth |
|----------------|------------------|-----------|
| assigned | assigned | waiting for someone to notice the assignment |
| in review | in review | blocking a reviewer who has not seen the item |
| waiting on client | waiting on client | the client stopped responding three weeks ago |
| done | completed | not yet integrated or shipped |

If your system does not separate waiting states from active states, your data describes a backlog you cannot see. The fix is to introduce explicit waiting states and measure how long items spend in them.

## Queues and Buffering

Every handoff is a queue. When a work item moves from one actor to the next, the receiving actor's queue is the number of items waiting for them. Queues are inescapable. The design question is whether the queues are visible.

### Measuring a Queue

- **Length**: the number of items waiting.
- **Age**: the time the oldest item has been waiting.
- **Arrival rate**: how many new items enter the queue per time unit.
- **Service rate**: how many items the resource can process per time unit.

### Rules for queue design

- A queue that nobody measures is a queue that nobody will drain. Each queue must have an owner and a visible size.
- Capacity for a queue should be sized for the 80th percentile of historical arrivals, not the average.
- The maximum acceptable age for an item in a queue must be defined before the queue is designed. This sets the urgency to press.
- When the service rate does not match the arrival rate, the only options are to increase service rate, reduce arrival rate (escalate to a triage step), or accept bounded delay. In the case of the last, announce the delay.

### Batching

Batching is the decision to accumulate items before processing them as a group. Batching affects lead time.

What happens to lead time when batching:

- Per-item lead time grows linearly with batch size.
- Per-item processing efficiency can increase (setup cost is amortized) or decrease (big batches get harder, frailer, more rework).
- The optimal batch size depends on variance and switching cost between task types.

If your process has a batch step, the batch size should be explicit. The default should be the smallest batch that makes a person willing to do the work.

## Bottleneck Theory Basics

A bottleneck is any resource whose capacity is less than or equal to the demand placed on it. The throughput of a system equals the capacity of its bottleneck.

### Finding the Bottleneck

1. Walk the floor. Find the resource with the largest backlog of items waiting for it.
2. Look for the resource that people avoid starting work items on because that step is painful.
3. Check which step everyone complains about when asked about delays.
4. Measure: total items entering the system per day divided by capacity of each station. The step with the highest ratio is the bottleneck.

### Protecting the Bottleneck

Once the bottleneck is identified:

- Do not let the bottleneck run out of work. Place a surplus buffer queue in front of it.
- Do not assign non-essential tasks to the bottleneck. The bottleneck should do only bottleneck work.
- Do not produce work for the bottleneck that fails the bottleneck's acceptance criteria. Incoming bad work at the bottleneck wastes the bottleneck's time.
- Measure the bottleneck's utilization. Target 80-90 percent utilization, not 100 percent. Bottlenecks at 100% cannot absorb variability.

### The Bottleneck Myth of Perfection

Improving a non-bottleneck step's efficiency does not increase the throughput of the system. It only increases the speed of waiting in the queue in front of the bottleneck. The only improvements that matter are improvements at the bottleneck.

## Little's Law in Practice

The fundamental equation of workflow: **WIP = Throughput × Cycle Time**

WIP: Work in Progress. Throughput: items completed per unit time. Cycle Time: the time an item stays in the system.

If you have three of these numbers, the fourth is determined. Most teams find that cycle time is best understood by dividing WIP by throughput.

A corollary: to reduce cycle time, you must reduce WIP or increase throughput. Reducing WIP is usually the easier lever.

## Capacity and Lead Time

Lead time = wait time in queues + processing time.

In almost any knowledge-work process, wait time dominates processing time by an order of magnitude. A five-minute review that sits in queue for three days is a three-day process. The queue time is the process time.

### Parking Spaces

Think of capacity as parking spaces in a lot. A process has a fixed number of spaces: some are occupied (work in progress), some are empty. When a new item arrives and no spot is open, the lot gates close. The owner of the lot has the option to add more spaces (increase capacity) or to reject incoming traffic (stop accepting work).

In process terms: finite engineered capacity, infinite demand, bounded WIP, admission control.

## Workflow Diagram Notation

A workflow diagram does not show lanes or actors. It shows:

- Circles or boxes for states
- Arrows for transitions
- A separate line for guard conditions (dashed arrows with the guard condition written beside them)
- An aggregate queue indicator line before each state to suggest relative queue size
- The bottleneck indicated with a B label

Keep the Hamming distance from states to transitions small: given 6 states, many transitions. Visual sprawl indicates poor design: too many states, too many transitions, totoo few states for what the model represents.

## Workflow Design Checklist

- Every possible state is in the model -- states include waiting, stalled, rejected, and dead-end states.
- Exactly one start state and one or more terminal states.
- Every transition has a known owner to authorize it.
- Guards are explicit for every transition that is not automatic.
- A work item can be in only one state at a time.
- The lead queue in interface of the bottleneck is the right-sized buffer.
- Non-bottlenecks are not starving the bottleneck.
- An explicit WIP limit is set for each queue.
- All states and transitions form a directed graph with no dead-end loops.
- The model includes a timeout or escalation for any state where an item can be held without a time commitment.