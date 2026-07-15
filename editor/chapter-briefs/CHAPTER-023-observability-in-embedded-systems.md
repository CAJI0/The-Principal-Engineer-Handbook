# CHAPTER-023 Canonical Brief: Observability in Embedded Systems

## 1. Metadata

- Stable ID: `CHAPTER-023`.
- Title: `Observability in Embedded Systems`.
- Part: Part IV - Building a Product.
- Chapter number: 23.
- Expected manuscript path:
  `book/04-building-a-product/23-observability-in-embedded-systems.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-023-observability-in-embedded-systems.md`.
- Branch: `chapter23`.
- Verified baseline `origin/main`: `e393001c8aa4d20668233766378695e537df13cb`.
- Baseline evidence: PR #24 squash commit, `Chapter 22: Configuration, Variants, and Product Lines (#24)`.
- Chapter 22 feature Freeze commit checked for tree equivalence:
  `3fe6f47`.
- Canonical predecessor: `CHAPTER-022` - Configuration, Variants, and Product Lines.
- Part position: fourth chapter of Part IV - Building a Product.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 23 follows the current no-primary Part IV practice and is carried by a material
  relationship set rather than by a new registry attribute.
- Central anchor or practice: none registered. Observability, product event, diagnostic surface, support evidence,
  reset snapshot, crash snapshot, and field diagnostic remain chapter-local working terms.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `e393001c8aa4d20668233766378695e537df13cb`.
- That baseline is the PR #24 squash commit, `Chapter 22: Configuration, Variants, and Product Lines (#24)`.
- The squash commit is an ancestor of current `origin/main` and has parent
  `4176829b64f5d920349fe27cb05cfaf654c8d306`.
- The Chapter 22 feature-branch Freeze commit `3fe6f47` remains tree-equivalent for the checked Chapter 22 lifecycle
  files in the squash commit.
- `CHAPTER-001` through `CHAPTER-022` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-022` is the third Part IV chapter and is canonical.
- The table of contents places `Observability in Embedded Systems` fourth in Part IV - Building a Product.
- `book/04-building-a-product/README.md` exists and remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `ARTIFACT-005` - Event Catalog and `SMELL-006` - Event Explosion exist and are available as central supporting
  concepts for event meaning and event noise.
- `CHAPTER-023` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 23 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter23` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part IV Role

Chapter 23 follows Chapter 22 by showing that supported product promises must be explainable after the product leaves
engineering control.

Chapter 20 moved the reader from prototype evidence to product obligations. Chapter 21 made manufacturing and field
reality architecture inputs. Chapter 22 made configuration, variants, and product-line differences explicit. Chapter 23
should now teach that a product with owned state, supported variants, update paths, recovery behavior, service tools,
and field obligations must be able to explain enough of its state and history for people without a debugger to make
supportable decisions.

The chapter must not become a generic logging tutorial, cloud observability guide, metrics-platform design, tracing
framework handbook, monitoring-operations playbook, incident-response chapter, release-discipline chapter, or vendor
tooling comparison. It is an architecture chapter about embedded products making their important state transitions,
boundary outcomes, failures, and diagnostic meanings visible under product constraints.

## 4. Canonical Purpose

Prepare Chapter 23 to teach that observability is not "add logs later." It is an architectural promise that the product
can explain important state transitions, failures, and decisions after it leaves engineering control.

Candidate thesis for the future manuscript:

> Observability in an embedded product is the ability to reconstruct enough of the product's state, history, and
> boundary interactions to make supportable decisions without a debugger.

The chapter should move the reader away from treating observability as print debugging, verbose logging, cloud
dashboards, metrics everywhere, tracing framework adoption, post-release support tooling, support's responsibility, a
storage-size problem only, a single debug mode, developer-only messages, or a replacement for state ownership, failure
design, testing, and release discipline.

The core question should become:

> When this device fails away from engineering, what evidence will tell us what state it was in, what it was trying to
> do, what boundary failed, and what decision we can safely make next?

