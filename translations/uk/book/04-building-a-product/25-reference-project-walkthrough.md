# Прохід референсним проєктом

## Вступна цитата

> Продукт - це не одне рішення, зроблене добре. Це ланцюг рішень, які все ще можна знайти, коли field питає чому.

## Історія

### Один продукт, пʼять точок тиску

Prototype був достатньо малим для одного bench і достатньо складним, щоб стати product.

Команда називала його Field Sensor Gateway. Він sampled one field sensor, stored local configuration, reported readings over low-power radio link і exposed simple service tool for setup and diagnosis. First customer хотів pilot. Prototype довів, що sensor reading корисний, reporting path працює в lab, а technician може змінити basic configuration без rebuilding firmware.

Це був focused prototype: hard-coded reporting interval, manual calibration для пʼяти units, service tool, що показував developer logs, firmware update through lab cable/script, latest build updating to next build on bench, одна hardware revision, один sensor offset, один radio module, одна configuration shape, один customer package.

Prototype success створив pressure. Sales хотіли десять pilot units. Manufacturing хотіло serial identity і calibration flow. Support хотів діагностувати radio failures без firmware engineer, який читає raw logs. Product owner хотів regional package із довшим reporting interval і ще один package з іншою radio option. Customer попросив special timeout, бо gateway зникав на minutes. Release хотів v1.1 з new configuration schema. Field units на v1.0 і v1.0.2 уже існували.

Кожний pressure виглядав local. Firmware могла замінити hard-coded interval на setting. Manufacturing могло додати station file. Support міг отримати richer log. Service-tool owner міг додати regional toggle. Release міг додати migration. Radio owner міг tune retry. Жодне рішення не було хибним окремо; разом вони створили б product, який ніхто не міг пояснити.

Перший argument: reporting interval. Один engineer хотів global `reportingInterval` у non-volatile configuration. Manufacturing writes it, service tool edits it, firmware reads it, regional package sets default, special timeout another value. Просто, доки не зʼявилися combinations: standard every ten minutes; regional every thirty; battery package longer interval plus different retry; special customer timeout був не reporting interval, а gateway-absence tolerance. One broad value виглядав би flexible, але ніхто не owned promise.

Mara запитала:

> Яку difference ми обіцяємо support, а яку лише tolerating for the pilot?

Regional reporting interval став supported variant promise. Battery package deferred, бо він змінював measurement cadence, retry timing і field-support expectations. Special customer timeout став pilot exception з owner і review trigger. Global setting зник. Configuration стала owned state, а не hiding place for product difference.

Другий argument: manufacturing. Station могла записати serial identity і calibration. Проблемою була authority. Manufacturing вимірювало calibration; firmware використовувала її; service tool міг request recalibration; v1.1 migration мала preserve it; older hardware revision stored backup differently; recovery могла restore firmware, але не знала, чи calibration still matched hardware revision без owner. Команда назвала state owners: manufacturing owns first measurement/evidence, firmware owns runtime calibration state and validation rules, service tool requests workflow but cannot write raw product truth, release owns migration evidence, support owns field procedure. Device reports serial identity, hardware revision, calibration version, active configuration fingerprint і firmware version in support-safe diagnostic snapshot.

Третій argument: second board revision. Sensor offset змінився. Happy path виглядав нормально. Old calibration flow, service-tool label, event meaning і v1.0 update path тепер залежали від hardware revision. Команда майже додала flag. Mara попросила trace Change Radius. Він зачіпав firmware validation, station programming, service-tool display, field diagnostics, release notes, migration evidence, support scripts і Event Catalog. Це був не local flag, а product promise. Команда відкрила RFC для hardware-revision and configuration compatibility across firmware, manufacturing, service tooling, QA, support і release.

Четвертий pressure: field. Три pilot units stopped reporting after v1.1 update. Два завершили migration і втратили radio contact during first report. Один rejected configuration migration, бо regional package used old field name. Service tool показав те саме message: update failed. Правда, але марна.

Support потребував identity, active firmware, configuration fingerprint, variant, calibration validity і rejected boundary. Команда написала перші Event Catalog entries:

- `upgrade_started`: package accepted; записано source version, target version, hardware revision і variant.
- `configuration_migration_rejected`: firmware відхилила migration і зберегла source configuration.
- `first_report_not_acknowledged`: radio path не отримав очікуване acknowledgement у supported retry window.
- `recovery_ready`: device увійшов у supportable recovery state з identity, calibration state, active version і configuration fingerprint.

