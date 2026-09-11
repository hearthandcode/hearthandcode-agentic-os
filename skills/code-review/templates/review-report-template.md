# Review Report

**Review ID:** `<generated>`
**Author:** `<reviewer-name>`
**Artifact:** `<file-or-module>`
**Date:** `<date>`

---

## Overall Verdict

**PASS / PASS-WITH-NOTES / REVISION-REQUIRED**

---

## Summary

In <N> lines, I found:
- <X> blocking issues
- <Y> major issues
- <Z> minor issues
- <W> suggestions

---

## Findings

### Finding #1: <Short Name>
- **Severity:** blocking / major / minor / suggestion
- **Location:** `<file:line>`
- **Evidence:** `<what I observed>`
- **Impact:** `<why it matters>`
- **Recommendation:** `<what to change>`

### Finding #2: <Short Name>
...

---

## Positive Notes

- `<what the code does well>`

---

## Checklist Summary

| Category | Count | Pass? |
|----------|-------|-------|
| Correctness | <N> | Yes/No |
| Security | <N> | Yes/No |
| Performance | <N> | Yes/No |
| Readability | <N> | Yes/No |
| Edge cases | <N> | Yes/No |

---

## Review Checklist (for the reviewer)

- [ ] I read every line of the diff, not just the hunks that looked suspicious
- [ ] Every blocking finding has a concrete exploit path or failure scenario
- [ ] Every major finding has a specific location and recommendation
- [ ] I distinguished blocking issues from personal preferences
- [ ] I included at least one positive note
- [ ] My feedback is actionable — the author can make a specific change
- [ ] I checked for related issues (same pattern elsewhere in the diff)