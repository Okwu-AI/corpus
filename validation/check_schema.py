#!/usr/bin/env python3
"""Validate every fixture record against schema/public-record.schema.json."""
import json, pathlib, sys

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("pip install jsonschema", file=sys.stderr)
    sys.exit(1)

schema = json.loads(pathlib.Path("schema/public-record.schema.json").read_text(encoding="utf-8"))
validator = Draft202012Validator(schema)

total = errors = 0
for p in sorted(pathlib.Path("fixtures").glob("*.json")):
    data = json.loads(p.read_text(encoding="utf-8"))
    for rec in (data if isinstance(data, list) else [data]):
        total += 1
        for e in validator.iter_errors(rec):
            errors += 1
            rid = rec.get("record_id", "<no id>")
            print(f"FAIL {p.name} {rid}: {'/'.join(map(str, e.path)) or '(root)'}: {e.message}",
                  file=sys.stderr)

print(f"Validated {total} record(s) against schema {schema.get('$id', '?')}")
sys.exit(1 if errors else 0)
