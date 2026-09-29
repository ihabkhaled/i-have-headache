# i-have-headache

I have a headache. A Claude Code, Codex and Cursor plugin that stops AI from
being talkative and from over-engineering code. **Always on** — concise answers
plus clean, organized, readable code with the amount of architecture the actual
task needs.

## Install

macOS / Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/ihabkhaled/i-have-headache/main/install.sh | sh
```

Windows (PowerShell):

```powershell
irm https://raw.githubusercontent.com/ihabkhaled/i-have-headache/main/install.ps1 | iex
```

It installs for every one of Claude Code, Codex and Cursor it finds. Re-run to
update. Add `--uninstall` (`-Uninstall`) to remove; `--repo PATH` (`-Repo`) to
install into one project only.

Claude Code without the script:

```bash
claude plugin marketplace add https://github.com/ihabkhaled/i-have-headache.git
claude plugin install i-have-headache@i-have-headache
```

In the VS Code extension: `/plugins` → Marketplaces → add the URL above → install.

## Use

Nothing. It is always on. To get detail back for one answer, ask for it.

The one command re-asserts it: `/i-have-headache:i-have-headache` (Claude Code),
`$i-have-headache` (Codex), `/i-have-headache` (Cursor).

For coding, the same skill first decides what the task actually is. A minor
patch stays small. A requested or genuinely necessary refactor can use proper
architecture. The goal is not "always fewer lines" or "never use patterns" — it
is the easiest maintainable code that fits the real work.

It prefers descriptive names, focused functions, clear control flow, organized
files, project conventions and existing dependencies. Abstractions, design
patterns, shared error frameworks, validation, retries, fallbacks, caching and
other engineering tools are used when they solve a real problem or fit the
codebase, not because they sound sophisticated.

It asks useful questions when answers can materially change the implementation,
covers all relevant success/error/edge/regression cases, and performs one final
simplification pass after the solution works.

## How

| Platform | Always on via |
|---|---|
| Claude Code | SessionStart hook |
| Codex | a marked block in `~/.codex/AGENTS.md` |
| Cursor | an `alwaysApply` rule in `~/.cursor/rules/` |

All three are cut from one file, `skills/i-have-headache/SKILL.md`.

## Why

AI assistants can fail in two opposite directions: turning a tiny patch into an
architecture project, or forcing an actually complex requirement into a brittle
tiny patch. This plugin aims for the right amount of engineering.

Simple task → simple change. Real refactor → proper refactor. In both cases the
code should be clean, readable and easy for the next developer to maintain.

The name is literal.

## Documentation

The maintainer has a headache. Do not talk too much or over-engineer — that rule
applies to agents working on this repo, not just to the product's output.

| Read | For |
|---|---|
| [AGENTS.md](AGENTS.md) | Canonical instructions for every AI agent |
| [.ai/business-logic.md](.ai/business-logic.md) | Why it exists, what it refuses to do |
| [.ai/technical-logic.md](.ai/technical-logic.md) | How it works and what breaks it |
| [.ai/decisions/](.ai/decisions/) | Why always on, one command, and right-sized clean code |
| [.ai/context/repo-map.md](.ai/context/repo-map.md) | Every file, and where to look for what |

## Contributing

One rule: **never add a second command** — no aliases, flags, modes, extra
skills or command files. See
[ADR-0002](.ai/decisions/ADR-0002-one-command-only.md).

For code changes, match implementation size to requested scope, follow project
conventions, keep patches narrow when patching is requested, and allow proper
architecture when a real refactor needs it. See
[ADR-0008](.ai/decisions/ADR-0008-right-sized-clean-code.md).

Behavior changes must bump the plugin version and keep the Claude plugin, Claude
marketplace and Cursor manifest versions identical. This release is `1.3.0`.

MIT licensed. See [LICENSE](LICENSE).
