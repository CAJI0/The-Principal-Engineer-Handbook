# Простота — це функція продукту

## Вступна цитата

> Simple system — не та, де найменше parts. Це та, чиї consequences все ще можна пояснити.

## Історія

Command path виглядав clean, коли controller уперше shipped.

Input приходив із service interface. Command проходила validation. Runtime state owner вирішував, чи command allowed. Якщо allowed, надсилалася hardware command. Hardware повідомляв result. Controller записував outcome і надсилав diagnostic.

Path був direct, а product behavior легко пояснювалася: validation failed, state owner rejected, hardware sent, completed, failed або entered recovery. Service tool показував reason. Logs показували state. Tests описували product rule.

Потім product виріс. Manufacturing отримав second entry path. UI потребував immediate feedback. Field-service command потребувала іншого diagnostic text. Hardware revision потребувала wrapper. Configuration routed commands інакше для одного variant. Recovery path памʼятав late hardware completion. Support попросив fallback, коли service interface disconnected during calibration.

Ніщо з цього не було foolish. Team додала global service locator, manager modules, generic command objects, callback registries, event forwarding, platform wrappers, configuration routing, utilities, pass-through adapters, fallback paths і shared context.

Кожне addition розвʼязувало local problem. Diagram і далі виглядав organized. Methods були short. Local pieces виглядали tidy.

Потім field issue вимагав малої change: reject one unsafe command while calibration is active, preserve diagnostics and recovery for already-started hardware work.

Це звучало як одна condition.

Engineer знайшов calibration flag в UI command manager, але це був display hint, не authority. Service path використовував інший manager і utility helper. Manufacturing bypassed helper. Fallback path використовував generic command object із platform names. Callback registry міг report completion після повернення manager. Event forwarding оновлював diagnostics after helper accepted. Global context flag читався before routing в одному adapter і after routing в іншому.

Acceptance decision залежав від UI state, configuration, manager state, callback order, global context, utility helper, platform wrapper, deferred hardware completion і logging side effects. Жоден single component не міг пояснити, чому command accepted або rejected.

Tests mocked managers, routers, helpers, configuration, drivers, callbacks і diagnostic strings. Вони доводили forwarding, а не product behavior: command rejected while calibration active, hardware not started, diagnostic explains reason, recovery for already-started work intact.

Logs перелічували infrastructure hops, а не product decision.

Перші proposed fixes додавали ще більше concepts: calibration manager, callback before dispatch, Boolean in shared context, generic policy interface, central module, utility helper rule, call-sequence documentation, more mocks, rewrite, duplicated calibration path.

Principal Engineer змінив питання: «Яке product decision ухвалюється, хто ним owns, і який shortest truthful path веде від input до consequence?»

Decision було accept/reject product command while calibration active, preserving recovery and diagnostics. Owner був runtime state owner, який уже owned calibration state і allowed commands. Team mapped real path і знайшла Manager Mania (`ANTIPATTERN-004`), Silent Coupling (`SMELL-001`), Platform Leakage (`SMELL-005`) і Callback Hell (`ANTIPATTERN-005`).

New shape не був rewrite. Team defined explicit acceptance boundary, owned by product state owner. Boundary використовував product language: command accepted, rejected because calibration active, invalid input, hardware execution started, hardware execution failed, completion deferred, completion timed out, late completion, recovery required, unknown outcome. Entry paths migrated toward boundary. Platform wrapper залишився behind bounded integration edge і не вирішував product acceptance.

Ordinary path став visible: input, validation, state owner decision, hardware integration start, immediate or deferred completion, product-language result, diagnostics at decision and completion.

Tests описували behavior directly. Integration tests і далі covered platform wrapper and callbacks. Change Radius shrank. ADR recorded collapse of command routing into one product-owned decision path.

System не стала tiny. Вона стала explainable.

## Обговорення

`LAW-004` states: Simplicity Is a Feature, тобто простота є функцією продукту, бо робить майбутні зміни безпечнішими.

