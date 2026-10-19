# 400 historical Astra reference pairs

Read [the style guidance](astra_style.md) first. All 400 pairs retain the exact source and output text from the best saved 2,000-row Astra run. They span everyday and factual contexts, Tamil-led and English-led constructions, questions, corrections and reports.

Start with the 14 examples below, then consult 2-6 relevant pairs for the current task. Do not load the entire library into every prompt or imitate one frame across a batch. Historical review acceptance is verified against each exact tagged output; selection inspection is not a new independent review or human certification.

## Find relevant pairs

From the frozen rule folder, use the read-only lookup tool:

```bash
python3 references/astra_examples.py --context health_and_care --query "appointment report" --limit 4
python3 references/astra_examples.py --list-contexts
```

Use repeatable `--exclude-id SOURCE_LOCK_ID` to avoid current target IDs where possible; record returned IDs in inspection notes. Query matches rank relevant source words, not linguistic quality. Context labels are navigation annotations, sometimes overlapping or incidental, not original corpus metadata.

| Context | Pairs |
|---|---:|
| [Health And Care](astra_examples/health_and_care.md) | 27 |
| [Education And Study](astra_examples/education_and_study.md) | 56 |
| [Money And Purchases](astra_examples/money_and_purchases.md) | 55 |
| [Transport And Travel](astra_examples/transport_and_travel.md) | 46 |
| [Technology And Communication](astra_examples/technology_and_communication.md) | 29 |
| [Food And Dining](astra_examples/food_and_dining.md) | 47 |
| [Arts Media And Sport](astra_examples/arts_media_and_sport.md) | 23 |
| [Public Services And Law](astra_examples/public_services_and_law.md) | 43 |
| [Family And Social](astra_examples/family_and_social.md) | 27 |
| [Work And Admin](astra_examples/work_and_admin.md) | 57 |
| [Science Environment And Places](astra_examples/science_environment_and_places.md) | 17 |
| [Conversation and General](astra_examples/conversation_and_general.md) | 85 |

This teaching subset averages **46.96% English** by the script-token metric; the full historical run averages **51.92%**. The full run supplies the soft overall balance reference, not a quota imposed on these examples or individual rows.

## 14 starter examples

Construction notes describe possibilities, not obligatory patterns.

| ID suffix | Historical source | Saved Astra output | Construction to notice |
|---|---|---|---|
| 0012 | Because the Grab fare at Bishan was too high, we were late. | Bishan-ல Grab fare too high-ஆ இருந்ததால நாங்க late ஆயிட்டோம். | An English fare phrase sits inside a Tamil cause-and-result construction. |
| 0018 | We need to submit the assignment in Jurong East before lunch. | நாம Jurong East-ல assignment-ஐ lunch-க்கு முன்னாடி submit பண்ணணும். | Tamil handles obligation, location and deadline around intact English content words. |
| 0020 | We have to follow up the doctor review by 5 pm. | நாம doctor review-ஐ 5 pm-க்குள்ள follow up பண்ணணும். | The follow up verb phrase stays together; Tamil carries obligation and the deadline. |
| 0033 | Rejoice because you can enjoy free undergraduate education at the University of Helsinki, regardless of your nationality. | சந்தோஷப்படுங்க, உங்க nationality எதுவா இருந்தாலும் University of Helsinki-ல free undergraduate education படிக்கலாம். | The Tamil concessive clause connects nationality to the education opportunity. |
| 0071 | Administrative buildings, living quarters, and a mess hall were damaged, as were roads, a nearby airfield and other infrastructure. | Administrative buildings, living quarters, mess hall எல்லாம் சேதமாச்சு; roads, பக்கத்துல இருந்த airfield, மத்த infrastructure-க்கும் சேதம் ஏற்பட்டுச்சு. | English list items share Tamil damage predicates across two coordinated clauses. |
| 0139 | No, not this week; use next week. | No, இந்த வாரம் இல்ல. Use next week. | A correction switches at a discourse boundary, followed by an English instruction. |
| 0159 | The committee will review the residents' feedback in Jurong East this week. | Committee இந்த வாரம் Jurong East-ல residents' feedback-ஐ review பண்ணும். | English committee and feedback phrases integrate with Tamil time, case and future tense. |
| 0173 | Meena said we need to confirm the clinic trip with the family. | Family-ஓட clinic trip-ஐ நாம confirm பண்ணணும்னு Meena சொன்னாங்க. | The report is organized around a Tamil quotative, not an English sentence with a translated tail. |
| 0209 | Nisha said the clinic appointment is confirmed, but I cannot fix it now. | Nisha said the clinic appointment is confirmed, ஆனா என்னால இப்போ அதை fix பண்ண முடியல. | An English report leads into a Tamil contrast and inability clause; fix stays English. |
| 0369 | Coincidentally, there were people who were trained. | Coincidentally, training பெற்றவங்க இருந்தாங்க. | An English discourse adverb and training noun integrate with a Tamil existence clause. |
| 0418 | The earth's core is made of iron and nickel. | Earth-ஓட core iron, nickel-ஆல ஆனது. | English technical terms retain their identity; Tamil marks possession and composition. |
| 0502 | Standardisation of project documentation reduces costs and uncertainty and helps identify common risk issues and solutions. | Project documentation-ஐ standardise பண்றது costs-ஐயும் uncertainty-ஐயும் குறைக்குது, common risk issues-ஐயும் solutions-ஐயும் கண்டறிய உதவுது. | English technical phrases are coordinated through Tamil case, predicates and a nominalized action. |
| 0540 | It also urged patience on the part of the rest of the world. | அது மேலும், rest of the world patience காட்டணும்னு வலியுறுத்துச்சு. | English phrases integrate into a Tamil reported request with its original force. |
| 0699 | Two other North Korean vessels were hit with a global assets freeze, but are not banned from port entry. | இன்னும் two North Korean vessels-க்கு global assets freeze விதிச்சாங்க, ஆனா port entry-க்கு தடை இல்ல. | The contrast changes clause structure while retaining English technical expressions. |

Exact tagged text is in [JSONL](astra_style_examples.jsonl); file hashes and measured profiles are in [the provenance receipt](astra_style_provenance.json).
Examples are disjoint from the current 20-row pilot. A full same-2,000 rerun necessarily includes their IDs: keep those rows and disclose their exposure to references rather than calling their evaluation blind.
