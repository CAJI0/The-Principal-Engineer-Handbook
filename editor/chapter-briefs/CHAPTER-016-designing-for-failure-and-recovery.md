# CHAPTER-016 Canonical Brief: Designing for Failure and Recovery

## 1. Metadata

- Stable ID: `CHAPTER-016`.
- Title: `Designing for Failure and Recovery`.
- Part: Part III - Architecture Playbook.
- Chapter number: 16.
- Expected manuscript path: `book/03-architecture-playbook/16-designing-for-failure-and-recovery.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-016-designing-for-failure-and-recovery.md`.
- Branch: `chapter16`.
- Verified baseline `origin/main`: `e1160e0ee78f87424983b94e80eb29e5ecd4058d`.
- Baseline evidence: PR #17 squash commit, `Chapter 15: Managing Change Radius (#17)`.
- Chapter 15 feature Freeze commit checked for tree equivalence:
  `c90da497d5c8cc2ea4222222a1df049310650422`.
- Canonical predecessor: `CHAPTER-015` - Managing Change Radius.
- Part position: third chapter of Part III - Architecture Playbook.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 16 is a Part III practice chapter, and current repository convention does not require a
  primary PEAK concept for practice chapters.
- Central PEAK anchor: `FAILURE-002` - One Lost Packet.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `e1160e0ee78f87424983b94e80eb29e5ecd4058d`.
- That baseline is the PR #17 squash commit, `Chapter 15: Managing Change Radius (#17)`.
- The Chapter 15 feature-branch Freeze commit `c90da497d5c8cc2ea4222222a1df049310650422` remains tree-equivalent for the
  checked Chapter 15 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-015` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-015` is the second Part III chapter and is canonical.
- `editor/EDITOR_LOG.md` records Chapter 15 Editorial, Canon, Technical, and Freeze Review entries in order.
- The table of contents places `Designing for Failure and Recovery` immediately after Chapter 15 in Part III.
- `FAILURE-002` exists exactly once as `One Lost Packet`.
- `LAW-001`, `LAW-002`, `LAW-003`, `LAW-005`, and `LAW-007` exist and are available as supporting laws.
- `SMELL-001`, `SMELL-004`, `SMELL-006`, `ANTIPATTERN-005`, `ANTIPATTERN-006`, `ARTIFACT-001`, `ARTIFACT-003`, and
  `ARTIFACT-005` exist and are available as supporting concepts.
- `book/03-architecture-playbook/README.md` remains a placeholder and should not be expanded in this phase.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-016` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 16 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter16` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part III Role

Chapter 16 is the third Part III practice chapter. Chapter 14 taught where authority, responsibility, and knowledge
belong. Chapter 15 taught how to map affected surface when a decision changes. Chapter 16 teaches how to design the
system behavior that follows consequential failure.

The chapter should move from affected-surface planning into runtime and lifecycle resilience. It should show that
Principal Engineers do not ask only whether failure can happen. They ask what the system can still know, what state
remains safe, who is allowed to act, what is retried, what is contained, what is reported, and how the system returns to
a known state.

Chapter 16 must remain a practice chapter. It should not become an incident-response chapter, an observability platform
chapter, or a reliability taxonomy.

## 4. Canonical Purpose

Prepare Chapter 16 to teach a Principal Engineer how to design for failure and recovery before the failure path is only
an emergency patch.

The chapter should move the reader from asking:

> What happens if this fails?

to asking:

> Which states can the system enter, which outcomes can it know, which actions are safe to repeat, and which path brings
> the system back to a known state?

The chapter must teach both failure semantics and recovery design. Detecting failure without designing the recovery path
creates alarms. Recovering without clear semantics creates hidden state and duplicate work.

## 5. Primary-Concept Resolution

Chapter 16 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records, and Chapter 14 and
Chapter 15 established that Part III practice chapters may be carried by a relationship set rather than by one primary
concept. Chapter 16 therefore records an explicit no-primary decision.

`FAILURE-002` - One Lost Packet is the central failure-story anchor. It supplies the story shape: a dropped or reordered
message exposes hidden assumptions about ordering, retry behavior, and recovery ownership. It is not promoted into a
primary concept.

