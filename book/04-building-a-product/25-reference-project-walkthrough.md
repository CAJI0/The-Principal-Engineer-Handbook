# Reference Project Walkthrough

## Opening Quote

> A product is not one decision made well. It is a chain of decisions that can still be found when the field asks why.

## Story

### One Product, Five Pressure Points

The prototype was small enough to fit on one bench and complicated enough to become a product.

The team called it the Field Sensor Gateway. It sampled one field sensor, stored local configuration, reported readings
over a low-power radio link, and exposed a simple service tool for setup and diagnosis. The first customer wanted a
pilot before committing to a wider installation. The prototype did what the team needed it to do: it proved that the
sensor reading was useful, the reporting path worked in the lab, and a technician could change basic configuration
without rebuilding firmware.

It was not a careless prototype.

It was a focused one.

The firmware used a hard-coded reporting interval because the pilot question was about measurement quality, not regional
data plans. Calibration was manual because the team had only five units. The service tool showed developer logs because
the firmware team was still bringing up the radio path. Firmware update worked through a lab cable and a script. The
latest build could update to the next build on the bench. The first hardware revision had one sensor offset, one radio
module, one configuration shape, and one customer package.

The prototype was successful enough to create pressure.

Sales wanted ten pilot units. Manufacturing wanted serial identity and a calibration flow. Support wanted to diagnose
radio failures without asking a firmware engineer to read raw logs. The product owner wanted one regional package with a
longer reporting interval and one package with a different radio option. A customer asked for a special timeout because
their gateway sometimes disappeared for several minutes. Release wanted v1.1 to include the new configuration schema.
Field units on v1.0 and v1.0.2 already existed because the first pilots had been hand-carried into customer sites.

Each pressure point looked local.

The firmware team could replace the hard-coded interval with a setting. Manufacturing could add a station file for
serial identity. Support could get a richer log. The service-tool owner could add a regional toggle. Release could add
a migration from v1.0 to v1.1. The radio owner could tune retry behavior for the customer with the unstable gateway.

None of those answers were wrong by themselves.

Together, they would have created a product nobody could explain.

The first argument was about the reporting interval.

One engineer wanted a single global setting called `reportingInterval`. It would live in non-volatile configuration.
Manufacturing could write it. The service tool could edit it. Firmware could read it during startup. The regional
package could set a different default. The special customer timeout could be another value in the same file.

That sounded simple until the team wrote the combinations on the board.

The standard package reported every ten minutes. The regional package reported every thirty minutes because the radio
network charged differently. The battery package needed a longer interval but also a different retry window. The special
customer timeout was not a reporting interval at all; it was a gateway-absence tolerance. If the team hid all of that
inside one broad configuration value, the product would look flexible while nobody owned the promise.

Mara, the principal engineer, changed the question.

> Which difference are we promising to support, and which difference are we only tolerating for the pilot?

The room slowed down.

The regional reporting interval became a supported variant promise. The battery package became a deferred variant
because it changed measurement cadence, retry timing, and field-support expectations. The special customer timeout
became a pilot exception with an owner and a review trigger. The global setting disappeared. Configuration became owned
state, not a place to hide product difference.

The second argument came from manufacturing.

The station could write serial identity and calibration values into the device. That part was straightforward. The
problem was authority. Manufacturing measured calibration. Firmware used calibration during sensing. The service tool
could request recalibration under support guidance. The v1.1 migration needed to preserve calibration across a schema
change. The older hardware revision stored the backup in a different layout. The recovery path could restore firmware,
but it could not know whether calibration still matched the hardware revision if nobody owned the meaning.

Each participant had a legitimate role.

None of them could be the whole truth.

The team named the state owners. Manufacturing owned the first measurement and station evidence. Firmware owned the
runtime calibration state and validation rules. The service tool could request a recalibration workflow, but it could
not write a raw value as product truth. Release owned the migration evidence for calibration preservation. Support owned
the field procedure for a unit that recovered without enough calibration evidence. The device would report serial
identity, hardware revision, calibration version, active configuration fingerprint, and firmware version in a
support-safe diagnostic snapshot.

