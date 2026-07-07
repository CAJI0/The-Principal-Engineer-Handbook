# Every API Is a Promise

## Opening Quote

> A signature tells you how to call. A promise tells you what you may trust.

## Story

The radio team thought it had preserved the interface.

The function name was the same. The parameter was the same. The return type was
the same. Every caller still compiled.

```c
status_t radio_set_channel(uint8_t channel);
```

That was the argument in the review: no public header had changed, no command
identifier had changed, no new packet format had been introduced, and no
consumer needed to update its build. The radio service had been rewritten
because the old implementation blocked while the hardware settled. The new
implementation queued the work so other tasks could keep running.

The change looked like an implementation improvement.

The first failure did not look like an API failure.

A service application reported that the device had moved to channel 17. The
operator saw the new value and started a diagnostic capture. The capture came
back empty. The device was still transmitting on the old channel because the
hardware operation had not completed yet.

The UI was not lying. It was reporting what the call had returned.

The second failure came from retry logic. A supervisory task saw a temporary
radio-unavailable error and retried the call. In the old implementation, a
retry after that error usually meant the original operation had not started. In
the new implementation, the first request had already been accepted into the
queue. The retry created a second channel-change request. Sometimes the two
requests collapsed into the same final channel. Sometimes they interleaved with
a scan request and left diagnostics attached to the wrong assumption.

The third failure came after reset.

The radio service restored the last requested channel from persistent storage.
The hardware still needed calibration before it could apply that channel. The
service tool displayed the restored channel as current because that was how the
old API had behaved after restart. Manufacturing tooling used the displayed
value to choose a test path. The test failed intermittently, and the logs made
the radio look unreliable.

The old implementation had carried more meaning than its signature admitted.

Callers had learned that a successful return meant the hardware had applied the
channel. They had learned that invalid input left the prior channel unchanged.
They had learned that callbacks arrived before the function returned. They had
learned that repeated calls with the same channel were harmless. They had
learned that an invalid channel and an unavailable radio were different kinds of
failure. They had learned which task contexts were safe. They had learned that
a persisted channel after reset represented something close to current hardware
state.

Some of those behaviors were documented. Some were in tests. Some were in
examples. Some were only in the memory of service engineers and manufacturing
scripts.

All of them had become part of the promise.

The team proposed fixes that were familiar because each one protected one
consumer.

Add a delay in the UI before reporting the new channel. Add a version number to
the radio service. Add an optional callback for the service tool. Tell callers
to wait until the next telemetry update. Keep the old function name so old code
continues to build. Make the supervisor retry more carefully. Add a note that
the new implementation is asynchronous.

None of those changes answered the shared question.

What does `radio_set_channel()` promise now?

The principal engineer asked the team to write the old promise before approving
the new implementation.

Not the signature. Not the module name. The promise.

They wrote down what consumers had been relying on:

- which channel values were accepted;
- when the hardware was considered changed;
- what success meant;
- what each error meant;
- which calls could be repeated safely;
- which task contexts could call the function;
- when callbacks were delivered;
- who owned the callback data;
- what persisted state meant after reset;
- how a consumer could tell request acceptance from operation completion.

The list changed the conversation.

The new implementation did not have to be rejected. Queuing hardware work was a
reasonable design. The problem was that the team had changed completion
semantics while preserving the old shape. The old API had promised "channel
applied." The new implementation returned after "request accepted."

Those are different promises.

The team split the behavior. The old function remained as a compatibility path
for consumers that needed blocking completion during the migration window. A new
request-oriented API made acceptance explicit. Completion arrived through a
named event with defined ordering and callback context. Error codes separated
invalid input, rejected request, queued request, unavailable radio, and failed
application. Repeated requests had a documented result. Persistence recorded the
last requested channel and the last applied channel separately, because those
were not the same fact.

The tests changed too.

The old unit test that checked only the return code stayed useful, but it was
not enough. Integration tests now checked that UI state did not report applied
hardware before completion. Supervisory retry tests checked duplicate requests.
Reset tests checked whether restored state meant requested, applied, or unknown.
Service-tool tests checked which errors should be retried and which should be
shown to the operator.

The header had hidden a contract. The failure made it visible.

The final decision was not "never make APIs asynchronous." The decision was
more precise: when an API crosses a meaningful boundary, the observable behavior
is the contract. If that behavior changes, the architecture has changed even
when the compiler is satisfied.

