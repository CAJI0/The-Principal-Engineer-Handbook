# Using ADRs and RFCs Well

## Opening Quote

> A record is useful only when it preserves the reasoning someone will need after the room has forgotten it.

## Story

The ADR looked responsible.

The team was changing how an embedded controller accepted configuration updates. The product had a device firmware
image, a gateway, a service tool, manufacturing tests, release packaging, and a support workflow for field technicians.
Configuration updates had started as a simple command: send a new profile, validate it on the device, store it, and show
the result in the service tool.

The old command had become too small for the product.

New product variants needed configuration profiles with explicit schema versions, validation rules, compatibility
markers, and a way to reject settings that older firmware could not safely interpret. Manufacturing wanted to load the
same profiles at the end of test. Support wanted the service tool to display why a profile was rejected. Release wanted
to know whether old gateways could still send the previous format. The firmware team wanted to start with the protocol
they believed would work and avoid turning the project into a meeting.

One engineer did what the team had learned to do in earlier chapters.

He opened a new ADR.

The title was clear:

```text
Use Versioned Configuration Updates
```

The context said the old command could not represent new validation rules. The decision said the team would add a
versioned update protocol. The consequences said firmware, gateway, and service tooling would need changes. The ADR had
headings. It had a status. It even had alternatives.

It was not careless.

It was too late to be the first review artifact.

Implementation had already begun. Firmware had a branch with a packet layout. The gateway had a parser behind a feature
flag. The service tool had a draft screen. Manufacturing had not reviewed the profile load path. Support had not seen the
new rejection reasons. Release had not checked old gateway behavior. The test team had only one sample profile, and it
matched the firmware engineer's preferred layout.

Reviewers commented on the ADR.

One person asked whether "profile" and "configuration" meant the same thing. Another suggested renaming a field. A
third asked for more detail in the consequences section. Someone from the gateway team asked whether the gateway was
allowed to validate a profile before forwarding it. The service-tool owner asked whether users would see device
validation errors or translated product messages. Manufacturing asked whether profile loading at the station was in
scope. Support asked whether rejected profiles would appear in exported diagnostics. Release asked whether devices on
old firmware would reject the new format safely or accept it partially.

The ADR grew.

The decision did not get clearer.

The engineer added a bigger alternatives section. Then he added an implementation plan. Then he added a migration plan.
Then he added a list of review comments and responses. The file was now long enough that people stopped reading it
carefully.

Someone suggested renaming the ADR to an RFC.

That sounded plausible. The document was still being discussed. It had comments. It had unresolved questions. It asked
for feedback. Maybe the problem was the label.

The Principal Engineer did not argue about the filename.

She asked:

> Is this still a proposal, or are we documenting a decision that implementation has already made?

The room paused.

For firmware, the decision felt almost made. The packet layout existed. The code compiled. A prototype device accepted a
test profile. For manufacturing, the decision was still open because station loading had not been designed. For the
service tool, the decision was still open because rejection semantics were unclear. For release, the decision was not
reviewable because compatibility assumptions were missing. For support, the decision did not yet exist because no one
had named the diagnostic promise.

The same file was trying to be two artifacts.

It was trying to be an RFC for people who still had evidence to add.

It was trying to be an ADR for a choice the firmware branch had already started to make.

That confusion mattered more than the template.

The Principal Engineer drew four states on the whiteboard:

```text
Question -> Proposal -> Decision -> Record
```

Then she added two side paths:

```text
Smaller judgment -> Decision Journal
Active decision -> Architecture Ledger
```

"We do not need a larger document," she said. "We need to know what state the decision is in."

They split the work.

The existing ADR stopped pretending to be accepted. The team moved the live question into an RFC. The RFC had a narrow
proposal: change the configuration-update protocol so profiles carry schema version, validation result, and product-level
rejection meaning across firmware, gateway, service tool, manufacturing, and support.

The RFC named its non-goals.

