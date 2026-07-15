# CHAPTER-022 Canonical Brief: Configuration, Variants, and Product Lines

## 1. Metadata

- Stable ID: `CHAPTER-022`.
- Title: `Configuration, Variants, and Product Lines`.
- Part: Part IV - Building a Product.
- Chapter number: 22.
- Expected manuscript path:
  `book/04-building-a-product/22-configuration-variants-and-product-lines.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-022-configuration-variants-and-product-lines.md`.
- Branch: `chapter22`.
- Verified baseline `origin/main`: `4176829b64f5d920349fe27cb05cfaf654c8d306`.
- Baseline evidence: PR #23 squash commit,
  `Chapter 21: Designing for Manufacturing and Field Reality (#23)`.
- Chapter 21 feature Freeze commit checked for tree equivalence:
  `7551641be74b13c97a5360174043d49004f0c3f4`.
- Canonical predecessor: `CHAPTER-021` - Designing for Manufacturing and Field Reality.
- Part position: third chapter of Part IV - Building a Product.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 22 is carried by a material relationship set and chapter-local framing rather than by a
  new primary-concept field.
- Central anchor or practice: none registered. Configuration, variant, and product line are chapter-local working
  distinctions, not new PEAK concepts.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `4176829b64f5d920349fe27cb05cfaf654c8d306`.
- That baseline is the PR #23 squash commit, `Chapter 21: Designing for Manufacturing and Field Reality (#23)`.
- The squash commit is an ancestor of current `origin/main` and has parent
  `c0c3bf50d869e3fcb58c7930ffd7da71c6589c2a`.
- The Chapter 21 feature-branch Freeze commit `7551641be74b13c97a5360174043d49004f0c3f4` remains tree-equivalent for
  the checked Chapter 21 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-021` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-021` is the second Part IV chapter and is canonical.
- The table of contents places `Configuration, Variants, and Product Lines` third in Part IV - Building a Product.
- `book/04-building-a-product/README.md` exists and remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-022` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 22 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter22` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part IV Role

Chapter 22 follows Chapter 21 by showing what happens after manufacturing and field reality are visible: product
differences must be modeled deliberately before they become accidental architecture.

Chapter 20 moved the reader from prototype evidence to product obligations. Chapter 21 made manufacturing and field
assumptions explicit. Chapter 22 should show that configuration values, product variants, customer packages, hardware
options, regional behavior, licensed capabilities, and product-line boundaries are architecture decisions when other
teams and customers rely on them.

The chapter must not become a product-management chapter, SKU spreadsheet tutorial, feature-flag operations handbook,
configuration database design, build-system guide, release-train process, or testing-matrix tutorial. It should teach
architecture judgment for embedded product variation.

## 4. Canonical Purpose

Prepare Chapter 22 to teach that configuration and variants are architecture decisions, not just parameter files,
compile-time defines, product labels, or late sales requests.

Candidate thesis for the future manuscript:

> Every supported variant is an architectural promise. Configuration is the mechanism by which that promise becomes
> behavior.

The chapter should move the reader away from treating configuration and variants as:

- a JSON file problem;
- a compile-time define list;
- a SKU spreadsheet;
- a UI setting collection;
- a late-stage product request;
- a sales-only concern;
- a firmware-only concern;
- a build-system detail;
- an unbounded feature-flag system;
- a way to avoid making architecture decisions.

The core question should become:

> Which differences are product variants, which are configuration, which are unsupported combinations, who owns them,
> and what promises must remain stable across the product line?

## 5. Primary-Concept Resolution

Chapter 22 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Chapter 22 follows that
convention and should be carried by its exact relationship set.

Configuration, variant, product line, product package, supported combination, unsupported combination, configuration
owner, variant contract, compatibility matrix, feature flag, and SKU are necessary prose terms for the chapter, but none
becomes a PEAK vocabulary concept, law, metric, artifact, ritual, smell, anti-pattern, failure story, or primary
concept during this registration.

## 6. Central Thesis

Configuration is owned product state. A supported variant is a product promise. A product line is the architecture that
keeps shared behavior stable while allowing intentional differences to remain bounded, testable, discoverable, and
supportable.

Approved supporting formulation for the future draft:

