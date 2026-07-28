# Кожен стан має одного власника

## Вступна цитата

> Копія може повідомляти стан. Тільки власник може його вирішувати.

## Історія

Контролер мав шість режимів і забагато істин.

На папері режими були простими. Під час старту пристрій входив у `Boot`. Коли він не міг безпечно працювати, переходив у `SafeIdle`. Після завершення ініціалізації ставав `Ready`. Під час нормальної роботи був `Active`. Під час сервісу міг входити в `Service`. Коли interlock падав або спрацьовувала умова захисту, контролер переходив у `Fault`.

Режим був важливий, бо пристрій керував реальними виходами. У `Active` він міг живити мотор і відкривати технологічний клапан. У `Service` він міг запускати калібрування з guard-умовами, непридатними для production operation. У `SafeIdle` виходи лишалися вимкненими, доки контролер не відновлював достатню впевненість для руху далі. Режим не був ярликом UI. Це була відповідь системи на практичне питання: що цьому контролеру дозволено робити зараз?

Перша реалізація мала runtime state machine у firmware. Команди надходили, preconditions перевірялися, transitions логувалися, виходи змінювалися, а поточний режим публікувався у service interface.

Ця модель недовго лишалася самотньою.

Додали persistent field, щоб контролер пам'ятав, що service work тривав перед restart. Service application кешував режим, щоб техніки могли швидко перепід'єднатися після USB drop. Manufacturing fixture отримав privileged diagnostic command, щоб лінія могла входити в calibration без проходження нормального service workflow. Supervisory controller навчився виводити режим із outputs і telemetry, бо published mode інколи затримувався в busy network.

Кожне доповнення мало причину.

Persistent field допомагав технікам відновити контекст після reset. Service cache робив tool responsive. Fixture bypass економив секунди на кожній одиниці. Supervisor inference дозволяв plant automation реагувати, навіть коли service channel не був під'єднаний. Жодна з цих змін не виглядала як architecture decision у момент внесення. Кожна була локальною зручністю навколо одного meaningful state.

Потім watchdog reset стався під час service calibration.

Firmware перезапустився консервативно і ввійшов у `SafeIdle`. Це була правильна runtime поведінка. Контролер втратив execution context, output state було reset, і state machine мав переоцінити умови перед дозволом operation.

Persistent field усе ще казав `Service`.

Service application перепід'єднався і показав cached `Service` state до того, як контролер опублікував новий режим. Manufacturing fixture усе ще вважав calibration активним, бо diagnostic sequence не отримала clean completion event. Supervisory controller побачив кілька outputs у нормальних ready positions і вивів `Ready`.

П'ять компонентів тепер мали п'ять правдоподібних відповідей.

Firmware відмовив у transition до `Active`, бо був у `SafeIdle`. Service application намагався повернути контролер у `Service`, бо технік не завершив роботу. Fixture повторно надіслав privileged calibration write, бо припустив, що reset перервав communication, а не authority. Supervisor запросив operation, бо outputs виглядали ready. Persistent field знову відновив `Service` після пізнішого reboot, і баг почав здаватися таким, що повертається зі storage.

Логи не брехали. Вони були локальними.

Один log показував firmware, що входить у `SafeIdle` після watchdog recovery. Інший показував service tool, який надсилає `Service`. Fixture log показував повтор calibration command. Supervisor записав, що controller appears ready. Storage показував last saved mode як `Service`. Команда бачила, що зробив кожен компонент. Вона не могла відповісти на головне питання: якому компоненту було дозволено вирішувати поточний operational mode?

Перші запропоновані fixes були знайомими, бо трактували розбіжність режимів як synchronization problem.

Синхронізувати mode flags частіше. Додати retry, коли service application бачить disagreement. Persist every transition immediately. Додати timestamp і нехай newest value wins. Дати кожному actor setter, але задокументувати порядок використання. Додати ще один Boolean `modeValid`. Навчити supervisor знову infer mode, коли reported value виглядає stale.

Вони були привабливими, бо їх можна було призначити локально. Firmware публікує частіше. Service tool retry. Storage пише швидше. Supervisor infer агресивніше.

Жодна зміна не називала authority.

Principal Engineer попросила команду припинити малювати стрілки між копіями і намалювати межу навколо authority.

"Якому значенню дозволено бути неправильним деякий час?" - запитала вона.

Service cache міг бути неправильним. Він мав ставати stale, коли controller публікує новіший transition. Persistent field міг бути старим. Він міг означати boot policy, pending service intent або history, але не runtime truth після watchdog reset. Supervisor inference міг бути корисним: він виявляв, що outputs виглядають ready. Але він не міг вирішити, що controller is ready. Fixture міг мати privilege. Він міг request bounded calibration transition. Він не міг bypass state owner.

