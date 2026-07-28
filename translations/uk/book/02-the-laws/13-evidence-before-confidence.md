# Докази перед впевненістю

## Вступна цитата

> Confidence корисна лише тоді, коли її evidence досі належить system, яку ви змінюєте.

## Історія

Timing margin був comfortable, коли product був prototype.

Controller sent command to peripheral module, waited for acknowledgement, then allowed next product state transition. If acknowledgement arrived within deadline, controller continued. If not, controller stayed in previous state and reported timeout.

First team measured path carefully enough for decision. One prototype board, one module revision, one component lot, room temperature, stable bench supply, one firmware build, one traffic pattern, debug instrumentation, limited repeated command cycles. Response arrived well inside deadline. Worst observed result still left margin. Team recorded ADR (`ARTIFACT-001`): existing bus schedule and command deadline acceptable for prototype and early controlled deployment.

That was not foolish. Evidence supported narrow claim: on that prototype, with that build, board, module, load, and measurement path, acknowledgement arrived with enough margin for tested command sequence.

Then product kept living. Compiler upgrade, diagnostic logging, RTOS workload, interrupt source, peripheral firmware, board revision, component tolerance, power management, service-tool mode, colder environment, broader field exposure.

No single change announced, "the timing evidence is no longer yours."

ADR stayed accepted. Deadline constant same. Team referred to original measurement as "timing-margin proof." New engineers heard path had been measured. Confidence survived; evidence conditions did not.

Weak signals appeared: rare field timeouts, rising retries in one variant, local workaround, longer latency on one board revision, cold-room intermittent failure, support reports without enough timing context. No single observation proved architecture wrong. But it lowered confidence in broad active claim.

In PEAK terms, those were Weak Signals (`VOCAB-002`): early, low-confidence signs that decision may be aging badly.

First responses defended old confidence: increase timeout, add retry, repeat bench test, product worked for years, original engineer knew bus, field reports not reproducible, keep ADR unchanged until proof, redesign everything.

Principal Engineer wrote: which current architecture claim are we relying on, what evidence still supports it, and what changed since evidence was collected?

Active claim was no longer "prototype command responded quickly." It was: current controller and peripheral module receive acknowledgement inside product deadline with enough margin for products, firmware versions, board revisions, power states, loads, environments, and exposure now allowed to use command path.

That claim was larger than original evidence.

Team recovered evidence provenance: prototype board revision, peripheral firmware, compiler version, optimization, RTOS workload, bench supply, room temperature, traffic pattern, instrumentation method, run count, latency range. Old evidence remained valuable for original claim and baseline. It did not automatically transfer.

Changes were sorted by materiality. Weak signals went into Weak Signal Register (`ARTIFACT-007`). Decision Journal (`VOCAB-003` and `ARTIFACT-003`) recorded active claim, historical evidence, current confidence, residual uncertainty, and review trigger.

Next evidence action was not "test everything." Team selected smallest targeted revalidation for changed assumption: production-equivalent builds, current RTOS workload, variants carrying claim, board revision with longer latency, relevant peripheral firmware, voltage/temperature, traffic patterns matching signals, minimal diagnostics without altering timing.

Exposure stayed bounded while confidence limited. Product variant would not broaden deployment until evidence supported broader claim. Existing deployments kept monitored path and review trigger.

No one declared original decision irresponsible or current design broken. Team moved confidence back under evidence.

## Обговорення

`LAW-005` states: Confidence should follow evidence, not replace it.

Chapter 5 asked whether evidence is sufficient for decision being made now. This chapter asks lifecycle question: does that evidence still support architecture claim the system continues to carry?

Architecture decisions remain active for years. Original evidence may have been good. Problem begins when confidence keeps moving forward after evidence conditions stop moving with it.

Architecture confidence is temporary and conditional. It must remain traceable to specific claim, evidence provenance, product version, operating conditions, residual uncertainty, and review trigger.

Confidence is not certainty, authority, consensus, large test count, successful prototype, accepted ADR, old review note, or years without reported failure. Confidence is current degree of belief justified by available evidence for claim being carried.

