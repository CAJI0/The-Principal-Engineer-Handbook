# CHAPTER-025 Canonical Brief: Reference Project Walkthrough

## 1. Metadata

- Stable ID: `CHAPTER-025`.
- Title: `Reference Project Walkthrough`.
- Part: Part IV - Building a Product.
- Chapter number: 25.
- Expected manuscript path: `book/04-building-a-product/25-reference-project-walkthrough.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-025-reference-project-walkthrough.md`.
- Branch: `chapter25`.
- Verified baseline `origin/main`: `56c90ec7cfec4e7fe0d839b0f89d8ce8825d2268`.
- Baseline evidence: PR #26 squash commit,
  `Chapter 24: Release Discipline and Upgrade Paths (#26)`.
- Chapter 24 feature Freeze commit checked for tree equivalence:
  `fab9ea9ec9eda79123280f90550e45f50a1db3a6`.
- Canonical predecessor: `CHAPTER-024` - Release Discipline and Upgrade Paths.
- Part position: sixth and final chapter of Part IV - Building a Product.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 25 is a synthesis walkthrough and should be carried by a relationship set rather than
  a new primary-concept field.
- Central chapter-local practice: walking one embedded product through a connected product decision chain.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `56c90ec7cfec4e7fe0d839b0f89d8ce8825d2268`.
- That baseline is the PR #26 squash commit,
  `Chapter 24: Release Discipline and Upgrade Paths (#26)`.
- The squash commit has parent `f2550e7a243d794960a2ef48fc6e40ed24269c05` and is an ancestor of current
  `origin/main`.
- The Chapter 24 feature-branch Freeze commit `fab9ea9ec9eda79123280f90550e45f50a1db3a6` remains tree-equivalent for
  the checked Chapter 24 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-024` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-024` is the fifth Part IV chapter and is canonical.
- The table of contents places `Reference Project Walkthrough` sixth and final in Part IV - Building a Product.
- `book/04-building-a-product/README.md` exists and remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-025` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 25 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter25` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part IV Role

Chapter 25 closes Part IV by showing how the product-building chapters work together on one small embedded reference
project. It should not summarize Chapters 20 through 24 as separate checklists. It should let the reader watch one
product move from prototype evidence to a limited, supportable release baseline.

The chapter should make visible that:

- Chapter 20 creates the first product-baseline question;
- Chapter 21 tests that baseline against manufacturing and field reality;
- Chapter 22 turns product difference into explicit supported and unsupported combinations;
- Chapter 23 makes field evidence support-safe and decision-ready;
- Chapter 24 turns release and upgrade behavior into explicit promises.

Chapter 25 prepares the transition into Part V by showing that product decisions become shared organizational memory.
It must not write Part V early.

## 4. Canonical Purpose

Prepare Chapter 25 to teach a compact reference-project walkthrough that connects the product-building decisions from
Part IV.

Candidate thesis for the future manuscript:

> A product architecture is not proven by one clean decision. It is proven by a connected chain of product decisions
> that stay owned, testable, diagnosable, releasable, and supportable over time.

The chapter should move the reader away from treating prototype-to-product work, manufacturing, variants,
observability, and release as unrelated checklists.

The core question should become:

> If we had to take one embedded product from prototype to supported release, which architecture decisions would we
> make, record, test, review, freeze, and revisit?

The chapter should synthesize existing canon. It must not introduce a new theory, new PEAK concept, or new artifact.

## 5. Primary-Concept Resolution

Chapter 25 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Recent practice
chapters are carried by material relationship sets. Chapter 25 follows that convention.

The central chapter-local practice is a product decision chain. That phrase is useful prose for the future manuscript
but must not become a new PEAK law, vocabulary term, artifact, ritual, metric, smell, anti-pattern, failure story, or
registry field.

Do not create PEAK concepts such as Reference Project, Field Sensor Gateway, Product Baseline, Product Decision Chain,
Pilot Release, Product Memory, Supportable Baseline, or Walkthrough.

## 6. Central Thesis

A product becomes supportable when its decisions connect. Prototype assumptions, manufacturing identity, calibration,
configuration, variants, event meanings, diagnostics, release artifacts, upgrade paths, and recovery behavior must form
a chain of named promises, owners, evidence, records, and revisit triggers.

