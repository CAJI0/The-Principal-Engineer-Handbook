# Editor Log

Chronological log of editorial maintenance work.

## 2026-07-03

- Bootstrapped Sprint 0 repository foundation.
- Reviewed Sprint 0 repository foundation and recorded cleanup recommendations.
- Started Sprint 1 reader-facing manuscript work by creating front matter before chapters.
- Added manifesto, preface, and table of contents to keep the project architecture-first.
- Defined the canonical chapter architecture before drafting Chapter 1.
- Started Sprint 3 and created the first manuscript chapter.
- Applied the canonical chapter architecture to Chapter 1.
- Introduced PEAK as the internal knowledge model behind the handbook.
- Moved the project from a linear manuscript toward a knowledge-backed handbook.
- Established that future chapters should reuse PEAK concepts instead of redefining them.

## Sprint 4 Knowledge Architecture

- Introduced PEAK as a structured knowledge model.
- Treated the handbook as one rendering of a broader engineering knowledge graph.
- Added stable IDs, relationship types, and the first machine-readable knowledge index.

## Sprint 5 Architecture Review 0

- The project paused manuscript expansion to review repository architecture and PEAK knowledge architecture.
- This follows the handbook's own principle that architecture should be reviewed before scaling implementation.

## Sprint 6 Foundation Cleanup Before Freeze

- Resolved main Architecture Review 0 actions before Freeze 0.
- Defined source-of-truth rules for manuscript, documentation, knowledge concepts, canon, book architecture, and templates.
- Made stable knowledge IDs visible in existing concept Markdown files.
- Clarified that `book/` is canonical manuscript source and `docs/` is publishing support.

## Phase 2 Chapter 1 Reviews

- Chapter: What Is a Principal Engineer?
- Editorial Review: Approved with minor changes.
- Editorial result: tightened narrative flow, reduced repetition, and preserved the chapter's central thesis.
- Canon Review followed as a separate stage.
- Canon Review: Approved with minor changes.
- Canon result: resolved the chapter-level principle versus PEAK law conflict, clarified the chapter-local ADR label, and aligned CHAPTER-001 PEAK relationships.
- Technical Review followed as a separate stage.
- Technical Review: Approved with minor changes.
- Technical result: tightened technical precision around story causality, duplicated assumptions, role contrast, technical debt, abstraction obligations, decision timing, decision retirement, and the architecture exercise.
- Unresolved AUTHOR NOTE items: none.
- Freeze Review has not been performed.

## Phase 2 Chapter 1 Technical Review Remediation

- Chapter: What Is a Principal Engineer?
- Stage: Technical Review remediation.
- Outcome: Approved with minor changes.
- Remaining technical review areas examined: manufacturing-story causality, duplicated assumptions, role distinction, technical debt, abstraction obligations, decision lifecycle, architecture exercise, and remaining absolutes.
- Corrections: clarified investigation signals versus confirmed cause, replaced unowned duplication wording with an authoritative calibration contract, clarified retirement of commitments versus preservation of decision records, and tightened architecture exercise criteria.
- Unresolved AUTHOR NOTE items: none.
- Freeze Review has not been performed.

## Phase 2 Chapter 1 Freeze Review

- Chapter: What Is a Principal Engineer?
- Stable ID: CHAPTER-001.
- Stage: Freeze Review.
- Baseline commit reviewed: 7825661b612573c5a0ce43ce22df26ecc532e39f.
- Outcome: Approved.
- Prior review stages present: Editorial Review, Canon Review, Technical Review, and Technical Review remediation.
- Freeze Criteria checked: review history, one central idea, canonical chapter architecture,
  editorial stability, canon stability, technical stability, story credibility, PEAK integrity,
  and reader value.
- Manuscript changes made: none.
- Unresolved AUTHOR NOTE items: none in Chapter 1.
- Validation commands and results:
  - `git diff --check`: passed.
  - Direct Python Freeze checks: section order, AUTHOR NOTE, conflict markers, CHAPTER-001 uniqueness,
    path resolution, relationships, supported statuses, supported relationship types, and lifecycle state passed.
  - `npm run lint:md`: not run; `npm` is unavailable in the local PATH.
  - `npm run lint:spelling`: not run; `npm` is unavailable in the local PATH.
  - `npm run lint:links`: not run; `npm` is unavailable in the local PATH.
  - `vale docs`: not run; `vale` is unavailable in the local PATH.
  - `mkdocs build --strict`: not run; `mkdocs` is unavailable in the local PATH.
- Final lifecycle state: CHAPTER-001 moved from draft to canonical.
- Chapter 1 is Frozen.
- Future substantive changes require reopening the chapter at the appropriate review stage.

## Chapter 1 Post-Freeze Consistency Maintenance

- Removed the stale `(Draft)` marker from the reader-facing table of contents.
- Chapter 1 remains Frozen and canonical.
- Manuscript content changed: none.
- Review stage reopened: none.

## Pre-Chapter 2 Canon Classification Alignment

- Found classification drift between the editorial canon summary and the PEAK registry.
- Moved `LAW-002` through `LAW-006` from the Maxims summary to the Laws summary.
- PEAK IDs, concept files, statuses, and relationships changed: none.
- Chapter 1 remains Frozen and canonical.
- Chapter 2 was not started.

## Phase 2 Chapter 2 Draft

- Title: Decision-Making Under Constraints.
- Stable ID: CHAPTER-002.
- Manuscript path: `book/01-thinking-like-a-principal/02-decision-making-under-constraints.md`.
- Central idea: a sound engineering decision makes constraints, evidence, uncertainty, consequences,
  and cost of reversal explicit before committing.
- Story type: embedded-product release and hardware-freeze decision under memory, recovery, scope,
  schedule, and qualification constraints.
- Primary PEAK concepts used: `LAW-005`, `ARTIFACT-003`, and `VOCAB-001`.
- Supporting PEAK concepts used: `LAW-004` and `LAW-006`.
- Chapter-local ADR title: Preserve Recovery by Reducing Scope.
- Status: Draft.
- Editorial Review has not been performed.
- Canon Review has not been performed.
- Technical Review has not been performed.
- Freeze Review has not been performed.
- Chapter 1 remains Frozen and canonical.

## Phase 2 Chapter 2 Editorial Review

- Chapter: Decision-Making Under Constraints.
- Stable ID: CHAPTER-002.
- Branch: `chapter2`.
- Stage: Editorial Review.
- Current `origin/main` tip: `1e01e56`.
- Current `origin/chapter2` tip: `dc4b926`.
- Current merge base: `1e01e56`.
- Current Draft baseline commit: `da10687`.
- Outcome: Approved with minor changes.
- Major editorial improvements: tightened the opening quote, smoothed story rhythm, removed meta-manuscript wording,
  reduced repeated discussion, integrated PEAK references into natural prose, and strengthened the closing transition.
- Material intentionally preserved: embedded-product release story, central constrained-decision thesis, final engineering
  decision, Decision Journal example fields, chapter-local ADR structure, required chapter architecture, and all existing
  PEAK references.
- Unresolved `AUTHOR NOTE` items: none.
- Chapter 1 remains Frozen and canonical.
- Canon Review has not been performed.
- Technical Review has not been performed.
- Freeze Review has not been performed.
- Branch merged: no.

## Phase 2 Chapter 2 Canon Review

- Chapter: Decision-Making Under Constraints.
- Stable ID: CHAPTER-002.
- Branch: `chapter2`.
- Stage: Canon Review.
- Current `origin/main` tip: `1e01e56`.
- Current `origin/chapter2` tip: `e67bf6c`.
- Current merge base: `1e01e56`.
- Current Editorial Review baseline: `e67bf6c`.
- Outcome: Approved.
- Central idea verified: the chapter remains focused on making constraints, evidence, uncertainty, consequences, and
  reversal cost explicit before committing.
- Chapter-boundary result: distinct from Chapter 1, not a release-management chapter, not a Decision Journal tutorial,
  and not an early draft of Chapter 3.
- Terminology reviewed: constraint language remains descriptive, not a formal taxonomy; reversibility, ownership,
  decision quality, and accepted risk do not introduce new PEAK concepts.
- PEAK relationships preserved: `CHAPTER-002 illustrates LAW-005`; `CHAPTER-002 references ARTIFACT-003`;
  `CHAPTER-002 references VOCAB-001`; `CHAPTER-002 references LAW-004`; `CHAPTER-002 references LAW-006`.
- PEAK relationships added, removed, or corrected: none.
- Chapter-local ADR result: reader-facing, locally scoped, unregistered, and structurally consistent.
- Chapter 1 continuity result: Chapter 2 builds on future system cost and decision discipline without reopening or
  contradicting Chapter 1.
- Unresolved canon issues: none.
- Unresolved `AUTHOR NOTE` items: none.
- Chapter 1 remains Frozen and canonical.
- Technical Review has not been performed.
- Freeze Review has not been performed.
- Branch merged: no.

## Phase 2 Chapter 2 Technical Review

- Chapter: Decision-Making Under Constraints.
- Stable ID: CHAPTER-002.
- Branch: `chapter2`.
- Stage: Technical Review.
- Current Canon Review baseline commit: `6085a8a`.
- Outcome: Approved with minor changes.
- Technical areas reviewed: software update and recovery model, meaning of validation and evidence, memory constraint
  credibility, complex update mechanism, prototype evidence, interrupted-update examples, hardware qualification,
  release commitments, recovery versus diagnostics, speculative flexibility, simplicity claims, Change Radius,
  reversibility, decision quality versus outcome quality, risk ownership, review triggers, Decision Journal confidence,
  architecture exercise, and chapter-local ADR consistency.
- Technical corrections applied: replaced architecture-specific or guarantee-sounding recovery wording with neutral
  recovery capability, recoverable update path, and validated recovery mode language.
- Story-causality result: credible embedded-product release scenario; no unsupported causal leap found.
- Update and recovery model result: preserved as a general recoverable update trade-off without prescribing dual-bank,
  full-image rollback, compression, or delta-update architecture.
- Change Radius and reversibility result: technically distinct and credible; reversibility is treated as evidence
  threshold and learning capacity, not safety.
- Unresolved technical issues: none.
- Unresolved `AUTHOR NOTE` items: none.
- Chapter 1 remains Frozen and canonical.
- Freeze Review has not been performed.
- Branch merged: no.

## Phase 2 Chapter 2 Freeze Review

- Chapter: Decision-Making Under Constraints.
- Stable ID: CHAPTER-002.
- Branch: `chapter2`.
- Stage: Freeze Review.
- Technical Review baseline commit: `847db1aec67e93d961512f66e61c908dc342e7c8`.
- Outcome: Request changes.
- Prior review stages present: Draft, Editorial Review, Canon Review, and Technical Review.
- Freeze Criteria checked: review history, one central idea, distinct chapter role, canonical chapter architecture,
  editorial stability, canon stability, technical stability, story credibility, PEAK integrity, Decision Journal
  integrity, chapter-local ADR integrity, reader value, timelessness, and repository validation.
- Manuscript changes made: none.
- PEAK integrity result: Chapter 2 structure, path, status, and relationships are valid; `CHAPTER-002` remains `draft`
  because repository validation did not pass.
- Unresolved canon issues: none.
- Unresolved technical issues: none.
- Unresolved `AUTHOR NOTE` items: none.
- Validation commands and results:
  - Direct Freeze checks: passed.
  - `git diff --check`: passed.
  - YAML parse for `knowledge/index.yaml`: passed.
  - `npm.cmd run lint:md`: passed.
  - `npm.cmd run lint:spelling`: passed.
  - `npm.cmd run lint:links`: passed.
  - `vale book/01-thinking-like-a-principal/02-decision-making-under-constraints.md editor/EDITOR_LOG.md`: failed
    because configured Vale styles are missing from the local styles path.
  - `mkdocs build --strict`: failed because the configured Markdown extension package is missing.
- Final lifecycle state: CHAPTER-002 remains `draft`.
- Chapter 2 is not Frozen.
- Chapter 1 remains Frozen and canonical.
- Branch merged: no.
- Chapter 3 started: no.

## Phase 2 Chapter 2 Freeze Validation Remediation

- Chapter: Decision-Making Under Constraints.
- Stable ID: CHAPTER-002.
- Branch: `chapter2`.
- Stage: Freeze Validation Remediation.
- Previous Freeze Review outcome: Request changes.
- Previous blockers: Vale configured styles were not available to the local Vale installation; `mkdocs build --strict`
  could not complete because required documentation dependencies were unavailable or incomplete.
- Vale diagnosis: repository-local style and vocabulary are now available under `.vale/`; external package styles are not
  required by the active repository configuration.
- Vale remediation applied: repository Vale configuration and vocabulary were stabilized before this record; no manuscript
  edits were made during this remediation.
- Vale command and result: `vale --config .vale.ini book/01-thinking-like-a-principal/02-decision-making-under-constraints.md`
  passed with 0 errors, 0 warnings, and 0 suggestions; `vale .` passed with 0 errors and 5 existing AuthorBoundary warnings
  outside Chapter 2.
- MkDocs diagnosis: `mkdocs.yml` directly uses `pymdownx.*` extensions, but `pymdown-extensions` was not declared in
  `requirements.txt`; optional PDF export also caused the default strict site build to fail when PDF export was disabled.
- MkDocs remediation applied: declared `pymdown-extensions` explicitly; kept default `mkdocs.yml` as the strict site-build
  configuration; moved PDF export to `mkdocs-pdf.yml`; updated README commands.
- MkDocs command and result: `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`
  passed; `$env:ENABLE_PDF_EXPORT = "1"; python -m mkdocs build --config-file mkdocs-pdf.yml` passed.
- Other validation commands and results: `git diff --check` passed; `npm.cmd run lint:md` passed; `npm.cmd run lint:spelling`
  passed; `npm.cmd run lint:links` passed; `knowledge/index.yaml` parsed successfully; `python -m pip check` passed.
- Manuscript changed: no.
- Canon changed: no.
- PEAK changed: no.
- `CHAPTER-001` remains `canonical`.
- `CHAPTER-002` remains `draft`.
- Unresolved validation blockers: none for the previous Freeze Review blockers.
- Remediation outcome: Approved with minor changes.
- Freeze Review Retry has not been performed.
- Branch merged: no.
- Chapter 3 started: no.

## Phase 2 Chapter 2 Freeze Review Retry

- Chapter: Decision-Making Under Constraints.
- Stable ID: CHAPTER-002.
- Branch: `chapter2`.
- Technical Review baseline commit: `847db1aec67e93d961512f66e61c908dc342e7c8`.
- Freeze Validation Remediation baseline commit: `fbcb07d`.
- Previous Freeze Review outcome: Request changes.
- Freeze Validation Remediation outcome: Approved with minor changes.
- Retry outcome: Approved.
- Review-history verification: Draft, Editorial Review, Canon Review, Technical Review, previous Freeze Review, and
  Freeze Validation Remediation records are present and distinct.
- Freeze Criteria result: central idea, chapter architecture, editorial stability, canon stability, technical stability,
  PEAK integrity, and validation remediation were checked and passed.
