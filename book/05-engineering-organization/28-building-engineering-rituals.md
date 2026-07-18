# Building Engineering Rituals

## Opening Quote

> A ritual earns its place when the behavior survives without the people who started it.

## Story

### The Ritual That Kept Running After It Stopped Helping

The weekly architecture review began for a good reason.

Two product teams had shipped compatible-looking changes that were not compatible in practice. Firmware changed the
device provisioning handshake. The backend accepted the new state names. Manufacturing kept using the old station
script because nobody had told the station owner that the handshake had a new failure mode. Support saw devices that
looked half-provisioned and opened an incident with three different owners named in three different places.

The failure was not that the teams had skipped a meeting. The failure was that high Change Radius decisions had crossed
ownership boundaries without being seen early enough.

Mara helped the engineering leads create a weekly Architecture Review. It was small at first. A decision owner brought
an RFC when a proposal crossed team boundaries or would become expensive to reverse. Adjacent owners attended only when
their systems were in the path. The review asked for context, constraints, alternatives, evidence, risks, open
questions, and the decision the owner wanted to make. If the group accepted the decision, the owner wrote an ADR or
updated one already in progress. If the decision was smaller or reversible, the owner captured it in the Decision
Journal with evidence, confidence, and a review trigger. The Architecture Ledger kept the active decisions visible:
owner, status, related artifact, and review date.

For a few months, it worked.

A service-tool change arrived before implementation and exposed a manufacturing dependency nobody had named. A mobile
application proposal looked local until the team measured the Change Radius and saw that support diagnostics and device
recovery would need changes too. ADRs improved because the review forced rejected options into the record instead of
leaving them in chat. Engineers joining a project could find why a boundary had been drawn without finding the people
who had been in the room.

Then the ritual kept running after the protected behavior faded.

Attendance grew because managers treated presence as a signal of diligence. Teams started bringing small, reversible
choices because waiting for review felt safer than explaining why review was unnecessary. A firmware team delayed a
local logging change for nine days because the next review was full. A backend team presented status on an already
implemented migration because "architecture review" had become the place where important-looking work was seen. The
same checklist was used for a local retry setting and for a cross-region data-retention change.

The outputs decayed first. Follow-up owners were named in the call but not recorded. The Decision Journal fell behind
because people thought the review notes were enough. The Architecture Ledger still listed decisions whose status had
changed twice. A deferred compatibility question had no owner, only a memory that "we discussed it last month."

The visible meeting was healthy. The technical behavior was not.

The proof came when a high-risk dependency change arrived too late. A platform team had wrapped a vendor library with a
thin adapter but had allowed its callback model, retry behavior, and error meanings to spread through firmware tests,
service tooling, and backend diagnostics. Everyone agreed the dependency had a broad Change Radius. Everyone also
agreed the weekly review had not seen it until implementation was mostly complete.

In the next staff meeting, the argument split into two familiar camps.

"Cancel the review," one director said. "It has become approval bureaucracy."

"Make attendance mandatory," another said. "The issue is that the right people are not always there."

Mara did not argue for either. She wrote one question on the whiteboard:

What technical behavior was this ritual meant to protect, and is it still protecting it?

The room went quiet in the useful way.

The answer was not "hold a weekly architecture meeting." The answer was "make expensive, cross-boundary technical
decisions visible before they are expensive to change, and leave enough decision memory for future engineers to act
without reconstructing the room."

Once the behavior was named, the fixes became more obvious.

The review would be triggered by risk, not by the desire to be seen. A proposal needed review when the decision had
broad Change Radius, introduced or changed a dependency, crossed ownership boundaries, was hard to reverse, changed
release or support behavior, or depended on evidence that was still weak. The weekly slot remained as a service window,
but no one had to fill it. If no proposal met the trigger, the owner used the time to close stale ledger entries or
cancelled the session.

