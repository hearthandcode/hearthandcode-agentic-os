---
name: software-architecture-design
description: >
  Load this skill when you are starting a new system or major subsystem, choosing
  between architecture styles, documenting decisions for a team, or reviewing an
  existing architecture. It walks from quality-attribute scenarios through component
  decomposition to recorded decisions (ADRs) and a review pass, producing an
  architecture overview, decision records, and findings you can defend to a team.
---

# software-architecture-design

## 01 — Purpose

- Software architecture is the set of decisions about a system's shape that are expensive to change later: what the major components are, who talks to whom, where state lives, and which qualities the design must guarantee versus trade away.
- Architecture is not the diagram on the wall.
- It is the reasoning behind the diagram, written down while the reasoning is fresh and findable long after the people have moved on.
- This skill walks one complete, defensible design pass, from fuzzy requirements to a reviewed, recorded design that production code can be written against.
- The pass has five movements: frame the problem as quality-attribute scenarios; decompose into components with real boundaries; choose and justify a style; design interfaces and the data model; record decisions as ADRs and review the whole.
- You can run the full pass in one to three working days for a small system, or spread it across a week of part-time work on a larger one.
- The economics justify the time: a design flaw caught in this pass costs an afternoon to fix; the same flaw caught after launch costs a migration, an incident, or both.

**Three outcomes this skill owns:**

1. **A component decomposition with explicit boundaries.**
   - For each component you can state its responsibility in one sentence, its collaborators, its owned data, and the reason the boundary exists.
   - Each boundary passes named tests (one-sentence purpose, tell-nothing, data ownership) rather than resting on intuition.
   - The decomposition is small enough to hold in one head and honest enough to survive the team's growth.
   - You can point at the table row that proves each claim.
2. **Decision records a new engineer can read in twenty minutes.**
   - The records show not just *what* was chosen but *why*, which alternatives were rejected and on what argument, and under what observable conditions the choice should be revisited.
   - The records are immutable once accepted, so they remain trustworthy as history.
   - New ADRs link backward (supersedes, relates-to), so the decision history reads as one connected document.
3. **A reviewed design that survives a skeptic.**
   - Every important claim is tied to a scenario, a measurement, or a named trade-off.
   - Every review finding carries a recorded disposition: fixed, accepted with rationale, or tracked as a decision.
   - A repeat reviewer can verify the dispositions in minutes because each one names its evidence.
   - The sacrifice list is explicit, so the design is honest about what it chose not to do.

- The skill assumes a practitioner who can program and read a schema, but who may never have run a formal design exercise.
- It teaches the craft itself: how to elicit scenarios from slogans, how to test whether a boundary is real, how to write an ADR that stays useful for years.
- The skill is stack-agnostic; its examples use Postgres, REST, and event publishing because they are common, not because they are required.
- It works for a lone engineer who must decide and record alone, and for a team running the pass as a facilitated exercise.
- The artifacts interlock deliberately: scenarios justify boundaries, boundaries carry ownership, ownership constrains the data model, and every consequential choice lands in an ADR — skip a layer and the later layers inherit the gap.
- The workflow is deliberately sequential but not rigid: Steps 5-8 iterate as decomposition reveals interface and data questions, and you should expect to loop between them two or three times on a real system.
- What you should NOT expect: a tool that generates the design for you. The skill structures your judgment; it does not replace it. Every artifact carries your reasoning, which is why the records stay useful.
- What you SHOULD expect: the review step to hurt a little. Finding five real problems in your own fresh design is the pass working, not failing.
- It does not cover line-level code feedback (see `code-review`), test planning (see `testing-strategy`), or vendor scoring — it covers the decisions those activities must obey.
- Scope note: "architecture" here means the structure of one system or product area — components, contracts, data, decisions. It does not mean organization design, team topology, or portfolio planning, which deserve their own passes.

## 02 — When to Use / When Not to Use

### Use this skill when:

1. **You are starting a new system or major subsystem.**
   - Greenfield service, a rewrite, a new product area inside an existing product — anywhere the first structural decisions are unmade and will be hard to reverse.
   - The earlier in the project you run this workflow, the cheaper every subsequent step is; the workflow itself is designed for a day of work, not a month.
   - Typical first artifacts of this trigger: a brief the whole team can repeat, a stakeholder list with each person's sharpest concern, and the first scenario draft.
2. **You are choosing between architecture styles.**
   - You are weighing a layered monolith against a modular one, hexagonal ports-and-adapters, event-driven pipelines, or a microkernel plugin design.
   - You need a defensible selection tied to scenarios — not a fashion choice, and not a copy of whatever a famous company does.
   - The catalog reference exists precisely for this comparison; the workflow forces the selection into a recorded ADR.
3. **You are documenting decisions for a team.**
   - The team keeps relitigating the same choices ("why is a broker in the middle?"), or new hires ask questions no wiki answers.
   - An external review, audit, or due-diligence process needs the rationale behind the design written down and linked.
4. **You are reviewing an existing architecture.**
   - A system has grown painful: every change touches five modules, deploys are scary, a query melts the database.
   - You need a structured audit that separates real structural debt from complaint, and produces findings with owners.
5. **You are evaluating a proposal against quality attributes.**
   - Someone says "it must scale to 10x" or "security is critical," and the design needs to be checked against claims rather than adjectives.
   - The workflow converts the slogans into testable scenarios first, then checks mechanisms against them.
   - This is also the right entry point for vendor proposals: run their claims through the scenario conversion and watch which ones lose their measures.
6. **You are splitting a monolith or merging services.**
   - You need a principled basis for where to cut: which boundaries are real seams and which are folder names with ambitions.
   - The decomposition and data-ownership steps are exactly the analysis an extraction needs before any code moves.
   - Extraction performed without this analysis reproduces the tangle at higher latency — the mistake compounds, it does not reset.
7. **You are onboarding a team that will inherit the system.**
   - A design pass produces the overview and ADRs that make the inheritance survivable.
   - Even if the design is settled, running the review steps records what was previously oral tradition.