> Treat configuration as owned state and variants as product promises. Keep the product line small enough to understand,
> explicit enough to test, and discoverable enough to support.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. configuration is just a file, flag, define, or database row;
2. a variant is a product-management label rather than an architecture promise;
3. adding one more flag is cheaper than naming a product-line decision;
4. defaults can be copied between products without a decision record;
5. supported combinations can be inferred from what has shipped;
6. a customer exception can remain temporary because everyone remembers it;
7. tests of a few examples prove the product line;
8. service, manufacturing, update, recovery, and release effects can be handled later.

By the end of the chapter, the reader should be able to:

1. classify a product difference as configuration, variant, implementation detail, temporary exception, or unsupported
   combination;
2. assign ownership for configuration values and variation points;
3. define defaults, validation, migration, and source of truth for configuration;
4. identify which variant promises affect customers, manufacturing, service, release, update, recovery, and support;
5. name shared core, variation points, supported combinations, and intentionally unsupported combinations;
6. map the Change Radius of adding a new variant;
7. record consequential variation decisions in ADRs, RFCs, Decision Journal entries, or an Architecture Ledger;
8. decide which variation points need Architecture Review or temporary freeze before release or manufacturing.

## 8. Configuration, Variants, and Product Lines

The future manuscript should use these as working distinctions, not a rigid taxonomy.

Configuration means runtime or deployment-time values that select behavior inside an existing product contract.
Configuration must have owner, scope, validation, default, migration path, storage or source of truth, and support
meaning. It is not a dumping ground for unfinished architecture.

A variant is a supported product difference with an explicit promise. A variant may involve hardware, firmware, region,
customer package, licensed capability, manufacturing flow, service-tool behavior, diagnostics, release packaging, update
or recovery compatibility, or support horizon. It must be discoverable, testable, supportable, and bounded.

A product line is a family of related products that share architecture but differ intentionally. A product line needs
decisions about shared core, variation points, compatibility, test scope, release support, and lifecycle ownership.

The chapter should help the reader classify the difference before deciding where it belongs.

## 9. Good and Bad Variation

Good variation has:

- a named owner;
- bounded scope;
- a clear default;
- validation;
- compatibility meaning;
- support meaning;
- visible records and tests;
- discoverable supported combinations;
- explicit unsupported combinations;
- resistance to hidden coupling and accidental combination growth.

Bad variation includes:

- global flags with unclear owner;
- compile-time defines that change API meaning without a versioned promise;
- product behavior controlled only by a sales spreadsheet;
- manufacturing values that support cannot read;
- configuration copied between products without a decision record;
- variants that are not testable;
- temporary customer exceptions that become product-line behavior;
- debug options shipped as product behavior;
- hardware differences hidden behind the same software promise;
- configuration that bypasses state ownership.

The future manuscript should show that variation is not automatically bad. Unowned variation is the danger.

## 10. Configuration Ownership

Configuration should be treated as state.

The future manuscript should require the reader to ask:

- who owns each configuration value;
- who may change it;
- when it may change;
- where it is stored or sourced;
- how it is validated;
- what default means;
- how it migrates;
- how it is diagnosed;
- how it affects manufacturing and service;
- what happens when it is missing, stale, invalid, incompatible, or from an older version.

Tie this to `LAW-001` - Every State Has One Owner. Do not turn the chapter into a storage-system design, configuration
database design, or feature-flag service chapter.

## 11. Variant Promises

Variants should be treated as promises.

A variant promise may include:

- supported hardware revision;
- supported region;
- supported customer package;
- supported radio, protocol, or module option;
- licensed capability;
- service-tool behavior;
- manufacturing flow;
- diagnostics meaning;
- update and recovery compatibility;
- supported default configuration;
- support horizon.

Tie this to `LAW-002` - Every API Is a Promise and `METRIC-003` - Discoverability. Avoid turning the chapter into a
SKU-management chapter or product-packaging playbook.

## 12. Product-Line Boundaries

Chapter 22 should teach that a product line needs explicit boundaries.

The future manuscript should ask:

- What is shared core?
- What is a variation point?
- Which combinations are supported?
- Which combinations are impossible?
- Which combinations are intentionally unsupported?
- Which parts are product-specific?
- Which parts are customer-specific?
- Which differences belong in hardware, firmware, configuration, manufacturing, service, or release?
- What needs review before becoming a new variation point?

Tie this to Change Radius, dependency decisions, and Architecture Review. Do not teach a full product-line engineering
methodology.

## 13. In-Scope and Out-of-Scope

### In Scope

Chapter 22 covers:

