# CHAPTER-036 Canonical Brief: Deleting Safely

## 1. Metadata

- Stable ID: `CHAPTER-036`.
- Title: `Deleting Safely`.
- Part: Part VI - Legacy.
- Chapter number: 36.
- Expected manuscript path: `book/06-legacy/36-deleting-safely.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-036-deleting-safely.md`.
- Branch: `chapter36`.
- Verified baseline `origin/main`: `52193fc288f4fc3b1c6cd9d7c48de470b67a1413`.
- Baseline evidence: PR #37 Chapter 35 squash merge commit,
  `Chapter 35: Reducing Boolean Explosion (#37)`.
- Canonical predecessor: `CHAPTER-035` - Reducing Boolean Explosion.
- Canonical successor: `CHAPTER-037` - Refactoring Without Losing Product Trust.
- Part position: fifth chapter of Part VI - Legacy.
- Reader-facing draft created: no.
- Expected lifecycle status after registration: `draft`.
- Primary concept: none. Chapter 36 illustrates the existing `RITUAL-003` Deletion Day ritual and references the
  existing `VOCAB-005` Deletion Day vocabulary term; it must not add a `primary_concept` registry field.
- Central illustrated concept: `RITUAL-003` - Deletion Day.
- Central vocabulary term: `VOCAB-005` - Deletion Day.
- Central chapter-local practice: removing old behavior, promises, assumptions, workflows, and records with evidence,
  ownership, communication, staged removal, validation, and recovery paths.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `52193fc288f4fc3b1c6cd9d7c48de470b67a1413`.
- That baseline is the PR #37 Chapter 35 squash merge commit,
  `Chapter 35: Reducing Boolean Explosion (#37)`.
