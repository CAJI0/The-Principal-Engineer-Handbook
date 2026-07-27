# CHAPTER-037 Canonical Brief: Refactoring Without Losing Product Trust

## 1. Metadata

- Stable ID: `CHAPTER-037`.
- Title: `Refactoring Without Losing Product Trust`.
- Part: Part VI - Legacy.
- Chapter number: 37.
- Expected manuscript path:
  `book/06-legacy/37-refactoring-without-losing-product-trust.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-037-refactoring-without-losing-product-trust.md`.
- Branch: `chapter37`.
- Verified baseline `origin/main`: `f0c14c968e85ad777f5991425e641c9ce02163fa`.
- Baseline evidence: PR #38 Chapter 36 squash merge commit, `Chapter 36: Deleting Safely`.
- Canonical predecessor: `CHAPTER-036` - Deleting Safely.
- Part position: sixth and final chapter of Part VI - Legacy.
- Book position: final reader-facing main chapter before the Appendix.
- Reader-facing draft created: no.
- Expected lifecycle status after registration: `draft`.
- Primary concept: none. Chapter 37 is a capstone practice chapter and must not add a `primary_concept` registry field.
- Central practice: trust-preserving refactoring.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `f0c14c968e85ad777f5991425e641c9ce02163fa`.
- That baseline is the PR #38 Chapter 36 squash merge commit, `Chapter 36: Deleting Safely`.
- The baseline contains the Chapter 36 manuscript, canonical brief, editor log, and index updates.
- `CHAPTER-036` is registered as `canonical` in `knowledge/index.yaml`.
- `book/06-legacy/36-deleting-safely.md` exists on `origin/main`.
- `CHAPTER-001` through `CHAPTER-036` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-037` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 37 canonical brief or reader-facing manuscript existed before this registration.
- No previous editor log entry recorded Chapter 37 Canonical Brief Registration.
- The Part VI table of contents order is Reading a Legacy System, Finding Silent Coupling, Managing Utility Gravity,
  Reducing Boolean Explosion, Deleting Safely, and Refactoring Without Losing Product Trust.
- `book/06-legacy/README.md` remains intentionally minimal and still contains its section-level author note.
- No tracked `site/` output existed before this registration.
- The PEAK graph already contains the laws, metrics, records, rituals, smells, anti-patterns, and failure stories
  needed for the chapter. No Product Trust, Trust-Preserving Refactoring, Legacy Refactoring, Refactoring Safety, or
  Product Trust Surface concept is required.

## 3. Chapter Role in the Book

Chapter 37 closes Part VI and the main reader-facing chapter sequence of the handbook. The preceding Legacy chapters
teach the reader to understand a legacy system, find hidden dependents, map shared-helper responsibility, reduce product
state complexity, and delete old behavior safely. Chapter 37 turns those inputs into structural change while preserving
product trust.

The chapter should teach refactoring as a product-trust exercise, not only a code-structure exercise. A cleaner design
that surprises users, support, manufacturing, operations, release owners, or downstream teams is not successful yet.
The Principal Engineer's responsibility is to change the system's future change cost while keeping current product
promises intact.

## 4. Reader Problem

The reader may enter the chapter believing refactoring succeeds when the code becomes cleaner, dependency direction
looks better, boundaries are more elegant, or a legacy subsystem is moved behind a modern interface. In a product system,
that is not enough.

Legacy refactoring can break trust without breaking local tests. It can change diagnostics, timing, service-tool flows,
manufacturing scripts, dashboards, event meaning, release sequencing, upgrade behavior, support knowledge, rollback
expectations, ownership, and the organization's ability to understand what changed.

The reader needs a way to refactor without turning structural improvement into product surprise.

## 5. Core Promise

Prepare the future manuscript to teach this core stance:

> Refactoring is only successful when the product remains trustworthy while the system becomes easier to change.

The chapter should move the reader away from asking:

> How do we make this code cleaner?

to asking:

> Which product promises must remain trustworthy while the structure changes, and how will we prove that they did?

## 6. Primary-Concept Resolution

Chapter 37 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Chapter 37 is a capstone
practice chapter. It references existing canon rather than illustrating one central PEAK smell, ritual, law, artifact,
metric, vocabulary term, anti-pattern, or failure story.

Trust-preserving refactoring, product trust, trust surface, refactoring map, migration slice, compatibility seam,
strangler path, branch-by-abstraction, shadow path, dual write, rollback proof, recovery proof, and trust erosion signal
remain chapter-local prose. Do not create a new PEAK concept, ID, artifact, ritual, metric, smell, anti-pattern, failure
story, vocabulary term, relationship verb, or primary-concept field for them.

## 7. Central Practice

Trust-preserving refactoring means changing structure, boundaries, ownership, dependency direction, state placement,
APIs, configuration models, event flows, utility boundaries, timing paths, and operational workflows while users and
the organization can still trust the product.

The practice starts with the product promise being protected, not the code shape being disliked. It uses evidence from
Chapters 32 through 36, stages movement in small observable steps, records trade-offs, preserves external promises while
internal structure changes, and proves that the system is easier to change afterward.

## 8. Reader Transformation

Before the chapter, the reader may think:

1. refactoring is safe when behavior-preserving tests pass;
2. a cleaner internal boundary is the main success criterion;
3. users and support do not care about internal structure;
4. a big-bang rewrite may be the fastest way out of legacy constraints;
5. adapters, seams, shadow paths, and compatibility layers are merely tactical code patterns;
6. product trust is protected by rollback alone;
7. service tools, manufacturing scripts, dashboards, operational guides, and release notes are outside the refactor;
8. preserving behavior means preserving every implementation accident;
9. the refactor is done when the old code is gone;
10. unresolved risks can be handled by the next team after the cleanup lands.

By the end of the chapter, the reader should be able to:

1. start from the product promise being protected;
2. name the refactoring target: boundary, dependency direction, ownership, API, state placement, configuration model,
   event flow, utility extraction, timing path, or operational workflow;
3. identify who can lose trust: users, customer teams, support, manufacturing, service, operations, release managers,
   downstream teams, and future maintainers;
4. separate product behavior, operational behavior, internal structure, and organizational memory;
5. build a refactoring map from evidence gathered in Chapters 32 through 36;
6. preserve external promises while changing internal structure;
7. use characterization tests, contract tests, observability, field telemetry, logs, release checks, service-tool checks,
   and upgrade-path validation;
8. choose small, reversible, observable steps with explicit rollback or recovery;
9. record decisions through ADRs, RFCs, Decision Journal entries, Architecture Ledgers, and Architecture Review notes;
10. close the refactor by proving the system is easier to change, not merely cleaner to read.

## 9. Non-Goals

Chapter 37 is not:

- a generic refactoring catalog;
- a rewrite recommendation;
- a clean-code chapter;
- a pattern catalog;
- a testing-only chapter;
- a migration-only chapter;
- a strangler-fig tutorial;
- a feature-flag playbook;
- a performance optimization chapter;
- a management alignment chapter;
- a chapter about deleting old code; Chapter 36 owns deletion safety;
- a claim that all legacy systems can become clean quickly;
- a claim that internal structure matters more than product trust.

## 10. Boundaries With Chapters 32-36

- Chapter 32 owns reading the legacy system before the first change. Chapter 37 may use reading maps as input, but it
  must not reteach legacy reading.
- Chapter 33 owns finding Silent Coupling. Chapter 37 may refactor after hidden dependents are named, but it must not
  become the coupling-discovery chapter.
- Chapter 34 owns Utility Gravity. Chapter 37 may move utility responsibility after utility promises and consumers are
  visible, but it must not become the shared-helper mapping chapter.
- Chapter 35 owns Boolean Explosion and state-space reduction. Chapter 37 may migrate from scattered switches toward a
  clearer state model, but it must not teach state-space classification.
- Chapter 36 owns Deleting Safely. Chapter 37 may decide what to leave alone, what to freeze, and what to delete later,
  but it must not teach deletion evidence or Deletion Day.

Chapter 37 should use the outputs of Chapters 32 through 36: reading maps, silent-dependency findings, utility maps,
state-space classifications, deletion evidence, ownership records, and architecture health findings.

## 11. Boundaries With Earlier Parts I-V

Use earlier canon as supporting material without rewriting those chapters:

- Part I supplies judgment, evidence, ownership, better questions, and stewardship.
- Part II supplies state ownership, API promises, dependencies, time, simplicity, unused flexibility, and evidence.
- Part III supplies boundaries, Change Radius, failure and recovery, ADR/RFC discipline, Architecture Reviews, and
  Architecture Freeze.
- Part IV supplies product reality: manufacturing, field constraints, variants, observability, releases, upgrade paths,
  diagnostics, and supportability.
- Part V supplies leadership, review memory, rituals, mentoring through artifacts, team alignment, and Architecture
  Health Reviews.

Chapter 37 should apply those ideas as constraints for a final legacy refactoring practice. It must not recap the whole
book.

## 12. Selected PEAK Concepts

- `LAW-001` - Every State Has One Owner: material because refactoring often moves state placement, authority, repair
  paths, and ownership.
- `LAW-002` - Every API Is a Promise: material because APIs, diagnostics, events, tools, and operational surfaces must
  keep their trusted meaning while internals change.
- `LAW-003` - Time Is a Dependency: material because rollout order, upgrade windows, shadow paths, dual operation,
  timing behavior, and recovery windows shape safe refactoring.
- `LAW-004` - Simplicity Is a Feature: material because the refactor should reduce future change cost without
  surprising the product.
- `LAW-005` - Evidence Before Confidence: material because structural confidence is not enough without behavior,
  operational, and release evidence.
- `LAW-006` - Unused Flexibility Is Waste: material because compatibility layers, adapters, and temporary seams need
  retirement triggers.
- `LAW-007` - Every Dependency Is a Decision: material because refactoring changes dependency direction, ownership
  obligations, and replacement costs.
- `VOCAB-001` and `METRIC-001` - Change Radius: material for sizing the affected product and organizational surface.
- `METRIC-002` - Bus Factor: material because refactoring should reduce dependence on expert memory.
- `METRIC-003` - Discoverability: material because the new structure must be easier for future engineers to understand.
- `METRIC-004` - API Stability: material because consumers must still trust boundary behavior.
- `METRIC-005` - Architecture Health: material because the chapter closes Part VI by feeding unresolved refactoring risk
  back into health review.
- `ARTIFACT-001` - ADR: material for consequential structural choices.
- `ARTIFACT-002` - RFC: material when cross-team refactoring needs proposal review.
- `ARTIFACT-003` - Decision Journal: material for smaller assumptions, trade-offs, and follow-up decisions.
- `ARTIFACT-004` - Mistake Ledger: material when a prior migration, release, or refactor failure should inform the plan.
- `ARTIFACT-005` - Event Catalog: material when event flows, diagnostics, or dashboards change meaning.
- `ARTIFACT-006` - Architecture Ledger: material for owners, consumers, risk, evidence, and revisit triggers.
- `RITUAL-001` - Architecture Review: material for reviewing cross-boundary movement before it hardens.
- `RITUAL-002` - Architecture Freeze: material for deciding what becomes stable during a staged refactor.
- `RITUAL-004` - Architecture Health Review: material for recurring legacy areas that remain risky after the refactor.
- `SMELL-001` - Silent Coupling: material because refactoring must preserve or make explicit hidden dependents.
- `SMELL-002` - Utility Gravity: material because utility responsibility often needs trust-preserving movement.
- `SMELL-003` - Boolean Explosion: material because state-space complexity often motivates refactoring.
- `SMELL-004` - Hidden State: material because moving state can break product behavior unless authority is explicit.
- `SMELL-005` - Platform Leakage: material because refactoring may restore or redefine platform boundaries.
- `SMELL-006` - Event Explosion: material because event and diagnostic flows often change during refactoring.
- `ANTIPATTERN-001` - God Module: material because large responsibility centers are common refactoring targets.
- `ANTIPATTERN-002` - HAL Everywhere: material because embedded refactoring often reclaims hardware abstraction
  boundaries.
- `ANTIPATTERN-003` - Global Configuration: material because configuration ownership and meaning may need migration.
- `ANTIPATTERN-006` - Temporary Solution: material because seams and compatibility layers must not become permanent
  architecture by accident.
- `FAILURE-003` - The Successful Prototype: material because refactoring often repairs prototype-era structure.
- `FAILURE-004` - The Hero Engineer: material because refactoring should reduce single-expert dependence.
- `FAILURE-005` - The Release We Should Have Delayed: material because rushed structural change can break product
  trust.

## 13. Rejected and Intentionally Avoided PEAK Concepts

- `RITUAL-003` and `VOCAB-005` - Deletion Day: Chapter 36 owns deletion safety. Chapter 37 may reference deletion as an
  input or later outcome but should not center Deletion Day.
- `RITUAL-005` - Architecture Court and `RITUAL-006` - RFC Friday: existing rituals, but not central to
  trust-preserving refactoring.
- `ANTIPATTERN-004` - Manager Mania and `ANTIPATTERN-005` - Callback Hell: possible local examples, but not material to
  the chapter's canonical relationship set.
- `ARTIFACT-007` - Weak Signal Register: useful for health sensing, but Chapter 37 uses Architecture Health Review and
  concrete refactoring evidence instead.
- `VOCAB-002` - Weak Signal and `VOCAB-006` through `VOCAB-010`: useful prior vocabulary, but the final chapter should
  not recenter weak signals, Architecture Freeze, Architecture Health, Silent Coupling, Utility Gravity, or Boolean
  Explosion as its own topic.
- No candidate relationship from the approved set was omitted. The final chapter is intentionally broad because it is a
  capstone practice, but every selected target is tied to preserving product trust during structural change.
- No new PEAK concept, relationship verb, primary-concept field, artifact, ritual, metric, smell, anti-pattern,
  vocabulary term, law, or failure story should be introduced.

## 14. Outgoing Relationship Set

```yaml
- from: CHAPTER-037
  type: references
  to: LAW-001
