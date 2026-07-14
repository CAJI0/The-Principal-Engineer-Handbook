# CHAPTER-021 Canonical Brief: Designing for Manufacturing and Field Reality

## 1. Metadata

- Stable ID: `CHAPTER-021`.
- Title: `Designing for Manufacturing and Field Reality`.
- Part: Part IV - Building a Product.
- Chapter number: 21.
- Expected manuscript path:
  `book/04-building-a-product/21-designing-for-manufacturing-and-field-reality.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-021-designing-for-manufacturing-and-field-reality.md`.
- Branch: `chapter21`.
- Verified baseline `origin/main`: `c0c3bf50d869e3fcb58c7930ffd7da71c6589c2a`.
- Baseline evidence: PR #22 squash commit, `Chapter 20: From Prototype to Product (#22)`.
- Chapter 20 feature Freeze commit checked for tree equivalence:
  `525c15f42b6583533aab0eb9ebd8138d57053244`.
- Canonical predecessor: `CHAPTER-020` - From Prototype to Product.
- Part position: second chapter of Part IV - Building a Product.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 21 is carried by a material relationship set and chapter-local framing rather than by a
  new primary-concept field.
- Central anchor or practice: none registered. Manufacturing reality and field reality are chapter-local design-input
  frames, not new PEAK concepts.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `c0c3bf50d869e3fcb58c7930ffd7da71c6589c2a`.
- That baseline is the PR #22 squash commit, `Chapter 20: From Prototype to Product (#22)`.
- The squash commit is an ancestor of current `origin/main` and has parent
  `c06c0143bc86c446815900e94508230414b0ff24`.
- The Chapter 20 feature-branch Freeze commit `525c15f42b6583533aab0eb9ebd8138d57053244` remains tree-equivalent for
  the checked Chapter 20 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-020` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-020` is the first Part IV chapter and is canonical.
- The table of contents places `Designing for Manufacturing and Field Reality` second in Part IV - Building a Product.
- `book/04-building-a-product/README.md` exists and remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-021` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 21 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter21` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part IV Role

Chapter 21 deepens Chapter 20 by showing where product reality arrives first: the product must be built repeatedly and
understood after it leaves engineering control.

Chapter 20 taught that a successful prototype is evidence, not product architecture. Chapter 21 should show that
manufacturing and field conditions are not downstream chores. They are design inputs that reveal whether ownership,
interfaces, diagnostics, calibration, identity, recovery, traceability, and evidence are explicit enough for the product
to survive outside the lab.

The chapter should give the reader architectural judgment for manufacturing and field pressure without turning into a
manufacturing engineering handbook, QA handbook, support process, observability chapter, release playbook, compliance
chapter, or fixture-design guide.

## 4. Canonical Purpose

Prepare Chapter 21 to teach that manufacturing and field reality are architecture constraints, not late-stage
implementation details.

Candidate thesis for the future manuscript:

> A product architecture is not complete until it can be built repeatedly and understood after it leaves the lab.

The chapter should move the reader away from treating manufacturing and field concerns as another team's process
problem, a QA detail, fixture-only work, documentation cleanup, support improvisation, hardware-only concern, or testing
that can be added after architecture is done.

The core question should become:

> What must the architecture make repeatable, testable, diagnosable, able to be calibrated, recoverable, and supportable
> when the product is built many times and used away from the lab?

## 5. Primary-Concept Resolution

Chapter 21 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Chapter 21 follows that
convention and should be carried by its exact relationship set.

Manufacturing reality and field reality are necessary chapter-local frames, but neither becomes a PEAK vocabulary
concept, law, metric, artifact, ritual, smell, anti-pattern, failure story, or primary concept. The chapter may use the
phrases to teach architecture judgment without registering `Manufacturing Reality`, `Field Reality`, `Production
Readiness`, `Service Surface`, `Calibration Contract`, `Fixture Contract`, `Pilot Manufacturing`, or any similar new
concept.

## 6. Central Thesis

