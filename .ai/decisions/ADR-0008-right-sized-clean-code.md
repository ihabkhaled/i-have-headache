# ADR-0008 — Right-sized clean code

*Status: accepted — 2026-09-29. Refines ADR-0007; preserves ADR-0002,
ADR-0005 and ADR-0006.*

## Context

Version 1.2.0 added a simple-code default. The maintainer then clarified that
"simple" must not become a rigid ban on abstractions, patterns, shared error
frameworks or broader refactors.

The real requirement is contextual:

- a user asking for a patch wants a patch, not an architecture rewrite;
- a user asking for a refactor wants the refactor done properly;
- a genuinely complex requirement may deserve abstractions or patterns;
- project conventions should win over a generic clean-code ideology;
- code should remain understandable from junior developer through CTO;
- useful planning and questions should happen before implementation when they
  can materially change the solution.

## Decision

The skill uses **right-sized engineering** rather than a fixed minimum-complexity
rule.

Before coding, determine the requested and necessary change shape: patch/minor
change, feature, refactor, or architectural change. Ask grouped questions when
their answers materially affect scope, design, behavior, risk or acceptance.

For an explicit patch or minor change, minimize touched surface and avoid
unrelated refactors. For an explicit or genuinely necessary refactor, use the
architecture required to leave the code clean and maintainable.

The following are flexible defaults, not contracts:

- follow repository conventions before generic preferences;
- use descriptive names and focused functions without arbitrary size limits;
- prefer clear control flow and guard clauses when they improve readability;
- create files and abstractions when they give a real responsibility or concept
  a clearer, more maintainable home;
- tolerate small simple duplication when extracting it would create a worse
  abstraction;
- use design patterns when the problem or codebase justifies them;
- prefer existing dependencies, but add a dependency when it materially
  improves the real solution;
- add defensive mechanisms for real requirements and risks, not imagined ones;
- follow the codebase's error-handling architecture, including generic/shared
  frameworks where conventional;
- keep comments small and focused on why or constraints;
- cover all relevant normal, edge, error, regression and integration cases for
  changed behavior;
- finish with one simplification pass without fighting the project's
  architecture.

## Why

The two failure modes are symmetrical:

1. **Over-engineering** — turning a local change into layers, patterns, files or
   dependencies the problem did not need.
2. **Under-engineering** — refusing a useful abstraction or real refactor just
   to keep the diff artificially small.

The skill should prevent both.

"Easy code" means easy to understand, change, debug and maintain for the current
system. It does not mean minimum line count, minimum file count or zero
architecture.

## Consequences

Good: patch requests remain patch-sized.

Good: clean architecture is still available when it genuinely improves the
solution or matches the existing codebase.

Good: the rules are explicit enough to guide an agent but flexible enough to
use engineering judgment.

Tradeoff: right-sizing requires reading the existing code and sometimes asking
the user before coding. That planning cost is intentional when it prevents the
wrong-sized implementation.

Release: this behavior refinement bumps the plugin from `1.2.0` to `1.3.0`.
All plugin manifests remain synchronized.

## Reversal

Revisit if the maintainer asks for strict mechanical limits instead of
context-sensitive engineering judgment.
