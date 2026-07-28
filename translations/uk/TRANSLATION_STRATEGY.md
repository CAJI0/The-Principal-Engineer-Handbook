# Ukrainian Translation Strategy

The Ukrainian translation is a localization of release `v1.0.0`, not a new edition of the book.

## Source Of Truth

- The immutable English source baseline is the Git tag `v1.0.0`.
- Canonical English manuscript content remains in `book/`.
- Ukrainian translation source will later live under `translations/uk/book/`.
- Generated publishing output such as `site/` is not translation source and must not be committed.
- English manuscript files must not be modified during translation phases unless a separate maintainer-approved English correction is requested.

## Branch Policy

- Strategy and planning work uses `translation-uk-strategy`.
- Translation phases should use focused branches, for example `translation-uk-phase-1-front-matter-part-i`.
- Each branch should cover one declared phase or one narrow review correction.
- Branches should be based on `v1.0.0` or on the latest accepted Ukrainian translation branch, according to the active phase plan.
- Commits should use Conventional Commits style.

## Phase-Based Translation

- Translation proceeds in declared phases, not opportunistic chapter edits.
- Each phase must state its source files, Ukrainian target files, review gates, validation commands, and stop conditions before drafting begins.
- A phase is not complete until terminology, Ukrainian editorial quality, structure, links, and publishing readiness have been reviewed.

## No Conceptual Rewriting

- Translate the released English manuscript faithfully.
- Improve Ukrainian readability without changing the book's claims, examples, structure, or technical meaning.
- Do not add new concepts, remove author intent, merge sections, or rewrite the book for a different audience.
- If the English source appears ambiguous or incorrect, record the issue in the phase notes instead of silently changing the meaning.

## Terminology Control

- Use `TERMINOLOGY_GLOSSARY.md` as the controlled vocabulary for Ukrainian rendering.
- Do not silently change a term once a phase has adopted it.
- When a term needs a new rendering, update the glossary in the same branch and explain the reason.
- On first use of a canonical concept name, preserve the English term when the glossary requires it.

## Uncertain Translations

- Mark unresolved choices in phase review notes rather than leaving reader-facing placeholders.
- Prefer a short reviewer note with the source sentence, candidate renderings, and the reason for uncertainty.
- Do not ship `TODO`, `AUTHOR NOTE`, or placeholder text in Ukrainian release output.

## Examples, Code, Commands, Paths, IDs, And Links

- Keep code samples, shell commands, file paths, commit subjects, API names, IDs, and machine-readable values unchanged.
- Preserve PEAK IDs such as `CHAPTER-037`, `LAW-001`, `ARTIFACT-002`, and similar identifiers exactly.
- Translate explanatory prose around commands and code, not the commands or code themselves.
- Preserve link targets unless the linked target has a Ukrainian counterpart and the phase explicitly updates navigation.
- If a link cannot be validated, record it as a phase blocker.

## English Terms To Preserve

Some terms should usually remain in English because they are role names, ecosystem names, acronyms, or canonical project tooling. Examples include `Principal Engineer`, `Staff Engineer`, `Senior Engineer`, `API`, `RFC`, `ADR`, `CI/CD`, `GitHub`, `MkDocs`, and `Vale`.

When an English term remains in English, Ukrainian surrounding grammar should make the sentence natural without altering the term itself.

## Review Model

Each translation phase follows this review sequence:

```text
Translation Draft -> Terminology Review -> Ukrainian Editorial Review -> Publishing Review
```

- Translation Draft checks completeness against the English source.
- Terminology Review checks glossary consistency and unresolved terms.
- Ukrainian Editorial Review checks clarity, tone, grammar, punctuation, and absence of Russianisms.
- Publishing Review checks structure, links, generated navigation, and PDF readiness when publishing support exists.