- Validation commands and results:
  - `git status --short`: only `knowledge/index.yaml` changed before this log entry.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed.
  - `npm.cmd run lint:spelling`: passed.
  - `npm.cmd run lint:links`: passed.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/02-decision-making-under-constraints.md`: passed with
    0 errors, 0 warnings, and 0 suggestions.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed.
  - `vale .`: passed with 0 errors and 5 existing AuthorBoundary warnings outside Chapter 2.
  - `knowledge/index.yaml` parsed successfully.
- Manuscript changes made: none.
- PEAK integrity result: `CHAPTER-002` exists exactly once, path resolves, expected relationships are present, targets
  exist, relationship types are supported, and no duplicate relationship edge exists.
- Unresolved canon issues: none.
- Unresolved technical issues: none.
- Unresolved validation blockers: none.
- Unresolved `AUTHOR NOTE` items: none in Chapter 2.
- Final lifecycle state: `CHAPTER-002` moved from `draft` to `canonical`.
- Chapter 2 is Frozen.
- Future substantive changes require reopening the chapter at the appropriate review stage.
- Chapter 1 remains Frozen and canonical.
- Branch merged: no.
- Chapter 3 started: no.

## Phase 3 Chapter 3 Draft

- Chapter: Asking Better Engineering Questions.
- Stable ID: CHAPTER-003.
- Branch: `chapter3`.
- Baseline `main` commit: `3bdf3e9d38b98784235415e4ce339b815b12f6dc`.
- Lifecycle stage: Draft.
- Central idea: better engineering questions make hidden assumptions testable before those assumptions become architecture.
- Story type: intermittent stale-state investigation across a device, gateway, and user-facing application.
- Engineering Principle: Better questions make assumptions testable before they become architecture.
- Architecture Exercise: rewrite one unresolved engineering question by separating observations, interpretations,
  assumptions, boundaries, explanations, discriminating evidence, ownership, and the next evidence-gathering action.
- Chapter ADR: Define Authoritative State and Freshness Semantics.
- PEAK concepts reused: `LAW-005`, `VOCAB-002`, `ARTIFACT-007`, `LAW-001`, `LAW-002`, `LAW-003`, `SMELL-001`,
  `SMELL-004`, `RITUAL-001`, and `METRIC-003`.
- Files changed: `book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md`,
  `knowledge/index.yaml`, and `editor/EDITOR_LOG.md`.
- Validation commands and results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed.
  - `npm.cmd run lint:spelling`: passed.
  - `npm.cmd run lint:links`: passed.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md`: passed with
    0 errors, 0 warnings, and 0 suggestions.
  - `python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed.
  - `knowledge/index.yaml` parsed successfully.
- New PEAK concepts: none.
- Canon changed: no.
- Frozen chapters changed: no.
- Chapter 4 started: no.
- Next required lifecycle stage: Editorial Review.

## Phase 3 Chapter 3 Editorial Review

- Chapter: Asking Better Engineering Questions.
- Stable ID: CHAPTER-003.
- Branch: `chapter3`.
- Reviewed baseline commit: `0b67babf033d8f3aa4ac40bf802d2f6ce3f4b18c`.
- Lifecycle stage: Editorial Review.
- Review scope: clarity, structure, narrative flow, pacing, chapter architecture, continuity with Chapters 1 and 2,
  prose quality, reader comprehension, repetition, and style-guide compliance.
- Review outcome: Approved with minor changes.
- Central-idea assessment: preserved; the chapter remains focused on making hidden assumptions testable before they
  become architecture.
- Story assessment: the stale-state story establishes customer-visible contradiction, plausible local questions, and a
  Principal Engineer intervention that reshapes the inquiry rather than solving the incident by authority.
- Structure and flow assessment: the chapter follows the canonical chapter architecture and moves from story, to
  reasoning, to principle, exercise, notebook, ADR, and commentary.
- Repetition and pacing assessment: purposeful reinforcement remains; no excessive repetition required structural
  removal.
- Continuity with Chapters 1 and 2: Chapter 3 advances Chapter 1's question discipline and stops before Chapter 2's
  option selection and commitment-management territory.
- Chapter-boundary assessment: clarified that the chapter-local ADR represents the resulting decision after the inquiry
  becomes answerable, not a decision made before evidence is gathered.
- Engineering Principle assessment: preserved exactly and supported by the story and discussion.
- Architecture Exercise assessment: practical, evidence-oriented, and bounded before architectural option selection;
  final question preserved.
- Principal's Notebook assessment: concise, distinct from Chapters 1 and 2, and supported by the chapter.
- Chapter ADR assessment: locally scoped, credible, and sequenced after the inquiry; it does not become a handbook-wide
  mandate.
- Editor's Commentary assessment: states the chapter's role after Chapters 1 and 2 and points to the next planned topic
  without starting Chapter 4.
- PEAK-reference readability assessment: references support the narrative and do not require Canon Review changes.
- Editorial changes made: clarified the story-to-ADR chronology and tightened the transition showing that the ADR follows
  the shaped inquiry.
- Unresolved editorial issues: none.
- Remaining `AUTHOR NOTE` items: none.
- Files changed: `book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md` and
  `editor/EDITOR_LOG.md`.
- Validation commands and results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed.
  - `npm.cmd run lint:spelling`: passed.
  - `npm.cmd run lint:links`: passed.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed.
- Canon changed: no.
- PEAK index changed: no.
- Frozen chapters changed: no.
- Chapter 4 started: no.
- Next lifecycle stage: Canon Review.

## Pre-Chapter 3 Canon Classification Alignment

- Branch: `chapter3`.
- Baseline commit: `1b5df5cfd9d249401f0ce7c4a2dbe6037d224528`.
- Issue found: `Weak Signal` was incorrectly summarized under Smells in `editor/CANON.md`.
- Authoritative classification: `VOCAB-002`, type `vocabulary`.
- Correction made: moved the summary entry from Smells to Vocabulary.
- Concept identity changed: no.
- Stable ID changed: no.
- Concept file changed: no.
- `knowledge/index.yaml` changed: no.
- PEAK relationships changed: no.
- Manuscript changed: no.
- Frozen chapters changed: no.
- Chapter 3 lifecycle state changed: no.
- Chapter 4 started: no.
- Chapter 3 Canon Review performed: no.
- Next lifecycle stage: Chapter 3 Canon Review.

## Phase 3 Chapter 3 Canon Review

- Chapter: Asking Better Engineering Questions.
- Stable ID: CHAPTER-003.
- Branch: `chapter3`.
- Reviewed baseline commit: `fee89e71243f12af07515a602d1672da85676bea`.
- Lifecycle stage: Canon Review.
- Review scope: central idea, chapter boundaries, canonical terminology, PEAK concept reuse, Chapter 3 relationships,
  concept duplication, chapter-local Engineering Principle, chapter-local ADR, and chapter architecture.
- Review outcome: Approved with minor changes.
- Central-idea result: preserved; every major section supports making hidden assumptions testable before they become
  architecture.
- Chapter-boundary result relative to Chapters 1 and 2: Chapter 3 builds on Chapter 1's question discipline and stops
  before Chapter 2's option selection, accepted risk, and commitment-management work.
- Later-chapter boundary result: ownership, evidence quality, incident handling, and Architecture Review remain bounded
  support topics rather than replacement chapter theses.
- Terminology result: canonical names and IDs are used correctly for `LAW-005`, `LAW-001`, `LAW-002`, `LAW-003`,
  `VOCAB-002`, `ARTIFACT-007`, `SMELL-001`, `SMELL-004`, and `RITUAL-001`.
- Undefined-term result: no undefined canonical terminology found.
- Canonical-name and stable-ID result: all explicit PEAK IDs in the manuscript exist and match their entity types.
- PEAK concept reuse result: existing concepts are reused without redefining them.
- Concept-duplication result: no duplicate law, ritual, artifact, metric, smell, or vocabulary concept is implied.
- New-concept requirement: none.
- Chapter-local Engineering Principle result: preserved exactly and not registered as a PEAK law or principle.
- Chapter-local ADR result: locally scoped; wording clarified so device ownership is a story-local decision, not a
  universal mandate.
- Existing Chapter 3 relationships audited: `CHAPTER-003 illustrates LAW-005`; `CHAPTER-003 references VOCAB-002`;
  `CHAPTER-003 references LAW-001`; `CHAPTER-003 references LAW-002`; `CHAPTER-003 references LAW-003`;
  `CHAPTER-003 references SMELL-004`.
- Relationships retained: all existing Chapter 3 relationships.
- Relationships added: `CHAPTER-003 references SMELL-001`; `CHAPTER-003 references ARTIFACT-007`;
  `CHAPTER-003 references RITUAL-001`.
- Relationships removed: none.
- Relationships corrected: none.
- Relationship-change justification: `SMELL-001`, `ARTIFACT-007`, and `RITUAL-001` are explicitly named and materially
  used in the Chapter 3 discussion; `references` is the strongest accurate supported relationship type.
- Draft-log reuse discrepancy: Draft log listed `METRIC-003`, but the manuscript uses discoverability only as ordinary
  prose; no `CHAPTER-003` relationship to `METRIC-003` was added.
- Manuscript corrections made: clarified story-local scope of the Chapter ADR decision.
- Unresolved canon issues: none.
- Remaining `AUTHOR NOTE` items: none.
- Files changed: `book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md`, `knowledge/index.yaml`,
  and `editor/EDITOR_LOG.md`.
- Validation commands and results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed.
  - `npm.cmd run lint:spelling`: passed.
  - `npm.cmd run lint:links`: passed.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed.
  - `knowledge/index.yaml` parsed successfully and direct Chapter 3 relationship integrity checks passed.
- `editor/CANON.md` changed: no.
- PEAK concept files changed: no.
- PEAK entity statuses changed: no.
- Frozen chapters changed: no.
- Chapter 4 started: no.
- Technical Review performed: no.
- Freeze Review performed: no.
- Next lifecycle stage: Technical Review.

## Phase 3 Chapter 3 Technical Review

- Chapter: Asking Better Engineering Questions.
- Stable ID: CHAPTER-003.
- Branch: `chapter3`.
- Reviewed baseline commit: `a89cd3cddadc2c8fd83a3c18287ff2752fff551f`.
- Lifecycle stage: Technical Review.
- Review scope: distributed-system story model, embedded-device state semantics, observation versus inference,
  acknowledgment semantics, command/state separation, authoritative state, timing and ordering, retries and duplication,
  freshness and validity, evidence and instrumentation, exercise usefulness, chapter ADR, alternatives, and timelessness.
- Review outcome: Approved with minor changes.
- System-model result: credible application, gateway, field-device, command path, and state-reporting path model.
- Story-causality result: the Principal Engineer reshapes evidence collection rather than diagnosing the answer in
  advance.
- Observation-versus-inference result: observations, interpretations, assumptions, and competing explanations remain
  separated.
- Acknowledgment-semantics result: transport receipt, command acceptance, operation result, and state publication remain
  distinct.
- Command/state separation result: command handling is not treated as proof of resulting state.
- Authoritative-state result: story-local ownership remains scoped to this system.
- Physical-reality wording result: physical-state completion language was narrowed to device-observed operational state.
- Timing and clock-model result: local timestamps are not treated as a shared global timeline.
- Ordering and correlation result: the investigation now names the need for a usable correlation or ordering model.
- Retry and duplication result: retries are treated as potentially useful but capable of hiding duplicate attempts or
  repeated reports.
- Freshness and validity result: last-observed, latest received, current, stale, unknown, and pending states remain
  distinguishable.
- Stale/unknown/pending-state result: application presentation does not create state authority.
- Evidence and instrumentation result: logs remain observations; instrumentation is framed as discriminating evidence,
  not automatic proof.
- Engineering Principle result: preserved exactly and technically supported.
- Architecture Exercise result: still produces actionable evidence-gathering output and stops before option selection.
- Chapter ADR result: technically credible after narrowing claims about what can be distinguished and adding
  consumer-handling cost.
- Alternatives result: alternatives remain credible and bounded to the story model.
- Timelessness result: no vendor, protocol, RTOS, cloud, broker, or radio technology was introduced.
- Technical corrections made: narrowed physical-state wording to device-observed operational state, added correlation
  and ordering caveat, acknowledged duplicate attempts and repeated reports under retries, narrowed the ADR consequence
  about distinguishing failure modes, and added consumer-handling cost for unknown or stale states.
- Unresolved technical issues: none.
- Remaining `AUTHOR NOTE` items: none.
- Files changed: `book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md` and
  `editor/EDITOR_LOG.md`.
- Validation commands and results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed.
  - `npm.cmd run lint:spelling`: passed.
  - `npm.cmd run lint:links`: passed.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed.
- Canon changed: no.
- `knowledge/index.yaml` changed: no.
- PEAK relationships changed: no.
- PEAK concept files changed: no.
- Frozen chapters changed: no.
- Chapter 4 started: no.
- Freeze Review performed: no.
- Next lifecycle stage: Freeze Review.

## Phase 3 Chapter 3 Freeze Review

- Chapter: Asking Better Engineering Questions.
- Stable ID: CHAPTER-003.
- Branch: `chapter3`.
- Reviewed baseline commit: `ace15331c69a2535410cbf86621f395ab1994c9b`.
- Current `origin/main` commit: `3bdf3e9d38b98784235415e4ce339b815b12f6dc`.
- Current merge base with `origin/main`: `3bdf3e9d38b98784235415e4ce339b815b12f6dc`.
- Technical Review baseline commit: `a89cd3cddadc2c8fd83a3c18287ff2752fff551f`.
- Lifecycle stage: Freeze Review.
- Review outcome: Approved.
- Lifecycle-history result: Draft, Editorial Review, Canon Review, Technical Review, and required pre-Freeze alignment
  records are present; no prior Chapter 3 Freeze Review record existed.
- Branch-scope result: branch changes are limited to Chapter 3 manuscript work, Chapter 3 PEAK/index updates,
  Canon classification alignment, and editor log records; Chapter 1 and Chapter 2 remain untouched in this review.
- Complete branch changed-file set before Freeze transition: `book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md`,
  `editor/CANON.md`, `editor/EDITOR_LOG.md`, and `knowledge/index.yaml`.
- Central-idea result: the chapter remains focused on making assumptions testable before they become architecture.
- Chapter-boundary result: Chapter 3 advances question quality and shaped inquiry; it does not become Chapter 1,
  Chapter 2, an incident-response guide, an Architecture Review process, or Chapter 4.
- Chapter-architecture result: required sections are present in canonical order.
- Editorial-stability result: story, discussion, principle, exercise, notebook, ADR, and commentary are stable after
  Editorial Review and Technical Review.
- Canon-stability result: PEAK terminology and references match the existing canon; no new concept was required.
- Technical-stability result: distributed state, acknowledgments, freshness, ordering, retries, and ownership language
  remain bounded and technically credible after Technical Review.
- Story result: the stale-state investigation is realistic and introduces the problem before the solution.
- Engineering Principle result: `Better questions make assumptions testable before they become architecture.`
- Architecture Exercise result: practical, evidence-oriented, and bounded before option selection.
- Principal's Notebook result: exactly three concise observations.
- Chapter ADR result: local to the story system and not registered as a handbook-wide ADR.
- Editor's Commentary result: explains the chapter's position after Chapters 1 and 2 and points to Chapter 4 without
  starting Chapter 4.
- PEAK entity result: `CHAPTER-003` exists exactly once, path resolves, and status moved from `draft` to `canonical`.
- PEAK relationships retained:
  - `CHAPTER-003 illustrates LAW-005`.
  - `CHAPTER-003 references VOCAB-002`.
  - `CHAPTER-003 references LAW-001`.
  - `CHAPTER-003 references LAW-002`.
  - `CHAPTER-003 references LAW-003`.
  - `CHAPTER-003 references SMELL-004`.
  - `CHAPTER-003 references SMELL-001`.
  - `CHAPTER-003 references ARTIFACT-007`.
  - `CHAPTER-003 references RITUAL-001`.
- PEAK relationships changed during Freeze Review: none.
- PEAK concept files changed during Freeze Review: none.
- `editor/CANON.md` changed during Freeze Review: no.
- Manuscript changes made during Freeze Review: none.
- Frozen chapters changed during Freeze Review: none.
- Chapter 4 started: no.
- Branch merged: no.
- Unresolved editorial issues: none.
- Unresolved canon issues: none.
- Unresolved technical issues: none.
- Remaining `AUTHOR NOTE` items: none.
- Remaining validation blockers: none.
- Validation commands and results:
  - `git fetch --all --prune`: passed.
  - `git switch chapter3`: passed; branch already current.
  - `git pull --ff-only`: passed; branch already up to date.
  - `git status --short`: passed; working tree clean before review edits.
  - `git rev-parse HEAD`: `ace15331c69a2535410cbf86621f395ab1994c9b`.
  - `git rev-parse origin/main`: `3bdf3e9d38b98784235415e4ce339b815b12f6dc`.
  - `git merge-base origin/main HEAD`: `3bdf3e9d38b98784235415e4ce339b815b12f6dc`.
  - `git diff --name-status origin/main...HEAD`: four expected branch files only.
  - `python -m pip install -r requirements.txt`: passed after local network access was allowed.
  - `python -m pip check`: passed with no broken requirements.
  - `npm.cmd install`: passed; dependencies already up to date.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues.
  - `npm.cmd run lint:links`: passed; 123 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions before Freeze transition.
  - `vale .`: exited 0 with 0 errors, 5 existing AuthorBoundary warnings outside Chapter 3, and 0 suggestions.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --strict`: passed as the workflow-style PDF job command.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and generated
    `site/pdf/the-principal-engineer-handbook.pdf`.
  - Direct pre-transition Freeze checks: passed for chapter architecture, markers, notebook count, Chapter 4 boundary,
    YAML parse, `CHAPTER-003` draft status, `CHAPTER-001` and `CHAPTER-002` canonical status, unique `CHAPTER-003`,
    path resolution, exact relationships, no `METRIC-003` edge, and no duplicate `CHAPTER-003` edge.
  - `git diff --check`: passed before Freeze transition.
  - `git status --short`: passed before Freeze transition; no tracked validation output changed.
  - `git diff --name-only`: passed before Freeze transition; no tracked validation output changed.
- Post-transition validation commands and results:
  - `git diff --check`: passed with local LF/CRLF notices for the two changed files.
  - `git diff --name-only`: returned only `editor/EDITOR_LOG.md` and `knowledge/index.yaml`.
  - `git status --short`: returned only `editor/EDITOR_LOG.md` and `knowledge/index.yaml`.
  - `git diff --exit-code -- book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md`: passed.
  - `git diff --exit-code -- book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md book/01-thinking-like-a-principal/02-decision-making-under-constraints.md`:
    passed.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues after replacing one log word that was not in the dictionary.
  - `npm.cmd run lint:links`: passed; 123 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `vale .`: exited 0 with 0 errors, 5 existing AuthorBoundary warnings outside Chapter 3, and 0 suggestions.
  - `python -m pip check`: passed with no broken requirements.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and generated
    `site/pdf/the-principal-engineer-handbook.pdf`.
  - Direct final Freeze checks: passed for `CHAPTER-003` canonical status, `CHAPTER-001` and `CHAPTER-002` canonical
    status, chapter architecture, markers, path resolution, exact relationships, no `METRIC-003` edge, no duplicate
    edge, and Chapter 4 boundary.
- Final lifecycle state: `CHAPTER-003` moved from `draft` to `canonical`.
- Chapter 3 is Frozen.
- Future substantive changes require reopening the chapter at the appropriate review stage.
- Next repository step: begin Chapter 4 only through a separate Draft prompt.

## Phase 3 Chapter 4 Canonical Brief Setup

- Chapter: Ownership Beyond Code.
- Stable ID: CHAPTER-004.
- Branch: `chapter4`.
- Baseline commit: `a29d238d9177a9d3cb583c352ca0a505623cc6c4`.
- Lifecycle stage: Draft preparation.
- Chapter 4 preparation started.
- Canonical brief and exact scope established at `editor/chapter-briefs/CHAPTER-004-ownership-beyond-code.md`.
- `CHAPTER-004` registered as `draft` in `knowledge/index.yaml`.
- Reader-facing Draft written: no.
- Chapter 4 manuscript file created: no.
- New PEAK concept registered: no.
- PEAK relationships added: none.
- Editorial, Canon, Technical, and Freeze Review performed: no.
- Chapter 1, Chapter 2, and Chapter 3 remain canonical and untouched.

## Phase 3 Chapter 4 Author Draft

- Chapter: Ownership Beyond Code.
- Stable ID: CHAPTER-004.
- Branch: `chapter4`.
- Author Draft phase completed.
- Reader-facing manuscript path: `book/01-thinking-like-a-principal/04-ownership-beyond-code.md`.
- Central thesis: ownership is responsibility for closure across boundaries, not possession of every task.
- Main story direction: a manufacturing diagnostic reused by service becomes assigned across teams but not owned as an
  end-to-end workflow.
- Chapter-local exercise included: Map an Ownership Gap.
- Chapter-local ADR included: Assign End-to-End Ownership for the Diagnostic Workflow.
- PEAK relationships added: `CHAPTER-004 references LAW-001`; `CHAPTER-004 references LAW-002`;
  `CHAPTER-004 references SMELL-001`; `CHAPTER-004 illustrates FAILURE-004`;
  `CHAPTER-004 references METRIC-002`; `CHAPTER-004 references METRIC-003`;
  `CHAPTER-004 references ARTIFACT-006`.
- Lifecycle remains: `draft`.
- New PEAK concepts registered: none.
- Editorial, Canon, Technical, and Freeze Review performed: no.
- Next step: separate Editorial Review.

## Phase 4 Chapter 4 Editorial Review

- Chapter: Ownership Beyond Code.
- Stable ID: CHAPTER-004.
- Branch: `chapter4`.
- Reviewed baseline commit: `227f72468997aa3f4096041ed38afb7f1991e40a`.
- Lifecycle stage: Editorial Review.
- Review scope: clarity, structure, narrative flow, pacing, readability, continuity with Chapters 1-3, canonical chapter
  architecture, style-guide compliance, repetition, terminology readability, and PEAK-reference readability.
- Review outcome: Approved with minor changes.
- Central-idea assessment: the chapter remains focused on ownership as responsibility for closure across boundaries,
  not possession of every task.
- Story assessment: the diagnostic workflow story remains intact; local teams remain reasonable, the Principal Engineer
  routing dependency remains visible, and the owned outcome is named before Discussion.
- Structure and flow assessment: required chapter sections remain in canonical order and progress from story to
  discussion, principle, exercise, notebook, ADR, and commentary.
- Repetition and pacing assessment: minor repeated phrasing around team reuse, private memory, and local ownership was
  tightened without changing the story or decision.
- Continuity with Chapters 1-3: Chapter 4 follows Chapter 3 by moving from exposed ownership gaps to bounded closure,
  without reteaching the Chapter 1 role frame, Chapter 2 decision framework, or Chapter 3 question-shaping work.
- Chapter-boundary assessment: the chapter does not become an org-chart, management, release-management, or Chapter 5
  evidence-quality chapter.
- Engineering Principle assessment: the principle remains singular and bounded: ownership means making a bounded
  outcome reach visible closure across boundaries.
- Architecture Exercise assessment: the exercise remains immediately usable and ends with the required question,
  `What is currently assigned, but not truly owned?`
- Principal's Notebook assessment: exactly three concise observations remain.
- Chapter-local ADR assessment: the ADR remains local to the diagnostic workflow and preserves distributed component
  ownership.
- Editor's Commentary assessment: the commentary explains the Chapter 3-to-Chapter 4 transition, chapter boundary, use
  of existing PEAK concepts, and the handoff to Chapter 5.
- PEAK-reference readability assessment: direct references to `LAW-001`, `LAW-002`, `SMELL-001`, `FAILURE-004`,
  `METRIC-002`, `METRIC-003`, and `ARTIFACT-006` remain readable and naturally integrated.
- Editorial changes made:
  - tightened repeated role-benefit phrasing in the Story;
  - reduced repeated descriptions of the Principal Engineer's memory;
  - removed an unnecessary standalone repetition about local owners not composing automatically;
  - tightened outcome-owner language so it does not imply a universal implementer;
  - clarified observable closure wording and avoided vague alignment language;
  - made the Hero Engineer transition less heroic in tone.
- Unresolved editorial issues: none.
- Canon concerns deferred to Canon Review: verify that the existing PEAK relationships are sufficient and that no
  ownership term should be promoted into canon.
- Technical concerns deferred to Technical Review: validate the diagnostic compatibility, capability-detection,
  migration, timeout, and release-gate details.
- Remaining `AUTHOR NOTE` items: none.
- Files changed:
  - `book/01-thinking-like-a-principal/04-ownership-beyond-code.md`;
  - `editor/EDITOR_LOG.md`.
- Validation commands and results:
  - `git fetch --all --prune`: passed during preflight.
  - `git status --short --branch`: passed during preflight; branch was `chapter4` and working tree was clean.
  - `git rev-parse HEAD`: `227f72468997aa3f4096041ed38afb7f1991e40a` before review edits.
  - `git merge-base origin/main HEAD`: `a29d238d9177a9d3cb583c352ca0a505623cc6c4`.
  - Direct Chapter 4 structural and PEAK checks: passed for heading order, one H1, required sections, exactly three
    Principal's Notebook entries, ADR sections, no placeholder markers, `CHAPTER-004` draft status, expected
    relationships, supported relationship types, and no duplicate relationship edges.
  - `git diff --exit-code -- knowledge/index.yaml`: passed; PEAK relationships unchanged.
  - `git diff --exit-code -- book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md book/01-thinking-like-a-principal/02-decision-making-under-constraints.md book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md`:
    passed; frozen Chapters 1-3 unchanged.
  - `git diff --check`: passed with local LF/CRLF notices only.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/04-ownership-beyond-code.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues.
  - `npm.cmd run lint:links`: passed; 125 links scanned successfully.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed with no broken requirements.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --strict`: passed as the workflow-style PDF export build.
- Lifecycle remains: `draft`.
- New PEAK concepts registered: none.
- Canon Review performed: no.
- Technical Review performed: no.
- Freeze Review performed: no.
- Branch merged: no.
- Next lifecycle stage: separate Chapter 4 Canon Review.

## Phase 4 Chapter 4 Canon Review

- Chapter: Ownership Beyond Code.
- Stable ID: CHAPTER-004.
- Branch: `chapter4`.
- Reviewed baseline commit: `c681aac409b64f818adb66553a413060c2ff55c6`.
- Lifecycle stage: Canon Review.
- Review scope: central idea, canonical brief compliance, chapter boundaries, canonical terminology, PEAK definitions,
  stable IDs, relationship graph, chapter-local principle, chapter-local ADR, and new-concept risk.
- Review outcome: Approved.
- Central-idea result: Chapter 4 teaches one approved idea: ownership is responsibility for closure across boundaries,
  not possession of every task.
- Canonical-brief compliance result: the manuscript stays inside the approved brief for bounded responsibility, visible
  closure, accepted handoffs, residual risks, discoverability, and avoidance of permanent Principal Engineer routing.
- Boundary result relative to Chapters 1-3: Chapter 4 operationalizes one responsibility of the Principal Engineer role,
  starts after an ownership gap is visible, and does not reteach Chapter 1 role definition, Chapter 2 constrained
  decision-making, or Chapter 3 question shaping.
- Later-chapter boundary result: the chapter requires observable closure evidence without teaching Chapter 5 evidence
  quality or Chapter 6 broad stewardship.
- Canonical terminology result: exact PEAK names and IDs are used where concepts are formal; ownership phrases remain
  ordinary or chapter-local prose.
- Undefined-term result: no undefined formal term blocks Canon Review.
- Exact PEAK names and IDs reviewed: `LAW-001` Every State Has One Owner; `LAW-002` Every API Is a Promise;
  `SMELL-001` Silent Coupling; `FAILURE-004` The Hero Engineer; `METRIC-002` Bus Factor; `METRIC-003`
  Discoverability; `ARTIFACT-006` Architecture Ledger.
- PEAK concept reuse result: existing concepts are applied without redefining laws, metrics, smells, artifacts, or
  failure stories.
- Concept-duplication result: no duplicate of an existing PEAK concept was found.
- New-concept requirement result: no new PEAK concept is required.
- Ownership-term promotion decision: `outcome owner`, `owner of closure`, `bounded ownership`, `ownership gap`,
  `handoff acceptance`, `closure evidence`, `ownership architecture`, and `Own the closure, not all the work` remain
  ordinary or chapter-local language.
- Chapter-local Engineering Principle result: the principle is consistent with the brief, distinct from `LAW-001` and
  `LAW-002`, and was not promoted into `editor/CANON.md` or `knowledge/index.yaml`.
- Chapter-local ADR result: the ADR remains reader-facing, story-local, and scoped to the diagnostic workflow; it does
  not create a repository-level ADR or universal ownership rule.
- Chapter architecture result: required sections remain present in canonical order with one H1, exactly three
  Principal's Notebook observations, and a complete chapter-local ADR.
- Distinct handbook value result: Chapter 4 adds the move from exposed ownership gap to durable closure while avoiding
  both fragmented responsibility and Hero Engineer centralization.
- Existing Chapter 4 relationships audited:
  - `CHAPTER-004 references LAW-001`.
  - `CHAPTER-004 references LAW-002`.
  - `CHAPTER-004 references SMELL-001`.
  - `CHAPTER-004 illustrates FAILURE-004`.
  - `CHAPTER-004 references METRIC-002`.
  - `CHAPTER-004 references METRIC-003`.
  - `CHAPTER-004 references ARTIFACT-006`.
- Relationships retained: all seven Chapter 4 relationships.
- Relationships added: none.
- Relationships removed: none.
- Relationships corrected: none.
- Justification for relationship changes: not applicable; no relationship changes were needed.
- Manuscript corrections made: none.
- `editor/CANON.md` changed: no.
- PEAK concept files changed: no.
- PEAK entity statuses changed: no.
- `knowledge/index.yaml` changed: no.
- Unresolved canon issues: none.
- Technical concerns deferred to Technical Review: diagnostic compatibility, capability detection, migration sequencing,
  timeout behavior, and release-gate feasibility.
- Remaining `AUTHOR NOTE` items: none in Chapter 4.
- Frozen Chapters 1-3 changed: no.
- Lifecycle remains: `draft`.
- Technical Review performed: no.
- Freeze Review performed: no.
- Branch merged: no.
- Validation commands and results:
  - `git fetch --all --prune`: passed.
  - `git status --short --branch`: passed; branch was `chapter4` and working tree was clean before the log entry.
  - `git rev-parse HEAD`: `c681aac409b64f818adb66553a413060c2ff55c6` before the log entry.
  - `git merge-base origin/main HEAD`: `a29d238d9177a9d3cb583c352ca0a505623cc6c4`.
  - Direct chapter identity and PEAK ID checks: passed for `CHAPTER-004` uniqueness, type, name, manuscript path,
    `draft` status, explicit PEAK IDs, and exact PEAK name/ID pairs in the manuscript.
  - Direct chapter architecture and graph checks: passed for required section order, one H1, exactly three Principal's
    Notebook entries, complete ADR sections, no placeholder markers, exact Chapter 4 edge set, target existence,
    supported relationship types, no duplicate edges, and no self-edge.
  - `git diff --exit-code c681aac409b64f818adb66553a413060c2ff55c6 -- book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md book/01-thinking-like-a-principal/02-decision-making-under-constraints.md book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md knowledge/index.yaml editor/CANON.md`:
    passed before the log entry; frozen Chapters 1-3, PEAK registry, and `editor/CANON.md` were unchanged.
  - `git diff --check`: passed after the log entry with local LF/CRLF notice only.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/04-ownership-beyond-code.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions after the log entry.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues.
  - `npm.cmd run lint:links`: passed; 125 links scanned successfully.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed with no broken requirements.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --strict`: passed as the workflow-style PDF export build.
