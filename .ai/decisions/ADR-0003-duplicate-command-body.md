# ADR-0003 — Duplicate the command body rather than generate it

*Status: accepted — 2026-09-13*

## Context

Claude Code and Codex need the same prompt text. Claude Code requires YAML
frontmatter; Codex must not have it. So the two files are identical except for a
four-line header.

## Options

**A. Generate the Codex file from the Claude one.** A script strips frontmatter;
CI verifies they match. Guarantees no drift. Cost: the repo gains a build step,
a script, and a CI config — for a three-file plugin with no other tooling. The
machinery would be larger than the product.

**B. Duplicate, and document the sync obligation.** Both files are checked in
and hand-maintained. Cost: they can drift silently, and nothing mechanical stops
it.

## Decision

Option B, with the obligation written down in three places: `AGENTS.md`,
[technical-logic](../technical-logic.md), and a dedicated skill,
[sync-command-bodies](../../skills/sync-command-bodies/SKILL.md).

The body is one screen of prose that changes rarely. Build tooling would be
permanent overhead against an occasional, low-severity, easily-detected failure.

## Consequences

Good: the repo stays a pile of text files. Clone and read; no toolchain.

Bad: drift is possible and nothing prevents it mechanically. A missed sync means
the two platforms behave differently with no error anywhere. Detection is manual
— someone notices Codex acting differently.

Bad: the mitigation is documentation, which is weaker than a check. Accepted
because the blast radius is "one platform is slightly more verbose," not data
loss.

## Revisit when

The command body grows past roughly one screen, gains a third *file* to sync,
or a drift incident actually occurs. Any of those flips the arithmetic toward
Option A.

Cursor was added later and did **not** trigger this: it shares
`commands/` with Claude Code, so the file count is unchanged. See
[ADR-0004](ADR-0004-cursor-shares-the-command-directory.md). What matters is
files to sync, not platforms supported.