Manufacturing and field reality are not downstream validation details. They are architecture inputs. Before a product
depends on repeated builds and remote support, the architecture must make identity, calibration, configuration,
diagnostics, recovery, traceability, ownership, and evidence explicit enough for people outside engineering to use.

Approved supporting formulation for the future draft:

> Design the product for the places where engineers are absent.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. manufacturing is a process concern after architecture;
2. field failures are QA or support problems;
3. a fixture interface is not architecture;
4. calibration is just a value;
5. serial identity and traceability are administrative details;
6. diagnostics mean logs for developers;
7. update recovery can be solved by the release process later;
8. support training can compensate for unclear product states.

By the end of the chapter, the reader should be able to:

1. identify which manufacturing and field assumptions are architectural;
2. separate process details from product obligations;
3. assign ownership for calibration, configuration, identity, diagnostic, and service-visible state;
4. ask what a fixture, station, service tool, or support engineer can know without developer help;
5. map the Change Radius of a manufacturing or field assumption;
6. record consequential manufacturing and field contracts in ADRs or Decision Journal entries;
7. recognize when field learning belongs in a Mistake Ledger;
8. decide what must be reviewed or frozen before pilot manufacturing or field trial.

## 8. Manufacturing Reality

For this chapter, manufacturing reality means the repeatability, variation, traceability, calibration, programming,
test, fixture, and provisioning pressures that appear when a product must be built repeatedly.

Manufacturing reality includes:

- unit-to-unit variation;
- board revisions;
- component tolerance and substitution;
- programming and provisioning flow;
- calibration repeatability;
- serial number or identity assignment;
- manufacturing test boundaries;
- fixture interfaces;
- pass/fail criteria;
- traceability;
- factory reset or recovery path;
- configuration at line speed;
- work instructions that depend on architecture assumptions;
- data needed by service or support later.

Architecture is involved when these concerns require stable interfaces, test modes, calibration ownership,
configuration ownership, diagnostic surfaces, identity or provisioning models, update and recovery models, data
ownership, dependency constraints, artifact records, or owner accountability.

The future manuscript should not teach manufacturing process design. It should teach where manufacturing pressure
reveals missing architecture.

## 9. Field Reality

For this chapter, field reality means the constraints that appear after the product leaves engineering control.

Field reality includes:

- noisy power;
- environmental variation;
- network instability;
- device aging;
- user behavior;
- partial upgrades;
- configuration drift;
- service tools used by non-developers;
- logs and diagnostics available after failure;
- replacement units;
- rollback and recovery;
- support triage;
- long support horizon;
- unavailable debugger;
- unknown exact reproduction path.

Architecture is involved when these concerns require observable failure states, stable external promises, clear state
ownership, recoverable update paths, service-safe configuration, compatibility boundaries, supportable dependencies,
accessible diagnostics, repeatable reset or recovery flows, and discoverable decision records.

The future manuscript should not become Chapter 23's observability chapter, Chapter 24's release discipline chapter, or
a field-service manual.

## 10. Manufacturing and Field as Design Inputs

Chapter 21 should require the future manuscript to treat manufacturing and field reality as design inputs, not
acceptance tests after architecture.

Good architecture questions include:

- How will this be programmed repeatedly?
- Which values are calibrated, configured, derived, or fixed?
- Who owns calibration data?
- Which identity is assigned at manufacturing?
- How does a fixture talk to the device?
- What can the line test without developer tools?
- What evidence proves a unit is built correctly?
- What changes when a component or board revision changes?
- What can support see when the device fails in the field?
- What can be recovered without opening the enclosure?
- Which logs survive reset or reboot?
- Which configuration can be changed safely?
- What field failure would force an architectural change?

The future draft may use selected questions for rhythm. It should not become an oversized checklist.

## 11. In-Scope and Out-of-Scope

### In Scope

Chapter 21 covers:

