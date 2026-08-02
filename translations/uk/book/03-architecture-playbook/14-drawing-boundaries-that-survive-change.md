# Проведення меж, які витримують зміни

## Вступна цитата

> Межа — це не місце, де поділено code. Це місце, де responsibility, authority і knowledge перестають непомітно перетинатися.

## Історія

Radio wrapper виглядав чисто на diagram.

Product був embedded field controller. Він збирав data з локальних devices, надсилав command acknowledgements до supervisory system і використовував radio module, коли wired connectivity була unavailable. Перша версія мала одного radio vendor, один transport, одну RTOS task, один service tool і одну product behavior, яку всі розуміли: keep controller connected when radio is present, report link state, send product messages і recover without losing what product promised upstream.

Team зробила розумну річ: не дала кожній feature напряму викликати vendor driver. Вона створила radio manager. Спершу це відчувалося як boundary.

Product code викликав `RadioManager_Send`. Manager реєстрував vendor callback, owning driver initialization, socket address, vendor channel handle і retry loop навколо відомих driver errors. Service tool, UI і tests проходили через manager. Diagram мав один box з label «radio».

Ніхто не був careless. Product був small, vendor driver worked, schedule тиснув. Один manager був кращим, ніж direct driver headers everywhere.

Потім details почали travel. Product state machine зберіг vendor connection state. UI перевіряв vendor `channel busy` error. Persistence record зберігав channel identifier. Command handler трактував raw packet types як product meanings. Diagnostics task logged driver retry reason codes. Network service learned socket address format. Service tool sent vendor control command for link reset. Tests mocked vendor callback signature. Timing assumption from driver увійшов у product timeout.

Manager усе ще був там. Leak теж.

Platform Leakage (`SMELL-005`) became normal product language. HAL Everywhere (`ANTIPATTERN-002`) не виглядав як raw register reads у кожному file; він виглядав respectable: vendor status values, driver packet shapes, RTOS event bits, socket details і service commands spreading through product decisions.

Trigger став second radio family. User-visible behavior мала лишитися same: report link state, accept product messages, send outbound messages, recover after loss, expose useful diagnostics. Але second radio мав different control protocol, connection states, completion behavior, retry codes і no equivalent for one service command.

Estimate sounded small: «We already have a manager. We'll add an adapter.»

Adapter edit touched manager, UI status text, persistence, tests, diagnostics, command handler, recovery і commissioning path, який bypassed manager. Work уже не був «add an adapter». Він став «find every place where product had learned first radio».

Це був Silent Coupling (`SMELL-001`). Real dependency graph не був represented by diagram. Teams coordinated by memory. Tests encoded assumptions outside product contract. Driver change reached UI, storage, command handling, diagnostics, recovery, service tooling і release testing without obvious call path.

Hidden State (`SMELL-004`) made it worse. Manager мав own view of link state. Product state machine stored copied vendor state. UI cached derived state. Service tool kept last raw driver status. Callback could mutate state during recovery before product owner accepted transition.

Manager став polite version of Manager Mania (`ANTIPATTERN-004`): він coordinated behavior without owning product decision. Коли запитали, чи controller may accept outbound messages during partial link recovery, answer lived in cooperation among manager, state machine, adapter і tool, not in one owner.

Перші proposals tried to preserve wrapper shape: vendor flag, more methods, universal driver interface, duplicate product logic, generic event bus, renamed statuses, conditional compilation, one platform service, another abstraction layer або direct HAL access for exceptional paths.

Жодна ідея не була universally foolish. Але жодна не відповідала на architecture question.

Principal Engineer переформулював work:

> Which product decision must remain stable, which integration details vary, and where should translation occur?

Answer was not «radio». Radio was a device category, not yet a boundary.

Stable product decision was controller radio control behavior: when link is available, which commands may be sent, what completion means, how retries affect promises, what recovery may change, and what diagnostics support needs.

Before another wrapper, decision needed product vocabulary. Product did not need `vendor state 7`; it needed link unavailable, ready to send, waiting for completion, temporarily congested, failed with retry scheduled, product-visible loss, or recovery state blocking new commands.

Team drew intended boundary around product-owned control behavior. Product owner owned authoritative radio control state, honoring Every State Has One Owner (`LAW-001`). Adapter could observe driver state, hold mechanism-specific handles і translate completion. It could not mutate product truth through callback.

Контракт став явним because Every API Is a Promise (`LAW-002`): product-level commands, accepted inputs, observable outcomes, completion semantics, failure categories, retry ownership, recovery handoff і lifecycle constraints.

