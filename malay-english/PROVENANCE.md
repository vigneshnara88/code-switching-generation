# Provenance and scope

Prepared on 21 September 2026 for the requested Malay–English lexical rulebook.
The package structure follows the existing Tamil rulebook's separation of an
agent entrypoint, language references, examples and review guidance. Malay
constructions were researched and written separately; Tamil case endings,
mixed-script filters and light-verb requirements were not transferred.

The authoring and review in this session were performed by the same AI assistant.
No independent agent review, native-speaker review, listener study or model
benchmark is claimed. Linguistic examples are proposed worked renderings, with
their status recorded in every JSONL row. Mechanical checks validate packaging
and declared structure, not conversational naturalness.

## Evidence types

- [Sources](references/sources.md) records 35 source entries, their scope and
  the depth of access. Some entries include multiple directly related DBP pages.
- General rules cite standard grammar or descriptive research where applicable.
  Dataset selection, label inventories and review procedures are project choices.
- All 64 worked source/candidate pairs, 12 annotation fixtures and lexical contexts
  were authored for this guide. None is presented as an observed utterance.
- [Benchmark observations](references/benchmark_observations.md) is a separate
  diagnostic note. Its tiny quotations are exact saved-reference excerpts and
  have not been checked against audio. Test exposure is disclosed there.
- The machine-readable lexicon distinguishes dictionary-backed entries from
  contextual authoring aids; an empty source-ID list is deliberate and does not
  imply independent lexical verification.

## What was checked

The existing 749-row FLEURS and 993-row Mesolitica manifests were parsed for
counts, durations and file hashes. Key values matched the frozen experiment
receipts. The first eight Mesolitica references were read as a limited diagnostic
sample; no exhaustive language classification was performed.

Primary PDFs used for research were downloaded to temporary research storage.
They are cited rather than redistributed. Website access failures and scoped
abstract-only evidence are disclosed in the source ledger. No current government
pronunciation policy is inferred from a historical paper.

## Future maintenance

For a new language claim, add a source and its actual supporting section, distinguish
standard from colloquial use, and state the population/register. Add an original
positive example and a meaningful contrast where useful. Record whether a local
speaker assessed it. Do not upgrade `authored_draft_not_native_validated` merely
because a validator passed.

Keep the surface transcript immutable when changing analysis. Track the new
analysis separately with a reason and the exact reviewed text. Freeze rules,
lexicon, examples and annotation choices for a model comparison; later edits
must not silently change an old run's reference or acceptance criteria.
