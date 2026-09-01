# Data schema

Each record conforms to `schema/public-record.schema.json`.

| Field | Type | Description |
|---|---|---|
| `record_id` | string | Stable identifier, persists across versions |
| `source_lang` | string | ISO 639-3 code (`yor`, `swa`, `pcm`) |
| `source_text` | string | Source-language sentence or phrase |
| `source_text_normalized` | string | NFC-normalised form used for comparison |
| `english_translation` | string | English translation |
| `verified` | boolean | Human bidirectional validation |
| `source` | string | Origin of the record |
| `source_url` | string | Source URL where applicable |
| `created_at` | date | Record creation date |
