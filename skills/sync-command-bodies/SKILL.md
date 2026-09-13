---
name: sync-command-bodies
description: Use when editing the text of the /i-have-headache command, or when Claude Code and Codex appear to behave differently — keeps the two command bodies identical.
---

# Sync command bodies

Two files carry the same prompt. They must stay identical below the frontmatter.

| File | Frontmatter | Read by |
|---|---|---|
| `commands/i-have-headache.md` | yes — source of truth | Claude Code, Cursor |
| `.codex/prompts/i-have-headache.md` | no | Codex |

Cursor shares the first file, so there are three platforms but only two files.

## When to use

- Changing the wording of the `/i-have-headache` command.
- Claude Code, Cursor or Codex behave differently after the same command.
- Reviewing any diff that touches either file.

## When not to use

- Editing agent instructions — that is `AGENTS.md`, and no sync applies.
- Adding docs, rules or ADRs under `.ai/`.
- Adding a second command. That is forbidden outright; see
  [ADR-0002](../../.ai/decisions/ADR-0002-one-command-only.md).

## Procedure

1. Edit `commands/i-have-headache.md`. Never hand-edit the Codex file.
2. Regenerate the Codex copy:

   ```bash
   sed '1{/^---$/!q}; 1,/^---$/d; /./,$!d' commands/i-have-headache.md \
     > .codex/prompts/i-have-headache.md
   ```

3. Verify no drift:

   ```bash
   diff <(sed '1{/^---$/!q}; 1,/^---$/d; /./,$!d' commands/i-have-headache.md) \
        .codex/prompts/i-have-headache.md && echo "in sync"
   ```

4. Commit both files together. A commit touching only one is the bug this skill
   exists to prevent.

## Definition of done

- [ ] The `diff` in step 3 is empty.
- [ ] The Codex file has no YAML frontmatter — Codex renders it as literal text.
- [ ] The Claude/Cursor file still has both `name:` and `description:` in its
      frontmatter. Cursor resolves the command from `name:`; dropping it breaks
      Cursor silently.
- [ ] Neither file was renamed; the filename is the command name on both
      platforms.
- [ ] Both files are in the same commit.
- [ ] Still exactly one command per platform:
      `ls commands/ .codex/prompts/` shows one file each.

## Constraints

Why duplication instead of a build step:
[ADR-0003](../../.ai/decisions/ADR-0003-duplicate-command-body.md).