Approved supporting formulation for the future draft:

> Build the product as a chain of explicit decisions. Each decision should name the promise it creates, the owner who
> keeps it true, the evidence that supports it, and the next condition that should make the team revisit it.

This formulation is chapter-level language. Do not register it as new canon.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. A prototype-to-product checklist, manufacturing checklist, variant checklist, observability checklist, and release
   checklist can be completed independently.
2. A reference project walkthrough should be a code tutorial or product specification.
3. Product baseline means every future variant is already solved.
4. Observability is a logging layer rather than evidence for product decisions.
5. Release readiness means the current image installs on the latest lab unit.
6. Records are paperwork after decisions are done.
7. A pilot baseline is either perfect or irresponsible.

By the end of the chapter, the reader should be able to:

1. trace one prototype assumption through product reality;
2. name the owner of identity, calibration, configuration, variant, event meaning, and release-critical state;
3. identify which interfaces have become promises;
4. state supported and unsupported combinations;
5. connect diagnostics to support-safe decisions;
6. define one supported upgrade path and one deferred path;
7. choose the right record for a consequential product decision;
8. decide when Architecture Review or a narrow Architecture Freeze is justified;
9. leave a discoverable baseline future engineers can reuse.

## 8. Reference Project Shape

Use a small embedded reference project:

`The Field Sensor Gateway`

The project should be generic enough to transfer across domains and concrete enough to feel real.

It may include:

- one MCU-based controller;
- one sensor or measurement input;
- one gateway, radio, or network dependency;
- local non-volatile configuration;
- serial identity and calibration data;
- two hardware revisions;
- two product packages or regional variants;
- a service-tool connection;
- an event log or Event Catalog;
- a firmware release and upgrade from v1.0 to v1.1;
- a field issue that forces a decision.

Do not require a specific MCU, RTOS, board, sensor, radio, cloud service, boot loader, configuration store, file system,
manufacturing system, CI/CD system, service tool, or issue tracker.

## 9. Walkthrough Structure

The future manuscript should walk the reference project through the Part IV sequence.

### Prototype to Product

Show what the prototype proved, what assumptions it hid, which shortcuts are kept, replaced, expired, or accepted, what
becomes a product promise, and which owners are assigned.

### Manufacturing and Field Reality

Show identity, calibration, provisioning, fixture and service boundaries, support-safe diagnosis, reset or recovery
expectations, and field constraints.

### Configuration, Variants, and Product Line

Show configuration values as owned state, supported variants as promises, unsupported combinations, defaults,
validation, migration, and support meaning.

### Observability

Show events or diagnostics that support decisions, reset and update context, version/configuration/variant identity,
support-safe messages, Event Catalog use, and avoidance of Event Explosion.

### Release and Upgrade Path

Show one supported source-to-target path, one unsupported or deferred path, release-critical state owners,
compatibility and support horizon, evidence required, and a narrow Architecture Freeze.

Chapter 25 is a connection walkthrough rather than a summary of Chapters 20 through 24. Its scope is a reference
project that shows how their decisions connect.

## 10. Part IV Closure

Chapter 25 is the capstone of Part IV. It should end the part by giving the reader a reusable mental walkthrough:

1. start with what the prototype proved;
2. expose what product reality changed;
3. decide what state, interface, dependency, configuration, diagnostic, or release path became a promise;
4. assign an owner;
5. gather evidence;
6. record the decision;
7. review or freeze only where the Change Radius and release risk justify it;
8. revisit the decision when the product learns something new.

The chapter should close with a supported product baseline, not a perfect system.

## 11. In-Scope and Out-of-Scope

### In Scope

Chapter 25 covers:

- one small embedded reference product;
- a successful prototype moving toward a pilot release baseline;
- identity, calibration, configuration, variants, diagnostics, release, update, recovery, and support obligations;
- connected decisions across Chapters 20 through 24;
- ADRs, RFCs, Decision Journal entries, Mistake Ledger entries, Event Catalog entries, and Architecture Ledger rows as
  existing records;
- Architecture Review where Change Radius is broad;
- narrow Architecture Freeze for upgrade-path validation;
- unsupported combinations and deferred paths;
- a discoverable trail for support and future engineers.

### Explicitly Out of Scope

Do not turn Chapter 25 into:

- a tutorial implementation;
- a product specification;
- an MCU, RTOS, boot loader, cloud, protocol, or vendor guide;
- a code walkthrough;
- a product-management case study;
- a manufacturing-process guide;
- a CI/CD or release-management cookbook;
- a recap chapter that repeats the full teaching of Chapters 20 through 24;
- an early Part V organizational-leadership chapter;
- a new PEAK concept proposal.

## 12. Recommended Embedded-Systems Story

### Working Title

One Product, Five Pressure Points

### Starting System

A small field sensor gateway has a successful prototype. It reports sensor readings over a network, stores
configuration locally, has a simple service tool, and can be updated in the lab.

The team wants to take it to a supported pilot release.

### Pressure Points

1. Prototype shortcut:
   - hard-coded reporting interval;
   - manual calibration;
   - developer-only debug logs;
   - update tested only from latest build.
2. Manufacturing and field:
   - manufacturing needs serial identity and calibration flow;
   - second board revision changes sensor offset;
   - support needs to diagnose communication failure without a debugger.
3. Configuration and variants:
   - regional reporting interval and radio option become product variants;
   - one customer asks for a special timeout;
   - supported and unsupported combinations must be named.
4. Observability:
   - field units stop reporting after update;
   - event meanings are too generic;
   - reset reason, active version, configuration fingerprint, variant, and boundary outcome must be preserved.
5. Release and upgrade:
   - v1.1 changes configuration schema;
   - v1.0 and v1.0.2 field units exist;
   - one hardware revision needs a different migration path;
   - rollback would lose calibration unless state ownership is fixed.

### Principal Engineer Intervention

Instead of solving each pressure point separately, the Principal Engineer creates a connected product decision chain:

- classify prototype assumptions;
- assign owners to identity, calibration, configuration, variant promises, event meaning, and release-critical state;
- define product contracts and unsupported combinations;
- create minimal Event Catalog entries;
- record consequential choices in ADRs, RFCs, Decision Journal entries, Architecture Ledger rows, or Mistake Ledger
  entries where appropriate;
- use Architecture Review where the Change Radius is broad;
- use Architecture Freeze narrowly for upgrade-path validation;
- keep the product simple enough to understand;
- leave a discoverable trail for support and future engineers.

The story should end with a supportable pilot baseline, not a perfect system.

## 13. Expected Discussion Arc

1. A reference project is useful when it connects decisions, not when it tries to be universal.
2. The Field Sensor Gateway prototype proves useful behavior under prototype conditions.
3. The first product move is to expose assumptions and decide which become promises.
4. Manufacturing and field reality force identity, calibration, provisioning, service, and recovery ownership.
5. Configuration and variants force the team to name supported and unsupported combinations.
6. Observability turns field behavior into decision evidence that support can use.
7. Release and upgrade paths turn version movement into explicit state-transition promises.
8. Records keep the decision chain discoverable after the pilot pressure passes.
9. Review and freeze are scoped tools, not blanket ceremonies.
10. Part IV closes when the product baseline is owned, testable, diagnosable, releasable, supportable, and ready for
    review.

These are intellectual progression points, not mandatory manuscript headings.

## 14. Boundaries With Earlier Part IV Chapters

Chapter 25 uses Chapters 20 through 24 as the steps of one walkthrough. It should not retell their full lessons.

- Chapter 20 owns the prototype-to-product transition.
- Chapter 21 owns manufacturing and field reality.
- Chapter 22 owns configuration, variants, and product lines.
- Chapter 23 owns embedded observability.
- Chapter 24 owns release discipline and upgrade paths.

Chapter 25 may show a small example of each practice in the same product. It must not expand any one practice into the
full chapter again.

## 15. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating them:

- Chapters 7 through 10 supply state ownership, API promises, dependency decisions, and time dependencies.
- Chapter 13 supplies evidence before confidence.
- Chapter 15 supplies Change Radius.
- Chapter 16 supplies failure and recovery judgment.
- Chapter 17 supplies ADR, RFC, and Decision Journal practice.
- Chapter 18 supplies Architecture Review.
- Chapter 19 supplies Architecture Freeze.

The future manuscript should show these tools in use inside the Field Sensor Gateway. It should not reteach Part II or
Part III.

## 16. Applicability

Chapter 25 is most useful when:

