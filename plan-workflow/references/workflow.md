# Plan Workflow Reference

## Repo-local override order

1. If the repository has `plans/README.md`, `plans/TEMPLATE.md`, or `plans/index.md`, follow those first.
2. If repo-local plan docs are missing, use the skill-local template and guidance in this skill directory.
3. If repo-local docs conflict with the skill defaults, repo-local docs win.

## Required status set

Use exactly one status value.

- `planned` - The slice is identified but not started.
- `in progress` - Work is actively underway.
- `ready to verify` - Implementation is in place and validation is next.
- `done` - Acceptance criteria and verification are complete.

## Completion standard

Do not stop at a partially executed slice unless the work is truly blocked by an external dependency or a repo decision.
A plan is not complete until the plan file, plan index, and matching roadmap item are all aligned.
