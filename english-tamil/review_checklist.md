# Review checklist for English–Tamil text

Review the actual source/context and the exact complete candidate. An author's
claim that rules were followed is not evidence that the final text was inspected.
Use the task mode and annotation policy supplied by the caller.

## 1. Source and meaning

- Confirm the source ID and whether the task is rewriting, authoring or transcription.
- Check actors, actions, objects, recipients, possession and relationships.
- Preserve names, quantities, units, time relations, negation, aspect and modality.
- Check conditions, cause/contrast, quantifier scope, question type and quoted speech.
- Identify facts added or omitted. Authoring freedom must be explicit; a sparse
  cue is not authority to invent facts in a faithful rewrite.
- Retain ambiguity where the source leaves it open. Names alone do not establish
  gender; a generic relative does not establish a specific Tamil kinship term.

## 2. Grammar, switches and register

- Read each clause as a grammatical unit and the whole turn for coherence.
- Check Tamil case, suffix form, agreement, negation and light/result verbs around
  English material. Do not attach suffixes or `பண்ணு` mechanically.
- Keep an English auxiliary with a complete compatible predicate. Do not leave
  `been` stranded inside a Tamil predicate as a shortcut to mixing.
- Preserve the referent through multiple switches and the boundary of a quote.
- Judge brief insertions on their grammatical function and meaning. Do not reject
  a natural short mix solely because it has one English word or one Tamil span.
- Choose spoken/formal register from context, including respect, intimacy and
  quoted register. Do not impose a gender/name lookup or one dialect as truth.
- Check particles and fillers for discourse function; event meaning alone does
  not establish unchanged stance. Preserve the source endpoint without padding.
- Assess naturalness separately from meaning and tag validity. Identify any
  arbitrary translated tail, literal calque, incompatible register or awkward
  information flow. Compare a different full construction for doubtful rows.
- For the Astra-style brief, consult the [reference examples](references/astra_style_examples.md).
  Explain what makes the new switch coherent in its own source; matching an old
  percentage, noun or ending is insufficient.

## 3. Annotation and speech views

- Check the declared tags, language spans, Tamil/Latin boundaries and punctuation.
- Preserve Tamil suffixes while retaining intended English stems in Latin.
- Review loanword suggestions contextually; avoid substring substitutions.
- Check that literal annotations, glosses or speaker metadata have not become speech.
- Distinguish a linguistic error from the validator's character/inventory limits.
- Compare tagged text, plain transcript and TTS text for equal spoken content
  after their explicitly defined annotation transformations.

## 4. Acceptance, repair and deferral

| Decision | Appropriate when | Required finding |
|---|---|---|
| Accept | Meaning, grammar, register and annotation satisfy the declared task | Specific findings tied to the source and current text |
| Revise | A concrete repair can satisfy the task without guessing material facts | Exact defect, intended correction and source evidence |
| Pending | Source meaning, policy or local usage cannot be resolved yet | The ambiguity and smallest clarification needed |

For example, “Kept past sending, the same file and yesterday; did not add a
reply” is a concrete semantic finding. “Looks good” or “all rules checked” is not.
Record the source/candidate identity, relevant rule references, reviewer identity,
resolved machine flags and any remaining concern. A hash binds an approval to a
string; it does not prove linguistic correctness or reviewer independence.

Repair the defect, then reinspect the affected complete clause/turn and regenerate
annotation/TTS views. Recheck duplicates against the whole pool. Preserve earlier
versions. Under an independent-review workflow, the author cannot supply the
independent approval; retain separate session records. At the retry limit, keep
unresolved rows pending instead of dropping them to claim full coverage.

## 5. Corpus review

Inspect coverage by the declared contexts and forms, output duplication, repeated
wrappers, language balance, turn lengths, particle use and review disagreement.
Repeated grammar is normal; near-identical stories or fixed openings can reveal
template over-concentration. There is no universal ratio, word count, switch count
or quota in this rulebook. Use only predeclared study targets and source-supported
variety. Do not fabricate content or treat a local result as a general grammar rule.

The [Astra reference](references/astra_style.md) suggests roughly 50/50 overall,
slightly toward English, as a soft project preference. Measure and report the
aggregate; let individual sentences vary. Inspect repeated English-prefix/Tamil-tail
patterns and forced morphology even when the aggregate looks right. Do not repair
already natural rows solely to hit a percentage or turn this preference into an
undeclared rejection threshold.

Model-assisted acceptance is not native-speaker certification. Review a stratified
sample with qualified speakers to assess linguistic quality, including flagged
and apparently easy cases. Text review, audio quality and downstream model
performance require separate evidence.