- Next lifecycle stage: Chapter 4 Technical Review.

## Phase 4 Chapter 4 Technical Review

- Chapter: Ownership Beyond Code.
- Stable ID: CHAPTER-004.
- Branch: `chapter4`.
- Reviewed Canon Review baseline commit: `3a5f0ad37ede5c5a719668e420e1c8a9ac3a36c8`.
- Lifecycle stage: Technical Review.
- Review scope: diagnostic-workflow system model, story causality, `ready` semantics, interface compatibility,
  capability detection, old-firmware limitations, timeout language, command-versus-state boundaries, migration,
  mixed-fleet support, release gates, supported-combination evidence, safety-language scope, technical ownership,
  accepted risk lifecycle, deprecation, exercise usefulness, chapter-local ADR, and timelessness.
- Review outcome: Approved with minor changes.
- System-model result: plausible and internally coherent; manufacturing reuse, field-service reuse, changed firmware
  semantics, unchanged response shape, mixed deployed versions, staggered fixture migration, support procedure drift,
  and Principal Engineer routing dependency can coexist without contradiction.
- Story-causality result: the sequence remains credible; local completion does not establish end-to-end compatibility
  because semantic, tooling, fixture, support, and release concerns move on different schedules.
- `ready` semantic result: treated as an interface semantic and completion condition, not as physical truth or a
  universal safety guarantee.
- Interface-compatibility result: the chapter correctly frames the problem as semantic compatibility, not response-shape
  syntax alone.
- Capability-detection result: credible after preserving the distinction between version information, capability
  signaling, fallback handling, and already-shipped firmware that cannot be retrofitted.
- Old-firmware limitation result: preserved; new capability signaling cannot make old firmware report a new capability.
- Timeout-model result: minor wording was narrowed so timeout language refers to completion bounds and workflow behavior,
  not a universal safe timeout.
- Command-versus-state result: the chapter does not equate command receipt, diagnostic completion, service workflow
  closure, or release support.
- Retry behavior result: no retry or duplicate-command claim is made; no additional retry model was needed.
- Manufacturing-fixture migration result: credible; fixture images and client libraries may migrate on a different
  schedule from product firmware, and migration state affects supported combinations.
- Mixed-fleet result: credible; the chapter allows old firmware, skipped updates, temporary compatibility handling,
  support restrictions, and deprecation state without assuming every device can be updated.
- Release-gate result: release gates are treated as enforcement of an agreed supported-combination policy, not as the
  source of firmware or tool semantics.
- Supported-combination evidence result: evidence examples were narrowed to supported combinations, agreed policy,
  maintained records, and closure evidence rather than proof of all possible field behavior.
- Safety-language result: broad safety wording was narrowed to supported diagnostic workflow behavior and
  supportability.
- Authoritative-state ownership result: separate authoritative owners for capability, migration, deprecation, release
  combination, and risk state remain possible; the outcome owner does not become authoritative for every state.
- Interface-promise result: firmware command semantics, timing/completion behavior, errors, capability applicability,
  and deprecation remain interface promises rather than tool or documentation guesses.
- Silent Coupling result: valid; fixture, service tool, support procedure, and release gate depend on shared diagnostic
  meaning that must be explicit.
- Hero Engineer result: valid; the failure mode is dependency on private compatibility knowledge, not expert involvement
  itself.
- Bus Factor and Discoverability result: valid; used as risk signals and maintenance properties, not proof of closure.
- Architecture Ledger result: valid after narrowing; a maintained ledger or equivalent record improves discoverability
  and does not replace validation or runtime truth.
- Outcome-owner feasibility result: technically credible; one owner ensures composition of component owners, interface
  owners, state owners, risk owners, accepted handoffs, and evidence without becoming universal implementer or approver.
- Handoff-acceptance result: credible; acceptance means understanding the bounded concern, current state, contract,
  uncertainty, consequence, closure condition, and ability to act or escalate.
- Accepted-risk lifecycle result: credible; old firmware capability limits, temporary compatibility tables, delayed
  fixture migration, support restrictions, and temporary compatibility behavior can have owners and review triggers.
- Deprecation result: credible; deprecation remains an active lifecycle state, not a date written in a plan.
- Engineering Principle result: preserved exactly and technically supported.
- Architecture Exercise result: still actionable; prompts distinguish component owners, authoritative-state owners,
  interface-promise owners, risk owners, closure evidence, discoverable records, and human single points of failure.
- Chapter-local ADR result: technically credible and local to the diagnostic workflow; component ownership remains
  distributed, bottleneck risk remains acknowledged, and records/evidence must stay maintained.
- Timelessness result: no vendor, MCU, RTOS, protocol, cloud, CI provider, ticket system, or release-methodology
  dependency was introduced.
- Technical corrections made:
  - narrowed `safe timeout` wording to timeout sufficiency for a completion condition;
  - scoped `valid` result-code wording to the legacy workflow;
  - scoped support-procedure and owned-outcome safety language to supported diagnostic workflow behavior;
  - changed broad valid-image and valid-combination wording to supported or isolated validity language;
  - narrowed closure evidence to supported combinations and release gates based on an agreed policy;
  - clarified that discoverable records such as an Architecture Ledger must be maintained;
  - replaced broad safety-condition language with supportability-condition language;
  - clarified that closure evidence must remain current.
- Unresolved technical issues: none.
- Canon concerns deferred: none.
- Editorial concerns deferred: none.
- Remaining `AUTHOR NOTE` items: none in Chapter 4.
- Files changed:
  - `book/01-thinking-like-a-principal/04-ownership-beyond-code.md`;
  - `editor/EDITOR_LOG.md`.
- `knowledge/index.yaml` changed: no.
- PEAK relationships changed: no.
- `editor/CANON.md` changed: no.
- PEAK concept files changed: no.
- Frozen Chapters 1-3 changed: no.
- Lifecycle remains: `draft`.
- Freeze Review performed: no.
- Branch merged: no.
- Validation commands and results:
  - `git fetch --all --prune`: passed.
  - `git status --short --branch`: passed during preflight; branch was `chapter4` and working tree was clean.
  - `git rev-parse HEAD`: `3a5f0ad37ede5c5a719668e420e1c8a9ac3a36c8` before review edits.
  - `git merge-base origin/main HEAD`: `a29d238d9177a9d3cb583c352ca0a505623cc6c4`.
  - Direct chapter structure and marker checks: passed for one H1, required H2 order, exactly three Principal's
    Notebook entries, complete ADR sections, and no `TODO`, `TBD`, `AUTHOR NOTE`, placeholders, or conflict markers.
  - Direct YAML graph checks: passed for `CHAPTER-004` draft status, exact seven Chapter 4 relationships, target
    existence, supported relationship types, and no duplicate relationships.
  - Targeted technical search: passed; no newly introduced vendor, protocol, packet-format, guarantee, formal-safety,
    or technology-specific wording was found. The `CAN` search produced only ordinary-word false positives such as
    `cannot`.
  - `git diff --exit-code -- book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md book/01-thinking-like-a-principal/02-decision-making-under-constraints.md book/01-thinking-like-a-principal/03-asking-better-engineering-questions.md knowledge/index.yaml editor/CANON.md`:
    passed; frozen Chapters 1-3, PEAK registry, and `editor/CANON.md` were unchanged.
  - `git diff --check`: passed with local LF/CRLF notice only.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/04-ownership-beyond-code.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues.
  - `npm.cmd run lint:links`: passed; 125 links scanned successfully.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed with no broken requirements.
  - `$env:ENABLE_PDF_EXPORT='1'; mkdocs build --strict`: passed as the PowerShell equivalent of the workflow-style PDF
    export build.
- Next lifecycle stage: Chapter 4 Freeze Review.

## Phase 4 Chapter 4 Freeze Review

- Chapter: Ownership Beyond Code.
- Stable ID: CHAPTER-004.
- Branch: `chapter4`.
- Reviewed Technical Review baseline commit: `6fb3a8e9add08df0e9eed8af4b90eb018a8aea37`.
- Lifecycle stage: Freeze Review.
- Review outcome: Approved.
- Prior review-history result: Draft preparation, Author Draft, Editorial Review, Canon Review, and Technical Review
  records are present, distinct, ordered, and permit progression. No prior Chapter 4 Freeze Review was recorded.
- Branch-scope result: branch diff against `origin/main` contains only Chapter 4 work:
  `book/01-thinking-like-a-principal/04-ownership-beyond-code.md`, `editor/EDITOR_LOG.md`,
  `editor/chapter-briefs/CHAPTER-004-ownership-beyond-code.md`, and `knowledge/index.yaml`.
- Complete branch changed-file set:
  - `book/01-thinking-like-a-principal/04-ownership-beyond-code.md`;
  - `editor/EDITOR_LOG.md`;
  - `editor/chapter-briefs/CHAPTER-004-ownership-beyond-code.md`;
  - `knowledge/index.yaml`.
- Central-idea result: passed; Chapter 4 teaches that ownership is responsibility for closure across boundaries, not
  possession of every task.
- Chapter-boundary result: passed; the chapter applies the Principal Engineer role without reteaching Chapters 1-3,
  requires closure evidence without teaching Chapter 5 evidence quality, and does not become a management,
  responsibility-matrix, release management, incident ownership, or organization-design chapter.
- Chapter-architecture result: passed; one H1, required H2 sections in canonical order, no empty required section,
  exactly three Principal's Notebook observations, complete chapter-local ADR, and no optional structure competing with
  the chapter architecture.
- Editorial-stability result: passed; story progression, terminology, paragraph density, PEAK integration, and tone are
  stable after Editorial Review and Technical Review.
- Canon-stability result: passed; Canon Review conclusions still hold, ownership phrases remain ordinary or
  chapter-local prose, no new PEAK concept is required, `editor/CANON.md` remains unchanged, and PEAK concept files
  remain unchanged.
- Technical-stability result: passed; Technical Review conclusions remain present, including semantic compatibility,
  capability detection, mixed-fleet support, bounded timeout language, supported-combination evidence, maintained records,
  and bounded safety/supportability wording.
- Story result: passed; the diagnostic workflow story remains realistic, shows local teams acting reasonably, exposes an
  end-to-end ownership gap, avoids fabricated catastrophe, resolves through bounded ownership, and preserves distributed
  implementation.
- Engineering Principle result: passed; the principle remains chapter-local and distinct from `LAW-001` and `LAW-002`.
- Architecture Exercise result: passed; Map an Ownership Gap remains immediately usable and ends with
  `What is currently assigned, but not truly owned?`
- Principal's Notebook result: passed; exactly three concise observations remain with distinct meanings.
- Chapter-local ADR result: passed; the ADR is local to the diagnostic workflow, contains Context, Decision,
  Consequences, and Alternatives Considered, preserves component implementation ownership, requires maintained current
  evidence, and does not create a repository-level ADR.
- Editor's Commentary result: passed; it explains why Chapter 4 follows Chapter 3, preserves the management and
  Chapter 5 boundaries, reuses existing PEAK concepts, and does not contain repository workflow details.
- PEAK entity result: `CHAPTER-004` exists exactly once, type `chapter`, name `Ownership Beyond Code`, path
  `../book/01-thinking-like-a-principal/04-ownership-beyond-code.md`, and pre-transition status `draft`.
- Relationships retained:
  - `CHAPTER-004 references LAW-001`;
  - `CHAPTER-004 references LAW-002`;
  - `CHAPTER-004 references SMELL-001`;
  - `CHAPTER-004 illustrates FAILURE-004`;
  - `CHAPTER-004 references METRIC-002`;
  - `CHAPTER-004 references METRIC-003`;
  - `CHAPTER-004 references ARTIFACT-006`.
- Relationship changes during Freeze Review: none.
- PEAK concept changes: none.
- `editor/CANON.md` changed: no.
- Manuscript changes during Freeze Review: none.
- Frozen Chapters 1-3 changed: no.
- Chapter 5 started: no.
- Branch merged: no.
- Unresolved editorial issues: none.
- Unresolved canon issues: none.
- Unresolved technical issues: none.
- Remaining `AUTHOR NOTE` items: none in Chapter 4.
- Remaining validation blockers: none.
- Validation commands and results:
  - `git fetch --all --prune`: passed.
  - `git status --short --branch`: passed; branch was `chapter4` and working tree was clean before transition.
  - `git rev-parse HEAD`: `6fb3a8e9add08df0e9eed8af4b90eb018a8aea37` before transition.
  - `git rev-parse origin/chapter4`: `6fb3a8e9add08df0e9eed8af4b90eb018a8aea37`.
  - `git rev-parse origin/main`: `a29d238d9177a9d3cb583c352ca0a505623cc6c4`.
  - `git merge-base origin/main HEAD`: `a29d238d9177a9d3cb583c352ca0a505623cc6c4`.
  - `git log --decorate --graph origin/main..HEAD`: passed; branch contains the five expected Chapter 4
    commits through Technical Review.
  - `git diff --name-status origin/main...HEAD`: passed; only expected Chapter 4 files were present.
  - `git diff --check`: passed.
  - Direct pre-transition Freeze checks: passed for lifecycle records, no prior Freeze Review, exact chapter structure,
    markers, complete ADR, `CHAPTER-004` draft status, Chapters 1-3 canonical status, exact seven Chapter 4
    relationships, target existence, supported relationship types, no duplicate edges, no self-edge, no new PEAK
    concept, no Chapter 5 manuscript, no duplicate Chapter 4 under `docs/`, and generated PDF output not tracked.
  - YAML parse for `knowledge/index.yaml`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues.
  - `npm.cmd run lint:links`: passed; 125 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/04-ownership-beyond-code.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions before transition.
  - `vale .`: exited 0 with 0 errors, 5 existing AuthorBoundary warnings outside Chapter 4, and 0 suggestions.
  - `python -m pip check`: passed with no broken requirements.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and generated
    `site/pdf/the-principal-engineer-handbook.pdf`.
  - `$env:ENABLE_PDF_EXPORT='1'; mkdocs build --strict`: passed as the PowerShell equivalent of the CI PDF command.
  - Post-transition validation rerun: `git diff --check`, `npm.cmd run lint:md`, `npm.cmd run lint:spelling`,
    `npm.cmd run lint:links`, targeted Vale, YAML parse, `python -m pip check`, strict MkDocs build, documented PDF
    build, CI-equivalent PDF build, protected-file diff, final direct Freeze checks, and generated-output tracking checks
    passed.
- Pre-transition status: `CHAPTER-004` was `draft`.
- Final lifecycle state: `CHAPTER-004` moved from `draft` to `canonical`.
- Chapter 4 is Frozen.
- Future-change rule: future substantive changes require reopening Chapter 4 at the appropriate review stage.
- Next repository step: prepare and merge a pull request for `chapter4`; do not start Chapter 5 on this branch.

## Phase 5 Chapter 5 Author Draft

- Chapter: Technical Judgment and Evidence.
- Stable ID: CHAPTER-005.
- Branch: `chapter5`.
- Baseline `origin/main` commit: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
- Expected Chapter 4 merge SHA ancestor result: yes; the expected full SHA is the baseline.
- Author Draft phase completed.
- Canonical brief path: `editor/chapter-briefs/CHAPTER-005-technical-judgment-and-evidence.md`.
- Manuscript path: `book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md`.
- Central thesis: technical judgment is the disciplined calibration of confidence to evidence quality, remaining
  uncertainty, and the consequences of being wrong.
- Main story direction: an industrial controller's buffered NOR-flash logging path passes a narrow endurance test, but
  the team must separate the tested laboratory claim from the broader production durability claim under power
  disturbance and recovery conditions.
- Engineering Principle: Evidence Before Confidence (`LAW-005`); the confidence behind a commitment should be no
  stronger than the evidence that supports its specific claim.
- Architecture Exercise: Build an Evidence-Bounded Judgment.
- Chapter-local ADR: Stage the Flash-Logging Rollout Until Power-Loss Evidence Matches the Product Claim.
- PEAK relationships added:
  - `CHAPTER-005 illustrates LAW-005`.
  - `CHAPTER-005 references ARTIFACT-003`.
  - `CHAPTER-005 references VOCAB-002`.
  - `CHAPTER-005 references ARTIFACT-007`.
  - `CHAPTER-005 references VOCAB-001`.
  - `CHAPTER-005 references METRIC-001`.
  - `CHAPTER-005 illustrates FAILURE-003`.