- manufacturing repeatability as an architecture constraint;
- field diagnosis and supportability as architecture constraints;
- calibration, configuration, identity, traceability, and provisioning ownership;
- fixture and service-tool interfaces as product promises where other people depend on them;
- diagnostic and support-safe state without teaching full observability infrastructure;
- reset, rollback, recovery, and update implications without teaching the release playbook;
- board revisions, component substitution, environmental variation, and product evidence;
- manufacturing and field workarounds becoming hidden product behavior;
- ADRs, Decision Journal entries, Mistake Ledger entries, Architecture Review, Architecture Freeze, and
  Discoverability where proportionate.

### Explicitly Out of Scope

Do not turn Chapter 21 into:

- Chapter 22's configuration, variants, and product lines chapter;
- Chapter 23's observability in embedded systems chapter;
- Chapter 24's release discipline and upgrade-path chapter;
- Chapter 25's reference project walkthrough;
- Chapter 20's prototype-to-product transition repeated;
- a manufacturing operations manual;
- a field-service procedure;
- a QA handbook;
- a test-fixture design tutorial;
- a compliance or certification chapter;
- a new PEAK concept proposal.

## 12. Recommended Embedded-Systems Story

### Working Title

The Product That Only Worked in Engineering

### Starting System

After Chapter 20-style prototype-to-product work, an embedded team believes the product is ready for pilot manufacturing
and field trial. The lab unit works. The architecture is cleaner than the prototype. The update path, configuration path, and
service tool exist.

But the design still assumes engineering control.

### Symptoms

- Manufacturing cannot reproduce manual calibration at line speed.
- One board revision needs a different timing or sensor offset.
- Fixture access relies on a debug connector not available in the enclosure.
- Serial identity is assigned by a spreadsheet.
- The service tool shows raw developer states instead of support-safe diagnosis.
- Update recovery requires a developer laptop.
- Field logs are lost on reset.
- One component substitution changes behavior.
- Support cannot tell whether failure is configuration, hardware, firmware, or environment.
- Manufacturing workarounds become invisible product behavior.

### Principal Engineer Intervention

The Principal Engineer restates:

> Why did manufacturing and the field break the architecture?

as:

> Which manufacturing and field realities were missing from the architecture contract?

The intervention should separate manufacturing process details from architectural obligations, name repeatability,
calibration, identity, fixture, diagnostic, update and recovery, and traceability assumptions, identify owners for
manufacturing-visible state and service-visible state, expose missing evidence, define minimum architectural surfaces,
record consequential decisions, decide which deeper playbooks belong to Chapters 22 through 24, and preserve product
simplicity instead of adding a broad manufacturing mode that becomes a second architecture.

## 13. Expected Discussion Arc

1. Chapter 20 made prototype assumptions visible; Chapter 21 tests product architecture against repeated builds and
   unsupported field use.
2. Manufacturing and field reality are design inputs because they reveal who can build, diagnose, recover, and explain
   the product.
3. Some concerns are process details, but others become architecture when they require owned state, stable interfaces,
   evidence, or recoverable behavior.
4. Calibration, configuration, identity, and traceability must have owners before the product depends on them.
5. Fixture and service-tool interfaces become API promises once manufacturing or support relies on them.
6. Field reality exposes hidden state, silent coupling, platform leakage, and temporary solutions.
7. Evidence must cover repeatability, variation, substitution, reset behavior, and support diagnosis, not only lab
   success.
8. ADRs, Decision Journal entries, Mistake Ledger entries, Architecture Review, Architecture Freeze, and Discoverability
   keep manufacturing and field contracts findable.
9. The chapter names hooks for configuration, observability, and release without teaching those later chapters early.

These are intellectual progression points, not mandatory manuscript headings.

## 14. Boundaries With Part IV Chapters

Chapter 21 owns manufacturing and field reality as architecture constraints.

- Chapter 20 owns the prototype-to-product transition and prototype-to-product gap.
- Chapter 22 owns configuration, variants, and product lines.
- Chapter 23 owns observability in embedded systems.
- Chapter 24 owns release discipline and upgrade paths.
- Chapter 25 owns the reference project walkthrough.