Useful terms:

- Claim: statement architecture relies on.
- Evidence: observation or result relevant to claim.
- Evidence provenance: origin, version, conditions, measurement path.
- Evidence transfer: reason evidence from one context supports claim in another.
- Revalidation: targeted evidence gathering after material assumption changes.
- Weak signal: early low-confidence observation that affects investigation or confidence without being proof.
- Counter-evidence: observation that narrows or contradicts claim.
- Review trigger: condition requiring judgment to reopen.
- Residual uncertainty: what remains unknown.

These definitions keep existing law honest in long-lived system.

The Successful Prototype (`FAILURE-003`) shows the trap. Prototype can prove something real and still fail as evidence for production claim later. Failure is treating success as permanent architecture property.

Evidence belongs to claim, version, configuration, hardware revision, component lot, build setting, workload, environment, instrumentation path, exposure level, and failure-detection capability. Not every decision needs every field, but broad product claims need known evidence envelope.

Evidence transfer is judgment, not wish. Lab evidence transfers when material conditions remain similar. It fails when debug build changes timing, room temperature does not cover cold, one board revision does not represent another, one traffic pattern misses disputed load, long test repeats easy path, or field reports share instrumentation blind spot.

Old evidence remains useful. Mistake is carrying old confidence without checking whether evidence still belongs to current claim.

Confidence ages when material assumptions change: code, compiler settings, workload, hardware, component tolerances, firmware, variants, load, temperature, voltage, power management, diagnostics, exposure, and team memory.

Weak signals help before proof exists. Ignoring them because not proof is as wrong as treating them as proof. Weak Signal Register keeps observations alive without confirming defects.

Operational evidence is useful only when system can observe what matters. "No failures reported" may mean no failure, or no visibility. Sometimes architecture work is adding enough diagnostic context to make claim reviewable.

Revalidation should target changed assumption. "Test more" is not a plan. Smallest useful evidence action attacks material change: workload, board revision, temperature, instrumentation, retries, exposure.

Bounded exposure keeps commitment proportionate while evidence gathered, but only helps when versions known, failure detectable, team can respond, and trigger owned.

Ownership matters because confidence can become folklore. Someone should own active claim, evidence record, confidence/residual uncertainty, and revalidation trigger.

Existing artifacts are enough: ADR, Decision Journal, Weak Signal Register, Architecture Review. Architecture Health (`VOCAB-007` and `METRIC-005`) includes this upkeep.

Decision quality and outcome quality differ. Good engineering preserves what team knew, did not know, why confidence was sufficient, and what reopens decision.

Part II laws create architecture claims. They remain useful only while supported by evidence.

## Інженерний принцип

Keep architecture confidence attached to specific claim, evidence envelope, and review trigger. When system or conditions change, revalidate assumption before carrying confidence forward.

Review habit:

1. What claim are we relying on?
2. What evidence supports it now?
3. Which version, hardware, build, load, and environment did it cover?
4. What changed?
5. Why should evidence transfer?
6. What can measurement not see?
7. Which weak signals exist?
8. What would lower confidence?
9. Who owns revalidation?
10. What is smallest targeted evidence action?
11. What confidence is enough for next commitment?
12. What trigger reopens decision?

## Архітектурна вправа

### Revalidate One Architecture Claim

Choose active architecture claim affecting product behavior, release confidence, support, manufacturing, recovery, timing, dependency behavior, or future change.

1. What exact claim is architecture relying on?
2. Which products, versions, and variants rely on it?
3. Which original decision or artifact recorded it?
4. What original evidence supported it?
5. Under which hardware, software, build, load, environment, timing, and instrumentation conditions was evidence collected?
6. What evidence supports claim now?
7. What changed since evidence collected?
8. Which assumptions required for old evidence to transfer?
9. Which evidence remains valid?
10. Which evidence no longer transfers cleanly?
11. What can current measurement or operational feedback not see?
12. Which weak signals exist?
13. Which counter-evidence narrows or contradicts claim?
14. What is current confidence and scope?
15. What consequence if claim wrong?
16. How reversible is next commitment?
17. How detectable would failure be?
18. What is smallest targeted revalidation?
19. Who owns claim and revalidation?
20. What condition should reopen decision?
21. Which ADR, Decision Journal, or Weak Signal Register entry needs creation/update?

