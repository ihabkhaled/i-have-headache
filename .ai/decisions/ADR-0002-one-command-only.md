# ADR-0002 — Exactly one user-facing command, permanently

*Amended 2026-09-19 by [ADR-0006](ADR-0006-always-on-one-source.md): concise mode is always on at the maintainer's request. Still exactly one command.*

*Status: accepted — 2026-09-13*

## Context

The obvious feature requests write themselves: `/i-have-headache off`,
`--level=terse`, a config file for default verbosity, a `/headache-status`
check. Each is individually reasonable and cheap.

## Options

**A. Add options as requested.** Standard product evolution. Cost: the product
is *not having to think*. A user with a headache who must choose between
`--terse` and `--brief` has been handed a decision at the exact moment they
wanted zero decisions. Each option is cheap; the sum is the thing the product
exists to avoid.

**B. Freeze at one command.** No second command, subcommand, alias, flag,
argument, mode, or setup step, ever. Cost: real requests get declined, and
turning concise mode off requires plain language instead of a command.

## Decision

Option B, and it is treated as a product invariant rather than a default.

The maintainer specified this in unusually forceful terms. That emphasis is
itself the requirement: the constraint is the feature.

## Consequences

Good: nothing to learn, configure, or choose. The command name is the entire
documentation.

Bad: legitimate requests will be refused. "Let me set a default level" has no
answer and will not get one.

Bad: turning it off means saying "give me more detail" in plain language. This
is slightly worse than a command and is accepted deliberately.

Bad: contributors will propose second commands in good faith. Every agent
config file in this repo restates the rule so the answer arrives before the PR.

## Revisit when

The maintainer explicitly says so, in the same forceful terms. Not on the
strength of an accumulated feature-request backlog — that backlog is the
predicted outcome, not new information.
