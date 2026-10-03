# 2026-10-03 - always followed, version discipline (1.4.0)

**Before.** Concise mode was injected once per session; versions were
hand-edited and no changelog existed; `--uninstall` left the downloaded source
cache `~/.i-have-headache/src` and the Claude marketplace entry behind; no tests,
no CI.

**Change.**
- `hooks/prompt-reminder.sh` and a `UserPromptSubmit` entry in `hooks/hooks.json`
  ([ADR-0009](../../.ai/decisions/ADR-0009-prompt-submit-reminder-hook.md)).
- `skills/i-have-headache/scripts/headache_version.py`, a CI `version` job and
  the `version-discipline` rule
  ([ADR-0010](../../.ai/decisions/ADR-0010-version-discipline-in-the-one-skill.md)).
- Both installers: uninstall removes the cache, the marketplace entry and an
  emptied `~/.codex`; the AGENTS.md block, the Cursor rule and the final message
  say no command is needed.
- `tests/`, `.github/workflows/ci.yml`, `CHANGELOG.md`, `docs/wiki/`, a short
  install-first README.
- Rebased onto the owner's 1.3.0 clean-code release; set to 1.4.0 via `headache_version.py set`. The tool now also covers `.cursor-plugin/plugin.json`. The 5-bullet cap governs chat replies; the clean-code rules govern code.

- Incident the same day: a long answer (about 25 lines, tables, seven numbered
  problems) to a summary request despite the plugin. The skill, hooks, Codex
  block and Cursor rule are now loud with hard limits (5 short bullets);
  `tests/test_loud.py` pins them.

**Now.** Every prompt carries a short loud reminder; a shipped change cannot merge
without a bump and a changelog entry; uninstall leaves nothing.

**Why.** The maintainer's requirement that the plugin is followed without ever
typing the command, and that every release is versioned and documented.

**Verified.** Live hook run (both events, exit 0, one slash command);
`python -m pytest tests -q`; `headache_version.py check`; a fresh clone of the
commit.
- `tests/test_hooks.py`: the session-start line cap became "no acknowledgement text, under 8,000 bytes" because the clean-code rules lengthened the injected rules.
