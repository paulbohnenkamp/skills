# Coding Conventions Reference

Use this checklist when a repo does not already define its own coding rules.

## Workflow

- Read the repo instructions before editing code.
- Find any plan, spec, or handoff docs that govern the change.
- Inspect nearby code before deciding on style or structure.
- Ask before changing public names, file layout, or contracts.
- Keep edits focused on the requested slice.
- Run the smallest useful verification after the change.

## Style

- Match local naming, formatting, and architectural patterns.
- Prefer file names that describe the file's role:
  - `PascalCase` for React component files and class-oriented modules, such as `WorkspaceShell.tsx` or `ComponentRegistry.tsx`.
  - `kebab-case` for utility modules, loaders, validators, scripts, and entrypoints, such as `view-loader.ts` or `render-workspace.tsx`.
  - Keep a repo consistent within each category instead of mixing styles for the same kind of file.
- Prefer small, composable functions and components.
- Keep types and interfaces aligned with the code that consumes them.
- Avoid new abstractions unless they reduce real repetition or confusion.
- Prefer deletion over broad deprecation when a concept is obsolete.

## Safety

- Do not invent new top-level concepts if an existing one fits.
- Do not mix concerns across layers just to make a change easy.
- Preserve repository-specific boundaries and ownership rules.
- Update docs when behavior, workflow, or conventions change.

## Verification

- Choose checks that prove the change, not just that the code compiles.
- Run tests closest to the changed surface first.
- If a change has no automated proof, note the gap explicitly.
