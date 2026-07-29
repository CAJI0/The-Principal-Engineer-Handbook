# Конфігурація, варіанти і продуктові лінійки

## Вступна цитата

> Flag дешевий, доки комусь не треба пообіцяти, що він означає.

## Історія

Команда називала це easy variant. Support пізніше назвав це The Variant That Was Just a Flag.

Це був той самий industrial controller з pilot build. Продукт уже керував pumps у трьох environments, які виглядали схоже, але поводилися інакше після installation. Перший package обслуговував standard industrial sites. Другий package додав дешевший radio module і трохи інший service-tool flow. Запит на третій package просив той самий controller, інший pressure range, licensed remote-control capability і довший protocol timeout, бо gateway повільно прокидався після power loss.

Ніхто не хотів product-line architecture project. Команда щойно пережила prototype-to-product transition і manufacturing/field reality. Product уже здавався чеснішим: board-revision handling був stable, manufacturing provisioning defined, support бачив product-level diagnostics, release мав достатню packaging discipline.

Тому перший instinct був practical: «Can we add one more flag?»

Перші два packages справді shipped that way. Hardware revision flag, region behavior flag, licensed feature flag, customer protocol timeout, manufacturing-mode flag, hidden service-tool option, debug flag left in production, build define for cheaper radio, field override in configuration file. Recovery behavior також залежала від package: один міг recover over service link, дешевший потребував local cable.

Кожен flag мав story і виглядав розумно сам по собі. Разом вони стали product line.

Manufacturing дало перше warning: station selected regional package, але tested wrong radio behavior, бо cheaper module selected by build define, not product package record. Unit пройшов electrical test і provisioning, але failed customer installation, бо service tool expected standard radio capability. Manufacturing engineer сказав, що station used package in order. Firmware engineer сказав, що radio module was build variant. Support запитав, яке джерело authoritative. Швидкої відповіді не було.

Друге warning прийшло від update package. Update assumed default configuration for standard package. Для regional package це було wrong. Firmware accepted valid package id. Service tool reported success. Unit restarted into legal firmware configuration, unsupported for customer. Configuration file казав одне. Package label - інше. Service tool - третє. Support script - четверте.

Третє warning прийшло від licensed remote-control capability. Firmware flag, service-tool button, customer package spreadsheet і release package не збігалися. Technician міг бачити button; device rejected command. `unsupported operation` було true but useless. Support не міг сказати, чи missing license, wrong package, wrong firmware image, wrong radio module або active recovery mode. API changed without named promise.

Tests проходили examples, а не product line. Вони покривали standard package, один regional package, один happy-path update, але не combinations, які customers, manufacturing, service tooling, release packaging і support уже почали treating as possible.

Agenda item виглядав малим: add third product package. Mara написала перше question: «Can we add one more flag?» Потім закреслила два words і запитала:

> Це supported variant, configuration value, implementation detail, temporary exception чи unsupported combination?

Команда перелічила кожну відмінність: board revision, radio module, region behavior, licensed remote control, protocol timeout, manufacturing mode, hidden service-tool option, debug flag, field override, recovery path, default configuration, customer package, update package, diagnostic vocabulary і support horizon.

Після цього вони перестали називати все це flags.

Protocol timeout був configuration. Він вибирав behavior усередині existing product contract і потребував owner, default, validation, migration rule, source of truth і support meaning. Cheaper radio module був variant promise: capability, diagnostics, recovery, manufacturing test, update packaging і support behavior. Region behavior був вужчим variant promise. Licensed remote control був і configuration, і variant promise: license selected exposure, але supported package мав promise для firmware command, radio capability, service-tool behavior, diagnostics, recovery compatibility і support path.

Manufacturing-mode flag не був product variant. Це було Temporary Solution/Global Configuration: broad switch, що змінював calibration, identity, logging, provisioning і safety checks. Debug flag не був supported customer difference. Hidden service-tool option була promise, якщо support на неї depended; інакше - engineering escape hatch. Field override був configuration і Hidden State (`SMELL-004`), бо firmware, support і release не могли одночасно see or explain it. Build define був dependency decision, not `just build setting`.

Mara намалювала три колонки: shared core, variation points, unsupported combinations.

Shared core: pump-control behavior, calibration record shape, identity lifecycle, product-level diagnostic categories, configuration validation rules і update state model. Вони лишаються stable across supported packages, якщо product line не змінює їх intentionally.

Variation points, які команда була готова підтримувати: radio capability, region behavior, licensed remote control, customer protocol timing і recovery access. Кожен потребував owner, validation, default, supported combinations, unsupported combinations і discoverable record.

Unsupported combinations змінили кімнату. Cheaper radio plus licensed remote control був unsupported for next release, бо module не міг виконати recovery promise. Regional package plus old service-tool version був unsupported, бо tool не міг показати required diagnostic reason. Debug evidence flag був unsupported in customer builds. Manufacturing-mode flag був unsupported outside station flow. Field override без Decision Journal entry і review trigger був unsupported as product-line practice.

