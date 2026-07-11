# Time Is a Dependency

## Opening Quote

> A timestamp tells you what a clock said. It does not tell you what the system may trust.

## Story

The controller had three kinds of time before anyone admitted it had one timing model.

It had an RTC that stored UTC. It had a monotonic hardware timer that started when the controller booted. It had a
network sync path that corrected wall-clock time after the device found connectivity. The design also had ordinary
features that needed time: persisted records with timestamps, command freshness checks, communication timeouts,
periodic cleanup, retry scheduling, and a local UI that displayed calendar time to technicians.

None of those features looked strange in isolation.

The record store needed to say when data was written. The communication task needed to stop waiting when a peer did not
answer. The command path needed to reject stale commands. The cleanup loop needed to delete expired records. The UI
needed to show a time a human could understand. Tests needed a way to advance time without waiting in real life.

So the platform team exposed a simple helper.

`now()`.

It returned the current UTC timestamp when the RTC had a value. During early boot it returned the last persisted RTC
value until synchronization completed. The monotonic timer was available elsewhere, but most code did not ask for it.
`now()` was easy, and it fit every call site well enough at first.

The first failures did not look related.

A field unit rebooted after a long power interruption. Its RTC came up stale. The network link took several minutes to
connect because the site gateway was also recovering. During that gap, the controller accepted a command that should
have been too old. The command carried a timestamp, the controller subtracted it from `now()`, and the age looked small.
The timestamp was not fresh. It only happened to be close to the controller's stale wall clock.

Another unit extended a communication timeout across the same kind of restart. The timeout had been calculated as
"expire at `now() + 30 seconds`" and persisted with the operation state. After reboot, the stale RTC made the deadline
appear farther away than it really was. In a later test, the opposite happened: network sync corrected the clock
backward while an operation was waiting, and the timeout did not expire when the engineer expected. A different build
corrected forward and expired immediately.

Records became hard to trust.

Some records looked as if they came from the future. Others were cleaned up as if they were old even though they had
just been written. The retry scheduler backed off in surprising ways. The UI and diagnostics disagreed about which
event happened first. A support engineer looking at logs saw a startup event after a communication failure, even though
the device had plainly rebooted before the failure was reported.

The test suite did not help much.

Its fake clock always moved forward. It never lost validity. It never corrected backward. It never drifted. It never
wrapped. It never rebooted with persisted records from a previous run. The tests proved that arithmetic worked when the
clock behaved like a polite counter. The field failure required reset followed by delayed synchronization and a
backward wall-clock correction.

The first fixes sounded practical.

"Increase the timeout."

"Clamp negative elapsed time to zero."

"Use Unix time everywhere."

"Synchronize more often."

"Add a `time_valid` flag."

"Ignore timestamps before sync."

"Trust the newest timestamp."

"Persist the monotonic counter."

"Add retries."

Each proposal solved one symptom in one path. None of them explained why the symptoms kept appearing in unrelated
modules.

The Principal Engineer asked the team to stop calling it a clock bug.

"We have one API that means different things to different callers."

The room got quieter because that sentence made the bug larger and more solvable at the same time.

The command path was not asking for the time. It was asking whether a command was fresh enough to execute. The
communication path was not asking for the date. It was measuring elapsed waiting time and deciding what state remained
after expiry. The record store needed wall-clock evidence for external interpretation. The cleanup loop needed an
expiration rule that survived reboot. The retry scheduler needed safe spacing between attempts. The UI needed local
display. Diagnostics needed to show both what the device believed and how valid that belief was.

Those were not the same dependency.

The team inventoried temporal decisions instead of searching for one better `now()`. They named the clock domains:
runtime monotonic time since boot, UTC wall-clock time after validation, persisted timestamps written under a known
clock state, server receipt time, and UI-local display time. They made elapsed runtime behavior use monotonic time.
Timeouts became relative waits measured on the runtime clock, with explicit state after expiry and rules for late
completion. UTC wall-clock time remained the stored calendar meaning for records that needed external interpretation,
but records also carried whether wall-clock time was valid when they were written.

They separated freshness from timestamp comparison.

