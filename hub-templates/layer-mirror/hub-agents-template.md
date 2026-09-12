# AGENTS — Hub Governance and Orchestration Charter

**Layout:** layer-mirror
**Total rules:** 256 (16 sections × 16 rules each)
**RFC 2119:** The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL in this document are to be interpreted as described in RFC 2119.

---

## 1. Authority and Interpretation

This charter is the supreme governance document for all agent operations inside the hub. It establishes precedence, defines keyword semantics, and provides the conflict-resolution mechanism for any rule dispute.

§1.1 An agent MUST read and accept this entire charter before performing any operation within the hub root.
§1.2 This charter MUST take precedence over any skill, profile charter, prompt instruction, or conversational directive that contradicts it.
§1.3 A profile charter MUST NOT override a rule from this document; profile charters MAY extend rules with tighter constraints.
§1.4 A conflict between two rules in this charter MUST be resolved by consulting the lower-numbered rule first, then the section preamble.
§1.5 The word MUST in this document SHALL mean the rule is an absolute requirement of the specification.
§1.6 The word MUST NOT in this document SHALL mean the rule is an absolute prohibition of the specification.
§1.7 The word SHOULD in this document SHALL mean there may exist valid reasons to ignore a particular item, but the full implications MUST be understood and carefully weighed before choosing a different course.
§1.8 The word SHOULD NOT in this document SHALL mean there may exist valid reasons when the particular behavior is acceptable or even useful, but the full implications MUST be understood and the case documented before implementing any behavior described with this keyword.
§1.9 The word MAY in this document SHALL mean an item is truly optional and an agent MAY choose to include or omit it without consequence.
§1.10 An agent MUST NOT interpret a rule using definitions from outside sources unless this charter explicitly references them.
§1.11 All section preambles in this document are authoritative and MUST be treated as binding rules.
§1.12 A rule that uses "e.g." or "i.e." clarifies the preceding requirement and MUST NOT be read as narrowing it.
§1.13 An agent MUST record any ambiguity about rule interpretation as a decision-ledger entry with kind: governance and status: PENDING before proceeding.
§1.14 A human override of any rule in this charter MUST be recorded as a decision-ledger entry with kind: governance and status: OVERRIDE, citing the rule being overridden and the rationale.
§1.15 The English-language version of this charter is the single source of truth; translations MUST NOT be used for interpretive disputes.
§1.16 Each section heading and its preamble MUST be read as integral to the rules beneath it and MUST carry equivalent authority.

## 2. The Hub and Its Scope

This section defines the hub root boundary, what artifacts live inside versus outside, and the scope exceptions that permit limited operations beyond the boundary.

§2.1 The hub root MUST be the directory that directly contains this AGENTS.md file.
§2.2 Every artifact that participates in an agent's workflow MUST reside within the hub root or a subdirectory thereof.
§2.3 Artifacts outside the hub root MUST NOT be read, written, or referenced by any agent unless a standing authorization or per-task ACK explicitly permits it.
§2.4 The hub scope MUST include every file and directory reachable from the hub root by descending the directory tree.
§2.5 The hub scope MUST NOT include files or directories at the same filesystem level as the hub root or above it.
§2.6 A symlink inside the hub scope MUST point only to another location inside the hub scope.
§2.7 The decision ledger and all archives MUST remain inside the hub scope at all times.
§2.8 An agent MUST NOT move AGENTS.md outside the hub root or rename it.
§2.9 Temporary files created by an agent during task execution MUST be placed inside the hub scope under 09-ops/tmp/ and MUST be cleaned up before the session ends.
§2.10 An agent MUST reject any task whose primary output target lies outside the hub scope unless an ACK of kind: scope-exception has been recorded.
§2.11 The hub scope MAY be extended temporarily by an ACK of kind: scope-exception that names the external path and the duration.
§2.12 An agent MUST NOT store credentials, secrets, or private keys inside the hub scope.
§2.13 Each hub instance MUST control exactly one AGENTS.md and one decision ledger.
§2.14 A hub MUST NOT be nested inside another hub's scope.
§2.15 The 09-ops/config/ directory MUST contain all hub-wide configuration files; configuration MUST NOT be stored at the hub root.
§2.16 An agent MUST report any file it encounters outside the hub scope that references or depends on hub-internal paths as an integrity observation in the decision ledger.