- New PEAK concepts: none.
- Existing PEAK concept files changed: no.
- `editor/CANON.md` changed: no.
- Frozen Chapters 1-4 changed: no.
- Lifecycle remains: `draft`.
- Editorial Review performed: no.
- Canon Review performed: no.
- Technical Review performed: no.
- Freeze Review performed: no.
- Unresolved `AUTHOR NOTE` items: none.
- Validation commands and results:
  - `git fetch --all --prune`: passed.
  - `git status --short --branch`: passed during preflight; branch was `chapter5` and working tree was clean.
  - `git rev-parse origin/main`: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
  - `git log -1 origin/main` with one-line output: `54d6b4e Chapter 4: Ownership Beyond Code (#4)`.
  - `git merge-base chapter5 origin/main`: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
  - `git branch -r --list origin/chapter5`: passed; no remote Chapter 5 branch existed during preflight.
  - Direct structural checks: passed for one H1, required H2 sections in canonical order, exactly three Principal's
    Notebook observations, complete chapter-local ADR sections, no unresolved markers, no duplicate Chapter 5 manuscript
    under `docs/`, `CHAPTER-005` uniqueness, Chapters 1-4 canonical status, relationship target existence, supported
    relationship types, no duplicate edges, no self-edges, and no new PEAK entity beyond `CHAPTER-005`.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues after replacing one spelling-unrecognized term with ordinary
    wording.
  - `npm.cmd run lint:links`: passed; 127 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md editor/chapter-briefs/CHAPTER-005-technical-judgment-and-evidence.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed with no broken requirements.
  - `$env:ENABLE_PDF_EXPORT = '1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and generated
    `site/pdf/the-principal-engineer-handbook.pdf`.
- Expected branch file set:
  - `book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md`;
  - `editor/chapter-briefs/CHAPTER-005-technical-judgment-and-evidence.md`;
  - `editor/EDITOR_LOG.md`;
  - `knowledge/index.yaml`.
- Next required lifecycle stage: separate Chapter 5 Editorial Review.

## Phase 6 Chapter 5 Editorial Review

- Chapter: Technical Judgment and Evidence.
- Stable ID: CHAPTER-005.
- Branch: `chapter5`.
- Reviewed baseline full SHA: `153fa046afe5ceecb304ad89de84a1d98b98b91e`.
- Lifecycle stage: Editorial Review.
- Review scope: clarity, structure, narrative flow, pacing, readability, paragraph rhythm, continuity with Chapters 1-4,
  Chapter 6 and later-part boundaries, canonical chapter architecture, style-guide compliance, repetition, terminology
  readability, PEAK-reference integration, Architecture Exercise usability, chapter-local ADR, and Editor's Commentary.
- Review outcome: Approved with minor changes.
- Central-idea assessment: preserved; the chapter remains focused on evidence-calibrated technical judgment under
  incomplete information.
- Story assessment: credible and bounded; the NOR-flash logging story still moves from a successful endurance test to a
  broader unsupported field-power durability claim, weak signals, targeted evidence gathering, minimum useful
  operational feedback, and a staged commitment.
- Structure and flow assessment: passed; the chapter keeps the canonical section order and the Discussion follows the
  approved arc from claim, to reasoning layers, to evidence conditions, evidence quality, confidence, consequence,
  next evidence action, weak signals, operational feedback, and visible residual uncertainty.
- Repetition and pacing assessment: improved; several repeated transition sentences were consolidated, and the opening
  story was tightened without changing the technical scenario.
- Continuity with Chapters 1-4: preserved; the chapter builds on the Principal Engineer role, constrained commitments,
  answerable questions, and ownership of closure without reteaching those chapters.
- Chapter 6 and later-parts boundary assessment: preserved; the chapter points toward stewardship, observability,
  validation, and release topics only as evidence sources or consumers, not as their definitive treatment.
- Engineering Principle assessment: preserved; `LAW-005` remains the primary anchor, with one chapter-local operational
  expression and no new canonical principle.
- Architecture Exercise assessment: improved; the exercise was consolidated from a long prompt list into grouped prompts
  while preserving the approved semantic targets and final question.
- Principal's Notebook assessment: passed; exactly three concise observations remain with distinct meanings.
- Chapter-local ADR assessment: passed; the ADR remains story-local, balanced about benefits and costs, and clear that
  staged rollout is bounded learning rather than a validation substitute.
- Editor's Commentary assessment: improved; it now states that the chapter reuses existing PEAK concepts instead of
  creating a new evidence framework.
- PEAK-reference readability assessment: improved; PEAK references remain naturally integrated and explainable from the
  manuscript without changing the relationship set.
- Editorial changes made:
  - tightened the story's opening technical setup;
  - replaced a jokey logging sentence with clearer product-language phrasing;
  - consolidated short repeated transition paragraphs in the Discussion;
  - grouped the Architecture Exercise prompts for usability;
  - added a concise PEAK reuse sentence to the Editor's Commentary.
- Unresolved editorial issues: none.
- Canon concerns deferred to Canon Review: verify whether all seven Chapter 5 PEAK relationships remain materially
  justified after editorial consolidation.
- Technical concerns deferred to Technical Review: flash interruption boundaries, production-equivalent timing,
  representative flash lots, staged rollout language, and operational feedback sufficiency should receive technical
  scrutiny.
- New PEAK concepts created: none.
- `knowledge/index.yaml` changed during Editorial Review: no.
- `editor/CANON.md` changed: no.
- Frozen Chapters 1-4 changed: no.
- Chapter 6 started: no.
- Lifecycle remains: `draft`.
- Canon Review performed: no.
- Technical Review performed: no.
- Freeze Review performed: no.
- Validation commands and results:
  - `git fetch --all --prune`: passed.
  - `git status --short --branch`: passed during preflight; branch was `chapter5` and working tree was clean.
  - `git rev-parse HEAD`: `153fa046afe5ceecb304ad89de84a1d98b98b91e`.
  - `git rev-parse origin/chapter5`: `153fa046afe5ceecb304ad89de84a1d98b98b91e`.
  - `git rev-parse origin/main`: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
  - `git merge-base origin/main HEAD`: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
  - Condensed decorated git log for `origin/main..HEAD`: passed; branch contained the two expected Chapter 5
    commits before Editorial Review.
  - `git diff --name-status origin/main...HEAD`: passed during preflight; branch diff contained only the expected
    Chapter 5 file set.
  - `git diff --check`: passed.
  - Direct structural checks: passed for one H1, required H2 sections in canonical order, no empty required section,
    exactly three Principal's Notebook observations, complete chapter-local ADR sections, no unresolved markers, no
    duplicate Chapter 5 manuscript under `docs/`, no Chapter 6 manuscript, and no accidental new canonical-looking
    artifact name or stable ID.
  - Direct PEAK checks: passed for valid YAML parsing, exactly one `CHAPTER-005` entity, `CHAPTER-005` status `draft`,
    Chapters 1-4 status `canonical`, unchanged Chapter 5 relationship set, valid relationship targets, supported
    relationship types, no duplicate relationship edges, and no self-edges.
  - Protected-file checks: passed for unchanged canonical brief, unchanged `knowledge/index.yaml`, unchanged
    `editor/CANON.md`, unchanged existing PEAK concept files, unchanged Frozen Chapter 1-4 manuscripts, and no tracked
    generated site or PDF output.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues.
  - `npm.cmd run lint:links`: passed; 127 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m pip check`: passed with no broken requirements.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `$env:ENABLE_PDF_EXPORT = '1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and generated
    `site/pdf/the-principal-engineer-handbook.pdf`.
- Next required lifecycle stage: separate Chapter 5 Canon Review.

## Phase 7 Chapter 5 Canon Review

- Chapter: Technical Judgment and Evidence.
- Stable ID: CHAPTER-005.
- Branch: `chapter5`.
- Reviewed Editorial Review baseline full SHA: `49aa253a6e958c1bf5405413735e5e88af599c83`.
- Lifecycle stage: Canon Review.
- Review scope: canonical brief compliance, one central idea, adjacent-chapter boundaries, PEAK terminology, stable IDs,
  relationship integrity, chapter-local terminology, new-concept risk, chapter-local ADR status, and preservation of
  Frozen Chapters 1-4 and the wider canon.
- Outcome: Approved.
- Central-idea result: passed; every major section supports evidence-calibrated technical judgment under incomplete
  information.
- Canonical-brief compliance result: passed; the chapter preserves claim-evidence alignment, distinguishes observation,
  measurement, inference, assumption, confidence, and commitment, keeps residual uncertainty visible, scales evidence
  threshold to consequence and reversibility, treats weak signals as incomplete observations, and avoids becoming a
  test-strategy, observability, release, or stewardship chapter.
- Boundaries with Chapters 1-4: passed; Chapter 5 demonstrates one Principal Engineer capability without redefining the
  role, uses consequence and reversibility without recreating Chapter 2's decision framework, uses observation and
  inference without reteaching Chapter 3's question-formation work, and asks what evidence makes a claim believable
  without redefining Chapter 4 ownership or closure.
- Chapter 6 and later-part boundary result: passed; stewardship, observability design, release discipline, test strategy,
  Architecture Review mechanics, ADR/RFC mechanics, incident response, and recovery practice remain later-chapter
  topics.
- Terminology result: passed; claim, evidence, confidence, uncertainty, commitment, validation, operational feedback,
  evidence envelope, evidence threshold, evidence-bounded judgment, decision-critical uncertainty, and staged commitment
  are used as ordinary or chapter-local prose.
- Canonical name and stable-ID result: passed; all explicit PEAK references use existing IDs and canonical names.
- Chapter-local terminology result: passed; the reasoning chain, Engineering Principle expression, exercise title,
  Principal's Notebook observations, and chapter-local ADR do not imply new PEAK entities.
- `LAW-005` result: passed; Evidence Before Confidence is applied without redefining the canonical law, requiring
  certainty, or treating senior confidence as a substitute for evidence.
- Exact seven-relationship audit:
  - `CHAPTER-005 illustrates LAW-005`: retained; Chapter 5 directly operationalizes Evidence Before Confidence.
  - `CHAPTER-005 references ARTIFACT-003`: retained; the Decision Journal is materially used as a lightweight record of
    commitment, claim, evidence, confidence, uncertainty, and review trigger.
  - `CHAPTER-005 references VOCAB-002`: retained; Weak Signal is materially used for low-confidence field observations
    that justify investigation without proving cause.
  - `CHAPTER-005 references ARTIFACT-007`: retained; Weak Signal Register is materially used to preserve weak
    observations, possible causes, confidence, next evidence, and review timing.
  - `CHAPTER-005 references VOCAB-001`: retained; Change Radius is materially used as shared vocabulary for affected
    surface and consequence.
  - `CHAPTER-005 references METRIC-001`: retained; Change Radius as a metric is materially and distinctly used as an
    approximate assessment, explicitly without false precision.
  - `CHAPTER-005 illustrates FAILURE-003`: retained; the story materially illustrates The Successful Prototype by
    showing narrow prototype/lab evidence generalized into a production claim.
- Relationships retained: all seven Chapter 5 relationships.
- Relationships added: none.
- Relationships removed: none.
- Relationships corrected: none.
- Justification for relationship changes: not applicable; no relationship changes were needed.
- New-concept decision: no new PEAK concept is required. Evidence envelope, evidence-bounded judgment, confidence
  calibration, decision-critical uncertainty, minimum useful operational evidence, operational feedback, and staged
  commitment remain chapter-local prose.
- Engineering Principle result: passed; the chapter-local expression remains anchored in `LAW-005`, supported by the
  story and Discussion, and not registered as a standalone law, maxim, principle, metric, or artifact.
- Architecture Exercise result: passed; Build an Evidence-Bounded Judgment remains chapter-local, practical, and not a
  new canonical artifact or generic decision framework.
- Principal's Notebook result: passed; exactly three observations remain and are not registered as maxims.
- Chapter-local ADR result: passed; the ADR is reader-facing, story-local, demonstrates evidence-calibrated commitment,
  keeps residual uncertainty visible, and is not a repository ADR or new PEAK artifact.
- Editor's Commentary result: passed; it positions Chapter 5 after Chapters 1-4, explains the distinct
  claim-evidence-confidence role, reuses existing PEAK concepts, and leaves Chapter 6's stewardship scope intact.
- Manuscript corrections made: none.
- `knowledge/index.yaml` changes: none.
- `editor/CANON.md` changes: none.
- Existing PEAK concept-file changes: none.
- Frozen Chapters 1-4 change result: none.
- Chapter 6 started: no.
- Unresolved canon issues: none.
- Deferred technical concerns: flash interruption boundaries, production-equivalent timing, representative flash lots,
  staged rollout language, and operational feedback sufficiency remain for Technical Review.
- Remaining `AUTHOR NOTE` items: none in Chapter 5.
- Validation commands and results:
  - `git fetch --all --prune`: passed.
  - `git status --short --branch`: passed during preflight; branch was `chapter5` and working tree was clean.
  - `git rev-parse HEAD`: `49aa253a6e958c1bf5405413735e5e88af599c83`.
  - `git rev-parse origin/chapter5`: `49aa253a6e958c1bf5405413735e5e88af599c83`.
  - `git rev-parse origin/main`: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
  - `git merge-base origin/main HEAD`: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
  - Condensed decorated git log for `origin/main..HEAD`: passed; branch contained the three expected Chapter 5 commits
    before Canon Review.
  - `git diff --name-status origin/main...HEAD`: passed during preflight; branch diff contained only the expected
    Chapter 5 file set.
  - `git diff --check`: passed.
  - Direct chapter-structure checks: passed for one H1, required H2 sections in canonical order, no empty required
    section, exactly three Principal's Notebook observations, complete chapter-local ADR sections, no unresolved markers,
    no duplicate Chapter 5 manuscript under `docs/`, and no Chapter 6 manuscript.
  - Direct PEAK checks: passed for valid YAML parsing, exactly one `CHAPTER-005` entity, path resolution,
    `CHAPTER-005` status `draft`, Chapters 1-4 status `canonical`, exact Chapter 5 relationship set, valid targets,
    supported relationship types, no duplicate edges, no self-edges, no accidental new stable ID, no new PEAK entity
    beyond `CHAPTER-005`, and no existing PEAK entity status changes.
  - Protected-file checks: passed for unchanged canonical brief, unchanged `knowledge/index.yaml`, unchanged
    `editor/CANON.md`, unchanged existing PEAK concept files, unchanged Frozen Chapter 1-4 manuscripts, and no tracked
    generated site or PDF output.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues.
  - `npm.cmd run lint:links`: passed; 127 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed with no broken requirements.
  - `$env:ENABLE_PDF_EXPORT = '1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and generated
    `site/pdf/the-principal-engineer-handbook.pdf`.
- Lifecycle remains: `draft`.
- Technical Review performed: no.
- Freeze Review performed: no.
- Branch merged: no.
- Next lifecycle stage: separate Chapter 5 Technical Review.

## Phase 8 Chapter 5 Technical Review

- Chapter: Technical Judgment and Evidence.
- Stable ID: `CHAPTER-005`.
- Branch: `chapter5`.
- Reviewed Canon Review baseline full SHA: `a0123fd21c3a37c2878bad830e244cf5936f15d2`.
- Lifecycle stage: Technical Review.
- Review scope: embedded-system story model, NOR-flash wording, power-disturbance causality, fault-injection boundaries,
  recovery and atomicity model, endurance representativeness, production-equivalent configuration and timing,
  CRC/integrity claims, operational feedback sufficiency, staged rollout credibility, evidence/inference/confidence
  reasoning, Change Radius and reversibility, Decision Journal, Engineering Principle, Architecture Exercise,
  chapter-local ADR, timelessness, and safety/guarantee language.
- Review outcome: Approved with minor changes.
- System-model result: credible and internally coherent; the industrial controller, external NOR flash, buffered RAM
  records, batched programming, story-local recovery metadata, reset-time reconstruction, production/debug configuration
  differences, power disturbances, staged deployment, and support feedback all remain plausible without becoming a
  universal flash-logging design.
- Story-causality result: passed; field notes remain weak signals rather than confirmed flash, supply, or recovery root
  cause.
- NOR-flash semantics result: passed after minor corrections; wording now avoids implying that one marker universally
  guarantees atomicity or that a boot scan proves full recovery.
- Power-disturbance wording result: passed; resets near high-current activity, missing records, and boot behavior remain
  observations with plausible alternative explanations.
- CRC and integrity result: passed; CRC remains evidence for bounded record integrity, not proof of completeness,
  freshness, ordering, atomic commit, or absence of omitted records.
- Interruption-boundary and fault-injection result: passed after minor corrections; the chapter now describes timing
  windows, observable device states, externally meaningful transitions, and recovery-metadata updates rather than exact
  internal flash failure instants.
- Recovery-model result: passed after minor corrections; the text distinguishes generated, programmed, committed,
  reconstructed, and operationally observed records closely enough for the chapter's purpose.
- Production-equivalent timing result: passed after minor corrections; debug/build configuration language now says
  configuration and instrumentation may change timing or behavior enough to matter to the claim.
- Board/flash-lot/environment representativeness result: passed after minor corrections; board, lot, voltage, and
  temperature coverage is tied to relevant production variation rather than treated as automatically sufficient.
- Weak-signal result: passed; weak signals lower confidence and justify investigation without confirming a defect.
- Operational-feedback sufficiency result: passed after minor corrections; the manuscript now requires feedback that is
  independent enough to survive the evaluated failure and includes version/configuration context where support and
  engineering need correlation.
- Staged-rollout result: passed after minor corrections; staged rollout remains bounded learning, not validation, and
  now requires owned review triggers plus a supported stop, disable, rollback, or escalation path.
- Evidence/inference/confidence result: passed; the reasoning chain from observation to interpretation to inference to
  confidence to commitment remains explicit and claim-scoped.
- Change Radius and reversibility result: passed; Change Radius is used approximately, consequence and reversibility
  affect evidence threshold, and reversibility is not treated as safety.
- Decision Journal result: passed after minor correction; the review trigger now includes version/configuration context
  for bounded operational feedback.
- Engineering Principle result: passed; `LAW-005` remains the canonical anchor and the chapter-local expression is
  technically bounded.
- Architecture Exercise result: passed; the exercise remains usable for embedded commitments without becoming a complete
  test-plan template.
- Chapter-local ADR result: passed after minor corrections; the ADR preserves the bounded claim, relevant targeted
  validation, production-equivalent configuration language, operational feedback sufficiency, staged-rollout constraints,
  costs, and residual uncertainty.
- Timelessness result: passed; the chapter uses durable embedded concepts and does not depend on vendor, MCU, RTOS,
  cloud, framework, CI, or release-methodology specifics.
- Technical corrections made:
  - changed broad batched-write and recovery-marker wording to story-local programmed batches and recovery metadata used
    to reconstruct committed log state;
  - replaced exact-boundary and marker-boundary wording with externally meaningful transitions, timing windows,
    observable device states, and recovery-metadata updates;
  - bounded debug/production wording to configuration and instrumentation that may change timing or behavior enough to
    matter to the claim;
  - tied board, flash-lot, voltage, and temperature coverage to relevant production variation rather than automatic
    sufficiency;
  - strengthened operational-feedback language to require a survival path independent enough for the evaluated failure
    and version/configuration context for correlation;
  - strengthened staged-rollout language with owned review triggers and a supported stop, disable, rollback, or
    escalation path;
  - updated the Decision Journal review trigger and ADR to match those technical constraints.
- Unresolved technical issues: none.
- Canon/editorial concerns deferred: none.
- Remaining `AUTHOR NOTE` items: none in Chapter 5.
- Files changed: `book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md`,
  `editor/EDITOR_LOG.md`.
- `knowledge/index.yaml` changed: no.
- PEAK relationships changed: no; the exact seven Chapter 5 relationships remain unchanged.
- `editor/CANON.md` changed: no.
- PEAK concept files changed: no.
- Frozen Chapters 1-4 changed: no.
- Chapter 6 started: no.
- Lifecycle status: `CHAPTER-005` remains `draft`.
- Freeze Review performed: no.
- Branch merged: no.
- Validation commands and results:
  - `git fetch --all --prune`: passed.
  - `git pull --ff-only`: passed; branch was already up to date.
  - `git status --short --branch`: passed during preflight; working tree was clean and branch was `chapter5`.
  - `git rev-parse HEAD`: passed; pre-review HEAD was
    `a0123fd21c3a37c2878bad830e244cf5936f15d2`.
  - `git rev-parse origin/chapter5`: passed; remote matched local pre-review HEAD.
  - `git rev-parse origin/main`: passed; `origin/main` was
    `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
  - `git merge-base origin/main HEAD`: passed; merge base matched `origin/main`.
  - Condensed decorated git log for `origin/main..HEAD`: passed; branch contained Chapter 5 Author Draft, Editorial
    Review, Canon Review, and no prior Technical Review.
  - `git diff --name-status origin/main...HEAD`: passed during preflight; branch diff was limited to the expected
    Chapter 5 manuscript, Chapter 5 canonical brief, `editor/EDITOR_LOG.md`, and `knowledge/index.yaml`.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues across 127 files.
  - `npm.cmd run lint:links`: passed; 127 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md
    editor/EDITOR_LOG.md`: passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed; no broken requirements found.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed; generated local PDF
    output was not tracked.
  - Direct technical review checks: passed for one H1, required H2 sections in canonical order, no empty required
    section, exactly three Principal's Notebook observations, complete chapter-local ADR sections, no Chapter 5
    `TODO`/`TBD`/conflict marker/accidental `AUTHOR NOTE`, no duplicate Chapter 5 manuscript under `docs/`, no Chapter
    6 manuscript, valid YAML, exactly one `CHAPTER-005`, correct Chapter 5 path, `CHAPTER-005` status `draft`, Chapters
    1-4 status `canonical`, exact seven Chapter 5 relationships, valid relationship targets, supported relationship
    types, no duplicate edges, no self-edge, no accidental new stable ID, no new PEAK entity, no PEAK status changes, and
    no tracked generated `site/` or PDF output.
  - Protected-file diff checks: passed; canonical brief, `knowledge/index.yaml`, `editor/CANON.md`, existing PEAK
    concept files, Frozen Chapters 1-4, table of contents, and unrelated configuration were unchanged.
- Next lifecycle stage: Chapter 5 Freeze Review.

## Phase 9 Chapter 5 Freeze Review

- Chapter: Technical Judgment and Evidence.
- Stable ID: `CHAPTER-005`.
- Branch: `chapter5`.
- Reviewed Technical Review baseline full SHA: `a0c8d5e2de7d05c77669fe50240bcbb7196b1e0d`.
- Current `origin/main` full SHA: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
- Merge-base full SHA: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
- Lifecycle stage: Freeze Review.
- Review outcome: Approved.
- Lifecycle-history result: Author Draft, Editorial Review, Canon Review, and Technical Review records are present,
  distinct, ordered, and progression-permitting; no prior Chapter 5 Freeze Review, Freeze Validation Remediation, or
  Freeze Review Retry was recorded.
- Branch-scope result: branch diff against `origin/main` contains only the expected Chapter 5 work.
- Complete branch changed-file set before transition:
  `book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md`, `editor/EDITOR_LOG.md`,
  `editor/chapter-briefs/CHAPTER-005-technical-judgment-and-evidence.md`, and `knowledge/index.yaml`.
- Central-idea result: passed; every major section supports technical judgment as confidence calibrated to evidence
  quality, remaining uncertainty, and the consequence of being wrong.
- Canonical-purpose result: passed; the chapter teaches claim identification, observation/inference/assumption
  separation, evidence quality, confidence scope, residual uncertainty, targeted next evidence, weak signals,
  operational feedback, and sufficiency for the next commitment without false precision or certainty.
- Adjacent-chapter boundary result: passed; Chapter 5 does not redefine the Principal Engineer role, recreate Chapter
  2's constrained-decision framework, reteach Chapter 3's question formation, redefine Chapter 4 ownership and closure,
  or consume Chapter 6's broader stewardship scope.
- Chapter-architecture result: passed; one H1, required H2 sections in canonical order, no empty required section, story
  before resolution, Discussion develops reasoning, one Engineering Principle, immediately usable Architecture Exercise,
  exactly three Principal's Notebook observations, complete chapter-local ADR sections, and reader-facing Editor's
  Commentary.
- Editorial-stability result: passed; the manuscript reads as a finished chapter, has stable terminology, natural PEAK
  references, no reviewer-facing instructions, no accidental repository workflow, no placeholder wording, and no
  formatting defect requiring correction.
- Canon-stability result: passed; `LAW-005` remains the primary anchor, chapter-local language stays ordinary prose, the
  exercise is not a new artifact, the chapter-local ADR is not a repository ADR, no Principal's Notebook entry becomes a
  maxim, no PEAK concept is redefined, and no canon change is required.
- Technical-stability result: passed; Technical Review corrections are present in the current manuscript, including
  bounded recovery metadata, CRC/integrity scope, weak-signal causality, timing-window fault injection,
  production-configuration wording, representativeness limits, operational-feedback survival path, and staged-rollout
  stop/review conditions.
- Story result: passed; the embedded story is credible, preserves valid narrow endurance evidence, shows unsupported
  broad generalization, avoids a careless-team villain, uses weak signals without inventing root cause, and illustrates
  `FAILURE-003`.
- Engineering Principle result: passed; the chapter-local expression remains `The confidence behind a commitment should
  be no stronger than the evidence that supports its specific claim`, derives from `LAW-005`, does not demand certainty,
  and is not promoted into PEAK.
- Architecture Exercise result: passed; `Build an Evidence-Bounded Judgment` is immediately usable, claim-specific,
  separates observation/inference/assumption/uncertainty, exposes evidence conditions and blind spots, defines next
  evidence and review trigger, and does not become a test-plan template or duplicate Chapter 2.
- Principal's Notebook result: passed; exactly three concise, distinct observations remain and none overstates the
  chapter or creates a new maxim.
- Chapter-local ADR result: passed; the ADR is story-local, contains Context/Decision/Consequences/Alternatives
  Considered, states a bounded durability claim, treats validation and staging proportionally, includes costs and
  residual uncertainty, and does not prescribe a universal flash architecture.
