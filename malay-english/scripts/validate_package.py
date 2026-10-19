#!/usr/bin/env python3
"""Validate package structure and declared annotations, not linguistic correctness."""

import json
import math
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LABELS = {"MS", "EN", "MIXED", "NE", "SHARED", "AMBIG", "PART", "FILLER",
          "OTHER", "UNCLEAR", "NONLEX"}
CATEGORIES = {"lexical_ms_en", "ms_only", "en_only", "particle_only_mix",
              "entity_or_loan_only_mix", "mixed_morpheme_only", "ambiguous",
              "other_language", "unusable"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_jsonl(relative):
    rows = [json.loads(line) for line in (ROOT / relative).read_text(encoding="utf-8").splitlines()
            if line.strip()]
    require(len({row["id"] for row in rows}) == len(rows), f"Duplicate IDs in {relative}")
    return rows


def check_spans(text, spans, begin=0, end=None):
    end = len(text) if end is None else end
    cursor = begin
    for span in spans:
        require(span["label"] in LABELS, f"Unknown label: {span}")
        require(type(span["start"]) is int and type(span["end"]) is int,
                f"Noninteger offset: {span}")
        require(span["start"] == cursor and cursor < span["end"] <= end,
                f"Gap, overlap or out-of-range span: {span}")
        require(text[span["start"]:span["end"]] == span["text"], f"Offset mismatch: {span}")
        if span["label"] == "MIXED":
            components = span["components"]
            require({"MS", "EN"} <= {item["label"] for item in components},
                    f"Mixed span missing language components: {span}")
            check_spans(text, components, span["start"], span["end"])
        else:
            require("components" not in span, f"Unexpected component spans: {span}")
        cursor = span["end"]
    require(cursor == end, "Spans do not cover the declared interval")


def main():
    rule_text = (ROOT / "references/linguistic_rules.md").read_text(encoding="utf-8")
    rule_ids = set(re.findall(r"^## (R\d{2}) —", rule_text, re.M))
    source_text = (ROOT / "references/sources.md").read_text(encoding="utf-8")
    source_ids = set(re.findall(r"^### (S\d{2})$", source_text, re.M))
    sound_text = (ROOT / "references/pronunciation_and_asr.md").read_text(encoding="utf-8")
    sound_ids = set(re.findall(r"^## (P\d{2}) —", sound_text, re.M))
    require(rule_ids == {f"R{i:02}" for i in range(1, 41)}, "Expected R01–R40")
    require(source_ids == {f"S{i:02}" for i in range(1, 36)}, "Expected S01–S35")
    require(sound_ids == {f"P{i:02}" for i in range(1, 12)}, "Expected P01–P11")

    for path in sorted(ROOT.rglob("*.md")):
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            local = (path.parent / unquote(url.path)).resolve() if url.path else path
            require(local.is_relative_to(ROOT), f"Link escapes standalone package: {path}: {target}")
            require(local.exists(), f"Missing local link: {path}: {target}")
            if local.name == "sources.md" and url.fragment:
                require(url.fragment.upper() in source_ids, f"Invalid source anchor: {target}")
        require(set(re.findall(r"\bR\d{2}\b", content)) <= rule_ids,
                f"Unknown rule ID in {path}")
        require(set(re.findall(r"\bS\d{2}\b", content)) <= source_ids,
                f"Unknown source ID in {path}")

    examples = read_jsonl("examples/worked_examples.jsonl")
    require({row["id"] for row in examples} == {f"ME{i:03}" for i in range(1, 65)},
            "Expected 64 worked examples")
    human_examples = (ROOT / "examples/worked_examples.md").read_text(encoding="utf-8")
    for row in examples:
        require(row["source_origin"] == "authored_for_this_guide" and row["benchmark_derived"] is False,
                f"Unexpected source provenance: {row['id']}")
        require(row["review_status"] == "authored_draft_not_native_validated",
                f"Unexpected review claim: {row['id']}")
        require(row["task"] == "rewrite" and row["input_language"] in {"en", "ms", "mixed"},
                f"Invalid task/language: {row['id']}")
        require(row["profile"] == "sg_conversational", f"Unexpected profile: {row['id']}")
        require(row["rule_ids"] and set(row["rule_ids"]) <= rule_ids,
                f"Bad rule references: {row['id']}")
        for field in ("ms_evidence", "en_evidence"):
            require(row[field] and row[field].casefold() in row["candidate"].casefold(),
                    f"Missing evidence substring: {row['id']} {field}")
        section = human_examples.split(f"## {row['id']} —", 1)[1].split("\n## ", 1)[0]
        for field in ("source", "candidate", "explanation"):
            require(row[field] in section, f"Markdown/JSONL mismatch: {row['id']} {field}")

    lexicon = json.loads((ROOT / "lexicon.json").read_text(encoding="utf-8"))["entries"]
    require(len(lexicon) == 53 and len({row["id"] for row in lexicon}) == 53,
            "Expected 53 unique lexical entries")
    for row in lexicon:
        require(set(row["source_ids"]) <= source_ids and set(row["rule_ids"]) <= rule_ids,
                f"Invalid lexical references: {row['id']}")
        require(row["automatic_replacement"] is False and row["evidence_scope"],
                f"Missing contextual limitation: {row['id']}")

    annotations = read_jsonl("examples/annotation_examples.jsonl")
    require(len(annotations) == 12, "Expected 12 annotation fixtures")
    for row in annotations:
        require(row["evidence"] == "authored_fixture", f"Unexpected evidence claim: {row['id']}")
        require(row["text_category"] in CATEGORIES, f"Unknown text category: {row['id']}")
        check_spans(row["text"], row["spans"])
        if row["text_category"] == "lexical_ms_en":
            require({"MS", "EN"} <= {span["label"] for span in row["spans"]},
                    f"Fixture missing its declared lexical evidence: {row['id']}")

    audit = json.loads((ROOT / "evidence/benchmark_audit.json").read_text(encoding="utf-8"))
    require(audit["language_classification_performed"] is False
            and audit["audio_review_performed"] is False, "Unexpected benchmark review claim")
    expected = {"fleurs_ms": (749, 2.264, 0), "mesolitica_ms": (993, 2.75152609375, 4)}
    require({row["key"] for row in audit["datasets"]} == set(expected), "Unexpected datasets")
    for row in audit["datasets"]:
        count, hours, flags = expected[row["key"]]
        require(row["clip_count"] == count and math.isclose(row["summed_clip_hours"], hours),
                f"Benchmark count/duration mismatch: {row['key']}")
        require(row["character_flag_count"] == len(row["character_flag_ids"]) == flags,
                f"Character flag mismatch: {row['key']}")
        require(row["receipt_checks_passed"] and row["lexical_code_switch_count"] is None
                and row["audio_confirmed_code_switch_count"] is None, "Unsupported benchmark count")
    print(f"PASS: {len(rule_ids)} grammar rules, {len(sound_ids)} sound rules, {len(source_ids)} sources")
    print(f"PASS: {len(examples)} worked examples {dict(Counter(row['input_language'] for row in examples))}")
    print(f"PASS: {len(lexicon)} lexical entries, {len(annotations)} annotation fixtures, local links and audit metadata")
    print("These are structural checks; they do not certify meaning, fluency, language labels or audio.")


if __name__ == "__main__":
    main()
