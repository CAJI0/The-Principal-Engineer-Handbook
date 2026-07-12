# CHAPTER-014 Canonical Brief: Drawing Boundaries That Survive Change

## Metadata

- Stable ID: `CHAPTER-014`.
- Title: `Drawing Boundaries That Survive Change`.
- Part: Part III - Architecture Playbook.
- Chapter number: 14.
- Expected manuscript path: `book/03-architecture-playbook/14-drawing-boundaries-that-survive-change.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-014-drawing-boundaries-that-survive-change.md`.
- Branch: `chapter14`.
- Verified baseline `origin/main`: `b478e3d5a01977ffb2676c9b309c9f700ba78a80`.
- Canonical predecessor: `CHAPTER-013` - Evidence Before Confidence.
- Part position: first chapter of Part III - Architecture Playbook.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 14 is a practice chapter, and current repository convention does not require a
  practice chapter to declare one primary PEAK concept.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## Repository-Grounded Findings

- `origin/main` resolves to `b478e3d5a01977ffb2676c9b309c9f700ba78a80`.
- That baseline is the PR #15 squash commit, `Chapter 13: Evidence Before Confidence (#15)`.
- The Chapter 13 feature-branch Freeze commit `41d2ffaefd8632c8193160396e485e890ebf631f` is not required to be an
  ancestor of `main` because PR #15 used squash merge.
- The final Chapter 13 lifecycle files in the PR #15 squash commit are tree-equivalent to the final feature-branch
  Freeze commit for the checked Chapter 13 paths.
