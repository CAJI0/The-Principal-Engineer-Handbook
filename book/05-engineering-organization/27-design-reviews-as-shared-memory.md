# Design Reviews as Shared Memory

## Opening Quote

> A review is useful only when its reasoning can travel farther than the room.

## Story

### The Review Everyone Attended and Nobody Remembered

Three months after the provisioning compatibility decision closed, the team was surprised to discover that everyone had
agreed and almost nobody remembered what they had agreed to.

The decision had seemed responsible at the time.

The provisioning change touched firmware behavior, backend assumptions, service tooling, manufacturing provisioning,
support diagnostics, and release timing. The device would own final provisioning acceptance. The backend would own
reservation and entitlement. Manufacturing would write a bounded package and record station evidence. The service tool
would expose compatible operator behavior. Support would receive enough diagnostic meaning to explain failed
provisioning without asking a firmware engineer to read raw state. Release would support the new path only for named
firmware and service-tool versions.

Mara had helped shape the work in the previous chapter, but she did not own the decision by authority. The product
architecture owner owned the final boundary. Firmware, backend, manufacturing, service tooling, support, test, and
release owned affected surfaces. Mara's job was to keep the decision reviewable without becoming its hidden owner.

The design review looked like a success.

Important people attended. The slides were polished. The RFC was linked in the invite. The ADR draft was visible at the
end. Senior engineers asked useful questions. Manufacturing challenged station-package timing. Support asked about
field diagnosis. Backend asked whether the compatibility adapter had an expiration condition. Firmware explained why
device-owned acceptance was safer than backend-owned readiness. Nobody raised a major objection. The room reached the
ordinary sentence teams learn to trust:

> This looks approved.

The implementation moved.

Then Alex joined the team.

He was a new engineer assigned to clean up a confusing test around old service-tool behavior. The test expected an older
tool to receive a compatible response from the backend even though the device owned final acceptance. Alex found the ADR.
It said the device owned final provisioning acceptance. It said the backend owned reservation and entitlement. It listed
alternatives. It did not say why the team had chosen this boundary over backend-owned readiness. It did not explain the
service-tool assumption that made the temporary compatibility adapter necessary. It did not preserve the concerns that
had shaped the review.

Alex asked a simple question:

> Why did this design win?

No one could answer cleanly.

The failure was not only ramp-up.

Manufacturing believed an unsupported option had been approved. A station engineer remembered discussion about letting
the station write a richer provisioning package for old devices and assumed it had survived as a fallback path. Firmware
had rejected that option during review because it would make station behavior a second authority for provisioning
meaning. The rejection lived only in someone's memory.

Support repeated a rejected diagnostic request. They asked for one detailed firmware code to appear in the service tool
because technicians wanted a single visible reason. During review, the team had rejected that option because it would
turn private firmware diagnostics into a product-level API promise. The service tool was supposed to translate stable
product reasons and keep raw firmware detail diagnostic. The ADR recorded the final service-tool boundary, but not the
rejected request or why it mattered.

Backend treated the temporary compatibility workaround as permanent. The adapter for one older service-tool version had
an owner during the review, but the owner was never written beside the accepted risk. No removal condition appeared in
the Architecture Ledger. A comment in code said "temporary." The review had created a Temporary Solution
(`ANTIPATTERN-006`) with the right intent and then failed to leave behind the owner and trigger that would keep it
temporary.

One risk had no follow-up owner at all. The old service tool could mislabel an expired backend package as a device
rejection. That risk had been discussed, accepted for one release, and assigned to a service-tool follow-up in the room.
The follow-up ticket existed, but the review notes did not connect it to the decision. When the ticket moved teams, the
reason moved with nobody.

The records were close enough to be painful.

The ADR recorded the final decision, but not the review concerns that shaped it. The review notes listed attendees and
topics, but not trade-offs, rejected options, evidence gaps, ownership decisions, or revisit triggers. The RFC had a
comment thread with good questions, but the final outcome did not close those questions into durable memory. The
Architecture Ledger had a row for the active provisioning decision, but it did not point to the review outcome or the
compatibility adapter trigger.

The next meeting opened with blame disguised as analysis.

"Why did the review not prevent this?"

Mara did not answer by defending the meeting. The meeting had done useful work. People had asked the right questions.
The design was better because manufacturing, backend, service tooling, support, release, and test were in the room.

She wrote a different sentence:

> The review was not finished when the meeting ended. It was finished when its reasoning became reusable.

That changed the investigation.

