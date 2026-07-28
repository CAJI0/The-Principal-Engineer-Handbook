# Час — це залежність

## Вступна цитата

> Timestamp каже, що сказав clock. Він не каже, чому system may trust.

## Історія

Controller мав три види time before anyone admitted design had one timing model.

У ньому був RTC, що зберігав UTC, monotonic hardware timer, який стартував під час boot, і шлях network sync, що коригував wall-clock time після появи connectivity. Функціям теж потрібен був час: persisted records, перевірки freshness команд, communication timeouts, periodic cleanup, retry scheduling і local UI display.

Platform team відкрила простий helper: `now()`.

Він повертав current UTC, коли RTC виглядав придатним. Під час early boot він повертав last persisted RTC value, доки synchronization не завершувалася. Monotonic timer існував окремо, але більшість коду його не просила. `now()` був зручним і достатньо добре підходив кожному call site, бо callers не мусили казати, який саме вид часу вони мають на увазі.

Failures виглядали не повʼязаними. Field unit rebooted після тривалого power interruption. RTC повернувся stale. Network підключалася кілька хвилин. У цей проміжок controller прийняв command, яка мала бути надто старою, бо command timestamp виявився близьким до stale `now()`.

Another unit extended communication timeout across restart. Timeout had been calculated as "expire at `now() + 30 seconds`" and persisted with operation state, so runtime wait became wall-clock timestamp. After reboot stale RTC made deadline appear farther away. Later network sync corrected clock backward and timeout did not expire when expected; another build corrected forward and expired immediately.

Records стало важко довіряти: future records, premature cleanup, дивна поведінка retry delay, розбіжність UI і diagnostics, logs із неможливим порядком.

Tests не допомогли. Fake clock завжди рухався вперед, ніколи не втрачав validity, не коригувався назад, не drifted, не wrapped і не rebooted разом із persisted records. Tests доводили арифметику, коли clock поводився як чемний counter. Field failure вимагав reset, delayed sync і backward wall-clock correction.

First fixes solved symptoms: increase timeout, clamp negative elapsed time, use Unix time everywhere, sync more often, add `time_valid`, ignore timestamps before sync, trust newest timestamp, persist monotonic counter.

Principal Engineer переформулював проблему: «У нас є один API, який означає різні речі для різних callers».

Command path не питав «котра година»; він питав, чи command достатньо fresh. Communication path вимірював elapsed waiting і state after expiry. Record store потребував wall-clock evidence. Cleanup потребував expiration, що переживає reboot. Retry scheduler потребував safe spacing. UI потребував local display. Diagnostics потребували і того, що device вважав часом, і того, наскільки valid була ця belief.

Це були не одна й та сама dependency.

Команда inventoried temporal decisions. Вона назвала clock domains: runtime monotonic time since boot, UTC wall-clock time after validation, persisted timestamps written under known clock state, server receipt time, UI-local display time. Elapsed runtime behavior used monotonic time. Timeouts became relative waits measured on runtime clock, with explicit state after expiry and late-completion rules. UTC wall-clock remained stored calendar meaning for externally interpreted records, but records carried whether wall-clock time was valid when written.

Freshness відділили від timestamp comparison. Command була fresh лише тоді, коли source, transport delay assumptions, receipt path, clock validity і maximum acceptable age задовольняли command rule. Сам timestamp не робив command fresh.

Synchronization behavior визначили явно. Wall-clock correction не рухала elapsed timers. Diagnostics записували correction. Persisted records зберігали original clock domain і validity. Cleanup не видаляв records лише тому, що corrected clock змінив assumption. Periodic work отримав policy: fixed-rate там, де missed samples важливі; delay-after-completion там, де важливе load; skipped periods там, де catch-up створив би unsafe backlog.

Reset став частиною моделі. Monotonic counter reset on boot. Runtime deadlines не переживали reboot як monotonic values. Persisted expiration використовував wall-clock rules лише після validity або product-specific ordering, коли validity не було. Boot generation увійшов у diagnostics.

Tests змінилися й стали корисними: invalid wall-clock startup, monotonic advance, wall-clock jumps, drift, wrap, reboot with persisted records, late sync, late completion after timeout.