### Do NOT use this skill when:

1. **You are giving feedback on a specific diff or pull request.**
   - Line-level correctness, security, and style feedback is a different craft at a different altitude.
   - Use `code-review` — it covers injection-class flaws, logic bugs, and comment phrasing on concrete diffs.
2. **You are planning what to test and how.**
   - Test plans, coverage strategy, flake quarantine, and CI test-stage design belong to `testing-strategy`.
   - Architecture and testing inform each other, but the artifacts and workflows are separate.
3. **The real question is which vendor or library to pick.**
   - Framework and product comparison is procurement research with its own methods.
   - This skill fixes the constraints such a choice must satisfy (record them in a small ADR); it does not do vendor scoring.
4. **You need a diagram, not a decision.**
   - If the deliverable is a picture for a slide and no decision will change, no skill is needed — draw the picture.
   - Architecture work exists to change decisions, not to decorate them.
   - Beware the request phrased as "update the architecture diagram": it usually means a decision changed and nobody wrote it down — find the decision first.
5. **You are sizing infrastructure or doing capacity planning.**
   - Instance counts, autoscaling thresholds, and budgets are operations work with their own tools.
   - This skill produces the scenarios and mechanisms those numbers must satisfy, then hands off.
6. **You are writing user-facing documentation or tutorials.**
   - That is technical writing; the overview it may describe is this skill's output, but the writing craft is separate.

## 03 — Inputs and Outputs

### Inputs

You should arrive with at least ONE of these; more is better:

- **A system brief.**
  - What the system does, for whom, at what rough scale — "a notes app for a 200-person company, web and mobile clients, must survive a database failover."
  - One paragraph is enough to start; the first workflow steps exist to sharpen it.
- **Quality requirements, even vague ones.**
  - "Must be fast," "auditors need a trail," "two teams will own this" are all valid starting points.
  - The workflow's scenario step converts them into measurable statements; do not pre-polish them.
- **Constraints.**
  - Mandated stack, team size and skills, deadlines, compliance regimes, operational maturity, budget caps on managed services.
  - Mark each constraint as a verified mandate or a soft preference — the difference changes the design.
- **An existing design or codebase.**
  - For review or evolution passes: the current component map, deployment layout, or repository structure.
  - The workflow's review steps accept reality as input; documents that lie are findings in themselves.
- **Prior decisions.**
  - Anything already recorded: ADRs, meeting notes, a decision log.
  - Architecture work extends a decision history; it rarely starts from zero, and the workflow will link to what exists.
- Useful but optional: usage data (which endpoints are hot), incident history (which failures already happened), and on-call rotation reality.

### What good inputs look like

- A brief that names a user, an action, and a scale — even roughly — beats a requirements document of unmeasured adjectives.
- Constraints stated with their source ("security team mandate, 2025 review") age better than constraints stated as facts.
- An existing codebase is best supplied with its pain points: where changes hurt, what breaks, who gets paged.
- If all you have is a napkin sketch and enthusiasm, that is enough for Steps 1-3; the workflow manufactures its own precision from there.

### Outputs

The skill produces documents. Each has a template or a governing reference:

1. **An architecture overview** (`templates/architecture-overview-template.md`).
   - The system in one document: brief, stakeholders, scenario table with mechanisms and verification, component map with data ownership, interfaces, failure behavior, decision index, revisit triggers.
   - A new engineer should understand the system from this alone in twenty minutes.
2. **Architecture Decision Records** (`templates/adr-template.md`, validated by `schemas/adr.schema.json`).
   - One short document per consequential decision: context, options considered, decision, consequences, revisit trigger.
   - Numbered, linked to each other, immutable once accepted.
3. **A quality-attribute scenario table** (governed by `references/quality-attribute-scenarios.md`).
   - Every vague requirement converted to six-part scenario form and prioritized by cost of failure.
   - Includes the explicit sacrifice list: what the design will not optimize for, with revisit triggers.
4. **A review report** from the 40-point checklist (`references/architecture-review-checklist.md`).
   - Findings with severity, evidence quoted from the documents, and a disposition for each: fixed, accepted-with-rationale, or tracked.
   - A review without dispositions is a formality; this output is designed to prevent that.
5. **A comparative style analysis** when the choice is contested.
   - Candidate styles scored against your scenarios using the catalog's table (`references/architecture-styles-catalog.md`).
   - Grounded in the two case studies (`references/architecture-case-studies.md`) so the analysis inherits real failure knowledge.
   - Includes the operational-fit row scored for your actual team, not an imaginary mature platform org.
   - The analysis names the conditions under which the losing style would win instead.

### Output quality bar

- Every output is self-contained: a reader with no access to the conversation that produced it can still act on it.
- Every number has a source: measured, estimated with a method, or marked as an assumption to verify.
- Every output names its date and its owner; unowned documents decay into decoration.
- Every output names the scenarios it serves; outputs that serve no scenario are decoration by definition.

## 04 — Workflow

### Step 1 — Write the system brief and identify stakeholders
**Reference:** `references/component-decomposition.md`

- Write one paragraph: what the system does, who uses it, what "working" means.
- List stakeholders with one line each: end users, the team that operates it, the team that pays for it, any regulator or external integrator.
- Note each stakeholder's single sharpest concern in their own words if you can get it ("I never want to lose a note").
- Why this matters: stakeholders determine which quality attributes matter; a system with no on-call rotation has different concerns than one paged at 3 a.m.
- If the brief runs over five sentences, split it: you are describing two systems.
- Decide now who signs off on the design and how — consensus, tech lead, or a named architect; the ADR lifecycle needs a decider.
- Timebox: 30 minutes for the brief and stakeholder list on a small system; more than an hour means you are designing already.
- Common trap: the loudest stakeholder is rarely the one with the sharpest constraint; the operator who never speaks in meetings usually holds the deployment reality.
- Checkpoint question: "Could a new engineer repeat this brief back to me in one sentence?"