The problem was not that the review had failed to produce agreement. The problem was that the agreement could not travel.
A future engineer could find the decision, but not the shape of the reasoning. A support owner could find the diagnostic
boundary, but not the rejected request. Manufacturing could find the accepted package flow, but not the option that had
been declined. Backend could find the compatibility adapter, but not why it was temporary or when it should expire.

Mara asked the team to reconstruct the review around the person who was not in the room.

What should Alex have been able to understand six months later?

He should have found the decision statement: device-owned provisioning acceptance, backend-owned reservation and
entitlement, bounded manufacturing package write, service-tool translation, and named compatibility support for one
older tool version.

He should have found the context and constraints: old devices in the field, station timing, backend package expiry,
service-tool version drift, support diagnosis, release date, and the need to avoid two authorities for provisioning
state.

He should have found the owner and affected owners: the product architecture owner for the accepted decision; firmware,
backend, manufacturing, service tooling, support, test, and release for their surfaces.

He should have found the alternatives: backend-owned readiness, manufacturing final readiness, station-written legacy
package expansion, raw diagnostic forwarding, and a permanent backend compatibility adapter.

He should have found evidence and uncertainty: firmware acceptance tests, old service-tool behavior, station package
proof, backend expiry behavior, and the missing evidence around mislabeled package rejection.

He should have found trade-offs, risks, assumptions, rejected options, review outcome, follow-up actions, owners,
revisit triggers, and links to the RFC, ADR, Decision Journal entries, Architecture Ledger row, compatibility matrix,
and release note.

None of that required a new artifact.

It required the existing artifacts to agree about what memory each carried.

The RFC would keep the proposal history and the questions that changed the decision. The review notes would close with
an outcome rather than an attendance list. The ADR would preserve the accepted decision, context, alternatives, evidence
that mattered, consequences, owner, and revisit trigger. The Decision Journal would hold smaller follow-ups: the old
service-tool mislabel risk, station package evidence, and compatibility adapter removal condition. The Architecture
Ledger would point to the active decision, owner, status, linked records, review date, and next trigger.

The team updated the records.

They did not rewrite history to make the review look cleaner. They named the concerns that had shaped the decision.
They recorded why manufacturing final readiness had been rejected: it would create competing ownership for provisioning
state. They recorded why raw firmware codes stayed out of the service tool: they were diagnostics, not product promises.
They recorded the backend adapter as temporary with one owner, one supported service-tool version, one removal trigger,
and one date to review. They recorded the old service-tool mislabel risk as accepted for the current release with a
follow-up owner.

They also made the practice lighter than the problem.

Mara did not ask every small decision to receive this treatment. A local display tweak inside the service tool did not
need a formal design review. A reversible backend log change did not need an ADR. A small test cleanup did not need the
Architecture Ledger. But the provisioning compatibility decision crossed firmware, backend, manufacturing, service
tooling, support diagnostics, and release timing. Its Change Radius (`VOCAB-001` and `METRIC-001`) was broad enough
that memory was part of the design.

The review had not been useless.

It had been unfinished.

## Discussion

Design reviews are useful when they make reasoning durable.

That sentence is more demanding than "the meeting went well." A review can feel successful because important people
attended, senior engineers asked good questions, nobody objected loudly, and the team left with momentum. Those signals
matter. They are not organizational memory.

Review for memory, not performance.

The subject of a design review is not the deck, the meeting, the seniority of the room, or the apparent approval. The
subject is the decision and the reasoning future work will depend on. A good review leaves behind enough memory that
someone who was not in the room can understand why the system is the way it is, which promises were accepted, which
options were rejected, and what should cause the team to revisit the choice.

This does not make design review a documentation ceremony.

The goal is not to collect notes. The goal is to make the useful parts of the review survive the review. If the meeting
exposes a hidden dependency, but the dependency never appears in the RFC, ADR, Decision Journal, or Architecture Ledger,
the organization has learned only locally. If the room rejects an option, but the rejection is not findable later, the
option will return with fresh confidence and no memory. If a risk receives a verbal owner, but the owner is not attached
to a follow-up record, the risk becomes background.

A review succeeds when the organization can later understand the decision.

That future audience is broad. It includes the engineer changing the code, the manufacturing owner maintaining a
station script, the support lead explaining behavior in the field, the release owner deciding whether a version pair is
supported, the backend engineer deleting a compatibility adapter, and the Principal Engineer who is trying not to become
the only path back to history.

Silence in the room is not enough.

Silence may mean agreement. It may mean fatigue. It may mean the right person was absent. It may mean the concern is
hard to phrase. It may mean the design is good. The record should not depend on interpreting silence. It should state
the outcome: accepted, accepted with changes, narrowed, deferred, split, rejected, sent for evidence, escalated, or
scheduled for revisit.

