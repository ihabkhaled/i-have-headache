# Agent instructions

See [AGENTS.md](AGENTS.md). It is the single source of truth for this
repository and applies to every AI agent without exception.

Three rules that matter before you read anything else:

1. The maintainer has a headache — do not talk too much. Shortest complete
   answer, always.
2. Exactly one user-facing command exists, `/i-have-headache`. Never add a
   second command, alias, flag or mode.
3. Editing the command text touches three files that must stay identical:
   `commands/i-have-headache.md` (source), `skills/i-have-headache/SKILL.md`
   and `.codex/prompts/i-have-headache.md`. Follow
   [.ai/technical-logic.md](.ai/technical-logic.md).