- `CHAPTER-001` through `CHAPTER-013` are registered as `canonical` in `knowledge/index.yaml`.
- Part II contains all seven planned law chapters in table-of-contents order.
- `CHAPTER-013` is the final Part II chapter and is canonical.
- `editor/EDITOR_LOG.md` records Chapter 13 Editorial, Canon, Technical, and Freeze Review entries in order.
- The repository table of contents places `Drawing Boundaries That Survive Change` as the first chapter of Part III.
- `book/03-architecture-playbook/README.md` remains a Part III placeholder and should not be expanded in this phase.
- `CHAPTER-014` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 14 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter14` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 1. Part III Opening Role

Chapter 14 opens Part III by turning the Part II laws into an architecture practice.

Part II named the laws. Part III should show how a Principal Engineer uses those laws to make architecture decisions
visible, reviewable, and durable. Boundaries are the first practice because they are where ownership, API promises,
dependency direction, time, flexibility, simplicity, and evidence become concrete in the shape of a system.

The chapter should not summarize every law at length. It should show that boundary decisions are the place where laws
stop being slogans and become product-level contracts, translation points, ownership decisions, and change constraints.

## 2. Canonical Purpose

Prepare Chapter 14 to teach how to draw architecture boundaries that survive expected change.

The chapter should move the reader from treating boundaries as directories, interfaces, layers, processes, services, or
driver wrappers toward treating a boundary as an intentional separation of responsibility, authority, and knowledge.

The chapter must help readers answer:

> Which decisions belong together, which decisions must remain separate, and what may cross between them?

The chapter must not create a reader-facing draft during this task. It must constrain the later Author Draft.

## 3. Primary-Concept Resolution

Chapter 14 has no primary PEAK concept at canonical-brief registration time.

Repository precedent for Part II law chapters uses a primary law because those chapters are organized around laws.
Chapter 14 is the first Part III practice chapter. Current `knowledge/index.yaml` chapter records do not contain a
primary-concept field, and current canon does not define a primary-concept requirement for practice chapters.

The chapter should therefore record an explicit no-primary resolution and use outgoing PEAK relationships to show the
concepts materially carried by the chapter. Do not force `LAW-001`, `LAW-002`, `LAW-007`, `VOCAB-001`, or any other
existing concept into a primary role merely because it is relevant.

## 4. Central Thesis

A durable boundary separates decisions that change for different reasons, keeps product authority and vocabulary on the
correct side, and limits what a change must know about the rest of the system.

Approved supporting formulation for the future draft:

> Draw boundaries around product decisions and coherent reasons to change. Keep authority, vocabulary, and dependency
> direction explicit, and translate volatile mechanisms at the edge.

This formulation is chapter-level language. Do not register it as a new PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 5. Reader Transformation

Before the chapter, the reader may think:

1. a boundary is a directory, file, class, C module, interface, task, process, service, library, or HAL wrapper;
2. adding an interface means the system is decoupled;
3. layers prove that responsibilities are separated;
4. runtime call direction is the same thing as dependency direction;
5. product code can use vendor enumeration values and RTOS details if a wrapper exists somewhere nearby;
6. callbacks, events, queues, or messages are automatically better boundary mechanisms than direct calls;
7. the right response to a second vendor is a universal driver interface;
8. more boundaries always reduce change cost.

By the end of the chapter, the reader should be able to:

1. define an architecture boundary as a separation of responsibility, authority, and knowledge;
2. distinguish a boundary from a module, interface, layer, process, or driver wrapper;
3. identify the product decision and reason to change that belong inside a boundary;
4. keep product vocabulary from being shaped by platform vocabulary;
5. separate dependency direction from runtime flow;
6. decide what may cross a boundary and what must be translated at the edge;
7. detect back channels that reveal a false boundary;
8. weigh boundary granularity and cost proportionately.

## 6. Semantic Definition of an Architecture Boundary

An architecture boundary is an intentional separation of responsibility, authority, and knowledge.

A useful boundary clarifies:

- which product decision lives inside it;
- who owns that decision;
- what state is authoritative;
- which dependencies point inward or outward;
- which vocabulary may cross;
- what behavior is promised;
- what remains hidden;
- how failures and completion are represented;
- which reasons for change it contains.

A boundary is not defined solely by deployment, compilation, process separation, directory structure, language boundary,
or interface shape. Those structures may implement a boundary. They do not prove that the boundary protects a product
decision.

## 7. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 14 covers:

- boundary placement and boundary integrity;
- product decisions and coherent reasons to change;
- authority, ownership, and state visibility at a boundary;
- product vocabulary versus platform vocabulary;
- dependency direction versus runtime call direction;
- boundary contracts and translation at the edge;
- direct calls, messages, callbacks, events, queues, shared memory, snapshots, and asynchronous completion as mechanisms;
- back channels that bypass the intended contract;
- boundary granularity, boundary cost, and proportionality;
- a radio or peripheral integration story where a wrapper leaks vendor details through the product;
- an ADR that places integration behind a product-owned control boundary.

### Explicitly Out of Scope

Do not turn Chapter 14 into:

- a Clean Architecture summary;
- a ports-and-adapters tutorial;
- a SOLID chapter;
- a dependency-injection tutorial;
- a directory-layout guide;
- a layer-count argument;
- an API versioning chapter;
- a dependency-selection chapter;
- a state-ownership chapter;
- a complete Change Radius chapter;
- a failure and recovery chapter;
- an ADR or RFC tutorial;
- an Architecture Review procedure;
- a generic microservices argument;
- an anti-HAL essay;
- a framework-building exercise;
- a heroic rewrite narrative.

## 8. Boundary Versus Module, Interface, Layer, and Process

The future draft must distinguish:

- module: a code organization unit;
- interface: a contract surface;
- layer: a structural ordering;
- process or task: a runtime execution unit;
- boundary: a decision and knowledge separation.

A boundary may be implemented by several modules. One module may contain more than one boundary and therefore be
architecturally unhealthy. An interface can exist without protecting a meaningful boundary. A process boundary can still
leak product authority and platform details.

The chapter should not reward structure for its own sake. The reader should learn to ask what decision the structure
protects.

## 9. Product Decisions and Reasons to Change

A boundary should group decisions that change for coherent reasons and separate decisions that change for different
reasons.

The future draft should distinguish reasons such as:

- product policy;
- hardware integration;
- vendor protocol;
- UI presentation;
- persistence;
- transport;
- manufacturing;
- field diagnostics;
- release compatibility;
- timing and recovery behavior.

This must not become simplistic volatility grouping. Some changes must remain coordinated because they implement one
product invariant. Do not separate everything into tiny abstractions.

## 10. Product Vocabulary and Platform Vocabulary

A durable boundary should keep product decisions expressed in product language.

Examples of platform vocabulary include HAL handles, vendor enumeration values, socket error codes, RTOS event bits, DMA
callbacks, peripheral register state, transport frame structures, and raw device status values.

Those terms should not casually appear in UI decisions, product state machines, storage schema, business rules,
system-level command semantics, support tooling, or product diagnostics. Translation should occur at a bounded edge.

The chapter must not imply platform details can disappear completely. Embedded systems have real hardware, timing,
memory, and vendor constraints. The boundary's job is to keep those constraints from becoming product authority unless
the product intentionally owns them.

## 11. Authority and State Across Boundaries

A boundary should preserve one clear authority for product state.

Cross-boundary copies, caches, snapshots, projections, and diagnostic views may be useful. They should not silently
become competing truth. If a callback, event consumer, UI cache, persistence record, or driver status mutates product
truth outside the owner, the boundary is not protecting authority.

Use Chapter 7 as a governing law. Do not reteach state ownership.

## 12. Dependency Direction and Runtime Flow

A boundary should make dependency direction explicit.

Product policy should not depend directly on volatile platform mechanisms merely because calls flow that way at runtime.
The future draft should distinguish compile-time dependency, runtime call direction, ownership, control inversion, data
flow, event flow, and authority.

This is not a dependency-inversion tutorial and must not repeat Chapter 9. The chapter should focus on what knowledge
each side must have and which side pays when the other side changes.

## 13. Boundary Contracts and Translation

A boundary contract describes what the other side may rely on.

For Chapter 14, a boundary contract may name:

- product-level commands;
- accepted inputs;
- observable outcomes;
- lifecycle;
- completion semantics;
- failure categories;
- ownership of retries or recovery;
- versioning or compatibility where material.

Translation at the edge should preserve meaning while converting vocabulary, identifiers, error categories, lifecycle,
data representation, temporal semantics, and ownership expectations. Translation is not merely renaming types.

This must not become Chapter 8 repeated. Chapter 8 owns API promises. Chapter 14 owns deciding where a contract should
exist and what knowledge it should contain.

## 14. Cross-Boundary Communication

The future draft should examine direct calls, messages, callbacks, events, queues, shared memory, snapshots, and
asynchronous completion.

No mechanism is automatically architecturally superior. A direct call can preserve a truthful boundary. An event stream
can hide authority. A queue can help isolate timing or become a dumping ground for platform payloads. A callback can
represent necessary asynchronous completion or mutate authoritative state outside the owner.

The relevant question is whether the mechanism preserves authority, contract, dependency direction, and product meaning.

## 15. Boundary Integrity and Back Channels

A nominal boundary fails when bypassed by:

- global state;
- shared mutable structures;
- utility helpers;
- direct HAL calls;
- vendor types;
- temporary callbacks;
- debug-only access;
- duplicated configuration;
- hidden event subscriptions;
- test hooks used by production logic.

The future draft should treat these as evidence that the boundary does not contain the decision. Back channels reveal
the real architecture because they show which path the system actually relies on when the intended contract is
inconvenient.

## 16. Granularity and Boundary Cost

Boundaries can be too broad or too narrow.

Too broad:

- unrelated decisions share one owner;
- change spreads through a god service;
- testing requires the whole subsystem;
- platform and product semantics mix.

Too narrow:

- forwarding interfaces multiply;
- every function becomes a service;
- ownership fragments;
- simple changes cross many small boundaries;
- translation overhead dominates.

Boundaries impose real costs: copies, memory, latency, serialization, queues, synchronization, mapping code, versioning,
error handling, test fixtures, observability, and operational complexity. An in-process module boundary should not
imitate a distributed system without reason.

## 17. What It Means to Survive Change

A boundary survives change when a material change can be absorbed on one side without forcing unrelated decisions to
move or leak.

This does not mean callers never change, contracts never evolve, the boundary predicts every future variant,
implementation replacement is free, or compatibility is permanent. A boundary may need to move when the product model
changes.

Durability means the boundary remains truthful under expected change, not eternal.

## 18. Transition From Part II

Part II ends by showing that laws require current evidence. Chapter 14 begins Part III by showing where those laws become
architecture practice.

Boundaries make the laws operational:

- state ownership needs a place where authority lives;
- API promises need a contract surface that contains the right knowledge;
- dependency decisions need direction and containment;
- timing and completion need explicit meaning at the edge;
- unused flexibility and simplicity need proportionate structure;
- confidence needs evidence that the boundary actually contains the decision.

Do not turn this into a Part II summary. Use the laws as inputs to boundary drawing.

## 19. Boundaries With Chapters 1-13

### Chapters 1-4 - Principal Engineering Foundations

Chapter 14 may use role clarity, constraints, better questions, and ownership as premises. It must not repeat the
Principal Engineer role, decision-making under constraints, inquiry habits, or cross-team closure ownership.

### Chapter 7 - Every State Has One Owner

Chapter 7 owns authoritative state. Chapter 14 uses state authority as one input when drawing boundaries.

### Chapter 8 - Every API Is a Promise

Chapter 8 owns observable API promises and compatibility. Chapter 14 owns deciding where a contract should exist and
what knowledge it should contain.

### Chapter 9 - Every Dependency Is a Decision

Chapter 9 owns dependency commitment and imported assumptions. Chapter 14 owns placing dependencies behind truthful
product boundaries and defining direction.

### Chapter 10 - Time Is a Dependency

Chapter 10 owns temporal semantics. Chapter 14 may require completion and timeout meaning at a boundary, but must not
re-teach clocks, deadlines, ordering, or freshness.

### Chapter 12 - Simplicity Is a Feature

Chapter 12 owns system-level simplicity and direct decision paths. Chapter 14 may use simplicity to assess boundary
shape, but must focus on boundary placement and integrity.

### Chapter 13 - Evidence Before Confidence

Chapter 13 owns confidence and revalidation. Chapter 14 may require evidence that a boundary reduces leakage or Change
Radius, but must not repeat the evidence lifecycle.

## 20. Boundaries With Later Part III Chapters

### Chapter 15 - Managing Change Radius

This is the primary forward-duplication risk. Chapter 14 owns drawing and evaluating a boundary: reasons to change,
authority, vocabulary, dependency direction, translation, integrity, and back channels.

Chapter 15 owns the full Change Radius method.

That method includes mapping Change Radius, propagation paths, planning cross-boundary modifications, sequencing change,
and impact containment.

Chapter 14 may use Change Radius as evidence. It must not teach the full Change Radius method.

### Chapter 16 - Designing for Failure and Recovery

Chapter 14 may require failure categories, completion semantics, and retry ownership at a boundary.

Chapter 16 owns failure and recovery design.

That includes complete failure detection, containment, degradation, retry, recovery, and unknown-outcome design.

### Chapter 17 - Using ADRs and RFCs Well

Chapter 14 may include one chapter-local ADR.

Chapter 17 owns ADR/RFC practice.

That includes artifact choice, authoring, review, lifecycle, and quality.

### Chapter 18 - Reviewing Architecture Before It Hardens

Chapter 14 may state what a boundary decision should make reviewable.

Chapter 18 owns Architecture Review.

### Chapter 19 - Freezing Architecture Without Freezing Learning

Chapter 14 may define a boundary expected to persist.

Chapter 19 owns Architecture Freeze.

That includes freeze, exceptions, and revalidation.

## 21. Boundaries With Later Parts

Part IV should retain detailed product-line architecture, manufacturing boundaries, observability implementation, release
discipline, upgrade systems, and the reference project.

Part V should retain organizational rituals, mentoring, alignment, and Architecture Health Review operation.

Part VI should retain full legacy-boundary discovery, silent-coupling recovery, utility-gravity cleanup, broad
refactoring, Boolean Explosion reduction, and deletion programs.

Chapter 14 may point toward these later practices only where needed to constrain boundary drawing.

## 22. Recommended Embedded-Systems Story

### Working Title

The Radio Driver That Was Everywhere

### System

Use an embedded communications product that begins with one radio or peripheral vendor. The team creates a radio manager
or driver wrapper intended to isolate the hardware.

The wrapper exposes vendor or mechanism details such as vendor channel identifiers, connection-state values, callback
signatures, raw packet types, retry and error codes, socket addresses, RTOS event bits, timing assumptions, and service
tool commands.

Those details spread into UI, product state, persistence, diagnostics, command handling, tests, and network services.
The code has directories and interfaces, so the team believes a boundary exists.

### Trigger

A material change arrives: a second radio family, a transport replacement, a revised control protocol, or a product
variant that preserves user-visible behavior while using a different integration mechanism.

The change reveals that the product depends on the old vendor model everywhere. Product state uses vendor connection
states. UI logic checks raw driver errors. Stored configuration encodes transport details. Tests mock vendor callbacks.
Recovery rules are spread across layers. A callback changes authoritative state outside its owner. Direct platform access
bypasses the manager.

### Inadequate Responses

The team may propose another vendor flag, more manager methods, one universal driver interface, duplicated product logic
per vendor, a generic event bus, status-value renaming, conditional compilation, one platform service, another
abstraction layer, or direct HAL access for exceptional cases.

Show why these responses may preserve the wrong boundary.

### Principal Engineer Intervention

The Principal Engineer recasts the problem from:

> How do we wrap the new driver?

to:

> Which product decision must remain stable, which integration details vary, and where should translation occur?

The intervention should map product capabilities and invariants, identify authoritative state, identify reasons to
change, separate product commands and outcomes from vendor operations, define dependency direction, place translation at
the integration edge, prevent vendor status values and callbacks from crossing, preserve necessary asynchronous
completion, assign retry and recovery ownership, remove back channels, migrate one product path at a time, test the
product contract independently from the adapter, measure the resulting Change Radius, and record the boundary decision
in an ADR.

The result should not be a universal framework. It should be a product-owned boundary with one or more integration
adapters.

## 23. Expected Discussion Arc

1. The system appears layered but the decision boundary is missing.
2. A new integration exposes knowledge that leaked across the product.
3. Structural separation is not the same as architectural separation.
4. Boundaries separate authority, vocabulary, and reasons to change.
5. Product decisions should not be expressed in vendor or platform language.
6. Dependency direction differs from runtime call direction.
7. Translation at the edge preserves meaning and contains volatility.
8. Back channels reveal false boundaries.
9. Boundary granularity and cost must be proportional.
10. Tests and diagnostics should align with the product contract.
11. A durable boundary absorbs expected change without pretending to be eternal.
12. Part III begins by making the laws operational.

Do not mechanically turn this arc into top-level headings. Follow the repository-approved chapter architecture.

## 24. Applicability

Boundary design applies to product policy versus platform integration, application versus driver, state owner versus
projections, UI versus command handling, persistence versus domain model, network protocol versus product semantics,
bootloader versus application, hardware variant adapters, configuration ownership, diagnostics and service tools,
firmware versus host software, synchronous versus asynchronous integration, library and subsystem interfaces, and team
or repository ownership where technically relevant.

Review depth should be proportionate to consequence of leakage, expected rate of change, number of consumers,
cross-team use, product lifetime, hardware variability, recovery difficulty, compatibility obligations, test surface,
and Change Radius.

Not every helper function or header deserves an architecture boundary.

## 25. Limits and Exceptions

The future draft must not claim:

- every dependency needs an interface;
- every module is a boundary;
- more boundaries are better;
- layers guarantee decoupling;
- runtime process separation is required;
- compile-time independence is always possible;
- platform details never cross an edge;
- product code should know nothing about hardware constraints;
- callbacks are always wrong;
- events are always better than calls;
- messages are always more decoupled;
- domain vocabulary solves every integration problem;
- dependency inversion removes runtime coupling;
- a second implementation is required to justify a boundary;
- contracts never change;
- boundaries should be permanent;
- one architecture pattern fits every embedded system;
- boundary code has no performance cost;
- duplicated translation is always acceptable;
- a clean directory structure proves clean architecture.

## 26. Violation Patterns

The future draft should make these violations visible:

- a driver wrapper that leaks vendor types everywhere;
- UI logic interpreting HAL or socket errors;
- product state built from RTOS event bits;
- persistence storing transport-specific identifiers;
- callbacks mutating authoritative state outside the owner;
- a manager interface that only renames vendor calls;
- direct HAL access bypassing the intended service;
- shared mutable configuration across both sides;
- generic events carrying platform payloads;
- tests coupled to vendor callback order;
- retry and recovery ownership split across layers;
- one module serving product policy, transport, persistence, and diagnostics;
- two independent modules joined by global utilities;
- an interface with no protected invariant or reason to change;
- adding one hardware variant requiring edits throughout the product;
- an in-process boundary designed like a distributed system without need.

## 27. Engineering Principle Target

Target principle for the future draft:

> Draw boundaries around product decisions and coherent reasons to change. Keep authority, vocabulary, and dependency
> direction explicit, and translate volatile mechanisms at the edge.

The principle should imply review questions:

1. What product decision belongs inside this boundary?
2. Which reasons for change does it contain?
3. What is authoritative here?
4. What may cross?
5. Which vocabulary crosses?
6. Which side owns completion, retry, and recovery?
7. Which dependencies point in which direction?
8. What platform knowledge leaks?
9. Which back channels bypass the boundary?
10. What change should be absorbed on one side?
11. What cost does the boundary add?
12. What evidence shows the boundary is truthful?

The final manuscript may shorten this list for reader rhythm.

## 28. Architecture Exercise Target

### Working Title

Redraw One Leaky Boundary

Ask the reader to choose one integration boundary and document:

1. product capability;
2. product decision;
3. authoritative state;
4. current modules and runtime components;
5. callers and consumers;
6. current contract;
7. current vocabulary;
8. platform or vendor types crossing;
9. dependency direction;
10. runtime call direction;
11. state and data crossings;
12. callbacks, events, or queues;
13. completion semantics;
14. failure and recovery ownership;
15. direct bypasses;
16. shared mutable data;
17. reasons to change on each side;
18. one realistic future change;
19. current Change Radius;
20. desired product-owned contract;
21. required translation;
22. migration sequence;
23. tests at the boundary;
24. diagnostics at the boundary;
25. cost introduced;
26. ADR location.

The exercise must end with one small, reviewable boundary decision. Do not create a new canonical artifact such as
Boundary Map, Boundary Ledger, Contract Register, Volatility Matrix, Adapter Catalog, or Boundary Score.

## 29. Chapter-Local ADR Brief

### Working Title

Place Radio Integration Behind a Product-Owned Control Boundary

### Context

- One vendor-specific integration model has leaked through the product.
- UI, storage, command handling, tests, and diagnostics depend on vendor details.
- A second integration must preserve user-visible behavior.
- The existing manager is only a structural wrapper.
- Authoritative state and recovery ownership are unclear.

### Decision

- Define a product-level control contract.
- Keep product commands and outcomes in product vocabulary.
- Assign authoritative state to the product owner.
- Isolate vendor operations in adapters.
- Translate identifiers, status, errors, and completion at the edge.
- Preserve necessary asynchronous behavior without exposing vendor callbacks.
- Assign retry and recovery ownership.
- Remove direct platform bypasses.
- Migrate one product path at a time.
- Test product contract separately from adapters.
- Instrument boundary decisions and integration failures.

### Alternatives Considered

- Extend the current vendor-shaped manager.
- Create one universal lowest-common-denominator driver interface.
- Duplicate product logic per vendor.
- Use conditional compilation throughout.
- Introduce a generic event bus.
- Keep direct platform access for exceptional paths.
- Replace the subsystem in one rewrite.
- Postpone boundary work until more variants exist.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits:

- product semantics remain stable;
- vendor knowledge is contained;
- authority becomes explicit;
- tests align with product behavior;
- integration changes have a smaller affected surface;
- diagnostics identify whether failure is product or adapter behavior.

Costs:

- translation code;
- migration effort;
- possible copies and latency;
- temporary coexistence;
- explicit product-specific contract;
- risk of an overly broad product boundary;
- future contract evolution still requires work.

The ADR must make a genuine boundary decision. It must not reduce to "add an interface."

## 30. PEAK Concept Map

### Concepts Inspected

- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `VOCAB-007` - Architecture Health.
- `VOCAB-008` - Silent Coupling.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `METRIC-005` - Architecture Health.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-001` - God Module.
- `ANTIPATTERN-002` - HAL Everywhere.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-004` - Manager Mania.
- `ANTIPATTERN-005` - Callback Hell.
- `ANTIPATTERN-006` - Temporary Solution.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-006` - Architecture Ledger.
- `RITUAL-001` - Architecture Review.
- `RITUAL-004` - Architecture Health Review.
- `FAILURE-001` - Logger That Became a Platform.
- `FAILURE-002` - One Lost Packet.
- `FAILURE-003` - The Successful Prototype.
- `FAILURE-005` - The Release We Should Have Delayed.

