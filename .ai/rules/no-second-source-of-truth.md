# Rule — no second source of truth

`AGENTS.md` is canonical. Every other agent config file (`CLAUDE.md`,
`CODEX.md`, `KIMI.md`, `GEMINI.md`, `QWEN.md`, `GROK.md`, `LLM.md`,
`.clinerules`, `.windsurfrules`, `.rules`, `.cursor/rules/agents.mdc`,
`.github/copilot-instructions.md`) is a pointer.

Each pointer restates exactly three rules: the headache behavior (concise output
plus right-sized code), one command only, and the command text lives in one
file. When any of those three changes, edit `AGENTS.md` and update every
pointer together, or router sync is stale.

Never let a pointer grow tool-specific product behavior. If a tool genuinely
needs something the others do not, that reopens
[ADR-0001](../decisions/ADR-0001-agents-md-canonical.md).