Runtime state machine став єдиною authority для current operational mode.

Інші компоненти перестали напряму assign mode. Service tool надсилав `RequestServiceMode`. Fixture надсилав privileged calibration request через той самий transition boundary. Supervisor міг request operation, але не міг перетворити inferred observation на `Ready`. Persistence зберігав boot policy, acknowledged service intent і transition history. Він не володів current runtime mode.

Owner validated transitions. Він перевіряв, чи outputs disabled перед входом у `Service`. Він rejected `Active`, доки recovery incomplete. Він приймав fixture requests тільки через bounded path із тими самими invariants. Він публікував accepted transitions із sequence number і reset generation, щоб observers могли detect stale values. Він записував rejection reasons, щоб service tool міг показати "recovery incomplete", а не вдавати, що command vanished.

Reset behavior теж змінилася. Після watchdog recovery controller входив у `SafeIdle`, завантажував лише persisted inputs, яким реально довіряв, і публікував new transition. Cached UI state став last observation. Fixture мав request calibration again. Supervisor міг report inferred view, але мав treat published mode and generation as authoritative for commands.

Система не стала меншою. Вона стала менш неоднозначною.

Кеші, persistence, telemetry, privileged commands і supervisory observations лишилися. Копії корисні. Змінилася їхня роль: request, observe, remember, infer, display. Не decide current operational mode.

Один стан мав одну authority for change.

## Обговорення

State - це не просто stored data.

Це перша помилка в багатьох ownership discussions. Команда показує на field, table, variable, register або cache, де живе value, і каже: "Ось owner". Іноді цього досить для local implementation detail. Для meaningful state - ні.

Meaningful state має наслідки. Operational mode змінює, які outputs можуть бути enabled, які commands valid, які alarms важливі, який recovery path має запускатися і яке пояснення отримує technician. Він має valid values, valid transitions, invariants, history і failure behavior. Value важить, бо система робитиме різні речі залежно від того, у що вона вірить.

Тому Every State Has One Owner (`LAW-001`) сильніше за "keep one copy". Копія може зберігати value. Owner вирішує, чи value valid, чи transition allowed, що робити в uncertainty і як interpreted інші representations.

Owner - це semantic authority.

Це не автоматично memory address, де value stored. Не module, який last wrote field. Не thread, що зараз executing. Не database row, cache, UI, service tool, fixture, consumer team або компонент із найзручнішим setter.

Owner - це boundary, який може відповісти:

- Чи valid цей transition?
- Які invariants мають виконуватися перед acceptance?
- Хто може request transition?
- Що означає rejection?
- Яке value authoritative now?
- Що observers мають робити зі stale або conflicting copies?
- Що відбувається після reset, standby switch або handoff?

Ці питання architectural, бо вони формують behavior навколо state. Код, який зберігає current value, - лише частина відповіді.

Копії не вороги.

Embedded systems часто потребують багато representations одного state. UI потребує display value. Service application потребує recent observation. Supervisor може потребувати telemetry mirror. Boot path може consult persisted policy. Hardware може expose shadow state. Gateway може keep last reported value, доки device sleeps. Test fixture може hold expected state, чекаючи response.

Law не забороняє копії. Він питає, чи кожна копія має declared role.

Це value authoritative, requested, applied, observed, reported, last-known, persisted, cached, derived чи inferred? Команді не потрібна taxonomy для кожного value. Їй потрібна достатня відмінність, щоб не трактувати old copy, desired outcome і accepted transition як той самий факт.

Service application's cached `Service` mode був корисний як last observation. Він став небезпечним, коли tool treated it as current authority. Persisted `Service` field був корисний, якщо означав "service work was interrupted" або "resume service workflow if the owner accepts it". Він став небезпечним, коли restored runtime mode by assignment. Supervisor inference був корисний як diagnostic signal. Він став небезпечним, коли symptoms turned into truth.

Це Hidden State (`SMELL-004`) у поширеній embedded формі. State affects behavior, але source of authority не видно через clear owner, interface або model. Кожен component може explain local value. System не може explain which value should win.

Multiple writers створюють policy випадково.

Коли кілька components можуть assign same meaningful state, кожен writer носить фрагмент transition policy. Service tool знає, коли technician wants service. Fixture знає, коли manufacturing wants calibration. Supervisor знає, коли outputs appear ready. Storage знає last saved value. Firmware знає current interlocks.

Ці факти не еквівалентні. Request is not a transition. Persisted value is not runtime authority. Inferred condition is not permission. Якщо кожен component отримує setter, system більше не має one transition policy. Вона має кілька local policies, що конкурують через timing.

