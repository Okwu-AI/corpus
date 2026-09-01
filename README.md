# African Language Parallel Corpus & Validation Toolkit

Open parallel-text resources for Yorùbá, Swahili and Nigerian Pidgin, together with the
validation tooling and documented review process used to produce them.

**Current release:** v1.0 · **Licence:** Apache-2.0 (code) · CDLA-Permissive-2.0 (data) · CC BY 4.0 (docs) — see [LICENSING.md](LICENSING.md)

| | |
|---|---|
| Corpus | 10,363 validated pairs — Yorùbá 1,193 · Swahili 7,126 · Nigerian Pidgin 2,044 |
| Access | Hugging Face: `Okwu/african-language-parallel-corpus` |
| Citation | See `CITATION.cff` |
| Contributing | See `CONTRIBUTING.md` |
| Governance | See `GOVERNANCE.md` |

## What is here

| Path | What it is |
|---|---|
| `schema/` | The record schema, field definitions and visibility rules |
| `validation/` | Automated checks run on every contribution |
| `eval/` | Benchmark policy and held-out evaluation sets |
| `docs/` | Getting started, schema reference, validation guide, limitations |
| `release/` | Release runbook and manifest format |
| `fixtures/` | Sample records used by tests and documentation |

## Status

**Available now**
- Public versioned corpus release
- Machine-readable record schema, enforced in CI
- Automated checks: schema, Unicode normalisation, duplicate detection
- Documented contribution and review process

**Roadmap**
- Language-identity checking
- Provenance and rights classification
- Benchmark leakage checking
- Web contribution and review interface (currently handled through issues and pull requests)

## Quick start

```python
from datasets import load_dataset
ds = load_dataset("Okwu/african-language-parallel-corpus")
```

See `docs/getting-started.md` for loading, filtering and citation guidance.

## Known limitations

See `docs/known-limitations.md`. Read it before using this data in published work.