- from: CHAPTER-037
  type: references
  to: LAW-002
- from: CHAPTER-037
  type: references
  to: LAW-003
- from: CHAPTER-037
  type: references
  to: LAW-004
- from: CHAPTER-037
  type: references
  to: LAW-005
- from: CHAPTER-037
  type: references
  to: LAW-006
- from: CHAPTER-037
  type: references
  to: LAW-007
- from: CHAPTER-037
  type: references
  to: VOCAB-001
- from: CHAPTER-037
  type: references
  to: METRIC-001
- from: CHAPTER-037
  type: references
  to: METRIC-002
- from: CHAPTER-037
  type: references
  to: METRIC-003
- from: CHAPTER-037
  type: references
  to: METRIC-004
- from: CHAPTER-037
  type: references
  to: METRIC-005
- from: CHAPTER-037
  type: references
  to: ARTIFACT-001
- from: CHAPTER-037
  type: references
  to: ARTIFACT-002
- from: CHAPTER-037
  type: references
  to: ARTIFACT-003
- from: CHAPTER-037
  type: references
  to: ARTIFACT-004
- from: CHAPTER-037
  type: references
  to: ARTIFACT-005
- from: CHAPTER-037
  type: references
  to: ARTIFACT-006
- from: CHAPTER-037
  type: references
  to: RITUAL-001
