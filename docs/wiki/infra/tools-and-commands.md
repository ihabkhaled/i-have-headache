# Tools and commands

<!-- akinator:generated:begin -->
<!-- Facts extracted from the tree. This block is rewritten on every run;
     write outside it. -->
### Commands

| Command | What | Where defined |
|---|---|---|
| `CI job test` | - | `.github/workflows/ci.yml` |
| `CI job version` | - | `.github/workflows/ci.yml` |
| `python skills/i-have-headache/scripts/headache_version.py` | Version discipline for i-have-headache: one version, every manifest, a changelog. | `skills/i-have-headache/scripts/headache_version.py` |

### Required CLI tools

| Tool | Implied by |
|---|---|
| `gh` | `.github` |
| `git` | `.git`, `.github/workflows/ci.yml` |
| `python` | `.github/workflows/ci.yml`, `skills/i-have-headache/scripts/headache_version.py` |

Regenerate with: `python <skill>/scripts/extract_operations.py --write`
<!-- akinator:generated:end -->

## Notes on tools and commands

Release: `python skills/i-have-headache/scripts/headache_version.py next|bump|check` ([rule](../../../.ai/rules/version-discipline.md)). Test: `python -m pytest tests -q`. Logo: `python assets/make_logo.py`.
