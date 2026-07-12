# Evidence Before Confidence

## Opening Quote

> Confidence is useful only while its evidence still belongs to the system you are changing.

## Story

The timing margin was comfortable when the product was still a prototype.

The controller sent a command to a peripheral module, waited for an acknowledgement, and then allowed the next product
state transition. The command was not complicated. The product used it to arm an output stage after a configuration
change. If the acknowledgement arrived within the deadline, the controller continued. If it did not, the controller
stayed in the previous state and reported a timeout.

The first team measured the path carefully enough for the decision they were making.

They used one prototype board, one peripheral module revision, one component lot, room temperature, a stable bench
supply, one firmware build, one traffic pattern, debug instrumentation, and a limited run of repeated command cycles.
The command response arrived well inside the deadline. The worst observed result still left margin. The team recorded
the decision in an ADR (`ARTIFACT-001`): the existing bus schedule and command deadline were acceptable for the product
prototype and early controlled deployment.

That was not a foolish decision.

The evidence supported a narrow claim: on that prototype, with that build, board, module, load, and measurement path,
the acknowledgement arrived with enough margin for the command sequence the team was testing. The team did not claim to
have proven every possible board, load, temperature, supply condition, firmware variant, or future release.

Then the product kept living.

A compiler upgrade changed optimization around the communication task. A new diagnostic path logged command attempts
and retry outcomes. The RTOS workload grew when a sensor fusion task moved onto the same controller. Another interrupt
source appeared for a newer product variant. The peripheral module gained new firmware. A board revision changed a
component tolerance. Power management started entering a lower idle state between command bursts. The service tool added
a mode that produced a different traffic pattern. One product variant shipped into colder environments. Another shipped
with broader field exposure.

No single change announced, "The timing evidence is no longer yours."

The ADR stayed accepted. The deadline constant stayed the same. The team still referred to the original measurement as
"the timing-margin proof." New engineers heard that the command path had been measured. Reviewers saw no open risk in
the Architecture Review (`RITUAL-001`) notes. The system appeared to satisfy several laws: state ownership was named,
the command API had a documented promise, the dependency was wrapped, timeouts were explicit, unused flexibility had
been trimmed, and the design was simpler than the older command path.

The confidence survived.

The evidence conditions did not.

The first weak signals were easy to explain away.

A few field units reported rare command timeouts. One product variant showed rising retries, but only during a factory
stress sequence that the product team did not consider representative. A service engineer added a local workaround that
sent the command again after a short delay. One board revision showed a longer acknowledgement latency during a lab run,
but the run used debug traces and was dismissed as instrumentation noise. A cold-room test produced one intermittent
failure. Support had two reports from sites with unstable supply, but the logs did not preserve enough timing context to
say whether the acknowledgement was late, missing, or hidden by recovery.

No single observation proved the architecture was wrong.

That mattered.

It was also not enough to keep confidence unchanged.

In PEAK terms, those observations were Weak Signals (`VOCAB-002`): early, low-confidence signs that a system decision
may be aging badly. They did not establish a root cause. They did lower confidence in the broad claim the team was now
carrying: that the current product line still had enough command-response timing margin across the versions, variants,
loads, environments, and exposure that depended on it.

The first proposed responses defended the old confidence.

"Increase the timeout."

"Add one more retry."

"Repeat the original bench test."

"The product has worked for years."

"The engineer who made the decision knew the bus better than anyone."

"The field reports are not reproducible."

"Keep the ADR unchanged until someone proves the deadline is wrong."

"Redesign the communication path so we do not have to debate the margin."

Each response had a piece of engineering sense. A timeout might need adjustment. Retries might be appropriate. The
original engineer may have understood the system well. A bench test might still be useful. A redesign might eventually
be needed.

None of those responses answered the current architecture question.

The Principal Engineer wrote it on the board:

> Which current architecture claim are we relying on, what evidence still supports it, and what changed since that
> evidence was collected?

The room got quieter in the productive way.

