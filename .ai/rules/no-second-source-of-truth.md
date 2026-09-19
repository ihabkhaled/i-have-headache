# Rule — no second source of truth

`AGENTS.md` is canonical. Every other agent config file (`CLAUDE.md`,
`CODEX.md`, `KIMI.md`, `GEMINI.md`, `QWEN.md`, `GROK.md`, `LLM.md`,
`.clinerules`, `.windsurfrules`, `.rules`, `.cursor/rules/agents.mdc`,
`.github/copilot-instructions.md`) is a pointer.

Each pointer restates exactly three rules: be concise, one command only, and the
command text lives in one file. When instructions change, edit `AGENTS.md`. Touch a
pointer only if one of those three has changed — then update all of them
together, or `router-sync` in the coverage check will fail.

Never let a pointer grow tool-specific content. If a tool genuinely needs
something the others do not, that reopens
[ADR-0001](../decisions/ADR-0001-agents-md-canonical.md).