Every API is a promise.

## Discussion

An API begins where behavior becomes observable.

That does not mean every helper function deserves a compatibility policy. A
local function used by one file can change with the implementation that owns it.
A private data structure can be rearranged when no consumer can observe or rely
on its shape. Engineering would become impossible if every temporary boundary
were treated like a public standard.

The threshold is reliance.

When another component, task, tool, test, script, team, or field procedure can
observe behavior and build expectations on it, the boundary has started to
become an API. The boundary might be a C function, a header, a driver call, an
RTOS service, a callback, an event, a command packet, a persisted format, a
bootloader handoff, a manufacturing command, a debug hook, or a service-tool
workflow.

The shape is only the easiest part to see.

The radio function had a name, a parameter, and a return value. Those mattered.
They did not contain the whole promise. Consumers cared about when the hardware
changed, what success meant, whether a retry duplicated work, which task
contexts were safe, what data lived long enough for a callback, and what reset
restored.

Consumers depend on behavior, not declarations.

That sentence is the practical core of Every API Is a Promise (`LAW-002`). A
declaration can stay still while behavior moves underneath it. A source file can
compile while the product becomes incompatible. A packet can keep the same
fields while a receiver changes the meaning of an optional value. A callback can
keep the same type while arriving from a different context. A persisted record
can keep the same layout while changing what the stored value means after
startup.

Compatibility is larger than type compatibility.

Source compatibility asks whether existing source still builds. Binary
compatibility asks whether existing binaries still link and run. Wire
compatibility asks whether messages still cross a boundary correctly. Data
compatibility asks whether stored formats remain readable and meaningful.
Operational compatibility asks whether deployment, rollback, diagnostics,
manufacturing, service, and field workflows still work.

Behavioral compatibility cuts across all of them.

Does success still mean the same thing? Does an error still tell the caller what
to do next? Does the callback still arrive before a consumer releases memory?
Does the call still block? Does the system still make the same promise after
reset? Does a repeated request still have the same effect? Does an old tool see
the same state the old tool was designed to interpret?

The answer can be "no." APIs are allowed to evolve. The danger is pretending
that the answer is "yes" because a signature, version field, or packet shape
survived.

Undocumented behavior can still become a contract.

This is uncomfortable because it sounds unfair to the producer. The team may
say, "We never promised callbacks before return." That may be true in the
formal documentation. It may not be true in the system.

Consumers learn from what the system repeatedly does. They learn from examples,
tests, sample applications, manufacturing scripts, field tools, support
procedures, and previous releases. If every released implementation delivered a
callback before return, a consumer may have built a reasonable expectation. If a
service tool has used a debug command for three years, calling that command
"internal" does not make the service workflow disappear. If a test station
depends on field order in a file, the file has become part of a promise even if
the parser was never advertised.

That is Silent Coupling (`SMELL-001`): a hidden dependency affects behavior but
is not represented as an explicit contract. The producer thinks it is changing
an implementation detail. The consumer experiences a broken promise.

The remedy is not to promise everything forever.

A good API also says what is intentionally unspecified. It names behavior that
callers may not rely on. It distinguishes intentional contract, accidental
contract, implementation detail, undefined behavior, unsupported behavior, and
deprecated behavior. Those labels are useful only when consumers can discover
them before they depend on the wrong thing.

Errors are part of the promise.

Error handling is often where hidden API promises become expensive. A return
code that means "invalid input" leads a caller to correct its arguments. A
return code that means "radio temporarily unavailable" leads a caller to retry,
wait, or show a different message. A return code that means "request accepted
but not completed" leads a caller to observe completion somewhere else.

If those meanings blur, recovery becomes guesswork.

Timeouts, immediate rejection, partial success, stale data, duplicate requests,
unavailable dependencies, invalid state, and diagnostic messages all shape what
consumers can safely do. Chapter 10 will treat time as its own dependency, but
Chapter 8 needs the simpler point: when timing and failure behavior are
observable, they are part of the API promise.

Internal APIs also accumulate compatibility cost.

Internal does not mean free. It means the cost may be easier to coordinate if
the producer and consumers release together, share ownership, have strong test
coverage, and can roll back together. Many internal APIs do not have those
conditions. A firmware module may be consumed by production code, diagnostics,
manufacturing scripts, service tools, automated tests, bootloader code, and
support procedures. Some of those consumers may release on a different schedule. Some
may be hard to find. Some may live outside the repository. Some may be difficult
to update in the field.

