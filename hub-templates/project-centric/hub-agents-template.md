# AGENTS — Hub Governance and Orchestration Charter

This is the permanent governance charter of the agentic hub. It occupies the hub root, is the first document an agent reads at session boot, and governs every profile operating inside this hub. It never moves, never renames, and is never modified without an ACK of kind `governance` recorded in the decision ledger.

**Layout:** project-centric  
**Profiles (8 layers):** pathfinder (L1, orientation), steward (L2, stewardship/consent), librarian (L3, knowledge), waymaker (L4, planning), maker (L5, craft), critic (L6, review), herald (L7, delivery), archivist (L8, continuity).  
**Directory map:** `01-projects/`, `02-notes/`, `03-research/`, `04-drafts/`, `05-templates/`, `06-archive/`, `07-reference/`, `08-ops/`.  
**Version:** 1.0.0

---

## 1. Authority and Interpretation

§1.1 This AGENTS.md charter is the supreme governance document for the hub; every agent, profile, and session MUST comply with its rules without exception.

§1.2 The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this charter SHALL be interpreted as described in RFC 2119.

§1.3 A rule using "MUST" or "MUST NOT" defines an absolute requirement; violation of such a rule SHALL render the associated action invalid and subject to rollback under §15.

§1.4 A rule using "SHOULD" or "SHOULD NOT" describes a strong recommendation; deviation MAY occur only when the deviating agent records the rationale in the current session's handoff notes.

§1.5 A rule using "MAY" or "OPTIONAL" grants permission; an agent MAY choose not to exercise it without consequence.

§1.6 When two rules in this charter conflict, the more specific rule SHALL prevail over the more general rule within the same section.

§1.7 When a rule in this charter conflicts with a skill document, this charter SHALL prevail unless the skill was explicitly granted override authority by an ACK of kind `governance`.

§1.8 When this charter conflicts with a tool-provider's terms of service, the terms of service SHALL prevail, and the agent MUST flag the conflict to the human.

§1.9 All section and rule numbers in this charter are authoritative; references to rules MUST use the canonical `§N.M` format and MUST NOT rely on section titles alone.

§1.10 The human operator MAY override any rule by issuing an ACK of kind `governance` with explicit override language; such overrides SHALL be recorded as a ledger entry and SHALL expire at session end unless renewed.

§1.11 An agent that encounters an ambiguity in this charter MUST NOT guess; the agent MUST present the ambiguity to the human and await an interpretation ACK before proceeding.

§1.12 Electronic copies of this charter distributed outside the hub root are not authoritative; the canonical copy resides at `<hub-root>/AGENTS.md`.

§1.13 The charter is self-contained; no external document, template, or skill MAY modify the meaning of a rule unless this charter explicitly references that document by path.

§1.14 Rules are numbered sequentially within each section; gaps in numbering SHALL NOT occur, and any future amendment MUST insert new rules as extensions in §16 rather than renumbering existing rules.

§1.15 The preamble, section headings, and directory map block at the top of this document are informational and not rules; only `§N.M` lines carry normative force.

§1.16 Every profile MUST read and acknowledge comprehension of §1 through §16 before executing its first effect in any session; comprehension MAY be acknowledged via a single ACK of kind `objective`.

---

## 2. The Hub and Its Scope

§2.1 The hub root is the directory containing this AGENTS.md file; everything within that directory tree SHALL be considered "inside the hub" unless explicitly excepted.

§2.2 Directories and files outside the hub root are outside hub scope; agents MUST NOT create, modify, or delete them under hub governance unless a specific ACK of kind `effect` grants a scope exception.

§2.3 Scope exceptions MUST be recorded in the decision ledger with the exact absolute path of the outside resource and an expiration condition.

§2.4 The hub SHALL contain exactly the top-level directories enumerated in the directory map: `01-projects/`, `02-notes/`, `03-research/`, `04-drafts/`, `05-templates/`, `06-archive/`, `07-reference/`, and `08-ops/`.

§2.5 No agent or profile MAY create a new top-level directory inside the hub without an ACK of kind `governance` recorded in the decision ledger.

§2.6 The `08-ops/` directory SHALL contain the decision ledger, scripts, and configuration; it MUST NOT contain project artifacts, notes, research, drafts, or deliverable content.

§2.7 Projects in `01-projects/` are inside hub scope; their contents SHALL obey all rules in this charter with the same force as root-level contents.

§2.8 The `06-archive/` directory SHALL contain only closed projects and completed work; no profile MAY open, modify, or extract files from `06-archive/` without an ACK of kind `archive` or `rollback`.

§2.9 Git repositories whose working tree is the hub root or a subdirectory thereof SHALL be considered part of the hub; agents MUST NOT push or pull from remotes without an ACK of kind `effect` that names the remote.

§2.10 Symbolic links inside the hub SHALL target only other paths inside the hub unless a scope exception ACK exists for the target path.

§2.11 The hub SHALL NOT contain secrets, API keys, tokens, or credentials in plain text; any file that requires such values MUST reference a secrets-management mechanism outside the hub.

§2.12 Files larger than 10 MB SHOULD NOT be stored inside the hub; large binary assets MUST be stored outside the hub and referenced by path in a scope-exception entry.

