# CHAPTER-007 Canonical Brief: Every State Has One Owner

## Metadata

- Stable ID: `CHAPTER-007`.
- Title: `Every State Has One Owner`.
- Part: Part II - The Laws.
- Chapter number: 7.
- Expected manuscript path: `book/02-the-laws/07-every-state-has-one-owner.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-007-every-state-has-one-owner.md`.
- Branch: `chapter7`.
- Canonical predecessor: `CHAPTER-006` - Leaving Systems Better Than You Found Them.
- Part position: opening chapter of Part II - The Laws.
- Baseline `origin/main`: `8b95decf73a2771268c885143564f0bb4c23bd0f`.
- Reader-facing draft created: no.
- Primary law: `LAW-001` - Every State Has One Owner.
- Lifecycle status at brief-registration time: draft preparation.
- Next lifecycle stage: Author Draft after author approval.

## Repository-Grounded Findings

- `origin/main` resolves to `8b95decf73a2771268c885143564f0bb4c23bd0f`.
- That baseline includes Chapter 2 post-freeze revalidation in `main`.
- The Chapter 2 manuscript blob at the verified baseline is `e78bd7f8468350622ae4b49f6590473818c5894e`.
- `CHAPTER-001` through `CHAPTER-006` are registered as `canonical` in `knowledge/index.yaml`.
- Chapter 6 is present at `book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md`.
- `editor/EDITOR_LOG.md` records the required Chapter 6 review and freeze workflow.
- The table of contents places `Every State Has One Owner` first in Part II.
- `LAW-001` exists and is named `Every State Has One Owner`.
- `CHAPTER-007` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 7 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter7` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 1. Canonical Purpose

Prepare Chapter 7 to open Part II by teaching the first PEAK law: every meaningful state needs one unambiguous authority
for its valid value and transitions at a given time and scope.

The chapter should move the reader from vague "single source of truth" language to a reviewable architecture question:
who is allowed to decide what this state means now, which transitions are valid, and how every other representation
relates to that authority?

The chapter must not create a reader-facing draft during this task. It must constrain the later Author Draft.

## 2. Central Thesis

A meaningful state may have many observers, copies, projections, and persistence forms, but exactly one authority must
decide its valid value and transitions.

Approved supporting formulation for the future draft:

> One state, one authority for change.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 3. Reader Transformation

Before the chapter, the reader may think:

1. state ownership means choosing a module or storing a value in one place;
2. synchronization can compensate for multiple authorities;
3. caches, persistence, telemetry, and UI values are harmless copies;
4. a setter is sufficient when several components need control;
5. the latest timestamp or most convenient writer can resolve disagreement.

By the end of the chapter, the reader should be able to:

1. identify the semantic owner of meaningful state;
2. separate requests, observations, caches, persistence, and derived views from authority;
3. detect duplicate writers and inferred owners;
4. replace raw writes with intent-level commands routed through the owner;
5. define reset, recovery, stale-observation, and ownership-handoff behavior;
6. record the decision in existing PEAK artifacts and test invalid transitions.

## 4. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 7 covers:

- semantic ownership of meaningful system state;
- one authority for valid values and transitions;
- the difference between commands and raw setters;
- duplicate writers and competing sources of truth;
- hidden state created by inference and local reconstruction;
- persisted copies versus runtime authority;
- ownership transfer across lifecycle or subsystem boundaries;
- observers, caches, projections, and versioned snapshots;
- failure modes when ownership is unclear;
- architectural techniques for restoring one-owner semantics;
- evidence that ownership is understandable and discoverable;
- documenting the decision with existing PEAK artifacts.

### Explicitly Out of Scope

Do not turn Chapter 7 into:

- organizational accountability in general;
- project ownership, delivery ownership, or taking initiative;
- generic clean-code encapsulation;
- database normalization;
- distributed consensus algorithms in depth;
- event sourcing as a universal answer;
- API compatibility and versioning in depth;
- dependency management in depth;
- clock synchronization or temporal ordering in depth;
- configuration strategy as a complete topic;
- broad observability or metrics design;
- a catalog of concurrency primitives;
- implementation recipes for one language, RTOS, MCU, cloud platform, database, or framework.

Those topics may appear only where they clarify state authority.

## 5. Boundaries With Chapters 1-6

### Chapter 1 - What Is a Principal Engineer?

Chapter 1 frames architecture as decision-making and future system cost. Chapter 7 applies that frame to state
authority. It must not repeat the Principal Engineer role definition or the general decision-system argument.

### Chapter 2 - Decision-Making Under Constraints

Chapter 2 teaches constrained commitments. Chapter 7 may show that state ownership is one decision a team must make, but
it must not repeat the full constraint, consequence, uncertainty, or reversal-cost framework.

### Chapter 3 - Asking Better Engineering Questions

Chapter 3 already asks which component owns authoritative device state and freshness semantics. Chapter 7 turns that
kind of question into the law itself. It must not repeat Chapter 3's inquiry-shaping story or root-cause investigation
arc.

### Chapter 4 - Ownership Beyond Code

Chapter 4 concerns responsibility for outcomes, accepted handoffs, and durable closure across boundaries.

Chapter 7 concerns architectural authority over a specific piece of system state and its valid transitions.

Do not collapse these meanings of ownership. Chapter 7's owner is the authority responsible for state validity and
transition control, not the person or team responsible for every outcome near the state.

### Chapter 5 - Technical Judgment and Evidence

Chapter 5 owns evidence quality and confidence calibration. Chapter 7 may require evidence that state ownership is
discoverable and testable, but it must not reteach evidence-quality dimensions or experimental design.

### Chapter 6 - Leaving Systems Better Than You Found Them

Chapter 6 closes Part I with bounded stewardship. Chapter 7 starts Part II by naming a durable law that future
stewardship work can apply. It must not become another proportional-cleanup or future-change-cost chapter.

## 6. Boundary With Later Part II Laws and Later Parts

Chapter 7 must preserve the primary arguments of later Part II chapters:

- Chapter 8 - `Every API Is a Promise`: Chapter 7 may show commands and observations crossing interfaces, but Chapter 8
  owns the broader API-contract argument.
- Chapter 9 - `Every Dependency Is a Decision`: Chapter 7 may mention dependencies that duplicate or reconstruct state,
  but dependency selection and governance belong later.
- Chapter 10 - `Time Is a Dependency`: Chapter 7 may address stale observations, epochs, ordering, and reset
  re-establishment, but time semantics belong later.
- Chapter 11 - `Unused Flexibility Is Waste`: Chapter 7 may reject extra setters and duplicate owners, but the broader
  cost of unused options belongs later.
- Chapter 12 - `Simplicity Is a Feature`: Chapter 7 may prefer a clearer authority model, but simplicity as a system
  property belongs later.
- Chapter 13 - `Evidence Before Confidence`: Chapter 7 may require reviewable evidence, but the full evidence law
  belongs later.

Later parts should retain boundary playbooks, configuration and product variants, diagnosing hidden coupling, Boolean
Explosion as a dedicated smell, event architecture as a complete discipline, observability design, release discipline,
legacy recovery, and organizational operating models.

## 7. Recommended Embedded-Systems Story

### Working Title

The Mode That Had Five Truths

### System

Use an industrial embedded controller with meaningful operational modes such as `Boot`, `SafeIdle`, `Ready`, `Active`,
`Service`, and `Fault`.

Over time, several components acquire their own idea of current operational mode:

1. the firmware runtime state machine;
2. a persisted configuration or last-mode field;
3. a service application that caches and sometimes rewrites mode;
4. a manufacturing or maintenance fixture with a privileged diagnostic command;
5. a supervisory controller that infers mode from outputs or telemetry.

The system exposes raw setters or writable flags rather than intent-level commands.

### Incident Shape

After a watchdog reset or interrupted service operation:

- firmware enters `SafeIdle`;
- persisted storage still says `Service`;
- the service application displays cached `Service`;
- the fixture believes calibration is still active;
- a supervisor infers `Ready` from a subset of outputs.

Different actors attempt to correct one another. The result may include an output enabled under the wrong assumptions,
an operation rejected without an explainable reason, inconsistent safety interlock behavior, a mode that flips after
reboot, logs that cannot identify the authoritative decision, or a defect reproduced only through a reset, reconnect,
and retry sequence.

### Tempting But Inadequate Response

The team initially proposes synchronization tactics:

- synchronize all mode flags more frequently;
- add retries;
- let the newest timestamp win;
- give every component a setter and rely on convention;
- persist every transition immediately;
- add another mode-valid Boolean;
- infer mode from outputs when values disagree.

The future draft must show why these responses make ambiguity more durable. They move guesses faster; they do not name
authority.

### Principal Engineer Intervention

The Principal Engineer recasts the issue from state synchronization to state authority.

The corrective model:

- the controller runtime state machine is the sole authority for current operational mode;
- other components send intent-level commands such as `RequestServiceMode` instead of assigning a raw mode value;
- the owner validates preconditions and invariants;
- the owner accepts or rejects the request with an explainable reason;
- the owner publishes accepted state transitions with a version, epoch, or transition identity where appropriate;
- UI, supervisor, and service-tool values are explicit observations, not competing owners;
- persistence owns only information it actually owns, such as boot policy, acknowledged configuration, or history;
- a manufacturing fixture receives a bounded privileged transition path, not a bypass setter;
- reset behavior defines which persisted inputs are consulted and how the runtime owner re-establishes authority;
- any ownership handoff is explicit, ordered, and mutually exclusive.

The point is not that a state machine class is always the answer. The point is that one decision authority exists and
all change flows through it.

## 8. Expected Discussion Arc

1. **State is not just data.**
   Meaningful state includes invariants, valid transitions, history, and consequences.
2. **Copies are not owners.**
   Persistence, caches, telemetry, and UI projections can represent state without deciding it.
3. **Multiple writers create policy by accident.**
   Several components assigning the same meaning fragment validation and transition semantics.
4. **Inference creates hidden ownership.**
   A component reconstructing state from symptoms can silently become an unofficial authority.
5. **Raw setters erase intent.**
   Commands should express requested outcomes; the owner decides whether the transition is allowed.
6. **One owner does not mean one consumer.**
   Many observers, callers, replicas, and snapshots can coexist with one authority.
7. **Ownership is scoped in time and responsibility.**
   Transfer is possible, but it must be explicit, ordered, and mutually exclusive.
8. **Recovery requires choosing authority, not merging guesses.**
   When copies disagree, reconciliation must be grounded in ownership.
9. **Ownership should be discoverable.**
   Engineers should be able to find the owner, invariants, commands, events, persistence semantics, and handoff rules.
10. **The law reduces coordination cost.**
    Clear authority improves diagnosis, testing, review, change safety, and incident explanation.

These are intellectual progression points, not mandatory top-level manuscript headings.

## 9. Engineering Principle Target

Target principle for the future draft:

> For every meaningful state, name one authority that validates its value and controls its transitions. Other components
> may request, observe, cache, persist, or derive that state, but they must not become competing sources of truth.

The principle should be memorable, precise enough for architecture review, applicable beyond the story, careful about
ownership transfer and derived views, and compatible with embedded, distributed, and software-intensive systems.

The principle should imply review questions:

1. What state is being discussed?
2. What invariants define it?
3. Who owns its transitions?
4. Which interfaces request change?
5. Which representations are derived?
6. What happens after reset?
7. How is stale or conflicting state detected?
8. How is ownership handed over?
9. Can an engineer find the answer in the repository?

## 10. Architecture Exercise Target

### Working Title

Trace One State to One Owner

Ask the reader to choose one meaningful state from a real system and document:

1. the state's exact name and scope;
2. the business or system meaning;
3. valid values;
4. invariants;
5. valid transitions;
6. current decision authority;
7. all current writers;
8. all callers;
9. all observers;
10. persisted representations;
11. caches and projections;
12. inferred versions of the state;
13. reset and recovery semantics;
14. ownership-transfer boundaries;
15. evidence that identifies the owner;
16. duplicate writers or unofficial owners to remove;
17. command and observation interfaces;
18. tests proving invalid transitions are rejected;
19. the ADR or existing artifact where the decision should be recorded.

The exercise must produce an actionable review of a real architecture. It must not create a new canonical artifact such
as State Ownership Map. A temporary table or worksheet is acceptable inside the chapter when it relies on existing PEAK
artifacts such as ADRs and the Event Catalog.

## 11. Chapter-Local ADR Brief

### Working Title

Make the Device Mode State Machine the Sole Authority for Operational Mode

### Context

- Current operational mode is duplicated across firmware, persistence, service tooling, and fixture logic.
- Multiple components can assign or repair mode.
- Reset and reconnect sequences expose disagreement.
- Validation rules are inconsistent.
- Diagnosis cannot reliably explain who changed the state.

### Decision

- Assign current operational mode to one runtime authority.
- Replace raw external setters with intent-level commands.
- Validate transitions in the owner.
- Publish accepted state with enough versioning or transition identity to identify stale observations.
- Define persistence as input or history according to its own responsibility, not as a second runtime owner.
- Define privileged fixture behavior through the same ownership boundary.
- Document reset recovery and any ownership handoff.

### Alternatives Considered

- Keep multiple writers and synchronize them.
- Let the newest timestamp win.
- Make persistent storage authoritative at all times.
- Infer current mode from outputs.
- Use a distributed ownership protocol.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits:

- one place for invariants and transition policy;
- explainable rejection of invalid commands;
- fewer race conditions and contradictory repairs;
- simpler tests and diagnosis;
- clearer reset behavior;
- better discoverability.

Costs:

- migration of existing writers;
- compatibility work for service tooling;
- possible queueing or serialization;
- explicit versioning and stale-observation handling;
- extra design work for ownership transfer;
- pressure on the owner interface to remain focused rather than become a god object.

The ADR is story-local and reader-facing. It must not become a repository-level ADR or a tutorial on ADR mechanics.

## 12. PEAK Concept Map

### Primary Concept

- `LAW-001` - Every State Has One Owner: the chapter directly illustrates this law as the opening law of Part II.

### Required Supporting Concepts

- `SMELL-004` - Hidden State: material because inferred or locally reconstructed mode becomes behavior-affecting state
  without a clear owner.
- `ANTIPATTERN-003` - Global Configuration: material because broad mode flags and last-mode fields can turn operational
  state into configuration without scope.
- `ARTIFACT-001` - ADR: material because the state-owner decision affects future architecture, ownership, cost, and
  reversibility.
- `ARTIFACT-005` - Event Catalog: material because published state transitions and observations need named events,
  producers, consumers, ordering assumptions, and failure behavior.
- `METRIC-003` - Discoverability: material because engineers must be able to find the state owner, invariants, commands,
  persistence semantics, and handoff rules.

### Optional Supporting Concepts

- `SMELL-001` - Silent Coupling may appear if the story shows tools or supervisors depending on hidden mode semantics.
- `SMELL-003` - Boolean Explosion may appear if the draft uses mode-valid or service-active flags as a contrast to named
  states.
- `SMELL-006` - Event Explosion may appear if extra events obscure state meaning rather than clarifying it.

Do not force optional concepts into `knowledge/index.yaml` unless the final manuscript materially teaches them.

## 13. Exact Proposed PEAK Relationships

Register `CHAPTER-007` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-007
  type: illustrates
  to: LAW-001

- from: CHAPTER-007
  type: illustrates
  to: SMELL-004

- from: CHAPTER-007
  type: references
  to: ANTIPATTERN-003

- from: CHAPTER-007
  type: references
  to: ARTIFACT-001

- from: CHAPTER-007
  type: references
  to: ARTIFACT-005

- from: CHAPTER-007
  type: references
  to: METRIC-003
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 14. Required Chapter Architecture

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

## 15. Required Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- Copies are not owners.
- A setter is not authority.
- Recovery needs a named truth.

These are semantic targets, not mandatory final wording.

## 16. Evidence and Technical Credibility Requirements

The future draft must be credible for embedded systems. It should treat the following correctly:

- reset and startup behavior;
- runtime versus persisted state;
- concurrency and serialization;
- command acceptance and rejection;
- stale observations;
- version or epoch semantics where appropriate;
- privilege boundaries for service and manufacturing tools;
- failure recovery;
- state-transition logging;
- tests for invalid transitions;
- ownership handoff.

The story should remain architecture-neutral unless a small illustrative detail is necessary. Do not require a specific
RTOS, programming language, MCU, cloud platform, database, protocol, or framework.

## 17. Terminology and Precision Guardrails

The owner is the authority responsible for:

- deciding whether a transition is valid;
- enforcing state invariants;
- accepting or rejecting commands that request change;
- publishing resulting state to observers;
- explaining why the state has its current value;
- defining recovery behavior when state is uncertain or corrupted.

The owner is not automatically:

- the memory address where a value is stored;
- the module that last wrote a field;
- the thread or task currently executing code;
- the database table containing a persisted copy;
- the team that happens to maintain a consumer;
- the UI that displays the value;
- the cache that most recently refreshed;
- the component with the most convenient setter.

The chapter must avoid these misleading statements:

- "Only one function may ever write the value."
- "The database is always the owner."
- "The component that stores the value owns it."
- "One owner means no replication."
- "One owner means no concurrency."
- "Every derived value needs its own independent source of truth."
- "The newest timestamp always identifies the truth."
- "A singleton solves ownership."
- "A state machine class automatically establishes ownership."
- "Events eliminate the need to define an owner."
- "Ownership can never move."
- "Centralization is always superior to distributed authority."

The law is satisfied only when there is one unambiguous authority at a given time and scope, or when ownership transfer
is explicit, ordered, and mutually exclusive.

## 18. Failure Modes to Avoid

The later draft must not become:

- a generic single-source-of-truth essay with no transition semantics;
- an organizational responsibility chapter;
- a ban on caches, replicas, persistence, telemetry, or UI projections;
- an argument for one global variable;
- a concurrency tutorial;
- event sourcing, CQRS, or consensus as fashionable decoration;
- a new PEAK artifact proposal;
- a repetition of Chapter 4;
- an early version of Chapter 8's API-contract argument;
- a shallow ADR that restates the principle without deciding anything;
- a worksheet with no real architectural decision;
- an unqualified safety claim;
- unexplained implementation jargon;
- reader-facing draft prose inside the canonical brief.

## 19. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains concrete disagreement among competing state authorities;
- the Principal Engineer move recasts synchronization as authority;
- the law is explained beyond the slogan;
- runtime, persisted, desired, observed, reported, last-known, cached, UI, telemetry, and derived state are distinguished;
- ownership transfer is addressed;
- reset and recovery semantics are credible;
- the exercise can be applied to a real system;
- the ADR makes a genuine decision and acknowledges benefits and costs;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally;
- boundaries with Chapters 1-6, later Part II laws, and later parts are respected;
- claims are technically credible and reviewable.

## 20. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into a systems-programming tutorial.

Canon Review should verify that the chapter illustrates `LAW-001`, materially uses the registered supporting concepts,
does not imply a new PEAK artifact or vocabulary term, and preserves the boundaries with Chapter 4 and later Part II
laws.

Technical Review should focus on reset behavior, persisted versus runtime state, command semantics, stale observations,
ownership transfer, concurrency, privilege paths, and recovery after disagreement.

Freeze Review should confirm that Chapter 7 truly opens Part II, keeps the manuscript architecture intact, uses exactly
three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the reader-facing manuscript in
canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
mode names, fixture details, versioning mechanism, and final notebook wording while preserving the state-authority thesis,
story shape, PEAK map, and chapter boundaries.

## Final Scope Statement

Chapter 7 should define state ownership as one scoped authority for valid values and transitions. It should show an
embedded operational-mode failure where synchronization tactics fail because the system lacks authority, then guide the
reader toward commands, observations, persistence semantics, event records, reset behavior, handoff rules, tests, and an
ADR that make ownership discoverable without banning copies or inventing new canon.