That decision did not add much code.

It removed ambiguity.

The third argument started after the second board revision arrived.

The sensor offset changed slightly. The prototype still reported readings. The happy path still looked fine. But the
old calibration flow, old service-tool label, old event meaning, and old v1.0 update path now depended on hardware
revision. A support engineer could no longer tell whether a low reading meant sensor drift, calibration mismatch,
regional interval, radio dropout, old firmware, or board revision.

The team almost fixed it with another flag.

Mara asked them to trace the Change Radius instead.

Changing hardware revision handling touched firmware validation, station programming, service-tool display, field
diagnostics, release notes, migration evidence, support scripts, and the Event Catalog. That was not a local flag. It
was a product promise. The team opened an RFC for the hardware-revision and configuration compatibility proposal because
firmware, manufacturing, service tooling, QA, support, and release all needed to review it before the decision hardened.

The RFC did not make the product heavy.

It kept a broad decision from pretending to be small.

The fourth pressure point arrived from the field.

Three pilot units stopped reporting after a v1.1 update. The devices were not dead. Two had completed migration and lost
radio contact during the first report. One had rejected configuration migration because the regional package was using
an old field name. The service tool showed the same message for all three:

> update failed

That message was true in the way useless messages are true.

The firmware log had more detail. One unit had `radio timeout`. Another had `first report missing ack`. The third had
`config key rejected`. The support team did not have the firmware log. The customer did not care which internal module
had produced the text. Support needed to know whether the device had preserved identity, which firmware version was
active, which configuration fingerprint had been applied, which variant was selected, whether calibration was still
valid, and which boundary had rejected the next step.

The team had observability.

It did not have product observability.

They wrote the first small Event Catalog entries. Not a logging platform. Not a telemetry strategy. A few owned event
meanings:

- `upgrade_started`: the device accepted a package and recorded source version, target version, hardware revision, and
  variant.
- `configuration_migration_rejected`: firmware rejected a configuration migration and preserved the source
  configuration.
- `first_report_not_acknowledged`: the radio path did not receive the expected acknowledgement within the supported
  retry window.
- `recovery_ready`: the device entered a supportable recovery state with identity, calibration state, active version,
  and configuration fingerprint available.

Each event had an owner, producer, consumer, ordering assumption, and failure meaning. Event Explosion was the risk on
one side: every module wanted to add one more event. Hidden State was the risk on the other side: the product could not
explain what state it was in after update. The team chose fewer events with sharper meaning.

The fifth pressure point was release.

The new v1.1 release changed the configuration schema. The latest lab build upgraded cleanly. That was useful evidence,
but not enough. Field units existed on v1.0 and v1.0.2. One hardware revision needed a different calibration migration
path. The regional variant had a different reporting interval and radio option. The special customer timeout was a pilot
exception, not a supported variant. Rollback could return to the old executable, but it could lose the meaning of
migrated configuration unless the source snapshot and calibration state were preserved.

The release owner asked the familiar question:

> Can we ship v1.1?

Mara wrote a better one beside it:

> Which product baseline are we promising, and what evidence keeps that promise true?

The team built a decision chain instead of a checklist.

They started with the prototype assumptions. The hard-coded reporting interval became a supported regional variant
default, not a global setting. Manual calibration became a manufacturing measurement with firmware ownership of runtime
validity. Developer logs became support-safe diagnostics tied to event meanings. The lab-only update script became a
release path with supported source versions and recovery behavior.

They named the supported baseline for pilot release.

The pilot would support hardware revision A and revision B, standard and regional packages, configuration schema v2,
service tool 4.3 or later, direct upgrade from v1.0.2 to v1.1, and upgrade from v1.0 to v1.1 only through an
intermediate migration package. The special customer timeout would remain a pilot exception in the Decision Journal,
with a review trigger after thirty field days or after the second customer request. The battery package would be
deferred. The older service tool would be rejected for v1.1 upgrade because it could not display support-safe failure
reasons.