A command was fresh only if the issuing source, transport delay assumptions, receipt path, clock validity, and maximum
acceptable age all satisfied the command rule. A timestamp alone did not make a command fresh. When the controller could
not prove the rule, it rejected the command or accepted it through an explicit degraded path.

They defined synchronization behavior.

When network sync corrected wall-clock time, elapsed timers did not move because they were not tied to wall clock.
Diagnostics recorded the correction. Persisted records kept their original clock domain and validity. Cleanup did not
delete records just because a corrected clock made an old assumption look new. Periodic work gained a policy: fixed-rate
where missed samples mattered, delay-after-completion where load mattered, and skipped periods where catching up would
create unsafe backlog.

They made reset part of the model.

The monotonic counter reset on boot. Runtime deadlines did not survive reboot as monotonic values. Persisted expiration
used wall-clock rules only after wall-clock validity was established, or it used product-specific ordering when validity
was absent. The system recorded a boot generation in diagnostics so engineers could distinguish one runtime timeline
from another.

The test harness changed last, and that is when the team learned the most.

Tests could now start with invalid wall-clock time, advance monotonic time, jump wall clock forward, jump it backward,
simulate drift, wrap a counter, reboot with persisted records, synchronize late, and complete an operation after timeout.
Several old assumptions failed immediately. That was useful evidence. The system had not become more complicated because
the tests were harder; the tests were finally exercising the complexity the field had already exposed.

The final ADR did not say, "Use monotonic time."

It said which decisions used monotonic runtime timing, which decisions used UTC wall-clock time, how wall-clock validity
was represented, what synchronization could change, what reset invalidated, how timeouts changed state, how late
completion was handled, which freshness rules did not rely on timestamps alone, and which diagnostics had to expose
clock source, domain, validity, correction, and uncertainty.

The controller still depended on time.

It stopped pretending time was one thing.

## Discussion

Any code that depends on timing depends on architecture.

That is `LAW-003`. It is easy to agree with in principle and easy to miss in code because time often arrives as a helper
function, a timestamp field, a delay call, a retry interval, or a scheduler setting. Those forms look small. The
assumptions behind them are not.

Every consequential use of time imports assumptions about clock source, accuracy, monotonicity, synchronization,
ordering, persistence, reset behavior, validity, and failure. Those assumptions are dependencies and must be designed
explicitly.

The trap is that the same value can look usable for several meanings.

A wall-clock timestamp can tell a human when a record was written. It cannot, by itself, prove elapsed duration. It
cannot prove causal order between devices whose clocks disagree. It cannot prove freshness unless the freshness rule
also knows clock validity, transport delay, sampling behavior, caching, update policy, and acceptable uncertainty.

A monotonic timer can measure elapsed time inside one runtime domain. It is a strong choice for timeouts and runtime
deadlines because it does not move backward when wall clock is corrected. It is not a calendar. It may reset at reboot,
wrap, lose power, or be meaningless outside the domain where it was measured. Persisting a monotonic value without its
runtime context does not create durable time.

Wall clock and monotonic time solve different problems.

Wall clock is useful when the system needs calendar meaning: external records, human diagnostics, audit trails, protocol
requirements, or UI display. Wall clock may jump forward, jump backward, be corrected after boot, be set by a human, be
invalid, drift, or disagree with another device.

Monotonic time is useful when the system needs elapsed measurement: waits, retries, runtime deadlines, watchdog windows,
and performance intervals inside a domain. It usually should not jump backward during one runtime, but it still has
failure behavior. It may reset. It may wrap. It may have limited resolution. It may not share meaning across processors
or devices.

The rule is not "wall clock bad, monotonic good."

The rule is: choose the clock and the temporal meaning before relying on the value.

One generic `now()` hides incompatible meanings. That is Silent Coupling (`SMELL-001`) in temporal form. Callers believe
they depend on a local utility. In practice, they depend on a clock domain, validity rule, correction policy, reset
behavior, and interpretation that may never have been named.

Hidden State (`SMELL-004`) appears when the system's behavior depends on invisible temporal facts. Is wall-clock time
valid? Was this timestamp written before synchronization? Did this deadline come from a previous boot? Has the counter
wrapped? Is this record from the current runtime or an earlier one? If those facts are not represented, the code will
infer them from a number that cannot carry the meaning alone.