Chapter 21 may identify configuration, observability, release, upgrade, and reference-project hooks. It must not provide
detailed configuration or variant architecture, observability infrastructure, release governance, upgrade-system design,
or reference-project implementation.

## 15. Boundaries With Earlier Parts

Use earlier chapters as constraints without repeating them:

- Chapters 5 and 13 - evidence, assumptions, and confidence.
- Chapter 7 - state ownership.
- Chapter 8 - API and protocol promises.
- Chapter 9 - dependency decisions.
- Chapter 14 - boundary placement.
- Chapter 15 - Change Radius.
- Chapter 16 - failure and recovery.
- Chapter 17 - ADR and Decision Journal records.
- Chapter 18 - Architecture Review before hardening.
- Chapter 19 - Architecture Freeze during high-risk phases.
- Chapter 20 - prototype-to-product gap and prototype assumptions.

Chapter 21 applies those ideas to manufacturing and field reality. It should not repeat Part III.

## 16. Applicability

Chapter 21 is most useful when:

- a product is moving toward pilot manufacturing or field trial;
- the lab path works but the line, support team, or field path does not;
- calibration or provisioning depends on developer knowledge;
- fixture, service-tool, or station behavior has become a product promise;
- board revision, component substitution, environment, network, reset, or aging changes behavior;
- support cannot diagnose a unit without developer tools;
- manufacturing workarounds are becoming invisible product behavior.

Not every manufacturing or field issue requires an architecture change. Local process changes with low Change Radius may
need work instructions, tests, or ownership rather than an ADR. The chapter should teach judgment, not a universal gate.

## 17. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- manufacturing is owned by software engineers;
- field failures are only architecture failures;
- every fixture detail belongs in architecture;
- every field issue requires observability infrastructure;
- every manufacturing concern requires a new API;
- support training can replace architecture;
- calibration is just a parameter;
- diagnostics are merely logs;
- all variants must be solved in Chapter 21;
- release discipline belongs in Chapter 21;
- manufacturing and field reality are new PEAK concepts.

Some issues should remain with manufacturing engineering, QA, service, release, or support. The architectural question is
whether the product needs an explicit owner, interface, state model, dependency boundary, evidence path, or recovery
promise.

## 18. Violation Patterns

The future draft should make these violations visible:

- manual calibration cannot be repeated at line speed;
- serial identity is assigned outside the product model;
- a fixture depends on a debug connector or developer-only state;
- manufacturing pass/fail criteria do not match product behavior;
- calibration state has multiple writers or no owner;
- service tools expose raw internal state instead of support-safe diagnosis;
- reset hides the evidence needed to explain a field failure;
- update recovery depends on a developer laptop;
- board or component substitutions change behavior without review;
- configuration drifts between device, station, and support records;
- manufacturing workarounds become product behavior without a decision;
- support cannot distinguish configuration, hardware, firmware, and environment failures.

Do not create a new smell or anti-pattern ID.

## 19. Engineering Principle Target

Target principle for the future draft:

> Design the product for the places where engineers are absent. Manufacturing and field reality require architecture to
> make identity, calibration, configuration, diagnostics, recovery, traceability, and ownership explicit before the
> product depends on them.

The principle should imply these questions:

1. What manual engineering step must become repeatable?
2. Which values are calibrated, configured, derived, or fixed?
3. Who owns manufacturing-visible state?
4. Who owns service-visible state?
5. How does the fixture prove the unit is built correctly?
6. What can support diagnose without developer tools?
7. Which field failure survives reset?
8. What recovery path works outside the lab?
9. Which board or component variation affects behavior?
10. Which field constraint changes the architecture?
11. Which decision record preserves the manufacturing or field contract?

The final manuscript may shorten this list for reader rhythm.

## 20. Architecture Exercise Target

### Working Title

`Expose One Manufacturing or Field Assumption`

Ask the reader to choose one product assumption that only appears outside engineering and document:

- assumption;
- whether it is manufacturing, field, or both;
- where the architecture currently hides it;
- owner;
- affected state, API, dependency, boundary, or test surface;
- evidence available;
- evidence missing;
- repeatability requirement;
- diagnostic or support need;
- recovery or rollback implication;
- calibration or configuration implication;
- traceability need;
- decision record needed;
- review or freeze trigger.

The exercise must end with:

1. one manufacturing or field assumption;
2. one owner;
3. one architectural surface to add or change;
4. one evidence or validation action.

Do not create a new canonical artifact.

## 21. Chapter-Local ADR Brief

### Working Title

`Make Calibration and Recovery Product Responsibilities Before Pilot Manufacturing`

### Context

- The lab product works with developer-assisted calibration and update recovery.
- Pilot manufacturing and field trial require repeatable calibration, fixture access, device identity, support
  diagnostics, and a recoverable update path.
- Keeping these as scripts and developer knowledge would hide architecture risk.

### Decision

- Make calibration ownership explicit.
- Define a manufacturing-safe calibration and provisioning path.
- Define minimum service-visible diagnostic states.
- Preserve update recovery without developer tools.
- Make device identity and traceability part of the architecture contract.
- Record residual assumptions and review triggers.
- Defer detailed variant, observability, and release playbooks to later chapters.

### Alternatives Considered

- Let manufacturing own the workaround.
- Keep developer scripts and train the line.
- Add a broad manufacturing mode without clear boundaries.
- Postpone service diagnostics until after field trial.
- Rely on release notes and support training.
- Rework the full product architecture before pilot.

### Consequences

Benefits include repeatability, clearer ownership, supportable diagnosis, reduced hidden field risk, and better
discoverability for future engineers.

Costs include integration effort before pilot, explicit ownership decisions, more evidence work, and constraints that
may affect future variants.

The ADR must make a real story-local architecture decision. It must not reduce to "manufacturing needs tests."

## 22. PEAK Concept Map

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
- `LAW-004` - Simplicity Is a Feature.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.

### Selected Concepts

- `LAW-001` - Every State Has One Owner: material because calibration data, configuration, identity, provisioning,
  recovery state, and service-visible state need owners.
- `LAW-002` - Every API Is a Promise: material because fixture interfaces, service tools, provisioning paths, and
  diagnostic meanings become promises once manufacturing or support relies on them.
- `LAW-005` - Evidence Before Confidence: material because lab success does not prove repeatability, variation handling,
  field diagnosis, reset behavior, or recovery outside engineering control.
- `LAW-007` - Every Dependency Is a Decision: material because fixtures, tools, vendor components, component
  substitutions, manufacturing scripts, and support processes can become architecture dependencies.
- `VOCAB-001` - Change Radius: material because manufacturing and field assumptions can affect firmware, hardware,
  fixtures, service tools, support records, tests, and release paths.
- `METRIC-001` - Change Radius: material because the chapter estimates affected surface for each manufacturing or field
  assumption.
- `METRIC-003` - Discoverability: material because manufacturing and field contracts must be findable when developers
  are absent.
- `ARTIFACT-001` - ADR: material because calibration, recovery, identity, diagnostic, and fixture contracts may require
  durable decisions.
- `ARTIFACT-003` - Decision Journal: material because smaller assumptions, accepted risks, evidence gaps, and review
  triggers need lightweight closure.
- `ARTIFACT-004` - Mistake Ledger: material because field escapes and manufacturing misses should preserve the failed
  assumption and changed architecture, without turning the chapter into a postmortem playbook.
- `RITUAL-001` - Architecture Review: material because manufacturing and field contracts should be reviewed before they
  harden into pilot behavior.
- `RITUAL-002` - Architecture Freeze: material because selected calibration, recovery, identity, and service contracts
  may need temporary stabilization before pilot manufacturing or field trial.
- `ANTIPATTERN-006` - Temporary Solution: material because manufacturing and field workarounds need owners, expiration,
  removal, or explicit risk decisions.
