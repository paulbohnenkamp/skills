---
name: coding-conventions
description: Use when you need to follow or define repository coding conventions, editing rules, and agent working norms before making code changes.
---

# Coding Conventions

Use this skill when a repository needs consistent coding rules, edit discipline, or agent behavior norms.

## Core model

- Repository-local instructions win.
- Coding conventions should be explicit, short, and easy to verify.
- Keep workflow rules separate from style rules when they need different loading paths.
- Prefer existing repo patterns over generic defaults.

## First pass

1. Read the repo entry points for instructions, plans, and docs.
2. Check for repository-local coding rules first.
3. If repo-local rules exist, follow them.
4. If the repo has no local rules, use [references/conventions.md](references/conventions.md) as the default checklist.
5. Identify any local patterns that override the default conventions.
6. If the task changes public naming, contracts, or structure beyond what the user requested, confirm before editing.

## Working rule

- Make the smallest change that satisfies the request.
- Keep code style consistent with nearby code.
- Use file names that match the file's role: `PascalCase` for React components and class-heavy modules, `kebab-case` for utility modules, loaders, validators, scripts, and entrypoints.
- Avoid mixing naming styles for the same kind of file within one repo unless the repo already has a hard rule.
- Do not introduce new abstractions unless the repo already trends that way or the change demands it.
- Avoid unrelated cleanup in the same change unless it is required for correctness.
- Update tests, docs, or examples when the change affects behavior or developer workflow.

## Completion rule

Consider a coding task ready when:

- The change matches repo-local conventions.
- The resulting code is coherent with surrounding patterns.
- Required checks pass or a clear verification gap is noted.
- Any convention changes are documented where the repo expects them.
