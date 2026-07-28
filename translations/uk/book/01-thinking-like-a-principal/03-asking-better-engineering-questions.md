# Як ставити кращі інженерні питання

## Opening Quote

> Питання успадковує кожне припущення, якого не виявляє.

## Story

Alert виглядав меншим, ніж суперечка навколо нього.

Field device повідомляв, що valve open. User-facing application показувала valve closed. Gateway logs показували, що last command acknowledged. Device logs, зібрані пізніше через service tool, показували, що command arrived і valve eventually moved.

Нікому не сподобалося слово eventually.

Issue не повторювався щоразу. У lab та сама command зазвичай completed cleanly. У field failure зʼявлявся після weak connectivity, battery-saving sleep і repeated user actions. Product team не називала це crash. Customers описували це гірше за crash: system said one thing while equipment did another.

Перші questions були local і reasonable:

«Which packet was lost?»

«Should the timeout be longer?»

«Should the gateway retry more aggressively?»

«Is the application cache broken?»

«Did the device miss the command?»

Кожне питання вказувало на місце, де хтось міг start working. Gateway engineer дістав packet traces. Application engineer inspected cache invalidation. Firmware engineer checked command handling around sleep and wake. Operations engineer compared timestamps. Test engineer reproduced failure by dropping acknowledgments.

Команда швидко зібрала data. Ясніше не стало.

Один trace показував command acknowledgment from gateway to application. Інший — device reporting old state after command. Третій — device later reporting new state with no second user action. Application іноді показувала old state seconds, іноді new state і briefly returned to old one. Gateway cache містив technically latest received value, але ніхто не погоджувався, чи це current.

Fixes multiplied: longer timeout, extra retry, cache invalidation, synthetic state, ignore old reports, pending badge, repeated publish, sequence number, timestamp, both.

Principal Engineer не відкинула options. Вона попросила команду stop writing fixes and write the question.

Перша версія була: «Why does the app show stale state?»

Вона звучала useful, доки команда не спробувала відповісти. Вона вже припускала, що application is where staleness created; що всі agree what stale means; що state існує в одній obvious form; що transport acknowledgment, command acceptance і completed device state — один event.

Жодне припущення не було proven.

Principal Engineer розділила facts і interpretations:

- Application displayed a value that did not match physical device.
- Gateway acknowledged receipt of at least some commands.
- Device sometimes reported old state after command and new state later.
- Different components used different timestamps and retry rules.

Нижче вона записала interpretations:

- Packet was lost.
- Timeout is too short.
- Cache is stale.
- Device state machine is wrong.

Коли два lists розійшлися, room стала тихішою. Interpretations plausible, але not facts.

Вона запитала інакше:

«What evidence would distinguish delayed state, lost state, duplicated state, and incorrectly owned state?»

Питання не solved incident. Воно changed investigation.

Gateway engineer added logging for command receipt, forwarding, device acknowledgment і state publication as separate events. Firmware engineer added events for command accepted into device state machine and device observed resulting operational state. Application engineer stopped treating gateway acknowledgment as evidence that displayed state was current. Test engineer built a run that delayed state reports without dropping acknowledgments.

Команда також записала питання, якого раніше не відповідала:

«Which component owns authoritative device state, and how does every consumer know whether the state is fresh?»

Final architectural decision ще не було.

Це було правильно. Команда still shaping inquiry. Decision мав прийти лише after evidence could distinguish explanations.

## Discussion

Слабке investigation часто fails before first experiment.

Воно fails, коли question accepts untested boundary; коли observation treated as explanation; коли team collects more data without deciding what data must distinguish; коли every component answers different question and meeting mistakes activity for progress.

«Why does the app show stale state?» не було foolish. User saw problem in application, so application became visible boundary. Але visible boundaries не завжди system boundaries. Display was where contradiction appeared, not necessarily where contradiction was created.

Тут questions become engineering instruments.

Useful question makes work smaller by making assumptions visible. Воно не просто просить answer; воно asks for kind of evidence that would change answer.

Команда мала observations: application displayed wrong physical state, acknowledgment existed, device reported old then new state, logs disagreed about timing. Вони важливі, але lost packet, short timeout, stale cache, device-state bug і ownership gap могли fit evidence. Picking one too early turns investigation into confirmation work.

Evidence Before Confidence (`LAW-005`) корисний ще до commitment — when team decides what question it is trying to answer.

Better question has properties:

- separates observation from explanation;
- exposes implicit assumption;
- tests whether accepted boundary is real;
- identifies discriminating evidence;
- reveals ownership.

Acknowledgment був найнебезпечнішим detail, бо звучав precise. Він може означати bytes received, command accepted, operation completed або gateway recorded intent. Якщо interface не каже which meaning applies, acknowledgment becomes Silent Coupling (`SMELL-001`). Teams use same word and trust different promise.

Every API Is a Promise (`LAW-002`) because callers build behavior on meaning they believe interface provides. У story promise стосувався timing, ownership, freshness і validity. Application trusted gateway acknowledgment. Gateway treated cache as last observed value. Device treated physical state as authoritative. Locally none absurd; together they created a customer-visible gap.

