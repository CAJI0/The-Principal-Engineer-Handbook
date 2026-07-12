# Simplicity Is a Feature

## Opening Quote

> A simple system is not the one with the fewest parts. It is the one whose consequences can still be explained.

## Story

The command path looked clean when the controller first shipped.

An input arrived from the service interface. The command was validated. The runtime state owner decided whether the
command was allowed. If it was allowed, the hardware command was issued. When the hardware reported a result, the
controller recorded the outcome and sent a diagnostic back to the caller.

That path was not glamorous. It was direct.

The product behavior was easy to explain. A command either failed validation, was rejected by the state owner, was sent
to hardware, completed, failed, or entered recovery. The service tool could show a reason. The firmware logs could show
which state mattered. Tests could describe the product rule without reproducing every internal hop.

Then the product grew.

A second entry path arrived for manufacturing. A UI path needed more immediate feedback. A field-service command needed
different diagnostic text. A hardware revision needed a wrapper around a changed driver. A new configuration file routed
some commands differently for one product variant. A recovery path needed to remember a late hardware completion. A
support request asked for a fallback path when the service interface disconnected during calibration.

None of those changes was foolish.

The team added a global service locator so command code did not have to thread dependencies through every call. It added
manager modules so the UI, service, manufacturing, and recovery paths had a common place to call. It added generic
command objects so commands could move through queues and callbacks. It added callback registries so the hardware layer
could report completion without blocking. It added event forwarding so the service tool and logs could hear about the
same operation.

The path kept collecting reasonable pieces. Platform wrappers kept product code away from hardware headers.
Configuration-driven routing let one command family be steered without rebuilding. Utility helpers normalized command
names, diagnostic labels, and retry decisions. Pass-through adapters protected callers that still expected the old
shape. Fallback paths and a shared context object helped recovery know what had happened earlier.

Each addition solved a local problem.

The code still looked organized in a diagram. There were boxes for managers, adapters, command objects, routers,
platform wrappers, and utilities. No box looked absurd. Most methods were short. Several classes had only one obvious
job. Reviewers could still say, with some confidence, that each local piece was tidy.

Then a field issue required a small change.

Reject one unsafe command while calibration is active, but preserve diagnostics and existing recovery behavior.

The command controlled an output that was normally safe after validation. During calibration, however, the same command
could move hardware in a way that invalidated the calibration result. The product rule was narrow: while calibration is
active, reject that one command before hardware execution starts, report a clear reason, and leave the recovery behavior
for already-started hardware work unchanged.

It sounded like a one-condition patch.

The engineer assigned the patch opened the UI command manager and found a calibration flag, but the flag was not
authoritative. It was a display hint cached from the last event. The service path entered through a different manager
and used a utility helper to decide whether a command could be sent onward. Manufacturing bypassed that helper because
the line needed privileged calibration access. The fallback path passed through a generic command object whose fields
used platform names rather than product names. The callback registry could report a hardware completion after the command
manager had already returned. The event forwarding path updated diagnostics after the utility helper had accepted the
command. A global context flag recorded whether recovery was in progress, but one adapter read it before configuration
routing and another read it after.

The acceptance decision depended on UI state, configuration, manager state, callback order, a global context flag, a
utility helper, a platform wrapper, deferred hardware completion, and logging side effects.

No single component could explain why the command was accepted or rejected.

Several entry paths encoded similar rules with different names. The UI path spoke about "enabled actions." The service
path spoke about "commands ready to send." The manufacturing path spoke about "privileged operations." The hardware
wrapper spoke about "driver-ready requests." The utility helper spoke about "safe routing." The shared context object
spoke about "calibration hints." They were all near the same product decision, but none of them owned it.

Tests did not help as much as the team expected.

The command manager tests mocked the router. The router tests mocked the utility helper. The utility tests mocked
configuration. The platform wrapper tests mocked the driver. The callback tests asserted completion order. The service
tool tests checked that a diagnostic string appeared. Those tests proved that layers forwarded values to other layers.
They did not prove the product behavior: a command is rejected while calibration is active, hardware is not started, the
diagnostic explains the reason, and recovery for already-started work remains intact.

The logs had the same problem.

They showed "UI command received," "manager accepted," "route selected," "callback registered," "platform request
started," "event forwarded," and "diagnostic emitted." During the field issue, support did not need a list of
infrastructure hops. Support needed to know which command was considered, which calibration state mattered, who made the
acceptance decision, whether hardware execution had started, whether completion was deferred, and whether recovery was
required.

