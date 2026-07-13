# CHAPTER-015 Canonical Brief: Managing Change Radius

## 1. Metadata

- Stable ID: `CHAPTER-015`.
- Title: `Managing Change Radius`.
- Part: Part III - Architecture Playbook.
- Chapter number: 15.
- Expected manuscript path: `book/03-architecture-playbook/15-managing-change-radius.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-015-managing-change-radius.md`.
- Branch: `chapter15`.
- Verified baseline `origin/main`: `346f5801c1326e836b81ce6d92e7564d9c946f94`.
- Canonical predecessor: `CHAPTER-014` - Drawing Boundaries That Survive Change.
- Part position: second chapter of Part III - Architecture Playbook.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 15 is a Part III practice chapter, and current repository convention does not require a
  primary PEAK concept for practice chapters.
- Central PEAK concepts: `VOCAB-001` - Change Radius and `METRIC-001` - Change Radius.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `346f5801c1326e836b81ce6d92e7564d9c946f94`.
- That baseline is the PR #16 squash commit, `Chapter 14: Drawing Boundaries That Survive Change (#16)`.
- The Chapter 14 feature-branch Freeze commit `f80988fb40cfeecd4685d9082a3b2d32bfd3f351` remains resolvable.
- The checked final Chapter 14 lifecycle files in the PR #16 squash commit are tree-equivalent to the feature Freeze
  commit.
- `CHAPTER-001` through `CHAPTER-014` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-014` is the first Part III chapter and is canonical.
- `editor/EDITOR_LOG.md` records Chapter 14 Editorial, Canon, Technical, and Freeze Review entries in order.
- The table of contents places `Managing Change Radius` immediately after Chapter 14 in Part III.
- `VOCAB-001` exists exactly once as `Change Radius`.
- `METRIC-001` exists exactly once as `Change Radius`.
- Neither Change Radius concept changed during the Chapter 14 Freeze or squash merge.
- `book/03-architecture-playbook/README.md` remains a placeholder and should not be expanded in this phase.
- `editor/CHAPTER_ARCHITECTURE.md` remains unchanged by Chapter 14.
- `CHAPTER-015` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 15 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter15` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part III Role

Chapter 15 is the second Part III practice chapter. Chapter 14 taught how to draw a boundary around responsibility,
authority, and knowledge. Chapter 15 teaches how to make the real affected surface of a proposed change visible before
implementation hardens the plan.

The chapter should move from boundary placement to change planning. It should show that a Principal Engineer does not
judge a change by the diff alone. The relevant surface includes decisions, assumptions, artifacts, teams, tests, tools,
released behavior, and compatibility obligations that must move together or be validated again when one decision changes.

Chapter 15 should keep Part III practical. It must teach a method the reader can apply before a change becomes a pile of
tickets, but it must not become a project-management chapter.

## 4. Canonical Purpose

Prepare Chapter 15 to teach a Principal Engineer how to map and manage Change Radius.

The chapter should move the reader from asking:

> Which files will we edit?

to asking:

> Which system surfaces must change, be reviewed, be retested, be migrated, or remain compatible because this decision
> changes?

The chapter must teach both mapping and management. Mapping without a decision becomes documentation theater. Managing
without mapping becomes optimistic planning.

## 5. Primary-Concept Resolution

Chapter 15 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records, and Chapter 14
established that Part III practice chapters may be carried by a relationship set rather than by one primary concept.
Chapter 15 therefore records an explicit no-primary decision.

`VOCAB-001` and `METRIC-001` are the central paired Change Radius concepts. The vocabulary concept supplies the semantic
meaning. The metric concept supplies the measurement posture: approximate affected surface, not false precision.

Do not create a new concept such as Impact Radius, Change Surface, Change Map, Propagation Radius, Review Radius,
Retest Radius, Change Budget, Change Topology, or Change-Radius Ledger.

## 6. Central Thesis

The cost and risk of a change are determined by the system surfaces that must move, be reviewed, be retested, be
migrated, remain compatible, or be observed because one decision changes, not by the number of edited files.

Approved supporting formulation for the future draft:

> Map the decision, not the diff; then contain accidental spread and sequence the required spread deliberately.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. a small diff means a small change;
2. affected files are the same as affected system surface;
3. implementation tasks reveal the review and test scope;
4. static code search can find every consumer;
5. broad Change Radius always proves bad design;
6. the right response to a broad radius is always redesign;
7. compatibility work can be planned after implementation starts;
8. unknown consumers are edge cases rather than part of the risk.

