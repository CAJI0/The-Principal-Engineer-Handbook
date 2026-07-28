# Інженерне судження й докази

## Вступна цитата

> Доказ корисний лише тоді, коли ви знаєте, яке твердження він підтримує.

## Історія

Test report заспокоював так, як може заспокоювати добре число.

Industrial controller отримав новий buffered logging path. Device зберігав diagnostic і process events у external NOR flash. Старий path писав надто часто, нерівномірно зношував blocks і іноді робив bursts of events видимими як small stalls elsewhere in the system. Новий design batched records in RAM, programmed them in larger batches і тримав story-local recovery metadata, щоб device міг reconstruct committed log state after reset.

Change був ordinary in the best sense: reduced wear, made bursts less intrusive, and promised better evidence when next field issue arrived.

Team had evidence. Prototype board completed multi-day endurance run. Test wrote far more records than typical customer site. CRC checks passed. No data loss reproduced. Product demonstration went well. Support lead liked new logs; firmware lead liked reduced write amplification; product owner liked no hardware change.

Release note draft said:

«The new logging path preserves diagnostic records through unstable field power.»

That sentence changed the room.

Principal Engineer asked what test had proven.

First answer: logger survived endurance run. True.

Then answers widened: many records written, recovered after resets, no CRC failures, no lab data loss, supported demonstration, reduced flash wear, did not disturb normal operation. None useless.

Principal Engineer wrote three claims:

1. The buffered logging implementation works under the tested laboratory conditions.
2. Record recovery behaves correctly when flash operations are interrupted.
3. The production product preserves useful diagnostic records through realistic field power disturbances.

Team agreed first claim had evidence.

Second was less comfortable. Endurance run included orderly software resets, but not interrupted erase/program around critical transitions, repeated power removal while recovery metadata updated, partly programmed record followed by boot with marginal supply.

Third was broader: one prototype board, one flash lot, nominal temperature, stable lab power, debug build timing, repeated same sequence. Repeatable did not mean independent.

Team did not like the direction. Nobody wanted restart release or dismiss successful endurance test. Support had practical concern: field diagnostics already weak; delaying new path kept old one longer.

Then field notes arrived. They were not proof. A few devices had missing records after reported power disturbances. Two support cases mentioned rare resets near high-current activity. One log stopped shortly before event support needed. Another booted cleanly but lacked recovery detail.

Each observation could be explained away. Customer may have power-cycled twice. Support tool may have collected logs after rotation. Reset may have been unrelated. Missing records may have come from old path.

All possible.

Principal Engineer did not call logger broken. She called field notes weak signals.

In PEAK terms, Weak Signal (`VOCAB-002`) is early, low-confidence sign that system decision may be aging badly. Observations did not establish root cause. They reduced confidence in broad production claim.

Team changed release question:

«What evidence would justify the claim that this logging path preserves diagnostic records through realistic power disturbance, and what commitment can we make before that evidence exists?»

Answer was not to test forever.

Team kept successful endurance result and narrowed what it proved. They planned targeted power-fault injection around erase, program, record commit, and recovery-metadata transitions. They added production-configuration testing on boards and flash lots chosen for relevant variation. They included voltage and temperature conditions matching product environment.

They also changed reporting. Incomplete recovery had to become observable enough for support and engineering. Quiet boot after failed recovery would make next field case look better than system deserved.

Team chose staged commitment: bounded deployment, supported stop/disable path, version context, operational feedback. Decision Journal (`ARTIFACT-003`) recorded claim, evidence, confidence, residual uncertainty, and review trigger. Release language changed: it no longer promised lab endurance had proved field durability; it stated narrower evidenced property and conditions for revisiting broader claim.

No one became less technical.

They became less willing to let successful test prove wrong claim.

## Обговорення

Data does not interpret itself. Test result, measurement, prototype, benchmark, simulation, field report, or expert opinion becomes evidence only in relation to a claim. Same result can be strong evidence for one claim, weak for another, irrelevant for third.

Endurance run was not bad evidence. It was good evidence for bounded claim: buffered logging path could run for several days, on that board, with that flash part, in that environment, along that repeated path, without failures the test could detect.

Problem appeared when team let result support wider claim: production device would preserve diagnostic records through unstable field power.

Wider claim included power interruption, recovery behavior, product variation, build timing, temperature, supply conditions, and observability of failures. Some may eventually be covered. Original test did not cover them.

That is danger behind The Successful Prototype (`FAILURE-003`): valid result in one environment becomes production architecture before claim reviewed.

