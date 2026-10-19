# Observations from the Malay benchmarks already tested

These are limited diagnostic observations from the existing saved references,
not a new language annotation or audio audit of the complete test collection.
They informed cautions in this guide and are deliberately outside the authored
example library.

## Exact saved datasets

| Saved dataset | Frozen repository revision | Selected clips | Summed clip hours |
|---|---|---:|---:|
| FLEURS Malay derivative | `07a721caafabac39fe70037497492166ecfa49eb` | 749 | 2.264000 |
| Mesolitica Malay derivative | `6a68d38bfb85ba552d751505867b71427842ab05` | 993 | 2.751526 |

The recorded repositories are [knoveleng/fleurs-malay](https://huggingface.co/datasets/knoveleng/fleurs-malay)
and [knoveleng/mesolitica-malay](https://huggingface.co/datasets/knoveleng/mesolitica-malay).
Counts, durations and hashes were recomputed from local manifests and matched
their saved selection receipts. All eligible rows were retained in these two
experiments; the receipts do **not** document a per-clip lexical-switch gate.
Do not describe these selections as having used the new rulebook's proposed filter.

FLEURS provides a read-speech retention context. Calling the Mesolitica dataset
“Malay CS” in the experiment report does not establish that all 993 individual
clips satisfy a stricter lexical or audio-confirmed definition. The precise
number of such clips has **not** been established here.

## Small reference inspection

The first eight Mesolitica rows were read for diagnostic variety. That is an
illustrative prefix, not a random or representative sample. The following
excerpts are quoted exactly from the saved reference, including lowercase text;
no audio confirmation is claimed.

| ID | Very short reference excerpt | Observation |
|---|---|---|
| `mesolitica_ms_000000` | `public toilet ataupun tandas awam` | Clear English phrase followed by Malay; a strong text candidate for lexical mixing. |
| `mesolitica_ms_000000` | `tetapi i see where it comes from` | A larger English clause occurs after a Malay connector. |
| `mesolitica_ms_000001` | `steven spielberg` | A name does not itself provide substantive English evidence. The rest of this short reference has Malay and a hesitation; it should not automatically pass a lexical-switch gate. |

Additional observations, without reproducing more transcript text:

- `mesolitica_ms_000002` contains Han characters in the reference. Listening would
  be needed to determine whether they represent actual speech, a rendering choice
  or a reference error. Do not infer a third spoken language from the characters.
- `mesolitica_ms_000003` includes a repair and English material; grammar cleanup
  should not silently erase a genuine repair when the task is transcription.
- `mesolitica_ms_000006` contains a product name and short conversational items.
  Their roles need contextual review before classifying the clip.

A mechanical scan of **all** saved references found four Mesolitica rows and zero
FLEURS rows matching at least one character in the Han, Tamil or Arabic ranges
used by the audit. This is a character flag only, not a language count or reference
quality verdict. Malay/English detection cannot be reduced to that scan.

## Provenance and reproducibility

The original manifests were read from the experiment workspace:

```text
/home/azureuser/projects/HTX_Vig/data/validation/whisper_retention_20260909/datasets/
  fleurs_ms/manifest.jsonl
  mesolitica_ms/manifest.jsonl
```

The repository also retains frozen selection receipts/cards under
`publication/results/retention_20260910/selection/`. The standalone package records
the receipts' key values and source hashes in
[benchmark_audit.json](../evidence/benchmark_audit.json). It includes no full
benchmark transcript or waveform collection.

To repeat the mechanical checks with the original local data:

```bash
python3 scripts/audit_local_benchmarks.py \
  --datasets-root /path/to/whisper_retention_20260909/datasets \
  --output /tmp/malay_benchmark_audit.json
```

The script reports counts/hours/hashes, verifies saved receipts and records IDs
for the narrow character flag. It does not assign language labels, listen, or
estimate a code-switching percentage. The quoted examples above were checked as
exact substrings of their source references.

## Use in future experiments

These test references were inspected while developing the guide, so future systems
tuned with it should disclose that exposure. No held-out utterance was copied into
the authored example library, but separating files does not undo test-informed
development. Prefer a fresh unseen evaluation set for final claims about gains
from rules or examples. A complete language audit of the old set would be a
separate, explicitly recorded text-and-audio annotation exercise.

The frozen Mesolitica derivative card did not state a substantive license or
per-clip linguistic quality guarantee. This package includes only the short
diagnostic quotations above and metadata; it makes no new licensing claim about
the underlying corpus.
