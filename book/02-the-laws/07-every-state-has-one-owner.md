# Every State Has One Owner

## Opening Quote

> A copy can report state. Only an owner can decide it.

## Story

The controller had six modes and too many truths.

On paper, the modes were simple. During startup the device entered `Boot`.
When it could not run safely, it entered `SafeIdle`. When initialization was
complete, it moved to `Ready`. During normal operation it was `Active`. During
service work it could enter `Service`. When an interlock failed or a protection
condition tripped, it moved to `Fault`.

The mode mattered because the device controlled real outputs. In `Active`, it
could energize a motor and open a process valve. In `Service`, it could run
calibration routines with guards that were not appropriate for production
operation. In `SafeIdle`, outputs stayed disabled until the controller had
re-established enough confidence to move forward. The mode was not a label for
the user interface. It was the system's answer to a practical question: what is
this controller allowed to do now?

The first implementation had a runtime state machine in firmware. Commands
arrived, preconditions were checked, transitions were logged, outputs changed,
and the current mode was published to the service interface.

That model did not stay alone.

A persistent field was added so the controller could remember that service work
had been in progress before a restart. The service application cached the mode
so technicians could reconnect quickly after a USB drop. A manufacturing fixture
received a privileged diagnostic command so the line could enter calibration
without walking through the normal service workflow. A supervisory controller
learned to infer mode from outputs and telemetry because the published mode was
sometimes delayed on a busy network.

Each addition had a reason.

The persistent field helped technicians recover context after a reset. The
service cache made the tool feel responsive. The fixture bypass saved seconds on
every unit. The supervisor inference let the plant automation react even when
the service channel was not connected. None of those changes looked like an
architecture decision when it was made. Each one was a local convenience around
the same meaningful state.

Then a watchdog reset happened during a service calibration.

The firmware restarted conservatively and entered `SafeIdle`. That was the
right runtime behavior. The controller had lost execution context, the output
state had been reset, and the state machine needed to revalidate conditions
before it allowed operation.

The persistent field still said `Service`.

The service application reconnected and showed its cached `Service` state before
the controller finished publishing the new mode. The manufacturing fixture still
believed calibration was active because its diagnostic sequence had not received
a clean completion event. The supervisory controller saw several outputs in
their normal ready positions and inferred `Ready`.

Five components now had five plausible answers.

The firmware refused an `Active` transition because it was in `SafeIdle`. The
service application tried to repair the controller back to `Service` because
the technician had not finished. The fixture resent its privileged calibration
write because it assumed the reset had interrupted communication, not authority.
The supervisor requested operation because the outputs looked ready. The
persistent field restored `Service` again after a later reboot, which made the
bug appear to come back from storage.

The logs were not lying. They were worse than lying. They were local.

One log showed the firmware entering `SafeIdle` after watchdog recovery. Another
showed the service tool sending `Service`. A fixture log showed a calibration
command being retried. The supervisor recorded that the controller appeared
ready. Storage showed the last saved mode as `Service`. The team could see what
each component had done. It could not answer the question that mattered most:
which component had been allowed to decide the current operational mode?

The first proposed fixes were familiar.

Synchronize the mode flags more often. Add a retry when the service application
sees disagreement. Persist every transition immediately. Add a timestamp and let
the newest value win. Give every actor a setter but document the order in which
they should use it. Add another Boolean called `modeValid`. Teach the supervisor
to infer the mode again when the reported value looks stale.

Those fixes were attractive because they treated the visible symptom:
disagreement.

They did not treat the cause.

The principal engineer asked the team to stop drawing arrows between copies and
draw a boundary around authority.

"Which value is allowed to be wrong for a while?" she asked.

The service cache could be wrong. It should become stale when the controller
publishes a newer transition. The persistent field could be old. It might
represent boot policy, pending service intent, or history, but it could not be
the runtime truth after a watchdog reset. The supervisor inference could be
useful. It could detect that outputs looked ready. It could not decide that the
controller was ready. The fixture could have privilege. It could request a
bounded calibration transition. It could not bypass the state owner.