Technical judgment begins before asking whether evidence sufficient. Team must say what evidence supports. «Logger passed endurance testing» is result. «Logger preserves records through interrupted flash operations in field» is claim. «We should enable this path across fleet» is commitment. Related, but not interchangeable.

A useful reasoning chain:

```text
Observation -> interpretation -> inference -> confidence -> commitment
```

Observation may be no CRC failures. Interpretation: stored records internally consistent. Inference: recovery likely working. Confidence: medium for tested path. Commitment: staged rollout or broad release. Each arrow introduces uncertainty.

Evidence has an envelope: hardware and software version, build configuration, environment, load, timing, duration, sample diversity, state boundaries, failure boundaries, and instrumentation. It reminds team that evidence is collected somewhere, under conditions, with blind spots.

In embedded systems, those conditions matter. Supply voltage, temperature, flash lots, build configuration, instrumentation timing, reset style, field power loss — all can change what evidence means.

Repetition is useful when it exercises claim. Ten thousand clean writes through one sequence may be less valuable than one fault-injection run around externally visible commit transition.

Evidence quality depends on questions:

- Is it relevant to the claim?
- Is it representative of conditions commitment will face?
- Does it cover important states and boundaries?
- Are sources independent?
- Is evidence fresh?
- What can measurement not see?
- What evidence would contradict preferred explanation?

These do not require statistics lecture. They require intellectual cleanliness.

Confidence should attach to a specific claim. Team can have high confidence for lab endurance run, lower confidence for interrupted flash operations, and lower still for broad production durability. Those levels can coexist.

Evidence Before Confidence (`LAW-005`) means confidence should follow evidence, not replace it. Experience and intuition matter, but need basis. Otherwise confidence becomes private memory with serious voice.

Stronger commitment needs stronger evidence. Small exposure, easy rollback, strong detectability, low recovery cost can move with modest evidence and review trigger. Broad exposure, difficult rollback, weak detectability, high recovery cost, or large Change Radius (`VOCAB-001`) deserves stronger evidence.

Change Radius metric (`METRIC-001`) should not become fake precision. It asks how much surface must change, be reviewed, or retested if decision changes. Logging durability claim affects firmware, support tooling, release notes, customer diagnostics, and field investigation.

Detectability matters. Failure that announces itself allows learning after limited commitment. Failure hidden inside missing diagnostic records is more dangerous because evidence disappears with failure. «We have not seen failures» is not same as «system is reliable».

Next evidence action should attack decision-critical uncertainty. «Test more» too vague. Better: which experiment, measurement, or observation can change commitment?

For logger, next action was targeted power-fault injection around erase, program, commit, and recovery; production-like configurations; operational feedback independent enough to survive failure; broader hardware/environment conditions where claim depends on them.

Weak signals deserve disciplined respect. Field observations did not prove buffered logger wrong. Treating them as proof would be bad judgment. They were low-confidence observations conflicting with broad confidence — enough to lower confidence and investigate.

Weak Signal Register (`ARTIFACT-007`) records observation, where it appeared, possible cause, confidence, next evidence, and review date/trigger. It should not turn discomfort into confirmed defect.

Operational feedback is evidence too, only if system can observe what team needs to learn. Staged rollout can be responsible when exposure bounded, feedback meaningful, version/configuration context present, review triggers owned, and stop/disable/rollback path credible. It is not substitute for validation.

Sometimes next technical task is not the feature. It is making result of feature knowable.

