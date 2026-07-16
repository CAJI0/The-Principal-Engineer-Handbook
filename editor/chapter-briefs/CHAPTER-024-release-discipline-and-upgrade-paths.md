# CHAPTER-024 Canonical Brief: Release Discipline and Upgrade Paths

## 1. Metadata

- Stable ID: `CHAPTER-024`.
- Title: `Release Discipline and Upgrade Paths`.
- Part: Part IV - Building a Product.
- Chapter number: 24.
- Expected manuscript path:
  `book/04-building-a-product/24-release-discipline-and-upgrade-paths.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-024-release-discipline-and-upgrade-paths.md`.
- Branch: `chapter24`.
- Verified baseline `origin/main`: `f2550e7a243d794960a2ef48fc6e40ed24269c05`.
- Baseline evidence: PR #25 squash commit, `Chapter 23: Observability in Embedded Systems (#25)`.
- Chapter 23 feature Freeze commit checked for tree equivalence:
  `bab1617e1348d6c90e59257932666969d3ee2ca5`.
- Canonical predecessor: `CHAPTER-023` - Observability in Embedded Systems.
- Part position: fifth chapter of Part IV - Building a Product.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 24 follows the current no-primary Part IV practice and is carried by a material
  relationship set rather than by a new registry attribute.
- Central anchor or practice: release discipline and upgrade path remain chapter-local working terms. The central
  registered story is `FAILURE-005` - The Release We Should Have Delayed.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `f2550e7a243d794960a2ef48fc6e40ed24269c05`.
- That baseline is the PR #25 squash commit, `Chapter 23: Observability in Embedded Systems (#25)`.
- The squash commit is an ancestor of current `origin/main` and has parent
  `e393001c8aa4d20668233766378695e537df13cb`.
- The Chapter 23 feature-branch Freeze commit `bab1617e1348d6c90e59257932666969d3ee2ca5` remains tree-equivalent for
  the checked Chapter 23 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-023` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-023` is the fourth Part IV chapter and is canonical.
- The table of contents places `Release Discipline and Upgrade Paths` fifth in Part IV - Building a Product.
- `book/04-building-a-product/README.md` exists and remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `FAILURE-005` - The Release We Should Have Delayed exists and is available as the central failure story for release
  risk, unresolved architecture uncertainty, and delayed evidence.
- `RITUAL-002` - Architecture Freeze and `VOCAB-006` - Architecture Freeze exist and are available to frame narrow
  stabilization of release-critical decisions.
