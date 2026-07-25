# Finding Silent Coupling

## Opening Quote

> A change is not local because the code is local. It is local only after the behavior's hidden dependents have been
> named.

## Story

The Change That Broke Nothing Locally began with a review nobody expected to be interesting.

A firmware team needed to adjust device registration for a legacy controller. A new peripheral module sometimes took a
little longer to report readiness after cold startup. The firmware change was small: accept one transitional readiness
state, wait through one extra retry window, and then continue through the existing registration path.

The modified code belonged to one component.

The visible API signature did not change.

The unit tests passed.

The service diagram did not show a large risk. The controller spoke to the module. The controller reported status to
the backend. The service tool read diagnostics from the controller. Manufacturing had a script that checked the same
registration sequence during final test. Support had a field procedure for devices that did not come online after an
upgrade. All of those surfaces were known, but nothing in the diagram said they had to change together.

The pull request looked disciplined.

It changed a state transition from `WAITING_FOR_READY` to `WAITING_FOR_READY_OR_PENDING`. It preserved the existing
error code. It added firmware tests for the new peripheral. It left the backend API payload unchanged. The reviewer
asked whether the extra retry could delay failure reporting. The author showed the timing budget. The reviewer asked
whether old peripherals still registered. The author showed the compatibility test. The change shipped into release
validation.

Nothing broke locally.

Then the service tool failed to recognize a recoverable startup state.

The tool was not calling the firmware function. It was not linked to the firmware package. It was not mentioned by the
import graph. It watched a diagnostic stream and looked for one state name before offering the technician a recovery
action. The firmware change had kept the old error code, but the diagnostic sequence now emitted the transitional
state where the tool expected a stable waiting state. The device was healthy. The technician workflow was not.

The backend team saw a different symptom.

Their mapper still accepted the same status payload. No contract test failed. But one backend rule treated the old
waiting state as a delayed module and the new transitional state as an unknown report. That difference mattered only
during upgrade, when old module firmware and new controller firmware could run together for a few minutes. The mapper
had been added after an earlier release nearly delayed shipment because customers upgraded sites in an order the
original design did not expect.

Manufacturing saw a third symptom.

Their final-test script read the diagnostic stream because it was faster than waiting for the backend report. The script
looked for the previous state ordering: module detected, waiting, ready, registered. The new state inserted itself
between waiting and ready. The hardware still passed its electrical tests. The script marked the unit as inconclusive.
The line lead did not know whether to rerun, quarantine, or override the result.

The firmware team was surprised in a precise way.

They had not broken an interface they knew about. They had broken a relationship nobody had named as an interface.

The first conversation sounded familiar.

"Why is the service tool parsing that diagnostic?"

"Why is the backend mapping a firmware state that is not in the API?"

"Why is manufacturing depending on field ordering?"

"Why did support write a recovery procedure around a phrase from a log?"

Each question was fair. None of them made the release safer by itself.

Mara, the Principal Engineer, stopped the discussion before it became a search for the first team to blame.

"The problem is not that one team did something strange," she said. "The problem is that the behavior has dependents we
did not know to review."

She asked the team to stop tracing files and start tracing behavior.

The behavior was not "a firmware state transition changed." That was the local edit. The behavior was "a controller
communicates whether a peripheral is still recoverable during startup, and several surfaces interpret that signal."

They wrote that sentence at the top of a short coupling map.

Then they listed the surfaces that assumed the behavior.

Firmware owned the registration state machine. The peripheral supplied readiness signals. The backend mapped the
reported status into fleet state. The service tool interpreted diagnostics for a technician. The manufacturing script
interpreted event order during final test. Support interpreted the same words as a recovery instruction. Release
validation interpreted the sequence as evidence that old and new versions could coexist.

Those were not equal dependents. Some depended on a product promise. Some depended on a shortcut. Some depended on a
temporary solution that had outlived its original owner. But they were all real enough to break.

Mara asked for evidence before confidence.