### Selected Concepts

- `SMELL-005` - Platform Leakage: material because the recommended story centers on vendor and platform vocabulary
  escaping into product decisions.
- `ANTIPATTERN-002` - HAL Everywhere: material because the boundary fails when low-level integration details shape UI,
  product state, storage, diagnostics, tests, and command semantics.
- `LAW-001` - Every State Has One Owner: material as a governing law because boundary placement must preserve product
  authority and avoid competing truth across callbacks, caches, projections, and driver status.
- `LAW-002` - Every API Is a Promise: material as a governing law because the boundary contract names commands,
  outcomes, lifecycle, completion, failure categories, retries, recovery, and compatibility where material.
- `LAW-007` - Every Dependency Is a Decision: material as a governing law because the chapter teaches containment of
  imported vendor behavior and dependency direction.
- `SMELL-001` - Silent Coupling: material because false boundaries hide dependencies in callbacks, configuration, tests,
  shared state, and diagnostics.
- `SMELL-004` - Hidden State: material because cross-boundary copies, caches, snapshots, event bits, and driver status
  can become unowned product truth.
- `ANTIPATTERN-004` - Manager Mania: material because the story's radio manager appears to isolate hardware while
  coordinating behavior without owning the product decision.
- `ANTIPATTERN-001` - God Module: material as the too-broad boundary failure mode where unrelated decisions gather in
  one platform or product service.