Саме тому raw setters дорогі. Setter відповідає "яке value записати?" Intent-level command ставить краще питання: "який outcome requested, і чи може owner accept it now?"

`RequestServiceMode` відрізняється від `mode = Service`. Command carries intent. Owner перевіряє outputs, calibration, recovery, privilege і current mode; accept, reject, publish і explain.

Inference - subtle form of ownership.

Supervisor міг infer `Ready` з outputs і telemetry. Це не дурість. Operators часто потребують useful interpretations, коли direct communication delayed. Але inferred value стає небезпечним, коли починає control behavior як authoritative.

Global Configuration (`ANTIPATTERN-003`) часто створює ту саму проблему. Broad mode flag починається як convenient configuration value, а потім розповзається в logging, calibration, connectivity, power behavior і service tooling. Незабаром зміна одного setting змінює unrelated modules, бо configuration стала shared state authority без scope, lifecycle або validation.

One owner не означає one participant.

Багато callers можуть request change. Багато adapters можуть receive commands. Багато functions можуть participate in implementing transition. Багато hardware operations можуть бути потрібні перед safe publish. Replicas і snapshots можуть існувати. Concurrency може вимагати serialization, arbitration або stronger distributed protocol.

Law не каже, що тільки одна function може ever write memory. Він каже, що one authority must decide valid value and transitions for the state at the given time and scope.

Scope matters.

During boot bootloader може own update mode. After handoff application може own runtime operational mode. During firmware-update recovery component може own narrower update state. In active-standby pair active controller може own current control state, standby keeps replica. During standby switch ownership may transfer.

Такі designs comply with the law, якщо transfer explicit, ordered і mutually exclusive at relevant scope. Вони violate law, коли обидві сторони вірять, що можуть decide same state at same time, або observers не можуть tell which authority is active.

Recovery requires choosing authority, not merging guesses.

Найважчі ownership bugs часто з'являються після reset, reconnect, partial failure, controller handoff або interrupted service. Representations disagree for understandable reasons. Якщо recovery rule - "merge the best-looking values", system asks copies to vote on truth. Newest-timestamp-wins має ту саму пастку: new value не обов'язково authoritative value.

Кращий recovery rule starts from ownership. Runtime state machine входить у conservative mode і re-establishes authority. Він може consult persisted boot policy, read acknowledged configuration, use hardware observations, publish recovery transition і reject requests until invariants hold. Але old cache, inferred state або persisted last value не assign current operational mode directly.

State ownership should be discoverable.

Discoverability (`METRIC-003`) - це не decorative documentation. Для meaningful state repository має дати знайти owner, valid values, invariants, commands, published observations, persistence semantics, reset rule, handoff rule і tests, що prove invalid transitions rejected.

ADR (`ARTIFACT-001`) добре фіксує ownership decision, коли вона affects architecture, cost або reversibility. Event Catalog (`ARTIFACT-005`) може record events that publish accepted transitions, producer, consumers, ordering assumptions і failure behavior. Важлива не ceremony, а те, щоб наступний engineer не виводив authority із найзручнішого setter.

Практична вигода проста: callers request, owner decides, observers observe, caches remember with freshness limits, persistence stores what it owns, derived values explain their derivation, recovery chooses authority instead of merging guesses.

## Інженерний принцип

Для кожного meaningful state назвіть одну authority, яка validates its value and controls its transitions. Інші components можуть request, observe, cache, persist, replicate або derive that state, але не мають ставати competing sources of truth.

Принцип reviewable через питання:

1. Який exact state обговорюється?
2. Що цей state означає для system або product?
3. Які values valid?
4. Які invariants визначають safe або correct transitions?
5. Хто owns the transitions?
6. Хто може request a change?
7. Які representations є observations, caches, persistence або derivations?
8. Що відбувається після reset, reconnect, partial failure або stale restoration?
9. Як stale/conflicting observations detected?
10. Як ownership transferred across lifecycle boundaries?
11. Де decision recorded, щоб інший engineer міг його знайти?

Trade-off: one authority часто потребує more explicit interfaces. Callers можуть потребувати commands замість setters. Observers можуть потребувати versions або generations. Persistence може потребувати narrower responsibility. Fixtures можуть потребувати privileged paths, які still respect invariants. Ці costs real.

Альтернатива гірша: every copy carries a little policy, every repair path becomes a writer, and recovery becomes negotiation among stale values.

## Архітектурна вправа

### Простежте один стан до одного власника

Оберіть meaningful state із системи, над якою працюєте. Не беріть trivial local variable. Оберіть state, whose value changes behavior: operational mode, configuration state, calibration state, connection state, update state, safety interlock state, entitlement state або інший value with consequences.

