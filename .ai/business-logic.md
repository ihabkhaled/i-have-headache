# Business logic

*Last verified: 2026-09-13*

## The problem being sold

AI coding assistants default to verbose. They restate the request, explain what
they are about to do, do it, explain what they did, then offer next steps. For a
user who already knows what they want, that is noise — and on a bad day it is
physically unpleasant to read.

The name is literal. This exists for the moment when you have a headache and the
assistant will not shut up.

## The product rule

**One command. `/i-have-headache`. Nothing else.**

This is the entire product. It is also the entire constraint. See
[ADR-0002](decisions/ADR-0002-one-command-only.md) for why it is inviolable.

The value is not the prompt text — anyone can write "be concise." The value is
that there is nothing to learn, configure, or choose. Zero decisions between
headache and relief.

## Who it is for

Someone mid-task, already annoyed, who will not read documentation. If using it
requires reading anything, it has failed.

## Success criteria

| Criterion | Met when |
|---|---|
| Zero learning cost | The command name is the entire instruction |
| Zero configuration | No settings, no arguments, no setup step |
| Works everywhere | Identical behavior in Claude Code, Cursor and Codex |
| Reversible | Asking for detail restores normal verbosity, no second command needed |

## Explicit non-goals

- Persistence across sessions. Concise mode lasts the session; a new session
  starts normal. Making it sticky would need config, which would need a command.
- Adjustable verbosity levels. That is a flag. Flags are forbidden.
- A way to turn it off. Ask for more detail in plain language instead.
- Any platform beyond Claude Code, Cursor and Codex, unless someone asks.

## Money, entitlements, limits

None. No pricing, no quotas, no thresholds, no user data, no network calls, no
telemetry. The plugin is three text files and a manifest. Nothing here can cost
anyone money or break a commercial commitment.
