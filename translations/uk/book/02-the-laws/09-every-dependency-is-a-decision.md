# Кожна залежність — це рішення

## Вступна цитата

> Dependency не стає безкоштовною лише тому, що перший call compiled.

## Історія

Radio decision виглядало практичним.

Product потребував new wireless module для next controller revision. Hardware choice звужувався, pilot line date мав значення, і team потребувала initialization, channel setup, packet handling, power-state transitions, retries, diagnostics і enough compliance behavior, не витрачаючи whole release на writing radio stack.

Vendor надав software kit для radio. Він supported hardware, мав example initialization code, handled protocol details, moved packets on evaluation board і included painful but useful errata: timing around wake, retry sequence after channel loss і narrow compiler version range.

Використати його було not foolish.

Building complete stack internally затримав би release і move risk into area with less evidence. Selecting another part reopened би hardware work. Delaying product, доки every replacement risk was understood, protected би architecture in theory while failing product in practice.

Firmware team зробила reasonable compromise: vendor kit behind thin wrapper. Product code called wrapper. Лише radio driver directory included vendor headers. Short ADR казав, що team would use kit for first release and preserve option to replace later. Review був brief, бо boundary looked obvious.

Для first release цього було enough.

Потім dependency spread.

Vendor kit expected radio work from one task context. Callbacks приходили from that context і carried buffers owned by kit until callback returned. Wrapper preserved that shape. Product code learned vendor buffer format. Supervisory task learned vendor errors. Logging copied vendor reason names. Manufacturing scripts waited for vendor ready event. Service tool displayed same error categories. Tests mocked wrapper, але used vendor-style errors. Production fixture used vendor diagnostic sequence. Release engineering pinned compiler version.

Ніхто не вирішував «let vendor software kit define product». Product learned it anyway.

Next hardware revision exposed the real surface. New kit мав similar functions, але callback context, buffer ownership, error model, tooling support, calibration readiness, compiler assumptions, tests, scripts, service messages і field compatibility did not match old assumptions.

"It is behind the wrapper" was partly true. It hid headers and names. It did not isolate behavior.

Principal Engineer попросив team draw the real dependency surface: task context, callback ordering, buffer ownership, error meanings, retry policy, power-state behavior, logging names, test harness assumptions, calibration sequence, service-tool messages, compiler support, release cadence і field compatibility.

Diagram виглядав less like driver boundary and more like product decision.

Команда змінила work from "swap library" to "name and contain commitments." Vendor kit лишився, бо solved real risk. Але product boundary змінилася. Integration layer тепер naming product-owned outcomes: radio ready, send accepted, send completed, receive available, radio unavailable, safe to retry, unsupported, permanently failed. Vendor errors translated before leaving integration. Callback context normalized. Buffer ownership defined in product terms. Tests rewritten around product contract. Fixture waited for product-level calibration readiness. Service tooling displayed product meanings and kept vendor detail only as diagnostic context. Compiler and kit version became owned release assumption.

ADR rewritten. Він більше не казав лише «use vendor kit behind wrapper». Він казав, які commitments team accepted, where dependency may appear, who owns updates, what evidence proves boundary і what triggers replacement.

System не став independent of vendor kit. Він став honest about depending on it.

Ця honesty changed architecture more than wrapper had.

## Обговорення

Dependency — це будь-яка external або internal thing, на чию behavior system relies і яку cannot freely change alone.

Це ширше за imported code: library, service, protocol, hardware part, file format, build image, compiler, release tool, production fixture, test harness, support procedure, internal platform. If system relies on it and cannot change it freely, decision carries architectural cost.

Every dependency commits system to behavior, failure modes, lifecycle constraints, ownership boundaries і replacement cost.

Це не означає, що dependencies bad. Radio kit reduced schedule risk і brought hardware knowledge. Many good decisions depend on other people's work. Law не «avoid dependencies». Law — «know what you are accepting».

First mistake — treating dependency choice as implementation detail, бо first integration local. Wrapper lived in one directory, але behavior moved through product: callback context, error meanings, logging language, compiler support, calibration events.

Це Silent Coupling (`SMELL-001`): hidden dependency affects behavior, але не є explicit contract. Team thinks product depends on wrapper. In practice, він depends on vendor timing, error vocabulary, memory ownership і lifecycle.

Dependency use і dependency spread — різні речі.

Using dependency може бути reasonable. Dependency spread трапляється, коли dependency concepts escape containment boundary: product errors become vendor errors, tests assert vendor callback order, manufacturing waits for vendor event, support docs use vendor names, release planning follows dependency support horizon without owner.

Wrapper може допомогти. Але це not proof.

Syntactic isolation hides names, headers, types і call shapes. Semantic isolation питає, чи consumers depend on product-owned contract або underlying dependency behavior. Якщо wrapper exposes vendor errors, callback context, memory rules, ordering і categories, architecture remains dependent on vendor semantics.

Replacement cost includes more than swapping code: contract redesign, product migration, data migration, tests, fixture updates, operational retraining, support documentation, shipped-version compatibility, confidence rebuilding, release coordination, compiler updates, hardware qualification і customer migration risk.

"We can swap it later" deserves follow-up: what exactly would have to change if we did?

Direct dependencies visible в imports, build files, service calls, protocol choices, hardware selections, interface definitions, process handoffs і recorded decisions. Transitive dependencies arrive through other dependencies. Transitive не означає, що another team owns consequence; це означає, що commitment is one step farther from first choice.

Dependency direction preserves architectural control, коли product code depends on stable product contract, narrow integration layer depends on volatile vendor component, і product owns vocabulary, errors, states і lifecycle. Bad direction lets volatile component define product.

