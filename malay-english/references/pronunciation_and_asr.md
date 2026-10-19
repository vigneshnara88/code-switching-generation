# Malay sounds, spelling and speech evaluation

This is a guide to relevant distinctions, not a complete phonetic dictionary.
IPA in slashes describes a broad sound category; brackets describe a possible
realization. A voice's region, register and actual recording take precedence over
a generic expected accent. No audio was listened to or synthesized to validate
this package's authored examples.

## Quick sound reference

The Standard Malay account in [S28](sources.md#s28) describes six vowel categories,
/i e a o u ə/. Actual realizations depend on the variety; the Singapore sources
S26–S27 explain why a spelling-to-sound lookup cannot settle the target voice.
The table combines the broad phonetic account with DBP spelling conventions
([S09](sources.md#s09)); it is a reading aid, not a complete pronunciation lexicon.

| Written element in Malay material | Broad distinction to check |
|---|---|
| `a`, `i`, `u`, `o` | Broad /a i u o/ categories; inspect final-syllable and register variation rather than copying English letter names. |
| `e` | Either /ə/ or /e/; the word and meaning determine the reading. |
| `ng`, `ny` | /ŋ/ and /ɲ/ within the relevant word, rather than two English consonant names. |
| `c`, `j` | Broad /tʃ/ and /dʒ/ in ordinary Malay spelling. |
| `sy`, `kh` | Common loan-related /ʃ/ and /x/ correspondences; actual loan adaptation varies. |
| Final `k`, other final stops | Check unreleased or glottal realizations and whether the audio boundary has cut the word. |
| `r` and final `a` | Check the chosen variety and register; do not apply one global deletion or vowel replacement. |

Apply this table to Malay material. An English insertion keeps its own lexical
pronunciation possibilities, including a speaker's local English accent.

## P01 — Choose the pronunciation profile separately from spelling

Singapore research distinguishes Sebutan Baku and Johor–Riau patterns and
documents hybrid realizations in both scripted and spontaneous speech
([S26](sources.md#s26), [S27](sources.md#s27)). Do not assume that using standard
spelling selects one accent. Record the voice and intended register when using TTS.
Do not label a natural hybrid pronunciation erroneous solely because it fails a
single idealized pronunciation model.

## P02 — Written e represents more than one vowel

Distinguish e pepet /ə/ and e taling /e/. Ordinary Rumi spelling normally does not
mark the contrast. Use a verified lexical pronunciation where it matters; a
global “read every e as English e” rule fails. The corrected DBP explanation in
[S23](sources.md#s23) is consistent with the phonetic literature. The search results
also contained an older reversed-symbol answer; that answer is not adopted here.

Authored diagnostic prompts can use `perang` in a war context versus a brown-colour
context, but a native speaker should validate the intended word and realization.
Do not insert diacritics into an existing benchmark reference just to guide a TTS
engine. Keep any phoneme hints in a separate field.

## P03 — Final a and r have variety-dependent realizations

Johor–Riau and Baku differ in relevant final-vowel and rhotic patterns; the Singapore
studies discuss these distinctions. Ordinary `saya`, for example, need not be
respelt `saye` merely because a speaker realizes a final schwa. Avoid global
rules that replace every final `a` or delete every written `r`. Loans, suffixes,
speakers and register can affect the outcome. See S26–S27.

## P04 — Final stops may be weakly released or glottalized

Malay varieties can differ in realization of final stops, including final /k/.
An unreleased or glottal realization does not itself justify deleting the written
consonant. The Brunei Standard Malay illustration documents its own speaker and
contrasts with Peninsular realizations ([S28](sources.md#s28)); it must not be
used as a universal Singapore voice prescription. In ASR review, distinguish
expected variation from a clipped word ending by listening around the boundary.

## P05 — Digraphs are not English letter-by-letter sequences

In Malay words, `ng` and `ny` commonly correspond to /ŋ/ and /ɲ/; `sy` and `kh`
occur in loan-related spellings. `C` and `j` commonly represent /tʃ/ and /dʒ/,
respectively. The spelling guide documents consonant combinations (S09), and
S28 supplies phonetic context. Check the *whole word*: a character sequence
crossing a morpheme boundary need not behave like a single digraph.

## P06 — Affixes can alter the sound at the stem boundary

Nasal-prefix alternation, as in `tulis → menulis` or `sapu → menyapu`, changes the
surface form. Model both the correct lexical word and its sound. Do not assume
the spelling of an English stem determines how every speaker integrates it.
For a mixed affixed token, store the stem, affix and language interpretation
without rewriting the acoustic evidence. See S17 and R21–R24.

## P07 — Vowel sequences and connected speech need listening

Vowel sequences can have variable timing, and rapid speech can involve glide-like
realizations. S28 discusses these for its recorded variety. Do not force English
diphthong rules onto Malay or prescribe one segmentation for all voices. An ASR
word boundary is an annotation decision, not necessarily an audible pause.

## P08 — Stress and intonation are not a one-rule conversion

Do not impose “stress every penultimate syllable” or an English stress template
on all Malay words. S28 questions inherent lexical stress for its Brunei variety;
that is a scoped analysis, not proof that all Malay varieties share one prosodic
system. For particles and questions, assess the whole phrase's intonation rather
than looking only at punctuation.

## P09 — A local pronunciation does not automatically make a word Malay

An English phrase can be spoken with Singaporean or Malaysian English phonetics.
A conventional Malay loan can retain an English-like pronunciation. Classify using
construction, lexical choice, context and audio together, not accent imitation.
`Air` illustrates why a shared spelling can need different pronunciation and
meaning decisions ([S06](sources.md#s06)). Avoid invented spellings such as an
arbitrary vowel after every English consonant cluster.

## P10 — Contractions and noise are different phenomena

`Dah`, `nak` and `tak` can be lexical conversational forms. A lost syllable at a
bad cut or under background noise is not the same phenomenon. Keep a surface
transcript and an optional formalized layer; do not train on an expanded word
as if all its sounds were present. Mark unclear audio instead of guessing a
fluent word from the surrounding grammar.

## P11 — Audit the synthesized or extracted waveform

**Project procedure:** listen across both sides of a switch and check that TTS
did not translate an English insertion, select the wrong shared-word reading,
omit an affix, or add a pause inside one word. For extracted recordings, check
initial and final consonants, overlap and nearby speech introduced by padding.
Retain source offset, end time, padding and final duration. A readable reference
and passing language-label check do not replace this acoustic check.

For a new evaluation, include clear switches, difficult shared spellings, short
functional words, affixed stems, regional variation and monolingual controls.
Report actual coverage; these categories are suggestions, not fixed corpus quotas.
