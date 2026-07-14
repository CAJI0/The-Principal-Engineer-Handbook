# Reviewing Architecture Before It Hardens

## Opening Quote

> A review is useful only while the decision can still change.

## Story

The team later called it The Review That Could Only Approve.

It had a calendar invite, a deck, and an answer.

The team was changing the configuration update path for a long-lived embedded product. Profiles were no longer simple key and value files. New variants needed schema versions, product-level validation rules, rejection reasons, and compatibility behavior across device firmware, a gateway, a service tool, manufacturing fixtures, and field support.

The direction seemed obvious after the Chapter 17 work. The team had an RFC. It named the proposal: let the device own configuration validation, let the gateway validate framing only, and let the service tool translate device rejection reasons into product messages. An ADR draft existed too, waiting for the decision to close.

Nobody thought they were skipping review.

The firmware branch compiled. It accepted the new profile envelope and rejected a small set of invalid payloads. The gateway adapter forwarded the new envelope behind a feature flag. A service-tool screen showed profile status and a draft rejection message. Manufacturing had started changing the fixture so station profiles used the same package. Tests had begun to encode the device-owned validation boundary. Release planning assumed the new path would land before the next field-service rehearsal.

The Architecture Review was scheduled after all of that because the team wanted something concrete to show. That was not laziness. It was the first sign that review timing and review subject had already drifted apart.

The first slides were tidy. The decision appeared to be: approve the versioned configuration protocol.

Then the questions arrived.

The gateway owner asked whether older gateways were allowed to reject profiles that crossed their historic length limit. The firmware owner said the device owned validation, but the old gateway code had always inspected one field before forwarding. The service-tool owner asked which rejection reasons were stable product messages and which were firmware diagnostics. Manufacturing asked whether station-only metadata belonged inside the device payload or around it. Support asked how a technician would know whether a rejected profile was incompatible with the firmware, invalid for the product variant, or blocked by a temporary recovery state. Test asked which old firmware and gateway pairs had to be covered before release. Release asked why rollback looked like a small task when the Change Radius now included service tooling and manufacturing fixtures.

Each question was reasonable. None fit the slide titled "open comments."

The decision was not only a packet layout. It was a validation authority decision. It was an API promise to the gateway and service tool. It was a state ownership question around pending, accepted, rejected, and partially applied profiles. It was a dependency decision because old gateway behavior and manufacturing fixture behavior were now part of the release path. It was a failure and recovery decision because profile application could be interrupted after acceptance but before durable storage.

The review room discovered this after implementation had started to make the answers expensive.

The firmware engineer said the branch could change, but not cheaply. The service-tool owner said the screen could change, but release translation strings were due that week. Manufacturing could still change the fixture, but the station team had already reserved validation time. The test lead could add cases, but old gateway coverage would shift the schedule. Release could absorb a small change, but not an undefined compatibility investigation.

Rejecting the protocol now felt impossible.

The first proposed response was to approve the direction and track the concerns as follow-up tickets.

That sounded responsible. The concerns would not disappear. Owners could be assigned. The release plan could keep moving. But the tickets would start after the decision crossed the next hardening point. The device-owned validation boundary would be encoded in tests. The service-tool message shape would become a product promise. The manufacturing fixture would carry the package format. The old gateway behavior would become either supported by accident or broken by surprise.

Another response was to add more reviewers next time.

That was also tempting. The team had missed manufacturing and support early. More invitations might have surfaced the issue sooner. But the problem was not only attendance. The review subject had been vague. "Approve the protocol" hid several decisions with different owners, evidence, and hardening points. More people in a vague review would still be reacting to the wrong object.

Someone suggested extending the meeting.

The Principal Engineer shook her head. More time in the same meeting would only let the team negotiate around a decision that had already started to harden.

She wrote one question on the board:

> What is still changeable, what has already hardened, and what evidence must exist before the next irreversible step?

The room stopped defending the slides.

They separated the decision into pieces.

