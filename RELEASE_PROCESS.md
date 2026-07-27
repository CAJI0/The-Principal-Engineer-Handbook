# Release Process

This process describes how maintainers prepare a release. It does not approve manuscript content.

## Release Checklist

1. Confirm the authors have approved the manuscript state for release.
2. Run Markdown linting.
3. Run Vale prose checks.
4. Run spell checking.
5. Run dead link checking.
6. Build the MkDocs site with strict mode.
7. Build the PDF export.
8. Review generated artifacts.
9. Create a release branch or tag using the author-approved version.
10. Update `CHANGELOG.md`.

## Versioning

Release tags are created only after an approved release-readiness audit and explicit maintainer approval.
Until a versioning ADR is accepted, use the release candidate branch and changelog entry as the release boundary.