- `VOCAB-001` - Change Radius: material because boundary quality is tested by how far a realistic integration change
  travels.
- `METRIC-001` - Change Radius: material because the exercise asks readers to compare the current and desired affected
  surface.
- `ARTIFACT-001` - ADR: material because the chapter-local decision records a durable boundary placement and its
  consequences.

### Rejected Concepts

- `LAW-003` - Time Is a Dependency: completion semantics matter at a boundary, but Chapter 10 owns temporal semantics.
- `LAW-004` - Simplicity Is a Feature: proportional boundary cost and simple explanations matter, but Chapter 12 owns
  system-level simplicity.
- `LAW-005` - Evidence Before Confidence: evidence can show whether a boundary is truthful, but Chapter 13 owns
  confidence and revalidation.
- `LAW-006` - Unused Flexibility Is Waste: generic universal interfaces may create unused flexibility, but Chapter 11
  owns optionality and retained flexibility.
- `VOCAB-007` and `METRIC-005` - Architecture Health: boundary integrity affects health, but the selected graph should
  not pull Chapter 14 into a health-review chapter.
- `VOCAB-008` - Silent Coupling: related vocabulary exists, but `SMELL-001` carries the selected failure signal more
  directly.
- `METRIC-003` - Discoverability: useful for finding decisions and contracts, but Change Radius and ADR are more central
  to the chapter's exercise and decision.