The team checked the service-tool repository and found the state-name parser. They checked backend mappings and found
the upgrade rule. They checked manufacturing scripts and found the event-order check. They checked release notes and
found a sentence from three years earlier: "Controller startup diagnostics remain compatible with service recovery
workflow." They checked the support article and found the exact phrase technicians had been taught to wait for. They
checked the Architecture Ledger and found an old row saying, "Device registration fallback remains until upgrade data
shows it is safe to retire." The row had no current owner.

Then the senior engineer remembered why.

One customer had modules that reported readiness late after cold storage. Another customer upgraded controllers before
modules because their field schedule made the reverse order expensive. A backend tolerance and a service-tool behavior
had been added during the same release week. Nobody had tried to hide the dependency. They were trying to get a real
product through a real upgrade without losing recovery confidence.

The memory helped. It also exposed a Bus Factor risk. If one person had to be in the room for the relationship to be
found, the relationship was not discoverable enough to be safe.

The team named the silent coupling.

The shared behavior was the recoverable startup signal. The hidden dependents were the service tool, backend mapper,
manufacturing script, support procedure, and release validation path. The owner was not one team yet. The evidence was
spread across code, tests, logs, release notes, support records, and memory. The failure mode was not a controller
crash. It was loss of recovery confidence across product surfaces.

The next decision became smaller and better.

They did not revert the firmware change. They did not start a broad refactor. They did not remove the fallback. They
made the relationship explicit enough to continue.

The firmware team restored the diagnostic wording consumed by the service tool and added a separate structured field
for the new transitional state. The backend team added a contract test for the upgrade mapping. Manufacturing updated
the final-test script to use the Event Catalog meaning rather than raw event order. Support updated the article to name
the recoverable state instead of relying on one phrase. The Architecture Ledger gained an owner, a revisit trigger, and
a link to the characterization test. The Decision Journal recorded why the old behavior stayed stable while the new
module path was introduced.

The change still shipped.

It shipped with a named contract where there had been shared behavior by habit. It shipped with a review path for the
next startup change. It shipped with a later question: when upgrade evidence is strong enough, should the compatibility
path be stabilized, simplified, or removed?

That question belonged to later work.

For this release, the important discovery was sharper:

The local code had not been local.

The behavior had been shared all along.

## Discussion

Silent coupling is a hidden behavioral dependency.

It exists when two or more surfaces must remain aligned, but the relationship is not represented as an explicit
contract, record, owner, test, schema, API, or review path. The code may be separated cleanly. The teams may have
different backlogs. The import graph may look quiet. The service diagram may look stable. The behavior still changes
together.

That is what makes silent coupling dangerous. It lets a change look local while its consequences are shared.

Chapter 32 taught reading a legacy system before changing it. Chapter 33 narrows that reading to a particular question:
what else assumes this behavior will not change?

The first mistake is to equate dependency discovery with static structure.

Static structure matters. Imports, call graphs, package boundaries, ownership maps, and service diagrams are useful
evidence. They show visible dependency. They do not show the whole dependency graph of a living product.

A diagnostic string can be a dependency. A test station can depend on event order. A backend mapper can depend on a
firmware state name. A support procedure can depend on a phrase in a tool. A release path can depend on one retry
window being longer than another. A global configuration flag can connect product variants that appear separate in the
code. A temporary fallback can become a product promise after customers build work around it.

These relationships are easy to miss because they often do not look like architecture. They look like operational
detail. They look like support language. They look like a script. They look like a test fixture. They look like an old
exception. They look like memory.

Principal Engineers learn to treat those surfaces as architecture when product behavior depends on them.

The useful starting point is the behavior being changed.

Not the file. Not the component. Not the owner. The behavior.

Ask what will be true after the change that was not true before. Ask what will stop being true. Ask which state,
diagnostic, event, named value, data shape, timing window, support instruction, tool output, or release sequence carries
that behavior. Then ask who or what assumes it.

