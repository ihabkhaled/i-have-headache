# Changelog

Newest first. Every change to a shipped path bumps the version and adds a
section here - `skills/i-have-headache/scripts/headache_version.py check`
enforces it (see [.ai/rules/version-discipline.md](.ai/rules/version-discipline.md)).

## [1.4.0] - 2026-10-03

### Added
- UserPromptSubmit hook: three short loud lines on every prompt, so concise mode
  is re-asserted each turn and cannot drift. SessionStart keeps no matcher.
- Version discipline inside the one skill:
  `skills/i-have-headache/scripts/headache_version.py` (show, check, next, bump,
  set), a CI step, and a rule. No new command.
- `CHANGELOG.md`, tests (`tests/`) and CI (`.github/workflows/ci.yml`).
- Wiki under `docs/wiki/`, change record, ADR-0009, ADR-0010.

### Changed
- The 5-bullet cap and the other hard limits govern chat replies only; the
  clean-code rules from 1.3.0 govern generated code.
- The contract is loud and countable (NOT OPTIONAL, at most 5 short bullets for
  a summary, no tables or ids) in the skill, both hooks, the Codex block and the
  Cursor rule, after a polite contract was ignored.
- README is short and install-first.
- The Codex block and Cursor rule say no command is needed.

### Fixed
- `--uninstall` / `-Uninstall` left behind the downloaded source cache
  (`~/.i-have-headache/src`) and the Claude marketplace entry; both are removed.

## [1.3.0] - 2026-09-29

### Changed
- Right-sized clean-code rules in the same skill: match the engineering to the
  real task (patch stays a patch, a real refactor is done properly), project
  conventions first, one simplification pass (ADR-0007, ADR-0008).

## [1.2.0] - 2026-09-29

### Added
- Simple-first coding default in the same skill.

## [1.1.0] - 2026-09-19

### Changed
- Always on: one skill, which is also the one command; concise mode is injected
  at every session start on every platform.
- One-line installers for Claude Code, Codex and Cursor.
- Shell scripts pinned to LF; the always-on rules are extracted with CR stripped.

## [1.0.0] - 2026-09-13

### Added
- The `/i-have-headache` command, with Cursor support, icons and a knowledge layer.