The runtime state machine became the sole authority for current operational
mode.

Other components stopped assigning the mode directly. The service tool sent
`RequestServiceMode`. The fixture sent a privileged calibration request through
the same transition boundary. The supervisor could request operation, but it
could not convert an inferred observation into `Ready`. Persistence stored boot
policy, acknowledged service intent, and transition history. It did not own
current runtime mode.

The owner validated transitions. It checked whether outputs were disabled before
entering `Service`. It rejected `Active` while recovery was incomplete. It
accepted fixture requests only through a bounded path with the same invariants.
It published accepted transitions with a sequence number and reset generation so
observers could detect stale values. It recorded rejection reasons so a service
tool could show "recovery incomplete" instead of pretending the command had
vanished.

The reset behavior changed too. After watchdog recovery, the controller entered
`SafeIdle`, loaded only the persisted inputs it actually trusted, and published a
new transition. Cached UI state became a last observation. The fixture had to
request calibration again. The supervisor could report its inferred view, but it
had to treat the published mode and generation as authoritative for commands.

The system did not become smaller. It became less ambiguous.

There were still caches, persistence, telemetry, privileged commands, and
supervisory observations. They did not disappear because copies are useful. What
changed was their role. They could request, observe, remember, infer, and
display. They could not decide current operational mode.

One state had one authority for change.

## Discussion

State is not just stored data.

That is the first mistake in many ownership discussions. A team points to the
field, table, variable, register, or cache where a value lives and says, "There
is the owner." Sometimes that answer is good enough for a local implementation
detail. It is not good enough for meaningful state.

Meaningful state has consequences. Operational mode changes which outputs may
be enabled, which commands are valid, which alarms matter, which recovery path
should run, and which explanation a technician receives. It has valid values,
valid transitions, invariants, history, and failure behavior. The value matters
because the system will do different things depending on what it believes.

That is why Every State Has One Owner (`LAW-001`) is stronger than "keep one
copy." A copy can store a value. An owner decides whether the value is valid,
whether a transition is allowed, what happens when the system is uncertain, and
how other representations should be interpreted.

The owner is semantic authority.

It is not automatically the memory address where the value is stored. It is not
the module that last wrote a field. It is not the thread currently executing. It
is not the database row, the cache, the UI, the service tool, the fixture, the
team that maintains a consumer, or the component with the most convenient
setter.

The owner is the boundary that can answer:

- Is this transition valid?
- Which invariants must hold before it is accepted?
- Who may request the transition?
- What does rejection mean?
- Which value is authoritative now?
- What should observers do with stale or conflicting copies?
- What happens after reset, standby switch, or handoff?

Those questions are architectural because they shape the behavior around the
state. The code that stores the current value is only one part of the answer.

Copies are not the enemy.

Embedded systems often need many representations of the same state. A UI needs
a display value. A service application needs a recent observation. A supervisor
may need a telemetry mirror. A boot path may consult persisted policy. Hardware
may expose shadow state. A gateway may keep the last reported value while a
device sleeps. A test fixture may hold the state it expects while it waits for a
response.

The law does not ban those copies. It asks whether each copy has a declared
role.

Is this value authoritative, requested, applied, observed, reported,
last-known, persisted, cached, derived, or inferred? The chapter does not need a
taxonomy for every project. It needs the distinction because confusion between
those roles creates bugs that look like timing, communication, or tooling
problems.

The service application's cached `Service` mode was useful as a last
observation. It became dangerous when the tool treated it as current authority.
The persisted `Service` field was useful if it meant "service work was
interrupted" or "resume service workflow if the owner accepts it." It became
dangerous when it restored runtime mode by assignment. The supervisor's
inference was useful as a diagnostic signal. It became dangerous when it
converted symptoms into truth.

This is Hidden State (`SMELL-004`) in a common embedded form. State affects
behavior, but the source of authority is not visible through a clear owner,
interface, or model. Each component can explain its local value. The system
cannot explain which value should win.

Multiple writers create policy by accident.

