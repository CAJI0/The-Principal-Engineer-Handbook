# Drawing Boundaries That Survive Change

## Opening Quote

> A boundary is not where code is divided. It is where responsibility, authority, and knowledge stop crossing unnoticed.

## Story

The radio wrapper looked clean in the diagram.

The product was an embedded field controller. It collected data from several local devices, sent command acknowledgements
to a supervisory system, and used a radio module when wired connectivity was unavailable. The first version had one
radio vendor, one transport, one RTOS task that handled the driver, one service tool, and one product behavior that
everyone understood: keep the controller connected when the radio is present, report link state, send product messages,
and recover without losing the product's idea of what it had promised upstream.

The team did something reasonable. They did not let every feature call the vendor driver directly. They created a radio
manager.

At first, that felt like a boundary.

The product code called `RadioManager_Send`. The manager registered the vendor callback. It owned driver initialization,
the socket address, the vendor channel handle, and the retry loop around a few known driver errors. When the service
tool needed to ask for radio diagnostics, it went through the manager. When the UI needed link state, it asked the
manager. When tests needed to simulate radio events, they triggered the callback through a helper. The diagram had one
box labeled "radio."

No one was being careless. The product was small. The vendor driver worked. The team had a schedule. Hiding the driver
behind one manager was better than letting every module use the driver header directly.

Then the details began to travel.

The product state machine stored the vendor's connection state because it was already available. The UI checked for the
vendor's "channel busy" error so it could show a different message during commissioning. The persistence record saved
the channel identifier because support wanted to compare it with radio logs. The command handler treated one raw packet
type as "remote command pending" and another as "service mode." The diagnostics task logged driver retry reason codes
without translating them. The network service learned a socket address format. The service tool sent the vendor's
control command for link reset because that was the only command that worked reliably. The tests mocked the vendor
callback signature because that was how completion arrived. A timing assumption from the driver made its way into a
product timeout.

The manager was still there.

So was the leak.

Platform Leakage (`SMELL-005`) had become normal product language. HAL Everywhere (`ANTIPATTERN-002`) did not look like
raw register reads in every file. It looked more respectable: vendor status values, driver packet shapes, RTOS event
bits, socket details, and service commands spreading through product decisions that should have been expressed in
product terms.

The trigger was a second radio family.

The product team wanted a variant for a market where the original radio module was hard to source. The user-visible
behavior was supposed to remain the same. The controller should still report link state, accept product messages, send
outbound messages, recover after loss, and expose diagnostics useful enough for support. The second radio had a
different control protocol, different connection states, different completion behavior, different retry codes, and no
equivalent for one service command.

The first estimate sounded small.

"We already have a manager. We'll add an adapter."

The first adapter edit touched the manager. The second touched UI status text. The third touched persistence because the
new radio did not have the same channel identifier. The fourth touched tests because the callback arguments were
different. The fifth touched diagnostics because support could not compare the same raw reason codes. The sixth touched
the command handler because packet classification had used vendor packet types. The seventh touched recovery because
the old driver retried before signalling failure while the new one signalled earlier and expected the caller to decide.
The eighth touched a direct platform call in a commissioning path that bypassed the manager because a previous release
needed a fast fix.

The work was no longer "add an adapter."

It was "find every place where the product had learned the first radio."

That was Silent Coupling (`SMELL-001`). The real dependency graph was not represented by the diagram. Teams had been
coordinating by memory. Tests encoded assumptions not present in the product contract. A change in one driver reached
UI, storage, command handling, diagnostics, recovery, service tooling, and release testing without an obvious call path.

Hidden State (`SMELL-004`) made the situation worse. The manager had its own view of link state. The product state
machine stored a copied vendor state. The UI cached a derived state so it could avoid blocking on the manager. The
service tool kept the last raw driver status. The callback could mutate state during recovery before the product owner
had accepted the transition. A reset sometimes fixed the problem because it erased one of those views, not because
anyone understood which truth had been wrong.

