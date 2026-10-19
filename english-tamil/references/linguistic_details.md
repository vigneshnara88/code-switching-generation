# Detailed EN-TA linguistic reference

Consult relevant sections when the compact rules or a flagged row need clarification. Examples are schematic possibilities, not source facts or mandatory templates. First select the task mode in [the input guide](english_input_examples.md).

For spoken versus literary Tamil, contextual reductions and register exceptions,
read [spoken_tamil.md](spoken_tamil.md). Tamil Unicode can represent either
register; the script requirement does not require literary wording.

## 1. Mixed-script annotation convention

For the mixed-script convention used here (not all Tamil orthography), use:

- English words spoken as English: Latin script.
- Tamil speech: Tamil Unicode.
- Tamil case/aspect/negation/quotative material around English roots: preserve in Tamil, attached or adjacent according to the output format.
- Singapore particles/backchannels: use sparingly and only when natural.

Preferred plain-text examples:

```text
office-ல இருந்தேன்
meeting-க்கு late ஆயிடுச்சு
file-ஐ upload பண்ணு
ready-ஆ இல்ல
Actually நான் try பண்ணேன், ஆனா work ஆகல.
அவர் "call me later"-னு சொன்னார்.
```

Preferred tagged examples:

```text
<en>school</en><ta>-க்கு</ta>
<en>income</en><ta>-ஓட</ta>
<en>effective</en><ta>-ஆ</ta>
<en>declare</en> <ta>பண்ணணும்</ta><cse>[lah]</cse>
```

## 2. English material, names and entities

Keep intended English material in Latin under this annotation convention.
Names and acronyms may be kept in their supplied form but do not by themselves
prove that a language switch occurred. Examples of useful lexical material:

- Names and entities: `Kaushi`, `Nithin`, `Bayshore International`, `Singapore`.
- Acronyms and institutions: `NUS`, `NTU`, `ITE`, `ICA`, `NS`, `MRT`.
- School/work/tech terms: `school`, `project`, `assignment`, `meeting`, `interview`, `office`, `phone`, `online`, `WhatsApp`, `Instagram`.
- Food/media/logistics terms when they are English anchors: `ticket`, `movie`, `scene`, `concert`, `Grab`, `carpark`, `bazaar`, `market`, `mall`.
- English predicates used with Tamil grammar: `try`, `upload`, `confirm`, `share`, `apply`, `focus`, `continue`, `pack`, `submit`, `call`.

Do not translate these away into Tamil if they are meant to be code-switch anchors.

## 3. What Counts As Tamil

For Tamil-script output, write Tamil words and grammar in Tamil Unicode:

```text
என்ன, எப்படி, இப்போ, அப்போ, வந்து, ஆனா, இல்ல, இருக்கு, பண்ணு,
பண்ணல, பண்ணணும், சொன்னாங்க, தெரியல, கிடைக்கல, முடியல
```

Romanized Tamil such as `enna`, `panna`, `irukku`, `veetla`, `sonna`, `vandhu`, or `namma` may appear in source artifacts and ASR hypotheses, but it should not be introduced into new Tamil-script labels unless the task is explicitly Tanglish/romanized.

## 4. Matrix Language Modes

Natural Singapore EN-TA code-switching is not random alternation. Use either mode as supported by the source and brief; a corpus may include both:

- Tamil-matrix: Tamil supplies clause frame, case, tense, aspect, negation, quotative, and discourse flow; English supplies content words.
- English-matrix: English supplies the main clause; Tamil contributes kinship terms, stance, particles, short Tamil clauses, or emotional emphasis.

Examples:

```text
Tamil-matrix: அந்த project-ஐ நாளைக்கு submit பண்ணணும்.
English-matrix: I sent the file, ஆனா reply இன்னும் வரல.
```

## 5. Do Not Force 50/50 Balance

Choose the balance from the declared training design and what the selected
sources support; no held-out benchmark percentage is a universal target.
A varied source pool may support:

