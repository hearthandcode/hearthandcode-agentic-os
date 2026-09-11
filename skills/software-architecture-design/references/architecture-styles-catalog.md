# Architecture Styles Catalog — Layered, Hexagonal, Event-Driven, Microkernel

An architecture style is a prepackaged answer to "where do responsibilities live and how do components talk." Styles are not good or bad; each buys specific qualities at specific prices. This catalog gives the structure, the forces each style serves, the price you pay, and the signals that say it fits. For the style-selection procedure, see the workflow in SKILL.md (Step 6); for scoring two styles against your scenarios, use the table at the end.

## 1. Layered

**Structure:** Code organized into horizontal layers, each allowed to depend only on the layer below. The classic four: presentation → business logic → data access → database. Requests descend; responses ascend.

```
[presentation]     controllers, CLI, UI components
      ↓
[business logic]   domain rules, use cases
      ↓
[data access]      repositories, queries, mappers
      ↓
[database]
```

**Serves well:** time-to-market, familiar onboarding (every developer knows the shape), straightforward call-stack debugging, and small-to-medium systems where the domain is not yet stable.

**Costs:** business logic drifts toward whatever layer is most convenient — queries creep into controllers, rules creep into SQL. The database becomes the center of gravity: data access is defined *after* the schema, so the data model shapes the domain instead of the reverse. Testing a use case requires the layers below it.

**Fits when:** the team is small, the domain is CRUD-flavored, and the primary quality demand is shipping features weekly. Typical failure mode: after a year, the "layers" are folders, and the dependency rule exists only in the README.

**Fit check:** will someone actively enforce the dependency direction? If not, you are buying the cost of ceremony (interfaces per layer, DTO mapping) without the benefit (isolated layers).

## 2. Hexagonal (Ports and Adapters)

**Structure:** The domain and use cases sit at the center and own no knowledge of infrastructure. The center defines **ports** — interfaces the core needs (a `NoteRepository` port, a `MailSender` port) or exposes (an `OrderService` API). **Adapters** implement ports on the outside: a Postgres adapter, an HTTP adapter, an in-memory adapter for tests. Dependencies point inward only.

```
        [HTTP adapter]   [CLI adapter]
              ↓               ↓
    ┌──────────────────────────────────┐
    │  core: use cases + domain rules  │
    │  defines ports it needs/exposes  │
    └──────────────────────────────────┘
        ↑               ↑
  [Postgres adapter] [mail adapter]
```

**Serves well:** testability (run use cases against in-memory adapters), storage and delivery-mechanism swappability, keeping domain logic independent of framework churn, and long-lived systems whose infrastructure will change several times.

**Costs:** indirection up front — ports and mapping code exist before any benefit is visible; teams without discipline turn "ports" into leaky pass-throughs of framework types. More ceremony than layered for genuinely CRUD-shaped systems.

**Fits when:** the core logic is rich and long-lived; infrastructure replacement or dual-running is plausible; testing without infrastructure is a stated need. Also the natural style for a *modular monolith*: each module exposes ports, and module-to-module calls go through ports, keeping extraction to a service cheap.

**Fit check:** name the infrastructure you expect to replace or the extraction you expect to perform. If you cannot, you are buying insurance for a fire you have no reason to expect.

## 3. Event-Driven

**Structure:** Components do not call each other; they publish events (facts that happened: `OrderPlaced`, `NoteUpdated`) and subscribe to events they care about. Communication is asynchronous through a broker (or in-process event bus); producers do not know consumers.

```
[Orders] --publish OrderPlaced--> [broker/bus]
                                     ├──> [Inventory] reacts
                                     ├──> [Email] reacts
                                     └──> [Analytics] reacts
```

**Serves well:** independent evolution (add a consumer without touching producers), load absorption (spiky writes queue instead of cascading), horizontal scaling per consumer, and integration across team boundaries where synchronous coupling would create change-freeze chains.

**Costs — all of them operational:** eventual consistency becomes the default and every reader must handle staleness and duplicates; debugging a flow means correlating events across components; failure handling needs dead-letter queues, retries, idempotency; the total behavior of the system is emergent and no single call stack describes it.

**Fits when:** components have genuinely independent scaling or release cadences; the consistency requirements tolerate seconds-to-minutes of lag; the organization can operate the machinery (tracing, DLQs, replay tooling). Not fitted when one team operates everything and call-stack thinking would do — event-driven adds distributed-systems cost without a distributed-team benefit.

**Fit check:** for each event flow, can you state what the user sees during the consistency lag? If the answer is "they see stale data and we hope it's fine," the style is not fitting that flow yet.

## 4. Microkernel (Plug-in)

**Structure:** A small, stable core system with minimal logic, surrounded by plug-in modules that implement features or extensions. The core defines the plug-in contract — registration points, extension APIs, shared services. Most of the system's functionality lives in plug-ins.

```
[plug-in A] [plug-in B] [plug-in C]      third parties or feature teams
     └──────────┼──────────────┘
        [microkernel core]
   contract: registration, extension API,
   shared services, isolation boundaries
```

**Serves well:** systems where third parties (or many teams) extend a stable core without core changes: editors, build tools, commerce platforms, automation engines. Isolation of extension failure; independent release of extensions; a core that can be audited small.

**Costs:** the plug-in contract is a public API — designing it well is the whole difficulty, and breaking it is expensive once plug-ins exist in the wild. Core must anticipate extension points; wrong guesses produce plug-ins full of workarounds. Performance tax at boundaries; versioning burden (N plug-ins × M core versions).

**Fits when:** extensibility by parties you do not control is the *product*. Overkill when the "plug-ins" are just your own feature modules — use modular layering or hexagonal instead.

**Fit check:** list the parties who will extend the system without your involvement. If the list is only your own team, choose a simpler modular style and keep the option of a plug-in contract open.

## Choosing among styles — the comparison table

Score each candidate style 1-5 against your top scenarios, then score the operational row honestly:

| Criterion | Layered | Hexagonal | Event-driven | Microkernel |
|---|---|---|---|---|
| Time-to-first-feature | 5 | 3 | 2 | 2 |
| Domain-logic testability w/o infrastructure | 2 | 5 | 3 | 3 |
| Independent scaling of parts | 1 | 1 | 5 | 2 |
| Independent evolution by outside parties | 1 | 2 | 4 | 5 |
| Operational simplicity (one team, no broker) | 5 | 5 | 1 | 3 |
| Ease of later extraction to services | 2 | 4 | 4 | 2 |
| Debuggability (call-stack thinking) | 5 | 4 | 2 | 4 |

Rules for using the table:

1. **Score your scenarios, not the style in the abstract.** The numbers above are defaults; your Q1-Q6 scenario table (SKILL.md Step 2) re-weights them.
2. **The operational row is scored last and cannot be gamed.** If nobody on the team has operated a message broker in production, event-driven's operational score for *your* team is lower than the catalog value.
3. **Styles compose by area.** A hexagonal modular monolith may use in-process events internally and adopt a broker later behind the same port — record that as the revisit trigger, not as a present-tense commitment.
4. **The default is boring.** If two styles score within a point, take the one with fewer moving parts. Complexity must be purchased by a scenario, not by ambition.