- `METRIC-004` - API Stability exists and is available for compatibility promises.
- `CHAPTER-024` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 24 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter24` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part IV Role

Chapter 24 follows Chapter 23 by showing that an observable product still needs disciplined release and upgrade
commitments. Chapter 23 asked what evidence the product preserves so people can decide what happened. Chapter 24 asks
which release and upgrade promises the product can support after it leaves engineering control.

Chapter 20 moved the reader from prototype success to product obligations. Chapter 21 made manufacturing and field
reality architectural inputs. Chapter 22 made configuration, variants, and product-line differences explicit. Chapter
23 made field evidence and diagnostic meaning visible. Chapter 24 should now teach that release is where those promises
become obligations across versions, variants, configurations, manufacturing paths, service tools, support horizons,
recovery paths, and future change.

The chapter must not become a CI/CD cookbook, OTA implementation guide, deployment-tool tutorial, rollback algorithm,
release-manager checklist, release-note template, product-management launch plan, or DevOps process chapter. It is an
architecture chapter about making embedded products releasable, upgradeable, diagnosable, recoverable, compatible, and
supportable.

## 4. Canonical Purpose

Prepare Chapter 24 to teach that releasing an embedded product is not the moment engineering responsibility ends. It is
the moment architecture promises become field obligations.

Candidate thesis for the future manuscript:

> A release is an architectural commitment. An upgrade path is the proof that the commitment can change safely.

The chapter should move the reader away from treating release and upgrade as packaging work, CI/CD configuration,
boot loader work only, a release-manager checklist, support's problem, a one-time shipment event, a version number, a
customer notification, a QA sign-off, a rollback script, a deployment-tool choice, or something separate from
architecture.

The core question should become:

> What must remain true before, during, and after an upgrade so the product can change without losing compatibility,
> identity, data, recovery capability, diagnosis, or trust?

## 5. Primary-Concept Resolution

Chapter 24 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a dedicated primary concept attribute to chapter records. Chapter 24 follows
that convention and should be carried by its exact relationship set.

Release discipline, upgrade path, rollback, retry, forward-fix, release candidate, firmware image, version matrix,
migration contract, upgrade compatibility, support horizon, release gate, and release notes are chapter-local prose
terms only. They are not registered as PEAK vocabulary, laws, artifacts, rituals, metrics, smells, anti-patterns,
failure stories, or primary concepts.

No new PEAK concept is required for this brief.

## 6. Central Thesis

Release discipline is the architecture-aware practice of deciding what can ship, what must be held, what evidence is
required, what promises are being made, and how the product can be supported after release.

An upgrade path is a supported transition from one product state to another. It includes the source version, target
version, preserved state, compatibility promises, migration behavior, recovery behavior, diagnostic evidence, service
tool compatibility, and support horizon.

Approved supporting formulation for the future draft:

> Release only the promises you can support, and upgrade only along paths you can explain, recover, and validate.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. a release is mostly a versioned image or package;
2. a successful lab update proves field upgrade readiness;
3. rollback is enough to make upgrades safe;
4. compatibility is communicated by version numbers;
5. release notes are a customer-facing communication task only;
6. service-tool compatibility can be handled after release;
7. older field versions can be treated as rare exceptions;
8. upgrade failures are implementation bugs rather than architecture promises.

By the end of the chapter, the reader should be able to:

1. distinguish image correctness from release readiness;
2. define supported source-to-target upgrade paths;
3. name unsupported or deferred paths honestly;
4. identify release-critical state and its owner;
5. preserve identity, calibration, configuration, variant meaning, data, and recovery state through supported paths;
6. reason about backward, forward, service-tool, manufacturing, field-data, configuration, variant, diagnostic, and
   update-package compatibility;
7. use Architecture Freeze proportionately for release-critical surfaces;
8. require evidence for supported upgrade paths before broad release exposure;
9. record release risks, known limits, and support notes where future engineers can find them.

## 8. Release Discipline

For this chapter, release discipline means architecture-aware release judgment.

It includes:

- release criteria;
- compatibility promises;
- supported variants and configurations;
- version identity;
- artifact integrity;
- migration and rollback strategy;
- field diagnostics readiness;
- support readiness;
- manufacturing and service coordination;
- known risk decisions;
- review and freeze triggers;
- release notes as discoverable support evidence;
- ownership of release-critical state;
- evidence before confidence.

The future manuscript should show that release discipline is not a generic checklist. It is the act of making product
commitments explicit before customers, manufacturing, support, service tools, installers, diagnostics, and future
engineers depend on them.

## 9. Upgrade Paths

For this chapter, an upgrade path is a supported transition from one product state to another, not merely a firmware
image.

An upgrade path may include:

- source version;
- target version;
- boot loader or installer behavior at a conceptual level;
- configuration migration;
- data migration;
- calibration preservation;
- identity preservation;
- hardware revision and product variant compatibility;
- feature flag or license migration;
- recovery state;
- rollback, retry, or forward-fix behavior;
- power-loss handling;
- network-interruption handling;
- partial upgrade detection;
- progress and failure observability;
- service-tool compatibility;
- support horizon and deprecation.

Architecture is involved when the upgrade touches state ownership, API promises, dependencies, time windows, recovery,
observability, field support, product trust, or release evidence.

The future manuscript must not become an OTA implementation guide.

## 10. Compatibility and Support Horizon

The future draft should distinguish:

- backward compatibility;
- forward compatibility;
- service-tool compatibility;
- manufacturing compatibility;
- field-data compatibility;
- configuration compatibility;
- variant compatibility;
- diagnostic compatibility;
- update-package compatibility;
- support horizon.

A release changes what customers, manufacturing, support, service tools, installers, diagnostics, and future engineers
can rely on. `LAW-002` - Every API Is a Promise, `METRIC-004` - API Stability, and `METRIC-003` - Discoverability are
material because compatibility is not communicated by a version number alone.

The chapter should avoid semantic-versioning doctrine. Version numbers may help, but the architectural work is naming
which promises remain valid, where they are recorded, which versions are supported, and what happens when a path is not
supported.

## 11. Release Decisions and Freeze

Chapter 24 should use Architecture Freeze proportionately.

A release may need a temporary freeze around:

- upgrade path;
- supported variant set;
- configuration schema;
- diagnostics and event meanings;
- release-critical APIs;
- boot and recovery behavior;
- service-tool protocol;
- manufacturing programming path;
- migration logic;
- support notes;
- known risk decisions.

The point is not bureaucracy. The point is to stop uncontrolled architectural change while evidence, compatibility, and
recovery are being validated.

Tie to Chapter 19 without repeating it. The future draft should show a narrow freeze over release-critical surfaces,
with allowed movement, exception path, evidence threshold, record updates, and exit criteria.

## 12. In-Scope and Out-of-Scope

### In Scope

Chapter 24 covers:

- release discipline as architecture-aware product commitment;
- supported and unsupported upgrade paths;
- compatibility promises across versions, tools, variants, configurations, diagnostics, and manufacturing paths;
- release-critical state ownership;
- identity, calibration, configuration, data, variant, and recovery preservation;
- rollback, retry, recovery, and forward-fix trade-offs;
- service-tool and diagnostic compatibility;
- release evidence and validation for supported paths;
- support horizon, deprecation, and known limits;
- Architecture Review, Architecture Freeze, ADRs, RFCs, Decision Journal entries, Architecture Ledger entries, Event
  Catalog entries, release notes, and Mistake Ledger entries where proportionate.

### Explicitly Out of Scope

Do not turn Chapter 24 into:

- Chapter 20's prototype-to-product transition repeated;
- Chapter 21's manufacturing and field reality chapter repeated;
- Chapter 22's configuration, variants, and product lines chapter repeated;
- Chapter 23's observability chapter repeated;
- Chapter 25's reference project walkthrough;
- a CI/CD cookbook;
- a boot loader implementation guide;
- an OTA vendor comparison;
- a deployment-tool tutorial;
- a rollback algorithm chapter;
- a release-manager checklist;
- a product-management launch plan;
- a semantic-versioning doctrine chapter;
- a new PEAK concept proposal.

## 13. Recommended Embedded-Systems Story

### Working Title

The Upgrade That Worked Only Once

### Starting System

An embedded product from Chapters 20 through 23 has product-ready architecture, manufacturing and field contracts,
supported variants and configuration, field observability, a service tool, and an update and recovery path.

The team prepares a release that changes firmware behavior and the configuration schema. A lab upgrade from the latest
engineering build works. The team plans to ship.

### Symptoms

- field units are on multiple older versions;
- one hardware revision needs a different migration path;
- a customer variant uses a deprecated option;
- service tool version compatibility is unclear;
- rollback would preserve firmware but not migrated configuration;
- calibration data ownership is ambiguous during upgrade;
- device identity survives in the lab but not in one recovery path;
- update progress is observable, but failure reason is not support-safe;
- release notes list features but not compatibility or support assumptions;
- QA tested examples, not supported upgrade paths;
- a late change lands after the team thought the release was stable.

### Principal Engineer Intervention

The team asks:

> Did the new image pass?

The Principal Engineer restates:

> Which upgrade paths are we promising, and what must remain true before, during, and after the upgrade?

The intervention should enumerate supported source-to-target upgrade paths, identify unsupported or deferred paths,
name release-critical state owners, preserve identity, calibration, configuration, and variant meaning, define rollback,
retry, forward-fix, or recovery behavior, ensure service-tool and diagnostic compatibility, require evidence for each
supported path, use Architecture Freeze to stabilize release-critical decisions, record risk decisions and known limits,
and feed escaped release assumptions into the Mistake Ledger where appropriate.

Do not implement boot loader logic, OTA protocol, release automation, or CI/CD workflow.

## 14. Expected Discussion Arc

1. Chapter 23 made field evidence visible; Chapter 24 asks which release and upgrade commitments that evidence must
   support.
2. A release is an architectural commitment, not only a file, package, or tag.
3. An upgrade path is a supported state transition, not only a firmware image.
4. The lab's latest-build upgrade is evidence for one path, not for every field path.
5. Compatibility includes versions, variants, configurations, service tools, manufacturing paths, diagnostics, and
   support horizon.
6. Release-critical state needs owners before the upgrade can preserve it.
7. Rollback, retry, recovery, and forward-fix are different promises and must be chosen deliberately.
8. Release notes, ADRs, RFCs, Decision Journal entries, Architecture Ledger entries, Event Catalog entries, and Mistake
   Ledger entries keep release assumptions discoverable.
9. Architecture Freeze can stabilize release-critical surfaces while evidence is gathered, without freezing all
   learning.
10. The chapter prepares the reference project walkthrough without writing it.

These are intellectual progression points, not mandatory manuscript headings.

## 15. Boundaries With Part IV Chapters

Chapter 24 owns release discipline and upgrade paths as architecture obligations.

- Chapter 20 owns the prototype-to-product transition and prototype assumptions.
- Chapter 21 owns manufacturing and field reality.
- Chapter 22 owns configuration, variants, and product lines.
- Chapter 23 owns observability in embedded systems.
- Chapter 25 owns the reference project walkthrough.

Chapter 24 may mention prototype-to-product work, manufacturing, variants, and observability only as release surfaces created by
earlier chapters. It must not re-teach those chapters.

Chapter 24 may prepare concepts Chapter 25 will use, but it must not walk through the reference project, invent project
components, or write implementation examples for the reference project.

## 16. Boundaries With Earlier Parts

Use earlier chapters as constraints without repeating them:

- Chapter 7 - release-critical state needs owners.
- Chapter 8 - released APIs, diagnostics, tools, protocols, and upgrade behavior become promises.
- Chapter 9 - update tooling, boot loaders, installers, signing systems, service tools, and distribution paths are
  dependency decisions.
- Chapter 10 - release windows, support horizons, migration timing, staged rollout assumptions, and retry windows depend
  on time.
- Chapter 13 - upgrade-path confidence requires evidence, not a successful lab update alone.
- Chapter 15 - release changes can have Change Radius across firmware, hardware, manufacturing, service, support,
  documentation, tests, and customers.
- Chapter 16 - release and upgrade paths must preserve recovery, not bypass failure design.
- Chapter 17 - ADR, RFC, Decision Journal, Architecture Ledger, Event Catalog, and Mistake Ledger preserve release
  decisions and assumptions.
- Chapter 18 - high-risk release changes may need Architecture Review before hardening.
- Chapter 19 - Architecture Freeze stabilizes release-critical decisions during validation.
- Chapters 20 through 23 - prototype-to-product work, manufacturing and field reality, variants, and observability create the
  release surface.

Chapter 24 applies those ideas to release and upgrade obligations. It should not repeat Part II laws or the Part III
playbook.

## 17. Applicability

Chapter 24 is most useful when:

- field units exist on multiple versions;
- an update changes configuration, data, identity, calibration, variant behavior, diagnostics, or recovery behavior;
- support or service tools must remain compatible across releases;
- rollback is possible for firmware but not for state;
- release pressure is turning known uncertainty into field risk;
- a late architecture change lands during release hardening;
- QA has tested examples rather than supported upgrade paths;
- release notes describe features but not compatibility, support assumptions, or known limits;
- manufacturing, support, service, firmware, and release owners each hold part of the release promise.

Not every device needs heavy release machinery. A small local fix with low Change Radius may need a clear record, a
targeted validation, and a bounded support note rather than a broad freeze. The chapter should scale discipline to
consequence.

## 18. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- every release needs a full architecture freeze;
- every old version must be supported forever;
- rollback is always safe;
- factory reset is acceptable recovery by default;
- version numbers automatically communicate compatibility;
- CI/CD passing proves upgrade safety;
- observability alone solves release risk;
- release notes replace architecture records;
- all customers can be forced to latest immediately;
- every release risk must block shipment;
- every upgrade path needs the same validation depth;
- OTA implementation details belong in this chapter.

Some paths may be explicitly unsupported. Some releases may be bounded pilots. Some recovery may be forward-fix rather
than rollback. Some old versions may require service intervention or deprecation. The architectural obligation is to
make the commitment, evidence, unsupported path, and support consequence explicit.

## 19. Violation Patterns

The future draft should make these violations visible:

- a release is treated as a successful build artifact;
- the latest lab upgrade is generalized to every field source version;
- rollback restores firmware but corrupts or invalidates configuration;
- calibration and identity ownership are ambiguous during upgrade;
- service tools and firmware disagree about supported versions;
- diagnostics change meaning without support or tool compatibility;
- release notes list features but hide compatibility assumptions;
- unsupported field versions are discovered by support after release;
- a late architectural change lands after validation begins;
- update package compatibility is assumed from version number shape;
- factory reset is used as the default escape hatch;
- known release risks lack owners, records, or review triggers.

Do not create a new smell or anti-pattern ID.

## 20. Engineering Principle Target

Target principle for the future draft:

> Release only the promises you can support, and upgrade only along paths you can explain, recover, and validate. A
> version is not a release unless its compatibility, state transitions, evidence, and support obligations are known.

The principle should imply these questions:

1. Which source versions can upgrade to this release?
2. Which variants and configurations are supported?
3. What state must survive the upgrade?
4. Who owns release-critical state?
5. What happens if power or network fails mid-upgrade?
6. What can be rolled back, retried, recovered, or forward-fixed?
7. Which service tool versions are compatible?
8. What evidence proves this path works?
9. What diagnostic evidence will support see if it fails?
10. What changed after freeze?
11. What risk is accepted, deferred, or unsupported?
12. What must release notes make discoverable?

The final manuscript may shorten this list for reader rhythm.

## 21. Architecture Exercise Target

### Working Title

`Trace One Upgrade Path`

Ask the reader to choose one product upgrade path and document:

- source version;
- target version;
- hardware revision;
- product variant;
- configuration schema;
- data or calibration that must survive;
- release-critical state owner;
- compatibility promises;
- migration step;
- rollback, retry, recovery, or forward-fix behavior;
- observability needed during and after upgrade;
- service-tool compatibility;
- evidence available;
- evidence missing;
- unsupported paths;
- decision record needed;
- freeze or review trigger.

The exercise must end with:

1. one supported upgrade path;
2. one unsupported or deferred path;
3. one release-critical state owner;
4. one validation or recovery action.

Do not create a new canonical artifact.

## 22. Chapter-Local ADR Brief

### Working Title

`Freeze Supported Upgrade Paths Before Field Release`

### Context

- The product has multiple field versions, hardware revisions, configurations, variants, and service-tool versions.
- A lab upgrade from the latest build works.
- Field release would expose unsupported source versions and uncertain migration paths.
- Rollback and recovery behavior are not equally safe for every path.

### Decision

- Enumerate supported source-to-target upgrade paths.
- Explicitly reject or defer unsupported paths.
- Freeze release-critical state transitions, configuration migration, diagnostic meanings, and service-tool
  compatibility before final validation.
- Preserve identity, calibration, configuration, and variant meaning across supported paths.
- Require evidence for each supported path.
- Record release risks, known limits, and support notes in appropriate artifacts.
- Defer reference-project integration walkthrough to Chapter 25.

### Alternatives Considered

- Ship the image because the latest lab upgrade worked.
- Support every field version.
- Require all customers to factory reset.
- Rely on rollback only.
- Patch unsupported paths in support scripts.
- Defer upgrade-path definition until after release.
- Freeze the whole architecture instead of release-critical surfaces.

### Consequences

Benefits include clearer support promises, fewer field surprises, stronger compatibility evidence, explicit
unsupported paths, better recovery decisions, and more durable product trust.

Costs include more validation work, slower late changes, visible unsupported paths, service-tool coordination,
compatibility records, and extra discipline around release-critical state.

The ADR must make a real story-local architecture decision. It must not reduce to "run release checklist" or "add
rollback."

## 23. PEAK Concept Map

### Concepts Inspected

- `FAILURE-005` - The Release We Should Have Delayed.
- `RITUAL-002` - Architecture Freeze.
- `VOCAB-006` - Architecture Freeze.
- `RITUAL-001` - Architecture Review.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-005` - Evidence Before Confidence.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-006` - Architecture Ledger.
- `FAILURE-002` - One Lost Packet.
- `FAILURE-003` - The Successful Prototype.
- `ANTIPATTERN-006` - Temporary Solution.
- `SMELL-004` - Hidden State.
- `SMELL-001` - Silent Coupling.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-002` - HAL Everywhere.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-005` - Callback Hell.

### Selected Concepts

- `FAILURE-005` - The Release We Should Have Delayed: material because the chapter's story is about release pressure
  turning unresolved upgrade uncertainty into field risk.
- `RITUAL-002` - Architecture Freeze: material because the chapter uses a narrow freeze to stabilize supported upgrade
  paths, compatibility promises, diagnostic meanings, and release-critical state before final validation.
- `VOCAB-006` - Architecture Freeze: material because the chapter must preserve the temporary, exit-criteria-bound
  meaning of freeze rather than using it as a broad ban on change.
- `RITUAL-001` - Architecture Review: material because high-risk release and upgrade changes may need review before
  hardening or freeze.
- `LAW-001` - Every State Has One Owner: material because release-critical state such as identity, calibration,
  configuration, variant, data, migration, and recovery state needs clear authority.
- `LAW-002` - Every API Is a Promise: material because released APIs, service tools, diagnostics, protocols, update
  behavior, and compatibility meanings become promises.
- `LAW-003` - Time Is a Dependency: material because release windows, support horizons, migration timing, retry windows,
  deprecation timing, and staged exposure depend on time assumptions.
- `LAW-005` - Evidence Before Confidence: material because upgrade-path confidence requires evidence for supported
  paths, not only a successful latest-build lab update.
- `LAW-007` - Every Dependency Is a Decision: material because boot loaders, installers, signing systems, service tools,
  distribution paths, gateways, and update tooling import lifecycle and failure obligations.
- `VOCAB-001` - Change Radius: material because a release or upgrade change can affect firmware, hardware,
  manufacturing, service, support, diagnostics, documentation, tests, and customers.
- `METRIC-001` - Change Radius: material because the chapter estimates affected surface when deciding release risk,
  validation depth, and exception handling.
- `METRIC-003` - Discoverability: material because supported paths, unsupported paths, compatibility assumptions,
  release notes, owners, and records must be findable.
- `METRIC-004` - API Stability: material because compatibility is about preserving behavior, errors, timing, and meaning
  across releases and service-tool versions.
- `ARTIFACT-001` - ADR: material because consequential release and upgrade decisions need durable records.
- `ARTIFACT-002` - RFC: material because broad upgrade-path, compatibility, or service-tool changes may need review
  before hardening.
- `ARTIFACT-003` - Decision Journal: material because smaller release risks, deferred paths, confidence judgments, and
  review triggers need lightweight records.
- `ARTIFACT-004` - Mistake Ledger: material because escaped release assumptions should preserve the failed assumption
  and detection gap.
- `ARTIFACT-005` - Event Catalog: material because diagnostic and event meanings that support upgrade progress and
  failure interpretation must remain compatible.
- `ARTIFACT-006` - Architecture Ledger: material because active release-critical decisions, freeze scope, upgrade-path
  status, and review dates should be discoverable.
- `ANTIPATTERN-006` - Temporary Solution: material because late release workarounds, support scripts, and temporary
  upgrade bypasses need owner, trigger, and removal or support decision.
- `SMELL-004` - Hidden State: material because hidden configuration, calibration, identity, migration, or recovery state
  can break an upgrade path.
- `SMELL-001` - Silent Coupling: material because firmware, service tools, manufacturing scripts, release packages,
  diagnostics, and support records can depend on the same release promise without an explicit contract.
- `SMELL-005` - Platform Leakage: material because low-level boot loader, driver, hardware, or vendor details can leak
  into product release and support promises without translation.
- `SMELL-006` - Event Explosion: material because upgrade diagnostics can become noisy or incompatible when event
  meanings are not owned and versioned.
- `ANTIPATTERN-002` - HAL Everywhere: material because hardware-revision and update behavior should not force product
  release logic to depend on scattered low-level vocabulary.
- `ANTIPATTERN-003` - Global Configuration: material because broad release or migration flags can change unrelated
  behavior across variants, diagnostics, recovery, and service tools.
- `ANTIPATTERN-005` - Callback Hell: material because asynchronous installer, service-tool, gateway, and recovery flows
  can hide ordering and failure behavior during upgrade.
- `FAILURE-002` - One Lost Packet: material because interrupted or reordered update communication can expose weak retry,
  recovery, and diagnostic contracts.

### Rejected Concepts

- `FAILURE-003` - The Successful Prototype: relevant as a background Part IV failure, but Chapter 20 already owns the
  prototype-to-product transition.
- `LAW-004` - Simplicity Is a Feature: useful as general judgment, but release and upgrade scope is more directly
  carried by state ownership, API promises, time, evidence, dependency decisions, Change Radius, and compatibility.
- `LAW-006` - Unused Flexibility Is Waste: relevant to over-supporting old versions or speculative compatibility, but
  not necessary for the Chapter 24 relationship set.
- `ARTIFACT-007` - Weak Signal Register and `VOCAB-002` - Weak Signal: useful for field learning, but release evidence,
  risks, and escaped assumptions are carried sufficiently by Decision Journal, Mistake Ledger, Event Catalog,
  Architecture Ledger, review, and freeze.
- `RITUAL-006` - RFC Friday and later operating rituals: related to organizational practice, but not material to this
  chapter's release and upgrade architecture.
- `METRIC-005` - Architecture Health and `VOCAB-007` - Architecture Health: useful for later operating models, but not
  needed as outgoing Chapter 24 relationships.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as release discipline, upgrade path, rollback, retry, forward-fix, firmware image, release candidate,
version matrix, migration contract, upgrade compatibility, support horizon, release gate, release notes, and release
evidence remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-024` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-024
  type: illustrates
  to: FAILURE-005

