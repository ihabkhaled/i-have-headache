#!/bin/sh
# i-have-headache UserPromptSubmit hook: three short loud lines per prompt, so
# the limits are restated every turn and cannot drift. Must stay instant.
printf '%s
'   "HEADACHE MODE IS NOT OPTIONAL. SHORT MEANS SHORT."   "Summary or status: at most 5 short bullets, under 12 words each. No tables, ids, paths, preamble, recap or closing offer."   "Count your bullets before sending. Over 5? Cut."
exit 0