When several components can assign the same meaningful state, each writer starts
carrying a fragment of transition policy. The service tool knows when a
technician wants service. The fixture knows when manufacturing wants
calibration. The supervisor knows when outputs appear ready. Storage knows what
the last saved value was. Firmware knows which interlocks currently hold.

Those facts are not equivalent. A request is not a transition. A persisted value
is not runtime authority. An inferred condition is not permission. If every
component gets a setter, the system no longer has one transition policy. It has
several local policies competing through timing.

That is why raw setters are so expensive. A setter answers the question "What
value should be written?" An intent-level command asks a better question: "What
outcome is being requested, and may the owner accept it now?"

`RequestServiceMode` is different from `mode = Service`. The command carries
intent. The owner can check whether outputs are disabled, whether calibration is
already active, whether recovery is complete, whether the requester has
privilege, and whether the current mode permits the transition. It can accept,
reject, publish, and explain.

`EnterSafeIdle` is different from assigning a flag after an error. It says the
system is moving into a conservative runtime state for a reason the owner can
record. `ApplyValidatedConfiguration` is different from writing configuration
bits into several modules. It gives one boundary responsibility for validation
and resulting state.

This is not the full API-contract argument. Later chapters can discuss
interface promises in depth. Here, the point is narrower: commands protect state
authority because they route change through the boundary that owns validity.

Inference is a subtle form of ownership.

In the story, the supervisory controller inferred `Ready` from outputs and
telemetry. That inference was not foolish. Operators often need useful
interpretations when direct communication is delayed. A system that never
derives state can become slow, noisy, or unusable.

The danger appears when an inferred value starts controlling behavior as if it
were authoritative. If the supervisor uses outputs to decide that the controller
is ready, then requests operation on that basis, it has become an unofficial
owner. If a service application sees a cached mode and repairs the device back
to that value, it has become an owner. If a boot path reads a persisted field and
sets runtime mode without validation, storage has become an owner.

The architecture may not say this. The code may not look like an ownership
transfer. The failure will still behave as if ownership moved.

Global Configuration (`ANTIPATTERN-003`) often creates the same problem. A broad
mode flag starts as a convenient configuration value, then spreads into logging,
calibration, connectivity, power behavior, and service tooling. Soon changing
one setting changes unrelated modules because the configuration has become a
shared state authority without scope, lifecycle, or validation.

One owner does not mean one participant.

Many callers may request a change. Many adapters may receive commands. Many
functions may participate in implementing the transition. Many hardware
operations may be needed before the state is safe to publish. Many replicas and
snapshots may exist. Concurrency may require serialization, arbitration, or a
stronger distributed protocol in some systems.

The law does not say only one function may ever write memory. It says one
authority must decide the valid value and transitions for the state at the
given time and scope.

Scope matters.

During boot, a bootloader may own update mode. After handoff, the application
may own runtime operational mode. During a firmware-update sequence, a recovery
component may own a narrower update state while the application is inactive. In
an active-standby controller pair, the active controller may own current
control state while the standby keeps a replica. During a standby switch,
ownership may transfer.

Those designs can satisfy the law if the transfer is explicit, ordered, and
mutually exclusive at the relevant scope. They violate the law when both sides
believe they may decide the same state at the same time, or when observers
cannot tell which authority is active.

This distinction matters because simplistic centralization is not engineering
judgment. A database is not always the owner. A singleton does not prove
ownership. A state machine class does not automatically establish authority.
Distributed systems do not become correct by pretending distribution does not
exist. The useful question is whether the architecture can name the authority
for the state now, and whether handoff rules prevent two authorities from
overlapping.

Recovery requires choosing authority, not merging guesses.

The hardest ownership bugs often appear after reset, reconnect, partial
failure, controller handoff, or interrupted service. Those are the moments when
representations disagree for understandable reasons. A cache may be old. Storage
may contain the last committed input. A fixture may remember a command in
progress. Hardware may hold a shadow value. Telemetry may arrive out of order.
The UI may display what was true before the link dropped.

If the recovery rule is "merge the best-looking values," the system is asking
copies to vote on truth. That may feel pragmatic, but it often preserves the
ambiguity that caused the failure. Newest-timestamp-wins has the same trap. A
new value is not necessarily an authoritative value. It may be a newer guess.

