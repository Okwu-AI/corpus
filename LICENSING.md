# Licensing

Open by default. Everything this project releases is openly licensed, under three licences:

| What | Licence | SPDX | Full text |
|---|---|---|---|
| Code, tooling and the JSON schema | Apache-2.0 | `Apache-2.0` | [`LICENSE`](LICENSE) |
| Data (sentence pairs and their metadata) | CDLA-Permissive-2.0 | `CDLA-Permissive-2.0` | [`LICENSE-DATA`](LICENSE-DATA) |
| Documentation and dataset cards | CC BY 4.0 | `CC-BY-4.0` | [`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt) |

## Code and tooling: Apache-2.0
The validation toolkit, evaluation harness, release tooling and the JSON schema
(`schema/public-record.schema.json`) are licensed under Apache-2.0.

Rationale: a permissive licence with an explicit patent grant, universally accepted, that
places no barrier on adoption by researchers, institutions, or industry.

## Data: CDLA-Permissive-2.0
All released sentence pairs and their metadata are licensed under the Community Data
License Agreement – Permissive, Version 2.0.

You may use, modify and share the data, including commercially. The one condition: if you
share the data, with or without changes, make the text of the agreement available with it.
The agreement places no restrictions on results, such as models trained on the data.

CDLA-Permissive-2.0 does not require attribution. We ask that you cite the corpus (see
[Citation](#citation)).

Rationale: CDLA-Permissive-2.0 is the Linux Foundation's permissive licence built
specifically for data. Unlike licences designed for creative works, it is purpose-built for
datasets, avoiding ambiguity about how copyright applies to factual records. It is
SPDX-registered and loads natively on major dataset platforms.

## Documentation: CC BY 4.0
Okwu documentation © 2026 ESM Global Productions LLC, licensed under
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)
(CC BY 4.0).

This covers the Markdown documentation in this repository (including `README.md`, `docs/`,
`schema/*.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `GOVERNANCE.md` and `SECURITY.md`) and
the dataset card on Hugging Face. Each covered file ends with this licence notice.

**How to credit it.** If you reuse or adapt the documentation, give credit, link to the
licence, and say whether you made changes. For example:

> Adapted from the Okwu documentation (https://github.com/Okwu-AI/corpus),
> © 2026 ESM Global Productions LLC, licensed under CC BY 4.0
> (https://creativecommons.org/licenses/by/4.0/). Changes: [describe your changes].

Do not suggest that Okwu endorses you or your use, and do not add terms or technical
measures that restrict what the licence allows.

## Not covered
- **Third-party material.** `CODE_OF_CONDUCT.md` is adapted from the
  [Contributor Covenant](https://www.contributor-covenant.org), version 2.1, which its
  authors license under CC BY 4.0; its own attribution section applies. The licence texts
  (`LICENSE`, `LICENSE-DATA`, `LICENSES/`) keep their own terms.
- **Names and logos.** The Okwu and NKENNE names and logos are not licensed under any of
  these licences.

## Contributions
By contributing, you license what you contribute under the licence for its kind: code under
Apache-2.0, data under CDLA-Permissive-2.0 and documentation under CC BY 4.0. See
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Citation
Cite the corpus using [`CITATION.cff`](CITATION.cff), giving the version you used. Citation
of the data is requested, not required by its licence. Credit for the documentation is
required by CC BY 4.0, as described above.

## Data governance
Governance follows the CARE Principles for Indigenous Data Governance alongside FAIR,
ensuring the communities whose languages are represented share in the benefit and retain
a voice in how the data is stewarded.

## Scope boundary
These open licences cover the public ecosystem only — released data, schemas,
documentation, benchmarks, validation utilities, and contribution infrastructure.
Proprietary commercial assets (model weights, commercial APIs, customer data, and
confidential training methods) are separate and are not covered here.

---

Okwu documentation © 2026 ESM Global Productions LLC, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