Do not create a new PEAK law, vocabulary term, metric, artifact, ritual, smell, anti-pattern, or failure story for
failure and recovery design. Terms used in this chapter remain chapter-local unless a later Canon Review identifies an
approved repository-wide gap.

## 6. Central Thesis

A system is designed for failure when each consequential operation has explicit outcomes, bounded retry behavior,
observable uncertainty, containment, and a deliberate path back to a known state.

Approved supporting formulation for the future draft:

> Design the state after failure as carefully as the happy path.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. failure handling means adding retries;
2. a timeout means an operation failed;
3. success and failure are the only meaningful outcomes;
4. rollback is the same as recovery;
5. logging an error is enough observability;
6. every caller can decide its own fallback;
7. degraded behavior is always better than stopping;
8. restart clears uncertainty.

By the end of the chapter, the reader should be able to:

1. define operation outcomes before implementing the failure path;
2. distinguish rejection, failure, timeout, late completion, partial completion, duplicate completion, and unknown
   outcome;
3. decide which state authority owns recovery decisions;
4. design retry behavior with repeat safety and duplicate handling in mind;
5. contain failure spread across boundaries and dependencies;
6. represent uncertainty visibly enough for humans and systems to act;
7. restore or move toward a known state after reset, restart, power loss, or network loss;
8. record residual recovery risk in existing artifacts.

## 8. Semantic Definition

For this chapter, designing for failure and recovery means defining the system's behavior when an operation does not
complete on the happy path and then making that behavior observable, bounded, testable, and owned.

The chapter should treat failure as an architectural state question, not as an exception branch. Important questions are:

- what was requested;
- whether execution started;
- whether side effects may have occurred;
- whether completion can arrive late;
- whether retry may duplicate work;
- which state remains authoritative;
- which dependency is allowed to keep working;
- which behavior is safe to offer while recovery is incomplete;
- which evidence proves recovery succeeded;
- when a human or later process must take over.

## 9. In-Scope and Out-of-Scope

### In Scope

Chapter 16 covers:

- operation outcomes and unknown outcome;
- detection, containment, retry, partial completion, duplicate completion, late completion, recovery, and escalation;
- state ownership during recovery;
- repeat safety and duplicate suppression;
- recovery after reset, restart, power loss, network loss, dependency failure, and callback loss;
- explicit failure categories at architecture boundaries;
- degradation and containment where product meaning stays honest;
- event and callback behavior when completion is asynchronous;
- observability needed to diagnose and prove recovery;
- tests that exercise failure timing, interruption, replay, and restart;
- an embedded communication or update story anchored in one lost acknowledgment.

### Explicitly Out of Scope

Do not turn Chapter 16 into:

- Chapter 10 repeated;
- Chapter 14 boundary placement repeated;
- Chapter 15 Change Radius repeated;
- Chapter 17 ADR/RFC practice;
- Chapter 18 Architecture Review;
- Chapter 19 Architecture Freeze;
- an incident-management handbook;
- an SRE reliability taxonomy;
- a distributed-consensus chapter;
- a queueing or messaging tutorial;
- a product-line availability chapter;
- a release rollback handbook;
- an observability platform chapter;
- a new PEAK concept proposal.

## 10. Consequential Operations

The future draft should define consequential operation broadly: any action whose failure can change user-visible
behavior, product state, durable data, hardware state, safety posture, recovery cost, support work, or future
architecture.

Examples include command execution, firmware update, device configuration, calibration write, payment capture, data
export, protocol handoff, manufacturing transition, service action, and state migration. Not every function call needs
architecture-level failure design. Review depth should grow with consequence, side effects, durability, exposure,
dependency uncertainty, and recovery cost.

## 11. Success, Failure, Recovery

The chapter should avoid binary thinking.

Success means the system can prove that the promised effect happened and that the authoritative state reflects it.
Failure means the system can prove that the promised effect did not happen or cannot be accepted. Recovery means the
system moves from failed, partial, inconsistent, or uncertain state toward a known state with explicit ownership and
evidence.

