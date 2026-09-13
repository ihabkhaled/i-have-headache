# Knowledge layer

Start at [AGENTS.md](../AGENTS.md). This directory holds the detail behind it.

| Path | What is in it |
|---|---|
| [business-logic.md](business-logic.md) | Why this exists, who for, what it refuses to do |
| [technical-logic.md](technical-logic.md) | How it works, packaging, what breaks it |
| [context/repo-map.md](context/repo-map.md) | Every file and where to look for what |
| [memory.md](memory.md) | Durable notes and their reversal conditions |

## Decisions

| ADR | Subject |
|---|---|
| [0001](decisions/ADR-0001-agents-md-canonical.md) | AGENTS.md canonical, other agent files are pointers |
| [0002](decisions/ADR-0002-one-command-only.md) | Exactly one user-facing command, permanently |
| [0003](decisions/ADR-0003-duplicate-command-body.md) | Duplicate the command body rather than generate it |

## Rules

| Rule | Enforces |
|---|---|
| [be-concise.md](rules/be-concise.md) | The headache rule |
| [one-command-only.md](rules/one-command-only.md) | ADR-0002 |
| [no-second-source-of-truth.md](rules/no-second-source-of-truth.md) | ADR-0001 |

## Skills

| Skill | Use when |
|---|---|
| [sync-command-bodies](../skills/sync-command-bodies/SKILL.md) | Editing the command text, or platforms behave differently |