- English-heavy rows with Tamil stance/family/discourse spans.
- Tamil-heavy rows with a small number of English lexical items.
- Balanced rows.
- Some Tamil-only or English-only rows only for contrast, not for the strict mixed synthetic set unless the experiment calls for negatives.

Avoid alternating every word between languages.

For this project's Astra-style brief, the [saved reference](astra_style.md)
provides a soft corpus-level orientation near 50/50, slightly toward English
(historical mean 51.92%). It does not require English main clauses or balanced
counts in every row. Read the [actual constructions](astra_style_examples.md)
and choose coherent phrases; do not translate an arbitrary sentence ending to
move the ratio. Naturalness and source fidelity take precedence over counts.

## 6. English Nouns With Tamil Grammar

Common suffix/postposition possibilities (choose by meaning and clause structure):

```text
-ஐ / -a / -e        direct object: file-ஐ, assignment-ஐ
-க்கு / -ku/-kku   dative/to/for: meeting-க்கு, school-க்கு
-ல / -la/-le       locative/in/on/at: office-ல, class-ல
-லிருந்து          from/source: app-லிருந்து, house-லிருந்து
-ஓட / -oda         with/of/possessive: friend-ஓட, income-ஓட
-கிட்ட             with/to person: boss-கிட்ட, teacher-கிட்ட
-ஆல / -ஆலே         by/with/because of: stress-ஆல, phone-ஆல
-ம் / -um          also/even: project-ம் assignment-ம்
-வே                emphasis: same-வே, first-வே
-னு / -nu          quotative/as-called: okay-னு, cancel-னு
```

Generation rule:

- Preserve the English root.
- Preserve the Tamil suffix or postposition.
- In tagged output, split the stem and Tamil suffix across tags.
- In plain output, hyphenation is preferred for clarity: `school-க்கு`, not `schoolக்கு`.

Case marking is context-sensitive. An object is not required to carry an
explicit accusative suffix in every utterance. When a suffix is needed, use
the appropriate allomorph and preserve its meaning; do not append this inventory
mechanically to every noun. The romanized aliases above help recognize forms,
not spell new Tamil-script labels. A possessive, comitative, location and recipient
are different relations even when some forms have several contextual uses.

## 7. English Predicate Plus Tamil Light Verb

The `பண்ணு` family is a major pattern, but it must not be overused.

Natural:

```text
try பண்ணினேன்
upload பண்ணு
confirm பண்ணுங்க
cancel பண்ணிட்டாங்க
apply பண்ணல
focus பண்ணணும்
share பண்ணிட்டு இருந்தேன்
continue பண்ணுவோம்
```

Rules:

- Use English root + `பண்ணு` for actions that naturally borrow the English verb.
- Keep tense, aspect, person, modality, and negation on the Tamil side.
- Do not force `பண்ணு` when a normal Tamil verb is more natural. For example, `நான் சாப்பிட்டேன்` is often better than `eat பண்ணேன்`.

## 8. English Adjective/Adverb Plus Tamil `ஆ`

English adjectives and adverbs often integrate through Tamil `ஆ`, `ஆன`, or `ஆக`.

Natural:

```text
correct-ஆ சொன்னார்
ready-ஆ இருக்கு
safe-ஆ போங்க
slow-ஆ பேசுறாங்க
strict-ஆ இருக்காங்க
proper-ஆக பண்ணணும்
```

Retain the integration required by the chosen construction. Do not attach `ஆ`
indiscriminately to every English adjective, especially inside a complete English
clause; different clause frames can express the same state naturally.

## 9. Result-State English Roots With `ஆகு`

Use `ஆகு`/`ஆயிடு` style forms for result states or intransitive changes:

```text
change ஆயிடுச்சு
open ஆகல
miss ஆகிடும்
crash ஆயிடுச்சு
shock ஆயிட்டாங்க
work ஆகல
```

