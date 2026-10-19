# Astra reference: natural phrasing and overall balance

Use this reference when the brief asks for the project's established Astra
style. Start with the 14 starter examples in the [400-pair library](astra_style_examples.md),
then consult 2-6 relevant pairs by context or query before drafting. Do not load
all 400 into every prompt. They come from the best saved Astra 2,000-row workflow; their source
IDs, complete outputs and [provenance](astra_style_provenance.json) are retained.
They are style context, not new facts to add or templates to apply everywhere.

## Balance across the corpus

The saved 2,000-row run averages **51.92% English** using `profile_text.py`:
count Latin words and Tamil Unicode spans per row, calculate the English
fraction, then average the rows. This measures text composition, not speaking
time or which language supplies the grammar.

For similar future runs, aim **roughly around 50/50 overall, slightly toward
English: about 50-55% mean English** is an orientation. This is a soft project
preference, not an exact band that every run or sentence must pass. Individual
rows may be Tamil-heavy, English-heavy or balanced. English content words can
sit naturally in Tamil grammar; a balanced corpus does not require mostly
English sentence frames. Judge balance over a varied collection, not one short
utterance or every small batch.

Meaning and natural phrasing take priority. If the aggregate drifts, inspect
whether the prompt or repeated constructions caused it. Revise awkward rows
on linguistic grounds; do not translate arbitrary words, append particles,
pad a sentence or edit an already natural row just to move the percentage.
Report the observed profile and the reason for any material drift. An exact
numerical gate belongs only to a separately declared study, not this reference.

## Compose the utterance, not a translated fragment

1. Understand the whole event or speech act: speaker, purpose, relationships,
   tense, condition, emphasis and what remains unspecified.
2. Choose a coherent bilingual construction for that meaning. It may use Tamil
   grammar with English nouns/verbs, a complete English clause plus a Tamil
   clause, a quotative, a correction or a short integrated phrase. No one frame
   is the default for every source.
3. Keep useful expressions together. English technical/domain expressions can
   stay intact while Tamil supplies case, aspect, negation or a predicate. A
   Tamil phrase should do real grammatical or conversational work.
4. Read the full result as one spoken turn. For a doubtful boundary, try a
   different full construction and choose the more coherent version that keeps
   the same meaning. Do not merely translate the last few English words because
   a second language is needed.
5. Compare the *construction* with relevant saved examples, then inspect the
   actual new source/output pair. Never borrow an example's people, events,
   particles or missing context to make a new source fluent.

For example, the saved row `0173` uses `Family-ஓட clinic trip-ஐ நாம confirm
பண்ணணும்னு Meena சொன்னாங்க.` The Tamil case and quotative form a coherent report
around English content. Row `0209` instead retains an English report and uses
Tamil for the contrasting inability clause. Both are useful patterns; neither
means every row should become a report or acquire a contrast.

An English opening followed by Tamil can be natural. It needs revision when
the boundary feels arbitrary, the continuation uses a mismatched register,
the phrase is a literal calque, or the same tail structure appears regardless
of source. Do not reject all end switches or impose obligatory suffixes and
light verbs as the opposite template. Context decides.

## Review naturalness separately from the ratio

For each pair, assess whether the clause frame, switch boundary, morphology,
register and information flow work together. Identify the phrase that sounds
translated or forced and explain why, rather than approving because both
scripts are present. A fluent monolingual back-translation or a passing token
ratio is not enough. Preserve semantic checks while comparing alternative
phrasing for difficult cases.

Across the batch, look for repeated English-prefix/Tamil-tail patterns, stock
connectors, indiscriminate suffixes, unnecessary formal vocabulary and copied
reference stories. Repetition of legitimate grammar is not itself an error;
judge whether it is natural in each source and overused across different ones.
The independent reviewer must apply these checks even if the author accepted
every row. Owner/speaker feedback can expose weaknesses that model review missed.

## Reference use and scope

The examples are unchanged historical model outputs, selected for varied
contexts and useful constructions. They are not a certified gold set, a random sample
or proof that every historical wording is ideal. Current source fidelity still
governs new rows. Do not copy old scenario elaborations or particles automatically.

Freeze the same reference folder for generator and reviewer. Record which
examples were actually consulted. The 400 library IDs do not overlap the current
20-row pilot. Exclude current target IDs from lookup where possible. For a full
same-2,000 run, keep every original ID and disclose library availability and
actual reference exposure; do not present exposed rows as unseen evaluation.
Never apply this generation preference to verbatim transcription: preserve the
languages actually spoken in audio.
