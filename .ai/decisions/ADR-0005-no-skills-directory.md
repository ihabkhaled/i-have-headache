# ADR-0005 — No `skills/` directory; procedures live in `.ai/`

*Status: accepted — 2026-09-13, superseding part of ADR-0003*

## Context

A `sync-command-bodies` skill was added to hold the one repeatable procedure in
this repo. Claude Code, Cursor and the OpenAI submission flow all surface a
plugin's skills as **user-facing slash commands**. The result was two entries in
the palette:

```
/i-have-headache:i-have-headache
/i-have-headache:sync-command-bodies
```

That directly violates [ADR-0002](ADR-0002-one-command-only.md), the product's
one hard invariant. The skill was authored as internal documentation; the
packaging made it a command anyway.

## Options

**A. Keep the skill, accept two entries.** Cost: breaks the single hard
invariant. Not viable.

**B. Keep the skill, hide it from packaging.** No manifest key reliably hides a
skill across all three platforms, and OpenAI's scanner reads the directory
regardless. Unreliable, and relies on each vendor not changing behavior.

**C. Delete `skills/`; move the procedure to `.ai/`.** The content survives
verbatim as a document. Cost: agents no longer get automatic skill-triggering on
it; they must find it through `AGENTS.md`, which every agent config file already
points at.

## Decision

Option C. `skills/` is deleted. The procedure lives at
[.ai/syncing-command-bodies.md](../syncing-command-bodies.md).

**No `skills/` directory may be added to this repository.** In a plugin, a skill
is a command, and this plugin ships one command.

## Consequences

Good: the palette shows exactly one entry on every platform, which is the
product requirement.

Bad: the procedure is no longer auto-triggered by a skill description; it is
reached by reading. Mitigated by every agent config file naming it in their
three rules.

Bad: an obvious future contribution — "let's add a skill for X" — is now
forbidden and will feel arbitrary without this record.

## Revisit when

A platform offers a genuinely non-user-facing skill or private-instruction slot
that no command palette lists. Verify on every target platform before reopening,
not just one.