The first proposed fixes were familiar.

"Add another manager for calibration."

"Add a callback before dispatch."

"Put a Boolean in the shared context."

"Introduce a generic policy interface."

"Route every command through one central module."

"Move the rule into the utility helper."

"Document the call sequence."

"Add more mocks."

"Rewrite the command system in a new framework."

"Duplicate the command path for calibration mode."

Each response reduced discomfort in one place. None of them made the product decision easier to explain end to end. A
new manager would add another forwarding layer unless it owned the decision. A new callback would make ordering more
important. A Boolean would create another hidden dependency. A generic policy interface might hide the product rule
behind broader vocabulary. A central module could become one more place where unrelated decisions gathered. A utility
helper would make Utility Gravity (`SMELL-002`) worse by letting a convenient helper accumulate product decisions. More
mocks would prove the mechanics of forwarding, not the rule. A rewrite would risk replacing unclear concepts with new
unclear concepts. A duplicated calibration path would make the same product command mean different things in different
places.

The Principal Engineer changed the question.

The team had been asking, "Where should this condition go?"

She asked, "What product decision is being made, who owns it, and what is the shortest truthful path from input to
consequence?"

That question made the work smaller and deeper at the same time.

The product decision was not "call the manager." It was not "route the event." It was not "invoke the callback." It was
not "set platform state." The decision was: accept or reject a product command while calibration is active, while
preserving recovery and diagnostics.

The owner was not the UI cache, the router, the utility helper, the platform wrapper, or the callback registry. The
runtime state owner already owned whether calibration was active and which commands were allowed during that state. That
owner did not need to issue every hardware call or format every log message. It did need to own the acceptance decision.

The team mapped the real decision path.

They marked every place where the command changed meaning. They marked every pass-through abstraction. They marked every
duplicated rule. They marked every place platform vocabulary had crossed into product logic. They marked callbacks whose
ordering affected ordinary control flow. The map showed Manager Mania (`ANTIPATTERN-004`) because several manager layers
coordinated behavior without clear domain ownership. It showed Silent Coupling (`SMELL-001`) because callbacks,
configuration, utilities, diagnostics, and global context all had to agree without an explicit contract. It showed
Platform Leakage (`SMELL-005`) because driver vocabulary had shaped product acceptance rules. It showed Callback Hell
(`ANTIPATTERN-005`) because ordinary command behavior was spread across asynchronous callbacks and event forwarding.

The new shape was not a rewrite.

The team defined one explicit acceptance boundary owned by the product state owner. The boundary used product language:
command accepted, rejected because calibration is active, invalid input, hardware execution started, hardware execution
failed, completion deferred, completion timed out, late completion, recovery required, and unknown outcome. The UI,
service, manufacturing, and fallback entry paths migrated toward that boundary. The platform wrapper stayed behind a
bounded integration edge. It translated hardware execution and completion; it did not decide whether calibration made the
product command unsafe.

The ordinary path became visible again.

Input arrived. Validation checked the command shape. The product state owner made the acceptance decision. If accepted,
the hardware integration edge started execution. Completion could be immediate or deferred. The result was reported in
product language. Diagnostics were emitted at the decision point and at hardware completion, with the two facts kept
separate.

The exceptional paths stayed distinct.

Rejected because calibration is active was not the same as invalid input. Hardware execution failed was not the same as
hardware completion deferred. A timeout waiting for completion was not the same as a late completion. A late completion
was not the same as cancellation. Recovery required was not the same as unknown outcome. The team did not erase
essential hardware and recovery behavior in the name of simplicity. It removed accidental concepts around the decision.

Tests changed in the same direction.

Instead of mocking every manager in sequence, product-level tests described the behavior: accept the command when
calibration is inactive; reject it when calibration is active; do not start hardware after rejection; preserve deferred
completion for a command already started; report recovery when completion arrives late; emit diagnostics that explain
the decision. Integration tests still covered the platform wrapper and callback behavior. Mocks did not disappear. They
stopped being the main evidence for the product rule.

The change radius shrank in a way reviewers could see.

The first patch would have touched managers, utilities, configuration, callback order, platform wrappers, logs, mocks,
and recovery code. The new decision touched the state owner, entry-path migration points, product behavior tests,
diagnostics, and the bounded hardware edge. Some familiar abstractions disappeared. Some stayed because they still
transformed behavior. The team removed pass-through layers only where evidence showed they were adding concepts without
owning decisions.