### Step 2 — Elicit quality-attribute scenarios
**Reference:** `references/quality-attribute-scenarios.md`

- Convert every vague requirement into six-part scenarios: source, stimulus, environment, artifact, response, response measure.
- Write 6-10 scenarios; more means the design is being asked to be everything at once.
- Include at least one modifiability scenario (the near-term change the design must absorb cheaply) and one failure scenario (what recovery must look like).
- Use p95 as the default measure; use p99 where stalls are user-visible and costly (payment, login).
- State the load each performance measure assumes: rps, data volume, concurrency. "p95 < 300 ms" without load is half a scenario.
- A scenario missing its response measure is a wish; do not carry wishes into design.
- Sources for scenarios: stakeholder concerns from Step 1, the product roadmap's next two quarters, and the compliance or audit requirements already binding.
- Mark each scenario's source requirement; in review you will be asked which slogan produced it.
- Worked micro-example: "search must be fast" becomes "Signed-in user searches their notes; p95 < 500 ms up to 50k notes per user; index lag ≤ 10 s." Six parts, one measure, one load.
- If a requirement resists conversion after two attempts, escalate it: it is either two requirements fused together or a preference in costume.
- Checkpoint question: "For each scenario, can I name the measurement that would tell us it failed?"

### Step 3 — Prioritize scenarios and name the sacrifice
**Reference:** `references/quality-attribute-scenarios.md`

- Rank scenarios by cost of getting them wrong: data loss and breaches first, visible user pain second, internal friction third, hypothetical futures last.
- Rank by cost, not by who shouted loudest in the meeting.
- Write one explicit line per quality the design will NOT optimize for, each with a revisit trigger.
- An architecture that optimizes for everything optimizes for nothing; a design that has named its sacrifices is honest, and honesty is reviewable.
- Get explicit assent on the sacrifice list from whoever owns the budget; silent sacrifice is future incident report.
- Write the sacrifice list into the overview's scenario section, not a sidebar; it will be checked in review.
- If two stakeholders disagree on the ranking, the disagreement is about cost of failure — resolve it with numbers or timestamps, not volume.
- Sanity check: if the sacrifice list is empty, the ranking was not honest; every design gives something up.
- Checkpoint question: "If we had to drop one scenario entirely, which one — and does everyone accept that?"

### Step 4 — Draft context and constraints
**Reference:** `templates/architecture-overview-template.md`

- Fill the overview's context section: external systems, client types, data flows crossing the boundary, non-negotiable constraints.
- Interrogate each constraint: is the mandated stack a real mandate or a preference with budget attached? Mark each verified or soft.
- Record the operational maturity of the team: what can be operated today, with whose labor.
- Constraints discovered late cost the most; the ones people are embarrassed to state are usually the binding ones.
- Include the deployment reality: where will this actually run, who deploys it, how often, and what the rollback story is today.
- Ask for the org chart reality too: which teams will own which parts after launch — ownership intent belongs in the design, not discovered later.
- Budget reality: if a managed service is capped by spend, that cap is a scenario input, not a footnote.
- Checkpoint question: "Which constraint, if it turned out to be soft, would change the design?"

### Step 5 — Decompose into components
**Reference:** `references/component-decomposition.md`

- Identify components by grouping responsibilities that change together; split where the reasons to change differ.
- Run the boundary tests from the reference: one-sentence purpose (no "and"), tell-nothing test, standalone-test test, data-ownership test.
- For each component, record three columns: what it owns (data and behavior), what it may ask for via ports, and what it never does.
- Expect to run the four discovery probes (responsibilities, data ownership, rate of change, failure isolation) and reconcile the results.
- Three components with clean ownership beat ten with muddy ones; boundaries cost maintenance, so buy only the ones scenarios demand.
- If a candidate component has no owned data and no distinct failure mode, it is probably a layer, not a component — fold it in.
- Sketch the component map in the overview's table format as you go; the table, not the diagram, is the artifact of record.
- When probes disagree, the disagreement is information: rate-of-change and failure-isolation pulling the same responsibility apart is a sign of a future service, and the port design should anticipate it even if extraction does not happen now.
- Write the component table into the overview immediately; components that live only in conversation get redrawn by the next meeting.
- Checkpoint question: "Which boundary am I least sure about, and what would prove it wrong?"

### Step 6 — Choose the architecture style per area
**Reference:** `references/architecture-styles-catalog.md`

- For each major area, compare candidate styles against the top scenarios using the catalog's comparison table.
- Score the operational row honestly for YOUR team: machinery nobody can operate is a liability, not an architecture.
- Default to the boring style unless a named scenario defeats it; complexity must be purchased by a scenario, not by ambition.
- Styles compose by area: a modular monolith may keep an in-process event port that later takes a broker behind the same interface.
- If two styles score within a point on your scenarios, take the one with fewer moving parts and record why.
- Record the comparison in an ADR — chat and slides are where style decisions go to evaporate.
- Write the scoring table itself into the ADR's options section: the scores are the argument, and the argument is the asset.
- Checkpoint question: "What evidence would make us abandon this style in a year — and would we see it in time?"

### Step 7 — Design the interfaces between components
**Reference:** `references/api-design-principles.md`

- For each boundary, design the contract: resources and operations for request/response; events and payload contracts for async.
- Decide versioning policy, pagination limits, idempotency semantics, and the error taxonomy now — these hurt most to change later.
- Every mutating operation gets stated retry behavior; every list operation gets a maximum page size.
- Write the contract down even if implementation is days away; the contract is the architecture at that boundary.
- Test the design against the reference's five review questions (double-call behavior, timeout semantics, field coupling, worst page, discovery-by-implementation).
- For async boundaries, write the event payload contract now, including the fields consumers may rely on and the delivery guarantee.
- Name each port after the capability, not the implementation ("NoteSearch", not "PostgresFTS") — the name is the seam.
- Define the error surface now, not at implementation time: which failures are the caller's to handle, which the callee's to retry, which are reported and which are swallowed.
- Budget the worst-case response of each interface (max page, max batch, max payload); unbounded interfaces are how "temporary" outages become permanent ones.
- Checkpoint question: "If the implementation behind this interface is replaced wholesale, does anything about the contract need to change? If yes, the wrong things are in the contract."

