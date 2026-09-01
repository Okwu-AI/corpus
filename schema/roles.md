# Roles and permissions


| Capability | Public | Contributor | Reviewer | Maintainer | Governance | Admin |
|---|---|---|---|---|---|---|
| Browse catalogue, read docs | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Download a release | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| See public record fields | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| See reviewer-only fields | — | — | ✅ | ✅ | — | ✅ |
| Report an error | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Submit a contribution | — | ✅ | ✅ | ✅ | — | ✅ |
| See own submissions | — | ✅ | ✅ | ✅ | — | ✅ |
| Review assigned records | — | — | ✅ | ✅ | — | ✅ |
| Escalate a disagreement | — | — | ✅ | ✅ | — | ✅ |
| Adjudicate an escalation | — | — | — | ✅ | — | ✅ |
| Assign reviewers | — | — | — | ✅ | — | ✅ |
| Cut a release | — | — | — | ✅ (2 needed) | — | ✅ |
| Withdraw or retract | — | — | — | ✅ | — | ✅ |
| See audit log | — | — | — | ✅ | — | ✅ |
| See ecosystem metrics | partial | partial | ✅ | ✅ | ✅ | ✅ |
| Change roles / permissions | — | — | — | — | — | ✅ |

## Notes
- "2 needed" on release = a second-maintainer approval, enforced by branch protection, not app logic.
- Governance participant is deliberately read-heavy: visibility, not operational power.
- V1 identity: **GitHub OAuth**. Free, no user database, and contributors already have accounts. Revisit if non-technical contributors need a path that avoids GitHub.