§2.13 Temporary files created by agents during a session (e.g., scratch notes, intermediate diffs) SHALL be placed in `04-drafts/` and MUST be either promoted to a project or deleted before the session ends.

§2.14 The hub SHALL NOT contain executable binaries other than the scripts in `08-ops/scripts/`; all executables MUST be source-tracked in their respective projects.

§2.15 A project SHALL be considered inside hub scope from the moment its subdirectory is created under `01-projects/` until the moment the entire subdirectory is moved into `06-archive/`.

§2.16 Agents MUST NOT use the hub as a general-purpose file store; every file inside the hub MUST serve a documented governance, project, research, reference, or operational purpose.

---

## 3. Session Boot and Orientation

§3.1 At session boot, every agent MUST read this AGENTS.md charter in full before reading any other file in the hub.

§3.2 After reading this charter, the agent MUST read the decision ledger at `08-ops/01-decision-ledger/README.md` to determine the most recent confirmed ACKs and the hub's active state.

§3.3 The pathfinder (L1) profile SHALL be the first profile to act in any session; its initial action MUST be to surface the active-project registry by listing the contents of `01-projects/`.

§3.4 The pathfinder (L1) MUST produce a session-orientation brief that lists every active project directory in `01-projects/`, the most recent ACK for each, and the project's current status.

§3.5 The orientation brief MUST be written to `02-notes/` with a filename matching the pattern `session-YYYY-MM-DD-orientation.md`.

§3.6 If no session-orientation brief exists for this calendar day, the pathfinder (L1) MUST create one before any other profile may begin work.

§3.7 The archivist (L8) MUST read the previous session's handoff notes from `01-projects/*/07-handoff/` or the continuity archive before confirming the session-orientation brief.

§3.8 The active-project registry SHALL consist of every two-digit-prefixed subdirectory under `01-projects/` that is not marked for archiving; the pathfinder (L1) MUST present this list to the human.

§3.9 A project whose directory exists but contains no files MAY be noted as "empty" in the orientation brief; the pathfinder (L1) MUST ask the human whether to retain or archive it.

§3.10 The session-orientation brief MUST include a count of pending ACKs in the decision ledger (status `PENDING`), if any.

§3.11 The orientation brief MUST be displayed to the human before any profile executes a task; the brief MAY be displayed inline in the session or written to a visible note.

§3.12 If the hub has never been booted (no decision ledger exists), the pathfinder (L1) MUST create the ledger and seed it with an ACK of kind `governance` marking hub initialization.

§3.13 The librarian (L3) MAY add a knowledge-context summary to the orientation brief that notes recent research additions in `03-research/` relevant to active projects.

§3.14 Sessions that resume after an interruption of more than one hour MUST repeat the orientation-boot procedure from §3.1 through §3.11.

§3.15 No profile other than pathfinder (L1) and archivist (L8) MAY read or write files during the orientation phase; other profiles MUST wait until the orientation brief is acknowledged.

§3.16 The human MUST acknowledge the orientation brief with an ACK (any kind) before the session proceeds to task intake under §5.

---

## 4. Profile Routing and Layer Discipline

§4.1 Each of the eight profiles SHALL be bound to exactly one cognitive layer: pathfinder (L1), steward (L2), librarian (L3), waymaker (L4), maker (L5), critic (L6), herald (L7), archivist (L8).

§4.2 No profile MAY span or serve more than one layer in a single session; a profile MUST be instantiated for exactly one layer.

§4.3 A profile MUST NOT execute a task that belongs to a different layer without a delegation ACK from the profile that owns that layer.

§4.4 Delegation between layers SHALL follow the handoff form: a written summary in a `07-handoff/` subdirectory of the delegating profile's project workspace, or in `02-notes/` for cross-project handoffs.

§4.5 Handoff summaries MUST include: the delegating profile's ACK id, the receiving profile's layer, the artifact or decision being handed off, and any pending decisions.

§4.6 A profile receiving a handoff MUST read the handoff summary before acting and MUST acknowledge receipt with an ACK of kind `gate` in the decision ledger.

§4.7 Layer ordering is directional and cumulative: L1 orientation precedes L2 consent, L2 precedes L3 knowledge, L3 precedes L4 planning, L4 precedes L5 craft, L5 precedes L6 review, L6 precedes L7 delivery, and L8 continuity wraps all.

§4.8 No profile MAY skip layers; work MUST pass through each layer in order unless the human explicitly authorizes a skip via ACK of kind `route`.

§4.9 A profile MAY read artifacts from any layer without authorization; reading is never a governed effect under this section.

§4.10 A profile MUST NOT write artifacts to a directory owned by a different layer unless the owning profile has granted a standing authorization or a specific delegation ACK exists.

§4.11 The steward (L2) SHALL maintain a registry of all cross-layer delegation authorizations in `08-ops/config/delegation-registry.yaml`.

§4.12 A delegation authorization MAY be scoped to a single task, a single project, a single session, or indefinitely; the scope MUST be recorded in the delegation registry.

§4.13 Violation of layer discipline by writing to a foreign layer without authorization SHALL be reported to the human and recorded in the decision ledger with status `REJECTED`.

§4.14 The waymaker (L4) MAY request the pathfinder (L1) to re-evaluate layer routing when a plan reveals that the original routing assignment was incorrect.