### Step 8 — Design the data model
**Reference:** `references/data-modeling-basics.md`

- Identify entities and relationships from the domain's nouns and their independent existence.
- Assign exactly one owning component per entity's write path; two writers is a missing boundary, not a coordination problem.
- Decide normalization deliberately: 3NF default for transactional data; each denormalization recorded with the read it serves, its refresh mechanism, and its drift check.
- Every derived copy (cache, index, materialized view) states its rebuild path or it is a second source of truth that will eventually lie.
- State the consistency model per boundary (strong within a store, eventual across) and match it to what users are promised.
- Decide identifier policy early: opaque surrogate keys internally, and which identifier (if any) is exposed in the public API — it becomes contract.
- Add provenance columns (`created_at`, `updated_at`, soft-delete where deletion is undoable) in the first migration, not the fifth.
- Checkpoint question: "If two components both need to write the same entity, which one wins — and is that written down?"

### Step 9 — Record decisions as ADRs
**Reference:** `references/architecture-decision-records.md`, `templates/adr-template.md`, `schemas/adr.schema.json`

- Write one ADR per consequential, hard-to-reverse decision: style choice, data ownership, consistency model, interface policy, constrained technology selections.
- Include options considered with steel-manned arguments, consequences with costs, and a measurable revisit trigger.
- Validate each ADR against the schema; link related records (supersedes, amends, relates-to).
- Accepted ADRs are immutable: a changed decision gets a new ADR, never an edit.
- If a decision is deferred, record the deferral with its decision trigger; an unrecorded shrug resurfaces as an emergency.
- Keep ADRs to one page; if the document needs two, link a design doc and record only the decision here.
- Store ADRs next to the code, reviewed like code — a wiki outside review flow drifts within a quarter.
- Number sequentially and never reuse numbers; a reused number is a lie about history.
- Write the options section as if the losing option might win: give each real option its best honest case, then say why it lost.
- The consequences section lists both kinds: what you get, and what you now accept living with.
- Checkpoint question: "If the context changed, would a reader know this decision is up for re-examination — or does it look eternal?"

### Step 10 — Review the design against the 40-point checklist
**Reference:** `references/architecture-review-checklist.md`

- Run the full checklist yourself first; a second reviewer then checks only what you marked — fresh eyes on blind spots, not a duplicate pass.
- Group findings by severity: blocker (a scenario is unmet), major (a boundary or ownership question is unanswered), minor (inconsistency, missing rationale).
- Check documents against each other (scenarios vs. mechanisms vs. ADRs) before critiquing the design itself; most findings are inconsistencies, not errors.
- Give every finding a disposition: fixed, accepted-with-rationale, or tracked-as-decision. No silent drops.
- Timebox the pass to about 90 minutes for a system of moderate size; note second-pass items instead of exhausting yourself.
- For a first design, expect 5-12 findings; zero findings on a fresh design means the reviewer was confirming, not checking.
- Attach the review report to the overview's review-record section with the date; unattached reviews get re-litigated.
- If you are both author and reviewer (solo work), run the checklist in two sittings a day apart; the second sitting reads the documents as a stranger would.
- Checkpoint question: "Which checklist item did I skip because it was inconvenient — and is the inconvenience telling me something?"

### Step 11 — Compare against the case studies
**Reference:** `references/architecture-case-studies.md`

- Compare your design's trajectory against the two case studies: the monolith whose seams dissolved, the modular design that kept them through enforcement.
- Identify the analogous pressure points in your design — where would a "just this once" shortcut land?
- Name the concrete countermeasure for each pressure point: an enforced test, an ownership rule, a documented exception path.
- Case studies are pattern libraries for failure; the comparison converts them into your design's early-warning list.
- Write the comparison into the overview's revisit-trigger section as named risks with countermeasures, not as a separate memo nobody files.
- Note what the case studies got right that your design should copy — enforcement in CI, explicit ownership, dated triggers are the recurring winners.
- If neither case study matches your pressure profile, say so explicitly in the overview; absence of an analogue is itself a risk note.
- Checkpoint question: "Which case-study failure is my design closest to, and what protects that seam?"

### Step 12 — Publish, and schedule the revisit
**Reference:** `templates/architecture-overview-template.md`

- Publish the overview and ADR set where the team works; version them with the code so they get updated in the same pull requests.
- Fill the overview's revisit-trigger table: each decision, its measurable trigger, and the action if it fires.
- Schedule the next review (date or trigger) in the overview itself; unscheduled reviews do not happen.
- Assign ownership explicitly: one name per document, responsible for keeping it true.
- Announce the publication where the team actually reads announcements; a perfect overview nobody knows about is a diary.
- Why this matters: architecture is a living set of decisions; the revisit table is what keeps the documents honest after the meeting ends.
- Checkpoint question: "If I am hit by a bus, will the next engineer know both the design and the deadline each decision is good until?"

## 05 — Rules and Quality Bar

How to use these rules: they are checkpoints for self-review, not aspirational maxims. Run any artifact against the rule that governs it; a violated rule with no rationale is a defect. The rubric-level details live in the referenced files; these rules are the bar you hold work to before anyone else sees it.

1. **Scenarios before structure.** Every component boundary must trace to a scenario it serves; structure without a scenario is decoration.
   - Form and craft: `references/quality-attribute-scenarios.md`.
   - Why: boundaries justified by taste get redrawn by the next person's taste; boundaries justified by scenarios survive.
   - Corollary: when someone proposes a mechanism, ask "which scenario is this for?" — an unanswerable question kills it politely.