The ADR was short because the decision was finally clear.

Collapse command routing into one product-owned decision path. Keep platform execution behind a bounded edge. Preserve
asynchronous completion. Emit diagnostics where the decision is made. Migrate entry paths incrementally. Remove accidental
forwarding where it no longer earns its keep.

The system did not become tiny.

It became explainable.

## Discussion

`LAW-004` states: Simplicity is a product capability because it makes future change safer.

That sentence is easy to admire and easy to weaken. If simplicity becomes a matter of taste, the chapter becomes a style
argument. If simplicity becomes a count of lines, files, layers, diagrams, or abstractions, the system can look simple
while remaining hard to change. If simplicity means whatever feels familiar to the current team, it becomes local
comfort rather than product capability.

Simplicity is the property that lets important behavior be explained, changed, tested, operated, diagnosed, and recovered
with a small, truthful set of concepts.

The word truthful matters.

A simplistic design removes distinctions the product still needs. One generic `status` can look cleaner than separate
outcomes for rejected input, rejected state, hardware failure, deferred completion, late completion, and recovery. It is
not simpler if the support tool, recovery code, and tests have to rediscover those distinctions somewhere else. One
universal manager can look cleaner than several product boundaries. It is not simpler if it hides who owns each
decision. One event stream can look cleaner than direct calls. It is not simpler if ordinary behavior can only be
understood by reconstructing callback order.

Simple does not mean short.

Concise code has few words or lines. Compact code carries more meaning in less space. Easy code is familiar, locally
convenient, quick to call, or quick to patch. Explicit code makes ownership, state, boundary, decision, or consequence
visible. Understandable code can be explained by the intended maintainers under real pressure.

Those qualities can support simplicity. They are not the same thing.

A global helper may be easy to call and make the system less simple. A small explicit boundary may require more code now
and make future behavior easier to change. A compact abstraction may hide a product decision. A longer function may be
more explicit than a chain of generic forwarding calls. Verbosity is not a virtue by itself. The goal is truthful
explanation.

The product pays for every concept that must be understood together.

In the story, the unsafe-command change was small as product behavior. It became expensive because the decision was
distributed across UI state, configuration, managers, callbacks, utilities, platform wrappers, logs, and global context.
Those concepts did not all exist because someone had made a bad decision. They accumulated through reasonable local
decisions. A local convenience became a system cost when it joined the set of things a future engineer had to understand
before changing one rule safely.

That is why simplicity is a system-level property.

A local abstraction can reduce code in one module while increasing the number of concepts required across the product. A
locally repetitive implementation can sometimes be simpler than premature unification if it keeps two product decisions
separate. Duplication is not automatically good. Unification is not automatically good. The question is whether the
result reduces truthful reasoning or merely moves complexity into a place with a cleaner name.

Essential complexity comes from real product needs.

Embedded and long-lived systems have hardware constraints, protocols, timing, safety behavior, manufacturing flows,
field lifetime, recovery obligations, support tools, and operational constraints. Those do not vanish because a team
wants a simpler diagram. Deferred hardware completion is real. Late completion can matter. Calibration state can make a
command unsafe. Recovery may need to distinguish rejection from failure. Platform integration may need driver-specific
knowledge behind a boundary.

Accidental complexity comes from extra concepts the product did not need.

Manager layers that only forward calls. Utility areas that accumulate product decisions. Event routing that hides
ordinary control flow. Callback chains that make ordering implicit. Configuration that recreates code structure at
runtime. Platform terms that leak into product acceptance. Shared context flags that become unofficial contracts.
Generic command objects that erase product vocabulary. Pass-through adapters that preserve old shapes without reducing
change radius.

Simplicity preserves essential complexity and removes accidental concepts.

That sentence sounds clean. In practice, it requires judgment. Removing a platform wrapper and calling hardware directly
from product logic may feel simpler for one change, but it can increase Platform Leakage. Keeping a wrapper may be
simpler if it protects product code from driver vocabulary and failure detail. Removing all callbacks may be impossible
or wrong when hardware completion is genuinely asynchronous. Naming the completion semantics and limiting where callback
ordering affects product behavior may be the simpler design.

Abstraction earns its place when it names a stable concept, protects a meaningful boundary, reduces duplicated
reasoning, narrows Change Radius, preserves dependency direction, clarifies ownership, improves testability, or keeps
platform details behind a product-level edge.

