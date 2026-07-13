# Designing for Failure and Recovery

## Opening Quote

> A timeout tells you the wait ended. It does not tell you what the system did.

## Story

The update looked harmless.

The team had a small field device with a communication module, a gateway, and a service tool. The service tool could
install a firmware package onto the device through the gateway. The feature had been added because support teams were
driving to sites for changes that should have been remote.

Nobody thought of the update path as risky architecture. It was "just an operation."

The happy path was short.

The service tool uploaded a package to the gateway. The gateway sent an update command to the device. The device
validated the package header, wrote the package into a staging area, switched the active image after verification, and
reported completion.

The original diagram had five boxes and four arrows. It made the work look smaller than it was.

The first incident came from a site with weak radio coverage. A technician started an update from the service tool. The
device received the command, accepted the package, and began writing to its staging area. Then the gateway lost the
acknowledgment from the device.

The service tool waited.

After thirty seconds, it reported:

```text
Update failed: device did not acknowledge request.
```

The technician tried again.

The second request reached the device while the first update was still in progress. The device had enough local state to
know that it was busy, but not enough state to explain whether the busy work belonged to the same package, a different
package, or a previous incomplete attempt. The gateway logged the second response as a rejected command. The service tool
showed the technician a failure.

Three minutes later, the original update completed.

Now every surface told a different story.

The device was running the new firmware. The gateway's last command log said the retry had been rejected. The service
tool said the update had failed. The support dashboard showed a completion event, but it arrived after the failure event,
so it was grouped under the wrong attempt. The next health check passed, which made the failure look harmless, until
someone asked the question that mattered:

"If the next package depends on this one, are we allowed to send it?"

The logs could not answer.

The team tried the familiar fixes first.

One engineer suggested increasing the timeout from thirty seconds to five minutes. That would reduce false failures, but
it would not explain what happened when the acknowledgment was lost. Another suggested retrying until the device accepted
the request. That made the operation more persistent, but it also made the repeated command more dangerous. Someone else
wanted the gateway to trust the latest event. That worked for the incident report, but it made event order the recovery
model. A fourth person suggested adding a new "still updating" event. That helped visibility, but it did not decide who
owned the truth.

The principal engineer drew four boxes on the whiteboard.

```text
Requested -> Accepted -> Applying -> Completed
```

Then she crossed it out.

"This is not enough. These are happy-path words with one sad arrow missing."

She drew the same line again and added the states the system had already experienced:

```text
Requested
Accepted but not observed
Applying
Completed but reported late
Rejected because another operation owns the device
Unknown to the service tool
Known by the device
```

The room got quieter.

The bug was not that one packet had been lost. Lost packets were allowed. Late events were allowed. Retries were allowed.
The bug was that the system had no designed state for "the command may have succeeded, but the caller does not know yet."

That missing state was the architecture.

The principal engineer asked three questions.

"Who owns the update outcome?"

The answer was the device. The gateway could transport commands. The service tool could initiate work. The dashboard
could display evidence. But the device was the only component that could say whether the package had been accepted,
whether bytes had been made durable, whether the staged image matched the manifest, and whether the active firmware had
changed.

"What does retry mean?"

The answer was not "send the same request again." The first request might still be running. A retry had to mean "ask the
device about the operation, and only repeat the command if the device proves that no compatible operation exists."

"What is the recovery path?"

The answer was not "show an error." Recovery had to return the operator and the device to a known state. Sometimes that
state would be "new firmware installed." Sometimes it would be "old firmware still active." Sometimes it would be
"device applying package; command surface is read-only until completion or manual intervention." But "timeout" by itself
was not a known state.

The design changed.

Every update command received a stable operation identifier derived from the package and the update attempt. The device
persisted the current operation before acknowledging acceptance. The gateway stopped treating a missing acknowledgment as
proof of failure. The service tool changed its retry button into a recovery action: query operation status, reconcile the
view, then decide whether a new command was allowed.

The event model changed too.

The team wrote an Event Catalog for the update flow. `UpdateAccepted` meant that the device had persisted the operation
record. `UpdateApplying` meant that the device had begun changing local staging state. `UpdateCompleted` meant that the
device had verified and activated the package. `UpdateAbandoned` meant that the device had proven that no active or
recoverable operation remained. Each event named its producer, consumers, ordering assumptions, and recovery behavior.

