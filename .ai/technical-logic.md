# Technical logic

*Last verified: 2026-09-13*

## How it works

There is no code. The plugin is prompt text delivered through each platform's
native command mechanism. Invoking the command injects the text into the
conversation as a user-authored instruction, which steers the rest of the
session.

That is the whole mechanism. No runtime, no dependencies, no build, no tests to
run, nothing to install beyond copying files.

## The two delivery paths

| Platform | Mechanism | File |
|---|---|---|
| Claude Code | Plugin command | `commands/i-have-headache.md` |
| OpenAI Codex | Custom prompt | `.codex/prompts/i-have-headache.md` |

Both files carry the same body. They differ in exactly one way: the Claude Code
file has YAML frontmatter (`description:`) and the Codex file does not, because
Codex prompts have no frontmatter concept and would render it as literal text.

This duplication is deliberate — see
[ADR-0003](decisions/ADR-0003-duplicate-command-body.md). It is also the repo's
one real failure mode: edit one, forget the other, and the two platforms drift.
[skills/sync-command-bodies](../skills/sync-command-bodies/SKILL.md) exists
solely to prevent that.

## Claude Code packaging

`.claude-plugin/plugin.json` declares the plugin and points `commands` at
`./commands`. `.claude-plugin/marketplace.json` makes the repository serve as
its own single-plugin marketplace, so `/plugin marketplace add
ihabkhaled/i-have-headache` works without a separate marketplace repo.

Both manifests live in `.claude-plugin/`. A plugin manifest and a marketplace
manifest can coexist there; the repo is simultaneously the plugin and the
storefront that lists it.

## Codex packaging

Codex has no plugin installer. Installation is a file copy into
`~/.codex/prompts/`. The filename becomes the command name, which is why the
file must stay named `i-have-headache.md`.

## Why the command replies "Concise mode on."

The command body ends by instructing a fixed three-word acknowledgement. Without
it the assistant tends to confirm the instruction verbosely — violating the rule
in the act of accepting it. The fixed reply makes the first response a
demonstration.

## What would break this

| Change | Consequence |
|---|---|
| Renaming either command file | Breaks the command name on that platform |
| Adding frontmatter to the Codex file | Frontmatter renders as literal prompt text |
| Removing frontmatter from the Claude file | Command loses its description in the palette |
| Editing one body only | Silent cross-platform behavior drift |
| Moving `commands/` | Breaks `plugin.json`'s `commands` path |
