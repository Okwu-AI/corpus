# Validation toolkit

Checks run on every contribution.

| Check | What it enforces |
|---|---|
| `check_schema.py` | Records match `schema/public-record.schema.json` |
| `check_normalisation.py` | One Unicode form across the corpus |
| `check_duplicates.py` | No exact duplicate pairs |

Language identity, benchmark-leakage, and provenance checks are planned for future releases.
