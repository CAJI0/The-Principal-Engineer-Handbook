# CHAPTER-008 Canonical Brief: Every API Is a Promise

## Metadata

- Stable ID: `CHAPTER-008`.
- Title: `Every API Is a Promise`.
- Part: Part II - The Laws.
- Chapter number: 8.
- Expected manuscript path: `book/02-the-laws/08-every-api-is-a-promise.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-008-every-api-is-a-promise.md`.
- Branch: `chapter8`.
- Canonical predecessor: `CHAPTER-007` - Every State Has One Owner.
- Part position: second chapter of Part II - The Laws.
- Baseline `origin/main`: `0776ab64b48d4e36a9b952964ab5739b9eaf55d2`.
- Reader-facing draft created: no.
- Primary law: `LAW-002` - Every API Is a Promise.
- Lifecycle status at brief-registration time: draft preparation.
- Next lifecycle stage: Author Draft after author approval.

## Repository-Grounded Findings

- `origin/main` resolves to `0776ab64b48d4e36a9b952964ab5739b9eaf55d2`.
- That baseline is the Chapter 7 merge commit, `Chapter 7: Every State Has One Owner (#9)`.
- `CHAPTER-001` through `CHAPTER-007` are registered as `canonical` in `knowledge/index.yaml`.
- Chapter 7 exists at `book/02-the-laws/07-every-state-has-one-owner.md`.
- `editor/EDITOR_LOG.md` records Chapter 7 Editorial, Canon, Technical, and Freeze Review entries in order.
- The table of contents places `Every API Is a Promise` second in Part II, after `Every State Has One Owner`.
- `LAW-002` exists and is named `Every API Is a Promise`.
- `LAW-002` defines an API as a commitment about behavior, meaning, errors, timing, and ownership.
- `LAW-002` already relates to `ARTIFACT-001` in `knowledge/index.yaml`.
- `SMELL-001` - Silent Coupling, `METRIC-004` - API Stability, `METRIC-003` - Discoverability, `ARTIFACT-001` - ADR,
  and `VOCAB-001` - Change Radius all exist exactly once.
