# Простота — це функція продукту

## Вступна цитата

> Simple system - не та, де найменше parts. Це та, чиї consequences still can be explained.

## Історія

Command path looked clean when controller first shipped.

Input arrived from service interface. Command validated. Runtime state owner decided whether command allowed. If allowed, hardware command issued. Hardware reported result. Controller recorded outcome and sent diagnostic.

Path was direct, and product behavior easy to explain: validation failed, state owner rejected, hardware sent, completed, failed, or entered recovery. Service tool showed reason. Logs showed state. Tests described product rule.

Then product grew. Manufacturing got second entry path. UI needed immediate feedback. Field-service command needed different diagnostic text. Hardware revision needed wrapper. Configuration routed commands differently for one variant. Recovery path remembered late hardware completion. Support requested fallback when service interface disconnected during calibration.

None was foolish. Team added global service locator, manager modules, generic command objects, callback registries, event forwarding, platform wrappers, configuration routing, utilities, pass-through adapters, fallback paths, and shared context.

Each addition solved local problem. Diagram still looked organized. Methods were short. Local pieces looked tidy.

Then field issue required small change: reject one unsafe command while calibration is active, preserve diagnostics and recovery for already-started hardware work.

It sounded like one condition.

Engineer found calibration flag in UI command manager, but it was display hint, not authority. Service path used different manager and utility helper. Manufacturing bypassed helper. Fallback path used generic command object with platform names. Callback registry could report completion after manager returned. Event forwarding updated diagnostics after helper accepted. Global context flag was read before routing in one adapter and after routing in another.

Acceptance decision depended on UI state, configuration, manager state, callback order, global context, utility helper, platform wrapper, deferred hardware completion, and logging side effects. No single component could explain why command accepted or rejected.

Tests mocked managers, routers, helpers, configuration, drivers, callbacks, and diagnostic strings. They proved forwarding, not product behavior: command rejected while calibration active, hardware not started, diagnostic explains reason, recovery for already-started work intact.

Logs listed infrastructure hops, not product decision.

First proposed fixes added more concepts: calibration manager, callback before dispatch, Boolean in shared context, generic policy interface, central module, utility helper rule, call-sequence documentation, more mocks, rewrite, duplicated calibration path.

Principal Engineer changed question: "What product decision is being made, who owns it, and what is the shortest truthful path from input to consequence?"

Decision was accept/reject a product command while calibration active, preserving recovery and diagnostics. Owner was runtime state owner that already owned calibration state and allowed commands. Team mapped real path and found Manager Mania (`ANTIPATTERN-004`), Silent Coupling (`SMELL-001`), Platform Leakage (`SMELL-005`), and Callback Hell (`ANTIPATTERN-005`).

New shape was not rewrite. Team defined explicit acceptance boundary owned by product state owner. Boundary used product language: command accepted, rejected because calibration active, invalid input, hardware execution started, hardware execution failed, completion deferred, completion timed out, late completion, recovery required, unknown outcome. Entry paths migrated toward boundary. Platform wrapper stayed behind bounded integration edge and did not decide product acceptance.

Ordinary path became visible: input, validation, state owner decision, hardware integration start, immediate or deferred completion, product-language result, diagnostics at decision and completion.

Tests described behavior directly. Integration tests still covered platform wrapper and callbacks. Change Radius shrank. ADR recorded collapse of command routing into one product-owned decision path.

System не стала tiny. Вона стала explainable.

## Обговорення

`LAW-004` states: Simplicity Is a Feature, тобто простота є функцією продукту, бо робить майбутні зміни безпечнішими.

Simplicity is not taste, line count, file count, layer count, or familiar code. Simplicity is the property that lets important behavior be explained, changed, tested, operated, diagnosed, and recovered with a small truthful set of concepts.

Truthful matters. Simplistic design removes distinctions product still needs. One generic `status` can look cleaner than separate outcomes for rejected input, rejected state, hardware failure, deferred completion, late completion, and recovery. It is not simpler if support tool, recovery code, and tests rediscover those distinctions elsewhere.

Simple does not mean short. Concise, compact, easy, explicit, and understandable code are related but not identical. Global helper may be easy and make system less simple. Small explicit boundary may require more code and make future behavior easier.

Product pays for every concept that must be understood together. Local abstraction can reduce code in one module while increasing concepts across product. Duplication and unification are not automatically good or bad. Question is whether result reduces truthful reasoning or only moves complexity behind a clean name.

