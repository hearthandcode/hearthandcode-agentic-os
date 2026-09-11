# System Case Studies: Design System Adoption in Practice

## Case Study 1: Veridius — Product analytics dashboard redesign

**Team.** Veridius is a seven-person startup building a product analytics dashboard for mid-market e-commerce teams. Two engineers, one designer, one product manager, one QA, and two founders. Timeline from first system commit to shipped first-adopter surface: 11 weeks.

**Context before the system started.** The product had 43 surfaces, 12 component files per engineer's personal preference, three competing color palettes (original-launch blue, experimental gradient, CEO's personal brand palette), and no shared component file. Loading any page required importing between 18 and 34 separate CSS files. The product shipped, but the team spent 30% of every sprint resolving visual inconsistencies and another 20% reimplementing components that should have been shared. Sprint velocity had declined for four consecutive releases.

**Foundation phase (weeks 1-4).** One engineer and one designer, allocated 50% each, started with tokens. They audited all 43 surfaces using the component-inventory method — finding 17 distinct component types — and built a token set with 58 primitives and 42 semantic tokens. The semantic tier was deliberately smaller than the primitive tier so the team could not accidentally use a primitive directly in markup.

The first-adopter surface was the main analytics dashboard — the most-visited page, high-frequency use, built with ten system components: AppShell, Sidebar, TabPanel, DataTable, MetricCard, Select, DateRangePicker, Button, Badge, and Pagination. Veridius rebuilt the dashboard in nine days once the components were available. Pre-system: the dashboard rendered in 2,100 ms with 38 CSS imports. Post-system: 890 ms with 6 imports.

**Pull phase (weeks 5-9).** The system team grew to include a rotating engineer from the product team. The pull ratio was 3:1 — for every system-team-initiated feature, they fulfilled three requests from consuming parts of the product (the settings surface adopted Select and DateRangePicker; the reports surface adopted DataTable and Badge). Two metrics drove decisions: adoption rate climbed from 20% to 65%, and the component backlog never exceeded 12 items.

**Governance phase (weeks 10+).** By week 10, 75% of new surfaces used system components. The governance body — system lead, rotating engineer, founder — met and approved five guidelines: (1) no new semantic tokens without two documented use surfaces, (2) Request For Comment period of three days for new component proposals, (3) deprecation timeline of two releases, (4) mandatory a11y review before MAJOR release, and (5) quarterly adoption review against targets.

**What worked.** Dedicated capacity produced a real first-adopter surface. The pull ratio kept the system relevant. Publishing the pre-and-post build time numbers converted skeptics.

**What they would do differently.** Start the accessibility audit in foundation phase, not phase 3. The dark theme, shipped in week 8, failed contrast on three token pairs and needed an urgent patch. They also underestimated governance reading time — the RFC process, well-intentioned, added a week to each minor release. They tightened the RFC window from five days to three.

**Measurable outcomes at week 26.** Adoption rate: 82% of new surfaces. Sprint velocity: up 40% from pre-system baseline. New engineer onboarding time for UI tasks: down from two weeks to three days. Open a11y violations: zero at the MAJOR release.

---

## Case Study 2: Dovetail — B2B contract management platform

**Team.** Dovetail is a 12-person company (eight engineers, two designers, two PMs) that signed three enterprise contracts before it had a button component. The design system adoption was driven by an enterprise customer's accessibility clause in the contract.

**Context before the system started.** The product shipped with four distinct button implementations — each engineer wrote their own on their first task. Forms had no consistent validation pattern. The accessibility audit that the enterprise customer required found 73 WCAG violations across 21 surfaces, including missing labels on 40% of form inputs, no visible focus indicators on 80% of interactive elements, and one surface where tab order jumped from the header to the footer without visiting the main content.

**Foundation phase (weeks 1-5).** The entire team agreed that the a11y requirement was the system's first job. They built the token set with contrast metadata required on every color token — tokens that could not declare a contrast pair were not committed. They built five components: Button (with focus-visible state from day one), TextInput (with aria-describedby wiring for errors), Dialog (with focus trap), FormField (with label association), and ErrorSummary.

The first-adopter surface was the contract signing flow — the surface the enterprise customer used most and the one with the most a11y violations (31 out of 73). It was rebuilt in 12 days. Pre-system: the signing flow failed automated a11y checks on 9 criteria. Post-system: zero violations passed. The enterprise customer signed the contract extension on the same day the rebuilt surface shipped.

**Pull phase (weeks 6-14).** Dovetail's pull ratio was 2.5:1. Three components were contributed by the product engineering team: a tabbed navigation that the content surfaces needed, a file upload zone for document management, and a timeline component for contract lifecycle tracking. Each contributed component was paired with a system team member for documentation review.

**Governance phase (weeks 15+).** The governance body — system lead, one rotating engineer, the accessibility representative — formalized the a11y-enforcement rule: every component's CI build includes an axe-core check with zero-violation threshold. A component that introduces an a11y violation blocks the release. Two releases were blocked in the first quarter, each for one day while a missing label was added.

**What worked.** The a11y-first approach gave the system a clear value proposition that everyone understood. The enterprise customer's requirement was a forcing function that prevented scope creep. The consumer-impact-first approach to component changes — every change begins with "which surfaces does this affect and who do we need to tell" — prevented the system from becoming a black box that shipped surprises.

**What they would do differently.** They should have built the component inventory before the token set. The tokens made it easy to create new components, but the team spent three weeks on components that, it turned out, nobody needed (a social-share button, a collapsible code block). The inventory would have told them to build Table and Select instead. They also under-invested in the deprecation process — removing a rarely-used Chart component took four months and three escalation meetings.

**Measurable outcomes at week 20.** Adoption rate: 70% of new surfaces. Contract value directly tied to a11y compliance: $240k annually from the enterprise customer who required it. Open a11y violations in the product: down from 73 to 4 (all in legacy surfaces with scheduled migrations). Keyboard audit pass rate: 100% across system components. Screen reader user test pass rate: 100% (three participants, five key flows, no critical findings).

---

## Abstraction: Transferable patterns

Across both case studies, five patterns produced results:

1. **First-adopter surface before day 30.** Ship something real that a real team uses before the system's second month. The first-adopter surface is the system's proof-of-existence — without it, the system is a plan, not a product.
2. **One dedicated builder from the system team embedded in one consuming team.** Half-time from two people beats full-time from someone who does not ship production code. The embedded role is the conduit for real usage pressure.
3. **Track two simple metrics and publish them.** The pull ratio and the adoption rate are self-correcting: a low pull ratio means the system team is building ahead of demand; a flat adoption rate means the components are not solving real problems. Publish both on a dashboard visible to all consuming teams.
4. **Accessibility is not a later phase.** Both teams that started a11y work in the foundation phase had a smoother governance phase, fewer regression tests, and no eleventh-hour contrast patches. Both teams that deferred it paid for the delay.
5. **Governance before it is needed is overhead; governance after it is needed is chaos.** The transitions from foundation to pull and from pull to governance were signalled by metrics (adoption rate thresholds, request volume), not by weeks on a calendar. A team that adopts governance when adoption rate passes 60% has rules that fit their reality; a team that adopts governance at week 10 of a 26-week plan has rules that fit their plan.