---
name: plan-workflow
description: Use when turning a feature spec or idea into a durable implementation plan with scope, steps, verification, and status tracking.
---

# Plan Workflow

Use this skill when a repository tracks implementation work in plan files.

## Core model

- A spec or feature brief defines the target behavior.
- A plan defines how to build it in a durable, session-resumable way.
- Repo-local plan docs, if present, override the skill defaults for that repository.
- Skill-local references provide the fallback workflow when repo-local plan docs are missing.
- A plan index tracks active work and completion state.
- A roadmap or release tracker is updated after the plan is verified.

## First pass

1. Read the spec or source brief.
2. Check for repo-local plan docs first: `plans/README.md`, `plans/TEMPLATE.md`, and `plans/index.md`.
3. If repo-local plan docs exist, follow them.
4. If they do not exist, use the skill-local references in `references/` and any templates in `assets/`.
5. Identify the smallest useful slice.
6. Write or update the plan with goal, related roadmap item, context, scope, steps, acceptance criteria, verification, status, completion notes, outcome summary, and tooling notes.

## Working rule

- Keep plans focused on execution, not product brainstorming.
- Make the verification path explicit.
- Use the documented status lifecycle exactly.
- Work the slice until it is done or a real external blocker is recorded.
- Record completion notes, outcome summary, and tooling notes after the slice is done or ready to verify.

## Completion rule

Mark a plan done only when:

- Acceptance criteria are satisfied.
- Required checks or tests have passed.
- The active plan index reflects the completed status.
- Any matching roadmap item is updated.
- The plan file itself includes completion notes and an outcome summary.

## Good triggers

- "Turn this spec into a plan"
- "Write the implementation plan"
- "Update the plan and verification"
- "Mark the slice complete"
