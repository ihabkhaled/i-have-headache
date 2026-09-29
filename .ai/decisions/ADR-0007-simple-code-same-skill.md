# ADR-0007 — Simple code belongs in the same skill

*Status: accepted — 2026-09-29. Extends ADR-0006; preserves ADR-0002 and
ADR-0005. Coding semantics refined by ADR-0008.*

## Context

The maintainer asked `/i-have-headache` to do more than reduce prose: coding
answers should also prefer minimal, easy-to-read, easy-to-maintain code. The
requested standard is simple enough for a junior developer to follow and clear
enough for a CTO to scan, with the easiest correct path considered before more
complicated designs.

The one-command invariant still applies. A second "clean code", "simple code" or
"refactor" skill would violate the product.

## Options

**A. Add a second coding skill or mode.** Clear separation, but it creates
another command or configuration choice and breaks the core constraint.

**B. Extend the existing `i-have-headache` skill.** The same always-on prompt
handles concise communication and simple-first coding. No new activation path,
runtime or dependency.

**C. Keep the plugin prose-only.** Smallest change, but it does not satisfy the
requested coding behavior.

## Decision

Option B.

The coding rules live in `skills/i-have-headache/SKILL.md` above the
`Concise mode is always on` marker so the existing Claude hook, Codex installer
block and Cursor rule all inherit them automatically.

Version 1.2.0 established the simple-first direction. ADR-0008 refines the
meaning of "simple": it is context-sensitive, not a prohibition on abstraction
or architecture. Patch requests stay patch-sized; requested or necessary
refactors can use the structure they genuinely need.

## Consequences

Good: one command still means everything; no new surface to learn.

Good: the installers and hook require no functional change because they already
extract the skill body up to the existing marker.

Release history: 1.2.0 introduced simple-first coding. 1.3.0 refines it into
right-sized clean-code judgment. Future user-facing behavior changes must also
bump the version and keep all plugin manifests synchronized.

Tradeoff: "simple" is contextual. It means lower unnecessary cognitive load,
not minimum line count, file count or architecture.

## Reversal

Revisit only if the maintainer explicitly changes the coding default or lifts
the one-command constraint.