The claim was no longer "the prototype command responded quickly." The active claim was:

The current controller and peripheral module receive the acknowledgement inside the product deadline with enough margin
for the products, firmware versions, board revisions, power states, loads, and environments that are now allowed to use
the command path.

That claim was larger than the original evidence.

The team recovered the evidence provenance: prototype board revision, peripheral firmware revision, compiler version,
optimization level, RTOS workload, bench supply, room temperature, traffic pattern, instrumentation method, run count,
and measured latency range. Some details were in the ADR. Some were in an old test report. Some were in a notebook. Some
had to be reconstructed from the build archive.

The team did not discard the old evidence.

It still supported the prototype claim. It still showed that the command path had margin under the conditions tested. It
still helped identify which part of the path had once been measured. It gave the team a baseline for comparison.

The team also stopped pretending that the old evidence transferred automatically.

The new compiler, workload, logging, interrupt source, peripheral firmware, board revision, power state, product variant,
cold environment, and broader exposure were not all equally material. The team sorted them. Some changes could be
argued harmless for the claim. Some needed a small confirmation. Some directly touched the timing path or the ability to
observe it.

The weak signals went into a Weak Signal Register (`ARTIFACT-007`). The entries did not say "timing margin defect
confirmed." They said where each observation appeared, which products and versions were involved, what confidence the
team had, and what evidence would change the judgment.

The team also updated a Decision Journal (`VOCAB-003` and `ARTIFACT-003`) entry. It recorded the active claim, the
historical evidence, the current confidence, residual uncertainty, and the review trigger. The record did not make the
decision correct. It made the confidence reviewable.

The next evidence action was not "test everything."

The Principal Engineer asked for the smallest targeted revalidation that would test the changed assumption. The team
selected production-equivalent builds, the current RTOS workload, the product variants carrying the claim, the board
revision with longer latency, the relevant peripheral firmware, voltage and temperature conditions that affected the
margin, and traffic patterns that matched the weak signals. They removed debug instrumentation where it changed timing
and added only the minimum diagnostics needed to observe missed deadlines, late acknowledgements, retries, power state,
firmware version, board revision, and recovery behavior.

Exposure stayed bounded while confidence was limited.

The newer product variant would not broaden deployment until the current evidence supported the broader timing claim.
Existing deployments kept a monitored path and a review trigger. If retry counts rose, if deadline misses appeared in a
new board revision, if the peripheral firmware changed again, if the product entered a colder environment, or if the
team could not reproduce the old measurement, the architecture decision would reopen.

No one declared the original decision irresponsible.

No one declared the current design broken.

The team did something more useful: it moved confidence back under evidence.

## Discussion

`LAW-005` states: Confidence should follow evidence, not replace it.

Chapter 5 used that law to teach how a Principal Engineer forms a defensible judgment for a current commitment. It
asked whether the evidence is sufficient for the decision being made now.

This chapter asks the next lifecycle question: does that evidence still support the architecture claim the system
continues to carry?

That distinction matters because architecture decisions do not stop affecting the product when the review meeting ends.
A decision may remain active for years. It may shape firmware, tests, support tools, diagnostics, manufacturing flows,
release notes, and future feature work. The original evidence may have been good. The original confidence may have been
responsible. The problem begins when the confidence keeps moving forward after the evidence conditions stop moving with
it.

Architecture confidence is temporary and conditional. It must remain traceable to a specific claim, evidence
provenance, product version, operating conditions, residual uncertainty, and review trigger.

Confidence is not certainty. It is not authority. It is not consensus. It is not a large test count, a successful
prototype, an accepted ADR, an old review note, or years without reported failure. Confidence is the current degree of
belief justified by available evidence for the claim being carried.

A claim is a statement the architecture relies on.

Evidence is an observation or result relevant to that claim.

Evidence provenance is the origin, version, conditions, and measurement path behind the evidence.

Evidence transfer is the reason evidence collected in one context supports a claim in another.

Revalidation is targeted evidence gathering after a material assumption or condition changes.