- from: CHAPTER-024
  type: illustrates
  to: RITUAL-002

- from: CHAPTER-024
  type: references
  to: VOCAB-006

- from: CHAPTER-024
  type: references
  to: RITUAL-001

- from: CHAPTER-024
  type: references
  to: LAW-001

- from: CHAPTER-024
  type: references
  to: LAW-002

- from: CHAPTER-024
  type: references
  to: LAW-003

- from: CHAPTER-024
  type: references
  to: LAW-005

- from: CHAPTER-024
  type: references
  to: LAW-007

- from: CHAPTER-024
  type: references
  to: VOCAB-001

- from: CHAPTER-024
  type: references
  to: METRIC-001

- from: CHAPTER-024
  type: references
  to: METRIC-003

- from: CHAPTER-024
  type: references
  to: METRIC-004

- from: CHAPTER-024
  type: references
  to: ARTIFACT-001

- from: CHAPTER-024
  type: references
  to: ARTIFACT-002

- from: CHAPTER-024
  type: references
  to: ARTIFACT-003

- from: CHAPTER-024
  type: references
  to: ARTIFACT-004

- from: CHAPTER-024
  type: references
  to: ARTIFACT-005

- from: CHAPTER-024
  type: references
  to: ARTIFACT-006

- from: CHAPTER-024
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-024
  type: references
  to: SMELL-004