2. **Name the trade-off or it will name you.** Every design choice gives something up; write the cost next to the benefit.
   - Why: a trade-off only you can see is a trade-off that will be relitigated at the worst possible time.
   - Corollary: the cost belongs in the artifact (overview row, ADR consequence), not in your head.
   - Corollary: if you cannot name the cost, you have not understood the choice yet — go find it before someone production does.
3. **One owner per piece of data.** If two components write the same entity, stop and fix the boundary before anything else.
   - Why: shared write access is the root of most architectural pain — drift, races, and blame without diagnosis.
   - Corollary: read-only consumers may hold derived copies, but only with a stated refresh mechanism and rebuild path.
4. **Decisions are records, not vibes.** Consequential, hard-to-reverse decisions get ADRs with options considered.
   - Format and lifecycle: `references/architecture-decision-records.md`.
   - Why: verbal decisions decay within a quarter; the argument is the asset, and memory is not storage.
   - Corollary: if a decision cannot be written as one imperative sentence, it is several decisions — split the ADR.
5. **Prefer boring styles by default.** Layered or modular monolith until a named scenario forces otherwise.
   - Why: exotic styles must earn their complexity; complexity purchased by ambition is paid for by operators.
   - Corollary: "we might need it someday" is not a scenario; someday has no measure.
6. **Boundaries are promises about change.** A boundary is justified by what it lets you change without telling other components.
   - Why: if nothing changes behind it, it is a seam without a job — pure maintenance cost.
   - Corollary: name what changes behind each boundary; unnamed promises are unfalsifiable.
7. **Design for the readable failure.** Ask what every component's failure looks like: timeout, retry storm, silent loss, degrade-and-continue.
   - Why: a design whose failures are legible is operable; one whose failures are mysteries pages people at random.
   - Corollary: every failure answer needs a detection mechanism — a failure you cannot see is a failure you cannot operate.
8. **Interfaces before implementations.** Get the contract right and the implementation can be replaced; get it wrong and every implementation is a hostage.
   - Contract craft: `references/api-design-principles.md`.
   - Why: contracts radiate outward; code behind them does not.
   - Corollary: write the contract down before the first client exists; after, it is archaeology.
9. **The data model outlives the code.** Spend proportionate time on entities, relationships, and ownership.
   - Modeling craft: `references/data-modeling-basics.md`.
   - Why: frameworks change around the data model, not the reverse; schema migrations on live data are among the most expensive operations in software.
   - Corollary: denormalize only with a stated refresh mechanism; every derived copy is a promise to keep it true.
10. **Deferred decisions are decisions too — record the deferral.** An ADR with status "proposed" and a decision trigger beats an unrecorded shrug.
    - Why: deferrals without records resurface as emergencies with no context.
11. **Every review finding gets a disposition: fixed, accepted-with-rationale, or tracked.** Findings may not be silently dropped.
    - Checklist and scoring: `references/architecture-review-checklist.md`.
    - Why: silent drops are how designs rot while their documents smile.
12. **Small words, precise claims.** Ban "scalable," "robust," "modern"; write numbers and mechanisms.
    - Good: "p95 < 300 ms at 500 rps with the read-replica topology in ADR-0004."
    - Why: precision is testable, and testability is what separates design from mood.
13. **If a diagram cannot be drawn from the overview in ten minutes, the overview is incomplete.**
    - Why: components, responsibilities, and data flows must be unambiguous to everyone, not just the author.
    - Corollary: if the diagram requires explaining exceptions, the exceptions belong in the overview as rows, not in folklore.
14. **Architecture serves the team you have.** A design the team cannot operate is wrong regardless of its elegance.
    - Why: the org's operational maturity is a constraint as real as any latency budget.
    - Corollary: adopting machinery ahead of the team's maturity requires an operator plan in the same ADR, or it does not happen.
15. **Update the overview in the same change that breaks it.** The overview that lags reality is worse than none: it is trusted and wrong.
    - Why: documentation debt compounds silently and then surprises everyone at the worst moment.
16. **Keep the file index honest.** Section 08 must match the directory exactly; a skill that lies about its own contents teaches its reader to distrust it.

### Using the rules together

- Rules 1-3 govern decomposition; rules 4-8 govern contracts and styles; rules 9-12 govern data and review; rules 13-16 govern the published artifacts.
- When two rules appear to conflict (a scenario demands machinery the team cannot operate), the conflict is itself a design signal: resolve it in a scenario priority or an operator plan, not by ignoring a rule.
- The rules are stable, but their application scales with stakes: a two-day prototype honors them in lightweight form; a five-year system honors every corollary.

## 06 — Worked Example

**Scenario:** design **QuickNotes**, a small multi-user notes service for a 40-person startup.

- Users create notes, tag them, share individual notes, and full-text search everything they can read.
- Clients: web SPA and a mobile app. ~200 daily active users; growth hoped for, unproven.
- One full-stack engineer builds it; a second joins in six months.
- Constraints: managed Postgres (existing company account), no Kubernetes, budget for at most one additional managed service.
- The full artifacts — scenario table, component map, both finished ADRs, and the review findings log — live in `examples/worked-architecture-design.md`.

### Steps 1-4 — Brief, scenarios, priorities, constraints

- Brief (one sentence): "Users store, tag, share, and search text notes from web and mobile; notes are never lost."
- Stakeholders: users (speed, reliability), the founding engineer (maintainability while working alone), the founder (optionality to grow without a rewrite).
- Sharpest stakeholder concern, in their own words: "I never want to lose a note" — this became scenario Q3, the top-priority row.
- Sign-off decided: the founding engineer proposes, a senior advisor outside the company accepts ADRs — the decider question from Step 1 answered in one line.
- Scenarios distilled from "must be fast and reliable":
  - Q1 — note list p95 < 300 ms at weekday load, warm cache miss.
  - Q2 — full-text search p95 < 500 ms up to 50k notes per user; index lag ≤ 10 s.
  - Q3 — primary database failure: recovery < 5 min, ≤ 5 min data loss.
  - Q4 — ACL rules change in ≤ 1 day, confined to one module, no client changes.
  - Q5 — malformed note bodies rejected or quarantined; corruption never spreads.
  - Q6 — share revocation effective by the next read.