Inputs became explicit. A decision owner had to arrive with a decision statement, affected owners, constraints,
alternatives, evidence, known uncertainty, and the artifact being updated: RFC, ADR, Decision Journal entry, or
Architecture Ledger row. Confidence without evidence no longer counted as readiness. The review could accept risk, but
it had to record what evidence justified that acceptance and what would cause the team to revisit it.

Outputs became owned. Every review ended with one of four outcomes: accepted decision, rejected decision, required
evidence before decision, or redirected decision because the review was the wrong weight. Every output had exactly one owner.
Attendance did not create ownership. The owner changed the ADR, Decision Journal, RFC, or Architecture Ledger before
the decision was treated as complete.

Small decisions stopped waiting for the large ritual. A reversible choice with a narrow Change Radius went into the
Decision Journal. A decision that would affect future ownership, cost, or reversibility became an ADR. A proposal that
needed cross-boundary feedback before commitment remained an RFC until the real trade-off was understood. The review
was not a badge of seriousness. It was a proportional tool.

The team also added decay signals. If the review had no output for two sessions, the owner would ask whether the ritual
was protecting anything. If attendance grew while decisions grew smaller, the trigger was too vague. If hidden
dependencies still survived review, the inputs were weak. If the Architecture Ledger went stale, the ritual was creating
hidden state instead of removing it. If engineers used the review to delay obvious work, the ritual had become process
load.

Mara insisted on one more line: retirement is allowed.

The team had an Architecture Freeze ritual before release hardening. It served a different purpose: stabilize named
decisions during a high-risk phase, define allowed exceptions, and record an exit date. The old version had sometimes
become permanent because nobody named what would make removal safe. The redesigned version treated the freeze like any
temporary solution: owner, scope, exception log, review date, and expiration condition.

Three months later, the architecture review was smaller and more useful. Some weeks it did not happen. Some decisions
never reached it because they had clean owners and narrow boundaries. The decisions that did reach it arrived earlier,
with better evidence and clearer trade-offs. New engineers could search the ledger, find the ADR or Decision Journal
entry, and understand the decision without asking who had attended the meeting.

The ritual had not been saved by protecting the meeting.

It had been saved by protecting the behavior.

## Discussion

An engineering ritual is a repeated practice that preserves a technical judgment the organization cannot afford to
rediscover accidentally.

That definition matters because engineering organizations often confuse rituals with meetings. A meeting is only one
possible container. A ritual is the repeatable protection around a behavior: the trigger that starts it, the owner who
keeps it honest, the input that makes it useful, the output that survives it, and the health signal that shows whether
it still works.

Build rituals around behaviors, not meetings.

The weekly architecture review in the story was valuable when it protected early visibility for broad Change Radius
decisions. It decayed when it became a calendar event whose success was measured by attendance, presentation polish, and
manager confidence. The organization still had a ritual, but it no longer had the behavior the ritual was created to
protect.

The Principal Engineer move is to name the behavior before arguing about the format.

For Architecture Review, the behavior might be: review decisions before they become expensive to change. For an
Architecture Freeze, it might be: stabilize named decisions during a high-risk phase and make exceptions visible. For a
release-readiness practice, it might be: expose recovery, compatibility, diagnostics, and support gaps before the
release is treated as safe. The wording can vary. The discipline is the same. If the behavior is vague, the ritual will
eventually protect the ritual itself.

A useful ritual has a trigger.

The trigger tells people when the ritual applies and when it does not. "Every Friday" is a time, not a trigger. "When a
decision crosses ownership boundaries or has broad Change Radius" is a trigger. "Before validation, field trials, or
release hardening when named decisions must remain stable" is a trigger. Clear triggers keep small decisions from
waiting for heavyweight review and keep high-risk decisions from slipping past because the next session is
inconvenient.

A useful ritual has an owner.

