# Refine the English–Tamil rules

Vignesh developed this comprehensive project rulebook through iterative human
review and transcription work: inspecting generated sentences, collecting/scraping online
Tamil vocabulary and language references, considering Singapore English context,
and revising rules when examples failed. This is one person's evolving project
rulebook. It needs peer review, feedback from Tamil–English speakers, and further
rules and counterexamples as users encounter new situations. It is not an
exhaustive or independently certified description of Tamil code-switching.

## Where to make a change

Edit the maintained files under `vig-codex_approach/lexical_rules/`:

| File | What belongs there |
|---|---|
| [SKILL.md](SKILL.md) | Short agent entrypoint and links to relevant detail |
| [references/linguistic_details.md](references/linguistic_details.md) | Switching, Tamil case endings, light verbs, agreement, negation and contextual Singapore particles |
| [references/spoken_tamil.md](references/spoken_tamil.md) | Conversational register, respectful forms and dialect-sensitive examples |
| [references/astra_style.md](references/astra_style.md) | Natural phrasing and a soft corpus-level balance reference from the saved Astra run |
| [references/meaning_and_edge_cases.md](references/meaning_and_edge_cases.md) | Source meaning, ambiguity, quantities, conditions and exceptions |
| [references/worked_pairs.md](references/worked_pairs.md) | Good/bad source–output examples with explanations |
| [loanwords.json](loanwords.json) | Contextual lexical candidates, using the existing JSON schema |
| [review_checklist.md](review_checklist.md) | What a reviewer must check before accepting a row |
| [references/sources.md](references/sources.md) | Evidence links and the scope/limitations of each reference |

The top-level `lexical_rules/` directory mirrors this maintained folder. From
the repository root, synchronize and check it after editing:

```bash
python scripts/sync_lexical_rules.py --write
python scripts/sync_lexical_rules.py
```

## Write rules an agent can apply

Use a short descriptive heading or stable rule ID, then provide the condition,
required action, exceptions, one faithful example and one failed alternative.
Explain why the alternative fails. Cite the language reference or label the
item as a proposed local convention. Do not make a dialect preference universal.

For example, a proposed rule about negation should show that “has not arrived
yet” retains **both negation and the current not-yet state**; an output meaning
“will not come” changes the source. Do not simply tell the model to “sound natural.”

Keep `SKILL.md` compact. Put detailed examples in the relevant reference file
and link them from the entrypoint/checklist when they affect review. Agents read
these files during generation and review; adding a rule does **not** retrain the
model's weights. A useful entry makes the condition and evidence easy to find.

When an output sounds translated, record the full source/output pair, identify
the awkward boundary or register choice and propose a whole-utterance repair.
Explain how it improves the construction without changing the meaning. Put new
teaching examples in `references/worked_pairs.md`; do not silently rewrite the
exact historical Astra examples. Their extraction and hashes are checked by
`python3 scripts/build_astra_style_reference.py --check` from the repository root.
If intentionally selecting different historical examples, update the IDs and
context labels in `publication/provenance/astra_style_400_selection.json` from
the repository root. Inspect complete pairs before selecting them; a historical
approval alone does not make an example suitable. Run the extraction script
without `--check` to regenerate all topic pages and provenance, then synchronize
the rule copies. Keep the starter notes in the script aligned with their exact
rows. The portable lookup helper only retrieves examples; it does not grade them.

Try the change on a small fixed English-input pilot, have a fresh reviewer inspect
the actual source–output pairs, retain failures, and refine the rule. Add a code
check only for an objectively testable property; scripts cannot certify semantic
faithfulness or fluent Tamil. Freeze the revised rule folder in a new run and
give comparison systems the same version. Do not edit a completed run's frozen
rules or reuse approvals after changing the candidate or its review context.

The example workflow starts from English. The linguistic guidance also supports
Tamil-only and already mixed English–Tamil input when the task requests a
meaning-preserving rewrite. That input support is not evidence that every input
type has been benchmarked equally. Transcription must preserve the languages
actually spoken rather than introduce new switches.
