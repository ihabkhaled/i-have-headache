# AGENTS.md

Canonical instructions for every AI agent working in this repository.
All other agent config files in this repo are pointers to this one.

## The headache rule

The maintainer has a headache. Do not talk too much.

Give the shortest complete answer that solves the request. No filler, no
preamble, no restating the request, no long intros or conclusions, no
over-explaining, no giant lists when a sentence works. Expand only when
explicitly asked.

This is not just house style — it is the product. This repository ships a
command whose entire purpose is enforcing that rule. An agent that is verbose
while working on it has misunderstood the codebase.

## What this repository is

A plugin for Claude Code, OpenAI Codex and Cursor that keeps the assistant
concise. It is **always on**: nothing needs to be typed. `/i-have-headache` is
the one command, and it only re-asserts it. See
[ADR-0006](.ai/decisions/ADR-0006-always-on-one-source.md).

## The hard constraint

**Exactly one user-facing command exists: `/i-have-headache`.**

Do not add a second command, a subcommand, an alias, a flag, an argument, a
mode, a setup/reset/config/helper command, or an alternative activation path.
This is a product requirement, not a preference. See
[ADR-0002](.ai/decisions/ADR-0002-one-command-only.md).

Adding docs, rules and ADRs is fine — none of those are commands. Skills are
different: a plugin skill is surfaced as a slash command. Exactly one skill
exists, `skills/i-have-headache/`, and it is the command. **Never add a second
skill, a `commands/` file or a Codex prompt** — each is a second entry. See
[ADR-0005](.ai/decisions/ADR-0005-no-skills-directory.md).

## Layout

| Path | Purpose |
|---|---|
| `skills/i-have-headache/SKILL.md` | The only copy of the text — the skill and the command |
| `hooks/` | Claude SessionStart hook: prints the rules from the skill — always on |
| `install.sh`, `install.ps1` | One-line install for Claude Code, Codex and Cursor |
| `.claude-plugin/plugin.json` | Claude Code plugin manifest |
| `.claude-plugin/marketplace.json` | Makes the repo its own marketplace |
| `.cursor-plugin/plugin.json` | Cursor plugin manifest (skills only) |
| `assets/` | Logo and composer icon, plus the script that draws them |
| `.ai/` | Knowledge layer — logic, decisions, rules, context |

## Before you change the command text

Edit `skills/i-have-headache/SKILL.md` — it is the only copy. Keep the line that
starts `Concise mode is always on`: the hook and both installers cut the
always-on text there. See [.ai/technical-logic.md](.ai/technical-logic.md).

## Knowledge

- [Business logic](.ai/business-logic.md)
- [Technical logic](.ai/technical-logic.md)
- [Decisions](.ai/decisions/)
- [Rules](.ai/rules/)
- [Repo map](.ai/context/repo-map.md)
