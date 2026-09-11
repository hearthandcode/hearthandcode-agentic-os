# Data Modeling Basics — Entities, Relationships, Normalization Trade-offs

The data model outlives the code. Frameworks are replaced and interfaces rewritten; tables and their constraints persist and shape every future feature. This reference covers the core craft: finding entities and relationships, deciding ownership, and making normalization decisions deliberately instead of by accident.

## Entities and attributes

An entity is a thing the system must remember, about which it stores facts that change independently. Practical extraction sequence:

1. **Mine the nouns from the domain language.** In a notes domain: user, note, tag, share, comment. Nouns that are only ever *values* of other things (a color, a currency code) are attributes, not entities.
2. **Apply the independent-existence test.** A `tag` exists independently of any note (a user can create tags before using them) → entity. A `note_title` exists only as part of a note → attribute.
3. **Name entities as singular nouns** (`note`, not `notes`) and be consistent; the plural belongs to collections and tables-as-set semantics, not the concept.
4. **Give each entity a stable identifier.** Surrogate keys (opaque ids) survive real-world identifier changes; natural keys (email) invite migration pain. Record which identifier is exposed externally — it becomes part of your API contract (`api-design-principles.md` rule: ids are opaque).
5. **Every entity carries provenance columns:** `created_at`, `updated_at`, and a soft-delete marker *if* deletion is undoable or auditable. Adding these later is a migration on the worst day of your quarter.

Attributes follow the atomicity rule: one fact per column. A `full_name` column becomes a problem the day you need to sort by surname; an `address` blob becomes a problem the day you filter by country. Do not over-split either — split when a query needs the parts, not speculatively.

## Relationships

Three kinds cover almost everything:

| Kind | Shape | Example | Modeling notes |
|---|---|---|---|
| **One-to-many** | FK on the many side | user → notes | The default. Index the FK; the FK defines ownership |
| **Many-to-many** | Join table | notes ↔ tags | Join table gets its own identity when it carries data (`note_tags(tag_id, note_id, position)`) |
| **One-to-one** | Unique FK | user ↔ settings | Usually a design smell: often two views of one entity, or a lazy split. Keep if the parts have different owners or lifecycles |

Rules that prevent pain:

1. **Decide cardinality from the domain, not the current feature.** "Notes have one owner" may become "notes have collaborators" — model what you know, but do not paint yourself into cardinality corners for no reason (e.g., a join table you can extend beats a comma-separated column you cannot).
2. **Cardinality is enforced in the schema** (constraints, unique indexes), not only in application code. Application-only invariants are eventually violated by the script that forgot them.
3. **Reference by id, display by join.** Store `owner_id`, never a denormalized `owner_email` string, unless you have consciously accepted the sync burden (see denormalization below).
4. **Model relationships for their lifecycle.** A share can be created, changed in permission, and revoked → it is a row with a state, not a footnote. A like with no un-like in the product is still usually a row — event history beats flag flips.

## Ownership

Every entity has exactly one owning component — the only writer of its tables. This is a modeling decision, not just a service-layout one:

- **Owner** defines schema, validates writes, and is the only component that mutates.
- **Readers** either query through the owner's interface or hold *explicitly derived* copies (caches, indexes, materialized views) that they can rebuild from the owner's data.
- **Two writers = a missing boundary.** If two components write the same table, the fix is not "be careful" — it is choosing one owner and converting the other to commands-through-owner or events.

A derived copy is only safe when it is *rebuildable*: state the rebuild path ("search index rebuilds from `notes` + `note_shares` in under 10 minutes"). A derived copy without a rebuild path is a second source of truth that will drift and eventually lie.

## Normalization and its trade-offs

Normalization organizes data so every fact is stored once. It is the default because it prevents the three classic anomalies:

- **Update anomaly:** the same fact in five rows; updating misses one → inconsistent data.
- **Insertion anomaly:** you cannot record a fact without unrelated facts existing.
- **Deletion anomaly:** removing one fact destroys another.

The normal forms in working terms (full formal definitions are in any database textbook):

- **1NF:** atomic values, no repeating groups. `tags = "work,urgent"` in a column is 1NF violation — you cannot index, join, or constrain members of that string. Fix: join table (or array/JSON column *if* you only ever read the whole list — a conscious trade-off, not a default).
- **2NF:** no partial dependency — a non-key column must depend on the whole key. In `order_items(order_id, product_id, product_name)`, `product_name` depends only on `product_id`. Fix: `product_name` lives with products.
- **3NF:** no transitive dependency — non-key columns depend on the key "and nothing but the key." In `notes(owner_id, owner_email)`, `owner_email` depends on `owner_id`. Fix: email lives with users.
- **BCNF and beyond:** matters for complex keys; in practice, 3NF-with-attention is the working target for transactional schemas.

**Stop at 3NF for OLTP.** The forms past 3NF resolve edge cases most application schemas never hit; the cost of chasing them is joins nobody reads. The honest exceptions are temporal and multi-valued facts, which deserve deliberate design rather than form-chasing.

### Denormalization: a trade you make on purpose

Denormalize when a *measured* read pattern beats the write-and-consistency cost. Each denormalization is a small contract with three clauses:

1. **The read it serves** — "note list shows tag chips without a join per note."
2. **The refresh mechanism** — updated in the same transaction as the source / by event / by periodic rebuild. Pick per case; "same transaction" is the strongest and cheapest when both rows live in one database.
3. **The drift check** — how you detect the copy disagreeing with the source ("nightly count comparison; alert on delta > 0.1%").

Common, usually-justified denormalizations: cached aggregates (comment counts), display copies of immutable-at-rest facts (an order's currency code at purchase time — history, not state), materialized search views. Common, rarely-justified: copying mutable display fields "to save a join" — a join on an indexed id costs microseconds; drift costs days.

### When a document store fits

Relational is the default because most domains have relationships. Reach for document models when: facts about an item arrive and are read as one blob (event payloads, per-device settings); the schema is per-variant; or write volume outpaces relational budgets. Still model entities and ownership first — a document store without a model is a pile of JSON with eventual opinions.

## A worked modeling pass (QuickNotes, condensed)

Domain nouns: user, note, tag, share, search index (derived).

1. Entities: `user`, `note`, `tag` (independent existence: yes), `share` (has lifecycle: permission, revocation).
2. Relationships: user→notes 1:N (FK on note); notes↔tags M:N via `note_tags(note_id, tag_id, position)`; note↔shares 1:N (`note_shares(note_id, user_id, permission)` — unique pair constraint).
3. Ownership: Notes owns `notes` + `note_tags`; Access owns `note_shares`; users in its own table owned by the account area. Search owns a derived index with a stated rebuild path.
4. Normalization: 3NF throughout. Deliberate denormalization: none yet — the tag-chips read is served by one indexed join at current scale; the revisit trigger is p95 list latency.
5. Consistency: strong inside Postgres for all owned data; search index eventually consistent (seconds), acceptable per scenario Q2.

Every derived copy names its rebuild; every constraint lives in the schema; one owner per entity. That is the whole discipline — the rest is iteration.