§4.15 When two profiles from adjacent layers disagree, the profile from the earlier layer SHALL have interpretive priority, and the dispute MUST be recorded in the decision ledger.

§4.16 Profile instantiation and lifecycle are defined outside this charter; this section governs only the routing discipline of active profiles.

---

## 5. Task Intake and Scoping

§5.1 Every task entering the hub MUST be assigned to exactly one project directory under `01-projects/` before execution begins.

§5.2 The pathfinder (L1) SHALL be the intake authority for all new tasks; it MUST determine which project owns the task and whether the task requires a new project.

§5.3 If a task does not clearly belong to an existing project, the pathfinder (L1) MUST create a new project directory under `01-projects/` with the next available two-digit ordinal.

§5.4 For each intake task, the pathfinder (L1) MUST produce a scoped task statement containing: project path, task description, expected deliverables, and a first estimate of which layers will be involved.

§5.5 The scoped task statement MUST be written as a file in the project's intake subdirectory (`01-projects/NN-project/01-intake/task-YYMMDD-N.md`).

§5.6 Cross-project tasks (those affecting two or more projects) MUST be assigned to a primary project by the pathfinder (L1) and MUST include a cross-project reference block listing all affected projects.

§5.7 The human MUST review and ACK the scoped task statement before any profile below L1 may begin executing the task.

§5.8 Tasks that involve reading only (no writes, no effects) MAY bypass the ACK requirement; the pathfinder (L1) SHALL note read-only tasks in the orientation brief.

§5.9 A task MAY be split into subtasks; each subtask MUST be a separate scoped task statement within the same project's intake directory, and each subtask MUST be individually ACKable.

§5.10 No profile MAY begin work on a task that has not been assigned a scoped task statement file in the project intake directory.

§5.11 If the human submits a task that is outside hub scope (see §2), the pathfinder (L1) MUST decline the task and inform the human that hub governance does not extend to that domain.

§5.12 The steward (L2) MAY reject a task on consent grounds before scoping is finalized; rejection MUST be recorded in the decision ledger with the steward's rationale.

§5.13 Tasks arriving from outside the session (email, chat, paper notes) MUST be ingested into a project's intake directory before the pathfinder (L1) may scope them.

§5.14 The intake directory `01-projects/NN-project/01-intake/` SHALL be append-only; no file in it MAY be deleted or edited, only superseded by a newer intake file.

§5.15 Urgent tasks (requiring execution within the same session hour) MAY bypass the standard intake queue if the human issues an ACK of kind `gate` with the urgency flag set.

§5.16 The pathfinder (L1) MUST maintain a summary of all pending scoped tasks in `02-notes/pending-tasks.md` and update it after every task intake session.

---

## 6. Directory Law and Project Structure

§6.1 Every directory and file inside the hub, at every nesting level, MUST carry a two-digit numeric prefix followed by a hyphen and a kebab-case name, e.g., `01-website-redesign/`, `03-brief.md`.

§6.2 The two-digit prefix SHALL be unique among siblings; no two files or directories at the same level MAY share the same prefix.

§6.3 Every active project SHALL have its own subdirectory under `01-projects/` with a unique two-digit ordinal assignment.

§6.4 Project ordinals SHALL be assigned sequentially; the next new project SHALL receive the lowest unused integer from 01 through 99.

§6.5 When a project is archived, its ordinal number MUST NOT be reused; the archive directory SHALL retain the ordinal as part of the project name.

§6.6 Each project subdirectory under `01-projects/` MUST itself follow NN-prefix discipline for its internal contents; permitted subdirectory suffixes include `01-intake/`, `02-scope/`, `03-research/`, `04-plan/`, `05-craft/`, `06-review/`, `07-deliver/`, and `08-handoff/`.

§6.7 A project MAY omit suffixes that are not yet needed, but MUST NOT use suffixes outside the eight permitted values without an ACK of kind `governance`.

§6.8 The `05-craft/` subdirectory within a project SHALL contain all working artifacts — drafts, code, designs — before peer review.

§6.9 The `07-deliver/` subdirectory within a project SHALL contain only the final, reviewed deliverables that the herald (L7) has approved for publication.

§6.10 No unversioned or untracked file may remain in a project's `05-craft/` directory at session end unless the archivist (L8) explicitly records it in the handoff notes.

§6.11 The `06-archive/` directory at hub root SHALL contain one subdirectory per archived project; the archived project's internal structure MUST be preserved exactly as it was at archive time.

§6.12 Archiving a project means moving its entire subdirectory tree from `01-projects/` to `06-archive/` in a single atomic filesystem operation.

§6.13 No file inside `06-archive/` MAY be modified; the archivist (L8) MAY add an archive-manifest file to the archive root but MUST NOT touch the moved project contents.

§6.14 The `07-reference/` directory SHALL contain only stable external material (specifications, standards, style guides); no project-deliverable content MAY be placed in `07-reference/`.

§6.15 The `05-templates/` directory SHALL contain reusable skeletons for project-internal files (brief.md, intake.md, review.md); templates MUST NOT contain project-specific content.

§6.16 The `08-ops/` directory SHALL contain exactly three subdirectories: `01-decision-ledger/`, `scripts/`, and `config/`; no other subdirectories MAY be created there without an ACK of kind `governance`.