Abstraction harms simplicity when it hides ordinary control flow, generalizes one case without evidence, mirrors
platform vocabulary, adds managers or registries without reducing system concepts, spreads generic terms into product
logic, creates extension points no owned variation uses, or makes diagnostics describe forwarding steps instead of
decisions.

The count of abstractions is not the metric.

The metric is whether a future change has fewer truthful concepts to understand.

Change Radius (`VOCAB-001` and `METRIC-001`) is a practical signal. A design is not simple if one small product-rule
change touches unrelated managers, event infrastructure, configuration, utility modules, platform wrappers, mocks, logs,
support tooling, and recovery code. That radius tells the team where the architecture has made one decision depend on
too many surfaces.

Change Radius is not only a file count. It is the amount of system surface that must change, be reviewed, or be retested
when one decision changes. In the command story, the important question was not "how many files will the patch touch?"
It was "which behavior, ownership, tests, diagnostics, tools, and recovery paths must move for the rule to be safe?"

Discoverability (`METRIC-003`) is another signal.

A future engineer should be able to find the decision, owner, and contract behind important behavior. Search may find a
manager, a callback, or a helper. That is not enough if it cannot reveal why the command is accepted, who owns the
acceptance rule, which state matters, what diagnostics mean, and which tests prove the rule. Poor discoverability turns
maintenance into archaeology. Simple systems reduce the amount of archaeology required before a safe change.

Architecture Health (`VOCAB-007` and `METRIC-005`) gives the broader product connection. A healthy architecture can
absorb necessary change at acceptable cost. Simplicity supports that health because visible behavior, bounded ownership,
and direct decision paths make change less disproportionate. The feature is not developer happiness. The feature is a
product that can be corrected, extended, diagnosed, released, supported, and recovered without every small rule becoming
a cross-system expedition.

Tests and diagnostics reveal whether simplicity is real.

Tests that mock forwarding layers may be useful for local mechanics, but they are weak evidence for product behavior.
If the rule is "reject this command while calibration is active," then a useful test should say that directly. It should
prove whether hardware started, which state mattered, what diagnostic was emitted, and what recovery behavior remained.
Forwarding mocks can support that evidence. They should not replace it.

Diagnostics should answer product questions. Which command was considered? Which state mattered? Who made the decision?
Why was the command accepted or rejected? Did hardware execution start? Was completion deferred? Is recovery required?
Logs that list infrastructure hops are sometimes helpful for debugging local plumbing. They are not enough when support
needs to explain product behavior under pressure.

Deletion and narrowing are design work.

Removing a pass-through adapter, narrowing a utility helper, renaming a generic status, or migrating entry paths to one
decision boundary can be architectural work when it reduces accidental concepts. It should be done with evidence and
scope. This chapter is not a deletion ritual, an option audit, or a legacy migration playbook. Chapter 11 owns unused
options, unsupported modes, dormant paths, combinatorial variation, and evidence for retained flexibility. Chapter 12
uses removal only where it serves a different purpose: making product behavior easier to explain and safely change.

The boundary with the next chapter matters too. Chapter 13 will own evidence quality and confidence. This chapter can
use tests, diagnostics, Change Radius, and the ability to explain behavior as signals of simplicity. It should not become
the full model for proof.

Simplicity must be maintained as the product evolves.

A system can begin with a direct command path and become hard to understand through reasonable additions. That does not
mean the original team failed. It means simplicity is not a one-time property. It is maintained through review, naming,
narrowing, migration, ownership, product vocabulary, and refusal to keep accidental concepts merely because they are
familiar.

The Principal Engineer's habit is to ask for the product decision.

What behavior is changing? Who owns the decision? What is the ordinary path from input to consequence? Which paths are
exceptional on purpose? Which concepts must be understood together? Which layer transforms the behavior, and which layer
only forwards it? Where has platform vocabulary leaked? Which tests prove product behavior? Which diagnostics explain
the decision? What is the true Change Radius?

Those questions make simplicity operational.

The design that wins is not automatically the shortest, flattest, cleverest, most abstract, most direct, or most
familiar. Prefer the design that makes product behavior, ownership, and consequences easiest to explain and safely
change. Preserve essential complexity; remove accidental concepts.

That is how simplicity becomes a feature.

## Engineering Principle

Prefer the design that makes product behavior, ownership, and consequences easiest to explain and safely change.
Preserve essential complexity; remove accidental concepts.