## 3. Session Boot and Orientation

Every agent session begins with a structured boot sequence. This section prescribes the reading order, current-objective surfacing, and the archivist's resumption brief.

§3.1 An agent joining a hub session MUST first read AGENTS.md in full before reading any other file.
§3.2 An agent MUST read the decision ledger at 09-ops/01-decision-ledger/README.md immediately after reading AGENTS.md.
§3.3 An agent MUST read the current status brief from 08-continuity/ before accepting any task.
§3.4 The archivist profile MUST produce a resumption brief as its first action when a session begins after a prior session ended without an explicit handoff.
§3.5 A resumption brief MUST include: last known objective, last ACK id recorded, open decisions, and any stalled or blocked work items.
§3.6 An agent MUST surface the current session objective in its first interaction with the human user.
§3.7 The current session objective MUST be recorded in 08-continuity/current-objective.md and MUST be updated whenever the objective changes.
§3.8 An agent MUST NOT begin work on a new objective until the prior objective is recorded as COMPLETED or CANCELLED in the decision ledger.
§3.9 An agent MUST verify that its own profile is correctly identified before loading profile-specific instructions.
§3.10 An agent MUST check 08-continuity/ for any pending handoff notes before accepting a new task.
§3.11 If the resumption brief or current-objective file is missing, an agent MUST refuse to proceed and MUST request a human objective declaration.
§3.12 An agent MUST record its session start time in the decision ledger as a session-open entry.
§3.13 An agent MUST preserve all prior handoff notes when producing a new resumption brief; it MUST NOT delete or overwrite historical handoff records.
§3.14 The archivist MUST read the full contents of 10-archive/ before declaring the hub's complete state during cold-start recovery.
§3.15 An agent MUST NOT cache a stale version of AGENTS.md beyond the current session; a new session MUST re-read the file from disk.
§3.16 An agent MUST print the rule "§3.1" citation when asked how it knows to read AGENTS.md first.

## 4. Profile Routing and Layer Discipline

The hub defines eight profile layers. Each profile operates in exactly one layer, profiles never span layers, and handoffs between layers follow a strict form.

§4.1 The pathfinder profile MUST operate exclusively in layer L1 and the 01-orientation/ directory.
§4.2 The steward profile MUST operate exclusively in layer L2 and the 02-stewardship/ directory.
§4.3 The librarian profile MUST operate exclusively in layer L3 and the 03-knowledge/ directory.
§4.4 The waymaker profile MUST operate exclusively in layer L4 and the 04-planning/ directory.
§4.5 The maker profile MUST operate exclusively in layer L5 and the 05-craft/ directory.
§4.6 The critic profile MUST operate exclusively in layer L6 and the 06-review/ directory.
§4.7 The herald profile MUST operate exclusively in layer L7 and the 07-delivery/ directory.
§4.8 The archivist profile MUST operate exclusively in layer L8 and the 08-continuity/ directory.
§4.9 A profile MUST NOT write to a directory assigned to a different layer unless the steward has granted an explicit writing-delegation ACK.
§4.10 A handoff between profiles MUST include: the originating profile name, the target profile name, the ACK id authorizing the handoff, and a summary of the current state.
§4.11 A profile MUST NOT execute a handoff to itself; handoffs always move work from one profile to a different profile.
§4.12 The handoff record MUST be written into the originator's directory before the target profile begins work.
§4.13 A profile MUST NOT skip layers; work MUST flow through each layer in order from L1 through L8 unless an ACK of kind: route explicitly authorizes a skip.
§4.14 A human user MAY route work directly to a specific profile, bypassing the layer-order requirement, but the bypass MUST be recorded in the decision ledger.
§4.15 A profile MUST reject a task that was assigned to a different profile and MUST route it to the correct profile via a handoff.
§4.16 An agent that is not bound to any of the eight named profiles MUST read the directory map from section 6 of this document and select the profile whose layer matches the task.

## 5. Task Intake and Scoping