By the end of the chapter, the reader should be able to:

1. state the decision that is changing;
2. map direct, indirect, and latent affected surfaces;
3. distinguish required radius from accidental radius;
4. identify review, retest, migration, release-observation, and compatibility surfaces separately from implementation;
5. mark uncertainty without stopping all work;
6. compare alternatives approximately without inventing a numerical scoring system;
7. choose containment and sequencing actions;
8. record residual radius and accepted uncertainty in existing artifacts.

## 8. Semantic Definition of Change Radius

Use the repository meaning exactly:

> Change Radius is the amount of system surface that must change, be reviewed, or be retested when one decision changes.

For Chapter 15, the affected surface may include code, product behavior, state models, APIs, protocols, persistence,
firmware, boot support, hardware integration, manufacturing tools, calibration stations, host applications, service
tools, UI, test fixtures, simulators, continuous integration, packaging, release notes, telemetry, diagnostics, support
procedures, field upgrade paths, team ownership, customer workflows, and evidence records.

Not every surface matters for every change. The radius is change-specific.

## 9. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 15 covers:

- mapping affected surface before implementation;
- managing affected surface through containment and sequencing;
- direct, indirect, latent, required, accidental, unknown, and residual radius as chapter-local analytical phrases;
- product behavior, state, contract, dependency, temporal, test, tool, release, organizational, and evidence dimensions;
- review, retest, migration, compatibility, and release-observation surfaces;
- approximate comparison of design options without false precision;
- existing ADR and Decision Journal use for recording material decisions and residual uncertainty;
- an embedded calibration-record story crossing firmware, storage, manufacturing, service tools, tests, and field
  upgrade behavior.

### Explicitly Out of Scope

Do not turn Chapter 15 into:

- a file-impact checklist;
- a project-management or ticket-decomposition guide;
- a static-analysis tools survey;
- a release-management chapter;
- a schema-migration tutorial;
- a manufacturing chapter;
- a product-line architecture chapter;
- a test-strategy handbook;
- a dependency graph tutorial;
- Chapter 14 repeated;
- Chapter 16 failure and recovery design;
- Chapter 17 ADR/RFC practice;
- Chapter 18 Architecture Review;
- Chapter 19 Architecture Freeze;
- a numerical scoring framework;
- a new PEAK concept proposal.

## 10. Change Radius Versus Diff Size

Change Radius is not lines changed, files changed, number of commits, number of modules, number of repositories, number
of tickets, code complexity, story points, or implementation time alone.

File count may be one signal. It misses unchanged consumers whose assumptions must be validated again, tests outside the
repository, manufacturing and service tools, release compatibility, field migration, operational procedures, hidden
coupling, team review needs, and old versions that must coexist.

A one-line change can have a large Change Radius. A large mechanical refactor can have a bounded semantic radius.

## 11. Dimensions of Affected Surface

The future draft should define a practical, non-numeric map across dimensions:

- Behavioral radius: externally or internally observable behavior that changes.
- State radius: authorities, transitions, caches, persistence records, and migration paths affected.
- Contract radius: APIs, protocols, schemas, events, command meanings, and compatibility promises affected.
- Dependency radius: imported assumptions, libraries, platforms, tools, vendor behavior, and support horizons involved.
- Temporal radius: timing, ordering, completion, timeout, retry, reset, and lifecycle assumptions to revalidate.
- Test radius: unit, integration, system, manufacturing, regression, compatibility, field, and hardware-in-the-loop
  tests that matter.
- Tool radius: build, calibration, service, packaging, deployment, and support tools that move with the decision.
- Release radius: shipped versions, upgrade paths, rollback paths, staged exposure, release notes, and support
  obligations.
- Organizational radius: owners, reviewers, teams, suppliers, and operational roles that must participate.
- Evidence radius: previous evidence that no longer transfers and what must be validated again.

These are chapter-local analytical dimensions, not new PEAK vocabulary entities. Do not force every change through every
dimension.

## 12. Direct, Indirect, and Latent Radius

The future draft should distinguish three chapter-local phrases:

- direct radius: code, artifacts, or behavior intentionally changed;
- indirect radius: consumers and workflows relying on the changed decision;
- latent radius: hidden or uncertain assumptions revealed through failures, release differences, service tools,
  manufacturing, field conditions, or team memory.

These phrases help the reader look beyond visible call graphs. They must not be registered as PEAK concepts.

## 13. Required Versus Accidental Radius

A large radius is not automatically bad.

Required radius is affected surface that must move together to preserve one coherent product decision. Examples include
a wire-format version change, a safety threshold change, or a persistent schema change that requires migration and
downgrade decisions.

Accidental radius is affected surface caused by leaked or duplicated knowledge. Examples include UI interpreting
platform state, manufacturing scripts duplicating a parser, test fixtures depending on undocumented event order, service
tools reading internal storage layout, and unrelated modules sharing global configuration.

The goal is not always to minimize Change Radius. The goal is to make it truthful, separate required from accidental
spread, shrink accidental spread, and plan required spread explicitly.

## 14. Mapping Before Implementation

The future draft should teach a lightweight pre-implementation sequence:

1. State the decision that is changing.
2. Name the visible behavior affected.
3. Identify the authoritative owner.
4. Trace contracts and representations.
5. Trace runtime and lifecycle paths.
6. Identify tests and evidence supporting the old behavior.
7. Identify tools and operational workflows.
8. Identify released versions and compatibility obligations.
9. Identify owners and reviewers.
10. Separate required from accidental radius.
11. Mark uncertainty and unknown paths.
12. Choose containment and sequencing actions.

The method should work for embedded teams with incomplete documentation. It must not become an exhaustive enterprise
impact-analysis process.

## 15. Sources of Evidence

A Change Radius map may use code search, call graphs, dependency graphs, build targets, schemas, protocol definitions,
event catalogs, tests, continuous-integration configuration, manufacturing scripts, service tools, support procedures,
release notes, ADRs, RFCs, Decision Journal entries, Architecture Ledger entries, commit history, incident reports, weak
signals, interviews with owners, field telemetry, and product variants.

No source is complete by itself. Static analysis cannot discover all Change Radius. Team memory is useful but
insufficient. Chapter 15 should not become a tools survey.

## 16. Unknown Radius and Uncertainty

A credible map includes uncertainty.

Examples include unknown consumer ownership, undocumented manufacturing dependency, active old field versions, unclear
service-tool behavior, copied schema outside the repository, undocumented event ordering, untested rollback behavior,
and supplier firmware behavior.

Unknown radius should affect commitment, sequencing, review depth, test scope, rollout, observability, and
reversibility. It is not a reason to stop all work by default. Use bounded discovery and staged commitment.

Do not duplicate Chapter 5 or Chapter 13's full evidence frameworks.

## 17. Managing and Containing Radius

The chapter must go beyond mapping.

Management actions may include moving translation to a boundary, centralizing one authoritative decision, making an
implicit contract explicit, adding a compatibility adapter, separating product behavior from representation, migrating a
schema deliberately, removing a back channel, sequencing changes by dependency, preserving old and new paths
temporarily, adding targeted observability, narrowing initial product exposure, choosing a reversible first step,
coordinating one cross-team transition, updating tests at the correct boundary, and recording unresolved radius.

Do not prescribe all actions for every change. Do not make feature flags the default solution. Do not create a universal
change-management framework.

## 18. Sequencing and Compatibility

A Change Radius plan should identify order.

Potential sequencing concerns include producer before consumer, consumer before producer, backward-compatible reader
before new writer, schema migration before behavior change, diagnostics before rollout, adapter before consumer
migration, test fixture before firmware enforcement, manufacturing tool before factory transition, boot support before
application image, service tooling before field support, and cleanup after old-version retirement.

The correct order depends on compatibility and failure semantics. Chapter 15 should teach architecture-level
sequencing, not the full release playbook.

## 19. Review, Retest, Migration, and Observation Surfaces

The future draft should distinguish implementation surface, review surface, retest surface, migration surface, and
release-observation surface.

These surfaces may differ. An unchanged parser may need review because a schema meaning changed. A hardware test may
need rerunning although firmware code is untouched. Support documentation may change although product behavior is
preserved. A service tool may remain compatible but still need verification against a new version. A rollback path may
need testing despite no code edit in the rollback component.

