# Repo map

*Last verified: 2026-09-13*

No runtime code. No build. No tests. No dependencies at runtime — text files
and two generated PNGs. The only script in the repo draws the logo.

```
AGENTS.md                          canonical agent instructions
CLAUDE.md CODEX.md KIMI.md         pointers to AGENTS.md
GEMINI.md QWEN.md GROK.md LLM.md
.clinerules .windsurfrules .rules
.cursor/rules/agents.mdc
.github/copilot-instructions.md

commands/i-have-headache.md        THE command — Claude Code + Cursor
.codex/prompts/i-have-headache.md  same body, frontmatter stripped

.claude-plugin/plugin.json         Claude Code manifest (icons under interface)
.claude-plugin/marketplace.json    repo serves as its own marketplace
.cursor-plugin/plugin.json         Cursor manifest (logo top-level)

assets/make_logo.py                draws the artwork
assets/logo.png                    512x512
assets/composer-icon.png           256x256

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
| Why does Cursor share `commands/`? | `.ai/decisions/ADR-0004-cursor-shares-the-command-directory.md` |
| How do I change the logo? | `python assets/make_logo.py` after editing it |
| Why so many agent files? | `.ai/decisions/ADR-0001-agents-md-canonical.md` |
| I need to edit the command | `skills/sync-command-bodies/SKILL.md` |

## Change surface

Almost every change is one of four things: editing the command body (sync both
files), editing agent instructions (edit `AGENTS.md` only), adding knowledge
under `.ai/`, or regenerating the artwork (`python assets/make_logo.py`).
Anything else is probably a second command — see ADR-0002.
