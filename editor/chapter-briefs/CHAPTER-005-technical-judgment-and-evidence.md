# CHAPTER-005 Canonical Brief: Technical Judgment and Evidence

## Metadata

- Stable ID: `CHAPTER-005`.
- Title: Technical Judgment and Evidence.
- Expected manuscript path: `book/01-thinking-like-a-principal/05-technical-judgment-and-evidence.md`.
- Lifecycle status: draft preparation.
- Canonical predecessor: `CHAPTER-004` - Ownership Beyond Code.
- Expected successor: Leaving Systems Better Than You Found Them.
- Baseline commit: `54d6b4e13b6ae8f38619b9b7be40c91b6bbb03c8`.
- Reader-facing draft created: no at brief-registration time.

## Canonical Purpose

Prepare Chapter 5 to teach how a Principal Engineer forms defensible technical judgment when information is incomplete.

The chapter must explain how to:

- identify the precise claim or commitment that requires support;
- distinguish observations and measurements from proxies, inferences, assumptions, and opinions;
- evaluate whether available evidence is relevant, representative, sufficiently independent, recent, and observable;
- calibrate confidence without pretending uncertainty has disappeared;
- decide what additional evidence would materially improve the judgment;
- recognize when evidence is sufficient for the next commitment rather than waiting for impossible certainty;
- update judgment when weak signals or operational feedback contradict the original evidence.

This is the Part I operational treatment of `LAW-005` - Evidence Before Confidence.

## Central Thesis

Technical judgment is the disciplined calibration of confidence to the quality of evidence, the uncertainty that remains,
and the consequences of being wrong.

Approved supporting formulation:

> Evidence is sufficient when it justifies the next commitment, not when it eliminates every unknown.

Do not register either sentence as a new PEAK law, maxim, principle, metric, artifact, ritual, smell, or vocabulary
concept.

## Reader Transformation

The reader should move from merely possessing data or test results to constructing an evidence-bounded judgment.

By the end of the chapter, the reader should be able to ask:

1. What exact claim are we making?
2. What evidence directly supports that claim?
3. Under which conditions was that evidence collected?
4. Which parts are observed, inferred, assumed, or still unknown?
5. What alternative explanations remain plausible?
6. How strong should the evidence be for this commitment's consequences and reversibility?
7. What evidence would lower or reverse our confidence?
8. What is the cheapest next experiment that reduces decision-critical uncertainty?
9. What operational feedback will cause us to revisit the judgment?

## Exact Scope

Chapter 5 covers:

- claim-evidence alignment;
- direct observation, measurement, experiments, field observations, proxies, simulation, inference, expert judgment,
  explicit assumptions, and absence of observed failure;
- evidence relevance;
- representativeness of real operating conditions;
- coverage of important states and boundaries;
- measurement resolution and limitations;
- repeatability;
- independence versus correlation between evidence sources;
- evidence freshness;
- missing, censored, or unobservable outcomes;
- alternative explanations and disconfirming evidence;
- confidence attached to a specific claim;
- residual uncertainty;
- stronger evidence thresholds for severe, broad, difficult-to-reverse, difficult-to-detect, or difficult-to-recover
  commitments;
- Change Radius as an approximate consequence indicator, without false precision;
- targeted experiments that reduce a named uncertainty;
- weak signals as low-confidence observations that justify investigation without proving a cause;
- operational feedback as new evidence that can strengthen, narrow, or reopen a judgment;
- sufficiency of evidence for the next commitment.

## Explicit Out Of Scope

Do not turn Chapter 5 into:

- a second generic decision framework;
- a statistics textbook;
- a complete test-strategy handbook;
- a formal-verification tutorial;
- an observability architecture chapter;
- a logging or telemetry implementation guide;
- a root-cause-analysis procedure;
- an incident-management chapter;
- a complete Architecture Review process;
- an ADR or RFC mechanics tutorial;
- a release-gating or production-readiness chapter;
- a broad stewardship chapter;
- Chapter 6.

## Boundaries With Adjacent Chapters

### Chapter 1

Chapter 1 defines the Principal Engineer role and responsibility for future system cost. Chapter 5 develops one core
capability of that role: forming defensible technical conclusions when experience, tests, field behavior, uncertainty,
and consequences do not align cleanly.

Do not repeat the general role definition.

### Chapter 2

Chapter 2 asks:

> Given these constraints and consequences, what should we commit to?

Chapter 5 asks:

> Is the evidence strong enough to justify the confidence behind that commitment?

Chapter 5 may use consequence and reversibility to scale the required strength of evidence. It must not repeat option
comparison, accepted-cost analysis, or the constrained commitment framework.

### Chapter 3

Chapter 3 asks:

> What question would reveal what is actually happening?

Chapter 5 asks:

> Once answers and measurements arrive, how much should they change our confidence?

Chapter 5 receives the investigation frame from Chapter 3. It must not reteach question formation,
observation-versus-interpretation, the stale-state story, or root-cause inquiry.

