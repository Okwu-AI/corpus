#!/usr/bin/env python3
"""Fail if text fields use more than one Unicode normalisation form."""
import json, pathlib, sys, unicodedata
from collections import Counter

CANONICAL = None  # "NFC" or "NFD"
TEXT_FIELDS = ("source_text", "source_text_normalized", "english_translation")


def records():
    for p in sorted(pathlib.Path("fixtures").glob("*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        yield from (data if isinstance(data, list) else [data])


def main():
    seen, checked = Counter(), 0
    for rec in records():
        for f in TEXT_FIELDS:
            t = rec.get(f)
            if not isinstance(t, str) or not t:
                continue
            checked += 1
            forms = [n for n in ("NFC", "NFD") if unicodedata.is_normalized(n, t)]
            seen[tuple(forms) or ("neither",)] += 1

    if not checked:
        print("No text fields found in fixtures/.")
        return 0

    print(f"Checked {checked} text values:")
    for forms, n in seen.items():
        print(f"  {'+'.join(forms):12} {n}")

    distinct = {f for f in seen if f != ("neither",) and len(f) == 1}
    if len(distinct) > 1:
        print("\nFAIL: corpus mixes NFC and NFD.", file=sys.stderr)
        return 1
    if ("neither",) in seen:
        print("\nFAIL: some values are in neither NFC nor NFD.", file=sys.stderr)
        return 1
    if CANONICAL and distinct and (CANONICAL,) not in distinct:
        print(f"\nFAIL: expected {CANONICAL}.", file=sys.stderr)
        return 1
    print("\nOK: consistent normalisation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