The manager had become a polite version of Manager Mania (`ANTIPATTERN-004`). It coordinated behavior without owning the
product decision. When someone asked whether the controller was allowed to accept outbound messages during partial link
recovery, the answer was not in the manager, not in the product state machine, not in the driver adapter, and not in the
service tool. It lived in the way all of those places happened to cooperate.

The first proposals tried to preserve the shape of the old wrapper.

"Add a vendor flag."

"Put more methods on the manager."

"Define one universal driver interface."

"Duplicate the product logic for the second radio."

"Use a generic event bus so neither side knows about the other."

"Rename the status values to product names."

"Use conditional compilation around the differences."

"Move everything into one platform service."

"Add another abstraction layer above the manager."

"Allow direct HAL access for exceptional paths."

None of those ideas was universally foolish. A vendor flag might be a short bridge during migration. A new method might
be exactly right when the product contract has grown. A common driver interface can help when two mechanisms truly have
the same meaning. Events can preserve timing isolation. Conditional compilation can be appropriate at a narrow hardware
edge. Direct platform access can be necessary for bring-up code that is not product behavior.

But none of the proposals answered the architecture question.

The Principal Engineer recast the work:

> Which product decision must remain stable, which integration details vary, and where should translation occur?

The answer was not "radio."

"Radio" was a device category. It was not yet a boundary.

The stable product decision was the controller's radio control behavior: when the product considers the link available,
which product commands may be sent, what completion means, how retries affect product promises, what recovery may
change, and what diagnostics support needs in order to explain product behavior.

That decision needed product vocabulary.

The product did not need to know "vendor state 7." It needed to know whether the link was unavailable, ready to send,
waiting for completion, temporarily congested, failed with a retry scheduled, failed with product-visible loss, or in a
recovery state that blocked new commands. The product did not need raw packet structures. It needed product commands and
outcomes. The product did not need every driver retry code. It needed failure categories that matched what the product
could responsibly do.

The team drew the intended boundary around that product-owned control behavior.

The product owner would own authoritative radio control state. That honored Every State Has One Owner (`LAW-001`):
every meaningful state in the system must have exactly one clear owner. The adapter could observe driver state, hold
mechanism-specific handles, and translate completion. It could not mutate product truth through a callback. The UI,
persistence, command handling, tests, diagnostics, and service tool would depend on the product contract, not on vendor
states.

The contract became explicit because Every API Is a Promise (`LAW-002`). It named product-level commands, accepted
inputs, observable outcomes, completion semantics, failure categories, retry ownership, recovery handoff, and lifecycle
constraints. It did not promise that every radio family behaved identically. It promised the meanings that product code
was allowed to rely on.

The dependency direction changed even though runtime flow did not become simple.

At runtime, the driver still invoked callbacks. The radio still signalled completion asynchronously. A queue still
carried events from the driver task. The service tool still requested diagnostics. But design knowledge no longer
pointed from product policy into vendor mechanism. The adapter depended on the product-owned contract. Product code did
not depend on vendor headers, RTOS event bits, raw packet types, socket address structures, or driver retry meanings.

That made Every Dependency Is a Decision (`LAW-007`) visible. The radio vendor still mattered. Its behavior, failure
modes, lifecycle constraints, ownership boundaries, and replacement cost were real. The boundary did not pretend
hardware reality disappeared. It constrained where the imported knowledge could spread.

Translation moved to the edge.

The adapter translated vendor channel identifiers into product link identities. It translated connection states into
product link outcomes. It translated raw packet types into product commands or unsupported input. It translated driver
errors into product failure categories. It translated completion callbacks into product-owned completion events. It
translated service diagnostics into two views: product diagnostics for normal support work and adapter diagnostics for
radio-specific investigation.

Translation was not just renaming.

One old vendor status had meant both "not connected" and "driver is starting again after reset." The product had
treated both as "link down." The second radio separated those cases. The team had to decide which product state each
case meant, whether new product behavior was required, and how recovery ownership should work. That was a boundary
decision, not a type conversion.

The team also removed back channels.

