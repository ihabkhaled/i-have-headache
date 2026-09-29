# Memory

*Last verified: 2026-09-29*

## 2026-09-29 — clean-code rules are flexible and scope-aware

The maintainer clarified the simple-code direction after 1.2.0.

The core rule is not "avoid abstractions." It is: understand what was requested,
plan the right size, and use the amount of engineering the task really needs.

Explicit patch/minor work should minimize touched surface and avoid unrelated
refactors. Explicit refactor work should be allowed to refactor properly.
Abstractions and patterns are valid when they improve maintainability or clean
architecture. Shared/generic error handling should follow project conventions.
Defensive mechanisms belong when real work needs them.

Functions should be focused without arbitrary line limits. Names should be
descriptive. Comments should be small, not large narrative blocks. Tests should
cover all relevant cases.

Questions and planning happen before code when answers materially affect the
solution. These are flexible engineering defaults, not rigid contracts.

This ships as 1.3.0. See ADR-0008.

Reverses when: the maintainer explicitly replaces the context-sensitive coding
policy.

## 2026-09-29 — behavior changes bump the version

The maintainer explicitly requires a version bump whenever user-facing plugin
behavior changes. Keep the Claude plugin, Claude marketplace and Cursor manifest
versions identical. The simple-code behavior shipped as `1.2.0`; the
right-sized clean-code refinement ships as `1.3.0`.

Reverses when: the maintainer explicitly changes the release/versioning policy.

## 2026-09-29 — simple code belongs in the same skill

The maintainer explicitly asked to keep the same `/i-have-headache` skill and
the same one-command product while adding a coding default: easiest correct
solution first, junior-to-CTO readable code, smallest safe changes, no
over-engineering, no speculative complexity, and one simplification pass after
the solution works.

ADR-0008 later refined "smallest safe changes" into a scope-aware rule: patch
requests stay narrow, but requested or necessary refactors are allowed to be
proper refactors.

This extends `skills/i-have-headache/SKILL.md`; it does not create a second
skill, command, mode or configuration surface.

## 2026-09-19 — always on, at the maintainer's request

"No need to write down /i-have-headache" meant: concise without typing anything.
Asked and confirmed before building. Concise mode is now injected every session
(ADR-0006); the acknowledgement stays for explicit runs only, or every session
would open with it.

Reverses when: the maintainer asks for opt-in back.

## 2026-09-13 — one command is a hard product invariant

The maintainer specified "one single command only" with unusual force and
repetition. Read that emphasis as the specification itself, not as venting.
Treat every "small option" proposal as out of scope by default.

Reverses when: the maintainer explicitly lifts it. Not on accumulated feature
requests.

## 2026-09-13 — the headache is literal, and it is the spec

"I have a headache, don't talk too much" is a standing instruction for agents
working in this repo, not only the behavior the command produces. Verbose
summaries of trivial changes are a defect here.

## 2026-09-13 — installed locally from the working directory

The plugin is installed at user scope from a directory-source marketplace
pointing at this working tree, not at GitHub. Edits to the command file take
effect on restart with no reinstall — convenient locally, but it means a local
install can silently differ from what is pushed. Verify with `git status` before
concluding a behavior came from the published version.

Reverses when: reinstalled from the GitHub source.

## 2026-09-13 — knowledge layer added deliberately, against first instinct

An earlier pass judged a full knowledge layer to be overkill for a four-file
repo and said so. The maintainer overrode that. Do not re-litigate it or propose
trimming `.ai/` as cleanup — it is wanted.

## 2026-09-13 — a plugin skill IS a user-facing command

A `skills/` directory was added and immediately produced a second palette entry,
`/i-have-headache:sync-command-bodies`, breaking the one hard invariant.

Corrected 2026-09-13: OpenAI submission requires at least one skill. The real
invariant is **one user-facing name**. Exactly one skill exists, named
`i-have-headache` like the command. A differently-named skill would create a
second entry. See ADR-0005.

Reverses when: a platform offers a private, non-palette instruction slot —
verified on every target platform, not just one.