- configuration as owned state;
- supported variants as product promises;
- product-line boundaries and shared core;
- defaults, validation, migration, source of truth, and support meaning;
- supported, impossible, and intentionally unsupported combinations;
- customer-specific behavior, regional behavior, licensed capabilities, hardware options, and product packages;
- compile-time flags, build variants, runtime configuration, and field overrides as architectural surfaces when they
  affect promises;
- variant Change Radius across firmware, hardware, manufacturing, service, diagnostics, update, recovery, release,
  support, and tests;
- ADRs, RFCs, Decision Journal entries, Architecture Ledger rows, Architecture Review, Architecture Freeze, and
  Discoverability where proportionate;
- temporary flags, global configuration, hidden state, silent coupling, platform leakage, and accidental product-line
  behavior.

### Explicitly Out of Scope

Do not turn Chapter 22 into:

- Chapter 20's prototype-to-product transition repeated;
- Chapter 21's manufacturing and field reality chapter repeated;
- Chapter 23's observability in embedded systems chapter;
- Chapter 24's release discipline and upgrade-path chapter;
- Chapter 25's reference project walkthrough;
- a generic product-management chapter;
- a feature-flag operations handbook;
- a SKU spreadsheet tutorial;
- a configuration-database design;
- a build-system guide;
- a release-train process;
- a full product-line engineering methodology;
- a test-matrix tutorial;
- a new PEAK concept proposal.

## 14. Recommended Embedded-Systems Story

### Working Title

The Variant That Was Just a Flag

### Starting System

An embedded product from the Chapter 20 and Chapter 21 sequence has moved from pilot to multiple customers or product
packages. The team has a working product, manufacturing and field contracts, and a pressure to reuse the architecture
for a third package.

### Trigger

The first two variants ship after the team adds configuration quickly:

- hardware revision flag;
- region behavior flag;
- licensed feature flag;
- customer-specific protocol timeout;
- manufacturing-mode flag;
- service-tool hidden option;
- debug flag left in production;
- build define for a cheaper module;
- field override stored in a configuration file;
- recovery behavior depending on variant.

The third customer or second hardware option arrives, and the team asks, "Can we add one more flag?"

### Symptoms

- Nobody knows which combinations are supported.
- One flag changes API behavior.
- Manufacturing tests the wrong combination.
- The service tool reads a value differently than firmware.
- The update package assumes default configuration.
- Support cannot reproduce a field issue because variant state is invisible.
- A customer exception becomes a permanent product promise.
- Adding one variant changes behavior for another.
- Tests cover examples rather than the supported product line.

### Principal Engineer Intervention

The Principal Engineer restates:

> Can we add one more flag?

as:

> Is this a supported variant, a configuration value, an implementation detail, or an unsupported combination?

The intervention should list existing variation points, separate configuration from supported variants, name owners,
define supported and unsupported combinations, make default and migration behavior explicit, identify shared core versus
variation points, map Change Radius, record consequential choices, decide what must be reviewed or frozen before
release, remove or expire temporary flags, and preserve product-line simplicity.

## 15. Expected Discussion Arc

1. Chapter 21 made manufacturing and field assumptions explicit; Chapter 22 asks how product differences remain explicit
   as the product line grows.
2. Configuration is state and must have ownership, validation, defaults, migration, source of truth, and support meaning.
3. A variant is not a label; it is a promise about behavior, compatibility, manufacturing, service, release, and support.
4. Product lines need shared core, bounded variation points, and explicit supported or unsupported combinations.
5. Good variation is intentional and discoverable; bad variation is accidental, global, hidden, or copied without a
   decision.
6. Flags, defines, build variants, and field overrides are acceptable only when their promises and owners are named.
7. Simplicity and unused-flexibility judgment keep the product line small enough to understand.
8. Evidence determines which variants are supported and which remain imagined, temporary, or unsupported.
9. ADRs, RFCs, Decision Journal entries, Architecture Ledger rows, review, and freeze keep product-line promises
   discoverable.
10. The chapter names consequences for diagnostics, release, update, and recovery without teaching Chapters 23 or 24.

These are intellectual progression points, not mandatory manuscript headings.

## 16. Boundaries With Part IV Chapters

Chapter 22 owns configuration, variants, and product lines as architecture pressure.