- `SMELL-004` - Hidden State: material because calibration flags, reset effects, provisioning status, and support-visible
  state often affect behavior without a clear model.
- `SMELL-001` - Silent Coupling: material because firmware, fixtures, station scripts, service tools, and support
  records can depend on each other without an explicit contract.
- `SMELL-005` - Platform Leakage: material because hardware, driver, and vendor-specific details can leak into product
  behavior, diagnostics, and support meanings.
- `ANTIPATTERN-002` - HAL Everywhere: material because fixture and product code must not let low-level hardware
  abstractions become the support or manufacturing contract.
- `ANTIPATTERN-003` - Global Configuration: material because calibration, station values, service settings, and field
  configuration can spread without scope, owner, or lifecycle.

### Rejected Concepts

- `FAILURE-003` - The Successful Prototype: central to Chapter 20 and predecessor context here, but Chapter 21 should not
  continue making that failure story the chapter anchor.
- `FAILURE-005` - The Release We Should Have Delayed: relevant to field-trial and release pressure, but Chapter 24 owns
  release discipline and upgrade paths.
- `LAW-004` - Simplicity Is a Feature: relevant to avoiding a broad manufacturing mode, but not selected because the
  chapter's main architecture pressure is repeatability and field supportability.
- `LAW-006` - Unused Flexibility Is Waste: relevant to avoiding premature variant machinery, but Chapter 22 owns variants
  and product lines.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as manufacturing reality, field reality, field contract, manufacturing contract, service surface,