Simplicity — це не taste, line count, file count, layer count або familiar code. Simplicity — це property, яка дозволяє important behavior пояснювати, змінювати, тестувати, operated, diagnosed і recovered через малий truthful set of concepts.

Truthful matters. Simplistic design прибирає distinctions, які product ще потребує. Один generic `status` може виглядати cleaner, ніж окремі outcomes для rejected input, rejected state, hardware failure, deferred completion, late completion і recovery. Це не simpler, якщо support tool, recovery code і tests rediscover those distinctions elsewhere.

Simple не означає short. Concise, compact, easy, explicit і understandable code повʼязані, але не identical. Global helper може бути easy і робити system less simple. Small explicit boundary може вимагати more code і робити future behavior easier.

Product платить за кожен concept, який треба understood together. Local abstraction може reduce code в одному module і водночас increasing concepts across product. Duplication і unification не є automatically good or bad. Питання в тому, чи result reduces truthful reasoning, чи лише moves complexity behind a clean name.

Essential complexity приходить із real product needs: hardware constraints, protocols, timing, safety behavior, manufacturing, field lifetime, recovery, support tools. Accidental complexity приходить із concepts, яких product не потребував: forwarding managers, utility gravity, event routing hiding control flow, callback chains, runtime configuration recreating code structure, platform terms in product policy, shared context flags, generic command objects.

Simplicity preserves essential complexity і removes accidental concepts.

Abstraction заслуговує місце, коли names stable concept, protects meaningful boundary, reduces duplicated reasoning, narrows Change Radius, preserves dependency direction, clarifies ownership, improves testability або keeps platform details behind product edge. Вона шкодить simplicity, коли hides ordinary control flow, generalizes without evidence, mirrors platform vocabulary, adds managers/registries without reducing concepts або creates unused extension points.

Change Radius (`VOCAB-001` and `METRIC-001`) — practical signal. Це не лише file count; це behavior, ownership, tests, diagnostics, tools і recovery paths, які мають move for safe change.

Discoverability (`METRIC-003`) — ще один signal. Future engineer має знайти decision, owner, contract, state, diagnostics і tests. Poor discoverability перетворює maintenance на archaeology.

Architecture Health (`VOCAB-007` and `METRIC-005`) привʼязує simplicity до product capability: product можна corrected, extended, diagnosed, released, supported і recovered без того, щоб кожне small rule ставало expedition.

Tests і diagnostics показують, чи simplicity реальна. Product-level tests мають named behavior. Diagnostics мають відповідати на product questions: which command, which state, who decided, why accepted/rejected, hardware started, completion deferred, recovery required.

Deletion і narrowing — це design work, коли вони reduce accidental concepts. Simplicity треба підтримувати, поки product evolves, через review, naming, narrowing, migration, ownership, product vocabulary і refusal to keep accidental concepts merely because familiar.

## Інженерний принцип

Обирайте design, який робить product behavior, ownership і consequences найлегшими для пояснення й safe change. Preserve essential complexity; remove accidental concepts.

Review habit:

1. What product decision is being made?
2. Who owns that decision?
3. What is ordinary path from input to consequence?
4. Which exceptional paths must remain distinct?
5. Which concepts must be understood together?
6. Which layers transform behavior, and which only forward it?
7. Where does platform vocabulary leak into product policy?
8. What is true Change Radius?
9. Do tests prove product behavior or architecture mechanics?
10. Can diagnostics explain why decision occurred?
11. Which complexity is essential?
12. Which concept can be removed, narrowed, or renamed?

## Архітектурна вправа

### Поясніть одну поведінку end to end

Оберіть важливу product behavior, що перетинає кілька boundaries: command, state transition, recovery action, manufacturing flow, service-tool operation, hardware interaction або diagnostic decision.