This is where `LAW-002`, Every API Is a Promise, becomes practical. In a mature product, promises often escape the
formal API. A signature can remain stable while meaning changes. A payload shape can remain stable while timing changes.
An error code can remain stable while recovery behavior changes. A diagnostic can look internal while a service tool,
manufacturing script, or support article treats it as a contract.

API Stability (`METRIC-004`) therefore asks more than "did the interface compile?" It asks whether dependents can still
trust the meaning, timing, error behavior, and recovery behavior they built around the interface.

Silent coupling also hides inside state.

`LAW-001`, Every State Has One Owner, is not a paperwork rule. It is a way to find responsibility. When several
surfaces interpret state without a shared owner, the state can carry hidden promises. Firmware may own the state
machine. Backend may store the state. Support may describe the state. A service tool may translate the state into an
operator action. Manufacturing may use the state as test evidence.

If the state owner is unclear, a local change can move meaning under several teams at once. Hidden State (`SMELL-004`)
makes this worse because the important fact may not be stored in a field at all. It may live in ordering, freshness,
startup history, an override, or a global flag.

Global Configuration (`ANTIPATTERN-003`) is a common source. A flag that began as a lab option may later distinguish
customers, product variants, recovery modes, or release paths. If several surfaces read the flag with different
meanings, the flag has become a shared behavioral boundary without a shared contract.

Time is another place silent coupling hides.

`LAW-003`, Time Is a Dependency, matters because many legacy promises are temporal. A retry window, timeout, startup
order, event ordering, upgrade sequence, cache freshness rule, or release window may be the relationship. If one
surface changes timing and another surface depends on the old timing, the code can be correct locally and wrong as a
system.

This is how a story like One Lost Packet (`FAILURE-002`) becomes relevant without turning the chapter into an incident
review. Packet loss, retry timing, diagnostic meaning, and recovery behavior often cross boundaries. If no record names
the relationship, teams discover it only when the sequence fails under pressure.

Dependencies are broader than calls.

`LAW-007`, Every Dependency Is a Decision, means a dependency can be a tool, script, data format, release habit,
manufacturing fixture, backend tolerance, support procedure, vendor behavior, or person. A hidden dependency still
imports cost. It imports coordination. It imports review requirements. It imports failure modes. It imports replacement
work.

Platform Leakage (`SMELL-005`) often creates silent coupling because platform detail escapes its intended boundary.
A driver timing detail becomes product behavior. A vendor error meaning becomes support language. A build path becomes
manufacturing behavior. A backend retry rule becomes firmware expectation. The more the product depends on leaked
details, the more local changes need cross-boundary evidence.

Temporary Solution (`ANTIPATTERN-006`) is another frequent source. A fallback added for one release, one customer, one
factory issue, or one upgrade path may survive long enough to become normal. The problem is not that the temporary
solution existed. Real products need temporary moves. The problem appears when the reason, owner, expiry condition, and
dependents disappear while the behavior remains trusted.

Silent coupling is found with evidence.

This is where `LAW-005`, Evidence Before Confidence, protects the team from both panic and folklore. Not every rumored
dependency is active. Not every old workaround is still needed. Not every surprising consumer is legitimate. The task
is to prove enough to act responsibly.

Useful evidence comes from many places:

- source code and tests;
- tool repositories and scripts;
- logs and diagnostic streams;
- backend mappings and data contracts;
- Event Catalog rows;
- support articles and field procedures;
- manufacturing and final-test records;
- release notes and upgrade guides;
- ADRs, RFCs, Decision Journal entries, and Architecture Ledger rows;
- incidents, validation failures, and senior memory.

Each source has limits.

Tests show what someone chose to check. Logs show what the system emitted, not always what the event meant. Support
articles show operational promises, but may lag behind implementation. Release notes show what the organization told
customers, but may compress the reason. Senior memory can explain context that records lost, but memory alone creates
Bus Factor (`METRIC-002`) risk.

Discoverability (`METRIC-003`) is the test of whether the next engineer can find the relationship without guessing who
to ask. If the relationship is real but discoverable only through one person, one script nobody knows about, or one
release note in an archive, it is not visible enough for safe change.