Some operations remain uncertain for a while. A timeout may mean the system stopped waiting, not that the remote work
did not happen. A restart may erase volatile context without erasing external side effects. A late callback may prove
work completed after the caller already made another decision.

## 12. Operation Outcomes and Unknown Outcome

The future draft should use a practical outcome set without creating a formal taxonomy:

- rejected before execution;
- accepted but not started;
- started and completed;
- started and failed;
- started and timed out;
- started and may still complete;
- completed late;
- completed more than once from the observer's perspective;
- partially completed;
- canceled before effect;
- cancel requested but effect uncertain;
- recovery required;
- outcome unknown.

The unknown outcome is chapter-local language. It is not a new PEAK vocabulary concept. It means the system cannot yet
prove whether the operation happened, failed, or partially happened, so the next action must be constrained.

## 13. Detection and Ownership

Detection should answer what changed, who is allowed to decide, and what evidence is trustworthy.

Use `LAW-001` as a governing law. The state authority owns the recovery decision. Logs, callbacks, event streams,
service tools, and caches may provide evidence, but they must not silently become competing writers of product truth.

Detection should distinguish mechanism symptoms from product outcomes. A missing acknowledgment, driver reset, queue
overflow, or late callback is not automatically the product failure. The architecture must translate the symptom into a
product-level state and next action.

## 14. Retry Semantics

Retry is not recovery by itself.

The future draft should require every consequential retry path to answer:

1. What evidence says the first attempt did not complete?
2. Can the first attempt still complete?
3. Would retry duplicate side effects?
4. Which component is allowed to retry?
5. What spacing or limit prevents amplification?
6. What state changes after retry is exhausted?
7. What evidence is recorded for support and later review?

Longer waiting, blind retry, and infinite retry loops must be treated as design risks, not default safety.

## 15. Repeat Safety and Duplicate Handling

The chapter should teach repeat safety as a property of an operation in context, not a magic label.

An operation may be repeat-safe because it carries a stable operation ID, because the receiver stores completion, because
the action is naturally overwrite-like, because duplicate completion is suppressed, or because the second attempt is
validated against authoritative state before acting. Those mechanisms have different costs.

Duplicate handling should be explicit for commands, events, updates, writes, cancellations, and service actions.
Claiming retry safety without naming duplicate behavior is not acceptable.

## 16. Partial Completion

Partial completion is a product and state question.

The future draft should show that an operation may update durable state, affect hardware, send a message, alter a
remote system, or emit an event before the caller knows the outcome. Recovery must decide whether to finish, compensate,
reconcile, reject further action, or mark the state for human review.

Avoid saying that the system can always roll back. Some effects cannot be undone. A truthful recovery path may preserve
evidence, prevent further unsafe work, and require reconciliation rather than returning to the exact prior state.

## 17. Recovery to Known State

Recovery should aim for a known state, not necessarily the previous state.

A known state has named ownership, explicit allowed operations, visible uncertainty, and evidence that the system has
completed the recovery step or has stopped safely. The future draft should include reset, restart, reconnect, update
resume, journal replay, command reconciliation, and manual service handoff only where they clarify this idea.

The chapter should avoid making rollback the default answer. Rollback may be useful when it has been designed and
tested. Otherwise it can hide partial completion, stale dependencies, lost evidence, or unsupported old behavior.

## 18. Degradation and Containment

Degradation should be honest.

The system may offer reduced behavior when recovery is incomplete, but only if the remaining behavior does not depend on
the failed or uncertain state. A device may allow local read-only diagnostics while rejecting commands that need the
unknown state. A service may serve stale data with a clear validity marker while refusing writes. A controller may keep
safe monitoring active while blocking actuation until recovery evidence is available.

Containment means preventing failure in one dependency, boundary, queue, callback, or state owner from silently changing
unrelated product promises.

## 19. Persistence, Restart, Reset, Power Loss

The future draft must treat restart as part of the architecture.

Recovery design should ask what survives power loss, what is reconstructed, what is discarded, which operation IDs or
journal records remain, which events can replay, which callbacks are lost, and which external side effects may already
exist. It should also ask what the system does at boot when it finds partial state.