The gateway still dropped messages sometimes.

That was no longer the interesting part.

When the acknowledgment was lost again in a test, the service tool showed:

```text
Update status unknown. Checking device state.
```

Then:

```text
Update accepted by device. Applying package.
```

The operator no longer had to guess whether pressing retry would help or harm the system.

The incident report changed from "lost acknowledgment caused update failure" to "lost acknowledgment exposed undefined
operation outcome." That wording mattered. It moved the team from packet folklore to architecture.

## Discussion

Failure design starts by refusing to let one symptom name the system state.

A timeout is a symptom. A dropped acknowledgment is a symptom. A rejected retry is a symptom. A late completion event is a
symptom. Each may be useful evidence, but none is automatically the truth. Chapter 3 made this distinction when it argued
that observation and explanation are different things. In recovery work, confusing them is how systems turn a recoverable
interruption into a durable contradiction.

The failure story in this chapter is a concrete form of `FAILURE-002`: one lost packet exposes the hidden architecture.
The lost packet does not create every weakness. It reveals that the operation had no explicit owner, no durable outcome
model, and no safe meaning for retry.

Designing for failure is not the same as writing more error handlers.

An error handler catches a local condition. Recovery architecture defines what the whole system is allowed to believe and
do after the condition occurs. The difference matters because many serious failures are not local. They cross a boundary,
arrive late, duplicate a command, leave partial state behind, or give two surfaces enough evidence to disagree.

The first recovery question is ownership.

`LAW-001` says that every meaningful state must have one clear owner. This is easy to accept when the state is a value in
a database. It is harder when the state is an operation outcome. In the story, the service tool wanted to own the user's
view, the gateway wanted to own the command log, and the dashboard wanted to own the latest event. None of those surfaces
owned the update outcome. The device did.

Once that ownership was named, the design became less mystical.

The gateway could say, "I transported a command, or I did not observe a response." The service tool could say, "The user
requested an update, and my current view is unknown." The dashboard could say, "I have observed these events." The device
could say, "This operation is accepted, applying, completed, abandoned, or not known." Each sentence has a boundary. Each
sentence has a source.

This is why hidden state is so dangerous. `SMELL-004` appears whenever state affects behavior but is not visible through a
clear owner, interface, or model. The hidden state in the story was not merely the firmware version. It was the outcome of
an operation that had crossed several boundaries. Until that outcome had an owner, every component was tempted to invent
one.

The second recovery question is promise.

`LAW-002` says that an API promises behavior, meaning, errors, timing, and ownership. That promise includes failure
semantics. If a command returns no acknowledgment, what does the caller know? If the caller sends the same command again,
is that a transport retry, a user retry, a recovery query, or a new operation? If completion arrives after failure has
already been shown, does completion override failure, create a conflict, or require reconciliation?

These questions belong in the API contract, not in scattered comments around retry code.

Many systems make retry look like a mechanical behavior. Try three times. Wait longer each time. Give up after a limit.
Those rules can be useful, but they do not define the meaning of the operation. Retrying a status read is different from
retrying a payment, an update, a migration, a deletion, or a command to open a valve. The architectural question is not
"how many times should we retry?" The question is "what is safe to repeat, and what evidence do we need before repeating
it?"

That is why retry belongs next to ownership and outcome.

If an operation can be repeated safely, the contract should say why. If repeating it creates a second operation, the
contract should make that visible. If the caller must query before repeating, the query is part of recovery, not a
convenience endpoint. If the only safe answer is "block until a human inspects the device," that is still a design. It is
better than pretending that repeated uncertainty will become certainty.

The third recovery question is time.

Chapter 10 already owns temporal dependency as a subject. Chapter 16 uses time as a recovery input. `LAW-003` matters
here because timeouts, deadlines, ordering assumptions, and late arrivals are all contracts. A timeout does not prove the
remote side failed. It proves that the local waiting policy expired. That is a narrower statement, and the narrower
statement is the honest one.