## 5. Primary-Concept Resolution

Chapter 23 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a dedicated primary concept attribute to chapter records. Chapter 23 follows
that convention and should be carried by its exact relationship set.

Observability is a necessary chapter-local frame, but it is not registered as a PEAK vocabulary concept, law, metric,
artifact, ritual, smell, anti-pattern, failure story, or primary concept. Product event, field event, diagnostic
surface, support evidence, reset snapshot, crash snapshot, event severity, trace context, debug mode, diagnostic
contract, and observability debt are also chapter-local prose terms only.

## 6. Central Thesis

Observability in an embedded product is decision-oriented evidence under constraint. The product should preserve enough
owned event meaning, state transition history, reset or fault context, version and configuration identity, variant
identity, and boundary outcomes to let support and engineering decide what happened and what to do next without a
debugger.

Approved supporting formulation for the future draft:

> Design observability around decisions, not volume.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. observability means more logs;
2. developer debug output is close enough to field diagnostics;
3. support can infer product state from symptoms;
4. error codes are enough if they are documented somewhere;
5. field diagnostics can be added after the product ships;
6. cloud telemetry is required for useful observability;
7. every module should emit whatever events it knows;
8. retained crash context is only an implementation detail.

By the end of the chapter, the reader should be able to:

1. name the decisions observability must support;
2. distinguish developer debug logs from support-safe product diagnostics;
3. identify which state transitions, boundary outcomes, versions, configurations, variants, reset reasons, and recovery
   states must be visible;
4. assign ownership for event meaning and diagnostic interpretation;
5. keep event volume bounded by decision use;
6. reason about time, ordering, boot counters, sequence numbers, and clock uncertainty;
7. record event meanings in an Event Catalog or equivalent durable record;
8. decide what must survive reset, what may be sampled, and what should remain out of scope for RAM, flash, power,
   bandwidth, privacy, security, or support-safety reasons.

## 8. Embedded Observability Scope

For this chapter, embedded observability means a constrained product capability to reconstruct relevant state, history,
and boundary interactions after engineering is absent.

It may include:

- product events;
- state transitions;
- counters;
- error codes;
- reset reasons;
- fault snapshots;
- version and configuration fingerprints;
- variant identity;
- update and recovery state;
- dependency health;
- boundary interaction outcomes;
- service-tool diagnostics;
- manufacturing and field diagnostics;
- compact logs;
- retained crash context;
- time correlation;
- severity and support-safe meaning.

It is bounded by RAM, flash, CPU budget, power budget, flash wear, privacy, security, bandwidth, service access, field
replacement realities, unreliable time sources, partial logs, reset and reboot loss, product variants, release
compatibility, and update compatibility.

Do not write a logging library tutorial.

## 9. Observability as Product Architecture

Observability is architecture when it defines:

- what states are observable;
- who owns event meaning;
- what boundary interactions are recorded;
- what diagnostics are support-safe;
- what is retained across reset;
- what is available without developer tools;
- how events map to API promises and state ownership;
- how versions, configurations, and variants are visible;
- how recovery and update progress can be reconstructed;
- how field evidence flows into decisions, Decision Journal entries, and Mistake Ledger entries.

Observability is not the same as logging volume. More logs can reduce clarity when event meaning, ownership, time, and
decision use are missing. The future draft should show that the right event can be more valuable than a large stream of
unowned messages.

## 10. Event Design and Event Catalog

Use `ARTIFACT-005` - Event Catalog materially.

The chapter should distinguish:

- event name;
- event owner;
- state or boundary represented;
- trigger;
- severity;
- payload;
- retention;
- support meaning;
- privacy and security sensitivity;
- versioning;
- deprecation;
- relation to recovery or update decisions.

The future manuscript may use an Event Catalog as a compact inventory of product events, but it must not become a
template tutorial.

