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
- `configuration_migration_rejected`: firmware відхилила migration і preserved source configuration.
- `first_report_not_acknowledged`: radio path не отримав expected acknowledgement у supported retry window.
- `recovery_ready`: device entered supportable recovery state з identity, calibration state, active version і configuration fingerprint.

Кожен event мав owner, producer, consumer, ordering assumption і failure meaning. Event Explosion був risk з одного боку; Hidden State - з іншого. Команда обрала менше events із гострішим meaning.

Пʼятий pressure: release. v1.1 змінив configuration schema. Latest lab build upgraded cleanly, але field units існували на v1.0 і v1.0.2. Hardware revision потребувала different calibration migration. Regional variant мав different reporting interval і radio option. Special timeout був pilot exception, а не supported variant. Rollback міг повернути executable, але втратити migrated configuration meaning, якщо source snapshot і calibration state не preserved.

Release owner запитав: «Can we ship v1.1?» Mara запитала:

> Який product baseline ми обіцяємо, і яка evidence тримає цю promise true?

Команда побудувала decision chain замість checklist. Prototype assumptions стали owned product decisions. Hard-coded interval став regional variant default, а не global setting. Manual calibration стала manufacturing measurement із firmware ownership of runtime validity. Developer logs стали support-safe diagnostics, tied to event meanings. Lab-only update script став release path із supported source versions і recovery behavior.

Supported pilot baseline включав hardware revisions A and B, standard and regional packages, configuration schema v2, service tool 4.3+, direct upgrade з v1.0.2 до v1.1 і upgrade з v1.0 до v1.1 лише через intermediate migration package. Special customer timeout лишився pilot exception у Decision Journal з review trigger після thirty field days або second customer request. Battery package deferred. Older service tool rejected for v1.1 upgrade.

Unsupported combinations: revision A with unvalidated calibration backup не може upgrade directly; regional package cannot use special timeout; battery package cannot be hidden flags; v1.0 cannot skip intermediate migration; service tool older than 4.3 cannot upgrade; factory reset is not default recovery, бо він destroys identity, calibration evidence і trust.

Records: pilot baseline in ADR; compatibility proposal in RFC; special timeout in Decision Journal; event meanings in Event Catalog; active decisions in Architecture Ledger; escaped assumption «latest lab update proves field update readiness» in Mistake Ledger.

Review and freeze: Architecture Review для broad compatibility decision, що crossed firmware, manufacturing, service tooling, support, QA, release і field behavior. Architecture Freeze був narrow для v1.1 upgrade-path validation: supported paths, migration rules, service-tool compatibility, event meanings, release-critical state owners і recovery behavior. Bug fixes могли continue, якщо preserving decisions; changes required exception, owner review, record updates і evidence.

Pilot не став perfect. Він став supportable. Коли unit stopped reporting, support бачив source version, target version, active variant, configuration fingerprint, hardware revision, calibration state, reset reason, migration result і first-report outcome. Вони знали різницю між radio acknowledgement failure і rejected migration, коли rollback safe, коли retry enough, коли forward-fix honest. Future engineers могли знайти baseline decision, unsupported combinations, event meanings, review notes і reopen conditions.

Ось що таке walkthrough: не universal design і не reference implementation, а chain of decisions, який тримався разом, коли product left bench.

## Обговорення

Reference project корисний, коли він connects decisions. Якщо Field Sensor Gateway стає product specification, він argues with real systems. Якщо code walkthrough - teaches mechanics. Якщо recap - repeats. Корисне питання:

> Якби нам треба було провести один embedded product від prototype до supported release, які architecture decisions ми б made, recorded, tested, reviewed, frozen and revisited?

Відповідь - chain.

Prototype довів useful behavior under prototype conditions. Він не довів manufacturing repeatability, field diagnosis, regional variants, release compatibility, calibration migration, support horizon або interrupted reporting recovery. Це distinction із Chapter 20: successful prototype - evidence, not baseline.

Перший product move exposes assumptions і decides promises. Hard-coded interval може стати regional variant promise, battery trade-off, support expectation, radio dependency і release compatibility concern. Manual calibration стає identity, manufacturing evidence, firmware validation, support diagnosis і migration behavior. Developer logs допомагають bring-up, але support потребує stable product meaning.