Final ADR не казав просто «Use monotonic time». Він записував, які decisions використовують monotonic runtime timing, які використовують UTC wall-clock time, як представлена validity, що змінює sync, що invalidates reset, як timeouts змінюють state, як обробляється late completion, які freshness rules не покладаються тільки на timestamps, і які diagnostics потрібні.

Controller і далі залежав від time. Він перестав удавати, що time — це одна річ.

## Обговорення

Будь-який code, що залежить від timing, залежить від architecture.

Це `LAW-003`. Time часто приходить як helper function, timestamp field, delay call, retry interval або scheduler setting. Форми виглядають малими; assumptions — ні.

Кожне consequential use of time приносить assumptions про clock source, accuracy, monotonicity, synchronization, ordering, persistence, reset behavior, validity і failure. Ці assumptions є dependencies, і їх треба проектувати явно.

Одне й те саме число може виглядати придатним для кількох meaning. Wall-clock timestamp може сказати людині, коли record був written. Сам по собі він не доводить elapsed duration, causal order або freshness. Monotonic timer вимірює elapsed time всередині одного runtime domain. Він сильний для timeouts і runtime deadlines, бо wall-clock correction його не рухає, але він не є calendar і може reset, wrap або бути meaningless outside domain.

Правило не в тому, що «wall clock bad, monotonic good». Правило таке: оберіть clock і temporal meaning до того, як покладатися на value.

Один generic `now()` hides incompatible meanings. Це Silent Coupling (`SMELL-001`) у temporal form. Hidden State (`SMELL-004`) appears, коли behavior depends on invisible temporal facts: wall-clock validity, timestamp before sync, previous boot deadline, counter wrap, runtime generation.

Common temporal meanings are not interchangeable: duration, timestamp, deadline, timeout, ordering, freshness, display. Command timestamp — не freshness. Freshness — rule, not a field.

Ordering не завжди requires wall-clock time. Events можуть be ordered by sequence numbers, accepted transitions, event IDs, server receipt order, local monotonic measurements або protocol rules. Event Catalog (`ARTIFACT-005`) can record producer, consumers і timing/ordering assumptions.

Timeouts — це state transitions. Коли timeout expires, operation failed, became unknown, remained canceling чи continued in background? Can it complete late? Is late completion ignored, reconciled або reported? Is retry safe? Which clock measures wait? What happens after reboot?

Periodic work також needs policy: delay-after-completion, fixed-rate, skip missed periods, catch up, merge, tolerate jitter, cap backlog або fault backlog.

Reset exposes assumptions. Monotonic starts over, RTC may be invalid або corrected later, persisted data may contain timestamps from different clock state, absolute wall-clock deadline may be interpreted before clock valid.

Synchronization може move time forward or backward. Precision — не accuracy. Valid RTC does not prove data fresh. Multiple devices можуть have reasonable clocks and still disagree enough that comparison unsafe.

Drift і wrap matter in long-lived systems. Testability — part of dependency: tests need controllable clocks to advance elapsed time, jump wall clock, start invalid, sync late, simulate drift, force wrap, reboot, miss periods і complete after timeout.

Diagnostics — part of design. Field failures should reveal clock source, domain, validity, correction, uncertainty, boot generation і whether timestamp was written before or after sync.

Discoverability (`METRIC-003`) matters, бо temporal assumptions age quietly. ADR (`ARTIFACT-001`) appropriate, коли temporal decision shapes behavior across components, persistence, tests, diagnostics або product promises.

Time — dependency, бо systems depend не лише on numbers, а on what those numbers mean.

## Інженерний принцип

Name the clock і temporal meaning behind every consequential use of time. Use elapsed time, wall time, ordering, freshness і deadlines deliberately.

Питання для review:

1. Яке temporal decision приймається?
2. Який clock domain supplies the value?
3. Це duration, timestamp, deadline, ordering signal, freshness input чи display value?
4. Чи може clock jump, drift, reset, wrap або become invalid?
5. Що відбувається після reboot?
6. Що timeout expiry змінює в system state?
7. Чи може operation complete after timeout?
8. Чи retry safe, якщо перша operation later completes?
9. Як represented uncertainty?
10. Як tests control time enough to prove behavior?