- `SMELL-006` - Event Explosion: relevant to event-heavy boundaries, but the chapter treats events as one mechanism
  rather than making event growth central.
- `ANTIPATTERN-003` - Global Configuration: relevant as a back channel, but Hidden State and Silent Coupling cover the
  selected boundary failure more directly.
- `ANTIPATTERN-005` - Callback Hell: relevant to asynchronous completion, but Chapter 14 should not become a callback
  ordering chapter.
- `ANTIPATTERN-006` - Temporary Solution: relevant to bypasses, but not central to the boundary placement story.
- `ARTIFACT-002` - RFC: useful for cross-team proposals, but Chapter 17 owns ADR/RFC practice and the chapter-local
  artifact is an ADR.
- `ARTIFACT-006` - Architecture Ledger: useful for large systems, but not necessary for the central boundary decision.
- `RITUAL-001` - Architecture Review: boundary decisions should be reviewable, but Chapter 18 owns the review practice.
- `RITUAL-004` - Architecture Health Review: relevant to long-term upkeep, but later parts own the review operation.
- `FAILURE-001` - Logger That Became a Platform: related to accidental platforms, but the selected story is a radio
  integration boundary rather than a logging utility.
- `FAILURE-002` - One Lost Packet: relevant to protocol failure, but Chapter 16 should own full failure and recovery
  design.
