# Getting started

## Load the corpus

```python
from datasets import load_dataset

ds = load_dataset("Okwu/african-language-parallel-corpus", "swa-eng")
```

Configurations: `yor-eng`, `swa-eng`, `pcm-eng`.

## Fields

Each record has `record_id`, `source_lang`, `source_text`, `source_text_normalized`,
`english_translation`, `verified`, `source`, `source_url`, and `created_at`.
See [data-schema.md](data-schema.md).

## Citation

See [licensing-and-citation.md](licensing-and-citation.md) and `CITATION.cff`.