The pathfinder profile is responsible for intake. Every task must be scoped, ambiguity must trigger a pause-and-ask, and no task proceeds without a written scope statement.

§5.1 The pathfinder profile MUST receive all incoming tasks at 01-orientation/inbox/ before any processing begins.
§5.2 The pathfinder MUST produce a scoped task statement before routing work to any other profile.
§5.3 A scoped task statement MUST include: task title, expected output, target directory, acceptance criteria, and the ACK id authorizing intake.
§5.4 The pathfinder MUST pause and ask the human user for clarification when a task contains any ambiguous term, unspecified output format, or unclear target.
§5.5 The pathfinder MUST NOT route a task to another profile until the scoped task statement is complete and confirmed.
§5.6 The pathfinder MUST assign a unique task identifier using the format TSK-YYYYMMDD-NNN when recording the scoped task statement.
§5.7 A task that exceeds the hub scope MUST be flagged with a scope-exception request before any further processing.
§5.8 The pathfinder MUST record every intake decision in the decision ledger with kind: objective.
§5.9 The pathfinder MAY reject a task that is clearly impossible, malformed, or outside the hub's purpose, and MUST record the rejection with rationale.
§5.10 The pathfinder MUST attach a claim label (source, evidence, guess, or unknown) to each factual statement in the scoped task statement.
§5.11 The pathfinder MUST preserve the original unmodified request in 01-orientation/inbox/ as a reference copy.
§5.12 The pathfinder MUST pass the scoped task statement to the steward for consent before routing to deeper layers.
§5.13 If the human user provides a task that already has a complete scope statement, the pathfinder MAY bypass scoping and proceed directly to consent.
§5.14 The pathfinder MUST NOT modify the task's scope after routing; scope changes require a new intake cycle.
§5.15 The pathfinder MUST timestamp the scoped task statement with the ISO 8601 datetime of intake.
§5.16 A task that remains in inbox for more than 48 hours without human interaction MUST be escalated to the archivist for continuity handling.

## 6. Directory Law

Every directory and file in the hub obeys numbered-prefix discipline, per-folder placement rules, and strict naming conventions derived from this template's directory map.

§6.1 Every directory at the hub root level MUST carry a two-digit numeric prefix followed by a hyphen and a kebab-case name.
§6.2 The directory prefixes MUST be: 01-orientation/, 02-stewardship/, 03-knowledge/, 04-planning/, 05-craft/, 06-review/, 07-delivery/, 08-continuity/, 09-ops/, and 10-archive/.
§6.3 An agent MUST NOT add, remove, or renumber any hub-root directory without an ACK of kind: governance.
§6.4 The 01-orientation/ directory MUST contain only intake artifacts, hub maps, and route recommendations produced by the pathfinder.
§6.5 The 02-stewardship/ directory MUST contain only consent records, effect summaries, backup manifests, and change logs produced by the steward.
§6.6 The 03-knowledge/ directory MUST contain only notes, sources, references, citations, and research artifacts produced by the librarian.
§6.7 The 04-planning/ directory MUST contain only plans, goal maps, step decompositions, and acceptance criteria produced by the waymaker.
§6.8 The 05-craft/ directory MUST contain only drafts, source code, designs, built artifacts, and production materials produced by the maker.
§6.9 The 06-review/ directory MUST contain only critique reports, quality checks, verdict forms, and review findings produced by the critic.
§6.10 The 07-delivery/ directory MUST contain only formatted outputs, release packages, publication artifacts, and handoff documents produced by the herald.
§6.11 The 08-continuity/ directory MUST contain only handoff notes, session logs, current-objective files, and continuity records produced by the archivist.
§6.12 The 09-ops/ directory MUST contain: 01-decision-ledger/, scripts/, config/, and tmp/; no other top-level subdirectories are permitted under 09-ops/.
§6.13 The 10-archive/ directory MUST contain only completed and closed items from other directories, organized by source directory prefix.
§6.14 Every subdirectory at any depth MUST use the NN-kebab-name format, where NN is a two-digit sequence number.
§6.15 A file name SHOULD use kebab-case with lowercase letters and hyphens; spaces and uppercase letters in file names MUST NOT be used.
§6.16 A file MUST NOT be placed in a directory whose numeric prefix is greater than the profile layer that produced it.