Do not turn these into new canonical metric types.

## 20. Approximate Measurement and False Precision

Use `METRIC-001` exactly: measure approximate affected surface; do not chase false precision.

The future draft may compare:

- expected versus observed affected surface;
- before versus after a boundary improvement;
- one design option versus another;
- one migration sequence versus another;
- one product variant versus another.

Useful signals may include independent owners, contracts, released versions, evidence that no longer transfers,
manufacturing or service paths, and compatibility obligations. Do not create a universal numerical threshold, score, or
rating.

## 21. Boundary With Chapter 14

Chapter 14 owns drawing and evaluating architecture boundaries: responsibility, authority, knowledge, vocabulary,
dependency direction, translation, integrity, back channels, and proportional boundary cost.

Chapter 15 owns the full Change Radius method: mapping affected surface, separating required from accidental spread,
planning review and retest surfaces, managing uncertainty, and sequencing change.

Chapter 15 may use Chapter 14's boundaries as inputs. It must not re-teach boundary placement or repeat the radio
boundary story.

## 22. Boundaries With Chapters 1-13

### Chapters 1-6 - Principal Engineering Foundations

Chapter 15 may use decision quality, constraints, questions, outcome ownership, evidence, and stewardship as premises.
It must not repeat the Part I mindset chapters.

### Chapter 7 - Every State Has One Owner

Chapter 15 may ask which state authority is affected and who owns migration. It must not reteach state ownership.

### Chapter 8 - Every API Is a Promise

Chapter 15 may map contract radius and compatibility promises. It must not become an API-versioning chapter.

### Chapter 9 - Every Dependency Is a Decision

Chapter 15 may map imported dependency assumptions and update surfaces. It must not retell dependency selection or
replacement cost.

### Chapter 10 - Time Is a Dependency

Chapter 15 may map temporal radius. It must not teach clock domains, timeout semantics, or freshness rules in depth.

### Chapter 11 - Unused Flexibility Is Waste

Chapter 15 may distinguish temporary compatibility from unsupported option surface. It must not become a flexibility
audit.

### Chapter 12 - Simplicity Is a Feature

Chapter 15 may show accidental radius as complexity cost. It must not become a general simplicity chapter.

### Chapter 13 - Evidence Before Confidence

Chapter 15 may ask which evidence no longer transfers. It must not teach the full confidence and revalidation law.

## 23. Boundaries With Chapters 16-19

### Chapter 16 - Designing for Failure and Recovery

Chapter 15 may include sequencing, rollback-path awareness, and release observation. Chapter 16 owns full failure
detection, containment, degradation, retry, recovery, and unknown-outcome design.

### Chapter 17 - Using ADRs and RFCs Well

Chapter 15 may include one chapter-local ADR and may use existing records. Chapter 17 owns artifact choice, authoring,
review, lifecycle, and quality.

### Chapter 18 - Reviewing Architecture Before It Hardens

Chapter 15 may identify what must be reviewed. Chapter 18 owns the Architecture Review ritual.

### Chapter 19 - Freezing Architecture Without Freezing Learning

Chapter 15 may name residual radius and review triggers. Chapter 19 owns freeze, exceptions, and revalidation.

## 24. Boundaries With Later Parts

Part IV should retain detailed product-line architecture, manufacturing and field workflows, observability
implementation, release discipline, upgrade systems, and the reference project.

Part V should retain organizational rituals, alignment, mentoring, and Architecture Health Review operation.

Part VI should retain full legacy discovery, silent-coupling recovery, utility-gravity cleanup, Boolean Explosion
reduction, deletion programs, and broad refactoring practice.

Chapter 15 may point toward those topics only where needed to constrain Change Radius.

## 25. Recommended Embedded-Systems Story

### Working Title

The Calibration Record That Was Not One Change

### System

Use an embedded product with calibration data stored on the device, produced by a manufacturing station, read by
firmware, inspected by a service tool, summarized in diagnostics, and preserved across field updates.

The team changes the meaning or representation of one calibration value. The source edit appears small, but the affected
surface includes firmware storage, schema versioning, manufacturing scripts, service tooling, tests, diagnostics,
released devices, downgrade behavior, support procedure, and product variants.

### Incident Shape

