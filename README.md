# i-have-headache
I have a headache. One-command Claude Code, Cursor and OpenAI Codex plugin that stops AI from being talkative, chatty, loquacious, verbose, long-winded, garrulous, wordy, a blabbermouth, motor-mouth, or chatterbox. Run /i-have-headache for concise, direct, summarized responses.


## Install

**Claude Code**

```
/plugin marketplace add ihabkhaled/i-have-headache
/plugin install i-have-headache
```

**Cursor**

Install from the Cursor marketplace, or clone the repo and point Cursor at
it — the manifest is `.cursor-plugin/plugin.json`.

**OpenAI Codex**

```
curl -o ~/.codex/prompts/i-have-headache.md \
  https://raw.githubusercontent.com/ihabkhaled/i-have-headache/main/.codex/prompts/i-have-headache.md
```

## Use

```
/i-have-headache
```

That is the only command. Concise mode stays on for the session. Ask for more
detail explicitly when you want it back.

## Layout

| Path | Platform |
|---|---|
| `.claude-plugin/plugin.json` | Claude Code manifest |
| `commands/i-have-headache.md` | Claude Code + Cursor command |
| `.cursor-plugin/plugin.json` | Cursor manifest |
| `.codex/prompts/i-have-headache.md` | Codex prompt (same text, no frontmatter) |

Keep the two command bodies in sync. The Codex copy is the Claude one with the
YAML frontmatter stripped. Cursor shares the Claude file, so three platforms
need only two files.

The logo is generated, not hand-drawn — edit `assets/make_logo.py` and re-run
it rather than editing the PNGs.

## Why

AI assistants default to verbose: they restate your request, explain what they
are about to do, do it, then explain what they did. When you have a headache,
that is not neutral — it hurts. One command turns it off.

The name is literal.

## Documentation

The maintainer has a headache. Do not talk too much — that rule applies to
agents working on this repo, not just to the command's output.

| Read | For |
|---|---|
| [AGENTS.md](AGENTS.md) | Canonical instructions for every AI agent |
| [.ai/business-logic.md](.ai/business-logic.md) | Why it exists, what it deliberately refuses to do |
| [.ai/technical-logic.md](.ai/technical-logic.md) | How it works and what breaks it |
| [.ai/decisions/](.ai/decisions/) | Why one command, why duplicated text, why AGENTS.md |
| [.ai/context/repo-map.md](.ai/context/repo-map.md) | Every file, and where to look for what |

Per-tool config files (`CLAUDE.md`, `CODEX.md`, `KIMI.md`, `GEMINI.md`,
`QWEN.md`, `GROK.md`, `.cursor/rules/`, `.github/copilot-instructions.md`,
`.windsurfrules`, `.clinerules`) are four-line pointers to `AGENTS.md`.

## Contributing

One rule: **never add a second command.** No aliases, flags, modes or setup
steps. See [ADR-0002](.ai/decisions/ADR-0002-one-command-only.md) — the
constraint is the product.

Editing the command text touches two files that must stay identical. Follow
[skills/sync-command-bodies](skills/sync-command-bodies/SKILL.md).

MIT licensed. See [LICENSE](LICENSE).
