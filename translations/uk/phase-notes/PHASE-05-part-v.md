# Ukrainian Translation Phase 5 - Part V

## Scope

Phase 5 covers Part V, `book/05-engineering-organization`, translated from the immutable `v1.0.0` source baseline.

Source baseline:

- `origin/main`: `75a5e3bbbb11be89d0ba38f78e9b7b24506494bf`
- immutable source tag `v1.0.0`: `5baef38d555712d6e572888285d3715e46fba118`

Source directory: `book/05-engineering-organization`

Target directory: `translations/uk/book/05-engineering-organization`

Translated files:

- [x] `translations/uk/book/05-engineering-organization/README.md`
- [x] `translations/uk/book/05-engineering-organization/26-technical-leadership-without-authority.md`
- [x] `translations/uk/book/05-engineering-organization/27-design-reviews-as-shared-memory.md`
- [x] `translations/uk/book/05-engineering-organization/28-building-engineering-rituals.md`
- [x] `translations/uk/book/05-engineering-organization/29-mentoring-through-artifacts.md`
- [x] `translations/uk/book/05-engineering-organization/30-aligning-teams-around-decisions.md`
- [x] `translations/uk/book/05-engineering-organization/31-architecture-health-reviews.md`

## Translation Decisions

- Part V `README.md` source contains only an author note. The Ukrainian file provides a concise reader-facing overview and links to Chapters 26-31; it does not translate or reproduce the author note.
- Canonical artifact and concept names are retained when they function as registered PEAK vocabulary: `ADR`, `RFC`, `Decision Journal`, `Architecture Ledger`, `Architecture Review`, `Architecture Freeze`, `Architecture Health Review`, `Event Catalog`, `Mistake Ledger`, `Weak Signal Register`, `Change Radius`, `Bus Factor`, `Discoverability`.
- Stable IDs are preserved exactly in backticks.
- Product/system labels such as `provisioned`, `package_written`, `reservation_expired`, `device_rejected` and `accepted` are preserved where the text discusses literal interface or event language.
- Ukrainian prose uses "власник", "відповідальний власник", "узгодження", "докази", "тригер перегляду", "тимчасовий шлях сумісності" and "провізіонування" consistently for the Part V decision vocabulary.

## Open Terminology Questions

- None recorded as blocker-level terminology questions in this draft pass.

## Structural and Literal Preservation

- Section inventory checked for all seven source/target file pairs: heading counts match.
- Stable identifier comparison checked for Chapters 26-31: missing `0`, extra `0`.
- Link checks passed for the Ukrainian translation tree.
- Code spans and literal labels were preserved where they represent machine-visible UI, event, path, version, or identifier text.

## Residual-English Audit

Result: passed after targeted remediation.

Policy applied: retain only governed PEAK names, acronyms, code spans, identifiers, file paths, event names, exact UI/API literals, versions, and proper names.

Targeted remediation was applied to Chapters 27, 29, 30, and 31, plus additional residual mixed-language prose found in Chapters 26 and 28 during the full seven-file scan.

Audit command:

```powershell
rg -n "\b(the|and|or|with|without|because|where|what|when|owner|owners|decision|review|evidence|trigger|accepted|rejected|missing|changed|unchanged|temporary|support|release|team|teams|system|record|records|artifact|artifacts|health|should|would|could|must|not|from|into|through|around|visible|memory|reasoning|behavior|change|changes|status|output|inputs|outputs|context|constraints|alternatives|consequences|question|questions|path|paths|ready|readiness|field|device|backend|firmware|manufacturing|service|tool|tools|station|test|tests|product)\b" translations\uk\book\05-engineering-organization translations\uk\phase-notes\PHASE-05-part-v.md
```

Final classification:

- Governed PEAK artifact or concept names retained: `ADR`, `RFC`, `Decision Journal`, `Architecture Ledger`, `Architecture Review`, `Architecture Freeze`, `Architecture Health Review`, `Event Catalog`, `Mistake Ledger`, `Weak Signal Register`, `Change Radius`, `Bus Factor`, `Discoverability`, `Temporary Solution`, `Hidden State`, `Silent Coupling`, `The Hero Engineer`.
- Acronyms and stable IDs retained: `API`, `LAW-*`, `VOCAB-*`, `METRIC-*`, `RITUAL-*`, `ARTIFACT-*`, `SMELL-*`, `ANTIPATTERN-*`, `FAILURE-*`.
- Machine-visible or literal labels retained where needed: `provisioned`, `package_written`, `reservation_expired`, `device_rejected`, `accepted`, `apply configuration`, `Retry failed gateway requests three times with exponential delay`, `retry helper`, `service command`, `manufacturing provisioning`, file paths, branch names, commit identifiers, commands, and version tags.
- Proper names retained: `Mara`, `Alex`, `Sam`.
- Reader-facing English prose category: no unresolved instances found after remediation and direct reading.

## UTF-8 and Integrity

- Strict UTF-8 decoding passed for all eight new files.
- No replacement characters, question-mark substitution runs, conflict markers, or encoding corruption were found in the eight new files during the final pass.

## Validation Log

Commands run:

- `git diff --check` - passed.
- Exact changed-path inventory - passed: exactly the allowed eight files are present as untracked changes.
- Phase 5 source/target inventory - passed: source `7`, target `7`, missing `0`, extra `0`.
- Section heading inventory - passed for all seven source/target pairs.
- Stable-ID comparison - passed for Chapters 26-31: missing `0`, extra `0`.
- Strict UTF-8/corruption audit - passed for all eight new files after removing a literal corruption-marker example from this note.
- Residual-English audit - passed after targeted remediation and manual classification.
- `npm.cmd run lint:md` - passed, `0` errors.
- `npm.cmd run lint:spelling` - passed, `0` issues.
- `npm.cmd run lint:links` - passed.
- `npx.cmd linkinator "translations/uk/**/*.md" --markdown --recurse --skip "^mailto:" --skip "node_modules" --skip "site" --timeout 60000` - passed, `52` links scanned.
- `vale .` - passed with `0` errors, `3` warnings, `0` suggestions. The warnings are the accepted pre-existing `PrincipalEngineerHandbook.AuthorBoundary` warnings in `CONTRIBUTING.md`, `editor/ARCHITECTURE_REVIEW_0.md`, and `editor/SOURCE_OF_TRUTH.md`.
- `python -m mkdocs build --strict` - passed.
- `python -m pip check` - passed.

Scope confirmation:

- Canonical English `book/` files were not edited.
- Prior Ukrainian phases were not edited.
- Phase 6+ translation targets were not edited.
- Translation governance, glossary, MkDocs, Vale, cspell, Node package scripts, CI, and tooling files were not edited.
- No review gate, pull request, merge, release, or Phase 6 work was performed.

Outcome: Translation Draft complete. Ready for Terminology Review.
