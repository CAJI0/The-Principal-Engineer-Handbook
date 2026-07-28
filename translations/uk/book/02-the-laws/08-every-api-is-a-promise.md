# Кожен API - це обіцянка

## Вступна цитата

> Signature каже, як викликати. Promise каже, чому можна довіряти.

## Історія

Radio team думала, що зберегла interface.

Function name лишилася та сама. Parameter той самий. Return type той самий. Every caller still compiled.

```c
status_t radio_set_channel(uint8_t channel);
```

Саме це було аргументом на review: public header не змінився, command identifier не змінився, packet format не змінився, і жодному consumer не треба оновлювати build. Radio service переписали, бо стара implementation блокувала, доки hardware settles. Нова implementation queued the work, щоб інші tasks могли keep running.

Зміна виглядала як implementation improvement.

Перший failure не виглядав як API failure. Service application повідомив, що device перейшов на channel 17. Operator побачив displayed new value і запустив diagnostic capture. Capture повернувся empty. Device still transmitting on old channel, бо hardware operation ще не completed.

Service application не брехав. Він reported what the call had returned.

Другий failure прийшов із retry logic. Supervisory task побачив temporary radio-unavailable error і retried the call. У старій implementation retry після такого error зазвичай означав, що original operation had not started. У новій implementation перший request уже був accepted into the queue. Retry created a second channel-change request. Іноді requests collapsed into same final channel. Іноді вони interleaved with a scan request і залишали diagnostics attached to wrong assumption.

Третій failure прийшов після reset.

Radio service restored last requested channel from persistent storage. Hardware ще потребував calibration before it could apply that channel. Service tool displayed restored channel as current, бо old API так поводився after restart. Manufacturing tooling used displayed value to choose test path. Test failed intermittently, а logs made the radio look unreliable.

Стара implementation несла більше meaning, ніж визнавала signature.

Callers learned that successful return meant hardware had applied the channel. They learned that invalid input left prior channel unchanged. They learned callbacks arrived before function returned. They learned repeated calls with same channel were harmless. They learned what different failures meant, which task contexts were safe, and what persisted channel after reset represented.

Частина цього була documented. Частина була в tests. Частина - в examples. Частина - only in memory of service engineers and manufacturing scripts.

Усе це стало part of the promise.

Team proposed local fixes: delay UI before reporting channel, add version number, optional callback, tell callers to wait for telemetry, keep old function name, make supervisor retry carefully, add note that implementation is asynchronous.

Жодна зміна не відповідала на shared question:

What does `radio_set_channel()` promise now?

Principal Engineer попросила записати old promise before approving new implementation. Не signature. Не module name. Promise.

Команда записала, на що consumers relied:

- які channel values accepted;
- when hardware considered changed;
- what success meant;
- what each error meant;
- which calls could be repeated safely;
- which task contexts could call the function;
- when callbacks were delivered;
- who owned callback data;
- what persisted state meant after reset;
- how consumer could tell request acceptance from operation completion.

Цей список змінив conversation.

Нова implementation не мусила бути rejected. Queuing hardware work was reasonable. Проблема була в тому, що команда змінила completion semantics while preserving old shape. Old API promised "channel applied". New implementation returned after "request accepted".

Це різні promises.

Team split behavior. Old function лишився compatibility path for migration window. New request-oriented API made acceptance explicit. Completion arrived through named event with defined ordering and callback context. Error codes separated invalid input, rejected request, queued request, unavailable radio, and failed application. Repeated requests got documented result. Persistence recorded last requested channel and last applied channel separately, бо це were not the same fact.

Tests changed too. Unit test checking return code was still useful, but not enough. Integration tests checked UI state did not report applied hardware before completion. Supervisory retry tests checked duplicate requests. Reset tests checked whether restored state meant requested, applied, or unknown. Service-tool tests checked which errors should be retried and which should be shown to the operator.

Header had hidden a contract. Failure made it visible.

Final decision was not "never make APIs asynchronous." More precise: when an API crosses a meaningful boundary, observable behavior is the contract. If that behavior changes, architecture has changed even when compiler is satisfied.

Every API is a promise.

## Обговорення

API begins where behavior becomes observable.

Це не означає, що кожна helper function deserves a compatibility policy. Local function used by one file can change with the implementation that owns it. Private data structure can be rearranged when no consumer can observe or rely on it.