- a prototype is moving toward a pilot or first supported release;
- manufacturing, support, variants, diagnostics, and release are beginning to interact;
- product decisions are scattered across team memory, scripts, issue comments, and partial records;
- the team needs a small example of how to connect Part IV practices;
- a Principal Engineer must help the team decide what to own now and what to revisit later.

Not every product needs every artifact or ritual. The walkthrough should teach judgment about connection and scale.

## 17. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- one reference project proves universal correctness;
- every product needs the same records;
- every decision needs every record type;
- every Part IV practice has equal weight in every situation;
- a pilot baseline means the product is complete forever;
- supportable means risk-free;
- a walkthrough replaces validation;
- Architecture Review or Architecture Freeze should be used for every product decision;
- unsupported combinations are always failures;
- simplicity means ignoring product obligations.

The chapter should allow a limited pilot baseline when risk is visible, owned, bounded, evidenced, and tied to a revisit
trigger.

## 18. Violation Patterns

The future draft should make these violations visible:

- the prototype is shipped because it worked once;
- identity, calibration, configuration, and update state have no single owner;
- regional behavior is added as a local flag instead of a supported variant promise;
- unsupported combinations remain implicit;
- a debug log is treated as field observability;
- event meanings are generic or unstable;
- firmware, service tool, fixture, support notes, and release package depend on silent assumptions;
- a temporary workaround survives without owner, expiration, or decision;
- release evidence covers only the latest lab path;
- rollback is assumed safe without checking preserved state;
- architecture records are written after nobody remembers why the decision was made;
- the chapter drifts into implementation detail rather than decision connection.

Do not create a new anti-pattern ID.

## 19. Engineering Principle Target

Target principle for the future draft:

> Build the product as a chain of explicit decisions. Each decision should name the promise it creates, the owner who
> keeps it true, the evidence that supports it, and the next condition that should make the team revisit it.

The principle should imply these questions:

1. What did the prototype actually prove?
2. Which product reality changed the architecture?
3. Which state needs an owner?
4. Which interface became a promise?
5. Which dependency became a support obligation?
6. Which configuration difference is a supported variant?
7. Which unsupported combination must be stated?
8. Which field failure must explain itself?
9. Which upgrade path is promised?
10. Which evidence supports the release?
11. Which decision needs review, freeze, or a ledger entry?

The final manuscript may shorten the list for reader rhythm.

## 20. Architecture Exercise Target

### Working Title

`Walk One Product Decision Chain`

Ask the reader to choose a small product or subsystem and trace one connected decision chain:

- prototype assumption;
- manufacturing or field reality;
- configuration or variant decision;
- observable event or diagnostic;
- release or upgrade path;
- owner;
- promise;
- evidence;
- record;
- review or freeze trigger;
- revisit condition.

End with five outputs:

1. one product promise;
2. one owner;
3. one evidence requirement;
4. one record to update;
5. one revisit trigger.

Do not create a new canonical artifact for this exercise.

## 21. Chapter-Local ADR Brief

### Working Title

Set the Field Sensor Gateway Product Baseline for Pilot Release

### Context

- The prototype works.
- Manufacturing needs identity and calibration.
- Field support needs diagnostic evidence.
- Regional and hardware variants exist.
- v1.1 changes configuration schema.
- Support and future engineers need a discoverable baseline.

### Decision

- Accept a limited supported baseline for pilot release.
- Define supported hardware revision, configuration schema, regional variant, service-tool version, and source-to-target
  upgrade path.
- Explicitly reject or defer unsupported combinations.
- Assign owners for identity, calibration, configuration, variant promises, event meanings, and release-critical state.
- Record core decisions in ADRs, RFCs, Decision Journal entries, Architecture Ledger rows, Event Catalog entries, or
  Mistake Ledger entries as appropriate.
- Run Architecture Review for broad Change Radius decisions.
- Apply Architecture Freeze narrowly to upgrade-path validation.
- Use Mistake Ledger entries for escaped assumptions discovered during pilot.

### Alternatives Considered

- Ship the prototype baseline.
- Wait for a perfect product-line architecture.
- Support every requested configuration.
- Defer observability and upgrade evidence until after pilot.
- Split every customer into separate firmware.
- Freeze the entire architecture until all unknowns are resolved.

### Consequences

