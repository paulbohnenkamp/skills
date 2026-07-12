# Skills

This repository is a reusable library of agent skills.

Each skill lives in its own folder and focuses on one repeatable workflow.

## Current skills

- [repo-handoff-workflow](./repo-handoff-workflow/): reusable guidance for repos that separate reference docs from active plans
- [repo-scaffold-workflow](./repo-scaffold-workflow/): create a durable, agent-friendly repository scaffold
- [feature-definition](./feature-definition/): turn an idea or rough request into a durable spec
- [coding-conventions](./coding-conventions/): follow repository coding rules and edit norms
- [plan-workflow](./plan-workflow/): turn a spec into an implementation plan with verification and status tracking
- [verification-loop](./verification-loop/): select, run, and interpret the right checks before calling a slice done
- [handoff-summary](./handoff-summary/): write a compact continuation note for the next session
- [job-application-workbench](./job-application-workbench/): create truthful, manifest-tracked job application artifacts

## Suggested flow

1. Orient to the repo with [repo-handoff-workflow](./repo-handoff-workflow/).
2. Define non-trivial behavior with [feature-definition](./feature-definition/).
3. Turn the spec into a plan with [plan-workflow](./plan-workflow/).
4. Verify the slice with [verification-loop](./verification-loop/).
5. Leave a note with [handoff-summary](./handoff-summary/).

Use the smallest workflow that fits the change. Trivial, low-risk edits do not need a standalone spec and plan unless the repository requires them.

## How to add a skill

1. Create a new folder named after the skill.
2. Add a `SKILL.md` file with `name` and `description` frontmatter.
3. Keep the skill focused on one job.
4. Add references or scripts only when the skill needs them.
5. Add `agents/openai.yaml` with a display name, short description, and a default prompt that names the skill.
6. Validate the skill and check every local link before publishing.

## License

This repository is intended to be public and reusable.

## Install

Install this skill library into your Codex setup:

```bash
npx skills@latest add paulbohnenkamp/skills
```