Threshold is reliance.

Коли інший component, task, tool, test, script, team або field procedure може observe behavior і build expectations on it, boundary starts becoming an API. Boundary may be C function, header, driver call, RTOS service, callback, event, command packet, persisted format, bootloader handoff, manufacturing command, debug hook, or service-tool workflow.

Shape is only easiest part to see. Radio function had name, parameter, return value. Consumers cared about hardware completion, success meaning, retry duplication, task context, data lifetime, reset behavior.

Consumers depend on behavior, not declarations.

That is the practical core of Every API Is a Promise (`LAW-002`). Declaration can stay still while behavior moves underneath. Source can compile while product becomes incompatible. Packet can keep same fields while meaning changes. Callback can keep type while arriving from different context. Persisted record can keep layout while changing what stored value means after startup.

Compatibility is larger than type compatibility.

Source compatibility asks whether source builds. Binary compatibility asks whether binaries link and run. Wire compatibility asks whether messages cross boundary correctly. Data compatibility asks whether stored formats remain readable and meaningful. Operational compatibility asks whether deployment, rollback, diagnostics, manufacturing, service, and field workflows still work.

Behavioral compatibility cuts across all of them.

Does success still mean same thing? Does error still tell caller what to do next? Does callback still arrive before memory release? Does call still block? Does system make same promise after reset? Does repeated request still have same effect? Does old tool see state it was designed to interpret?

APIs may evolve. Danger is pretending answer is yes because signature, version field, or packet shape survived.

Undocumented behavior can still become a contract.

Consumers learn from repeated behavior, examples, tests, sample applications, manufacturing scripts, field tools, support procedures, and previous releases. If every released implementation delivered callback before return, consumer may reasonably expect it. If service tool used "internal" debug command for three years, service workflow became real.

That is Silent Coupling (`SMELL-001`): hidden dependency affects behavior but is not represented as explicit contract. Producer thinks it changes implementation detail. Consumer experiences broken promise.

Remedy is not to promise everything forever. Good API says what is intentionally unspecified, distinguishes intentional contract, accidental contract, implementation detail, undefined behavior, unsupported behavior, and deprecated behavior.

Errors are part of promise. Invalid input tells caller to fix arguments. Temporarily unavailable tells caller to retry, wait, or show message. Request accepted but not completed tells caller to observe completion elsewhere. If meanings blur, recovery becomes guesswork.

Internal APIs also accumulate compatibility cost. Internal means cost may be easier to coordinate, not free. Firmware modules may be consumed by production code, diagnostics, manufacturing scripts, service tools, automated tests, bootloader code, and support procedures. Some release on different schedules or live outside repository.

Cost of change depends on consumers, not on whether boundary is called public.

Change Radius (`VOCAB-001`) matters. A small signature change can have small radius. Behavioral change behind stable signature can have large one. Affected surface includes code, tests, scripts, docs, release procedures, manufacturing instructions, service training, and rollback plans.

API Stability (`METRIC-004`) is not "APIs never change." It asks how reliably API preserves behavior its dependents trust. Stable APIs evolve by naming promise, naming incompatible part, and giving consumers a path.

Version numbers do not create compatibility. They help choose behavior or reject unsupported combinations, but cannot make incompatible semantic change safe by themselves.

Deprecation is a promise too. It says old behavior continues long enough for migration, replacement is known, consumers can detect or test difference, and removal happens after evidence shows migration is real.

Tests and documentation reveal the promise. They do not create it alone. ADR (`ARTIFACT-001`) can record why compatibility decision was made. Discoverability (`METRIC-003`) matters because promise that cannot be found will be rediscovered through failures.

Good API work protects implementation freedom. Vague promises restrict more because consumers depend on whatever happens. Precise API narrows what consumers may trust and leaves implementation free inside the boundary.

API is not merely the thing you call. It is behavior other parts of the system are allowed to trust.

## Інженерний принцип

Treat every observable boundary as a contract.

Specify what consumers may rely on, preserve those promises deliberately, and make incompatible change explicit instead of hiding it behind unchanged interface.

Use questions:

1. Who are the consumers?
2. What behavior can they observe?
3. What assumptions do they rely on today?
4. Which behaviors are guaranteed?
5. Which behaviors are intentionally unspecified?
6. What do success, rejection, and failure mean?
7. What are retry and repeated-call semantics?
8. Who owns memory, lifetime, and persisted state?
9. What execution context is supported?
10. Which compatibility dimensions matter for this boundary?
11. How will consumers migrate if the promise changes?

Goal is not to freeze every interface forever. Goal is to make change honest enough that consumers can survive it.

## Архітектурна вправа

### Запишіть обіцянку за одним API

Оберіть real API з system you work on. Choose boundary where another component, tool, test, script, or workflow already relies on behavior.

1. Who produces the API?
2. Who consumes it?
3. What purpose does it serve?
4. Which inputs are accepted?
5. Which inputs are rejected?
6. What preconditions must hold?
7. What does success mean?
8. What can fail, and what does each failure mean?
9. What side effects occur?
10. Who owns memory, handles, buffers, callbacks, or other lifetime-sensitive values?
11. Which execution contexts are supported?
12. Does API block, return after acceptance, or report completion later?
13. What ordering does it promise?
14. What happens when same request repeated?
15. Which failures should consumers retry?
16. Does API read or write persisted state?
17. Which compatibility dimensions matter: source, binary, wire, behavioral, data, or operational?
18. What behavior intentionally unspecified?
19. What accidental behavior do consumers appear to rely on?
20. Which tests encode promise?
21. What plausible incompatible change would require migration?
22. Where should decision be recorded: ADR, RFC, test, documentation, or existing artifact?

End with:

What would break if the implementation changed but the declaration stayed the same?

## Нотатник Principal Engineer

- Signatures are not promises.
- Errors teach consumers what to do.
- Compatibility is behavior.

## ADR

### Chapter ADR: Separate Channel-Change Acceptance from Completion

### Context

Existing `radio_set_channel()` API hides synchronous completion assumptions. Several consumers rely on successful return to mean radio hardware has applied channel. Service tooling, UI code, supervisory retry logic, and integration tests all depend on parts of that behavior.

Radio implementation needs queued hardware work so other tasks can continue running while radio settles. Keeping old signature while changing completion semantics creates race conditions, false UI state, confusing retries, and reset behavior consumers cannot interpret safely.

### Decision

Separate channel-change request acceptance from channel-change completion.

Keep old blocking API only as compatibility path during defined migration window. Introduce request-oriented API whose success means "request accepted." Publish completion through named event or callback with documented ordering and execution context.

Define error meanings for invalid input, rejected request, accepted request, temporarily unavailable radio, and failed application. Define retry and repeated-call behavior. Define ownership and lifetime for request data, callback data, and persisted channel state. Record whether persisted channel state means last requested, last applied, or unknown after reset.

Retire old behavior only after migration evidence shows consumers no longer depend on blocking completion.

### Consequences

Consumers can distinguish accepted work from completed hardware state. UI avoids reporting applied state too early. Retry logic avoids duplicating queued work. Integration tests encode completion ordering, error meanings, and reset semantics. Radio implementation can become asynchronous without pretending old promise still holds.

The decision creates work: migration, compatibility maintenance, event/callback states, documentation and service tooling changes, and visible unsupported/deprecated behavior until migration is complete.

### Alternatives Considered

Preserve blocking semantics indefinitely. Protects old consumers but ties implementation to hardware wait time.

Change implementation silently behind old signature. Header stable, consumers broken.

Add only timeout parameter. Exposes one timing concern but not acceptance, completion, retry behavior, callback context, or persistence semantics.

Create second API without migration policy. Gives new consumers better shape but leaves old behavior ambiguous.

Expose hardware state directly. Pushes radio state interpretation into consumers and increases change radius.

## Коментар редактора

Chapter 8 continues Part II by taking the boundary that Chapter 7 made visible and asking what crosses it.

Chapter 7 defined owner of meaningful state and transitions. This chapter defines what consumers may rely on when they call, observe, subscribe, persist, or automate across that boundary. A state owner can be correct internally and still harm system if API around it silently changes its promise.

The PEAK concepts carrying this chapter are Every API Is a Promise (`LAW-002`), Silent Coupling (`SMELL-001`), API Stability (`METRIC-004`), ADR (`ARTIFACT-001`), Discoverability (`METRIC-003`), and Change Radius (`VOCAB-001`). They are enough.