The first plan treats the work as a firmware field update. Integration reveals that the station still writes the old
record, the service tool reads internal layout, tests assume old defaults, a field upgrade path must preserve existing
valid state, and a reset-to-default fallback would erase customer-specific calibration.

### Principal Engineer Intervention

The Principal Engineer recasts the work from "change this field" to "map the product decision whose representation is
changing." The team identifies required radius, accidental radius, unknown consumers, compatibility sequence, targeted
tests, diagnostics, and one containment action before implementation hardens.

The story should stay grounded in architecture and sequencing. It must not become a schema-migration tutorial.

## 26. Expected Discussion Arc

1. **The diff is not the change.**
   The chapter should begin by separating source edits from affected system surface.
2. **A decision has a radius.**
   The changing product decision determines what must move, not the edited file.
3. **Affected surfaces differ.**
   Implementation, review, retest, migration, compatibility, and observation surfaces are not identical.
4. **Required spread and accidental spread need different responses.**
   Required spread gets planned. Accidental spread gets contained.
5. **Unknown consumers are part of the map.**
   Uncertainty changes commitment, sequencing, and evidence needs.
6. **Approximation is useful.**
   Relative comparison is enough; false precision weakens judgment.
7. **Management follows mapping.**
   Boundaries, translation, compatibility adapters, tests, diagnostics, staged exposure, and records make the map useful.
8. **The decision must be recorded.**
   Residual radius and accepted uncertainty should not live only in memory.

## 27. Applicability

The chapter applies when a change may affect:

- product behavior;
- persistent or released data;
- external or internal contracts;
- firmware and tools;
- manufacturing or service workflows;
- tests and evidence;
- dependencies and vendor behavior;
- timing or lifecycle assumptions;
- released versions;
- team ownership and review responsibility.

The method is proportional. A local implementation cleanup may need only a quick radius check. A product contract,
schema, firmware, tool, or field-compatibility change deserves a fuller map.

## 28. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- every change needs a full map;
- every broad radius proves bad architecture;
- every narrow radius proves correctness;
- all radius can be known before implementation;
- all consumers can be found with code search;
- every compatibility path deserves feature flags;
- every broad change needs a redesign;
- passing regression tests proves unknown consumers do not exist;
- a smaller diff means lower release risk.

Sometimes the responsible move is to accept a broad required radius because the product decision genuinely spans many
surfaces. Sometimes the responsible move is to proceed with known residual uncertainty and a clear owner.

## 29. Violation Patterns

The future draft should make these violations visible:

- one-line change requiring unrelated release and support changes;
- schema copied into multiple repositories;
- tests depending on undocumented event order;
- service tool reading internal storage layout;
- manufacturing script duplicating firmware validation;
- UI interpreting raw platform state;
- one global configuration value shaping unrelated modules;
- hidden compatibility assumptions across product variants;
- dependency upgrade changing callback context or ownership;
- unchanged consumer omitted from review because no file changed;
- rollback path ignored because the forward path passed;
- broad required radius treated as architecture failure;
- accidental radius accepted as inevitable coordination;
- "all tests passed" despite missing manufacturing or field paths;
- radius discovered only after integration.

## 30. Engineering Principle Target

Target principle for the future draft:

> Map the decision, not the diff. Identify the surfaces that must change, be reviewed, be retested, migrated, or remain
> compatible; then contain accidental spread and sequence the required spread deliberately.

The principle should imply review questions:

1. What decision is changing?
2. Which product behavior changes?
3. Who owns the authoritative meaning?
4. Which contracts and representations carry it?
5. Which consumers rely on the old meaning?
6. Which surfaces change, review, retest, migrate, or remain compatible?
7. Which radius is required?
8. Which radius is accidental?
9. What remains unknown?
10. Which evidence no longer transfers?
11. What sequence preserves compatibility?
12. Which owner accepts the residual radius?

The final manuscript may shorten this list for reader rhythm.

## 31. Architecture Exercise Target

### Working Title

Map One Change Before You Implement It

Ask the reader to choose one upcoming change and document:

1. exact decision changing;
2. visible behavior;
3. authoritative owner;
4. current representation;
5. APIs, protocols, schemas, events, and storage;
6. direct consumers;
7. indirect consumers;
8. uncertain or historical consumers;
9. hardware variants;
10. software variants;
11. released versions;
12. state and migration implications;
13. timing and lifecycle assumptions;
14. tests and evidence;
15. manufacturing, calibration, service, support, packaging, and release paths;
16. owners and reviewers;
17. implementation surface;
18. review surface;
19. retest surface;
20. migration surface;
21. release-observation surface;
22. required radius;
23. accidental radius;
24. unknown radius;
25. containment action;
26. compatibility sequence;
27. reversible first step;
28. ADR or Decision Journal update.

