# Final Release v1.0.0

Date: 2026-07-27

Version: `v1.0.0`

Branch: `final-release-v1.0.0`

Baseline `origin/main` SHA: `5115ddfa8b883ebd2913e38562cabbf2f7dd4dd1`

## Approval

Maintainer approval was provided for the final release version:

```text
Approve final release v1.0.0
```

## Scope

Final Release v1.0.0 covers the completed manuscript after:

- Chapters 1-37 were merged and marked canonical.
- Appendix was merged.
- Final Release Readiness Audit was merged.
- Release Candidate 1 was merged.

## Release Boundary

- Canonical manuscript source: `book/`
- Publishing support: generated `docs/manuscript/`
- Final audit: `editor/final-audit/FINAL_RELEASE_READINESS_AUDIT.md`
- Release candidate: `editor/final-audit/RELEASE_CANDIDATE_1.md`
- Release process: `RELEASE_PROCESS.md`
- Changelog: `CHANGELOG.md`

## Validation Results

| Command | Result |
| --- | --- |
| `git fetch --all --tags --prune` | Passed |
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
| `vale .` | Passed with 0 errors and 3 documented non-blocking author-boundary warnings |
| PDF export build | Passed |
| `git ls-files site` | Passed |

## Artifact Review

- Web build output reviewed: Yes
- PDF output generated: Yes
- PDF path: `site/pdf/the-principal-engineer-handbook.pdf`
- PDF SHA256: `4B70DAD435811EBE651AE20E2C74613AFD98545DC8F052B8D2F916F17185C7D3`
- PDF page count: 316
- Tracked `site/` output: None

## Remaining Blockers

None.

## Tag Plan

After this branch is merged into `main`, create an annotated release tag on the resulting `main` commit:

```bash
git fetch --all --tags --prune
git switch main
git pull --ff-only origin main
git tag -a v1.0.0 -m "The Principal Engineer Handbook v1.0.0"
git push origin v1.0.0
```

## GitHub Release Plan

Build the PDF from the tagged commit and publish a GitHub Release named `The Principal Engineer Handbook v1.0.0` with the generated PDF artifact.