It would not redesign the entire configuration system. It would not define every product variant. It would not replace
the service tool. It would not decide the release rollout. It would not teach the gateway to own configuration truth. It
would not require the manufacturing station to understand private firmware layout.

Those non-goals helped.

Reviewers stopped asking the document to solve every nearby problem. They could ask sharper questions.

The firmware team owned the proposal. The product architecture owner owned the eventual decision. Required reviewers
were named by affected surface: firmware, gateway, service tool, manufacturing, test, support, and release. The RFC
listed the evidence the team had: one prototype profile accepted by firmware, one compatibility test against the old
gateway, two field support cases where rejected configuration had been hard to explain, and a manufacturing station path
that still needed proof.

It also listed assumptions.

Old gateways would forward unknown profile versions without interpreting them. The device would own validation. The
service tool would display product-level rejection reasons, not raw firmware error codes. Manufacturing would load the
same profile format that field service used. Old firmware would reject new profiles cleanly. Those statements had looked
like background detail in the ADR. In the RFC, they became reviewable claims.

At the next RFC Friday, the team did not try to collect signatures.

They walked through open questions.

The gateway owner showed that one old gateway release did inspect a length field and would reject profiles over a
threshold. The service-tool owner showed that raw firmware error codes were already leaking into support exports. The
manufacturing engineer pointed out that station profiles were generated from a different source than field profiles. The
test lead asked whether compatibility tests needed old gateway versions, old firmware versions, or both.

The RFC changed direction.

The packet layout stayed close to the prototype, but the validation boundary moved. The device remained the authority
for configuration acceptance. The gateway would validate framing only. Product-level rejection reasons would be defined
at the firmware boundary and translated by the service tool. Manufacturing would use the same profile package format as
field service, but station-only metadata would remain outside the device payload. The team added one compatibility test
for old gateway forwarding and one for old firmware rejection.

One issue did not close in RFC Friday.

Release compatibility across a mixed fleet affected manufacturing, field support, gateway behavior, service tooling, and
customer rollout. The team scheduled an Architecture Review for that specific risk. The RFC did not become the review
ritual. It carried the proposal and the open question into the right review.

After the compatibility question closed, the decision was accepted.

Then the ADR became useful.

The new ADR did not copy the whole RFC. It linked to it. It recorded the accepted decision, the evidence that mattered,
the alternatives rejected, the consequences accepted, the owner, the status, and the trigger that would force a revisit.
It said that if old gateway forwarding failed in field rehearsal, the decision would be superseded by a compatibility
adapter decision rather than patched silently in the service tool.

Smaller choices did not become ADRs.

The test team used a Decision Journal entry for the first profile-generator assumption because it was reversible and
needed a review trigger, not a full decision record. The Architecture Ledger gained one row for the active protocol
decision: owner, status, related RFC, related ADR, and review date.

The code changed too, but the code was no longer the only place where the decision lived.

A future engineer could start at the service-tool rejection message, follow the link to the governing ADR, see the RFC
that shaped it, find the compatibility tests, and identify the owner of the active decision. That was not documentation
for its own sake. It was shared memory with enough structure to survive turnover.

The original ADR had not been wrong because it used the wrong headings.

It had been wrong because it tried to record a decision before the affected people had been able to influence it.

## Discussion

ADRs and RFCs work when they make architectural reasoning reviewable before commitment and discoverable after
commitment.

The sentence has two halves because the artifacts serve different moments.

An RFC is useful while meaningful change is still possible. It invites review before a decision becomes hard to change.
It exposes motivation, scope, non-goals, proposal, risks, and open questions. It gives affected owners a place to bring
evidence and constraints before implementation cost turns rejection into theater.

An ADR is useful when a material architectural decision has been accepted. It records what was decided, why it was
decided, which alternatives were rejected, and what consequences the team accepts. It gives future maintainers enough
context to understand the system without reconstructing the original conversation.

The distinction is not ceremonial.

