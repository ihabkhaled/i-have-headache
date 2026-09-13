# ADR-0004 — Cursor reuses `commands/`; it does not get its own copy

*Status: accepted — 2026-09-13*

## Context

Cursor plugins declare `.cursor-plugin/plugin.json` and read commands from a
`commands/` directory of markdown files with YAML frontmatter — the same shape
Claude Code uses. Cursor derives the command name from a frontmatter `name`
field; Claude Code derives it from the filename and ignores unknown keys.

Codex, by contrast, has no manifest and no frontmatter concept, which is why it
already needs a separate stripped copy
([ADR-0003](ADR-0003-duplicate-command-body.md)).

## Options

**A. Give Cursor its own copy**, mirroring the Codex arrangement. Uniform
handling of all three platforms. Cost: a third file to keep in sync, for no
technical reason — the format is already compatible. Sync burden grows with
each platform even when the format does not require it.

**B. Point Cursor's manifest at the existing `commands/`** and add `name:` to
the frontmatter so both platforms resolve the command. Cost: the shared file
carries one key Claude Code does not use, and the repo now depends on Cursor
and Claude Code keeping their command formats compatible.

## Decision

Option B. `.cursor-plugin/plugin.json` sets `"commands": "./commands"`.

Copy a file only when a format actually forces it. Codex forces it; Cursor does
not.

## Consequences

Good: adding Cursor cost one manifest and one frontmatter line. Still two
command bodies to sync, not three — the sync procedure is unchanged.

Good: `commands/i-have-headache.md` stays the single source of truth, with
Codex generated from it.

Bad: the repo now depends on two vendors' formats staying compatible. If Cursor
diverges, this ADR reopens and Cursor gets its own copy under the existing
sync skill.

Bad: `name: i-have-headache` in the frontmatter is inert on Claude Code, so it
looks redundant to anyone who does not know why it is there. Recorded here for
that reason.

## Revisit when

Cursor's command format diverges from Claude Code's, or a fourth platform
appears that also cannot share the directory.
