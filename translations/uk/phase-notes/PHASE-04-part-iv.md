# Ukrainian Translation Phase 4 - Part IV

## Source Baseline

- English source tag: `v1.0.0`
- English source commit: `5baef38d555712d6e572888285d3715e46fba118`

## Scope

- Part IV - Building a Product
- Source directory: `book/04-building-a-product/`
- Target directory: `translations/uk/book/04-building-a-product/`

## Files Translated

- [x] README
- [x] Chapter 20 - From Prototype to Product
- [x] Chapter 21 - Designing for Manufacturing and Field Reality
- [x] Chapter 22 - Configuration, Variants, and Product Lines
- [x] Chapter 23 - Observability in Embedded Systems
- [x] Chapter 24 - Release Discipline and Upgrade Paths
- [x] Chapter 25 - Reference Project Walkthrough

## Terminology Notes

- `prototype` rendered as `прототип` where natural; canonical phrase `The Successful Prototype` remains English with `FAILURE-003`.
- `productization` preserved as `productization` where it names the chapter-local gap; Ukrainian explanation uses `перехід від прототипу до продукту`.
- `manufacturing` rendered as `виробництво` in headings/prose; kept as `manufacturing` in mixed technical register when paired with existing English product terms.
- `field reality`, `field device`, and `field trial` use Ukrainian surrounding prose with `field` preserved where it acts as embedded/product-domain register.
- `service tool`, `firmware`, `gateway`, `release`, `rollback`, `release candidate`, `Event Catalog`, and `reference project` remain mostly English technical terms with Ukrainian surrounding prose.
- `configuration`, `variant`, `product line`, `observability`, `telemetry`, `diagnostics`, `upgrade path`, and `update path` require Terminology Review for final consistency across Part IV.

## Structural Notes

- Section structure, H1/H2/H3 hierarchy, notebook sections, exercises, ADR shapes, IDs, code spans, commands, paths, and API-like names were preserved.
- The English Part IV README author note was not copied; the Ukrainian README contains a concise reader-facing overview and links to Chapters 20-25.
- No links to Phase 5 files were created.
- Draft intentionally preserves a mixed Ukrainian/English engineering register for embedded/product terms that should be resolved or accepted during Terminology Review.

## Validation

- `git diff --check` - passed.
- `git status --short` - passed; only Phase 4 Ukrainian draft files and this phase note are untracked before staging.
- `npm.cmd run lint:md` - passed.
- `npm.cmd run lint:spelling` - passed; repository cspell policy currently excludes `translations/uk/**` from English-oriented spelling checks.
- `npm.cmd run lint:links` - passed.
- `npx.cmd linkinator "translations/uk/**/*.md" --markdown --recurse --skip "^mailto:" --skip "node_modules" --skip "site" --timeout 60000` - passed.
- `python -m pip check` - passed.
- No English source changes - passed.
- No Phase 5 files created - passed.
- No generated `site/` output committed - passed.

## Outcome

Translation Draft complete. Ready for Terminology Review.