Benefits include a supportable pilot baseline, clearer ownership, fewer hidden promises, explicit unsupported paths,
stronger field diagnosis, and more reusable product memory.

Costs include more validation work, more visible deferrals, explicit ownership work, coordination across firmware,
manufacturing, service, support, and release, and extra care keeping records discoverable.

The ADR must make a real story-local architecture decision. It must not reduce to "do the walkthrough" or "ship the
pilot."

## 22. PEAK Concept Map

### Concepts Inspected

- `FAILURE-003` - The Successful Prototype.
- `FAILURE-005` - The Release We Should Have Delayed.
- `FAILURE-002` - One Lost Packet.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `VOCAB-002` - Weak Signal.
- `VOCAB-006` - Architecture Freeze.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.
- `SMELL-004` - Hidden State.
- `SMELL-001` - Silent Coupling.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-006` - Temporary Solution.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-002` - HAL Everywhere.
- `ANTIPATTERN-005` - Callback Hell.

### Selected Concepts

- `FAILURE-003` - The Successful Prototype: material because the walkthrough begins with a successful prototype being
  promoted toward a product baseline.
- `FAILURE-005` - The Release We Should Have Delayed: material because the release pressure tests whether unresolved
  upgrade and support assumptions become field risk.
- `FAILURE-002` - One Lost Packet: material because the gateway's reporting, update, and recovery path can fail through
  missing or late communication evidence.
- `LAW-001` - Every State Has One Owner: material because identity, calibration, configuration, variant, event meaning,
  update, and recovery state need clear authority.
- `LAW-002` - Every API Is a Promise: material because service-tool commands, diagnostics, variant behavior, and
  release interfaces become promises.
- `LAW-003` - Time Is a Dependency: material because reporting intervals, update windows, event ordering, retry
  behavior, and support horizons depend on time.
- `LAW-004` - Simplicity Is a Feature: material because the product baseline should stay small enough to understand
  instead of growing speculative variant machinery.
- `LAW-005` - Evidence Before Confidence: material because prototype, manufacturing, observability, variant, and
  release confidence must follow evidence.
- `LAW-006` - Unused Flexibility Is Waste: material because the walkthrough rejects perfect product-line architecture
  and unsupported future combinations.
- `LAW-007` - Every Dependency Is a Decision: material because radio/network dependencies, service tools, manufacturing
  fixtures, boot/update mechanisms, and vendor libraries import product obligations.
- `VOCAB-001` - Change Radius: material because the chapter decides when a product decision needs review, record, or
  freeze based on affected surface.
- `METRIC-001` - Change Radius: material because the exercise should estimate affected firmware, manufacturing,
  service, support, diagnostics, release, and field surfaces.
- `METRIC-003` - Discoverability: material because the baseline must be findable by support and future engineers.
- `METRIC-004` - API Stability: material because service-tool, diagnostic, configuration, event, and upgrade promises
  need stable meaning.
- `ARTIFACT-001` - ADR: material because the baseline decision needs a durable decision record.
- `ARTIFACT-002` - RFC: material because broad variant, service-tool, or upgrade changes may need review across owners.
- `ARTIFACT-003` - Decision Journal: material because smaller pilot risks, evidence gaps, and revisit triggers need
  lightweight records.
- `ARTIFACT-004` - Mistake Ledger: material because escaped assumptions discovered during pilot should become reusable
  engineering memory.
- `ARTIFACT-005` - Event Catalog: material because support-safe event meanings are part of the walkthrough.
- `ARTIFACT-006` - Architecture Ledger: material because active baseline decisions, owners, and review dates should be
  discoverable.
- `RITUAL-001` - Architecture Review: material because broad Change Radius decisions need review before hardening.
- `RITUAL-002` - Architecture Freeze: material because the upgrade-path validation scope may need a narrow, temporary
  freeze.
- `SMELL-004` - Hidden State: material because hidden identity, calibration, configuration, update, and recovery state
  can break the baseline.
- `SMELL-001` - Silent Coupling: material because firmware, fixture, service tool, release package, diagnostics, and
  support notes can share unstated assumptions.
- `SMELL-005` - Platform Leakage: material because low-level radio, board, driver, or update details can leak into
  product promises.
- `SMELL-006` - Event Explosion: material because generic or multiplying event meanings can make field diagnosis
  unusable.
