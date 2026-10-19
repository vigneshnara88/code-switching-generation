# Spoken Malay, community and pragmatic meaning

Use this alongside R03, R13–R20, R27 and R31–R38 in the
[linguistic rules](linguistic_rules.md). These are profiles for choosing examples,
not claims that all members of a community speak alike.

## Profiles

| Profile | Authoring guidance | Review boundary |
|---|---|---|
| `sg_conversational` — default | Conversational Malay–English for a Singapore setting; moderate reductions, relationship-appropriate pronouns, ordinary spelling. | Do not add Singapore locations or particles when the source gives no reason. |
| `my_conversational` | Malaysian Malay–English; retain supplied local vocabulary and the speaker's established register. | Do not assume Kuala Lumpur usage represents every Malaysian region. |
| `formal_mixed` | A formal explanation containing an English technical term, quotation or phrase where the brief permits switching. | A code-switched example is not automatically suitable for an official Malay document. |
| `source_faithful` | Preserve the recording's actual variety, register, grammar and language choices. | This profile overrides generation preferences; uncertainty needs a flag. |

Singapore conversational research identifies differences within its participant
sample, including age-related differences in switch functions ([S03](sources.md#s03)).
The NSC analysis concerns a particular conversational subset ([S02](sources.md#s02)).
Neither licenses stereotypes about a speaker inferred from age, ethnicity or name.

Malay and Indonesian are closely related but have distinct standardization and
usage histories ([S26](sources.md#s26)). Do not default to Jakarta colloquialisms
such as `gue`, `lo`, or `nggak` for this package. This is a scope preference, not
a ban on faithfully transcribing Indonesian or cross-border speech. Add a declared
regional profile when the task needs Brunei, Sabah, Sarawak, Kelantan, Kedah or
another variety; do not merge them into a generic “Malay accent.”

## Conversational forms

The table is a contextual reading aid. A full form is not always a one-to-one
replacement in every utterance. DBP explicitly discusses shortened `tu`, `ni`,
`kan` and `nak` in dialogue ([S32](sources.md#s32)); S01 documents reduced
aspect/demonstrative forms in mixed usage, and S15 discusses `tak nak`.

| Form | Typical reading | What a rewrite must preserve |
|---|---|---|
| `tak` | `tidak`, negation | Scope and whether the speaker refuses, denies or reports absence. |
| `nak` | `hendak/mahu`, wanting or intending | Do not turn desire into a completed event; in address it may have another source, such as `anak`. |
| `dah` | `sudah`, already/completion or change of state | Completion is different from merely past time. |
| `ni`, `tu` | `ini`, `itu` | Near/distal reference and discourse function. |
| `je` / `saja` | `sahaja`, only/just in common uses | Restriction, reassurance or dismissiveness depends on context. |
| `kat` | Location in many conversational constructions | Does not always mean physically near; check `dekat` separately. |
| `tengah` | Ongoing activity in some verbal constructions | Can also mean the middle; do not label it an aspect marker everywhere. |
| `tak ada`, `takde` | Nonexistence or absence | This is not necessarily “do not own”; use the source context. |
| `korang` | Plural familiar addressees | Do not substitute for singular or formal “you.” |
| `diorang` / `dia orang` | Colloquial “they” in relevant usage | Resolve whether the sequence is a pronoun or literal words; keep plurality. |
| `macam` | Like/as if/kind in different contexts | A hedge or comparison is not an assertion of identity. |
| `pasal` | About/because in different constructions | Topic and cause cannot be exchanged blindly. |

The last eight entries are practical interpretation guidance, not claims of
equal frequency across Singapore and Malaysia. Confirm them against the speaker
or relevant corpus when that distinction matters. The default written style uses
readable `tak ada`, `ini/itu` or `ni/tu` consistently within the chosen context;
it does not require every available reduction in one sentence.

## Pronouns, politeness and address

Maintain an established `saya/awak`, `aku/kau`, or `I/you` relationship. Switching
between them may itself carry a change in social stance; do not vary them merely
for lexical diversity. `Anda` is useful in some public or formal address but can
sound different from ordinary conversation. Names and titles can replace pronouns
when the source supports them. Avoid invented `abang`, `kak`, `adik`, `pakcik`,
`makcik`, `bro` or `sis` as automatic local styling.

`Kita` and `kami` deserve a separate semantic check, even when the rest of a
sentence is English. With unresolved English *we*, an English pronoun can preserve
the ambiguity. A Malay `dia` can similarly remain Malay when the source gives no
gender and switching to English would force an unsupported choice.

## Particles are choices with consequences

The authored examples below illustrate possible readings, not fixed dictionary
translations. Prosody and preceding turns may change the reading. S04 studies
Chinese Malaysian young adults' Facebook interaction; S05 studies Colloquial
Singapore English across ethnic groups. They support contextual interpretation,
not a claim that each particle is an ordinary Malay word or evidence of a
Malay–English switch.

| Form | Possible contribution | Authored illustration / constraint |
|---|---|---|
| `lah` | Insistence, encouragement, softening or shared stance in different contexts | `Try dulu lah.` cannot be assigned one force without delivery/context. |
| `kan` | A check, reminder or appeal to assumed shared knowledge | `You dah hantar, kan?` anticipates confirmation more than a neutral information question. |
| `ke` | Conversational question/alternative function | `You nak datang ke?` differs from directional `ke pejabat`. |
| `eh` | Attention, surprise or repair | Keep a genuine self-correction; do not add surprise to a neutral source. |
| `ah` | Context-sensitive regional particle or hesitation | Classify from its actual function rather than treating all `ah` as the same item. |
| `meh`, `lor`, `leh`, `hor`, `mah` | Possible regional English/contact-variety particles | Use only when the speaker/profile supports them; no automatic Malay label. |

Distinguish suffix `-kan` from free `kan`: an apparent `check kan` may require
audio and context to resolve. DBP's dialogue advice makes this distinction
([S32](sources.md#s32)). Likewise, formal written Malay attaches `-lah/-kah`,
whereas a corpus may tokenize discourse `lah` separately. Pick and document the
annotation convention; never silently change benchmark tokenization midway.

## Spoken does not mean synthetically broken

Keep a manageable sentence with a coherent event and switch. Do not deliberately
delete articles, invert every noun phrase, or add fillers to imitate a regional
identity. A native speaker's actual omission is evidence to transcribe; an
author's random omission is not evidence of naturalness. A generation reviewer
should explain the specific awkward construction rather than simply saying
“too much English” or “not Malay enough.”
