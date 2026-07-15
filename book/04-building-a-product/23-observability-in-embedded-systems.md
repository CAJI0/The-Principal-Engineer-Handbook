# Observability in Embedded Systems

## Opening Quote

> A log is useful only when it helps someone decide what happened next.

## Story

### The Device That Could Not Explain Itself

The field trial was supposed to prove that the product could leave the lab.

The device was no longer a successful prototype. It had a manufacturing identity, a supported firmware image, a small
set of supported configurations, a service tool, a recovery path, and a documented set of product variants. The team had
done the difficult work from the previous chapters: they had stopped treating every board as a snowflake, had named the
supported product line, and had made enough commitments that manufacturing, support, and product could talk about the
same thing.

Then the first field update went out.

Most devices updated and kept reporting normally. A smaller group stopped reporting sometime after the update. Not
immediately. Not always. Not on the same variant. Not at the same customer site. The support dashboard showed silence.
The service tool said only `communication failed`. When a device came back to the lab, the debug build produced useful
logs, but the field image did not include them. The reset reason had been overwritten by normal boot code. The
configuration version was invisible to the support tool. The variant state was stored in nonvolatile memory but never
reported. The update state disappeared after reboot. Radio failures, gateway failures, firmware faults, configuration
mistakes, application errors, and power interruptions all collapsed into one product error code.

The support team could not tell whether the problem was firmware, configuration, gateway behavior, network coverage,
power, variant selection, a vendor dependency, or recovery after the update. Manufacturing identity existed, but it was
not tied to the diagnostic information anyone could see. A returned unit could be matched to a batch, but the field
evidence could not say which image, configuration, variant, update step, reset sequence, or boundary outcome had made it
silent.

The first proposal was predictable: add more logs.

Developers asked for verbose radio logs, update logs, gateway logs, power logs, application logs, and a temporary flag
that would let support turn everything on. The Principal Engineer did not reject the impulse. More information might
help. But volume was not the missing architecture.

She wrote a different question on the board:

What decision must support or engineering make, and what evidence must the device preserve so that decision is possible?

That question changed the work.

Support needed to decide whether to retry communication, ask the customer to power-cycle, send a replacement, escalate
to engineering, or mark a site issue. Engineering needed to decide whether the update mechanism had failed, the device
had rebooted during a critical step, the selected variant had loaded the wrong configuration, the gateway protocol had
changed, the radio dependency had behaved differently in the field, or the application had entered a state it did not
own cleanly.

Those decisions did not require every debug message. They required a small set of preserved facts.

The team listed the state transitions that mattered: update started, image verified, configuration migrated, variant
selected, gateway session opened, first post-update report sent, recovery entered, recovery completed, and normal
operation resumed. Each transition got an owner. Each boundary failure got a name. The radio driver could report radio
boundary outcomes, but it could not invent product meaning. The update component owned update state. The configuration
component owned configuration version and migration result. The product identity component owned manufacturing identity,
hardware revision, and supported variant identity.

They separated developer debug logs from product diagnostics. Developer logs could remain detailed, unstable, and useful
in the lab. Product diagnostics had to be part of the product promise. A service technician without a debugger needed to
see the last meaningful product events, the reset context, the update and recovery context, the firmware version, the
configuration version, the supported variant, the manufacturing identity, and the failure domain that was currently most
credible.

They also resisted the opposite failure. Every interesting line of code did not become an event. The Principal Engineer
created an Event Catalog and made each candidate event answer three questions: who owns it, what decision does it
support, and how long must it survive? Events without decisions were removed. Events without owners were sent back.
Events that merely copied a developer log message were rejected. The team kept a Mistake Ledger for false assumptions:
they had assumed reset reason would be available after boot; they had assumed configuration version was obvious from the
firmware image; they had assumed the gateway error code was enough; they had assumed manufacturing identity and
diagnostics would be joined later.

The next field update did not make every failure disappear. It did something more useful: it made failures explainable.

