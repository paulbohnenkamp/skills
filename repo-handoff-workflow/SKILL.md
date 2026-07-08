---
name: repo-handoff-workflow
description: Use when working in a code repository that separates reference docs from active plans and needs durable handoff between sessions.
---

# Repo Handoff Workflow

Use this skill when a repository has durable reference docs and active implementation plans.

## Core model

- Reference docs explain the product, architecture, and intended behavior.
- Plan files explain the active implementation handoff.
- A plan index is the resume point for continuing work later.
- Roadmap items are checked off only after the matching plan is done and verified.

## First pass

1. Find the repository entry points for working instructions, roadmap, specs, and active plans.
2. Identify where the repo says to resume work.
3. Read the spec or equivalent reference doc for the feature you are working on.
4. Read the plan template and active plan entry for that work.

## Working rule

- Update reference docs when product intent or stable behavior changes.
- Update plans when execution details, status, or verification change.
- Keep specs and plans separate even when they refer to the same feature.

## Completion rule

Mark work complete only when:

- The plan acceptance criteria are satisfied.
- Required tests or checks pass.
- The plan index is updated.
- The roadmap item is checked off.

## Good triggers

- "Pick up where we left off"
- "Continue the next slice"
- "Update the plan and roadmap"
- "Work from the repo handoff docs"

