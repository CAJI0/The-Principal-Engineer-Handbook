# Phase 3 Ukrainian Translation Draft - Part III

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
- Chapter titles use natural Ukrainian while preserving recognizability:
  - `Architecture Playbook` -> `Архітектурний playbook`
  - `Drawing Boundaries That Survive Change` -> `Проведення меж, які витримують зміни`
  - `Managing Change Radius` -> `Керування Change Radius`
  - `Designing for Failure and Recovery` -> `Проєктування для відмов і відновлення`
  - `Using ADRs and RFCs Well` -> `Як добре використовувати ADR і RFC`
  - `Reviewing Architecture Before It Hardens` -> `Перегляд архітектури до того, як вона затвердіє`
  - `Freezing Architecture Without Freezing Learning` -> `Заморожування архітектури без заморожування навчання`
- `boundary` is rendered as `межа` or preserved in mixed technical phrases during draft where review should decide final register.
- `failure` is rendered as `відмова` when discussing system failure; `recovery` as `відновлення`.
- `Change Radius` is preserved as the canonical metric/concept name and explained in Ukrainian prose around it.
- `Architecture Review` and `Architecture Freeze` remain English canonical ritual names, with Ukrainian explanatory framing.

## Pending Cross-Phase Links

- No new links to future Ukrainian Phase 4-7 files were introduced.
- Part III references later concepts such as Architecture Health Review and later organizational/publishing practices only as canonical text, not as new Ukrainian links.

## Unresolved Translation Questions

- The draft intentionally preserves a mixed Ukrainian/English engineering register for terms such as `review`, `freeze`, `runtime`, `service tool`, `gateway`, `firmware`, `Change Radius`, `boundary`, `contract`, and `owner`.
- Later Terminology Review should decide whether repeated chapter-local phrases such as `Review habit`, `hardening point`, `allowed movement`, and `exception path` should remain English or receive stable Ukrainian renderings.
- No reader-facing placeholders remain.

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
- Reader-facing marker search for `AUTHOR NOTE`, `TODO`, `TBD`, `placeholder`, `draft-only`, and `Draft` in Phase 3 files - passed.
- `npm.cmd run lint:md` - passed.
- `npm.cmd run lint:spelling` - passed.
- `python -m pip check` - passed.
- `python -m mkdocs build --strict` - passed.
- `npx.cmd linkinator "translations/uk/**/*.md" --markdown --recurse --skip "^mailto:" --skip "node_modules" --skip "site" --timeout 60000` - passed.
- `npm.cmd run lint:links` - passed.
- `git -c safe.directory=D:/Projects/ThePrincipaEngineerHandbook ls-files site` - passed; no tracked `site/` output.

## Outcome

Translation Draft complete.
