# Докази перед впевненістю

## Вступна цитата

> Confidence корисна лише тоді, коли її evidence досі належить system, яку ви змінюєте.

## Історія

Timing margin був comfortable, коли product був prototype.

Controller надсилав command до peripheral module, чекав acknowledgement, а тоді дозволяв наступний product state transition. Якщо acknowledgement приходив within deadline, controller продовжував. Якщо ні, controller лишався в previous state і reported timeout.

First team виміряла path достатньо уважно для decision. One prototype board, one module revision, one component lot, room temperature, stable bench supply, one firmware build, one traffic pattern, debug instrumentation, limited repeated command cycles. Response приходив well inside deadline. Worst observed result still left margin. Team recorded ADR (`ARTIFACT-001`): existing bus schedule and command deadline acceptable for prototype and early controlled deployment.

Це не було foolish. Evidence supported narrow claim: on that prototype, with that build, board, module, load, and measurement path, acknowledgement arrived with enough margin for tested command sequence.

Потім product продовжив жити. Compiler upgrade, diagnostic logging, RTOS workload, interrupt source, peripheral firmware, board revision, component tolerance, power management, service-tool mode, colder environment, broader field exposure.

Жодна окрема change не оголосила: «the timing evidence is no longer yours».

ADR залишився accepted. Deadline constant — той самий. Team посилалася на original measurement як на «timing-margin proof». New engineers чули, що path had been measured. Confidence вижила; evidence conditions — ні.

Зʼявилися weak signals: rare field timeouts, rising retries in one variant, local workaround, longer latency on one board revision, cold-room intermittent failure, support reports without enough timing context. Жодне single observation не доводило, що architecture wrong. Але воно lowering confidence in broad active claim.

У PEAK terms це були Weak Signals (`VOCAB-002`): early, low-confidence signs, що decision may be aging badly.

Перші responses захищали old confidence: increase timeout, add retry, repeat bench test, product worked for years, original engineer knew bus, field reports not reproducible, keep ADR unchanged until proof, redesign everything.

Principal Engineer написав: на який current architecture claim ми покладаємося, what evidence still supports it, і what changed since evidence was collected?

Active claim уже не був «prototype command responded quickly». Він став ширшим: current controller and peripheral module receive acknowledgement inside product deadline with enough margin for products, firmware versions, board revisions, power states, loads, environments і exposure, яким тепер дозволено use command path.

Цей claim був більшим за original evidence.

Команда recovered evidence provenance: prototype board revision, peripheral firmware, compiler version, optimization, RTOS workload, bench supply, room temperature, traffic pattern, instrumentation method, run count, latency range. Old evidence remained valuable for original claim and baseline. It did not automatically transfer.

Changes sorted by materiality. Weak signals пішли до Weak Signal Register (`ARTIFACT-007`). Decision Journal (`VOCAB-003` and `ARTIFACT-003`) recorded active claim, historical evidence, current confidence, residual uncertainty і review trigger.

Next evidence action не був «test everything». Team selected smallest targeted revalidation for changed assumption: production-equivalent builds, current RTOS workload, variants carrying claim, board revision with longer latency, relevant peripheral firmware, voltage/temperature, traffic patterns matching signals, minimal diagnostics without altering timing.

Exposure залишався bounded, поки confidence limited. Product variant не broaden deployment, доки evidence не supported broader claim. Existing deployments зберегли monitored path і review trigger.

Ніхто не оголосив original decision irresponsible або current design broken. Команда moved confidence back under evidence.

## Обговорення

`LAW-005` стверджує: Confidence should follow evidence, not replace it.

Chapter 5 питав, чи evidence sufficient for decision being made now. Цей chapter ставить lifecycle question: чи ця evidence still supports architecture claim, який system continues to carry?

Architecture decisions лишаються active роками. Original evidence могла бути good. Problem починається, коли confidence keeps moving forward після того, як evidence conditions перестали рухатися разом із нею.

Architecture confidence є temporary і conditional. Вона має лишатися traceable to specific claim, evidence provenance, product version, operating conditions, residual uncertainty і review trigger.

Confidence — це не certainty, authority, consensus, large test count, successful prototype, accepted ADR, old review note або years without reported failure. Confidence — це current degree of belief, justified by available evidence for claim being carried.

Корисні terms:

- Claim: statement architecture relies on.
- Evidence: observation or result relevant to claim.
- Evidence provenance: origin, version, conditions, measurement path.
- Evidence transfer: reason evidence from one context supports claim in another.
- Revalidation: targeted evidence gathering after material assumption changes.
- Weak signal: early low-confidence observation that affects investigation or confidence without being proof.
- Counter-evidence: observation that narrows or contradicts claim.
- Review trigger: condition requiring judgment to reopen.
- Residual uncertainty: what remains unknown.

Ці definitions keep existing law honest у long-lived system.

The Successful Prototype (`FAILURE-003`) показує trap. Prototype може prove something real і все одно later fail як evidence for production claim. Failure — treating success as permanent architecture property.

Evidence belongs to claim, version, configuration, hardware revision, component lot, build setting, workload, environment, instrumentation path, exposure level і failure-detection capability. Не кожна decision потребує кожного field, але broad product claims потребують known evidence envelope.