Also address `SMELL-006` - Event Explosion. Too many unowned events can become noise, hidden coupling, and incompatible
support promises. The test for a product event is not whether a module can emit it. The test is whether an owner can
state the decision it helps someone make.

## 11. Time and Causality

Tie observability to `LAW-003` - Time Is a Dependency.

Embedded products often lack reliable wall-clock time. The future draft should cover monotonic time, boot counters,
sequence numbers, reset reasons, event ordering, correlation IDs where appropriate, local timestamps, server or service
timestamps when available, clock uncertainty, power-loss gaps, and partial histories.

The chapter should not become a timekeeping implementation guide. It should teach that event interpretation depends on
the time model the product can honestly provide. A timestamp without source, validity, boot generation, sequence, or
uncertainty may be weaker evidence than a simple ordered record that explains what happened before reset.

## 12. In-Scope and Out-of-Scope

### In Scope

Chapter 23 covers:

- observability as embedded product architecture;
- decision-oriented field evidence;
- state transitions and boundary outcomes;
- owned event meaning and Event Catalog entries;
- avoiding Event Explosion;
- reset reasons, retained fault context, boot counters, and update or recovery state;
- version, configuration, variant, and manufacturing identity visibility;
- service-tool and support-safe diagnostics;
- time, ordering, sequence, and partial histories;
- constraints from RAM, flash, CPU, power, wear, bandwidth, privacy, security, service access, and field replacement;
- ADRs, Decision Journal entries, Mistake Ledger entries, Architecture Review, and Architecture Freeze where
  proportionate.

### Explicitly Out of Scope

Do not turn Chapter 23 into:

- Chapter 20's prototype-to-product transition repeated;
- Chapter 21's manufacturing and field reality chapter repeated;
- Chapter 22's configuration, variants, and product lines chapter repeated;
- Chapter 24's release discipline and upgrade-path chapter;
- Chapter 25's reference project walkthrough;
- a logging library tutorial;
- a cloud observability or telemetry platform guide;
- a metrics or tracing framework handbook;
- a dashboard design chapter;
- an incident-response playbook;
- a support operations process;
- a vendor tooling comparison;
- a new PEAK concept proposal.

## 13. Recommended Embedded-Systems Story

### Working Title

The Device That Could Not Explain Itself

### Starting System

An embedded product from Chapters 20 through 22 is in field trial. It has manufacturing identity, supported variants,
service tools, update and recovery paths, and supported configurations. It works in normal tests.

### Field Issue

Devices intermittently stop reporting after update. The service tool shows generic "communication failed." Development
builds had debug logs, but field builds do not. The reset reason is overwritten. Configuration version is not visible.
Variant state is stored but not reported. Update state is lost after reboot. Radio, network, gateway, firmware,
configuration, and application errors share one code. Manufacturing identity exists but is not tied to field
diagnostics. Support cannot tell whether the fault is firmware, configuration, gateway, network, power, variant, or
recovery path.

### Principal Engineer Intervention

The team asks:

> Can we add more logs?

The Principal Engineer restates:

> What decision must support or engineering make, and what evidence must the device preserve so that decision is
> possible?

The intervention should identify the decisions observability must support, define owned events for important state
transitions and boundary failures, separate developer debug logs from product diagnostics, preserve reset, recovery,
and update context where necessary, make variant, configuration, version, and identity visible, distinguish radio,
gateway, network, firmware, configuration, dependency, and power failures, define what service can see without
developer tools, avoid event explosion, record event meaning in an Event Catalog, and feed false assumptions or field
escapes into the Mistake Ledger where appropriate.

## 14. Expected Discussion Arc

1. Chapter 22 made product differences explicit; Chapter 23 asks whether those supported realities can be explained in
   the field.
2. Observability is not logging volume. It is evidence for decisions after engineering is absent.
3. A useful diagnostic starts with the decision it must support.
4. Developer debug logs and product diagnostics have different audiences, meanings, retention, and safety constraints.
5. Events need owners, triggers, payloads, retention rules, support meaning, versioning, and deprecation.
6. Reset, power loss, partial logs, and unreliable clocks are normal embedded constraints, not excuses to avoid
   evidence.
