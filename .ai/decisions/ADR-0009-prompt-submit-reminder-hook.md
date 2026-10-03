# ADR-0009 - Re-assert concise mode on every prompt

*Status: accepted - 2026-10-03. Amends ADR-0006.*

## Context

The maintainer's requirement: concise mode must always be followed, with no
slash command ever typed. ADR-0006 injects the rules once, at SessionStart. In a
long session that text sits far behind the conversation and the model drifts
back to verbose.

## Options

**A. SessionStart only.** Cost: drift in long sessions.

**B. Add a UserPromptSubmit hook** that prints one short line per prompt. Cost:
one more hook script, a few tokens per turn.

**C. Re-inject the full rules every prompt.** Cost: hundreds of tokens per turn,
which is the verbosity this product exists to remove.

## Decision

Option B. `hooks/prompt-reminder.sh` prints three short loud lines (the
`NOT OPTIONAL` headline and the numeric limits) and exits 0; it reads nothing and
stays instant. Both hooks
are exec form (`command: sh`, `args: [...]`). SessionStart keeps **no matcher**
so it fires on startup, resume, clear and compact.

The full rules still live in one file, the skill; the reminder is a pointer, not
a second copy. Codex and Cursor already load the rules on every turn (AGENTS.md
block, `alwaysApply` rule), so they need nothing more.

## Amendment - 2026-10-03, the contract must be loud and countable

A polite "be concise" was ignored: a summary request got ~25 lines, tables and
seven numbered problems until the owner shouted. The skill now opens with an
all-caps headline, tough-love aimed at the AI only, and hard limits with a
number: summary or status = at most 5 short bullets under 12 words, no tables,
ids or paths, count before sending. The text lives once in the skill; the
SessionStart hook, Codex block and Cursor rule derive from it; the per-prompt
hook restates it in three lines. `tests/test_loud.py` and the installer tests
fail if `NOT OPTIONAL` or `5 short bullets` leaves any of them.

## Evidence

Run live with `claude --plugin-dir . -p hi --output-format stream-json --verbose
--include-hook-events`: `hook_response` for both events, exit 0, and
`slash_commands` listed one entry for this plugin, `i-have-headache:i-have-headache`.
`tests/test_hooks.py` proves each part fires.