The cost of change depends on consumers, not on whether the boundary is called
public.

That is why Change Radius (`VOCAB-001`) matters for API work. A small signature
change can have a small radius. A behavioral change behind a stable signature
can have a large one. The affected surface includes code, tests, scripts,
documentation, release procedures, manufacturing instructions, service training,
and rollback plans.

API Stability (`METRIC-004`) is not a demand that APIs never change. It asks how
reliably the API preserves the behavior its dependents trust. Stable APIs can
evolve. They evolve by naming the promise, naming the incompatible part, and
giving consumers a path.

Version numbers do not create compatibility.

A version number can help a consumer choose behavior. It can help a producer
reject unsupported combinations. It can make migration visible. It cannot make
an incompatible semantic change safe by itself. Neither can adding a field,
adding an optional callback, or wrapping the old function with a new one.

Additive changes can still break consumers. An optional field can become
required in practice. A new callback can change ordering. A compatibility layer
can preserve old behavior for one caller while hiding cost for everyone else.
An adapter can become permanent architecture if nobody owns its retirement.

Deprecation is a promise too.

It says old behavior will continue long enough for migration, that the
replacement is known, that consumers can detect or test the difference, and that
removal will happen only after evidence shows the migration is real. Without
that evidence, deprecation becomes a comment attached to behavior everyone still
depends on.

Tests and documentation reveal the promise. They do not create it alone.

A test can encode an expectation so future changes notice it. Documentation can
tell consumers what they may rely on. An ADR (`ARTIFACT-001`) can record why a
compatibility decision was made, what alternatives were rejected, and what costs
the team accepted. Discoverability (`METRIC-003`) matters because a promise that
cannot be found will be rediscovered through failures.

But a document that says "do not rely on callback order" is not enough if every
example relies on callback order. A test that checks only the return type is not
enough if consumers depend on completion timing. A version table is not enough
if it does not say what changed.

Good API work protects implementation freedom.

That may sound backwards. A precise promise feels restrictive. In practice, a
vague promise restricts more. When consumers do not know what is guaranteed,
they depend on whatever happens. Every implementation detail can become risky to
change because nobody knows whether a consumer relies on it.

A precise API narrows the promise. It says what consumers may trust, what they
must not assume, how errors behave, what completion means, who owns data, which
contexts are supported, and how incompatible change will be made visible. Inside
that boundary, the implementation can move.

The radio service could become asynchronous once consumers could distinguish
acceptance from completion. The implementation gained freedom because the
promise became explicit.

That is the discipline behind the law.

An API is not merely the thing you call. It is the behavior other parts of the
system are allowed to trust.

## Engineering Principle

Treat every observable boundary as a contract.

Specify what consumers may rely on, preserve those promises deliberately, and
make incompatible change explicit instead of hiding it behind an unchanged
interface.

Use questions like these before changing an API:

1. Who are the consumers?
2. What behavior can they observe?
3. What assumptions do they rely on today?
4. Which behaviors are guaranteed?
5. Which behaviors are intentionally unspecified?
6. What do success, rejection, and failure mean?
7. What are the retry and repeated-call semantics?
8. Who owns memory, lifetime, and persisted state?
9. What execution context is supported?
10. Which compatibility dimensions matter for this boundary?
11. How will consumers migrate if the promise changes?

The goal is not to freeze every interface forever. The goal is to make change
honest enough that consumers can survive it.

## Architecture Exercise

### Write the Promise Behind One API

Choose one real API from a system you work on. Do not choose the biggest public
interface by default. Choose a boundary where another component, tool, test,
script, or workflow already relies on behavior.

Write short answers to these prompts:

1. Who produces the API?
2. Who consumes it?
3. What purpose does it serve?
4. Which inputs are accepted?
5. Which inputs are rejected?
6. What preconditions must hold?
7. What does success mean?
8. What can fail, and what does each failure mean?
9. What side effects occur?
10. Who owns memory, handles, buffers, callbacks, or other lifetime-sensitive
    values?