They named unsupported combinations too.

Revision A with a calibration backup that had not been validated could not upgrade directly to v1.1. The regional
package could not use the special timeout. The battery package could not be enabled by setting hidden flags. v1.0 units
could not skip the intermediate migration package. A service tool older than 4.3 could not perform the upgrade. Factory
reset was not the default recovery path because it would destroy identity, calibration evidence, and the customer's
trust in the device.

Then they assigned records.

The pilot baseline went into an ADR. The hardware-revision and service-tool compatibility proposal stayed in an RFC
until affected owners accepted the trade-offs. The special customer timeout went into the Decision Journal because it
was bounded, reversible, and tied to evidence. Event meanings went into the Event Catalog. Active baseline decisions,
owners, and review dates went into the Architecture Ledger. The assumption that almost escaped - "latest lab update
proves field update readiness" - went into the Mistake Ledger after the pilot issue exposed it.

Finally, they reviewed and froze the right things.

The broad compatibility decision received Architecture Review because its Change Radius crossed firmware,
manufacturing, service tooling, support, QA, release, and field behavior. The team did not freeze the whole product.
They froze only the v1.1 upgrade-path validation surfaces: supported source-to-target paths, configuration migration
rules, service-tool compatibility, diagnostic event meanings, release-critical state owners, and recovery behavior for
interrupted update. Bug fixes could continue if they preserved those decisions. Changes to those decisions required an
exception, affected-owner review, record updates, and new evidence.

The pilot did not become perfect.

It became supportable.

When a unit stopped reporting after the next update, support could see source version, target version, active variant,
configuration fingerprint, hardware revision, calibration state, reset reason, migration result, and first-report
outcome. They could tell the difference between a radio acknowledgement failure and a rejected configuration migration.
They could tell when rollback was safe, when retry was enough, and when forward-fix was the only honest path. Future
engineers could find the baseline decision, the unsupported combinations, the event meanings, the review notes, and the
conditions that would reopen the decision.

That was the walkthrough: not a universal design, not a reference implementation, but a chain of decisions that held
together when the product left the bench.

## Discussion

A reference project is useful when it connects decisions.

It is less useful when it tries to be universal. If the Field Sensor Gateway becomes a product specification, it will
argue with every real system the reader has ever built. If it becomes a code walkthrough, it will teach local mechanics
instead of architectural judgment. If it becomes a recap of Part IV, it will repeat the previous chapters without
showing how their decisions meet each other.

The useful question is smaller and more durable:

> If we had to take one embedded product from prototype to supported release, which architecture decisions would we make,
> record, test, review, freeze, and revisit?

The answer is not one decision.

It is a chain.

The Field Sensor Gateway prototype proved useful behavior under prototype conditions. It proved that a sensor reading
could be collected, stored, reported, configured, and updated in the lab. It did not prove manufacturing repeatability,
field diagnosis, regional variants, release compatibility, calibration migration, support horizon, or recovery after
interrupted reporting. That distinction is the point of Chapter 20. A successful prototype is evidence. It is not yet a
product baseline.

The first product move is to expose assumptions and decide which become promises. A hard-coded interval may be a useful
prototype shortcut. In a product, it can become a regional variant promise, a battery-life trade-off, a support
expectation, a radio dependency, and a release compatibility concern. Manual calibration may be acceptable on five
units. In the field, it becomes identity, manufacturing evidence, firmware validation, support diagnosis, and migration
behavior. Developer logs may help bring-up. In a pilot, they may be insufficient because support needs stable product
meaning, not raw module vocabulary.

That is why state ownership appears so early in the walkthrough.

Identity, calibration, configuration, variant, event meaning, update state, and recovery state are not passive values.
They decide what the product may do and what support can believe. Every State Has One Owner (`LAW-001`) is the
difference between a device that can explain itself and a device where firmware, station scripts, service tools,
release packages, and support notes each carry a competing truth.

