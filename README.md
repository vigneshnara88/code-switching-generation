# Rule-guided code-switching generation

Language guidance, annotation conventions and review tools for English–Tamil and Malay–English code-switched text. The project grew from an interest in making multilingual language technology reflect how people actually move between languages.

**Status:** ongoing research and language-resource development.

## Why I started this project

In multilingual, cosmopolitan settings, people often use English alongside a home or community language rather than choosing one language for an entire conversation. They might keep a familiar sentence structure while borrowing a technical term, change language for emphasis, or use an expression that fits a particular relationship or setting. My interest is in making language technology work with that everyday mixture.

As social life becomes more internationally connected, I want to understand how these English–local-language combinations develop and how models can represent them. Code-switching is not simply replacing random words with translations: the choice of where to switch, which expressions to borrow and what sounds natural depends on the speakers and context. A model can produce a grammatically possible mixed sentence that still feels unlike the way a community speaks.

This motivates the central question: **can a generation-and-review workflow make those choices explicit enough to produce useful, inspectable code-switched examples?** English–Tamil and Malay–English provide the initial language pairs. The longer-term interest is a framework that can be adapted with speakers of other language communities.

Code-switched NLP is also a distinct evaluation problem in the research literature. [LinCE](https://aclanthology.org/2020.lrec-1.223/) brings together tasks and language pairs for comparison, while [Winata et al.](https://aclanthology.org/2021.calcs-1.20/) examine whether multilingual models handle mixed-language inputs effectively. These studies provide context for the project rather than performance claims about this implementation.

## What the rule-guided approach changes

Instead of asking a model only to “make this bilingual,” the workflow gives a drafting agent and a reviewing agent the same explicit language resources. Those resources record decisions about register, borrowing, morphology, meaning and annotation. When a reviewer rejects a phrase, the decision can be tied to a stated rule or a question for a speaker to resolve.

The point is to make generation easier to inspect and improve. A rule can be revised, an example can be traced to its explanation, and a disagreement can become a documented annotation decision. A successful structural check means the package or labels follow the contract; naturalness still requires speaker judgement.

## How a project uses these resources

1. **Choose the task and context.** Authoring a new sentence, rewriting an existing meaning and transcribing speech have different requirements. In transcription, the speaker's actual language choices take priority.
2. **Select a language package.** Read its task guidance, register notes, examples and annotation conventions before drafting.
3. **Draft and review.** Use the generator guidance to propose text, then the reviewer guidance to identify unsupported choices, meaning changes or awkward switches.
4. **Check the representation.** Use the included utilities where available to inspect examples, validate package structure and audit benchmark annotations.
5. **Build a speaker-reviewed collection.** Keep accepted examples, revisions and unresolved cases distinct so later evaluation can use a clear evidence base.

The files here provide the shared language-resource and review layer. They can support a model workflow without prescribing a particular model provider or claiming that a full training experiment is bundled in this repository.

## Longer-term motivation: documenting living language norms

I am interested in whether this work could help document how people actually combine languages, including forms that receive little attention in conventional monolingual resources. A speaker-reviewed collection could record not just a phrase, but the context, register and reasoning that make a particular switch appropriate. That would make it useful for future research on how multilingual communication changes.

“Preservation” here means keeping a record of language practices and making them visible to future tools and researchers. It should leave room for regional differences, individual preferences and changing norms. The aim is not to freeze a community's speech into one supposedly correct rulebook or substitute synthetic examples for its speakers.

Possible applications include better mixed-language captions and speech recognition, cross-community comparisons of switching conventions, and carefully evaluated synthetic examples for language technology. These are directions to investigate, with community participation and human review, rather than outcomes already demonstrated by this package.

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