- `FAILURE-003` - The Successful Prototype: relevant to prototype boundaries, but Chapter 13 already uses it for
  evidence transfer.
- `FAILURE-005` - The Release We Should Have Delayed: relevant to release risk, but not to the central boundary
  placement decision.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as architecture boundary, boundary integrity, product boundary, translation edge, volatility boundary,
boundary contract, back channel, reason to change, and adapter boundary remain chapter-local prose unless a later Canon
Review finds a stable reusable gap and the author approves a canon change.

## 31. Exact Proposed PEAK Relationships

Register `CHAPTER-014` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-014
  type: illustrates
  to: SMELL-005

- from: CHAPTER-014
  type: illustrates
  to: ANTIPATTERN-002

- from: CHAPTER-014
  type: references
  to: LAW-001

- from: CHAPTER-014
  type: references
  to: LAW-002

- from: CHAPTER-014
  type: references
  to: LAW-007

- from: CHAPTER-014
  type: references
  to: SMELL-001

- from: CHAPTER-014
  type: references
  to: SMELL-004

- from: CHAPTER-014
  type: references
  to: ANTIPATTERN-004

- from: CHAPTER-014
  type: references
  to: ANTIPATTERN-001

- from: CHAPTER-014
  type: references
  to: VOCAB-001

- from: CHAPTER-014
  type: references
  to: METRIC-001