If the team writes an ADR while the real choice is still open, reviewers may treat a proposal as a decision. If the team
renames an after-the-fact ADR as an RFC, review may appear open while the implementation has already made rejection
economically fake. If the team keeps an RFC open after the decision happened elsewhere, the comment thread becomes a
shadow record. If the team never writes the ADR after a useful RFC, the accepted decision disappears into the review
conversation.

The first question is decision state.

Is there only an emerging question? Is there a concrete proposal? Is evidence still being gathered? Has the decision been
accepted? Was the proposal rejected, narrowed, deferred, or split? Is this only a reversible local judgment? Has an old
decision been superseded? Has it retired because it no longer governs architecture?

These are chapter-local words, not a new lifecycle model. Their purpose is to stop the template from making the decision
look more mature than it is.

The document type follows consequence, uncertainty, reversibility, affected ownership, and future maintenance cost.

Some choices need no architecture artifact. A local implementation detail with low reversal cost may be clear enough in
code, tests, or a commit message. Some choices need a Decision Journal entry: date, decision, evidence, confidence, and
review trigger. That is useful when the choice matters but a full ADR or RFC would be too heavy.

Some proposals need an RFC because the team still needs review across ownership boundaries. Some accepted decisions need
an ADR because they affect architecture, ownership, cost, reversibility, compatibility, operations, product behavior, or
maintenance.

Artifact weight should follow the lifetime of the reasoning.

A decision that affects firmware, gateway behavior, service tooling, manufacturing, tests, release, and support will
probably outlive the sprint. A decision that changes a retry constant inside one module may not. A decision that can be
reversed in an afternoon needs less durable reasoning than a decision that will shape field compatibility for years.

This does not make small choices unimportant. It means the record should be proportionate.

Timing matters as much as weight.

Too early, and the document becomes speculative architecture fiction. The proposal is vague. Alternatives are not real.
Evidence is absent. Reviewers argue with guesses rather than a decision.

Too late, and the document becomes a defense. Implementation has hardened the path. Alternatives have disappeared. The
team remembers only the reasons that support the current code. The RFC becomes approval theater. The ADR becomes a story
written by the current branch.

Write enough before commitment to improve the decision. Record enough at commitment to preserve why it was made.

Experiments can happen before the final artifact. A spike may produce evidence. A prototype may reveal constraints. A
small branch may prove that a packet layout fits. The mistake is not experimenting. The mistake is treating the existence
of code as evidence that review is no longer needed.

Scope and non-goals make review possible.

A useful RFC or ADR contains one coherent decision. When one file tries to decide a protocol, a storage format, a UI
redesign, release sequencing, manufacturing policy, and team process, every reviewer reads a different document. Some
parts are proposals. Some are accepted assumptions. Some are implementation details. Some belong in later decisions.

Non-goals are not a way to avoid hard questions. They are a way to make the question reviewable.

In the story, the RFC did not redesign the configuration system, replace the service tool, or decide the whole release
rollout. That did not make those topics unimportant. It kept them from hiding the protocol decision. If a non-goal later
becomes material, it can become its own proposal or review item.

Evidence belongs inside the artifact, but not as decoration.

`LAW-005` says confidence follows evidence. In ADR and RFC practice, this means records should separate evidence,
assumptions, preferences, forecasts, open questions, and accepted risk. A prototype result is not the same as a
compatibility test. A benchmark is not the same as field behavior. A senior engineer's memory is not the same as a
release constraint. Each may matter, but they support different claims.

An RFC should expose evidence gaps while the decision can still change. An ADR should preserve the evidence that made
the accepted decision reasonable in its context. A review trigger should say when that evidence may no longer transfer.

This is not Chapter 13 repeated. Chapter 13 owns the full discipline of evidence provenance, transfer, aging, and
revalidation. Chapter 17 cares about how evidence appears in the record so the record does not become an opinion archive.

Alternatives deserve fair treatment.

A weak ADR lists alternatives only to make the selected option look inevitable. A useful ADR explains why an option was
attractive and why it was not selected in this context. That distinction matters later. A rejected option may become
valid when constraints change, when evidence improves, when a product variant appears, or when the support horizon
changes.

