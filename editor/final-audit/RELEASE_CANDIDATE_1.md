# Release Candidate 1

Date: 2026-07-27

Branch: `release-candidate-1`

Baseline `origin/main` SHA: `82c8b681cc9cd5d8d91b9be3379e8be39ba7d580`

## Scope

Release Candidate 1 covers the completed manuscript after Chapters 1-37, Appendix, and Final Release Readiness Audit were merged to `main`.

## Release Boundary

- Canonical manuscript source: `book/`
- Publishing support: generated `docs/manuscript/`
- Final audit: `editor/final-audit/FINAL_RELEASE_READINESS_AUDIT.md`
- Release process: `RELEASE_PROCESS.md`

## Validation Results

| Command | Result |
| --- | --- |
| `git fetch --all --prune` | Passed |
| `git switch main` | Passed |
| `git pull --ff-only origin main` | Passed |
| `git status --short` | Passed |
| `python tools/generate_publishing_docs.py` | Passed |
| `git diff --check` | Passed |
| `npm install` | Passed |
| `npm run lint:md` | Passed |
| `npm run lint:spelling` | Passed |
| `npm run lint:links` | Passed |
| `python -m pip check` | Passed |
| `python -m mkdocs build --strict` | Passed |
| `vale sync` | Passed |
| `vale .` | Passed with 0 errors and 3 intentional author-boundary warnings in maintainer policy documents |
| PDF export build | Passed |
| `git ls-files site` | Passed |

## Artifact Review

- Web build output reviewed: Yes
- PDF output generated: Yes
- Tracked `site/` output: None

## Release Boundary Review

- `book/00-front-matter/table-of-contents.md` lists all six parts, Chapters 1-37, and Appendix.
- `book/appendix/README.md` links the appendix files.
- `docs/manuscript/` has generated publishing pages for front matter, Chapters 1-37, and Appendix.
- `mkdocs.yml` navigation exposes the generated manuscript pages.
- `README.md` no longer describes the project as early draft.
- `CHANGELOG.md` contains the completed manuscript coverage entry and this RC boundary.
- `RELEASE_PROCESS.md` states release/tag boundary rules.
- `editor/final-audit/FINAL_RELEASE_READINESS_AUDIT.md` records no remaining blockers.

## Remaining Blockers

None.

## Tag Status

No Git tag was created in this task because release tags require explicit maintainer approval and an author-approved version.

## Recommended Next Step

Open a PR titled `Release Candidate 1`, review this release candidate record, and merge it before creating an approved release tag.