Use this principle as a review habit:

1. What product decision is being made?
2. Who owns that decision?
3. What is the ordinary path from input to consequence?
4. Which exceptional paths must remain distinct?
5. Which concepts must be understood together?
6. Which layers transform behavior, and which only forward it?
7. Where does platform vocabulary leak into product policy?
8. What is the true Change Radius?
9. Do tests prove product behavior or architecture mechanics?
10. Can diagnostics explain why the decision occurred?
11. Which complexity is essential?
12. Which concept can be removed, narrowed, or renamed?

The point is not to make every design flat. The point is to make the important behavior reviewable before the next
change arrives under pressure.

## Architecture Exercise

### Explain One Behavior End to End

Choose one important product behavior from a system you know. Pick behavior that crosses more than one boundary: a
command, state transition, recovery action, manufacturing flow, service-tool operation, hardware interaction, or
diagnostic decision.

Write short answers to these prompts:

1. What trigger starts the behavior?
2. What inputs arrive?
3. Who owns the decision?
4. Which state must be known before the decision is safe?
5. What is the ordinary control path from input to consequence?
6. Which exceptional paths must stay distinct?
7. Where is the hardware or platform boundary?
8. Which dependencies shape the behavior?
9. Which side effects occur?
10. Does the operation complete immediately or later?
11. What can fail, and what recovery behavior follows?
12. Which diagnostics explain the decision?
13. Which tests prove the product behavior?
14. Which files, modules, services, tools, or teams are involved?
15. Which vocabulary does the path use?
16. What is the Change Radius for one realistic modification?
17. Which layers transform behavior?
18. Which layers only forward behavior?
19. Where do duplicated policies exist?
20. Which hidden state affects the outcome?
21. Which concepts can be removed, narrowed, or renamed?
22. Where should the decision be recorded if it affects future architecture?

End with one small, reviewable simplification decision:

- remove one pass-through layer;
- move one rule to the owner;
- rename one generic outcome in product language;
- narrow one utility helper;
- align one test with product behavior;
- emit one diagnostic at the decision point;
- record one scoped ADR.

Do not create a new scoring system or artifact for the exercise. Use the records and review paths the system already
has.

## Principal's Notebook

- Simple survives incident pressure.
- Easy now can be expensive later.
- Remove concepts, not truth.

## ADR

### Chapter ADR: Collapse Command Routing into One Product-Owned Decision Path

### Context

An embedded control subsystem accepts commands through UI, service, manufacturing, and recovery entry paths. The command
path has grown manager modules, generic command objects, callback registries, event forwarding, configuration-driven
routing, utility helpers, pass-through adapters, platform wrappers, fallback paths, and shared context state.

One field issue requires a narrow product rule: reject one unsafe command while calibration is active, but preserve
diagnostics and existing recovery behavior.

The current design cannot explain that rule in one place. Different entry paths apply similar but inconsistent
acceptance logic. Tests verify forwarding through managers and callbacks more than product behavior. Diagnostics show
infrastructure hops but do not reliably explain why a command was accepted or rejected. Hardware completion may be
deferred, and recovery depends on whether execution already started.

### Decision

Assign command acceptance to the product state owner that owns calibration state and command validity.

Define one product-level command vocabulary: invalid input, accepted, rejected because calibration is active, hardware
execution started, hardware execution failed, completion deferred, completion timed out, late completion, recovery
required, cancellation, and unknown outcome. Use that vocabulary at entry paths, tests, and diagnostics.

Create one explicit acceptance boundary. UI, service, manufacturing, and fallback paths request command acceptance
through that boundary instead of duplicating product policy. Keep hardware calls behind one bounded integration edge. The
integration edge translates platform execution and completion behavior; it does not decide product acceptance.

Remove pass-through manager, adapter, utility, and callback layers where evidence shows they only forward the decision
or hide ownership. Preserve manager or adapter code that still transforms behavior, protects a boundary, or supports
migration. Preserve asynchronous hardware completion and the recovery distinctions that depend on it.

Align tests with product-level behavior: accepted command, rejected command during calibration, invalid input, hardware
failure, deferred completion, late completion, recovery behavior, and diagnostic content. Keep lower-level tests for the
platform edge and callback mechanics.

Emit diagnostics at the decision point and at hardware completion. Diagnostics should identify the command, relevant
state, decision owner, acceptance result, hardware-start status, deferred completion, and recovery requirement.

