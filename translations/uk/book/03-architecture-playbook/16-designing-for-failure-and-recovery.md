# Проєктування для відмов і відновлення

## Вступна цитата

> Timeout каже, що очікування закінчилося. Він не каже, що зробила system.

## Історія

Update виглядав harmless. Team мала small field device з communication module, gateway і service tool. Service tool міг install firmware package onto device through gateway, щоб support teams не їздили на sites для remote-capable changes.

Happy path був short: service tool uploaded package to gateway, gateway sent update command, device validated package header, wrote package into staging area, switched active image after verification and reported completion.

Original diagram had five boxes and four arrows. It made work look smaller than it was.

First incident came from weak radio coverage. Technician started update. Device received command, accepted package and began writing to staging area. Then gateway lost acknowledgement from device.

Service tool waited and after thirty seconds reported:

```text
Update failed: device did not acknowledge request.
```

Technician tried again. Second request reached device while first update was still in progress. Device knew it was busy, but not whether busy work belonged to same package, different package or previous incomplete attempt. Gateway logged second response as rejected command. Service tool showed failure.

Three minutes later original update completed. Device was running new firmware; gateway last command log said retry rejected; service tool said update failed; dashboard saw completion after failure and grouped it under wrong attempt. Then came real question: if next package depends on this one, are we allowed to send it?

Logs could not answer.

Familiar fixes appeared: increase timeout, retry until accepted, trust latest event, add «still updating» event. Each helped symptom; none decided who owned truth.

Principal Engineer drew happy-path states:

```text
Requested -> Accepted -> Applying -> Completed
```

Then crossed them out: happy-path words with recovery branch missing. She added states system had already experienced:

```text
Requested
Accepted but not observed by the caller
Applying
Completed but reported late
Rejected because another operation owns the device
Unknown to the service tool
Known by the device ???????
```

Bug was not lost packet. Lost packets, late events and retries were allowed. Bug was missing designed state for «command may have succeeded, but caller does not know yet».

Principal Engineer asked: who owns update outcome? Device. Gateway transports, service tool initiates, dashboard displays evidence, but only device can say package accepted, bytes durable, staged image matched manifest and active firmware changed.

What does retry mean? Not «send same request again». Retry means query operation status and repeat command only if device proves no compatible operation exists.

What is recovery path? Not «show error». Recovery returns operator and device to known state: new firmware installed, old firmware active, device applying package with command surface read-only, or operation unknown with escalation.

Design changed. Every update command got stable operation identifier. Device persisted current operation before acknowledging acceptance. Gateway stopped treating missing acknowledgement as proof of failure. Service tool retry button became recovery action: query status, reconcile view, then decide whether new command is allowed.

Event model changed. Event Catalog (`ARTIFACT-005`) defined `UpdateAccepted`, `UpdateApplying`, `UpdateCompleted` and `UpdateAbandoned`: producer, consumers, ordering assumptions and recovery behavior.

Gateway still dropped messages sometimes. That was no longer interesting. When acknowledgement was lost again, service tool showed:

```text
Update status unknown. Checking device state.
```

Then:

```text
Update accepted by device. Applying package.
```

Operator no longer guessed whether retry would help or harm system. Incident wording changed from «lost acknowledgement caused update failure» to «lost acknowledgement exposed undefined operation outcome».

## Обговорення

Failure design starts by refusing to let one symptom name system state. Timeout, dropped acknowledgement, rejected retry and late completion event are evidence, not automatically truth.

This story is concrete `FAILURE-002`: one lost packet exposes hidden architecture. Packet did not create every weakness; it revealed no explicit ???????, no durable outcome model and no safe retry meaning.

Designing for failure is not writing more error handlers. Error handler catches local condition. Recovery architecture defines what whole system may believe and do after condition occurs.

First recovery question is ownership. `LAW-001` says every meaningful state has one clear ???????. Operation outcome is state. Service tool owns user view, gateway owns transport observation, dashboard owns observed events, but device owns update outcome.

Second question is promise. `LAW-002` says API promises behavior, meaning, errors, timing and ownership. That includes failure semantics: what missing acknowledgement means, what repeated command means, and whether late completion overrides failure or requires reconciliation.

Retry is architectural. Retrying status read differs from retrying payment, update, migration, deletion or physical command. Question is not how many times to retry; it is what is safe to repeat and what evidence is needed.

Third question is time. `LAW-003` matters because timeouts, deadlines, ordering and late arrivals are ?????????. Timeout proves local waiting policy expired; it does not prove remote side failed. Unknown may be uncomfortable, but it can be truthful.

Mature recovery design gives unknown bounded place: what work is allowed, what is blocked, what evidence resolves unknown and who escalates if it persists.

Fourth question is dependency. `LAW-007` says dependency imports behavior, failure modes, lifecycle and replacement cost. Gateway is not just pipe; it imports unreliable network behavior.