- `CHAPTER-008` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 8 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter8` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 1. Canonical Purpose

Prepare Chapter 8 to teach the second Part II law: every API is a promise about observable behavior across a boundary.

The chapter should move the reader from thinking about APIs as signatures, headers, endpoints, packet layouts, or
function shapes toward a reviewable architecture question: what may consumers rely on, and what will it cost to change
that expectation?

The chapter must not create a reader-facing draft during this task. It must constrain the later Author Draft.

## 2. Exact Law Statement

`LAW-002` states:

> Every API promises behavior that other code and people will trust.

Chapter 8 should preserve that law while making the promise concrete enough for architecture review.

## 3. Central Thesis

Every API creates expectations about valid inputs, outputs, errors, timing, ordering, side effects, compatibility,
ownership, and failure behavior. Once consumers depend on those expectations, changing them has a cost even when the
type signature stays the same.

Approved supporting formulation for the future draft:

> Consumers depend on behavior, not declarations.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 4. Reader Transformation

Before the chapter, the reader may think:

1. an API is mainly a function signature, header, endpoint, message shape, or public surface;
2. internal APIs are cheap to change because they are not public;
3. undocumented behavior is not part of the contract;
4. compatibility means the compiler still accepts the call;
5. version numbers, optional fields, or adapters make evolution safe by themselves.

By the end of the chapter, the reader should be able to:

1. identify when observable behavior has become a promise;
2. separate implementation detail, intentional contract, accidental contract, unsupported behavior, and undefined
   behavior;
3. name the consumers who rely on the promise;
4. describe input, output, error, timing, ordering, context, ownership, lifetime, side-effect, persistence, and recovery
   semantics;
5. assess compatibility across source, binary, wire, behavioral, data, and operational dimensions where relevant;
6. plan API evolution with migration evidence, compatibility cost, and explicit incompatible change.

## 5. Semantic Definition of an API Promise

An API is any boundary where another component, tool, team, product surface, test, script, or human workflow can observe
behavior and build expectations on it.

The boundary may be formal:

- an exported C function;
- a header file;
- a driver interface;
- a HAL or BSP boundary;
- an RTOS service call;
- a callback registration;
- a command protocol;
- an event interface;
- a network message;
- a persisted format;
- a bootloader/application handoff;
- a CLI command;
- a manufacturing or service-tool command.

The boundary may also be informal when repeated observable behavior becomes part of how consumers work:

- callback timing;
- task-context assumptions;
- error-code meanings;
- shared data-structure layout;
- debug hooks relied on by field tooling;
- filesystem or NVS conventions;
- undocumented ordering;
- retry behavior learned from experience.

The chapter should not claim that every private helper is automatically an architecture-level API. The threshold is
consumer reliance across a meaningful boundary.

## 6. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 8 covers:

- APIs as observable boundary promises;
- signature versus behavior;
- intentional and accidental contracts;
- internal and external API compatibility cost;
- accepted inputs, preconditions, outputs, errors, timing, ordering, side effects, ownership, lifetime, execution
  context, and failure behavior;
- source, binary, wire, behavioral, data, and operational compatibility where useful;
- deprecation, migration, adapters, and compatibility layers;
- explicit unsupported and intentionally unspecified behavior;
- tests and documentation as evidence of the promise;
- preserving implementation freedom by making the promise precise.

### Explicitly Out of Scope

Do not turn Chapter 8 into:

- a REST or public web API chapter;
- a C ABI handbook;
- a formal methods taxonomy;
- a semantic-versioning tutorial;
- a network protocol design chapter;
- a dependency-selection or dependency-governance chapter;
- a deep time, deadline, freshness, or clock chapter;
- a broad simplicity chapter;
- a testing-methodology chapter;
- a release-management or field-upgrade playbook;
- an observability architecture chapter;
- a Part III boundary-design procedure.

Those topics may appear only where they clarify API promises.

## 7. Contract Dimensions

The future draft should show that an API promise may include:

- accepted inputs and invalid inputs;
- preconditions;
- output meaning;
- error semantics;
- blocking behavior;
- latency expectations;
- callback context;
- ownership and lifetime;
- thread, task, or ISR safety;
- ordering;
- repeated-call behavior;
- retry behavior;
- side effects;
- state transitions;
- persistence effects;
- version negotiation;
- fallback behavior;
- diagnostics and observability.

The chapter should use enough dimensions to make the law reviewable. It must not become an exhaustive taxonomy.

## 8. Intended and Accidental Contracts

The brief must distinguish:

- intentional contract: behavior the producer deliberately promises;
- accidental contract: repeated observable behavior consumers rely on even though the producer did not intend to promise
  it;
- implementation detail: behavior consumers are not meant to observe or rely on;
- undefined behavior: behavior outside the API obligations;
- unsupported behavior: behavior the producer has explicitly declined to support;
- deprecated behavior: behavior still available during migration but scheduled for removal or replacement.

"We never documented it" does not automatically remove compatibility cost. If consumers reasonably learned to depend on
behavior through tests, examples, field tooling, manufacturing scripts, or repeated releases, removing that behavior may
still require migration.

## 9. Compatibility Model

Chapter 8 should distinguish compatibility dimensions only where they matter to the story:

- source compatibility: existing source still compiles or builds;
- binary compatibility: existing binaries or objects still link and run;
- wire compatibility: messages, packets, commands, or events still work together;
- behavioral compatibility: meaning, errors, ordering, timing, and side effects remain within the promise consumers
  rely on;
- data compatibility: persisted formats and stored values remain readable and meaningful;
- operational compatibility: deployment, rollback, diagnostics, manufacturing, service, and field workflows keep working.

The central point is that compatibility is multidimensional. A signature can stay unchanged while the promise changes.

## 10. Failure and Error Semantics

Errors are part of the API promise.

The chapter should consider:

- timeout versus immediate failure;
- partial success;
- retry behavior;
- duplicate requests;
- stale data;
- unavailable dependencies;
- invalid state;
- recovery expectations;
- error reporting and diagnostics.

The draft may name timing and timeout behavior as contract dimensions, but it must leave deep time semantics for
`LAW-003` - Time Is a Dependency.

## 11. Evolution and Migration

Chapter 8 should explain that:

- version numbers do not create compatibility by themselves;
- additive change is not always safe;
- optional fields can become required in practice;
- silent semantic change is often worse than explicit incompatibility;
- adapters and compatibility layers have maintenance cost;
- deprecation requires migration evidence and an exit plan;
- compatibility decisions should be recorded where future maintainers can find them.

The draft should treat evolution as a deliberate architecture choice, not as a formatting rule for version strings.

## 12. Boundaries With Chapters 1-7

### Chapter 1 - What Is a Principal Engineer?

Chapter 1 frames architecture as decision-making and future system cost. Chapter 8 applies that frame to API promises.
It must not repeat the general Principal Engineer role definition.

### Chapter 2 - Decision-Making Under Constraints

Chapter 2 teaches constrained commitments. Chapter 8 may show that API compatibility is a commitment with cost, but it
must not repeat the full constraint, consequence, uncertainty, or reversibility framework.

### Chapter 3 - Asking Better Engineering Questions

Chapter 3 teaches inquiry that reveals hidden assumptions and stale state. Chapter 8 may use questions to uncover API
promises, but it must not repeat Chapter 3's investigation arc.

### Chapter 4 - Ownership Beyond Code

Chapter 4 concerns responsibility for durable closure across boundaries. Chapter 8 concerns observable behavior across
technical and workflow boundaries. It may name API-promise ownership, but it must not become an outcome-ownership
chapter.

### Chapter 5 - Technical Judgment and Evidence

Chapter 5 owns evidence quality and confidence calibration. Chapter 8 may require tests, examples, or telemetry as
evidence that a promise is preserved, but it must not reteach evidence-quality dimensions.

### Chapter 6 - Leaving Systems Better Than You Found Them

Chapter 6 teaches stewardship and reducing future friction. Chapter 8 may show that clarifying an API leaves future
change safer, but it must not become a broad stewardship chapter.

### Chapter 7 - Every State Has One Owner

Chapter 7 defines who owns state and transitions.

Chapter 8 defines what consumers may rely on when crossing the owner's boundary.

The future draft may show that state-owner commands form an API, but it must not retell the state-ownership argument.

## 13. Boundaries With Later Part II Laws

- Chapter 9 - `Every Dependency Is a Decision`: Chapter 8 may explain what a chosen dependency promises, but dependency
  selection, direction, replacement cost, and governance belong later.
- Chapter 10 - `Time Is a Dependency`: Chapter 8 may name timing, ordering, callback context, and timeouts as API
  contract dimensions, but deep clock, freshness, ordering, deadline, and temporal-assumption analysis belong later.
- Chapter 11 - `Unused Flexibility Is Waste`: Chapter 8 may reject speculative API extension points, but the broader cost
  of unused options belongs later.
- Chapter 12 - `Simplicity Is a Feature`: Chapter 8 may prefer precise contracts, but simplicity as a system property
  belongs later.
- Chapter 13 - `Evidence Before Confidence`: Chapter 8 may require compatibility evidence, but the full evidence law
  belongs later.

## 14. Boundaries With Later Parts

Later parts should retain detailed boundary-design playbooks, ADR and RFC practice, review rituals, architecture freeze
methods, product configuration, manufacturing workflows, release architecture, field telemetry, upgrade orchestration,
legacy migration, and organizational operating models.

Chapter 8 may mention these areas only to show where API promises appear.

## 15. Recommended Embedded-Systems Story

### Working Title

The Setter That Became a Contract

### System

Use a firmware radio service API called by several consumers:

```c
status_t radio_set_channel(uint8_t channel);
```

The original implementation appears to promise only a setter. Over time, consumers rely on more behavior:

1. the call returns only after the hardware has applied the channel;
2. the call is safe from any task context;
3. invalid channels leave the previous channel unchanged;
4. callbacks are delivered before return;
5. repeated calls with the same channel are harmless;
6. error codes distinguish invalid input from unavailable radio hardware;
7. service tooling assumes the numeric channel maps directly to the device;
8. a persisted value restores the channel after reset.

### Incident Shape

A new implementation keeps the same signature but queues hardware work asynchronously. The immediate return now means
"request accepted," not "channel applied."

The change creates failures:

- UI reports the new channel before hardware applies it;
- retry logic duplicates operations;
- reset restores a value whose ownership is unclear;
- callers block or call from contexts the new implementation cannot support;
- error handling treats a temporary unavailable-radio failure as invalid input;
- integration behavior changes even though module-level tests still pass.

### Tempting But Inadequate Response

The team initially proposes local fixes:

- update one caller's delay;
- add a version number without defining behavior;
- add an optional callback without specifying ordering;
- document that callers "should wait";
- keep the old name because the signature still compiles;
- ask service tooling to retry more often.

Those fixes treat symptoms. They do not name the promise.

### Principal Engineer Intervention

The Principal Engineer recasts the issue from API shape to API contract.

The corrective model:

- enumerate the actual observable contract of the old API;
- distinguish request acceptance from operation completion;
- define completion events or callbacks, including context and ordering;
- define ownership and lifetime for inputs, internal state, callbacks, and persisted values;
- define error meanings, retry behavior, and repeated-call behavior;
- define which behavior is guaranteed, unsupported, deprecated, or intentionally unspecified;
- provide a compatibility adapter or migration window where needed;
- record the decision in an ADR and update tests to encode the promise.

The point is not that asynchronous APIs are bad. The point is that an unchanged signature can hide an incompatible
promise.

## 16. Expected Discussion Arc

1. **An API begins where behavior becomes observable.**
   A boundary becomes an API when consumers can build expectations on it.
2. **Consumers depend on behavior, not declarations.**
   Types and names are only part of the promise.
3. **Undocumented behavior can still become a contract.**
   Repeated observable behavior can create compatibility cost.
4. **Errors and failure modes are part of the API.**
   Retry, rejection, partial success, and diagnostics shape consumer behavior.
5. **Timing, ordering, context, ownership, and lifetime are observable.**
   Consumers often rely on these dimensions before anyone names them.
6. **Internal APIs also accumulate cost.**
   The cost depends on consumers, release independence, coupling, tests, rollback, and replacement effort.
7. **Compatibility is multidimensional.**
   Source compatibility does not guarantee behavioral, wire, data, or operational compatibility.
8. **Evolution requires explicit choices.**
   Versioning, adapters, deprecation, and migration require evidence and an exit plan.
9. **Tests and documentation reveal the promise.**
   They help make the promise durable, but they do not create it alone.
10. **Precise promises protect implementation freedom.**
    A clear contract lets implementation change safely inside the boundary.

These are intellectual progression points, not mandatory top-level manuscript headings.

## 17. Law Applicability

The law applies across embedded-system boundaries, including:

- C functions and header files;
- module interfaces;
- driver APIs;
- HAL and BSP boundaries;
- RTOS services;
- callbacks;
- event interfaces;
- command protocols;
- network messages;
- persisted formats;
- bootloader/application contracts;
- manufacturing and service tooling;
- debug hooks that field workflows rely on.

The law also applies to internal APIs when consumers rely on their behavior across meaningful boundaries.

## 18. Law Limits and Exceptions

Not every helper function needs a formal compatibility policy.

The law becomes architecturally important when the boundary has one or more of these traits:

- multiple consumers;
- release independence;
- ownership boundaries;
- deployment or rollback constraints;
- long-lived tests, scripts, tools, or field procedures;
- difficult replacement cost;
- safety, recovery, manufacturing, or customer-visible consequences;
- behavior that is hard to rediscover from code alone.

Local implementation details may remain intentionally unspecified if consumers cannot reasonably rely on them and the
boundary keeps that lack of promise clear.

## 19. Violation Patterns

The future draft should be able to show these common violations:

- keeping a signature stable while changing completion semantics;
- changing error meanings without consumer migration;
- treating undocumented behavior as free to remove;
- calling an internal API "private" while many teams, tests, or tools depend on it;
- adding optional fields that become required in practice;
- relying on callback ordering without naming it;
- changing persistence or reset behavior behind the same interface;
- hiding incompatibility behind a version number;
- creating adapters without owning their retirement.

## 20. Engineering Principle Target

Target principle for the future draft:

> Treat every observable boundary as a contract. Specify what consumers may rely on, preserve those promises
> deliberately, and make incompatible change explicit rather than hiding it behind an unchanged interface.

The principle should imply review questions:

1. Who are the consumers?
2. What behavior can they observe?
3. What assumptions do they rely on?
4. Which behaviors are guaranteed?
5. Which behaviors are intentionally unspecified?
6. What are the error and retry semantics?
7. What owns memory and lifetime?
8. What execution context applies?
9. Which compatibility dimensions matter?
10. How will consumers migrate?

## 21. Architecture Exercise Target

### Working Title

Write the Promise Behind One API

Ask the reader to choose one real API and document:

1. producer;
2. consumers;
3. purpose;
4. accepted inputs;
5. preconditions;
6. outputs;
7. errors;
8. side effects;
9. ownership and lifetime;
10. execution context;
11. blocking or asynchronous behavior;
12. ordering;
13. repeated-call behavior;
14. retry semantics;
15. persistence effects;
16. compatibility dimensions;
17. intentionally unspecified behavior;
18. accidental behavior consumers may rely on;
19. tests that encode the promise;
20. migration strategy for one plausible incompatible change;
21. ADR or existing artifact where the decision belongs.

The exercise must not create a new canonical PEAK artifact. It should use existing records such as ADRs, RFCs, tests,
and Event Catalog entries where appropriate.

## 22. Chapter-Local ADR Brief

### Working Title

Separate Channel-Change Acceptance from Completion

### Context

- The existing `radio_set_channel()` signature hides synchronous assumptions.
- Several consumers rely on the old call returning after hardware has applied the channel.
- The implementation must move to queued hardware operations.
- Changing the implementation without changing the contract creates race conditions, false UI state, and retry bugs.
- Service tooling and tests rely on old error and completion behavior.

### Decision

- Expose an intent-level channel-change request.
- Distinguish accepted, rejected, and completed states.
- Define callback or event context and ordering.
- Define retry and repeated-call semantics.
- Define persistence responsibility.
- Provide a compatibility adapter and migration window for old consumers.
- Remove old behavior only after consumer migration evidence exists.

### Alternatives Considered

- Preserve blocking semantics indefinitely.
- Change implementation silently behind the old signature.
- Add only a timeout parameter.
- Create a second API without migration policy.
- Expose hardware state directly.

### Consequences

Benefits:

- consumers can distinguish request acceptance from hardware completion;
- callback ordering and context become reviewable;
- retries and duplicate requests can be tested;
- compatibility cost is visible before migration;
- implementation can become asynchronous without pretending the old promise survived.

Costs:

- old consumers need migration work;
- compatibility adapters must be maintained and retired deliberately;
- tests must cover both accepted and completed behavior;
- documentation and tooling must update together;
- the API owner must decide which behavior remains guaranteed.

The ADR is story-local and reader-facing. It must not become a repository-level ADR or a full tutorial on ADR mechanics.

## 23. PEAK Concept Map

### Concepts Inspected

- `LAW-002` - Every API Is a Promise.
- `SMELL-001` - Silent Coupling.
- `METRIC-004` - API Stability.
- `ARTIFACT-001` - ADR.
- `METRIC-003` - Discoverability.
- `VOCAB-001` - Change Radius.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-005` - Event Catalog.
- `RITUAL-001` - Architecture Review.
- `FAILURE-002` - One Lost Packet.
- `LAW-001` - Every State Has One Owner.
- `LAW-003` - Time Is a Dependency.
- `ANTIPATTERN-005` - Callback Hell.
- `ANTIPATTERN-002` - HAL Everywhere.

