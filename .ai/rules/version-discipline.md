# Rule - every shipped change bumps the version

Enforces [ADR-0010](../decisions/ADR-0010-version-discipline-in-the-one-skill.md).

A change to a shipped path - `skills/**`, `hooks/**`, `install.sh`,
`install.ps1`, `.claude-plugin/**`, `.codex-plugin/**`, `.cursor-plugin/**`, `.agents/**`,
`agents/**`, `templates/**` - ships with:

1. a strictly greater version in every manifest, and
2. a `## [x.y.z] - date` section in `CHANGELOG.md`.

Do it with the tool, never by hand:

```bash
T=skills/i-have-headache/scripts/headache_version.py
python $T next                      # which level, and why
python $T bump minor --date YYYY-MM-DD   # manifests + changelog skeleton
python $T check --base origin/main  # what CI runs
```

Manifests must agree at all times (`check` without `--base`). This adds no
command: it is a script in the skill folder, not a skill.