- Editor's Commentary result: passed; it positions Chapter 5 after Chapters 1-4, explains the distinct evidence-quality
  role, reuses existing PEAK concepts, preserves Chapter 6 stewardship scope, and does not expose repository workflow.
- Reader-value and timelessness result: passed; the chapter leaves readers able to identify the claim, evidence,
  evidence limits, assumptions, justified confidence, next evidence, responsible commitment, and feedback trigger without
  depending on a specific MCU, flash vendor, RTOS, cloud service, observability product, CI provider, release
  methodology, or proprietary protocol.
- PEAK entity result: pre-transition `CHAPTER-005` existed exactly once with type `chapter`, name `Technical Judgment
  and Evidence`, path `../book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md`, and status `draft`.
- Exact relationships retained:
  - `CHAPTER-005 illustrates LAW-005`.
  - `CHAPTER-005 references ARTIFACT-003`.
  - `CHAPTER-005 references VOCAB-002`.
  - `CHAPTER-005 references ARTIFACT-007`.
  - `CHAPTER-005 references VOCAB-001`.
  - `CHAPTER-005 references METRIC-001`.
  - `CHAPTER-005 illustrates FAILURE-003`.
- Relationship changes during Freeze Review: none.
- New PEAK concepts: none.
- PEAK concept-file changes: none.
- `editor/CANON.md` changes: none.
- Manuscript changes during Freeze Review: none; Chapter 5 manuscript remained byte-for-byte unchanged from the
  Technical Review baseline.
- Canonical-brief changes: none.
- Frozen Chapters 1-4 changes: none.
- Chapter 6 started: no.
- Unresolved editorial issues: none.
- Unresolved canon issues: none.
- Unresolved technical issues: none.
- Remaining `AUTHOR NOTE` items: none in Chapter 5.
- Validation blockers: none. `vale .` reported 0 errors, 5 existing `AuthorBoundary` warnings outside Chapter 5, and 0
  suggestions; repository precedent treats these existing outside-chapter warnings as non-blocking when targeted Vale
  for the reviewed chapter is clean.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - `git pull --ff-only`: passed; branch was already up to date.
  - `git status --short --branch`: passed during preflight; branch was `chapter5` and working tree was clean.
  - `git rev-parse HEAD`: passed; pre-transition HEAD was
    `a0c8d5e2de7d05c77669fe50240bcbb7196b1e0d`.
  - `git rev-parse origin/chapter5`: passed; remote matched local pre-transition HEAD.
  - `git rev-parse origin/main`: passed; `origin/main` was
    `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
  - `git merge-base origin/main HEAD`: passed; merge base matched `origin/main`.
  - Condensed decorated git log for `origin/main..HEAD`: passed; branch contained the expected five Chapter 5 commits
    through Technical Review.
  - `git diff --name-status origin/main...HEAD`: passed during preflight; branch diff was limited to the expected
    Chapter 5 file set.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors.
  - `npm.cmd run lint:spelling`: passed with 0 issues across 127 files.
  - `npm.cmd run lint:links`: passed; 127 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md
    editor/EDITOR_LOG.md`: passed with 0 errors, 0 warnings, and 0 suggestions.
  - `vale .`: completed with 0 errors, 5 existing `AuthorBoundary` warnings outside Chapter 5, and 0 suggestions.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `python -m pip check`: passed; no broken requirements found.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and generated local PDF
    output under `site/pdf/`; generated output was not tracked.
  - Direct pre-transition Freeze checks: passed for one H1, required H2 sections in canonical order, no empty required
    section, exactly three Principal's Notebook observations, complete chapter-local ADR sections, no Chapter 5
    `AUTHOR NOTE`/`TODO`/`TBD`/placeholder/conflict marker, no duplicate Chapter 5 manuscript under `docs/`, no Chapter
    6 manuscript, valid `knowledge/index.yaml`, exactly one `CHAPTER-005`, correct title/type/path, pre-transition
    status `draft`, Chapters 1-4 status `canonical`, exact seven Chapter 5 relationships, valid relationship targets,
    supported relationship types, no duplicate edges, no self-edge, no accidental new stable ID, no new PEAK entity, no
    PEAK concept-file change, no tracked generated `site/` or PDF output, and no branch file outside the expected
    Chapter 5 set.
  - Protected-file comparisons against the Technical Review baseline: passed for Chapters 1-4, Chapter 5 manuscript,
    Chapter 5 canonical brief, `editor/CANON.md`, existing PEAK concept files, table of contents, and repository
    configuration.
  - Post-transition validation rerun: `git diff --check`, markdown lint, spelling lint, link lint, targeted Vale,
    whole-repository Vale with the known outside-Chapter-5 warnings, strict MkDocs build, PDF build, `pip check`, final
    direct Freeze checks, protected-file comparisons, and generated-output tracking checks passed.
- Pre-transition Chapter 5 status: `draft`.
- Final Chapter 5 status: `canonical`.
- Chapter 5 is Frozen: yes.
- Future-change rule: future substantive changes to Chapter 5 require reopening the appropriate review stage.
- Branch merged status: no.
- Next repository step: prepare and merge a pull request for `chapter5`; do not start Chapter 6 on this branch.

## Phase 10 Chapter 6 Canonical Brief Registration

- Chapter: Leaving Systems Better Than You Found Them.
- Stable ID: `CHAPTER-006`.
- Branch: `chapter6`.
- Lifecycle stage: canonical brief registration / draft preparation.
- Verified baseline `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Registration commit present before this remediation: `1a079b02730d70fb4cc08b62edcaa2c593e0cb56`.
- Chapter 5 merge ancestry was verified; merge base between `chapter6` and `origin/main` is
  `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Chapters 1-5 remain Frozen and canonical.
- Canonical brief path:
  `editor/chapter-briefs/CHAPTER-006-leaving-systems-better-than-you-found-them.md`.
- Reserved manuscript path:
  `book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md`.
- `CHAPTER-006` status: `draft`.
- Reader-facing manuscript created: no.
- Author Draft started: no.
- Chapter 7 or Part II started: no.
- Approved central thesis: When a change exposes or creates structural cost, include the smallest justified improvement
  that reduces that cost without displacing the product outcome.
- Recommended embedded story direction: a new board revision introduces another power-monitor peripheral; the fast path
  would add another platform-specific conditional to an overloaded shared module; the bounded stewardship action
  localizes device-specific behavior, removes one verified obsolete path or unused option, records the decision, and
  adds only minimal useful diagnostics; the product commitment remains deliverable; no broad rewrite is started.
- Engineering Principle target: When a change exposes or creates structural cost, include the smallest justified
  improvement that reduces that cost without displacing the product outcome.
- Architecture Exercise target: Define a Bounded Stewardship Action.
- Chapter-local ADR working title: Localize Power-Monitor Variation While Delivering the New Board Revision.
- Exact PEAK relationships registered:
  - `CHAPTER-006 references VOCAB-007`.
  - `CHAPTER-006 illustrates LAW-004`.
  - `CHAPTER-006 illustrates LAW-006`.
  - `CHAPTER-006 references VOCAB-001`.
  - `CHAPTER-006 references METRIC-001`.
  - `CHAPTER-006 references METRIC-003`.
  - `CHAPTER-006 illustrates SMELL-002`.
  - `CHAPTER-006 illustrates SMELL-005`.
  - `CHAPTER-006 references ANTIPATTERN-006`.
  - `CHAPTER-006 references ARTIFACT-003`.
- New PEAK concepts created: none.
- Existing PEAK concept files changed: no.
- Existing entity statuses changed: no.
- `editor/CANON.md` changed: no.
- Frozen Chapters 1-5 changed: no.
- Canonical manuscript duplicated under `docs/`: no.
- Protected files changed during this remediation before the log entry: none.
- Required repository reading completed: `editor/EDITOR_LOG.md`, `editor/REVIEW_PROCESS.md`,
  `editor/SOURCE_OF_TRUTH.md`, `knowledge/index.yaml`, and the Chapter 6 canonical brief.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - `git switch chapter6`: passed; branch was already tracking `origin/chapter6`.
  - `git status --short --branch`: passed before editing; branch was `chapter6` and the working tree was clean.
  - `git rev-parse HEAD`: passed and returned `1a079b02730d70fb4cc08b62edcaa2c593e0cb56`.
  - `git rev-parse origin/chapter6`: passed and returned `1a079b02730d70fb4cc08b62edcaa2c593e0cb56`.
  - `git rev-parse origin/main`: passed and returned `749e6239c0561cf510bffc85f500261bdb287b0c`.
  - `git merge-base HEAD origin/main`: passed and returned `749e6239c0561cf510bffc85f500261bdb287b0c`.
  - Pre-edit `git diff --check`: passed.
  - YAML parse and direct PEAK checks: passed; `CHAPTER-006` entity count was exactly 1; `CHAPTER-006` had type
    `chapter`, name `Leaving Systems Better Than You Found Them`, path
    `../book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md`, and status `draft`;
    Chapters 1-5 remained `canonical`; outgoing Chapter 6 relationship count was exactly 10; the relationship set
    exactly matched the approved set; every relationship target existed; no duplicate relationships were present; the
    Chapter 6 manuscript was absent; the Chapter 6 canonical brief existed.
  - `npm.cmd run lint:md`: passed with 0 errors across 129 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 128 checked files after this log entry.
  - Post-edit `git diff --check`: passed.
  - Post-edit direct PEAK checks: passed.
  - `vale --config .vale.ini editor\EDITOR_LOG.md`: passed with 0 errors, 0 warnings, and 0 suggestions.
  - Changed-file verification: `git diff --name-status` showed only `editor/EDITOR_LOG.md`.
- Changed-file intent for this remediation: only `editor/EDITOR_LOG.md`.
- Next required stage: Chapter 6 Author Draft, only after author approval.

## Phase 11 Chapter 6 Author Draft

- Chapter: Leaving Systems Better Than You Found Them.
- Stable ID: `CHAPTER-006`.
- Branch: `chapter6`.
- Lifecycle stage: Author Draft.
- Starting HEAD for this authoring pass: `e603967153986b46bf9b9f307487e62827117c21`.
- Verified baseline `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- `origin/main..HEAD` commit count before authoring: 1.
- Pre-existing branch commit before authoring: `e603967153986b46bf9b9f307487e62827117c21`
  (`docs: Register Chapter 6 canonical brief`).
- Squashed preparation state accepted: yes; branch contained the single Chapter 6 canonical-brief registration commit.
- Manuscript path created:
  `book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md`.
- Approximate manuscript word count after authoring checks: 3610.
- Required reader-facing structure present: yes; H1 and required H2 sections match the Chapter 6 brief and template.
- Opening Quote present: yes; original and unattributed.
- Story used: One More Board Revision / power-monitor variation.
- Engineering Principle used: When a change exposes or creates structural cost, include the smallest justified
  improvement that reduces that cost without displacing the product outcome.
- Architecture Exercise used: Define a Bounded Stewardship Action.
- Principal's Notebook observations: exactly 3.
- Chapter-local ADR present: yes; required Chapter ADR title and Context, Decision, Consequences, and Alternatives
  Considered sections are present.
- PEAK relationships supported in manuscript: yes; the draft materially references or illustrates the registered
  Chapter 6 concepts and laws: `VOCAB-007`, `LAW-004`, `LAW-006`, `VOCAB-001`, `METRIC-001`, `METRIC-003`,
  `SMELL-002`, `SMELL-005`, `ANTIPATTERN-006`, and `ARTIFACT-003`.
- New PEAK concepts created: none.
- `knowledge/index.yaml` changed during Author Draft: no.
- Existing PEAK concept files changed during Author Draft: no.
- Canonical brief changed during Author Draft: no.
- `editor/CANON.md` changed during Author Draft: no.
- Frozen Chapters 1-5 changed during Author Draft: no.
- Chapter 7 or Part II manuscript started: no.
- Canonical manuscript duplicated under `docs/`: no.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed during preflight.
  - `git switch chapter6`: passed during preflight; branch was already tracking `origin/chapter6`.
  - `git status --short --branch`: passed during preflight; branch was `chapter6` and the working tree was clean.
  - `git rev-parse HEAD`: passed during preflight and returned
    `e603967153986b46bf9b9f307487e62827117c21`.
  - `git rev-parse origin/chapter6`: passed during preflight and returned
    `e603967153986b46bf9b9f307487e62827117c21`.
  - `git rev-parse origin/main`: passed during preflight and returned
    `749e6239c0561cf510bffc85f500261bdb287b0c`.
  - `git merge-base HEAD origin/main`: passed during preflight and returned
    `749e6239c0561cf510bffc85f500261bdb287b0c`.
  - `git rev-list --count origin/main..HEAD`: passed during preflight and returned `1`.
  - Condensed decorated git log for `origin/main..HEAD`: passed during preflight; showed only the one-line entry
    `e603967 docs: Register Chapter 6 canonical brief`.
  - `git diff --name-status origin/main...HEAD`: passed during preflight; branch diff was limited to the Chapter 6
    canonical brief, `knowledge/index.yaml`, and `editor/EDITOR_LOG.md`.
  - Direct manuscript checks: passed for exact manuscript path, one H1, required H2 order, no empty required section,
    exact ADR section structure, exactly three Principal's Notebook observations, required Architecture Exercise final
    question, required thesis/supporting formulation, Part I / Part II bridge, required PEAK references, no raw URLs,
    no conflict markers, no `TODO`/`TBD`/`AUTHOR NOTE`, and no banned chapter-local scoring artifacts.
  - Direct PEAK checks: passed; `CHAPTER-006` entity count was exactly 1; path, title, type, and status matched the
    canonical brief; Chapters 1-5 remained `canonical`; the outgoing Chapter 6 relationship count was exactly 10; the
    relationship set exactly matched the approved canonical-brief set; every relationship target existed; no duplicate
    relationships were present.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - Initial targeted Vale run failed on an early hardware-work spelling term; the manuscript text was revised to avoid
    that term.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md
    editor/EDITOR_LOG.md`: passed after revision with 0 errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
- Protected-file comparison result: expected Author Draft changes are limited to the new Chapter 6 manuscript and this
  editor log entry; previously registered Chapter 6 canonical-brief files remain unchanged by this authoring pass.
- Next required stage: Editorial Review.

## Phase 12 Chapter 6 Editorial Review

- Chapter: Leaving Systems Better Than You Found Them.
- Stable ID: `CHAPTER-006`.
- Branch: `chapter6`.
- Author Draft baseline full SHA: `de019efc710d4b5d8ff1481f172a9b1fa0b475ea`.
- Verified baseline `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Merge base with `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Stage: Editorial Review.
- Outcome: Approved with minor changes.
- Editorial issues reviewed: opening quote, story clarity and pacing, concrete power-monitor detail, bounded Principal
  Engineer intervention, discussion flow, stewardship-versus-cleanup distinction, "when not to refactor" section,
  stop condition, Engineering Principle prominence, exercise usability, Principal's Notebook brevity, chapter-local
  ADR compactness, and Editor's Commentary transition.
- Exact editorial corrections made:
  - Rewrapped one long story sentence about diagnostic text and configuration flags for readability.
  - Revised the Architecture Exercise prompts so product validation and stewardship-action validation are distinct, debt
    left out of scope is explicit, and the decision record or review trigger is discoverable.
  - Added the missing chapter-brief ADR alternatives for a speculative generic plug-in framework and feature-only
    delivery with every structural correction deferred.
  - Tightened one Editor's Commentary line break in the Part II transition.
- Central thesis preserved: yes.
- Story and product outcome preserved: yes; the new board revision still ships without another unconditional
  conditional patch or a broad startup rewrite.
- Required structure result: passed; one H1 and the eight required H2 sections are present exactly once and in order.
- Principal's Notebook count: exactly 3.
- ADR result: passed; required chapter-local ADR title and Context, Decision, Consequences, and Alternatives Considered
  sections are present, with alternatives aligned to the canonical brief.
- Editor's Commentary result: passed; it explains the Chapter 5 transition, closes Part I, and preserves later-part
  boundaries without repository workflow language.
- All ten PEAK relationships preserved: yes.
- New PEAK concepts: none.
- Unresolved author notes: none.
- Chapters 1-5 unchanged: yes.
- Canonical brief unchanged: yes.
- `knowledge/index.yaml` unchanged: yes.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed during Gate 0.
  - `git switch chapter6`: passed; branch was already tracking `origin/chapter6`.
  - `git pull --ff-only`: passed; branch was already up to date.
  - `git status --short --branch`: passed before editing; branch was clean and synchronized with `origin/chapter6`.
  - `git rev-parse HEAD`: passed and returned `de019efc710d4b5d8ff1481f172a9b1fa0b475ea`.
  - `git rev-parse origin/chapter6`: passed and returned `de019efc710d4b5d8ff1481f172a9b1fa0b475ea`.
  - `git rev-parse origin/main`: passed and returned `749e6239c0561cf510bffc85f500261bdb287b0c`.
  - `git merge-base origin/main HEAD`: passed and returned `749e6239c0561cf510bffc85f500261bdb287b0c`.
  - `git log -1 --format=%s`: passed and returned `docs(chapter-6): add author draft`.
  - `git diff --name-status origin/main...HEAD`: passed during Gate 0; branch diff was limited to the exact Chapter 6
    file set.
  - Direct Gate 0 checks: passed for lifecycle headings Phase 10 and Phase 11, no existing Phase 12-15 records, exact
    manuscript and canonical brief paths, no duplicate manuscript under `docs/`, valid `knowledge/index.yaml`,
    `CHAPTER-006` status `draft`, Chapters 1-5 status `canonical`, exact ten Chapter 6 relationships, no Chapter 7 or
    Part II manuscript, no tracked generated output, no conflict markers, and clean working tree.
  - Direct editorial checks: passed for exact H1, required H2 order, no empty required section, complete ADR headings,
    exactly three Principal's Notebook bullets, required PEAK references, no `AUTHOR NOTE`/`TODO`/`TBD`, no raw URL or
    external citation, exact PEAK entity and relationship state, no protected-file change, and no tracked generated
    output.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md
    editor/EDITOR_LOG.md`: passed with 0 errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
- Next stage: Canon Review.

## Phase 13 Chapter 6 Canon Review

- Chapter: Leaving Systems Better Than You Found Them.
- Stable ID: `CHAPTER-006`.
- Branch: `chapter6`.
- Editorial Review baseline full SHA: `a98f566a671c869a51e9c2ec8d3d4b63d1a150c5`.
- Verified baseline `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Merge base with `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Stage: Canon Review.
- Outcome: Approved.
- Central thesis result: passed; the chapter remains centered on the smallest justified improvement that reduces
  change-exposed structural cost without displacing the product outcome.
- Chapter 1 boundary result: passed; it operationalizes responsibility for future system cost without redefining the
  Principal Engineer role.
- Chapter 2 boundary result: passed; the product commitment is treated as given, and the chapter does not repeat the
  constrained decision framework.
- Chapter 3 boundary result: passed; discoverability helps the next engineer without becoming an inquiry-method chapter.
- Chapter 4 boundary result: passed; ownership appears only to make the current boundary visible and does not reteach
  handoff or closure.
- Chapter 5 boundary result: passed; evidence is used as a guardrail without repeating confidence calibration or weak
  signal handling.
- Part II and later-part boundary results: passed; `LAW-004` and `LAW-006` are applied without surveying all laws, and
  the chapter does not consume Part III boundary-design, Part IV product-line or observability, Part V ritual, or Part
  VI legacy-refactoring material.
- Canonical structure result: passed; one H1, required H2 order, exactly three Principal's Notebook bullets, and
  complete chapter-local ADR are present.
- Terminology result: passed; stewardship and related phrases remain chapter-local ordinary prose, with no new stable ID.
- PEAK material-support results:
  - `CHAPTER-006 references VOCAB-007`: supported by the Architecture Health definition of absorbing necessary change
    without disproportionate cost.
  - `CHAPTER-006 illustrates LAW-004`: supported by the simplicity discussion around reviewable boundaries and reduced
    mental burden.
  - `CHAPTER-006 illustrates LAW-006`: supported by the unused monitor-selection option and obsolete fallback.
  - `CHAPTER-006 references VOCAB-001`: supported by the Change Radius discussion around review, test, and ownership
    surface.
  - `CHAPTER-006 references METRIC-001`: supported by the approximate, non-numeric Change Radius metric treatment.
  - `CHAPTER-006 references METRIC-003`: supported by selected implementation visibility, stable failure categories,
    and Decision Journal discoverability.
  - `CHAPTER-006 illustrates SMELL-002`: supported by the shared support module accumulating unrelated boot behavior.
  - `CHAPTER-006 illustrates SMELL-005`: supported by monitor-specific timing and status details leaking into product
    startup code.
  - `CHAPTER-006 references ANTIPATTERN-006`: supported by the prototype fallback as a temporary path requiring
    evidence, owner, and removal conditions.
  - `CHAPTER-006 references ARTIFACT-003`: supported by the Decision Journal entry recording boundary, evidence, scope,
    and review triggers.
- Relationship changes: none.
- New PEAK concepts: none.
- Chapter-local language result: passed; no chapter-local phrase is presented as a canonical PEAK entity.
- Chapter-local ADR result: passed; it is reader-facing, story-local, aligned with the story, principle, and exercise,
  and does not imply an `editor/decisions/` ADR was created.
- Part I closure result: passed; the chapter closes the six-chapter Part I sequence and transitions naturally to Part
  II without claiming the Principal Engineer role is exhaustively defined.
- Unresolved canon issues: none.
- `knowledge/index.yaml` unchanged: yes.
- `editor/CANON.md` unchanged: yes.
- PEAK concept files unchanged: yes.
- Frozen Chapters 1-5 unchanged: yes.
- Manuscript changed during Canon Review: no.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - Gate preconditions: passed; working tree was clean, local `HEAD` equaled `origin/chapter6`, latest commit subject
    was `docs(chapter-6): complete editorial review`, Editorial Review outcome was `Approved with minor changes`, and
    `CHAPTER-006` status remained `draft`.
  - Direct canon checks: passed for canonical brief alignment, exact Chapter 6 relationship set, all targets existing,
    supported relationship types, no duplicate edge, no self-edge, no new stable ID, no status change, no accidental
    capitalized chapter-local PEAK concept, no changed `knowledge/index.yaml`, no changed PEAK concept file, no changed
    `editor/CANON.md`, no changed Frozen Chapters 1-5, and no manuscript duplicate under `docs/`.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md
    editor/EDITOR_LOG.md`: passed with 0 errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