API promises appear next because product boundaries begin as conveniences.

A service-tool command, diagnostic event, configuration file, regional package, update package, station record, or
support note may feel informal until another surface depends on it. Every API Is a Promise (`LAW-002`) does not mean
every internal shape needs ceremony. It means that once manufacturing, support, release, QA, or customers trust a
meaning, the team has made a promise about behavior, errors, timing, and ownership. API Stability (`METRIC-004`) is the
measure of whether that promise can survive change without surprising its dependents.

Dependencies become visible when the product leaves the prototype bench.

The radio link is not only a transport. It brings retry behavior, timing assumptions, acknowledgement semantics,
gateway compatibility, field failure modes, and support cost. The service tool is not only a convenience. It decides
what technicians can see, install, reject, and recover. The manufacturing fixture is not only a station script. It
creates identity and calibration evidence the product may rely on for years. Every Dependency Is a Decision (`LAW-007`)
because those dependencies import lifecycle obligations whether the architecture record names them or not.

Time becomes a product concern for the same reason.

Reporting intervals, gateway absence tolerance, update windows, retry timing, event ordering, support horizons, and
revisit triggers all depend on time. Time Is a Dependency (`LAW-003`) because a behavior that works on the bench may
fail when the device sleeps, waits for a network, misses an acknowledgement, updates during a service window, or waits
for support to reach a field unit. A timeout is rarely just a number after the product ships.

Manufacturing and field reality make the baseline honest.

Chapter 21 is not about turning engineers into manufacturing-process owners. It is about making sure product
architecture survives the moment other people have to build, identify, configure, diagnose, recover, and support the
device. The Field Sensor Gateway needs serial identity because support cannot reason about "one of the pilot units."
It needs calibration ownership because a reading is not trustworthy if nobody can explain which measurement, hardware
revision, firmware version, and configuration produced it. It needs fixture and service boundaries because a station
write, service request, and firmware validation are different authorities.

Configuration and variants then force deliberate difference.

Chapter 22 matters because product difference is easy to hide in flags. A regional reporting interval is a supported
variant when the product can test, release, diagnose, document, and support it. The special customer timeout is not the
same kind of promise if it exists only for one pilot and has a review trigger. A deferred battery package is not a
failure; it is a named unsupported combination until evidence justifies it. Simplicity Is a Feature (`LAW-004`) because
the supported baseline stays understandable. Unused Flexibility Is Waste (`LAW-006`) because a perfect product-line
architecture for imagined variants would expand test space, support meaning, and release risk before the product has
earned it.

Global Configuration (`ANTIPATTERN-003`) is the tempting shortcut here.

One broad flag can blur regional behavior, hardware revision, migration, diagnostics, and support behavior. It feels
fast because every team can read it. It becomes expensive because every team gives it local meaning. The recovery is to
name supported combinations, reject unsupported combinations, keep defaults owned, and give each configuration value a
scope and lifecycle.

Observability turns field behavior into usable evidence.

Chapter 23 is not a logging chapter. It asks whether a device can explain enough of its behavior away from engineering.
For the Field Sensor Gateway, useful evidence includes reset reason, active firmware version, source version, target
version, hardware revision, configuration fingerprint, variant, calibration state, migration result, radio boundary
outcome, first-report result, service-tool compatibility, and recovery state. Those are not random facts. They are the
evidence support needs to distinguish a lost acknowledgement, a rejected configuration migration, a stale service tool,
a board-revision calibration issue, and an interrupted upgrade.

The Event Catalog (`ARTIFACT-005`) keeps event meanings stable enough to trust. Hidden State (`SMELL-004`) appears when
the device behaves differently after calibration, migration, reset, or recovery but cannot explain why. Silent Coupling
(`SMELL-001`) appears when firmware, station scripts, service tools, release packages, diagnostics, and support notes
depend on the same meaning without a shared contract. Platform Leakage (`SMELL-005`) appears when low-level board,
radio, driver, or update details leak into product language without translation. Event Explosion (`SMELL-006`) appears
when every local module adds a new message and support receives noise instead of meaning.

