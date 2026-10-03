# Architecture

What this answers: the system, its modules, data and integrations.

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## What are the main components, how does data flow between them, and which external systems does it integrate with?

Text in, text out; no runtime service.

- One skill file, `skills/i-have-headache/SKILL.md`, is the only copy of the text.
- Claude Code: two hooks print it ([ADR-0006](../../../.ai/decisions/ADR-0006-always-on-one-source.md), [ADR-0009](../../../.ai/decisions/ADR-0009-prompt-submit-reminder-hook.md)).
- Codex and Cursor: the installers cut the same text into an AGENTS.md block and an `alwaysApply` rule.
- Version discipline is a script in the skill folder ([ADR-0010](../../../.ai/decisions/ADR-0010-version-discipline-in-the-one-skill.md)).

Detail: [technical logic](../../../.ai/technical-logic.md).
