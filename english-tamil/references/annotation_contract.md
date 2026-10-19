# Annotation conventions and checker boundaries

Grammar, linguistic judgment, corpus-selection policy and file format are
separate layers. A format failure need not mean the language is unnatural, and
a format pass does not establish semantic correctness.

## Mixed-script convention

The convention here writes intended English material in Latin and Tamil material
in Tamil Unicode. It is useful for inspecting English–Tamil text, but does not
assert that all Tamil writers must use this spelling policy. Names, acronyms,
borrowings and numbers require a declared annotation policy and contextual review.

Romanized Tamil can occur in source text. In a task requesting Tamil-script
output, resolve its reading before rendering it in Tamil; uncertain names or
homographs must not be blindly transliterated. Pure Tamil and already mixed
sources are valid inputs when the task permits them.

For an English stem with Tamil grammatical material, use a visible boundary:
`file-ஐ`, `school-க்கு`, `office-ல`, `ready-ஆ`. Select the suffix and its form by
context. A hyphen is a spelling convention, not evidence of an audible pause.
Word counts based on whitespace and switch counts based on scripts do not
necessarily correspond to linguistic words or audio boundaries.

## Tagged format used by the bundled checker

Use balanced, unnested `<en>`, `<ta>` and optional `<cse>` spans. Tag language
characters completely; punctuation and numerals follow the declared policy.
English text does not belong inside a Tamil span just because it is in a
Tamil-matrix clause. Split a stem and suffix into their own language spans:

```text
<ta>தயவுசெய்து</ta> <en>file</en><ta>-ஐ அனுப்புங்க.</ta>
<en>The report</en> <ta>இன்னும்</ta> <en>ready</en><ta>-ஆ இல்ல.</ta>
```

`<en>file</en><ta>-ஐ</ta>` does not change the Tamil suffix into an English token.
These tags are annotations, not text for the synthesizer to say aloud.
For a different tag inventory or orthography, adapt the caller and validator
explicitly; do not pretend a format rejected by the checker is supported.

## Particles and discourse markers

The bundled format recognizes these CSE forms:

```text
[lah] [leh] [lor] [ah] [eh] [oh] [sia] [mah] [orh] [nah] [meh] [hor]
!wah! !aiyo! !walao! !alamak! !aiya! !huh!
(uh) (um) (err) (mm) (hm) (hmm)
```

The closed list is a tooling convention, not a complete linguistic inventory.
Ordinary English `okay`, `ya`, `sorry` and `please` need not receive CSE tags.
Tamil interrogative/adverbial `ஆ`, Tamil locative `ல` and Singapore particles
must be distinguished by grammar and discourse, not sound-alike spelling alone.

Do not add a particle for the sole purpose of making a row “local.” Do not remove
an audible particle from a faithful transcript because a synthetic-data quota
would prefer fewer. See the grammar reference for contextual interpretation.

## Tagged text, transcript and TTS text

The bundled exports keep three views:

| Field | Purpose | Example |
|---|---|---|
| `cs_text_clean` | Language-tagged annotation | `<en>The report</en> <ta>இன்னும்</ta> <en>ready</en><ta>-ஆ இல்ல.</ta>` |
| `transcript` | Remove language tags; retain spoken-content spelling | `The report இன்னும் ready-ஆ இல்ல.` |
| `tts_text` | Remove annotation delimiters from spoken content | `The report இன்னும் ready-ஆ இல்ல.` |

For tagged `<cse>[lah]</cse>`, the transcript may retain `[lah]` while TTS gets
`lah`. Do not send review notes, source IDs or non-speech metadata to TTS.

The bundled text-view helper strips bracket/parenthesis delimiters and language
tags. It is not a general converter for stage directions, mathematical notation,
URLs, dates or pronunciation markup. A source containing such material needs a
declared spoken rendering and a checked transcript/TTS pair; otherwise it stays
unresolved. Check synthesized audio for pronunciations, omissions and added
speech separately from checking the text.

## Unicode, token boundaries and the loanword map

Preserve the original string and make any Unicode normalization explicit.
Tamil combining marks are part of their letters; avoid chopping strings at
arbitrary code-point positions. A zero-width or unusual-space character may be
an artifact, but inspect it before removal. Do not globally replace look-alike
characters or strip meaningful punctuation from identifiers.

The loanword map has candidate categories such as `high_confidence` and
`medium_confidence_review_first`. Those names are historical schema labels,
not measured probabilities. Even a listed candidate needs source context.
Match complete tokens or phrases and inspect adjacent morphology; do not
replace a short substring inside a larger Tamil word. Preserve the English stem,
Tamil grammar and factual meaning together. Record uncertain mappings and any
actual changes. A phrase candidate that contains extra grammatical material
must not be substituted where its full meaning is unsupported.

## What the current checker can and cannot establish

The bundled checker validates this narrow tag/script format, catches some
suffix/glue/loanword patterns and duplicates, and checks review records. It also
has implementation limits: many non-ASCII names and symbols fall outside its
accepted character range, and its final-question-mark check is only a heuristic.
It may flag a valid name or a mixed question followed by a spoken particle.
Treat these as format/policy conflicts needing an explicit change or supported
rendering, not permission to alter source facts.

Literal format errors can be repaired mechanically. Language identity, meaning,
register, optional case marking, particle force and whether a single insertion
is natural require contextual review. Short mixed utterances need no invented
minimum number of English anchors. A proper name in Latin alongside Tamil can
pass a script check without establishing genuine lexical switching.