### Selected Concepts

- `LAW-002` - Every API Is a Promise: the chapter directly illustrates this law as the second law of Part II.
- `SMELL-001` - Silent Coupling: material because accidental API promises are hidden behavioral dependencies not
  represented as explicit contracts.
- `METRIC-004` - API Stability: material because the chapter teaches preservation of behavior dependents trust.
- `ARTIFACT-001` - ADR: material because API compatibility, migration, and incompatible changes can be architectural
  decisions with future cost.
- `METRIC-003` - Discoverability: material because engineers must be able to find the promise, consumers, errors,
  compatibility rules, and migration path.
- `VOCAB-001` - Change Radius: material because API changes spread review, testing, and migration cost across consumers.

### Rejected Concepts

- `ARTIFACT-002` - RFC: relevant for future cross-boundary review, but the chapter should not teach RFC practice or
  require an RFC relationship at brief registration.
- `ARTIFACT-005` - Event Catalog: useful when events carry the API, but the selected story can mention events without
  making Event Catalog a required supporting concept.
- `RITUAL-001` - Architecture Review: relevant to API decisions, but review mechanics belong later.
- `FAILURE-002` - One Lost Packet: relevant to protocol failures, but this chapter should not become a packet-ordering
  or time-dependency chapter.
- `LAW-001` - Every State Has One Owner: Chapter 8 depends on Chapter 7's boundary clarity but must not retell state
  ownership.
