#!/usr/bin/env python3
"""Read-only provenance audit; does not perform language identification or ASR."""

import argparse
import hashlib
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path


CHARACTER_FLAG = re.compile(r"[\u4e00-\u9fff\u0b80-\u0bff\u0600-\u06ff]")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def audit_dataset(root, key):
    manifest = root / key / "manifest.jsonl"
    receipt_path = root / key / "receipt.json"
    raw = manifest.read_bytes()
    rows = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    receipt_raw = receipt_path.read_bytes()
    receipt = json.loads(receipt_raw)
    digest = hashlib.sha256(raw).hexdigest()
    spec = receipt["spec"]
    require(rows, f"{key}: empty manifest")
    require(len({row["id"] for row in rows}) == len(rows), f"{key}: duplicate IDs")
    require(digest == receipt["manifest_sha256"], f"{key}: manifest hash mismatch")
    require(len(rows) == receipt["selected"], f"{key}: selected count mismatch")
    for row in rows:
        require(isinstance(row["reference"], str), f"{row['id']}: reference is not text")
        duration = row["duration"]
        require(isinstance(duration, (int, float)) and math.isfinite(duration)
                and duration > 0, f"{row['id']}: invalid duration")
        for field, expected in (("repository", spec["repo"]), ("revision", spec["revision"]),
                                ("config", spec["config"]), ("split", spec["split"])):
            require(row[field] == expected, f"{row['id']}: {field} differs from receipt")
    seconds = math.fsum(row["duration"] for row in rows)
    require(math.isclose(seconds / 3600, receipt["hours"], rel_tol=0, abs_tol=1e-9),
            f"{key}: duration differs from receipt")
    flagged = [row["id"] for row in rows if CHARACTER_FLAG.search(row["reference"])]
    return {
        "key": key,
        "manifest_relative_path": f"{key}/manifest.jsonl",
        "manifest_sha256": digest,
        "receipt_sha256": hashlib.sha256(receipt_raw).hexdigest(),
        "repository": spec["repo"], "revision": spec["revision"],
        "config": spec["config"], "split": spec["split"],
        "clip_count": len(rows), "summed_clip_seconds": seconds,
        "summed_clip_hours": seconds / 3600,
        "minimum_clip_seconds": min(row["duration"] for row in rows),
        "maximum_clip_seconds": max(row["duration"] for row in rows),
        "receipt_scanned": receipt["scanned"], "receipt_eligible": receipt["eligible"],
        "receipt_selected": receipt["selected"],
        "receipt_excluded_by_reason": receipt["excluded_by_reason"],
        "receipt_sampling": receipt["sampling"],
        "all_eligible_retained": receipt["eligible"] == receipt["selected"],
        "receipt_checks_passed": True,
        "character_flag_count": len(flagged), "character_flag_ids": flagged,
        "lexical_code_switch_count": None, "audio_confirmed_code_switch_count": None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--datasets-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path,
                        help="New JSON file; existing files are not overwritten")
    args = parser.parse_args()
    result = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "method": "Read original JSONL manifests and saved selection receipts; no audio access",
        "duration_basis": "Sum of manifest clip durations, not unique recording coverage",
        "character_flag_pattern": CHARACTER_FLAG.pattern,
        "character_flag_scope": "Han U+4E00–9FFF, Tamil U+0B80–0BFF, Arabic U+0600–06FF; not language identification",
        "language_classification_performed": False,
        "audio_review_performed": False,
        "datasets": [audit_dataset(args.datasets_root, key)
                     for key in ("fleurs_ms", "mesolitica_ms")],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    for dataset in result["datasets"]:
        print(f"{dataset['key']}: {dataset['clip_count']} clips, "
              f"{dataset['summed_clip_hours']:.6f} hours; receipt checks passed")
    print(f"Wrote {args.output}. No language or acoustic classification performed.")


if __name__ == "__main__":
    main()
