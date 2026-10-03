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

## The right-sized code rule

Plan the size of the change before designing it. A patch should remain a patch;
a requested or genuinely necessary refactor should be allowed to become a real
refactor. Do not force every task into either extreme.

Read the surrounding code and follow the project's conventions first. Ask
grouped questions when the answers materially change scope, architecture,
behavior, risk or acceptance; do not block an obvious minor patch on trivial
questions.

Write clean, organized code a junior developer can follow, a senior can maintain,
and a CTO can scan. Use descriptive names, focused functions, straightforward
control flow, sensible file boundaries and the project's existing patterns.

Abstractions, patterns, shared error frameworks and defensive mechanisms are
allowed when they solve a real problem, fit the codebase, or improve
maintainability. They are not goals by themselves. A little simple duplication
can be better than a bad abstraction; a good abstraction should be used when it
makes the code easier to understand and maintain.

When the user explicitly asks for a patch or minor change, minimize touched
surface and avoid unrelated refactors. When the user explicitly asks for a
refactor, refactor it properly. Preserve correctness, security, all relevant
tests and real performance requirements in either case.

After the change works, simplify it once without fighting the project's
architecture. See
[ADR-0008](.ai/decisions/ADR-0008-right-sized-clean-code.md).

## What this repository is

A plugin for Claude Code, OpenAI Codex and Cursor that keeps the assistant
concise and generated code clean, readable and right-sized for the actual task.
It is **always on**: nothing needs to be typed. `/i-have-headache` is the one
command, and it only re-asserts it. See
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
| `hooks/` | Claude hooks: SessionStart prints the rules from the skill, UserPromptSubmit adds a one-line reminder — always on |
| `skills/i-have-headache/scripts/` | `headache_version.py`, version discipline; not a command |
| `tests/`, `.github/workflows/ci.yml` | `python -m pytest tests -q`; CI runs it and the version check |
| `CHANGELOG.md`, `docs/` | Release notes; the wiki and one record per change |
| `install.sh`, `install.ps1` | One-line install for Claude Code, Codex and Cursor |
| `.claude-plugin/plugin.json` | Claude Code plugin manifest |
| `.claude-plugin/marketplace.json` | Makes the repo its own marketplace |
| `.cursor-plugin/plugin.json` | Cursor plugin manifest (skills only) |
| `assets/` | Logo and composer icon, plus the script that draws them |
| `.ai/` | Knowledge layer — logic, decisions, rules, context |

## Before you change the command text

Edit `skills/i-have-headache/SKILL.md` — it is the only copy. Keep the line that
starts `Concise mode is always on`: the hook and both installers cut the
always-on text there. All always-on behavior, including the clean-code rules,
must stay above that line. See [.ai/technical-logic.md](.ai/technical-logic.md).

## Versioning

Every user-facing behavior change must bump the plugin version. Keep the version
identical in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` and
`.cursor-plugin/plugin.json`. This right-sized clean-code release is `1.3.0`.
Do not merge a future behavior change with stale or mismatched manifest versions.

## Releasing

A change to a shipped path bumps the version and the changelog, with the tool:
[.ai/rules/version-discipline.md](.ai/rules/version-discipline.md).

## Knowledge

- [Business logic](.ai/business-logic.md)
- [Technical logic](.ai/technical-logic.md)
- [Decisions](.ai/decisions/)
- [Rules](.ai/rules/)
- [Repo map](.ai/context/repo-map.md)