One silent device reported that it had verified the image, migrated configuration, selected the cellular variant, lost
gateway handshake after reboot, and preserved a brownout reset reason from four minutes after installation. Another
reported that the configuration migration had failed because the variant table did not contain the manufacturing option
burned into the unit. A third had no device failure at all; the gateway had rejected the first report because a
dependency contract had changed.

The product still had defects. But the team no longer had to guess which defect they were looking at.

## Discussion

Embedded observability is not the act of printing everything the firmware knows. It is the discipline of preserving the
evidence that lets someone make a product decision when the device is far away, partially failed, power constrained,
network constrained, and no longer attached to a debugger.

That distinction matters because field reality is harsher than the lab. A developer can rebuild firmware, attach tools,
raise logging levels, and reproduce a path with local context. A support engineer usually gets a generic failure message,
a customer report, a device identity, and maybe one chance to ask the device what happened. If the product cannot answer
with stable evidence, the organization substitutes confidence, habit, escalation, or blame.

Chapter 13's law, Evidence Before Confidence (`LAW-005`), becomes concrete here. The evidence has to survive the event
that makes people need it. A reset reason that is overwritten during boot is not field evidence. An update state that
disappears after reboot is not field evidence. A configuration version known only to a developer script is not field
evidence. A variant bit stored somewhere in nonvolatile memory is not field evidence if the support surface cannot show
it. The product has evidence only when the right person can see enough to decide what to do next.

The first architectural move is ownership. Every State Has One Owner (`LAW-001`) applies to diagnostics as much as to
runtime behavior. If update state is copied into three modules, none of them owns the truth. If a radio driver, gateway
client, and product service all produce the same "communication failed" code, the product has hidden state disguised as
simplicity. The device should name the state transition or boundary outcome at the level where the meaning is owned. A
driver may own a low-level radio result. The gateway client may own session negotiation. The product reporting component
may own whether the first post-update report was delivered. Those facts can be connected, but they should not be blurred.

This is also an API problem. Every API Is a Promise (`LAW-002`), and a service tool is an API to the field organization.
When it says `communication failed`, it promises very little. When it reports the last owned events, reset context,
firmware version, configuration version, variant identity, update phase, recovery state, manufacturing identity, and
failure domain, it promises that support can make bounded decisions without developer-only tools. That promise must be
stable enough that service procedures, escalation rules, and customer conversations can rely on it.

Time is another dependency. The failure may have happened before the reboot, during the update, after configuration
migration, while waiting for a gateway response, or after the first report left the device. Time Is a Dependency
(`LAW-003`) does not require every embedded product to have perfect wall-clock time. It does require the product to
preserve useful order. Sequence numbers, boot counters, monotonic ticks, install attempt numbers, update phases, and
retained reset snapshots may be enough. Without ordering, a device can tell you facts but not a story.

The same is true of external systems. Every Dependency Is a Decision (`LAW-007`) becomes visible when gateway behavior,
radio coverage, vendor drivers, network policy, manufacturing data, and configuration delivery all participate in one
field symptom. Observability should not hide those dependencies behind one error. It should make the boundary outcome
plain enough to decide whether the product needs a firmware fix, a gateway fix, a configuration correction, a service
action, or a dependency review. Remote telemetry, dashboards, or cloud services may help, but the product should still
preserve enough local and service-visible evidence for cases where connectivity, access, or backend interpretation is
part of the failure.

The Event Catalog (`ARTIFACT-005`) is the central artifact for this chapter because it turns diagnostic ambition into an
owned product surface. A good event entry is not a clever log message. It records the owner, name, trigger, payload,
severity, retention, reset behavior, support visibility, privacy and security constraints, versioning, deprecation, and
the decision the event supports. It gives Architecture Review (`RITUAL-001`) something concrete to inspect before the
product accumulates diagnostic promises no one owns. It also gives Architecture Freeze (`RITUAL-002`) a way to say
which diagnostic commitments must be preserved while a release or field trial is stabilized.

Those commitments still live inside embedded constraints. RAM, flash, CPU time, power budget, radio bandwidth, service
access, privacy, security, and flash wear all shape what the product can preserve. A small retained ring buffer, a few
compact counters, a boot counter, a reset snapshot, a partial history, or a bounded fault or crash snapshot may be
stronger evidence than a large debug stream that disappears at reset or drains the battery. The point is not to make
every log durable. The point is to decide which context is worth its cost because it changes a field decision.