## Архітектурна вправа

### Простежте одне temporal decision

Оберіть один consequential use of time: command freshness check, retry interval, timeout, periodic job, expiration rule, stored timestamp, lease, watchdog, UI display, diagnostic event або cleanup process.

1. Яке decision приймається?
2. Яке clock source supplies value?
3. Який clock domain дає value meaning?
4. Це duration, timestamp, deadline, timeout, ordering, freshness чи display?
5. Які units і resolution важливі?
6. Яка accuracy assumed?
7. Чи має clock бути monotonic?
8. Чи може clock бути invalid?
9. Чи може він drift?
10. Чи може він wrap?
11. Що відбувається після reset?
12. Чи persisted якесь value?
13. Що відбувається під час synchronization або correction?
14. Що означає timeout або deadline expiry?
15. Який state лишається після expiry?
16. Чи може completion arrive late?
17. Чи retry safe?
18. Які ordering assumptions можуть робити consumers?
19. Яке freshness rule enforced?
20. Які diagnostics expose source, domain, validity, correction, uncertainty?
21. Які tests control time enough to exercise jumps, drift, reset, wrap, invalidity і late sync?
22. Де recorded decision?

Завершіть реченням:

The system depends on this time value as ______, and the value is trustworthy only when ______.

## Нотатник Principal Engineer

- A timestamp is not freshness.
- A timeout is a state decision.
- Clock validity is part of the contract.

## ADR

### Chapter ADR: Separate Monotonic Runtime Timing from Wall-Clock Time

### Context

Embedded controller використовує one generic `now()` API для timeouts, timestamps, command freshness, cleanup, retry scheduling, diagnostics і UI display. Device має RTC storing UTC, monotonic hardware timer starting at boot і network synchronization, що may correct wall-clock after connectivity. RTC may be invalid або stale during boot. Wall-clock correction may move time forward or backward. Monotonic time useful for elapsed runtime behavior, але resets at reboot.

Field failures appeared після reset followed by delayed synchronization.

### Decision

Separate monotonic runtime timing від UTC wall-clock time.

Use monotonic runtime time для elapsed duration, timeout measurement, retry spacing, watchdog windows і runtime deadlines inside one boot. Do not persist monotonic deadlines as durable calendar meaning.

Use UTC wall-clock для persisted records, external timestamps і diagnostics needing calendar interpretation. Store whether wall-clock was valid when record was written там, де validity affects later behavior. Keep UI-local time as display conversion.

Represent wall-clock validity explicitly. Define behavior before synchronization, changes after synchronization і effects of forward/backward correction. Define reset behavior, timeout state, late completion, retry safety, freshness separate from timestamp comparison, controllable clocks in tests і diagnostics.

### Consequences

Elapsed-time behavior більше не змінюється, коли wall-clock corrected. Timeouts become state decisions. Persisted records carry context. Freshness checks reject uncertainty. Tests can reproduce field failures.

Design стає more explicit. Callers choose temporal meaning. Multiple clock representations must be maintained. Existing call sites migrate. Some persisted data may need versioned interpretation.

### Alternatives Considered

Continue using wall clock everywhere. Simple API, але wrong elapsed behavior under correction.

Use monotonic time everywhere. Better elapsed measurement, але loses calendar meaning and durable time.

Persist monotonic counter. Це treats boot-relative value as durable.

Clamp clock jumps. Це hides arithmetic without defining semantics.

Reject all time-dependent behavior until synchronization. Може block safe local behavior і still not define elapsed runtime timing.

Add generic clock abstraction. Helps tests, але without semantic separation preserves confusion.

## Коментар редактора

Chapter 10 бере одну dependency з Chapter 9 і дає їй власну форму. Він не переказує ownership, API, dependency, observability або testing chapters. Reader-facing move малий і міцний: before relying on time, name which time you mean.

PEAK concepts цього chapter: Time Is a Dependency (`LAW-003`), Hidden State (`SMELL-004`), Silent Coupling (`SMELL-001`), Event Catalog (`ARTIFACT-005`), ADR (`ARTIFACT-001`) і Discoverability (`METRIC-003`).