The packet envelope was mostly changeable. The firmware branch existed, but no compatibility promise had shipped. The device-owned validation boundary was partly hardened because tests already encoded it. The gateway framing behavior was not settled because old gateway evidence was weak. The service-tool rejection vocabulary was still changeable if the team acted before translation freeze. Manufacturing profile packaging was still changeable, but the fixture work needed an answer within two days. Release compatibility was not reviewable yet because the old firmware and old gateway matrix had not been named.

Then they named the actual review subject:

Whether the configuration update protocol may harden around device-owned validation before old gateway forwarding, service-tool rejection semantics, manufacturing package boundaries, and recovery behavior have enough evidence.

That sentence was heavier than the slide title. It was also reviewable.

The decision owner was the product architecture owner. The proposal owner remained the firmware lead. Required reviewers were not chosen by seniority. They were chosen by affected surface: firmware, gateway, service tool, manufacturing, test, support, release, and the future maintainer of the configuration package. The facilitator would keep the review closing, not own the decision by accident.

The Change Radius (`VOCAB-001` and `METRIC-001`) changed the participant list. The decision touched code, tests, fixture scripts, release notes, support diagnostics, compatibility rehearsal, and the Architecture Ledger. That made the review bigger than firmware, but still smaller than the whole project.

The evidence split into three groups, which kept missing data from becoming a single undifferentiated blocker.

One group was strong enough: the device could parse and reject the new envelope in the happy path. Another group was missing but obtainable: old gateway forwarding behavior, old firmware rejection behavior, service-tool translation, and fixture package handling. The third group was not a blocker if owned explicitly: station-only metadata could remain outside the payload for this release, with a Decision Journal entry and review trigger.

The review outcome was not "approved," and it was not "blocked."

It was:

- proceed with the envelope shape for firmware work that does not create compatibility promises;
- change the service-tool boundary so product-level rejection reasons are stable and raw firmware diagnostics stay diagnostic;
- request old gateway and old firmware compatibility evidence before merging the protocol boundary tests;
- keep station-only metadata outside the device payload until manufacturing evidence exists;
- record recovery behavior for accepted, rejected, partially applied, and interrupted profiles before release rehearsal;
- update the RFC with the review outcome;
- write the ADR only after the compatibility evidence closes;
- add one Architecture Ledger row with owner, status, related RFC, pending evidence, and review date.

The team did not leave with less work.

It left with a decision that could still be improved before it became expensive to move.

## Discussion

Architecture Review is not approval after implementation. It is a structured challenge to a consequential decision while evidence, alternatives, boundaries, risks, and consequences can still change the outcome.

That timing matters more than the meeting format.

A decision hardens when the system begins to depend on it. Code depends on it. Tests encode it. Data formats and protocols implement it. Tools assume it. Release plans use it. Teams staff around it. Customer commitments reflect it. Compatibility promises appear in support material. Rollback becomes costly. Alternatives still exist in language, but not in economics.

The review in the story happened late enough to reveal the trap. The team had done responsible Chapter 17 work. It had an RFC. It had an ADR draft. It had reviewers. The problem was that implementation had started turning one proposal into several system facts before Architecture Review (`RITUAL-001`) challenged the decision.

That is how review becomes approval theater.

People ask useful questions, but the questions arrive after the decision can no longer move without embarrassment, delay, or rework. Comments become wording suggestions. Missing evidence becomes a follow-up ticket. Risks are acknowledged but not owned. Approval signatures replace technical challenge. Dissent disappears into a thread. The room performs review while the architecture has already chosen.

The cure is not a larger board.

The first useful question is the review subject.

"Review the design" is too vague. "Approve the protocol" is usually too broad. "Look at these slides" is not a decision. A review subject should name the decision under review, the decision owner, the proposal owner if different, affected owners, current decision state, scope, non-goals, alternatives, evidence, assumptions, risks, Change Radius, expected consequences, unresolved questions, deadline, reversibility, and records to update.

That sounds like a lot until the alternative appears in production. If the team cannot state the decision in that form, it probably does not yet know what it is reviewing.

Too early is also real.

A review before the decision exists asks reviewers to argue with fog. Alternatives are vague. Evidence is absent. Scope keeps changing. Reviewers debate preferences because there is no concrete commitment to challenge. The output becomes generic advice.

