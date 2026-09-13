# Rule — one command only

**Exactly one user-facing command exists: `/i-have-headache`.**

Forbidden without exception: a second command, subcommand, alias, flag,
argument, mode, setup/reset/config/helper command, interactive option, or any
alternative activation path.

Docs, rules and ADRs are not commands. Adding those is fine.

A **skill is a command**. Plugin skills appear in the slash-command palette, so
no `skills/` directory may exist in this repo. Procedures go in `.ai/`. See
[ADR-0005](../decisions/ADR-0005-no-skills-directory.md).

If asked to add an option, decline and point at
[ADR-0002](../decisions/ADR-0002-one-command-only.md). The constraint is the
product, not an oversight.