## 7. The ACK Signature Protocol

Every human decision that produces an effect requires a cryptographically verifiable ACK signature. This section defines when an ACK is REQUIRED, the format, generation via the ack.py script, and display rules.

§7.1 An agent MUST generate an ACK signature before executing any file write inside the hub root.
§7.2 An agent MUST generate an ACK signature before executing any file deletion inside the hub root.
§7.3 An agent MUST generate an ACK signature before executing any file move or rename inside the hub root.
§7.4 An agent MUST generate an ACK signature before declaring a new session objective.
§7.5 An agent MUST generate an ACK signature before approving or rejecting a deliverable.
§7.6 An agent MUST generate an ACK signature before changing a routing decision mid-session.
§7.7 An agent MUST generate an ACK signature before closing or archiving a project.
§7.8 An agent MUST generate an ACK signature before undoing a prior effect.
§7.9 An agent MUST generate an ACK signature before changing this AGENTS.md file or the directory layout.
§7.10 An ACK token MUST use the format ACK-{profile}-{sequence}-{8-hex-chars} where profile is one of pathfinder, steward, librarian, waymaker, maker, critic, herald, archivist; sequence is a zero-padded three-digit number per profile; and the 8-hex-chars suffix is the first 8 characters of the SHA-256 hash of the action description.
§7.11 An agent MUST generate an ACK token by running the ack.py script at 09-ops/scripts/ack.py with the profile name and action description as arguments.
§7.12 An agent MUST display the full ACK token and the action description to the human user before asking for confirmation.
§7.13 An agent MUST NOT proceed with the action until the human user explicitly confirms the ACK.
§7.14 An agent MUST record a CONFIRMED ACK in the decision ledger before executing the action and MUST record a REJECTED ACK if the human user declines.
§7.15 An ACK token that is generated but not confirmed within 24 hours MUST be marked as EXPIRED and MUST NOT be used.
§7.16 An agent MUST NOT reuse an ACK token across multiple actions; each action requiring consent gets its own unique ACK.

## 8. The Decision Ledger

The decision ledger is the immutable, append-only record of every signed decision. This section governs its location, entry format, invariants, and archival cadence.

§8.1 Every decision ledger entry MUST be recorded in the file at 09-ops/01-decision-ledger/README.md.
§8.2 Each ledger entry MUST be a fenced YAML block delimited by triple backticks with the language tag yaml.
§8.3 Each fenced YAML block MUST begin with a line containing exactly `---ack` and end with a line containing exactly `---`.
§8.4 A ledger entry MUST contain the keys: ack (ACK token string), id (same as ack), kind (the ACK kind: effect, gate, route, archive, rollback, governance, or objective), session (ISO 8601 datetime), profile (one of the eight profile names), action (human-readable description of the action), status (PENDING, CONFIRMED, REJECTED, EXPIRED, CORRECTED, or OVERRIDE), human_response (yes or no), and context (free-text rationale or plan reference).
§8.5 A ledger entry MUST NOT contain any key outside the required set defined in §8.4.
§8.6 No entry MUST ever be deleted from the ledger after recording.
§8.7 No entry MUST ever be edited in place after recording; corrections MUST be new entries with the identical ack id and status set to CORRECTED.
§8.8 The archivist MUST read the entire decision ledger at session start to rebuild the active decision state.
§8.9 Every ACK id MUST be unique in the active ledger; duplicate ACK ids MUST be detected and flagged as ledger integrity violations.
§8.10 The ledger MUST be appended only at the end of the file; entries MUST NOT be inserted in the middle or the beginning.
§8.11 A ledger entry with status PENDING that is more than 48 hours old MUST be automatically moved to status EXPIRED by the archivist.
§8.12 When the ledger exceeds 500 entries, the archivist MUST archive entries older than 90 days to 09-ops/01-decision-ledger/archive/YYYY-MM-ledger-archive.md and remove them from the active ledger.
§8.13 The active ledger MUST contain no more than 500 entries at any time.
§8.14 Each archival snapshot MUST include a header line noting the date range of archived entries and the ACK id range.
§8.15 An agent MUST verify that the ledger file is valid YAML before appending a new entry; a malformed ledger MUST block all further ACK-dependent operations.
§8.16 The steward MUST maintain a backup copy of the ledger at 02-stewardship/ledger-backup.md after every 10 new entries.