- Chapter 20 owns the prototype-to-product transition and prototype-to-product gap.
- Chapter 21 owns manufacturing and field reality.
- Chapter 23 owns observability in embedded systems.
- Chapter 24 owns release discipline and upgrade paths.
- Chapter 25 owns the reference project walkthrough.

Chapter 22 may mention diagnostics, release packaging, update compatibility, recovery, and support only as consequences
of configuration and variant promises. It must not provide detailed observability infrastructure, release governance,
upgrade-system design, or reference-project implementation.

## 17. Boundaries With Earlier Parts

Use earlier chapters as constraints without repeating them:

- Chapter 7 - configuration is state and needs an owner.
- Chapter 8 - variants and service-tool behavior create promises.
- Chapter 9 - hardware modules, protocols, tools, libraries, and build paths are dependency decisions.
- Chapter 10 - timing, migration windows, and lifecycle timing may constrain configuration, but Chapter 22 does not
  reteach time as a dependency.
- Chapter 11 - unused flexibility makes product lines harder.
- Chapter 12 - simplicity is a product-line asset.
- Chapter 13 - prototype, manufacturing, field, and customer evidence should constrain supported variants.
- Chapters 14 and 15 - boundaries and Change Radius define variation impact.
- Chapter 17 - ADRs, RFCs, Decision Journal entries, and Architecture Ledger rows record supported variation.
- Chapter 18 - variation points may need Architecture Review before hardening.
- Chapter 19 - selected variant promises may need Architecture Freeze before release or manufacturing.
- Chapters 20 and 21 - product and field realities create variant pressure.

Chapter 22 applies those ideas to product-line variation. It should not repeat Part II or Part III.

## 18. Applicability

Chapter 22 is most useful when:

- one embedded product is becoming several product packages;
- customer, region, hardware, protocol, radio, module, or licensing differences are accumulating;
- configuration values are copied between products without ownership;
- build flags or compile-time defines alter product promises;
- a manufacturing or service path cannot tell which variant it is handling;
- support cannot reproduce a field problem because variant state is invisible;
- tests cover examples but not the supported product line;
- a temporary customer exception is becoming permanent;
- a new variation point would affect firmware, hardware, manufacturing, service, release, support, or update behavior.

Not every difference requires heavy process. A local implementation detail with low Change Radius may need code review
or a Decision Journal entry rather than an ADR. The chapter should teach classification and judgment, not a universal
gate.

## 19. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- configuration is always bad;
- compile-time flags are always bad;
- feature flags are always bad;
- product lines require a formal product-line engineering framework;
- every variant needs separate firmware;
- every configuration value needs an ADR;
- every customer difference should be supported;
- every product difference should be configurable;
- a spreadsheet is always wrong;
- a test matrix proves architecture is sound;
- release discipline or observability must be solved in Chapter 22.

Some differences are implementation details. Some differences are unsupported. Some differences should become separate
products. Some temporary exceptions may ship with an owner, expiration, and review trigger. The architectural question is
whether the difference creates a product promise or changes the product line's supported surface.

## 20. Violation Patterns

The future draft should make these violations visible:

- a flag without an owner changes product behavior;
- a compile-time define changes API meaning;
- a SKU spreadsheet is the only source of truth for behavior;
- manufacturing writes values that service cannot read;
- service tooling interprets variant state differently than firmware;
- an update package assumes the wrong default;
- support cannot reproduce a field issue because variant state is hidden;
- a temporary customer exception becomes permanent product-line behavior;
- hardware differences hide behind the same software promise;
- configuration bypasses state ownership;
- every possible combination becomes accidentally supported;
- tests cover examples rather than supported combinations;
- platform details leak into product variation logic.

Do not create a new smell or anti-pattern ID.

## 21. Engineering Principle Target

Target principle for the future draft:

> Treat configuration as owned state and variants as product promises. Keep the product line small enough to understand,
> explicit enough to test, and discoverable enough to support.

The principle should imply these questions:

1. Is this difference configuration, a variant, an implementation detail, or unsupported?
2. Who owns this value or variation point?
3. Who may change it?
4. What is the default?
5. How is it validated?
6. How does it migrate?
7. Which combinations are supported?
8. Which combinations are intentionally unsupported?
9. Which promise does this variant make to customers, manufacturing, service, release, or support?
10. What is the Change Radius of adding this variant?
11. What must be recorded, reviewed, tested, or frozen?

The final manuscript may shorten this list for reader rhythm.

## 22. Architecture Exercise Target

