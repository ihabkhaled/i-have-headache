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
| [0004](decisions/ADR-0004-cursor-shares-the-command-directory.md) | Cursor reuses `commands/` instead of getting a copy |
| [0005](decisions/ADR-0005-no-skills-directory.md) | Exactly one skill, named as the command |
| [0006](decisions/ADR-0006-always-on-one-source.md) | Always on; the skill is the only copy of the text |
| [0007](decisions/ADR-0007-simple-code-same-skill.md) | Simple-first code belongs in the same skill and command |
| [0008](decisions/ADR-0008-right-sized-clean-code.md) | Match architecture and refactoring depth to the real task |
| [0009](decisions/ADR-0009-prompt-submit-reminder-hook.md) | One-line reminder on every prompt (UserPromptSubmit) |
| [0010](decisions/ADR-0010-version-discipline-in-the-one-skill.md) | Version discipline is a script in the one skill |

## Rules

| Rule | Enforces |
|---|---|
| [be-concise.md](rules/be-concise.md) | Concise output and right-sized clean code |
| [one-command-only.md](rules/one-command-only.md) | ADR-0002 |
| [no-second-source-of-truth.md](rules/no-second-source-of-truth.md) | ADR-0001 |
| [version-discipline.md](rules/version-discipline.md) | ADR-0010 |

## Procedures

| Procedure | Where |
|---|---|
| Editing the command text (one file: the skill) | [technical-logic.md](technical-logic.md#always-on-per-platform) |
| Regenerating the logo | `python assets/make_logo.py` |
| Releasing | [version-discipline.md](rules/version-discipline.md) |
| Tests | `python -m pytest tests -q` |

The [wiki](../docs/wiki/index.md) holds the rest; [changes](../docs/changes/) holds one record per change.

Procedures are documents, not skills. A plugin skill is a slash command, and
this plugin ships one — see [ADR-0005](decisions/ADR-0005-no-skills-directory.md).