The commissioning path stopped calling the platform reset command directly. The UI stopped reading raw driver status.
The service tool stopped sending vendor commands as product commands. Tests stopped mocking vendor callbacks when they
were meant to test product behavior. Diagnostic records stopped using raw driver codes as the main explanation for
product outcomes. Direct platform access stayed only in adapter tests and bring-up procedures, where it was named as
platform work rather than product behavior.

The migration was deliberately small.

The team did not rewrite the subsystem. They picked one path: outbound product message submission. They defined the
product command, completion meanings, allowed states, retry ownership, adapter translation, tests, and diagnostics for
that path. They measured the current Change Radius (`VOCAB-001` and `METRIC-001`) by listing every file, test, review
owner, diagnostic path, and support procedure touched by the second radio. Then they compared it with the desired
surface after the product contract existed.

The measure was approximate. That was enough.

Before the boundary, one integration change touched unrelated product areas because product code knew platform details.
After the first path moved, changes to a vendor retry code touched the adapter tests and diagnostics translation, but
not UI status text, product state transition rules, or command handling.

The team recorded the decision in an ADR (`ARTIFACT-001`) because the boundary would affect future architecture,
ownership, cost, and reversibility. The ADR did not say "add an interface." It said where product authority lived, what
vocabulary could cross, what translation the edge owned, which bypasses had to close, how migration would proceed, and
what costs the team accepted.

The radio wrapper in the diagram did not disappear.

It became less important than the question it had failed to answer:

What must this part of the system be allowed to know?

## Discussion

An architecture boundary is an intentional separation of responsibility, authority, and knowledge.

That definition is stricter than "there is a module here." It is stricter than "there is an interface here." It is
stricter than "the code is in another process." A module organizes code. An interface exposes a surface. A layer orders
dependencies. A task or process changes runtime execution. A boundary decides what knowledge may cross, who owns the
decision, and which reasons to change are allowed to travel together.

Those structures can implement a boundary. They do not prove one exists.

The story's radio manager was a useful structure. It centralized driver setup and reduced direct calls. But it did not
protect the product decision. The product still knew vendor status values, packet shapes, retry meanings, event bits,
socket details, and service commands. The system had a wrapper around the mechanism, not a boundary around the product
authority.

Start boundary work by naming the decision.

"Radio" is too broad. "Transport" is often too vague. "Driver integration" can be too mechanism-centered. The useful
question is: which product decision must remain coherent when the mechanism changes?

In the story, the decision was product-owned radio control behavior: availability, command acceptance, completion,
failure categories, retry ownership, recovery handoff, diagnostics, and lifecycle. That is why UI, persistence, command
handling, tests, diagnostics, and service tooling belonged on the product side of the contract. It is also why vendor
handles, raw packet formats, RTOS bits, and driver retry codes belonged on the adapter side.

Boundaries separate reasons to change.

Product policy changes for one set of reasons. Hardware integration changes for another. Vendor protocol changes for
another. UI presentation, persistence, diagnostics, manufacturing, support tooling, and release compatibility each have
their own sources of change. A durable boundary does not split every file until nothing can move. It groups decisions
that must change together and separates decisions that should not be forced to change together.

This is why boundary granularity matters.

A boundary that is too broad becomes a God Module (`ANTIPATTERN-001`). It gathers unrelated responsibilities, makes many
features edit the same place, and turns tests into subsystem exercises. A boundary that is too narrow creates forwarding
surfaces, fragmented ownership, extra copies, excessive synchronization, and many tiny changes that still need broad
coordination. The right size is not the smallest abstraction. It is the smallest truthful separation that protects the
decision at stake.

Product vocabulary belongs with product authority.

When product code says "driver channel closed," "vendor status 4," or "RTOS bit 0x20," the product has imported the
platform's model. Sometimes that is intentional and correct. Embedded systems have hardware constraints, timing
constraints, memory constraints, and vendor behavior that cannot be wished away. But if those terms decide UI behavior,
state transitions, persistence schema, command semantics, support procedures, or release compatibility, the platform
has become product authority.