- from: CHAPTER-024
  type: references
  to: SMELL-001

- from: CHAPTER-024
  type: references
  to: SMELL-005

- from: CHAPTER-024
  type: references
  to: SMELL-006

- from: CHAPTER-024
  type: references
  to: ANTIPATTERN-002

- from: CHAPTER-024
  type: references
  to: ANTIPATTERN-003

- from: CHAPTER-024
  type: references
  to: ANTIPATTERN-005

- from: CHAPTER-024
  type: references
  to: FAILURE-002
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 24. Required Reader-Facing Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 24 role:

- Opening Quote: establish that a release is a promise and an upgrade path is a state transition.
- Story: show a product whose latest-build lab upgrade worked while field upgrade paths remained unsupported.
- Discussion: teach release discipline, upgrade paths, compatibility, support horizon, state preservation, rollback,
  retry, forward-fix, recovery, service-tool compatibility, diagnostics, release evidence, and narrow freeze.
- Engineering Principle: anchor the move from passing image to supported release promise.
- Architecture Exercise: trace one upgrade path.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local decision to freeze supported upgrade paths before field release.
- Editor's Commentary: explain how Chapter 24 follows Chapter 23 without writing the Chapter 25 reference walkthrough.

## 25. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A release is a promise, not a file.
- An upgrade path includes the state it must preserve.
- A rollback that loses trust is not recovery.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 26. Technical Credibility Requirements