- `LAW-003` - Time Is a Dependency: timing is a contract dimension here, but deep time semantics belong later.
- `ANTIPATTERN-005` - Callback Hell: callback context and ordering are relevant, but the chapter should not become a
  callback-control-flow chapter.
- `ANTIPATTERN-002` - HAL Everywhere: HAL boundaries are in scope, but the selected story does not primarily teach the
  HAL Everywhere anti-pattern.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as API promise, behavioral contract, accidental contract, compatibility surface, and migration contract remain
chapter-local prose unless a later Canon Review finds a stable reusable gap.

## 24. Exact Proposed PEAK Relationships

Register `CHAPTER-008` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-008
  type: illustrates
  to: LAW-002

- from: CHAPTER-008
  type: illustrates
  to: SMELL-001

- from: CHAPTER-008
  type: references
  to: METRIC-004

- from: CHAPTER-008
  type: references
  to: ARTIFACT-001

- from: CHAPTER-008
  type: references
  to: METRIC-003

- from: CHAPTER-008
  type: references
  to: VOCAB-001
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 25. Required Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

The `Principal's Notebook` must contain exactly three short observations and no explanations.

## 26. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- Signatures are not promises.
- Errors are part of the API.
- Compatibility is behavior.

These are semantic targets, not mandatory final wording.

