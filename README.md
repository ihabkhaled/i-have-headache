# i-have-headache
I have a headache. A Claude Code, Codex and Cursor plugin that stops AI from being talkative, chatty, loquacious, verbose, long-winded, garrulous, wordy, a blabbermouth, motor-mouth, or chatterbox. **Always on** — concise, direct, summarized responses without typing anything.

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

## How

| Platform | Always on via |
|---|---|
| Claude Code | SessionStart hook |
| Codex | a marked block in `~/.codex/AGENTS.md` |
| Cursor | an `alwaysApply` rule in `~/.cursor/rules/` |

All three are cut from one file, `skills/i-have-headache/SKILL.md`.

## Why

AI assistants default to verbose: they restate your request, explain what they
are about to do, do it, then explain what they did. When you have a headache,
that is not neutral — it hurts.

The name is literal.

## Documentation

The maintainer has a headache. Do not talk too much — that rule applies to
agents working on this repo, not just to the product's output.

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

MIT licensed. See [LICENSE](LICENSE).