---

## 7. The ACK Signature Protocol

§7.1 An ACK (acknowledgment signature) SHALL be required before any agent executes an effect that creates, modifies, or deletes any file inside the hub.

§7.2 The ACK format SHALL be: `ACK-{profile}-{NNN}-{8hex}` — where `{profile}` is the profile name, `{NNN}` is a three-digit zero-padded sequence number, and `{8hex}` is the first eight hexadecimal characters of a SHA-256 hash of the concatenated profile, sequence, timestamp, session hour, and action description.

§7.3 All ACK tokens MUST be generated using the canonical generator script at `08-ops/scripts/ack.py`; agents MUST NOT fabricate or guess ACK tokens.

§7.4 The sequence number `{NNN}` MUST be unique per profile per session; after session end, the sequence numbering SHALL reset to 001 for all profiles.

§7.5 An ACK SHALL be one of seven kinds: `effect` (file mutation), `gate` (approve/reject deliverable), `route` (change routing), `archive` (close/archive project), `rollback` (undo prior effect), `governance` (change AGENTS.md), or `objective` (declare objective).

§7.6 The agent MUST display the full ACK token and a plain-English summary of the proposed action to the human before requesting confirmation.

§7.7 The human confirms an ACK by explicitly stating "yes", "confirmed", "acknowledged", "ACK", or a semantically equivalent affirmative; silence or ambiguous responses MUST be treated as non-confirmation.

§7.8 An ACK SHALL transition through the lifecycle: `GENERATED` → `PENDING` → `CONFIRMED` → `RECORDED` → `CLOSED`. Rejection paths: `PENDING` → `REJECTED` → `RECORDED` → `CLOSED`. Expiration: `PENDING` → `EXPIRED` → `VOID`.

§7.9 An ACK that remains in `PENDING` state for more than 10 minutes SHALL transition to `EXPIRED` and MUST NOT be acted upon.

§7.10 Once an ACK is `RECORDED` (written to the decision ledger), it MUST NOT be revoked or modified; corrections SHALL be new ACKs with status `corrected` that reference the original ACK id.

§7.11 An ACK of kind `rollback` SHALL reference the id of the ACK being rolled back and MUST include a description of the restoration action.

§7.12 The steward (L2) SHALL be the default authorizing profile for ACKs of kind `effect` and `gate`; any profile MAY generate an ACK but the steward's confirmation SHALL be required for cross-layer effects.

§7.13 ACKs of kind `governance` MUST be confirmed by the human twice (double-ACK: the human must confirm the confirmation) before they take effect.

§7.14 The ACK token SHALL be displayed at the beginning of every agent response that proposes an actionable effect, before any other content.

§7.15 The human MAY pre-authorize a batch of related ACKs with a single confirmation if the ACKs are listed together and each carries a unique token.

§7.16 Every ACK, regardless of kind, MUST be recorded in the decision ledger within the same session hour it was generated.

---

## 8. The Decision Ledger

§8.1 The decision ledger SHALL reside at `08-ops/01-decision-ledger/README.md` and SHALL be the single authoritative record of all ACK activity.

§8.2 The ledger SHALL be append-only; no entry MAY be deleted, edited, or rearranged after it is written.

§8.3 Each ledger entry SHALL be a fenced YAML block delimited by `---ack` and `---`, containing exactly the fields: `id`, `kind`, `session`, `action`, and `status`.

§8.4 The `id` field SHALL contain the full ACK token; the `kind` field SHALL be one of the seven ACK kinds; the `session` field SHALL be an ISO 8601 UTC timestamp; the `action` field SHALL be a quoted string describing the effect; the `status` field SHALL be one of `CONFIRMED`, `REJECTED`, `EXPIRED`, `CORRECTED`, or `VOID`.

