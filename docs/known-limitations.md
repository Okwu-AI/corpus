# Known limitations

- **Register.** Content is everyday/beginner register: greetings, conversation, and common
  vocabulary. It suits foundational machine-translation and language-learning use, and is not
  a broad-domain or literary corpus.
- **Composition.** Includes short phrases and single-word vocabulary entries alongside full
  sentences.
- **Metadata.** Records carry text, provenance, and a validation flag. Richer per-record
  metadata (dialect, domain, register, quality tier) is supported by the schema but not
  populated in this release.
- **Validation coverage.** Records carry a `verified` flag indicating review status.
- **Yorùbá diacritics.** A minority of Yorùbá records omit the sub-dot characters
  (`ẹ`, `ọ`, `ṣ`) entirely. These are distinct letters in Yorùbá orthography rather than
  optional accents, so their absence can be ambiguous. The affected rows are concentrated
  in a single translator batch. Tone marks are not separately validated.
- **Unicode form.** All text is NFC. Yorùbá combines a dot-below with a tone mark on the
  same vowel and several such combinations have no precomposed codepoint, so consumers
  comparing strings should normalise to NFC before comparing.
- **Translation depth (Nigerian Pidgin).** Pidgin is English-lexified, so high word overlap
  with the English source is expected. Even allowing for that, roughly 340 records added in
  v1.1 sit close to the English, carrying Pidgin function words and orthography over
  otherwise English phrasing. They are genuine renderings rather than untranslated text,
  but they are thin, and they cluster in one contributed batch.

