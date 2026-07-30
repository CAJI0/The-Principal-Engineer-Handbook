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

## Localization Remediation

- Outcome: Reader-facing Phase 4 prose remediated after the review blocker on large untranslated English paragraphs.
- Scope: `translations/uk/book/04-building-a-product/`
- Notes:
  - Chapters 21-25 received focused localization passes for English-heavy narrative, discussion, exercises, ADR prose, and editor comments.
  - Chapter 20 received targeted cleanup for remaining English-heavy reader-facing lines.
  - Canonical labels, PEAK IDs, artifact names, code spans, commands, file paths, interface literals, and embedded/software terms were preserved where required for correctness.
  - No Phase 4 review gates were completed in this remediation run.
  - Phase 5 was not started.

## Terminology Review

- Outcome: Passed.
- Baseline commit before gate: `4474a08937efc2b84085d566dc6912e780b46f10`
- Source baseline: `v1.0.0` (`5baef38d555712d6e572888285d3715e46fba118`)
- Scope reviewed:
  - `translations/uk/book/04-building-a-product/README.md`
  - `translations/uk/book/04-building-a-product/20-from-prototype-to-product.md`
  - `translations/uk/book/04-building-a-product/21-designing-for-manufacturing-and-field-reality.md`
  - `translations/uk/book/04-building-a-product/22-configuration-variants-and-product-lines.md`
  - `translations/uk/book/04-building-a-product/23-observability-in-embedded-systems.md`
  - `translations/uk/book/04-building-a-product/24-release-discipline-and-upgrade-paths.md`
  - `translations/uk/book/04-building-a-product/25-reference-project-walkthrough.md`
- Findings:
  - Canonical source-to-target coverage passed for the complete Phase 4 scope.
  - Section structure, ADR content, exercises, notebook sections, examples, IDs, code spans, paths, links, and exact literals remain aligned with canonical source and localization governance.
  - Previously reported English heading, quoted-assumption, part-reference, and ordinary-sentence blockers are corrected.
  - Broad Latin-script audit found 324 candidate lines and 55 sentence-like Latin lines. All were classified as governed artifact or concept names, stable IDs, acronyms, versions, paths, exact event/message literals, or the proper name `Field Sensor Gateway`.
  - Exact message literals `write failed`, `unsupported operation`, and `update failed` were verified against canonical source and intentionally retained.
  - No known or unclassified reader-facing English prose remains in Phase 4.
  - Strict UTF-8 integrity passed for all seven Phase 4 files.
  - No canonical English source, governance, tooling, review-record, Phase 5, or later-phase file was modified during the review.
- Remaining terminology questions:
  - None for this gate.