A weak signal is an early low-confidence observation that should affect investigation or confidence without being
treated as proof.

Counter-evidence is an observation that narrows or contradicts the claim.

A review trigger is a condition that requires the judgment to reopen.

Residual uncertainty is what remains unknown after the current evidence.

Those definitions are not a new PEAK framework. They are the vocabulary needed to keep the existing law honest in a
long-lived system.

The original timing decision in the story may have been responsible. The team had measured the path it was about to
use. The measurement covered the prototype, build, board, load, and environment in front of them. A responsible team
does not need perfect proof before it moves. It needs confidence that matches the evidence and a record of where that
confidence stops.

The later team had a different problem.

It was no longer deciding whether the prototype path could move forward. It was relying on an architecture claim across
new versions, variants, workloads, hardware revisions, power states, environments, and exposure. The old measurement did
not become useless. It became narrower than the confidence attached to it.

That is the danger behind The Successful Prototype (`FAILURE-003`). A prototype can prove something real and still fail
as evidence for the production claim later. The failure is not that the prototype worked. The failure is treating its
success as a permanent architecture property.

Evidence belongs somewhere.

It belongs to a claim, version, configuration, hardware revision, component lot, build setting, workload, operating
environment, instrumentation path, exposure level, and failure-detection capability. Not every decision needs every
field written in a table. But when a claim affects broad product behavior, difficult recovery, weak detectability, or a
large Change Radius (`VOCAB-001` and `METRIC-001`), the team should know which conditions the evidence covered.

Evidence transfer is a judgment, not a wish.

Prototype evidence may transfer to production when the timing path, hardware, build, load, measurement method, and
environment remain materially similar. A unit test may support a system claim when the unit boundary genuinely owns the
behavior being claimed. A staged rollout may support broader deployment when exposure is meaningful, feedback is
observable, versions are known, and the stop or rollback path is real. A lab measurement may support a field claim when
the material environmental and operating differences have been examined.

Evidence may also fail to transfer.

A debug build can change timing. Instrumentation can hide or create latency. Room-temperature passing does not prove
cold tolerance. One board revision does not automatically represent another. A single traffic pattern may miss the load
that matters. A long test can repeat one easy path for a long time without exercising the disputed boundary. Field
reports may be correlated through the same instrumentation blind spot. No logs may mean no failure, or it may mean the
system could not observe the failure.

The right response is not to distrust all old evidence.

Old evidence often remains valuable. It may still support the original claim. It may show the shape of the system when a
decision was made. It may identify the path that needs comparison. It may reduce the amount of revalidation needed. The
mistake is not using old evidence. The mistake is carrying old confidence without checking whether the evidence still
belongs to the current claim.

Confidence ages when material assumptions change.

Code changes. Compiler settings change. RTOS workload changes. Hardware revisions change. Component tolerances change.
Peripheral firmware changes. Product variants change. Load changes. Temperature, voltage, and power-management behavior
change. Diagnostics change. Exposure changes. The team that remembers the decision changes too.

Not every change invalidates every claim. A documentation edit may not affect a timing margin. A UI text change may not
affect a dependency boundary. A board change outside the communication path may not affect command latency. The point is
not to create a universal expiry date for evidence. The point is to ask whether a change is material to the claim and to
scale revalidation to the consequence of being wrong.

Weak signals help before proof exists.

The rare timeout, rising retry count, local workaround, longer latency on one board revision, intermittent cold-room
failure, and incomplete support report did not prove the timing margin was insufficient. Treating them as proof would
overstate the evidence. Ignoring them because they were not proof would make the opposite mistake. They were confidence
signals. They said the old claim deserved review.

A Weak Signal Register can keep those observations alive without turning them into confirmed defects. The useful entry
names the signal, where it appeared, a possible cause, current confidence, the next evidence to gather, and the review
trigger. That is enough to prevent small observations from evaporating because they are inconvenient.

Operational evidence is useful only when the system can observe what matters.