Dependency direction changed. Runtime still had callbacks, queues and asynchronous completion, but design knowledge stopped pointing from product policy into vendor mechanism. Adapter depended on product-owned contract; product code no longer depended on vendor headers, RTOS bits, packet types, socket structures або driver retry meanings.

That made Every Dependency Is a Decision (`LAW-007`) visible. Vendor still mattered; boundary did not pretend hardware reality disappeared. It constrained where imported knowledge could spread.

Translation moved to the edge: identifiers into product link identities, connection states into outcomes, raw packet types into product commands or unsupported input, driver errors into product failure categories, callbacks into product-owned completion events, diagnostics into product and adapter views.

Translation was not just renaming. One old vendor status meant both «not connected» and «driver is starting again after reset». Product had collapsed both into «link down». Second radio separated them. Team had to decide product meaning and recovery ownership. That was boundary decision, not type conversion.

Team removed back channels. Commissioning stopped direct platform reset. UI stopped reading raw driver status. Service tool stopped sending vendor commands as product commands. Tests stopped mocking vendor callbacks for product behavior. Diagnostics stopped using raw driver codes as main product explanation.

Migration was deliberately small: outbound product message submission. Team defined product command, completion meanings, allowed states, retry ownership, adapter translation, tests і diagnostics. They measured current Change Radius (`VOCAB-001` and `METRIC-001`) and compared it with desired surface after product contract.

ADR (`ARTIFACT-001`) recorded where product authority lived, what vocabulary could cross, what translation edge owned, which bypasses had to close, how migration would proceed, and what costs team accepted.

Radio wrapper did not disappear. It became less important than the question it had failed to answer: what must this part of the system be allowed to know?

## Обговорення

Architecture boundary — intentional separation of responsibility, authority and knowledge. Це stricter than module, interface, layer, process, library, service or deployment boundary. Those structures can implement boundary; they do not prove one exists.

Start boundary work by naming the decision. «Radio» is too broad. Useful question: which product decision must remain coherent when mechanism changes?

boundary separate reasons to change. Product policy, hardware integration, vendor protocol, UI, persistence, diagnostics, manufacturing, support tooling and release compatibility have different sources of change. Durable boundary groups decisions that must move together and separates decisions that should not be forced together.

Granularity matters. Too broad boundary becomes God Module (`ANTIPATTERN-001`). Too narrow boundary creates forwarding surfaces, fragmented ownership and synchronization cost. Right size is smallest truthful separation that protects the decision at stake.

Product vocabulary belongs with product authority. Platform terms may be real and unavoidable, but if they decide UI behavior, state transitions, persistence schema, command semantics, support procedures or release compatibility, platform has become product authority.

Translation at boundary preserves meaning while changing vocabulary. It converts identifiers, states, errors, lifecycle states, completion signals, data representation, timing expectations, ownership rules and diagnostics. It should neither collapse real differences into one generic status nor expose every mechanism detail.

Authority is hardest to fake. Callbacks, events, queues, caches, snapshots, persistence records, diagnostics and service tools may observe or request, but they must not silently become competing writers of product truth.

Dependency direction is not runtime flow. Driver may call product completion handler at runtime; this does not mean product policy depends on driver. Knowledge dependency asks which side must understand the other's concepts to compile, test, change and explain behavior.

Back channels reveal real architecture. Rare HAL calls, debug commands, test hooks, persistence fields and hidden subscriptions show what the system relies on when intended contract is inconvenient.

A boundary survives change when expected change can be absorbed on one side without forcing unrelated decisions to move or leak. It does not make replacement free or contracts eternal. Durability means boundary remains truthful under expected change.

Chapter 14 gives later Part III practices a concrete object: where authority lives, what vocabulary crosses, which dependencies are contained, which back channels remain, and what change the boundary should survive.

## Інженерний принцип

Проводьте межі навколо product decisions і coherent reasons to change. Keep authority, vocabulary and dependency direction explicit, and translate volatile mechanisms at the edge.

Use this principle as звичка перегляду:

1. What product decision does this boundary protect?
2. Who owns authoritative state?
3. Which product terms are allowed to cross?
4. Which platform terms must be translated?
5. Which dependencies point toward stable product meaning?
6. Which runtime calls, callbacks, events, queues or messages are only mechanisms?
7. Which completion, failure, retry and recovery meanings are promised?
8. Which back channels bypass intended contract?
9. Which reasons to change belong on each side?
10. What cost does boundary add?
11. What expected change should boundary absorb?
12. What evidence shows boundary is truthful?

Goal is not making every mechanism replaceable. Goal is keeping product authority from being accidentally owned by first mechanism.

## Архітектурна вправа

### Перемалюйте одну leaky boundary

Choose one integration boundary: driver wrapper, service client, protocol adapter, manufacturing path, diagnostic interface, payment integration, storage connector, device bridge or subsystem API.