State ownership зʼявляється рано. Identity, calibration, configuration, variant, event meaning, update state і recovery state визначають, що product може робити і чому support може вірити. Every State Has One Owner (`LAW-001`) відділяє explainable device від competing truths across firmware, station scripts, service tools, release packages і support notes.

API promises зʼявляються далі. Service-tool command, diagnostic event, configuration file, regional package, update package, station record або support note можуть здаватися informal, доки інша surface не почне від них залежати. Every API Is a Promise (`LAW-002`) і API Stability (`METRIC-004`) означають, що promise має survive change without surprising dependents.

Dependencies стають видимими off bench. Radio link приносить retry behavior, timing assumptions, acknowledgements, gateway compatibility, field failure modes і support cost. Service tool вирішує, що technicians see/install/recover. Manufacturing fixture створює identity і calibration evidence. Every Dependency Is a Decision (`LAW-007`).

Time стає product concern: reporting intervals, gateway absence tolerance, update windows, retry timing, event ordering, support horizons і revisit triggers. Time Is a Dependency (`LAW-003`), бо bench behavior може fail, коли device sleeps, misses acknowledgement, updates during service window або waits for support.

Manufacturing and field reality роблять baseline чесним. Product потребує serial identity, calibration ownership, fixture/service boundaries. Configuration and variants змушують difference бути deliberate. Regional interval - supported variant; special timeout - pilot exception; battery package deferred. Simplicity Is a Feature (`LAW-004`) тримає baseline understandable. Unused Flexibility Is Waste (`LAW-006`) не дає будувати perfect product-line architecture для imagined variants.

Global Configuration - спокусливий shortcut: one broad flag розмиває regional behavior, hardware revision, migration, diagnostics і support. Recovery: name supported/unsupported combinations, keep defaults owned, give values scope/lifecycle.

Observability перетворює field behavior на usable evidence. Корисна Field Sensor Gateway evidence: reset reason, active/source/target firmware, hardware revision, configuration fingerprint, variant, calibration state, migration result, radio boundary outcome, first-report result, service-tool compatibility і recovery state. Event Catalog тримає meanings stable. Hidden State, Silent Coupling, Platform Leakage і Event Explosion - risks. Відповідь не more events, а owned events with product meaning.

Release and upgrade paths перетворюють chain на promise. Supported baseline називає direct path v1.0.2 to v1.1 with hardware revisions, regional packages, schema v2, service tool 4.3+ і preserved identity/calibration/configuration/event/recovery state. Deferred v1.0 path потребує intermediate package. Rejected paths включають old service tools, hidden variants і factory reset as default. One Lost Packet (`FAILURE-002`), The Release We Should Have Delayed (`FAILURE-005`) і The Successful Prototype (`FAILURE-003`) усі важливі, бо missing facts і release pressure expose hidden assumptions.

Records keep chain discoverable: ADR для baseline, RFC для compatibility proposal, Decision Journal для bounded exception, Mistake Ledger для escaped assumption, Event Catalog для event meanings, Architecture Ledger для active decisions. Discoverability (`METRIC-003`) - це те, як future engineers не treats same assumptions as new.

Review and freeze scoped. Architecture Review (`RITUAL-001`) коли Change Radius crosses owners. Architecture Freeze (`RITUAL-002`) коли selected decisions need stability for validation. Freeze names release-critical decisions, а не whole product, і keeps exception path.

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
6. Яка configuration difference is supported variant?
7. Яку unsupported combination треба state?
8. Яка field failure must explain itself?
9. Який upgrade path promised?
10. Яка evidence supports release?
11. Яке decision needs review, freeze або ledger entry?

Мета не apply every Part IV practice equally. Мета - connect decisions that must stay true after product leaves prototype bench.

## Архітектурна вправа

### Walk One Product Decision Chain

Оберіть small product або subsystem, ideally starting from real prototype assumption.

Запишіть:

> Оскільки prototype assumption A стала product promise P, owner O має preserve evidence E until revisit trigger T.