### Working Title

`Classify One Product Difference`

Ask the reader to choose one product difference and document:

- difference;
- whether it is configuration, variant, implementation detail, temporary exception, or unsupported combination;
- owner;
- who may change it;
- default;
- validation rule;
- migration rule;
- storage or source of truth;
- affected state, API, dependency, test, manufacturing, service, release, and support surfaces;
- supported combinations;
- unsupported combinations;
- evidence available;
- decision record needed;
- review or freeze trigger;
- expiration or removal trigger if temporary.

The exercise must end with:

1. one classification;
2. one owner;
3. one supported or unsupported boundary;
4. one validation or decision action.

Do not create a new canonical artifact.

## 23. Chapter-Local ADR Brief

### Working Title

`Define Supported Variant Boundaries Before Adding the Third Product Package`

### Context

- The first product package shipped with small configuration differences.
- The second package added hardware and service-tool differences.
- A third package request would turn temporary flags into product-line promises.
- Support, manufacturing, and release cannot see or validate every combination.

### Decision

- Separate configuration values from supported variants.
- Define shared core and variation points.
- Name owners for configuration and variant promises.
- Define supported and unsupported combinations.
- Require validation and discoverability for supported combinations.
- Remove or expire temporary flags.
- Record consequential variation decisions in ADRs, Decision Journal entries, or Architecture Ledger rows.
- Require review before adding a new variation point with large Change Radius.
- Defer observability and release-discipline details to Chapters 23 and 24.

### Alternatives Considered

- Add another flag.
- Create separate firmware for each customer.
- Make everything configurable.
- Freeze the current variant model immediately.
- Support every combination discovered in the field.
- Postpone variant modeling until after the next customer ships.

### Consequences

Benefits include simpler product-line reasoning, clearer ownership, smaller accidental test space, better supportability,
reduced silent coupling, and more explicit product-line promises.

Costs include slower feature addition for unsupported combinations, more explicit decision work before adding a new
package, and possible constraints on future customer-specific behavior.

The ADR must make a real story-local architecture decision. It must not reduce to "create a variant matrix."

## 24. PEAK Concept Map

### Concepts Inspected

- `FAILURE-003` - The Successful Prototype.
- `FAILURE-005` - The Release We Should Have Delayed.
- `ANTIPATTERN-002` - HAL Everywhere.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-006` - Temporary Solution.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-006` - Architecture Ledger.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.

### Selected Concepts

- `LAW-001` - Every State Has One Owner: material because configuration values, defaults, migration state, licensed
  capabilities, field overrides, and variant selection need owners.
- `LAW-002` - Every API Is a Promise: material because supported variants, service-tool behavior, update compatibility,
  diagnostics meanings, and customer packages create promises.
- `LAW-004` - Simplicity Is a Feature: material because a product line must remain small enough to understand, test, and
  support.
- `LAW-005` - Evidence Before Confidence: material because supported variants should be constrained by prototype,
  manufacturing, field, support, and customer evidence rather than imagined future combinations.
- `LAW-006` - Unused Flexibility Is Waste: material because unneeded variation points, generic flag systems, and
  speculative combinations expand test and review cost.
- `LAW-007` - Every Dependency Is a Decision: material because hardware modules, protocols, libraries, tools, build
  flags, configuration sources, and service tooling import product-line constraints.
- `VOCAB-001` - Change Radius: material because adding a variant can affect firmware, hardware, manufacturing, service,
  release, support, tests, and documentation.
- `METRIC-001` - Change Radius: material because the chapter estimates the surface affected by each product difference
  or variation point.
- `METRIC-003` - Discoverability: material because supported combinations, owners, defaults, validation rules, and
  promises must be findable.
- `ARTIFACT-001` - ADR: material because product-line boundaries and supported variant promises may require durable
  architecture decisions.
- `ARTIFACT-002` - RFC: material because new variation points with broad ownership impact may need proposal review
  before implementation hardens.
- `ARTIFACT-003` - Decision Journal: material because smaller configuration choices, temporary exceptions, and evidence
  gaps may need lightweight closure.
- `ARTIFACT-006` - Architecture Ledger: material because active product-line decisions, variant promises, and review
  dates may need a compact inventory.
- `RITUAL-001` - Architecture Review: material because adding a variation point with broad Change Radius should be
  challenged before it hardens.