The future draft must treat the following accurately:

- firmware image identity;
- boot loader or installer behavior at a conceptual level;
- source and target version paths;
- configuration and data migration;
- calibration preservation;
- device identity preservation;
- variant and hardware revision compatibility;
- service-tool compatibility;
- diagnostic and event compatibility;
- release notes and support knowledge;
- signing and artifact integrity at a conceptual level where relevant;
- power-loss and network-interruption during upgrade;
- partial upgrade detection;
- rollback versus retry versus forward-fix;
- factory reset as last resort, not assumed recovery;
- field units on older versions;
- release validation evidence;
- support horizon and deprecation;
- field failure after release;
- upgrade observability and support-safe failure reporting.

Do not require a specific MCU, boot loader, OTA protocol, signing scheme, cloud service, CI/CD system, deployment
platform, package manager, test framework, release process, or organization structure.

## 27. Terminology and Precision Guardrails

Use terms precisely:

- Release discipline: architecture-aware judgment about what can ship, what must be held, what evidence is required,
  what promises are made, and how the product can be supported after release.
- Upgrade path: a supported transition from one product state to another.
- Release-critical state: state whose loss, ambiguity, or incompatible migration can break a supported release or
  upgrade promise.
- Compatibility: preserved behavior, meaning, data, diagnostics, tooling, or support promises across versions and
  contexts.
