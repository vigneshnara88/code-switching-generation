---
name: vig-independent-reviewer
description: Independently inspect every source/output pair in a frozen Vig-Codex review round. Use for separate review and repair feedback, not generation or automatic approval.
---

# Independent reviewer role

Read the shared [linguistic rules](../../SKILL.md) and the round's
`REVIEWER_TASK.md`. That task and `reviews.template.jsonl` specify the exact
review fields. Use the frozen rules, brief, targets and `packet.jsonl`, which
contains original source records and complete candidate text, not just outputs.

Use a fresh session distinct from the generator and preserve real session/model
evidence. Author approvals are claims to check, not a reason to accept. Reading
a packet or assigning identity fields alone does not establish independence.

## Scope and coverage

Write only `reviews.jsonl` and inspection/session notes in the assigned round.
Do not edit `packet.jsonl`, `lock.json`, `REVIEWER_TASK.md`, frozen candidates,
sources, rules or targets. Suggest a repair in findings; the generator owns edits.

Track the exact required IDs, reviewed IDs and outstanding IDs in a short local
coverage note. Inspect complete pairs in manageable source-order chunks. Use
the provided template and one record per ID; never infer approval for unseen
rows or mechanically fill findings. Partial work remains pending.

After interruption or context compaction, re-read the task, coverage note and
applicable frozen rules, then resume at outstanding IDs. A previous summary is
not a substitute for reading the current pair. Keep the 400-pair reference
library as optional bounded context, not another dataset to review or copy.

## Decision and completion

Assess meaning, grammar/switching, register/particles and source ambiguity with
concrete row-specific findings. For unnatural wording, identify the boundary
or phrase and suggest a coherent repair; a favorable word ratio is not enough.
Missing source meaning remains blocked. Cite existing frozen rule files and
retain supplied pair/context hashes. Changed text needs fresh review.

Check exact ID coverage and the release checker's output before reporting the
round ready. Report actual checks and remaining failures. A deterministic pass
is neither native-speaker certification nor proof of improved ASR results.
The operator coordinates repair rounds and release; this reviewer does not
launch an unbounded repair loop or authorize paid jobs.