Consequences deserve the same honesty.

The chosen direction may improve review timing and make ownership explicit. It may also add review latency, maintenance
work, indexing work, and a risk that people perform the document without doing the thinking. Good records do not hide
those costs. They make the accepted cost visible.

Ownership keeps artifacts alive.

Review participation is not the same as decision authority. A firmware owner may own the proposal. A product
architecture owner may own the accepted decision. A service-tool owner may be a required reviewer. A release owner may
own a compatibility gate. A future maintenance owner may need to revisit the decision when field evidence changes.

If those roles are not named, the artifact can look complete while ownership drifts back into private memory.

Comments also need closure.

An RFC comment thread can improve a decision, but comments alone are not the decision. The artifact should close with an
outcome: accepted, rejected, narrowed, deferred, split, experiment requested, evidence requested, or escalated to
Architecture Review. The accepted ADR should link back to the proposal and preserve the reasoning that still matters.

Chapter 18 will own the full Architecture Review ritual. Chapter 17 only needs the boundary: if artifact-level review
exposes unresolved architecture risk, escalate it deliberately. Do not pretend an RFC comment thread is the same as a
review ritual. Do not send every open question to Architecture Review merely because disagreement exists.

Status is part of meaning.

A record with unclear status is dangerous because engineers do not know whether to follow it, review it, ignore it, or
replace it. Proposed, under review, accepted, rejected, deferred, superseded, retired, and withdrawn are useful words
when the team uses them consistently. They are chapter-local examples, not a mandatory global vocabulary.

The important rule is not to rewrite history silently.

If a decision changes, supersede the old ADR or change its status with a link to the successor. Preserve enough old
context to explain why the system took that path. If a decision no longer affects architecture, retire it so future
engineers do not treat it as live guidance. An old ADR can be obsolete as instruction and still valuable as history.

Discoverability is the test that tells you whether shared memory survived.

`METRIC-003` asks how easily an engineer can find the decision, owner, and contract behind system behavior. A record
hidden in the right folder but unreachable from the affected behavior is weaker than it looks. Future engineers should be
able to move from a module, test, rejection message, release note, incident, or owner to the decision that governs it.

Links help, but links are not a dumping ground.

An RFC may link to experiments. An ADR may link to the accepted implementation, compatibility tests, release notes, or a
superseded record. An Architecture Ledger may point to active decisions, owners, status, related artifacts, and review
dates. Code or configuration may link to a governing decision when the connection is not obvious. The goal is not to
duplicate rationale everywhere. The goal is to preserve one authoritative place for each kind of information and make it
findable from the surfaces it affects.

That is where the Architecture Ledger fits.

`ARTIFACT-006` is not a second ADR. It is a compact inventory of active decisions and known debts. It helps a team find
the current record, owner, status, related artifact, and review date when decisions are spread across many files and
teams. If the ledger starts repeating the full rationale, it will drift. If it lists everything, it will stop helping.

Decision Journals fit the other side of the scale.

`ARTIFACT-003` is useful when a decision is real but smaller, more reversible, or not yet worth a full ADR. It captures
decision, evidence, confidence, and review trigger. It is not a diary, meeting notebook, backlog, or substitute for an
ADR when the decision has long-lived architecture consequences.

Implementation and records must continue to talk to each other.

An accepted ADR does not freeze architecture. Chapter 19 will own freeze. An ADR records the decision the team has
accepted now. If implementation changes the meaning, if field evidence invalidates an assumption, if an alternative
becomes viable, or if the decision is no longer active, the record needs to be updated, superseded, retired, or linked to
a new decision.

The failure mode is not having too few files.

The failure mode is making future engineers reconstruct a consequential decision from code, chat, old meetings, branch
names, and someone's memory. Good ADR and RFC practice reduces that reconstruction. It keeps proposals open while they
can still change and keeps accepted reasoning legible after the original conversation has disappeared.