Кожен event мав owner, producer, consumer, ordering assumption і failure meaning. Event Explosion був risk з одного боку; Hidden State - з іншого. Команда обрала менше events із гострішим meaning.

Пʼятий pressure: release. v1.1 змінив configuration schema. Latest lab build upgraded cleanly, але field units існували на v1.0 і v1.0.2. Hardware revision потребувала different calibration migration. Regional variant мав different reporting interval і radio option. Special timeout був pilot exception, а не supported variant. Rollback міг повернути executable, але втратити migrated configuration meaning, якщо source snapshot і calibration state не preserved.

Release owner запитав: «Can we ship v1.1?» Mara запитала:

> Який product baseline ми обіцяємо, і яка evidence тримає цю promise true?

Команда побудувала decision chain замість checklist. Prototype assumptions стали owned product decisions. Hard-coded interval став regional variant default, а не global setting. Manual calibration стала manufacturing measurement із firmware ownership of runtime validity. Developer logs стали support-safe diagnostics, tied to event meanings. Lab-only update script став release path із supported source versions і recovery behavior.

Supported pilot baseline включав hardware revisions A and B, standard and regional packages, configuration schema v2, service tool 4.3+, direct upgrade з v1.0.2 до v1.1 і upgrade з v1.0 до v1.1 лише через intermediate migration package. Special customer timeout лишився pilot exception у Decision Journal з review trigger після thirty field days або second customer request. Battery package був deferred. Older service tool rejected for v1.1 upgrade.

Unsupported combinations: revision A з unvalidated calibration backup не може оновлюватися напряму; regional package не може використовувати special timeout; battery package не може бути hidden flags; v1.0 не може пропускати intermediate migration; service tool older than 4.3 не може оновлювати; factory reset не є default recovery, бо він знищує identity, calibration evidence і trust.

Records: pilot baseline записано в ADR; compatibility proposal - в RFC; special timeout - у Decision Journal; event meanings - в Event Catalog; active decisions - в Architecture Ledger; escaped assumption «latest lab update proves field update readiness» - у Mistake Ledger.

Review and freeze: Architecture Review для broad compatibility decision, що перетинало firmware, manufacturing, service tooling, support, QA, release і field behavior. Architecture Freeze був narrow для v1.1 upgrade-path validation: supported paths, migration rules, service-tool compatibility, event meanings, release-critical state owners і recovery behavior. Bug fixes могли продовжуватися, якщо вони зберігали decisions; changes потребували exception, owner review, record updates і evidence.

Pilot не став perfect. Він став supportable. Коли unit stopped reporting, support бачив source version, target version, active variant, configuration fingerprint, hardware revision, calibration state, reset reason, migration result і first-report outcome. Вони знали різницю між radio acknowledgement failure і rejected migration, коли rollback safe, коли retry enough, коли forward-fix honest. Future engineers могли знайти baseline decision, unsupported combinations, event meanings, review notes і reopen conditions.

Ось що таке walkthrough: не universal design і не reference implementation, а chain of decisions, який тримався разом, коли product вийшов зі стенда.

## Обговорення

Reference project корисний, коли він поєднує decisions. Якщо Field Sensor Gateway стає product specification, він сперечається з real systems. Якщо code walkthrough - навчає mechanics. Якщо recap - repeats. Корисне питання:

> Якби нам треба було провести один embedded product від prototype до supported release, які architecture decisions ми б ухвалили, записали, перевірили, переглянули, заморозили і повернули на перегляд?

Відповідь - chain.

Prototype довів useful behavior under prototype conditions. Він не довів manufacturing repeatability, field diagnosis, regional variants, release compatibility, calibration migration, support horizon або interrupted reporting recovery. Це розрізнення із Chapter 20: successful prototype - evidence, not baseline.

Перший product move відкриває assumptions і визначає promises. Hard-coded interval може стати regional variant promise, battery trade-off, support expectation, radio dependency і release compatibility concern. Manual calibration стає identity, manufacturing evidence, firmware validation, support diagnosis і migration behavior. Developer logs допомагають bring-up, але support потребує stable product meaning.

State ownership зʼявляється рано. Identity, calibration, configuration, variant, event meaning, update state і recovery state визначають, що product може робити і чому support може вірити. Every State Has One Owner (`LAW-001`) відділяє explainable device від competing truths across firmware, station scripts, service tools, release packages і support notes.

