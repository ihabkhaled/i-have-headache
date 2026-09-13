# Memory

*Last verified: 2026-09-13*

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
