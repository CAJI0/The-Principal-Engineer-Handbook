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