The exercise must end with one explicit radius map, one sequencing decision, one containment action, and one accepted
residual uncertainty. Do not create a new canonical artifact.

## 32. Chapter-Local ADR Brief

### Working Title

Version and Migrate the Calibration Record Across Product and Tooling Boundaries

### Context

- A calibration value changes meaning or representation.
- Firmware, storage, manufacturing station, service tool, tests, and field upgrade paths depend on the old
  representation.
- Some dependencies are explicit; others are duplicated or undocumented.
- Released devices and product variants exist.
- Reset-to-default fallback would lose valid field state.
- The visible source edit understates the product change.

### Decision

- State the product-level meaning of the new calibration data.
- Assign one authoritative schema and version.
- Define compatible read and write behavior.
- Update producer and consumer sequence deliberately.
- Preserve old-record reading where required.
- Define migration and downgrade behavior.
- Remove duplicated offset or magic-value knowledge.
- Add targeted tests at representation and product-contract boundaries.
- Update manufacturing and service tools before transition.
- Add diagnostics for record version and migration outcome.
- Record unknown external consumers.
- Accept a bounded temporary compatibility path.
- Retire the old path under an explicit trigger.

### Alternatives Considered

- Append a field and rely on structure layout.
- Reset old records to defaults.
- Update firmware first and tools later.
- Keep duplicated schemas synchronized manually.
- Introduce a global compatibility flag.
- Use conditional compilation per product variant.
- Redesign the entire configuration subsystem first.
- Postpone the product change.
- Ship one variant only.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits include explicit radius, controlled consumer movement, reduced duplicated knowledge, preserved field state,
testable manufacturing and service compatibility, and more visible release risk.

Costs include schema and version logic, migration code, temporary dual-read or dual-write behavior where justified, tool
coordination, additional tests and diagnostics, residual unknown consumers, cleanup work, and possible downgrade
constraints.

The ADR must make a real architecture and sequencing decision. It must not reduce to "update all consumers."

## 33. PEAK Concept Map

### Concepts Inspected

- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `SMELL-002` - Utility Gravity.
- `SMELL-003` - Boolean Explosion.
- `ANTIPATTERN-001` - God Module.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-004` - Manager Mania.
- `ANTIPATTERN-006` - Temporary Solution.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-005` - Evidence Before Confidence.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-007` - Architecture Health.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `METRIC-005` - Architecture Health.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-006` - Architecture Ledger.
- `RITUAL-001` - Architecture Review.
- `RITUAL-004` - Architecture Health Review.
- `FAILURE-001` - Logger That Became a Platform.
- `FAILURE-002` - One Lost Packet.
- `FAILURE-003` - The Successful Prototype.
- `FAILURE-005` - The Release We Should Have Delayed.

### Selected Concepts

- `VOCAB-001` - Change Radius: material because the chapter directly teaches the semantic concept.
- `METRIC-001` - Change Radius: material because the chapter teaches approximate affected-surface measurement.
- `LAW-001` - Every State Has One Owner: material because state authority determines who owns changed meaning and
  migration.
- `LAW-002` - Every API Is a Promise: material because contract radius and compatibility promises are central surfaces.
- `LAW-003` - Time Is a Dependency: material because temporal assumptions are part of affected surface.
- `LAW-005` - Evidence Before Confidence: material because evidence that supported old behavior may no longer transfer.
- `LAW-007` - Every Dependency Is a Decision: material because dependency assumptions import affected surface.
- `SMELL-001` - Silent Coupling: material because hidden consumers and workflows make radius larger than the visible
  call graph.
- `SMELL-004` - Hidden State: material because state copies, cached values, and persistent records can create latent
  radius.
- `SMELL-005` - Platform Leakage: material because platform representation leaking into product surfaces creates
  accidental radius.
- `ANTIPATTERN-003` - Global Configuration: material because broad settings often expand accidental radius.
- `ANTIPATTERN-006` - Temporary Solution: material because temporary compatibility paths create residual radius unless
  owned and retired.
