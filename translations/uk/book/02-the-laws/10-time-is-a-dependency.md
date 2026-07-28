# Час — це залежність

## Вступна цитата

> Timestamp каже, що сказав clock. Він не каже, чому system may trust.

## Історія

Controller мав три види time before anyone admitted design had one timing model.

It had RTC storing UTC, monotonic hardware timer starting at boot, and network sync path correcting wall-clock time after connectivity. Features needed time too: persisted records, command freshness checks, communication timeouts, periodic cleanup, retry scheduling, and local UI display.

Platform team exposed simple helper: `now()`.

It returned current UTC when RTC looked usable. During early boot it returned last persisted RTC value until synchronization completed. Monotonic timer existed elsewhere, but most code did not ask for it. `now()` was easy and fit every call site well enough because callers did not have to say which kind of time they meant.

Failures looked unrelated. A field unit rebooted after long power interruption. RTC came stale. Network took minutes to connect. During gap controller accepted a command that should have been too old because command timestamp compared close to stale `now()`.

Another unit extended communication timeout across restart. Timeout had been calculated as "expire at `now() + 30 seconds`" and persisted with operation state, so runtime wait became wall-clock timestamp. After reboot stale RTC made deadline appear farther away. Later network sync corrected clock backward and timeout did not expire when expected; another build corrected forward and expired immediately.

Records became hard to trust: future records, premature cleanup, strange retry delay behavior, UI and diagnostics disagreement, logs with impossible order.

Tests did not help. Fake clock always moved forward, never lost validity, never corrected backward, never drifted, never wrapped, never rebooted with persisted records. Tests proved arithmetic when clock behaved like polite counter. Field failure required reset, delayed sync, and backward wall-clock correction.

First fixes solved symptoms: increase timeout, clamp negative elapsed time, use Unix time everywhere, sync more often, add `time_valid`, ignore timestamps before sync, trust newest timestamp, persist monotonic counter.

Principal Engineer recast it: "We have one API that means different things to different callers."

Command path was not asking for time; it asked whether command was fresh enough. Communication path measured elapsed waiting and state after expiry. Record store needed wall-clock evidence. Cleanup needed expiration surviving reboot. Retry scheduler needed safe spacing. UI needed local display. Diagnostics needed both what device believed and how valid that belief was.

Those were not same dependency.

Team inventoried temporal decisions. They named clock domains: runtime monotonic time since boot, UTC wall-clock time after validation, persisted timestamps written under known clock state, server receipt time, UI-local display time. Elapsed runtime behavior used monotonic time. Timeouts became relative waits measured on runtime clock, with explicit state after expiry and late-completion rules. UTC wall-clock remained stored calendar meaning for externally interpreted records, but records carried whether wall-clock time was valid when written.

Freshness separated from timestamp comparison. A command was fresh only if source, transport delay assumptions, receipt path, clock validity, and maximum acceptable age satisfied command rule. Timestamp alone did not make command fresh.

Synchronization behavior defined. Wall-clock correction did not move elapsed timers. Diagnostics recorded correction. Persisted records kept original clock domain and validity. Cleanup did not delete records merely because corrected clock changed assumption. Periodic work gained policy: fixed-rate where missed samples matter, delay-after-completion where load matters, skipped periods where catch-up would create unsafe backlog.

Reset became part of model. Monotonic counter reset on boot. Runtime deadlines did not survive reboot as monotonic values. Persisted expiration used wall-clock rules only after validity or product-specific ordering when validity absent. Boot generation entered diagnostics.

Tests changed and became useful: invalid wall-clock startup, monotonic advance, wall-clock jumps, drift, wrap, reboot with persisted records, late sync, late completion after timeout.

Final ADR did not say "Use monotonic time." It recorded which decisions used monotonic runtime timing, which used UTC wall-clock time, how validity represented, what sync changes, what reset invalidates, how timeouts change state, how late completion handled, which freshness rules do not rely on timestamps alone, and diagnostics required.

Controller still depended on time. It stopped pretending time was one thing.

## Обговорення

Any code that depends on timing depends on architecture.

That is `LAW-003`. Time often arrives as helper function, timestamp field, delay call, retry interval, or scheduler setting. Forms look small; assumptions are not.

Every consequential use of time imports assumptions about clock source, accuracy, monotonicity, synchronization, ordering, persistence, reset behavior, validity, and failure. Those assumptions are dependencies and must be designed explicitly.

Same number can look usable for several meanings. Wall-clock timestamp can tell human when record was written. It cannot by itself prove elapsed duration, causal order, or freshness. Monotonic timer measures elapsed time inside one runtime domain. It is strong for timeouts and runtime deadlines because wall clock correction does not move it, but it is not calendar and may reset, wrap, or be meaningless outside domain.

Rule is not "wall clock bad, monotonic good." Rule is: choose clock and temporal meaning before relying on value.

One generic `now()` hides incompatible meanings. That is Silent Coupling (`SMELL-001`) in temporal form. Hidden State (`SMELL-004`) appears when behavior depends on invisible temporal facts: wall-clock validity, timestamp before sync, previous boot deadline, counter wrap, runtime generation.

Common temporal meanings are not interchangeable: duration, timestamp, deadline, timeout, ordering, freshness, display. A command timestamp is not freshness. Freshness is a rule, not a field.

Ordering does not always require wall-clock time. Events can be ordered by sequence numbers, accepted transitions, event IDs, server receipt order, local monotonic measurements, or protocol rules. Event Catalog (`ARTIFACT-005`) can record producer, consumers, and timing/ordering assumptions.

Timeouts are state transitions. When timeout expires, did operation fail, become unknown, remain canceling, or continue in background? Can it complete late? Is late completion ignored, reconciled, or reported? Is retry safe? Which clock measures wait? What happens after reboot?

