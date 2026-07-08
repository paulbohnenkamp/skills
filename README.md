# Skills

This repository is a reusable library of agent skills.

Each skill lives in its own folder and focuses on one repeatable workflow.

## Current skills

- [repo-handoff-workflow](./repo-handoff-workflow/): reusable guidance for repos that separate reference docs from active plans
- [feature-definition](./feature-definition/): turn an idea or rough request into a durable spec
- [plan-workflow](./plan-workflow/): turn a spec into an implementation plan with verification and status tracking
- [verification-loop](./verification-loop/): select, run, and interpret the right checks before calling a slice done
- [handoff-summary](./handoff-summary/): write a compact continuation note for the next session

## Suggested flow

1. Orient to the repo with [repo-handoff-workflow](./repo-handoff-workflow/).
2. Define the feature with [feature-definition](./feature-definition/).
3. Turn the spec into a plan with [plan-workflow](./plan-workflow/).
4. Verify the slice with [verification-loop](./verification-loop/).
5. Leave a note with [handoff-summary](./handoff-summary/).

## How to add a skill

1. Create a new folder named after the skill.
2. Add a `SKILL.md` file with `name` and `description` frontmatter.
3. Keep the skill focused on one job.
4. Add references or scripts only when the skill needs them.

## License

This repository is intended to be public and reusable.

## Install

Install this skill library into your Codex setup:

```bash
npx skills@latest add paulbohnenkamp/skills
```