## 27. Evidence and Technical Credibility Requirements

The future draft must be credible for embedded systems. It should treat the following correctly:

- C function and header boundaries;
- driver, HAL, BSP, and RTOS APIs;
- callback context and ordering;
- task versus ISR expectations;
- blocking versus asynchronous behavior;
- invalid input and error semantics;
- retry and repeated-call behavior;
- ownership and lifetime;
- persisted formats and reset behavior;
- bootloader/application compatibility;
- manufacturing, service, and debug tooling;
- compatibility adapters and migration windows;
- tests that encode the promise.

The story should remain architecture-neutral unless a small illustrative detail is necessary. Do not require a specific
RTOS, MCU, radio component, cloud platform, database, protocol, or framework.

## 28. Terminology and Precision Guardrails

The API promise is the set of observable behaviors consumers may rely on.

The API promise may include:

- shape;
- meaning;
- accepted inputs;
- outputs;
- errors;
- timing;
- ordering;
- side effects;
- ownership;
- lifetime;
- execution context;
- persistence;
- compatibility and migration behavior.

The API is not automatically:

- only the function signature;
- only the header file;
- only a public web endpoint;
- only documented behavior;
- only external to the organization;
- free to change because it is internal;
- compatible because the compiler accepts it;
- compatible because a version number changed;
- safe because an adapter exists.

