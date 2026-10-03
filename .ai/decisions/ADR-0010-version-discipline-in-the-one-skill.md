# ADR-0010 - Version discipline lives in the one skill

*Status: accepted - 2026-10-03. Clarifies ADR-0005.*

## Context

Shipped changes went out under the same version (a 1.1.0 install could differ
from 1.1.0 on GitHub), and the manifests were edited by hand. Claude Code
updates an installed plugin only when the version changes, so a forgotten bump
means users never receive the change.

## Options

**A. A new skill or command for releasing.** Rejected: a second user-facing
entry, forbidden by ADR-0002 and ADR-0005.

**B. A document of manual steps.** Cost: it is forgotten.

**C. A script inside the existing skill folder plus a CI step.** The script is
not a skill and not a command: only `SKILL.md` makes an entry, and a `scripts/`
folder adds none (live check: one slash command).

## Decision

Option C. `skills/i-have-headache/scripts/headache_version.py` (stdlib Python)
with `show`, `check [--base REF]`, `next`, `bump`, `set`. `check` fails when
manifests disagree, or when a shipped path changed since REF without a strictly
greater version and a `## [x.y.z]` CHANGELOG section. `bump` takes `--date` and
reads no clock. The CI `version` job runs it. Rule:
[version-discipline](../rules/version-discipline.md).

The skill gets one maintainer-only line after its acknowledgement block, so the
tool is part of the one skill and is not injected into sessions (the always-on
text stops at `Concise mode is always on`).

Consequence: `scripts/` ships to Codex and Cursor in the copied skill folder;
`SKILL.md` stays under Codex's 8,000 byte limit.