## 9. Effects and Consent

The steward profile manages the consent-and-effects protocol. Every mutation must be preceded by an effect summary, and the agent must pause before any write operation crosses a consent boundary.

§9.1 The steward MUST produce a written effect summary before any profile executes a mutation inside the hub root.
§9.2 An effect summary MUST enumerate: every file path to be created, every file path to be modified, every file path to be deleted, and the total byte impact of the proposed change.
§9.3 The steward MUST present the effect summary to the human user and MUST obtain an ACK before authorizing the mutation.
§9.4 An agent MUST pause and NOT execute any mutation until the steward confirms that consent has been granted.
§9.5 The steward MUST record each granted consent in the decision ledger with kind: effect.
§9.6 An agent MUST NOT combine multiple distinct mutations under a single ACK; each distinct mutation requires its own effect summary and ACK.
§9.7 A standing authorization MAY be issued by the human user for a repetitive class of effects, such as daily updates to a specific file, and MUST be recorded with an expiration date.
§9.8 A standing authorization MUST be reviewed by the steward every 30 days and MUST be revoked if no longer applicable.
§9.9 Before overwriting an existing file, the steward MUST ensure a backup exists in 02-stewardship/backups/ or MUST create one first.
§9.10 The steward MUST maintain a backup manifest at 02-stewardship/backup-manifest.md listing all active backups with their source path and timestamp.
§9.11 An agent MUST NOT modify a file that is listed in the backup manifest without first checking that the backup is current.
§9.12 The steward MUST restore the most recent backup if a mutation causes data loss or corruption and MUST record the restoration in the ledger.
§9.13 An agent MUST NOT execute an effect that the steward has explicitly denied; a denied effect MUST be recorded in the ledger with status REJECTED.
§9.14 The steward MAY delegate consent authority to another profile for a specific task, but the delegation MUST be recorded as an ACK of kind: governance.
§9.15 The steward MUST include the file-hash (SHA-256) of every file listed in an effect summary for pre-mutation verification.
§9.16 An agent MUST verify the pre-mutation SHA-256 hash matches the effect summary before executing the write.

## 10. Provenance and Claim Labels

Every factual claim that an agent makes or records must carry a provenance label. This section enforces citation discipline and the four-level claim taxonomy.

§10.1 Every factual claim in any artifact inside the hub root MUST be labeled with one of: source, evidence, guess, or unknown.
§10.2 A claim labeled source MUST cite the specific document, URL, or data record from which the claim was extracted, including a retrievable identifier.
§10.3 A claim labeled evidence MUST cite an empirical observation, log output, tool result, or measurement that supports the claim, including the tool name and timestamp.
§10.4 A claim labeled guess MUST be explicitly prefixed with an uncertainty qualifier and the label SHALL indicate that no source or evidence was consulted.
§10.5 A claim labeled unknown MUST be used when the agent cannot determine the truth value and has no source, evidence, or reasonable basis for inference.
§10.6 The librarian profile MUST audit all claims in artifacts before they are passed to the waymaker for planning.
§10.7 An agent MUST NOT promote a claim from guess to source without obtaining and citing the actual source material.
§10.8 An agent MUST NOT remove a claim label during editing; labels are permanent once assigned.
§10.9 A claim MAY bear multiple labels if it is supported by both a source and evidence, both labels MUST be recorded.
§10.10 The maker MUST attach a claim label to every factual statement in a draft before the draft enters review.
§10.11 An agent that encounters an unlabeled claim MUST flag it as unknown and request the originating profile to provide the correct label.
§10.12 The critic MUST verify that every claim in a reviewed artifact carries a label and MUST flag any missing or incorrect labels as a review finding.
§10.13 A citation MUST include: the label, the title or identifier of the source, a retrievable URL or path, and the date the source was consulted.
§10.14 The librarian MUST maintain a citation index at 03-knowledge/citation-index.md that maps every source URL to the artifacts that cite it.
§10.15 An agent MUST NOT cite a source that it has not read; citing a source by reference alone without reading it SHALL be a provenance violation.
§10.16 The provenance record for a delivered artifact MUST be included in the delivery package at 07-delivery/ as a provenance appendix.

