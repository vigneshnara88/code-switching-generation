# General English–Tamil lexical rules

A reusable rulebook for agents generating or reviewing English–Tamil text.
It supports English, Tamil and mixed-language inputs. Select rewriting,
scenario authoring or transcription before editing: each permits different
changes. These rules are language guidance and explicit annotation conventions,
not instructions for a particular model, dataset, experiment or sample count.

**Vignesh developed this comprehensive project rulebook through human iteration,
transcription work, generated-example inspection and Tamil language research.**
Its coverage includes meaning, grammar, spoken register, switching, morphology
and review. Peer feedback and further refinement are welcome. See
[how to add or revise rules](CONTRIBUTING.md).

| Read | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Compact agent entrypoint: task mode, meaning, grammar, annotation and review |
| [Astra style and overall balance](references/astra_style.md) | Natural bilingual constructions and roughly 50/50 overall, slightly toward English; no per-row quota |
| [400 historical Astra pairs](references/astra_style_examples.md) | Topic index, bounded lookup, 14 starter examples and exact saved pairs with provenance |
| [Linguistic details](references/linguistic_details.md) | Detailed suffix, light-verb, result-state, quotation, agreement, particle and switching guidance |
| [Input modes and examples](references/english_input_examples.md) | English, Tamil and mixed inputs; rewriting versus authoring versus transcription |
| [Meaning and edge cases](references/meaning_and_edge_cases.md) | Numbers, negation, conditions, ambiguous pronouns, quotations, multiple switches and incomplete sources |
| [Spoken Tamil](references/spoken_tamil.md) | Spoken/formal register, respect, dialect variation and contextual examples |
| [Worked pairs](references/worked_pairs.md) | Possible outputs, failed alternatives and the reasons to accept, repair or defer |
| [Annotation contract](references/annotation_contract.md) | Tags, script boundaries, names, loanwords, transcript/TTS views and checker limits |
| [Review checklist](review_checklist.md) | Whole-row review, concrete findings, repair and corpus-level checks |
| [Loanword candidates](loanwords.json) | Contextual mapping candidates; not an automatic replacement dictionary |
| [Evidence and scope](references/sources.md) | Research grounding and the limits of examples and local conventions |

Begin with the compact entrypoint and load the relevant detail as needed. Copy
the whole folder so references remain available. Application commands, source
selection, numerical targets and speech/training settings belong in the caller's
workflow and brief. For a matched comparison, give every arm the same source,
rule snapshot, examples and declared review policy.

No template can guarantee native naturalness or downstream recognition gains.
The examples are illustrative, not a human-certified gold corpus. Keep uncertain
local usage for contextual review by speakers familiar with the intended community.
