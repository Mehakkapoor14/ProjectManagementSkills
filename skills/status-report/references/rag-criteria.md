# RAG Criteria

If the organization has defined RAG thresholds, use theirs. Otherwise apply these defaults and state in the report that default criteria were used.

## Definitions

| Rating | Meaning | Who needs to act |
|---|---|---|
| 🟢 **Green** | On track to meet committed objectives within approved tolerances. Problems exist but the team can handle them. | Team |
| 🟡 **Amber** | At risk. Tolerances are threatened or exceeded, but a credible recovery plan exists within the PM's authority. | PM, with sponsor awareness |
| 🔴 **Red** | Off track. Committed objectives will be missed without intervention, or no credible recovery plan exists within current authority. | Sponsor / steering committee decision needed |

## Default tolerances by dimension

| Dimension | Green | Amber | Red |
|---|---|---|---|
| **Schedule** | Key milestones forecast within 5% of remaining duration of baseline, or delays absorbed by float | Critical-path milestone slipping 5–10%, or float nearly consumed | Committed date (go-live, event day, contractual handover) will be missed, or slip > 10% |
| **Budget** | Forecast at completion within ±5% of approved budget | Forecast 5–10% over, or contingency more than half used with significant work left | Forecast > 10% over, or contingency exhausted |
| **Scope** | All committed deliverables expected | Some deliverables at risk, or pending change requests that would affect commitments | Committed deliverable will not be delivered, or uncontrolled scope change |
| **Quality** | Acceptance criteria being met | Defects/rework trending up; some criteria at risk | Deliverables failing acceptance; safety or compliance concern |
| **Resources** | Staffed as planned | Gaps covered by short-term workarounds | Key role vacant or critical skills unavailable with no fix in hand |

Fixed-date projects (events, regulatory deadlines, product launches tied to a season): any credible threat to the fixed date is at least Amber.

## Rules

1. **Overall rating** = the worst dimension that threatens a committed objective. A Red that is purely internal (e.g., one team's velocity) with no effect on commitments may roll up as Amber — explain why.
2. **No unsupported Green.** If the data to judge a dimension is missing, mark it "Not assessed" and list what's needed.
3. **Amber/Red must include**: cause, impact (with numbers), recovery action, owner, and date by which it should return to Green (or the decision needed).
4. **Trend** compares with the previous report: ↑ improving, → unchanged, ↓ worsening. A Green that is worsening deserves a sentence.
5. **Moving to Red is not failure** — it is the report doing its job. Early Red with a decision request beats late Red with no options left.