7. Version, configuration, variant, identity, update state, recovery state, and boundary outcomes must be visible when
   they affect diagnosis.
8. Event Catalog entries and records keep diagnostic meaning discoverable.
9. Event Explosion, Hidden State, Silent Coupling, Platform Leakage, Global Configuration, HAL Everywhere, Callback
   Hell, and Temporary Solution are common ways observability becomes noise or false confidence.
10. The chapter names release and upgrade consequences without teaching Chapter 24.

These are intellectual progression points, not mandatory manuscript headings.

## 15. Boundaries With Part IV Chapters

Chapter 23 owns observability in embedded systems as architecture pressure.

- Chapter 20 owns the prototype-to-product transition and prototype-to-product gap.
- Chapter 21 owns manufacturing and field reality.
- Chapter 22 owns configuration, variants, and product lines.
- Chapter 24 owns release discipline and upgrade paths.
- Chapter 25 owns the reference project walkthrough.

Chapter 23 may mention update state, recovery state, release compatibility, and upgrade diagnostics only as
observability consequences. It must not teach release governance, rollout strategy, upgrade architecture, rollback
policy, or reference-project implementation.

## 16. Boundaries With Earlier Parts

Use earlier chapters as constraints without repeating them:

- Chapter 7 - observable state needs owners.
- Chapter 8 - diagnostic outputs and event meanings are promises.
- Chapter 9 - telemetry transports, logging libraries, service tools, gateways, and cloud services are dependency
  decisions.
- Chapter 10 - event ordering and timestamps depend on time assumptions.
- Chapter 13 - field evidence must support confidence, not noise.
- Chapter 15 - adding observability has Change Radius across firmware, service tools, support, storage, bandwidth,
  release, and tests.
- Chapter 16 - observability helps recovery decisions but does not replace failure design.
- Chapter 17 - Event Catalog, ADRs, Decision Journal entries, and Mistake Ledger entries preserve meanings and follow-up
  decisions.
- Chapter 21 - manufacturing and field diagnostics are context, not the whole chapter.
- Chapter 22 - variants and configuration must be visible in diagnostics.

Chapter 23 applies those ideas to embedded observability. It should not repeat Part II laws or the Part III playbook.

## 17. Applicability

Chapter 23 is most useful when:

- a product is entering field trial, pilot, or supported release;
- support cannot distinguish firmware, configuration, variant, gateway, network, power, dependency, update, or recovery
  failure;
- field builds differ from developer builds in diagnostic behavior;
- reset or reboot destroys the evidence needed to explain failure;
- service tools expose raw internal states instead of support-safe meanings;
- product variants, configuration versions, and manufacturing identity affect diagnosis;
- cloud telemetry is unreliable, unavailable, expensive, or insufficient;
- logs exist but nobody can state what decision they support.

Not every device needs heavy telemetry. A low-cost product, privacy-sensitive product, battery-powered product, or
offline device may need compact retained context, service-tool diagnostics, counters, and support-safe error meaning
rather than continuous remote streams.

## 18. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- every product needs cloud telemetry;
- more logs automatically improve observability;
- all logs must survive reset;
- all diagnostics must be user-visible;
- every event needs an ADR;
- every module should emit events freely;
- error codes are useless;
- support can replace missing product evidence with training;
- observability replaces testing, failure design, release discipline, or incident response;
- verbose debug builds are product observability;
- storing everything is responsible.

Some failures may remain impossible to reconstruct fully. The architectural obligation is to preserve enough evidence
for the decisions the product reasonably needs to support under its constraints.

## 19. Violation Patterns

The future draft should make these violations visible:

- field builds remove the only useful diagnostic path;
- reset overwrites the reason support needed;
- update state is lost after reboot;
- configuration and variant identity are invisible to service;
- radio, gateway, network, firmware, configuration, power, and dependency failures share one code;
- events have names but no owners;
- logs contain volume without decision use;
- service tools expose raw developer vocabulary;
- event payloads leak private or security-sensitive data;
- timestamps exist without source, validity, boot generation, or ordering meaning;
- each module invents its own event vocabulary;
- retained logs wear flash or drain power without supporting a decision.

Do not create a new smell or anti-pattern ID.

## 20. Engineering Principle Target

Target principle for the future draft:

> Design observability around decisions, not volume. Name the state transitions, boundary outcomes, versions, variants,
> reset context, and failure evidence the product must preserve so people without a debugger can decide what happened
> and what to do next.

The principle should imply these questions:

1. What decision will this evidence support?
2. Which state transition matters?
3. Which boundary interaction failed?
4. Who owns the event meaning?
5. What must survive reset?
6. Which version, configuration, and variant were active?
7. What can support see without developer tools?
8. Which error is recoverable, safe to retry, fatal, or customer-actionable?
9. What event is noise?
10. What event needs catalog ownership?
11. What field failure would be impossible to diagnose today?

The final manuscript may shorten this list for reader rhythm.

## 21. Architecture Exercise Target

### Working Title

`Make One Failure Explain Itself`

Ask the reader to choose one field failure or ambiguous support case and document:

- decision the evidence must support;
- current missing evidence;
- state transition or boundary involved;
- event owner;
- event or diagnostic name;
- payload;
- severity;
- retention requirement;
- reset or reboot behavior;
- time or sequence model;
- version, configuration, and variant context;
- support-safe meaning;
- privacy or security consideration;
- record to update;
- validation action.

The exercise must end with:

1. one decision the evidence must support;
2. one owned event or diagnostic;
3. one retained context requirement;
4. one validation action.

Do not create a new canonical artifact.

## 22. Chapter-Local ADR Brief

### Working Title

`Adopt Decision-Oriented Field Events for Update and Recovery Failures`

### Context

- Field-trial devices can fail after update or recovery.
- Current debug logs do not exist in field builds.
- Service diagnostics cannot distinguish firmware, configuration, variant, gateway, network, power, update, or recovery
  failure.
- Storage, bandwidth, wear, and privacy are constrained.

### Decision

- Define a bounded set of owned product events for update, recovery, reset, configuration, variant, and boundary
  failures.
- Preserve reset reason, update state, active version, configuration fingerprint, variant identity, and selected
  boundary outcomes when needed.
- Separate developer debug logs from support-safe product diagnostics.
- Maintain Event Catalog entries for event meaning, owner, payload, retention, support meaning, and versioning.
- Avoid event explosion by requiring a decision use for each product event.
- Record false assumptions and field escapes in Mistake Ledger entries where appropriate.
- Defer release and upgrade-path policy to Chapter 24.

### Alternatives Considered

- Add verbose logs everywhere.
- Rely on developer debug builds.
- Push all telemetry to the cloud.
- Keep only error codes.
- Let service support infer state from symptoms.
- Wait until after release to add diagnostics.
- Let every module define its own event vocabulary.

### Consequences

Benefits include better field diagnosis, clearer support decisions, bounded storage cost, stronger event ownership,
more discoverable diagnostic meaning, and better evidence for future architecture decisions.

Costs include Event Catalog maintenance, compatibility and versioning work, privacy and security review, flash wear and
retention trade-offs, service-tool updates, and validation work to prove that events actually support decisions.

The ADR must make a real story-local architecture decision. It must not reduce to "add logging."

## 23. PEAK Concept Map

### Concepts Inspected

- `ARTIFACT-005` - Event Catalog.
- `SMELL-006` - Event Explosion.
- `FAILURE-002` - One Lost Packet.
- `FAILURE-005` - The Release We Should Have Delayed.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-005` - Evidence Before Confidence.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-002` - Weak Signal.
- `ARTIFACT-007` - Weak Signal Register.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-001` - ADR.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `SMELL-004` - Hidden State.
- `SMELL-001` - Silent Coupling.
- `SMELL-005` - Platform Leakage.
- `ANTIPATTERN-002` - HAL Everywhere.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-005` - Callback Hell.
- `ANTIPATTERN-006` - Temporary Solution.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.