- from: CHAPTER-014
  type: references
  to: ARTIFACT-001
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 32. Required Reader-Facing Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Part III does not currently have an approved alternate chapter architecture. The standard eight-section structure still
applies, with a playbook emphasis:

- Opening Quote: establish that boundaries are about decisions, not shapes.
- Story: show a radio or peripheral wrapper whose structural boundary leaks platform knowledge everywhere.
- Discussion: teach boundary placement, authority, vocabulary, dependency direction, translation, integrity, and cost.
- Engineering Principle: anchor boundary drawing as a review habit.
- Architecture Exercise: redraw one leaky boundary and end with one reviewable boundary decision.
- Principal's Notebook: three short observations, no explanations.
- ADR: record a scoped radio integration boundary decision.
- Editor's Commentary: explain how Part III begins and how this chapter differs from Part II and later playbooks.

## 33. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A boundary separates decisions, not files.
- Translation belongs where vocabularies meet.
- Back channels reveal the real architecture.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 34. Technical Credibility Requirements

The future draft must treat the following accurately:

- compile-time dependency versus runtime call direction;
- synchronous and asynchronous calls;
- callbacks and completion;
- queues and messages;
- state authority;
- snapshots and caches;
- driver and vendor types;
- HAL, RTOS, and network semantics;
- product-level commands and outcomes;
- error translation;
- retry and recovery ownership;
- version and lifecycle assumptions;
- in-process boundary costs;
- copies, memory, latency, and synchronization;
- incremental migration;
- tests at contract and adapter levels;
- diagnostics at the boundary.

Do not require a specific MCU, RTOS, radio vendor, network stack, message bus, object-oriented language,
dependency-injection framework, code generator, or repository layout.

## 35. Terminology and Precision Guardrails