Rule of thumb:

- `பண்ணு` for doing/causing.
- `ஆகு` family for becoming/happening/result state.

## 10. Tamil Negation And Modality Around English Anchors

These are meaning-critical and must be preserved:

```text
ready இல்ல
confirm பண்ணல
submit பண்ண முடியல
work ஆகல
plan இல்ல
meeting முடியல
ticket கிடைக்கல
```

Common negation/ability tokens:

```text
இல்ல, இல்லை, பண்ணல, ஆகல, முடியல, வேணாம், தெரியல, கிடைக்கல, வரல
```

Never normalize `ready இல்ல` into `not ready` for a mixed-script transcript if the Tamil was spoken.

## 11. Quotative And Reported Speech

Tamil frequently wraps English words or clauses with `னு`.

Natural:

```text
okay-னு சொன்னார்
meeting cancel-னு சொன்னாங்க
அவங்க "call me later"-னு message பண்ணாங்க
chips-னு சொல்லுவாங்க
```

ASR risk:

- English ASR may catch the quote and miss `னு சொன்னாங்க`.
- Tamil ASR may replace the English quote with a Tamil meaning.
- The correct mixed label keeps both parts if they were spoken.

## 12. Tamil Discourse Bridges

Useful spoken Tamil bridge/filler words:

```text
வந்து, அப்போ, இப்போ, அப்படி, அதான், சரி, ஆனா, இல்ல, என்ன, ஏன்னா
```

Rules:

- Preserve when audible.
- Do not sprinkle them mechanically.
- `வந்து` often acts as a discourse bridge, not literally "came".

## 13. Singapore Particles And Backchannels

Use only when natural for a Singapore-style conversational clip.

The bundled tagged format accepts this closed CSE inventory. This is an
annotation limit, not the complete inventory of Singapore speech:

```text
[lah], [leh], [lor], [ah], [eh], [oh], [sia], [mah], [orh], [nah]
[meh], [hor]
!wah!, !aiyo!, !walao!, !alamak!, !aiya!, !huh!
(uh), (um), (err), (mm), (hm), (hmm)
```

Ordinary English discourse words such as `okay`, `ya`, `sorry`, and `please` can appear in English text. They are not CSE tags.

Rules:

- Preserve audible particles in manual transcripts.
- For synthetic text, use them sparingly.
- Choose particles by speech act and discourse; no particle is compulsory.
- Do not hallucinate particles merely to make an utterance "Singaporean".
- Extend the gate before generating new CSE tokens outside the inventory above.

Ambiguity:

- `la` can be Tamil locative, romanized Tamil suffix, or Singlish particle.
- `ah` can be Singlish question/stance particle or Tamil `ஆ`.
- `ma`, `pa`, `da`, `di` can be address terms, not English.

## 14. Kinship, Address, And Local Social Context

Conversational English–Tamil can mix English names with Tamil relationship/address terms.

Examples:

```text
james மாமா
gowri அக்கா
ganesh அண்ணே
அம்மா, அப்பா, பாட்டி
டா, டி
மச்சான் (only if this address term and register fit the source/context)
```

Rules:

- Preserve Tamil kinship/address in Tamil script when that is the Tamil word.
- Preserve names in Latin if spoken as names.
- This is a high-value Singapore family/friend register.

## 15. Domain Lexicon For Singapore EN-TA

Examples of source-supported English vocabulary across domains follow. They
are options, not required topics or evidence that a word was spoken in English.
Other domains are equally valid; do not insert a local institution absent from
the source to make the text look Singaporean:

