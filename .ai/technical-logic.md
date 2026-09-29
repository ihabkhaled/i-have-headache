# Technical logic

*Last verified: 2026-09-29*

## How it works

No runtime code beyond two installers and a hook. The product is prompt text.
**One file holds it: `skills/i-have-headache/SKILL.md`.** Everything else is
derived from that file at run time — see
[ADR-0006](decisions/ADR-0006-always-on-one-source.md).

The skill carries concise-output rules plus right-sized clean-code judgment in
the same body. It first determines the real change shape — patch, feature,
refactor or architectural work — then applies the coding rules proportionally.
No second skill, command, mode, runtime, dependency or configuration was added.

See [ADR-0007](decisions/ADR-0007-simple-code-same-skill.md) and
[ADR-0008](decisions/ADR-0008-right-sized-clean-code.md).

## Always on, per platform

| Platform | Mechanism | Where |
|---|---|---|
| Claude Code | SessionStart hook prints the rules | `hooks/hooks.json` → `hooks/session-start.sh` |
| Codex | marked block in `AGENTS.md` | `~/.codex/AGENTS.md`, or a repo's `AGENTS.md` |
| Cursor | `alwaysApply` rule | `~/.cursor/rules/i-have-headache.mdc`, or a repo's |

"The rules" = the skill body after its frontmatter, up to the line
`Concise mode is always on`. That includes planning, scope, clean-code,
testing and simplification rules. The acknowledgement below that line is only
for an explicit run of the command.

Change that marker and the hook, `install.sh` and `install.ps1` stop at the wrong
place — all three look for it. Move a rule below it and that rule stops being
always on.

The hook is in exec form (`command: sh`, `args: [...]`): the shell form exits 126
on Claude Code 2.1.154 under Git Bash.

## The one entry

The skill is the command. Claude Code shows it as
`/i-have-headache:i-have-headache`, Codex as `$i-have-headache`, Cursor as
`/i-have-headache`. There is no `commands/` directory and no Codex prompt — each
would be a second entry.

## Coding semantics

Version 1.3.0 treats the coding rules as **context-sensitive defaults**, not
mechanical prohibitions.

- Explicit patch/minor request → keep the change narrow.
- Explicit refactor/architecture request → do the refactor or architecture
  properly.
- Ambiguous scope with materially different implementations → ask grouped,
  useful questions before coding.
- Trivial implementation choices → decide and proceed without unnecessary
  interruption.
- Project conventions → preferred over generic style doctrine.
- Abstractions/patterns → use when they improve maintainability, clarify a real
  concept or fit established architecture.
- Error/defensive infrastructure → follow the real requirement and project
  conventions, including shared frameworks.
- Verification → cover all relevant behavior touched by the change.
- Finish → simplify once without undoing useful architecture.

## Packaging

Version `1.3.0` refines the existing simple-code behavior into right-sized
clean-code behavior. Installation and activation are unchanged.

Every future user-facing behavior change must bump the version. The version must
stay identical in `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`
and `.cursor-plugin/plugin.json`; mismatched or stale versions are a release
defect.

- `.claude-plugin/plugin.json` + `marketplace.json`: the repo is its own
  marketplace. Skills and hooks are discovered from `skills/` and `hooks/`.
- `.cursor-plugin/plugin.json`: `skills` only. It must never point `rules` at
  `.cursor/rules` — that folder is this repo's agent pointer, not product.
- Codex and Cursor read skills from `~/.agents/skills` (or a repo's
  `.agents/skills`), so the installer's one copy serves both.

## Installers

`install.sh` and `install.ps1` behave identically: detect platforms, install
the skill, write the always-on block and rule, remove the old Codex prompt, keep
line endings, and uninstall only their own content.

The installer extraction logic needs no change for 1.3.0 because every new rule
lives before the existing marker and is therefore included automatically.

## Icons

`assets/logo.png` (512×512) and `assets/composer-icon.png` (256×256) are drawn by
`assets/make_logo.py` (Pillow). Both must stay square.

```bash
python assets/make_logo.py
```

## What would break this

| Change | Consequence |
|---|---|
| Renaming the skill or its folder | Name no longer matches; Cursor rejects it |
| Adding a second skill, `commands/` or a Codex prompt | A second menu entry |
| Editing the `Concise mode is always on` line | Always-on text cut at the wrong place |
| Moving coding rules below that line | They stop being injected automatically |
| Treating flexible coding defaults as rigid bans | Reintroduces under-engineering |
| Ignoring explicit patch scope | Reintroduces over-engineering |
| Shell-form hook | Exits 126 on Claude Code 2.1.154 (Windows) |
| Non-square icons | Claude Code manifest validation fails |