The chapter must avoid these misleading statements:

- "If it compiles, it is compatible."
- "Internal APIs are free to change."
- "Undocumented behavior has no cost."
- "Adding fields is always backward compatible."
- "A version number is a migration plan."
- "A wrapper eliminates compatibility cost."
- "Errors are implementation details."
- "Callbacks are only control flow, not contract."
- "Consumers should have known better."
- "All implementation behavior must be promised forever."

The law is satisfied when the boundary makes clear what consumers may rely on, what is intentionally unspecified, and how
incompatible change will be made explicit.

## 29. Failure Modes to Avoid

The later draft must not become:

- a REST API essay;
- a public API branding chapter;
- a function-signature checklist with no behavioral semantics;
- a C ABI tutorial;
- a semantic-versioning tutorial;
- a formal specification chapter;
- a network-protocol chapter;
- a retelling of Chapter 7 state ownership;
- a dependency-selection chapter;
- a timeouts and clocks chapter;
- a testing-methodology chapter;
- a new PEAK artifact proposal;
- a shallow ADR that restates the principle without deciding anything;
- reader-facing draft prose inside the canonical brief.

## 30. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete unchanged-signature, changed-promise failure;
- the Principal Engineer move recasts API shape as observable contract;
- the law is explained beyond the slogan;
- accepted inputs, outputs, errors, timing, ordering, context, ownership, lifetime, side effects, persistence, and
  compatibility are treated where relevant;
