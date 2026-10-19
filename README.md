# Rule-guided code-switching generation

Language guidance, annotation conventions and review tools for English–Tamil and Malay–English code-switched text. The project grew from an interest in making multilingual language technology reflect how people actually move between languages.

**Status:** ongoing research and language-resource development.

## The approach

A drafting agent and a reviewing agent use a shared rulebook. The rules make constraints explicit: preserve meaning, use an appropriate spoken register, respect grammatical boundaries, and record annotation choices. The reviewer can then point to a specific constraint when a draft needs revision.

This repository contains the language-resource and review layer: rule packages, authored examples, source notes, an example lookup utility and Malay–English validation/benchmark-audit scripts. Model training, speech synthesis and the full experiment runner are separate from this package.

## Contents

| Directory | Contents |
| --- | --- |
| `english-tamil/` | Language guidance, morphology, spoken register, review instructions, annotation conventions and historical example lookup. |
| `malay-english/` | Language guidance, lexical decisions, worked examples, source ledger, package validator and local benchmark auditor. |

Each language package retains its own evidence and provenance notes. Illustrative generated examples are not a speaker-validated gold corpus. Language usage varies by community and context.

## Using the resources

Start with the relevant package's README and compact `SKILL.md`. Choose rewriting, authoring or transcription before applying the rules: transcription should preserve what was spoken, rather than invent language switches.

The Malay–English package's structural validator can be invoked from its directory:

```powershell
cd malay-english
python scripts/validate_package.py
```

The utility checks structure and annotation consistency. It does not establish linguistic naturalness or speech-model performance. Python 3.10 or later is required for the included utilities; see each package's instructions for optional benchmark inputs.

## Connection to SwitchF1

The generation work also motivated a separate evaluation tool, [SwitchF1](https://github.com/vigneshnara88/SwitchF1). I developed it to examine whether an ASR transcript preserves the language switches in a reference, a question that ordinary word error rate does not directly answer. Its precision, recall and F1 structure is familiar; the project defines how aligned, directed switch events are matched and counted.

Use switch preservation alongside word/character recognition scores and human review. Neither a linguistic rulebook nor a switch score alone establishes the quality of a speech recognizer.

## Research directions

Possible extensions include cross-language comparisons, speaker-reviewed generation, documentation of switching conventions and evaluation of synthetic multilingual training data. These are research questions, not claims that generated text already preserves community conventions or improves every downstream model.

This side project was influenced by internship experience. Broader experimental materials require a separate ownership and release review before inclusion.