API promises зʼявляються далі. Service-tool command, diagnostic event, configuration file, regional package, update package, station record або support note можуть здаватися informal, доки інша surface не почне від них залежати. Every API Is a Promise (`LAW-002`) і API Stability (`METRIC-004`) означають, що promise має переживати change without surprising dependents.

Dependencies стають видимими поза bench. Radio link приносить retry behavior, timing assumptions, acknowledgements, gateway compatibility, field failure modes і support cost. Service tool вирішує, що technicians бачать, install і recover. Manufacturing fixture створює identity і calibration evidence. Every Dependency Is a Decision (`LAW-007`).

Time стає product concern: reporting intervals, gateway absence tolerance, update windows, retry timing, event ordering, support horizons і revisit triggers. Time Is a Dependency (`LAW-003`), бо bench behavior може відмовити, коли device sleeps, misses acknowledgement, updates during service window або waits for support.

Manufacturing and field reality роблять baseline чесним. Product потребує serial identity, calibration ownership, fixture/service boundaries. Configuration and variants змушують difference бути deliberate. Regional interval - supported variant; special timeout - pilot exception; battery package deferred. Simplicity Is a Feature (`LAW-004`) тримає baseline understandable. Unused Flexibility Is Waste (`LAW-006`) не дає будувати perfect product-line architecture для imagined variants.

Global Configuration - спокусливий shortcut: один broad flag розмиває regional behavior, hardware revision, migration, diagnostics і support. Recovery: називайте supported/unsupported combinations, тримайте defaults у власності, давайте values scope/lifecycle.

Observability перетворює field behavior на usable evidence. Корисна Field Sensor Gateway evidence: reset reason, active/source/target firmware, hardware revision, configuration fingerprint, variant, calibration state, migration result, radio boundary outcome, first-report result, service-tool compatibility і recovery state. Event Catalog тримає meanings stable. Hidden State, Silent Coupling, Platform Leakage і Event Explosion - risks. Відповідь - не more events, а owned events with product meaning.

Release and upgrade paths перетворюють chain на promise. Supported baseline називає direct path v1.0.2 to v1.1 із hardware revisions, regional packages, schema v2, service tool 4.3+ і preserved identity/calibration/configuration/event/recovery state. Deferred v1.0 path потребує intermediate package. Rejected paths включають old service tools, hidden variants і factory reset as default. One Lost Packet (`FAILURE-002`), The Release We Should Have Delayed (`FAILURE-005`) і The Successful Prototype (`FAILURE-003`) усі важливі, бо missing facts і release pressure expose hidden assumptions.

Records тримають chain discoverable: ADR для baseline, RFC для compatibility proposal, Decision Journal для bounded exception, Mistake Ledger для escaped assumption, Event Catalog для event meanings, Architecture Ledger для active decisions. Discoverability (`METRIC-003`) - це те, завдяки чому future engineers не сприймають same assumptions як new.

Review and freeze мають scope. Architecture Review (`RITUAL-001`) потрібен, коли Change Radius перетинає owners. Architecture Freeze (`RITUAL-002`) потрібен, коли selected decisions need stability for validation. Freeze називає release-critical decisions, а не whole product, і keeps exception path.

Temporary Solution (`ANTIPATTERN-006`) зʼявляється всюди: prototype shortcut, pilot timeout, support script, calibration bypass, manual recovery note. Temporary work не shameful; йому потрібен path out.

Product стає supportable, коли decisions connect: promises, owners, evidence, records і revisit triggers утворюють chain. Part IV завершується тут, бо product уже не лише design problem. Це shared memory, bridge into technical leadership.

## Інженерний принцип

Build product як chain of explicit decisions. Кожне decision називає promise, owner, evidence і revisit condition.

Запитуйте:

1. Що prototype actually proved?
2. Яка product reality changed architecture?
3. Який state needs owner?
4. Який interface became promise?
5. Яка dependency became support obligation?
6. Яка configuration difference є supported variant?
7. Яку unsupported combination треба state?
8. Яка field failure must explain itself?
9. Який upgrade path promised?
10. Яка evidence supports release?
11. Яке decision needs review, freeze або ledger entry?

Мета не в тому, щоб застосувати кожну практику Part IV однаково. Мета - поєднати decisions, які мають лишатися true після того, як product залишає prototype bench.

## Архітектурна вправа

### Пройти один product decision chain

Оберіть small product або subsystem, бажано починаючи з real prototype assumption.