- `ARTIFACT-001` - ADR: material because the chapter-local decision has architecture, ownership, cost, and reversibility
  consequences.
- `ARTIFACT-003` - Decision Journal: material because smaller residual-radius and uncertainty decisions can be recorded
  without a full ADR.

### Rejected Concepts

- `SMELL-002` - Utility Gravity: relevant to accumulated helpers, but not central to the calibration-record radius
  method.
- `SMELL-003` - Boolean Explosion: relevant when configuration flags expand radius, but Chapter 11 owns option
  combinations.
- `SMELL-006` - Event Explosion: relevant to event-heavy systems, but Chapter 15 treats events as one possible surface.
- `ANTIPATTERN-001` - God Module: relevant when broad modules expand radius, but not central enough for a registered
  edge.
- `ANTIPATTERN-004` - Manager Mania: relevant when managers hide ownership, but Chapter 14 already carries that boundary
  failure.
- `VOCAB-007` and `METRIC-005` - Architecture Health: Change Radius contributes to health, but Chapter 15 should not
  become a health-review chapter.
- `METRIC-003` - Discoverability: useful for finding owners and decisions, but the selected artifacts carry the record
  need more directly.
- `METRIC-004` - API Stability: relevant to contract radius, but Chapter 8 owns API stability.
- `ARTIFACT-002` - RFC: useful for broad proposals, but Chapter 17 owns ADR/RFC practice.
- `ARTIFACT-005` - Event Catalog: useful when events are central, but not required for this calibration-record story.
- `ARTIFACT-006` - Architecture Ledger: useful for large systems, but not necessary for the chapter's central decision.
- `RITUAL-001` - Architecture Review: Chapter 15 identifies review surface, but Chapter 18 owns the ritual.
- `RITUAL-004` - Architecture Health Review: relevant to long-term upkeep, but later parts own the review operation.
- `FAILURE-001`, `FAILURE-002`, `FAILURE-003`, and `FAILURE-005`: related failure stories, but the selected story is
  a calibration-record radius story rather than an existing failure-story edge.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as required radius, accidental radius, direct radius, indirect radius, latent radius, residual radius,