### Chapter 4

Chapter 4 asks:

> Who owns the outcome and ensures that it reaches closure?

Chapter 5 asks:

> What evidence makes the claimed outcome, risk, or closure believable?

Chapter 5 must not redefine ownership, assignment, handoff acceptance, or closure.

### Chapter 6

Chapter 5 is about the quality of judgment under incomplete information.

Chapter 6 retains broader stewardship:

- reducing future friction;
- improving system health;
- leaving stronger architecture, boundaries, ownership, and feedback mechanisms;
- leaving the system better than it was before the immediate task.

Do not start Chapter 6.

### Later Parts

Leave definitive treatment of these topics to later chapters:

- detailed Architecture Review mechanics;
- ADR and RFC mechanics;
- architecture metrics;
- release discipline;
- production qualification;
- test strategy;
- observability design;
- operational feedback systems;
- incident and recovery practices.

## Future Embedded-Systems Story Brief

Working story concept: The Test That Proved the Wrong Claim.

System:

- an industrial embedded controller stores diagnostic and process events in external NOR flash;
- a buffered logging design reduces write amplification and is expected to preserve records through unstable field
  power.

Initial evidence:

- a large number of successful writes;
- a multi-day endurance run;
- zero observed CRC failures;
- no reproduced data loss;
- a successful product or customer demonstration.

Evidence limitations:

- one prototype board;
- one flash lot;
- stable laboratory power;
- nominal temperature;
- debug or otherwise non-production-equivalent timing;
- orderly resets instead of interrupted erase/program operations;
- repeated execution of strongly correlated test paths;
- inadequate observation of failed boots or incomplete recovery.

The evidence validly supports a narrow claim that the implementation works under tested conditions. It does not yet
support the broader production durability claim.

Weak field observations later include:

- occasional missing records after power disturbances;
- rare resets near high-current activity;
- support reports that cannot be correlated with a write phase;
- logs that stop before the evidence needed to explain the event.

These weak signals do not prove one root cause. They reduce confidence in the broad claim and justify targeted evidence
gathering.

The Principal Engineer intervention must:

1. separate narrow and broad claims;
2. classify observations, inferences, and assumptions;
3. identify correlated evidence sources;
4. lower confidence in the production claim without discarding valid laboratory evidence;
5. select targeted fault injection around erase/program and commit boundaries;
6. broaden conditions across voltage, temperature, production builds, boards, and flash lots;
7. define minimum operational feedback needed to detect incomplete recovery;
8. recommend a bounded staged commitment with explicit review triggers.

The story must not become:

- a flash-driver tutorial;
- a file-system tutorial;
- a power-supply design lesson;
- an observability implementation guide;
- another ownership or release-management story.

## Expected Discussion Arc

1. Start with the claim, not the dataset.
2. Separate observation from interpretation, inference, confidence, and commitment.
3. Define the evidence envelope: configuration, environment, timing, load, duration, sample diversity, and
   instrumentation limits.
4. Evaluate quality rather than volume.
5. Calibrate confidence for a specific claim.
6. Scale evidence requirements to consequences, Change Radius, reversibility, detectability, and recovery cost.
7. Choose the next evidence action that most reduces decision-critical uncertainty.
8. Commit while keeping residual uncertainty, accepted risk, review triggers, and operational feedback visible.

## Engineering Principle Target

Primary canonical anchor:

`LAW-005` - Evidence Before Confidence.

Chapter-local operational expression:

> The confidence behind a commitment should be no stronger than the evidence that supports its specific claim.

Supporting sentence:

> Increase the required strength of evidence as consequences grow and reversal becomes harder.

Do not register these as new PEAK concepts.

## Architecture Exercise Target

Working title: Build an Evidence-Bounded Judgment.

The exercise should ask the reader to examine one pending technical commitment and produce:

1. the commitment;
2. the exact claim that must be true;
3. directly observed evidence;
4. inference;
5. assumptions;
6. the evidence envelope;
7. relevance, representativeness, coverage, independence, freshness, limitations, and disconfirming evidence;
8. current confidence and its scope;
9. Change Radius, reversibility, detectability, recovery cost, and exposure;
10. the next evidence action;
11. the evidence threshold sufficient for the next commitment;
12. the review trigger.

Required final question:

> What evidence would justify this commitment, and what evidence would merely make the team feel more comfortable?

The exercise is chapter-local. Do not create a new canonical artifact named `Evidence Case`, `Evidence Packet`,
`Confidence Record`, or similar.

## Principal's Notebook Semantic Targets

The final manuscript must contain exactly three short observations.

Candidate semantic targets:

- A test result proves only the claim it actually exercised.
- Repetition is not independence.
- Operational silence is not evidence when failure is unobservable.

These are semantic targets, not mandatory final wording.

## Chapter-Local ADR Brief