## Engineering Principle

Use the smallest durable artifact that makes a consequential proposal or decision reviewable now and discoverable later.

Use these questions before choosing the artifact:

- Is this a proposal, an accepted decision, or a smaller judgment?
- Is meaningful change still possible?
- Who owns the proposal?
- Who owns the decision after acceptance?
- Who is materially affected?
- What evidence exists?
- What remains uncertain?
- Which alternatives are real?
- What is explicitly out of scope?
- Which consequences are accepted?
- What closes the RFC?
- What preserves the accepted decision?
- What would trigger review, supersession, or retirement?
- How will a future engineer find the record from the affected system surface?

The answer may be no artifact, a Decision Journal entry, an RFC, an ADR, or a linked RFC and ADR. The responsible choice
is the one that matches consequence, uncertainty, ownership, and lifetime.

## Architecture Exercise

### Choose the Right Decision Artifact

Choose one current or recent architecture choice. Do not choose the whole system. Choose one decision or proposal whose
reasoning someone may need later.

Write one sentence that states the choice.

Then answer:

1. Is this still an emerging question, an open proposal, an evidence-gathering effort, an accepted decision, a rejected
   proposal, a deferred decision, a reversible local judgment, a superseded decision, or a retired decision?
2. What product behavior, boundary, state, API, protocol, dependency, test, tool, release, support path, or owner is
   affected?
3. How reversible is the choice?
4. What is the approximate Change Radius?
5. What evidence exists today?
6. What assumptions are still unproven?
7. What remains uncertain?
8. Which alternatives are real enough to review fairly?
9. What is explicitly out of scope?
10. What risks and consequences would the team accept?
11. Who owns the proposal?
12. Who owns the accepted decision?
13. Who must review because they own affected surface?
14. What would close the proposal?
15. What status should the record have?
16. Which implementation, test, release, incident, or compatibility links matter?
17. What would trigger review or supersession?
18. If the decision remains active, where should the Architecture Ledger point?
19. Where will a future engineer find the record from the behavior it governs?

Now choose the artifact weight:

- no architecture artifact;
- Decision Journal entry;
- RFC;
- ADR;
- linked RFC and ADR.

End the exercise with four outputs:

1. one artifact choice and why that weight is sufficient;
2. one named owner;
3. one evidence statement;
4. one discoverability action.

If your answer is "write an ADR because we always write ADRs," keep going. The artifact should follow the decision, not
the habit.

## Principal's Notebook

- An RFC preserves choice; an ADR preserves commitment.
- A record without evidence is an opinion with a filename.
- A decision nobody can find is not shared memory.

## ADR

### Chapter ADR: Adopt RFC-First Review for the Configuration Update Protocol

#### Status

Accepted.

#### Context

The configuration-update protocol affects firmware, gateway behavior, service tooling, manufacturing tests, support
diagnostics, release compatibility, and field operation. Implementation began before affected owners had a shared
proposal. The first ADR draft recorded a preferred protocol direction, but it hid unresolved questions about scope,
non-goals, old gateway behavior, service-tool translation, manufacturing profile loading, and support-visible rejection
reasons.

Review arrived after sunk cost had grown. Some reviewers were commenting on wording while others were still trying to
influence the architecture. Future maintainers need one place to find the accepted decision, the RFC that shaped it, the
evidence available at acceptance, and the alternatives rejected in this context.

#### Decision

Convert the live protocol proposal into an RFC before accepting the architecture decision.

The RFC will record motivation, scope, non-goals, proposal, risks, evidence, assumptions, alternatives, affected owners,
and open questions. It will name a proposal owner and a decision owner. Firmware, gateway, service-tool, manufacturing,
test, support, and release owners will review because they own affected surface.

Use RFC Friday for lightweight proposal review while meaningful alternatives remain open. Escalate unresolved
cross-boundary compatibility risk to Architecture Review when ordinary artifact review cannot close it.

