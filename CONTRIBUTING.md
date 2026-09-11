# Contributing

Thank you for considering a contribution to hearthandcode-agentic-os. This
repository is a starter system built from general professional knowledge —
the principles, patterns, and techniques that any practitioner can write
about. Every contribution must maintain that posture.

## What we accept

- **New skills** — self-contained expertise packages following the contract in
  `spec/0006-skill-charter-contract.yaml`. See `docs/04-skills.md` for the
  how-to-author guide and `docs/06-extending.md` for the full checklist.
- **New profiles** — layer-bound profile charters following the template in
  `spec/0004-profile-charter-template.yaml`. See `docs/06-extending.md`.
- **Improvements to docs, installer, or scripts** — bug fixes, better
  explanations, deeper worked examples.

## Before you submit

1. **Read the contracts.** The `spec/` directory is the law of this
   repository. Any code or content you write must match the contract that
   governs its location. When prose disagrees with a contract, the contract
   wins.

2. **Follow the safety rules in `spec/0008-abstraction-and-safety.yaml`:**
   - Write from general professional knowledge. No internal code names,
     project names, hostnames, paths, usernames, emails, or personal
     identifiers from any private system.
   - If a passage could only have been written by reading a private system,
     it is a leak — rewrite from public knowledge or cut it.
   - When unsure whether something leaks, exclude it.

3. **Meet the style bar from `spec/0006`:** Depth over shallow presentation.
   Every artifact should teach its craft operationally. A reader should be
   able to *do the work* after reading, not merely know about it. Generic
   filler and restated boilerplate are defects.

4. **Run the verifier:**
   ```bash
   python3 scripts/verify_repo.py --shape
   python3 scripts/verify_repo.py --installer
   python3 scripts/scan_leaks.py
   ```
   All checks must pass before opening a pull request. If you are adding a
   new skill, the shape check will validate your skill directory against the
   contract in `spec/0006`.

5. **No placeholders.** No TODO, FIXME, "lorem ipsum", or "example content
   goes here" anywhere. If a section is not ready, the submission is not
   ready.

## Pull request process

1. Fork the repository.
2. Create a feature branch (`my-name/my-change`).
3. Make your changes.
4. Run the verifier suite and fix any failures.
5. Open a pull request with a description of what you changed and why.
6. A maintainer reviews against the spec contracts. If the contracts need
   updating to accommodate your change, that discussion happens before the
   merge.

## Code of conduct

Be constructive. Assume good faith. This is a small project about building
tools that respect human agency — the review process reflects that value.