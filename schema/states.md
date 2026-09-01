# Submission state machine

The submission lifecycle uses these states:

*draft, submitted, needs changes, in review, accepted, rejected, withdrawn, released*


| State | Means | Who sets it | Can go to |
|---|---|---|---|
| `draft` | Contributor started, not sent | contributor | `submitted`, deleted |
| `submitted` | Sent, waiting for automated checks | contributor | `checks_failed`, `in_review` |
| `checks_failed` | Automated checks rejected it | system | `draft`, `withdrawn` |
| `in_review` | A reviewer is assigned and looking | system / maintainer | `accepted`, `rejected`, `needs_changes`, `escalated` |
| `needs_changes` | Reviewer sent it back with feedback | reviewer | `submitted`, `withdrawn` |
| `escalated` | Reviewers disagreed, needs adjudication | reviewer | `accepted`, `rejected` |
| `accepted` | Approved, waiting for a release | reviewer / adjudicator | `released`, `withdrawn` |
| `rejected` | Declined, with a reason | reviewer / adjudicator | terminal |
| `withdrawn` | Pulled by contributor or maintainer | contributor / maintainer | terminal |
| `released` | Published in a versioned release | maintainer | `corrected`, `retracted` |
| `corrected` | Changed after release, changelog entry exists | maintainer | `released` |
| `retracted` | Removed after release, notice published | maintainer | terminal |
