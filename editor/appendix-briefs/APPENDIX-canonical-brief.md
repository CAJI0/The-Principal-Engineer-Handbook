# Appendix Canonical Brief

## Status

Status: brief-registered
Baseline: b2099e80ba6742cc3f06d3e962f3a38d6245118b
Branch: appendix
Main chapters complete: yes
Reader-facing appendix drafted: no

## Baseline

The Appendix workflow starts from `origin/main` at
`b2099e80ba6742cc3f06d3e962f3a38d6245118b`, after Chapter 37 was merged and registered
as canonical.

Chapter 37 is the final main reader-facing chapter. The Appendix follows Part VI and makes
the handbook operational through reusable forms, templates, and short reference material.

## Scope

This brief covers the Appendix suite only:

- ADR Template.
- RFC Template.
- Decision Journal Template.
- Architecture Review Template.
- Chapter Review Checklist.
- Glossary.

## Non-Goals

- No new PEAK concepts.
- No changes to Chapters 1-37.
- No rewriting existing canon.
- No reader-facing appendix content in this step.
- No PDF/export work in this step.
- No MkDocs/nav restructuring unless required by existing repository policy.
- No new laws, rituals, artifacts, metrics, vocabulary terms, smells, anti-patterns, failure stories, or chapters.

## Appendix Items

### ADR Template

- Intended path: `book/appendix/adr-template.md`.
- Reader job: help a team record an architecture-significant decision, the evidence behind it, rejected options,
  ownership implications, API promises, dependency decisions, risks, and review triggers.
- Canon anchors: `ARTIFACT-001`, `LAW-001`, `LAW-002`, `LAW-005`, `LAW-007`, `METRIC-001`, `METRIC-003`,
  `RITUAL-001`, `RITUAL-004`.
- Boundary: do not turn the template into a long essay about ADRs. Chapter 17 already teaches ADR/RFC usage.
- Risks to avoid: approval-form language, generic status bureaucracy, missing owner, missing evidence, missing
  alternatives, stale accepted decisions with no revisit trigger.

### RFC Template

- Intended path: `book/appendix/rfc-template.md`.
- Reader job: help a team expose a proposed change before it hardens: context, problem, constraints, options, affected
  teams, product promises, operational consequences, rollout plan, and open questions.
- Canon anchors: `ARTIFACT-002`, `LAW-002`, `LAW-005`, `LAW-007`, `ARTIFACT-003`, `ARTIFACT-006`,
  `RITUAL-001`.
- Boundary: do not make this a generic corporate RFC template. It must reflect decisions, ownership, evidence, and
  Change Radius.
- Risks to avoid: consensus theatre, proposal after the decision has already hardened, missing affected owners, vague
  rollout language, and no path from open questions to review.

### Decision Journal Template

- Intended path: `book/appendix/decision-journal-template.md`.
- Reader job: help a reader track the quality of judgment over time: decision, confidence, evidence, assumptions,
  expected signals, review date, result, and what changed.
- Canon anchors: `ARTIFACT-003`, `LAW-005`, `VOCAB-002`, `ARTIFACT-007`, `METRIC-001`, `METRIC-005`.
- Boundary: do not invent `Decision Quality` as a metric. `METRIC-002` is Bus Factor and must remain Bus Factor.
- Risks to avoid: hindsight rewriting, confidence without evidence, no review date, no signal definition, and treating
  small follow-up decisions as full ADRs.

### Architecture Review Template

- Intended path: `book/appendix/architecture-review-template.md`.
- Reader job: help a team review an architecture decision or change before it hardens: context, affected boundaries,
  owners, APIs, state, dependencies, time behavior, failure modes, observability, rollout, and follow-up artifacts.
- Canon anchors: `RITUAL-001`, `ARTIFACT-001`, `ARTIFACT-002`, `ARTIFACT-006`, `LAW-001`, `LAW-002`, `LAW-003`,
  `LAW-005`, `LAW-007`, `METRIC-001`, `METRIC-003`, `METRIC-004`.
- Boundary: do not duplicate Chapter 18. The template should help a reader run the ritual, not retell why the ritual
  matters.
- Risks to avoid: approval-gate posture, code-review drift, missing closure, missing follow-up artifacts, and review
  notes that cannot become shared memory.

### Chapter Review Checklist