The opposing smell is Event Explosion (`SMELL-006`). Event Explosion happens when the product emits many events but few
decisions become easier. It often starts from a good instinct. A team has been blind once, so it decides never to be
blind again. Every callback gets an event. Every retry gets an event. Every branch in a driver gets an event. The field
then receives noise, storage pressure, battery cost, privacy questions, and unclear ownership. Discoverability
(`METRIC-003`) gets worse because nobody can find the important signal. Change Radius (`VOCAB-001`, `METRIC-001`) grows
because every behavior change now touches logs, tools, dashboards, support procedures, and tests.

Avoiding Event Explosion does not mean being stingy with evidence. It means designing evidence around decisions. If an
event cannot change support action, engineering triage, recovery behavior, release validation, or product learning, it
probably belongs in a developer debug log rather than the product diagnostic surface. Developer logs can be verbose and
temporary. Product events should be stable, owned, tested, and understandable by people outside the firmware team.

The common embedded smells show up quickly when this discipline is absent. Hidden State (`SMELL-004`) appears when reset
reasons, update phases, configuration versions, and variant selections exist but cannot be inspected. Silent Coupling
(`SMELL-001`) appears when a gateway change, service tool assumption, or manufacturing option changes field behavior
without an explicit boundary record. Platform Leakage (`SMELL-005`) appears when the diagnostic surface exposes raw
driver concepts that support cannot safely interpret. HAL Everywhere (`ANTIPATTERN-002`) makes this worse by spreading
hardware meaning across the product instead of preserving a clear boundary between device facts and product facts.

Global Configuration (`ANTIPATTERN-003`) creates another trap. If every component reads configuration directly, no single
owner can say which configuration version shaped a failure. Callback Hell (`ANTIPATTERN-005`) can make event order
unreadable because the causal path is scattered across asynchronous handlers. Temporary Solution (`ANTIPATTERN-006`)
appears when the team adds a quick diagnostic flag for the field trial and forgets that support has started relying on
it. Each shortcut may be understandable. Together they make the product unable to explain itself.

The failure story One Lost Packet (`FAILURE-002`) is useful because it reminds the team that a small missing fact can
dominate a large investigation. In Chapter 23, the missing fact might not be a packet. It might be whether the first
post-update report was ever attempted, which configuration was active, whether recovery ran, or whether the reset
happened before or after migration. The point is the same: the system must preserve the fact that separates plausible
stories.

Observability also creates shared memory. ADRs (`ARTIFACT-001`) record diagnostic commitments that have architectural
cost, such as retaining reset snapshots across boot or exposing support-safe event history. The Decision Journal
(`ARTIFACT-003`) records the field decisions made from incomplete evidence, including confidence and follow-up. The
Mistake Ledger (`ARTIFACT-004`) records assumptions that escaped into the field, such as assuming a debug-only log was
enough or assuming manufacturing identity could be joined to diagnostics later. The Weak Signal Register
(`ARTIFACT-007`) and the vocabulary of Weak Signal (`VOCAB-002`) help the team notice early patterns before they become
confirmed failures.

The product does not need a perfect observability platform to do this well. It needs enough durable, owned, support-safe
evidence to make decisions less speculative. The hard work is deciding what the product must remember when everything
else is unavailable.

## Engineering Principle

Design observability around decisions, not volume. Name the state transitions, boundary outcomes, versions, variants,
reset context, and failure evidence the product must preserve so people without a debugger can decide what happened and
what to do next.

Useful design questions are small and direct:

- What field decision will this evidence support?
- Which component owns the fact?
- What boundary outcome or state transition does it name?
- What context must survive reset, update, recovery, and service access?
- Who can safely see it, and how will they validate it?

## Architecture Exercise

### Make One Failure Explain Itself

Choose one ambiguous field failure or support case from a product you know. It can be a device that stops reporting, a
failed update, a confusing configuration issue, a manufacturing option that changes behavior, or a service tool message
that hides too much.

