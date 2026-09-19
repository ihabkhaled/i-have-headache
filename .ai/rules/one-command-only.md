# Rule — one command only

**Exactly one user-facing command exists: `/i-have-headache`.**

Forbidden without exception: a second command, subcommand, alias, flag,
argument, mode, setup/reset/config/helper command, interactive option, or any
alternative activation path.

Docs, rules and ADRs are not commands. Adding those is fine.

A **skill is a command**: plugin skills appear in the slash-command palette.
Exactly one skill exists, `skills/i-have-headache/`, and it *is* the command —
there is no `commands/` directory and no Codex prompt. Never add a second skill,
a command file or a prompt file: each is a second entry. Concise mode is always
on ([ADR-0006](../decisions/ADR-0006-always-on-one-source.md)); the command only
re-asserts it. Procedures go in `.ai/` as documents. See
[ADR-0005](../decisions/ADR-0005-no-skills-directory.md).

If asked to add an option, decline and point at
[ADR-0002](../decisions/ADR-0002-one-command-only.md). The constraint is the
product, not an oversight.