- The baseline contains the Chapter 35 manuscript, canonical brief, editor log, and index updates.
- `CHAPTER-035` is registered as `canonical` in `knowledge/index.yaml`.
- Chapter 35 Freeze Review is recorded in `editor/EDITOR_LOG.md` with Frozen lifecycle status.
- `CHAPTER-001` through `CHAPTER-035` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-036` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 36 canonical brief or reader-facing manuscript existed before this registration.
- No Chapter 37 manuscript existed before this registration.
- The Part VI table of contents order is Reading a Legacy System, Finding Silent Coupling, Managing Utility Gravity,
  Reducing Boolean Explosion, Deleting Safely, and Refactoring Without Losing Product Trust.
- `book/06-legacy/README.md` is intentionally minimal and still contains its section-level author note.
- No tracked `site/` output existed before this registration.
- The PEAK graph already contains `RITUAL-003` Deletion Day and `VOCAB-005` Deletion Day, so no new concept is
  required.

## 3. Part VI Role

Chapter 36 follows the first four Legacy chapters. Chapter 32 taught the reader to build a reading map before changing
a legacy system. Chapter 33 taught the reader to find hidden behavioral dependencies. Chapter 34 taught the reader to
map overgrown shared helpers before moving them. Chapter 35 taught the reader to name and reduce product state
combinations before changing behavior.

Chapter 36 turns those findings into safe removal work. Its center is deletion as a product change. The future chapter
should teach how to decide what can be removed, prove the decision, stage the change, communicate the removal, preserve
recovery where product trust requires it, and delete the surrounding promises and records. Chapter 37 owns broader
trust-preserving refactoring when deletion alone is not enough.

## 4. Canonical Purpose

Prepare Chapter 36 to teach that deletion is a product change, not housekeeping. The chapter should move the reader
away from asking:

> Is this code unused?

to asking:

> What behavior, promise, owner, consumer, evidence, communication path, recovery path, and record changes when this
> disappears?

Candidate thesis for the future manuscript:

> Deleting safely is not the same as deleting confidently.

This thesis is chapter-level prose. Do not register it as a PEAK law, maxim, principle, artifact, ritual, metric,
smell, anti-pattern, failure story, or vocabulary concept.

## 5. Primary-Concept Resolution

Chapter 36 has no new primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. The graph already
contains `RITUAL-003` Deletion Day and `VOCAB-005` Deletion Day. Chapter 36 should illustrate the existing ritual and
use the existing vocabulary term while referencing the laws, metrics, artifacts, rituals, smells, anti-patterns, and
failure stories needed to remove legacy behavior responsibly.

Deletion evidence, deletion candidate, compatibility window, removal proof, rollback trigger, recovery plan, deletion
classification, surrounding promise cleanup, and reopen evidence remain chapter-local prose. Do not create a new PEAK
concept, ID, artifact, ritual, metric, vocabulary term, smell, anti-pattern, failure story, primary-concept field, or
relationship verb for them.

## 6. Central Thesis

Legacy systems often preserve behavior because someone outside the code still depends on it. Deletion removes behavior,
promises, assumptions, workflows, recovery paths, and records, not only files or branches. A Principal Engineer treats
removal as a product change: identify what is being removed, find owners and consumers, gather evidence, communicate
the removal, stage it with guardrails when needed, validate the result, and update the records that made the old path
look supported.

Approved supporting formulation for the future draft:

> Shrink the system without surprising the product.

This formulation is chapter-local language, not a new PEAK concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. deletion is safe when source search finds no callers;
2. removing old code is housekeeping, not a product change;
3. absence of telemetry proves absence of use;
4. unsupported behavior can be deleted because it is unsupported;
5. old flags, compatibility paths, dashboards, scripts, tests, and procedures can be removed independently;
6. the team can delete first and rely on rollback if someone complains;
7. code cleanup is separate from release notes, support procedures, service tools, and manufacturing workflows;
8. temporary workarounds can be removed once the original team forgets why they exist;
9. deletion confidence is the same as deletion evidence;
10. safe deletion is a prelude to immediate broad refactoring.

By the end of the chapter, the reader should be able to:

1. name the specific behavior, API, flag, variant, event, script, dashboard, test, procedure, promise, or workaround
   being removed;
2. identify owners and consumers across code, products, teams, tools, manufacturing, support, operations, field
   upgrades, and customers;
3. distinguish "not seen" from "not possible" and "not supported" from "safe to delete";
4. gather evidence from telemetry, logs, field data, support cases, manufacturing records, release history, tests,
   source search, deployment inventory, and human memory;
5. classify deletion candidates as active, unused-with-evidence, obsolete, temporary-with-owner, unsupported-but-real,
   unknown, or dangerous;
6. add characterization, contract, or integration tests around behavior before removing it;
7. communicate consequential removal through ADRs, RFCs, Decision Journal entries, Architecture Ledger rows, release
   notes, and support or manufacturing updates;
8. stage deletion with warnings, observability, gates, compatibility windows, canary release, rollback, or recovery
   when product trust needs guardrails;
9. delete the surrounding promises, docs, dashboards, alerts, fixtures, scripts, tooling assumptions, support
   procedures, and migration instructions;
10. feed repeated deletion blockers into Architecture Health Review and defer broad refactoring to Chapter 37.

## 8. Deletion Scope

For Chapter 36, deletion means removing old behavior and the promises around it. The future manuscript may examine:

- old compatibility paths and fallback behavior;
- product flags, customer exceptions, unsupported variants, and temporary workarounds;
- APIs, events, configuration branches, dashboards, alerts, scripts, tests, fixtures, and operational procedures;
- service-tool diagnostics, manufacturing rework flows, support procedures, release scripts, and field-upgrade paths;
- documentation, Decision Journal entries, Architecture Ledger rows, release notes, and migration instructions that
  make old behavior appear supported;
- rollback, recovery, and reopen triggers when deletion touches product trust.

The chapter should not treat every old path as waste. Some old behavior is still active. Some is unsupported but real.
Some is unknown because the team lacks evidence. The safe response is proportionate deletion work, not permanent
preservation and not cleanup theater.

## 9. Deletion Order and Evidence

The future manuscript should teach a deletion order that starts from a candidate removal, not from dislike of messy
code.

Useful finding layers:

1. What exactly is being removed: behavior, API, flag, variant, event, configuration branch, script, dashboard, test,
   procedure, compatibility promise, or workaround?
2. Which product promises, owners, consumers, tools, manufacturing paths, support procedures, operations paths, field
   upgrades, and customer workflows may depend on it?
3. What evidence shows current use, historical use, unsupported use, or absence of use?
4. Was the telemetry designed to see this behavior, or is the team mistaking silence for evidence?
5. Which tests characterize the old behavior before it disappears?
6. Which records, release notes, support procedures, dashboards, alerts, scripts, or migration instructions must change
   with the deletion?
7. Which guardrails are needed: warning period, observability, feature gate, shadow detection, canary release, rollback
   path, compatibility window, or recovery procedure?
8. What evidence would pause, roll back, or reopen the deletion decision?
9. Which repeated deletion blockers should be surfaced in Architecture Health Review?
10. Which restructuring question belongs to Chapter 37 instead of this deletion chapter?

Do not turn this into a source-search checklist. The order should change the reader's attention from local cleanup to
trust-preserving removal.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 36 covers:

- deletion as a product change rather than housekeeping;
- behavior, API, flag, variant, event, configuration, script, dashboard, test, procedure, compatibility promise, and
  workaround removal;
- ownership and consumer discovery across code, products, teams, tools, manufacturing, support, operations, field
  upgrades, and customers;
- evidence from telemetry, logs, field data, support cases, manufacturing records, release history, tests, source
  search, deployment inventory, and human memory;
- deletion candidate classification and risk triage;
- characterization, contract, and integration tests around behavior before removal;
- ADRs, RFCs, Decision Journal entries, Mistake Ledger entries, Event Catalog updates, Architecture Ledger rows,
  Architecture Review, and Architecture Health Review as ways to communicate and remember removal;
- guardrails such as warnings, observability, feature gates, shadow detection, canary release, rollback paths,
  compatibility windows, and recovery plans;
- cleanup of surrounding promises, records, documentation, dashboards, alerts, fixtures, scripts, tooling assumptions,
  support procedures, and migration instructions.

### Explicitly Out of Scope

Do not turn Chapter 36 into:

- a generic cleanup chapter;
- a code deletion checklist only;
- a rewrite recommendation;
- a broad refactoring chapter;
- a test-coverage-only chapter;
- a feature flag management chapter;
- a product retirement playbook;
- a source-code search tutorial;
- a chapter about deleting old things because they are ugly;
- a chapter about preserving all old behavior forever;
- a new PEAK concept proposal.

## 11. Recommended Legacy-System Story

Use a story close to:

`The Code Nobody Used Until Tuesday`

A legacy product contains an apparently unused compatibility path. Local evidence says it is dead: source search is
quiet, ordinary telemetry has no obvious signal, and the current happy-path tests pass. The team deletes it and later
discovers field reality: old devices, service tools, backend interpretation, manufacturing rework, support procedures,
dashboards, release scripts, or customer-specific upgrade paths still depended on the behavior.

The Principal Engineer does not respond by preserving every old path forever or launching a broad refactor. They
rebuild the deletion evidence: name the promise, find owners and consumers, add characterization or contract tests,
communicate the removal, stage it with guardrails, update support and manufacturing records, keep a recovery plan where
product trust requires it, and record what evidence would reopen the decision. The story should end with a smaller
system and fewer hidden promises, not a triumphant line-count reduction.

## 12. Future Manuscript Moves

The future Author Draft should include these moves:

1. start from a candidate deletion, not from dislike of messy code;
2. name what is being removed: behavior, API, flag, variant, event, configuration branch, script, dashboard, test,
   procedure, compatibility promise, or workaround;
3. identify owners and consumers across code, products, teams, tools, manufacturing, support, operations, field
   upgrades, and customers;
4. treat deletion as a change to promises rather than only removing lines;
5. gather evidence before removal from telemetry, logs, field data, support cases, manufacturing records, release
   history, test coverage, source search, deployment inventory, and human memory;
6. separate "not seen" from "not possible" and "not supported" from "safe to delete";
7. classify candidates as active, unused-with-evidence, obsolete, temporary-with-owner, unsupported-but-real, unknown,
   or dangerous;
8. add characterization or contract tests around the behavior before removing it;
9. communicate removal through ADRs, RFCs, Decision Journal entries, Architecture Ledger rows, release notes, and
   support, manufacturing, or tooling updates where needed;
10. stage deletion behind guardrails where needed;
11. delete the surrounding promises, docs, dashboards, alerts, test fixtures, scripts, service-tool assumptions,
    support procedures, and migration instructions;
12. keep a rollback or recovery plan when deletion touches product trust;
13. record what evidence would reopen the decision;
14. feed repeated deletion blockers back into Architecture Health Review;
15. defer broad refactoring and migration strategy to Chapter 37.

## 13. Boundary With Neighboring Chapters

- Chapter 32 owns reading the legacy system before the first change. Chapter 36 may use reading maps as input, but it
  must not reteach legacy reading.
- Chapter 33 owns finding Silent Coupling. Chapter 36 may use discovered hidden dependents as deletion evidence, but it
  must not become a coupling-discovery chapter.
- Chapter 34 owns Utility Gravity. Chapter 36 may remove obsolete utility behavior after evidence exists, but it must
  not become a shared-helper mapping chapter.
- Chapter 35 owns Boolean Explosion. Chapter 36 may delete obsolete or unsupported combinations after the state space is
  named, but it must not teach state-space reduction.
- Chapter 37 owns Refactoring Without Losing Product Trust. Chapter 36 may point forward when deletion is insufficient,
  but it must not teach broad migration, restructuring, or refactoring strategy.

## 14. Required PEAK Relationship Set

Register Chapter 36 with these outgoing relationships:

- `CHAPTER-036 illustrates RITUAL-003`
- `CHAPTER-036 references VOCAB-005`
- `CHAPTER-036 references LAW-001`
- `CHAPTER-036 references LAW-002`
- `CHAPTER-036 references LAW-003`
- `CHAPTER-036 references LAW-004`
- `CHAPTER-036 references LAW-005`
- `CHAPTER-036 references LAW-006`
- `CHAPTER-036 references LAW-007`
- `CHAPTER-036 references VOCAB-001`
- `CHAPTER-036 references METRIC-001`
- `CHAPTER-036 references METRIC-002`
- `CHAPTER-036 references METRIC-003`
- `CHAPTER-036 references METRIC-004`
- `CHAPTER-036 references METRIC-005`
- `CHAPTER-036 references ARTIFACT-001`
- `CHAPTER-036 references ARTIFACT-002`
- `CHAPTER-036 references ARTIFACT-003`
- `CHAPTER-036 references ARTIFACT-004`
- `CHAPTER-036 references ARTIFACT-005`
- `CHAPTER-036 references ARTIFACT-006`
- `CHAPTER-036 references RITUAL-001`
- `CHAPTER-036 references RITUAL-004`
- `CHAPTER-036 references SMELL-001`
- `CHAPTER-036 references SMELL-002`
- `CHAPTER-036 references SMELL-003`
- `CHAPTER-036 references SMELL-004`
- `CHAPTER-036 references SMELL-005`
- `CHAPTER-036 references SMELL-006`
- `CHAPTER-036 references ANTIPATTERN-003`
- `CHAPTER-036 references ANTIPATTERN-006`
- `CHAPTER-036 references FAILURE-004`
- `CHAPTER-036 references FAILURE-005`

## 15. Selected PEAK Concept Rationale

- `RITUAL-003` is illustrated because Deletion Day is the chapter's central removal discipline.
- `VOCAB-005` is referenced because the chapter uses the existing Deletion Day vocabulary term.
- `LAW-001` is material because deleted state, behavior, and recovery paths need named owners.
- `LAW-002` is material because deleting an API, diagnostic, event, or tool behavior changes a promise.
- `LAW-003` is material because compatibility windows, release order, and old-device timelines shape safe removal.
- `LAW-004` is material because simplicity comes from shrinking supported behavior without surprising the product.
- `LAW-005` is material because removal requires evidence, not confidence from local search.
- `LAW-006` is material because unused flexibility can be waste only after the team proves it is truly unused or
  obsolete.
- `LAW-007` is material because old compatibility paths, scripts, and variants are dependency decisions that must be
  retired deliberately.
- `VOCAB-001`, `METRIC-001`, `METRIC-002`, `METRIC-003`, `METRIC-004`, and `METRIC-005` are useful lenses for Change
  Radius, memory risk, discoverability, interface stability, and health signals around deletion.
- `ARTIFACT-001`, `ARTIFACT-002`, `ARTIFACT-003`, `ARTIFACT-004`, `ARTIFACT-005`, and `ARTIFACT-006` are relevant
  because deletion can require ADRs, RFCs, Decision Journal entries, Mistake Ledger repair, Event Catalog cleanup, and
  Architecture Ledger rows.
- `RITUAL-001` and `RITUAL-004` are relevant because consequential deletion may need Architecture Review, and repeated
  deletion blockers belong in Architecture Health Review.
- `SMELL-001`, `SMELL-002`, `SMELL-003`, `SMELL-004`, `SMELL-005`, and `SMELL-006` are relevant as inputs that create
  deletion risk: hidden dependents, utility pull, state combinations, hidden state, platform leakage, and event drift.
- `ANTIPATTERN-003` and `ANTIPATTERN-006` are relevant because global configuration and temporary solutions often
  create deletion candidates that are unsafe to remove without evidence.
- `FAILURE-004` and `FAILURE-005` are relevant because deletion guarded only by memory or schedule pressure can become
  a product-trust failure.

## 16. Rejected and Intentionally Avoided PEAK Concepts

Do not register or center these concepts unless a later authorized canon revision provides a stronger reason:

- `RITUAL-002` - Architecture Freeze: release-freeze governance is nearby but not the chapter's center.
- `RITUAL-005` - Architecture Court and `RITUAL-006` - RFC Friday: existing rituals, but not central to deletion
  safety.
- `ANTIPATTERN-001` - God Module, `ANTIPATTERN-002` - HAL Everywhere, `ANTIPATTERN-004` - Manager Mania, and
  `ANTIPATTERN-005` - Callback Hell: possible background forces, but not needed for the core Deletion Day brief.
- `ARTIFACT-007` - Weak Signal Register: useful for health sensing, but Chapter 36 uses Architecture Health Review and
  concrete deletion evidence instead of centering weak-signal collection.
- `VOCAB-006` - Architecture Freeze, `VOCAB-007` - Architecture Health, `VOCAB-008` - Silent Coupling, `VOCAB-009` -
  Utility Gravity, and `VOCAB-010` - Boolean Explosion: nearby Part VI vocabulary, but Chapter 36 only uses those as
  inputs or boundaries.
- No candidate relationship was omitted from the approved relationship set because each selected concept is materially
  tied to deletion evidence, ownership, communication, staging, record cleanup, or product trust.
- No new PEAK concept, relationship verb, primary-concept field, artifact, ritual, metric, smell, anti-pattern,
  vocabulary term, law, or failure story should be introduced.

## 17. Outgoing Relationship Set

```yaml
- from: CHAPTER-036
  type: illustrates
  to: RITUAL-003