```text
school, class, lesson, teacher, homework, assignment, exam, result
poly, polytechnic, JC, NUS, NTU, ITE
office, work, boss, meeting, leave, shift, project, report, email
phone, app, message, video, online, post, upload, download, password
bus, MRT, taxi, Grab, card, ticket, station, stop, carpark
doctor, clinic, appointment, medicine, report, scan
police, case, statement, court, lawyer, officer, evidence, ICA, NS
money, bank, transfer, account, bill, receipt, budget
lunch, dinner, coffee, tea, shop, market, mall, order, delivery, bazaar
movie, scene, song, actor, theatre, concert, YouTube, Instagram, Netflix
Singapore, HDB, CPF, NRIC, road names, school names
```

## 16. Spoken Structure

Source-supported spontaneous-speech patterns include:

- Repetitions: `I I`, `ya ya`, `okay okay`.
- Repairs: partial starts, abandoned phrases.
- Fillers: `(uh)`, `(um)`, `(err)`, `(mm)`.
- Non-speech annotations only when explicitly defined by the transcription schema;
  they are not automatically spoken words or material to send to TTS.

For synthetic rows:

- Retain meaningful repairs in rewriting. Add disfluency only if the authoring
  brief allows it and it does not change meaning, certainty or the endpoint.
- Do not make labels unreadable.
- Do not create source artifacts like `<tamil>`, `tamil`, roman glosses, or unexplained noise tokens in new generated data.

## 17. Tamil Sound And ASR Confusion Rules

ASR often misses or confuses:

- Short Tamil suffixes after English roots: `-ஐ`, `-ஆ`, `-ல`, `-ம்`, `-னு`.
- Tamil reduced forms: `இல்ல`, `தெரியல`, `முடியல`, `பண்ணல`.
- English roots with Tamil/Singapore pronunciation: `bus-u`, `class-u`, `file-u`, `school-u`.
- Names and local terms that look like English to one recognizer and Tamil to another.
- Background music, overlap, phone filtering, far-field room audio, and emotional speech.

Review/gating should flag uncertainty instead of smoothing it into fluent text.

## 18. Anti-Patterns

Apply these checks within the selected task mode. Preserving audible languages
is required for transcription; bilingual rewriting necessarily changes some
language choices. Preserve explicitly locked anchors in either case. The
examples below are context-sensitive review prompts, not a word blacklist.

Reject or rewrite examples that show:

- Pure English or pure Tamil when the row is meant to be strict mixed EN-TA.
- Romanized Tamil in a new Tamil-script gold label.
- English translated into Tamil script when it should be an English anchor.
- Tamil translated into English when it should stay Tamil.
- Every sentence forced to exactly 50/50 English/Tamil.
- An arbitrary insertion that changes no coherent linguistic constituent or
  adds unrelated content merely to trigger a mixed-script detector. A legitimate
  one-word insertion, borrowing or short mixed fragment is not automatically bad.
- Random `[lah]`/`[ah]` overuse.
- Overuse of `பண்ணு` where a normal Tamil verb is more natural.
- New facts, changed meaning, or invented local context.
- Non-English/non-Tamil script leakage.
- Literal source artifacts: `<tamil>`, `</tamil>`, `tamil` markers, roman glosses after Tamil, broken tags, or duplicated subtitle text.
- Glued Latin+Tamil without an explicit switch boundary, such as `materialஎன்று`, `penaltyஆகும்`, or `ratioன்னா`; rewrite with a hyphen or space only when the audio/text truly contains that mixed form.
- Formal translation scaffolds such as bulk `இதில் சொல்லப்படுவது`, `நீங்க கேட்பது`, `என்பது`, `என்பவை`, or `என்று அர்த்தம்` rows when they make the utterance sound like a dictionary gloss rather than speech.

## 19. Strict Synthetic Gate

A generated row can enter the high-confidence synthetic pool only if:

- It preserves the original meaning, names, numbers, and facts.
- It contains both Tamil Unicode and Latin English.
- English is Latin and Tamil is Tamil Unicode.
- Tamil suffixes/grammar around English roots are retained.
- No unknown language tags or unrelated scripts appear.
- It sounds like spontaneous Singapore EN-TA speech, not a word-by-word translation.
- It is not an unintended duplicate output; repeated grammatical patterns are
  permissible, while corpus over-concentration calls for a distribution review.
