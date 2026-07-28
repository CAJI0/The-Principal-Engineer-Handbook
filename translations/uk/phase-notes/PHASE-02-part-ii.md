# Phase 2 Ukrainian Translation Draft - Part II

## Source Baseline

- English source tag: v1.0.0
- Current main baseline: 1fe46a6e96d49d115b7c25a6f8ed1a244ab6fdff

## Scope

- Part II - The Laws

## Created Target Files

- `translations/uk/book/02-the-laws/README.md`
- `translations/uk/book/02-the-laws/07-every-state-has-one-owner.md`
- `translations/uk/book/02-the-laws/08-every-api-is-a-promise.md`
- `translations/uk/book/02-the-laws/09-every-dependency-is-a-decision.md`
- `translations/uk/book/02-the-laws/10-time-is-a-dependency.md`
- `translations/uk/book/02-the-laws/11-unused-flexibility-is-waste.md`
- `translations/uk/book/02-the-laws/12-simplicity-is-a-feature.md`
- `translations/uk/book/02-the-laws/13-evidence-before-confidence.md`

## Terminology Decisions

- `Principal Engineer`, `ADR`, `RFC`, `API`, `Decision Journal`, `Architecture Review`, `Change Radius`, `Bus Factor`, and PEAK IDs remain in English according to the Ukrainian glossary.
- Law titles are translated for Ukrainian readability while keeping canonical recognition:
  - `Every State Has One Owner` -> `Кожен стан має одного власника`
  - `Every API Is a Promise` -> `Кожен API — це обіцянка`
  - `Every Dependency Is a Decision` -> `Кожна залежність — це рішення`
  - `Time Is a Dependency` -> `Час — це залежність`
  - `Unused Flexibility Is Waste` -> `Невикористана гнучкість — це марнування`
  - `Simplicity Is a Feature` -> `Простота — це функція продукту`
  - `Evidence Before Confidence` -> `Докази перед впевненістю`
- Draft keeps a mixed Ukrainian/English engineering register where Phase 1 already preserved canonical terms or where later review should decide the final rendering.
- Source `v1.0.0:book/02-the-laws/README.md` contains an author note; it was not copied into the Ukrainian reader-facing README.
- `LAW-007`, `LAW-003`, `LAW-006`, `LAW-004`, and `LAW-005` are preserved exactly as they appear in source, without renumbering.

## Pending Cross-Phase Links

- Part II chapters reference later parts and appendix concepts. No cross-phase target links were added in Phase 2.
- Ukrainian publishing navigation and PDF/site treatment remain deferred to later Ukrainian publishing phases.

## Unresolved Translation Questions

- The draft intentionally leaves several English technical nouns for later review: `boundary`, `runtime`, `callback`, `fixture`, `workflow`, `review`, `release`, `field`, `support`, and related engineering-register terms.
- `Simplicity Is a Feature` was resolved during Terminology Review as `Простота — це функція продукту`, preserving the product-capability meaning rather than using colloquial `feature` or the flatter `властивість`.

## Validation

- `git fetch --all --tags --prune` - passed.
- `git status --short` before edits - passed; worktree clean.
- `git rev-parse v1.0.0^{commit}` - passed: `5baef38d555712d6e572888285d3715e46fba118`.
- `git log -1 --oneline v1.0.0` - passed: `5baef38 Release 1 (#43)`.
- `git rev-parse origin/main` - passed after fetch: `1fe46a6e96d49d115b7c25a6f8ed1a244ab6fdff`.
- Required Ukrainian strategy, style, glossary, phase plan, and Phase 1 notes exist on `origin/main`.
- Phase 2 scope in `translations/uk/PHASE_PLAN.md` matches Part II.
- All Phase 2 source files exist in `v1.0.0`.
- Source H1 check passed for Part II README and Chapters 7-13.
- `git diff --check` - passed.
- `git diff --name-only origin/main...HEAD -- book/` - passed; no English canonical source files changed.
- Source-to-target mapping check - passed; all 8 Phase 2 source files have matching Ukrainian target files.
- Draft-marker search for Ukrainian Phase 2 files and this phase note - passed.
- `npm.cmd run lint:md` - passed.
- `npm.cmd run lint:spelling` - passed.
- `python -m pip check` - passed.
- `python -m mkdocs build --strict` - passed.
- `npx.cmd linkinator "translations/uk/**/*.md" --markdown --recurse --skip "^mailto:" --skip "node_modules" --skip "site" --timeout 60000` - passed.
- `npm.cmd run lint:links` - passed.
- `git -c safe.directory=D:/Projects/ThePrincipaEngineerHandbook ls-files site` - passed; no tracked `site/` output.
- `vale .` - passed with 0 errors and 3 existing non-blocking warnings outside Ukrainian Phase 2 files: `CONTRIBUTING.md`, `editor/ARCHITECTURE_REVIEW_0.md`, and `editor/SOURCE_OF_TRUTH.md`.

## Outcome

Translation Draft complete.

## Phase 2 Terminology Review

Baseline commit before gate: `a90fd7e8d3bac3c2f594dd96dd7c0a5905ad91a3`

Outcome: Passed.

Terminology changes made:

- Recorded that the terminology governance file for this repository is `translations/uk/TERMINOLOGY_GLOSSARY.md`.
- Standardized Ukrainian law-title punctuation with an em dash where the title uses an equative construction.
- Resolved `Simplicity Is a Feature` as `Простота — це функція продукту`, preserving the product-capability sense while avoiding the draft-level mixed rendering `feature`.
- Replaced several visible uses of `promise` in Chapter 8 with Ukrainian `обіцянка` where the word was not a canonical English law title.
- Preserved canonical law names and PEAK IDs exactly where the source uses them as canonical concepts.

Unresolved items:

- Broader English connective prose cleanup remains for the Ukrainian Editorial Review gate.
- Technical-register words such as `boundary`, `runtime`, `callback`, `fixture`, `workflow`, `review`, `release`, `field`, and `support` require editorial-context decisions rather than blanket replacement.

Validation:

- `git diff --check` - passed.
- `git diff --name-only origin/main...HEAD -- book/` - passed; no English canonical source files changed.
- `npm.cmd run lint:md` - passed.
- `npm.cmd run lint:spelling` - passed.
- `python -m pip check` - passed.
- `python -m mkdocs build --strict` - passed.
- `npx.cmd linkinator "translations/uk/**/*.md" --markdown --recurse --skip "^mailto:" --skip "node_modules" --skip "site" --timeout 60000` - passed.
- `npm.cmd run lint:links` - passed.
- `git -c safe.directory=D:/Projects/ThePrincipaEngineerHandbook ls-files site` - passed; no tracked `site/` output.