Product manager хвилювався, що unsupported combinations звучать як losing options. Mara відповіла: «They were not options. They were promises we could not explain.»

Change Radius (`VOCAB-001`, `METRIC-001`) визначав ceremony. Protocol timeout зачіпав firmware validation, customer configuration, одне service-tool message і tests: Decision Journal було достатньо. Licensed remote control на cheaper module зачіпав firmware, hardware, radio dependency, service-tool behavior, manufacturing test, update recovery, release packaging, support training і field diagnosis: RFC (`ARTIFACT-002`) і Architecture Review (`RITUAL-001`) перед hardening.

Shared core і variation points пішли в Architecture Ledger (`ARTIFACT-006`). ADR (`ARTIFACT-001`) визначив product-line boundary перед third package. Smaller defaults і temporary exceptions пішли в Decision Journal (`ARTIFACT-003`). Architecture Freeze (`RITUAL-002`) заморозив package identity, supported radio capability, diagnostic meaning for unsupported operations і recovery compatibility перед release validation.

Команда прибрала два flags: debug flag із production builds і broad manufacturing-mode flag, розділений на station-owned commands із product-level API promises. Hidden service-tool option або стала supported recovery action зі stable meaning, або зникла з customer support flows.

Third package вийшов повільніше, ніж flag-only version. Але він вийшов із меншою кількістю неправдивих обіцянок. Manufacturing знало, яку radio behavior тестувати. Firmware перевіряла configuration щодо supported combinations. Service tool пояснював unsupported capability. Support відтворював field reports, бо package identity, configuration version, module capability і recovery path були видимими. Product line не була grand. Вона була зрозумілою.

## Обговорення

Configuration і variants стають dangerous, коли команда uses them to avoid naming product decisions.

Теза: configuration — це owned product state. Supported variant — це product promise.

Configuration value впливає на behavior; тому йому потрібні owner, scope, default, validation, migration path, source of truth і support meaning. Variant - це promise: product може поводитися, відмовляти, відновлюватися, вироблятися, оновлюватися і підтримуватися так, щоб хтось міг йому довіряти. Product line - не spreadsheet; це architecture, яка дає related products спільне core і навмисні відмінності.

Flags, compile-time defines, configuration files, build variants і spreadsheets - це mechanisms. Проблема починається тоді, коли mechanisms are the only place where product promises live.

Every State Has One Owner (`LAW-001`) застосовується до configuration. Firmware може володіти validation, manufacturing може записувати first value, service tool може update, release може migrate, support може read. Вони можуть брати участь, не стаючи всі owners того самого meaning. Небезпечний випадок: firmware default, manufacturing station value, service tool cache, release assumption і support spreadsheet несуть partial truth.

Every API Is a Promise (`LAW-002`) застосовується до variants. Regional variant обіцяє radio behavior, label content, manufacturing checks, service-tool warnings, release packaging, diagnostic wording і support instructions. Сам flag у firmware не виконує цю promise.

Hardware options приносять dependencies. Cheaper module приносить behavior, capability limits, timing, failure modes, vendor lifecycle, test gaps, update packaging і replacement cost. Every Dependency Is a Decision (`LAW-007`), бо product line тепер покладається на те, що module може і не може робити.

Product-line boundaries називають shared core і variation points. Variation point - це bounded decision про те, де може зʼявитися difference, а не door to every combination. Unsupported combinations теж architecture. Якщо їх не назвати, field знайде їх випадково.

Good variation є навмисною: owner, scope, default, validation, compatibility meaning, support meaning, records і tests. Bad variation ховається в global flags, copied defaults, build defines, service-tool options, customer exceptions і field overrides. Це Silent Coupling (`SMELL-001`).

Global Configuration (`ANTIPATTERN-003`) - поширена trap: one setting controls logging, calibration, connectivity, diagnostics, safety behavior, recovery і service-tool options. Hidden State зʼявляється, коли variant state affects behavior, але не visible through clear owner/interface/model. Platform Leakage зʼявляється, коли hardware/vendor details escape into product variation logic. HAL Everywhere follows, коли hardware abstraction details shape unrelated product behavior.

Simplicity Is a Feature (`LAW-004`) має значення: product line with fewer combinations but direct explanation може бути healthier, ніж flexibility everywhere. Unused Flexibility Is Waste (`LAW-006`) не дає generic variation framework розширювати test space до того, як evidence це виправдає. Evidence Before Confidence (`LAW-005`) вирішує, що стає supported.

Records не дають product line стати oral history. Використовуйте ADR для boundaries, shared core, supported/unsupported combinations або long-lived variation point. Використовуйте RFC, коли broad variation point потребує review. Використовуйте Decision Journal для smaller configuration choices, temporary exceptions, evidence gaps і review triggers. Використовуйте Architecture Ledger для active decisions, owners і review dates. Discoverability (`METRIC-003`) - це здатність знайти, чому package supported або unsupported.

