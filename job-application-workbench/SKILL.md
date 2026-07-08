---
name: job-application-workbench
description: Use when building or operating a job application workflow that ingests job descriptions, compares them to an applicant profile, generates tailored resume artifacts, and tracks submission status in a manifest-driven folder structure.
metadata:
  short-description: Job application workflow and manifest tracking
---

# Job Application Workbench

Use this skill when the user wants to turn one or more job descriptions into tailored application artifacts and track them durably.

## Core workflow

1. Read the applicant profile, resume rules, and any existing job manifest.
2. Ingest the job description from a pasted URL, raw markdown, or a local snapshot.
3. Extract role requirements, nice-to-haves, and signals that matter for tailoring.
4. Compare the job against the applicant profile and identify evidence-backed matches.
5. Generate the requested artifacts, usually:
   - `resume.md`
   - `fit-notes.md`
   - `cover-letter.md` if requested
   - `manifest.json`
6. Save outputs in a dated job folder.
7. Update submission status as the job moves through the pipeline.

## Folder convention

Prefer a structure like:

```text
jobs/
  inbox/
    *.md
  applicant/
    profile.md
    experience.md
    resume-rules.md
  applications/
    YYYY/
      MM/
        DD/
          company-role-slug/
            manifest.json
            job-description.md
            fit-notes.md
            resume.md
            cover-letter.md
            submission.md
```

## Manifest rules

Keep a manifest for each application so the workflow survives later sessions and job postings that disappear.

Track at least:
- job title
- company
- source URL
- local source snapshot path
- application date
- submission date
- status
- output paths
- tags or fit themes

Prefer statuses like:
- `inbox`
- `analyzed`
- `drafted`
- `submitted`
- `interviewing`
- `offer`
- `rejected`
- `closed`

## Writing rules

- Do not invent experience.
- Use only evidence from the applicant profile, resume, or other provided sources.
- Prefer concise, specific matching notes over generic claims.
- If a source URL may disappear, snapshot the job description locally.
- If the user asks for a resume draft, tailor it to the job without changing truthfulness.
