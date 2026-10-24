---
name: raid-log
description: Create, update, score, and review a RAID log — Risks, Assumptions, Issues, Dependencies (and Decisions) — including probability × impact scoring, owners, response plans, and a heat-map summary. Use whenever the user mentions risks, a risk register, issue log, "what could go wrong", blockers, dependencies, assumptions, escalations, a pre-mortem, or wants to log something from a meeting or status update — in any field (construction, events, healthcare, marketing, research, IT, operations) — even if they just say "add this to the risks" or paste a list of concerns.
---

# RAID Log

The RAID log is a project's early-warning system. It only works if entries are specific, owned, and current. A vague risk ("budget issues") with no owner is just anxiety on paper. Your value is turning concerns into well-formed, scored, owned entries with real responses, and keeping the log honest over time.

## The four (five) types

| Type | Definition | Key question |
|---|---|---|
| **Risk** | Uncertain future event that would affect objectives (threat or opportunity) | What *might* happen? |
| **Assumption** | Something treated as true for planning but not yet confirmed | What are we betting on? |
| **Issue** | Something that *is* happening now and needs action | What's already wrong? |
| **Dependency** | Something this project needs from outside (or another project needs from it) | Who/what are we waiting on? |
| **Decision** *(optional D)* | A significant choice made, with rationale | Why did we choose this? |

Classify carefully: a risk that has occurred becomes an issue (close the risk, open a linked issue). A false assumption usually becomes an issue or a new risk.

## Workflow

1. **Load the existing log.** Default location is `pm/raid-log.csv`. If it exists, update it in place — never discard history. If not, create it from `templates/raid-log.csv`.

2. **Write each entry well.**
   - Risks use *cause → event → effect*: "Because the venue contract is unsigned (cause), we may lose the booking to another client (event), forcing a date change and reprinting invitations (effect)."
   - Issues state the impact now and what is needed.
   - Dependencies name the provider, what is needed, and the need-by date.
   - Assumptions name how and by when they'll be validated.

3. **Score risks** using `references/risk-scoring.md` (1–5 likelihood × 1–5 impact). Read it the first time you score in a session. Base scores on stated evidence; if you're inferring, say so in the notes so the user can adjust. Issues get a priority (Critical/High/Medium/Low) rather than a likelihood.

4. **Assign an owner and response.** Every open entry needs one named owner and a next action with a date. If no owner is known, mark `UNASSIGNED` and flag it — don't guess. Pick a response strategy (see the reference) and write a concrete action, not "monitor" alone, for anything scoring 10+.

5. **Review mode.** When asked to review the log or prepare for a status meeting:
   - Flag stale entries (no update in 14+ days or past their review/need-by date).
   - Flag risks whose trigger appears to have happened (convert to issues).
   - Flag dependencies past need-by date and assumptions never validated.
   - Produce a summary: counts by type and status, top 5 risks by score, a 5×5 heat map (text grid is fine), and items needing escalation.

6. **Report changes.** After editing, tell the user which IDs were added, changed, or closed, so they can sanity-check.

## Conventions

- IDs: `R-001`, `A-001`, `I-001`, `D-001` (dependency), `DEC-001` (decision). Never reuse IDs.
- Status: `Open`, `In progress`, `Closed`, plus `Occurred` for risks that became issues.
- Dates: ISO `YYYY-MM-DD`.
- Close rather than delete, with a closing note — the history is useful for lessons learned.

## Output

The CSV is the source of truth (it opens in Excel, Google Sheets, Smartsheet, Jira imports). When the user wants to read or present it, also render a Markdown view or summary. If the user keeps their log elsewhere (Excel, a database, a PM tool), follow their format and columns instead.

## Connects to

- **project-charter** — initial risks and assumptions come from there.
- **meeting-to-actions** — new risks/issues raised in meetings land here.
- **status-report** — the top risks and issues feed the status report.
- **schedule-planning** — risks on critical-path tasks matter most; check float when assessing schedule impact.
