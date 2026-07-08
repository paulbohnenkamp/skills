---
name: repo-scaffold-workflow
description: Use when creating a new repository scaffold that follows the durable README, AGENTS.md, ROADMAP.md, docs/specs, and plans pattern used for long-lived agent-friendly projects.
metadata:
  short-description: Create a durable repo scaffold
---

# Repo Scaffold Workflow

Use this skill when starting a new repo that should be immediately usable by another agent.

## Goal

Create a clean repo scaffold with:

- `README.md` for the public overview
- `AGENTS.md` for agent instructions
- `ROADMAP.md` for release-level progress
- `docs/` for reference docs and specs
- `plans/` for active execution handoff
- a minimal durable folder structure for the product domain

## Steps

1. Pick the repo name and root directory.
2. Create the root docs first: `README.md`, `AGENTS.md`, `ROADMAP.md`.
3. Add `docs/README.md` and `docs/specs/README.md` so reference docs stay separate from plans.
4. Add `plans/README.md`, `plans/TEMPLATE.md`, and `plans/index.md` so active work has a single entry point.
5. Add the product folders needed for the first slice.
6. Initialize git if the repo is meant to be versioned immediately.

## Defaults

Prefer this layout unless the user asks for something different:

```text
repo-name/
  AGENTS.md
  README.md
  ROADMAP.md
  docs/
    README.md
    specs/
      README.md
      <first-spec>.md
  plans/
    README.md
    TEMPLATE.md
    index.md
    <first-plan>.md
  .gitignore
```

## Rules

- Keep reference docs and active plans separate.
- Make `plans/index.md` the active-work entry point.
- Seed the first spec before the first plan.
- Keep the scaffold small enough that another agent can continue without guessing.
- If a manifest or domain folder is part of the repo, create the folder and document its role in the README.

## When to use references

Read `references/scaffold-checklist.md` when you need a quick checklist for what to create.