A better recovery rule starts from ownership. After watchdog reset, the runtime
state machine enters a conservative mode and re-establishes authority. It may
consult persisted boot policy. It may read acknowledged configuration. It may
use hardware observations. It may publish a recovery transition and reject
requests until invariants hold. But it does not let an old cache, inferred
state, or persisted last value assign current operational mode directly.

That distinction makes failures explainable. A rejected command can say
"recovery incomplete" or "service request denied because outputs are not
disabled." A stale UI value can be marked stale because its generation is older
than the published transition. A fixture can know that its previous calibration
intent did not survive reset as authority. A supervisor can report that outputs
look ready while still treating the runtime owner as the decision boundary for
operation.

State ownership should be discoverable.

Discoverability (`METRIC-003`) is not decorative documentation. It is how a
future engineer avoids rediscovering authority through incidents. For a
meaningful state, the repository should make it possible to find the owner, the
valid values, the invariants, the commands, the published observations, the
persistence semantics, the reset rule, the handoff rule, and the tests that
prove invalid transitions are rejected.

An ADR (`ARTIFACT-001`) is a good place to record the ownership decision when it
affects architecture, cost, or reversibility. An Event Catalog (`ARTIFACT-005`)
can record the events that publish accepted transitions, their producer,
consumers, ordering assumptions, and failure behavior. The important point is
not ceremony. It is that the next engineer should not have to infer authority
from the most convenient setter.

The payoff is practical.

One owner reduces coordination cost because every participant knows which role
it has. Callers request. The owner decides. Observers observe. Caches remember
with freshness limits. Persistence stores what it owns. Derived values explain
their derivation. Recovery chooses authority instead of merging guesses.

The system may still be complex. It may still be concurrent. It may still be
distributed. But the question "who decides this state?" has an answer.

That answer is what turns a mode from a collection of flags into architecture.

## Engineering Principle

For every meaningful state, name one authority that validates its value and
controls its transitions. Other components may request, observe, cache, persist,
replicate, or derive that state, but they must not become competing sources of
truth.

The principle is reviewable because it turns an abstract ownership claim into
concrete questions:

1. What exact state is being discussed?
2. What does that state mean to the system or product?
3. What values are valid?
4. What invariants define safe or correct transitions?
5. Who owns the transitions?
6. Who may request a change?
7. Which representations are observations, caches, persistence, or derivations?
8. What happens after reset, reconnect, partial failure, or stale restoration?
9. How are stale or conflicting observations detected?
10. How is ownership transferred across lifecycle boundaries?
11. Where is the decision recorded so another engineer can find it?

The trade-off is that one authority often requires more explicit interfaces.
Callers may need commands instead of setters. Observers may need versions or
generations. Persistence may need a narrower responsibility. Fixtures may need
privileged paths that still respect invariants. Those costs are real.

The alternative is worse: every copy carries a little policy, every repair path
becomes a writer, and recovery becomes a negotiation among stale values.

## Architecture Exercise

### Trace One State to One Owner

Choose one meaningful state from a system you work on. Do not choose a trivial
local variable. Choose state whose value changes behavior: operational mode,
configuration state, calibration state, connection state, update state, safety
interlock state, entitlement state, or another value with consequences.

Write short answers to these prompts:

1. What is the state's exact name and scope?
2. What does it mean to the product or system?
3. What values are valid?
4. What invariants must always hold?
5. Which transitions are valid?
6. Which boundary currently decides whether a transition is accepted?
7. Which components can currently write or repair the value?
8. Which components may request a change?
9. Which components observe it?
10. Where is it persisted?
11. Which caches, UI projections, telemetry mirrors, or derived values exist?
12. Which components infer the state from symptoms?
13. What happens after reset, reconnect, standby switch, or partial failure?
14. When can ownership transfer, and how is overlap prevented?
15. What evidence identifies the owner?
16. Which duplicate writers or unofficial owners should be removed?
17. Which commands request change, and which observations publish accepted state?
18. Which tests prove invalid transitions are rejected?
19. Which ADR or existing artifact records the decision?