This section may use Chapter 5 and Chapter 13 evidence ideas, but it must not become a storage-atomicity tutorial or a
testing-methodology chapter.

## 20. Events and Callbacks

Events and callbacks are common recovery mechanisms and common failure sources.

Use `ARTIFACT-005` where event meaning, producer, consumer, ordering, timing assumptions, or failure behavior must be
visible. Use `SMELL-006` when event growth hides ownership or lifecycle. Use `ANTIPATTERN-005` when callback control flow
hides ordering, error handling, or state transitions.

The chapter should not claim events are better than direct calls. It should ask whether the mechanism preserves
authority, completion meaning, retry ownership, and recovery evidence.

## 21. Failure Observability

Failure observability should answer what happened, what is uncertain, and what the system did next.

Useful signals may include operation ID, state before request, acceptance result, execution-start evidence, dependency
response, timeout point, late completion, retry attempt, duplicate detection, partial state found at restart, recovery
action, final known state, and owner or review trigger.

This is not an observability platform chapter. It teaches the minimum architecture-level evidence needed for recovery
behavior to be explainable and testable.

## 22. Testing

The future draft should require failure tests that match the design claims.

Relevant tests may include dropped messages, reordered messages, duplicate messages, delayed completion, timeout with
late completion, reset during operation, power loss during durable update, restart with partial state, dependency
restart, reconnect, event replay, callback loss, duplicate retry, failed recovery, and manual recovery handoff.

Do not imply every product needs all tests. The test surface should follow consequence and recovery cost.

## 23. Bounded Recovery and Escalation

Recovery must have bounds.

The future draft should show what happens when automated recovery cannot prove a known state. Bounds may include retry
limits, exposure limits, time limits, state limits, customer-impact limits, safety limits, and review triggers. When a
bound is reached, the system should enter a named safe or constrained state, preserve evidence, and hand off to the
right owner or process.

Escalation is not a failure of design. Unbounded automation pretending to know more than it knows is the failure.

## 24. Boundary With Chapter 10

Chapter 10 owns temporal dependency: clock domains, timestamps, freshness, ordering, timeout semantics, reset, and
controllable time.

Chapter 16 may use timeouts, late completion, ordering, and reset as recovery inputs, but it must not reteach clocks or
temporal semantics. Its focus is the state and recovery behavior after a temporal or operational uncertainty appears.

## 25. Boundaries With Earlier Chapters

### Chapters 1-6 - Principal Engineering Foundations

Chapter 16 may use decision quality, ownership, evidence, and stewardship as premises. It must not repeat the Part I
mindset chapters.

### Chapter 7 - Every State Has One Owner

Chapter 16 may ask who owns state during recovery. It must not reteach the ownership law.

### Chapter 8 - Every API Is a Promise

Chapter 16 may define failure, completion, retry, and recovery as promises when visible to consumers. It must not become
an API-contract chapter.

### Chapter 9 - Every Dependency Is a Decision

Chapter 16 may show that dependencies import failure behavior and lifecycle constraints. It must not retell dependency
selection or replacement cost.

### Chapter 11 - Unused Flexibility Is Waste

Chapter 16 may reject speculative fallback modes and unowned options. It must not become an optionality audit.

### Chapter 12 - Simplicity Is a Feature

Chapter 16 may preserve necessary recovery distinctions. It must not become a general simplicity chapter.

### Chapter 13 - Evidence Before Confidence

Chapter 16 may require evidence for recovery claims. It must not teach the full confidence framework.

## 26. Boundaries With Chapters 17-19

### Chapter 17 - Using ADRs and RFCs Well

Chapter 16 may include one chapter-local ADR and may use existing records. Chapter 17 owns artifact choice, authoring,
review, lifecycle, and quality.

### Chapter 18 - Reviewing Architecture Before It Hardens

Chapter 16 may identify recovery assumptions that need review. Chapter 18 owns the Architecture Review ritual.

### Chapter 19 - Freezing Architecture Without Freezing Learning

Chapter 16 may record recovery risks and review triggers. Chapter 19 owns freeze, exceptions, and revalidation.

## 27. Boundaries With Later Parts

