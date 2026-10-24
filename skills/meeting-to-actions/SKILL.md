---
name: meeting-to-actions
description: Turn meeting transcripts, recordings' text, rough notes, or chat threads into clean minutes with decisions, action items (owner + due date), open questions, and risks. Use whenever the user shares or mentions meeting notes, a transcript, a call summary, standup/steering/kickoff/site/client meeting output, or asks "what did we agree", "who's doing what", "write up the minutes", "send a recap", or "extract action items" — in any field (construction site meetings, event planning calls, board meetings, client workshops, sprint ceremonies), even when the notes are messy or partial.
---

# Meeting to Actions

Meetings produce value only through what happens afterwards: decisions that stick and actions that get done. The usual failure is ambiguity — "someone will look into it", "early next week", a decision implied but never stated. Your job is to convert discussion into unambiguous commitments and to flag where the meeting left things unresolved.

## Workflow

1. **Read the whole input first.** Transcripts circle back; a decision at minute 5 may be reversed at minute 40. Capture the final position, and note the reversal only if it matters.

2. **Extract into four buckets:**
   - **Decisions** — something was agreed that changes what people will do. State it as a complete sentence a non-attendee can understand, with who made or approved it.
   - **Action items** — a person committed (or was assigned) to do something. Each needs: action (starts with a verb), owner (one named person, not a team), due date, and context if needed.
   - **Open questions / parking lot** — raised but not resolved. Say who will resolve it if anyone said so.
   - **Risks and issues** — anything that threatens schedule, budget, quality, safety, or relationships. These feed the RAID log.

3. **Resolve ambiguity honestly.**
   - Relative dates ("Friday", "next week") → convert to absolute dates using the meeting date. If the meeting date is unknown, ask or write `Fri (date TBC)`.
   - Missing owner → write `Owner: UNASSIGNED` and list it under "Needs follow-up". Do not guess an owner; a wrongly assigned action gets silently dropped.
   - "We should…" with no commitment is not an action. Put it in open questions unless someone accepted it.
   - Speaker labels like "Speaker 2" — keep them as-is and ask the user to map names rather than guessing.

4. **Write the minutes** using `templates/minutes.md`. Keep the discussion summary short (bullets per topic, outcomes over narration). Readers skim for their name and the decisions.

5. **Offer follow-ons** where useful: a short recap email/message ready to paste, new risks to add to `pm/raid-log.md`, or actions in CSV for import into a task tool.

## Style

- Neutral and factual; attribute positions only when it matters for accountability ("Finance objected to the cost").
- Leave out sensitive personal remarks, side conversations, and off-topic chatter.
- Match the user's field vocabulary (RFIs and snag lists on a construction site, run-of-show on an event).

## Output

Save to `pm/meetings/YYYY-MM-DD-<topic>.md` when a workspace is in use, otherwise return in chat. For action CSV export use columns: `id,action,owner,due_date,status,source_meeting`.

## Connects to

- **raid-log** — new risks, issues, decisions, and dependencies go there.
- **status-report** — completed and overdue actions inform the weekly status.