The memory of a consequential review has recognizable parts.

It should name the decision under review. It should name the context and constraints. It should identify the decision
owner and the affected owners. It should preserve alternatives, including the rejected options that future teams may be
tempted to rediscover. It should separate evidence from assumption and confidence from hope. It should state trade-offs,
risks, responses, open questions, follow-up actions, owners, and revisit triggers. It should link to the RFC, ADR,
Decision Journal, Architecture Ledger, tests, compatibility matrix, release note, support diagnostic, or code surface
that will help the future reader travel from behavior to reasoning.

This is where Chapter 27 differs from Chapter 18.

Chapter 18 asked whether Architecture Review (`RITUAL-001`) happens before the decision hardens. It taught review timing,
participants, evidence, and closure while alternatives are still real. Chapter 27 uses that review ritual as a memory
source. The review may have happened at the right time and still leave the organization with private memory if its
reasoning does not land in durable records.

The distinction with Chapter 17 matters too.

Chapter 17 taught ADR (`ARTIFACT-001`) and RFC (`ARTIFACT-002`) practice: proposal versus decision, status, closure,
and discoverability. Chapter 27 does not reteach those mechanics. It asks whether the design review updates the right
records so future work can reuse the reasoning. An RFC may carry the proposal and open questions. An ADR may preserve
the accepted decision. A Decision Journal (`ARTIFACT-003`) may carry smaller evidence gaps, temporary judgments, and
follow-up triggers. An Architecture Ledger (`ARTIFACT-006`) may index the active decision, owner, status, links, and
review date.

The containers are not the point.

The point is that review memory has to live somewhere findable.

A design review is also not a status meeting. Status asks where the work is. Design review asks whether the decision
and its reasoning can survive future change. It is not implementation review. Implementation review asks whether the
chosen design is being built correctly. Design review asks whether the design, trade-offs, assumptions, and owners are
responsible before they become expensive. It is not code review. Code review can catch defects and local design issues,
but it is usually too narrow for cross-team provisioning, manufacturing, support, release, and compatibility memory.

A design review is not an approval gate by default.

Some organizations require approval for certain changes. That can be legitimate. But approval without memory is weak.
Approval can even be harmful when it makes people believe the decision is safer than it is. The useful outcome is not a
ceremonial yes. The useful outcome is an owned decision with preserved reasoning.

A design review is not an escalation meeting either.

Escalation asks a formal authority to resolve a decision the current owners cannot responsibly close. Design review
should make escalation less mysterious by showing the decision, evidence, affected owners, unresolved conflict, and
consequence. But most design reviews should close inside the responsible ownership model, not turn every hard trade-off
into hierarchy.

Not every design decision needs formal review.

Proportionality is part of engineering judgment. A reversible local choice inside one owned boundary may need only code
review, a test, or a short Decision Journal entry. A decision with persistent data, protocol promises, state ownership
changes, dependency commitments, manufacturing impact, support diagnostics, release timing, or broad Change Radius
usually deserves review memory strong enough to survive turnover.

Every State Has One Owner (`LAW-001`) is a memory question.

If a review decides who owns provisioning state, calibration validity, readiness, compatibility, or support-visible
meaning, the record must preserve that owner. Shared review does not mean shared ownership. Affected owners may shape,
challenge, and carry consequences. The decision still needs one accountable owner for the accepted architectural
outcome.

Every API Is a Promise (`LAW-002`) is also a memory question.

The service-tool response, backend package status, station package shape, firmware rejection reason, and support
diagnostic wording are promises once other people rely on them. The review should preserve which meanings are product
promises and which remain diagnostics or implementation detail. Otherwise private terms become accidental API behavior.

Evidence Before Confidence (`LAW-005`) keeps review memory honest.

A review may include prototype evidence, test evidence, station rehearsal, release constraints, field observations,
support experience, and expert judgment. They do not all support the same claim. Future teams need to know which
evidence justified the accepted decision, which assumptions remained unproved, and which trigger would reopen the
choice.

Every Dependency Is a Decision (`LAW-007`) keeps the review from seeing only code.

The old service tool, backend reservation flow, manufacturing station, support procedure, release matrix, compatibility
adapter, and diagnostic export are dependencies when the system relies on their behavior. A design review that exposes
those dependencies should make them visible in the record. Otherwise Silent Coupling (`SMELL-001`) survives the meeting:
teams depend on the same meaning without a shared contract.