Useful review sits between those failures. Enough is known that the decision can be challenged. Not so much has hardened that challenge becomes theater.

The participants should follow affected architecture, not hierarchy. A senior engineer who owns none of the affected surface may help with judgment, but seniority does not make them the owner of every consequence. A manufacturing engineer may be the critical reviewer if the decision changes station flow. A support lead may be essential if rejection behavior becomes a diagnostic promise. A test lead may reveal that the decision cannot be proved at the boundary where it claims to work.

Review authority is not the same as meeting attendance.

A decision owner is accountable for the outcome. A proposal owner carries the proposal through review. Reviewers bring ownership of affected surface or relevant experience. A facilitator helps the review close without becoming the decision owner by accident. Some organizations require formal approval, but approval should not erase ownership. Follow-up owners carry evidence requests, accepted risks, and record updates after the review.

Consensus can help. It is not proof.

Architecture Review should make disagreement useful. Disagreement is valuable when it exposes missing evidence, hidden owners, incompatible constraints, or consequences the proposal has not priced. It becomes waste when the team turns it into voting, status theater, or politeness. The question is not who likes the proposal. The question is what evidence, boundary, owner, or risk would change the decision.

Evidence Before Confidence (`LAW-005`) is the review posture. The review should separate evidence from assumption, preference, personal experience, product constraint, operational constraint, unresolved uncertainty, and accepted risk. A prototype result is evidence for the path it exercised. A release date is a constraint. A support concern may be operational evidence or it may be an assumption waiting for data. A senior engineer's memory may be useful, but it is not the same as a compatibility test.

The earlier laws become review lenses.

Every State Has One Owner (`LAW-001`) asks whether the decision creates competing authority for state or transitions. In the story, validation authority needed to belong somewhere. Was it the device, the gateway, the service tool, the manufacturing fixture, or some combination with clear boundaries?

Every API Is a Promise (`LAW-002`) asks what behavior consumers may rely on. A protocol decision is not only bytes on a wire. It promises error meanings, rejection behavior, compatibility, timing, and migration expectations.

Every Dependency Is a Decision (`LAW-007`) asks which external or internal behavior the system now relies on. Old gateway behavior, fixture scripts, package generators, release processes, and support diagnostics can become dependencies even when the team thinks it is only changing firmware.

Change Radius is both vocabulary and metric. The phrase (`VOCAB-001`) names affected surface. The metric (`METRIC-001`) helps estimate how much system surface must change, be reviewed, or be retested. It does not need false precision. It needs enough honesty to pick reviewers and evidence.

Failure and recovery from Chapter 16 are review lenses too. If the configuration profile is accepted and then power is lost, what state is authoritative after restart? Can the profile be partially applied? Which component can retry? What evidence proves recovery reached a known state?

The review input can be lightweight.

An RFC (`ARTIFACT-002`) is often the right input because it shows the proposal while alternatives are still open. An ADR (`ARTIFACT-001`) draft may help when the team can see the shape of the likely decision. A Decision Journal (`ARTIFACT-003`) entry may capture a smaller judgment, a bounded evidence request, or a reversible choice. A diagram, evidence summary, Change Radius map, owner list, and compatibility matrix may all help.

That does not create a new artifact. The chapter does not need a Review Packet or Challenge Map. The point is not a template. The point is to expose enough decision surface for challenge.

Good review outcomes are broader than approve or reject.

A review can proceed as proposed. It can proceed with explicit changes. It can narrow scope. It can split one decision into several. It can request evidence. It can ask for an experiment. It can change ownership. It can revise a boundary or contract. It can defer. It can reject. It can escalate unresolved risk. It can record accepted risk. It can update an RFC, ADR, Decision Journal, or Architecture Ledger (`ARTIFACT-006`).

A review that changes the decision before the next hardening point has succeeded. A review that finds missing evidence early has succeeded. A review that narrows the decision so the team can move safely has succeeded. A review that names which work can continue and which work must wait has also succeeded. "Approved" is only one possible outcome.

Comments are not closure.

A comment thread can improve a proposal. It can reveal risks, missing evidence, and better alternatives. It cannot be the final architecture record by itself. Comments should close into accepted changes, rejected concerns with reason, evidence requests, split decisions, deferrals, accepted risks, escalation, or record updates.