- accidental contracts and unsupported behavior are distinguished;
- internal API cost is addressed without claiming every helper is permanent;
- evolution and migration are concrete;
- the exercise can be applied to a real API;
- the ADR makes a genuine decision and acknowledges benefits and costs;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally;
- boundaries with Chapters 1-7, later Part II laws, and later parts are respected;
- claims are technically credible and reviewable.

## 31. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach one
idea without drifting into a programming-language, web API, or versioning tutorial.

Canon Review should verify that the chapter illustrates `LAW-002`, materially uses the registered supporting concepts,
does not imply a new PEAK artifact or vocabulary term, and preserves the boundary with Chapter 7 and later Part II laws.

Technical Review should focus on compatibility dimensions, asynchronous versus blocking behavior, callback context, task
and ISR assumptions, error and retry semantics, ownership and lifetime, persistence effects, and migration feasibility.

Freeze Review should confirm that Chapter 8 truly continues Part II, keeps the manuscript architecture intact, uses
exactly three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the reader-facing
manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
API name, radio details, callback mechanism, compatibility strategy, and final notebook wording while preserving the
API-promise thesis, story shape, PEAK map, and chapter boundaries.

## Final Scope Statement

Chapter 8 should define APIs as observable promises across boundaries. It should show an embedded firmware interface
whose unchanged signature hides an incompatible behavioral change, then guide the reader toward explicit inputs, outputs,
errors, timing, ordering, context, ownership, lifetime, compatibility, migration, tests, and an ADR that make the promise
discoverable without turning the chapter into a web API, ABI, protocol, or versioning tutorial.