End with this question:

What copy of this state currently behaves like an owner without being named as
one?

## Principal's Notebook

- Copies are not owners.
- A setter is not authority.
- Recovery needs a named truth.

## ADR

### Chapter ADR: Make the Device Mode State Machine the Sole Authority for Operational Mode

### Context

The industrial controller's current operational mode is duplicated across the
runtime state machine, persistent storage, service tooling, fixture logic, and
supervisory inference. Several components can assign or repair mode. Watchdog
reset, interrupted service, and reconnect sequences expose disagreement between
`SafeIdle`, `Service`, and inferred `Ready`.

Validation rules are inconsistent. Some paths check interlocks and recovery
state. Others write a raw mode value because they assume they are restoring the
truth. Logs show local actions but cannot reliably explain which component made
the authoritative decision.

### Decision

Make the controller runtime state machine the sole authority for current
operational mode.

Replace external raw mode setters with intent-level commands such as
`RequestServiceMode`, `EnterSafeIdle`, and fixture calibration requests routed
through the same transition boundary. Validate preconditions and invariants in
the owner. Publish accepted transitions with a sequence, generation, or
transition identity sufficient for observers to detect stale values.

Define persistence as input, policy, or history according to its own
responsibility, not as a second runtime owner. Define fixture privilege through
bounded commands rather than bypass assignment. Document reset recovery and any
ownership handoff so only one authority controls current mode at a given time
and scope.

### Consequences

Operational-mode invariants now have one reviewable home. Invalid commands can
be rejected with explainable reasons. Service tooling, fixtures, supervisors,
and UI surfaces can distinguish requests and observations from authority.
Reset behavior becomes clearer because recovery starts by re-establishing the
runtime owner instead of merging stale guesses. Tests can exercise invalid
transitions at one boundary.

This decision requires migration work. Existing writers must be converted to
commands. Service tools may need compatibility handling while older firmware
still exposes raw setters. The owner may need queueing or serialization around
concurrent requests. Observers need version, generation, or transition identity
where stale values matter. Ownership handoff requires explicit design. The
state-machine boundary must stay focused so it does not become a god object for
every operational concern.

### Alternatives Considered

Keep multiple writers and synchronize them more frequently. This preserves the
current ambiguity and only moves conflicting values faster.

Let the newest timestamp win. This can be useful for observations, but a newer
value may still be a newer guess rather than an authoritative transition.

Make persistent storage authoritative at all times. This would make reset
simple, but it would treat a stored value as runtime truth even when current
interlocks, outputs, or recovery state disagree.

Infer current mode from outputs. This can help diagnose disagreement, but it
turns symptoms into authority and cannot explain why a transition was valid.

Use a distributed ownership protocol. That may be appropriate for systems where
state authority is genuinely distributed, but this controller has one runtime
authority for current operational mode. A broader protocol would add complexity
without solving the immediate ownership gap.

## Editor's Commentary

Chapter 7 opens Part II by turning a question that appeared earlier into a law.
Chapter 3 used stale state to show how better questions expose ownership gaps.
Chapter 4 used ownership to mean responsibility for closing an engineering
outcome. This chapter uses ownership in a narrower architectural sense:
authority over a meaningful state and its valid transitions.

That distinction matters for the rest of the book. Many later chapters will use
state ownership as a premise. API promises, dependency direction, time,
simplicity, evidence, product configuration, observability, and legacy recovery
all become harder when meaningful state has several unofficial authorities.

The chapter starts Part II because the law is both small and unforgiving. It
does not require one physical copy, one global variable, one database row, or
one thread. It requires one clear authority at the relevant time and scope.

The PEAK concepts carrying this chapter are Every State Has One Owner
(`LAW-001`), Hidden State (`SMELL-004`), Global Configuration
(`ANTIPATTERN-003`), ADR (`ARTIFACT-001`), Event Catalog (`ARTIFACT-005`), and
Discoverability (`METRIC-003`). They are enough. The chapter does not need a new
artifact or vocabulary term to teach the law.
