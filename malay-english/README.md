# Malay–English code-switching lexical rules

A reusable guide for writing, reviewing and annotating Malay–English mixed
speech text. It covers Malay grammar, conversational vocabulary, switching,
pronunciation and ASR references. Its starting profile is conversational Malay
and English in Singapore, with Malaysian usage identified where relevant.

**Status:** researched guidance with newly authored examples; not a native-speaker
certified corpus or a validated speech model. The sources describe different
communities and registers. No single study establishes a universal Malay–English
grammar. Project choices below are explicitly distinguished from observations.

## Start here

| Need | Read |
|---|---|
| Use the rules with an agent | [SKILL.md](SKILL.md) |
| Apply the grammar and switching rules | [Linguistic rules](references/linguistic_rules.md) |
| Choose conversational forms and particles | [Spoken Malay and register](references/spoken_malay_and_register.md) |
| Understand Malay sounds and spelling | [Pronunciation and ASR](references/pronunciation_and_asr.md) |
| Label actual switches and build an evaluation subset | [Annotation and benchmarking](references/annotation_and_benchmarking.md) |
| Preserve the source meaning | [Meaning and edge cases](references/meaning_and_edge_cases.md) |
| See complete rewrites and explanations | [Worked examples](examples/worked_examples.md), [JSONL](examples/worked_examples.jsonl) |
| Look up ambiguous words, loans and colloquial forms | [Lexical decisions](references/lexical_decisions.md), [JSON](lexicon.json) |
| Understand the benchmarks already tested | [Benchmark observations](references/benchmark_observations.md) |
| Review a candidate | [Review checklist](review_checklist.md) |
| Inspect evidence and limits | [Sources](references/sources.md), [provenance](PROVENANCE.md) |

## The practical approach

Choose whether the task is rewriting, authoring or transcription. For rewriting,
keep the source meaning and compose a plausible bilingual utterance. For
transcription, keep the words and languages actually spoken. Do not translate a
recording to manufacture a switch.

Use a coherent Malay or English clause frame, or a motivated change between
clauses. English nouns are only one option: verbs, pronouns and larger phrases
also occur in the research. Avoid imposing a 50/50 split on each sentence.
The literature documents varied patterns; the worked examples are proposals
illustrating the guide, not quotations from those studies.

Malay uses the same Latin alphabet as English in this package. **A Latin-letter
test cannot identify Malay–English switching.** Check words in context, distinguish
established Malay loans from English spans, and record ambiguous cases. Names,
numbers and a final `lah` alone are insufficient evidence for the conservative
evaluation subset defined here. This is an evaluation convention, not a claim
that linguists must exclude all particle or single-word switches.

## Small examples

| Source meaning | Authored mixed rendering | Point |
|---|---|---|
| I haven't submitted the form yet. | Saya belum submit borang itu. | `belum` retains “not yet”; the verb supplies English material. |
| Please check this file first. | Tolong check fail ini dulu. | `fail` is a Malay spelling; `check` is the English insertion. |
| I'll call you after I get home. | I'll call you selepas saya sampai rumah. | An English clause leads into a Malay time clause. |
| We, including you, can start now. | Kita boleh start sekarang. | `kita` preserves inclusion of the addressee. |

## Reuse

Read only the relevant references after the entrypoint. The machine-readable
lexicon is a contextual decision aid, **not** a search-and-replace dictionary or
an automatic language classifier. The example library is authored independently
of benchmark text and includes Malay, English and already mixed inputs.

Benchmark observations are diagnostic records outside the example library.
They preserve dataset IDs and provenance; no benchmark audio or full transcript
collection is redistributed. Reading a test set while developing guidance is
test-informed development, so future evaluation claims should disclose that
exposure and use a fresh held-out set when assessing a system tuned with this guide.

Run `python3 scripts/validate_package.py` from this folder to check file links,
source/rule references, example structure and annotation offsets. These checks
cannot establish fluency, semantic fidelity or correct acoustic realization.
The scripts use Python 3.10+ and the standard library; no model credentials are needed.

An agent can start with this prompt, followed by your source text:

```text
Read malay-en-codeswitch/SKILL.md and the references needed for this task.
Rewrite my inputs as conversational Malay–English, preserving their IDs,
meaning, quantities, time, negation and social relationship. Use the Singapore
conversational profile unless I specify another. Do not force a language ratio.
Return each original, proposed rewrite, relevant rule IDs, and any unresolved
meaning or naturalness concern. Mark these as authored candidates requiring
review. Do not use benchmark transcripts as generation examples.
```

For transcription, replace the rewrite instruction with an explicit instruction
to preserve the actual spoken words; language annotation must not change them.

This folder is independent of the Tamil rules and does not change the existing
Tamil generation pipeline. There are no model calls, audio synthesis jobs or
benchmark runs bundled with it.
