# Technical Judgment and Evidence

## Opening Quote

> Evidence is useful only when you know which claim it supports.

## Story

The test report was comforting in the way a good number can be comforting.

An industrial controller had gained a new buffered logging path. The device stored diagnostic and process events in an
external NOR flash. The old path wrote too often, wore blocks unevenly, and sometimes made bursts of events visible as
small stalls elsewhere in the system. The new design batched records in RAM, committed them in larger writes, and kept a
compact recovery marker so the device could rebuild the log after reset.

The change was not glamorous. It was the kind of engineering work that lets future incidents be understood.

The team had evidence. A prototype board had completed a multi-day endurance run. The test had written far more records
than a typical customer site would write in the same period. The CRC checks passed. No data loss had been reproduced.
The product demonstration had gone well. The support lead liked the new logs because they made service sessions easier
to reconstruct. The firmware lead liked the reduced write amplification. The product owner liked that the improvement
did not require hardware change.

The release note draft used a sentence that sounded harmless:

"The new logging path preserves diagnostic records through unstable field power."

That sentence changed the room.

The Principal Engineer asked what the test had proven.

The first answer was quick: the logger had survived the endurance run.

That was true.

Then the answers widened. It had written a large number of records. It had recovered after resets. It had not produced
CRC failures. It had not lost records in the lab. It had supported the customer demonstration. It had reduced flash
wear. It had not disturbed normal operation during the test.

None of those answers was useless.

The Principal Engineer wrote three claims on the board:

1. The buffered logging implementation works under the tested laboratory conditions.
2. Record recovery behaves correctly when flash operations are interrupted.
3. The production product preserves useful diagnostic records through realistic field power disturbances.

The team agreed that the first claim had evidence behind it.

The second claim was less comfortable. The endurance run had included orderly software resets. It had not interrupted
erase or program operations at carefully chosen boundaries. It had not repeatedly removed power while a recovery marker
was being updated. It had not exercised a partly programmed record followed by a boot with marginal supply.

The third claim was broader still. The test had used one prototype board, one flash lot, nominal temperature, stable lab
power, and a debug build with slightly different timing from the production configuration. The test path repeated the
same sequence many times. That made it repeatable, but it did not make the evidence independent.

The team did not like where the conversation was going.

No one wanted to restart the release. No one wanted to dismiss a successful endurance test. No one wanted to add logging
to the logging system until it collapsed under its own irony. The support lead also had a practical concern: field
diagnostics were already weak, and delaying the new path meant keeping the old one longer.

Then the field notes arrived.

They were not proof. A few devices had missing records after reported power disturbances. Two support cases mentioned
rare resets near high-current activity. One log stopped shortly before the event that support needed most. Another
device booted cleanly but lacked enough recovery detail to say whether the log had been complete before reset.

The team could explain each observation away. The customer may have power-cycled the unit twice. The support tool might
have collected logs after rotation. The reset could have been unrelated to flash activity. The missing records might
have come from the old logging path, not the new one.

All of that was possible.

The Principal Engineer did not call the logger broken. She called the field notes weak signals.

In PEAK terms, a Weak Signal (`VOCAB-002`) is an early, low-confidence sign that a system decision may be aging badly.
These observations did not establish a root cause. They did reduce confidence in the broad production claim.

The team changed the release question.

It was no longer, "Did the endurance test pass?"

It became, "What evidence would justify the claim that this logging path preserves diagnostic records through realistic
power disturbance, and what commitment can we make before that evidence exists?"

The answer was not to test forever.

The team kept the successful endurance result. It still mattered. They narrowed what it proved. They planned targeted
power-fault injection around erase, program, record commit, and recovery-marker boundaries. They added production-build
testing on representative boards and more than one flash lot. They included voltage and temperature conditions that
matched the product's expected environment instead of the convenience of the lab bench.