Hidden State (`SMELL-004`) is the failure mode that often appears after a weak review record.

Provisioning accepted, reserved, expired, unsupported, rejected, partially written, and diagnostic-only can become
states that affect behavior but are not visible through a clear owner or model. Review memory should name those states
well enough that a future engineer can tell whether the device, backend, station, service tool, or support process owns
the meaning.

Temporary Solution (`ANTIPATTERN-006`) is another memory failure.

A temporary compatibility adapter is not bad because it is temporary. It is bad when "temporary" is only a comment and a
shared nod in a meeting. The review should leave behind the owner, expiration condition, evidence needed for removal,
and record that will be updated when the adapter disappears.

Discoverability (`METRIC-003`) is the test.

Can a new engineer find the decision, owner, and contract from the affected behavior? Can support find why a diagnostic
request was rejected? Can manufacturing find why a station fallback is unsupported? Can backend find when the adapter
expires? Can release find which versions are supported? If the answer depends on asking someone who happened to attend
the review, the review has not yet become shared memory.

The practice does not need a new PEAK concept.

Design review memory is a chapter-local habit built from existing tools: review, record, evidence, ownership, Change
Radius, and Discoverability. It is how organizational work keeps architecture from collapsing back into private memory.

The later Part V chapters will take different angles. Chapter 28 will ask how to build rituals that keep teams learning.
Chapter 29 will ask how artifacts teach people. Chapter 30 will ask how teams align around decisions. Chapter 31 will
ask how architecture health reviews find systemic drift. This chapter stays with one moment: the design review that must
leave behind reasoning durable enough for the people who were not there.

## Engineering Principle

Review for memory, not performance. A good design review leaves behind the decision, context, alternatives, evidence,
owners, risks, trade-offs, and revisit triggers so future teams can understand why the system is the way it is.

Use this principle when a design review crosses ownership boundaries.

Ask:

1. What decision is under review?
2. Who owns the accepted decision?
3. Which affected owners will inherit cost or operational consequence?
4. What context and constraints matter later?
5. Which alternatives were real?
6. Which rejected option is likely to return?
7. What evidence supports the decision?
8. What uncertainty remains?
9. Which trade-off did the team accept?
10. Which risk needs a response?
11. Which follow-up needs an owner?
12. Which trigger should reopen the decision?
13. Which existing record should carry the memory?
14. How will someone find the record from the affected behavior?

The goal is not to make reviews heavier. It is to finish the review by making the reasoning reusable.

## Architecture Exercise

### Turn One Review Into Shared Memory

Choose one consequential design review from your current system. Do not choose every architecture decision in the
project. Choose one review where the reasoning may matter to someone who was not in the room.

Write one sentence that states the decision under review.

Then answer:

1. What was the context?
2. What constraints shaped the decision?
3. Who owned the accepted decision?
4. Which affected owners participated or should have participated?
5. What alternatives were considered?
6. Which option was rejected but likely to return later?
7. What evidence supported the chosen direction?
8. What evidence was missing?
9. What uncertainty did the team accept?
10. What trade-off did the team make?
11. What risk needed a response?
12. What follow-up action was created?
13. Who owns that follow-up?
14. What trigger should cause revisit?
15. Which existing record should be updated: RFC, ADR, Decision Journal, Architecture Ledger, test, support note, or
    release note?
16. How will a future engineer find the record from the code, tool, diagnostic, test, or product behavior it affects?

End with five outputs:

1. one decision statement;
2. one owner;
3. one rejected option worth remembering;
4. one follow-up action;
5. one record to update.

If the exercise produces a meeting summary, keep going. The output should be memory a future team can use.

## Principal's Notebook

- A review is not done until the reasoning can travel.
- Silence in the room is not organizational memory.
- Rejected options deserve enough memory to stay rejected.

## ADR

### Chapter ADR: Record Design Review Memory for the Provisioning Compatibility Change

#### Status

Accepted for this chapter.

#### Context

The provisioning compatibility change affects firmware behavior, backend reservation and entitlement, service-tool
behavior, manufacturing provisioning, support diagnostics, compatibility testing, and release timing.

The design review improved the decision. It clarified that the device owns final provisioning acceptance, the backend
owns reservation and entitlement, manufacturing writes a bounded package and records station evidence, and the service
tool presents stable product-level meaning while keeping raw firmware detail diagnostic.

The review also produced important memory: rejected options, evidence gaps, accepted risks, follow-up owners,
temporary-compatibility triggers, and diagnostic boundaries. The ADR recorded the final decision, but the review notes
preserved mostly attendees and topics. Future engineers could find the decision without finding enough reasoning to
trust, challenge, or revisit it.

