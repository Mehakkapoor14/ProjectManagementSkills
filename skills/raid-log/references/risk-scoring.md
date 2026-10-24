# Risk Scoring Guide

Use a 1–5 scale for likelihood and impact; score = likelihood × impact (1–25). If the organization has its own matrix, use theirs instead.

## Likelihood

| Score | Label | Guide |
|---|---|---|
| 1 | Rare | < 10% chance; no precedent |
| 2 | Unlikely | 10–30%; has happened elsewhere |
| 3 | Possible | 30–50%; plausible given current conditions |
| 4 | Likely | 50–80%; warning signs present |
| 5 | Almost certain | > 80%; would be surprising if it didn't happen |

## Impact

Rate against the dimension hit hardest. Scale the thresholds to project size: a 2-week delay is minor on a 3-year build but severe on a 6-week event.

| Score | Label | Schedule | Cost | Scope / quality | Safety / reputation / compliance |
|---|---|---|---|---|---|
| 1 | Negligible | < 1% slip | < 1% of budget | Cosmetic | None |
| 2 | Minor | 1–5%, absorbed by float | 1–5% | Minor rework | Internal only |
| 3 | Moderate | 5–10%, milestone at risk | 5–10% | Noticeable shortfall that sponsor must accept | Customer complaint, minor non-compliance |
| 4 | Major | 10–20%, key date missed | 10–20% | Key objective not met | Public or regulator attention; injury requiring treatment |
| 5 | Severe | > 20%, or a fixed date missed (event day, regulatory deadline) | > 20% | Project fails its purpose | Serious injury, legal action, major reputational damage |

Safety and legal/regulatory risks: treat impact ≥ 4 as needing escalation regardless of likelihood.

## Rating bands

| Score | Rating | Expected handling |
|---|---|---|
| 15–25 | **High** (red) | Active response plan, sponsor visibility, review weekly |
| 8–14 | **Medium** (amber) | Response plan with owner and date, review every 2 weeks |
| 1–7 | **Low** (green) | Monitor; review monthly |

## Heat map (likelihood rows × impact columns)

```
            Impact →   1    2    3    4    5
Likelihood 5           5   10   15   20   25
           4           4    8   12   16   20
           3           3    6    9   12   15
           2           2    4    6    8   10
           1           1    2    3    4    5
```
In a summary, place risk IDs in their cells.

## Response strategies

**Threats**
- **Avoid** — change the plan to remove the cause (different supplier, drop the risky feature, move the date).
- **Mitigate** — reduce likelihood or impact (extra inspection, backup venue on hold, early prototype).
- **Transfer** — shift the financial impact (insurance, fixed-price contract, warranty, penalty clause).
- **Accept** — consciously take it; for meaningful risks, set aside contingency and define a trigger.
- **Escalate** — outside the project's authority; hand it to the sponsor/program and record who accepted it.

**Opportunities** (positive risks)
- **Exploit** — make sure it happens. **Enhance** — raise its likelihood or benefit. **Share** — partner with someone better placed to capture it. **Accept** — take it if it comes.

## Good vs. weak entries

| Weak | Better |
|---|---|
| Supplier delays | Because our only steel supplier is quoting 12-week lead times (cause), structural steel may arrive after the 15 March erection start (event), delaying topping-out by up to 4 weeks and adding crane hire costs (effect). |
| Weather | Because the outdoor ceremony has no covered alternative (cause), heavy rain on 14 June (event) would force a same-day relocation and degrade guest experience (effect). |
| Response: monitor | Response (mitigate): reserve marquee with a 72-hour cancellation option by 1 May — owner: J. Ortiz. |
