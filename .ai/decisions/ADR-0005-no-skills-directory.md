# ADR-0005 — Exactly one skill, named identically to the command

*Amended 2026-09-19 by [ADR-0006](ADR-0006-always-on-one-source.md): the skill is now the only copy and the command; `commands/` is gone.*

*Status: accepted — 2026-09-13. Supersedes the original ban on `skills/`.*

## Context

A `sync-command-bodies` skill was added first and immediately produced a second
palette entry, `/i-have-headache:sync-command-bodies`, violating
[ADR-0002](ADR-0002-one-command-only.md). It was deleted, and this ADR
originally banned `skills/` outright.

That ban then failed OpenAI submission:

```
Plugin has no valid skills
Add or fix at least one skill at `skills/<skill>/SKILL.md`
```

So the constraint is two-sided: OpenAI requires at least one skill, and the
product requires exactly one user-facing name.

## Options

**A. Keep the ban, skip OpenAI.** Cost: no ChatGPT/Codex distribution. The
platform is a target, so this is not viable.

**B. Add a differently-named skill.** Whatever it is called becomes a second
palette entry. This is exactly what already broke once.

**C. One skill, named `i-have-headache`** — the same name as the command,
carrying the same body. Satisfies OpenAI's minimum. Because the name matches,
the palette shows a single entry.

## Decision

Option C. `skills/i-have-headache/SKILL.md` exists and is the **only** permitted
skill.

The original rule was right about the danger and wrong about the mechanism. The
invariant is not "no skills" — it is **one user-facing name**. A skill sharing
that name adds no entry; any other name adds one.

## Consequences

Good: OpenAI submission passes and the palette still shows one name.

Bad: a third file now carries the command body. Sync burden grows from two files
to three. Covered by
[.ai/technical-logic.md](../technical-logic.md).

Bad: `skills/` existing invites a second skill, which is the original failure. A
second skill directory is forbidden — the checklist in the sync procedure
asserts one entry.

Bad: the name collision between command and skill is load-bearing but invisible.
Renaming either one silently produces two palette entries.

## Revisit when

OpenAI drops the minimum-one-skill requirement, or a platform starts listing
same-named commands and skills as two entries. Verify the palette after any
change here — do not assume.