- Rollback: a return to an earlier executable or product state when the associated preserved state remains trustworthy.
- Retry: another attempt along the same path after a recoverable interruption.
- Forward-fix: a supported move to a corrected state when rollback would be unsafe or incomplete.
- Support horizon: the versions, variants, tools, and paths the product promises to support for a bounded period.

Avoid misleading statements:

- A successful lab upgrade proves field readiness.
- Rollback is always safe.
- Factory reset is acceptable recovery by default.
- Every release needs a full architecture freeze.
- Version numbers automatically communicate compatibility.
- Release notes replace architecture records.
- CI/CD passing proves upgrade safety.
- All customers can be forced to latest version.
- Every old version must be supported forever.
- OTA implementation details belong here.
- Observability alone solves release risk.

## 28. Failure Modes to Avoid

The later draft must not become:

- a CI/CD cookbook;
- a deployment-tool tutorial;
- a boot loader implementation guide;
- an OTA vendor comparison;
- a rollback algorithm;
- a release-manager checklist;
- a product-management launch plan;
- a semantic-versioning doctrine chapter;
- Chapter 20, 21, 22, or 23 repeated;
- Chapter 25's reference project walkthrough written early;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 29. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story contains a concrete embedded product whose latest-build lab upgrade works while field upgrade paths remain
  uncertain;
