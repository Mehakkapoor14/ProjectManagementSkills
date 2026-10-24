---
name: status-report
description: Write project status reports and executive updates with an honest RAG (red/amber/green) rating, progress against plan, milestones, budget, top risks and issues, decisions needed, and next-period priorities. Use whenever the user asks for a status report, weekly/monthly update, progress report, steering committee or board update, sponsor/client update, highlight report, "where are we", "write the update for leadership", or "how do I report this delay" — in any field (construction, events, marketing, research, healthcare, nonprofit, IT) — even if they only give scattered notes, a task list, or a spreadsheet export.
---

# Status Report

A status report exists so a busy decision-maker can tell, in under a minute, whether the project is on track and whether they need to act. The two classic failures are **watermelon reporting** (green outside, red inside — optimism hiding problems until it's too late) and **activity lists** (a log of what people did, with no statement of whether that's enough). Write for the reader's decisions, not the team's effort.

## Workflow

1. **Gather sources.** Use what the user provides plus, if present in the workspace: `pm/charter.md` (objectives, milestones, budget), `pm/schedule.csv` (plan dates, critical path), `pm/raid-log.csv` (top risks/issues), the previous report in `pm/status/`, and recent `pm/meetings/` minutes. Comparing to last period's report is what lets you show trend and catch quietly slipping dates.

2. **Establish period and audience.** Reporting date, period covered, and who reads it (sponsor, steering committee, client, team). Executives get one page; teams can get more detail. Ask only if it changes the output materially; otherwise default to a one-page sponsor report.

3. **Rate RAG per dimension** — overall, schedule, budget, scope, and (if relevant) quality, resources, or safety — using `references/rag-criteria.md`. Read it before rating. Rules that matter:
   - The overall rating can't be greener than the worst dimension that threatens a committed objective.
   - Every Amber or Red needs a stated cause, a recovery action, and an owner.
   - If data is missing to judge a dimension, write "Not assessed — [what's missing]" rather than defaulting to green.
   - Show trend vs. last period (↑ improving, → stable, ↓ worsening) when a previous report exists.

4. **Write using `templates/status-report.md`.** Lead with the executive summary: 2–4 sentences stating the overall status, the single most important thing, and any decision needed. Then milestones (planned vs. forecast dates, with variance), accomplishments that matter against the plan, next period priorities, top risks/issues (max 5), and decisions/help needed.

5. **Be quantitative where possible.** "Milestone 3 forecast 12 Mar vs. baseline 28 Feb (+9 working days)" beats "slightly delayed". "€412k spent of €600k (69%) at 60% complete" beats "budget on track". If percent-complete is subjective, say how it was estimated.

6. **Check the tone.** Neutral and factual, no blame, no spin. Bad news early and plainly, with what's being done about it. If you think the user's own proposed rating is too optimistic given the facts, say so and explain why — that's the most valuable thing you can do for them.

## Output

Save as `pm/status/YYYY-MM-DD.md` when a workspace is in use. If the user needs an email or chat message, also produce a condensed version (summary + RAG + decisions needed). Adapt headings to an organization's required format if they have one (e.g., PRINCE2 highlight report).

## Connects to

- **raid-log** — top risks and issues come from there; new ones found while writing go back into it.
- **schedule-planning** — forecast dates and critical-path slippage.
- **meeting-to-actions** — decisions and overdue actions.
- **project-charter** — objectives and success criteria define what "on track" means.