The answer is not more events.

The answer is owned events with product meaning.

Release and upgrade paths turn the chain into a promise.

Chapter 24 matters because release pressure asks small questions at the worst time. Did the image pass? Did the package
install? Did the latest lab unit upgrade? Those are useful questions. They are not the whole promise. A supported
release needs source-to-target paths, state preservation, service-tool compatibility, variant support, diagnostic
meaning, recovery behavior, release artifact identity, and a support horizon.

The Field Sensor Gateway baseline names one direct supported path: v1.0.2 to v1.1 for supported hardware revisions,
supported regional packages, configuration schema v2, service tool 4.3 or later, and preserved identity, calibration,
configuration fingerprint, variant, event meaning, and recovery state. It names one deferred path: v1.0 to v1.1 requires
an intermediate migration package because direct migration lacks enough source configuration meaning. It names rejected
paths too: old service tools cannot perform the v1.1 upgrade, unsupported variant combinations cannot be enabled by
flags, and factory reset is not the default recovery because it destroys the very evidence the product needs to
preserve.

One Lost Packet (`FAILURE-002`) matters because reporting and update paths often fail on a missing or late message. A
lost acknowledgement after update can reveal whether retry, recovery, event meaning, and support diagnostics are real
promises. The Release We Should Have Delayed (`FAILURE-005`) matters because release pressure can convert unresolved
upgrade and support assumptions into field cost. The Successful Prototype (`FAILURE-003`) matters because the whole
story begins with prototype evidence that could have been mistaken for product architecture.

Records keep the chain discoverable.

An ADR (`ARTIFACT-001`) records the pilot baseline decision because it affects future architecture, ownership, cost,
and reversibility. An RFC (`ARTIFACT-002`) invites review when the compatibility proposal crosses ownership boundaries.
A Decision Journal (`ARTIFACT-003`) is enough for a bounded pilot exception or evidence gap. A Mistake Ledger
(`ARTIFACT-004`) preserves the escaped assumption after the field teaches the team something painful. An Architecture
Ledger (`ARTIFACT-006`) makes active decisions, owners, status, linked records, and review dates findable.
Discoverability (`METRIC-003`) is not paperwork. It is how future engineers avoid treating the same assumptions as new.

Review and freeze are scoped tools.

Architecture Review (`RITUAL-001`) is useful when a product decision's Change Radius crosses owners before it hardens.
Change Radius (`VOCAB-001`, `METRIC-001`) is the affected surface: firmware, manufacturing, service tooling, support,
QA, diagnostics, release notes, field behavior, customer promises, and recovery paths. A broad compatibility decision
deserves review because each owner will inherit the consequences.

Architecture Freeze (`RITUAL-002`) is useful later, when selected decisions need stability for validation. The team does
not freeze the whole product. It freezes named release-critical decisions for a bounded time: supported upgrade paths,
migration rules, event meanings, service-tool compatibility, state owners, and recovery behavior. The freeze remains
honest only if it keeps learning channels open and defines an exception path when evidence invalidates the decision.

Temporary Solution (`ANTIPATTERN-006`) is the pressure that appears throughout the chain.

The prototype shortcut, pilot timeout, old service-tool support script, calibration bypass, and manual recovery note can
all be reasonable for a moment. They become architectural cost when they have no owner, expiration condition, review
trigger, or explicit decision. The chapter's point is not that temporary work is shameful. The point is that temporary
work needs a path out.

A product becomes supportable when these decisions connect.

Prototype assumptions, manufacturing identity, calibration, configuration, variants, event meanings, diagnostics,
release artifacts, upgrade paths, and recovery behavior must form a chain of named promises, owners, evidence, records,
and revisit triggers. If one link is missing, the product may still work. It may even work for months. But when the
field asks a hard question, the team will discover whether the chain was real.