Fifth question is evidence. `LAW-005` says confidence follows evidence. Tests must drop acknowledgements, delay completions, repeat commands, restart gateway/device, interrupt power during staged write and disconnect service tool.

Events need discipline. Without Event Catalog (`ARTIFACT-005`), event names pretend everyone understands them. `SMELL-006` appears when event growth lacks meaning, ownership or lifecycle.

Callback-heavy designs make recovery harder. `ANTIPATTERN-005` appears when ordering, errors and state transitions spread across callbacks. Repair is not banning callbacks; repair is naming operation state and forcing callbacks to update it through one ???????.

Workarounds need ???????, trigger and removal path. Otherwise `ANTIPATTERN-006` turns emergency recovery into hidden protocol.

A useful recovery model names: consequential operation, ??????? of outcome, observable states, retry meaning in each state and path back to known state. Known state may be new version active, old version active, operation unknown with dependent operations blocked, or human inspection required.

Good architecture keeps important distinctions even when UI chooses simpler language.

## Інженерний принцип

Design the state after failure as carefully as happy path. For every consequential operation, define outcomes, retry safety, containment, evidence and path back to known state.

Review questions:

- What operation requires explicit recovery design?
- Who owns operation outcome?
- What can each ???? honestly say after timeout, dropped response, restart or late event?
- Which states are observable, durable and safe to depend on?
- What does retry mean in each state?
- What evidence is required before repeating command?
- What work is blocked while outcome unknown?
- What work can continue degraded?
- Which events carry recovery meaning, and who owns them?
- What trigger reopens decision when field evidence changes?

## Архітектурна вправа

### Design One Failure Path Before It Fails

Choose one operation that changes durable state, external state, trust, money, permissions, physical behavior or operational safety.

Answer: happy-path completion state, ???????, evidence accepted/started/completed/not started/unknown, late/duplicated/lost/reordered events, state surviving power loss, state reconstructed from events, retry meaning before/after acceptance and during unknown, blocked and safe user actions, event names needing catalog entries, workaround and ???????.

Start from:

```text
The caller times out after sending the command.
```

Do not stop at «return error». Continue until known state.

Output: one ???????, named states, retry meaning, evidence from unknown to known, one Event Catalog entry, one Decision Journal entry for weak assumption, and ADR only if recovery changes ????/API/ownership.

## Нотатник Principal Engineer

- Timeout is not proof of failure.
- Retry without outcome semantics repeats uncertainty.
- Recovery returns to known state, not always old state.

## ADR

### Chapter ADR: Make Firmware Update Recovery Explicit After Lost Acknowledgment

#### Status

Accepted.

#### Context

Firmware update flow crosses service tool, gateway, network and device. Lost acknowledgement can leave service tool unsure whether device accepted command. Previous design treated caller timeout as failure and allowed retry. Field evidence showed first command could still be applying when retry arrived.

Views conflicted: device applying or new firmware active; gateway missing acknowledgement or rejected retry; service tool failure; dashboard late completion. System lacked ??????? for outcome and recovery path from unknown to known.

#### Decision

Device owns firmware update outcome. Every update command uses stable operation identifier. Device persists operation record before acknowledging acceptance. Service tool treats missing acknowledgement as unknown outcome, not failure. Retry from unknown first queries device operation status. Repeated command allowed only when device proves no compatible operation active, completed or recoverable.

Event catalog defines `UpdateAccepted`, `UpdateApplying`, `UpdateCompleted` and `UpdateAbandoned`. Service tool blocks dependent update commands while outcome unknown; read-only diagnostics may continue.

#### Consequences

Update path gains explicit recovery model. Operators receive accurate uncertainty. Gateway remains transport and observation surface. Device must persist enough state for recovery after restart/power loss. Tests cover dropped acknowledgements, delayed completion, repeated commands, restarts, power interruption and service-tool disconnect.

#### Alternatives Considered

- Increase timeout. Reduces visible timeouts but does not define truth.
- Retry automatically. Can duplicate consequential operation.
- Trust latest event. Makes event arrival order recovery model.
- Require manual reboot after unknown status. Emergency procedure only if owned and reviewed under `ANTIPATTERN-006`.

## Коментар редактора

Chapter 16 is recovery chapter for Architecture Playbook. It centers `FAILURE-002`, One Lost Packet, and connects `LAW-001`, `LAW-002`, `LAW-003`, `LAW-005`, `LAW-007`, `SMELL-001`, `SMELL-004`, `SMELL-006`, `ANTIPATTERN-005`, `ANTIPATTERN-006`, `ARTIFACT-001`, `ARTIFACT-003` and `ARTIFACT-005`. It stops at recovery design ????; Chapter 17 owns broader ADR/RFC practice.