Change Radius appears after the hidden dependents are named.

A team often estimates Change Radius (`VOCAB-001`, `METRIC-001`) from code ownership. Silent coupling makes that
estimate too small. The real Change Radius includes any surface that assumes the behavior: firmware, backend, service
tooling, manufacturing, support, release validation, data migration, or field procedure.

The point is not to make the radius scary. The point is to make it true enough.

Once the coupling is visible, the next action depends on the kind of relationship found.

Some coupling should become an explicit contract. A diagnostic consumed by tools may need a stable meaning, owner, and
compatibility note. An event consumed across boundaries may need an Event Catalog row naming producer, consumers,
ordering assumptions, and failure behavior. A backend tolerance may need a contract test. A support procedure may need
to reference a product state rather than a fragile phrase. A cross-team change may need an RFC before it hardens.

Some coupling should become a decision record. An ADR can name a consequential architectural choice. A Decision Journal
entry can preserve a smaller assumption, owner, and revisit trigger. The Architecture Ledger can keep active coupling
visible until it is stabilized, changed, or retired.

Some coupling should trigger Architecture Review (`RITUAL-001`). If a local change crosses ownership, release, support,
or manufacturing boundaries, review is not ceremony. It is the point where dependents, evidence, alternatives, risks,
and owners become visible before the relationship hardens again.

Architecture Health Review (`RITUAL-004`) can also surface silent coupling. If health reviews keep finding changes
that require unexpected reviewers, repeated release surprises, stale records, or dependence on one expert, the team may
not have a delivery problem first. It may have hidden relationships that need to be named.

The response is not always removal.

A discovered coupling may be intentional and valuable. A product may need stable diagnostics for service recovery. A
manufacturing script may need a reliable event sequence. A backend may need to tolerate old firmware during staged
upgrade. The coupling becomes a problem when it is silent, not when it exists.

This boundary matters for the rest of Part VI. Silent coupling can feed utility pull, configuration complexity,
deletion risk, and refactoring trust risk. Later chapters own those moves. Chapter 33 stops at finding the hidden
relationship and deciding the next responsible action.

Name it. Prove it. Make it owned. Decide what happens next.

That is enough work for one chapter and often enough to save one release.

## Engineering Principle

Treat silent coupling as hidden shared behavior.

Find it by tracing what must change together across code, data, time, tools, tests, releases, and people. Then make the
relationship explicit enough to own, test, review, stabilize, or retire.

The practical move is to shift from structure-first questions to behavior-first questions.

Do not begin with:

> Which files call this code?

Begin with:

> What behavior is changing, and who or what assumes that behavior will stay stable?

Then trace the carriers of that behavior. It may be a diagnostic, event, named value, state meaning, timing window,
data shape, support instruction, tool output, release sequence, or test expectation. Ask where the promise is recorded
or tested. Ask which owner would know if it changed. Ask what would fail if the code changed but the name stayed the
same.

The answer does not have to be perfect before work can continue. It has to be strong enough to choose the next
responsible action.

If evidence proves the coupling is active, make the relationship visible. Add or repair the contract. Add a
characterization test or contract test. Update the Event Catalog, ADR, Decision Journal, or Architecture Ledger. Route
the change through Architecture Review when it crosses ownership or release boundaries. Preserve the later question of
whether the coupling should be removed until the dependent behavior is explicit and owned.

A local change is only local after the hidden dependents have been named.

## Architecture Exercise

Trace a Hidden Coupling Before the Change.

Choose one planned or recent change that appears local. Prefer a change involving a diagnostic, event, state meaning,
configuration flag, data shape, timeout, retry, service tool, manufacturing script, backend mapper, support procedure,
or release path.

Document:

1. the behavior being changed;
2. the visible owner;
3. the suspected hidden dependent;
4. the state, API, diagnostic, event, data shape, timing, or tool surface involved;
5. the evidence source;
6. the missing record or contract;
7. the likely Change Radius;
8. the failure mode if the relation is missed;
9. the owner to involve;
10. the record to update;
11. the test or safe probe to add;
12. the decision to make now;
13. the later cleanup, deletion, or refactoring question to defer.

