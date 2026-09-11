# Adoption Strategies: Phasing, Migration, and Team Buy-In

Adopting a design system is an organizational change, not a technical one. Teams that treat it as a component library install — add the package, swap the imports, done — burn out on the third migration and blame the system. Teams that treat it as a product with phases, milestones, and user research succeed because they built consent alongside components.

## The three-phase model

**Phase 1 — Foundation (weeks 1-6).** Tokens, two to three components, and documentation for those components. No migration. No one is asked to change anything. The purpose is to prove the system works: a new page built entirely from system components ships faster than the equivalent bespoke page. This is the artifact that funders see and skeptics measure against.

Who works on foundation: the design system team, one to two people embedded in a single consuming team that has agreed to be the first adopter. The first adopter is chosen by enthusiasm, not mandate — a team that volunteers ships faster than one that is assigned, and the resulting artifact is better because the builders wanted it.

Deliverable: one production surface built entirely with system components. The surface is documented as a case study in `system-case-studies.md`.

**Phase 2 — Pull (weeks 7-20).** Components ship as they are ready, not on a calendar. Consuming teams adopt when the component matches their need and the migration effort is less than the effort of building the same thing themselves. The system team sets a cadence — one release every two weeks — and processes incoming requests from consuming teams.

During Phase 2, the system team tracks two metrics:
- **Adoption rate:** Percentage of new components or surfaces that use system components. Target: 60% by end of phase.
- **Pull ratio:** Number of consuming-team requests fulfilled per system-team self-initiated feature. Target: 2:1 or higher. A ratio below 1:1 means the system team is building things nobody asked for.

Who works on pull: the system team grows to include one rotating member from a consuming team. The rotation lasts one release cycle, and the rotating member is responsible for bringing production pressure into the system — bug reports, missing variants, misaligned tokens — and taking system discipline back to their team.

**Phase 3 — Governance (weeks 21+).** The system has enough surface area that ungoverned growth would erode coherence. Governance processes from `versioning-and-governance.md` become active. New tokens require review. New components require a consumer impact assessment. The system team shifts from building to maintaining, curating, and reviewing contributions from consuming teams.

Adoption targets: 80% of new surfaces use system components. The remaining 20% are acknowledged exceptions with written approval from the governance body. The governance body starts meeting, and the deprecation policy is enforced.

## Migration strategy

Do not migrate everything. Migration has cost, and the cost is subtracted from the system's value proposition. Three rules for deciding what to migrate:

1. **High-frequency, low-variance surfaces first.** A page that renders the same five components across fifty rows is easier to migrate than a bespoke dashboard that renders one of every component at different sizes. The migration teaches the system team how their components behave under production load without requiring the team to rebuild a complex layout.
2. **Touch once; never revisit.** A surface that is being redesigned anyway is a natural migration target because the cost of building from system components is less than the cost of rebuilding from scratch. Do not deduplicate a surface that works fine and is not being touched — the system's value improves over time without the migration cost.
3. **Audit before and measure after.** Before migrating, record the page's render time, number of CSS rules, and number of imported component files. After migration, record the same metrics. If the numbers are worse, the migration was premature or the component is wrong for the use case. Publish both numbers so the next team knows the real tradeoff.

## Getting buy-in from skeptics

Skepticism about design systems usually takes one of three forms:

**"Our UI is too unique for a system."** The right response is not to argue but to audit. The `component-inventory.md` reference's audit pass will show that 60-80% of the interface is standard components (buttons, inputs, cards, tables) rendered with inconsistent styling. A system targets the standard 80% and leaves the unique 20% untouched. Show the audit, not the argument.

**"The system will slow us down."** This is true in the first six weeks and false after week eight. The measurable response is to publish the first-adopter case study with build times for a pre-system page versus the same team's post-system page. If the numbers do not show improvement, fix the system before recruiting more adopters.

**"We already have our own patterns."** Every team has local expertise that the system does not. Honor it by including rotating members in Phase 2. The system that incorporates its consumers' patterns is adopted; the system that overrides them is resisted. The difference is visible in the `pull ratio` metric.

## Communication cadence

Weekly: a status post in the consuming-team channel — what shipped this week, what is in review, what broke, what the system team needs to know. The post is four to six bullet points, never longer. A system that communicates weekly is trusted; a system that communicates quarterly is the department that sends the newsletter nobody opens.

Monthly: a demo of the system's newest components and the first-adopter's results. Invite all consuming teams, serve food, start on time, end early. The demo is the place to announce deprecations and migration windows because the audience is gathered.

Quarterly: a governance review with the governance body. The system team presents adoption metrics, open issues, and the roadmap for the next quarter. The governance body approves or blocks the roadmap items. Minutes are published.

## Anti-patterns

- **The big-bang migration.** Six months of building, then a forced switchover across all teams. The switchover date slips three times, the migration guide is obsolete by the time it lands, and teams who had working UIs now have broken ones. The big bang is how design systems fail in public.
- **The component backlog.** The system team accepts every request from consuming teams without prioritization. The backlog grows past 200 items, nothing ships, and the team burns out on triage. Close the backlog weekly; say "no, and here is a workaround" at least as often as "yes, and here is a timeline."
- **The renamed surface.** A team copies the system's CSS variables into a local file, renames them to match their existing naming convention, and claims they are "using the system." Track usage by package import, not by color values; imports do not lie.
- **The toolkit mandate without the toolkit team.** Leadership mandates the design system, but the team that must build it is one person with no release authority and an existing product to ship. A mandated system without dedicated capacity ships nothing, erodes trust, and makes the next system harder to start.