The common temporal meanings are not interchangeable.

A duration answers how much time elapsed. A timestamp answers when something happened according to a clock. A deadline
defines a boundary by which something must happen. A timeout is a relative wait bound and the state transition after
expiry. Ordering defines sequence or causality. Freshness says whether data is valid enough for a decision.

Mixing those meanings creates failures that appear only under reset, correction, drift, wrap, load, or disagreement.

For example, a command timestamp is not freshness. A command may be too old even if its timestamp is near local wall
clock, because the local clock may be stale. A command may be acceptable without a trustworthy shared wall clock if it
arrives through an ordered session with a bounded delay and a product rule that defines validity. Freshness is a rule,
not a field.

Ordering also does not always require wall-clock time.

Events can be ordered by sequence numbers, accepted state transitions, event IDs, server receipt order, local monotonic
measurements, or protocol-specific rules. The Event Catalog (`ARTIFACT-005`) is useful here because events should say
what produced them, who consumes them, and what timing or ordering assumptions consumers may rely on. If an event's
timestamp is for human interpretation, say so. If consumers may use it for ordering or expiration, that is a stronger
commitment and should be designed as one.

Timeouts deserve special care because they look like small waits and behave like state transitions.

When a timeout expires, what changed? Did the operation fail, become unknown, remain canceling, or continue in the
background? Can it still complete after the timeout? If it completes late, is that completion ignored, reconciled, or
reported? Is retry safe? Could retry duplicate the original operation? Which clock measures the wait? What happens if
the system reboots while waiting?

Longer timeouts are not automatically safer. They can hide failure, extend stale state, slow recovery, and make tests
less representative. Shorter timeouts are not automatically better. They can create unnecessary retries, false failure,
and unsafe duplicate work. The right timeout is tied to the state being bounded and the consequence of being wrong.

Periodic work has the same problem in a different costume.

"Run every minute" may mean delay one minute after the previous run completes. It may mean run at fixed-rate boundaries.
It may mean skip missed periods after sleep. It may mean catch up until every missed period is processed. It may mean
merge missed periods into one run. It may tolerate jitter, or it may not. It may allow backlog, cap backlog, or treat
backlog as a fault.

Those choices are architecture when the work affects correctness, load, freshness, cleanup, retry behavior, or external
coordination. A cleanup job that silently catches up after a wall-clock jump may delete data too aggressively. A sensor
sampling loop that silently skips periods may hide data loss. A retry loop that catches up after connectivity returns
may flood a peer. A watchdog that uses the wrong clock may prove the wrong thing.

Reset exposes temporal assumptions because it breaks the illusion of one continuous timeline.

After reboot, a monotonic counter usually starts over. An RTC may be invalid, stale, or corrected later. Persisted data
may contain timestamps written under a different clock state. A deadline stored as an absolute wall-clock value may be
interpreted before wall clock is valid. A duration stored as a timestamp may become nonsense. A value that was safe in
RAM may not be safe after power loss.

Synchronization exposes another kind of assumption.

When wall-clock time is corrected, it can move forward or backward. Precision is not accuracy. A synchronized clock is
not automatically monotonic. A valid RTC does not prove data is fresh. A network time source can improve calendar
meaning while leaving elapsed runtime behavior unchanged. Multiple devices may each have reasonable clocks and still
disagree enough that timestamp comparison is unsafe.

Drift and wrap are not exotic details in long-lived systems.

A clock can slowly diverge from real time. A counter can overflow. A scheduler tick can have limited resolution. A
device can sleep. A processor can pause. A retained clock can survive one reset and not another. These facts matter
only where behavior depends on them, but where they matter, they must be visible.

Testability is part of the dependency.

If time is supplied only by the platform clock, tests can usually prove only the happy path where time moves forward at
normal speed. Consequential temporal behavior needs controllable clocks. Tests should be able to advance elapsed time,
jump wall clock forward and backward, start with invalid wall-clock time, synchronize late, simulate drift, force wrap,
reboot with persisted records, miss periodic intervals, and complete work after timeout.

This is not a broad testing doctrine. It is the evidence required when the architecture depends on time.

Diagnostics are also part of the design.

