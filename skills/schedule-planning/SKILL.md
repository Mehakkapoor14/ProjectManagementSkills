---
name: schedule-planning
description: Build or update a project schedule — break work into tasks, estimate durations, set dependencies, compute the critical path and float, place milestones, and produce a Gantt chart and importable task list. Use whenever the user wants a project plan, timeline, schedule, Gantt chart, work plan, roadmap with dates, critical path, "when can we finish", "what happens if X slips", "backward plan from the event date", or needs a task list for MS Project, Smartsheet, Excel, Asana, Monday, or Jira — in any field (construction, events, campaigns, research, moves, launches, IT), even if they only describe the goal and deadline.
---

# Schedule Planning

A good schedule answers three questions: *when will we finish*, *which tasks control that date* (the critical path), and *how much slack does everything else have* (float). Don't compute critical paths by hand — use the bundled script, because dependency arithmetic is where hand-built schedules quietly go wrong.

## Workflow

1. **Collect constraints.** Start date or required finish date (backward planning from an event or deadline is common), working calendar (Mon–Fri by default; ask about holidays, shutdowns, or weekend work in construction/events), and fixed dates (permits, venue access, board meetings). Check `pm/charter.md` for milestones and deadline if it exists.

2. **Break down the work.** Decompose deliverables into tasks of roughly 1–10 working days (shorter for short projects). Each task should have a clear finish ("Floor plan approved", not "Work on floor plan"). Include the things non-experts forget:
   - Approvals, reviews, and sign-offs (they take calendar time)
   - Supplier and procurement lead times
   - Permits, inspections, legal or compliance checks
   - Testing, rehearsal, snagging/punch-list, and handover
   - Communication and training for the people affected

   Group tasks into phases. Mark milestones as zero-duration tasks.

3. **Estimate durations.** Use the user's numbers where given. Otherwise propose estimates and label them as assumptions. For uncertain tasks, use three-point (PERT) estimates: (optimistic + 4 × most likely + pessimistic) / 6, and keep the range in notes.

4. **Set dependencies.** Default is finish-to-start (FS). Use start-to-start (SS) with lag for overlapping work and finish-to-finish (FF) where two things must end together. Every task except the first should have a predecessor, and every task except the last should have a successor — dangling tasks hide schedule risk.

5. **Run the calculation.** Write the tasks to a CSV and run:
   ```bash
   python3 scripts/cpm.py pm/tasks.csv --start YYYY-MM-DD [--holidays YYYY-MM-DD,...] \
     --out pm/schedule.csv --gantt pm/gantt.md --title "Project name"
   ```
   (Run with the script path relative to this skill's directory.) Input columns: `id,name,duration,predecessors` plus optional `owner,phase,not_before` (`not_before` is a YYYY-MM-DD start-no-earlier-than date for fixed constraints like permit approval or venue access). Predecessor syntax: `A`, `A;B`, `A:SS+2`, `A:FF`, `A:FS-1`. The script reports early/late dates, float, critical tasks, finish date, and catches loops and unknown IDs. It only needs Python 3 with no extra packages.

   For backward planning, run with a trial start date, compare the finish with the deadline, and shift the start by the difference (or compress the plan — see step 6).

6. **Sanity-check and optimize.**
   - Does the finish date meet the deadline? If not, propose options in order of typical cost: remove or re-sequence dependencies (**fast-tracking**: overlap tasks, which adds risk), add resources to critical tasks (**crashing**, which adds cost), reduce scope, or move the date.
   - Is the critical path plausible? If it runs through something trivial, a dependency is probably wrong.
   - Are any people assigned to overlapping critical tasks? Flag over-allocation.
   - Add contingency explicitly (as a buffer task before key milestones) rather than padding every task.

7. **Present.** Show the finish date, the critical tasks, the milestones table, the Mermaid Gantt (`pm/gantt.md` renders on GitHub, in many Markdown viewers, and at mermaid.live), and the key assumptions. Mention the biggest schedule risks so they can go into the RAID log.

## Updating an existing schedule

Load `pm/tasks.csv`, apply actual progress (for completed tasks set duration to actual and note it; for in-progress tasks set `duration` to the remaining work and `not_before` to the status date; do the same for not-yet-started tasks whose predecessors are all complete), rerun, and report what moved: new finish date, changes in critical path, and milestones that slipped versus the previous run. Keep the original as the baseline (`pm/schedule-baseline.csv`) the first time you update, so variance can be reported.

## Export

- `pm/schedule.csv` imports into Excel, Google Sheets, and Smartsheet, and maps easily to MS Project (Name, Duration, Start, Finish, Predecessors) and to Asana, Monday, or Jira CSV importers.
- If the user needs an .xlsx or .mpp-compatible file, generate from the CSV with whatever tooling is available.

## Connects to

- **project-charter** — milestones and deadline.
- **raid-log** — risks on critical-path tasks; dependencies on external parties.
- **status-report** — baseline vs. forecast milestone dates.
