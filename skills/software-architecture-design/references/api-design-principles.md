# API Design Principles — Resource Modeling, Versioning, Errors

An interface is architecture's public promise. Implementation can be replaced; a bad contract radiates outward for years. This reference covers the three parts of interface design at a boundary: what the operations and data look like (resource modeling), how the contract evolves (versioning), and what failure looks like (errors).

## Resource modeling

Model the *things* the system manages as resources, and the operations on them as a small, uniform set. Most APIs need only: create, read (one / many), update, delete, plus a few domain actions.

Rules of thumb:

1. **Nouns for things, verbs for actions that are genuinely not state changes.** `POST /notes` creates a note; `POST /notes/{id}/shares` grants a share (the share is a thing you create and can later delete). Model processes as resources only when they have a lifecycle worth tracking: `POST /exports` returns an export with a status you poll.
2. **Hierarchy expresses ownership, not convenience.** `GET /users/{id}/notes` is right when notes belong to users in your model. Do not nest deeper than two levels; use top-level resources with filters for anything deeper.
3. **Relationships are their own resources when they have data or lifecycle.** A share with a permission level and a revocation is a resource (`DELETE /notes/{id}/shares/{userId}`), not a boolean.
4. **Pagination is part of the contract, not a feature.** Every list endpoint returns a bounded page with an explicit cursor or offset and a documented sort order. Unbounded lists are production incidents in waiting.
5. **Filtering and field selection are query parameters with documented semantics** (`?status=archived&sort=-updated_at`), not bespoke query languages per endpoint.
6. **Ids are opaque.** Expose stable identifiers; do not require clients to parse meaning out of them. If clients must compute something from an id, the id is a contract you cannot change.

### The interface shape checklist

Before declaring an interface design done:

- [ ] Every operation has a named actor and an authorization rule.
- [ ] Every list operation paginates with a documented maximum page size.
- [ ] Every field is typed, and nullability is stated (absent vs. null vs. empty is defined).
- [ ] Idempotency is defined per operation — what happens when the same request is retried?
- [ ] Mutations that a user can trigger twice (double-submit) are safe or carry an idempotency key.
- [ ] The interface is testable from a plain HTTP client with no SDK.

## Versioning

A contract evolves or it dies. Choose the policy up front — it is nearly impossible to retrofit.

### The compatibility rule

Everything else is tactics; this is the law: **do not break running clients.** Additive changes are safe; removing, renaming, retyping, or resemantizing is breaking. Write the rule down in the API's overview and hold every change against it.

### Safe vs. breaking changes

| Safe (no version bump) | Breaking (needs policy) |
|---|---|
| Adding an optional request field | Removing a field |
| Adding a response field* | Renaming a field |
| Adding a new endpoint or method | Changing a field's type or meaning |
| Adding a new error code | Changing default values clients see |
| Relaxing validation (accepting more) | Tightening validation (rejecting more) |

*Adding a response field is safe only if clients ignore unknown fields — state that expectation in your API guidelines and enforce it in your own clients.

### Versioning mechanisms

- **Path versioning** (`/v1/notes`): blunt, visible, easy to route and deprecate. The pragmatic default for service APIs.
- **Header versioning:** finer-grained, keeps URLs stable, invisible in logs and harder to debug.
- **No version + strict compatibility:** works for internal APIs with disciplined additive-only evolution and a deprecation process. Cheapest if the discipline holds.

Pick one mechanism; do not mix. Record the choice in an ADR — it is a policy decision, not an implementation detail.

### Deprecation is a workflow, not a mood

1. Announce with a date: "field X is deprecated; removal on 2027-03-01."
2. Mark responses/notifications with the deprecation (header or docs), so *clients* can detect dependence.
3. Offer the replacement and a migration path before the removal date.
4. Measure: which callers still use the deprecated shape? Removal without usage data is faith-based.
5. Remove only after usage drops to the agreed floor — and keep the tombstone error message ("removed 2027-03-01, use /v2/...") so stragglers get a signal, not a mystery.

## Errors

Error design is where the contract meets failure. Two audiences with different needs: machines (code, retryable-ness) and humans (message, next action).

### The error contract

Return errors in one consistent shape, for every endpoint:

```json
{
  "error": {
    "code": "note_not_found",
    "message": "No note with id 'abc' visible to this account.",
    "retryable": false,
    "details": { "field": "noteId", "reason": "not_found_or_forbidden" }
  }
}
```

Rules:

1. **Stable machine codes.** `note_not_found`, `validation_failed`, `rate_limited` — codes are enum values clients switch on. Never change a code's meaning; add a new one.
2. **HTTP status maps to a small, consistent set.** 400 validation, 401 unauthenticated, 403 unauthorized, 404 absent, 409 conflict, 429 throttled, 5xx ours. Resist richer status taxonomies; nobody remembers them.
3. **`retryable` is part of the contract.** Clients need to know whether to retry now, retry later with backoff, or surface to a human. Ambiguity here produces retry storms.
4. **Validation errors enumerate.** One response lists every field problem, not the first: `details: [{field, reason}]`. Saves clients a round trip per fix.
5. **404 vs. 403: decide the information-disclosure policy explicitly.** For multi-tenant resources, returning 404 for "exists but not yours" prevents existence leaks; record the decision so it is applied uniformly.
6. **Human messages never contain internals.** No stack traces, no SQL, no vendor error strings. Log the details server-side with a request id; return the id so support can find the log line.

### Bulk operations

Batch endpoints need per-item results, not a single status: `results: [{index, status, code}]`. Partial success is a first-class outcome to design, not an exception to ignore.

## Design review for interfaces

Run these questions over any interface before it ships (they overlap the 40-point architecture review at `architecture-review-checklist.md`):

1. What happens when this operation is called twice with identical input?
2. What does the caller do when the operation times out — did the operation happen or not?
3. Which fields, if removed tomorrow, would break the newest client? (If the answer is "many," the contract is over-coupled to presentation.)
4. What is the largest possible page, and who pays for requesting it?
5. Are there operations that can only be discovered by reading the implementation? Move them into the contract or remove them.