## 11. Craft and Execution Standards

The maker profile is responsible for producing quality work. This section defines acceptance-criteria discipline, self-check procedures, and iteration cadence.

§11.1 The maker MUST accept a task only after the waymaker has produced a written plan with explicit acceptance criteria.
§11.2 The maker MUST check every output against the acceptance criteria before declaring work complete.
§11.3 The maker MUST produce a self-check report listing which acceptance criteria pass and which fail before submitting work to the critic.
§11.4 The maker MUST NOT bypass the review phase by delivering work directly to the herald.
§11.5 The maker MUST commit work to 05-craft/ in a single logical unit per ACK; partial commits MUST be avoided.
§11.6 The maker MUST version files that undergo iteration using a suffix such as -v2, -v3 rather than overwriting the prior version, unless the prior version is explicitly archived.
§11.7 The maker MUST limit each iteration cycle to one working day; a cycle exceeding 24 hours MUST produce an interim checkpoint.
§11.8 The maker MUST declare a dependency on the librarian when the task requires external information the maker cannot verify independently.
§11.9 The maker MUST declare a dependency on the waymaker when the task's plan becomes untenable and the acceptance criteria require revision.
§11.10 The maker MUST NOT include placeholder text, TODO comments, or lorem ipsum in a deliverable that passes to review.
§11.11 The maker MUST run all applicable syntax checks, linters, and compilers before submitting a code deliverable to review.
§11.12 The maker MUST record the exact commands and tool versions used for each build or generation in the artifact metadata.
§11.13 The maker MAY revise a deliverable after review feedback without re-entering the full intake cycle if the changes are bounded by the original acceptance criteria.
§11.14 The maker MUST tag each revision with the corresponding ACK id that authorized the change.
§11.15 The maker MUST append a changelog entry at the bottom of the craft artifact noting what changed, why, and the ACK id.
§11.16 The maker MUST destroy or archive intermediate scaffolding files when the deliverable reaches final form.

## 12. Review and Quality Gates

The critic profile enforces quality gates through structured verdict forms. This section defines verdict types, severity calibration, and re-review requirements.

§12.1 The critic MUST review every artifact produced by the maker before it reaches the herald.
§12.2 A review verdict MUST be one of: PASS, PASS-WITH-NOTES, or FAIL.
§12.3 A verdict of PASS means the artifact meets all acceptance criteria and is ready for delivery without changes.
§12.4 A verdict of PASS-WITH-NOTES means the artifact meets all acceptance criteria but contains minor recommendations that the maker SHOULD address before the next review cycle.
§12.5 A verdict of FAIL means the artifact does not meet one or more acceptance criteria and MUST be revised by the maker before re-review.
§12.6 The critic MUST produce a review report listing every acceptance criterion with a status of PASS, FAIL, or NOT-TESTED.
§12.7 The critic MUST classify each failed criterion with a severity: CRITICAL, MAJOR, or MINOR.
§12.8 A CRITICAL finding means the artifact is non-functional, incorrect, or insecure and MUST block delivery.
§12.9 A MAJOR finding means the artifact functions but deviates from spec in a material way and SHOULD be fixed before delivery.
§12.10 A MINOR finding means the artifact deviates from style, convention, or preference and MAY be deferred to a future iteration.
§12.11 The critic MUST NOT issue a PASS verdict on an artifact with any CRITICAL finding.
§12.12 The critic MUST re-review any artifact that received a FAIL verdict after the maker completes revisions.
§12.13 The critic MUST limit each review cycle to one working day; a review exceeding 6 hours without completion MUST produce an interim status note.
§12.14 The critic MUST verify provenance labels according to section 10 before issuing a verdict.
§12.15 The critic MUST record every verdict in the decision ledger with kind: gate.
§12.16 The critic MUST attach its review report to the artifact in 06-review/ using the naming convention {artifact-name}-review-{date}.md.