1. What trigger starts behavior?
2. What inputs arrive?
3. Who owns decision?
4. Which state must be known?
5. What is ordinary control path?
6. Which exceptional paths stay distinct?
7. Where is hardware/platform boundary?
8. Which dependencies shape behavior?
9. Which side effects occur?
10. Does operation complete immediately or later?
11. What can fail and what recovery follows?
12. Which diagnostics explain decision?
13. Which tests prove product behavior?
14. Which files, modules, services, tools, or teams involved?
15. Which vocabulary does path use?
16. What is Change Radius for realistic modification?
17. Which layers transform behavior?
18. Which layers only forward behavior?
19. Where duplicated policies exist?
20. Which hidden state affects outcome?
21. Which concepts can be removed, narrowed, or renamed?
22. Where should decision be recorded?

Завершіть одним малим simplification decision: remove pass-through layer, move rule to owner, rename generic outcome in product language, narrow utility helper, align test with product behavior, emit diagnostic at decision point або record scoped ADR.

## Нотатник Principal Engineer

- Simple survives incident pressure.
- Easy now can be expensive later.
- Remove concepts, not truth.

## ADR

### Chapter ADR: Collapse Command Routing into One Product-Owned Decision Path

### Context

Embedded control subsystem accepts commands через UI, service, manufacturing і recovery entry paths. Path обріс managers, generic command objects, callbacks, event forwarding, configuration routing, utilities, adapters, platform wrappers, fallback paths і shared context.

Field issue вимагає narrow product rule: reject unsafe command while calibration active, preserve diagnostics and recovery.

Current design не може explain rule in one place. Tests verify forwarding more than behavior. Diagnostics показують infrastructure hops, але не why accepted/rejected. Hardware completion may be deferred.

### Decision

Assign command acceptance to product state owner, який owns calibration state and command validity.

Define product-level vocabulary українською в product language: invalid input, accepted, rejected because calibration active, hardware execution started, hardware execution failed, completion deferred, completion timed out, late completion, recovery required, cancellation, unknown outcome.

Create explicit acceptance boundary. Entry paths request acceptance through boundary. Keep hardware calls behind bounded integration edge. Remove pass-through layers там, де evidence shows they only forward or hide ownership. Preserve layers, які transform behavior, protect boundary або support migration. Align tests with product behavior. Emit diagnostics at decision point and hardware completion. Migrate incrementally. Record ADR (`ARTIFACT-001`).

### Consequences

Decision becomes discoverable. Change Radius falls. Diagnostics improve. Reviewers separate product policy from platform execution. Work remains: migration, narrowing familiar code, rewriting forwarding tests, preserving asynchronous hardware behavior і avoiding new central module.

### Alternatives Considered

Add another policy manager. Може додати Manager Mania.

Add calibration state to global context. Hides authority і creates Silent Coupling.

Route through generic event bus. Може hide ordinary control flow.

Duplicate command logic per entry point. Fast patch, потім drift.

Rewrite subsystem. Evidence supports scoped routing decision, а не framework replacement.

Document existing call chains. Не removes duplicated policies.

Make driver responsible for product acceptance. Це moves product policy into platform vocabulary.

Introduce generic rules framework. Це adds concept before evidence.

## Коментар редактора

Chapter 12 перетворює earlier laws на product-level property: здатність understand and change important behavior safely. Він використовує state owners, API promises, dependency spread і time тільки там, де вони роблять behavior легшою або важчою для пояснення.

PEAK concepts цього chapter: Simplicity Is a Feature (`LAW-004`), Utility Gravity (`SMELL-002`), Manager Mania (`ANTIPATTERN-004`), Silent Coupling (`SMELL-001`), Platform Leakage (`SMELL-005`), Callback Hell (`ANTIPATTERN-005`), Change Radius (`VOCAB-001` and `METRIC-001`), Discoverability (`METRIC-003`), Architecture Health (`VOCAB-007` and `METRIC-005`) і ADR (`ARTIFACT-001`).
