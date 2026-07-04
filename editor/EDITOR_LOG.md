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
- Chapter-local ADR result: clearly reader-facing, locally scoped, unregistered, and structurally consistent.
- Chapter 1 continuity result: Chapter 2 builds on future system cost and decision discipline without reopening or
  contradicting Chapter 1.
- Unresolved canon issues: none.
- Unresolved `AUTHOR NOTE` items: none.
- Chapter 1 remains Frozen and canonical.
- Technical Review has not been performed.
- Freeze Review has not been performed.
- Branch merged: no.
