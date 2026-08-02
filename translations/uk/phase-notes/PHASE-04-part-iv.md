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

## Terminology Review - Post-Editorial-Remediation Re-review

- Outcome: Passed.
- Baseline commit before gate: `6c29696c7de62652d33c6c67284063b3e0e8c40d`
- Previous terminology record: `c3d24860c246e409d07781f51c041af2f9761904`
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
  - This is a fresh Gate 1 review of the post-remediation reader-facing state, not a reuse of the historical Gate 1 record.
  - Canonical source-to-target coverage passed for the complete seven-file Phase 4 scope.
  - Remediation changes from `c3d24860c246e409d07781f51c041af2f9761904` to `6c29696c7de62652d33c6c67284063b3e0e8c40d` were compared against canonical `v1.0.0`, the pre-remediation Ukrainian text, and the remediated Ukrainian text.
  - Ownership-calque replacements preserve the canonical responsibility, authority, stewardship, evidence-accountability, and chapter-scope meanings.
  - Artifact-recording replacements preserve the canonical ADR, RFC, Decision Journal, Event Catalog, Architecture Ledger, and Mistake Ledger lifecycle meanings.
  - The graph-weight remediation preserves the canonical statement that no new PEAK concept is introduced and emphasis remains on the registered relationship set.
  - Stable PEAK IDs, links, code spans, versions, and exact message literals remain aligned with canonical source and localization governance.
  - Broad Latin-script audit found 324 candidate lines. All inspected sentence-like candidates were classified as governed canonical names, artifact or concept names, stable IDs, acronyms, versions, paths, exact message literals, or the proper name `Field Sensor Gateway`.
  - Exact message literals `write failed`, `unsupported operation`, `communication failed`, and `update failed` were verified in machine-visible contexts and intentionally retained.
  - Strict UTF-8 integrity passed for all seven Phase 4 files, with no replacement characters, `???` substitution, mojibake patterns, or suspicious loss of Cyrillic text.
  - The remediation commit changed only Chapters 20-25 in the Phase 4 scope and did not modify the README, Gate records, phase notes, governance files, glossary, tooling, canonical `book/`, Phase 5, later phases, or unrelated files.
- Remaining terminology questions:
  - None for this gate.

## Terminology Review - Post-Editorial-Remediation 2 Re-review

- Outcome: Passed.
- Baseline commit before gate: `353afa32039f59305e14b7805682672915293724`
- Previous terminology record: `3ed3a55d3519cfaefef2e656f788b2cd74ad986f`
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
  - This is a fresh Gate 1 review of the reader-facing state after `fix(translation): resolve phase 4 editorial blockers`, not a reuse of either historical Gate 1 record.
  - Canonical source-to-target coverage passed for the complete seven-file Phase 4 scope.
  - The remediation diff from `3ed3a55d3519cfaefef2e656f788b2cd74ad986f` to `353afa32039f59305e14b7805682672915293724` was compared against canonical `v1.0.0`, the pre-remediation Ukrainian text, and the current Ukrainian text.
  - The `field escape` remediation preserves the canonical distinction among defects found in manufacturing, defects found in field conditions, containment, evidence, and corrective action.
  - The `map` remediation preserves the canonical relation between internal state and support-safe diagnostic reasons.
  - The `bring-up`, `authority`, `reopen decision`, `expose assumptions`, and `open Architecture Review` remediations preserve the intended technical or governance action without changing terminology policy.
  - Stable PEAK IDs, links, code spans, versions, exact message literals, governed artifact names, and the proper name `Field Sensor Gateway` remain aligned with canonical source and localization governance.
  - Broad Latin-script audit found 324 candidate lines and 48 sentence-like Latin lines. All inspected candidates were classified as governed canonical names, artifact or concept names, stable IDs, acronyms, versions, paths, exact message literals, links, or proper names.
  - Exact message literals `write failed`, `unsupported operation`, `communication failed`, and `update failed` were verified in machine-visible contexts and intentionally retained.
  - Strict UTF-8 integrity passed for all seven Phase 4 files, with no replacement characters, `???` substitution, mojibake patterns, or suspicious loss of Cyrillic text.
  - The remediation commit changed only Chapters 20-25 in the Phase 4 scope and did not modify the README, Gate records, phase notes, governance files, glossary, tooling, canonical `book/`, Phase 5, later phases, or unrelated files.
