# Feature Definition Reference

## Repo-local override order

1. If the repository has `docs/specs/README.md` or `docs/specs/index.md`, follow those first.
2. If repo-local spec docs are missing, use the skill-local guidance and templates in this skill directory.
3. If repo-local docs conflict with the skill defaults, repo-local docs win.

## Required spec shape

A durable spec should answer:

- What problem are we solving?
- Who is the user?
- What should the feature do?
- What inputs does it need?
- What outputs does it produce?
- What is explicitly out of scope?
- How will we know it is complete?

## Completion standard

A spec is ready when it can be used as the source of truth for a downstream implementation plan without requiring the next agent to infer the feature boundaries.