- Next stage: Technical Review.

## Phase 14 Chapter 6 Technical Review

- Chapter: Leaving Systems Better Than You Found Them.
- Stable ID: `CHAPTER-006`.
- Branch: `chapter6`.
- Canon Review baseline full SHA: `0edd60df9c319d121b542c5298f0fb704b55d595`.
- Verified baseline `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Merge base with `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Stage: Technical Review.
- Outcome: Approved with minor changes.
- Technical areas examined: peripheral replacement credibility, product-level versus platform-level boundary, startup
  and safety claims, obsolete fallback removal, unused option narrowing, diagnostics, testing model, Utility Gravity,
  Platform Leakage, Change Radius, Discoverability, Decision Journal, Temporary Solution, non-refactoring guidance, stop
  condition, exercise applicability, and ADR consistency.
- Exact corrections applied:
  - Bounded obsolete fallback removal to supported product and service scope using product support, service,
    manufacturing, release, configuration, and test evidence.
  - Clarified that a missing owner is a warning sign, not proof by itself.
  - Aligned the ADR Decision and fallback alternative with that supported-scope evidence.
- Peripheral replacement credibility: passed; the chapter credibly describes external power-monitor differences in
  startup readiness, reset behavior, live versus latched status, status interpretation, error reporting, and diagnostic
  detail without naming a vendor or claiming interchangeability without validation.
- Boundary result: passed; product startup owns product-level continue/reject policy, while monitor implementations own
  timing, reset semantics, status interpretation, and device-specific translation.
- Startup and safety result: passed; power health remains a product-level interpretation, diagnostics do not replace
  validation, and timing/status validation remain necessary.
- Fallback-removal result: passed after correction; removal is bounded to supported product/service scope and supported
  by product support, service, manufacturing, release, configuration, and test evidence.
- Unused-option result: passed; `LAW-006` is applied to unsupported flexibility, not to all future options.
- Diagnostic result: passed; selected monitor implementation and product-level power-health failure reason are useful
  without leaking raw register semantics or becoming full observability design.
- Testing result: passed; monitor implementation tests, product startup tests, and manufacturing tests have distinct and
  credible responsibilities without claiming complete coverage.
- Utility Gravity and Platform Leakage result: passed; both smells are illustrated by concrete behavior in the shared
  startup-support module.
- Change Radius result: passed; the chapter avoids file-count precision and describes reduced review/test surface as a
  structurally enabled outcome.
- Discoverability and Decision Journal result: passed; implementation visibility, stable failure categories, boundary,
  owner, evidence, and review triggers are recorded without treating records as sufficient by themselves.
- Temporary Solution result: passed; the prototype fallback is treated as a temporary path needing owner, review trigger,
  and removal condition without becoming a safe-deletion tutorial.
- Non-refactoring and stop-condition result: passed; insufficient evidence, weak test protection, incident restoration,
  other-team ownership, and unclear review boundary remain credible reasons not to refactor, and the stop condition does
  not claim all risk is removed.
- Exercise result: passed; the exercise distinguishes product outcome, structural cost, supporting evidence, bounded
  change, unchanged behavior, validation, out-of-scope work, stop condition, and decision record/review trigger.
- ADR consistency result: passed; ADR context, decision, consequences, and alternatives match the story and avoid
  implementation guarantees.
- Unresolved technical issues: none.
- PEAK graph unchanged: yes.
- Canonical brief unchanged: yes.
- Frozen Chapters 1-5 unchanged: yes.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - Gate preconditions: passed; working tree was clean, local `HEAD` equaled `origin/chapter6`, latest commit subject
    was `docs(chapter-6): complete canon review`, Canon Review outcome was `Approved`, Editorial Review remained
    approved, `CHAPTER-006` status remained `draft`, and the PEAK graph remained exact.
  - Direct technical checks: passed for no unsupported electrical or safety guarantee, no vendor-specific factual claim,
    no raw register tutorial, no claim that diagnostics replace validation, no claim that the new boundary eliminates
    future variant cost, no claim that fallback removal is safe outside supported scope, no story/ADR contradiction, no
    story/exercise contradiction, and exact PEAK graph unchanged.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md
    editor/EDITOR_LOG.md`: passed with 0 errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
- Next stage: Freeze Review.

## Phase 15 Chapter 6 Freeze Review

- Chapter: Leaving Systems Better Than You Found Them.
- Stable ID: `CHAPTER-006`.
- Branch: `chapter6`.
- Technical Review baseline full SHA: `b613c698f8e82f2992f51ceb2b5b3e465e59306c`.
- Technical Review manuscript blob: `568d5a378b9e6cc622a75ff0728e0065751f5a32`.
- Verified baseline `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Merge base with `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Stage: Freeze Review.
- Outcome: Approved.
- Prior review outcomes:
  - Editorial Review: Approved with minor changes.
  - Canon Review: Approved.
  - Technical Review: Approved with minor changes.
- One central idea result: passed; the chapter teaches bounded stewardship of the current product commitment by making
  the next necessary change cheaper, safer, or easier to understand without turning the work into broad cleanup.
- Distinct chapter role result: passed; Chapter 6 closes Part I by showing how Principal Engineer habits leave a system
  behind, while Chapters 1-5 retain their separate roles around role definition, constraints, questions, ownership, and
  evidence.
- Structure result: passed; the chapter has opening quote, story, discussion, engineering principle, architecture
  exercise, Principal's Notebook, ADR, and Editor's Commentary sections.
- Editorial stability result: passed; story, discussion, exercise, ADR, and commentary are coherent and complete.
- Canon stability result: passed; the manuscript remains aligned with the canonical brief and existing PEAK graph.
- Technical stability result: passed; the final technical corrections are present, and no unresolved technical issues
  remain.
- Story credibility result: passed; the peripheral replacement story remains credible without vendor-specific claims or
  unsupported safety guarantees.
- Reader value result: passed; the chapter gives the reader a usable way to distinguish bounded stewardship from
  speculative refactoring or neglect.
- Timelessness result: passed; the chapter relies on durable engineering judgment rather than current product, tool, or
  vendor details.
- PEAK entity pre-transition: `CHAPTER-006` existed exactly once with status `draft`.
- PEAK entity final transition: `CHAPTER-006` status changed to `canonical`.
- Relationship result: passed; the exact ten Chapter 6 relationships were retained:
  - `CHAPTER-006 references VOCAB-007`.
  - `CHAPTER-006 illustrates LAW-004`.
  - `CHAPTER-006 illustrates LAW-006`.
  - `CHAPTER-006 references VOCAB-001`.
  - `CHAPTER-006 references METRIC-001`.
  - `CHAPTER-006 references METRIC-003`.
  - `CHAPTER-006 illustrates SMELL-002`.
  - `CHAPTER-006 illustrates SMELL-005`.
  - `CHAPTER-006 references ANTIPATTERN-006`.
  - `CHAPTER-006 references ARTIFACT-003`.
- Relationship changes: none.
- New PEAK concepts: none.
- PEAK concept files changed: no.
- Manuscript changes during Freeze Review: none.
- Manuscript byte identity result: passed; the manuscript blob remained
  `568d5a378b9e6cc622a75ff0728e0065751f5a32`.
- Protected files unchanged: manuscript, canonical brief, `editor/CANON.md`, PEAK concept files, and frozen Chapters
  1-5 remained unchanged during the freeze transition.
- Chapter 7 or later-part material started: no.
- Generated output tracked: no.
- Duplicate manuscript under `docs/`: no.
- Unresolved issues: none.
- Validation blockers: none.
- Validation commands and actual pre-transition results:
  - `git fetch --all --prune`: passed.
  - Gate preconditions: passed; working tree was clean, local `HEAD` equaled `origin/chapter6`, latest commit subject
    was `docs(chapter-6): complete technical review`, prior reviews were approved, `CHAPTER-006` status remained
    `draft`, branch diff was limited to the expected Chapter 6 files, and the manuscript blob matched the Technical
    Review blob.
  - Direct freeze checks: passed for central idea, distinct role, chapter structure, lifecycle records Phase 10-14,
    exact PEAK entity, Chapters 1-5 canonical, exact ten relationships, no tracked generated output, no duplicate
    manuscript, no Chapter 7 start, and manuscript byte identity.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md
    editor/EDITOR_LOG.md`: passed with 0 errors, 0 warnings, and 0 suggestions.
  - `vale .`: completed with 0 errors, 5 warnings, and 0 suggestions in 130 files; the warnings were existing
    `PrincipalEngineerHandbook.AuthorBoundary` warnings in `CONTRIBUTING.md`, Chapter 1, `editor/ARCHITECTURE_REVIEW_0.md`,
    and `editor/SOURCE_OF_TRUTH.md`.
  - `python -m pip check`: passed; no broken requirements found.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed; generated PDF output
    was not tracked by Git.
- Validation commands and actual post-transition results:
  - Direct post-transition freeze checks: passed for changed-file scope, `CHAPTER-006` final status `canonical`,
    Chapters 1-5 canonical, exact ten relationships, lifecycle records Phase 10-15, no tracked generated output, and
    manuscript byte identity.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md
    editor/EDITOR_LOG.md`: passed with 0 errors, 0 warnings, and 0 suggestions.
  - `vale .`: completed with 0 errors, 5 warnings, and 0 suggestions in 130 files; the warnings were existing
    `PrincipalEngineerHandbook.AuthorBoundary` warnings in `CONTRIBUTING.md`, Chapter 1, `editor/ARCHITECTURE_REVIEW_0.md`,
    and `editor/SOURCE_OF_TRUTH.md`.
  - `python -m pip check`: passed; no broken requirements found.
  - `Remove-Item Env:ENABLE_PDF_EXPORT -ErrorAction SilentlyContinue; python -m mkdocs build --strict`: passed.
  - `$env:ENABLE_PDF_EXPORT='1'; python -m mkdocs build --config-file mkdocs-pdf.yml`: passed; generated PDF output
    was not tracked by Git.
- Pre-transition Chapter 6 status: `draft`.
- Final Chapter 6 status: `canonical`.
- Chapter 6 Frozen: yes.
- Branch merged status: no.
- Next repository step: open the `chapter6` pull request.

## Phase 16 Chapter 1 Editorial Revalidation

- Chapter: What Is a Principal Engineer?
- Stable ID: `CHAPTER-001`.
- Branch: `chapter1-revalidation`.
- Current `origin/main` full SHA: `51404070540cc1bfeccb023da0e6a4cf8ddd60fb`.
- Revalidation baseline full SHA: `51404070540cc1bfeccb023da0e6a4cf8ddd60fb`.
- Original Chapter 1 Freeze baseline: `7825661b612573c5a0ce43ce22df26ecc532e39f`.
- Stage: Editorial Revalidation.
- Outcome: Request changes.
- Reason for revalidation: the original Chapter 1 Freeze Review approved the chapter, but recorded that `npm`, Vale,
  and MkDocs checks were unavailable in that review environment. The current audit reran the editorial gate with the
  repository validation tools now available.
- Editorial areas reviewed: central idea, manufacturing story flow, transition from story to discussion and principle,
  readability, pacing, repetition, terminology, voice consistency with Chapters 2-6, required chapter architecture,
  Architecture Exercise, Principal's Notebook, chapter-local ADR, Editor's Commentary, stale draft language, repository
  workflow language, unresolved author notes, placeholders, and accidental dependence on later Part I chapters.
- Part I continuity result: passed; Chapter 1 still works as the opening Part I chapter after Chapters 2-6 were added.
  It introduces Principal Engineering as responsibility for future system cost without absorbing the later detailed
  treatments of constraints, inquiry, ownership, evidence, or bounded stewardship.
- Chapter architecture result: passed; the required H2 sections are present exactly once and in order.
- Principal's Notebook count: passed; exactly three concise observations are present.
- ADR result: passed; the chapter-local ADR has context, decision, consequences, and alternatives considered.
- Unresolved editorial issues:
  - Targeted Vale now reports two Chapter 1 `PrincipalEngineerHandbook.AuthorBoundary` warnings in the frozen manuscript:
    line 158 column 201 and line 198 column 100.
  - Because these warnings are inside Chapter 1 and this audit must not edit frozen prose, they require an explicit
    Editorial Review reopen decision rather than a silent manuscript correction.
- Manuscript changes: none.
- Manuscript blob identity result: passed; the manuscript blob remained
  `8bec1ac7f6a7f0bed674a298865f649ffab0c5d1`.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - `git switch main`: passed.
  - `git pull --ff-only`: passed.
  - Gate 0 preflight: passed; local `main` equaled `origin/main`, the Chapter 6 merge commit was an ancestor of
    `origin/main`, no local or remote `chapter1-revalidation` branch existed, Chapter 1 existed only under `book/`,
    `knowledge/index.yaml` parsed successfully, `CHAPTER-001` and Chapters 2-6 were `canonical`, original Chapter 1
    review history was present, no existing Chapter 1 revalidation records existed, no Part II manuscript was started,
    and no generated `site/` output was tracked.
  - `git switch -c chapter1-revalidation origin/main`: passed.
  - Direct editorial checks: passed for exact H1, required H2 order, nonempty required sections, exactly three
    Principal's Notebook bullets, complete ADR headings, no unresolved `AUTHOR NOTE`, `TODO`, `TBD`, placeholder, or
    conflict marker, manuscript-only-under-`book/`, and unchanged manuscript blob.
  - `git diff --check`: passed.
  - `npm.cmd ci`: passed; repository JavaScript dependencies installed from `package-lock.json`.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md`: completed with
    0 errors, 2 warnings, and 0 suggestions; both warnings were `PrincipalEngineerHandbook.AuthorBoundary` warnings in
    Chapter 1.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
- Later revalidation gates run: no.
- Required reopen stage: Chapter 1 Editorial Review.

## Phase 17 Chapter 1 Editorial Revalidation Remediation

- Chapter: What Is a Principal Engineer?
- Stable ID: `CHAPTER-001`.
- Branch: `chapter1-revalidation`.
- Phase 16 baseline commit: `df59b09790d451b0cf386e99746f57dd204182ab`.
- Current `origin/main` full SHA: `51404070540cc1bfeccb023da0e6a4cf8ddd60fb`.
- Stage: Editorial Revalidation Remediation.
- Outcome: Approved.
- Reason for reopen: Phase 16 stopped because targeted Vale reported two
  `PrincipalEngineerHandbook.AuthorBoundary` warnings inside the frozen Chapter 1 manuscript. This phase reopened
  Chapter 1 at Editorial Review only to resolve those two lexical findings.
- Exact Vale findings resolved:
  - `book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md:158:201`.
  - `book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md:198:100`.
- Exact wording changes:
  - At line 158, replaced the prior decision-conditions phrase with "important decisions have visible reasoning,
    explicit ownership, and enough durable context to remain understandable".
  - At line 198, replaced the prior decision-system phrase with "designs the decision system around the software, not
    only the software itself".
- Central thesis preserved: yes; the chapter still defines Principal Engineering as responsibility for the future cost
  of the system.
- Chapter structure preserved: yes; no heading changed, no paragraph moved, and all required sections remain present in
  order.
- PEAK relationships preserved: yes; `CHAPTER-001 references ARTIFACT-001` and `CHAPTER-001 illustrates SMELL-001`
  remain unchanged.
- Old manuscript blob: `8bec1ac7f6a7f0bed674a298865f649ffab0c5d1`.
- New manuscript blob: `92da84beeaa8ca303d0518130646a56a27b6d23c`.
- Targeted Vale result: passed with 0 errors, 0 warnings, and 0 suggestions for Chapter 1.
- Validation commands and actual results:
  - Gate 0 preflight: passed; branch, local and remote HEAD, `origin/main`, merge base, latest subject, branch diff,
    original manuscript blob, Phase 16 Request changes record, canonical statuses, absence of Phase 17-20 records, no
    Part II manuscript, and no tracked generated output matched the prompt requirements.
  - Shared-reading checks: passed; the manuscript, Phase 16 entry, original Chapter 1 history, editor policy files,
    PEAK index, Chapter 1 PEAK concepts, Chapters 2-6, `.vale.ini`, and `AuthorBoundary.yml` were reviewed.
  - AuthorBoundary rule check: passed; it is an existence rule with tokens `obviously`, `clearly`, `simply`, and
    `everyone knows`.
  - Exact-fragment check: passed; both source fragments existed exactly once before replacement.
  - Editorial scope checks: passed; exactly two approved prose replacements were made, no heading changed, no paragraph
    moved, no PEAK stable ID changed, no raw URL was added, Chapter 1 still exists only under `book/`, the PEAK graph
    is unchanged, and Chapters 2-6 are unchanged.
  - `git diff --check`: passed.
  - `npm.cmd ci`: passed; repository JavaScript dependencies installed from `package-lock.json`.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md`: passed with
    0 errors, 0 warnings, and 0 suggestions.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
- Unresolved editorial issues: none.
- Next stage: Canon Revalidation.

## Phase 18 Chapter 1 Canon Revalidation

- Chapter: What Is a Principal Engineer?
- Stable ID: `CHAPTER-001`.
- Branch: `chapter1-revalidation`.
- Stage: Canon Revalidation.
- Outcome: Approved.
- Baseline remediation commit: `09429eed0948df568c3a24081b68c7b39b9dc3de`.
- Current `origin/main` full SHA: `51404070540cc1bfeccb023da0e6a4cf8ddd60fb`.
- Manuscript blob verified: `92da84beeaa8ca303d0518130646a56a27b6d23c`.
- Canon status: `CHAPTER-001` remains `canonical`.
- Chapter sequence status: `CHAPTER-001` through `CHAPTER-006` remain `canonical`.
- PEAK relationship check: passed; Chapter 1 still has exactly these relationships:
  - `CHAPTER-001 references ARTIFACT-001`.
  - `CHAPTER-001 illustrates SMELL-001`.
- Canon consistency checks:
  - `CHAPTER-001` exists exactly once in `knowledge/index.yaml`.
  - Title, path, type, and status match the canonical Chapter 1 entry.
  - Relationship endpoints exist, relationship types are supported, and no duplicate or self-edge relationship was
    found.
  - No PEAK stable ID, status, path, or relationship changed during the remediation.
- Validation commands and actual results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - Direct structured PEAK assertions: passed for Chapter 1 uniqueness, Chapter 1 metadata, Chapter 1 relationships,
    Chapter 1-6 canonical statuses, supported relationship types, endpoint existence, duplicate detection, and
    manuscript Git blob identity.
- Canon issues found: none.
- Next stage: Technical Revalidation.

## Phase 19 Chapter 1 Technical Revalidation

- Chapter: What Is a Principal Engineer?
- Stable ID: `CHAPTER-001`.
- Branch: `chapter1-revalidation`.
- Stage: Technical Revalidation.
- Outcome: Approved.
- Baseline canon revalidation commit: `c5d9f4a66c48c7dfff635401ab3d3283847987c9`.
- Current `origin/main` full SHA: `51404070540cc1bfeccb023da0e6a4cf8ddd60fb`.
- Manuscript blob verified: `92da84beeaa8ca303d0518130646a56a27b6d23c`.
- Technical review result:
  - The Chapter 1 remediation did not introduce unsupported engineering guarantees.
  - The chapter keeps implementation competence and technical depth as required context.
  - ADRs remain framed as decision records, not as a substitute for design, tests, or ownership.
  - The decision-system language remains bounded to the organizational and architectural conditions around software.
  - The production story, engineering principle, exercise, notebook, ADR, and editor commentary remain mutually aligned.
- PEAK relationship check: passed; `CHAPTER-001 references ARTIFACT-001` and `CHAPTER-001 illustrates SMELL-001`
  remain unchanged.
- Validation commands and actual results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - Direct technical assertions: passed for unsupported guarantee claims, impossible-causality claims, doc-alone
    prevention claims, decision-system-over-implementation claims, PEAK relationship identity, and manuscript Git blob
    identity.
- Technical issues found: none.
- Next stage: Freeze Revalidation.

## Phase 20 Chapter 1 Freeze Revalidation

- Chapter: What Is a Principal Engineer?
- Stable ID: `CHAPTER-001`.
- Branch: `chapter1-revalidation`.
- Stage: Freeze Revalidation.
- Outcome: Approved.
- Baseline technical revalidation commit: `10258dd7e5231e2b87e2a16dd7d0c9794df20e38`.
- Current `origin/main` full SHA: `51404070540cc1bfeccb023da0e6a4cf8ddd60fb`.
- Manuscript blob verified: `92da84beeaa8ca303d0518130646a56a27b6d23c`.
- Final lifecycle state: `CHAPTER-001` remains frozen and `canonical`.
- Protected-file scope: passed; branch diff versus `origin/main` is limited to:
  - `book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md`.
  - `editor/EDITOR_LOG.md`.
- Structure checks:
  - H1 matches `What Is a Principal Engineer?`.
  - H2 order is Opening Quote, Story, Discussion, Engineering Principle, Architecture Exercise,
    Principal's Notebook, ADR, Editor's Commentary.
  - Principal's Notebook contains exactly 3 bullets.
  - ADR contains the required chapter ADR title, Context, Decision, Consequences, and Alternatives Considered headings.
  - Manuscript contains no unresolved author markers, TODO/TBD markers, conflict markers, or raw URLs.
- Canon and PEAK checks:
  - `CHAPTER-001` through `CHAPTER-006` remain `canonical`.
  - `CHAPTER-001` path remains `../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md`.
  - Chapter 1 PEAK relationships remain exactly `CHAPTER-001 references ARTIFACT-001` and
    `CHAPTER-001 illustrates SMELL-001`.
  - No generated output is tracked.
  - No Part II manuscript files exist beyond README placeholders.
- Validation commands and actual results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `vale .`: completed with 0 errors, 3 warnings, and 0 suggestions across 130 files; the remaining warnings are
    outside Chapter 1 and `EDITOR_LOG.md` at `CONTRIBUTING.md:29:30`, `editor/ARCHITECTURE_REVIEW_0.md:49:85`, and
    `editor/SOURCE_OF_TRUTH.md:19:49`.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `ENABLE_PDF_EXPORT=1 python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and wrote
    `site/pdf/the-principal-engineer-handbook.pdf`.
  - PDF existence check: passed; generated PDF size was 275775 bytes.
  - Direct freeze assertions: passed for H1, H2 order, notebook bullet count, ADR headings, placeholder scan, conflict
    marker scan, raw URL scan, Chapter 1-6 canonical statuses, Chapter 1 path, Chapter 1 PEAK relationships, manuscript
    Git blob identity, PDF existence, absence of tracked `site/` output, absence of Part II manuscript files, and exact
    branch diff scope.