Failure behavior теж imported: unavailable states, latency, errors safe to retry, permanent failures, resources exhausted, version skew, support horizon, hardware degradation, service changes, tool support end.

Lifecycle — part of dependency. Selection, adoption, integration, update, support, deprecation, replacement і removal need owners, коли dependency material. Removal означає, що consumers no longer depend on behavior, tests no longer encode it, tools no longer assume it, manufacturing no longer waits for it, support no longer explains it.

Не кожна dependency needs same process. Small isolated utility with obvious behavior and cheap replacement needs little ceremony. Material dependencies need decision record, containment і discoverable owner.

Discoverability (`METRIC-003`) matters, бо dependency decisions age quietly. ADR (`ARTIFACT-001`) — good home for material dependency decision: why chosen, alternatives, imported behavior, update owner, limitations, replacement trigger.

Practical standard: deliberate dependencies, чиї commitments understood and proportionate to their value.

## Інженерний принцип

Name the commitment before accepting the dependency. Якщо вона can shape behavior, failure, lifecycle або replacement cost, record the decision and contain the spread.

Питання для review:

1. Яку проблему розвʼязує dependency?
2. Якого вона типу: code, service, protocol, hardware, tool, process чи platform?
3. Хто consumes it directly?
4. Хто consumes it transitively?
5. Яку behavior ми імпортуємо?
6. Які failures входять у нашу system?
7. Які vocabulary, errors, timing, ownership або lifecycle assumptions можуть leak?
8. Яка boundary тримає product semantics під product control?
9. Хто owns versions, updates, support і deprecation?
10. Чого replacement реально вимагатиме?
11. Які докази показують, що replacement plausible?
12. Яка подія trigger update, replacement або removal?

Суть не у формі. Суть у тому, щоб локальна зручність не стала architecture непомітно.

## Архітектурна вправа

### Простежте реальну вартість однієї залежності

Оберіть real dependency: library, service, hardware part, protocol, build tool, test fixture, file format, release process, or internal platform.

1. Що це за dependency?
2. До якої category вона належить?
3. Яку проблему вона розвʼязує?
4. Які components consume it directly?
5. Які components, tests, tools, fixtures або procedures consume it transitively?
6. Яку behavior вона імпортує?
7. Які failures вона імпортує?
8. Які runtime assumptions вона приносить?
9. Які build, release або support assumptions вона приносить?
10. Яка vocabulary або error meanings leak into product?
11. Яка data, protocol, storage або manufacturing behavior depends on it?
12. Хто owns updates?
13. Хто owns compatibility with existing releases?
14. Який support horizon важливий?
15. Які докази показують, що dependency contained?
16. Чого replacement вимагатиме beyond code?
17. Якою буде replacement cost in tests, tooling, operations, support і confidence?
18. Яка condition trigger update, replacement або removal?
19. Де recorded decision?

Завершіть питанням:

Яка частина system зараз depends on this dependencyʼs behavior, вважаючи, що depends only on your boundary?

## Нотатник Principal Engineer

- A dependency is a decision about future change.
- A wrapper helps only when callers depend on wrapper's contract.
- Replacement cost is real when someone can describe path out.

## ADR

### Chapter ADR: Adopt the Vendor Radio Software Kit Behind a Bounded Integration Layer

### Context

Product needs radio support для selected hardware in next controller revision. Vendor radio software kit provides working initialization, protocol handling, diagnostics і hardware-specific guidance, що reduce delivery and integration risk for first release.

Kit imports commitments: callback model, memory ownership, error meanings, retry behavior, compiler support, release cadence і diagnostic assumptions can spread into product code, tests, manufacturing, service tools і support procedures, якщо boundary too thin.

### Decision

Adopt vendor radio software kit, але constrain direct use to one bounded radio integration layer.

Define product-owned radio contract для readiness, send acceptance, send completion, receive behavior, unavailable states, failures safe to retry, unsupported states і permanent failures. Normalize vendor errors into product meanings before leaving integration layer. Normalize callback context і buffer ownership into product terms. Prohibit new direct vendor kit use outside integration boundary.

Add contract tests around product-owned behavior і integration tests around actual kit. Keep manufacturing, service tooling, logging і support procedures aligned to product meanings. Record supported kit versions, compiler assumptions, update ownership, support horizon і exit triggers.

### Consequences

Product може use vendor kit, не дозволяючи vendor semantics випадково стати product model. Delivery risk reduced. Replacement thinking more realistic. Tests check product contract first and vendor integration second. Upgrade decisions have owners.

Work remains: integration layer maintenance, careful translation of errors/lifecycle, contract and integration tests і unavoidable deep hardware behavior.

### Alternatives Considered

Build complete radio stack internally. More control, але delayed release.

Use vendor kit directly throughout product. Fastest at first, але vendor vocabulary and lifecycle define product behavior.

Delay product until all replacement risks solved. Protects optionality in theory, але ignoring current product commitment.

Select another radio vendor. Reopens hardware and qualification і introduces another dependency decision.

Create fully generic radio abstraction. Це likely unused flexibility before real variation known.

Avoid integration until every exit path cheap. Це makes replacement easy only by not shipping product.

## Коментар редактора

Chapter 9 розширює boundary з Chapters 7 і 8. Dependency decisions легко помилково класифікувати як implementation choices; cost може проявитися у failure behavior, release cadence, tests, manufacturing, service, support, hardware qualification і replacement planning.

PEAK concepts цього chapter: Every Dependency Is a Decision (`LAW-007`), Silent Coupling (`SMELL-001`), Change Radius (`VOCAB-001`), ADR (`ARTIFACT-001`) і Discoverability (`METRIC-003`). Їх достатньо. Chapter 10 візьме один imported commitment — time — і дасть йому власний law.