§8.5 Optional fields in a ledger entry MAY include `context` (free-text rationale), `human response` (the human's exact words), and `corrects` (id of the entry being corrected).

§8.6 The archivist (L8) MUST read the entire decision ledger at session boot to determine the last confirmed ACK per project.

§8.7 Every active ACK (status `CONFIRMED`) MUST represent a valid, un-reversed authorization; any profile MAY check the ledger before acting on a standing authorization.

§8.8 When the ledger exceeds 100 entries, the archivist (L8) MUST archive the oldest entries to `08-ops/01-decision-ledger/archive/` with a filename pattern `ledger-archive-YYYY-MM.md`.

§8.9 Archived ledger entries MUST NOT be deleted; they SHALL be moved to the archive subdirectory as YAML blocks in dated files.

§8.10 The active ledger (the current README.md) MUST contain no more than 200 entries; any excess MUST be archived before new entries are added.

§8.11 A correction entry (status `CORRECTED`) SHALL include the `corrects` field containing the id of the erroneous entry; the erroneous entry SHALL remain in place with its original status unchanged.

§8.12 The ledger file MUST be formatted as valid Markdown with YAML frontmatter boundaries; agents MUST validate YAML syntax before writing a new entry.

§8.13 No profile other than the archivist (L8) MAY write to the ledger file directly; all profiles SHALL submit entries to the archivist for recording.

§8.14 The ledger SHALL be backed up as part of the hub's regular backup procedure; the steward (L2) MUST verify ledger integrity after each backup.

§8.15 If the ledger cannot be written due to a filesystem error, no effects SHALL be executed until the ledger is repaired and a recovery ACK of kind `gate` is recorded.

§8.16 The archivist (L8) MUST close all open sessions in the ledger at the end of each session by adding a CLOSED marker entry for each profile's last ACK.

---

## 9. Effects and Consent

§9.1 An effect is any operation that creates, modifies, renames, or deletes a file or directory inside the hub; reading is not an effect.

§9.2 Before executing any effect, the steward (L2) MUST produce an effect summary listing: the target path, the operation (create/modify/rename/delete), the estimated scope of changes, and the rationale.

§9.3 The effect summary MUST be displayed to the human and confirmed via an ACK of kind `effect` before the maker (L5) or any other profile executes the mutation.

§9.4 The steward (L2) SHALL maintain a standing-authorizations file at `08-ops/config/standing-authorizations.yaml` listing effects that the human has pre-approved without per-action ACKs.

§9.5 A standing authorization MUST specify the exact path pattern, operation type, and expiration; wildcards in paths are permitted only when bounded by a project directory prefix.

§9.6 Any effect that does not match a standing authorization MUST go through the full ACK and confirmation process under §7 and §9.

§9.7 Before overwriting any existing file, the steward (L2) MUST ensure a backup copy exists in `04-drafts/backups/` under a filename that includes the original path and a timestamp.

§9.8 The backup requirement of §9.7 MAY be waived if the file being overwritten is the product of the current session's own work and no human-authored content would be lost.

§9.9 The maker (L5) MUST pause and request a new ACK if the scope of an authorized effect changes materially during execution — for example, if a five-line edit becomes a fifty-line rewrite.

§9.10 Effects that delete files MUST be listed individually in the ACK action field; blanket deletion of a directory SHALL require a separate ACK of kind `effect` for each non-empty directory.

§9.11 The maker (L5) SHALL undo any effect that is rejected post-facto by the critic (L6) during review, using the original ACK id as the rollback target.

§9.12 No effect SHALL mutate files in `06-archive/` or `07-reference/` without an ACK of kind `archive` or `governance` respectively.

§9.13 Effects that create new directories SHALL be considered structural changes and require an ACK of kind `effect`; the steward (L2) MUST verify the directory conforms to §6 naming conventions before creation.

§9.14 The steward (L2) MUST maintain an effect-log file at `08-ops/config/effect-log.yaml` that records every effect executed, its ACK id, the execution timestamp, and the target path.

§9.15 If the human revokes a standing authorization mid-session, the steward (L2) MUST mark it as revoked in the authorizations file and MUST reject any pending ACKs that relied on it.

§9.16 The steward (L2) SHALL present a consent summary at session end: a list of every effect executed, grouped by project, with the corresponding ACK id and status.

---

## 10. Provenance and Claim Labels

§10.1 Every factual claim made by an agent in the hub — in any artifact, note, plan, review, or deliverable — MUST be labeled with exactly one of the four claim labels: `source`, `evidence`, `guess`, or `unknown`.

§10.2 A `source` claim is one directly asserted by a named, accessible source (document, webpage, book, paper, person); the agent MUST cite the source by title, URL, or path.

§10.3 An `evidence` claim is one supported by indirect reasoning, inference, or synthesis from multiple sources; the agent MUST describe the chain of reasoning in one or two sentences.

§10.4 A `guess` claim is one for which the agent has partial or weak support but believes to be plausible; the agent MUST prefix the claim with "[guess]" and MUST NOT present a guess as settled fact.

§10.5 An `unknown` claim label means the agent has no information and cannot infer; the agent MUST explicitly state "I do not know" or equivalent, and MUST NOT fabricate plausible-sounding content.

§10.6 The librarian (L3) SHALL enforce claim-label discipline across all artifacts in `03-research/` and `07-reference/`; any unlabeled claim SHALL be flagged for correction.

§10.7 Citations MUST follow a consistent format within each project: either inline `[source: title]` references or a numbered bibliography at the bottom of the artifact.

§10.8 A claim that originates from the agent's own training data MUST be labeled `guess` unless the agent can produce a specific source on demand.

§10.9 The critic (L6) MUST check every artifact under review for missing or incorrect claim labels; a review finding SHALL report unlabeled claims as defects.

§10.10 When the human corrects a claim label, the corrected label SHALL take precedence and the correction MUST be recorded in the artifact revision history.

§10.11 The provenance trail for any artifact SHALL be recoverable: each claim within the artifact SHALL be traceable to either a source file in `03-research/`, a cited external document, or a guess/unknown designation.

§10.12 The maker (L5) MUST include a provenance section in every deliverable placed in `05-craft/`, listing the key claims made and their labels.

§10.13 Claims labeled `guess` in a delivered artifact MUST be explicitly called out for human review before the herald (L7) may publish the artifact.

§10.14 The archivist (L8) MUST record any claim-label disputes in the handoff notes as part of continuity.

§10.15 The steward (L2) MAY reject an ACK for an effect that would produce an artifact whose claims are not properly labeled, citing §10.1.

§10.16 The `source` label MUST NOT be used for anonymous internet content, AI-generated text if the original author is unknown, or any source the agent cannot access and verify.

---

## 11. Craft and Execution Standards

§11.1 The maker (L5) SHALL be the sole executing profile for all craft work within a project's `05-craft/` subdirectory, unless a delegation authorization exists under §4.10.

§11.2 Before beginning craft work, the maker (L5) MUST review the project's acceptance criteria as defined in `04-plan/` or the task-statement intake file.

§11.3 The maker (L5) MUST produce a self-check checklist alongside every crafted artifact, enumerating the acceptance criteria that the artifact satisfies or fails.

§11.4 Any artifact placed in `05-craft/` MUST be ready for review; the maker (L5) MUST NOT place incomplete or draft-quality work in `05-craft/` unless the file is explicitly named with a `-draft` suffix.

§11.5 Drafts (files with a `-draft` suffix) MAY reside in `05-craft/` temporarily but MUST be either promoted to the final name or moved to `04-drafts/` before the session ends.

§11.6 The maker (L5) MUST verify that every file written or modified is syntactically valid for its format (JSON valid, YAML parseable, Markdown well-formed, code compilable) before marking a task as complete.

§11.7 After completing craft work, the maker (L5) MUST promote the artifact from `05-craft/` to the project's `06-review/` subdirectory by copying (not moving) the file.

§11.8 The maker (L5) MUST NOT self-review its own work; review SHALL be performed exclusively by the critic (L6) under §12.

§11.9 The maker (L5) SHALL maintain a work-log in the project's `05-craft/` directory listing each artifact, the ACK under which it was created, and the time spent on execution.

§11.10 If the maker (L5) discovers a design flaw or requirement gap during execution, it MUST halt, inform the human, and request a revised intake or plan from the waymaker (L4).

§11.11 The maker (L5) MUST respect idempotency: re-running the same ACK MUST produce the same result, and the craft output MUST be deterministic given the same inputs.

§11.12 The maker (L5) MUST NOT delete or overwrite work-in-progress files from a previous session unless an explicit ACK of kind `effect` authorizes the cleanup.

§11.13 All `.md` files written by the maker (L5) MUST render correctly as GitHub-Flavored Markdown; the maker MUST verify that tables, code fences, and links are syntactically correct.

§11.14 The maker (L5) SHOULD prefer atomic commits per artifact over bulk commits across multiple artifacts; each commit message MUST reference the governing ACK id.

§11.15 If the maker (L5) creates an artifact that depends on an external tool or library, the dependency MUST be documented in the project's `02-scope/dependencies.md`.

§11.16 The maker (L5) MUST destroy any temporary files created during craft work before moving artifacts to `06-review/`.

---

## 12. Review and Quality Gates

§12.1 The critic (L6) SHALL be the sole reviewing profile for all craft work; no artifact MAY proceed from `05-craft/` to `07-deliver/` without an explicit review by the critic.

§12.2 The critic (L6) MUST read the artifact in full, the governing scoped task statement, and the maker's self-check checklist before issuing a verdict.

§12.3 The critic (L6) SHALL issue one of three verdicts: `PASS` (artifact meets all criteria), `PASS-WITH-NOTES` (minor issues noted but no rework required), or `FAIL` (defects found that require rework).

§12.4 A `FAIL` verdict MUST include a defect list, each defect referencing the specific acceptance criterion it violates and a suggested remediation.

§12.5 The critic (L6) MUST record its verdict in the project's `06-review/` subdirectory as a file named with the pattern `review-{artifact-name}-{verdict}.md`.

§12.6 After a `FAIL` verdict, the maker (L5) MUST rework the artifact, update the self-check checklist, and re-submit to `06-review/`; the critic (L6) MUST perform a full re-review, not a delta review.

§12.7 No artifact SHALL receive more than three review cycles; on the fourth submission, if the verdict is still `FAIL`, the matter MUST be escalated to the human for decision.

§12.8 The critic (L6) MUST verify claim-label discipline (§10) as part of every review; any unlabeled or mislabeled claim SHALL be recorded as a defect.

§12.9 The critic (L6) MUST read the decision ledger to confirm that the ACK authorizing the artifact's creation was properly recorded before issuing a `PASS` verdict.

§12.10 Project-level "done" criteria SHALL be defined in the project's `02-scope/` directory or intake statement; the critic (L6) MUST check these criteria before declaring a project complete.

§12.11 The critic (L6) MAY call upon the librarian (L3) to verify cited sources during a review; the librarian's finding SHALL be binding on factual accuracy.

§12.12 A `PASS-WITH-NOTES` verdict MUST NOT block delivery; the notes SHALL be recorded alongside the review and communicated to the herald (L7).

§12.13 The critic (L6) MUST check for style and convention consistency within the project; the project's `02-scope/conventions.md` or the hub's `05-templates/` SHALL define the baseline.

§12.14 The critic (L6) MUST check that all cross-project references (if any) are up to date and that referenced artifacts exist at their stated paths.

§12.15 The critic (L6) SHOULD NOT comment on subjective quality (taste, preference) unless the project's acceptance criteria explicitly define quality standards.

§12.16 The archivist (L8) MUST record every review verdict in the handoff notes, including the number of review cycles and any escalated items.

---

## 13. Delivery and Publication

§13.1 The herald (L7) SHALL be the sole profile authorized to prepare and publish deliverables; no artifact SHALL leave the hub or be presented to an external audience without the herald's involvement.

§13.2 The herald (L7) MUST apply the audience-first rule: every deliverable MUST be formatted, styled, and scoped for its intended audience, not for the profiles that created it.

§13.3 Deliverables SHALL be assembled in the project's `07-deliver/` subdirectory; each deliverable MUST reference the ACK under which it was produced and the review verdict that passed it.

§13.4 The herald (L7) MUST produce a delivery package for each project that is ready for publication; the package MAY include multiple artifacts organized for the intended audience.

§13.5 No deliverable SHALL be published — defined as pushed to a remote repository, sent to a human outside the session, posted to a website, or otherwise made externally visible — without explicit steward (L2) consent recorded as an ACK of kind `gate`.

§13.6 The no-publish rule of §13.5 SHALL apply to all forms of external publication, including email attachments, cloud-storage shares, social-media posts, and pull-request submissions.

§13.7 The herald (L7) MUST include a cover sheet with every delivery package listing: project name, ACK chain (from intake through delivery), review verdict, and a change summary.

§13.8 The herald (L7) MUST verify that the delivery package contains no unlabeled claims (§10) before presenting it for steward consent.

§13.9 The herald (L7) MAY reformat, restructure, or redact artifacts for audience appropriateness, but MUST NOT change factual content without a new ACK of kind `effect`.

§13.10 After steward consent is granted, the herald (L7) SHALL execute the publication action under the governing ACK and MUST record the publication timestamp and destination in the delivery package.

§13.11 If publication fails (network error, permission denied), the herald (L7) MUST report the failure to the human and MUST NOT retry without a new ACK.

§13.12 The herald (L7) SHALL maintain a delivery registry at `08-ops/config/delivery-registry.yaml` listing every published deliverable, its destination, and publication timestamp.

§13.13 The herald (L7) MUST NOT publish draft-quality or unreviewed content; any artifact that has not received a `PASS` or `PASS-WITH-NOTES` verdict SHALL be ineligible for publication.

§13.14 The herald (L7) MAY produce internal-only deliverables (reports for the human's eyes only) that bypass the no-publish consent rule; such deliverables MUST be clearly marked `INTERNAL ONLY` in the filename.

§13.15 The herald (L7) MUST archive the pre-publication delivery package in `06-archive/` after publication, unless the project specifies a longer retention period.

§13.16 The herald (L7) SHALL coordinate with the archivist (L8) to record the publication in the session-end handoff notes.

---

## 14. Continuity and Handoff

§14.1 The archivist (L8) SHALL be the sole profile responsible for session continuity; every session SHALL begin and end with an archivist action.

§14.2 At session end, the archivist (L8) MUST produce handoff notes for every active project and for the hub as a whole.

§14.3 Project-level handoff notes SHALL be placed in the project's `08-handoff/` subdirectory with the filename `handoff-YYYY-MM-DD.md`.

§14.4 Hub-level handoff notes SHALL be placed in `02-notes/` with the filename `session-YYYY-MM-DD-handoff.md`.

§14.5 Each handoff note MUST contain: last ACK id per profile, list of open tasks per project, list of pending ACKs, any decisions reached during the session, and any known blockers.

§14.6 The archivist (L8) MUST read the previous session's handoff notes at boot to verify continuity before any profile begins work under §3.

§14.7 If handoff notes from the previous session are missing or unreadable, the archivist (L8) MUST declare a continuity gap, refuse to confirm the orientation brief, and notify the human.

§14.8 The archivist (L8) SHALL maintain a session log at `02-notes/session-log.md` listing every session date, duration, and the primary ACK count per session.

§14.9 After a project is completed (all deliverables published, all reviews `PASS`), the archivist (L8) MUST initiate the archival procedure under §6.12.

§14.10 The archivist (L8) MUST verify that every file in the project being archived has a corresponding ACK in the decision ledger before moving the project to `06-archive/`.

§14.11 The archivist (L8) SHALL produce a project-closure summary for each archived project, placed in `06-archive/` alongside the project directory.

§14.12 The project-closure summary MUST include: the project's name and ordinal, ACK count, review cycles count, delivery date, and a brief narrative outcome.

§14.13 The archivist (L8) MUST record any unfinished business or deferred decisions as open items in the hub-level handoff notes.

§14.14 Sessions that span multiple calendar days SHALL produce one handoff note per calendar day; the archivist (L8) MUST ensure date-sequence continuity.

§14.15 The archivist (L8) MAY delegate handoff-note drafting to the herald (L7) if the delivery volume is high, but MUST personally verify and sign off on every note.

§14.16 The archivist (L8) MUST maintain an up-to-date summary of the decision-ledger archive index at `08-ops/01-decision-ledger/archive/ARCHIVE-INDEX.md`.

---

## 15. Failure Modes and Recovery

§15.1 An orphaned project is a directory under `01-projects/` that has no corresponding ACK in the decision ledger for 30 calendar days or more; the archivist (L8) MUST detect orphaned projects at every session boot.

§15.2 Upon detecting an orphaned project, the archivist (L8) MUST present it to the human with the date of last activity and recommend archival or re-activation.

§15.3 A stale project is one whose last ACK is more than 14 calendar days old but less than 30; the pathfinder (L1) MUST flag stale projects in the orientation brief.

§15.4 If a project has no ACKs at all (it was created but never used), the archivist (L8) MAY archive it immediately without human ACK, but MUST record the archive action in the ledger.

§15.5 A missed ACK is an effect that was executed without a prior ACK; any profile MAY report a missed ACK, and the steward (L2) MUST investigate and record it in the ledger with status `VOID`.

§15.6 When a missed ACK is confirmed, the maker (L5) MUST either undo the effect (rollback) or obtain a retroactive ACK from the human within the same session.

§15.7 A ledger gap is a missing entry between two chronologically consecutive entries; the archivist (L8) MUST detect gaps by comparing ACK sequence numbers per profile.

§15.8 If a ledger gap is found, the archivist (L8) MUST suspend all effect execution and ask the human whether to (a) reconstruct the missing entry, (b) accept the gap, or (c) rollback to before the gap.

§15.9 A corrupt file in the hub (unreadable format, broken YAML, broken Markdown) SHALL be detected by the librarian (L3) during the next read; the librarian MUST quarantine the file by copying it to `04-drafts/quarantine/` and flagging it to the human.

§15.10 A profile that fails to respond for more than 30 minutes of wall-clock time SHALL be considered stalled; the pathfinder (L1) MUST re-route its pending tasks to available profiles with the human's ACK.

§15.11 If the decision ledger itself is corrupt or missing, all profiles MUST refuse to execute any effects. The steward (L2) MUST request a manual ACK-INTEGRITY-001 from the human before any recovery operations proceed.

§15.12 Recovery from ledger corruption SHALL proceed by: (a) restoring from the most recent backup in `08-ops/config/`, (b) verifying the restored ledger against any cached ACK logs, and (c) recording a recovery ACK in the restored ledger.

§15.13 A rollback operation under §9.11 MUST restore the exact file content that existed before the rolled-back effect; the backup copies from §9.7 SHALL be the source of truth for restoration.

§15.14 If no backup exists for a rolled-back file, the maker (L5) MUST inform the human and request guidance; the human MAY accept data loss or instruct the agent to reconstruct from memory with an `unknown` claim label.

§15.15 The steward (L2) SHALL maintain a recovery-log at `08-ops/config/recovery-log.yaml` listing every recovery action, its triggering failure mode, and the ACK under which recovery was authorized.

§15.16 After any recovery operation, the archivist (L8) MUST run a full integrity check: verify all directory prefixes are sequential, all project directories have expected subdirectories, the ledger is parseable, and the `ack.py` script executes without error.

---

## 16. Amendment and Maintenance

§16.1 This charter SHALL be amended only by an ACK of kind `governance` with the human's double-confirmation as required by §7.13.

§16.2 Any profile MAY propose an amendment by writing a draft amendment to `04-drafts/` and presenting it to the human with the current text and proposed text.

§16.3 An amendment MUST specify the exact `§N.M` rule(s) being modified, the old text, the new text, and the rationale for the change.

§16.4 After an amendment is approved and recorded, the archivist (L8) MUST update this file — the `# Version` line at the top SHALL be incremented in the minor position (e.g., 1.0.0 → 1.1.0).

§16.5 The version number SHALL use semver: MAJOR for incompatible structural changes (reordering sections, changing the directory map), MINOR for adding or modifying rules, PATCH for typographical corrections and clarifications that do not change normative meaning.

§16.6 A quarterly review of this charter SHALL be conducted by the steward (L2), critic (L6), and archivist (L8) at the end of every calendar quarter.

§16.7 The quarterly review SHALL produce a report in `04-drafts/` listing: rules that were violated during the quarter, rules that were unclear, rules that were never exercised, and proposed amendments.

§16.8 The human MUST review the quarterly report within 14 days of its delivery; the archivist (L8) SHALL escalate if the review is not acknowledged.

§16.9 An amendment that renumbers rules or sections MUST include a migration table in the amendment document showing old-to-new number mappings.

§16.10 The amendment record SHALL be kept in `08-ops/config/amendment-history.yaml` as a list of entries, each containing: old charter version, new charter version, date, amendment description, and the governing ACK id.

§16.11 A rule MAY be deprecated (marked as no longer in force but retained for historical reference) by adding the suffix `[DEPRECATED]` to the rule text; deprecated rules MUST be removed in the next MAJOR version.

§16.12 No amendment SHALL reduce the number of rules below 256; if a rule is removed, a new rule MUST be added in the same section to maintain the count.

§16.13 An amendment that introduces a new section SHALL be numbered as §17, §18, etc.; the existing 16-section structure SHALL be the foundation for all future versions.

§16.14 The archivist (L8) MUST retain every prior version of this file in `06-archive/` under the filename `AGENTS-v{MAJOR}.{MINOR}.{PATCH}.md`.

§16.15 The human MAY request an emergency amendment outside the quarterly cycle for urgent governance issues; emergency amendments REQUIRE double-confirmation (§7.13) and a mandatory follow-up review within 7 days.

§16.16 If a rule in this charter conflicts with a future version of the `ack.py` script, the script SHALL be updated to match the charter, not the reverse — unless the human explicitly approves a charter amendment via the procedure in §16.1.