- `RITUAL-002` - Architecture Freeze: material because selected variant promises may need temporary stabilization before
  manufacturing, field trial, release validation, or customer shipment.
- `SMELL-004` - Hidden State: material because invisible flags, defaults, field overrides, and variant selection affect
  behavior without a clear model.
- `SMELL-001` - Silent Coupling: material because firmware, manufacturing, service tools, update packages, tests, and
  support records can depend on the same variation without a shared contract.
- `SMELL-005` - Platform Leakage: material because hardware module or driver details can leak into product-line behavior
  and service meaning.
- `ANTIPATTERN-003` - Global Configuration: material because broad flags without owner, scope, validation, or lifecycle
  turn product variation into hidden coupling.
- `ANTIPATTERN-006` - Temporary Solution: material because customer exceptions and short-term flags need owner,
  expiration, removal, or explicit risk decisions.
- `ANTIPATTERN-002` - HAL Everywhere: material because hardware variants should expose product-level capabilities rather
  than spreading low-level hardware abstraction through product behavior.

### Rejected Concepts

- `FAILURE-003` - The Successful Prototype: predecessor context from Chapter 20, but Chapter 22 should not make
  prototype success the chapter anchor.
- `FAILURE-005` - The Release We Should Have Delayed: relevant to late variant risk, but Chapter 24 owns release
  discipline and upgrade paths.
- `LAW-003` - Time Is a Dependency: relevant to migration windows and lifecycle timing, but not selected because time is
  a supporting constraint rather than a material chapter edge.
- `ARTIFACT-004` - Mistake Ledger: useful after variant or configuration failure, but Chapter 22 acts before retrospective
  learning becomes the main subject.
- `VOCAB-006` - Architecture Freeze: related through `RITUAL-002`, but the vocabulary concept itself is not needed as an
  outgoing Chapter 22 relationship.
- `METRIC-004` - API Stability: relevant to variant promises, but `LAW-002`, Change Radius, and Discoverability are
  sufficient for this chapter's scope.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as configuration, variant, product line, variant matrix, product package, SKU, feature flag, configuration