Translation at the boundary preserves meaning while changing vocabulary.

It converts identifiers, status values, errors, lifecycle states, completion signals, data representation, timing
expectations, ownership rules, and diagnostic detail. It should not collapse meaningful differences into one generic
status merely to make two mechanisms appear identical. It should also not expose every mechanism detail merely because
some product behavior depends on hardware reality. Good translation says, "This is the product meaning we own, and this
is the platform detail we contain."

Authority is the hardest part to fake.

If product state lives in one owner, then callbacks, events, queues, caches, snapshots, persistence records, diagnostic
views, and service tools must not silently become competing writers. They may observe. They may request. They may carry
facts. They may preserve history. They may help recovery. But if a callback can mutate product truth without the owner
accepting the transition, the boundary has failed even if the code path looks decoupled.

Dependency direction is not runtime flow.

A driver may call a product completion handler at runtime. A queue may deliver events from adapter to product owner. A
message may travel from lower-level code to higher-level code. None of that automatically means product policy depends
on the driver. The dependency question is about knowledge: which side must understand the other side's concepts in
order to compile, test, change, and explain behavior?

Direct calls are not automatically bad. Events are not automatically good. Callbacks are not automatically a boundary.
Queues are not automatically isolation. Shared memory is not automatically a leak. Snapshots are not automatically
hidden state. Each mechanism is architectural only in relation to authority, contract, dependency direction, and
meaning.

Back channels reveal the real architecture.

A direct HAL call in a rare commissioning path can matter more than the manager everyone points to. A debug-only command
can become the service team's actual recovery path. A test hook can encode product behavior. A persistence field can
keep an old vendor detail alive after the adapter has changed. A hidden event subscription can make a second owner of
state. These paths show what the system relies on when the intended contract is inconvenient.

A boundary survives change when expected change can be absorbed on one side without forcing unrelated decisions to move
or leak.

That does not mean callers never change. It does not mean contracts never evolve. It does not mean replacing a device,
vendor, protocol, or transport is free. It does not mean a boundary is eternal. When the product model changes, the
boundary may need to move.

Durability means the boundary remains truthful under the changes the architecture reasonably expects.

Evidence matters here, but this chapter does not teach the full Change Radius method. Use Change Radius as a signal:
when a small integration change touches UI, state, persistence, tests, diagnostics, support tooling, and recovery, the
boundary is probably lying. Chapter 15 owns the full practice of mapping and managing that radius. Here, the point is
simple: a boundary that claims to contain a decision should reduce the unrelated surface that decision must disturb.

Failure and recovery also matter, but this chapter does not become the failure chapter. A boundary contract should name
failure categories, completion meaning, retry ownership, and recovery handoff well enough that product authority is
clear. Chapter 16 owns failure and recovery design. That includes the full design of detection, containment,
degradation, retry, recovery, and unknown outcomes.

An ADR matters, but this chapter is not an ADR tutorial. Record a boundary decision when it affects future architecture,
ownership, cost, or reversibility. Chapter 17 owns the deeper practice of choosing, writing, reviewing, and maintaining
ADRs and RFCs. Here, the ADR is useful because it forces the boundary decision to state context, decision,
consequences, and alternatives.

Architecture Review and Architecture Freeze will come later. Chapter 18 owns review practice.

Chapter 19 owns Architecture Freeze.

Chapter 14 gives those later practices something concrete to inspect: where authority lives, what vocabulary crosses,
which dependencies are contained, which back channels remain, and what change the boundary is expected to survive.

This is how Part III begins.

Part II named the laws. Boundaries are where those laws become operational. State ownership needs a place where
authority lives. API promises need a contract surface that contains the right knowledge. Dependency decisions need
direction and containment. Timing and completion need meaning at the edge. Simplicity needs proportionate structure.
Evidence needs a way to show whether the boundary is truthful.

## Engineering Principle

Draw boundaries around product decisions and coherent reasons to change. Keep authority, vocabulary, and dependency
direction explicit, and translate volatile mechanisms at the edge.

Use this principle as a review habit:

1. What product decision does this boundary protect?
2. Who owns the authoritative state?
3. Which product terms are allowed to cross?
4. Which platform terms must be translated?
5. Which dependencies point toward stable product meaning?
6. Which runtime calls, callbacks, events, queues, or messages are only mechanisms?
7. Which completion, failure, retry, and recovery meanings are promised?
8. Which back channels bypass the intended contract?
9. Which reasons to change belong on each side?
10. What cost does the boundary add?
11. What expected change should the boundary absorb?
12. What evidence shows the boundary is truthful?

The goal is not to make every mechanism replaceable. The goal is to keep product authority from being accidentally
owned by whichever mechanism arrived first.

## Architecture Exercise

### Redraw One Leaky Boundary

Choose one integration boundary in your system. Pick something real: a driver wrapper, service client, protocol adapter,
manufacturing station path, diagnostic interface, payment integration, storage connector, device bridge, or subsystem
API that people already believe is isolated.

Write short answers to these prompts:

1. What product capability does this boundary support?
2. What product decision should remain stable when the mechanism changes?
3. Who owns the authoritative state?
4. Which modules, tasks, processes, tools, tests, and support paths touch it today?
5. What contract do callers believe exists?
6. Which product vocabulary appears at the boundary?
7. Which platform, vendor, transport, or tool terms cross the boundary?
8. Which side depends on the other's concepts at design or compile time?
9. Which direction do calls, callbacks, events, queues, or messages flow at runtime?
10. Which snapshots, caches, persistence records, or diagnostics can become hidden state?
11. Which completion, failure, retry, and recovery meanings are unclear?
12. Which back channels bypass the intended contract?
13. Which reasons to change belong on the product side?
14. Which reasons to change belong on the mechanism side?
15. What realistic future change would test the boundary?
16. What is the current affected surface if that change happens?
17. What product-owned contract would reduce unrelated edits?
18. What translation belongs at the edge?
19. What migration path moves one product path first?
20. What tests and diagnostics would prove the boundary is being used?
21. Where should the ADR live?

End with one small, reviewable boundary decision:

- the product decision being protected;
- the owner of authoritative state;
- the product terms allowed to cross;
- the mechanism terms translated at the edge;
- the first back channel to remove;
- the first path to migrate;
- the evidence that will show the Change Radius changed.

Do not invent a new architecture artifact for the exercise. Use the records and review paths your system already has.

## Principal's Notebook

- A boundary separates decisions, not files.
- Translation belongs where vocabularies meet.
- Back channels reveal the real architecture.

## ADR

### Chapter ADR: Place Radio Integration Behind a Product-Owned Control Boundary

### Context

The product began with one radio vendor and a radio manager intended to isolate hardware. Over time, vendor connection
states, channel identifiers, callback signatures, raw packet types, retry codes, socket details, RTOS event bits, timing
assumptions, and service commands spread into UI, product state, persistence, diagnostics, command handling, tests,
network services, and support tooling.

A second radio family must preserve the same user-visible behavior while using different integration details. The
current manager is a structural wrapper, not a durable boundary. Authoritative product state is split across product
state, manager state, UI cache, service tool status, and callback mutation. Recovery ownership is unclear. Direct
platform bypasses exist for commissioning and diagnostics.

### Decision

Define a product-owned radio control boundary.

The boundary owns product-level radio control behavior: link availability, command acceptance, completion meaning,
failure categories, retry ownership, recovery handoff, lifecycle, diagnostics, and support-visible outcomes.

Keep product code in product vocabulary. UI, persistence, command handling, diagnostics, tests, network services, and
service tooling depend on product commands and outcomes, not vendor states, raw packets, driver retry codes, RTOS event
bits, socket structures, or service commands.

Assign authoritative radio control state to the product owner. Driver callbacks and adapter events report observations
and completions; they do not mutate product truth outside that owner.

Place vendor operations in adapters. Adapters translate identifiers, status values, packet shapes, errors, completion,
timing assumptions, and diagnostic detail at the edge. Preserve necessary asynchronous completion without exposing
vendor callback signatures as the product contract.

