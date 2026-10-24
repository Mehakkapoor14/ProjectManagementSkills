---
name: project-charter
description: Draft a project charter (or project initiation document / project brief) that defines why a project exists, what it must achieve, its scope boundaries, constraints, sponsor, and how success is judged. Use whenever someone is starting, kicking off, proposing, or formally authorizing a project in any field — construction, events, marketing campaigns, research, nonprofit programs, product launches, office moves, IT — or asks for a "charter", "PID", "project brief", "one-pager", "kickoff doc", "business case summary", or "scope statement", even if they only paste rough notes or an email describing the idea.
---

# Project Charter

A charter is the document a sponsor signs to say "yes, spend resources on this." Its job is alignment: everyone agrees on the *why*, the *what*, and the *boundaries* before work starts. Most project failures trace back to fuzzy objectives or unstated scope, so the value you add is making those sharp and surfacing what's missing — not producing a long document.

## Workflow

1. **Gather what exists.** Read whatever the user provided (notes, emails, proposals). If a `pm/` folder exists in the workspace, check for an existing `pm/charter.md` to update rather than replace.

2. **Check the critical inputs.** A charter without these is not useful, so ask for any that are missing — in one short batch, not one at a time:
   - The problem or opportunity (why now?)
   - Sponsor (who authorizes and owns the business outcome) and project manager
   - Target deadline or key date, and budget if known
   - What "done" looks like

   If the user wants a draft immediately, proceed and mark gaps as `TBD — [question to answer]` rather than inventing facts. Invented budgets or dates get copied into later plans and become false commitments.

3. **Draft using the template** in `templates/project-charter.md`. Fill every section; delete a section only if it truly doesn't apply and say so.

4. **Sharpen objectives.** Rewrite vague goals into measurable ones (SMART: specific, measurable, achievable, relevant, time-bound). "Improve donor engagement" → "Increase repeat donors from 18% to 25% by 30 June 2027." If you can't make it measurable without guessing a number, keep the structure and flag the number as TBD.

5. **Make scope explicit both ways.** The *out of scope* list prevents more disputes than the in-scope list. Add likely misunderstandings a stakeholder might assume are included (e.g., for an office move: "IT hardware refresh is out of scope").

6. **Surface initial risks and assumptions.** List 3–7 of each. Assumptions are things being treated as true that could turn out false ("venue capacity permits 400 seated guests"). These seed the RAID log.

7. **Review and report.** End with a short list of open questions and decisions the sponsor needs to make before signing.

## Writing guidance

- Aim for 1–3 pages. Executives read the summary and objectives; keep those crisp.
- Use the vocabulary of the user's field (a construction charter talks about permits, site access, and handover; an event charter talks about attendance, venue, run-of-show).
- Success criteria must be checkable by someone outside the team at closure.
- Milestones here are high-level (5–10). Detailed scheduling belongs to the schedule-planning skill.
- Choose a project ID/short name if none exists; later documents reference it.

## Output

Save as `pm/charter.md` unless the user specifies another location or format. If they want Word/PDF, produce Markdown first, then convert with whatever document tooling is available.

## Connects to

- **raid-log** — seed it with the charter's risks, assumptions, and dependencies.
- **schedule-planning** — the milestones and deadline are its starting constraints.
- **status-report** — the objectives and success criteria are what status is measured against.