- Freeze issues found: none.
- Next step: open the revalidation pull request before starting Part II.

## Phase 21 Chapter 2 Editorial Revalidation

- Chapter: Decision-Making Under Constraints.
- Stable ID: `CHAPTER-002`.
- Branch: `chapter2-revalidation`.
- Current `origin/main` full SHA: `05911cd4ebcfd783ed2c51bf87aef77b3815ed6b`.
- Revalidation baseline full SHA: `05911cd4ebcfd783ed2c51bf87aef77b3815ed6b`.
- Original Technical Review baseline: `847db1aec67e93d961512f66e61c908dc342e7c8`.
- Original Freeze Review outcome: Request changes.
- Original Freeze Validation Remediation outcome: Approved with minor changes.
- Original Freeze Review Retry outcome: Approved.
- Reason for revalidation: Chapter 2 is Frozen and canonical, Chapter 1 post-freeze revalidation is now merged into
  `main`, and the completed Part I plus current repository tool chain require a fresh read-only audit before Part II.
- Stage: Editorial Revalidation.
- Outcome: Approved.
- Editorial areas reviewed: opening quote, hardware-freeze and release story context, stakeholder credibility, memory,
  recovery, diagnostics, qualification, schedule, variant-flexibility pressures, meeting sequence, story-to-discussion
  boundary, central idea, repetition, required chapter architecture, exercise, notebook, chapter-local ADR, editor
  commentary, stale workflow language, unresolved markers, and completed Part I continuity.
- Completed Part I continuity: passed; Chapter 2 remains the constrained-commitment chapter between Chapter 1's future
  system-cost frame and Chapter 3's inquiry-shaping work, without teaching the later ownership, evidence-quality, or
  stewardship frameworks early.
- Structure result: passed; the manuscript has exactly one H1 and the required H2 sections once in canonical order.
- Principal's Notebook count: passed; exactly three concise observations remain.
- ADR result: passed; the chapter-local ADR has Context, Decision, Consequences, and Alternatives Considered and remains
  consistent with the story, discussion, principle, exercise, and Decision Journal.
- Editor's Commentary result: passed; it accurately positions Chapter 2 after Chapter 1 and before Chapter 3.
- Unresolved editorial issues: none.
- Manuscript changes: none.
- Manuscript blob identity: passed; Chapter 2 remained
  `e78bd7f8468350622ae4b49f6590473818c5894e`.
- Validation commands and actual results:
  - Gate 0 preflight: passed; local `main` was clean and equaled `origin/main`, Chapter 1 post-freeze revalidation was
    merged, no local or remote `chapter2-revalidation` branch existed, Chapter 2 existed only under `book/`,
    `knowledge/index.yaml` parsed, `CHAPTER-002` was canonical with the expected metadata, Chapters 1 and 3-6 were
    canonical, original Chapter 2 lifecycle history was present, Phase 21-24 records were absent, no Part II manuscript
    existed, no tracked generated output existed, and the working tree had no unrelated files.
  - Shared repository reading: passed; editor policy files, full editor log, PEAK index, Chapter 2 manuscript,
    Chapters 1 and 3-6, table of contents, Chapter 2 PEAK concept files, and current tool chain configuration were read.
  - `npm.cmd ci`: passed; dependencies installed from `package-lock.json`.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/02-decision-making-under-constraints.md`: passed with
    0 errors, 0 warnings, and 0 suggestions.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - Direct editorial checks: passed for exact H1, H2 order, nonempty required sections, notebook bullet count, ADR
    headings, unresolved marker scan, conflict marker scan, raw URL scan, manuscript-only-under-`book/`, manuscript blob
    identity, exact five PEAK relationships, and protected-file scope before the log entry.
- Next stage: Canon Revalidation.

## Phase 22 Chapter 2 Canon Revalidation

- Chapter: Decision-Making Under Constraints.
- Stable ID: `CHAPTER-002`.
- Branch: `chapter2-revalidation`.
- Editorial Revalidation baseline full SHA: `8c5c4ca3caa669eb5f1b913906059cc5de9dcbc5`.
- Stage: Canon Revalidation.
- Outcome: Approved.
- Canonical purpose: passed; Chapter 2 remains focused on constrained commitments that name constraints, evidence,
  uncertainty, consequences, and reversal cost before commitment.
- Chapter 1 boundary: passed; the chapter builds on future system cost without redefining the Principal Engineer role
  or repeating Chapter 1 at length.
- Chapter 3 boundary: passed; the chapter stops before investigation framing, discriminating questions, root-cause
  inquiry, and observation-versus-interpretation work.
- Chapter 4 boundary: passed; the chapter may assign ownership to accepted consequences, but it does not teach outcome
  ownership, accepted handoffs, closure, or the ownership-beyond-code framework.
- Chapter 5 boundary: passed; `LAW-005` supports the constrained decision without duplicating evidence-quality
  dimensions, confidence calibration, weak signals, staged commitments, or experimental design.
- Chapter 6 boundary: passed; simplicity and unused flexibility support the Chapter 2 decision without turning the
  chapter into bounded stewardship.
- Part II boundary: passed; the chapter references `LAW-005`, `LAW-004`, and `LAW-006` without systematically teaching
  the laws.
- Exact PEAK relationship results:
  - `CHAPTER-002 illustrates LAW-005`: supported by the prototype-evidence, confidence, and commitment discussion.
  - `CHAPTER-002 references ARTIFACT-003`: supported by the compact Decision Journal entry.
  - `CHAPTER-002 references VOCAB-001`: supported by Change Radius reasoning around diagnostics and recovery.
  - `CHAPTER-002 references LAW-004`: supported by the preference for a reviewable, testable, explainable update path.
  - `CHAPTER-002 references LAW-006`: supported by removal of unowned speculative variant hooks.
- Relationship changes: none.
- New PEAK concepts: none.
- Decision Journal result: passed; it remains lightweight, subordinate to the thesis, aligned with `ARTIFACT-003`, and
  distinct from the chapter-local ADR.
- Chapter-local ADR result: passed; it records the story-local decision and does not become a handbook-wide canon entry.
- Completed Part I continuity: passed; Chapter 2 has a distinct role in the six-chapter Part I arc.
- Unresolved canon issues: none.
- Manuscript changes: none.
- PEAK changes: none.
- Manuscript blob identity: passed; Chapter 2 remained
  `e78bd7f8468350622ae4b49f6590473818c5894e`.
- Validation commands and actual results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/02-decision-making-under-constraints.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - Direct structured PEAK assertions: passed for exactly one `CHAPTER-002`, exact path and canonical status, Chapters
    1 and 3-6 canonical statuses, exact five Chapter 2 relationships, target existence, supported relationship types,
    duplicate and self-edge checks, stable entity identity, manuscript Git blob identity, and protected-file scope before
    this log entry.
- Next stage: Technical Revalidation.

## Phase 23 Chapter 2 Technical Revalidation

- Chapter: Decision-Making Under Constraints.
- Stable ID: `CHAPTER-002`.
- Branch: `chapter2-revalidation`.
- Canon Revalidation baseline full SHA: `5eba7a1a3f716d100b4e019684c709f88f7d2e74`.
- Stage: Technical Revalidation.
- Outcome: Approved.
- Memory constraint: passed; product image, recovery capability, diagnostics, and speculative hooks credibly compete for
  constrained memory without tying the chapter to one MCU or memory architecture.
- Recoverable update path: passed; the chapter remains architecture-neutral, does not prescribe A/B, dual-bank,
  rollback, delta, compression, or a specific bootloader, and treats recovery as important without making it an absolute
  guarantee.
- Complex mechanism evidence: passed; prototype and bench evidence are useful but insufficient for the low-reversibility
  field commitment described.
- Qualification: passed; changing the memory part credibly reopens board review, qualification, supply, manufacturing,
  or test work without claiming every substitution has identical cost.
- Diagnostics versus recovery: passed; deferred diagnostics carry product and service consequences, while recovery is
  treated as contextual rather than universally higher priority.
- Release commitment: passed; the date is a real external commitment, not a physical law, and deadline pressure does
  not erase risk.
- Speculative flexibility: passed; unused hooks consume memory, test, review, and release margin, and removal is tied to
  absent approved variant and absent committed owner.
- Simplicity: passed; the simpler mechanism is preferred because it is more reviewable, testable, explainable, and
  evidenced, not because simplicity has moral force.
- Change Radius: passed; the chapter treats Change Radius as affected product, support, tooling, service, trust, and
  deployed-device surface rather than changed-file count.
- Reversibility: passed; reversibility changes the evidence threshold and learning capacity without becoming harmlessness
  or failure probability.
- Decision quality: passed; good decisions can have bad outcomes, weak decisions can get lucky, and review triggers let
  later evidence update the decision.
- Risk ownership and review triggers: passed; accepted product and service cost has visible ownership, and review
  triggers are concrete enough to reopen the decision without claiming they enforce themselves.
- Decision Journal: passed; fields are meaningful, `Confidence: Medium` matches the evidence and uncertainty, and the
  date is a story-local record rather than a transient external dependency.
- Exercise: passed; a practicing engineer can distinguish hard constraints, renegotiable commitments, assumptions,
  evidence, consequence, Change Radius, reversibility, accepted risk, owner, and review trigger.
- ADR consistency: passed; Story, Discussion, Principle, Exercise, Decision Journal, and ADR describe one coherent
  constrained decision.
- Unresolved technical issues: none.
- Manuscript changes: none.
- Manuscript blob identity: passed; Chapter 2 remained
  `e78bd7f8468350622ae4b49f6590473818c5894e`.
- PEAK changes: none.
- Validation commands and actual results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/02-decision-making-under-constraints.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - Direct technical assertions: passed for memory pressure, update recovery, qualification, diagnostics, release date,
    speculative flexibility, simplicity, Change Radius, reversibility, Decision Journal confidence, ADR consistency,
    unsupported guarantee claims, impossible-causality claims, vendor-specific claims, deadline-justifies-risk claims,
    simple-means-safe claims, always-waste claims, self-enforcing-trigger claims, PEAK identity, and manuscript Git blob
    identity.
- Next stage: Freeze Revalidation.

## Phase 24 Chapter 2 Freeze Revalidation

- Chapter: Decision-Making Under Constraints.
- Stable ID: `CHAPTER-002`.
- Branch: `chapter2-revalidation`.
- Technical Revalidation baseline full SHA: `8d8a66b9ae7f2cbc342ae83dfdc0cd3bfd1d9576`.
- Stage: Freeze Revalidation.
- Outcome: Approved.
- Reason for revalidation: Chapter 2 was already Frozen and canonical; this gate validated it again against the completed
  Part I, current PEAK graph, current editorial policy, and current repository validation tools before Part II work.
- Original Technical Review baseline: `847db1aec67e93d961512f66e61c908dc342e7c8`.
- Original Freeze Review outcome: Request changes.
- Original Freeze Validation Remediation outcome: Approved with minor changes.
- Original Freeze Review Retry outcome: Approved.
- Current revalidation baseline: `05911cd4ebcfd783ed2c51bf87aef77b3815ed6b`.
- Phase 21 outcome: Approved.
- Phase 22 outcome: Approved.
- Phase 23 outcome: Approved.
- Central idea: passed; a sound engineering decision makes constraints, evidence, uncertainty, consequences, and reversal
  cost explicit before commitment.
- Distinct role: passed; Chapter 2 remains the constrained-commitment chapter and does not become a release-management,
  evidence-calibration, inquiry-method, ownership, stewardship, Decision Journal, or laws survey chapter.
- Structure: passed; one H1, required H2 order, exactly three Principal's Notebook bullets, and complete ADR headings.
- Editorial stability: passed; story, discussion, principle, exercise, notebook, ADR, and commentary remain stable.
- Canon stability: passed; no PEAK relationship, concept, status, or canon correction is required.
- Technical stability: passed; memory, recovery, update mechanism, qualification, diagnostics, release commitment,
  speculative flexibility, simplicity, Change Radius, reversibility, risk ownership, review triggers, Decision Journal,
  exercise, and ADR checks all passed.
- Story credibility: passed; the hardware-freeze and release story remains plausible and bounded.
- Decision Journal integrity: passed; it remains a lightweight record with date, decision, evidence, confidence, and
  review trigger.
- ADR integrity: passed; the chapter-local ADR remains consistent with the selected constrained decision.
- Exact PEAK integrity: passed; Chapter 2 relationships remain exactly:
  - `CHAPTER-002 illustrates LAW-005`.
  - `CHAPTER-002 references ARTIFACT-003`.
  - `CHAPTER-002 references VOCAB-001`.
  - `CHAPTER-002 references LAW-004`.
  - `CHAPTER-002 references LAW-006`.
- Reader value: passed; the chapter gives readers a usable way to name constraints, evidence, uncertainty, consequence,
  reversal cost, accepted risk, ownership, and review triggers.
- Timelessness: passed; the chapter does not depend on a specific vendor, MCU, bootloader architecture, update strategy,
  product, or transient external fact.
- Manuscript blob identity: passed; Chapter 2 remained
  `e78bd7f8468350622ae4b49f6590473818c5894e`.
- Manuscript changes: none.
- `CHAPTER-002` pre-state: `canonical`.
- `CHAPTER-002` final state: `canonical`.
- Chapter 2 remains Frozen: yes.
- Chapters 1 and 3-6 unchanged: yes.
- Part II started: no.
- Complete validations and actual results:
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 130 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 129 checked files.
  - `npm.cmd run lint:links`: passed; 129 links scanned successfully.
  - `vale --config .vale.ini book/01-thinking-like-a-principal/02-decision-making-under-constraints.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions.
  - `vale .`: completed with 0 errors, 0 warnings, and 0 suggestions in 0 files in this Windows environment.
  - `vale --config .vale.ini .`: completed with 0 errors, 3 warnings, and 0 suggestions across 130 files; the remaining
    warnings are pre-existing, outside Chapter 2 and `EDITOR_LOG.md`, at `CONTRIBUTING.md:29:30`,
    `editor/ARCHITECTURE_REVIEW_0.md:49:85`, and `editor/SOURCE_OF_TRUTH.md:19:49`.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `ENABLE_PDF_EXPORT=1 python -m mkdocs build --config-file mkdocs-pdf.yml`: passed and wrote
    `site/pdf/the-principal-engineer-handbook.pdf`.
  - PDF output verification: passed; generated PDF size was 275775 bytes.
  - Direct freeze assertions: passed for original Chapter 2 history, failed Freeze Review preservation, remediation
    preservation, Freeze Review Retry approval, Phase 21-23 approvals, H1, H2 order, notebook count, ADR headings,
    unresolved marker scan, conflict marker scan, raw URL scan, Chapter 2 entity integrity, exact five relationships,
    target existence, supported statuses, supported relationship types, duplicate and self-edge checks, path resolution,
    manuscript Git blob identity, exact branch changed-file set, no tracked generated output, and no Part II manuscript.
- Unresolved issues: none.
- Next step: merge this branch, then begin Chapter 7 preparation.

## Phase 25 Chapter 7 Canonical Brief Registration

- Chapter: Every State Has One Owner.
- Stable ID: `CHAPTER-007`.
- Branch: `chapter7`.
- Baseline `origin/main` full SHA: `8b95decf73a2771268c885143564f0bb4c23bd0f`.
- Stage: Canonical Brief Registration.
- Outcome: Canonical brief registered for Author Draft preparation.
- Reader-facing manuscript created: no.
- Canonical brief path: `editor/chapter-briefs/CHAPTER-007-every-state-has-one-owner.md`.
- Expected manuscript path reserved but not created:
  `book/02-the-laws/07-every-state-has-one-owner.md`.
- Index entity registration:
  - `id: CHAPTER-007`.
  - `type: chapter`.
  - `name: Every State Has One Owner`.
  - `path: ../book/02-the-laws/07-every-state-has-one-owner.md`.
  - `status: draft`.
- Exact Chapter 7 PEAK relationships registered:
  - `CHAPTER-007 illustrates LAW-001`.
  - `CHAPTER-007 illustrates SMELL-004`.
  - `CHAPTER-007 references ANTIPATTERN-003`.
  - `CHAPTER-007 references ARTIFACT-001`.
  - `CHAPTER-007 references ARTIFACT-005`.
  - `CHAPTER-007 references METRIC-003`.
- New PEAK concepts created: none.
- Changed files:
  - `editor/chapter-briefs/CHAPTER-007-every-state-has-one-owner.md`.
  - `knowledge/index.yaml`.
  - `editor/EDITOR_LOG.md`.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - `git status --short`: passed before edits with a clean working tree.
  - `git switch main`: passed; local `main` was up to date with `origin/main`.
  - `git pull --ff-only origin main`: passed; already up to date.
  - `git rev-parse HEAD`: returned `8b95decf73a2771268c885143564f0bb4c23bd0f`.
  - `git rev-parse origin/main`: returned `8b95decf73a2771268c885143564f0bb4c23bd0f`.
  - Pre-branch prerequisite checks: passed for Chapters 1-6 canonical status, Chapter 6 manuscript path, Chapter 6
    review and freeze history, Part II table-of-contents placement, `LAW-001` existence and name, absence of
    `CHAPTER-007`, absence of the Chapter 7 canonical brief, absence of the Chapter 7 reader-facing manuscript, absence
    of local and remote `chapter7` branches, absence of tracked `site/` output, supported relationship verbs, and clean
    working tree.
  - `git switch -c chapter7 origin/main`: passed.
  - Branch verification: passed; `chapter7` started at `8b95decf73a2771268c885143564f0bb4c23bd0f` with a clean working
    tree.
  - `git diff --check`: passed.
  - Direct YAML and file-boundary assertions: passed for exactly one `CHAPTER-007`, exact metadata, Chapters 1-6
    remaining canonical, exact six outgoing Chapter 7 relationships, target existence, duplicate-edge and self-edge
    checks, canonical brief existence, and reader-facing manuscript absence.
  - `npm.cmd run lint:md`: passed with 0 errors across 131 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 130 checked files.
  - `npm.cmd run lint:links`: passed; 130 links scanned successfully.
  - `vale --config .vale.ini editor/chapter-briefs/CHAPTER-007-every-state-has-one-owner.md editor/EDITOR_LOG.md`:
    passed with 0 errors, 0 warnings, and 0 suggestions after wording adjustments for Vale vocabulary.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
  - Manuscript absence check: passed; `book/02-the-laws/07-every-state-has-one-owner.md` does not exist.
- Next lifecycle stage: Author Draft after author approval.

## Phase 26 Chapter 7 Author Draft

- Chapter: Every State Has One Owner.
- Stable ID: `CHAPTER-007`.
- Branch: `chapter7`.
- Lifecycle stage: Author Draft.
- Starting HEAD for this authoring pass: `8b95a7b41b1e898d9923b0a30dcb2cbfa763b446`.
- Verified baseline `origin/main`: `8b95decf73a2771268c885143564f0bb4c23bd0f`.
- Canonical brief used: `editor/chapter-briefs/CHAPTER-007-every-state-has-one-owner.md`.
- Manuscript path created: `book/02-the-laws/07-every-state-has-one-owner.md`.
- Story used: industrial embedded controller with competing operational-mode authorities after watchdog reset,
  interrupted service, reconnect, and fixture retry.
- Engineering Principle used: For every meaningful state, name one authority that validates its value and controls its
  transitions; other components may request, observe, cache, persist, replicate, or derive that state, but they must not
  become competing sources of truth.
- Architecture Exercise used: Trace One State to One Owner.
- Principal's Notebook observations: exactly 3.
- Chapter-local ADR present: yes; `Make the Device Mode State Machine the Sole Authority for Operational Mode`.
- PEAK concepts used: `LAW-001`, `SMELL-004`, `ANTIPATTERN-003`, `ARTIFACT-001`, `ARTIFACT-005`, and `METRIC-003`.
- New PEAK concepts created: none.
- `knowledge/index.yaml` changed during Author Draft: no.
- Existing PEAK concept files changed during Author Draft: no.
- Canonical brief changed during Author Draft: no.
- `editor/CANON.md` changed during Author Draft: no.
- Frozen Chapters 1-6 changed during Author Draft: no.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - `git switch chapter7`: passed; branch was already tracking `origin/chapter7`.
  - `git status --short`: passed before editing with a clean working tree.
  - `git rev-parse HEAD`: passed and returned `8b95a7b41b1e898d9923b0a30dcb2cbfa763b446`.
  - `git rev-parse origin/chapter7`: passed and returned `8b95a7b41b1e898d9923b0a30dcb2cbfa763b446`.
  - `git merge-base HEAD origin/main`: passed and returned `8b95decf73a2771268c885143564f0bb4c23bd0f`.
  - Required preflight checks: passed for clean tree, `HEAD == origin/chapter7`, required starting commit, existing
    canonical brief, absent reader-facing manuscript, `CHAPTER-007` registered exactly once as `draft`, Chapters 1-6
    remaining `canonical`, and no unrelated local files.
  - Governing-material read: passed for root pointers, editor governance, source-of-truth policy, PEAK index and
    concept files, table of contents, canonical brief, template, and canonical Chapters 1-6.
  - Direct manuscript checks: passed for exact manuscript path, one H1, required H2 order, nonempty required sections,
    exact ADR section structure, exactly three Principal's Notebook observations, no `TODO`/`TBD`/`FIXME`/`AUTHOR NOTE`,
    no conflict markers, expected PEAK IDs only, and all required Chapter 7 PEAK IDs present.
  - Direct PEAK checks: passed; `CHAPTER-007` remained exactly one `draft` chapter and Chapters 1-6 remained
    `canonical`.
  - `npm.cmd run lint:md`: passed with 0 errors across 132 Markdown files.
  - Initial targeted Vale run failed on the spelling term `failover`; the manuscript text was revised to use
    `standby switch` and `controller handoff`.
  - `vale --config .vale.ini book/02-the-laws/07-every-state-has-one-owner.md editor/EDITOR_LOG.md`: passed after
    revision with 0 errors, 0 warnings, and 0 suggestions.
  - `git diff --check`: passed.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 131 checked files.
  - `npm.cmd run lint:links`: passed; 131 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
  - Protected-file checks: passed; the canonical brief, `knowledge/index.yaml`, `editor/CANON.md`, and Chapters 1-6
    were unchanged.