Decision Journal can preserve judgment:

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
bounded operational feedback from staged deployment with version/configuration context.
```

Record does not make decision correct. It makes judgment reviewable.

Good outcomes do not retroactively strengthen weak evidence. Failure can occur after responsible evidence work. Decision quality and outcome quality related, but not same.

New evidence should update confidence. If field feedback contradicts old evidence, team should not defend old confidence because release plan said so. If stronger testing supports claim, confidence can rise without pretending uncertainty gone. If evidence supports only smaller claim, commitment should shrink or next evidence action become clearer.

Evidence is sufficient when it justifies next commitment, not when it eliminates every unknown.

That is technical judgment under incomplete information.

## Інженерний принцип

Evidence Before Confidence (`LAW-005`) is canonical anchor for this chapter.

Confidence behind commitment should be no stronger than evidence supporting its specific claim.

This matters because teams rarely have perfect proof. Waiting for certainty can avoid judgment. But acting as if narrow test proves broad claim transfers uncertainty into product, field, or next engineer's investigation.

Trade-off is not evidence versus motion. It is honest motion versus unsupported confidence.

Increase required evidence strength as consequences grow and reversal becomes harder. Prototype success may justify next experiment. It should not automatically justify production claim.

Practical consequence: make claim explicit, name evidence, state confidence, expose uncertainty, and define feedback that would change judgment.

## Архітектурна вправа

### Build an Evidence-Bounded Judgment

Choose one pending or recent technical commitment.

Write short answers:

1. Commitment і claim:
   Який commitment розглядається? Яке точне claim має бути true, щоб цей commitment був responsible?
2. Докази й reasoning:
   Що було прямо observed? Що команда inferred? Які assumptions лишаються?
3. Умови та якість доказів:
   За яких hardware, software, build, environment, load, timing, duration та instrumentation conditions були зібрані докази? Наскільки вони relevant, representative, independent і fresh? Які states, boundaries, failure modes і blind spots covered або missing? Які observations contradicted або lowered confidence?
4. Confidence і consequence:
   Яка current confidence і її scope? Який Change Radius? Наскільки commitment reversible? Наскільки failure detectable? Якою буде recovery cost? Яку exposure створює commitment?
5. Наступна дія:
   Яка next evidence action найбільше зменшить decision-critical uncertainty? Який evidence threshold достатній для next commitment? Який review trigger має reopen judgment?

Які докази виправдали б цей commitment, а які лише зробили б команді спокійніше?

## Нотатник Principal Engineer

- Test result доводить лише claim, який він перевіряв.
- Repetition не є independence.
- Silence є слабким evidence, коли failure важко observe.

## ADR

### Chapter ADR: Stage the Flash-Logging Rollout Until Power-Loss Evidence Matches the Product Claim

### Context

New buffered flash-logging path passed endurance testing under stable lab conditions. That evidence supports implementation under tested environment.

Product claim is broader: preserve useful diagnostic records through realistic power disturbance and recovery. Current evidence does not cover interrupted erase/program, brownouts near commit transitions, production-equivalent timing, representative hardware/flash variation, temperature, or incomplete recovery visibility.

Weak field observations exist: missing records after reported power disturbance, rare resets near high-current activity, logs stopping before support-critical event. They do not prove root cause but reduce confidence in broad durability claim.

Instrumentation misses some relevant failure states. Failed or incomplete recovery can look like clean boot.

### Decision

Do not treat endurance result as sufficient evidence for immediate fleet-wide rollout.

Define exact durability claim. Run targeted power-fault injection around erase, program, commit, and recovery-metadata updates. Use production-equivalent configurations and boards, flash lots, voltages, and temperatures relevant to claim.

Add minimum useful operational evidence to detect incomplete recovery, with persistent recovery status and version/configuration context. Begin with bounded staged rollout that has owned review trigger and supported stop, disable, rollback, or escalation path. Record confidence, residual uncertainty, and review triggers before broad exposure.

### Consequences

Evidence better aligns with product claim. Team preserves valid confidence in lab result while refusing to overstate it. Exposure bounded while evidence accumulates. Review triggered by predefined observations.

Extra validation and instrumentation work. Broad deployment delayed. Support and operations may handle temporary staged behavior. Some uncertainty remains.

### Alternatives Considered

Ship broadly based on endurance result. Rejected because result supports narrower claim.

Delay until exhaustive proof exists. Rejected because exhaustive proof unrealistic.

Cancel buffering design. Rejected because design addresses real write-amplification and diagnostic needs.

Add redundancy without identifying disputed assumption. Rejected because complexity could grow while interruption and observability questions remain.

Restrict feature permanently to controlled environments. Rejected as premature.

## Коментар редактора

Chapter 1 established Principal Engineer as responsible for future cost. Chapter 2 made constrained commitments explicit. Chapter 3 shaped questions. Chapter 4 made ownership of closure visible.

Chapter 5 sits after those moves because evidence can still be misused after question, decision, and ownership are shaped. Team can possess real data and draw wrong boundary around what it proves.

Chapter makes confidence reviewable: ask whether evidence is good enough for specific claim and commitment.

It reuses PEAK concepts: Evidence Before Confidence (`LAW-005`), Weak Signal (`VOCAB-002`), Change Radius (`VOCAB-001` and `METRIC-001`), The Successful Prototype (`FAILURE-003`), Weak Signal Register (`ARTIFACT-007`), and Decision Journal (`ARTIFACT-003`).

Chapter 6 keeps broader stewardship question: how Principal Engineer leaves systems healthier, easier to change, and better supported after immediate work.
