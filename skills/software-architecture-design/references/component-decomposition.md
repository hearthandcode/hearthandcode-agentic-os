# Component Decomposition — Cohesion, Coupling, Boundary Discovery

Decomposition is the act of drawing the lines. Everything else in architecture — styles, interfaces, data ownership — depends on where the lines fall, and the lines are expensive to move once code accretes around them. This reference gives the two forces (cohesion, coupling), the tests that find real boundaries, and the corrections that fix bad ones.

## Cohesion: things that change together live together

Cohesion measures how strongly a component's internal responsibilities belong together. The practical test is **change together, live together**:

- **High cohesion:** a `Pricing` module where price calculation, discount rules, and currency rounding all change when pricing policy changes. One reason to change, many related behaviors.
- **Low cohesion:** a `Utils` module where date formatting, discount rules, and HTTP wrappers live because "they had to go somewhere." Multiple unrelated reasons to change.

Signals of low cohesion to watch for in a draft decomposition:

1. The component's purpose statement needs "and" to be stated ("handles validation *and* rendering *and* persistence").
2. Changes to the component come from unrelated stakeholders (finance wants pricing changed; operations wants the HTTP wrapper changed).
3. Half the component's code is touched by any feature.
4. The component has a "misc" or "helpers" area that grows monotonically.

The remedy is not smaller components — it is grouping by *reason to change*, not by technical kind. "All services" or "all models" is technical layering; "all pricing behavior" is a cohesive responsibility.

## Coupling: how much knowing is shared across the line

Coupling measures how much one component must know about another to do its job. Some coupling is unavoidable (components exist to compose); the design question is *what kind*:

| Coupling kind | Example | Verdict |
|---|---|---|
| **Data coupling** | Caller passes a note ID, gets a note back | Healthy — the good kind |
| **Interface coupling** | Caller depends on a declared port/interface | Healthy, and enables testing |
| **Temporal coupling** | B only works if A ran in the same second | Fix — makes ordering invisible |
| **Content coupling** | B reaches into A's tables/structs | Fix — boundary is fiction |
| **Shared-data coupling** | Both write one table outside any contract | Fix — pick an owner |
| **Message coupling** | B reacts to A's events, knows only the schema | Low, but adds consistency cost |

Two corollaries that matter more than the taxonomy:

- **Coupling through interfaces beats coupling through data format.** A caller depending on `NoteRepository.get(id)` survives storage changes; a caller depending on the notes table's column layout does not.
- **Event coupling hides ordering assumptions.** If B's correctness requires that A's event arrived, that is temporal coupling wearing an event costume. Either tolerate the delay explicitly or make the dependency synchronous.

## The seven boundary tests

Run these on every proposed boundary. A boundary that fails three or more is probably a folder, not a component.

1. **One-sentence purpose.** "Store and serve notes per ACL." If you need "and," split. If you cannot write the sentence, you have not found the component yet.
2. **The change-together test.** Name the two most likely near-term changes for the system. Each should land inside one component.
3. **The tell-nothing test.** Could the component's internals be rewritten — different language, different storage — without any caller changing? If callers reach past the interface, the boundary is decorative.
4. **The standalone-test test.** Could this component be unit-tested without booting other components? (In-memory doubles count; the real database in a container is integration, not a substitute.)
5. **The naming test.** Component names are nouns with clear scope ("Notes," "Access," "Search"). Verbs in component names ("NoteManager," "NoteProcessor") signal grab-bags.
6. **The data-ownership test.** Each entity's write path belongs to exactly one component. Two writers = no boundary.
7. **The deletion test.** Could this component be removed and replaced without archaeology? If its removal requires archaeology, its interface is not the contract — its internals are.

## Discovering boundaries: the four probes

When starting from scratch, these probes produce candidate components. Expect to run all four and reconcile.

### 1. Functional responsibilities
List the verbs of the system ("store notes, check permissions, index for search, notify shares"). Group verbs that serve the same actor and purpose. Verbs that always fire together are one component; verbs with different reasons to change split.

### 2. Data ownership
List the entities. Group entities that are written by the same workflows. An entity written by two workflows is either two entities with different owners or one entity with one owning component — resolve it now, not after both writers exist.

### 3. Rate of change
List what changes often (product rules, permissions) and what changes rarely (storage engines, protocols). Different rates of change want different components — the often-changing code should be a place you can edit without re-reading the stable code.

### 4. Failure isolation
Ask which parts may fail without taking the product down. Search being down is survivable; auth being down is not. Components whose failures have different blast radii want boundaries between them — this probe is where the decision to extract a component to its own process usually comes from.

## Boundary anti-patterns

- **The god component.** "Core" that everything imports. Usually an accretion, not a design. Fix: extract the two most-changed areas first, repeat.
- **The boundary everywhere.** Ten components for a system that fits in three. Every boundary is a contract to maintain; boundaries cost maintenance. A system with three components and clean ownership beats one with ten and muddy ones.
- **The layers-as-components mistake.** "Controllers / Services / Repositories" is layering, not decomposition — every feature touches all of them. Decompose by responsibility area (Notes, Access, Search), layer *within* a component if needed.
- **The anemic boundary.** A component that is pure CRUD over a table with no rules. Sometimes correct (a thin owner is fine); if there are rules about that data scattered in callers, the rules belong inside the owner.
- **The chatty boundary.** Two components that make dozens of small calls per user action. Either the boundary is wrong, or the interface needs a coarser operation — both fixes are cheaper than the latency and fragility of chatter.

## Refactoring a bad decomposition

1. **Write the current boundaries down honestly** — as they are in the code, not the slide. Every arrow that exists in reality gets drawn, including the ugly ones.
2. **Find the worst coupling first** (content or shared-data coupling) and fix ownership — this pays for itself even if nothing else changes.
3. **Move code by behavior, not by file.** A move is safe when tests move with the behavior and the receiving component's interface gains the operation.
4. **One boundary change per release.** Decomposition refactors that move five components at once cannot be attributed or reverted. Sequence them.
5. **Record the new boundary in an ADR** with the test results — which of the seven tests the old boundary failed and how the new one passes them.