11. Which execution contexts are supported?
12. Does the API block, return after acceptance, or report completion later?
13. What ordering does it promise?
14. What happens when the same request is repeated?
15. Which failures should consumers retry?
16. Does the API read or write persisted state?
17. Which compatibility dimensions matter: source, binary, wire, behavioral,
    data, or operational?
18. What behavior is intentionally unspecified?
19. What accidental behavior do consumers appear to rely on?
20. Which tests encode the promise?
21. What plausible incompatible change would require migration?
22. Where should the decision be recorded: ADR, RFC, test, documentation, or an
    existing artifact?

End with this question:

What would break if the implementation changed but the declaration stayed the
same?

## Principal's Notebook

- Signatures are not promises.
- Errors teach consumers what to do.
- Compatibility is behavior.

## ADR

### Chapter ADR: Separate Channel-Change Acceptance from Completion

### Context

The existing `radio_set_channel()` API hides synchronous completion assumptions.
Several consumers rely on a successful return to mean that the radio hardware
has applied the channel. Service tooling, UI code, supervisory retry logic, and
integration tests all depend on parts of that behavior.

The radio implementation needs to move to queued hardware work so other tasks
can continue running while the radio settles. Keeping the old signature while
changing completion semantics creates race conditions, false UI state,
confusing retries, and reset behavior that consumers cannot interpret safely.

### Decision

Separate channel-change request acceptance from channel-change completion.

Keep the old blocking API only as a compatibility path during a defined
migration window. Introduce a request-oriented API whose success means "request
accepted." Publish completion through a named event or callback with documented
ordering and execution context.

Define error meanings for invalid input, rejected request, accepted request,
temporarily unavailable radio, and failed application. Define retry and
repeated-call behavior. Define ownership and lifetime for request data,
callback data, and persisted channel state. Record whether persisted channel
state means last requested, last applied, or unknown after reset.

Retire the old behavior only after migration evidence shows that consumers no
longer depend on blocking completion.

### Consequences

Consumers can distinguish accepted work from completed hardware state. UI code
can avoid reporting applied state too early. Retry logic can avoid duplicating
queued work. Integration tests can encode completion ordering, error meanings,
and reset semantics. The radio implementation can become asynchronous without
pretending the old promise still holds.

The decision creates work. Existing consumers need migration. The compatibility
path must be maintained and retired deliberately. The event or callback adds
states that tests must cover. Documentation and service tooling must change
together. The API owner must keep unsupported and deprecated behavior visible
until the migration is complete.

### Alternatives Considered

Preserve blocking semantics indefinitely. This protects old consumers but keeps
the implementation tied to hardware wait time and limits scheduling freedom.

Change the implementation silently behind the old signature. This keeps the
header stable but breaks consumers that relied on completion, callback order,
and error behavior.

Add only a timeout parameter. This exposes one timing concern but does not
define acceptance, completion, retry behavior, callback context, or persistence
semantics.

Create a second API without a migration policy. This gives new consumers a
better shape but leaves old behavior ambiguous and may keep the compatibility
burden forever.

Expose hardware state directly. This may look transparent, but it pushes radio
state interpretation into consumers and increases change radius.

## Editor's Commentary

Chapter 8 continues Part II by taking the boundary that Chapter 7 made visible
and asking what crosses it.

Chapter 7 defined the owner of meaningful state and transitions. This chapter
defines what consumers may rely on when they call, observe, subscribe, persist,
or automate across that boundary. The distinction matters. A state owner can be
correct internally and still harm the system if the API around it changes its
promise silently.

The chapter also reaches backward into Part I. Chapter 1 framed architecture as
future cost. Chapter 2 treated commitments as real when consequences and
constraints make them hard to reverse. Chapter 3 exposed hidden assumptions.
Chapter 4 made ownership and closure explicit. Chapter 5 tied confidence to
evidence. Chapter 6 asked engineers to leave systems easier to change. API
promises touch all of that without replacing any of it.

The PEAK concepts carrying this chapter are Every API Is a Promise (`LAW-002`),
Silent Coupling (`SMELL-001`), API Stability (`METRIC-004`), ADR
(`ARTIFACT-001`), Discoverability (`METRIC-003`), and Change Radius
(`VOCAB-001`). They are enough. The chapter does not need a new contract
artifact or vocabulary term to teach the law.

The point is not to make every internal helper ceremonial. The point is to stop
treating observable behavior as accidental after consumers have built their work
on it.
