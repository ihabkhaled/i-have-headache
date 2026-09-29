# Copilot instructions

See [AGENTS.md](../AGENTS.md) — single source of truth for this repository.

1. The maintainer has a headache — be concise and right-size the code. A patch
   stays narrow; a real refactor may use the architecture it needs. Follow the
   project's conventions.
2. Exactly one user-facing command exists, `/i-have-headache`. Never add a
   second.
3. The command text lives in one file, `skills/i-have-headache/SKILL.md` - the
   skill, which is also the command. The always-on behavior is derived from that
   file. Follow [.ai/technical-logic.md](../.ai/technical-logic.md).