Essential complexity comes from real product needs: hardware constraints, protocols, timing, safety behavior, manufacturing, field lifetime, recovery, support tools. Accidental complexity comes from concepts product did not need: forwarding managers, utility gravity, event routing hiding control flow, callback chains, runtime configuration recreating code structure, platform terms in product policy, shared context flags, generic command objects.

Simplicity preserves essential complexity and removes accidental concepts.

Abstraction earns place when it names stable concept, protects meaningful boundary, reduces duplicated reasoning, narrows Change Radius, preserves dependency direction, clarifies ownership, improves testability, or keeps platform details behind product edge. It harms simplicity when it hides ordinary control flow, generalizes without evidence, mirrors platform vocabulary, adds managers/registries without reducing concepts, or creates unused extension points.

Change Radius (`VOCAB-001` and `METRIC-001`) is practical signal. It is not just file count; it is behavior, ownership, tests, diagnostics, tools, and recovery paths that must move for safe change.

Discoverability (`METRIC-003`) is another signal. Future engineer should find decision, owner, contract, state, diagnostics, and tests. Poor discoverability turns maintenance into archaeology.

Architecture Health (`VOCAB-007` and `METRIC-005`) ties simplicity to product capability: product can be corrected, extended, diagnosed, released, supported, and recovered without every small rule becoming expedition.

Tests and diagnostics reveal whether simplicity is real. Product-level tests should name behavior. Diagnostics should answer product questions: which command, which state, who decided, why accepted/rejected, hardware started, completion deferred, recovery required.

Deletion and narrowing are design work when they reduce accidental concepts. Simplicity must be maintained as product evolves through review, naming, narrowing, migration, ownership, product vocabulary, and refusal to keep accidental concepts merely because familiar.

## Інженерний принцип

Prefer the design that makes product behavior, ownership, and consequences easiest to explain and safely change. Preserve essential complexity; remove accidental concepts.

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

Embedded control subsystem accepts commands through UI, service, manufacturing, and recovery entry paths. Path has grown managers, generic command objects, callbacks, event forwarding, configuration routing, utilities, adapters, platform wrappers, fallback paths, and shared context.

Field issue requires narrow product rule: reject unsafe command while calibration active, preserve diagnostics and recovery.

Current design cannot explain rule in one place. Tests verify forwarding more than behavior. Diagnostics show infrastructure hops but not why accepted/rejected. Hardware completion may be deferred.

### Decision

Assign command acceptance to product state owner that owns calibration state and command validity.

Define product-level vocabulary: invalid input, accepted, rejected because calibration active, hardware execution started, hardware execution failed, completion deferred, completion timed out, late completion, recovery required, cancellation, unknown outcome.

Create explicit acceptance boundary. Entry paths request acceptance through boundary. Keep hardware calls behind bounded integration edge. Remove pass-through layers where evidence shows they only forward or hide ownership. Preserve layers that transform behavior, protect boundary, or support migration. Align tests with product behavior. Emit diagnostics at decision point and hardware completion. Migrate incrementally. Record ADR (`ARTIFACT-001`).

### Consequences

Decision becomes discoverable. Change Radius falls. Diagnostics improve. Reviewers separate product policy from platform execution. Work remains: migration, narrowing familiar code, rewriting forwarding tests, preserving asynchronous hardware behavior і avoiding new central module.

### Alternatives Considered

Add another policy manager. May add Manager Mania.

Add calibration state to global context. Hides authority and creates Silent Coupling.

Route through generic event bus. May hide ordinary control flow.

Duplicate command logic per entry point. Fast patch, later drift.

Rewrite subsystem. Evidence supports scoped routing decision, not framework replacement.

Document existing call chains. Does not remove duplicated policies.

Make driver responsible for product acceptance. Moves product policy into platform vocabulary.

Introduce generic rules framework. Adds concept before evidence.

## Коментар редактора

Chapter 12 перетворює earlier laws на product-level property: здатність understand and change important behavior safely. Він використовує state owners, API promises, dependency spread і time тільки там, де вони роблять behavior легшою або важчою для пояснення.

PEAK concepts цього chapter: Simplicity Is a Feature (`LAW-004`), Utility Gravity (`SMELL-002`), Manager Mania (`ANTIPATTERN-004`), Silent Coupling (`SMELL-001`), Platform Leakage (`SMELL-005`), Callback Hell (`ANTIPATTERN-005`), Change Radius (`VOCAB-001` and `METRIC-001`), Discoverability (`METRIC-003`), Architecture Health (`VOCAB-007` and `METRIC-005`) і ADR (`ARTIFACT-001`).
