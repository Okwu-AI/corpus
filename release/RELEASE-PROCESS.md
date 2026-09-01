# Release process

Every public release follows these steps. Nothing is published outside this process.

1. **Select** accepted records. Only records in `accepted` state are eligible.
2. **Apply the rights filter.** Only records cleared for public release are included.
3. **Normalise** all text to the canonical Unicode form.
4. **Run all checks.** A release cannot be cut with a failing check.
5. **Generate the manifest** — record count per language, checksums, schema version,
   tool versions, and the ID list.
6. **Second maintainer approves.** Enforced by branch restrictions, not by convention.
7. **Tag** `vX.Y.Z` and publish. Upload the archive to Zenodo to mint a version DOI.
8. **Write the changelog entry** — what changed, what was corrected, what was withdrawn.
9. **Update `CITATION.cff`** with the new DOI.

## Corrections and withdrawals

A released record is never silently edited. Corrections are published in a new version
with a changelog entry. Withdrawn records are recorded with a public notice explaining why.

## Manifest fields
