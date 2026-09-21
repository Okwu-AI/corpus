# Changelog

Every released version: what changed, what was corrected, what was withdrawn.

## [Unreleased]

### Added
- `yor-eng`: 3,996 Yorùbá-English pairs from four translator batches delivered
  2026-09-21 (`YOR-001194`-`YOR-005189`), taking the config from 1,193 to 5,189 records.
  Source text normalised to NFC; 515 delivered values were re-normalised on ingest.
  21 exact duplicates within the submission removed; none duplicated an existing record.

### Notes
- The new records carry `verified: true`. Note that 45 rows in one batch omit the Yorùbá
  sub-dot characters entirely; see the diacritics entry in `docs/known-limitations.md`.
- Five submitted rows were withheld: three with no translation supplied, and two carrying
  a stray value in an unexpected column.
- Published to Hugging Face on 2026-09-21; corpus counts in README.md updated to 14,359.
  Removed `okwu-portal-2026-09-20T08-32-59.csv`, a portal export holding a single
  placeholder test record that was being served as part of `yor-eng`.

## [1.0.0] - 2026-08-31
- Initial public release.