A concern without an owner becomes decoration. A risk without accepted ownership becomes background noise. A comment thread without a final decision record becomes a shadow architecture. Closure is the moment when review stops being conversation and becomes an owned change, evidence request, accepted risk, deferral, escalation, or record update.

This is where Chapter 18 differs from Chapter 17.

Chapter 17 taught how ADRs and RFCs work: proposal versus decision, artifact choice, status, closure, supersession, and Discoverability (`METRIC-003`). Chapter 18 uses those artifacts but does not reteach them. Architecture Review is the challenge practice. ADRs and RFCs carry the record before and after the challenge.

RFC Friday (`RITUAL-006`) can feed the review. It can clarify open questions, improve the proposal, and decide next evidence steps. It does not replace Architecture Review when the decision has broad Change Radius, expensive reversal, unresolved owner boundaries, or compatibility risk that must be challenged as architecture.

Architecture Review also differs from Architecture Freeze.

A review may say the decision is not ready for a freeze, needs more evidence, or must not cross the next hardening point. It does not define the freeze policy. It does not teach exceptions or post-freeze revalidation. Chapter 19 owns that.

Not every design choice needs this ritual.

A local, reversible implementation choice with low Change Radius may need code review or a Decision Journal entry. A small refactor inside one owned boundary may not need Architecture Review. A consequential decision with persistent data, protocol promises, state ownership changes, dependency commitments, failure behavior, manufacturing impact, safety consequences, product-line implications, or long support horizon usually deserves stronger challenge.

The practice is proportional.

The review is useful because it protects the moment when architecture can still learn.

## Engineering Principle

Review architecture while the decision can still change. Name the decision, owner, evidence, alternatives, risks, and hardening point; then close the review into a decision, evidence request, accepted risk, or revised proposal.

Use a focused set of questions:

- What decision is hardening?
- Who owns it?
- Who is materially affected?
- What would make the team choose differently?
- Which boundary, state, API, dependency, failure path, or Change Radius changes?
- Which evidence supports it?
- Which evidence is missing?
- Which alternatives remain real?
- What risk is accepted?
- What must change before the next irreversible step?
- What artifact preserves the outcome?

The purpose is not to slow every decision. It is to challenge the decisions whose cost will outlive the implementation sprint.

## Architecture Exercise

### Review One Decision Before It Hardens

Choose one pending architecture decision. Do not choose the whole project. Choose one decision whose direction is starting to shape code, tests, tools, data, release plans, or team commitments.

Write one sentence that states the decision under review.

Then document:

1. current decision state;
2. next hardening point;
3. decision owner;
4. proposal owner, if different;
5. affected owners;
6. RFC, ADR, or Decision Journal link;
7. affected boundaries;
8. affected state;
9. affected APIs or protocols;
10. dependency commitments;
11. approximate Change Radius;
12. evidence available;
13. evidence missing;
14. assumptions;
15. alternatives still real;
16. non-goals;
17. failure and recovery implications;
18. compatibility or migration implications;
19. review participants;
20. questions that could change the decision;
21. possible outcomes;
22. closure artifact;
23. follow-up owner.

End with four outputs:

1. one reviewable decision statement;
2. one named decision owner;
3. one hardening point;
4. one review outcome or evidence request.

If the only possible outcome is "approve," the review is probably late or the subject is too vague.

## Principal's Notebook

- Review is useful only while the decision can still change.
- A concern without an owner is decoration.
- Approval is weaker than a recorded outcome.

## ADR

### Chapter ADR: Hold Architecture Review Before Configuration Protocol Hardening

#### Status

Accepted.

#### Context

The configuration update protocol affects firmware, gateway behavior, service tooling, manufacturing tests, support diagnostics, compatibility, and release. An RFC exists, and an ADR draft is waiting for the accepted decision.

Implementation has begun. The firmware branch accepts the new envelope. The gateway adapter forwards it behind a feature flag. Service-tool UI and manufacturing fixture changes are starting to assume the preferred boundary. Tests are beginning to encode device-owned validation.