- from: CHAPTER-036
  type: references
  to: VOCAB-005
- from: CHAPTER-036
  type: references
  to: LAW-001
- from: CHAPTER-036
  type: references
  to: LAW-002
- from: CHAPTER-036
  type: references
  to: LAW-003
- from: CHAPTER-036
  type: references
  to: LAW-004
- from: CHAPTER-036
  type: references
  to: LAW-005
- from: CHAPTER-036
  type: references
  to: LAW-006
- from: CHAPTER-036
  type: references
  to: LAW-007
- from: CHAPTER-036
  type: references
  to: VOCAB-001
- from: CHAPTER-036
  type: references
  to: METRIC-001
- from: CHAPTER-036
  type: references
  to: METRIC-002
- from: CHAPTER-036
  type: references
  to: METRIC-003
- from: CHAPTER-036
  type: references
  to: METRIC-004
- from: CHAPTER-036
  type: references
  to: METRIC-005
- from: CHAPTER-036
  type: references
  to: ARTIFACT-001
- from: CHAPTER-036
  type: references
  to: ARTIFACT-002
- from: CHAPTER-036
  type: references
  to: ARTIFACT-003
- from: CHAPTER-036
  type: references
  to: ARTIFACT-004
- from: CHAPTER-036
  type: references
  to: ARTIFACT-005
