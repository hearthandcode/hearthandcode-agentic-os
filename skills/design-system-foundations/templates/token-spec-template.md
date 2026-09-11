# Token Spec Template

Copy this file per token proposal. Delete this guidance block after filling it in.
The companion guide is `../references/design-tokens.md`; the machine-checkable
contract is `../schemas/design-tokens.schema.json`. Every new token must pass
the governance review in `../references/versioning-and-governance.md` before
it enters the token set.

## Guidance

A token spec is a one-page proposal for one new token or one small related
family (same tier, same scale). Do not propose tokens in batches of more than
five — batches larger than that skip the review each token needs and the
governance body will table them.

Before writing the proposal, confirm the scaffolding questions are answered:
- Which tier does this token belong to? If you cannot decide, write the
  primitive and the semantic proposals as two separate specs, because they
  have different reviewers and different criteria.
- What existing token does this replace or make redundant? The system's token
  set should stay stable or shrink; every new token should come with a
  candidate for removal, even if that candidate is "none."
- Where will this token be used? Name two or more surfaces or components.
  A token proposed for one location is better handled as a component-level
  override.

```markdown
---
name: <hyphenated-token-name>
tier: primitive | semantic | component
version: 0.1
status: draft            # draft | in-review | approved | deprecated
author: <your-name-or-team>
date: YYYY-MM-DD
governance-track: fast | standard
supersedes: <token-name-or-none>
---

## Rationale

One paragraph: what surface or component needs this value and why the existing
token set cannot serve it. If the rationale is "the design looks better at this
number," the token belongs in a component override, not the shared set.

## Proposed value

For **primitive** tokens: the raw value (hex, px, ms, ease curve).
For **semantic** tokens: the primitive it references and any transformation.
For **component** tokens: the semantic token it overrides and the override value.

If the token is a family (e.g., a new color ramp), list the values in a table.

| name | value | notes |
|---|---|---|

## Consumption surfaces

- Surface one: <name or path>
- Surface two: <name or path>
- (List at least two.)

## Theme implications

Does this token exist in all themes? If not, which themes get it?

- Light: <value or N/A>
- Dark: <value or N/A>
- High-contrast: <value or N/A>
- Brand variants: <value or N/A>

## Contrast check (semantic tokens only)

Foreground token: <token-name>
Background token: <token-name>
Expected ratio: <ratio>
WCAG AA pass: yes | no
WCAG AAA pass: yes | no

If either check fails, the token may only ship with a written accessibility
exception from the governance body.

## Migration path

If this token supersedes an existing one, name the replacement map:
- Old token → New token

If this token adds new capability with no replacement, write "No migration needed.

## Open questions

- <Question> — owner: <name>, resolve by: <date>
```

Fill-in checklist before submitting for review:

- [ ] Tier is correct — component tokens are the exception, not the default.
- [ ] At least two consumption surfaces named.
- [ ] Theme implications documented per theme; no missing values.
- [ ] Contrast check filled for every semantic foreground-background pair.
- [ ] Migration path written when superseding a token.
- [ ] Governance track matches the tier (fast: patch/primitives value fix;
      standard: all semantic or new tokens).