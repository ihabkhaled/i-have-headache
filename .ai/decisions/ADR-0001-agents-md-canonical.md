# ADR-0001 — AGENTS.md is canonical; every other agent file is a pointer

*Status: accepted — 2026-09-13*

## Context

The repo needs instructions for many AI tools: Claude Code, Codex, Cursor,
Copilot, Windsurf, Cline, Gemini, Kimi, Qwen, Grok. Each reads a different
filename. All of them need the same two facts: be concise, and never add a
second command.

## Options

**A. Full copy in every file.** Each tool gets complete standalone instructions.
Works offline per-tool, no indirection. Cost: ten copies of the same text. The
first edit that misses one file creates a repo where Cursor and Claude disagree
about the rules, silently, forever. With ten files, drift is not a risk — it is
a schedule.

**B. One canonical file, thin pointers.** `AGENTS.md` holds everything; each
tool-specific file is a link plus the short list of rules whose omission
actually causes damage. Cost: one hop of indirection, and a tool that cannot
follow a relative link gets only the summary.

## Decision

Option B. `AGENTS.md` is canonical.

`AGENTS.md` is the emerging cross-tool convention and several agents read it
natively, so the canonical file is also directly useful rather than being pure
indirection.

Each pointer restates three things verbatim rather than only linking: be
concise, never add a second command, and sync the two command bodies when
editing the command text. If a tool never follows the link, it still gets the
parts whose omission causes damage.

The third was added after a coverage check flagged the pointers as forked
routers. It was right: an agent reading only `CLAUDE.md` would never learn the
sync obligation, which is this repo's most likely bug.

## Consequences

Good: one place to edit. Contradictions between tools become structurally
impossible for everything except the two duplicated rules.

Bad: an agent that reads only `.clinerules` sees a four-line summary, not the
full layout and workflow. Accepted — the summary contains the rules that cause
damage when violated.

Bad: three rules are now duplicated across ~12 files. If they ever change, all
must change together. Mitigated by their being genuinely fixed product
requirements rather than preferences — and by `router-sync` in the coverage
check, which fails when one pointer omits what the others carry.

The pointers are therefore not as thin as originally intended. Any further
addition should reopen this ADR rather than accrete quietly — the failure mode
is pointers slowly becoming copies, which is exactly Option A.

## Revisit when

A tool-specific instruction is needed that does not apply to other tools, or
`AGENTS.md` support becomes universal enough to delete the pointers.