- the story includes multiple older versions, one hardware-revision-specific migration path, a deprecated customer
  option, unclear service-tool compatibility, unsafe rollback for migrated configuration, ambiguous calibration
  ownership, identity loss in one recovery path, support-unsafe failure evidence, feature-only release notes, example
  testing instead of path testing, and a late release-critical change;
- the Principal Engineer move changes the question from whether the image passed to which upgrade paths are promised;
- release discipline and upgrade path remain chapter-local frames and no primary PEAK concept is assigned unless a
  later editor decision changes repository convention;
- `FAILURE-005` and `RITUAL-002` are materially present if the registered relationship set is kept;
- release criteria, compatibility promises, supported variants and configurations, version identity, artifact
  integrity, migration, rollback, recovery, diagnostics, support readiness, known risk decisions, and release notes as
  discoverable evidence are materially present;
- supported and unsupported upgrade paths are explicit;
- rollback, retry, recovery, and forward-fix are distinguished;
- service-tool, diagnostic, manufacturing, configuration, variant, field-data, update-package, backward, and forward
  compatibility are treated accurately;
- selected PEAK concepts are materially present if the registered relationship set is kept;
- Chapter 25 remains out of scope;
- earlier chapters are used as constraints without being retaught;
- the exercise ends with one supported path, one unsupported or deferred path, one release-critical state owner, and one
  validation or recovery action;
