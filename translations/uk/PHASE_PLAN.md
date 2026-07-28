# Ukrainian Translation Phase Plan

Each translation phase uses this review model:

```text
Translation Draft -> Terminology Review -> Ukrainian Editorial Review -> Publishing Review
```

## Phase 1: Front Matter + Part I

- Scope: front matter and Part I.
- Expected files: `book/00-front-matter/README.md`, `manifesto.md`, `preface.md`, `table-of-contents.md`, and `book/01-thinking-like-a-principal/*.md`.
- Required checks: source-to-target file mapping, unchanged IDs, glossary consistency, Markdown linting, link review.
- Review gates: Translation Draft, Terminology Review, Ukrainian Editorial Review, Publishing Review.
- Stop conditions: missing counterpart, modified English source, unresolved terminology, broken critical link, or reader-facing placeholder.

## Phase 2: Part II

- Scope: laws and principles in `book/02-the-laws/`.
- Expected files: Part II README and Chapters 7-13.
- Required checks: law IDs unchanged, chapter IDs unchanged, glossary consistency, Markdown linting, link review.
- Review gates: Translation Draft, Terminology Review, Ukrainian Editorial Review, Publishing Review.
- Stop conditions: altered law meaning, changed ID, missing counterpart, unresolved terminology, or placeholder text.

## Phase 3: Part III

- Scope: architecture playbook in `book/03-architecture-playbook/`.
- Expected files: Part III README and Chapters 14-19.
- Required checks: artifact and concept IDs unchanged, ADR/RFC terminology consistency, Markdown linting, link review.
- Review gates: Translation Draft, Terminology Review, Ukrainian Editorial Review, Publishing Review.
- Stop conditions: conceptual rewrite, broken artifact semantics, missing counterpart, or unresolved reviewer note.

## Phase 4: Part IV

- Scope: product-building chapters in `book/04-building-a-product/`.
- Expected files: Part IV README and Chapters 20-25.
- Required checks: product, manufacturing, observability, release, and reference-project terms checked against glossary.
- Review gates: Translation Draft, Terminology Review, Ukrainian Editorial Review, Publishing Review.
- Stop conditions: altered product example, changed command/path/API text, missing counterpart, or unresolved publishing issue.

## Phase 5: Part V

- Scope: engineering organization chapters in `book/05-engineering-organization/`.
- Expected files: Part V README and Chapters 26-31.
- Required checks: ritual IDs unchanged, leadership terminology consistent, Markdown linting, link review.
- Review gates: Translation Draft, Terminology Review, Ukrainian Editorial Review, Publishing Review.
- Stop conditions: role meaning drift, changed ritual semantics, missing counterpart, or unresolved terminology.

## Phase 6: Part VI

- Scope: legacy-system chapters in `book/06-legacy/`.
- Expected files: Part VI README and Chapters 32-37.
- Required checks: smell IDs unchanged, legacy-system glossary consistency, Markdown linting, link review.
- Review gates: Translation Draft, Terminology Review, Ukrainian Editorial Review, Publishing Review.
- Stop conditions: changed smell meaning, accidental English block, missing counterpart, or broken link.

## Phase 7: Appendix

- Scope: Appendix overview and templates.
- Expected files: `book/appendix/README.md`, `adr-template.md`, `rfc-template.md`, `decision-journal-template.md`, `architecture-review-template.md`, `chapter-review-checklist.md`, and `glossary.md`.
- Required checks: template fields preserved, IDs unchanged, links checked, Markdown linting.
- Review gates: Translation Draft, Terminology Review, Ukrainian Editorial Review, Publishing Review.
- Stop conditions: changed template contract, missing counterpart, broken internal link, or placeholder text.

## Phase 8: Ukrainian Full Editorial Pass

- Scope: all Ukrainian translated source.
- Expected files: all files under `translations/uk/book/`.
- Required checks: consistent voice, glossary consistency, absence of Russianisms, no accidental large English prose blocks.
- Review gates: Terminology Review, Ukrainian Editorial Review, Publishing Review.
- Stop conditions: unresolved glossary conflict, recurring style defect, or incomplete source mapping.

## Phase 9: Ukrainian Publishing/PDF Readiness

- Scope: Ukrainian MkDocs configuration, navigation, link checks, and PDF export readiness.
- Expected files: Ukrainian publishing config and generated output policy, without committing `site/`.
- Required checks: MkDocs build, link checks, PDF completeness, generated output untracked.
- Review gates: Publishing Review.
- Stop conditions: incomplete navigation, missing chapter in PDF, broken required link, or tracked generated output.

## Phase 10: Ukrainian Release Candidate

- Scope: Ukrainian release candidate validation and release notes.
- Expected files: release candidate audit, release notes, final validation record.
- Required checks: full validation suite, PDF artifact review, source-to-output completeness check.
- Review gates: Terminology Review, Ukrainian Editorial Review, Publishing Review, maintainer approval.
- Stop conditions: validation failure, unresolved blocker, missing artifact, or unapproved release boundary.