- It passes the declared linguistic review, with contextual resolution of flags.
  Name the kind of review accurately; a model pass is not human certification.

## 20. Contextual Orthography and Loanword Review

For this rulebook's mixed-script convention, keep intended English words in Latin
and genuine Tamil grammar/words in Tamil Unicode. The loanword map proposes
possible English anchors; it is not an instruction to replace every matching
Tamil-script substring.

- Resolve ambiguous loanword readings from the complete source and sentence.
- Preserve Tamil case and grammar when writing an English root: `school-க்கு`,
  `business-ல`, `family-ஓட`, `life-ஐ`.
- Do not split ambiguous short stems mechanically. `ஒன்` may mean `one`, but
  Tamil `ஒன்னு` must not become `one-னு` merely because of that spelling overlap.
- Preserve real Tamil words, fillers and source-supported names. A detector's
  foreign-looking flag does not establish that a word should be translated.
- Record uncertain mappings for review; do not turn a source correction guess
  into an accepted new fact. Benchmark reference cleaning is a separate task.

## 21. Source-Supported Discourse Variety

The supplied source and explicit context establish the facts. Select the task
mode before changing language choices. A monolingual source can support mixed
rewriting, but neither a summary nor a scenario cue is automatically a verbatim
transcript. Data-provider selection belongs in the calling workflow.

Select inputs covering the desired speech shapes before generation. Where
supported by those sources and the shared brief, include short fragments,
longer turns, English clauses with Tamil stance or family material, Tamil
reported speech, and multi-clause event sequences. Local institutions such as
HDB or CPF belong only where the source supplies them. Do not invent an
appointment or family member to make a row sound local.

Repairs/restarts such as `I mean` or `(um)` must preserve meaning and a clear
endpoint. Do not pad a complete short utterance or prescribe audio duration
from word count alone. Tamil-only/English-only contrast rows require an explicit
study design; they do not pass the default strict-mixed corpus contract.
Keep relevant family/domain metadata and inspect distributions by family before
TTS. Choose family targets explicitly for the source pool; none are universal.

## 22. Semantic plausibility and agreement

Whole-row review must check local plausibility as well as script correctness.
Mechanical object/action flags identify questions for that review; they cannot
certify the sentence meaning.

Named kinship (context governs):

Preserve the source's named person and stated relationship. When the source
means someone's sister, express the possessive relationship explicitly, e.g.
`Jason-ஓட அக்கா`. A bare `Jason அக்கா` can instead sound like direct address.
A name alone does not establish gender, kinship or the intended referent.
Review apparently unusual combinations against the source; do not delete a
name, invent a relationship, or substitute a generic kin term to satisfy a
name list. The compact skill's source-fidelity contract is authoritative.


Document/action plausibility:

```text
Good: consent form-ஐ sign பண்ணு
Good: claim form-ஐ submit பண்ணு
Good: meeting link-ஐ share பண்ணு
Good: receipt-ஐ keep பண்ணு
Needs context: consent form-ஐ book பண்ணு
Needs context: bank statement-ஐ cancel பண்ணு
Needs context: meeting link-ஐ print பண்ணு (printing a URL can be intended)
```

Rules:

- English action roots must make sense with the English document/entity.
- `keep` is acceptable for forms, statements, photos, reports, links, and receipts in Singapore English/Tamil-English instructions.
- If a helper proposes action/object pairs, condition them on the supplied
  meaning. An allowlist is a review aid, not authority to change the source action.

Long Tamil agreement:

```text
Good: நான் கொஞ்சம் tired-ஆ இருந்தேன்
Bad: நான் கொஞ்சம் tired-ஆ இருந்தது
Good: பிறகு நான் Yishun-ல இருந்து Gowri-க்கு update send பண்ணினேன்
Bad: பிறகு அது Yishun-ல இருந்து Gowri-க்கு update send பண்ணினேன்
```