Part IV should retain detailed observability implementation, release rollback systems, upgrade architecture, product-line
availability, field operations, manufacturing recovery, and the reference project.

Part V should retain incident-response operating models, organizational rituals, alignment, escalation practice, and
Architecture Health Review operation.

Part VI should retain legacy recovery, silent-coupling discovery, broad refactoring, utility cleanup, and deletion
programs.

Chapter 16 may point toward those later practices only where needed to constrain failure and recovery design.

## 28. Story

### Working Title

The Lost Acknowledgment That Froze the Update

### System

Use an embedded device performing a firmware or configuration update through an unreliable communication path. The device,
gateway, service tool, and update coordinator exchange commands, acknowledgments, progress events, retry attempts, and
final completion.

### Incident Shape

One acknowledgment is dropped or delayed. The update coordinator times out and retries. The device may still be applying
the first request. A late completion arrives after the coordinator has moved on. The service tool and device disagree
about whether the update is running, failed, complete, or safe to restart.

The system logs plenty of symptoms but cannot answer the architectural question: what state is authoritative after the
lost acknowledgment?

### Tempting But Inadequate Responses

- Increase the timeout.
- Retry until the request succeeds.
- Restart the device.
- Treat the next progress event as truth.
- Add another status event.
- Ask the service tool to repair the state manually.
- Roll back by default.
- Hide the failure behind a generic communication error.

These responses may be useful in narrow conditions, but they do not define operation outcomes, duplicate handling,
partial completion, or recovery to a known state.

### Principal Engineer Intervention

The Principal Engineer recasts the problem from "packet loss" to "undefined operation outcome and recovery state."

The corrective model:

- assign one authority for update state;
- define operation IDs and acceptance results;
- distinguish started, not started, completed, failed, partial, late, duplicate, and unknown outcomes;
- make retry safe through duplicate detection or state reconciliation;
- record enough durable progress to recover after reset;
- define what can run while recovery is incomplete;
- expose recovery evidence through diagnostics and events;
- test dropped, delayed, duplicated, and reordered messages;
- record the recovery decision in an ADR.

## 29. Discussion Arc

1. **Failure design starts before failure.** The happy path is not complete until the system knows what happens when it
   is interrupted.
2. **Timeout is not proof of failure.** It is only proof that a waiting policy expired.
3. **Outcome semantics drive retry safety.** Retrying before knowing side effects can duplicate work.
4. **State authority matters during recovery.** Evidence sources do not become owners.
5. **Partial completion is normal in real systems.** Recovery must reconcile, finish, compensate, or stop.
6. **Events and callbacks need lifecycle meaning.** More signals can make recovery less clear if ownership is hidden.
7. **Restart is a recovery case.** The system must know what durable evidence survives.
8. **Degradation must be honest.** Reduced behavior is safe only when it does not rely on unknown state.
9. **Testing must disturb the failure path.** A recovery claim needs evidence under interruption, delay, duplicate, and
   restart.
10. **Escalation is designed behavior.** When automation cannot know, the system should preserve evidence and hand off.

These are intellectual progression points, not mandatory manuscript headings.

## 30. Applicability

The chapter applies when a system performs consequential operations across unreliable boundaries, asynchronous
callbacks, durable state, external dependencies, human service actions, firmware updates, configuration changes,
payments, migrations, queues, or long-running work.

It is especially relevant when timeout, retry, restart, cancellation, or recovery can affect product state or customer
trust.

## 31. Limits

The future draft must avoid dogmatism. It should not claim:

- every failure needs a complex recovery state model;
- every timeout proves failure;
- retry is always safe;
- rollback is always possible;
- degraded behavior is always safer than stopping;
- logs alone prove recovery;
- restart clears uncertainty;
- exactly one recovery pattern fits every operation;
- every operation needs an ADR;
- all failure modes can be known before release;
- all recovery can be automated.

## 32. Violations

The future draft should make these violations visible:

- retry without duplicate handling;
- timeout with no resulting state;
- callback mutation outside the state owner;
- dropped acknowledgment freezing progress;
- late completion treated as impossible;
- restart losing operation context;
- rollback assumed without evidence;
- generic error status hiding partial completion;
- service tool overwriting state without authority;
- event stream with unclear ordering or lifecycle;
- degraded behavior depending on unknown state;
- recovery loop with no bound;
- observability that records symptoms but not outcomes;
- manual recovery path with no owner or evidence.

## 33. Engineering Principle

Target principle for the future draft:

> Design the state after failure as carefully as the happy path: define outcomes, retry safety, containment, evidence,
> and the path back to a known state.

The principle should imply review questions:

1. What operation is consequential?
2. Who owns the authoritative state?
3. What proves the operation was accepted?
4. What proves execution started?
5. What proves completion?
6. What happens after timeout?
7. Can completion arrive late?
8. Is retry repeat-safe?
9. What happens after duplicate completion?
10. What partial state can remain?
11. What survives reset or power loss?
12. Which behavior is allowed while recovery is incomplete?
13. What evidence proves recovery succeeded?
14. What happens when recovery cannot prove a known state?

The final manuscript may shorten this list for reader rhythm.

## 34. Exercise

### Working Title

Design One Failure Path Before It Fails

Ask the reader to choose one consequential operation and document:

1. operation and product promise;
2. authoritative state owner;
3. acceptance result;
4. execution-start evidence;
5. success evidence;
6. failure evidence;
7. timeout state;
8. possible late completion;
9. possible duplicate effect;
10. partial-completion state;
11. retry authority;
12. repeat-safety mechanism;
13. cancellation or stop behavior;
14. durable progress record;
15. restart and power-loss behavior;
16. event or callback meanings;
17. diagnostics needed for support;
18. allowed reduced behavior;
19. automated recovery bound;
20. escalation owner and evidence;
21. tests that disturb timing and restart;
22. ADR or Decision Journal update.

The exercise must end with one explicit failure path, one retry decision, one recovery-to-known-state decision, and one
accepted residual uncertainty. Do not create a new canonical artifact.

## 35. ADR

### Working Title

Make Firmware Update Recovery Explicit After Lost Acknowledgment

### Context

- A device update request can cross an unreliable communication path.
- The coordinator may lose the acknowledgment while the device continues execution.
- Completion may arrive late or be duplicated.
- Reset or power loss may occur while update state is partial.
- The service tool, gateway, coordinator, and device can each observe different symptoms.
- Retrying blindly may duplicate effects or hide partial completion.

### Decision

- Assign authoritative update state to the device update owner.
- Use stable operation IDs for update attempts.
- Record acceptance, execution start, durable progress, completion, failure, and recovery state.
- Treat timeout as a waiting-policy expiry, not proof that work failed.
- Permit retry only through duplicate detection or state reconciliation.
- Define late completion behavior.
- Define restart behavior from durable progress.
- Define reduced behavior while recovery is incomplete.
- Emit product-level events for accepted, started, progress, completed, failed, recovery-started, and recovery-complete.
- Preserve enough diagnostics to explain lost, delayed, duplicate, and reordered messages.
- Escalate when the device cannot prove a known state.

### Alternatives Considered

- Increase timeout and keep the current state model.
- Retry the same request until success.
- Restart the device after communication loss.
- Let the service tool decide state from the latest event.
- Roll back automatically after any timeout.
- Add more events without assigning state authority.
- Require a perfect transport before updates are allowed.
- Replace the update subsystem in one rewrite.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits include explicit recovery state, safer retry, clearer support diagnostics, better restart behavior, and tests
that can prove the intended behavior under dropped, delayed, duplicated, and reordered messages.

Costs include operation IDs, durable progress records, duplicate detection, more explicit event meanings, compatibility
work with tools, and residual cases where human review is still required.

The ADR must make a real architecture decision. It must not reduce to "add retries."

## 36. PEAK Concept Map

### Concepts Inspected

- `FAILURE-002` - One Lost Packet.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-005` - Evidence Before Confidence.
- `LAW-007` - Every Dependency Is a Decision.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-005` - Callback Hell.
- `ANTIPATTERN-006` - Temporary Solution.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-005` - Event Catalog.
- `VOCAB-002` - Weak Signal.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-001` - Architecture Review.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.