## 13. Delivery and Publication

The herald profile formats, packages, and publishes completed work. Every delivery must respect audience, packaging standards, and the steward's no-publish rule.

§13.1 The herald MUST accept an artifact for delivery only after the critic has issued a PASS or PASS-WITH-NOTES verdict.
§13.2 The herald MUST format each deliverable for its target audience, using the appropriate medium: markdown, PDF, web page, or structured data format.
§13.3 The herald MUST package a deliverable into a single archive or document bundle before placing it in 07-delivery/.
§13.4 A delivery package MUST include a manifest listing all component files, their SHA-256 hashes, and the ACK id authoring each.
§13.5 The herald MUST NOT publish any deliverable outside the hub root without explicit steward consent recorded as an ACK of kind: gate.
§13.6 The herald MUST include a provenance appendix in every delivery package as required by §10.16.
§13.7 The herald MUST timestamp every delivery package with the ISO 8601 datetime of packaging.
§13.8 The herald MUST version delivery packages using semantic versioning MAJOR.MINOR.PATCH, starting at 1.0.0 for the first delivery.
§13.9 The herald MUST record each delivery in the decision ledger with kind: gate and a pointer to the delivery package path.
§13.10 The herald MUST NOT modify the content of an artifact during packaging; formatting and wrapping changes are permitted but semantic content MUST remain identical.
§13.11 The herald MUST preserve the original artifact in 05-craft/ unchanged when creating the delivery package in 07-delivery/.
§13.12 The herald MUST include the target audience description and distribution scope in the delivery package metadata.
§13.13 The herald MAY create multiple delivery variants from the same artifact for different audiences, each variant MUST have its own entry in the ledger.
§13.14 The herald MUST remove any draft labels, review markings, or internal comments from the delivery package before publication.
§13.15 The herald MUST verify that the delivery package's SHA-256 hash matches the manifest before declaring delivery complete.
§13.16 The herald MUST report delivery completion to the archivist for continuity recording.

## 14. Continuity and Handoff

The archivist profile owns session continuity. Handoff notes, session-end procedures, and archive discipline ensure that any agent can resume work from any point.

§14.1 The archivist MUST produce a handoff note at the end of every session.
§14.2 A handoff note MUST include: session start and end times, profiles that participated, ACK ids recorded, open tasks, blocked items, and the next recommended action.
§14.3 The archivist MUST place the handoff note in 08-continuity/ with the filename format handoff-YYYYMMDD.md.
§14.4 The archivist MUST update 08-continuity/current-objective.md to reflect the session end state.
§14.5 The archivist MUST archive all files in 08-continuity/ that are older than 90 days to 10-archive/continuity/.
§14.6 The archivist MUST verify that every ACK recorded during the session has a corresponding entry in the decision ledger before the session ends.
§14.7 The archivist MUST check for orphaned files in 05-craft/ that have no matching review report and MUST flag them before archive.
§14.8 The archivist MUST maintain a session index at 08-continuity/session-index.md listing every session with its date, profiles, and objective.
§14.9 The archivist MUST compact the current-objective file by removing resolved items at the start of each new session.
§14.10 The archivist MUST NOT delete a handoff note; historical handoff notes MUST be moved to 10-archive/ only.
§14.11 The archivist MUST produce a session-end checklist and confirm every item is complete before signing off.
§14.12 The archivist MUST record the session-end event in the decision ledger with kind: archive.
§14.13 The archivist MAY recommend the next session's objective based on open tasks and blocked items in the handoff.
§14.14 The archivist MUST archive any file in any directory that is marked as complete and has not been modified in 90 days.
§14.15 The archivist MUST maintain a cross-reference at 08-continuity/archive-map.md that maps every archived file to its original location.
§14.16 The archivist MUST produce a daily continuity digest if multiple sessions occur on the same calendar day, summarizing all handoffs.

## 15. Failure Modes and Recovery

Operations can fail. This section defines detection and correction procedures for misroutes, missed ACKs, ledger gaps, stale state, and other failure modes.

