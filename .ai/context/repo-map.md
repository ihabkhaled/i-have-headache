# Repo map

*Last verified: 2026-09-19*

No runtime code, no build, no dependencies. The product is one text file.

```
skills/i-have-headache/SKILL.md    THE text - the one skill, also the one command
hooks/hooks.json                   Claude SessionStart hook (exec form)
hooks/session-start.sh             prints the rules from SKILL.md - always on
install.sh  install.ps1            one-line install for Claude Code, Codex, Cursor

.claude-plugin/plugin.json         Claude Code manifest (icons under interface)
.claude-plugin/marketplace.json    repo serves as its own marketplace
.cursor-plugin/plugin.json         Cursor manifest (skills only)

AGENTS.md                          canonical agent instructions
CLAUDE.md CODEX.md KIMI.md         pointers to AGENTS.md
GEMINI.md QWEN.md GROK.md LLM.md
.clinerules .windsurfrules .rules
.cursor/rules/agents.mdc
.github/copilot-instructions.md

assets/make_logo.py                draws the artwork
assets/logo.png                    512x512
assets/composer-icon.png           256x256

.ai/business-logic.md              why it exists, what it refuses to do
.ai/technical-logic.md             how it works, what breaks it
.ai/decisions/                     ADR-0001..0006
.ai/rules/                         enforceable constraints
.ai/context/repo-map.md            this file
.ai/memory.md                      durable notes

README.md                          install and use
```

## Where to look

| Question | File |
|---|---|
| Why does this exist? | `.ai/business-logic.md` |
| How does it work? | `.ai/technical-logic.md` |
| Why always on, one file? | `.ai/decisions/ADR-0006-always-on-one-source.md` |
| Can I add `--flag`? | `.ai/decisions/ADR-0002-one-command-only.md` (no) |
| Can I add a skill? | `.ai/decisions/ADR-0005-no-skills-directory.md` (no) |
| How do I change the logo? | `python assets/make_logo.py` after editing it |
| Why so many agent files? | `.ai/decisions/ADR-0001-agents-md-canonical.md` |

## Change surface

Almost every change is one of: editing `skills/i-have-headache/SKILL.md` (the
only copy), editing agent instructions (`AGENTS.md` only), adding knowledge
under `.ai/`, or regenerating the artwork. Anything else is probably a second
command — see ADR-0002.