### Selected Concepts

- `FAILURE-002` - One Lost Packet: material because the recommended story directly uses a lost or delayed
  acknowledgment to expose hidden retry and recovery assumptions.
- `LAW-001` - Every State Has One Owner: material because recovery decisions need a state authority.
- `LAW-002` - Every API Is a Promise: material because failure, completion, timeout, retry, and recovery behavior can be
  observable promises.
- `LAW-003` - Time Is a Dependency: material because timeouts, late completion, retry spacing, and restart timing shape
  recovery behavior.
- `LAW-005` - Evidence Before Confidence: material because recovery claims need test and diagnostic evidence.
- `LAW-007` - Every Dependency Is a Decision: material because dependencies import failure behavior and lifecycle
  constraints.
- `SMELL-001` - Silent Coupling: material because hidden dependency assumptions make retry and recovery unsafe.
- `SMELL-004` - Hidden State: material because partial, copied, stale, or durable state can affect recovery without a
  clear owner.
- `SMELL-006` - Event Explosion: material because recovery can be obscured by uncontrolled event growth.
- `ANTIPATTERN-005` - Callback Hell: material because callback ordering can hide error handling and state transitions.
- `ANTIPATTERN-006` - Temporary Solution: material because unowned fallback or compatibility paths can become permanent
  recovery behavior.
- `ARTIFACT-001` - ADR: material because the chapter-local decision affects ownership, cost, testability, and
  reversibility.
- `ARTIFACT-003` - Decision Journal: material because residual recovery uncertainty and bounded escalation can be
  recorded without a full ADR.
- `ARTIFACT-005` - Event Catalog: material because recovery events need meaning, producers, consumers, ordering, timing,
  and failure behavior.

### Rejected Concepts

- `VOCAB-002` - Weak Signal: useful for early evidence of recovery trouble, but Chapter 13 owns weak evidence.
- `ARTIFACT-007` - Weak Signal Register: useful when evidence is incomplete, but not central to the failure design
  practice.
- `RITUAL-001` - Architecture Review: recovery assumptions may need review, but Chapter 18 owns the ritual.
- `VOCAB-001` and `METRIC-001` - Change Radius: recovery work may affect many surfaces, but Chapter 15 owns the full
  method and metric.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as operation outcome, known state, recovery path, retry authority, duplicate handling, partial completion,