Write short answers:

1. What product capability does this boundary support?
2. What product decision should remain stable when mechanism changes?
3. Who owns authoritative state?
4. Which modules, tasks, processes, tools, tests and support paths touch it today?
5. What contract do callers believe exists?
6. Which product vocabulary appears at boundary?
7. Which platform, vendor, transport or tool terms cross boundary?
8. Which side depends on other's concepts at design or compile time?
9. Which direction do calls, callbacks, events, queues or messages flow at runtime?
10. Which snapshots, caches, persistence records or diagnostics can become hidden state?
11. Which completion, failure, retry and recovery meanings are unclear?
12. Which back channels bypass intended contract?
13. Which reasons to change belong on product side?
14. Which reasons to change belong on mechanism side?
15. What realistic future change would test boundary?
16. What is current affected surface if that change happens?
17. What product-owned contract would reduce unrelated edits?
18. What translation belongs at edge?
19. What migration path moves one product path first?
20. What tests and diagnostics would prove boundary is being used?
21. Where should ADR live?

End with one small reviewable boundary decision: protected product decision, owner of authoritative state, product terms allowed to cross, mechanism terms translated at edge, first back channel to remove, first path to migrate, and evidence that will show Change Radius changed.

## Нотатник Principal Engineer

- boundary separates decisions, not files.
- Translation belongs where vocabularies meet.
- Back channels reveal real architecture.

## ADR

### Chapter ADR: Place Radio Integration Behind a Product-Owned Control boundary

#### Context

Product began with one radio vendor and radio manager intended to isolate hardware. Over time vendor states, channel identifiers, callbacks, packet types, retry codes, socket details, RTOS bits, timing assumptions and service commands spread into UI, product state, persistence, diagnostics, command handling, tests and support tooling.

Second radio family must preserve same user-visible behavior with different integration details. Current manager is wrapper, not durable boundary. Product state is split across product state, manager state, UI cache, service tool status and callback mutation. Recovery ownership unclear. Direct platform bypasses exist.

#### Decision

Define product-owned radio control boundary. boundary owns product-level radio behavior: link availability, command acceptance, completion meaning, failure categories, retry ownership, recovery handoff, lifecycle, diagnostics and support-visible outcomes.

Product code uses product vocabulary. UI, persistence, command handling, diagnostics, tests, network services and service tooling depend on product commands and outcomes, not vendor states, raw packets, driver retry codes, RTOS bits, socket structures or service commands.

Assign authoritative radio control state to product owner. Driver callbacks and adapter events report observations and completions; they do not mutate product truth outside owner.

Place vendor operations in adapters. Adapters translate identifiers, status values, packet shapes, errors, completion, timing assumptions and diagnostics at edge. Preserve asynchronous completion without exposing vendor callback signatures as product contract.

Remove direct platform bypasses from product paths. Migrate outbound product message submission first. Record current and desired Change Radius for second radio integration.

#### Consequences

Product semantics become stable across radio families. Vendor knowledge is contained. State authority explicit. Tests target product behavior separately from adapter translation. Diagnostics distinguish product outcomes from radio-specific causes.

Decision adds translation code, adapter tests, migration work and temporary coexistence. Hardware constraints remain real; they are contained and named, not erased.

#### Alternatives Considered

- Extend current manager. Fast, but keeps product authority hidden.
- Create universal driver interface. Risks flattening different completion, retry and recovery meanings.
- Duplicate product logic per radio family. Preserves details but lets product behavior drift.
- Use conditional compilation throughout. Valid only at narrow hardware edge.
- Introduce generic event bus. Events do not assign authority or translate vocabulary by themselves.
- Keep direct platform access for exceptions. Useful for bring-up, dangerous as product behavior.
- Replace subsystem in one rewrite. Raises risk before boundary is proven.
- Postpone boundary work. Lets first vendor model embed deeper.

## Коментар редактора

Chapter 14 opens Part III by moving from knowing laws to practicing architecture. It has no primary PEAK concept by design. It uses Platform Leakage (`SMELL-005`), HAL Everywhere (`ANTIPATTERN-002`), Every State Has One Owner (`LAW-001`), Every API Is a Promise (`LAW-002`), Every Dependency Is a Decision (`LAW-007`), Silent Coupling (`SMELL-001`), Hidden State (`SMELL-004`), Manager Mania (`ANTIPATTERN-004`), God Module (`ANTIPATTERN-001`), Change Radius (`VOCAB-001` and `METRIC-001`) and ADR (`ARTIFACT-001`).

The reader-facing move is simple: do not ask whether system has wrapper. Ask what wrapper still allows the rest of product to know.