Remove direct platform bypasses from product paths. Keep platform-specific access in adapter tests, bring-up work, or
named diagnostic procedures where it does not become product behavior.

Migrate one product path first: outbound product message submission. Define its contract, translation, tests,
diagnostics, and recovery handoff before expanding the boundary to other radio paths.

Record current and desired Change Radius for the second radio integration. Use that evidence to decide whether the
boundary is reducing unrelated edits.

### Consequences

Product semantics become stable across radio families. Vendor knowledge is contained. State authority becomes explicit.
Tests can target product behavior separately from adapter translation. Diagnostics can distinguish product outcomes from
radio-specific causes. Future integration changes should affect a smaller, more understandable surface.

The decision adds translation code, adapter tests, migration work, and temporary coexistence. It may introduce copies,
latency, synchronization, or diagnostic mapping costs. The product contract may become too broad if the team puts
unrelated radio decisions inside it. Future product behavior changes may still require contract evolution. Hardware
constraints remain real; they are contained and named, not erased.

### Alternatives Considered

Extend the current manager. This is fast for the second radio, but it keeps product authority hidden in a coordinator
that already allowed vendor knowledge to spread.

Create one universal driver interface. This may help if mechanisms truly share meaning, but here it risks flattening
different completion, retry, and recovery meanings into a weak common shape.

Duplicate product logic per radio family. This preserves each integration's details, but it lets product behavior drift
and makes compatibility a repeated argument.

Use conditional compilation throughout. This may be valid at a narrow hardware edge, but it would spread integration
knowledge through product decisions.

Introduce a generic event bus. Events may help with timing and decoupling, but they do not by themselves assign
authority, translate vocabulary, or remove hidden dependencies.

Keep direct platform access for exceptions. This is useful for bring-up and adapter diagnostics, but product paths that
use exceptions as normal behavior make the intended boundary untrue.

Replace the subsystem in one rewrite. This might produce a cleaner endpoint, but it raises risk before the team has
proven the new boundary on one product path.

Postpone boundary work until more variants exist. This preserves short-term speed, but it lets the first vendor's model
become more deeply embedded in product behavior.

## Editor's Commentary

Chapter 14 opens Part III by changing the reader's posture from knowing laws to practicing architecture.

The chapter has no primary PEAK concept. That is intentional. Part II law chapters were organized around primary laws.
This practice chapter is carried by a relationship set: Platform Leakage (`SMELL-005`), HAL Everywhere
(`ANTIPATTERN-002`), Every State Has One Owner (`LAW-001`), Every API Is a Promise (`LAW-002`), Every Dependency Is a
Decision (`LAW-007`), Silent Coupling (`SMELL-001`), Hidden State (`SMELL-004`), Manager Mania (`ANTIPATTERN-004`), God
Module (`ANTIPATTERN-001`), Change Radius (`VOCAB-001` and `METRIC-001`), and ADR (`ARTIFACT-001`).

Those concepts are enough. The chapter does not need a new canon term for architecture boundary, product boundary,
translation edge, boundary contract, back channel, or reason to change. They remain chapter-local language for teaching
the practice.

The boundary with earlier chapters is also deliberate. Chapter 7 owns the full law of state ownership. Chapter 8 owns
API promise semantics. Chapter 9 owns dependency commitment. Chapter 12 owns system-level simplicity. Chapter 13 owns
evidence and revalidation. Chapter 14 uses those ideas to place a boundary; it does not reteach them.

The boundary with later Part III chapters matters even more. Chapter 15 owns the full Change Radius method. Chapter 16
owns failure and recovery design. Chapter 17 owns ADR and RFC practice. Chapter 18 owns Architecture Review. Chapter 19
owns Architecture Freeze. This chapter gives each of those later practices a first object to work on: a decision about
where responsibility, authority, and knowledge should stop crossing.

The reader-facing move is simple: do not ask whether the system has a wrapper. Ask what the wrapper still allows the
rest of the product to know.
