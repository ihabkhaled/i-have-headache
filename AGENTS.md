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

A one-command plugin for Claude Code, OpenAI Codex and Cursor. Invoking
`/i-have-headache` switches the assistant into concise mode for the session.

## The hard constraint

**Exactly one user-facing command exists: `/i-have-headache`.**

Do not add a second command, a subcommand, an alias, a flag, an argument, a
mode, a setup/reset/config/helper command, or an alternative activation path.
This is a product requirement, not a preference. See
[ADR-0002](.ai/decisions/ADR-0002-one-command-only.md).

Adding docs, rules and ADRs is fine — none of those are commands. Skills are
different: a plugin skill is surfaced as a slash command. Exactly one skill
exists, `skills/i-have-headache/`, named identically to the command so the
palette shows one entry. **Never add a second skill.** See
[ADR-0005](.ai/decisions/ADR-0005-no-skills-directory.md).

## Layout

| Path | Purpose |
|---|---|
| `commands/i-have-headache.md` | Command body — source of truth, shared by Claude Code and Cursor |
| `skills/i-have-headache/SKILL.md` | Same body as a skill — required by OpenAI submission |
| `.codex/prompts/i-have-headache.md` | Codex prompt — same text, frontmatter stripped |
| `.claude-plugin/plugin.json` | Claude Code plugin manifest |
| `.claude-plugin/marketplace.json` | Makes the repo its own marketplace |
| `.cursor-plugin/plugin.json` | Cursor plugin manifest |
| `assets/` | Logo and composer icon, plus the script that draws them |
| `.ai/` | Knowledge layer — logic, decisions, rules, context |

## Before you change the command text

The three command bodies must stay byte-identical below the frontmatter. Follow
[.ai/technical-logic.md](.ai/technical-logic.md). Editing one
without the other is the single most likely bug in this repo.

## Knowledge

- [Business logic](.ai/business-logic.md)
- [Technical logic](.ai/technical-logic.md)
- [Decisions](.ai/decisions/)
- [Rules](.ai/rules/)
- [Repo map](.ai/context/repo-map.md)