Write the decision that someone must make from the field evidence. Then identify the missing evidence that currently
forces the team to guess.

Map the relevant state transition or boundary outcome. Name the owner. Draft one event or diagnostic record with a
stable name, payload, severity, retention rule, reset behavior, time or sequence information, version, configuration,
variant, and manufacturing identity fields. Decide whether the record is support-safe, whether any privacy or security
constraint applies, where the decision should be recorded, and how the team will validate that the evidence survives the
failure path.

Your output should be:

1. one decision the evidence must support;
2. one owned event or diagnostic;
3. one retained context requirement;
4. one validation action.

## Principal's Notebook

- Logs are not evidence until someone can use them.
- An event without an owner becomes noise.
- A device should explain enough to be helped.

## ADR

### Chapter ADR: Adopt Decision-Oriented Field Events for Update and Recovery Failures

Status: Accepted for this chapter.

Context:

- Field devices can fail after update, reset, configuration migration, variant selection, gateway interaction, radio
  communication, or recovery.
- Developer debug logs are useful in the lab but are not a stable product promise for support.
- The current service surface can collapse many failure domains into one generic message.
- Manufacturing identity, firmware version, configuration version, variant state, reset context, and update state are
  useful only if they are preserved and visible where field decisions are made.
- RAM, flash, CPU, power, flash wear, bandwidth, privacy, and security limit how much evidence can be retained or
  exposed.
- Adding every possible log line would create Event Explosion rather than useful evidence.

Decision:

- Maintain an Event Catalog for product diagnostics that records owner, name, trigger, payload, severity, retention,
  reset behavior, support visibility, privacy and security constraints, validation, and supported decision.
- Treat update, recovery, reset, configuration, variant, gateway, radio, and reporting outcomes as owned product events
  when they affect field decisions.
- Keep developer debug logs separate from the support-safe diagnostic surface.
- Preserve enough context across reset and recovery to distinguish firmware, configuration, gateway, network, power,
  variant, dependency, and recovery causes.
- Record false diagnostic assumptions and field escapes in the Mistake Ledger.

Consequences:

- Support can make bounded decisions without requiring developer tools for every field issue.
- Engineering can triage update and recovery failures from retained product evidence instead of reconstructed guesses.
- Diagnostic events become part of the product API and require ownership, review, tests, and compatibility care.
- Event versions and deprecation rules must be treated as support promises when tools, tests, or procedures depend on
  event meaning.
- The team must reject noisy events that do not support a decision.
- Storage, power, privacy, security, and service-tool constraints must be designed with the diagnostic surface.

Alternatives Considered:

- Add verbose logging everywhere. Rejected because it increases noise, cost, and ownership ambiguity without guaranteeing
  better decisions.
- Keep diagnostics developer-only. Rejected because support and field operations need evidence when developer tools are
  unavailable.
- Add one generic field error code. Rejected because it hides dependency and boundary differences that require different
  actions.
- Defer diagnostics until after the field trial. Rejected because the first field trial is exactly when preserved
  evidence is most valuable.

## Editor's Commentary

Chapter 23 follows Chapter 22 by making supported product realities explainable in the field. Once a product has named
configurations, variants, manufacturing identity, update paths, recovery paths, and service tools, it also needs a way to
say which of those realities shaped a failure.

This chapter deliberately keeps observability as a chapter-local prose term. It does not add a new PEAK concept or a
primary concept. The PEAK weight stays on Event Catalog (`ARTIFACT-005`) and Event Explosion (`SMELL-006`), supported by
state ownership, API promises, time, evidence, dependency decisions, Change Radius, Discoverability, ADRs, Decision
Journal entries, Mistake Ledger entries, weak signals, Architecture Review, and Architecture Freeze.

It also preserves the boundary with Chapter 24. Chapter 23 asks what field evidence the product must preserve so people
can decide what happened. Chapter 24 can later take those product promises into release discipline, upgrade paths,
rollout control, compatibility, and recovery governance. Chapter 25 remains free to show these ideas in the reference
project rather than repeat the argument here.