Affected owners still have unresolved concerns. The gateway owner has not proved old forwarding behavior. The service-tool owner has not closed product-level rejection semantics. Manufacturing has not proved station package handling. Test has not named the old firmware and gateway matrix. Support does not yet have diagnostic wording for rejected or partially applied profiles.

Rejection will soon become expensive.

#### Decision

Hold Architecture Review before the next irreversible implementation step.

Review the actual protocol and ownership decision, not the whole project. Name the decision owner and affected owners. Use the RFC as review input. Review evidence, assumptions, alternatives, Change Radius, compatibility, failure and recovery behavior, and owner boundaries.

Classify findings as accepted changes, evidence requests, accepted risks, split decisions, or blockers. Update the RFC with the review outcome. Write the final ADR only after the evidence required for acceptance has closed. Proceed only for parts whose assumptions survived review. Record follow-up owners and review triggers in the Architecture Ledger.

#### Consequences

Real alternatives remain available longer. Ownership and boundary problems can be corrected before tests, tools, and release plans make them expensive. Evidence gaps become visible before compatibility promises are made. Affected owners have a defined path to influence the decision. The final RFC and ADR preserve the outcome instead of leaving it in comments.

The cost is preparation and possible delay. The team must pause some implementation work, gather compatibility evidence, and make uncomfortable sunk cost visible. Someone must own follow-up evidence and record updates. Some parts of the proposal may proceed while others wait, which requires discipline to avoid creating two competing decisions.

#### Alternatives Considered

Continue implementation and review later.

This preserves short-term momentum, but it lets code, tests, tools, and release plans harden the decision before review can change it.

Use code review only.

Code review can catch implementation defects. It is too narrow for validation authority, compatibility, manufacturing flow, support diagnostics, and release consequences.

Require Architecture Review for every related decision.

This would overload the ritual and make small reversible choices heavier than they deserve. Smaller judgments can use Decision Journal entries or RFC comments with clear closure.

Ask for more sign-offs without changing the decision.

Sign-offs may satisfy a process, but they do not create evidence, clarify ownership, or make alternatives real.

Move the decision to a standing board.

A board may help in some organizations, but it can also detach accountability from the decision owner. The affected owners still need to shape the outcome.

Let RFC Friday handle the architecture risk.

RFC Friday can improve the proposal and surface open questions. It does not replace Architecture Review when unresolved cross-boundary risk is about to harden.

Freeze the decision immediately and handle issues as exceptions.

The decision is not ready for freeze. Using exceptions before the review has closed would make Chapter 19's practice absorb work that belongs here.

## Editor's Commentary

Chapter 18 follows Chapter 17 deliberately.

Chapter 17 made consequential proposals and decisions reviewable through RFCs and ADRs, and discoverable through durable records. Chapter 18 asks what happens when those records expose a decision that must face challenge before implementation turns it into fact.

This chapter is not an artifact guide. It does not teach how to write an RFC or ADR. It teaches when a consequential architecture decision needs review, who should be in that review, what evidence and alternatives must be visible, and how the review closes into a real outcome.

The chapter has no primary PEAK concept. It is carried by Architecture Review (`RITUAL-001`) and supported by the artifacts and laws that make a review useful: ADR (`ARTIFACT-001`), RFC (`ARTIFACT-002`), Decision Journal (`ARTIFACT-003`), Architecture Ledger (`ARTIFACT-006`), RFC Friday (`RITUAL-006`), state ownership (`LAW-001`), API promises (`LAW-002`), evidence (`LAW-005`), dependency decisions (`LAW-007`), Change Radius (`VOCAB-001` and `METRIC-001`), and Discoverability (`METRIC-003`).

The boundary with Chapter 19 matters. Reviewing architecture before hardening is not the same as freezing architecture. A review may decide that a decision is not ready to cross the next hardening point, or that evidence must close before an ADR can be accepted. Chapter 19 will ask how to stabilize architecture without freezing learning once a decision is ready for that kind of commitment.

Chapter 17 made decisions reviewable and discoverable. Chapter 18 makes the consequential decision face challenge before it hardens. Chapter 19 will ask what happens when architecture is stable enough to freeze without pretending learning has stopped.
