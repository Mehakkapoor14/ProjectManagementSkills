# ProjectManagementSkills

Project management skills for AI agents (Claude Code, Pi, and other agents that support the `SKILL.md` Agent Skills format). They are domain-agnostic: built for project managers in construction, events, marketing, research, healthcare, nonprofits, operations, and IT alike.

## Skills

| Skill | What it does |
|---|---|
| [project-charter](skills/project-charter/) | Drafts a charter / project brief: objectives, scope in/out, milestones, budget, stakeholders, risks, governance |
| [meeting-to-actions](skills/meeting-to-actions/) | Turns transcripts or notes into minutes with decisions, owned and dated action items, open questions, and risks |
| [raid-log](skills/raid-log/) | Creates, scores, and reviews a Risks / Assumptions / Issues / Dependencies log with a 5×5 heat map |
| [status-report](skills/status-report/) | Writes status reports with honest RAG ratings, milestone variance, top risks, and decisions needed |
| [schedule-planning](skills/schedule-planning/) | Builds schedules with dependencies, critical path, and float; exports CSV and a Mermaid Gantt chart |

### Planned

scope-and-wbs · stakeholder-communication (RACI, power/interest) · change-control · estimation · budget-and-evm · resource-capacity-planning · procurement-vendor-management · lessons-learned-and-closure · decision-analysis · prioritization · agile-delivery · methodology-tailoring · organizational-change-management · project-health-check-recovery · quality-management

## How the skills work together

Skills share a `pm/` folder in the user's project, so each one can build on the others' output:

```
pm/
├── charter.md            project-charter
├── tasks.csv             schedule-planning (input)
├── schedule.csv          schedule-planning (calculated)
├── gantt.md              schedule-planning (Mermaid chart)
├── raid-log.csv          raid-log
├── meetings/YYYY-MM-DD-<topic>.md   meeting-to-actions
└── status/YYYY-MM-DD.md  status-report
```

A typical flow: **charter → schedule → RAID log → (meetings) → status reports**. Every skill also works on its own with whatever the user pastes in.

Outputs are Markdown, CSV, and Mermaid, so they open in Excel/Google Sheets and import into MS Project, Smartsheet, Asana, Monday, or Jira.

## Installation

**Claude Code** — copy (or symlink) the skill folders into a skills directory:

```bash
# for all your projects
cp -r skills/* ~/.claude/skills/
# or for a single project
mkdir -p .claude/skills && cp -r /path/to/ProjectManagementSkills/skills/* .claude/skills/
```

**Pi and other Agent Skills–compatible agents** — copy the folders under `skills/` into the agent's skills directory (see your agent's documentation for the location).

`schedule-planning` includes `scripts/cpm.py`, which needs only Python 3 (no packages).

## Skill layout

```
skills/<skill-name>/
├── SKILL.md       frontmatter (name, description) + instructions
├── templates/     output templates
├── references/    detail loaded only when needed
└── scripts/       deterministic helpers
```