#### Decision

Record the design review as reusable decision memory across the existing artifacts.

Update the RFC with the review outcome: accepted direction, material changes from review, open questions closed, and
questions deferred. Update the ADR with the context, accepted decision, owner, affected owners, alternatives,
consequences, evidence that mattered, rejected options worth remembering, and revisit trigger.

Use Decision Journal entries for bounded follow-ups and temporary choices: old service-tool mislabel risk,
manufacturing station-package evidence, and compatibility adapter removal. Add or update the Architecture Ledger row so
the active provisioning decision has owner, status, related RFC, related ADR, review date, active follow-up links, and
revisit trigger.

Do not create a new artifact for design review memory. Keep the review weight proportionate. Local reversible changes
may use ordinary code review, tests, or a small Decision Journal entry. Consequential cross-team reviews must close by
placing their reasoning in records a future engineer can find.

#### Consequences

The organization can recover the reasoning behind the provisioning boundary without relying on meeting memory. New
engineers can see why the chosen design won. Manufacturing can see which fallback option was rejected. Support can see
why raw diagnostic forwarding did not become a product promise. Backend can see who owns the temporary adapter and when
to remove it. Release can find supported service-tool and firmware combinations.

The cost is discipline after the meeting. Review outcomes must be closed into records. Someone must update links,
owners, and triggers. The team must avoid turning this into broad paperwork or a new gate. The practice succeeds only
when it preserves the reasoning people will need, not when it produces more polished notes.

#### Alternatives Considered

Treat the design review as approval.

This is fast and familiar, but approval does not preserve context, evidence, alternatives, rejected options, owners,
follow-up actions, or revisit triggers. It leaves future teams dependent on whoever remembers the room.

Keep meeting notes as the review record.

Meeting notes can be useful raw material, but an attendee list and topic list do not explain the accepted decision.
Notes are rejected as the sole record because they are hard to find from the affected system surface and often fail to
separate outcome from discussion.

Put everything into the ADR.

The ADR should preserve the accepted decision and the reasoning needed by future maintainers. It should not become a
full transcript, task tracker, compatibility matrix, or comment archive. Smaller follow-ups and temporary choices belong
in the Decision Journal or linked implementation records.

Leave rejected options out to avoid clutter.

This makes the record shorter, but it causes the same options to return without context. Rejected options deserve enough
memory to stay rejected until constraints or evidence change.

Create a separate artifact for review memory.

This might make the practice visible, but it adds a new container when the existing RFC, ADR, Decision Journal, and
Architecture Ledger are enough. The problem is not missing file types. The problem is failing to close review reasoning
into the records the organization already uses.

Require formal design review for every decision.

This is rejected because artifact and review weight should follow consequence. Small reversible choices do not need the
same memory as cross-team provisioning compatibility.

## Editor's Commentary

Chapter 27 follows Chapter 26 directly. Chapter 26 showed Mara helping a cross-team provisioning decision become
owned, reviewable, and recordable without taking formal authority. Chapter 27 returns three months later to ask whether
that review produced memory strong enough for people who were not in the room.

The chapter illustrates Architecture Review (`RITUAL-001`) without repeating Chapter 18's timing lesson. It uses RFC
(`ARTIFACT-002`), ADR (`ARTIFACT-001`), Decision Journal (`ARTIFACT-003`), and Architecture Ledger (`ARTIFACT-006`)
without becoming Chapter 17 again. The emphasis is organizational: a design review succeeds when its reasoning can be
found, trusted, challenged, and revisited.

The registered concepts stay material. State ownership (`LAW-001`), API promises (`LAW-002`), evidence
(`LAW-005`), dependency decisions (`LAW-007`), Change Radius (`VOCAB-001` and `METRIC-001`), Discoverability
(`METRIC-003`), Silent Coupling (`SMELL-001`), Hidden State (`SMELL-004`), and Temporary Solution
(`ANTIPATTERN-006`) all appear as reasons review memory matters.

The chapter does not introduce a new PEAK artifact or concept for design review memory. It deliberately treats design
review memory, shared memory, review outcome, rejected option, follow-up owner, and revisit trigger as chapter-local
language. The existing records are sufficient.

The boundary with the rest of Part V is also deliberate. Chapter 28 will focus on building rituals. Chapter 29 will
focus on mentoring through artifacts. Chapter 30 will focus on alignment around decisions. Chapter 31 will focus on
architecture health reviews. Chapter 27 stays with the design review as the moment where reasoning must become durable
enough to outlive attendance.