They also changed what the device would report. Not every internal detail needed to become telemetry, but incomplete
recovery had to become observable enough for support and engineering to notice. A quiet boot after a failed recovery
would make the next field case look better than the system deserved.

The team chose a staged commitment. The new path would ship first to a bounded deployment where operational feedback
could be watched. The Decision Journal (`ARTIFACT-003`) entry recorded the claim, evidence, confidence, residual
uncertainty, and review trigger. The release language changed too. It no longer promised that a lab endurance test had
proved field durability. It stated the narrower property the team had evidence for, and the conditions under which the
broader claim would be revisited.

No one in the room had become less technical.

They had become less willing to let a successful test prove the wrong claim.

## Discussion

Data does not interpret itself.

A test result, measurement, prototype, benchmark, simulation, field report, or expert opinion becomes evidence only in
relation to a claim. The same result can be strong evidence for one claim, weak evidence for another, and almost
irrelevant for a third.

The endurance run in the story was not bad evidence. It was good evidence for a bounded claim: the buffered logging path
could run for several days, on that board, with that flash part, in that environment, along that repeated path, without
the observed failures the test was able to detect.

The problem appeared when the team let that result support a wider claim: the production device would preserve
diagnostic records through unstable field power.

That wider claim included power interruption, recovery behavior, product variation, build timing, temperature, supply
conditions, and observability of failures. Some of those concerns may eventually be covered by evidence. They were not
covered by the original test.

That is the danger behind The Successful Prototype (`FAILURE-003`): a result that is valid in one environment becomes
production architecture before the claim has been reviewed.

Technical judgment begins with the claim.

Before asking whether the evidence is sufficient, the team needs to say what the evidence is supposed to support. "The
logger passed endurance testing" is a result. "The logger preserves records through interrupted flash operations in the
field" is a claim. "We should enable this path across the fleet" is a commitment. Those sentences are related, but they
are not interchangeable.

A useful way to slow the reasoning down is:

```text
Observation -> interpretation -> inference -> confidence -> commitment
```

The observation may be that no CRC failures appeared during a test. The interpretation may be that the stored records
were internally consistent when checked. The inference may be that the recovery mechanism is likely working. The
confidence may be medium for the tested path. The commitment may be a staged rollout or a broader release.

Each arrow can introduce uncertainty.

This does not mean every decision needs formal analysis. It means the Principal Engineer should notice when the team has
skipped from observation to commitment without making the middle steps visible.

Evidence has an envelope.

That envelope includes the hardware and software version, build configuration, environment, load, timing, duration,
sample diversity, state boundaries, failure boundaries, and instrumentation available during collection. The phrase is
ordinary chapter prose, not a new PEAK concept. Its value is practical: it reminds the team that evidence is collected
somewhere, under some conditions, with some blind spots.

In embedded systems, those conditions matter because the product eventually leaves the comfortable part of the lab.
Supply voltage changes. Temperature changes. Flash lots differ. A debug build may move timing enough to hide or reveal a
race. A fixture may reset the device cleanly while the field removes power halfway through a write. A test that repeats
one path many times may provide confidence in that path without providing much confidence in adjacent states.

Repetition is useful when it exercises the claim.

Repetition is weaker when it repeats the same narrow path and then gets treated as independent confirmation. Ten
thousand clean writes through one sequence may be less valuable for the disputed claim than one carefully designed
fault-injection run that interrupts the exact commit boundary everyone is assuming will recover.

The goal is not to insult the original test. The goal is to keep it honest.

Evidence quality depends on several questions.

Is it relevant to the claim? A CRC check is relevant to record integrity. It does not prove that every expected record was
committed before power loss.

Is it representative of the conditions the commitment will face? A stable bench supply may be appropriate for early
implementation confidence. It is weak evidence for behavior during field power disturbance.

Does it cover the important states and boundaries? For flash logging, the interesting boundary may be erase, program,
commit, recovery-marker update, boot scan, or record replay. A test that avoids those boundaries may be testing normal
operation while the claim is about abnormal interruption.