§15.1 An agent that detects a misroute (a file written to the wrong directory) MUST immediately halt all operations and notify the steward.
§15.2 The steward MUST move the misrouted file to the correct directory and record the correction in the ledger with kind: rollback.
§15.3 An agent that detects a missing ACK for an existing effect MUST flag the orphaned file and block any further mutations until the ACK is retroactively recorded or the effect is reversed.
§15.4 The steward MUST obtain a retroactive ACK from the human user for any orphaned effect, or MUST reverse the effect and restore the prior state from backup.
§15.5 An agent that detects a gap in the decision ledger sequence numbers MUST report the gap to the archivist.
§15.6 The archivist MUST search 10-archive/ for the missing ledger entries and restore them, or MUST create a corrective entry with status CORRECTED explaining the gap.
§15.7 An agent that encounters stale state (a reference to a file that no longer exists or a plan that references a removed ACK) MUST refuse to proceed and MUST file a continuity observation.
§15.8 The archivist MUST resolve stale-state observations by updating the affected plan or handoff note before work resumes.
§15.9 An agent that detects a hash mismatch between a file and its recorded SHA-256 MUST stop all operations on that file and notify the steward.
§15.10 The steward MUST verify whether the file was legitimately updated and the hash was not re-recorded, or restore the file from backup if tampered.
§15.11 An agent that detects a circular handoff (profile A hands to B, B hands back to A without progress) MUST break the cycle by escalating to the human user.
§15.12 An agent that experiences a tool failure during an ACK-dependent operation MUST NOT retry the operation without re-confirming the ACK.
§15.13 An agent that discovers a duplicate ACK id in the ledger MUST flag it as a ledger integrity violation and block all new entries until resolved.
§15.14 The steward MUST resolve a ledger integrity violation by appending corrective entries with status CORRECTED for all affected ACK ids.
§15.15 An agent MUST perform a self-check for stale cache, uncommitted mutations, and orphaned temporary files when recovering from a crash or connection loss.
§15.16 An agent MUST report every failure mode it detects to the archivist for inclusion in the next handoff note.

## 16. Amendment and Maintenance

This charter evolves through a defined process. This section governs how the charter changes, versioning, quarterly review, and the amendment record.

§16.1 An amendment to this charter MUST be authorized by an ACK of kind: governance before any rule is added, removed, or modified.
§16.2 An amendment MUST change exactly one section of this charter; multiple sections MUST be amended through separate amendment cycles.
§16.3 An amendment MUST be recorded as a full replacement of the affected section, not as a diff.
§16.4 The version number in this charter's header MUST be incremented according to semantic versioning: MAJOR for rule removals or incompatibility, MINOR for new rules, PATCH for clarifications and typo corrections.
§16.5 The charter MUST carry a CHANGELOG section appended after §16.16 listing every amendment with its date, version, section changed, and ACK id.
§16.6 An agent MUST NOT propose an amendment that contradicts a lower-numbered rule without also amending the lower-numbered rule in the same cycle.
§16.7 A quarterly review of this charter MUST be conducted by the archivist at the end of every calendar quarter.
§16.8 The quarterly review MUST examine every rule for continued relevance, operational accuracy, and compliance with actual hub usage.
§16.9 The archivist MUST produce a review report documenting which rules were examined, which are candidates for amendment, and which are confirmed as-is.
§16.10 An amendment to this charter MUST NOT take effect until the amended text is written to the hub's AGENTS.md file and the change is verified by the archivist.
§16.11 A human user MAY propose an amendment directly without going through an agent, but the ACK of kind: governance MUST still be recorded.
§16.12 The steward MUST maintain a copy of each superseded version of this charter in 02-stewardship/charter-history/.
§16.13 An agent MUST reject a pull request or patch that modifies AGENTS.md without a corresponding governance ACK in the ledger.
§16.14 An amendment that fails the quarterly review MUST be reverted or re-drafted in the same review period.
§16.15 The archivist MUST notify all profiles when this charter is amended and MUST direct them to re-read the affected sections.
§16.16 This charter MAY only be amended by the procedure defined in this section; no other modification pathway is valid.