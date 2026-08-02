# Phase 3 Ukrainian Translation Review - Part III

## Source Baseline

- English source tag: v1.0.0
- Current main baseline: 77aaac1fc4344fe41c3dbda12a3a4da2f4368e98

## Scope

- Part III - Architecture Playbook

## Created Target Files

- `translations/uk/book/03-architecture-playbook/README.md`
- `translations/uk/book/03-architecture-playbook/14-drawing-boundaries-that-survive-change.md`
- `translations/uk/book/03-architecture-playbook/15-managing-change-radius.md`
- `translations/uk/book/03-architecture-playbook/16-designing-for-failure-and-recovery.md`
- `translations/uk/book/03-architecture-playbook/17-using-adrs-and-rfcs-well.md`
- `translations/uk/book/03-architecture-playbook/18-reviewing-architecture-before-it-hardens.md`
- `translations/uk/book/03-architecture-playbook/19-freezing-architecture-without-freezing-learning.md`

## Terminology Decisions

- `Principal Engineer`, `ADR`, `RFC`, `API`, `Decision Journal`, `Architecture Review`, `Architecture Ledger`, `Architecture Freeze`, `Change Radius`, `Discoverability`, and PEAK IDs remain in English according to the Ukrainian glossary.
- Chapter titles use natural Ukrainian while keeping them recognizable:
  - `Architecture Playbook` -> `Архітектурний playbook`
  - `Drawing Boundaries That Survive Change` -> `Проведення меж, які витримують зміни`
  - `Managing Change Radius` -> `Керування Change Radius`
  - `Designing for Failure and Recovery` -> `Проєктування для відмов і відновлення`
  - `Using ADRs and RFCs Well` -> `Як добре використовувати ADR і RFC`
  - `Reviewing Architecture Before It Hardens` -> `Перегляд архітектури до того, як вона затвердіє`
  - `Freezing Architecture Without Freezing Learning` -> `Заморожування архітектури без заморожування навчання`
- `boundary` is rendered as `межа`; canonical compound phrases may retain English terms around it where the surrounding Ukrainian prose remains clear.
- `failure` is rendered as `відмова` when discussing system failure; `recovery` as `відновлення`.
- `Change Radius` is preserved as the canonical metric/concept name and explained in Ukrainian prose around it.
- `Architecture Review` and `Architecture Freeze` remain English canonical ritual names, with Ukrainian explanatory framing.

## Pending Cross-Phase Links

- No new links to future Ukrainian Phase 4-7 files were introduced.
- Part III references later concepts such as Architecture Health Review and later organizational/publishing practices only as canonical text, not as new Ukrainian links.

## Unresolved Translation Questions

- The reviewed Phase 3 text intentionally preserves a mixed Ukrainian/English engineering register for canonical and embedded terms such as `runtime`, `service tool`, `gateway`, `firmware`, `Change Radius`, `Architecture Review`, and `Architecture Freeze`.
- Phase 3 terminology review resolved repeated chapter-local phrases: `Review habit` -> `звичка перегляду`, `hardening point` -> `точка затвердіння`, `allowed movement` -> `дозволений рух`, and `exception path` -> `шлях винятку`.
- No reader-facing source-only markers remain.

## Validation

- `git fetch --all --tags --prune` - passed.
- `git rev-parse v1.0.0^{commit}` - passed: `5baef38d555712d6e572888285d3715e46fba118`.
- `git log -1 --oneline v1.0.0` - passed: `5baef38 Release 1 (#43)`.
- `git rev-parse origin/main` - passed: `77aaac1fc4344fe41c3dbda12a3a4da2f4368e98`.
- Required Ukrainian governance files exist on `origin/main`.
- Phase 3 scope in `translations/uk/PHASE_PLAN.md` matches Part III.
- All Phase 3 source files exist in `v1.0.0`.
- Source H1 check passed for Part III README and Chapters 14-19.
- `git status --short` - passed; only Phase 3 Ukrainian files and this phase note were untracked before staging.
- `git diff --check` - passed.
- `git diff --name-only origin/main...HEAD -- book/` - passed; no English canonical source files changed.
- All 7 Ukrainian Phase 3 target files exist.
- Phase note exists.
- Reader-facing source-only marker search in Phase 3 files - passed.
- `npm.cmd run lint:md` - passed.
- `npm.cmd run lint:spelling` - passed.
- `python -m pip check` - passed.
- `python -m mkdocs build --strict` - passed.
- `npx.cmd linkinator "translations/uk/**/*.md" --markdown --recurse --skip "^mailto:" --skip "node_modules" --skip "site" --timeout 60000` - passed.
- `npm.cmd run lint:links` - passed.
- `git -c safe.directory=D:/Projects/ThePrincipaEngineerHandbook ls-files site` - passed; no tracked `site/` output.

## Outcome

Translation and review complete.

## Terminology Review

- Outcome: Passed
- Commit: `05cbb79`
- Decisions:
  - Added Phase 3 terminology rows to `translations/uk/TERMINOLOGY_GLOSSARY.md` for `Architecture Playbook`, `Review habit`, `hardening point`, `allowed movement`, `exception path`, `contract`, `owner`, `firmware`, `gateway`, `service tool`, and `runtime`.
  - Standardized `boundary` as `межа`, `contract` as `контракт`, and `owner` as `власник` where these are not part of a preserved canonical label.
  - Preserved `Architecture Review`, `Architecture Freeze`, `Architecture Ledger`, `Decision Journal`, `ADR`, `RFC`, `API`, `Change Radius`, `Discoverability`, and all PEAK IDs in English.
  - Kept `firmware`, `gateway`, `service tool`, and `runtime` in English as common embedded/software terms with Ukrainian surrounding prose.
  - Confirmed reader-facing Phase 3 files contain no source-only markers.
- Remaining terminology questions:
  - None

## Ukrainian Editorial Review

- Outcome: Passed
- Commit: `0106c0a`
- Notes:
  - Removed corrupted replacement remnants in Phase 3 reader-facing chapters.
  - Restored Phase 3 local terms for `boundary`, `contract`, `owner`, `hardening point`, `allowed movement`, and `exception path` according to the terminology review.
  - Preserved canonical English labels and PEAK identifiers while keeping the surrounding Ukrainian/engineering register stable for publication.

## Publishing Review

- Outcome: Passed
- Commit: pending at commit time
- Validation:
  - `git status --short` - passed; working tree was clean before recording this review section.
  - `git diff --check` - passed.
  - `git diff --name-only origin/main...HEAD -- book/` - passed; no English source changed.
  - Phase 3 target file inventory - passed; all seven Part III Ukrainian files exist.
  - Reader-facing Phase 3 marker scan - passed.
  - Phase 4 creation check - passed; no files under `translations/uk/book/04-building-a-product/` were created by this branch.
  - `npm run lint:md` - passed.
  - `npm run lint:spelling` - passed.
  - `python -m pip check` - passed.
  - `python -m mkdocs build --strict` - passed.
  - `linkinator translations/uk/**/*.md` - passed.
  - `npm run lint:links` - passed.
  - tracked `site/` output - none.
- Outcome: Phase 3 review complete.