- Remaining terminology questions:
  - None for this gate.

## Terminology Review - Post-Editorial-Remediation 3 Re-review

- Outcome: Passed.
- Baseline commit before gate: `65e32af63b0b5e78e7a2a7c2e6d9b6a7e14d95eb`
- Previous terminology record: `dc6674c72c0fee4898175166ea3ea2d1c1f387fa`
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
  - This is a fresh Gate 1 review of the reader-facing state after `fix(translation): resolve residual phase 4 editorial calques`, not a reuse of any historical Gate 1 record.
  - Canonical source-to-target coverage passed for the complete seven-file Phase 4 scope.
  - The remediation diff from `dc6674c72c0fee4898175166ea3ea2d1c1f387fa` to `65e32af63b0b5e78e7a2a7c2e6d9b6a7e14d95eb` was compared against canonical `v1.0.0`, the pre-remediation Ukrainian text, and the current Ukrainian text.
  - The Chapter 23 Mistake Ledger remediation preserves that the ledger records false assumptions whose consequences became visible in field operation, without implying that the assumptions themselves physically moved or escaped.
  - Stable PEAK IDs, links, code spans, versions, exact message literals, governed artifact names, canonical concept names, and the proper name `Field Sensor Gateway` remain aligned with canonical source and localization governance.
  - Broad Latin-script audit found 324 candidate lines and 11 sentence-like lines after filtering code spans, links, stable IDs, acronyms, and governed names. All inspected candidates were classified as governed canonical names, artifact or concept names, stable IDs, acronyms, versions, paths, exact message literals, links, or proper names.
  - Exact message literals `write failed`, `unsupported operation`, `communication failed`, and `update failed` were verified in machine-visible contexts and intentionally retained.
  - Strict UTF-8 integrity passed for all seven Phase 4 files, with no replacement characters, `???` substitution, mojibake patterns, or suspicious loss of Cyrillic text.
  - The remediation commit changed only Chapter 23 in the Phase 4 scope and did not modify the README, Gate records, phase notes, governance files, glossary, tooling, canonical `book/`, Phase 5, later phases, or unrelated files.
- Remaining terminology questions:
  - None for this gate.

## Ukrainian Editorial Review - Post-Editorial-Remediation 3 Re-review

- Outcome: Passed.
- Baseline commit before gate: `fe4c9b0f17b001bfc5eae2845fb05587b95056d7`
- Reader-facing translation state reviewed: `65e32af63b0b5e78e7a2a7c2e6d9b6a7e14d95eb`
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
  - The complete seven-file Phase 4 scope was read as Ukrainian handbook prose after the fresh terminology re-review.
  - The Chapter 23 Mistake Ledger sentence changed in `65e32af63b0b5e78e7a2a7c2e6d9b6a7e14d95eb` is natural Ukrainian in context and preserves the canonical meaning of false assumptions whose consequences manifested during field operation.
  - The previous literal `припущення, що втекли в поле` blocker is absent from the reader-facing Phase 4 tree.
  - Known `field escape` defect formulations in Chapters 21 and 23 remain natural and precise as defects or wrong assumptions discovered in field conditions.
  - Remaining `вислизнуло` / `вислизнули` uses in Chapters 24 and 25 match canonical `almost escaped`, `escaped release assumptions`, or `escaped assumptions discovered during pilot` contexts and do not repeat the Chapter 23 physical-motion calque.
  - Ownership and responsibility language remains natural; no blocker-level `володіє` ownership calque was found.
  - `зіставляє`, `відображення`, `повʼязати`, bring-up / logging-level wording, authoritative-source wording, decision reopening, ADR/RFC/Event Catalog recording actions, and the graph-weight construction were inspected in context and remain idiomatic or technically justified.
  - Exact message literals `write failed`, `unsupported operation`, `communication failed`, and `update failed` remain only in machine-visible support-tool or product-output contexts.
  - No new Ukrainian grammar, syntax, agreement, punctuation, referent, agency, responsibility, authority, artifact-lifecycle, or decision-boundary blocker was found.
- Remaining editorial questions:
  - None for this gate.
