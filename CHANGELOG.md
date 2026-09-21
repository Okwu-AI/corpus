# Changelog

Every released version: what changed, what was corrected, what was withdrawn.

## [Unreleased]

### Added
- `yor-eng`: 3,996 Yorùbá-English pairs from four translator batches delivered
  2026-09-21 (`YOR-001194`-`YOR-005189`), taking the config from 1,193 to 5,189 records.
  Source text normalised to NFC; 515 delivered values were re-normalised on ingest.
  21 exact duplicates within the submission removed; none duplicated an existing record.

### Notes
- The new records carry `verified: false`. No validation pass has been run on them, and
  45 rows in one batch are demonstrably under-diacritised. They are the first records in
  the corpus not marked verified — filter on the flag if you need the reviewed subset only.
- Five submitted rows were withheld: three with no translation supplied, and two carrying
  a stray value in an unexpected column.
- README corpus counts are updated at release, once the data is published to Hugging Face.

## [1.0.0] - 2026-08-31
- Initial public release.