"No failures reported" is not the same as "the claim is true." It may mean the failure did not occur. It may also mean
exposure was too low, logs were lost, users did not report the symptom, the system recovered silently, classification
was wrong, or the affected version was rare. If the timeout path fails before it records version, board revision, power
state, retry count, and late acknowledgement behavior, field silence is weak evidence.

This is not an observability implementation chapter. The lesson is narrower: confidence from operations depends on
whether the relevant failure can be seen. Sometimes the next architecture work is adding just enough diagnostic context
to make the current claim reviewable.

Revalidation should target the changed assumption.

"Test more" is not an architecture plan. Repeating the old bench test may be useful if the old path is still disputed,
but it does not answer questions created by a new compiler, workload, board revision, power state, product variant, or
field environment. Running an exhaustive qualification program may be disproportionate. Redesigning immediately may
spend more than the evidence justifies.

The smallest useful evidence action attacks the assumption that changed.

If the claim depends on interrupt load, measure under the current workload. If it depends on board revision, include the
revision that changed. If it depends on cold operation, test the relevant temperature range. If debug traces move timing,
use a production-equivalent measurement path. If retries hide misses, record retry counts and late acknowledgements. If
the claim affects broad release exposure, bound the commitment while evidence catches up.

Bounded exposure is not a substitute for evidence. It is a way to keep commitment proportionate while evidence is
gathered. The bound only helps when versions are known, failure can be detected, the team can respond, and the review
trigger is owned.

Ownership matters because confidence can otherwise become folklore.

Someone should own the active claim. Someone should own the evidence record. Someone should own the current confidence
and residual uncertainty. Someone should own revalidation when a trigger fires. This is not a retelling of Chapter 4 or
Chapter 7. It is a specific ownership need: confidence must have a maintainer while the architecture claim is still
being used.

Existing artifacts are enough.

An ADR records a decision that affects future architecture, ownership, cost, or reversibility. A Decision Journal is a
lightweight record of decisions, evidence, confidence, and review triggers. A Weak Signal Register preserves immature
signals until they become strong enough to act on or dismiss. An Architecture Review can reopen a decision before
changed assumptions become expensive field behavior. The chapter does not need an Evidence Ledger, Confidence Register,
Validation Passport, or Architecture Proof Record.

Architecture Health (`VOCAB-007` and `METRIC-005`) includes this kind of upkeep. A system is less healthy when its
confidence lives in memory, old review status, or unowned assumptions. It is healthier when active claims, evidence
limits, weak signals, and review triggers can be found before a risky change ships.

Decision quality and outcome quality are related, but they are not the same thing.

A product may work for years after a weakly supported decision. That successful outcome does not repair the original
reasoning. A product may fail after a responsible, bounded decision. That bad outcome does not automatically make the
decision negligent. Good engineering preserves what the team knew, what it did not know, why confidence was sufficient
for the commitment, and what would cause the decision to reopen.

This is how Chapter 13 closes Part II.

The laws are not ceremonial compliance. They create architecture claims that need current evidence. What shows that one
component actually owns authoritative state? What shows that an API promise still holds across versions and failure
paths? What supports assumptions about dependency behavior, lifecycle, and replacement cost? What supports a timing
margin, timeout meaning, or ordering rule? What shows retained flexibility is justified or safe to remove? What shows a
simplification improved Change Radius instead of hiding important distinctions?

Those questions do not summarize the earlier chapters. They protect them from becoming slogans.

Part III will give the reader practices for making decisions visible, reviewable, and durable. Chapter 13 prepares that
move by making one thing clear: architecture confidence must remain attached to evidence, or the laws become a memory of
good intentions.

## Engineering Principle

Keep architecture confidence attached to a specific claim, evidence envelope, and review trigger. When the system or
conditions change, revalidate the assumption before carrying the confidence forward.

Use this principle as a review habit:

1. What claim are we relying on?
2. What evidence supports it now?
3. Which version, hardware, build, load, and environment did it cover?
4. What changed?
5. Why should the evidence transfer?
6. What can the measurement not see?
7. Which weak signals exist?
8. What would lower confidence?
9. Who owns revalidation?
10. What is the smallest targeted evidence action?
11. What confidence is enough for the next commitment?
12. What trigger reopens the decision?

The point is not to demand certainty before every change. The point is to keep confidence current enough for the
commitment the system is about to make.

## Architecture Exercise

### Revalidate One Architecture Claim

Choose one active architecture claim your system still relies on. Pick a claim that affects product behavior, release
confidence, support, manufacturing, recovery, timing, dependency behavior, or future change.

Write short answers to these prompts:

1. What exact claim is the architecture relying on?
2. Which products, versions, and variants rely on it?
3. Which original decision or artifact recorded it?
4. What original evidence supported it?
5. Under which hardware, software, build, load, environment, timing, and instrumentation conditions was that evidence
   collected?
6. What evidence supports the claim now?
7. What changed since the evidence was collected?
8. Which assumptions are required for the old evidence to transfer?
9. Which evidence remains valid?
10. Which evidence no longer transfers cleanly?
11. What can the current measurement or operational feedback not see?
12. Which weak signals exist?
13. Which counter-evidence narrows or contradicts the claim?
14. What is the current confidence, and what is its scope?
15. What is the consequence if the claim is wrong?
16. How reversible is the next commitment?
17. How detectable would failure be?
18. What is the smallest targeted revalidation?
19. Who owns the claim and the revalidation?
20. What condition should reopen the decision?
21. Which ADR, Decision Journal, or Weak Signal Register entry needs to be created or updated?

End with one decision:

- confidence remains justified;
- confidence narrows;
- revalidation is required;
- commitment must be bounded;
- the architecture decision must reopen;
- observability must improve before confidence can rise.

Do not create a new evidence artifact for the exercise. Use the records and review paths the system already has.

## Principal's Notebook

- Confidence ages with its conditions.
- Success does not repair weak reasoning.
- Weak signals speak before proof arrives.

## ADR

### Chapter ADR: Revalidate the Communication Timing Margin Before Broadening Product Exposure

### Context

The controller sends a command to a peripheral module and expects an acknowledgement before a product deadline. The
original timing margin was measured on one prototype board, one peripheral module revision, one component lot, room
temperature, stable supply, one firmware build, one traffic pattern, debug instrumentation, and a limited number of
runs.

That original evidence was valid for its tested conditions. The current product line still relies on the timing margin,
but the conditions have changed. The compiler, RTOS workload, diagnostic logging, interrupt load, hardware revision,
peripheral firmware, power-management behavior, product variants, and field exposure are no longer identical to the
original measurement.

Weak signals exist: rare timeout reports, rising retries in one variant, a local workaround, longer latency on one board
revision, a cold-environment intermittent failure, and support reports without enough timing logs. These observations do
not prove one root cause, but they lower confidence in the broad current claim.

Current observability cannot reliably show all deadline misses, late acknowledgements, retry causes, power-state
effects, version context, or recovery behavior.

### Decision

Do not broaden product exposure based only on the original prototype timing measurement.

Define the current timing claim and identify the products, firmware versions, hardware revisions, peripheral firmware,
build configurations, power states, and variants that rely on it. Preserve the valid historical evidence and record the
conditions under which it was collected.

Compare the original evidence conditions with current conditions. Run targeted production-equivalent measurements around
the disputed command-response boundary. Include current workload, relevant interrupt load, affected hardware revision,
peripheral firmware, voltage and temperature variation, power-management behavior, and traffic patterns only where they
are material to the claim.

Remove or account for debug instrumentation when it changes timing. Add the minimum diagnostics needed to observe
deadline misses, late acknowledgements, retries, version context, board revision, power state, and recovery behavior.

Bound exposure until evidence supports the broader claim. Record current confidence, residual uncertainty, and review
triggers in the Decision Journal. Put immature observations in the Weak Signal Register. Assign an owner for
revalidation. Reopen the Architecture Review if material timing assumptions change again.