- `ANTIPATTERN-006` - Temporary Solution: material because prototype shortcuts and pilot workarounds need owners,
  expiration conditions, or explicit decisions.
- `ANTIPATTERN-003` - Global Configuration: material because broad flags can blur regional variants, hardware
  revisions, migration, diagnostics, and support behavior.

### Rejected Concepts

- `VOCAB-002` and `ARTIFACT-007`: useful if the pilot story emphasizes weak early signals, but the canonical
  relationship set is already carried by Decision Journal, Mistake Ledger, Event Catalog, Architecture Ledger,
  Architecture Review, and Architecture Freeze.
- `VOCAB-006`: relevant through `RITUAL-002`, but the walkthrough needs the practice of a scoped freeze more than an
  additional vocabulary edge.
- `ANTIPATTERN-002`: relevant to hardware abstraction mistakes, but Chapter 25 should not drift into a HAL design
  walkthrough.
- `ANTIPATTERN-005`: relevant to asynchronous update logic, but the chapter should keep callback ordering as a local
  technical risk rather than a graph edge.
- `METRIC-005` and `VOCAB-007`: useful for Part V operating health, but Chapter 25 should not introduce the
  organizational-health frame early.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as reference project, Field Sensor Gateway, product baseline, product decision chain, pilot release,
