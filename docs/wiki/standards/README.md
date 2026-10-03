# Standards

<!-- akinator:generated:begin -->
<!-- Facts detected from the tree. This block is rewritten on every run;
     write outside it. Nothing here is guessed: every row names its file. -->

### Languages

| Detected | Where |
|---|---|
| Python (8 files) | `assets/make_logo.py`, `skills/i-have-headache/scripts/headache_version.py`, `tests/helpers.py` (+5 more) |
| Shell (3 files) | `hooks/prompt-reminder.sh`, `hooks/session-start.sh`, `install.sh` |
| PowerShell (1 file) | `install.ps1` |

### Linters, formatters and type checkers

Nothing detected.

### Pre-commit and git hooks

Nothing detected.

### Test frameworks

Nothing detected.

### CI

| Detected | Where |
|---|---|
| GitHub Actions workflows | `.github/workflows/ci.yml` |

### Ownership

Nothing detected.

### Import conventions

Nothing detected.

Regenerate with: `python <skill>/scripts/extract_platform.py --write`
<!-- akinator:generated:end -->

What this answers: languages, code standards, lint, hooks, imports, QA gates.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## Which code standards, lint rules, hooks, import rules and QA gates apply, and which are enforced by a tool?

One rule file per constraint under [.ai/rules](../../../.ai/rules/). Enforced by tool: tests (`python -m pytest tests -q`) and the CI `version` job. Shell scripts and Python files are pinned to LF in `.gitattributes`.