- Priority by cost of failure: Q3 > Q5 > Q1 > Q6 > Q2 > Q4.
- Q4 is the sleeper: it makes modifiability first-class, which rules out any design where ACL logic smears across every endpoint.
- Named sacrifice: no horizontal write scaling — single-writer Postgres; revisit trigger: write p95 > 200 ms sustained for a week.
- Constraints verified: managed Postgres is a real mandate (billing approved); "no Kubernetes" is really "nothing needing a dedicated operator."
- Deployment reality recorded: single small instance, deploys on Fridays with a one-click rollback; that constraint ruled out anything needing sidecars or operators.
- The scenario table went into the overview with a mechanism and verification column per row, per the workflow's Step 2 rule that unverified scenarios are rumors.
- Sign-off decided: the founding engineer proposes, a senior advisor outside the company accepts ADRs — the decider question from Step 1 answered in one line.

### Step 5 — Decomposition

- **Notes** — owns the `notes` and `note_tags` tables and all note read/write logic. Purpose: "store and serve notes per ACL." One sentence, no "and."
- **Access** — owns ACL rules and the `note_shares` table; the only module allowed to answer "can user X act on note Y."
- **Search** — owns the derived search index; consumes note-change events; answers search queries; rebuildable from Notes' data.
- Cohesion check: tagging stays inside Notes (changes with note attributes); ACL is separate (changes for legal/product reasons); Search is separate (different storage engine, survivable failure).
- Ownership check: each table has exactly one writing module; Search holds derived data only, with a stated rebuild path.
- Boundary tests: all three pass one-sentence purpose; Notes and Access pass tell-nothing (callers depend only on ports); Search passes standalone-test (runs against an in-memory event feed in tests).
- Reconciliation of probes: rate-of-change probe wanted ACL split from Notes (agree); failure-isolation probe wanted Search extractable (satisfied by the port, not yet by process).
- The god-component and anemic-boundary anti-patterns from the reference were checked and did not apply: no component is a grab-bag, none is pure CRUD.

### Step 6 — Style choice

- Candidates: layered monolith, hexagonal monolith, Notes+Search as two services.
- Layered rejected: the layer convention erodes without enforcement, and ACL logic leaks into handlers — the exact Q4 failure.
- Two services rejected: operational cost for one engineer exceeds the benefit at 200 DAU; Search's failure is survivable anyway.
- Chosen: **hexagonal modular monolith** — three in-process modules behind interfaces; a CI module-boundary test enforces import rules.
- Recorded in ADR-0001 with the rejected options steel-manned, per `references/architecture-decision-records.md`.
- Fit check from the catalog: the operational row scored first and honestly — one engineer, one pipeline, one datastore to page on.
- The catalog's "ease of later extraction" row is why the Search port got designed carefully despite staying in-process: the decision buys optionality, and the revisit trigger is what converts optionality into action.

### Steps 7-8 — Interfaces and data model

