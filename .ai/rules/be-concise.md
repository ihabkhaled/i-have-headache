# Rule — be concise

The maintainer has a headache. Do not talk too much or make simple work
complicated.

Give the shortest complete answer that solves the request. Cut filler,
preambles, restatements of the request, long intros and conclusions,
over-explaining, repetition, and giant lists where a sentence works.

For code, start with the easiest correct solution. Prefer the smallest safe
change, clear control flow, existing patterns and existing dependencies. Avoid
unnecessary abstractions, layers, future-proofing and cleverness. After the code
works, simplify it once.

"Simple" does not override correctness, security, required tests or real
performance requirements. Readability matters more than minimum line count.

Expand only when explicitly asked.

This applies to agents *working on* this repository, not only to the command's
output. A verbose summary or an over-engineered two-line change misses the point
of the codebase.
