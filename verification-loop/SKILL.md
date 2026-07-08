---
name: verification-loop
description: Use when you need to verify that a slice is actually done by selecting, running, and interpreting the right checks.
---

# Verification Loop

Use this skill when a change needs explicit validation before it can be marked complete.

## Core model

- Verification should match the size and risk of the change.
- The best checks are the ones that prove the intended behavior, not just that the code compiles.
- A verification loop should end with a clear pass/fail judgment and a short explanation.

## First pass

1. Identify the acceptance criteria or behavior that must be proved.
2. Select the smallest useful checks that cover that behavior.
3. Run the checks and capture the result.
4. Note any gaps that remain if the checks do not fully prove completion.

## Working rule

- Prefer deterministic checks when they exist.
- Keep verification steps explicit and repeatable.
- Separate local build health from feature-specific proof.
- If the first check fails, narrow the failure before broadening the search.

## Completion rule

Consider a slice verified when:

- The relevant checks pass.
- The result lines up with the acceptance criteria.
- Any known gaps are documented clearly.

## Good triggers

- "Verify this slice"
- "Run the checks"
- "Confirm the feature is done"
- "Interpret the test failure"

