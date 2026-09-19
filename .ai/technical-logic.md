# Technical logic

*Last verified: 2026-09-19*

## How it works

No code beyond two installers and a hook. The product is prompt text.
**One file holds it: `skills/i-have-headache/SKILL.md`.** Everything else is
derived from that file at run time — see
[ADR-0006](decisions/ADR-0006-always-on-one-source.md).

## Always on, per platform

| Platform | Mechanism | Where |
|---|---|---|
| Claude Code | SessionStart hook prints the rules | `hooks/hooks.json` → `hooks/session-start.sh` |
| Codex | marked block in `AGENTS.md` | `~/.codex/AGENTS.md`, or a repo's `AGENTS.md` |
| Cursor | `alwaysApply` rule | `~/.cursor/rules/i-have-headache.mdc`, or a repo's |

"The rules" = the skill body after its frontmatter, up to the line
`Concise mode is always on`. The acknowledgement below that line is only for an
explicit run of the command. Change that line and the hook, `install.sh` and
`install.ps1` stop at the wrong place — all three look for it.

The hook is in exec form (`command: sh`, `args: [...]`): the shell form exits 126
on Claude Code 2.1.154 under Git Bash.

## The one entry

The skill is the command. Claude Code shows it as
`/i-have-headache:i-have-headache`, Codex as `$i-have-headache`, Cursor as
`/i-have-headache`. There is no `commands/` directory and no Codex prompt — each
would be a second entry.

## Packaging

- `.claude-plugin/plugin.json` + `marketplace.json`: the repo is its own
  marketplace. Skills and hooks are discovered from `skills/` and `hooks/`.
- `.cursor-plugin/plugin.json`: `skills` only. It must never point `rules` at
  `.cursor/rules` — that folder is this repo's agent pointer, not product.
- Codex and Cursor read skills from `~/.agents/skills` (or a repo's
  `.agents/skills`), so the installer's one copy serves both.

## Installers

`install.sh` and `install.ps1` behave identically (same block, byte for byte):
detect platforms, install the skill, write the always-on block and rule, remove
the old `~/.codex/prompts/i-have-headache.md`, keep CRLF, and `--uninstall`
restores files exactly. They remove only what contains "I have a headache.".

## Icons

`assets/logo.png` (512×512) and `assets/composer-icon.png` (256×256) are drawn by
`assets/make_logo.py` (Pillow). Both must stay square. Edit the script, re-run:

```bash
python assets/make_logo.py
```

## What would break this

| Change | Consequence |
|---|---|
| Renaming the skill or its folder | Name no longer matches; Cursor rejects it |
| Adding a second skill, `commands/` or a Codex prompt | A second menu entry |
| Editing the `Concise mode is always on` line | Always-on text cut at the wrong place |
| Shell-form hook | Exits 126 on Claude Code 2.1.154 (Windows) |
| Non-square icons | Claude Code manifest validation fails |