- from: CHAPTER-036
  type: references
  to: ARTIFACT-006
- from: CHAPTER-036
  type: references
  to: RITUAL-001
- from: CHAPTER-036
  type: references
  to: RITUAL-004
- from: CHAPTER-036
  type: references
  to: SMELL-001
- from: CHAPTER-036
  type: references
  to: SMELL-002
- from: CHAPTER-036
  type: references
  to: SMELL-003
- from: CHAPTER-036
  type: references
  to: SMELL-004
- from: CHAPTER-036
  type: references
  to: SMELL-005
- from: CHAPTER-036
  type: references
  to: SMELL-006
- from: CHAPTER-036
  type: references
  to: ANTIPATTERN-003
- from: CHAPTER-036
  type: references
  to: ANTIPATTERN-006
- from: CHAPTER-036
  type: references
  to: FAILURE-004
- from: CHAPTER-036
  type: references
  to: FAILURE-005
```

### Valid Relationship Verbs

The registered relationships use only `illustrates` and `references`, valid PEAK relationship types in
`editor/KNOWLEDGE_MODEL.md` and the existing chapter graph.

### No-New-Concept Result

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, vocabulary concept, ID,
relationship verb, or primary-concept field is required.

## 18. Story Target

Use:

`The Code Nobody Used Until Tuesday`

The future story should show a legacy product where an apparently unused compatibility path is deleted after local
evidence says it is dead, only for field reality to reveal hidden dependents. The dependents may include old devices,
service tools, backend interpretation, manufacturing rework, support procedures, dashboards, release scripts, or
customer-specific upgrade paths.

The story should not punish deletion. It should punish deletion without enough product evidence, communication,
staging, and record cleanup.

## 19. Draft Constraints for the Future Author Draft

The Author Draft should be accepted only if it:

1. creates `book/06-legacy/36-deleting-safely.md`;
2. preserves this canonical brief unchanged unless a later prompt explicitly authorizes brief revision;
3. keeps `CHAPTER-036` as `draft` until freeze;
4. does not add a `primary_concept` field;
5. does not create new PEAK concepts or relationship verbs;
6. illustrates `RITUAL-003` and materially uses `VOCAB-005`;
7. frames deletion as a product change, not housekeeping;
8. teaches evidence, ownership, communication, staged removal, validation, recovery, and surrounding record cleanup;
9. includes the story target, engineering principle, architecture exercise, chapter-local ADR target, and exactly three
   Principal's Notebook observations;
10. distinguishes "not seen" from "not possible" and "not supported" from "safe to delete";
11. defers broad refactoring and migration strategy to Chapter 37;
12. does not create Chapter 37 or modify Chapters 1-35.

## 20. Validation Checklist

- Repository synchronized with `origin/main` before branch creation.
- `origin/main` contains Chapter 35 canonical state and manuscript.
- Working tree clean before editing.
- Branch `chapter36` created from `origin/main`.
- `editor/chapter-briefs/CHAPTER-036-deleting-safely.md` created.
- `CHAPTER-036` registered exactly once as `draft` in `knowledge/index.yaml`.
- No `primary_concept` field added to `CHAPTER-036`.
- Required `CHAPTER-036` relationship set registered.
- Every target in the Chapter 36 relationship set exists as an entity.
- Relationship verbs are only `illustrates` and `references`.
- No duplicate Chapter 36 relationships exist.
- Chapters 1-35 remain canonical.
- No Chapter 36 manuscript created.
- No Chapter 37 manuscript created.
- `editor/EDITOR_LOG.md` updated with Chapter 36 Canonical Brief Registration.
- Validation commands completed and recorded in the editor log.
- Commit subject: `docs(chapter-36): register canonical brief`.
- Next expected phase: Author Draft.

## 21. Next Expected Phase

Next expected phase: Chapter 36 Author Draft.

The next prompt should create the reader-facing manuscript only after this brief is committed and pushed. It should not
reopen Chapter 35 freeze work, revise Chapters 1-35, create Chapter 37 files, introduce a new PEAK concept, or add a
`primary_concept` field.