Part IV ends here because the product is no longer only a design problem.

It is shared memory.

That is the quiet bridge into the next part. Technical Leadership Without Authority begins when product decisions are
visible enough for other people to carry them, challenge them, and improve them without needing the original team in the
room.

## Engineering Principle

Build the product as a chain of explicit decisions. Each decision should name the promise it creates, the owner who keeps
it true, the evidence that supports it, and the next condition that should make the team revisit it.

Use this principle when product work starts to split into separate local fixes.

Ask:

1. What did the prototype actually prove?
2. Which product reality changed the architecture?
3. Which state needs an owner?
4. Which interface became a promise?
5. Which dependency became a support obligation?
6. Which configuration difference is a supported variant?
7. Which unsupported combination must be stated?
8. Which field failure must explain itself?
9. Which upgrade path is promised?
10. Which evidence supports the release?
11. Which decision needs review, freeze, or a ledger entry?

The goal is not to apply every Part IV practice with equal weight. The goal is to connect the decisions that must stay
true after the product leaves the prototype bench.

## Architecture Exercise

### Walk One Product Decision Chain

Choose one small product or subsystem. Start with a real prototype assumption if possible.

Write the chain in one sentence:

> Because prototype assumption A became product promise P, owner O must preserve evidence E until revisit trigger T.

Then trace:

1. prototype assumption;
2. manufacturing or field reality;
3. configuration or variant decision;
4. observable event or diagnostic;
5. release or upgrade path;
6. owner;
7. promise;
8. evidence;
9. record;
10. review or freeze trigger;
11. revisit condition.

End with five outputs:

1. one product promise;
2. one owner;
3. one evidence requirement;
4. one record to update;
5. one revisit trigger.

If the exercise produces a long checklist, narrow it. If it produces only one local fix, widen it until the next product
surface appears. The useful chain is small enough to act on and connected enough to survive the field.

## Principal's Notebook

- A product is a chain of promises.
- A baseline is useful only when its assumptions are findable.
- A good walkthrough leaves decisions people can reuse.

## ADR

### Chapter ADR: Set the Field Sensor Gateway Product Baseline for Pilot Release

#### Status

Accepted for this chapter.

#### Context

The Field Sensor Gateway prototype works. It reports sensor readings over a radio path, stores local configuration, has
a simple service tool, and can be updated in the lab.

Manufacturing now needs serial identity and a calibration flow. Field support needs diagnostic evidence that does not
depend on developer logs. Regional and hardware variants exist. Firmware v1.1 changes the configuration schema. Field
units already exist on v1.0 and v1.0.2. Support and future engineers need a discoverable baseline that states what is
supported, what is deferred, and what evidence protects the pilot release.

#### Decision

Accept a limited supported baseline for pilot release.

The pilot baseline supports hardware revisions A and B, standard and regional packages, configuration schema v2, service
tool 4.3 or later, and direct upgrade from v1.0.2 to v1.1. Upgrade from v1.0 to v1.1 requires an intermediate migration
package. The battery package, unsupported regional timeout combinations, and old service-tool upgrade path are deferred
or rejected for the pilot.

Assign owners for serial identity, calibration state, configuration schema, regional variant promises, event meanings,
release artifact identity, migration behavior, update state, and recovery state. Preserve identity, calibration,
configuration fingerprint, hardware revision, variant, source version, target version, migration result, reset reason,
and first-report outcome as support-safe evidence.

Record the pilot baseline in this ADR. Keep the broader hardware-revision and service-tool compatibility proposal in an
RFC until affected owners accept it. Use Decision Journal entries for bounded pilot exceptions and evidence gaps. Record
event meanings in the Event Catalog. Track active baseline decisions, owners, and review dates in the Architecture
Ledger. Use the Mistake Ledger for escaped assumptions discovered during pilot.

