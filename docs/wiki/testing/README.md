# Testing

What this answers: test strategy, coverage, user acceptance (UAT).

Part of the [project wiki](../index.md). One canonical home per fact -
link to it, never copy it. Current truth, history and future intent are
kept apart and labelled.

## What is the test strategy, what coverage is expected, and who signs off user acceptance?

`python -m pytest tests -q`: hooks (both events, exec form, exit 0), version tool (each invariant has a mutation test), installers in a temp home with the Claude CLI disabled, loud-contract markers, repo invariants. CI runs it on Linux and Windows.