Are the sources independent? A demonstration, endurance run, and automated test may all pass because they share the same
happy path. Multiple reports that come from the same instrumentation blind spot may be correlated too.

Is the evidence fresh? A result collected before a buffering change, compiler change, flash driver update, or board
revision may still inform judgment, but it should not be treated as unchanged truth.

What can the measurement not see? If the logging path fails before it records the failure, operational silence is not
strong evidence that failure did not occur. A missing observation can mean the event did not happen. It can also mean the
system was unable to observe it.

What evidence would contradict the preferred explanation? A team that only asks how to prove success tends to build
comfort. A team that asks what would lower confidence protects judgment from becoming a defense of the current plan.

None of these questions requires a statistics lecture. They require intellectual cleanliness.

Confidence should attach to a specific claim.

The team in the story could have high confidence that the implementation survived the lab endurance run. It could have
lower confidence that recovery worked through interrupted flash operations. It could have lower confidence still that
the product claim would hold across boards, lots, voltage, temperature, and field behavior.

Those confidence levels can coexist without contradiction.

This is where Evidence Before Confidence (`LAW-005`) becomes practical. Confidence should follow evidence, not replace
it. The law does not say that experience, intuition, and expert judgment are worthless. Experienced engineers often know
where systems break. Their judgment can identify which boundary deserves testing next. But experience still needs to
show its basis. Otherwise confidence becomes private memory with a serious voice.

The stronger the commitment, the stronger the evidence should be.

Chapter 2 already covered constrained commitments: choosing among imperfect options when every path spends something.
Chapter 5 uses consequence and reversibility in a narrower way. It asks how much confidence the evidence is allowed to
support before the team commits.

A change with small exposure, easy rollback, strong detectability, and low recovery cost may be reasonable with modest
evidence and a review trigger. A change with broad exposure, difficult rollback, weak detectability, high recovery cost,
or large Change Radius (`VOCAB-001`) deserves stronger evidence before confidence rises.

Change Radius as a metric (`METRIC-001`) should not become fake precision. It is useful because it asks how much system
surface must change, be reviewed, or be retested when the decision changes. If a logging durability claim affects
firmware, support tooling, release notes, customer diagnostics, and field investigation, the consequence of being wrong
is wider than the flash module alone.

Detectability matters too.

A failure that announces itself quickly allows learning after a limited commitment. A failure that hides inside missing
diagnostic records is more dangerous because the evidence needed to understand it may disappear with the failure. In
that case, "we have not seen failures" is not the same as "the system is reliable."

The next evidence action should attack the decision-critical uncertainty.

"Test more" is usually too vague. More tests can produce more comfort without producing more judgment. The better
question is which experiment, measurement, or observation can change the commitment.

For the logger, the important next action was not another long run of the same path. It was targeted power-fault
injection around erase, program, commit, and recovery boundaries. It was testing with production-equivalent timing. It
was adding enough operational feedback to make incomplete recovery visible. It was widening hardware and environmental
conditions where the production claim depended on them.

The cheapest test is not automatically the most useful. The most comprehensive test is not automatically necessary. The
right next evidence action reduces uncertainty that matters to the next commitment.

Weak signals deserve a disciplined kind of respect.

The field observations in the story did not prove that the buffered logger was wrong. Treating them as proof would be
another form of bad judgment. They were early, low-confidence observations that conflicted with the team's broad
confidence. That is enough to lower confidence in the broad claim and justify investigation.

A Weak Signal Register (`ARTIFACT-007`) can help when the team is not ready to decide. The useful entry records the
observation, where it appeared, a possible cause, current confidence, next evidence to gather, and a review date or
trigger. It should not turn vague discomfort into a confirmed defect. It should prevent weak observations from
evaporating because they are inconvenient and incomplete.