### Selected Concepts

- `ARTIFACT-005` - Event Catalog: material because the chapter needs a durable record of event meaning, owner, payload,
  retention, support meaning, timing assumptions, and failure behavior.
- `SMELL-006` - Event Explosion: material because the chapter must show how unbounded events become noise and hidden
  support promises.
- `LAW-001` - Every State Has One Owner: material because observable state, reset context, update state, configuration
  identity, and event meaning need owners.
- `LAW-002` - Every API Is a Promise: material because diagnostic outputs, event meanings, service-tool messages, and
  support-safe error categories become promises.
- `LAW-003` - Time Is a Dependency: material because event ordering, timestamps, boot counters, sequence numbers, and
  reset interpretation depend on time assumptions.
- `LAW-005` - Evidence Before Confidence: material because field evidence must support decisions rather than create
  false confidence.
- `LAW-007` - Every Dependency Is a Decision: material because telemetry transports, logging libraries, service tools,
  gateways, cloud services, storage, and protocols import failure modes and ownership.
- `VOCAB-001` - Change Radius: material because adding observability affects firmware, service tools, support, storage,
  bandwidth, privacy, release, tests, and records.
- `METRIC-001` - Change Radius: material because the chapter estimates affected surface for each product event or
  diagnostic change.
- `METRIC-003` - Discoverability: material because future engineers and support need to find event meaning, owner,
  diagnostic contract, and decision records.
- `ARTIFACT-001` - ADR: material because consequential observability scope, retained context, and diagnostic contract
  decisions may need durable records.
- `ARTIFACT-003` - Decision Journal: material because smaller diagnostic choices, evidence gaps, confidence, and review
  triggers may need lightweight closure.
- `ARTIFACT-004` - Mistake Ledger: material because field escapes should preserve the failed assumption and changed
  evidence path without becoming a postmortem chapter.
- `ARTIFACT-007` - Weak Signal Register: material because ambiguous field symptoms and repeated support reports may need
  tracking before they become confirmed failures.
- `VOCAB-002` - Weak Signal: material because observability often begins with incomplete field observations that should
  change investigation without becoming proof.
- `RITUAL-001` - Architecture Review: material because diagnostic contracts and retained evidence paths should be
  reviewed before they harden.
- `RITUAL-002` - Architecture Freeze: material because selected event meanings and diagnostic contracts may need
  temporary stability before field trial or release validation.
- `SMELL-004` - Hidden State: material because unobservable configuration, reset, update, recovery, or variant state
  forces diagnosis by guesswork.
- `SMELL-001` - Silent Coupling: material because firmware, service tools, gateways, support records, and tests can
  depend on event meaning without an explicit contract.
- `SMELL-005` - Platform Leakage: material because hardware, driver, and vendor-specific errors can leak into support
  language unless translated to product-level reasons.
- `ANTIPATTERN-002` - HAL Everywhere: material because diagnostics should not expose low-level hardware vocabulary as
  the product contract.
- `ANTIPATTERN-003` - Global Configuration: material because broad configuration affects diagnostic meaning,
  observability behavior, and support interpretation.
- `ANTIPATTERN-005` - Callback Hell: material because callback-driven ordering and failure behavior can make events hard
  to trace or own.
- `ANTIPATTERN-006` - Temporary Solution: material because temporary diagnostics and debug modes need owner, expiration,
  removal, or explicit decision.
- `FAILURE-002` - One Lost Packet: material because lost, reordered, or missing boundary events are a concrete
  observability failure in embedded update and communication paths.

### Rejected Concepts

- `FAILURE-005` - The Release We Should Have Delayed: relevant to late release pressure, but Chapter 24 owns release
  discipline and upgrade paths.