Once the team accepted that distinction, they stopped treating a timeout as a verdict.

The service tool could say, "The request did not produce an observed acknowledgment within thirty seconds." It could not
say, "The device did not accept the request." The gateway could say, "I did not deliver a response to the caller." It
could not say, "The operation did not start." The device could answer the operation-status query. If the device was
unreachable, the system had to report that the outcome was unknown, not failed.

Unknown is not a comfortable state, but it is often the truthful one.

A mature recovery design gives unknown a bounded place to live. It defines what work is allowed while the outcome is
unknown, what work is blocked, what evidence can resolve the unknown, and who is responsible for escalation if the
unknown persists. Without those boundaries, unknown leaks into user behavior, support procedures, dashboards, and future
features.

The fourth recovery question is dependency.

`LAW-007` says a dependency commits the system to behavior, failure modes, lifecycle, ownership, and replacement cost.
The gateway in the story was not just a pipe. It imported the failure behavior of an unreliable network and the lifecycle
of a message transport that could delay, drop, or reorder observations. The firmware update design had to treat that
dependency as part of the recovery model.

`SMELL-001` often appears here. A hidden dependency is not only an unlisted library or service. It can be an assumption
that "the acknowledgment will arrive before the retry" or "the latest event is the authoritative event." Those are
dependencies on timing and order. If they are not named, they become folklore.

The fifth recovery question is evidence.

`LAW-005` says confidence follows evidence. Recovery cannot depend on confidence that no one has earned. The team needed
tests that dropped acknowledgments, delayed completions, repeated commands, restarted the gateway, restarted the device,
and disconnected the service tool. Not because tests make failure impossible, but because tests expose which claims the
architecture can actually support.

Evidence also belongs in the decision record.

The team used a Decision Journal, `ARTIFACT-003`, while the design was still moving. They recorded the current decision,
the evidence behind it, their confidence level, and the trigger that would force a revisit. That was useful because some
answers were provisional. For example, they were confident that the device should own the operation outcome. They were
less confident that the first status-query interval was right for weak radio sites. The journal let them separate settled
architecture from operational tuning.

When the design stabilized, they wrote a small ADR, `ARTIFACT-001`. The ADR did not pretend that every failure was known.
It recorded the decision to make operation recovery explicit, the consequences of putting outcome ownership on the
device, and the alternatives they had rejected.

Events needed the same discipline.

Without an Event Catalog, `ARTIFACT-005`, the team had been using event names as if everyone understood them. They did
not. One consumer treated `UpdateAccepted` as proof that the firmware was changing. Another treated it as proof that the
gateway had queued a command. A third treated it as a user-facing success signal. These meanings were incompatible.

`SMELL-006` is event growth without clear meaning, ownership, or lifecycle. It is tempting to fix a recovery problem by
adding one more event for each confusing incident. That can improve visibility for a week and make the architecture worse
for a year. A recovery event should have a producer, a meaning, intended consumers, timing assumptions, and failure
behavior. If the event cannot answer those questions, it may be noise with a formal name.

Callback-heavy designs make this harder.

`ANTIPATTERN-005` appears when control flow is spread across callbacks so that ordering, errors, and state transitions
are no longer visible in one place. In the story, late completion arrived through one path, retry rejection through
another, and user failure through a third. Each callback was locally reasonable. Together they formed a recovery model no
one could see.

The repair was not to ban callbacks. The repair was to name the operation state and force callbacks to update that state
through one owner. Once the update outcome had a durable owner, callback order stopped being the architecture.

Workarounds deserve suspicion too.

`ANTIPATTERN-006` shows up when a workaround has no owner, review trigger, or removal plan. "If update status is unknown,
ask the technician to reboot the device" might be an acceptable emergency procedure. It is not an architecture unless it
has an owner, a reason, a review trigger, and a path out. Otherwise the workaround becomes a hidden recovery protocol
that future engineers inherit without context.

Designing for recovery does not mean designing a perfect rescue for every event.

Some failures are unrecoverable at the current boundary. Some require human inspection. Some require replacement
hardware. Some must fail closed. Some should degrade service and preserve evidence. The architectural work is to make
those outcomes explicit before the system discovers them under pressure.

