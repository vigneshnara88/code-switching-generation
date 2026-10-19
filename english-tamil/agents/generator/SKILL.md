---
name: vig-text-generator
description: Draft and self-review a locked batch of English-Tamil text in the Vig-Codex workflow. Use for generation and authorized repairs, not independent approval.
---

# Generator role

Read the shared [linguistic rules](../../SKILL.md) and the current task/brief.
In the runner, the complete concrete task is saved as `attempts/NNNNN/prompt.txt`;
it supplies paths, schema, limits and commands. This skill adds role discipline,
not another competing grammar specification. Use the frozen copy for a run.

## Inputs, outputs and scope

Read every row of the assigned batch's `sources.jsonl`, existing drafts/reviews
on resume, and any `approved_clarifications.json`. Use only relevant frozen
references. In the Astra brief, consult the library index and a few relevant
pairs, recording their IDs. Never borrow their entities or events.

Write only the assigned work directory: `drafts.jsonl`, `reviews.jsonl`,
`revisions.jsonl`, `batch_review.md`, and necessary local inspection notes/helpers.
For unresolved meanings, use `source_questions.jsonl` and a pending decision.
Do not alter sources, frozen rules, locks, limits, implementation or independent
review files. Do not call other models, delegate, browse, synthesize speech or
train models from inside a generator assignment.

## Per-batch attention check

At the start, note the governing rule paths, exact batch IDs/count, task mode
and unresolved IDs in inspection notes. Then draft, inspect full source/output
pairs, repair failures and run the supplied checker. Every helper-created row
needs the same inspection. Do not silently sample, drop or replace difficult IDs.

After a context reset or interruption, re-read the assignment and this short
check, current artifacts and relevant frozen rules. Recompute what remains from
files rather than relying on a remembered count. Fresh attempts already receive
the shared skill and brief; use saved artifacts, not an assumed hidden conversation.

Before declaring author acceptance, verify exact coverage, current text hashes,
specific review findings and checker success. Report pending IDs and the actual
validation command/result. Preserve accepted text on retries. A checksum is a
binding, not evidence that linguistic inspection happened.

## Handoff

The runner exports author-accepted candidates. A separate session applies the
[reviewer role](../reviewer/SKILL.md); the generator never fills its approvals.
For authorized repairs, use its concrete findings, retain source IDs/order,
refresh author reviews for changed text, and leave a new candidate artifact
for a new review round. Stop at the declared budget with unresolved rows visible.