owner, variant contract, compatibility matrix, supported combination, unsupported combination, and configuration debt
remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-022` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-022
  type: references
  to: LAW-001

- from: CHAPTER-022
  type: references
  to: LAW-002

- from: CHAPTER-022
  type: references
  to: LAW-004

- from: CHAPTER-022
  type: references
  to: LAW-005

- from: CHAPTER-022
  type: references
  to: LAW-006

- from: CHAPTER-022
  type: references
  to: LAW-007

- from: CHAPTER-022
  type: references
  to: VOCAB-001

- from: CHAPTER-022
  type: references
  to: METRIC-001

- from: CHAPTER-022
  type: references
  to: METRIC-003

- from: CHAPTER-022
  type: references
  to: ARTIFACT-001

- from: CHAPTER-022
  type: references
  to: ARTIFACT-002

- from: CHAPTER-022
  type: references
  to: ARTIFACT-003

- from: CHAPTER-022
  type: references
  to: ARTIFACT-006

- from: CHAPTER-022
  type: references
  to: RITUAL-001

- from: CHAPTER-022
  type: references
  to: RITUAL-002

- from: CHAPTER-022
  type: references
  to: SMELL-004

- from: CHAPTER-022
  type: references
  to: SMELL-001

- from: CHAPTER-022
  type: references
  to: SMELL-005

- from: CHAPTER-022
  type: references
  to: ANTIPATTERN-003

- from: CHAPTER-022
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-022
  type: references
  to: ANTIPATTERN-002
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 25. Required Reader-Facing Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 22 role:

- Opening Quote: establish that product differences become promises.
- Story: show a product line becoming unsafe because every difference was treated as one more flag.
- Discussion: teach configuration as state, variants as promises, product-line boundaries, owners, defaults,
  validation, migration, supported combinations, and unsupported combinations.
- Engineering Principle: anchor the move from flags and labels to owned product-line architecture.
- Architecture Exercise: classify one product difference.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local decision to define supported variant boundaries before adding the third package.
- Editor's Commentary: explain how Chapter 22 follows Chapter 21 without teaching Chapters 23 or 24 early.

## 26. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A flag without an owner is hidden state.
- Every supported variant is a promise.
- The cheapest product line is the one you can still understand.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 27. Technical Credibility Requirements

The future draft must treat the following accurately:

- runtime configuration;
- compile-time flags;
- build variants;
- hardware revisions;
- product packages;
- customer-specific behavior;
- regional behavior;
- licensed capabilities;
- manufacturing configuration;
- service-tool behavior;
- update and recovery compatibility;
- default values;
- validation and migration;
- source of truth;
- supported and unsupported combinations;
- variant test coverage;
- release packaging interaction;
- field diagnosis and supportability;
- dependency impact of hardware modules, protocols, tools, and libraries.

Do not require a specific MCU, RTOS, configuration store, feature-flag service, cloud platform, build system, SKU
system, license system, issue tracker, test framework, release process, or organization structure.

## 28. Terminology and Precision Guardrails

Use terms precisely:

- Configuration: runtime or deployment-time values that select behavior inside an existing product contract.
- Variant: a supported product difference with an explicit promise.
- Product line: a family of related products that share architecture but differ intentionally.
- Variation point: the boundary where supported differences are allowed to change behavior.
- Shared core: behavior, contracts, or implementation shared across supported variants.
- Supported combination: a combination the product line promises to build, test, release, diagnose, and support.
- Unsupported combination: a combination the product line explicitly does not promise.
- Temporary exception: a bounded difference with owner, expiration, and review trigger.

Avoid misleading statements:

- Configuration is always bad.
- Compile-time flags are always bad.
- Every variation point should be generic.
- Every customer difference should be supported.
- Every product difference should be configurable.
- A spreadsheet is always wrong.
- A test matrix proves architecture is sound.
- Release discipline or observability must be solved in this chapter.
- The chapter should register Configuration, Variant, Product Line, SKU, or Feature Flag as PEAK concepts.

## 29. Failure Modes to Avoid

The later draft must not become:

- a generic checklist;
- a product-management packaging chapter;
- a feature-flag operations handbook;
- a SKU spreadsheet tutorial;
- a configuration-database design;
- a build-system guide;
- a release-train process;
- a product-line engineering methodology chapter;
- a test-matrix tutorial;
- Chapter 20 or Chapter 21 repeated;
- Chapter 23 observability written early;
- Chapter 24 release discipline written early;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 30. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story contains a concrete embedded product moving from pilot to multiple product packages or customers;
- the story includes hardware revision flags, regional behavior, licensed capabilities, customer-specific behavior,
  manufacturing mode, service-tool hidden options, debug flags, build defines, field overrides, and variant-dependent
  recovery behavior where useful;
- the Principal Engineer move changes the question from adding another flag to classifying the product difference;
- configuration is treated as owned state;
- supported variants are treated as promises;
- product-line boundaries define shared core, variation points, supported combinations, and unsupported combinations;
- defaults, validation, migration, source of truth, and support meaning are materially present;
- no primary PEAK concept is assigned unless a later editor decision changes repository convention;
- no new PEAK concept, ID, relationship verb, artifact, metric, ritual, vocabulary term, smell, anti-pattern, or failure
  story is introduced;
- selected PEAK concepts are materially present if the registered relationship set is kept;
- later Part IV chapters remain out of scope;
- earlier chapters are used as constraints without being retaught;
- the exercise ends with one classification, one owner, one supported or unsupported boundary, and one validation or
  decision action;
- the ADR makes a genuine story-local decision about supported variant boundaries before adding a third product package;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist.

## 31. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into product-management packaging, feature-flag operations, build-system design, test-matrix
management, observability implementation, release discipline, or generic checklist advice.

Canon Review should verify that Chapter 22 remains no-primary, preserves the registered relationship set, does not
invent Configuration, Variant, Product Line, SKU, Feature Flag, Variant Matrix, Supported Combination, or Configuration
Debt as PEAK concepts, and keeps strict boundaries with Chapters 20, 21, 23, 24, and 25.

Technical Review should focus on realistic embedded product-line concerns: runtime configuration, compile-time flags,
build variants, hardware revisions, regional behavior, customer packages, licensed capabilities, manufacturing
configuration, service-tool behavior, update and recovery compatibility, defaults, validation, migration, supported
combinations, unsupported combinations, release packaging interaction, supportability, and dependency impact.

Freeze Review should confirm that Chapter 22 remains the third Part IV chapter, keeps the manuscript architecture
intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the
reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
product, customers, flags, hardware options, package names, support symptoms, product-line boundaries, and final notebook
wording while preserving the configuration-and-variant thesis, PEAK map, and chapter boundaries.