Operational feedback is evidence too, but only if the system can observe the thing the team needs to learn.

Field behavior can strengthen a judgment, narrow it, or reopen it. A staged rollout can be a responsible way to learn
when exposure is bounded and feedback is meaningful. It is not a substitute for validation. If the system cannot detect
the relevant failure, a staged rollout may only spread uncertainty slowly.

This is the uncomfortable part of evidence work: sometimes the next technical task is not the feature. It is making the
result of the feature knowable.

The Decision Journal is a small artifact for this kind of judgment. It is not ceremony. It prevents the team from
remembering confidence as stronger than it was.

```text
Date: 2026-07-05
Commitment: Stage buffered flash logging to a bounded deployment.
Claim: The logging path preserves useful diagnostic records through realistic power disturbance and recovery.
Evidence: Multi-day endurance run passed on one prototype board and one flash lot under stable lab power; CRC checks
passed; weak field observations suggest possible missing records after power disturbance; interruption behavior around
erase, program, commit, and recovery boundaries is not yet covered.
Confidence: High for tested lab operation. Low to medium for broad production durability until targeted power-fault and
representative-condition evidence is collected.
Review trigger: Revisit before broad rollout, after targeted fault injection, representative-condition testing, and
bounded operational feedback from staged deployment.
```

The record does not make the decision correct. It makes the judgment reviewable.

Good outcomes do not retroactively strengthen weak evidence. A broad rollout might succeed even if the original
confidence was poorly supported. A failure might occur even after responsible evidence work. Decision quality and outcome
quality are related, but they are not the same thing.

The narrower lesson for this chapter is that new evidence should update confidence.

When field feedback contradicts the original evidence, the team should not defend the old confidence because it was
written in a release plan. When stronger testing supports a claim, the team can raise confidence without pretending
uncertainty is gone. When evidence supports only a smaller claim, the commitment should shrink or the next evidence
action should become clearer.

Evidence is sufficient when it justifies the next commitment, not when it eliminates every unknown.

That is technical judgment under incomplete information.

## Engineering Principle

Evidence Before Confidence (`LAW-005`) is the canonical anchor for this chapter.

The confidence behind a commitment should be no stronger than the evidence that supports its specific claim.

This principle matters because engineering teams rarely have perfect proof. Waiting for certainty can be another way of
avoiding judgment. But acting as if a narrow test proves a broad claim transfers uncertainty into the product, the field,
or the next engineer's investigation.

The trade-off is not evidence versus motion. It is honest motion versus unsupported confidence.

Increase the required strength of evidence as consequences grow and reversal becomes harder. A reversible change with
clear detection can move with less evidence than a broad, difficult-to-reverse commitment whose failures hide from the
system's own instruments. A prototype success may justify the next experiment. It should not automatically justify the
production claim.

The consequence of the principle is practical: make the claim explicit, name the evidence, state the confidence, expose
the uncertainty, and define what feedback would change the judgment.

## Architecture Exercise

### Build an Evidence-Bounded Judgment

Choose one pending or recent technical commitment.

Write short answers to these prompts:

1. What commitment is being considered?
2. What exact claim must be true for that commitment to be responsible?
3. What evidence was directly observed?
4. What is being inferred from that evidence?
5. What assumptions remain?
6. Under which hardware, software, build, environment, load, timing, duration, and instrumentation conditions was the
   evidence collected?
7. How relevant is the evidence to the exact claim?
8. How representative is it of real operating conditions?
9. Which important states, boundaries, or failure modes are covered?
10. Which important states, boundaries, or failure modes are not covered?
11. Which evidence sources are independent, and which may be correlated repetitions?
12. Is the evidence fresh enough for the current system?
13. What measurement blind spots exist?
14. What observations would contradict or lower confidence in the claim?
15. What is the current confidence, and what is its scope?
16. What is the Change Radius?
17. How reversible is the commitment?
18. How detectable would failure be?
19. What would recovery cost?
20. How much exposure does the commitment create?
21. What next evidence action would most reduce decision-critical uncertainty?
22. What evidence threshold is sufficient for the next commitment?
23. What review trigger should reopen the judgment?

