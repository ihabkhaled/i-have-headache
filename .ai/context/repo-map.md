# Repo map

*Last verified: 2026-09-13*

No code. No build. No tests. No dependencies. Text files only.

```
AGENTS.md                          canonical agent instructions
CLAUDE.md CODEX.md KIMI.md         pointers to AGENTS.md
GEMINI.md QWEN.md GROK.md LLM.md
.clinerules .windsurfrules .rules
.cursor/rules/agents.mdc
.github/copilot-instructions.md

commands/i-have-headache.md        THE command — source of truth
.codex/prompts/i-have-headache.md  same body, frontmatter stripped

.claude-plugin/plugin.json         Claude Code plugin manifest
.claude-plugin/marketplace.json    repo serves as its own marketplace

skills/sync-command-bodies/        keeps the two bodies identical

.ai/business-logic.md              why it exists, what it refuses to do
.ai/technical-logic.md             how it works, what breaks it
.ai/decisions/                     ADR-0001..0003
.ai/rules/                         enforceable constraints
.ai/context/repo-map.md            this file
.ai/memory.md                      durable notes

README.md                          install and use
```

## Where to look

| Question | File |
|---|---|
| Why does this exist? | `.ai/business-logic.md` |
| How does it actually work? | `.ai/technical-logic.md` |
| Can I add `--flag`? | `.ai/decisions/ADR-0002-one-command-only.md` (no) |
| Why two copies of the same text? | `.ai/decisions/ADR-0003-duplicate-command-body.md` |
| Why so many agent files? | `.ai/decisions/ADR-0001-agents-md-canonical.md` |
| I need to edit the command | `skills/sync-command-bodies/SKILL.md` |

## Change surface

Almost every change is one of three things: editing the command body (sync both
files), editing agent instructions (edit `AGENTS.md` only), or adding knowledge
under `.ai/`. Anything else is probably a second command — see ADR-0002.
