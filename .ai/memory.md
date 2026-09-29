# Memory

*Last verified: 2026-09-29*

## 2026-09-29 — behavior changes bump the version

The maintainer explicitly requires a version bump whenever user-facing plugin
behavior changes. Keep the Claude plugin, Claude marketplace and Cursor manifest
versions identical. The simple-code behavior ships as `1.2.0`.

Reverses when: the maintainer explicitly changes the release/versioning policy.

## 2026-09-29 — simple code belongs in the same skill

The maintainer explicitly asked to keep the same `/i-have-headache` skill and
the same one-command product while adding a coding default: easiest correct
solution first, junior-to-CTO readable code, smallest safe changes, no
over-engineering, no speculative complexity, and one simplification pass after
the solution works.

This extends `skills/i-have-headache/SKILL.md`; it does not create a second
skill, command, mode or configuration surface. See ADR-0007.

Reverses when: the maintainer explicitly asks for a different default or lifts
the one-command constraint.

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
`/i-have-headache:sync-command-bodies`, breaking the one hard invariant. Plugin
skills are surfaced as slash commands by Claude Code, Cursor and the OpenAI
submission scanner alike.

Corrected 2026-09-13: OpenAI submission *requires* at least one skill, so the
ban was wrong. The real invariant is **one user-facing name**. Exactly one
skill exists, named `i-have-headache` like the command, which adds no palette
entry. A differently-named skill would. See ADR-0005.

Reverses when: a platform offers a private, non-palette instruction slot —
verified on every target platform, not just one.