- `METRIC-004` - API Stability: relevant to diagnostic meaning versioning, but `LAW-002`, Event Catalog, Change Radius,
  and Discoverability are sufficient for this chapter's graph.
- `ARTIFACT-002` - RFC: useful for broad observability proposals, but the chapter-local decision can be carried by ADR,
  Decision Journal, Event Catalog, review, and freeze without adding another outgoing edge.
- `ARTIFACT-006` - Architecture Ledger: useful for active decisions, but not necessary for the Chapter 23 relationship
  set.
- `VOCAB-006` - Architecture Freeze and later health-review concepts: related through `RITUAL-002` and later operating
  models, but not needed as outgoing Chapter 23 relationships.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as observability, telemetry, diagnostic surface, product event, field event, event severity, trace context,
debug mode, diagnostic contract, support evidence, reset snapshot, crash snapshot, and observability debt remain
chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-023` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-023
  type: illustrates
  to: ARTIFACT-005

- from: CHAPTER-023
  type: illustrates
  to: SMELL-006

- from: CHAPTER-023
  type: references
  to: LAW-001

- from: CHAPTER-023
  type: references
  to: LAW-002

- from: CHAPTER-023
  type: references
  to: LAW-003

- from: CHAPTER-023
  type: references
  to: LAW-005

- from: CHAPTER-023
  type: references
  to: LAW-007

- from: CHAPTER-023
  type: references
  to: VOCAB-001

- from: CHAPTER-023
  type: references
  to: METRIC-001

- from: CHAPTER-023
  type: references
  to: METRIC-003

- from: CHAPTER-023
  type: references
  to: ARTIFACT-001

- from: CHAPTER-023
  type: references
  to: ARTIFACT-003

- from: CHAPTER-023
  type: references
  to: ARTIFACT-004

- from: CHAPTER-023
  type: references
  to: ARTIFACT-007

- from: CHAPTER-023
  type: references
  to: VOCAB-002

- from: CHAPTER-023
  type: references
  to: RITUAL-001

- from: CHAPTER-023
  type: references
  to: RITUAL-002

- from: CHAPTER-023
  type: references
  to: SMELL-004

- from: CHAPTER-023
  type: references
  to: SMELL-001

- from: CHAPTER-023
  type: references
  to: SMELL-005

- from: CHAPTER-023
  type: references
  to: ANTIPATTERN-002

- from: CHAPTER-023
  type: references
  to: ANTIPATTERN-003

- from: CHAPTER-023
  type: references
  to: ANTIPATTERN-005

- from: CHAPTER-023
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-023
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

Each section should serve the Chapter 23 role:

- Opening Quote: establish that logs are useful only when they become decision-ready evidence.
- Story: show an embedded product in field trial that cannot explain a post-update communication failure.
- Discussion: teach decision-oriented observability, event ownership, reset and update context, time and causality,
  diagnostic meaning, constraints, and event noise.
- Engineering Principle: anchor the move from log volume to supportable evidence.
- Architecture Exercise: make one failure explain itself.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local decision to adopt decision-oriented field events for update and recovery failures.
- Editor's Commentary: explain how Chapter 23 follows Chapter 22 without teaching Chapter 24 early.

## 25. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- Logs are not evidence until someone can use them.
- An event without an owner becomes noise.
- A device should explain enough to be helped.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 26. Technical Credibility Requirements

The future draft must treat the following accurately:

- constrained RAM, flash, CPU, and power;
- flash wear and retained logs;
- ring buffers and compact logs at a conceptual level;
- reset reason retention;
- crash and fault snapshots;
- boot counters and sequence numbers;
- monotonic versus wall-clock time;
- partial logs and power loss;
- firmware, service-tool, gateway, and cloud boundaries;
- version, configuration, variant, and identity fingerprints;
- update and recovery state;
- transport, radio, and network failures;
- service-tool diagnostics;
- support-safe error meanings;
- privacy and security sensitivity;
- manufacturing identity and field diagnostics;
- event versioning and deprecation;
- field diagnosis without a debugger.

Do not require a specific RTOS, logging library, cloud platform, telemetry protocol, tracing format, storage device,
service tool, database, dashboard, or observability vendor.

## 27. Terminology and Precision Guardrails

Use terms precisely:

- Observability: the product's ability to preserve enough state, history, and boundary evidence to make supportable
  decisions after engineering is absent.
- Product event: an owned event whose meaning, trigger, payload, retention, and support use are part of the product
  diagnostic surface.
- Developer debug log: output intended for engineering during development, not automatically suitable for field support.
- Product diagnostic: support-safe evidence available through product-supported paths.
- Reset context: retained information that explains why a reboot or reset happened and what state may have been lost.
- Event owner: the boundary responsible for event meaning, lifecycle, versioning, and interpretation.
- Support-safe meaning: wording and categories that help support act without exposing private, unsafe, or misleading
  internal detail.

Avoid misleading statements:

- More logs automatically improve observability.
- Every module should emit events freely.
- Cloud telemetry is required.
- Error codes are useless.
- All logs must survive reset.
- All diagnostics must be user-visible.
- Every event needs an ADR.
- Observability replaces testing, failure design, release discipline, or support training.
- Verbose debug builds are product observability.
- Observability means storing everything.

## 28. Failure Modes to Avoid

The later draft must not become:

- a generic logging tutorial;
- a cloud telemetry architecture chapter;
- a metrics platform chapter;
- a tracing framework handbook;
- a dashboard or monitoring-operations guide;
- an incident-response chapter;
- a support procedure;
- a release-discipline or upgrade-path chapter;
- Chapter 21 or Chapter 22 repeated;
- Chapter 24 written early;
- a vendor tooling comparison;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 29. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story contains a concrete embedded product in field trial that cannot explain an intermittent post-update
  reporting failure;
- the story includes missing field logs, overwritten reset reason, invisible configuration version, invisible variant
  state, lost update state, ambiguous error codes, manufacturing identity not tied to diagnostics, and no developer
  debugger;
- the Principal Engineer move changes the question from adding logs to identifying decisions and required evidence;
- observability remains a chapter-local frame and no primary PEAK concept is assigned unless a later editor decision
  changes repository convention;
- `ARTIFACT-005` and `SMELL-006` are materially present if the registered relationship set is kept;
- event ownership, Event Catalog, reset context, update and recovery state, version, configuration, variant identity,
  boundary outcomes, support-safe diagnostics, time uncertainty, and constrained storage are materially present;
- selected PEAK concepts are materially present if the registered relationship set is kept;
- later Part IV chapters remain out of scope;
- earlier chapters are used as constraints without being retaught;
- the exercise ends with one decision, one owned event or diagnostic, one retained context requirement, and one
  validation action;
- the ADR makes a genuine story-local decision about decision-oriented field events for update and recovery failures;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 30. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into logging tutorial, cloud observability, support operations, incident response, release
discipline, or generic checklist advice.

Canon Review should verify that Chapter 23 remains no-primary, preserves the registered relationship set, does not
invent Observability or Diagnostic Surface as PEAK concepts, materially illustrates Event Catalog and Event Explosion,
and keeps strict boundaries with Chapters 20, 21, 22, 24, and 25.

Technical Review should focus on realistic embedded observability constraints: RAM, flash, CPU, power, flash wear,
partial logs, reset loss, crash context, boot counters, time uncertainty, field builds, service tools, gateways,
networks, versions, configurations, variants, update and recovery state, diagnostic language, privacy, security, and
support without a debugger.

Freeze Review should confirm that Chapter 23 remains the fourth Part IV chapter, keeps the manuscript architecture
intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the
reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
product, field-trial failure, service-tool details, event names, retained-context choices, diagnostic wording, and final
notebook wording while preserving the observability thesis, PEAK map, and chapter boundaries.
