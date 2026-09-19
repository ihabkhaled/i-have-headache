# ADR-0006 — Always on, one skill, one source

*Status: accepted — 2026-09-19. Supersedes ADR-0003 and ADR-0004; amends
ADR-0002 and ADR-0005.*

## Context

The maintainer asked for concise mode without typing `/i-have-headache` —
"everything under one skill and one command", as in Akinator. The body also
lived in three copies (`commands/`, `skills/`, `.codex/prompts/`) kept in sync
by hand, and the Cursor manifest shipped this repo's own agent pointer as a rule
into users' projects.

## Options

**A. Keep opt-in; only merge the copies.** Cost: the user still has to invoke it
each session — the exact decision the product exists to remove.

**B. Always on, one source.** The skill is the only copy and is also the command.
Concise mode is injected at session start on every platform. Cost: every session
is concise until the user asks for detail; the command stays only as an explicit
re-assert.

## Decision

Option B.

| Platform | Always on via | Explicit entry |
|---|---|---|
| Claude Code | SessionStart hook, exec form | `/i-have-headache:i-have-headache` |
| Codex | marked block in `AGENTS.md` | `$i-have-headache` |
| Cursor | `alwaysApply` rule | `/i-have-headache` |

The hook and both installers extract the rules from `skills/i-have-headache/SKILL.md`
at run time — everything after the frontmatter, up to the acknowledgement. The
acknowledgement ("Concise mode on.") is sent only on an explicit run, never on
injection. `commands/` and `.codex/prompts/` are deleted; the Cursor manifest no
longer ships `.cursor/rules`.

## Consequences

Good: nothing to type; one file to edit; one entry per platform (verified live on
Claude Code 2.1.154: `['i-have-headache:i-have-headache']`, hook exit 0, no
acknowledgement injected). The installer removes the old Codex prompt, which
would otherwise be a second entry.

Bad: concise everywhere, every session. Turning it off per request is plain
language ("more detail"); uninstalling is the only global off.

Bad: this is an activation path ADR-0002 would have forbidden — accepted because
the maintainer asked for exactly it.