What evidence would justify this commitment, and what evidence would merely make the team feel more comfortable?

## Principal's Notebook

- A test result proves only the claim it exercised.
- Repetition is not independence.
- Silence is weak evidence when failure is hard to observe.

## ADR

### Chapter ADR: Stage the Flash-Logging Rollout Until Power-Loss Evidence Matches the Product Claim

### Context

The new buffered flash-logging path passed endurance testing under stable laboratory conditions. That evidence supports
the implementation under the tested environment.

The product claim is broader. The team wants the logging path to preserve useful diagnostic records through realistic
power disturbance and recovery behavior. Current evidence does not yet cover interrupted erase and program operations,
brownouts near commit boundaries, production-equivalent timing, representative hardware and flash variation, temperature
conditions, or incomplete recovery visibility.

Weak field observations exist: occasional missing records after reported power disturbance, rare resets near
high-current activity, and logs that stop before the event support needs to interpret. These observations do not prove a
root cause, but they reduce confidence in the broad durability claim.

Current instrumentation also misses some relevant failure states. A failed or incomplete recovery can look like a clean
boot if the device does not preserve enough recovery status.

### Decision

Do not treat the endurance result as sufficient evidence for immediate fleet-wide rollout.

Define the exact durability claim. Run targeted power-fault injection around critical flash-operation boundaries,
including erase, program, commit, and recovery-marker updates. Use production-equivalent configurations and
representative boards, flash lots, voltages, and temperatures for the evidence that supports the production claim.

Add the minimum useful operational evidence needed to detect incomplete recovery. Begin with a bounded staged rollout.
Record confidence, residual uncertainty, and review triggers before broad exposure.

### Consequences

The evidence becomes better aligned with the actual product claim. The team can preserve valid confidence in the lab
result while refusing to overstate it. Exposure remains bounded while additional evidence accumulates. Review can be
triggered by predefined observations instead of vague discomfort.

This creates extra validation and instrumentation work. Broad deployment is delayed. Support and operations may need to
handle temporary staged behavior. Some uncertainty remains even after better evidence is collected, because targeted
fault injection and staged rollout cannot prove every possible field condition.

### Alternatives Considered

Ship broadly based on the endurance result. This was rejected because the result supports a narrower claim than the
fleet-wide durability commitment.

Delay until exhaustive proof exists. This was rejected because exhaustive proof is not realistic, and the product still
benefits from bounded learning and improved diagnostics.

Cancel the buffering design. This was rejected because the design addresses real write-amplification and diagnostic
needs, and the current evidence does not prove the design is wrong.

Add redundancy without first identifying the disputed assumption. This was rejected because it could add complexity while
leaving the interruption and observability questions unanswered.

Restrict the feature permanently to controlled environments. This was rejected as premature. The right next step is to
gather evidence that matches the production claim, then decide whether broader use is justified.

## Editor's Commentary

Chapter 1 established the Principal Engineer as someone responsible for the future cost of the system. Chapter 2 showed
how constrained commitments make costs, consequences, uncertainty, and reversibility explicit. Chapter 3 shaped
engineering questions so investigations become answerable. Chapter 4 made ownership of closure visible across
boundaries.

Chapter 5 sits after those moves because evidence can still be misused after a question is well formed, a decision is
under discussion, and ownership is named. A team can possess real data and still draw the wrong boundary around what the
data proves.

This chapter exists to make confidence reviewable. It teaches the reader to ask whether the evidence is good enough for
the specific claim and commitment in front of the team.

Chapter 6 retains the broader stewardship question: how a Principal Engineer leaves systems healthier, easier to change,
and better supported after the immediate work is done.