When time-related failures happen in the field, the system should reveal the clock source, clock domain, validity,
recent correction, uncertainty, boot generation where useful, and whether a timestamp was written before or after
synchronization. Without that, engineers will argue about arithmetic while the real problem remains hidden.

Discoverability (`METRIC-003`) matters because temporal assumptions age quietly. A future engineer may find a timeout
constant but not the state it bounds. They may find a timestamp but not whether it is a record time, receipt time, UI
display time, or expiration rule. They may find a clock helper but not whether it can jump, drift, reset, wrap, or lose
validity.

An ADR (`ARTIFACT-001`) is appropriate when a temporal decision shapes behavior across components, persistence, tests,
diagnostics, or product promises. The ADR does not need to invent a new artifact. It should record which clock and
meaning are being used, what alternatives were rejected, what failure behavior is accepted, and what evidence proves the
choice.

Time is a dependency because systems do not depend on numbers. They depend on what those numbers mean.

Make the meaning explicit.

## Engineering Principle

Name the clock and the temporal meaning behind every consequential use of time. Use elapsed time, wall time, ordering,
freshness, and deadlines deliberately rather than treating them as interchangeable.

This principle turns the law into review questions:

1. What temporal decision is being made?
2. Which clock domain supplies the value?
3. Is the value a duration, timestamp, deadline, ordering signal, freshness input, or display value?
4. Can the clock jump, drift, reset, wrap, or become invalid?
5. What happens after reboot?
6. What does timeout expiry change in system state?
7. Can the operation complete after timeout?
8. Is retry safe if the first operation later completes?
9. How is uncertainty represented?
10. How will tests control time enough to prove the behavior?

The point is not to make every delay architectural ceremony. The point is to make consequential temporal assumptions
reviewable before they become field behavior.

## Architecture Exercise

### Trace One Temporal Decision

Choose one consequential use of time in a system you know.

It may be a command freshness check, retry interval, timeout, periodic job, expiration rule, stored timestamp, lease,
watchdog, UI display, diagnostic event, or cleanup process.

Write short answers to these prompts:

1. What decision is being made?
2. What clock source supplies the value?
3. What clock domain gives that value meaning?
4. Is this duration, timestamp, deadline, timeout, ordering, freshness, or display?
5. What units and resolution matter?
6. What accuracy is assumed?
7. Must the clock be monotonic?
8. Can the clock be invalid?
9. Can it drift?
10. Can it wrap?
11. What happens after reset?
12. Is any value persisted?
13. What happens during synchronization or correction?
14. What does timeout or deadline expiry mean?
15. What state remains after expiry?
16. Can completion arrive late?
17. Is retry safe?
18. What ordering assumptions are consumers allowed to make?
19. What freshness rule is actually being enforced?
20. What diagnostics expose source, domain, validity, correction, and uncertainty?
21. Which tests control time enough to exercise jumps, drift, reset, wrap, invalidity, and late sync?
22. Where is the decision recorded?

End with this sentence:

The system depends on this time value as ______, and the value is trustworthy only when ______.

## Principal's Notebook

- A timestamp is not freshness.
- A timeout is a state decision.
- Clock validity is part of the contract.

## ADR

### Chapter ADR: Separate Monotonic Runtime Timing from Wall-Clock Time

### Context

The embedded controller uses one generic `now()` API for timeouts, timestamps, command freshness, cleanup, retry
scheduling, diagnostics, and UI display.

The device has an RTC that stores UTC, a monotonic hardware timer that starts at boot, and network synchronization that
may correct wall-clock time after connectivity begins. The RTC may be invalid or stale during boot. Wall-clock
correction may move time forward or backward. Monotonic time is useful for elapsed runtime behavior but resets at reboot.

Field failures have appeared after reset followed by delayed synchronization. Commands can be accepted as fresh when
they are stale. Runtime timeouts can extend or expire unexpectedly. Persisted records can appear to come from the
future. Cleanup and retry scheduling can behave differently depending on clock correction. Tests have not covered these
cases because their clock only moves forward.

### Decision

Separate monotonic runtime timing from UTC wall-clock time.

Use monotonic runtime time for elapsed duration, timeout measurement, retry spacing, watchdog windows, and runtime
deadlines inside one boot. Do not persist monotonic deadlines as durable calendar meaning.