Evidence transfer — це judgment, не wish. Lab evidence transfers, коли material conditions remain similar. Він fails, коли debug build changes timing, room temperature does not cover cold, one board revision does not represent another, one traffic pattern misses disputed load, long test repeats easy path або field reports share instrumentation blind spot.

Old evidence лишається useful. Mistake — carrying old confidence without checking whether evidence still belongs to current claim.

Confidence ages, коли material assumptions change: code, compiler settings, workload, hardware, component tolerances, firmware, variants, load, temperature, voltage, power management, diagnostics, exposure і team memory.

Weak signals допомагають before proof exists. Ігнорувати їх, бо вони not proof, так само wrong, як treating them as proof. Weak Signal Register keeps observations alive without confirming defects.

Operational evidence useful лише тоді, коли system can observe what matters. «No failures reported» може означати no failure або no visibility. Іноді architecture work — це adding enough diagnostic context to make claim reviewable.

Revalidation має target changed assumption. «Test more» — не plan. Smallest useful evidence action attacks material change: workload, board revision, temperature, instrumentation, retries, exposure.

Bounded exposure keeps commitment proportionate, поки evidence gathered, але допомагає лише тоді, коли versions known, failure detectable, team can respond і trigger owned.

Ownership matters, бо confidence може стати folklore. Хтось має own active claim, evidence record, confidence/residual uncertainty і revalidation trigger.

Existing artifacts достатньо: ADR, Decision Journal, Weak Signal Register, Architecture Review. Architecture Health (`VOCAB-007` and `METRIC-005`) includes this upkeep.

Decision quality і outcome quality differ. Good engineering preserves what team knew, did not know, why confidence was sufficient і what reopens decision.

Part II laws створюють architecture claims. Вони remain useful лише поки supported by evidence.

## Інженерний принцип

Тримайте architecture confidence привʼязаною до specific claim, evidence envelope і review trigger. Коли system або conditions змінюються, revalidate assumption before carrying confidence forward.

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

Оберіть active architecture claim, що affects product behavior, release confidence, support, manufacturing, recovery, timing, dependency behavior або future change.

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

Завершіть одним decision:

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

Controller sends command to peripheral module і expects acknowledgement before product deadline. Original timing margin був measured on one prototype board, one peripheral module revision, one component lot, room temperature, stable supply, one firmware build, one traffic pattern, debug instrumentation і limited runs.

Current product line still relies on timing margin, але compiler, workload, diagnostics, interrupt load, hardware revision, peripheral firmware, power management, product variants і field exposure changed. Weak signals exist. Current observability не може reliably show all deadline misses, late acknowledgements, retry causes, power-state effects, version context або recovery behavior.

### Decision

Не broaden product exposure based only on original prototype timing measurement.

Define current timing claim і products, firmware versions, hardware revisions, peripheral firmware, build configurations, power states і variants relying on it. Preserve valid historical evidence and conditions. Compare original and current conditions. Run targeted production-equivalent measurements around disputed boundary. Include only material workload, interrupt load, hardware revision, firmware, voltage, temperature, power state і traffic patterns.

Remove or account for debug instrumentation, коли it changes timing. Add minimum diagnostics for deadline misses, late acknowledgements, retries, version, board revision, power state і recovery. Bound exposure until evidence supports broader claim. Record confidence, residual uncertainty і triggers in Decision Journal. Put immature observations in Weak Signal Register. Assign revalidation owner. Reopen Architecture Review, якщо material assumptions change again.

### Consequences

Confidence стає traceable. Historical evidence preserved. Changed assumptions receive targeted testing. Weak signals become actionable without overstatement. Exposure remains proportionate, поки evidence catches up.

Work remains: measurement, instrumentation, constrained exposure, records previously left in memory і possible discovery that margin narrower than expected.

### Alternatives Considered

Keep confidence because product mostly worked. Treats absence of reported failure як stronger evidence, ніж observability supports.

Increase timeout. Може hide late responses і delay recovery.

Add retries. Може mask regression without validating margin.

Repeat original bench test. Це не відповідає на питання transfer to current conditions.

Demand proof of field failure. Це waits for product to pay uncertainty.

Redesign immediately. Може бути necessary later, але current evidence supports targeted revalidation.

Run exhaustive qualification. Може be disproportionate.

Ignore weak signals until reproducible. Це makes weak signals useful only after expensive.

Keep old ADR unchanged. Це hides narrower current confidence.

## Коментар редактора

Chapter 13 closes Part II by making laws answerable to evidence. Він не дублює Chapter 5: Chapter 5 питає, чи evidence sufficient for current decision; Chapter 13 питає, чи ця evidence досі supports claim, який system continues to carry.

PEAK concepts цього chapter: Evidence Before Confidence (`LAW-005`), The Successful Prototype (`FAILURE-003`), Weak Signal (`VOCAB-002`), Weak Signal Register (`ARTIFACT-007`), Decision Journal (`VOCAB-003` and `ARTIFACT-003`), ADR (`ARTIFACT-001`), Architecture Review (`RITUAL-001`), Change Radius (`VOCAB-001` and `METRIC-001`) і Architecture Health (`VOCAB-007` and `METRIC-005`).

Part III тепер може take over. Reader-facing move простий: не питайте, чи old decision was proven wrong. Питайте, чи current claim still supported by current evidence.
