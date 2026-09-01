#!/usr/bin/env python3
"""Fail on duplicate sentence pairs. Run after check_normalisation.py passes."""
import json, pathlib, sys, unicodedata
from collections import defaultdict


def records():
    for p in sorted(pathlib.Path("fixtures").glob("*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        yield from (data if isinstance(data, list) else [data])


def key(rec):
    def norm(s):
        return unicodedata.normalize("NFC", (s or "").strip().casefold())
    return (rec.get("source_lang"), norm(rec.get("source_text")), norm(rec.get("english_translation")))


def main():
    groups, total = defaultdict(list), 0
    for rec in records():
        total += 1
        groups[key(rec)].append(rec.get("record_id", "<no id>"))
    dupes = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"Checked {total} records, {len(groups)} unique pairs.")
    if dupes:
        print(f"\nFAIL: {len(dupes)} duplicated pair(s):", file=sys.stderr)
        for ids in list(dupes.values())[:20]:
            print("  " + ", ".join(ids), file=sys.stderr)
        return 1
    print("OK: no exact duplicates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
