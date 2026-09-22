# Changelog

Every released version: what changed, what was corrected, what was withdrawn.

## [Unreleased]

## [1.1.0] - 2026-09-22

Adds 10,527 pairs from commissioned human translation, taking the corpus from
14,359 to 24,886.

### Added
- `yor-eng`: 3,996 pairs (`YOR-001194`-`YOR-005189`), 1,193 -> 5,189.
- `swa-eng`: 6,560 pairs (`SWA-007127`-`SWA-013686`), 7,126 -> 13,686.
- `pcm-eng`: 3,967 pairs (`PCM-002045`-`PCM-006011`), 2,044 -> 6,011.

### Changed
- Dataset card now documents the automated release checks (schema, NFC, duplicates)
  that run in addition to bidirectional human validation.
- Card gains two limitations: Nigerian Pidgin translation depth, and Yorùbá diacritics.

### Removed
- `data/yor-eng/okwu-portal-2026-09-20T08-32-59.csv`, a portal export holding a single
  placeholder test record that was being served as part of `yor-eng`.

### Excluded from release
142 submitted rows were withheld rather than published:
- 94 Swahili sentences broken mid-way by an upstream splitting error. The English was
  split on line endings instead of sentence boundaries, so translators received half
  sentences. Concatenating the halves does not repair them — Swahili noun-class
  agreement propagates across the break, so the second half was translated against a
  guess about the first.
- 26 Nigerian Pidgin rows left in English.
- 12 duplicates, 3 rows where Pidgin had leaked into the English source column, and
  2 untranslated Swahili rows.
- 5 Yorùbá rows: three with no translation supplied, two carrying a stray value in an
  unexpected column. 21 exact duplicate Yorùbá pairs were also removed.

### Notes
- All records ship `verified: true`.
- Source text is NFC throughout; 515 Yorùbá values were re-normalised on ingest.
- Roughly 340 Pidgin records sit close to the English source. They are genuine
  renderings rather than untranslated text, but thin, and cluster in one batch.
- 45 Yorùbá records omit the sub-dot characters entirely; see `docs/known-limitations.md`.

## [1.0.0] - 2026-08-31
- Initial public release.
