# ADR-0007 — Simple code belongs in the same skill

*Status: accepted — 2026-09-29. Extends ADR-0006; preserves ADR-0002 and
ADR-0005.*

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

The simple-code rules live in `skills/i-have-headache/SKILL.md` above the
`Concise mode is always on` marker so the existing Claude hook, Codex installer
block and Cursor rule all inherit them automatically.

The default is:

- easiest correct solution before a complicated one;
- smallest safe change using existing patterns and dependencies;
- readable, direct code with no speculative abstractions or future-proofing;
- no imagined scale or edge cases unless current requirements or real risk need
  them;
- one simplification pass after the solution works;
- correctness, security, required tests and real performance needs remain
  non-negotiable.

## Consequences

Good: one command still means everything; no new surface to learn; generated
code has fewer moving parts and lower maintenance cost.

Good: the installers and hook require no functional change because they already
extract the skill body up to the existing marker.

Release: this user-facing behavior change bumps the plugin from `1.1.0` to
`1.2.0`. Future user-facing behavior changes must also bump the version and keep
all plugin manifests synchronized.

Tradeoff: "simple" is contextual. The skill therefore defines it as lower
cognitive load and fewer unnecessary moving parts, not minimum line count.

Bad: a genuinely complex requirement still produces complex code. The plugin
must not hide required complexity just to look minimal.

## Reversal

Revisit only if the maintainer explicitly changes the coding default or lifts
the one-command constraint.
