# Business logic

*Last verified: 2026-09-29*

## The problem being sold

AI coding assistants can fail in two opposite directions.

They can over-engineer small work: a local patch becomes abstractions, files,
patterns, configuration and future-proofing the user never asked for.

They can also under-engineer real work: a meaningful refactor or architectural
change gets forced into a tiny diff that is harder to maintain because the agent
is trying to look "simple."

For a user who already knows what they want, both are noise and maintenance
cost. The product should choose the amount of engineering the actual task needs.

The name is literal. This exists for the moment when you have a headache and the
assistant will not stop talking or turns straightforward work into something
harder than it needs to be.

## The product rule

**Always on. One skill, which is also the one command. Nothing else.**

Since 2026-09-19 nothing has to be typed: concise mode applies to every session
([ADR-0006](decisions/ADR-0006-always-on-one-source.md)).

Version 1.2.0 added simple-first coding
([ADR-0007](decisions/ADR-0007-simple-code-same-skill.md)). Version 1.3.0 refines
that into right-sized clean code
([ADR-0008](decisions/ADR-0008-right-sized-clean-code.md)): understand the task,
read the project, ask useful questions when needed, then match the implementation
size to the real scope.

The command remains an explicit re-assert.

The value is not a universal clean-code doctrine. The value is removing bad
choices at both extremes: needless complexity on small work and artificial
minimalism on work that really needs structure.

## Who it is for

Someone mid-task who wants an answer or code without ceremony, but still wants
good engineering judgment.

A patch should not become a redesign. A refactor should not be crippled just to
keep the diff small. The next junior, senior or CTO should be able to understand
why the code is shaped the way it is.

## Success criteria

| Criterion | Met when |
|---|---|
| Zero learning cost | The command name is the entire instruction |
| Zero configuration | No settings, arguments or modes |
| Works everywhere | Identical behavior in Claude Code, Cursor and Codex |
| Right-sized change | Implementation depth matches the requested and necessary scope |
| Project-native code | Existing conventions, architecture and error/testing styles are followed |
| Readable code | Names, control flow, responsibilities and files are easy to follow |
| Useful architecture | Abstractions and patterns exist when they improve the real solution, not by reflex |
| Complete verification | All relevant normal, edge, error, regression and integration cases are covered |
| Reversible verbosity | Asking for detail restores normal verbosity without a second command |

## Explicit non-goals

- A setting to make it opt-in again. Uninstalling is the global off.
- Adjustable coding-complexity levels. Those would be modes or flags.
- A separate clean-code, architecture, refactor or simplicity command.
- Mechanical limits for function length, file count, abstraction count or line
  count.
- Banning design patterns, shared error frameworks, defensive code or
  dependencies when the actual problem or project architecture needs them.
- Refactoring unrelated code during a patch just because it could be cleaner.
- Any platform beyond Claude Code, Cursor and Codex, unless someone asks.

## Money, entitlements, limits

None. No pricing, quotas, thresholds, user data, network calls or telemetry.
The plugin is prompt text, installers, hooks and manifests.
