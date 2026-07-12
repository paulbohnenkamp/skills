---
name: feature-definition
description: Use when turning an idea, request, or rough feature note into a durable spec with problem, user story, scope, inputs, outputs, and acceptance criteria.
---

# Feature Definition

Use this skill when a request needs to become a stable spec before implementation planning.

## Core model

- A good spec captures the problem, not just the desired fix.
- A spec should be stable enough for planning and implementation to follow.
- Repo-local spec docs, if present, override the skill defaults for that repository.
- Skill-local references provide the fallback spec structure when repo-local spec docs are missing.
- A spec should separate intended behavior from execution details.
- Acceptance criteria should be concrete enough to verify later.

## First pass

1. Clarify the feature goal in one sentence.
2. Identify the user story or primary use case.
3. Check for repo-local spec docs first, such as `docs/specs/README.md` and `docs/specs/index.md`.
4. If repo-local spec docs exist, follow them for naming, placement, and tone.
5. If they do not exist, read [references/spec-guidance.md](references/spec-guidance.md).
6. List the important inputs, outputs, and constraints.
7. Define acceptance criteria that can be tested or reviewed.

## Working rule

- Keep the spec short and durable.
- Avoid implementation details unless they are part of the product requirement.
- Note out-of-scope items so the plan stays focused.
- If the request is vague, inspect available repository context first; ask only when a missing choice would materially change the spec.

## Completion rule

Consider a spec ready when:

- The problem statement is clear.
- The intended behavior is clear.
- Inputs and outputs are named.
- Acceptance criteria are explicit.
- The spec can support a downstream implementation plan.