bounded recovery, degraded behavior, and escalation remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-016` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-016
  type: illustrates
  to: FAILURE-002

- from: CHAPTER-016
  type: references
  to: LAW-001

- from: CHAPTER-016
  type: references
  to: LAW-002

- from: CHAPTER-016
  type: references
  to: LAW-003

- from: CHAPTER-016
  type: references
  to: LAW-005

- from: CHAPTER-016
  type: references
  to: LAW-007

- from: CHAPTER-016
  type: references
  to: SMELL-001

- from: CHAPTER-016
  type: references
  to: SMELL-004

- from: CHAPTER-016
  type: references
  to: SMELL-006

- from: CHAPTER-016
  type: references
  to: ANTIPATTERN-005

- from: CHAPTER-016
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-016
  type: references
  to: ARTIFACT-001

- from: CHAPTER-016
  type: references
  to: ARTIFACT-003

- from: CHAPTER-016
  type: references
  to: ARTIFACT-005
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 37. Reader-Facing Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 16 role:

- Opening Quote: establish that the failure path is part of the design.
- Story: show a lost acknowledgment during a consequential embedded update or configuration operation.
- Discussion: teach outcomes, retry, repeat safety, partial completion, containment, observability, and recovery to known
  state.
- Engineering Principle: anchor recovery design as a review habit.
- Architecture Exercise: design one failure path before implementation.
- Principal's Notebook: three short observations, no explanations.
- ADR: record a scoped update recovery decision.
- Editor's Commentary: explain how Chapter 16 advances Part III after boundary and Change Radius work.

## 38. Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A timeout is not proof of failure.
- Retry without outcome semantics duplicates uncertainty.
- Recovery means returning to a known state, not necessarily the old state.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 39. Technical Requirements

The future draft must treat the following accurately:

- operation IDs;
- acceptance versus execution start;
- timeout expiry;
- late completion;
- duplicate completion;
- repeat safety;
- partial durable state;
- reset, restart, and power loss;
- dropped, delayed, duplicated, and reordered messages;
- callbacks and event ordering;
- retry limits and spacing;
- duplicate suppression;
- state reconciliation;
- update resume or stop behavior;
- diagnostics and support evidence;
- reduced behavior while recovery is incomplete;
- manual escalation when no known state can be proven;
- tests that inject interruption, delay, duplicate delivery, and restart.

Do not require a specific MCU, RTOS, transport, queue, database, update protocol, storage engine, cloud platform, or
observability tool.

## 40. Terminology

Use terms precisely:

- consequential operation: an action whose failure can change user-visible behavior, product state, durable data,
  hardware state, safety posture, recovery cost, support work, or future architecture;
- success: provable completion of the promised effect with authoritative state updated;
- failure: provable non-completion or rejected effect;
- timeout: expiry of a waiting policy, not proof that remote work did not happen;
- late completion: completion evidence arriving after the waiting party changed state;
- partial completion: some side effect may have happened before the final outcome was known;
- duplicate handling: explicit behavior when an operation or completion is observed more than once;
- repeat safety: explicit behavior for a specific operation under a specific state and contract;
- known state: a state with named ownership, allowed operations, visible uncertainty, and evidence;
- recovery: movement from failed, partial, inconsistent, or uncertain state toward a known state;
- escalation: designed handoff when automated recovery cannot prove a known state.

The chapter must avoid these misleading statements:

- timeout means failure;
- retry is safe by default;
- restart clears uncertainty;
- rollback always restores the old state;
- more events make recovery clearer;
- one generic error status is enough;
- logs prove recovery;
- repeat safety can be assumed because an API says so;
- degraded behavior is always better than stopping;
- humans can repair any unknown state without architecture support.

## 41. Failure Modes to Avoid

The later draft must not become:

- Chapter 10 repeated;
- Chapter 14 repeated;
- Chapter 15 repeated;
- an incident-response handbook;
- an SRE taxonomy;
- a distributed-systems proof chapter;
- a messaging tutorial;
- an observability platform chapter;
- a release rollback handbook;
- a product-line availability chapter;
- a generic "add retries" chapter;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 42. Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete lost-acknowledgment or dropped-message failure;
- the Principal Engineer move recasts the issue from communication loss to undefined outcome and recovery state;
- no primary PEAK concept is assigned unless a later author/editor decision changes repository convention;
- `FAILURE-002` is materially present as the central story anchor;
- timeout is not treated as proof of failure;
- retry behavior is designed with repeat safety and duplicate handling;
- partial completion and late completion are credible;
- state ownership during recovery is clear;
- recovery aims for a known state rather than promising universal rollback;
- events and callbacks preserve meaning, ordering, ownership, and evidence;
- degradation and containment are honest about unknown state;
- tests disturb timing, delivery, duplicate behavior, reset, and restart;
- the exercise ends with one explicit failure path, one retry decision, one recovery decision, and one residual
  uncertainty;
- the ADR makes a genuine architecture and recovery decision;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally;
- boundaries with Chapters 10, 14, 15, and 17-19 are respected.

## 43. Review Handoff

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into incident response, observability tooling, release rollback, or a generic retry chapter.

Canon Review should verify that Chapter 16 remains a Part III practice chapter with no forced primary concept, materially
uses `FAILURE-002` as the story anchor, preserves the registered relationship set, and does not imply a new PEAK
artifact, metric, ritual, or vocabulary term.

Technical Review should focus on operation IDs, timeout semantics, late completion, duplicate handling, partial state,
state authority, reset and power loss, event and callback ordering, retry bounds, diagnostics, recovery tests, and
honest degradation.

Freeze Review should confirm that Chapter 16 remains the third Part III practice chapter, keeps the manuscript
architecture intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and
leaves the reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
device, update protocol, transport, storage detail, recovery sequence, and final notebook wording while preserving the
failure-and-recovery thesis, story shape, PEAK map, and chapter boundaries.