Chapter 23 візьме observability; Chapter 24 - release discipline; Chapter 25 - reference project. Тут завдання вужче: назвати difference, класифікувати її, призначити owner, обмежити її, записати її і перевірити promise.

## Інженерний принцип

Ставтеся до configuration як до owned state, а до variants — як до product promises. Тримайте product line достатньо малою, щоб її можна було зрозуміти, достатньо explicit, щоб її можна було test, і достатньо discoverable, щоб її можна було support.

Запитуйте:

- Це difference: configuration, supported variant, implementation detail, temporary exception чи unsupported?
- Хто owns this value або variation point?
- Хто may change it?
- Який default?
- Як it is validated?
- Як it migrates?
- Які combinations supported?
- Які intentionally unsupported?
- Яку promise цей variant makes to customers, manufacturing, service, release або support?
- Який Change Radius?
- Що must be recorded, reviewed, tested або frozen?

Мета не prevent product differences. Мета - make every supported difference explicit enough, щоб product line могла keep promises.

## Архітектурна вправа

### `Classify One Product Difference`

Оберіть одну product difference, яка changes behavior, manufacturing, service, release, support, update, recovery або customer promise.

Задокументуйте:

1. classification: configuration, variant, implementation detail, temporary exception або unsupported combination;
2. owner;
3. who may change it;
4. default;
5. validation rule;
6. migration rule;
7. storage/source of truth;
8. affected state, API, dependency, test, manufacturing, service, release і support surfaces;
9. supported combinations;
10. unsupported combinations;
11. evidence available;
12. decision record needed;
13. review or freeze trigger;
14. expiration/removal trigger if temporary.

Завершіть однією classification, одним owner, однією supported/unsupported boundary, однією validation або decision action. Якщо відповідь - `just add a flag`, продовжуйте. Flag - це mechanism, not decision.

## Нотатник Principal Engineer

- Flag without owner is hidden state.
- Every supported variant is a promise.
- Cheapest product line - та, яку ви все ще можете зрозуміти.

## ADR

### ADR розділу: `Define Supported Variant Boundaries Before Adding the Third Product Package`

#### Статус

Прийнято для цього розділу.

#### Контекст

Перший product package shipped із small configuration differences. Другий додав cheaper hardware module і service-tool differences. Обидва дійшли до customers через configuration files, build defines, package labels, service-tool options і temporary flags. Third package додає pressure range, licensed remote-control capability, customer-specific protocol timing і recovery behavior depending on module capability. Поточна variation model is not explicit enough.

#### Рішення

Визначити supported variant boundaries перед third package. Відділити configuration values від supported variants. Configuration values потребують owner, default, validation, migration rule, source of truth і support meaning. Supported variants називають behavior, compatibility, manufacturing, service, release, update, recovery і support implications.

Визначити shared core: pump-control behavior, calibration record shape, identity lifecycle, product-level diagnostic categories, configuration validation rules і update state model. Визначити variation points: radio capability, region behavior, licensed remote control, customer protocol timing і recovery access. Кожен має owner, supported/unsupported combinations, validation evidence і discoverable record.

Видалити або завершити temporary flags, які не є supported product behavior. Записувати consequential product-line decisions в ADR; використовувати RFCs для broad variation points, Decision Journal для smaller choices, Architecture Ledger для active decisions. Вимагати Architecture Review перед new variation point із broad Change Radius. За потреби заморожувати selected variant promises перед release validation.

#### Наслідки

Product line стає легшою для розуміння. Configuration values мають owners; supported variants мають explicit promises; unsupported combinations названі. Accidental test space звужується. Supportability поліпшується. Ціна: повільніше додавання features для unsupported combinations, review для customer-specific behavior, підтримання records і removal of flexibility without evidence.

#### Розглянуті альтернативи

- Додати ще один flag.
- Створити separate firmware для кожного customer.
- Зробити все configurable.
- Негайно заморозити current variant model.
- Підтримувати every combination, знайдену в field.
- Відкласти variant modeling до відправлення наступному customer.

Відхилено, бо вони ховають promises, duplicate shared core, expand accidental combinations або freeze/ship unowned variation.

## Коментар редактора

Chapter 22 питає, що стається, коли product більше не є one product in one shape. Він не вводить primary PEAK concept; configuration, variant, product line, supported combination і unsupported combination є chapter-local working terms. Він застосовує state ownership, API promises, simplicity, evidence, unused flexibility, dependency decisions, Change Radius, Discoverability, ADR, RFC, Decision Journal, Architecture Ledger, Architecture Review, Architecture Freeze, Hidden State, Silent Coupling, Platform Leakage, Global Configuration, Temporary Solution і HAL Everywhere.

Це не product-management chapter, не feature-flag guide, не SKU tutorial і не build-system guide. Це architecture chapter про те, як product differences стають promises.