Time зробив gap гіршим. Time Is a Dependency (`LAW-003`) when correctness depends on ordering, delay, freshness, or timeout boundaries. Old state був не просто wrong; він був true earlier, false now, and received after newer intent. Value without freshness semantics forced consumers to guess.

Найкориснішим investigation step було вирішити, які facts timestamps мають separate:

- when command requested;
- when gateway received it;
- when device accepted it;
- when device observed resulting operational state;
- when device reported resulting state;
- when application displayed it.

Цей набір facts перетворив vague stale-state complaint на answerable inquiry.

Якщо retries involved, team needed distinguish original command from duplicates. Otherwise retry could hide failure mode.

Team also found a Weak Signal (`VOCAB-002`): several local defenses already existed. Extra gateway retry, application cache refresh, device-side repeat publish, support note telling operators to wait. Together they were low-confidence sign that system did not share one model of state freshness.

Weak Signal Register (`ARTIFACT-007`) would keep concern discoverable while team gathered evidence. It would not say «State architecture is broken». It would record where signal appeared, possible causes, confidence, and next evidence.

Architecture Review (`RITUAL-001`) may eventually decide contract. But review without shaped question becomes tour of opinions. Shaped question gives review something to decide.

Chapter-local ADR below belongs after inquiry separates transport receipt, command acceptance, completed state change, and state freshness into distinct facts.

Endpoint of this chapter is not selected option. Chapter 3 stops earlier. It asks whether team has turned ambiguous problem into inquiry answerable with evidence.

«Should we add another retry?» can be implemented by one team.

«What would prove that retrying addresses the failure mode rather than hiding stale state?» requires naming failure mode, evidence, and owner of relevant state.

Second question is slower at first. It is cheaper if first question would have produced another local fix around unnamed system contract.

## Engineering Principle

Кращі питання роблять припущення testable before they become architecture.

Engineering question becomes useful when it reveals assumption, accepted or challenged boundary, evidence that could change answer, and owner of relevant state, promise, or experiment.

Це не робить questions more important than implementation. Це робить implementation less likely to harden wrong assumption.

Poor question can silently choose architecture. «Should timeout be longer?» can create timing dependency. «Should gateway cache be trusted?» can create ownership boundary. «Should app hide stale state?» can create product promise. Risk is making them before team notices question contains them.

Better question does not need to sound clever. It needs to be answerable.

Strongest form is often plain:

«What evidence would cause us to change our current explanation?»

## Architecture Exercise

Оберіть unresolved engineering question зі своєї current або recent work.

Запишіть:

1. The original question.
2. Direct observations.
3. Interpretations currently presented as facts.
4. Embedded assumptions.
5. The accepted system boundary.
6. At least two plausible explanations.
7. Evidence that would distinguish them.
8. The owner of the relevant state, contract, or next experiment.
9. A rewritten, answerable question.
10. The next evidence-gathering action.

Завершіть питанням:

What evidence would cause us to change our current explanation?

## Principal's Notebook

- Observations are not explanations.
- A question can silently choose the system boundary.
- An answer without evidence or ownership does not close the inquiry.

## ADR

### Chapter ADR: Define Authoritative State and Freshness Semantics

### Context

Device, gateway і application all retain or infer device status. Transport success does not prove displayed state is current. Retries make some failures less visible while allowing stale or duplicated observations to appear valid.

After inquiry separates observable facts, current interface still does not separate transport receipt, command acceptance, completed state change, and freshness of observed state.

### Decision

У цій system device owns authoritative operational state.

Gateway publishes last-observed state with explicit freshness metadata. Acknowledgment, command acceptance, and resulting state are separate facts. Consumers do not infer freshness from transport success. Timing and validity semantics are part of interface promise.

### Consequences

- Ownership of operational state becomes explicit.
- Delay, loss, duplication, and stale-state conditions become more distinguishable.
- Application can show unknown or stale states instead of old data as current.
- Gateway must carry additional metadata and handling logic.
- Tests must cover timing, freshness, delayed reports, duplicated reports, and command/state separation.
- Interface documentation must make freshness semantics discoverable.
- Existing consumers may need to handle unknown or stale states.

### Alternatives Considered

- Increase retries.
- Increase timeout duration.
- Make the gateway cache authoritative.
- Treat the latest received value as current.
- Allow each consumer to infer freshness independently.

## Editor's Commentary

Chapter 1 showed why questions matter: вони expose decision system around code. Chapter 2 showed constrained commitments. Chapter 3 sits before commitment and teaches how to shape inquiry so team does not commit to assumption hidden inside first plausible question.

Chapter intentionally does not teach root-cause analysis, incident response, debugging technique, communication style, or complete Architecture Review process. It also does not decide broader ownership model beyond story-local ADR.

Chapter 4 will continue into ownership beyond code. This chapter prepares that move by showing why ownership often first appears as question: who owns state, promise, or next experiment that would make system knowable?