Working title: Stage the Flash-Logging Rollout Until Power-Loss Evidence Matches the Product Claim.

Context:

- the new flash-logging path passed endurance testing under stable laboratory conditions;
- existing evidence supports operation in that environment;
- it does not adequately support the durability claim across interrupted flash operations, brownouts, production
  variation, temperature extremes, or recovery behavior;
- weak field observations exist, but their cause is not proven;
- current instrumentation misses some relevant failure states.

Decision:

- do not treat the endurance result as sufficient for immediate fleet-wide rollout;
- define the exact durability claim;
- run targeted power-fault injection around critical flash-operation boundaries;
- use production-equivalent builds and representative hardware, flash lots, voltages, and temperatures;
- add only the minimum operational signals needed to detect incomplete recovery;
- begin with a bounded staged rollout;
- record confidence, residual uncertainty, and review triggers.

Alternatives considered:

- ship broadly based on the endurance result;
- delay until exhaustive proof exists;
- cancel the buffering design;
- add redundancy without first identifying the disputed assumption;
- restrict the feature permanently to controlled environments.

Consequences must include both benefits and costs.

The ADR must be reader-facing and story-local. It must not become a repository-level ADR or a tutorial on ADR mechanics.

## PEAK Concept Map

Primary:

- `LAW-005` - Evidence Before Confidence.

Expected supporting concepts when materially used:

- `ARTIFACT-003` - Decision Journal.
- `VOCAB-002` - Weak Signal.
- `ARTIFACT-007` - Weak Signal Register.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `FAILURE-003` - The Successful Prototype.

Optional supporting concepts only when they materially improve the chapter:

- `FAILURE-005` - The Release We Should Have Delayed.
- `LAW-003` - Time Is a Dependency.
- `SMELL-004` - Hidden State.
- `ARTIFACT-005` - Event Catalog.
- `RITUAL-001` - Architecture Review.
- `ARTIFACT-001` - ADR.

Do not force optional concepts into the manuscript merely to increase the relationship count.

Terms that remain ordinary or chapter-local prose unless a later Canon Review decides otherwise:

- evidence quality;
- confidence calibration;
- uncertainty;
- assumption;
- hypothesis;
- experiment;
- measurement;
- validation envelope;
- evidence envelope;
- disconfirming evidence;
- operational feedback;
- evidence sufficiency;
- evidence-bounded judgment;
- evidence case.

## New-Concept Decision

No new PEAK concept is required during Draft.

Do not:

- create a new law;
- create a new metric;
- create a new artifact;
- create a new ritual;
- create a new smell;
- create new vocabulary;
- allocate a new stable PEAK ID;
- change existing concept definitions;
- change `editor/CANON.md` merely to accommodate Chapter 5 prose.

A future Canon or Knowledge Review may reconsider only if the manuscript demonstrates a stable cross-chapter need that
existing concepts cannot represent.

## Canon Review Acceptance Criteria

Canon Review should ask:

> Does the chapter teach evidence-calibrated technical judgment without becoming a decision framework, test strategy,
> observability chapter, release gate, or stewardship chapter?

Acceptance criteria:

- The chapter has one central idea.
- The chapter preserves exact claim-evidence alignment.
- Observation, measurement, inference, and assumption remain visibly distinct.
- Evidence quality dimensions are concrete and materially used.
- Absence of observed failure is not treated automatically as reliability evidence.
- Correlated repetitions are not treated as independent confirmation.
- Disconfirming evidence and alternative explanations remain visible.
- Confidence is scoped to a specific claim.
- Residual uncertainty remains visible at commitment time.
- Evidence threshold scales to consequence, reversibility, detectability, recovery cost, exposure, and Change Radius.
- Experiments reduce named uncertainty rather than producing generic reassurance.
- Weak signals justify investigation without proving cause.
- Operational feedback can update, narrow, or reopen judgment.
- `Decision Journal` is used only as a lightweight record, not as a replacement for judgment.
- No new PEAK concept is introduced.
- Boundaries with Chapters 1-4, Chapter 6, and later parts are preserved.

## Draft Guardrails

- Do not write a second Chapter 2.
- Do not write a second Chapter 3.
- Do not write a second Chapter 4.
- Do not start Chapter 6.
- Do not create a general testing handbook.
- Do not create a telemetry design chapter.
- Do not imply that more data is always better evidence.
- Do not imply that perfect certainty is required.
- Do not use invented confidence percentages.
- Do not make a Principal Engineer the universal approver of evidence.
- Do not modify existing PEAK concept files during Draft.
- Do not modify `editor/CANON.md` during Draft.

## Final Scope Statement

Chapter 5 should define technical judgment as confidence calibrated to a specific claim, the evidence that supports it,
the uncertainty that remains, and the consequence of being wrong. The chapter should show how a Principal Engineer keeps
valid narrow evidence from being generalized into unsupported broad confidence, chooses targeted evidence actions, and
commits with uncertainty and operational feedback visible.