Rules:

- If the subject is `நான்`, use first-person agreement such as `இருந்தேன்` or `பண்ணினேன்`.
- If the subject is the situation/document, `இருந்தது` or `மாறிடுச்சு` can be correct.

## 23. Particle meaning and discourse scope

Particles can change stance, politeness or the force of a question while leaving
the event description intact. Judge the whole utterance and, for audio, its
intonation. The short glosses below are prompts for review, not exhaustive meanings.

Rules:

- Particle/no-particle pairs can be useful when explicitly requested, but may
  differ pragmatically. Do not claim automatic semantic or acoustic equivalence.
- Consider `[lah]` for contextually suitable assertion, reassurance or a
  softened directive; interpretation depends on contour and discourse.
- Keep `[leh]` for contradiction or stance.
- Keep `[ah]` for yes/no question or topic continuation.
- Keep `[lor]` for resignation.
- Keep `[hor]` for listener check.
- Keep `[eh]` for attention/surprise.
- Keep `[meh]` mostly for skeptical yes/no-style questions, not plain declaratives.
- Keep no-particle rows common enough that the model does not learn to insert particles everywhere.

## 24. ASR Label Versus TTS Speech Text

Keep separate fields when using the bundled format:

- `cs_text_clean`: language-tagged text for inspection.
- `transcript`: spoken-content text with language tags removed.
- `tts_text`: speech input with annotation delimiters removed.

These field names and transformations are a tool contract, not grammar rules.

TTS text should strip transcript markup while preserving spoken particles as words:

```text
Tagged: <en>This form ready</en><ta>-ஆ இருக்கு</ta> <cse>[lah]</cse>
TTS text: This form ready-ஆ இருக்கு lah
```

Do not use TTS reference transcripts as switching examples unless they were separately selected and reviewed as code-switch data.


## Evidence and annotation scope

See [the research and scope note](sources.md). Tag shapes, Tamil/Latin
spelling conventions, and the closed particle inventory
are annotation choices. Numerical corpus targets belong in the caller's brief. Particle glosses are contextual heuristics, not exhaustive
meanings; inspect the utterance's speech act and later the synthesized contour.

## 25. Multiple switches and long turns

A longer turn may switch repeatedly. Preserve each clause's speaker, subject,
object, time and logical connection; do not rate it by switch count alone.
An English clause should retain a complete predicate, while Tamil grammatical
support belongs to its intended predicate or noun phrase. Check the return from
English to Tamil as carefully as the first switch.

Compare each proposition to the source, then read the entire result to verify
that pronouns still refer to the same people, quotations keep their boundaries
and conjunctions preserve cause, contrast and conditions. Do not concatenate
independently plausible fragments if the combined meaning changes. Long turns
need more contextual review; additional switches are not inherently better.

## 26. Meaning-sensitive small words

Before acceptance, inspect negation, quantifiers, deadlines and connectors.
“Not all,” “none,” “only,” “also,” “at least,” “before,” “by,” “until,” “if” and
“because” can determine the meaning more than a long content word does.
A fluent output can still be wrong if it drops one of these distinctions.
See [meaning and edge cases](meaning_and_edge_cases.md) for concrete contrasts.

## 27. Orthography and ambiguity

Use [the annotation contract](annotation_contract.md) for script boundaries,
loanword candidates, Unicode and tag/TTS distinctions. A checker may reject an
unsupported name, symbol or annotation even when the utterance is linguistically
valid. Report that as a format/policy conflict; do not silently corrupt the name
or remove source meaning to make the check pass.

## 28. Review and repair

Use [the review checklist](../review_checklist.md). Preserve the source while
repairing the actual defect. Recheck the whole clause after any suffix, auxiliary,
particle or quotation edit. Inspect repaired rows again for meaning, register and
annotation, and check for duplicates across the complete candidate pool.