Run Architecture Review for broad Change Radius decisions that cross firmware, manufacturing, service tooling, support,
QA, release, and field behavior. Apply Architecture Freeze narrowly to v1.1 upgrade-path validation: supported
source-to-target paths, migration rules, service-tool compatibility, event meanings, release-critical state owners, and
recovery behavior. Keep the freeze scoped, temporary, and exception-based.

#### Consequences

The pilot baseline becomes supportable. Ownership is clearer. Hidden promises are reduced. Unsupported paths are stated
before support discovers them through failure. Field diagnosis improves because event meanings and diagnostic snapshots
carry product meaning. Future engineers can find the product memory behind the baseline.

The cost is real. The team must do more validation work. Deferrals become visible. Firmware, manufacturing, service,
support, QA, and release must coordinate around shared promises. Some customer requests will wait. Records must stay
discoverable enough to be useful after the pilot pressure passes.

#### Alternatives Considered

Ship the prototype baseline.

This is fastest, but it preserves hard-coded timing, manual calibration, developer-only logs, lab-only update evidence,
and hidden configuration assumptions as product architecture.

Wait for a perfect product-line architecture.

This avoids some future regret, but it adds speculative flexibility before the product has evidence for it. The pilot
needs a bounded baseline, not every imagined variant.

Support every requested configuration.

This sounds customer-friendly, but it makes unsupported combinations invisible and expands the test, release, and
support surface beyond the team's evidence.

Defer observability and upgrade evidence until after pilot.

This keeps the schedule clean until the field needs answers. Then support would discover that the product cannot
explain failures without developer-only context.

Split every customer into separate firmware.

This avoids some configuration complexity, but it multiplies release paths, service-tool behavior, support knowledge,
and upgrade evidence.

Freeze the entire architecture until all unknowns are resolved.

This sounds disciplined, but it blocks learning and treats local implementation fixes as if they were all architecture.
The team needs a narrow freeze around upgrade-path validation, not a ban on curiosity.

## Editor's Commentary

Chapter 25 closes Part IV by making the product-building chapters meet inside one reference product.

Chapter 20 asked what the successful prototype actually proved. Chapter 21 asked whether the product survives
manufacturing and field reality. Chapter 22 asked which differences are supported variants and which combinations are
unsupported. Chapter 23 asked whether the product can explain field behavior in support-safe language. Chapter 24 asked
which release and upgrade paths the team is promising. Chapter 25 does not repeat those chapters. It shows how one
Field Sensor Gateway decision chain touches all of them.

The chapter deliberately keeps reference project, Field Sensor Gateway, product baseline, product decision chain, pilot
release, supportable baseline, product memory, and walkthrough as chapter-local language. No new PEAK concept is
introduced. The graph weight remains on the registered relationship set: successful prototype pressure, release risk,
communication and recovery failure, state ownership, API promises, time, simplicity, evidence, unused flexibility,
dependency decisions, Change Radius, Discoverability, API Stability, ADRs, RFCs, Decision Journal entries, Mistake
Ledger entries, Event Catalog entries, Architecture Ledger rows, Architecture Review, Architecture Freeze, Hidden
State, Silent Coupling, Platform Leakage, Event Explosion, Temporary Solution, and Global Configuration.

The technical boundary is also intentional. This is not an MCU guide, RTOS design, boot loader pattern, radio protocol
comparison, service-tool specification, manufacturing-process manual, or CI/CD chapter. The embedded details exist to
keep the walkthrough credible: serial identity, calibration ownership, hardware revisions, local configuration,
service-tool behavior, field diagnostics, event meanings, radio acknowledgement, release artifact identity, upgrade
paths, rollback, retry, recovery, forward-fix, constrained memory, timing, storage, and support-safe evidence.

The transition to Part V is quiet but important. A product decision that cannot be found becomes private memory. A
product decision that can be found, challenged, reviewed, frozen, and revisited becomes something other people can
carry. That is where the next part begins: not with authority, but with shared memory strong enough for leadership to
work through it.