affected surface, containment, and sequencing remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-015` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-015
  type: illustrates
  to: VOCAB-001

- from: CHAPTER-015
  type: illustrates
  to: METRIC-001

- from: CHAPTER-015
  type: references
  to: LAW-001

- from: CHAPTER-015
  type: references
  to: LAW-002

- from: CHAPTER-015
  type: references
  to: LAW-003

- from: CHAPTER-015
  type: references
  to: LAW-005

- from: CHAPTER-015
  type: references
  to: LAW-007

- from: CHAPTER-015
  type: references
  to: SMELL-001

- from: CHAPTER-015
  type: references
  to: SMELL-004

- from: CHAPTER-015
  type: references
  to: SMELL-005

- from: CHAPTER-015
  type: references
  to: ANTIPATTERN-003

- from: CHAPTER-015
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-015
  type: references
  to: ARTIFACT-001

- from: CHAPTER-015
  type: references
  to: ARTIFACT-003
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 34. Required Reader-Facing Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 15 role:

- Opening Quote: establish that the diff is not the change.
- Story: show a calibration-record change whose affected surface is broader than the source edit.
- Discussion: teach mapping, required versus accidental radius, uncertainty, containment, sequencing, and approximate
  measurement.
- Engineering Principle: anchor Change Radius as a review habit.
- Architecture Exercise: map one real change before implementation and end with radius, sequence, containment, and
  residual uncertainty.
- Principal's Notebook: three short observations, no explanations.
- ADR: record a scoped calibration-record migration and sequencing decision.
- Editor's Commentary: explain how Chapter 15 advances Part III after boundary drawing and before failure, artifact,
  review, and freeze chapters.

## 35. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- The diff is not the change.
- Required radius should be planned; accidental radius should be contained.
- Unknown consumers are part of the risk.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 36. Technical Credibility Requirements

The future draft must treat the following accurately:

- persistent schema versions;
- firmware and boot compatibility;
- binary records and alignment;
- manufacturing tools;
- service tools;
- host and web interfaces;
- product variants;
- old and new firmware coexistence;
- upgrade and downgrade behavior;
- callbacks and events;
- timing assumptions;
- configuration defaults;
- test fixtures;
- hardware-in-the-loop and system tests;
- packaging and release artifacts;
- diagnostics;
- staged migration;
- temporary compatibility;
- unknown external consumers;
- approximate rather than falsely precise measurement.

Do not require a specific MCU, RTOS, storage implementation, file format, protocol, manufacturing system, build system,
test framework, issue tracker, or repository layout.

## 37. Terminology and Precision Guardrails

Use terms precisely:

- Change Radius: amount of system surface that must change, be reviewed, or be retested when one decision changes;
- affected surface: code, behavior, contract, artifact, tool, workflow, owner, evidence, or released compatibility
  implicated by the change;
- consumer: any component, tool, workflow, team, or released version relying on the old meaning;
- required radius: affected surface that must move to preserve one coherent product decision;
- accidental radius: affected surface caused by leaked or duplicated knowledge;
- direct radius: intentionally edited surface;
- indirect radius: known consumers or assumptions affected without direct editing;
- latent radius: hidden or uncertain coupling discovered outside obvious paths;
- containment: reducing accidental spread or making propagation explicit;
- sequencing: ordering changes to preserve compatibility and control risk;
- residual radius: affected surface intentionally left for later or accepted for the current commitment.

The chapter must avoid these misleading statements:

- appending a structure field is automatically backward-compatible;
- incrementing a schema version solves migration;
- old firmware can safely ignore every new field;
- rollback is safe if upgrade succeeds;
- tests in one repository cover manufacturing tools;
- no file change means no review is needed;
- all consumers can be found with code search;
- a compatibility flag has one meaning everywhere;
- dual-write is always safe;
- reset-to-default is an acceptable migration by default;
- a smaller diff means lower release risk;
- a larger radius proves bad design;
- all radius can be known before implementation;
- passing regression tests proves unknown consumers do not exist.

## 38. Failure Modes to Avoid

The later draft must not become:

- a file-impact checklist;
- a project-management chapter;
- a ticket-decomposition guide;
- a static-analysis tools survey;
- a release-management chapter;
- a schema-migration tutorial;
- a manufacturing chapter;
- a product-line architecture chapter;
- a test-strategy handbook;
- a dependency graph tutorial;
- Chapter 14 repeated;
- Chapter 16 written early;
- Chapter 17 written early;
- Chapter 18 written early;
- a claim that Change Radius must always be minimized;
- a numerical scoring framework with false precision;
- an argument for redesign before every cross-cutting change;
- a generic "communicate more" chapter.

## 39. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete embedded calibration-record change;
- the Principal Engineer move recasts the work from a file edit to a changed product decision with affected surfaces;
- `VOCAB-001` and `METRIC-001` are central without assigning a primary concept;
- implementation, review, retest, migration, compatibility, and release-observation surfaces are distinguished;
- required, accidental, direct, indirect, latent, unknown, and residual radius are used as chapter-local analytical
  phrases only;
- approximate measurement is used without numerical scoring;
- uncertainty changes sequencing and commitment rather than stopping all work;
- containment and management actions follow from the map;
- Chapter 14 boundary placement remains a premise, not the main topic;
- Chapters 16 through 19 remain out of scope except for handoff boundaries;
- the exercise ends in one explicit map, one sequencing decision, one containment action, and one accepted residual
  uncertainty;
- the ADR makes a genuine architecture and sequencing decision;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 40. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into project management, release management, schema migration, manufacturing, or a tools
survey.

Canon Review should verify that Chapter 15 remains a Part III practice chapter with no forced primary concept, materially
uses `VOCAB-001` and `METRIC-001` as paired foundations, preserves the registered relationship set, and does not imply a
new PEAK artifact, metric, or vocabulary term.

Technical Review should focus on persistent records, migration and downgrade behavior, firmware and service-tool
compatibility, manufacturing paths, test fixtures, diagnostics, callbacks, timing assumptions, unknown consumers,
temporary compatibility, and the difference between diff size and affected surface.

Freeze Review should confirm that Chapter 15 remains the second Part III practice chapter, keeps the manuscript
architecture intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and
leaves the reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
calibration data, product type, schema details, service-tool behavior, migration sequence, and final notebook wording
while preserving the Change Radius thesis, story shape, PEAK map, and chapter boundaries.