A useful recovery model usually names five things.

First, it names the consequential operation. Not every function call deserves this treatment. But operations that move
money, change identity, alter permissions, migrate data, update firmware, delete records, publish decisions, or change
physical state deserve it.

Second, it names the owner of the operation outcome.

Third, it names the observable states that other components are allowed to depend on.

Fourth, it names what retry means in each state.

Fifth, it names the path back to a known state.

The last phrase is important. Recovery does not always mean going back to the old state. After a package is installed,
the known state may be "new version active." After a partial write, the known state may be "old version active and staged
package discarded." After a long outage, the known state may be "operation unknown; dependent operations blocked until
device inspection." The system should not lie to make the state feel cleaner.

The principal engineer's responsibility is to keep the design honest at exactly this point.

Teams under deadline often want to collapse failure into a status code. They want "failed" to cover "not attempted,"
"attempted but not observed," "accepted but still running," "completed late," "completed but not reported," "partially
applied," and "state cannot be read." That collapse makes dashboards simpler and recovery harder.

A good architecture keeps the important distinctions even when the UI chooses simpler language.

The operator may see "checking device state." The support tool may see "operation outcome unknown." The device may store
"accepted and applying." The ADR may say "timeouts are not failure verdicts." These layers do not need to expose the same
words, but they must preserve the same truth.

Failure design is therefore a kind of restraint.

Do not turn every symptom into a conclusion. Do not turn every late event into authority. Do not turn every retry into a
new command. Do not turn every workaround into invisible policy. Do not let every consumer invent its own meaning for the
same event.

The goal is not dramatic resilience language. The goal is a system that can say, under stress, "Here is what we know,
here is what owns that knowledge, here is what is safe to do next, and here is how we get back to a known state."

## Engineering Principle

Design the state after failure as carefully as the happy path. For every consequential operation, define the outcomes,
retry safety, containment, evidence, and path back to a known state.

Use these questions when reviewing a failure path:

- What operation is consequential enough to require explicit recovery design?
- Who owns the outcome of that operation?
- What can each boundary honestly say after a timeout, dropped response, restart, or late event?
- Which states are observable, durable, and safe for other components to depend on?
- What does retry mean in each state?
- What evidence is required before repeating the command?
- What work is blocked while the outcome is unknown?
- What work can continue in a degraded mode?
- Which events carry recovery meaning, and who owns those meanings?
- What review trigger will reopen the decision when field evidence changes?

## Architecture Exercise

### Design One Failure Path Before It Fails

Choose one operation in your system that changes durable state, external state, user trust, money, permissions, physical
behavior, or operational safety.

Do not choose the whole system. Choose one operation.

Write the operation name at the top of the page. Then answer the following:

- What is the happy-path completion state?
- What component owns the authoritative outcome?
- What evidence proves the operation was accepted?
- What evidence proves the operation started?
- What evidence proves the operation completed?
- What evidence proves the operation did not start?
- What evidence proves that the outcome is unknown?
- What can arrive late?
- What can be duplicated?
- What can be lost?
- What can be reordered?
- What state survives a restart?
- What state is reconstructed from events?
- What does retry mean before acceptance?
- What does retry mean after acceptance?
- What does retry mean while completion is unknown?
- What user action is blocked while recovery is unresolved?
- What user action remains safe?
- What event names require catalog entries?
- What workaround exists today, and who owns its removal or review?

Now draw the recovery path.

Start from one concrete failure:

```text
The caller times out after sending the command.
```

Do not stop at "return error." Continue until the system reaches a known state.

Your output should include:

- One owner for the operation outcome.
- A small set of named operation states.
- The meaning of retry in each relevant state.
- The evidence needed to move from unknown to known.
- One event catalog entry for the most important recovery event.
- One decision-journal entry for any assumption that still has weak evidence.
- One ADR only if the recovery model changes a boundary, API promise, or ownership decision.

If the exercise produces only status codes, keep going. Status codes report symptoms. Recovery design explains what the
system believes and what it may safely do next.

## Principal's Notebook

- A timeout is not proof of failure.
- Retry without outcome semantics repeats uncertainty.
- Recovery returns to a known state, not always the old state.