### Consequences

The current confidence becomes traceable. Valid historical evidence is preserved instead of discarded. Changed
assumptions receive targeted testing. Weak signals become actionable without being overstated. Product exposure remains
proportionate while the evidence catches up. Future compiler, hardware, workload, peripheral firmware, environment, or
diagnostic changes gain explicit review triggers.

This creates measurement and instrumentation work. Some deployment or exposure may be temporarily constrained. The team
must maintain records that were previously left in memory. Some original evidence may be difficult to reproduce. Better
evidence may show that the margin is narrower than expected and that a design change is required. Uncertainty remains
even after targeted revalidation because the goal is justified confidence, not perfect proof.

### Alternatives Considered

Keep confidence because the product has mostly worked. This preserves schedule momentum, but it treats absence of
reported failure as stronger evidence than observability supports.

Increase the timeout. This may reduce visible timeouts, but it can hide late responses, delay recovery, and leave the
underlying timing claim unexamined.

Add retries. Retries may be useful for some failures, but they do not validate the original margin and can mask a timing
regression.

Repeat the original bench test. This may confirm the old path, but it does not answer whether evidence transfers to the
current build, workload, hardware, environment, and exposure.

Demand proof of field failure. This waits for the product to pay for uncertainty before reopening the decision.

Redesign immediately. This may eventually be necessary, but current evidence supports targeted revalidation before a
broad redesign.

Run an exhaustive qualification program. This may be disproportionate if a narrower revalidation can test the changed
assumption.

Ignore weak signals until they become reproducible. This makes weak signals useful only after they have become more
expensive.

Keep the old ADR unchanged. This preserves the historical decision but hides that current confidence is narrower than
the original record implies.

## Editor's Commentary

Chapter 13 closes Part II by making the laws answerable to evidence.

It does not duplicate Chapter 5. Chapter 5 asks whether the evidence is sufficient for the decision being made now.
Chapter 13 asks whether that evidence still supports the architecture claim the system continues to carry. The first is
about forming a current judgment. The second is about keeping confidence reviewable as the system changes.

That distinction lets this chapter return to Evidence Before Confidence (`LAW-005`) without repeating the buffered
flash-logging story, the evidence-bounded judgment exercise, or the staged flash-logging ADR. The story here is a timing
margin whose original evidence was reasonable and later became too narrow for the confidence attached to it.

The chapter also completes the Part II arc. Every State Has One Owner, Every API Is a Promise, Every Dependency Is a
Decision, Time Is a Dependency, Unused Flexibility Is Waste, and Simplicity Is a Feature all create claims about the
system. Those claims are useful only while they remain supported by evidence. A law-compliant design can still become
risky when the evidence behind its confidence ages out.

The PEAK concepts carrying the chapter are Evidence Before Confidence (`LAW-005`), The Successful Prototype
(`FAILURE-003`), Weak Signal (`VOCAB-002`), Weak Signal Register (`ARTIFACT-007`), Decision Journal (`VOCAB-003` and
`ARTIFACT-003`), ADR (`ARTIFACT-001`), Architecture Review (`RITUAL-001`), Change Radius (`VOCAB-001` and
`METRIC-001`), and Architecture Health (`VOCAB-007` and `METRIC-005`). They are enough. The chapter does not need a new
Evidence Ledger, Confidence Register, Evidence Envelope, Validation Passport, or Architecture Proof artifact.

Part III can now take over. It will give the reader practices for drawing boundaries, managing Change Radius, designing
for failure and recovery, using ADRs and RFCs, reviewing architecture, and freezing decisions without freezing learning.
This chapter does not teach those playbooks. It sets up why they matter: architecture decisions survive only when their
claims, evidence, uncertainty, owners, and review triggers remain visible.

The reader-facing move is simple: do not ask whether the old decision was proven wrong. Ask whether the current claim is
still supported by current evidence.
