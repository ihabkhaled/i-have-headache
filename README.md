# i-have-headache
I have a headache. A Claude Code, Codex and Cursor plugin that stops AI from being talkative and over-engineering code. **Always on** — concise answers plus simple, minimal, readable and maintainable code without typing anything.

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

When coding, the same skill prefers the easiest correct solution, the smallest
safe change, existing patterns and dependencies, and code a junior developer can
follow and a CTO can scan. It avoids speculative abstractions, unnecessary
layers and cleverness. After the code works, it does one simplification pass.

Correctness, security, required tests and real performance requirements still
win. "Simple" never means careless.

## How

| Platform | Always on via |
|---|---|
| Claude Code | SessionStart hook |
| Codex | a marked block in `~/.codex/AGENTS.md` |
| Cursor | an `alwaysApply` rule in `~/.cursor/rules/` |

All three are cut from one file, `skills/i-have-headache/SKILL.md`.

## Why

AI assistants default to verbose and often over-engineer straightforward code.
They restate the request, add abstractions for imagined futures, then explain all
of it. When you have a headache, that is the opposite of helpful.

The name is literal.

## Documentation

The maintainer has a headache. Do not talk too much or over-engineer — that rule
applies to agents working on this repo, not just to the product's output.

| Read | For |
|---|---|
| [AGENTS.md](AGENTS.md) | Canonical instructions for every AI agent |
| [.ai/business-logic.md](.ai/business-logic.md) | Why it exists, what it refuses to do |
| [.ai/technical-logic.md](.ai/technical-logic.md) | How it works and what breaks it |
| [.ai/decisions/](.ai/decisions/) | Why always on, why one file, why one command |
| [.ai/context/repo-map.md](.ai/context/repo-map.md) | Every file, and where to look for what |

## Contributing

One rule: **never add a second command** — no aliases, flags, modes, extra
skills or command files. See [ADR-0002](.ai/decisions/ADR-0002-one-command-only.md).
The text lives in one file; see [.ai/technical-logic.md](.ai/technical-logic.md).

Keep changes simple too: smallest safe diff, no unrelated refactors, no
abstractions without a current need.

Behavior changes must bump the plugin version and keep the Claude plugin, Claude
marketplace and Cursor manifest versions identical. This release is `1.2.0`.

MIT licensed. See [LICENSE](LICENSE).
