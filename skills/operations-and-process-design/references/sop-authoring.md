# SOP Authoring Guide

## What Makes an SOP Work

A standard operating procedure is not documentation. It is a set of instructions that, when followed without deviation by someone who has never done the task before, produces a consistent, correct result. If your SOP requires prior knowledge, assumptions, or judgment calls, it is not an SOP.

## The Five Signature Characteristics of Effective SOPs

1. **Single-task focus**. One SOP covers one discrete procedure. If the page title has the word "and" in it, split the document.
2. **Measurable opening and ending conditions**. The first line specifies the trigger: "When a client signs a contract." The last line specifies the settled state: "Project folder is created and the invoice is generated."
3. **A list of necessary prerequisites**. Every item the operator must have before starting: tools, access, permissions, information. If the operator cannot start because they are missing something, the book of instructions is incomplete.
4. **Steps, not paragraphs**. Short imperative sentences for one action each. No paragraphs, no context, no background. The background goes in a cover note in the outline; the SOP body is stripped of all context.
5. **Verification embedded**. Each step that produces a result should be followed by a verification: "Confirm the document renders with the correct formatting." Verification failures send the operator backward.

## The SOP Template Structure

The template, present in `templates/sop-template.md`, encodes these seven sections:

### 1. Title and Identifier
A unique ID in the format `[PROCESS-CODE]-[SEQUENCE]` for example `ONB-03`. The operator never writes this. It is seeded in the template.

### 2. Purpose Statement
One sentence beginning with "This procedure covers ..." and ending with "... from [trigger] to [terminal]." No more detail than that.

### 3. Prerequisites
A bullet list of everything required before starting: tools, access, documents, necessary approvals, knowledge. If the operator needs a specific permission level, write the set of permissions exactly.

### 4. Materials Referenced
A list of every template, form, or document the operator will need during execution. These should be hyperlinks, but in a paper SOP they should be a flat path to the physical file.

### 5. Procedure Steps
Numbered from 1. Each step is a single imperative sentence:
1. Open the template file.
2. Fill in the client name field.
3. Send the document to the reviewer.
If a step requires a decision, write it as: "___ If the approval is returned with changes, return to step 3."
Do not number the decision branches separately; use simplification.

### 6. Exit Criteria
One or two bullet points stating what must be true at the end of the procedure. "The document must be saved in the client folder and the document must be cc'd to billing."

### 7. Revision History
A small table: Date, Author, Change summary.

## The Newcomer Test

An SOP that passes the newcomer test: give the SOP to someone who has never done the task and no prior context on the process. The SOP is correct if they produce a correct result from the start in less than the standard time by a factor of 2. If they cannot, the SOP is missing a step, using jargon, relying on implicit knowledge, or having the wrong sequence.

### Running the Newcomer Test

1. Recruit someone who has never done the task.
2. Give them the SOP and the required tools, but no verbal guidance.
3. Observe without intervening.
4. Note where they stop, hesitate, or produce wrong output.
5. Revise the SOP at those points.
6. Repeat until the operator at step 4 of this test has no stop points or errors.

## Principles of SOP Clarity

- Write at a seventh-grade reading level. Short words, short sentences, short paragraphs.
- Use the active voice: "The operator opens the file" not "The file is opened."
- Use the imperative mood: "Open the file" is second person imperative, not "The operator opens the file." Consistent imperative voice is the norm across the SOP collection.
- Every step is verifiable. If a step cannot be right or wrong, collapse it into the surrounding context if possible.
- Defensive: include warnings for common mistakes. "Warning: renaming the file on export will break the reference in the client database."
- Jargon-free: any term that does not appear in the operator's training glossary gets a brief sidebar explanation.

## SOP Maintenance

- Every SOP has a review date. A 30-day review cycle for new SOPs, quarterly for established ones.
- When a process is changed, the SOP is updated before the process goes live. Not after: before.
- When someone raises a well-documented issue with an SOP, the SOP owner has one week to revise it or to produce a defensible reason not to.

### SOP Version Control

Removed SOPs are archived, not deleted. The archive record shows which version superseded them.

## Mistakes in SOP Writing

| Mistake | Why It Fails | Alternative |
|---------|-------------|-------------|
| Writing what the system should do rather than what the operator does | The operator cannot follow instructions to make the system do what it should | Describe operator actions only |
| Including "quality" steps in the instruction set separately with no way to enforce them | The operator will skip them if they are not required to verify | Make verification its own step in the procedure sequence |
| Over-specifying: too many contingent paths | The operator's mental model overloaded | Separate complex contingent paths into their own SOP |
| Using "if necessary" without a definition of the conditional | The operator has to guess what decision amounts to "necessary" | Replace "if necessary" with "If [condition], then [action]" |
| Writing the procedure from the author's perspective of the task, not the operator's | Expert blind spot: what is easy for the author is burdensome for the novice | Walk the steps alongside a novice with comprehension breakpoints |
| Style inconsistency across multiple SOPs | Operators lose trust in the document format | Enforce a consistent template: deviations need a clear rationale |

## SOP Style Reference

- Headings: H1 for the title of the SOP. No other H1 in the document. H2 for each of the 7 sections.
- Bold for actions: "**Open** the file manager." Do not bold whole sentences or long phrases.
- Lists for prerequisites: bullet style prefers bullet for enumeration, numbered for the procedure.
- Warnings: `> **⚠️** Warning text.` Do not use all-caps.
- Revisions: minor version formatting.

## Quality Check

Before delivering an SOP:

1. Leave the document for 24 hours after writing. Re-read the next day.
2. Run the text through a readability counter: aim for 13-15 or lower.
3. If you are giving it to a team, a second person reviews it first using the same newcomer test.
4. Check that every mention of a tool is the actual tool name and version, not a colloquial term.
5. Pair the SOP with the template it fills. The operator has both at the same time.