# Business logic

*Last verified: 2026-09-29*

## The problem being sold

AI coding assistants default to verbose. They restate the request, explain what
they are about to do, do it, explain what they did, then offer next steps. They
also often turn straightforward code into abstractions, layers and future-proofing
that the current problem did not ask for.

For a user who already knows what they want, both are noise: more to read, more
code to review, and more code to maintain.

The name is literal. This exists for the moment when you have a headache and the
assistant will not shut up or stop making simple work complicated.

## The product rule

**Always on. One skill, which is also the one command. Nothing else.**

Since 2026-09-19 nothing has to be typed: concise mode applies to every session
([ADR-0006](decisions/ADR-0006-always-on-one-source.md)). Since 2026-09-29 the
same skill also defaults coding work to the easiest correct, maintainable
implementation ([ADR-0007](decisions/ADR-0007-simple-code-same-skill.md)). The
command remains an explicit re-assert.

This is the entire product. It is also the entire constraint. See
[ADR-0002](decisions/ADR-0002-one-command-only.md) for why it is inviolable.

The value is not the prompt text — anyone can write "be concise" or "keep it
simple." The value is that there is nothing to learn, configure, or choose. Zero
decisions between headache and relief.

## Who it is for

Someone mid-task, already annoyed, who wants the answer or code without ceremony.
If using it requires reading anything, choosing a mode, or cleaning up
unnecessary architecture afterward, it has failed.

## Success criteria

| Criterion | Met when |
|---|---|
| Zero learning cost | The command name is the entire instruction |
| Zero configuration | No settings, no arguments, no setup step |
| Works everywhere | Identical behavior in Claude Code, Cursor and Codex |
| Simple code | The easiest correct maintainable solution is considered before a complicated one |
| Minimal change | Unrelated refactors and speculative abstractions are avoided |
| Reversible | Asking for detail restores normal verbosity, no second command needed |

## Explicit non-goals

- A setting to make it opt-in again. Uninstalling is the global off.
- Adjustable verbosity or coding-complexity levels. Those are modes or flags.
- A separate clean-code, architecture, refactor or simplicity command.
- Maximum line-count reduction. Readability and maintainability matter more.
- Avoiding necessary complexity when correctness, security, tests or real
  performance requirements demand it.
- Any platform beyond Claude Code, Cursor and Codex, unless someone asks.

## Money, entitlements, limits

None. No pricing, no quotas, no thresholds, no user data, no network calls, no
telemetry. The plugin is prompt text, installers, hooks and manifests. Nothing
here can cost anyone money or break a commercial commitment.
