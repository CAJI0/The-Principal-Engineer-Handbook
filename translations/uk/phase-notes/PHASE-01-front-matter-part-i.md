# Phase 1 Ukrainian Translation Draft - Front Matter + Part I

## Source Baseline

- English source tag: v1.0.0
- Current main baseline: 73e4a5d4e3924ab0505715a81fb1e2e852d8d84f

## Scope

- Front matter
- Part I - Thinking Like a Principal Engineer

## Created Target Files

- `translations/uk/book/00-front-matter/README.md`
- `translations/uk/book/00-front-matter/manifesto.md`
- `translations/uk/book/00-front-matter/preface.md`
- `translations/uk/book/00-front-matter/table-of-contents.md`
- `translations/uk/book/01-thinking-like-a-principal/README.md`
- `translations/uk/book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md`
- `translations/uk/book/01-thinking-like-a-principal/02-decision-making-under-constraints.md`
- `translations/uk/book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md`
- `translations/uk/book/01-thinking-like-a-principal/04-ownership-beyond-code.md`
- `translations/uk/book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md`
- `translations/uk/book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md`

## Terminology Decisions

- `Principal Engineer` was preserved in English.
- `ownership` was kept as `ownership` where it is a canonical engineering term and translated by context as responsibility language where the sentence required Ukrainian flow.
- `evidence` was rendered as `докази` or preserved as `evidence` when it is part of a canonical law or artifact phrase.
- `judgment` was rendered as `інженерне судження` in reader-facing explanatory prose.
- Canonical PEAK names such as `Change Radius`, `Decision Journal`, `Architecture Review`, `Discoverability`, `Bus Factor`, and IDs were preserved.

## Pending Cross-Phase Links

- Table of Contents names Parts II-VI and Appendix items whose Ukrainian chapter files are not created yet.
- Cross-phase PEAK concept references are preserved as canonical names and IDs until later translation phases create more Ukrainian context.

## Unresolved Translation Questions

- None for reader-facing placeholders.
- Later Terminology Review should decide whether repeated English technical nouns such as `workflow`, `release`, `support`, `field`, and `review` should remain as draft technical register or be made more consistently Ukrainian.

## Validation

- `git diff --check` - passed.
- Source-to-target mapping check for all Phase 1 files - passed.
- `git diff --name-only origin/main...HEAD -- book/` - passed; no English canonical source files changed.
- Placeholder search for `TODO`, `AUTHOR NOTE`, `PLACEHOLDER`, and `TBD` - passed.
- English-leftover review aid grep - inspected; remaining English is mostly canonical technical terminology, artifact names, or draft technical register to revisit during Terminology Review.
- `npm.cmd run lint:md` - passed.
- `npm.cmd run lint:spelling` - passed.
- `python -m mkdocs build --strict` - passed.
- `npx.cmd linkinator "translations/uk/**/*.md" --markdown --recurse --skip "^mailto:" --skip "node_modules" --skip "site" --timeout 60000` - passed.
- `npm.cmd run lint:links` - passed.
- `python -m pip check` - passed.
- `git -c safe.directory=D:/Projects/ThePrincipaEngineerHandbook ls-files site` - passed; no tracked `site/` output.
- `vale .` - passed with 0 errors and 3 existing non-blocking warnings outside the Ukrainian translation files.

## Outcome

Translation Draft complete.

## Phase 1 Terminology Review

Baseline commit before gate: `785ee03a9c94b94a9c04a383b80a624c2247928a`

Outcome: Passed.

Terminology changes made:

- Preserved `Principal Engineer` in English and confirmed it is not rendered as `головний інженер`.
- Replaced several misleading standalone uses of `ownership`, `evidence`, `judgment`, and `constraints` with the glossary-preferred Ukrainian responsibility, evidence, judgment, and constraint language where the term was not intentionally canonical.
- Preserved canonical PEAK names, artifact names, and IDs such as `Evidence Before Confidence`, `Change Radius`, `Decision Journal`, `LAW-005`, `SMELL-001`, and similar references.

Unresolved items:

- Editorial Review should still reduce draft-level English connective prose where it is not a canonical term, code-like text, or preserved artifact language.

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