- from: CHAPTER-037
  type: references
  to: RITUAL-002
- from: CHAPTER-037
  type: references
  to: RITUAL-004
- from: CHAPTER-037
  type: references
  to: SMELL-001
- from: CHAPTER-037
  type: references
  to: SMELL-002
- from: CHAPTER-037
  type: references
  to: SMELL-003
- from: CHAPTER-037
  type: references
  to: SMELL-004
- from: CHAPTER-037
  type: references
  to: SMELL-005
- from: CHAPTER-037
  type: references
  to: SMELL-006
- from: CHAPTER-037
  type: references
  to: ANTIPATTERN-001
- from: CHAPTER-037
  type: references
  to: ANTIPATTERN-002
- from: CHAPTER-037
  type: references
  to: ANTIPATTERN-003
- from: CHAPTER-037
  type: references
  to: ANTIPATTERN-006
- from: CHAPTER-037
  type: references
  to: FAILURE-003
- from: CHAPTER-037
  type: references
  to: FAILURE-004
- from: CHAPTER-037
  type: references
  to: FAILURE-005
```

### Valid Relationship Verbs

The registered relationships use only `references`, a valid PEAK relationship type in `editor/KNOWLEDGE_MODEL.md` and
the existing chapter graph. `illustrates` is intentionally avoided because Chapter 37 does not introduce or centrally
illustrate one existing PEAK concept. It is a capstone practice chapter.

### No-New-Concept Result

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, vocabulary concept, ID,
relationship verb, or primary-concept field is required.

## 15. Story Target

Use:

`The Refactor That Was Technically Right and Operationally Wrong`

The future story should show a legacy system where a technically clean refactor changes structure correctly but breaks
product trust because it misses a promise outside the code. The missed promise may live in support diagnostics, field
upgrade behavior, manufacturing scripts, service tools, dashboards, logs, customer workflows, timing behavior,
deployment sequencing, or release rollback expectations.

The Principal Engineer should not respond by banning refactoring or demanding a rewrite. They rebuild the plan from
product promises, evidence, owners, compatibility boundaries, observable slices, rollback and recovery paths, record
updates, and review checkpoints. The story should end with a system that is easier to change and still trusted by the
product surfaces that depend on it.

## 16. Draft Constraints for the Future Author Draft

The Author Draft should be accepted only if it:

1. creates `book/06-legacy/37-refactoring-without-losing-product-trust.md`;
2. preserves this canonical brief unchanged unless a later prompt explicitly authorizes brief revision;
3. keeps `CHAPTER-037` as `draft` until freeze;
4. does not add a `primary_concept` field;
5. does not create new PEAK concepts or relationship verbs;
6. frames refactoring as a product trust exercise, not a code-structure exercise only;
7. starts from protected product promises rather than disliked code shape;
8. uses Chapters 32 through 36 as inputs without reteaching them;
9. includes the story target, engineering principle, architecture exercise, chapter-local ADR target, and exactly three
   Principal's Notebook observations;
10. covers evidence, owners, boundaries, staged movement, observability, rollback, recovery, records, and review
    checkpoints;
11. avoids big-bang rewrite framing as the default posture;
12. closes Part VI and the main chapter sequence without starting appendix content;
13. does not modify Chapters 1-36.

## 17. Part VI Closure Role

Chapter 37 should close Part VI by showing how the prior legacy practices combine into responsible structural change.
The reader has learned to read the system, find hidden dependents, map utility responsibility, name product states, and
delete safely. The final move is to refactor where product trust can survive the change.

The chapter should avoid pretending that every legacy system can become clean quickly. It should teach durable judgment
under real constraints: some behavior should be preserved, some should be migrated, some should be deleted later, some
should be frozen during the change, and some should be left alone until evidence improves.

## 18. Final-Main-Chapter Closure Constraints

Because Chapter 37 is the final main chapter before the Appendix, it should close the handbook with the idea that
Principal Engineering is not purity. It is durable judgment under real constraints.

The future manuscript should not introduce a new book-wide framework in the final chapter. It should synthesize prior
canon through one trust-preserving refactoring practice and leave the reader with a practical closing standard:

> Make the system easier to change without making the product harder to trust.

This line is chapter-local prose, not a new PEAK concept.

## 19. Engineering Principle Target

The future chapter should include a principle close to:

> Refactor from the product promise inward.

The principle should say that a Principal Engineer names the promise, owners, dependents, evidence, staged movement,
rollback path, recovery path, records, and review checkpoints before moving structure across a trusted boundary.

## 20. Architecture Exercise Target

Use an exercise close to:

`Plan a Trust-Preserving Refactor`

Ask the reader to choose one legacy refactoring target and produce:

1. the product promise that must remain trustworthy;
2. the structural target: boundary, dependency direction, ownership, API, state placement, configuration model, event
   flow, utility extraction, timing path, or operational workflow;
3. the surfaces that can lose trust;
4. the evidence from reading, coupling, utility, state-space, and deletion work;
5. the tests, telemetry, logs, service-tool checks, manufacturing checks, release checks, and support checks that prove
   behavior still holds;
6. the staged movement plan with rollback and recovery;
7. the records and dashboards to update;
8. the review checkpoint and freeze point;
9. the evidence that proves the system is easier to change afterward.

Do not ask the reader to perform the refactor inside the exercise.

## 21. Chapter-Local ADR Target

Use a record close to:

`Refactor the Legacy Startup Path Behind a Compatibility Boundary`

The record should capture:

- the product promise being preserved;
- why the current structure is too expensive or risky to change;
- the hidden dependents and product-state findings from Chapters 32 through 36;
- the new boundary or dependency direction;
- the compatibility seam and retirement trigger;
- the characterization, contract, integration, service-tool, manufacturing, support, release, and observability checks;
- rollback and recovery criteria;
- the records, dashboards, alerts, release notes, support procedures, and Architecture Ledger rows to update;
- the condition under which the refactor can be frozen, continued, paused, or reversed.

## 22. Notebook Targets

The future draft should end with exactly three chapter-specific observations close to:

1. `A cleaner structure is not done until the product still trusts it.`
2. `Refactor from the promise inward.`
3. `The best legacy refactor lowers future change cost without spending current trust.`

These remain chapter prose, not registered PEAK concepts.

## 23. Validation Checklist

- Repository synchronized with `origin/main` before branch creation.
- `origin/main` contains Chapter 36 canonical state and manuscript.
- Working tree clean before editing.
- Branch `chapter37` created from `origin/main`.
- `editor/chapter-briefs/CHAPTER-037-refactoring-without-losing-product-trust.md` created.
- `CHAPTER-037` registered exactly once as `draft` in `knowledge/index.yaml`.
- No `primary_concept` field added to `CHAPTER-037`.
- Required `CHAPTER-037` relationship set registered.
- Every target in the Chapter 37 relationship set exists as an entity.
- Relationship verbs are only `references`.
- No duplicate Chapter 37 relationships exist.
- Chapters 1-36 remain canonical.
- No Chapter 37 manuscript created.
- No new PEAK concept file created.
- Part VI table of contents order unchanged.
- `editor/EDITOR_LOG.md` updated with Chapter 37 Canonical Brief Registration.
- Validation commands completed and recorded in the editor log.
- Commit subject: `docs(chapter-37): register canonical brief`.
- Next expected phase: Author Draft.

## 24. Next Expected Phase

Next expected phase: Chapter 37 Author Draft.

The next prompt should create the reader-facing manuscript only after this canonical brief is committed and pushed. It
should not reopen Chapter 36 freeze work, revise Chapters 1-36, create appendix content, introduce a new PEAK concept,
or add a `primary_concept` field.