supportable baseline, product memory, and walkthrough remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-025` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-025
  type: illustrates
  to: FAILURE-003

- from: CHAPTER-025
  type: references
  to: FAILURE-005

- from: CHAPTER-025
  type: references
  to: FAILURE-002

- from: CHAPTER-025
  type: references
  to: LAW-001

- from: CHAPTER-025
  type: references
  to: LAW-002

- from: CHAPTER-025
  type: references
  to: LAW-003

- from: CHAPTER-025
  type: references
  to: LAW-004

- from: CHAPTER-025
  type: references
  to: LAW-005

- from: CHAPTER-025
  type: references
  to: LAW-006

- from: CHAPTER-025
  type: references
  to: LAW-007

- from: CHAPTER-025
  type: references
  to: VOCAB-001

- from: CHAPTER-025
  type: references
  to: METRIC-001

- from: CHAPTER-025
  type: references
  to: METRIC-003

- from: CHAPTER-025
  type: references
  to: METRIC-004

- from: CHAPTER-025
  type: references
  to: ARTIFACT-001

- from: CHAPTER-025
  type: references
  to: ARTIFACT-002

- from: CHAPTER-025
  type: references
  to: ARTIFACT-003

- from: CHAPTER-025
  type: references
  to: ARTIFACT-004

- from: CHAPTER-025
  type: references
  to: ARTIFACT-005

- from: CHAPTER-025
  type: references
  to: ARTIFACT-006

- from: CHAPTER-025
  type: references
  to: RITUAL-001

- from: CHAPTER-025
  type: references
  to: RITUAL-002

- from: CHAPTER-025
  type: references
  to: SMELL-004

- from: CHAPTER-025
  type: references
  to: SMELL-001

- from: CHAPTER-025
  type: references
  to: SMELL-005

- from: CHAPTER-025
  type: references
  to: SMELL-006

- from: CHAPTER-025
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-025
  type: references
  to: ANTIPATTERN-003
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 23. Required Reader-Facing Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 25 role:

- Opening Quote: establish that a product is made of connected promises.
- Story: walk the Field Sensor Gateway through the five Part IV pressure points.
- Discussion: show how product decisions connect across prototype, manufacturing, variants, observability, release,
  records, review, and freeze.
- Engineering Principle: anchor the product decision chain.
- Architecture Exercise: walk one product decision chain.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local pilot baseline decision.
- Editor's Commentary: explain how Chapter 25 closes Part IV and prepares Part V without writing it early.

## 24. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A product is a chain of promises.
- A baseline is useful only when its assumptions are findable.
- A good walkthrough leaves decisions people can reuse.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 25. Technical Credibility Requirements

The future draft must treat the following accurately:

- embedded prototype assumptions;
- serial identity;
- calibration ownership;
- hardware revision variation;
- local configuration and migration;
- service-tool behavior;
- field diagnostics;
- event cataloging;
- network or radio dependency;
- version and variant fingerprints;
- release artifact identity;
- upgrade paths from existing field versions;
- rollback, retry, recovery, and forward-fix at a conceptual level;
- manufacturing and service boundaries;
- support-safe language;
- constrained memory, time, and storage;
- architecture records as decision aids, not paperwork for every minor choice.

Do not require a specific MCU, RTOS, board, sensor, radio, cloud, boot loader, configuration store, service tool,
manufacturing system, issue tracker, or release process.

## 26. Terminology and Precision Guardrails

Use terms precisely:

- Reference project: a small fictional product used to connect decisions, not a specification or reusable
  implementation.
- Product baseline: the bounded set of supported product promises for the story, not a claim that every future variant
  is solved.
- Product decision chain: chapter-local prose for connected promises, owners, evidence, records, and revisit triggers.
- Supported variant: a promised combination that the product can explain, test, release, and support.
- Unsupported combination: a named combination the product deliberately rejects or defers.
- Support-safe diagnostic: evidence that a support path can interpret without developer-only context.
- Revisit trigger: a condition that causes a decision to be reviewed again.

Avoid misleading statements:

- A reference project proves universal correctness.
- Every product needs the same artifacts.
- Every decision needs every record type.
- A pilot baseline is production-ready forever.
- A supportable baseline has no risk.
- A walkthrough replaces validation.
- All Part IV practices must be applied with equal weight.
- Part V leadership practices should be introduced here.

## 27. Failure Modes to Avoid

The later draft must not become:

- a tutorial implementation;
- a product specification;
- an MCU, RTOS, boot loader, cloud, protocol, or vendor guide;
- a code walkthrough;
- a product-management case study;
- a manufacturing-process guide;
- a CI/CD or release-management cookbook;
- a recap of Chapters 20 through 24;
- a Part V organizational chapter written early;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 28. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story uses one small embedded Field Sensor Gateway or equivalent reference product;
- the story includes prototype assumptions, manufacturing identity, calibration, hardware revision variation,
  configuration, variants, observability, release, upgrade, recovery, and support pressure;
- the Principal Engineer move connects the pressure points into one product decision chain;
- the chapter closes Part IV without merely summarizing Chapters 20 through 24;
- the manuscript does not become a tutorial implementation, product specification, vendor guide, code walkthrough, or
  product-management case study;
- no primary PEAK concept is assigned unless a later editor decision changes repository convention;
- selected PEAK concepts are materially present if the registered relationship set is kept;
- `FAILURE-003` is materially illustrated by the successful-prototype starting point;
- release pressure and communication/recovery failure are present if `FAILURE-005` and `FAILURE-002` edges are kept;
- supported and unsupported combinations are explicit;
- one supported upgrade path and one deferred or unsupported path are named;
- event meanings, identity, calibration, configuration, variant, and release-critical state have owners;
- ADR, RFC, Decision Journal, Mistake Ledger, Event Catalog, and Architecture Ledger appear only where appropriate;
- Architecture Review and Architecture Freeze are scoped, not blanket rituals;
- the exercise ends with one product promise, one owner, one evidence requirement, one record to update, and one revisit
  trigger;
- the ADR makes a genuine story-local pilot-baseline decision;
- exactly three Principal's Notebook observations are present;
- Part V is prepared only by transition, not written early;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 29. Review Handoff Notes

Editorial Review should check whether the story reads as one connected walkthrough rather than a list of chapter
summaries. It should also check that the reference product stays concrete without becoming an implementation guide.

Canon Review should verify that Chapter 25 remains no-primary, preserves only material outgoing relationships, avoids
new PEAK concepts, and keeps the product decision chain as chapter-local prose.

Technical Review should focus on realistic embedded constraints: identity, calibration, hardware revisions,
configuration migration, variants, service tools, event meanings, radio/network dependencies, release artifact
identity, upgrade paths, rollback limits, retry, recovery, forward-fix, manufacturing and service boundaries, and
support-safe evidence.

Freeze Review should confirm that Chapter 25 is the sixth and final Part IV chapter, keeps the manuscript architecture
intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, closes Part IV, and
does not write Part V early.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
reference product details, pressure points, baseline definition, event names, variant names, upgrade paths, records,
review triggers, freeze scope, ADR wording, and notebook wording while preserving the synthesis role, PEAK map, and
chapter boundaries.