- the ADR makes a genuine story-local decision about freezing supported upgrade paths before field release;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 30. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into CI/CD, release-management checklist, boot loader implementation, OTA vendor comparison,
semantic-versioning doctrine, support operations, or Chapter 25 walkthrough.

Canon Review should verify that Chapter 24 remains no-primary, preserves the registered relationship set, does not
invent Release Discipline or Upgrade Path as PEAK concepts, materially illustrates The Release We Should Have Delayed
and Architecture Freeze, and keeps strict boundaries with Chapters 20, 21, 22, 23, and 25.

Technical Review should focus on realistic embedded release and upgrade constraints: field units on older versions,
firmware image identity, migration, calibration and identity preservation, hardware revisions, variants, service-tool
compatibility, diagnostic compatibility, artifact integrity, power loss, network interruption, partial upgrade
detection, rollback limits, retry, recovery, forward-fix, support horizon, deprecation, release evidence, and
support-safe failure reporting.

Freeze Review should confirm that Chapter 24 remains the fifth Part IV chapter, keeps the manuscript architecture
intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the
reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
product, release, upgrade paths, state names, compatibility matrix, service-tool details, release-note details, freeze
scope, recovery choices, and final notebook wording while preserving the release/upgrade thesis, PEAK map, and chapter
boundaries.