Дайте короткі відповіді:

1. Яка exact name and scope цього state?
2. Що він означає для product або system?
3. Які values valid?
4. Які invariants must always hold?
5. Які transitions valid?
6. Який boundary зараз decides whether a transition is accepted?
7. Які components можуть currently write or repair the value?
8. Які components may request a change?
9. Які components observe it?
10. Де він persisted?
11. Які caches, UI projections, telemetry mirrors або derived values exist?
12. Які components infer the state from symptoms?
13. Що відбувається після reset, reconnect, standby switch або partial failure?
14. Коли ownership can transfer і як overlap prevented?
15. Які докази identify the owner?
16. Які duplicate writers або unofficial owners слід remove?
17. Які commands request change і які observations publish accepted state?
18. Які tests prove invalid transitions are rejected?
19. Який ADR або existing artifact records the decision?

Завершіть питанням:

Яка копія цього стану зараз поводиться як owner, не будучи так названою?

## Нотатник Principal Engineer

- Копії не є owners.
- Setter не є authority.
- Recovery потребує named truth.

## ADR

### Chapter ADR: Make the Device Mode State Machine the Sole Authority for Operational Mode

### Context

Поточний operational mode industrial controller duplicated across runtime state machine, persistent storage, service tooling, fixture logic і supervisory inference. Кілька components можуть assign або repair mode. Watchdog reset, interrupted service і reconnect sequences expose disagreement between `SafeIdle`, `Service`, and inferred `Ready`.

Validation rules inconsistent. Деякі paths check interlocks and recovery state. Інші write raw mode value, бо assume they restore truth. Logs show local actions but cannot reliably explain which component made the authoritative decision.

### Decision

Зробити controller runtime state machine єдиною authority for current operational mode.

Замінити external raw mode setters intent-level commands, such as `RequestServiceMode`, `EnterSafeIdle`, and fixture calibration requests routed through the same transition boundary. Validate preconditions and invariants in the owner. Publish accepted transitions with sequence, generation, or transition identity sufficient for observers to detect stale values.

Define persistence as input, policy, or history according to its own responsibility, not as a second runtime owner. Define fixture privilege through bounded commands rather than bypass assignment. Document reset recovery and any ownership handoff so only one authority controls current mode at a given time and scope.

### Consequences

Operational-mode invariants now have one reviewable home. Invalid commands can be rejected with explainable reasons. Service tooling, fixtures, supervisors, and UI surfaces can distinguish requests and observations from authority. Reset behavior becomes clearer because recovery starts by re-establishing the runtime owner instead of merging stale guesses. Tests can exercise invalid transitions at one boundary.

This decision requires migration work. Existing writers must be converted to commands. Service tools may need compatibility handling while older firmware still exposes raw setters. The owner may need queueing or serialization around concurrent requests. Observers need version, generation, or transition identity where stale values matter. Ownership handoff requires explicit design. The state-machine boundary must stay focused so it does not become a god object for every operational concern.

### Alternatives Considered

Keep multiple writers and synchronize them more frequently. Це зберігає ambiguity і лише швидше рухає conflicting values.

Let the newest timestamp win. Це може бути useful for observations, але newer value may still be a newer guess rather than authoritative transition.

Make persistent storage authoritative at all times. Це зробило б reset simple, але treated stored value as runtime truth even when current interlocks, outputs, or recovery state disagree.

Infer current mode from outputs. Це допомагає diagnose disagreement, але turns symptoms into authority.

Use a distributed ownership protocol. Це може бути appropriate for systems where state authority is genuinely distributed, but this controller has one runtime authority for current operational mode. Broader protocol would add complexity without solving the immediate ownership gap.

## Коментар редактора

Chapter 7 opens Part II by turning a question that appeared earlier into a law. Chapter 3 used stale state to show how better questions expose ownership gaps. Chapter 4 used ownership as responsibility for closing an engineering outcome. This chapter uses ownership in a narrower architectural sense: authority over a meaningful state and its valid transitions.

This distinction matters for the rest of the book. Later chapters use state ownership as a premise. API promises, dependency direction, time, simplicity, evidence, product configuration, observability, and legacy recovery all become harder when meaningful state has several unofficial authorities.

The PEAK concepts carrying this chapter are Every State Has One Owner (`LAW-001`), Hidden State (`SMELL-004`), Global Configuration (`ANTIPATTERN-003`), ADR (`ARTIFACT-001`), Event Catalog (`ARTIFACT-005`), and Discoverability (`METRIC-003`). They are enough. The chapter does not need a new artifact or vocabulary term to teach the law.