- Intended path: `book/appendix/chapter-review-checklist.md`.
- Reader job: help maintain the book itself through author boundary, editorial review, canon review, technical review,
  freeze review, validation, and merge readiness.
- Canon anchors: `BOOK_BIBLE.md`, `STYLE_GUIDE.md`, `editor/EDITOR_LOG.md`, `knowledge/index.yaml`, chapter brief
  files, and the existing four-gate chapter workflow.
- Boundary: this checklist is for maintaining The Principal Engineer Handbook, not for reviewing arbitrary engineering
  documents.
- Risks to avoid: turning the checklist into reader-facing engineering advice, skipping canon assertions, recording
  invented validation results, or weakening the freeze boundary.

### Glossary

- Intended path: `book/appendix/glossary.md`.
- Reader job: give a concise, canonical reader-facing glossary of PEAK terms, laws, artifacts, rituals, metrics,
  smells, anti-patterns, and failure stories used across the book.
- Canon anchors: `knowledge/index.yaml`, all canonical concept names and IDs, and all canonical chapter relationships.
- Boundary: do not write mini-chapters. Each entry should be short, precise, and cross-reference-friendly. Do not
  change concept definitions unless an explicit ADR is created and accepted.
- Risks to avoid: redefining canon, adding new PEAK terms, hiding ID/name mismatches, long explanatory essays, or using
  the glossary as a seventh part of the book.

## Canon Dependencies

Existing concepts only:

- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-005` - Evidence Before Confidence.
- `LAW-007` - Every Dependency Is a Decision.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-001` - Architecture Review.
- `RITUAL-004` - Architecture Health Review.
- `VOCAB-001` - Change Radius.
- `VOCAB-002` - Weak Signal.
- `VOCAB-007` - Architecture Health.
- `METRIC-001` - Change Radius.
- `METRIC-002` - Bus Factor.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `METRIC-005` - Architecture Health.
- `SMELL-001` - Silent Coupling.
- `SMELL-002` - Utility Gravity.
- `SMELL-003` - Boolean Explosion.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-006` - Temporary Solution.
- `FAILURE-004` - The Hero Engineer.
- `FAILURE-005` - The Release We Should Have Delayed.

Guardrail: `METRIC-002` is Bus Factor. It must not be renamed or reused as Decision Quality.

## File Plan

The future Appendix Author Draft should create these six reader-facing appendix files in one coherent Appendix pass,
unless the owner explicitly asks to split them:

- `book/appendix/adr-template.md`.
- `book/appendix/rfc-template.md`.
- `book/appendix/decision-journal-template.md`.
- `book/appendix/architecture-review-template.md`.
- `book/appendix/chapter-review-checklist.md`.
- `book/appendix/glossary.md`.

This canonical brief registration must not create those reader-facing appendix files.

## Registry Policy

No `knowledge/index.yaml` changes in this step, because the current registry does not yet define appendix entities and
no new PEAK concepts are being created.

The following local editorial identifiers may be used inside appendix planning or future review notes, but they are not
PEAK concept IDs:

- `APPENDIX-ADR-TEMPLATE`.
- `APPENDIX-RFC-TEMPLATE`.
- `APPENDIX-DECISION-JOURNAL-TEMPLATE`.
- `APPENDIX-ARCHITECTURE-REVIEW-TEMPLATE`.
- `APPENDIX-CHAPTER-REVIEW-CHECKLIST`.
- `APPENDIX-GLOSSARY`.

## Reader-Facing Style

For the future Appendix Author Draft:

- Use direct, practical templates.
- Keep instructions inside templates short.
- Use placeholder-friendly fields.
- Avoid decorative prose.
- Avoid generic management language.
- Avoid unexplained acronyms.
- Avoid long examples unless essential.
- Make each item printable or copyable.
- Make each item useful without requiring the reader to reread a chapter.

## Validation Requirements

For this brief registration, run all applicable checks that do not require nonexistent appendix files. At minimum, run
`git diff --check` and `git status --short`, plus the repository's available lightweight validation commands.

For the future Appendix Author Draft, run the normal repository checks after creating the six appendix files. Do not
track generated `site/` output, caches, or unrelated generated artifacts.

## Author Draft Instructions

Next stage: Appendix Author Draft
Expected branch: appendix
Expected commit subject: docs(appendix): add appendix draft

The future Author Draft should create all six appendix files in one coherent Appendix pass unless the owner explicitly
asks to split them.

## Open Questions

None.