Ownership does not mean the owner makes every decision. It means one person or role is responsible for the ritual's
state: whether the trigger is clear, whether inputs are ready, whether outputs are recorded, whether stale items are
closed, and whether the ritual still protects the intended behavior. Without an owner, ritual state becomes hidden
state. People remember different outcomes. Follow-ups drift. The Architecture Ledger says one thing while the team
believes another.

A useful ritual has inputs.

Inputs prevent theater. An RFC brings summary, motivation, scope, non-goals, proposal, risks, and open questions before
the decision becomes hard to change. An ADR draft brings context, decision, consequences, and alternatives considered.
A Decision Journal entry brings evidence, confidence, and a review trigger for smaller choices. These are not paperwork
requirements. They are evidence-bearing surfaces. They let the group test confidence before treating it as judgment.

A useful ritual has outputs.

The output is what remains after the people leave. It may be an accepted ADR, an updated RFC, a Decision Journal entry,
an Architecture Ledger update, an explicit rejection, or a named evidence request. Without an output, the ritual
creates oral history. Oral history can work for a while, but it fails exactly when the organization needs memory most:
after teams change, urgency fades, and the original context is gone.

A useful ritual has health and decay signals.

Health is not "the meeting happened." Health is evidence that the protected behavior still occurs. Are risky decisions
arriving early? Are dependencies named before they spread? Are owners clear? Are follow-ups closed? Can someone who was
not in the room discover the decision, owner, and contract? Are small reversible decisions moving without unnecessary
delay?

Decay has signals too. Attendance grows for safety. Status replaces decisions. The same checklist is applied to every
change. Outputs are stale. Review owners cannot explain what is still open. Hidden dependencies survive the review.
People use the ritual to avoid making a proportionate decision. At that point the ritual is no longer preserving
judgment. It is consuming it.

This is why retirement belongs in ritual design.

Some rituals should end. Some should be redesigned. Some should shrink. Some should become a lightweight artifact rather
than a recurring session. A temporary practice without owner, review trigger, or removal plan becomes a temporary
solution that silently turns permanent. Keeping such a ritual because it once helped is a form of unused flexibility:
the organization carries extra review cost, coordination cost, and cognitive load without receiving the protection that
justified the cost.

Principal Engineers do not create rituals to make the organization feel orderly. They create rituals to keep important
technical behavior alive when memory, urgency, and personal influence are no longer enough.

## Engineering Principle

Build rituals around behaviors, not meetings.

A ritual should name the technical behavior it protects, the trigger that invokes it, the owner who maintains it, the
inputs that make it evidence-based, the outputs that preserve memory, and the health signals that tell the organization
whether to keep, redesign, or retire it.

## Architecture Exercise

### Repair One Engineering Ritual

Choose one recurring engineering practice in your organization. It may be an architecture review, release readiness
check, design critique, incident review, freeze, dependency review, or any other repeated practice that claims to
protect technical quality.

Do not begin by asking whether the meeting is too long or too short. Ask what behavior would become unreliable if the
ritual disappeared.

Write the original purpose in one sentence. Then write the behavior the ritual currently protects in one sentence. If
those sentences differ, the ritual has drifted.

Identify the trigger. If the trigger is only a time on the calendar, replace it with a technical condition: broad Change
Radius, cross-boundary dependency, hard-to-reverse decision, weak evidence, release risk, ownership ambiguity, or stale
decision memory.

Identify the owner. The owner is not the most senior person in the room. The owner is the person or role responsible for
keeping the ritual's state accurate: inputs ready, outputs recorded, follow-ups assigned, stale items closed, and decay
signals visible.

Identify the input. What must someone bring for the ritual to protect judgment rather than confidence? It might be an
RFC, ADR draft, Decision Journal entry, evidence summary, compatibility matrix, Architecture Ledger entry, test result,
or named open question.

Identify the output. What artifact, decision, owner, review trigger, or evidence request survives the ritual? If the
answer is "notes," make the note specific enough that someone outside the room can find the decision, owner, and next
action.