Close the RFC with a clear outcome: accepted, rejected, narrowed, deferred, split, or sent for more evidence. After
acceptance, write an ADR that records context, decision, consequences, alternatives, owner, status, and revisit trigger.
Link the ADR to the RFC, implementation, compatibility tests, release notes, support diagnostics, and Architecture
Ledger entry.

Use Decision Journal entries for smaller reversible choices that need evidence and review triggers but do not deserve a
full RFC or ADR. Preserve superseded ADRs and link successors. Do not require an RFC or ADR for every implementation
choice.

#### Consequences

Review happens while the protocol can still change. Non-goals become explicit. Evidence and uncertainty remain visible.
Affected owners can contribute constraints before implementation hardens. The accepted rationale stays discoverable
after the proposal discussion closes. Proposal state and decision state remain distinct. Smaller decisions keep a
lightweight path.

The cost is real. The team must write and review the RFC, maintain artifact status, keep links current, and clean up
abandoned proposals. Consequential proposals may take longer to close. The practice can become theater if teams treat
the RFC as approval paperwork or the ADR as a victory note. The Architecture Ledger needs an owner so active decisions
remain findable without duplicating the records themselves.

#### Alternatives Considered

Keep the ADR and request approval.

This is attractive because the file already exists and the preferred direction is visible. It is rejected because several
affected owners still have architectural input, and approval of the ADR would make the decision look more closed than it
is.

Finish implementation and document later.

This preserves short-term speed, but it treats sunk cost as evidence. It is rejected because compatibility and support
questions are still material.

Use only a ticket.

A ticket can track work, but it is not enough to preserve architectural reasoning, alternatives, consequences, owner,
status, and review trigger for future maintainers.

Use meeting notes.

Meeting notes can capture discussion, but they rarely preserve the accepted decision and its consequences in a durable
form. They also become hard to find from the affected system surface.

Require full Architecture Review before any written proposal.

Architecture Review may be needed for unresolved cross-boundary risk, but requiring it before every written proposal
would delay useful RFC review and consume Chapter 18's ritual for work the artifact can handle.

Skip the ADR because the RFC exists.

The RFC preserves proposal review. It does not automatically preserve the accepted decision in a concise maintenance
record.

Create one large document mixing proposal and accepted decision.

This keeps information in one place, but it blurs state. Reviewers cannot tell which parts are open, accepted, rejected,
or historical.

Require RFCs for all changes.

This is rejected because artifact weight should follow consequence. Small reversible decisions need a lighter path.

Require ADRs for all merged changes.

This is rejected because merged code is not the same as architecture. Many implementation choices do not need durable
decision records.

## Editor's Commentary

Chapter 17 is the fourth practice chapter in Part III. Chapter 14 made boundaries concrete. Chapter 15 made affected
surface visible. Chapter 16 made failure outcomes explicit. This chapter makes the reasoning around those decisions
reviewable before commitment and legible after the original conversation disappears.

The chapter has no primary PEAK concept. It is carried by the paired artifacts ADR (`ARTIFACT-001`) and RFC
(`ARTIFACT-002`). Decision Journal (`ARTIFACT-003`) and Architecture Ledger (`ARTIFACT-006`) provide the lighter and
indexing paths. Evidence Before Confidence (`LAW-005`) governs how claims enter records. Architecture Review
(`RITUAL-001`) remains an escalation path, not the subject of the chapter. RFC Friday (`RITUAL-006`) supplies a
lightweight review space. Discoverability (`METRIC-003`) tests whether the record can actually be found from the system
surface it governs.

The chapter does not teach documentation style, repository layout, or process compliance. It teaches an architecture
habit: choose the artifact that matches decision state, consequence, uncertainty, ownership, and lifetime.

The boundary with the next chapters is intentional. Chapter 18 will teach how to review architecture before it hardens.
Chapter 19 will teach how to freeze architecture without freezing learning. Chapter 17 stays with the artifacts on both
sides of those practices: it keeps proposals reviewable while they can still change, and it keeps accepted decisions
discoverable after they matter.
