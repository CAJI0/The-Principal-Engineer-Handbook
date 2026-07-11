# CHAPTER-010 Canonical Brief: Time Is a Dependency

## Metadata

- Stable ID: `CHAPTER-010`.
- Title: `Time Is a Dependency`.
- Part: Part II - The Laws.
- Chapter number: 10.
- Expected manuscript path: `book/02-the-laws/10-time-is-a-dependency.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-010-time-is-a-dependency.md`.
- Branch: `chapter10`.
- Canonical predecessor: `CHAPTER-009` - Every Dependency Is a Decision.
- Part position: fourth chapter of Part II - The Laws.
- Verified baseline `origin/main`: `845755ab99988317229946c93f419cc79d4315a0`.
- Reader-facing draft created: no.
- Primary law: `LAW-003` - Time Is a Dependency.
- Lifecycle status at brief-registration time: draft preparation.
- Next lifecycle stage: Author Draft after author approval.

## Repository-Grounded Findings

- `origin/main` resolves to `845755ab99988317229946c93f419cc79d4315a0`.
- That baseline is the PR #11 squash commit, `Chapter 9: Every Dependency Is a Decision (#11)`.
- The Chapter 9 feature-branch Freeze commit `cd3556768e9dbcad17f5cb75e59fe77479ada969` is not required to be an ancestor
  of `main` because PR #11 used squash merge.
- The final Chapter 9 lifecycle files in the PR #11 squash commit are tree-equivalent to the final feature-branch Freeze
  commit for the checked Chapter 9 paths.
- `CHAPTER-001` through `CHAPTER-009` are registered as `canonical` in `knowledge/index.yaml`.
- Chapter 9 exists at `book/02-the-laws/09-every-dependency-is-a-decision.md`.
- `editor/EDITOR_LOG.md` records Chapter 9 Editorial, Canon, Technical, and Freeze Review entries in order.
- The repository table of contents lives at `book/00-front-matter/table-of-contents.md` and places `Time Is a
  Dependency` after `Every Dependency Is a Decision` in Part II.
- `LAW-003` exists exactly once and is named `Time Is a Dependency`.
- `LAW-003` states that code depending on timing depends on architecture, and its related concepts are Event Catalog,
  Hidden State, and Architecture Review.