Finally, choose one health or decay signal. Make it observable. The signal should tell you whether the ritual is
protecting the behavior or merely preserving the shape of the old meeting.

End with:

1. one behavior the ritual protects;
2. one input;
3. one output;
4. one owner;
5. one health or decay signal.

## Principal's Notebook

- A ritual protects a behavior, not a calendar slot.
- A meeting without an output is memory only while people remember it.
- Retiring a ritual can be stewardship.

## ADR

### Redesign the Weekly Architecture Review Ritual Around Change Radius

**Status:** Accepted

**Context:** The weekly Architecture Review was introduced after cross-team architecture decisions created hidden
dependencies, stale decision memory, and late compatibility failures. The ritual initially helped teams review risky
decisions before implementation, improve ADRs, update RFCs, and keep the Architecture Ledger current. Over time, the
meeting grew into a broad approval forum. Attendance increased, small reversible decisions waited unnecessarily, status
replaced decision review, follow-up owners were not tracked, and high-risk dependency changes still arrived too late.

**Decision:** Redesign the ritual around the protected behavior: make expensive, cross-boundary technical decisions
visible before they are expensive to change, and preserve enough decision memory for future engineers to act without
reconstructing the original discussion.

The ritual is triggered by broad Change Radius, changed dependencies, cross-owner impact, hard-to-reverse decisions,
release or support impact, weak evidence, or unclear ownership. The decision owner must bring the relevant RFC, ADR
draft, Decision Journal entry, evidence summary, and affected-owner list. The review ends with an accepted decision,
rejected decision, required evidence, or redirection to a lighter record. Every output has one owner and updates the
appropriate artifact: ADR, RFC, Decision Journal, or Architecture Ledger.

The ritual owner tracks health and decay signals. Health means risky decisions arrive early, decision records stay
discoverable, owners are clear, follow-ups close, and small decisions move without unnecessary review. Decay means the
meeting has no output, attendance grows for safety, hidden dependencies survive review, the ledger becomes stale, or the
review is used to delay proportionate decisions.

**Consequences:** The review becomes smaller and more useful. Some weeks it will not run. Some decisions will move
through lighter records. High-risk decisions should arrive earlier because the trigger is technical rather than social.
The organization accepts the cost of maintaining explicit outputs and review health signals. It also accepts that the
ritual may be redesigned or retired if it stops protecting the behavior.

**Alternatives considered:** Cancel the review entirely. This would remove bureaucracy but also remove the only shared
mechanism currently exposing broad Change Radius decisions before implementation. Make attendance mandatory. This would
increase visibility but would not fix weak triggers, missing outputs, stale records, or unclear ownership. Keep the
meeting unchanged and improve the way the discussion is guided. This would treat the visible session as the problem
instead of the missing technical behavior.

## Editor's Commentary

This chapter is the third chapter of Part V. Chapter 26 showed how Principal Engineers influence without authority.
Chapter 27 showed how reviews become shared memory. Chapter 28 now asks how an organization keeps important technical
behaviors alive after the original urgency and people are gone.

The chapter intentionally does not define a new PEAK concept. It applies existing concepts to ritual design.
Architecture Review is the central illustrated ritual. Architecture Freeze appears as a contrasting temporary ritual
that needs scope, exception handling, owner, review date, and exit condition. RFCs, ADRs, Decision Journal entries, and
the Architecture Ledger are treated as the artifacts that make ritual outputs durable. Change Radius determines when
review weight is justified. Discoverability tests whether the ritual leaves usable memory. Ownership, evidence,
dependency discipline, silent coupling, hidden state, unused flexibility, and temporary-solution discipline provide the
technical pressure behind the story.

The boundary is deliberate. This is not a general guide to running recurring sessions. It is a chapter about preserving
technical judgment through repeated practice. Chapter 29 will move from rituals to mentoring through artifacts. Chapter
30 will address aligning teams around decisions. Chapter 31 will take up architecture health reviews as a later
organizational feedback loop.
