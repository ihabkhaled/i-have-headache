# Rule — be concise and right-size the code

The maintainer has a headache. Do not talk too much or make the code harder than
the real task requires.

Give the shortest complete answer that solves the request. Cut filler,
preambles, restatements, long intros and conclusions, over-explaining,
repetition, and giant lists where a sentence works.

For code, determine the scope before the design. An explicit patch stays narrow;
an explicit or genuinely necessary refactor is allowed to refactor properly.

Follow project conventions. Prefer descriptive names, focused functions, clear
control flow, sensible file organization and readable responsibilities.

Abstractions, patterns, dependencies, defensive mechanisms and shared error
frameworks are neither forbidden nor required. Use them when the real problem,
maintainability or existing architecture justifies them. Do not add them merely
to make a small change look sophisticated.

Ask grouped questions when the answers materially change the implementation.
Do not interrupt for trivial choices.

Keep comments small and useful. Cover all relevant normal, edge, error,
regression and integration cases for changed behavior.

After the solution works, simplify it once without removing architecture that is
actually earning its keep.

These are flexible defaults, not mechanical limits. Correctness, security,
maintainability, project conventions and the user's explicit scope win.

This applies to agents *working on* this repository, not only to the command's
output.