Запишіть:

> Оскільки prototype assumption A стала product promise P, owner O має зберігати evidence E до revisit trigger T.

Простежте prototype assumption, manufacturing/field reality, configuration/variant decision, observable event/diagnostic, release/upgrade path, owner, promise, evidence, record, review/freeze trigger і revisit condition.

Завершіть:

1. одну product promise;
2. одного owner;
3. одну evidence requirement;
4. один record to update;
5. один revisit trigger.

Якщо exercise дає довгий checklist, звузьте його. Якщо виходить лише local fix, розширюйте, доки не зʼявиться next product surface.

## Нотатник Principal Engineer

- Product - це chain of promises.
- Baseline корисний лише тоді, коли assumptions findable.
- Good walkthrough лишає decisions, які people can reuse.

## ADR

### ADR розділу: Set the Field Sensor Gateway Product Baseline for Pilot Release

#### Статус

Прийнято для цього розділу.

#### Контекст

Field Sensor Gateway prototype працює: він передає sensor readings over radio path, зберігає local configuration, має simple service tool і може бути оновлений у лабораторії. Manufacturing потребує serial identity і calibration flow. Field support потребує diagnostic evidence beyond developer logs. Regional and hardware variants уже існують. Firmware v1.1 змінює configuration schema. Field units існують на v1.0 і v1.0.2. Support і future engineers потребують discoverable baseline: supported, deferred, evidence.

#### Рішення

Прийняти limited supported baseline for pilot release.

Pilot baseline підтримує hardware revisions A and B, standard and regional packages, configuration schema v2, service tool 4.3+ і direct upgrade from v1.0.2 to v1.1. Upgrade from v1.0 to v1.1 потребує intermediate migration package. Battery package, unsupported regional timeout combinations і old service-tool upgrade path відкладені або відхилені.

Призначити owners для serial identity, calibration state, configuration schema, regional variant promises, event meanings, release artifact identity, migration behavior, update state і recovery state. Зберігати identity, calibration, configuration fingerprint, hardware revision, variant, source version, target version, migration result, reset reason і first-report outcome як support-safe evidence.

Записати pilot baseline в ADR; тримати hardware-revision/service-tool compatibility proposal в RFC; використовувати Decision Journal для pilot exceptions/evidence gaps; Event Catalog - для event meanings; Architecture Ledger - для active baseline decisions; Mistake Ledger - для escaped assumptions. Провести Architecture Review для broad Change Radius decisions. Застосувати Architecture Freeze вузько до v1.1 upgrade-path validation.

#### Наслідки

Pilot baseline стає supportable. Ownership стає clearer, hidden promises зменшуються, unsupported paths названі до того, як їх знайде support. Field diagnosis поліпшується, future engineers можуть знайти product memory. Ціна: більше validation, visible deferrals, cross-team coordination, delayed customer requests і records to maintain.

#### Розглянуті альтернативи

- Ship prototype baseline.
- Чекати на perfect product-line architecture.
- Support every requested configuration.
- Відкласти observability and upgrade evidence until after pilot.
- Розділити every customer into separate firmware.
- Заморозити entire architecture until all unknowns resolved.

Відхилено, бо вони ховають assumptions, додають speculative flexibility, розширюють support surface або freeze too broadly.

## Коментар редактора

Chapter 25 closes Part IV тим, що змушує product-building chapters meet inside one reference product. Він не повторює previous chapters; він показує, як Field Sensor Gateway decision chain touches prototype evidence, manufacturing/field reality, variants, observability і release paths.

Reference project, Field Sensor Gateway, product baseline, product decision chain, pilot release і walkthrough лишаються chapter-local language. Нового PEAK concept немає. Relationship set включає successful prototype pressure, release risk, communication/recovery failure, state ownership, API promises, time, simplicity, evidence, unused flexibility, dependency decisions, Change Radius, Discoverability, API Stability, ADR, RFC, Decision Journal, Mistake Ledger, Event Catalog, Architecture Ledger, Architecture Review, Architecture Freeze, Hidden State, Silent Coupling, Platform Leakage, Event Explosion, Temporary Solution і Global Configuration.

Це не MCU guide, не RTOS design, не boot loader pattern, не radio protocol comparison, не service-tool spec і не manufacturing-process manual. Embedded details тримають walkthrough credible. Transition to Part V тихий: product decisions, які можна знайти, стають shared memory, достатньо сильною, щоб leadership могло працювати через неї.
