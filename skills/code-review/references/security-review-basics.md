# Security Review Basics — Injection, Authorization, Secrets, Dependencies

Security review has an asymmetric cost function: a missed finding can cost the company,
while a false alarm costs minutes. This reference gives the four checks that catch the
most consequential defects — where untrusted data goes, who is allowed to do what, where
credentials live, and what code you are importing — plus the discipline for raising
findings that survive scrutiny.

## The reviewer's threat model

For most application code, the adversarial assumptions are few and stable:

- **Some inputs are hostile.** Anything that arrives from outside the trust boundary —
  user input, third-party API responses, webhook payloads, file uploads, headers — may be
  crafted by someone trying to break the system.
- **Some users are malicious, and all users are curious.** Authorization mistakes are
  usually found by ordinary users poking at URLs before any attacker arrives.
- **The code will be reused.** A helper built without input checks will eventually take
  input from a source its author never imagined.
- **Mistakes compound quietly.** A logged token is only an incident when it leaks; a
  weak hash is only broken when the dump happens. Review is where the cheap prevention
  lives.

## 1. Injection — where does the data go?

Trace every piece of externally-controlled data from entry to sink. The dangerous sinks
and their rules:

- **SQL.** The only acceptable construction is parameterized queries or a query builder
  that binds values. String concatenation or interpolation of values into SQL is a
  Blocker, always, no exceptions for "internal" endpoints.
  - The subtle case: identifiers (table names, column names, ORDER BY directions) cannot
    be bound parameters. They must be allow-listed against a fixed set the code defines.
    Sanitizing or deny-listing is not a fix; allow-listing is.
  - Review tip: grep the diff for query construction. If SQL fragments meet string
    operations, read the whole query path.
- **Shell commands.** User data into a shell string is a Blocker. Use argument-array
  APIs that never invoke a shell, or remove the shell need entirely.
- **HTML/JavaScript output.** All untrusted content in HTML output is escaped by the
  template engine's autoescaping — verify it is on and that no code path marks content
  safe by hand. `innerHTML`-style sinks and `eval`/`Function` with data are Blockers.
  URLs built from data need scheme validation (`javascript:` is a URL).
- **File paths.** Path traversal: user-controlled path segments joined onto a base
  directory must be canonicalized and verified to remain under the base —
  `..%2f` and symlink tricks included.
- **URLs and redirects.** Open redirects (redirect target taken from a parameter) are a
  finding; validate against an allow-list of hosts or a relative-path rule.
- **Deserialization.** Deserializing untrusted data into live objects (rather than inert
  data) is a Blocker in every ecosystem that has ever shipped it.
- **LDAP, XML, templates, regexes.** Each has an injection grammar of its own; the
  general rule is identical — the query structure comes from code, the data comes
  parameterized. Regex from user input is also a denial-of-service vector
  (catastrophic backtracking).

The reviewer's one-line test: *for each sink, ask "could this string change the meaning
of the statement, not just the data in it?"* If yes, the construction is wrong.

## 2. Authorization — who may do what?

Injection gets the headlines; broken authorization ships more often. Check every changed
or added data-access path:

- **Is there a check?** Every endpoint, job, or function that reads or writes tenant or
  user data must enforce a permission check. The absence is a Blocker even if "no one
  knows that URL exists" — security by obscurity fails on the first directory listing.
- **Is it at the enforcement layer?** A check in the UI or the client is decoration;
  the check must live where the data is served. Server-side, every time, per request.
- **Does it cover indirect access?** IDOR (insecure direct object reference): fetching
  `/invoices/45812` must verify the caller owns or may see invoice 45812 — enumeration
  by guessing IDs is the most common real-world exploit pattern. Prefer checking
  ownership in the query itself (`WHERE id = ? AND tenant_id = ?`) over checking after
  fetching.
- **Horizontal vs vertical.** Horizontal: user A reading user B's data. Vertical:
  ordinary user reaching admin function. Check both on every new path.
- **Mass assignment.** Can a client set fields it should not (`is_admin: true` in a
  profile update payload)? Bind accepted fields explicitly; never bind request objects
  straight into domain objects.
- **Deny by default.** New features start closed: no permission means no access. The
  review question is "what happens when no role matches?" — if the answer is "allowed,"
  the logic is inverted.
- **Elevation through workflow.** Can a permission be reached by chaining allowed
  operations (share a note, then read through the share after revoking)? Check the
  whole path, not just the front door.

## 3. Secrets — where do credentials live?

- **In the diff.** Any credential, token, private key, or connection string with a
  password is a Blocker — even in tests, even if "it's just a dev key." Rewriting
  history is worse than fixing it now. Mark it revoked after removal; exposure is
  assumed.
- **In logs.** Tokens, passwords, session ids, and full authorization headers must not
  reach logs or error reports. Review new log lines with the same care as new queries.
- **In fixtures.** Test fixtures get obviously-fake values (`test-secret-do-not-use`),
  never copies of real configuration.
- **In client bundles.** Anything shipped to a browser or mobile app is public; API keys
  in client code need proxying or restriction, and the review verifies which.
- **Rotation.** New external-service integrations should read credentials from the
  secret manager from day one; retrofitting secret management after launch is painful.

## 4. Dependencies — what did you just import?

A new dependency is supply-chain trust. For each added package:

- **Necessity:** could the standard library or an existing dependency do this? Each
  dependency is permanent attack surface and maintenance load.
- **Provenance and health:** maintained? Multiple maintainers? Recent releases? Known
  vulnerabilities (check the advisory database)? Typosquatting distance from popular
  names?
- **Blast radius:** what does it actually pull in (transitive dependencies)? A tiny
  package that drags a framework is not tiny.
- **Version pinning:** lockfile updated? Pinned to exact versions where the ecosystem's
  convention allows it?
- **Upgrade diffs:** version bumps of existing dependencies get their changelog read —
  a patch release that changes parsing behavior can be the vulnerability.

## Crypto and randomness quick rules

- Use the platform's standard high-level primitives; home-rolled crypto in a diff is a
  Blocker regardless of how well it reads.
- Security randomness comes from the cryptographic RNG, never from language-default
  PRNGs (`Math.random` and equivalents are predictable).
- Passwords are hashed with memory-hard, salted, purpose-built hashes (bcrypt/argon2
  class), never MD5/SHA-family alone.
- Comparisons of secrets (tokens, MACs) use constant-time comparison functions.

## Raising security findings

- **Severity honestly, but never silently.** An injection or missing authorization check
  is a Blocker. Say so plainly and explain the exploit in one or two lines — a proof
  turns a debate into a fix.
- **Offer the fix, not just the verdict.** The parameterized query, the ownership clause,
  the allow-list map — write it out. Security findings with fixes get fixed the same day.
- **Escalate scope when the pattern repeats.** One bad query is a finding; a codebase
  pattern of string-built SQL is an architecture handoff (per the SKILL's cross-skill
  boundaries) plus a tracking ticket to fix all occurrences.
- **Post-merge discoveries are incidents-in-waiting.** If review finds a Blocker after
  merge, the finding names the exposure window and the remediation owner. Review's job
  is to make that window an exception, not a norm.