Migrate entry paths incrementally. Record this routing decision in an ADR (`ARTIFACT-001`) because it affects ownership,
future change cost, tests, diagnostics, and recovery behavior.

### Consequences

The product decision becomes discoverable. Engineers can find who owns command acceptance, what state matters, which
outcomes are distinct, and which tests prove the behavior. The system has fewer accidental concepts around one command
rule. Change Radius falls because a product acceptance change no longer requires coordinated edits across unrelated
managers, utilities, callback order, configuration, mocks, and log text.

Diagnostics become more useful during field support. Logs can explain why the command was rejected before hardware
execution or why recovery was needed after deferred completion. Reviewers can separate product policy from platform
execution. New engineers can ramp up by following the ordinary path rather than reconstructing a call chain from
forwarding layers.

The decision creates work. Existing entry paths need migration. Familiar managers, helpers, and callbacks may disappear
or narrow. Some product-specific code becomes more explicit. Old tests that proved forwarding mechanics need to be
rewritten around behavior. During migration, old and new paths may coexist temporarily. The team must preserve essential
asynchronous hardware behavior and recovery distinctions. The acceptance boundary must stay focused so it does not grow
into a new central module for every command concern.

### Alternatives Considered

Add another policy manager. This could create a named place for the condition, but it may add Manager Mania if the new
manager coordinates without owning calibration state or command acceptance.

Add calibration state to global context. This is easy to read from existing code, but it hides authority and creates
Silent Coupling across entry paths, callbacks, diagnostics, and recovery.

Route all commands through a generic event bus. This may help decouple producers and consumers, but it can hide ordinary
control flow and make ordering part of the product rule unless the acceptance decision remains explicit.

Duplicate command logic per entry point. This can move fast for one patch, but it makes UI, service, manufacturing, and
recovery behavior drift.

Rewrite the subsystem. This might eventually produce a cleaner design, but the current evidence supports a scoped
routing decision, not a framework replacement.

Document the existing call chains. Better documentation can improve discoverability, but it does not remove duplicated
policies, hidden ordering, or product decisions trapped in utilities and managers.

Make the driver responsible for product acceptance. This keeps the rule near hardware execution, but it moves product
policy into platform vocabulary and increases Platform Leakage.

Introduce a generic rules framework. This may be useful for a product with many owned rule variations. Here it would add
another concept before the team has evidence that the extra generality reduces reasoning.

## Editor's Commentary

Chapter 12 continues Part II by turning several earlier laws into one product-level property: the ability to understand
and change important behavior safely.

Chapter 7 owns state authority. Chapter 12 relies on the state owner as a simplicity mechanism, but it does not reteach
the one-owner law. Chapter 8 owns API promises. Chapter 12 may prefer product vocabulary and narrower boundaries, but it
does not retell compatibility or versioning. Chapter 9 owns dependency commitments. Chapter 12 uses dependency spread
only as one way concepts increase. Chapter 10 owns time. Chapter 12 mentions callback order and deferred completion only
where they make command behavior harder to explain.

The boundary with Chapter 11 is deliberate. Chapter 11 owns unused options, unsupported modes, dormant paths,
combinatorial variation, and evidence for retained flexibility. Chapter 12 owns comprehensibility, visible behavior,
direct decision paths, bounded concepts, easier operation, safer change, clearer recovery, and better review. Removing a
pass-through layer may be one simplification technique, but this is not another optionality audit.

The boundary with Chapter 13 is also deliberate. This chapter uses tests, diagnostics, Change Radius, and the ability to
explain behavior as signals that simplicity is real. It does not teach evidence quality, confidence calibration,
experiments, or proof standards.

The PEAK concepts carrying the chapter are Simplicity Is a Feature (`LAW-004`), Utility Gravity (`SMELL-002`), Manager
Mania (`ANTIPATTERN-004`), Silent Coupling (`SMELL-001`), Platform Leakage (`SMELL-005`), Callback Hell
(`ANTIPATTERN-005`), Change Radius (`VOCAB-001` and `METRIC-001`), Discoverability (`METRIC-003`), Architecture Health
(`VOCAB-007` and `METRIC-005`), and ADR (`ARTIFACT-001`). They are enough. The chapter does not need a new concept
budget, simplicity score, explanation map, layer tax, or complexity ledger to teach the law.

The reader-facing move is durable: do not ask whether the design looks small. Ask whether the product decision,
ownership, and consequences can still be explained and safely changed.