End with one decision:

- confidence remains justified;
- confidence narrows;
- revalidation is required;
- commitment must be bounded;
- architecture decision must reopen;
- observability must improve before confidence can rise.

## Нотатник Principal Engineer

- Confidence ages with its conditions.
- Success does not repair weak reasoning.
- Weak signals speak before proof arrives.

## ADR

### Chapter ADR: Revalidate the Communication Timing Margin Before Broadening Product Exposure

### Context

Controller sends command to peripheral module and expects acknowledgement before product deadline. Original timing margin was measured on one prototype board, one peripheral module revision, one component lot, room temperature, stable supply, one firmware build, one traffic pattern, debug instrumentation, and limited runs.

Current product line still relies on timing margin, but compiler, workload, diagnostics, interrupt load, hardware revision, peripheral firmware, power management, product variants, and field exposure changed. Weak signals exist. Current observability cannot reliably show all deadline misses, late acknowledgements, retry causes, power-state effects, version context, or recovery behavior.

### Decision

Do not broaden product exposure based only on original prototype timing measurement.

Define current timing claim and products, firmware versions, hardware revisions, peripheral firmware, build configurations, power states, and variants relying on it. Preserve valid historical evidence and conditions. Compare original and current conditions. Run targeted production-equivalent measurements around disputed boundary. Include only material workload, interrupt load, hardware revision, firmware, voltage, temperature, power state, and traffic patterns.

Remove or account for debug instrumentation when it changes timing. Add minimum diagnostics for deadline misses, late acknowledgements, retries, version, board revision, power state, and recovery. Bound exposure until evidence supports broader claim. Record confidence, residual uncertainty, and triggers in Decision Journal. Put immature observations in Weak Signal Register. Assign revalidation owner. Reopen Architecture Review if material assumptions change again.

### Consequences

Confidence becomes traceable. Historical evidence preserved. Changed assumptions receive targeted testing. Weak signals become actionable without overstatement. Exposure remains proportionate while evidence catches up.

Work remains: measurement, instrumentation, constrained exposure, records previously left in memory, possible discovery that margin narrower than expected.

### Alternatives Considered

Keep confidence because product mostly worked. Treats absence of reported failure as stronger evidence than observability supports.

Increase timeout. May hide late responses and delay recovery.

Add retries. May mask regression without validating margin.

Repeat original bench test. Does not answer transfer to current conditions.

Demand proof of field failure. Waits for product to pay uncertainty.

Redesign immediately. May be necessary later but current evidence supports targeted revalidation.

Run exhaustive qualification. May be disproportionate.

Ignore weak signals until reproducible. Makes weak signals useful only after expensive.

Keep old ADR unchanged. Hides narrower current confidence.

## Коментар редактора

Chapter 13 closes Part II by making laws answerable to evidence. It does not duplicate Chapter 5: Chapter 5 asks whether evidence is sufficient for current decision; Chapter 13 asks whether that evidence still supports claim system continues to carry.

The PEAK concepts carrying the chapter are Evidence Before Confidence (`LAW-005`), The Successful Prototype (`FAILURE-003`), Weak Signal (`VOCAB-002`), Weak Signal Register (`ARTIFACT-007`), Decision Journal (`VOCAB-003` and `ARTIFACT-003`), ADR (`ARTIFACT-001`), Architecture Review (`RITUAL-001`), Change Radius (`VOCAB-001` and `METRIC-001`), and Architecture Health (`VOCAB-007` and `METRIC-005`).

Part III can now take over. The reader-facing move is simple: do not ask whether old decision was proven wrong. Ask whether current claim is still supported by current evidence.