## ADR

### Chapter ADR: Make Firmware Update Recovery Explicit After Lost Acknowledgment

#### Status

Accepted.

#### Context

The firmware update flow crosses the service tool, gateway, network, and device. A lost acknowledgment can leave the
service tool unsure whether the device accepted the update command. The previous design treated the caller timeout as a
failure and allowed the user to retry the command. Field evidence showed that the first command could still be applying
when the retry arrived.

This created conflicting views:

- The device could be applying or already running the new firmware.
- The gateway could record a missing acknowledgment or rejected retry.
- The service tool could report failure.
- The dashboard could receive a late completion event.

The system lacked an explicit owner for the update outcome and lacked a recovery path from unknown to known.

#### Decision

The device owns the firmware update outcome.

Every update command uses a stable operation identifier. The device persists the operation record before acknowledging
acceptance. The service tool must treat a missing acknowledgment as an unknown outcome, not proof of failure. Retry from
unknown first queries device operation status. A repeated command is allowed only when the device proves that no
compatible operation is active, completed, or recoverable.

The update event catalog will define `UpdateAccepted`, `UpdateApplying`, `UpdateCompleted`, and `UpdateAbandoned`,
including producer, consumers, meaning, ordering assumptions, and recovery behavior.

The service tool will block dependent update commands while the current operation outcome is unknown. It may continue
read-only diagnostics that do not depend on the update result.

#### Consequences

The update path gains an explicit recovery model instead of relying on timeout interpretation. Operators receive a more
accurate status when the system is uncertain. The gateway remains a transport and observation surface, not the owner of
the operation outcome.

The device must persist enough operation state to answer recovery queries after restart. Tests must cover dropped
acknowledgments, delayed completion, repeated commands, gateway restart, device restart, and service-tool disconnect.

The design adds some protocol complexity, but it removes a more dangerous ambiguity: treating an unobserved response as a
failed operation.

#### Alternatives Considered

Increase the caller timeout.

This reduces the number of visible timeouts but does not define what happened when the timeout still occurs. It also makes
operators wait longer without improving the truth model.

Retry the command automatically.

This can duplicate a consequential operation unless the device can prove that repetition is safe. Automatic repetition
without outcome semantics was rejected.

Trust the latest event.

This makes event arrival order the recovery model. Late events can repair some displays, but they cannot own the
operation outcome.

Require manual reboot after unknown status.

This may remain an emergency procedure, but it is not acceptable as the normal recovery model. If retained, it needs an
owner, evidence, and a review trigger under `ANTIPATTERN-006`.

## Editor's Commentary

Chapter 16 is the recovery chapter for the Architecture Playbook. Earlier chapters set up its materials. Chapter 7 named
state ownership. Chapter 8 made API promises include errors, timing, and repeated calls. Chapter 10 separated timing
evidence from timing conclusions. Chapter 14 placed boundaries and handoffs under architectural scrutiny. Chapter 15
mapped the affected surfaces before change. This chapter turns those tools toward the question that appears when the
happy path breaks: what is the system allowed to believe now?

The chapter deliberately centers `FAILURE-002`, One Lost Packet. The lost packet is not a networking lesson. It is a
small event that exposes missing ownership, hidden state, unclear retry meaning, and event ambiguity. That keeps the
chapter inside the book's core canon: architecture is the discipline of making consequential decisions explicit before
they become accidental behavior.

No new primary concept is introduced here. The chapter illustrates and connects existing PEAK material: `LAW-001`,
`LAW-002`, `LAW-003`, `LAW-005`, `LAW-007`, `SMELL-001`, `SMELL-004`, `SMELL-006`, `ANTIPATTERN-005`,
`ANTIPATTERN-006`, `ARTIFACT-001`, `ARTIFACT-003`, and `ARTIFACT-005`. It uses them as a working recovery model rather
than registering a new concept.

The boundary with later chapters is also intentional. The ADR in this chapter is local and illustrative; Chapter 17 owns
the broader practice of ADRs and RFCs. Chapter 18 will own architecture review. Chapter 19 will own freeze. Chapter 16
stops at the recovery design boundary.