Keep the exercise small. The goal is not to map every dependency in the system. The goal is to find one behavior that
may be shared without being named.

End with five outputs:

1. one hidden dependent to verify;
2. one evidence source;
3. one owner;
4. one record or contract to repair;
5. one next decision.

Do not create a new permanent artifact for the exercise. Use the record the system already trusts.

## Principal's Notebook

- Silent coupling makes local changes non-local.
- Shared behavior needs a named relationship.
- The first fix is visibility.

## ADR

### Make Device Registration Diagnostics an Explicit Contract Before Changing Startup Behavior

### Status

Accepted for the next device-registration change.

### Context

The firmware team needs to change startup behavior for a legacy controller so a new peripheral module can report a
transitional readiness state before full registration.

The local firmware change modifies a diagnostic state, named value, and retry window. Existing firmware tests cover the
component path. The visible backend payload remains stable.

Several dependent surfaces may still assume the old behavior:

- the service tool identifies recoverable startup states from diagnostics;
- the backend mapper interprets registration status during staged upgrade;
- the manufacturing script checks event order during final test;
- the support procedure tells technicians which phrase or state to wait for;
- release validation relies on old and new versions coexisting during upgrade.

No current record names this shared behavior as a contract. The Architecture Ledger has an old fallback row with no
current owner.

### Decision

Do not treat the firmware change as local until the hidden dependents of the startup behavior are named.

Trace the behavior through diagnostics, events, backend mappings, service tooling, manufacturing scripts, release notes,
support procedures, tests, logs, and owners.

Add a characterization test or contract test for the shared recoverable-startup behavior.

Update the Event Catalog with the diagnostic meaning, producer, consumers, ordering assumptions, and failure behavior.
Update the ADR, Decision Journal, or Architecture Ledger with the owner, dependents, evidence, and revisit trigger.

Route the change through Architecture Review if the coupling crosses ownership or release boundaries.

Defer deletion or larger refactoring until the coupling is explicit and owned.

### Alternatives

Rely on import graphs and existing unit tests.

Change the diagnostic wording because it looks internal.

Ask the senior engineer and rely on memory.

Document the coupling without assigning an owner.

Remove the fallback as dead code.

Broaden the refactor before the coupling is understood.

### Consequences

The first edit takes longer because the team must trace dependents before changing the behavior.

Release validation becomes less surprising because the service tool, backend mapper, manufacturing script, support
procedure, and upgrade path are visible before the change ships.

The diagnostic gains an owner and a contract surface. Future changes can be reviewed against evidence instead of
memory.

The team keeps a future decision open: after enough upgrade and field evidence exists, stabilize, simplify, remove, or
refactor the compatibility path.

## Editor's Commentary

This chapter exists because legacy work often fails at the boundary between "the code is local" and "the product
behavior is shared."

Chapter 32 taught the reader to read a legacy system before changing it. Chapter 33 makes one part of that reading more
precise. Silent Coupling (`SMELL-001`, `VOCAB-008`) is not found by suspicion alone. It is found by tracing behavior
until the hidden dependents, owners, records, and evidence are visible enough to support a decision.

The chapter deliberately avoids making coupling a moral failure. Many silent couplings began as responsible moves under
real product pressure: keep a field recovery path alive, support old firmware during upgrade, preserve manufacturing
throughput, help technicians diagnose devices, or keep a customer from being stranded. The failure is not that the
relationship existed. The failure is letting it remain invisible after other teams and releases depend on it.

This also keeps the Part VI sequence clean. Finding silent coupling may reveal utility pull, configuration growth,
deletion candidates, and refactoring risk. Those are later chapters. Here the Principal Engineer's work is narrower:
make the hidden shared behavior visible, prove whether it is active, give it an owner or record, and choose the next
responsible action.

That is the difference between a local edit that hopes nothing else depends on it and a local edit that has earned the
right to be local.
