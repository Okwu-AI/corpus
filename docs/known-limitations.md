# Known limitations

- **Register.** The v1.0 core is everyday/beginner register: greetings, conversation, and
  common vocabulary. Later releases add longer narrative prose and dialogue, including short
  stories, a diary, a historical screenplay and a Christian devotional book, so sentence length
  and register vary widely across records. It is not a broad-domain corpus.
- **Composition.** Includes short phrases and single-word vocabulary entries alongside full
  sentences.
- **Metadata.** Records carry text, provenance, and a validation flag. Richer per-record
  metadata (dialect, domain, register, quality tier) is supported by the schema but not
  populated in this release.
- **Validation coverage.** Records carry a `verified` flag indicating review status.
- **Localised English (Swahili).** 1,071 `swa-eng` pairs (914 from 1.7.0, 157 from 1.8.0) use
  English that the translators rewrote with East African names, places and currency (for example
  Kelechi -> Maria, Kaduna -> Tanga, naira -> shillings). Each pair matches itself, but these lines
  will not align with the same story in Yorùbá or Pidgin. They are listed in
  [`english-exceptions.csv`](english-exceptions.csv).
- **Edited English.** 412 pairs keep English that the translator edited, usually by shortening or
  rewording the approved line, so it can differ from the same line in other languages: 21 from
  1.8.0 (20 Pidgin, 1 Yorùbá) and 391 Yorùbá from 1.9.0. They are listed in [`english-exceptions.csv`](english-exceptions.csv).
- **Yorùbá diacritics.** A minority of Yorùbá records omit the sub-dot characters
  (`ẹ`, `ọ`, `ṣ`) entirely. These are distinct letters in Yorùbá orthography rather than
  optional accents, so their absence can be ambiguous. The affected rows are concentrated
  in a single translator batch. Tone marks are not separately validated.
- **Unicode form.** All text is NFC. Yorùbá combines a dot-below with a tone mark on the
  same vowel and several such combinations have no precomposed codepoint, so consumers
  comparing strings should normalise to NFC before comparing.
- **Translation depth (Nigerian Pidgin).** Pidgin is English-lexified, so high word overlap
  with the English source is expected. Even allowing for that, roughly 900 of the 28,326
  records added since v1.1 (about 3%) sit close to the English, carrying Pidgin function
  words and orthography over otherwise English phrasing. They are genuine renderings rather
  than untranslated text, but they are thin.