Trace prototype assumption, manufacturing/field reality, configuration/variant decision, observable event/diagnostic, release/upgrade path, owner, promise, evidence, record, review/freeze trigger і revisit condition.

Завершіть:

1. one product promise;
2. one owner;
3. one evidence requirement;
4. one record to update;
5. one revisit trigger.

Якщо exercise produces long checklist, narrow it. Якщо only local fix, widen until next product surface appears.

## Нотатник Principal Engineer

- Product - це chain of promises.
- Baseline корисний лише тоді, коли assumptions findable.
- Good walkthrough лишає decisions, які people can reuse.

## ADR

### Chapter ADR: Set the Field Sensor Gateway Product Baseline for Pilot Release

#### Status

Accepted for this chapter.

#### Context

Field Sensor Gateway prototype працює: reports sensor readings over radio path, stores local configuration, має simple service tool і can be updated in lab. Manufacturing потребує serial identity і calibration flow. Field support потребує diagnostic evidence beyond developer logs. Regional and hardware variants exist. Firmware v1.1 changes configuration schema. Field units exist on v1.0 and v1.0.2. Support і future engineers потребують discoverable baseline: supported, deferred, evidence.

#### Decision

Прийняти limited supported baseline for pilot release.

Pilot baseline підтримує hardware revisions A and B, standard and regional packages, configuration schema v2, service tool 4.3+ і direct upgrade from v1.0.2 to v1.1. Upgrade from v1.0 to v1.1 requires intermediate migration package. Battery package, unsupported regional timeout combinations і old service-tool upgrade path are deferred or rejected.

Assign owners for serial identity, calibration state, configuration schema, regional variant promises, event meanings, release artifact identity, migration behavior, update state і recovery state. Preserve identity, calibration, configuration fingerprint, hardware revision, variant, source version, target version, migration result, reset reason і first-report outcome as support-safe evidence.

Record pilot baseline in ADR; keep hardware-revision/service-tool compatibility proposal in RFC; use Decision Journal for pilot exceptions/evidence gaps; Event Catalog for event meanings; Architecture Ledger for active baseline decisions; Mistake Ledger for escaped assumptions. Run Architecture Review for broad Change Radius decisions. Apply Architecture Freeze narrowly to v1.1 upgrade-path validation.

#### Consequences

Pilot baseline стає supportable. Ownership clearer, hidden promises reduced, unsupported paths stated before support discovers them. Field diagnosis improves, future engineers can find product memory. Cost: more validation, visible deferrals, cross-team coordination, delayed customer requests, records to maintain.

#### Alternatives Considered

- Ship prototype baseline.
- Wait for perfect product-line architecture.
- Support every requested configuration.
- Defer observability and upgrade evidence until after pilot.
- Split every customer into separate firmware.
- Freeze entire architecture until all unknowns resolved.

Відхилено, бо вони ховають assumptions, додають speculative flexibility, expand support surface або freeze too broadly.

## Коментар редактора

Chapter 25 closes Part IV тим, що змушує product-building chapters meet inside one reference product. Він не повторює previous chapters; він показує, як Field Sensor Gateway decision chain touches prototype evidence, manufacturing/field reality, variants, observability і release paths.

Reference project, Field Sensor Gateway, product baseline, product decision chain, pilot release і walkthrough лишаються chapter-local language. Нового PEAK concept немає. Relationship set включає successful prototype pressure, release risk, communication/recovery failure, state ownership, API promises, time, simplicity, evidence, unused flexibility, dependency decisions, Change Radius, Discoverability, API Stability, ADR, RFC, Decision Journal, Mistake Ledger, Event Catalog, Architecture Ledger, Architecture Review, Architecture Freeze, Hidden State, Silent Coupling, Platform Leakage, Event Explosion, Temporary Solution і Global Configuration.

Це не MCU guide, не RTOS design, не boot loader pattern, не radio protocol comparison, не service-tool spec і не manufacturing-process manual. Embedded details тримають walkthrough credible. Transition to Part V тихий: product decisions, які можна знайти, стають shared memory, достатньо сильною, щоб leadership могло працювати через неї.