- Changed-file intent for this authoring pass: only the new Chapter 7 manuscript and this editor log entry.
- Next required stage: Editorial Review.

## Phase 27 Chapter 7 Editorial Review

- Chapter: Every State Has One Owner.
- Stable ID: `CHAPTER-007`.
- Branch: `chapter7`.
- Stage: Editorial Review.
- Reviewed Author Draft commit: `cc366a8979a931b26140975af638a0f96453e935`.
- Manuscript path: `book/02-the-laws/07-every-state-has-one-owner.md`.
- Canonical brief path: `editor/chapter-briefs/CHAPTER-007-every-state-has-one-owner.md`.
- Outcome: Approved with minor changes.
- Editorial areas reviewed: opening quote, operational-mode story, reset and interrupted-service sequence, local log
  evidence, synchronization-fix proposals, principal-engineer intervention, discussion flow, terminology consistency,
  repetition, Engineering Principle, Architecture Exercise, Principal's Notebook, ADR, Editor's Commentary, Chapter 4
  boundary, and later Part II boundaries.
- Material editorial changes made: reduced one inflated story sentence about logs, made the initial synchronization-fix
  transition clearer, removed one meta-manuscript sentence from the Discussion, narrowed the API-boundary transition, and
  tightened one coordination-cost paragraph.
- Structure result: passed; the manuscript keeps the required H2 order from `editor/CHAPTER_ARCHITECTURE.md`.
- Principal's Notebook count: passed; exactly three concise observations remain.
- Story result: passed; the reset sequence remains coherent and distinguishes runtime, persisted, cached, observed, and
  inferred mode representations.
- Editorial boundary result: passed; Chapter 4's outcome ownership is not duplicated, and later Part II laws retain their
  primary material.
- Canon and PEAK graph changed: no.
- Validation commands and actual results:
  - Gate baseline checks: passed; `git status --short` was clean before editing, `HEAD` and `origin/chapter7` were both
    `cc366a8979a931b26140975af638a0f96453e935`, and the reviewed Author Draft commit was present.
  - Direct lifecycle assertions: passed for required H2 order, no duplicate H2 sections, exactly three Principal's
    Notebook observations, no unresolved authoring markers, expected Chapter 7 PEAK IDs only, `CHAPTER-007` registered
    exactly once as `draft`, Chapters 1-6 remaining `canonical`, and changed files limited to the Chapter 7 manuscript
    plus this editor log.
  - `git diff --check`: passed.
  - Protected-file checks: passed; the canonical brief, `knowledge/index.yaml`, `editor/CANON.md`, and Chapters 1-6
    were unchanged.
  - `npm.cmd run lint:md`: passed with 0 errors across 132 Markdown files.
  - `vale --config .vale.ini book/02-the-laws/07-every-state-has-one-owner.md editor/EDITOR_LOG.md`: passed with 0
    errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 131 checked files.
  - `npm.cmd run lint:links`: passed; 131 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
- Next stage: Canon Review.

## Phase 28 Chapter 7 Canon Review

- Chapter: Every State Has One Owner.
- Stable ID: `CHAPTER-007`.
- Branch: `chapter7`.
- Stage: Canon Review.
- Reviewed Editorial Review commit: `71c44609febc9e3530e76eb93826ced50417fb47`.
- Manuscript path: `book/02-the-laws/07-every-state-has-one-owner.md`.
- Canonical brief path: `editor/chapter-briefs/CHAPTER-007-every-state-has-one-owner.md`.
- Outcome: Approved.
- Canon areas reviewed: central thesis, reader transformation, in-scope and out-of-scope boundaries, Chapters 1-6
  boundaries, later Part II boundaries, embedded-systems story shape, discussion arc, Engineering Principle,
  Architecture Exercise, chapter-local ADR, Principal's Notebook, PEAK concept map, and exact registered relationships.
- Canon result: passed; the chapter teaches one scoped authority for valid state values and transitions, not generic
  organizational ownership, storage location ownership, or a generic single-source-of-truth essay.
- PEAK relationship result: passed; `LAW-001`, `SMELL-004`, `ANTIPATTERN-003`, `ARTIFACT-001`, `ARTIFACT-005`, and
  `METRIC-003` are materially present in the manuscript and no optional supporting concept requires registration.
- Boundary result: passed; Chapter 4's responsibility-for-outcomes argument remains distinct, and Chapters 8-13 retain
  their primary API, dependency, time, flexibility, simplicity, and evidence material.
- Canonical brief changed: no.
- `knowledge/index.yaml` changed: no.
- Existing PEAK concept files changed: no.
- Manuscript changed during Canon Review: no.
- Validation commands and actual results:
  - Gate baseline checks: passed; `git fetch --all --prune` completed, `git status --short` was clean, and `HEAD` and
    `origin/chapter7` were both `71c44609febc9e3530e76eb93826ced50417fb47`.
  - Direct canon assertions: passed for required H2 order, exactly three Principal's Notebook observations, expected
    Chapter 7 PEAK IDs only, all registered Chapter 7 outgoing relationships matching the canonical brief, all target
    PEAK concepts existing, `CHAPTER-007` remaining exactly one `draft` chapter entry, and Chapters 1-6 remaining
    `canonical`.
  - `git diff --check`: passed.
  - Protected-file checks: passed; the canonical brief, `knowledge/index.yaml`, `editor/CANON.md`, existing PEAK concept
    files, and Chapters 1-6 were unchanged.
  - `npm.cmd run lint:md`: passed with 0 errors across 132 Markdown files.
  - `vale --config .vale.ini book/02-the-laws/07-every-state-has-one-owner.md editor/EDITOR_LOG.md`: passed with 0
    errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 131 checked files.
  - `npm.cmd run lint:links`: passed; 131 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
- Next stage: Technical Review.

## Phase 29 Chapter 7 Technical Review

- Chapter: Every State Has One Owner.
- Stable ID: `CHAPTER-007`.
- Branch: `chapter7`.
- Stage: Technical Review.
- Reviewed Canon Review commit: `1b0a51bd0d5e0e342465da41c7491621a31b7ad5`.
- Manuscript path: `book/02-the-laws/07-every-state-has-one-owner.md`.
- Outcome: Approved.
- Technical areas reviewed: watchdog reset behavior, startup recovery, runtime versus persisted operational mode,
  command acceptance and rejection, raw setters, stale observations, sequence and generation semantics, fixture
  privilege, supervisor inference, concurrency and serialization, ownership handoff, distributed-protocol caveats,
  transition logging, invalid-transition tests, and recovery after disagreement.
- Reset and recovery result: passed; the runtime owner re-establishes authority after watchdog recovery, consults only
  trusted persisted inputs, rejects commands until invariants hold, and avoids merging stale guesses into truth.
- Runtime and persistence result: passed; persistence is treated as input, policy, or history rather than current runtime
  authority.
- Command semantics result: passed; intent-level commands carry requested outcomes and allow the owner to accept, reject,
  publish, and explain transitions.
- Stale-observation result: passed; sequence number, reset generation, version, or transition identity is used where
  observers need to detect stale values.
- Privilege and handoff result: passed; fixture privilege is routed through bounded commands, and ownership transfer is
  scoped, explicit, ordered, and mutually exclusive.
- Technical overstatement result: passed; the chapter does not claim that one owner means one copy, one thread, one
  database, no concurrency, no replication, or no distributed authority where a real distributed protocol is required.
- Manuscript changed during Technical Review: no.
- Canon and PEAK graph changed: no.
- Validation commands and actual results:
  - Gate baseline checks: passed; `git fetch --all --prune` completed, `git status --short` was clean, and `HEAD` and
    `origin/chapter7` were both `1b0a51bd0d5e0e342465da41c7491621a31b7ad5`.
  - Direct technical assertions: passed for required technical topics, forbidden overstatements absent, expected Chapter
    7 PEAK IDs only, registered Chapter 7 outgoing relationships unchanged, `CHAPTER-007` remaining `draft`, and
    Chapters 1-6 remaining `canonical`.
  - `git diff --check`: passed.
  - Protected-file checks: passed; the manuscript, canonical brief, `knowledge/index.yaml`, `editor/CANON.md`, existing
    PEAK concept files, and Chapters 1-6 were unchanged.
  - `npm.cmd run lint:md`: passed with 0 errors across 132 Markdown files.
  - `vale --config .vale.ini book/02-the-laws/07-every-state-has-one-owner.md editor/EDITOR_LOG.md`: passed with 0
    errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 131 checked files.
  - `npm.cmd run lint:links`: passed; 131 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
- Next stage: Freeze Review.

## Phase 30 Chapter 7 Freeze Review

- Chapter: Every State Has One Owner.
- Stable ID: `CHAPTER-007`.
- Branch: `chapter7`.
- Stage: Freeze Review.
- Reviewed Technical Review commit: `fb7ca148a2f45fdb2ec898a2ad25500e2db6277d`.
- Manuscript path: `book/02-the-laws/07-every-state-has-one-owner.md`.
- Canonical brief path: `editor/chapter-briefs/CHAPTER-007-every-state-has-one-owner.md`.
- Outcome: Approved.
- Freeze result: Chapter 7 is canonical-ready and now registered as `canonical` in `knowledge/index.yaml`.
- Manuscript architecture result: passed; the chapter keeps the required H2 order and complete chapter sections.
- Principal's Notebook result: passed; exactly three short observations remain.
- Canon result: passed; the chapter opens Part II by teaching `LAW-001` without creating a new artifact, vocabulary term,
  law, smell, anti-pattern, metric, ritual, or failure story.
- PEAK graph result: passed; the registered outgoing Chapter 7 relationships remain unchanged.
- Boundary result: passed; Chapters 1-6 remain frozen/canonical and unchanged, and later Part II material remains
  reserved for later chapters.
- Reader-facing manuscript changed during Freeze Review: no.
- Canonical brief changed during Freeze Review: no.
- `knowledge/index.yaml` changed during Freeze Review: yes; `CHAPTER-007` status changed from `draft` to `canonical`.
- Validation commands and actual results:
  - Gate baseline checks: passed; `git fetch --all --prune` completed, `git status --short` was clean, and `HEAD` and
    `origin/chapter7` were both `fb7ca148a2f45fdb2ec898a2ad25500e2db6277d`.
  - Direct freeze assertions: passed for required H2 order, complete lifecycle log entries for Editorial, Canon,
    Technical, and Freeze Review, exactly three Principal's Notebook observations, expected Chapter 7 PEAK IDs only,
    registered Chapter 7 outgoing relationships unchanged, all relationship targets existing, `CHAPTER-007` registered
    exactly once as `canonical`, and Chapters 1-6 remaining `canonical`.
  - `git diff --check`: passed.
  - Protected-file checks: passed; the manuscript, canonical brief, `editor/CANON.md`, existing PEAK concept files, and
    Chapters 1-6 were unchanged.
  - `npm.cmd run lint:md`: passed with 0 errors across 132 Markdown files.
  - `vale --config .vale.ini book/02-the-laws/07-every-state-has-one-owner.md editor/EDITOR_LOG.md`: passed with 0
    errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 131 checked files.
  - `npm.cmd run lint:links`: passed; 131 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
- Next action: Open a Chapter 7 pull request; do not merge in this workflow.

## Phase 31 Chapter 8 Canonical Brief Registration

- Chapter: Every API Is a Promise.
- Stable ID: `CHAPTER-008`.
- Branch: `chapter8`.
- Lifecycle stage: Canonical brief registration.
- Verified baseline `origin/main`: `0776ab64b48d4e36a9b952964ab5739b9eaf55d2`.
- Baseline meaning: Chapter 7 merge commit, `Chapter 7: Every State Has One Owner (#9)`.
- Chapter 7 merge and lifecycle confirmation: passed; Chapter 7 exists, `CHAPTER-007` is registered as `canonical`, and
  Editorial, Canon, Technical, and Freeze Review entries are present in order.
- Canonical brief created: `editor/chapter-briefs/CHAPTER-008-every-api-is-a-promise.md`.
- Reader-facing manuscript created: no.
- Index registration: `CHAPTER-008` added as `draft` at `book/02-the-laws/08-every-api-is-a-promise.md`.
- Primary law: `LAW-002` - Every API Is a Promise.
- Exact outgoing relationships registered:
  - `CHAPTER-008 illustrates LAW-002`.
  - `CHAPTER-008 illustrates SMELL-001`.
  - `CHAPTER-008 references METRIC-004`.
  - `CHAPTER-008 references ARTIFACT-001`.
  - `CHAPTER-008 references METRIC-003`.
  - `CHAPTER-008 references VOCAB-001`.
- Concepts selected: `LAW-002`, `SMELL-001`, `METRIC-004`, `ARTIFACT-001`, `METRIC-003`, and `VOCAB-001`.
- Concepts considered but not registered for Chapter 8: `ARTIFACT-002`, `ARTIFACT-005`, `RITUAL-001`, `FAILURE-002`,
  `LAW-001`, `LAW-003`, `ANTIPATTERN-005`, and `ANTIPATTERN-002`.
- New PEAK concepts created: none.
- Changed-file intent: only the Chapter 8 canonical brief, `knowledge/index.yaml`, and this editor log entry.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - `git status --short`: passed before branch creation with a clean working tree.
  - `git switch main`: passed; local `main` was already current.
  - `git pull --ff-only origin main`: passed; already up to date.
  - `git rev-parse HEAD`: returned `0776ab64b48d4e36a9b952964ab5739b9eaf55d2`.
  - `git rev-parse origin/main`: returned `0776ab64b48d4e36a9b952964ab5739b9eaf55d2`.
  - Pre-branch prerequisite checks: passed for clean tree, `HEAD == origin/main`, Chapter 7 merge commit presence,
    Chapter 7 manuscript presence, Chapter 7 canonical status, Chapter 7 review history, absent `CHAPTER-008`, absent
    Chapter 8 brief, absent Chapter 8 manuscript, absent local and remote `chapter8` branches, and no tracked `site/`
    output.
  - `git switch -c chapter8 origin/main`: passed.
  - Branch verification: passed; `chapter8` started at `0776ab64b48d4e36a9b952964ab5739b9eaf55d2` with a clean working
    tree.
  - Direct YAML and file-boundary assertions: passed for exactly one `CHAPTER-008`, exact metadata, `draft` status,
    Chapters 1-7 remaining `canonical`, exact six outgoing Chapter 8 relationships, relationship target existence,
    duplicate-edge and self-edge checks, canonical brief existence, manuscript absence, no new PEAK ID except
    `CHAPTER-008`, no tracked `site/` output, and changed files limited to expected registration files.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 133 Markdown files.
  - Initial targeted Vale and spelling runs failed on wording not present in the local dictionaries; the brief was
    revised to use repository-friendly wording such as `retry behavior`, `repeated-call behavior`, and `asynchronous`.
  - `vale --config .vale.ini editor/chapter-briefs/CHAPTER-008-every-api-is-a-promise.md editor/EDITOR_LOG.md`: passed
    after revision with 0 errors, 0 warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed after revision with 0 spelling issues across 132 checked files.
  - `npm.cmd run lint:links`: passed; 132 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
- Next lifecycle stage: Author Draft after author approval.

## Phase 32 Chapter 8 Author Draft

- Chapter: Every API Is a Promise.
- Stable ID: `CHAPTER-008`.
- Branch: `chapter8`.
- Lifecycle stage: Author Draft.
- Starting HEAD for this authoring pass: `c2a31ff6e1c2e694e70468d821118d002f65eca7`.
- Verified baseline `origin/main`: `0776ab64b48d4e36a9b952964ab5739b9eaf55d2`.
- Canonical brief used: `editor/chapter-briefs/CHAPTER-008-every-api-is-a-promise.md`.
- Manuscript path created: `book/02-the-laws/08-every-api-is-a-promise.md`.
- Story used: firmware radio service API `radio_set_channel(uint8_t channel)` whose unchanged signature hid a change
  from blocking hardware completion to queued request acceptance.
- Engineering Principle used: Treat every observable boundary as a contract; specify what consumers may rely on,
  preserve those promises deliberately, and make incompatible change explicit instead of hiding it behind an unchanged
  interface.
- Architecture Exercise used: Write the Promise Behind One API.
- Principal's Notebook observations: exactly 3.
- Chapter-local ADR present: yes; `Separate Channel-Change Acceptance from Completion`.
- PEAK concepts used: `LAW-002`, `SMELL-001`, `METRIC-004`, `ARTIFACT-001`, `METRIC-003`, and `VOCAB-001`.
- New PEAK concepts created: none.
- PEAK relationships changed during Author Draft: no.
- `knowledge/index.yaml` changed during Author Draft: no.
- Canonical brief changed during Author Draft: no.
- Existing PEAK concept files changed during Author Draft: no.
- Chapters 1-7 changed during Author Draft: no.
- Validation commands and actual results:
  - `git fetch --all --prune`: passed.
  - `git switch chapter8`: passed; branch was already current.
  - `git status --short`: passed before editing with a clean working tree.
  - `git rev-parse HEAD`: returned `c2a31ff6e1c2e694e70468d821118d002f65eca7`.
  - `git rev-parse origin/chapter8`: returned `c2a31ff6e1c2e694e70468d821118d002f65eca7`.
  - `git rev-parse origin/main`: returned `0776ab64b48d4e36a9b952964ab5739b9eaf55d2`.
  - Required preflight checks: passed for clean tree, `HEAD == origin/chapter8`, expected brief-registration commit
    subject, existing canonical brief, absent reader-facing manuscript, `CHAPTER-008` registered exactly once as
    `draft`, Chapters 1-7 remaining `canonical`, and no prior Chapter 8 Author Draft or review entry.
  - Governing-material read: passed for editor governance, source-of-truth policy, PEAK index and registered concepts,
    table of contents, Chapter 8 canonical brief, Chapter 7, current chapter template, and Author Draft precedent.
  - Direct manuscript checks: passed for exact manuscript path, one H1, required H2 order, nonempty required sections,
    exactly three Principal's Notebook observations, no `TODO`/`FIXME`/`AUTHOR NOTE`, no conflict markers, expected
    Chapter 8 PEAK IDs only, and all registered Chapter 8 PEAK IDs present.
  - Direct PEAK checks: passed; `CHAPTER-008` remained exactly one `draft` chapter and Chapters 1-7 remained
    `canonical`.
  - `git diff --check`: passed.
  - `npm.cmd run lint:md`: passed with 0 errors across 134 Markdown files.
  - Initial targeted Vale and spelling runs failed on a bootloader wording; the manuscript text was revised to use
    `bootloader code`.
  - `vale --config .vale.ini book/02-the-laws/08-every-api-is-a-promise.md`: passed after revision with 0 errors, 0
    warnings, and 0 suggestions.
  - `npm.cmd run lint:spelling`: passed after revision with 0 spelling issues across 133 checked files.
  - `npm.cmd run lint:links`: passed; 133 links scanned successfully.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
  - Protected-file checks: passed; the canonical brief, `knowledge/index.yaml`, existing PEAK concept files, and
    Chapters 1-7 were unchanged.
- Changed-file intent for this authoring pass: only the new Chapter 8 manuscript and this editor log entry.
- Next required stage: Editorial Review.

## Phase 33 Chapter 8 Editorial Review

- Chapter: Every API Is a Promise.
- Stable ID: `CHAPTER-008`.
- Branch: `chapter8`.
- Stage: Editorial Review.
- Reviewed Author Draft commit: `6586435c730f787c24f944911948750a18bb4daa`.
- Manuscript path: `book/02-the-laws/08-every-api-is-a-promise.md`.
- Canonical brief path: `editor/chapter-briefs/CHAPTER-008-every-api-is-a-promise.md`.
- Outcome: Approve with changes.
- Editorial areas reviewed: opening quote, radio-channel story, synchronous completion versus asynchronous acceptance,
  unchanged signature versus changed promise, local-fix proposals, principal-engineer intervention, discussion flow,
  terminology consistency, internal API compatibility cost, compatibility dimensions, Engineering Principle,
  Architecture Exercise, Principal's Notebook, ADR, Editor's Commentary, Chapter 7 boundary, and later Part II
  boundaries.
- Material editorial changes made: clarified that the service application reported the displayed channel value, replaced
  a UI reference with service-application wording, tightened one story transition, softened a compatibility-evolution
  sentence, clarified the undocumented-behavior paragraph, and repaired one awkward line break in the internal-API cost
  discussion.
- Structure result: passed; the manuscript keeps the required H2 order from `editor/CHAPTER_ARCHITECTURE.md`.
- Principal's Notebook count: passed; exactly three concise observations remain.
- Story result: passed; the radio-channel story concretely shows an unchanged `radio_set_channel(uint8_t channel)`
  signature hiding a change from blocking hardware completion to queued request acceptance.
- Editorial boundary result: passed; Chapter 7 state ownership is not retold, and later dependency, time, flexibility,
  simplicity, evidence, boundary-design, release, and migration material remains reserved for later chapters.
- Canon and PEAK graph changed: no.
- Validation commands and actual results:
  - Gate baseline checks: passed; `git fetch --all --prune` completed, `git status --short` was clean, and `HEAD` and
    `origin/chapter8` were both `6586435c730f787c24f944911948750a18bb4daa`.
  - Direct editorial assertions: passed for required H2 order, unique mandatory sections, exactly three Principal's
    Notebook observations, no unresolved authoring markers, expected Chapter 8 PEAK IDs only, `CHAPTER-008` registered
    exactly once as `draft`, and changed files limited to the Chapter 8 manuscript before this log entry.
  - `git diff --check`: passed.
  - `vale --config .vale.ini book/02-the-laws/08-every-api-is-a-promise.md`: passed with 0 errors, 0 warnings, and 0
    suggestions.
  - `npm.cmd run lint:md`: passed with 0 errors across 134 Markdown files.
  - `npm.cmd run lint:spelling`: passed with 0 spelling issues across 133 checked files.
  - `npm.cmd run lint:links`: passed after rerun outside the sandbox; 133 links scanned successfully. The first sandbox
    run used an incorrect sandbox working directory and returned 0 glob results.
  - `python -m pip check`: passed; no broken requirements found.
  - `python -m mkdocs build --strict`: passed.
  - `git ls-files site`: passed; no generated `site/` output is tracked.
- Next stage: Canon Review.