- `CHAPTER-010` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 10 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter10` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 1. Canonical Purpose

Prepare Chapter 10 to teach the fourth Part II law: time is not neutral background context. Any consequential use of
time imports assumptions about clock source, accuracy, monotonicity, synchronization, ordering, persistence, reset
behavior, validity, and failure.

The chapter should move the reader from treating `now()`, timestamps, delays, and timeouts as interchangeable utilities
toward a reviewable architecture question: which temporal meaning and clock domain does this decision depend on, and
what happens when that assumption fails?

The chapter must not create a reader-facing draft during this task. It must constrain the later Author Draft.

## 2. Exact Law Statement

`LAW-003` states:

> Any code that depends on timing depends on architecture.

Chapter 10 should preserve that law while broadening "timing" into concrete temporal dependencies: clocks, elapsed
duration, deadlines, timeouts, retry intervals, freshness, ordering, periodic work, synchronization, reset behavior, and
persisted temporal state.

## 3. Central Thesis

Every consequential use of time imports assumptions about clock source, accuracy, monotonicity, synchronization,
ordering, persistence, reset behavior, validity, and failure. Those assumptions are dependencies and must be designed
explicitly.

Approved supporting formulation for the future draft:

> Choose the clock and the temporal meaning before relying on the value.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 4. Reader Transformation

Before the chapter, the reader may think:

1. time is a utility value supplied by the platform;
2. one `now()` function is suitable for timeouts, timestamps, freshness, cleanup, and UI display;
3. a timestamp proves freshness;
4. a timeout merely means waiting for a fixed duration;
5. synchronized wall-clock time solves ordering and elapsed-time problems;
6. test clocks that move forward normally are enough evidence;
7. reset and clock correction are edge cases rather than architecture.

By the end of the chapter, the reader should be able to:

1. distinguish wall-clock time, monotonic time, duration, deadline, timestamp, ordering, and freshness;
2. name the clock domain behind a temporal decision;
3. identify whether a clock can jump, drift, reset, wrap, or become invalid;
4. define timeout and deadline semantics as state transitions, not just waits;
5. handle reboot, persisted time, synchronization, and correction deliberately;
6. separate external records and UI calendar meaning from elapsed runtime measurement;
7. test temporal behavior with controllable clocks that jump, drift, wrap, reset, and lose validity;
8. record temporal decisions where future maintainers can find them.

## 5. Semantic Definition of Time as a Dependency

Time becomes a dependency whenever system behavior relies on a temporal source, temporal meaning, or temporal ordering
assumption that the system cannot freely change without consequence.

Potential sources include:

- oscillator;
- hardware timer;
- RTC;
- monotonic counter;
- scheduler tick;
- RTOS timer;
- network time source;
- GPS time;
- supervisory controller;
- persisted timestamp;
- human-set clock;
- build time;
- device uptime;
- protocol-provided timestamp.

The chapter should not catalog peripherals for their own sake. It should show the architectural consequences of relying
on them: invalid startup time, drift, wrap, correction, synchronization delay, reset, uncertainty, unavailable authority,
and disagreement between components.

## 6. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 10 covers:

- time as an architectural dependency;
- wall-clock time versus monotonic time;
- duration versus timestamp;
- timeout versus deadline;
- retry intervals, schedules, periodic work, drift, jitter, missed periods, backlog, and catch-up behavior;
- event ordering without trustworthy wall-clock timestamps;
- freshness as a rule with validity, age, delay, sampling, caching, update, reset, and uncertainty;
- RTC validity, monotonic counter reset, retained and non-retained clocks, boot epochs, and persisted expiration;
- clock correction, synchronization after boot, drift, wrap, and disagreement between devices;
- ownership and authority for clock validity and wall-clock interpretation;
- testability with controllable time sources;
- diagnostics that reveal clock source, validity, domain, correction, and uncertainty;
- recording material temporal decisions in existing artifacts.

### Explicitly Out of Scope

Do not turn Chapter 10 into:

- a generic date/time programming guide;
- an RTOS timer tutorial;
- a distributed consensus or formal causal-ordering chapter;
- a date arithmetic or timestamp-format tutorial;
- an NTP, GPS, timezone, or calendar handbook;
- a full API-contract chapter;
- a retelling of state ownership;
- a retelling of dependency selection and replacement cost;
- a broad observability architecture chapter;
- a testing-methodology chapter;
- a speculative new PEAK artifact proposal;
- a Part III architecture-review playbook;
- a Part IV fleet-time-management chapter;
- a Part VI legacy migration chapter.

Those topics may appear only where they clarify temporal dependency.

## 7. Temporal Meanings

The future draft should distinguish several meanings of time:

- elapsed duration: how much time passed according to a suitable clock;
- deadline: a boundary by which something must happen;
- timeout: a relative wait bound with defined state after expiry;
- retry interval: spacing between attempts with safety and duplicate-operation implications;
- schedule: planned execution in relation to a clock or cadence;
- wall-clock timestamp: calendar time according to a clock domain;
- monotonic time: non-decreasing time appropriate for elapsed measurement inside one runtime domain;
- boot-relative time: time since a boot epoch or runtime start;
- event order: which event happened before another in a chosen ordering model;
- freshness: whether data is valid enough for a decision;
- lease validity: whether a granted right remains usable;
- expiration: when a value stops being valid by rule;
- sampling period: how often a value is observed;
- rate limit: how often an action may occur;
- watchdog window: temporal bounds for proving the system is still making progress;
- persisted timestamp: stored temporal evidence that must be interpreted after restart;
- external time authority: a source outside the local process or device.

The point is not taxonomy. The point is to prevent incompatible temporal meanings from being silently mixed.

## 8. Clock Domains and Sources

A clock domain is the scope within which a time value has a defined meaning, validity, monotonicity, resolution, and
failure behavior.

Examples:

- MCU monotonic timer since boot;
- RTOS tick counter;
- RTC UTC after validation;
- gateway wall-clock time;
- GPS-derived time;
- server receipt time;
- protocol sequence number or event counter;
- persisted timestamp from a previous boot;
- UI-local converted display time.

The author draft should show that moving a value between clock domains requires an explicit rule. A persisted RTC
timestamp, a boot-relative monotonic value, and a UI-local display time are not interchangeable because they answer
different questions.

## 9. Wall Clock and Monotonic Time

Wall-clock time is human or calendar time. It may jump forward, jump backward, be synchronized after boot, be set by a
human or external service, become invalid, drift, or disagree with another device.

Monotonic time is a non-decreasing measure within a runtime domain. It is appropriate for elapsed duration, timeout
measurement, and runtime deadline calculation. It may still reset at reboot, wrap, lose power, differ across processors,
or become unavailable if the underlying timer fails.

The chapter must not imply that wall clock is always wrong or that monotonic time solves every problem. Wall clock is
appropriate for external records, calendar meaning, logs that need human interpretation, and protocols that require
shared time. Monotonic time is appropriate for elapsed behavior inside a domain. Each use needs its own decision.

## 10. Duration, Deadline, Timestamp, Ordering, and Freshness

A duration answers "how much time elapsed?" A timestamp answers "when did this happen according to some clock?" A
deadline defines a boundary by which something must happen. Ordering defines sequence or causality. Freshness defines
whether data is valid enough for a decision.

The future draft must not allow code to silently subtract, compare, order, expire, or retry using values from
incompatible temporal domains.

Ordering is especially important. Events can be ordered without trustworthy wall-clock timestamps by using sequence
numbers, accepted state transitions, event IDs, local monotonic values, or protocol-specific ordering. Timestamps can
disagree even when causal order is known. The chapter may name this distinction without becoming a distributed-systems
theory chapter.

Freshness is not "timestamp exists." It depends on clock domain, validity, age calculation, transport delay, sampling,
caching, update policy, reset, and uncertainty.

## 11. Timeout Semantics

A timeout is an architectural decision about:

- what is being waited for;
- which clock measures the wait;
- what expiration means;
- whether the operation may still complete after timeout;
- what state remains after timeout;
- whether retry is safe;
- whether duplicate completion is possible;
- how diagnostics distinguish slow, failed, delayed, and unknown.

The chapter should connect timeout semantics to Chapter 8 only as a boundary: if consumers observe timeout behavior,
that behavior may be an API promise. Chapter 10 owns the deeper temporal meaning.

Longer timeouts are not automatically safer. They can hide failure, delay recovery, extend stale state, and make tests
less representative. Shorter timeouts are not automatically better. The decision depends on the state transition being
bounded and the consequence of being wrong.

## 12. Periodic Work, Drift, and Jitter

Periodic behavior needs policy.

The future draft should distinguish:

- delay-after-completion scheduling;
- fixed-rate scheduling;
- drift;
- jitter;
- missed periods;
- backlog;
- catch-up behavior;
- skipped periods;
- rate limiting;
- watchdog windows.

The chapter should show that a loop that "runs every minute" may mean several incompatible things. If work takes longer
than expected, if the clock jumps, or if the system sleeps, the architecture must decide whether to catch up, skip,
coalesce, fail, or mark the data uncertain.

## 13. Reset, Persistence, and Boot Epochs

Reset exposes temporal assumptions.

The future draft must address:

- monotonic counter reset;
- RTC validity after boot;
- retained versus non-retained clocks;
- persisted expiration interpreted after reboot;
- reboot during timeout;
- stale timestamps;
- boot epochs;
- time becoming valid after startup;
- records that appear to come from the future;
- data written under one clock assumption and read under another.

A boot epoch or generation can help distinguish one runtime timeline from another. It should remain chapter-local prose,
not a new PEAK concept.

## 14. Synchronization, Correction, Drift, and Wrap

The chapter must address what happens when time:

- jumps forward;
- jumps backward;
- is synchronized after boot;
- loses validity;
- differs across devices;
- wraps;
- drifts;
- is corrected while an operation is waiting;
- is corrected while persisted data is being interpreted.

NTP, GPS, or another external authority can improve wall-clock meaning, but it does not automatically make time
trustworthy for every purpose. Precision is not accuracy. Synchronization is not monotonicity. A valid RTC does not prove
freshness.

## 15. Boundaries With Chapters 1-9

### Chapters 1-6 - Principal Engineering Foundations

Chapter 10 may use decision quality, constraints, questions, ownership, evidence, and stewardship as premises. It must
not repeat the Part I mindset chapters. Temporal dependency is the subject.

### Chapter 7 - Every State Has One Owner

Chapter 7 owns state authority. Chapter 10 may ask which component owns wall-clock interpretation, clock validity,
timeout state, or freshness state, but it must not reteach state ownership.

### Chapter 8 - Every API Is a Promise

Chapter 8 owns API promises. Chapter 10 may state that timing, timeout, ordering, and freshness are observable contract
dimensions, but it must not become another API chapter.

### Chapter 9 - Every Dependency Is a Decision

Chapter 9 establishes that dependencies import behavior, failure, lifecycle, ownership, and replacement cost. Chapter 10
applies that reasoning specifically to clocks and temporal assumptions. It must not repeat generic dependency-selection
material.

## 16. Boundaries With Later Part II Laws

- Chapter 11 - `Unused Flexibility Is Waste`: Chapter 10 may approve controllable clocks or temporal abstractions where
  testing, portability, or multiple clock domains justify them. It must not propose speculative clock abstraction layers
  for every function.
- Chapter 12 - `Simplicity Is a Feature`: Chapter 10 may prefer clear temporal semantics over a generic time utility,
  but it must not become a broad simplicity argument.
- Chapter 13 - `Evidence Before Confidence`: Chapter 10 may require tests and diagnostics for temporal behavior, but the
  full evidence-quality argument belongs later.

## 17. Boundaries With Later Parts

Later parts should retain complete boundary-design playbooks, ADR and RFC operations, review rituals, product
configuration, field telemetry, release and upgrade architecture, fleet-time management, and legacy time archaeology.

Chapter 10 should remain at law level. It names temporal dependency and gives the reader enough practice to recognize
and constrain it.

## 18. Recommended Embedded-Systems Story

### Working Title

The Clock That Meant Everything

### System

Use an embedded controller with:

- an RTC storing UTC;
- a monotonic hardware timer;
- network synchronization after connectivity starts;
- persisted records with timestamps;
- command freshness checks;
- communication timeout logic;
- periodic cleanup;
- a UI that displays local time.

Over time, several modules call one generic `now()` API and assume it is suitable for every temporal decision.

### Incident Shape

A reboot occurs with invalid or stale RTC time. Later, network synchronization corrects the clock backward.

The system may then:

- accept a command incorrectly as fresh;
- extend an active timeout or expire it immediately;
- show records as if they came from the future;
- retain stale data or delete current data during cleanup;
- schedule retries unexpectedly;
- make UI and diagnostics disagree about event order;
- pass tests because the test clock never jumps, drifts, wraps, or resets.

### Tempting But Inadequate Response

The team initially proposes:

- increase the timeout;
- clamp negative elapsed time to zero;
- use Unix time everywhere;
- synchronize more frequently;
- add another `time_valid` Boolean;
- ignore timestamps before synchronization;
- use the newest timestamp as truth;
- persist the monotonic counter;
- add retries.

Those fixes may be useful in some systems, but they do not identify the temporal dependency. They still hide different
temporal meanings behind one value.

### Principal Engineer Intervention

The Principal Engineer recasts the issue from "clock bug" to "multiple temporal semantics hidden behind one API."

The corrective model:

- inventory temporal decisions;
- name clock domains;
- use monotonic time for elapsed duration and timeout measurement;
- use UTC wall clock for calendar meaning and external records;
- represent wall-clock validity explicitly;
- define synchronization and correction behavior;
- define reboot and epoch semantics;
- define persisted expiration rules;
- specify timeout state after expiry;
- separate freshness from timestamp comparison;
- define ordering where wall clock is unreliable;
- inject controllable clocks into tests;
- record architectural decisions;
- expose diagnostics for clock source, domain, validity, and correction.

The point is not "always use monotonic time." The point is to choose and name the temporal dependency for each decision.

## 19. Expected Discussion Arc

1. **Time enters architecture through assumptions.**
   A time value is not neutral when behavior depends on it.
2. **One generic clock hides incompatible meanings.**
   Timeout, timestamp, freshness, cleanup, retry, ordering, and UI display need different semantics.
3. **Wall clock and monotonic time solve different problems.**
   Neither is universally correct.
4. **Duration, deadline, timestamp, freshness, and ordering are not interchangeable.**
   Mixing domains makes failures appear during reset, correction, and field timing.
5. **Timeouts define state transitions, not merely waiting.**
   Expiry must say what remains true and whether late completion or retry is safe.
6. **Reset and synchronization expose hidden clock assumptions.**
   A value written before time is valid may not mean what consumers think later.
7. **Periodic work needs drift and missed-period policy.**
   Schedules should say what happens when reality does not match the cadence.
8. **Multiple clocks add uncertainty and disagreement.**
   Devices can order events without agreeing on wall-clock time.
9. **Testability requires controllable time.**
   Tests must exercise jumps, drift, reset, wrap, invalid clocks, and late synchronization.
10. **Explicit temporal dependencies preserve predictable behavior.**
    Naming the clock and meaning makes future change safer.

These are intellectual progression points, not mandatory manuscript headings.

## 20. Law Applicability

The law applies when a system uses:

- timeouts;
- deadlines;
- retries;
- expiration;
- scheduling;
- periodic work;
- freshness;
- timestamps;
- event ordering;
- leases;
- watchdogs;
- clock synchronization;
- persisted temporal state;
- multiple devices or processors;
- long-running operation;
- reset recovery.

The law is proportional. Not every local delay needs an ADR. Review depth should grow with consequence, number of clock
domains, cross-component visibility, reset and persistence behavior, field lifetime, coordination cost, and failure
impact.

## 21. Law Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- wall clock is always wrong;
- monotonic time never resets;
- distributed clocks can be perfectly synchronized;
- all event order requires timestamps;
- all timeouts should be configurable;
- every timer needs dependency injection;
- every delay is an architectural issue;
- retries solve timeout failures;
- longer timeouts are safer;
- timestamp precision equals accuracy;
- NTP or GPS automatically makes time trustworthy;
- one central clock API is always sufficient;
- local time should be used for persisted records;
- UTC solves duration and monotonicity;
- a valid RTC proves data is fresh.

## 22. Violation Patterns

The future draft should make these violations visible:

- one `now()` used for incompatible purposes;
- wall clock used for elapsed-time measurement;
- timestamp used as causal order;
- timeout expiration with undefined resulting state;
- retry triggered without duplicate-operation or completion semantics;
- persisted deadline interpreted after reboot without a clock-validity rule;
- `time_valid` Boolean without ownership or lifecycle;
- periodic loop drifting silently;
- missed periods accumulating unlimited backlog;
- time correction breaking age calculations;
- clock wrap ignored;
- UI-local time leaking into storage or protocol semantics;
- test clocks that never jump, drift, wrap, or reset;
- multiple devices comparing timestamps without uncertainty rules.

## 23. Engineering Principle Target

Target principle for the future draft:

> Name the clock and the temporal meaning behind every consequential use of time. Use elapsed time, wall time, ordering,
> freshness, and deadlines deliberately rather than treating them as interchangeable.

The principle should imply review questions:

1. What temporal decision is being made?
2. Which clock domain supplies the value?
3. Is this duration, timestamp, deadline, ordering, or freshness?
4. Can the clock jump, drift, reset, wrap, or become invalid?
5. What happens after reboot?
6. What does timeout change in system state?
7. Can an operation complete after timeout?
8. Is retry safe?
9. How is uncertainty represented?
10. How is the behavior tested under clock changes?

## 24. Architecture Exercise Target

### Working Title

Trace One Temporal Decision

Ask the reader to choose one consequential use of time and document:

1. decision being made;
2. clock source;
3. clock domain;
4. temporal meaning;
5. units and resolution;
6. accuracy assumptions;
7. monotonicity;
8. validity;
9. drift;
10. wrap behavior;
11. reset behavior;
12. persistence behavior;
13. synchronization or correction behavior;
14. timeout or deadline semantics;
15. state after expiry;
16. retry implications;
17. ordering assumptions;
18. freshness rule;
19. diagnostics;
20. tests with controlled time;
21. ADR location.

The exercise must not create a new canonical PEAK artifact such as Time Map, Clock Ledger, Temporal Contract, Clock
Registry, or Time Authority Matrix. A chapter-local worksheet is acceptable if it uses existing records such as ADRs,
tests, diagnostics, and the Event Catalog.

## 25. Chapter-Local ADR Brief

### Working Title

Separate Monotonic Runtime Timing from Wall-Clock Time

### Context

- One generic clock API serves timeouts, timestamps, freshness, cleanup, and UI display.
- The RTC may be invalid during boot.
- Synchronization may move wall time.
- Monotonic time resets at reboot.
- Current behavior fails after reset and clock correction.

### Decision

- Use monotonic time for elapsed duration, timeout, retry interval, and runtime deadline measurement.
- Use UTC wall clock for calendar timestamps and persisted external records.
- Expose wall-clock validity explicitly.
- Define synchronization and correction behavior.
- Define reboot and epoch semantics.
- Define persisted expiration rules.
- Separate UI-local conversion from stored time.
- Provide controllable clock sources for tests.
- Expose diagnostics for clock domain and validity.

### Alternatives Considered

- Continue using wall clock everywhere.
- Use monotonic time everywhere.
- Persist the monotonic counter.
- Clamp clock jumps.
- Reject all time-dependent behavior until synchronization.
- Use an external controller as the only time source.
- Add a generic clock abstraction without semantic separation.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits:

- reliable elapsed-time behavior;
- explicit wall-clock validity;
- predictable reset behavior;
- testability;
- clearer diagnostics;
- reduced accidental coupling.

Costs:

- multiple time representations;
- explicit conversion boundaries;
- boot and synchronization state;
- migration of existing callers;
- more deliberate persistence rules;
- need for wrap-safe and epoch-aware logic.

The ADR is story-local and reader-facing. It must not become a repository-level ADR or a tutorial on ADR mechanics.

## 26. PEAK Concept Map

### Concepts Inspected

- `LAW-003` - Time Is a Dependency.
- `SMELL-004` - Hidden State.
- `SMELL-001` - Silent Coupling.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-001` - ADR.
- `RITUAL-001` - Architecture Review.
- `METRIC-003` - Discoverability.
- `VOCAB-001` - Change Radius.
- `FAILURE-002` - One Lost Packet.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-007` - Every Dependency Is a Decision.
- `METRIC-004` - API Stability.
- `ARTIFACT-003` - Decision Journal.

### Selected Concepts

- `LAW-003` - Time Is a Dependency: the chapter directly illustrates this law as the fourth law of Part II.
- `SMELL-004` - Hidden State: material because invalid clocks, stale timestamps, boot epochs, and hidden clock validity
  affect behavior when they are not visible through a clear model.
- `SMELL-001` - Silent Coupling: material because one generic `now()` couples consumers to unstated clock assumptions.
- `ARTIFACT-005` - Event Catalog: material because events need meanings, producers, consumers, ordering assumptions, and
  timing or freshness rules.
- `ARTIFACT-001` - ADR: material because separating wall-clock time from monotonic runtime timing is an architectural
  decision with consequences and alternatives.
- `METRIC-003` - Discoverability: material because future engineers must be able to find the clock source, domain,
  validity rule, timeout semantics, and reset behavior behind temporal decisions.

### Rejected Concepts

- `RITUAL-001` - Architecture Review: relevant because temporal decisions deserve review, but the chapter should not
  teach review mechanics or require a registered ritual edge.
- `VOCAB-001` - Change Radius: relevant when temporal assumptions spread, but the selected story can discuss spread
  without making Change Radius a primary support concept.
- `FAILURE-002` - One Lost Packet: relevant to ordering, retries, and protocol recovery, but the recommended story is
  centered on RTC validity, wall-clock correction, and mixed temporal meanings rather than a packet-loss failure story.
- `LAW-001` - Every State Has One Owner: clock validity and timeout state need ownership, but Chapter 10 must not retell
  the state-ownership law.
- `LAW-002` - Every API Is a Promise: timing can be observable API behavior, but Chapter 10 must not become another API
  contract chapter.
- `LAW-007` - Every Dependency Is a Decision: Chapter 10 applies this dependency framing to time, but a registered edge
  would blur the primary law mapping.
- `METRIC-004` - API Stability: relevant only when temporal behavior crosses an API boundary.
- `ARTIFACT-003` - Decision Journal: useful for smaller decisions, but the selected story should use ADR as the primary
  temporal-decision artifact.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as clock domain, time authority, temporal contract, freshness policy, timeout state, boot epoch, monotonic
deadline, clock health, and time review remain chapter-local prose unless a later Canon Review finds a stable reusable
gap.

## 27. Exact Proposed PEAK Relationships

Register `CHAPTER-010` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-010
  type: illustrates
  to: LAW-003

- from: CHAPTER-010
  type: illustrates
  to: SMELL-004

- from: CHAPTER-010
  type: illustrates
  to: SMELL-001

- from: CHAPTER-010
  type: references
  to: ARTIFACT-005

- from: CHAPTER-010
  type: references
  to: ARTIFACT-001

- from: CHAPTER-010
  type: references
  to: METRIC-003
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 28. Required Chapter Architecture

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

## 29. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A timestamp is not freshness.
- A timeout is a state decision.
- Clock validity is part of the contract.

These are semantic targets, not mandatory final wording.

## 30. Evidence and Technical Credibility Requirements

The future draft must be credible for embedded and long-lived systems. It should treat the following correctly:

- RTC validity and invalid startup time;
- monotonic timers and reset;
- wall-clock correction forward and backward;
- clock drift and wrap;
- elapsed time versus timestamp comparison;
- timeout expiry and late completion;
- retry safety after timeout;
- command freshness and stale data;
- persisted records and expiration after reboot;
- periodic scheduling drift, jitter, missed periods, and backlog;
- UI-local time versus stored UTC;
- ordering where wall-clock time is unreliable;
- multiple devices or processors with disagreeing clocks;
- diagnostics for clock source, validity, correction, and uncertainty;
- tests that control jumps, drift, wrap, invalidity, reset, and late synchronization.

The story should remain architecture-neutral unless a small illustrative detail is necessary. Do not require a specific
RTOS, MCU, network time protocol, cloud platform, database, product, or vendor.

## 31. Terminology and Precision Guardrails

Use temporal terms precisely:

- wall-clock time: human or calendar time that may jump, be corrected, or be invalid;
- monotonic time: non-decreasing measure appropriate for elapsed duration and runtime deadlines within a domain;
- duration: elapsed amount of time;
- timestamp: when something happened according to a clock;
- deadline: a time boundary by which something must happen;
- timeout: a relative wait bound and the state transition after expiry;
- freshness: whether data is valid enough for the decision being made;
- ordering: sequence or causality, which may not require wall-clock agreement;
- clock domain: the scope in which a time value has defined meaning, validity, and failure behavior.

The chapter must avoid these misleading statements:

- "Use monotonic time for everything."
- "Use UTC and the problem is solved."
- "If the RTC is valid, data is fresh."
- "A timestamp proves order."
- "A longer timeout is safer."
- "A timeout means the operation failed."
- "A retry is safe after timeout."
- "Clock synchronization removes uncertainty."
- "A generic clock abstraction solves semantics."
- "Tests with a steadily increasing clock cover temporal behavior."

## 32. Failure Modes to Avoid

The later draft must not become:

- a calendar, timezone, or date-format chapter;
- an RTOS timer tutorial;
- a distributed-consensus chapter;
- a generic testing tutorial;
- a timestamp arithmetic checklist;
- a broad observability chapter;
- a retelling of Chapter 7 state ownership;
- a retelling of Chapter 8 API promises;
- a retelling of Chapter 9 dependency choice;
- a speculative PEAK artifact proposal;
- a shallow ADR that says only "use monotonic time";
- a worksheet with no real architectural decision;
- reader-facing draft prose inside the canonical brief.

## 33. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete reset and clock-correction failure;
- the Principal Engineer move recasts the issue from a clock bug to unnamed temporal dependencies;
- wall clock and monotonic time are distinguished without dogmatism;
- duration, deadline, timestamp, ordering, timeout, retry, freshness, and periodic behavior are treated where relevant;
- reset, persistence, boot epoch, synchronization, correction, drift, and wrap are credible;
- timeout semantics include state after expiry and late completion;
- freshness is not reduced to timestamp existence;
- tests use controllable time and cover jumps, drift, wrap, invalid clocks, reset, and synchronization;
- diagnostics expose clock source, domain, validity, and correction where useful;
- the exercise can be applied to a real temporal decision;
- the ADR makes a genuine decision and acknowledges benefits and costs;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally;
- boundaries with Chapters 1-9, later Part II laws, and later parts are respected;
- claims are technically credible and reviewable.

## 34. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into programming-language, date/time, RTOS, or distributed-systems tutorials.

Canon Review should verify that the chapter illustrates `LAW-003`, materially uses the registered supporting concepts,
does not imply a new PEAK artifact or vocabulary term, and preserves the boundaries with Chapters 7, 8, and 9.

Technical Review should focus on wall-clock versus monotonic semantics, reset and persisted-time behavior, timeout
state, late completion, retry safety, freshness rules, periodic scheduling policy, clock correction, drift, wrap,
multi-device disagreement, diagnostics, and controlled-time testing.

Freeze Review should confirm that Chapter 10 continues Part II, keeps the manuscript architecture intact, uses exactly
three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the reader-facing manuscript in
canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
controller details, synchronization source, event names, retry examples, and final notebook wording while preserving the
time-dependency thesis, story shape, PEAK map, and chapter boundaries.

## 35. Final Scope Statement

Chapter 10 should define time as an architectural dependency. It should show an embedded controller whose generic
`now()` API hides incompatible temporal meanings, then guide the reader toward named clock domains, explicit validity,
monotonic elapsed-time measurement, wall-clock records, timeout state, freshness rules, reset semantics, controlled-time
tests, diagnostics, and an ADR that makes temporal assumptions discoverable without creating new PEAK canon.
