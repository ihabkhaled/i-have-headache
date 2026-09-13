# Syncing the command bodies

*Last verified: 2026-09-13*

This is a procedure, deliberately **not** a skill. Skills in a plugin directory
are surfaced as slash commands, and this repo ships exactly one command. See
[ADR-0005](decisions/ADR-0005-no-skills-directory.md).

| File | Frontmatter | Read by |
|---|---|---|
| `commands/i-have-headache.md` | yes — source of truth | Claude Code, Cursor |
| `.codex/prompts/i-have-headache.md` | no | Codex |

Cursor shares the first file, so there are three platforms but only two files.

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

4. Commit both files together.

## Checklist

- [ ] The `diff` in step 3 is empty.
- [ ] The Codex file has no YAML frontmatter — Codex renders it as literal text.
- [ ] The Claude/Cursor file keeps both `name:` and `description:`. Cursor
      resolves the command from `name:`; dropping it breaks Cursor silently.
- [ ] Neither file was renamed; the filename is the command name.
- [ ] `ls commands/ .codex/prompts/` still shows one file each.

Why duplication instead of a build step:
[ADR-0003](decisions/ADR-0003-duplicate-command-body.md).