Use terms precisely:

- boundary: intentional separation of authority, responsibility, and knowledge;
- contract: behavior and information another side may rely on;
- product vocabulary: terms expressing user-visible or product-owned meaning;
- platform vocabulary: terms expressing mechanism, vendor, RTOS, HAL, transport, or driver details;
- translation: preservation of meaning while converting between vocabularies and contracts;
- dependency direction: which side requires knowledge of the other at design or compile time;
- runtime call direction: which side invokes or signals the other during execution;
- authority: the component permitted to decide or mutate product truth;
- back channel: an alternate path that bypasses the intended contract;
- reason to change: a coherent source of change, not merely a file edit;
- boundary integrity: degree to which communication and authority actually follow the intended contract.

The chapter must avoid these misleading statements:

- dependency direction equals call direction;
- an interface removes coupling;
- asynchronous messaging removes dependencies;
- process separation guarantees a boundary;
- vendor status values can be made product-level by renaming;
- all errors should map to one generic status;
- adapters should hide every hardware constraint;
- direct calls are inherently tightly coupled;
- events are inherently loosely coupled;
- a second implementation proves the abstraction;
- unit tests alone prove a boundary;
- smaller Change Radius proves correctness;
- every boundary needs serialization;
- architecture must be independent of physical constraints.

## 36. Failure Modes to Avoid

The later draft must not become:

- a Clean Architecture summary;
- a ports-and-adapters tutorial;
- a SOLID chapter;
- a dependency-injection tutorial;
- a directory-layout guide;
- a layer-count argument;
- an API versioning chapter;
- a dependency-selection chapter;
- a state-ownership chapter;
- a complete Change Radius chapter;
- a failure and recovery chapter;
- an ADR/RFC tutorial;
- an architecture-review chapter;
- a generic microservices argument;
- an anti-HAL essay;
- a framework-building exercise;
- a claim that product logic can ignore hardware reality;
- a heroic rewrite narrative;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 37. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete embedded radio or peripheral boundary failure;
- the Principal Engineer move recasts the work around product decision, stable behavior, varying integration details,
  and translation at the edge;
- no primary law or primary PEAK concept is assigned unless a later author/editor decision changes repository convention;
- boundary, contract, product vocabulary, platform vocabulary, translation, dependency direction, runtime call direction,
  authority, back channel, reason to change, and boundary integrity are used precisely;
- module, interface, layer, process, and boundary are distinguished;
- product vocabulary is protected from vendor and platform vocabulary without pretending hardware constraints disappear;
- dependency direction is distinguished from runtime flow;
- callbacks, events, queues, messages, direct calls, shared memory, snapshots, and asynchronous completion are treated as
  mechanisms, not automatic architecture answers;
- boundary cost and granularity are treated proportionately;
- Chapter 15's Change Radius method remains out of scope;
- Chapters 16 through 19 remain out of scope except for boundary handoffs;
- Platform Leakage, HAL Everywhere, state ownership, API promises, dependency decisions, Silent Coupling, Hidden State,
  Manager Mania, God Module, Change Radius, and ADR are materially present if their relationships remain registered;
- the exercise ends in one small, reviewable boundary decision;
- the ADR makes a genuine scoped decision and acknowledges benefits and costs;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 38. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach one
idea without drifting into a Clean Architecture summary, layer-count argument, framework tutorial, or generic boundary
essay.

Canon Review should verify that Chapter 14 remains a practice chapter with no forced primary concept, materially uses
the registered supporting concepts, does not imply a new PEAK artifact or vocabulary term, and preserves boundaries with
Chapters 7, 8, 9, 12, 13, and later Part III chapters.

Technical Review should focus on dependency direction versus runtime call direction, synchronous and asynchronous
communication, callbacks and completion, state authority, snapshots and caches, driver and vendor types, HAL/RTOS/network
semantics, error translation, retry and recovery ownership, boundary cost, incremental migration, tests, and diagnostics.

Freeze Review should confirm that Chapter 14 remains the first Part III practice chapter, keeps the manuscript
architecture intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and
leaves the reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
radio, peripheral, transport, product variant, adapter shape, migration sequence, and final notebook wording while
preserving the boundary thesis, story shape, PEAK map, and chapter boundaries.

## 39. Final Scope Statement

Chapter 14 should define architecture boundaries as intentional separations of authority, responsibility, and knowledge.
It should show an embedded radio or peripheral integration whose wrapper leaked vendor and platform vocabulary through
the product, then guide the reader toward product-owned contracts, explicit dependency direction, edge translation,
authority-preserving communication, proportional boundary cost, and a scoped ADR that places integration behind a
durable product boundary without inventing a universal framework.
