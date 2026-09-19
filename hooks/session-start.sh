#!/bin/sh
# i-have-headache SessionStart hook: concise mode is always on.
#
# Prints the skill's rules - everything below its frontmatter, up to the line
# that starts the acknowledgement - so the skill stays the only copy of the
# text. The acknowledgement is for an explicit run of the command only.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
SKILL="$HERE/../skills/i-have-headache/SKILL.md"
[ -f "$SKILL" ] || exit 0
awk '
  { sub(/\r$/, "") }
  NR == 1 && /^---$/ { front = 1; next }
  front && /^---$/ { front = 0; next }
  front { next }
  /^Concise mode is always on/ { exit }
  { print }
' "$SKILL"
exit 0
