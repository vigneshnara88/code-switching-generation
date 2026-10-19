# Lexical decisions

This curated lookup contains established forms, ambiguous spellings, conversational
forms and candidate English insertions. It is **not a complete dictionary** or a
replacement map. Evidence depth is recorded per entry. Some examples illustrate
ordinary lexical contrasts without a separately checked dictionary source; these
are marked as authored guidance and should be verified for the target variety.

For every token, first identify meaning and grammatical role. Then check the
speaker/register, lexicalization and available audio. Assign a label under
[the contract](annotation_and_benchmarking.md); preserve uncertainty where needed.
Never rewrite an entire benchmark by substituting the English side of a bilingual
word list. That can manufacture switches and alter the reference language.

English candidates below are authoring options, not claims that the cited papers
observed every word. The Malay gloss describes a possible sense rather than an
instruction to translate it. All contexts in this file are newly authored.

The [JSON](../lexicon.json) carries IDs, source/rule references, evidence scope
and a false `automatic_replacement` flag for every entry.


## established malay form

| ID / form | Interpretation | Decision |
|---|---|---|
| L001 / `komputer` | Malay computer noun | Label MS in ordinary Malay use; do not infer EN from etymology. |
| L002 / `telefon` | Malay phone noun or related lexical uses | Preserve the Malay form; a real English phrase elsewhere supplies English evidence. |

## homograph

| ID / form | Interpretation | Decision |
|---|---|---|
| L003 / `fail` | Malay file noun; English verb fail | Determine sense and syntax; do not globally translate or label it. |
| L004 / `air` | Malay water; English air | Resolve from phrase and audio; isolated form can remain AMBIG. |
| L005 / `main` | Malay play; English principal/main | Do not classify by English dictionary membership alone. |
| L006 / `can` | Malay colloquial opportunity in some contexts; English modal/container | Review the particular sense, register and pronunciation. |
| L007 / `cat` | Malay paint; English animal | Keep Malay and English pronunciations separate in a pronunciation layer. |
| L008 / `jam` | Malay hour/clock; English jam | Use the phrase meaning; do not assume an English-looking spelling is a switch. |

## shared or ambiguous

| ID / form | Interpretation | Decision |
|---|---|---|
| L009 / `pin` | Potential Malay loan or English noun/verb; PIN may be an acronym | Use context; no missing-language evidence solely from the isolated spelling. |
| L010 / `bank` | Established shared financial term and other English senses | Use contextual evidence or SHARED; do not count the isolated financial noun as decisive. |
| L011 / `hotel` | Shared accommodation term | Apply the sentence context and loan policy. |
| L012 / `video` | Shared media term | Avoid an automatic EN label from the spelling alone. |
| L013 / `radio` | Shared broadcast term | Preserve the actual word and use contextual labels. |
| L014 / `internet` | Widely shared technical term | Do not use as sole proof of English without stronger evidence. |

## entity or acronym

| ID / form | Interpretation | Decision |
|---|---|---|
| L015 / `MRT` | Transport acronym | Record spoken letters if audible; an expansion is a separate field. |
| L016 / `WhatsApp` | Product name; also usable in verbal constructions | Distinguish entity mention from a contextually analyzed verb. |

## numeric notation

| ID / form | Interpretation | Decision |
|---|---|---|
| L017 / `RM20` | Currency amount | Preserve currency and value; no EN/MS proof from written digits. |
| L018 / `SGD30` | Currency amount | Do not replace with RM or convert the amount while rewriting. |

## contextual malay form

| ID / form | Interpretation | Decision |
|---|---|---|
| L019 / `tak` | tidak / negation | Preserve scope; distinguish inability from refusal. |
| L020 / `nak` | want/intend; sometimes another contraction in address | Resolve the construction; do not automatically expand to one word. |
| L021 / `dah` | sudah / completed or changed state | Do not treat as a universal past-tense ending. |
| L022 / `ni` | ini / proximal demonstrative or discourse use | Preserve the intended referent. |
| L023 / `tu` | itu / distal demonstrative or discourse use | Keep this/that distinction and context. |
| L024 / `je` | sahaja / just or only in common uses | Check whether restriction, reassurance or stance is intended. |
| L025 / `kat` | locative in conversational usage | Do not translate every occurrence as near. |
| L026 / `tengah` | ongoing action or middle, depending on construction | Distinguish aspectual from spatial meaning. |
| L027 / `takde` | conversational tak ada | Keep a declared surface spelling; do not silently expand a benchmark. |
| L028 / `korang` | familiar plural you | Do not use for formal or singular addressees without support. |
| L029 / `diorang` | colloquial they | Preserve plurality; do not assume formal-writing status. |
| L030 / `macam` | like, kind or resemblance, depending on context | Do not turn a hedge into certainty. |
| L031 / `pasal` | about/because depending on construction | Separate topic from cause. |
| L032 / `kita` | ordinary inclusive we | Do not substitute for exclusive we when the source distinguishes it. |
| L033 / `kami` | ordinary exclusive we | Do not silently include the addressee. |
| L034 / `dia` | third-person referent without grammatical gender | Do not guess he/she from the word alone. |
| L035 / `kena` | obligation or affected/passive-like construction among other senses | Resolve who acts and who is affected. |

## particle or function ambiguity

| ID / form | Interpretation | Decision |
|---|---|---|
| L036 / `lah` | context-sensitive particle | Do not append universally or count as sole Malay lexical evidence. |
| L037 / `kan` | free particle or distinct suffix -kan | Analyze morphology versus confirmation/stance. |
| L038 / `ke` | directional preposition or conversational question use | Do not concatenate every occurrence with the next word. |
| L039 / `ah` | regional particle or hesitation | Identify function from delivery and context. |
| L040 / `eh` | attention, surprise or repair in different contexts | Do not add a new emotional stance to a source. |
| L041 / `okay` | lexical adjective/acknowledgment or shared conversational item | A context-sensitive label; no universal filler or English rule. |
| L042 / `uh` | possible hesitation | A hesitation alone does not provide substantive English evidence. |

## english candidate

| ID / form | Interpretation | Decision |
|---|---|---|
| L043 / `check` | English candidate; Malay interpretation: semak/periksa according to sense | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L044 / `submit` | English candidate; Malay interpretation: hantar/serahkan according to task | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L045 / `print` | English candidate; Malay interpretation: cetak | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L046 / `delete` | English candidate; Malay interpretation: padam | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L047 / `download` | English candidate; Malay interpretation: muat turun | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L048 / `upload` | English candidate; Malay interpretation: muat naik | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L049 / `meeting` | English candidate; Malay interpretation: mesyuarat/pertemuan according to context | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L050 / `deadline` | English candidate; Malay interpretation: tarikh akhir/batas masa according to context | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L051 / `follow up` | English candidate; Malay interpretation: susulan; determine the intended action | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |
| L052 / `ready` | English candidate; Malay interpretation: sedia/siap according to the predicate | Keep if it is the intended English insertion; do not automatically translate or assume its frequency. |

## mixed morphology

| ID / form | Interpretation | Decision |
|---|---|---|
| L053 / `di-check` | Malay passive prefix plus English stem | Store a MIXED parent and components; do not treat locative di as the same construction. |
