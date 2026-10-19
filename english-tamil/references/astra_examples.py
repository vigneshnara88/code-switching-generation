#!/usr/bin/env python3
"""Read a bounded selection of exact historical Astra pairs from frozen rules."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re


def select_examples(rows, *, context=None, query='', limit=6, exclude_ids=()):
    if not 1 <= limit <= 20:
        raise ValueError('limit must be between 1 and 20')
    contexts = {label for row in rows for label in row['reference_contexts']}
    if context is not None and context not in contexts:
        raise ValueError(f'Unknown context: {context}')
    excluded = set(exclude_ids)
    terms = set(re.findall(r'\w+', query.casefold()))
    candidates = [row for row in rows if row['source_lock_id'] not in excluded
                  and (context is None or context in row['reference_contexts'])]
    if terms:
        def score(row):
            return len(terms & set(re.findall(r'\w+', row['mono_text'].casefold())))
        candidates = sorted((row for row in candidates if score(row)),
                            key=lambda row: (-score(row), row['source_lock_id']))
    return candidates[:limit]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--context')
    parser.add_argument('--query', default='')
    parser.add_argument('--limit', type=int, default=6)
    parser.add_argument('--exclude-id', action='append', default=[])
    parser.add_argument('--list-contexts', action='store_true')
    args = parser.parse_args()
    rows = [json.loads(line) for line in
            Path(__file__).with_name('astra_style_examples.jsonl').read_text(encoding='utf-8').splitlines()]
    if args.list_contexts:
        counts = Counter(label for row in rows for label in row['reference_contexts'])
        print(json.dumps(dict(sorted(counts.items())), indent=2))
        return
    try:
        selected = select_examples(rows, context=args.context, query=args.query,
                                   limit=args.limit, exclude_ids=args.exclude_id)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps({'matched_examples': len(selected), 'examples': selected}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
