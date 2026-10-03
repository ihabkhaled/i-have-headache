# i-have-headache
I have a headache. A Claude Code, Codex and Cursor plugin that stops AI from being talkative, chatty, loquacious, verbose, long-winded, garrulous, wordy, a blabbermouth, motor-mouth, or chatterbox, and from over-engineering code. **Always on** - nothing to type.

## Install

macOS / Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/ihabkhaled/i-have-headache/main/install.sh | sh
```

Windows (PowerShell):

```powershell
irm https://raw.githubusercontent.com/ihabkhaled/i-have-headache/main/install.ps1 | iex
```

Installs for each of Claude Code, Codex and Cursor it finds. Re-run to update.

Explicit, per platform (`sh install.sh --claude --codex --cursor`; on Windows `.\install.ps1 -Claude -Codex -Cursor`):

| Platform | Flag | Always on via |
|---|---|---|
| Claude Code | `--claude` / `-Claude` | SessionStart + UserPromptSubmit hooks |
| Codex | `--codex` / `-Codex` | a marked block in `~/.codex/AGENTS.md` |
| Cursor | `--cursor` / `-Cursor` | an `alwaysApply` rule in `~/.cursor/rules/` |

<details>
<summary>Other routes: Claude Code CLI, VS Code, one project, uninstall</summary>

Claude Code without the script:

```bash
claude plugin marketplace add https://github.com/ihabkhaled/i-have-headache.git
claude plugin install i-have-headache@i-have-headache
```

VS Code extension: `/plugins` > Marketplaces > add the URL above > install.

One project only: `--repo PATH` (`-Repo`). Remove everything: `--uninstall` (`-Uninstall`).

</details>

## Use

Nothing. Ask for detail when you want it. The one command, `/i-have-headache:i-have-headache` (Claude Code), `$i-have-headache` (Codex), `/i-have-headache` (Cursor), only re-asserts it.

## Docs

What it does for code: the same skill first decides what the task is. A patch stays small; a requested or necessary refactor gets proper architecture. Easiest maintainable code that fits the real work, project conventions first, one simplification pass at the end ([ADR-0007](.ai/decisions/ADR-0007-simple-code-same-skill.md), [ADR-0008](.ai/decisions/ADR-0008-right-sized-clean-code.md)). Those rules shape the code; the 5-bullet cap shapes only the chat summary.

[AGENTS.md](AGENTS.md) (start here) | [wiki](docs/wiki/index.md) | [decisions](.ai/decisions/) | [changelog](CHANGELOG.md)

## Contributing

Never add a second command, alias, flag or mode ([ADR-0002](.ai/decisions/ADR-0002-one-command-only.md)). The text lives in one file, `skills/i-have-headache/SKILL.md`. Every shipped change bumps the version: [rule](.ai/rules/version-discipline.md). Test: `python -m pytest tests -q`.

MIT licensed. See [LICENSE](LICENSE).
