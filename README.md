# i-have-headache
I have a headache. One-command Claude Code and OpenAI Codex skill that stops AI from being talkative, chatty, loquacious, verbose, long-winded, garrulous, wordy, a blabbermouth, motor-mouth, or chatterbox. Run /i-have-headache for concise, direct, summarized responses.


## Install

**Claude Code**

```
/plugin marketplace add ihabkhaled/i-have-headache
/plugin install i-have-headache
```

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
| `commands/i-have-headache.md` | Claude Code command |
| `.codex/prompts/i-have-headache.md` | Codex prompt (same text, no frontmatter) |

Keep the two command bodies in sync. The Codex copy is the Claude one with the
YAML frontmatter stripped.
