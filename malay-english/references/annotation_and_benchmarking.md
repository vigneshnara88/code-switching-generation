# Language annotation and a defensible ASR subset

This is a proposed Malay–English annotation contract. It is **not a claim that
these labels or this filter were used in the existing retention experiments**.
For what those experiments actually selected, read
[benchmark observations](benchmark_observations.md).

Word-level identification matters when scripts overlap ([S06](sources.md#s06)).
The broader code-switching annotation literature distinguishes names, ambiguous
items and mixed words ([S07](sources.md#s07)). The exact inventory and decisions
below are this package's conventions, not that paper's Malay-specific gold labels.

## Keep three layers

1. **Original:** immutable source reference, audio ID, source recording/clip,
   source offsets, repository revision and available hashes.
2. **Surface transcript:** words actually spoken under a declared transcription
   and punctuation policy. Retain disfluencies according to that policy. Never
   translate the audio to satisfy a language filter.
3. **Analysis:** contextual language spans, lexical decisions, morphological
   decomposition where useful, uncertainty and review evidence. An optional
   scoring-normalized string is a fourth, derived field with its own rules.

Use UTF-8 and Unicode-code-point offsets, zero based and end exclusive, for spans
in this package. `text[start:end]` must equal the stored span text. Spans must not
overlap; punctuation and spacing can be retained as `NONLEX`. Do not use byte
offsets or silently switch to JavaScript UTF-16 indexing.

## Span labels

| Label | Meaning | Example decision |
|---|---|---|
| `MS` | Contextually Malay material, including accepted Malay loans | `saya`, `belum`, Malay noun `fail`. |
| `EN` | Contextually English material | A clear English verb or a full English phrase. |
| `MIXED` | A single token with analyzed Malay and English morphemes | `di-check`, with separate component spans. |
| `NE` | Name/entity kept separate for this analysis | A person's name or organization. |
| `SHARED` | Conventional shared form whose language assignment is intentionally neutral under this policy | A shared lexical item where no distinction is supportable. |
| `AMBIG` | Competing readings cannot be resolved from available evidence | An isolated `air` without context/audio. |
| `PART` | Discourse particle assigned a separate function label | Regional final `lah`; not automatically Malay evidence. |
| `FILLER` | Hesitation or nonlexical conversational filler | A genuine hesitation `uh`. |
| `OTHER` | Identifiable lexical material in another language | Record the language separately if known. |
| `UNCLEAR` | Material that cannot reliably be transcribed or interpreted | An unintelligible audio span. |
| `NONLEX` | Punctuation, spaces, numerical notation and similar nonlexical material | A comma or written digit string. |

Dictionary membership is evidence, not an automatic label. A loan is labeled
according to its contemporary use in the utterance, not only its etymology.
For shared spellings, compare meaning, surrounding syntax and audio. Annotator
uncertainty (`AMBIG`) differs from a declared neutral shared category (`SHARED`).

`Kan` can be a particle or a suffix; `lah` can be a Malay bound particle or a
regional discourse particle. Choose the analysis for the actual construction.
An `okay` used as the adjective in a coherent English phrase is not automatically
the same as an isolated acknowledgment. Do not use a context-free stoplist.

## Worked annotation

For authored `Saya belum submit borang itu.`, Malay material surrounds an English
verb: `[MS Saya belum] [EN submit] [MS borang itu]`. There are two direct lexical
language transitions. Spaces and punctuation do not count as lexical items.

For authored `Komputer itu rosak.`, the Malay loan `komputer` does not supply
English evidence. For authored `I agree lah.`, the final particle is recorded,
but this package's conservative lexical subset does not count it as a Malay
lexical span. Both decisions need a named policy; neither is a universal
definition of code-switching.

Exact offset examples are in
[annotation_examples.jsonl](../examples/annotation_examples.jsonl). They are
authored fixtures for explaining the contract, not automatic classifier outputs.

## Classification and evidence stages

Keep separate fields for:

- **Text category:** `lexical_ms_en`, `ms_only`, `en_only`, `particle_only_mix`,
  `entity_or_loan_only_mix`, `mixed_morpheme_only`, `ambiguous`, `other_language`,
  or `unusable`. Use a documented adjudication when more than one description
  applies; preserve secondary flags instead of discarding information.
- **Switch form:** word/phrase insertion, clause alternation, quoted material,
  particle-only, intra-word morphology, or multiple forms.
- **Evidence:** `text_candidate`, `text_adjudicated`, or `audio_confirmed`.
  Record the actual reviewer, date and rationale for adjudication. Do not set
  `audio_confirmed` unless the relevant waveform was inspected.

The **conservative lexical subset** requires at least one unambiguous Malay
lexical word and at least one unambiguous English lexical word in the same clip,
with sufficient reference/audio correspondence after review. A clear single-word
English insertion can qualify. Entities, digits, fillers, neutral shared forms and
discourse particles alone cannot provide the missing language. A lone mixed-affix
word is reported separately as `mixed_morpheme_only`, not silently discarded from
all broader analyses. A Malay affix on an English stem is still linguistically
interesting even when this particular subset definition is not met.

Here “lexical word” includes meaningful function words such as pronouns and
modals; it does not mean nouns/content words only. Particle and filler exclusions
are the explicitly declared exceptions above.

This conservative rule favors specificity and may undercount legitimate borrowed,
particle or very short switches. Report that tradeoff and retain a broader
annotated set. Do not claim an excluded clip contains no bilingual behavior.

## Counting switches

Count direct transitions between adjacent lexical tokens labeled `MS` and `EN`,
ignoring punctuation/whitespace. An intervening `AMBIG`, `SHARED`, `NE`, `PART`,
`FILLER`, `OTHER` or `UNCLEAR` interrupts that direct count. Record such intervals
as unresolved/non-direct rather than bridging them and inventing a boundary.
Count analyzed internal morpheme switches separately from word transitions.

Language labels on an entire clip are not enough to locate switch errors. For a
new benchmark, retain spans and, if available, word alignments. A per-language WER
requires a declared alignment/insertion-assignment method; simply counting errors
in words found in a dictionary is not valid. Report whole-clip WER/CER alongside
any switch-sensitive measure, defining tokenization and ambiguous-span handling.

## If preparing new clips from SRTs

1. Preserve original references and recording identities. Clean annotation markup
   and technical noise into a derived reference **before language selection**.
   Keep genuine spoken words, loans, reductions and particles. Log each cleanup.
2. Use the SRT start/end times as candidate reference intervals. Timestamps show
   where an annotation was placed; they are not proof of speech activity, complete
   transcription or good alignment. Inspect outliers and language-bearing spans.
3. Annotate contextual Malay/English evidence in each cleaned candidate. Review
   both languages against the corresponding audio when certifying the subset.
   Do not reuse a Tamil-script plus Latin-script regex.
4. Apply documented duration and quality criteria to those intervals. Choose limits
   for the experimental question/model interface, not because 1–30 seconds is
   inherently the correct Malay–English unit. Give every exclusion a reason.
5. Cut the retained intervals with declared padding, clipped to recording bounds.
   Check for truncated words and extra speech in the padding. If boundaries or
   references are adjusted, retain the originals and the adjustment record.
6. Validate the exported waveform and its reference together. Freeze the selected
   IDs, rules and hashes before comparing models.

Short clips provide controlled reference-aligned recognition units and simplify
error inspection. They also remove preceding context and may exclude switches
across sentence/clip boundaries. Report the task as short-form ASR. For claims
about conversation-level switching, evaluate a separate contextual/long-form task.
Do not concatenate arbitrary SRT entries and assume the gaps contain no speech.

Report original recording duration, summed annotation duration, retained interval
duration and padded exported duration separately. Overlapping padded clips can
repeat audio; summed clip duration is not necessarily unique acoustic coverage.

## Separation from training

Keep held-out recordings, speakers where known, and duplicate/near-duplicate
segments apart from training. Do not use benchmark utterances as generator
few-shot examples. Record unavoidable test exposure during rule development.
Rules researched from general language sources can be frozen before a fresh test;
reviewing an existing test while choosing rules should be disclosed as test-informed.
Corpus names and reported aggregate WER do not prove the presence of both languages
in every evaluated clip.