Periodic work also needs policy: delay-after-completion, fixed-rate, skip missed periods, catch up, merge, tolerate jitter, cap backlog, or fault backlog.

Reset exposes assumptions. Monotonic starts over, RTC may be invalid or corrected later, persisted data may contain timestamps from different clock state, absolute wall-clock deadline may be interpreted before clock valid.

Synchronization can move time forward or backward. Precision is not accuracy. Valid RTC does not prove data fresh. Multiple devices can have reasonable clocks and still disagree enough that comparison unsafe.

Drift and wrap matter in long-lived systems. Testability is part of dependency: tests need controllable clocks to advance elapsed time, jump wall clock, start invalid, sync late, simulate drift, force wrap, reboot, miss periods, and complete after timeout.

Diagnostics are part of design. Field failures should reveal clock source, domain, validity, correction, uncertainty, boot generation, and whether timestamp was written before or after sync.

Discoverability (`METRIC-003`) matters because temporal assumptions age quietly. ADR (`ARTIFACT-001`) is appropriate when temporal decision shapes behavior across components, persistence, tests, diagnostics, or product promises.

Time is a dependency because systems depend not on numbers alone, but on what those numbers mean.

## Інженерний принцип

Name the clock and temporal meaning behind every consequential use of time. Use elapsed time, wall time, ordering, freshness, and deadlines deliberately.

Review questions:

1. What temporal decision is being made?
2. Which clock domain supplies the value?
3. Is value duration, timestamp, deadline, ordering signal, freshness input, or display value?
4. Can clock jump, drift, reset, wrap, or become invalid?
5. What happens after reboot?
6. What does timeout expiry change in system state?
7. Can operation complete after timeout?
8. Is retry safe if first operation later completes?
9. How is uncertainty represented?
10. How will tests control time enough to prove behavior?

## Архітектурна вправа

### Простежте одне temporal decision

Choose one consequential use of time: command freshness check, retry interval, timeout, periodic job, expiration rule, stored timestamp, lease, watchdog, UI display, diagnostic event, or cleanup process.

1. What decision is being made?
2. What clock source supplies value?
3. What clock domain gives value meaning?
4. Is this duration, timestamp, deadline, timeout, ordering, freshness, or display?
5. What units and resolution matter?
6. What accuracy assumed?
7. Must clock be monotonic?
8. Can clock be invalid?
9. Can it drift?
10. Can it wrap?
11. What happens after reset?
12. Is any value persisted?
13. What happens during synchronization or correction?
14. What does timeout or deadline expiry mean?
15. What state remains after expiry?
16. Can completion arrive late?
17. Is retry safe?
18. What ordering assumptions may consumers make?
19. What freshness rule is enforced?
20. What diagnostics expose source, domain, validity, correction, uncertainty?
21. Which tests control time enough to exercise jumps, drift, reset, wrap, invalidity, and late sync?
22. Where is decision recorded?

End with:

The system depends on this time value as ______, and the value is trustworthy only when ______.

## Нотатник Principal Engineer

- A timestamp is not freshness.
- A timeout is a state decision.
- Clock validity is part of the contract.

## ADR

### Chapter ADR: Separate Monotonic Runtime Timing from Wall-Clock Time

### Context

Embedded controller uses one generic `now()` API for timeouts, timestamps, command freshness, cleanup, retry scheduling, diagnostics, and UI display. Device has RTC storing UTC, monotonic hardware timer starting at boot, and network synchronization that may correct wall-clock after connectivity. RTC may be invalid or stale during boot. Wall-clock correction may move time forward or backward. Monotonic time is useful for elapsed runtime behavior but resets at reboot.

Field failures appeared after reset followed by delayed synchronization.

### Decision

Separate monotonic runtime timing from UTC wall-clock time.

Use monotonic runtime time for elapsed duration, timeout measurement, retry spacing, watchdog windows, and runtime deadlines inside one boot. Do not persist monotonic deadlines as durable calendar meaning.

Use UTC wall-clock for persisted records, external timestamps, and diagnostics needing calendar interpretation. Store whether wall-clock was valid when record was written where validity affects later behavior. Keep UI-local time as display conversion.

Represent wall-clock validity explicitly. Define behavior before synchronization, changes after synchronization, and effects of forward/backward correction. Define reset behavior, timeout state, late completion, retry safety, freshness separate from timestamp comparison, controllable clocks in tests, and diagnostics.

### Consequences

Elapsed-time behavior no longer changes when wall-clock corrected. Timeouts become state decisions. Persisted records carry context. Freshness checks reject uncertainty. Tests can reproduce field failures.

Design is more explicit. Callers choose temporal meaning. Multiple clock representations must be maintained. Existing call sites migrate. Some persisted data may need versioned interpretation.

### Alternatives Considered

Continue using wall clock everywhere. Simple API, wrong elapsed behavior under correction.

Use monotonic time everywhere. Better elapsed measurement, loses calendar meaning and durable time.

Persist monotonic counter. Treats boot-relative value as durable.

Clamp clock jumps. Hides arithmetic without defining semantics.

Reject all time-dependent behavior until synchronization. May block safe local behavior and still not define elapsed runtime timing.

Add generic clock abstraction. Helps tests but without semantic separation preserves confusion.

## Коментар редактора

Chapter 10 takes one dependency from Chapter 9 and gives it its own shape. It does not retell ownership, API, dependency, observability, or testing chapters. The reader-facing move is small and durable: before relying on time, name which time you mean.

The PEAK concepts carrying the chapter are Time Is a Dependency (`LAW-003`), Hidden State (`SMELL-004`), Silent Coupling (`SMELL-001`), Event Catalog (`ARTIFACT-005`), ADR (`ARTIFACT-001`), and Discoverability (`METRIC-003`).
