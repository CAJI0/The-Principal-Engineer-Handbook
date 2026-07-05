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