- REST API (both clients are request/response; one engineer): `GET/POST /v1/notes`, `PATCH /v1/notes/{id}`, `POST /v1/notes/{id}/shares`, `GET /v1/search?q=`.
- Contract decisions: path versioning; stable error codes with a `retryable` flag; page size capped (default 50, max 200); idempotency keys on share creation.
- Double-call test passed: share creation with an idempotency key returns the existing share on retry; PATCH is naturally idempotent per-field.
- Timeout semantics: note writes are single-row and safe to retry; share revocation is checked at read, so a retried revoke is harmless.
- Internal ports: `NoteRepository` (Notes↔storage), `AccessPolicy` (any→Access), `NoteEvents` (Notes→Search), `NoteSearch` (Search's public face, free of Postgres types).
- Port naming rule applied: capabilities, not implementations — `NoteSearch` survives the extraction that `PostgresFTS` would not.
- Entities: `users`, `notes`, `note_tags`, `note_shares`, `tags`.
- One owner each: Notes owns `notes`/`note_tags`; Access owns `note_shares`; Search owns only its derived index (rebuild path stated: full rebuild from `notes` + `note_shares` in under 10 minutes at 10x current volume).
- Consistency: strong in Postgres for owned data; search index eventually consistent (≤ 10 s lag, acceptable per Q2/Q6).
- Constraint enforcement: unique `(note_id, user_id)` on shares; FK indexes on `notes.owner_id` and `note_tags.tag_id`; provenance columns in the first migration.
- Identifier policy: opaque surrogate keys internally; only note ids exposed publicly; user emails never appear in API payloads.
- Normalization decision: 3NF everywhere; the tag-chips read is one indexed join at current scale — no denormalization yet, revisit trigger is list p95.
- Information-disclosure policy decided per `references/api-design-principles.md`: notes not shared with you return 404, not 403 — existence is not disclosed across the ACL boundary.
- The five interface review questions from the reference all answered in writing; the two that found real issues (double-call, worst page) produced the idempotency-key and pagination decisions above.

### Step 9 — Two ADRs

- Two decisions carried real reversal cost, so two ADRs — the proportionality rule from `references/architecture-decision-records.md` applied literally.
- **ADR-0001 — Single deployable with hexagonal module boundaries.**
  - Options: layered monolith (rejected: boundary erosion under pressure), two services (rejected: operations exceed one-engineer budget).
  - Consequences: in-process calls today; Search port kept implementation-agnostic so extraction stays bounded.
  - Revisit trigger: extract Search if indexing starves request threads (p99 latency attributable to indexing) or a second team forms.
  - Schema validation: passed — two options with pros/cons and rejection rationale, dated, one-sentence decision.
- **ADR-0002 — Postgres full-text search instead of a dedicated engine.**
  - Options: managed search service (rejected: budget cap, second dependency), Postgres FTS over a trigger-maintained tsvector column with GIN index (chosen: same-transaction refresh, zero new infrastructure).
  - Consequences: advanced relevance out of reach; write latency coupled to index maintenance (negligible at measured volume).
  - Revisit trigger: search p95 > 500 ms or index build > 5 minutes for two consecutive weeks.
- Both ADRs validated against `schemas/adr.schema.json`: statuses, dated, linked (0002 relates-to 0001), each with a measurable revisit trigger.
- Note what did NOT get an ADR: pagination caps, error shape, deployment cadence. Reversible contract details live in the overview; only the two decisions with real reversal costs earned records. This proportionality is the discipline the format reference asks for.
- Full ADR text is in `examples/worked-architecture-design.md`; the fill-in template is `templates/adr-template.md`; validation uses `schemas/adr.schema.json`.

### Step 10 — Review pass (findings with dispositions)

- The author ran the 40-point checklist (`references/architecture-review-checklist.md`) alone first, marking each point; a senior advisor then checked the ✓ and N/A marks only.
- R-22 (major): consistency model implied, never stated — when does share revocation take effect? **Fixed:** ACL checked at read time; revocation effective by next read (Q6); recorded in the overview.
- R-31 (major): Search's failure behavior undefined. **Fixed:** search returns 503-retryable while the index is unavailable; notes CRUD unaffected; recorded in ADR-0002 consequences.
- R-26 (major): note list endpoint had no page-size cap. **Fixed:** default 50, max 200, cursor pagination.
- R-36 (minor): ADR-0001 claimed "easier testing" without a mechanism. **Fixed:** rewritten to name in-memory port doubles.
- R-30 (minor): versioning policy was a convention, not a record. **Tracked:** one-line policy added to the overview; full ADR deferred until a breaking change forces the question.
- R-33 (minor): in-process event fan-out had no backpressure note. **Accepted:** human-scale write volume; bounded queue with drop-oldest plus a lag alarm; rationale recorded.
- Blockers: none. Two of six findings appeared only when checking documents against each other — which is why the cross-check precedes design critique.
- The review took 75 minutes. The author-then-verifier split worked as designed: the second reviewer spent their time on the ✓ and N/A marks, where the author's blind spots lived.
- Findings by checklist area: A (scenarios) clean; C (data) produced R-22; D (interfaces) produced R-26; E (risk) produced R-31; F (decisions) produced R-30, R-33, R-36.
- Lesson: the data and risk sections found the consequential holes; the scenario section was clean because Step 2-3 forced measures early — the checklist pays best where the workflow was weakest.

### Steps 11-12 — Case-study comparison and publication

- Comparison: the live risk is the monolith case study's failure — seams that exist only as folder names.
- Countermeasure: the module-boundary test in CI plus per-entity ownership rules.
- Second risk, from the modular case study: drift through "quick" exceptions on incident weekends.
- Countermeasure: quarterly re-run of the checklist's data-ownership and decision-record sections.
- Third risk, generic to solo work: decisions made silently with no decider to challenge them.
- Countermeasure: the ADR options sections are written adversarially — argue the rejected option as if you favored it.
- All three risks went into the overview's revisit-trigger table as named rows with countermeasures, not a separate memo.
- The comparison also flagged what the case studies got right that this design copies: enforcement living in CI, not in good intentions.
- Published to `docs/architecture/` with the revisit-trigger table; the second engineer reads it on day one.
- The publication PR included the overview, both ADRs, and the review log — one reviewable unit, so the documents were born linked.
- Next scheduled review: six months out, or immediately if the write-p95 revisit trigger fires.
- What the pass cost, honestly: one focused day for steps 1-9, the 75-minute review, an afternoon revising. That is the price of a design that the second engineer will not have to reverse.

### What the example proves

- The scenario table did the arguing: every contested point (services vs. modules, dedicated engine vs. FTS) resolved by pointing at a scenario row, not by seniority.
- Two ADRs were enough; proportionality held — reversible contract details stayed in the overview, reversal-cost decisions got records.
- The review found real holes (revocation timing, search failure, page caps) that the author could not see; authors cannot read their own documents as strangers do.
- The revisit triggers make the design honest: every acceptance names the condition under which it stops being right.

## 07 — Failure Modes and Recovery

1. **The design optimizes for scale the product will never reach.**
   - Early signal: queues, shards, and a service mesh sketched for a system with dozens of users.
   - Corrective move: collapse to the simplest style satisfying the top three scenarios; move removed machinery into revisit triggers.
   - Prevention: every mechanism must name the scenario that justifies it. No scenario, no mechanism.
   - Detection: the cheapest reviewer prompt is "delete this component — which scenario breaks?" Silence is the finding.
   - Recovery cost note: collapsing early is cheap; after the machinery has consumers, removal needs a deprecation cycle.
2. **Requirements arrive as slogans ("must be highly scalable").**
   - Early signal: you cannot name a measurement that would show the requirement unmet.
   - Corrective move: run the six-part scenario conversion; refuse to proceed until the top scenarios have measures.
   - Prevention: make the scenario table the first artifact, reviewed before any boxes-and-lines drawing.
   - Detection: scan the design docs for unmeasured adjectives; each one is an unconverted requirement.
   - Recovery cost note: conversion takes minutes per slogan when done at Step 2; done at review, it reopens finished decisions.
3. **Decisions live in chat, not in records.**
   - Early signal: new engineers ask "why is X this way?" and the answer is a person's memory.
   - Corrective move: backfill ADRs for the five highest-change-cost decisions; mark reconstructed arguments as such.
   - Prevention: record every consequential decision at decision time; retroactive records lose the strongest arguments.
   - Detection: pick three load-bearing choices at random and try to find their rationale in a document; failures of the sample generalize.
   - Recovery cost note: backfilled records are honest about being reconstructions; never backdate a claim of rigor.
4. **The decomposition is one giant component with subfolders.**
   - Early signal: every change touches the same module; unit tests need the world booted.
   - Corrective move: apply the change-together test; split by differing reasons to change, starting with the two most-churned areas.
   - Prevention: one-sentence purpose test per component; any component needing "and" to describe gets split.
   - Detection: a module whose test suite requires a database, a message broker, and a 30-second startup is not a unit.
   - Recovery cost note: splitting late is safe if you move behavior with its tests, one boundary per release (`references/component-decomposition.md` has the sequence).
5. **Shared mutable data across boundaries.**
   - Early signal: two modules write one table; caches disagree; "who updated this?" is a recurring bug class.
   - Corrective move: pick one owner; convert the second writer to commands-through-owner or events.
   - Prevention: data ownership table in the overview, checked in every review (points 17-18 of the checklist).
   - Detection: `grep` for UPDATE/INSERT against one table from more than one module's source tree — every extra hit is a latent incident.
   - Recovery cost note: the conversion is mechanical once the owner is chosen; the expensive part is auditing the data already written by both sides.
6. **Event-driven enthusiasm before the team can operate it.**
   - Early signal: async chosen with no tracing, no dead-letter handling, one on-call engineer.
   - Corrective move: downgrade to synchronous inside a modular monolith; keep the message port so the async option stays open.
   - Prevention: style selection scores operational maturity alongside technical fit (the catalog's operations row).
   - Detection: ask "when a message fails, who finds out, and how?" — a shrug means the machinery is ahead of the org.
   - Recovery cost note: the synchronous downgrade usually removes more code than it adds; the queue plumbing was paying rent to nobody.
7. **The ADR set became a museum.**
   - Early signal: ADRs exist but code contradicts them; nobody remembers ADR-0007.
   - Corrective move: one reconciliation cycle — amend or supersede stale ADRs, delete ones that never described reality.
   - Prevention: dated, owned revisit triggers; the checklist asks "do the ADRs match the running system?"
   - Detection: quarterly, sample one ADR and verify the code still matches its decision column; museum rot starts small.
   - Recovery cost note: reconciliation is a half-day when caught in a quarter, a project when caught after a year.
8. **Review theater — the checklist is run to confirm, not to find.**
   - Early signal: a review of a never-reviewed design produces zero findings.
   - Corrective move: re-run the two weakest areas with a skeptic's script: "what makes this fail in production, and what would we see first?"
   - Prevention: the review's job is to disprove the design; findings are its success metric, not its embarrassment.
   - Detection: compare review timestamps against meeting calendars — a review finished in ten minutes was not a review.
   - Recovery cost note: a skeptical re-run takes 30 focused minutes and reliably yields 2-4 findings on designs that "passed."

### How the failure modes connect

- Modes 1 and 2 are the same disease at different stages: unmeasured ambition. The scenario table is the vaccine for both.
- Modes 3 and 7 are the documentation lifecycle: unrecorded at birth, unwatched after death. The ADR lifecycle rules (write at decision time, supersede, never edit) break the cycle.
- Modes 4 and 5 are decomposition failures in opposite directions: no boundaries versus fake boundaries. The data-ownership tests catch both.
- Modes 6 and 8 are people-shaped: machinery ahead of operators, review ahead of skeptics. Both are caught by asking "who actually operates this?" early and honestly.

## 08 — Supporting Files Index

Reading order: run §04 top to bottom; open a reference file when a step points to it; use templates only when producing that artifact; read the worked example after your first pass, not before.

Why the file set is shaped this way: the eight references each carry one body of craft so SKILL.md stays procedural rather than encyclopedic; the two templates define the two output shapes (decision, overview); the schema makes ADR validation mechanical; the example shows a full pass at realistic depth. If you read only one file before starting, make it `references/quality-attribute-scenarios.md` — the scenario table is the load-bearing artifact of the whole workflow.

| File | Purpose | Used In |
|---|---|---|
| `references/architecture-decision-records.md` | ADR format, lifecycle, linking, anti-patterns | §04 Step 9; §05 Rule 4 |
| `references/architecture-styles-catalog.md` | Layered, hexagonal, event-driven, microkernel — forces, costs, fit checks | §04 Step 6; §07 #6 |
| `references/quality-attribute-scenarios.md` | Six-part scenario form, prioritization, trade-off naming | §04 Steps 2-3; §05 Rule 1 |
| `references/component-decomposition.md` | Cohesion, coupling, boundary discovery and tests | §04 Steps 1, 5; §07 #4 |
| `references/api-design-principles.md` | Resource modeling, versioning, error design at boundaries | §04 Step 7; §05 Rule 8 |
| `references/data-modeling-basics.md` | Entities, relationships, ownership, normalization trade-offs | §04 Step 8; §05 Rules 3, 9 |
| `references/architecture-review-checklist.md` | 40-point review with scoring and dispositions | §04 Step 10; §05 Rule 11 |
| `references/architecture-case-studies.md` | One monolith and one modular design compared over time | §04 Step 11; §07 #7 |
| `templates/adr-template.md` | Fill-in ADR document matching the schema | §03 Outputs; §04 Step 9 |
| `templates/architecture-overview-template.md` | One-document overview with scenario and revisit tables | §03 Outputs; §04 Steps 4, 12 |
| `schemas/adr.schema.json` | JSON schema for ADR validation | §04 Step 9 |
| `examples/worked-architecture-design.md` | Full QuickNotes run: overview, two ADRs, review findings | §06 Worked Example |

Maintenance contract:

- This table must match the directory exactly — the verification suite diffs it against reality.
- If you add a file, add a row and cite it at its point of use in §04.
- If a file is no longer used, remove both the file and the row; dead rows are findings in review.

Cross-skill boundaries, for routing questions that arrive mid-workflow:

- Diff-level security findings discovered during architecture review (an injection-prone data access pattern, for instance) belong to `code-review` at the code stage; record the structural concern here and hand the craft over.
- Verification design for the scenarios (load tests, drills, matrix suites) belongs to `testing-strategy`; this skill names the verification, that skill designs it.
- If you find yourself making a third structural exception "temporarily," stop and re-run Steps 5-6: accumulated exceptions are how architectures rot, and the skill's answer is a fresh decision, not a shrug.
