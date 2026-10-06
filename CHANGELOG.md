# Changelog

Every released version: what changed, what was corrected, what was withdrawn.

## [Unreleased]

## [1.4.0] - 2026-10-01

Adds 1,567 pairs, taking the corpus from 37,684 to 39,251.

### Added
- `yor-eng`: 1,567 pairs (`YOR-009435`-`YOR-011001`), 9,434 -> 11,001. NKENNE-owned
  content: a screenplay about Patrice Lumumba, and everyday dialogue and narrative.

### Changed
- Dataset card and `docs/known-limitations.md`: the register note now reflects the
  narrative prose and dialogue added since v1.1, rather than describing the whole corpus as
  beginner lesson content.

### Excluded from release
From the 2026-09-30 submission:
- 5 faulty rows: 2 with an empty cell, 2 incomplete translations (the Yorùbá omits part of
  the English), and 1 carrying two alternative renderings in one cell.
- 8 duplicate pairs.

## [1.3.0] - 2026-09-30

Adds 4,954 pairs from commissioned human translation, taking the corpus from
32,730 to 37,684.

### Added
- `swa-eng`: 4,954 pairs (`SWA-013687`-`SWA-018640`), 13,686 -> 18,640. The Swahili
  translation of the full Neighbours workbook: Neighbours, Farmers diary, Final Year,
  My trip to America, and My fathers new wife.

### Changed
- Ingest now also rejects cells containing non-Latin script, embedded line breaks,
  non-translation text or several alternative renderings, and rows whose length is far
  outside the sheet norm.

### Excluded from release
From the 2026-09-30 submission:
- 18 faulty rows: 8 carrying several alternative renderings in one cell, 3 with stray
  non-Latin script, 3 with line breaks inside the cell, 2 whose Swahili belonged to a
  different sentence, and 2 with an empty cell.
- 31 duplicate pairs and 1 line already live in `swa-eng`.

## [1.2.0] - 2026-09-28

Adds 7,844 pairs from commissioned human translation, taking the corpus from
24,886 to 32,730.

### Added
- `yor-eng`: 4,245 pairs (`YOR-005190`-`YOR-009434`), 5,189 -> 9,434. Includes the
  1,000 sentences never previously sent for Yorùbá (state of healthcare, Housing and
  Landlords, part of First time in Nigeria) and 652 Sheet10 sentences not yet in any
  language.
- `pcm-eng`: 3,599 pairs (`PCM-006012`-`PCM-009610`), 6,011 -> 9,610. Includes 999
  First time in Nigeria and Nigerian Cuisine sentences and 647 Sheet10 sentences that
  Pidgin had not received.

### Changed
- Ingest now admits only rows whose English exactly matches the approved source text.
- Dataset card: the automated-checks description is no longer tied to a single release,
  and the Pidgin translation-depth limitation is re-measured across all records added
  since v1.1.

### Corrected
- The dataset card said "Version 1.0", labelled its counts table "v1.0", and cited
  `version = 1.0.0` — all stale since v1.1. Now 1.2 / 1.2.0.
- The 1.1.0 entry below originally said it added 10,527 pairs from 14,359. Measured from
  the previous release (1.0.0) it added 14,523, from 10,363.

### Excluded from release
From the 2026-09-28 submissions:
- 132 rows whose English had been edited by the translator or did not come from the
  approved source (91 Yorùbá, 41 Pidgin).
- 318 Pidgin rows in a mixed sheet whose English is not from the approved source,
  313 of them raw data that failed English QA.
- 14 duplicate Yorùbá pairs; 6 untranslated and 1 empty Pidgin row.
- Whole sheets not admitted: the *When Manna Ceases* book in both languages (not approved
  for translation; still contains broken sentence splits), a Yorùbá raw-data sheet (lines
  that failed English QA plus an extract approved only conditionally), a duplicate Pidgin
  sheet, and two files whose provenance is unconfirmed.

### Notes
- Invisible characters (zero-width spaces and similar) removed from 44 Yorùbá rows.
- All text NFC. All records ship `verified: true`.

## [1.1.0] - 2026-09-22

Adds 14,523 pairs from commissioned human translation, taking the corpus from
10,363 to 24,886.

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
