# Versioning and Governance: Release Cadence, Change Review, and Deprecation

A design system without governance is a suggestion engine. Every team adopts what they like, ignores what they do not, and the system converges back to the pre-system state — a collection of locally-pragmatic exceptions with a global name. Governance is the set of rules that keeps the system coherent under the pressure of real shipping.

## Versioning scheme

Design systems version independently of the products that consume them. Use semantic versioning (MAJOR.minor.patch) with these definitions:

- **MAJOR** — breaking change: a token is removed or renamed, a component's public API changes (props, slots, emitted events), or any change that requires a consumer to update imports or usage to avoid a build or runtime error.
- **minor** — additive change: a new component, a new component variant, a new token in an existing tier, or a new theme. API must be backward-compatible. Existing consumers can upgrade without changes.
- **patch** — fix: a color value correction, a11y enhancements that do not change the DOM or API, documentation corrections, or dependency bumps that do not change system behavior.

Pre-release tags (-alpha, -beta, -rc) are allowed for system components that are published for early testing. Pre-release components must be marked with a status of `experimental` in both `component-inventory.md` and the component doc's frontmatter.

## The change governance process

Every change to the system — a new token, a component variant, a deprecation — passes through one of two tracks. The track determines how many reviewers, how long the review window, and what artifact the change produces.

**Track 1 — Fast track (patch and documentation-only).** One reviewer from the system team. The change ships in the next patch release. Changes that need fast tracking: color value corrections, text edits to docs, fixing broken links, adding examples. The reviewer checks only that the change is indeed a patch and that it has not slipped a behavior change into a patch release.

**Track 2 — Standard track (all MINOR and MAJOR changes).** Three reviewers: one from the system team, one from a consuming team, and one from the accessibility team. Minimum review period of three business days. Every change produces a change record (a markdown file in the system's `changelog` directory) that states: the change, the rationale, the affected files, the migration path for consumers, and the deprecation timeline if applicable.

A proposed change that receives objections from any reviewer is tabled. The objector must state their concern in writing. The change may be resubmitted with the concern addressed or escalated to the system's governance body for a decision. The governance body meets every two weeks; its members are listed at the top of this file, and any team that consumes the system may send a representative.

## Deprecation policy

A deprecated token or component remains available for a minimum of two MINOR releases (or one MAJOR, whichever is shorter) before removal. During deprecation:

1. The deprecated item is documented as deprecated with the MINOR version when deprecation starts, the planned removal version, and the recommended replacement.
2. The build emits a warning when a deprecated item is referenced. The warning includes the replacement and the removal version.
3. Consumers receive a deprecation notice at least one MINOR release before removal. The notice is a markdown file in the system root named `DEPRECATIONS-<version>.md`.

Exceptions to the deprecation timeline require a written approval from the governance body and must be announced to all consumer teams. An exception is itself deprecated — the item must be removed by the next MAJOR release.

## Token change governance

Because token changes ripple through every component and every product, they have their own additional rules:

- **New tokens.** Propose the new token with its three-tier placement, its rationale (what surface or component needs it that the existing set cannot serve), and at least two surfaces where the token would be used. A token proposed for one surface is too narrow — use a component override instead. The governance body evaluates new tokens with the question: "If we add this, which existing token should we remove to keep the set stable in size?" A token set that only grows, never shrinks, becomes unusable within two years.
- **Token value changes.** A value change at the primitive tier (e.g., `blue-600: #2563eb` → `#1d4ed8`) is a MAJOR change, because every semantic token that references it shifts. A value change at the semantic tier (e.g., `color-bg-page` now points to a different primitive) is also MAJOR unless it is a them-only change (the light theme stays the same; the dark theme's mapping changes).
- **Token removal.** Follow the deprecation policy above. Name the migration path for each token being removed: which token replaces it and, if no direct replacement exists, the CSS or theme override path consumers should use to preserve their current rendering while they transition.

## Component change governance

Component changes follow the same tracks but add a consumer impact assessment step before the review:

1. **Inventory the consumers.** Which products or teams use this component? Which versions of it? Check `component-inventory.md` and the system's usage telemetry if available.
2. **Assess migration cost.** For a breaking change: estimate the migration effort per consumer and publish it alongside the change record. A MAJOR change with no migration guide is not accepted.
3. **Stage the rollout.** Breaking changes ship in a pre-release version first. Consumers test against the pre-release and file migration issuesbefore the MAJOR ships. The MAJOR ships only when the open migration issues are below a threshold set by the governance body.

## Release workflow

1. The system maintainer proposes a release with a version and a changelog. The changelog lists every change since the last release, organized by MAJOR, MINOR, and PATCH, with the change record links.
2. The release candidate is published as a pre-release for a minimum of five business days. Consumer teams are notified via the system's announcement channel.
3. During the pre-release window, consumer teams test the candidate against their staging environments and file issues.
4. At the end of the window, the governance body reviews open issues. Any blocking issue (breaking change with no migration path, a11y regression) delays the release. Non-blocking issues are tagged with the target release for the fix.
5. The release ships. The changelog and migration guide are published to the system's documentation site. The governance meeting minutes include the release decision.

## Governance body composition

The governance body has standing members (three) and rotating representatives from consuming teams (one per team, changes each meeting cycle). Standing members: the system lead (designer), the system lead (engineer), and the accessibility representative. Consuming team representatives serve a two-cycle term with one overlap, so no meeting has an entirely new member.

## Escalation path

When governance reaches an impasse (a change is tabled twice or a release is blocked for more than two weeks), the escalation path is: system lead (engineer and designer together) decides. That decision is published with the reasoning, and the change is revisited after three MINOR releases to evaluate whether its assumptions held.