Use UTC wall-clock time for persisted records, external timestamps, and diagnostics that need calendar interpretation.
Store whether wall-clock time was valid when a record was written when that validity affects later behavior. Keep
UI-local time as display conversion, not storage or protocol meaning.

Represent wall-clock validity explicitly. Define what behavior is allowed before synchronization, what changes when
synchronization completes, and how forward or backward correction affects existing records and decisions.

Define reset behavior. Runtime deadlines expire or are reconstructed according to product rules after reboot; they are
not interpreted as if the previous monotonic timeline still exists. Persisted expiration uses wall-clock rules only when
wall-clock validity is sufficient, or it uses a product ordering rule that does not require trustworthy wall clock.

Define timeout state. Expiry moves the operation to a named state. Late completion is either ignored, reconciled, or
reported according to the operation contract. Retry safety is decided before retry is allowed.

Define freshness separately from timestamp comparison. Command freshness depends on source, transport assumptions,
clock validity, receipt behavior, maximum acceptable age, and uncertainty.

Provide controllable clocks in tests. Tests must cover invalid startup time, wall-clock jumps forward and backward,
drift, wrap, reset, late synchronization, missed periods, and completion after timeout.

Expose diagnostics for clock source, domain, validity, recent correction, uncertainty, and runtime generation where
those facts affect interpretation.

### Consequences

Elapsed-time behavior no longer changes when wall-clock time is corrected. Timeouts become state decisions rather than
arithmetic around one timestamp. Persisted records become more honest because they carry enough context for later
interpretation. Freshness checks can reject uncertain data instead of trusting a nearby timestamp. Tests can reproduce
the field failures that previously required reset and delayed synchronization.

The design is more explicit. Callers must choose a temporal meaning instead of calling one helper. The integration layer
must maintain more than one clock representation. Existing call sites must be migrated. Diagnostics become richer.
Some persisted data may need versioned interpretation. The team must keep wall-clock validity and synchronization state
owned rather than treating them as incidental platform facts.

The decision does not make time simple. It makes the dependency visible enough to reason about.

### Alternatives Considered

Continue using wall clock everywhere. This preserves the simple API, but elapsed runtime behavior changes when wall
clock is corrected, invalid, stale, or reset.

Use monotonic time everywhere. This improves elapsed measurement, but it loses calendar meaning, cannot directly support
external records, and does not survive reboot as durable time.

Persist the monotonic counter. This treats a boot-relative value as if it were durable. It fails when the counter resets,
wraps, loses power, or changes meaning across runtime generations.

Clamp clock jumps. This hides negative arithmetic in some paths, but it does not define freshness, ordering, timeout
state, persistence, or synchronization behavior.

Reject all time-dependent behavior until synchronization. This may be appropriate for some commands, but it can block
safe local behavior and still does not define elapsed runtime timing after synchronization.

Add a generic clock abstraction. This may help tests, but an abstraction without semantic separation can preserve the
same confusion behind a cleaner interface.

## Editor's Commentary

Chapter 10 continues the Part II laws by taking one kind of dependency from Chapter 9 and giving it its own shape.

Chapter 7 owns the question of state authority. This chapter may ask who owns clock validity, timeout state, and
freshness state, but it does not retell the ownership law. Chapter 8 owns API promises. This chapter may note that
timing and timeout behavior can become observable promises, but it does not become another API chapter. Chapter 9 owns
the broader idea that dependencies import behavior and replacement cost. This chapter applies that reasoning to time.

The chapter deliberately avoids becoming a date and time programming guide, an RTOS timer tutorial, a distributed
ordering chapter, a general observability chapter, or a testing methodology chapter. Those topics matter only where they
clarify temporal dependency.

The PEAK concepts carrying the chapter are Time Is a Dependency (`LAW-003`), Hidden State (`SMELL-004`), Silent Coupling
(`SMELL-001`), Event Catalog (`ARTIFACT-005`), ADR (`ARTIFACT-001`), and Discoverability (`METRIC-003`). They are enough.
The chapter does not need a new clock registry, time authority artifact, freshness policy concept, or temporal contract
to teach the law.

The reader-facing move is small and durable: before relying on time, name which time you mean.
