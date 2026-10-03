# Security

<!-- akinator:generated:begin -->
<!-- Facts detected from the tree. This block is rewritten on every run;
     write outside it. Nothing here is guessed: every row names its file. -->

### Secret handling

| Detected | Where |
|---|---|
| No `.gitignore` rule covers `.env` | `.gitignore` |

### Environment variable names

Nothing detected.

### Dependency and vulnerability scanning

Nothing detected.

### Authentication libraries

Nothing detected.

### Ownership and policy

Nothing detected.

Regenerate with: `python <skill>/scripts/extract_platform.py --write`
<!-- akinator:generated:end -->

What this answers: secret handling, auth, threat model.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## How are secrets handled, how do users and services authenticate, and what is the threat model?

No secrets, accounts or network calls at run time; the registry is [sensitive-data](sensitive-data.md). The installers touch only files that contain their own marker and never edit other user config.