calibration contract, fixture contract, pilot manufacturing, and field readiness remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-021` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-021
  type: references
  to: LAW-001

- from: CHAPTER-021
  type: references
  to: LAW-002

- from: CHAPTER-021
  type: references
  to: LAW-005

- from: CHAPTER-021
  type: references
  to: LAW-007

- from: CHAPTER-021
  type: references
  to: VOCAB-001

- from: CHAPTER-021
  type: references
  to: METRIC-001

- from: CHAPTER-021
  type: references
  to: METRIC-003

- from: CHAPTER-021
  type: references
  to: ARTIFACT-001

- from: CHAPTER-021
  type: references
  to: ARTIFACT-003

- from: CHAPTER-021
  type: references
  to: ARTIFACT-004

- from: CHAPTER-021
  type: references
  to: RITUAL-001

- from: CHAPTER-021
  type: references
  to: RITUAL-002

- from: CHAPTER-021
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-021
  type: references
  to: SMELL-004

- from: CHAPTER-021
  type: references
  to: SMELL-001

- from: CHAPTER-021
  type: references
  to: SMELL-005

- from: CHAPTER-021
  type: references
  to: ANTIPATTERN-002

- from: CHAPTER-021
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

Each section should serve the Chapter 21 role:

- Opening Quote: establish that product architecture must survive where engineers are absent.
- Story: show a product that works in engineering but fails under pilot manufacturing and field trial pressure.
- Discussion: teach manufacturing and field reality as design inputs, with ownership, evidence, interfaces, recovery,
  traceability, and supportability.
- Engineering Principle: anchor the move from lab control to repeatable and supportable product architecture.
- Architecture Exercise: expose one manufacturing or field assumption.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local decision to make calibration and recovery product responsibilities before pilot.
- Editor's Commentary: explain how Chapter 21 deepens Chapter 20 without teaching Chapters 22 through 24 early.

## 24. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- The lab is not the environment.
- A product needs diagnostics where developers are absent.
- Manufacturing workarounds become architecture if nobody owns them.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 25. Technical Credibility Requirements

The future draft must treat the following accurately:

- manufacturing repeatability;
- unit-to-unit variation;
- board revisions;
- component substitution;
- calibration data and ownership;
- device identity and traceability;
- provisioning;
- fixtures and test boundaries;
- service tools;
- diagnostics and support-safe state;
- field power, environment, and network variation;
- update recovery outside the lab;
- reset behavior;
- logging after reboot;
- configuration drift;
- old and replacement units;
- support triage;
- manufacturing workarounds becoming hidden product behavior.

Do not require a specific MCU, RTOS, manufacturing execution system, test framework, fixture design, field-service
process, cloud platform, issue tracker, compliance standard, or organization structure.

## 26. Terminology and Precision Guardrails

Use terms precisely:

- Manufacturing reality: repeatability, variation, traceability, calibration, programming, test, fixture, and
  provisioning pressures that appear when a product must be built repeatedly.
- Field reality: constraints that appear after the product leaves engineering control.
- Calibration: an owned product behavior, state, or evidence path when the product depends on it, not just a parameter.
- Identity: the product-recognized device identity assigned, preserved, traced, and used across manufacturing, service,
  support, and replacement flows.
- Traceability: the ability to connect a unit, configuration, calibration, build, component, decision, or field finding
  to the record that explains it.
- Diagnostic surface: the product-visible information that lets manufacturing or support understand state and failure
  without developer tools.
- Recovery path: the repeatable way to return a device to known behavior outside the lab.

Avoid misleading statements:

- Manufacturing is only process.
- Field failures are only QA problems.
- Developers must own manufacturing.
- Manufacturing must own architecture.
- Every manufacturing concern requires an architecture change.
- Every field issue needs observability infrastructure.
- Fixtures are not architecture-relevant.
- Diagnostics are merely logs.
- Support training can replace architecture.
- The chapter must solve variants, observability, or release discipline in full.

## 27. Failure Modes to Avoid

The later draft must not become:

- a generic checklist;
- a manufacturing process handbook;
- a QA handbook;
- a field-service manual;
- a fixture-design tutorial;
- an observability implementation chapter;
- a release-management chapter;
- a configuration or variant architecture chapter;
- a compliance chapter;
- Chapter 20 repeated;
- Chapter 15, 16, 17, 18, or 19 repeated;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 28. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story contains a concrete embedded product that works in engineering but fails under pilot manufacturing and field
  conditions;
- the story includes repeatability, calibration, identity, fixture access, support-safe diagnostics, update recovery,
  field logs, component substitution, and manufacturing workarounds;
- the Principal Engineer move changes the question from blame to missing architecture contracts;
- manufacturing process details are separated from architectural obligations;
- manufacturing reality and field reality remain chapter-local framing, not new PEAK concepts;
- no primary PEAK concept is assigned unless a later editor decision changes repository convention;
- state ownership, API promises, evidence, dependency decisions, Change Radius, Discoverability, ADR, Decision Journal,
  Mistake Ledger, Architecture Review, Architecture Freeze, Temporary Solution, Hidden State, Silent Coupling, Platform
  Leakage, HAL Everywhere, and Global Configuration are materially present if the registered relationship set is kept;
- later Part IV chapters remain out of scope;
- earlier chapters are used as constraints without being retaught;
- the exercise ends with one manufacturing or field assumption, one owner, one architectural surface, and one evidence
  or validation action;
- the ADR makes a genuine story-local decision about calibration and recovery before pilot manufacturing;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 29. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into manufacturing operations, support procedure, observability implementation, release
process, configuration and variants, or generic product-management advice.

Canon Review should verify that Chapter 21 remains no-primary, preserves the registered relationship set, does not
invent Manufacturing Reality or Field Reality as PEAK concepts, and keeps strict boundaries with Chapters 20, 22, 23,
24, and 25.

Technical Review should focus on realistic embedded manufacturing and field concerns: repeatability, unit variation,
board revisions, component substitution, calibration ownership, identity, traceability, provisioning, fixture and service
interfaces, diagnostics, reset and recovery behavior, support-safe state, and field constraints.

Freeze Review should confirm that Chapter 21 remains the second Part IV chapter, keeps the manuscript architecture
intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the
reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
product, manufacturing station, field trial context, calibration path, fixture interface, service-tool behavior, recovery
path, and final notebook wording while preserving the manufacturing-and-field thesis, PEAK map, and chapter boundaries.
