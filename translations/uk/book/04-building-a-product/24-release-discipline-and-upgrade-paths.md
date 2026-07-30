# Release-дисципліна і шляхи оновлення

## Вступна цитата

> Release — це обіцянка пристроям, які не будуть у кімнаті, коли ця обіцянка зламається.

## Історія

### Оновлення, яке спрацювало лише один раз

Команда заслужила відчуття, що product готовий. Embedded controller пройшов шлях від prototype до product: manufacturing identity, calibration record, supported configuration model, named variants, product-level diagnostics, service tool, field events і update path більше не залежали від одного developer laptop. Field trial був шумним, але корисним; devices могли пояснити достатньо state, щоб support відрізняв firmware, configuration, gateway, radio, variant і power failures.

Next release здавався прямолінійним. New firmware поліпшила recovery після gateway outage і змінила configuration schema, щоб licensed remote control можна було ввімкнути без заміни unit. Release candidate існував, package був signed, service tool міг його install, latest engineering build чисто upgrade-ився в lab.

Release owner запитав: «Чи пройшов new image?» Відповідь: так. Current unit на previous engineering build прийняв package, verified image, migrated configuration, restarted, kept identity, reported new firmware і resumed normal operation. Service tool показував progress. Event Catalog update completion збігався з tool message. Release notes перелічували features.

Команда планувала ship. Потім support запитав, які field versions можуть отримати update.

Це адміністративне на вигляд питання було важким. Деякі field units були на latest pilot, деякі — на два releases позаду, невелика група — на early field build. Lab test покривав лише шлях від latest engineering build до release candidate, а не older field versions зі старішими configuration records.

Manufacturing підняло hardware revision issue: одна revision мала інший nonvolatile layout для calibration backup. New firmware могла читати його під час normal boot, але recovery installer використовував менший compatibility path. На older revision recovery path міг зберегти firmware і identity лише якщо calibration backup був ущільнений проміжним release.

Configuration owner помітив deprecated option. New schema мігрувала supported options, але customer variant використовував obsolete field. Migration зберігала value і мапила його на default, легальний для firmware, але неправильний для customer package.

Service-tool owner зауважив, що new release потребує service tool 4.3+, щоб показувати new support-safe failure reasons. Старіші tools могли install image і report success, але якщо migration failed, вони показали б `update failed` без reason, потрібної support.

Rollback ненадовго виглядав заспокійливо. Firmware image можна було roll back. Migrated configuration не завжди можна було roll back без втрати meaning. New schema merged fields і перенесла одну customer option за licensed capability. Повернення до old image не могло reconstruct original configuration, якщо installer не зберіг source snapshot, а package цього не вимагав.

Calibration ownership під час upgrade була ambiguous. Firmware володіла calibration record у normal operation; manufacturing володіло first measurement; service tool міг trigger recalibration; installer копіював calibration як bytes, бо раніше цього вистачало. Під час recovery installer міг знати, що record present, але не чи він досі valid для restored image, hardware revision і variant.

Кожна issue мала local answer: попередити customers, flag hardware revision, special migration branch, update service tool first, release notes, more examples, hold package one week. Жодна відповідь не називала release promise.

Late defect fix змінив gateway retry window під час first report after upgrade. Diff був малий, але зачіпав момент, коли device доводив, що upgrade complete, configuration preserved і service-visible reporting returned. Release owner знову запитав: «Чи пройшов new image?» Mara написала:

> Які upgrade paths ми обіцяємо, і що має лишатися true до, під час і після upgrade?

Команда перестала ставитися до release як до одного image. Вони перелічили source versions і target release, потім hardware revision, product variant, configuration schema, service-tool version, gateway compatibility, calibration layout, identity record, diagnostic event version і recovery behavior. Це виглядало як state transitions, а не переміщення файла на device.

Перший supported path: від latest field release до release candidate, newest hardware revision, standard/regional variants, service tool 4.3+, current configuration schema, no deprecated option. Evidence існувала, але ще потрібні були power-loss migration test і service-tool failure case.

Другий path був supportable після додаткової роботи: від one release behind до release candidate, та сама hardware revision/variants, compatibility migration for previous schema. Firmware володіє migration, service tool володіє failure wording, QA володіє path evidence, release володіє support note.

Третій path відклали: early field build to new release вимагав intermediate release, бо old configuration record не мав достатньо information для safe direct migration. Його записали як unsupported direct path, а не support surprise.

Older hardware revision стала окремим path: upgrade лише якщо calibration backup ущільнений intermediate release; інакше support recovery procedure зберігає firmware/identity, але вимагає calibration validation перед return to service. Factory reset відхилили як default, бо він стирає product trust разом із product state.

Deprecated customer option: package відхиляє unsupported option із support-safe diagnostic, зберігає original configuration і потребує service decision. Release notes називають unsupported path і support horizon.

Rollback став вужчим. Команда розділила rollback, retry, recovery і forward-fix. Retry означає, що той самий package може повторити той самий stage після recoverable interruption. Recovery означає known supportable state після partial upgrade. Rollback означає повернення до previous executable лише тоді, коли configuration, calibration, identity і diagnostic meaning йому відповідають. Forward-fix означає corrected package, коли rollback preserves code but not trust.

Supported paths зберігають identity, calibration, configuration snapshot, source version, target version, variant identity, migration result, service-tool compatibility і diagnostic event version. Event Catalog записує події upgrade started, image verified, migration accepted/rejected, recovery entered, rollback unavailable, retry allowed і upgrade complete.

Architecture Review (`RITUAL-001`) переглянув upgrade paths, state ownership, compatibility promises, evidence gaps і unsupported paths через firmware, service tools, manufacturing, support, QA, gateway і release owners. Architecture Freeze (`RITUAL-002`) заморозив supported source-to-target upgrade paths, migration rules, diagnostic event meanings, service-tool compatibility promise, release-critical state owners і gateway retry behavior під час first post-upgrade report. Implementation fixes могли продовжуватися, якщо вони зберігали decisions.

Late gateway retry change став exception request. Його Change Radius включав firmware, gateway behavior, first-report diagnostics, service-tool wording, update validation, support notes і release evidence. Його прийняли лише після збереження frozen promise і додавання targeted validation.

Records змінилися: ADR зафіксував supported upgrade path freeze, RFC записав service-tool compatibility/migration proposal, Decision Journal зафіксував smaller path decisions, Architecture Ledger перелічив active release-critical decisions, release notes стали support evidence, Mistake Ledger зафіксував assumption: «latest-build lab upgrade proves field upgrade readiness.»

Release не ship-нувся того тижня. Він вийшов пізніше з меншою кількістю surprises. Support знав units, яким потрібен intermediate release. Manufacturing пояснювало old hardware revision calibration validation. Service tool відмовляв unsupported paths. Firmware зберігала promised state. QA перевіряла paths, а не examples. Release notes казали future engineers, де закінчувалися promises. Delay був engineering decision.

## Обговорення

Release discipline — це не ceremony навколо build artifact. Це architecture-aware judgment про те, що можна випускати, що треба hold, яка evidence потрібна, які promises зроблені і як product можна підтримувати після release.

Upgrade path — це supported transition від одного product state до іншого, а не лише firmware image.

Release artifact видимий: file, hash, version label, service-tool success, lab install. Це важливо, але саме по собі не визначає promise. Release зобовʼязує product до behavior, на який покладатимуться other people, tools, devices, procedures і future versions. Він зобовʼязує support до explanations, manufacturing/service — до compatible paths, customers — до meaning of version/variant/configuration/diagnostic/recovery state, future engineers — до records.

«Чи пройшов new image?» — не погане питання, просто замале. Краще: які upgrade paths ми обіцяємо, і що має лишатися true до, під час і після upgrade?

Перед upgrade: source version, hardware revision, product variant, configuration schema, calibration state, identity record, data shape, service-tool expectation, diagnostic vocabulary, dependency behavior, support horizon. Під час upgrade: bootloader/installer states, migration, power-loss windows, network interruptions, partial writes, retries, recovery decisions, first-report handshakes. Після upgrade product пояснює, що сталося, і доводить, що target state supportable.

Every State Has One Owner (`LAW-001`) означає, що release-critical state має authority, перш ніж upgrade може його preserve. Every API Is a Promise (`LAW-002`) означає, що firmware command, diagnostic event, service-tool protocol, manufacturing programming path, configuration schema, update package format або recovery behavior стають promises після release. API Stability (`METRIC-004`) включає behavior, errors, timing і meaning.

Every Dependency Is a Decision (`LAW-007`) застосовується до boot loaders, installers, signing, distribution paths, gateways, service tools і vendor update libraries. Time Is a Dependency (`LAW-003`), бо migration timing, retry windows, support horizons, deprecation dates і staged exposure мають значення. Evidence Before Confidence (`LAW-005`) означає, що latest-build lab upgrade є evidence для одного path, а не для всіх source versions, hardware revisions, variants, tools, power-loss moments або recovery branches.

Compatibility має багато облич: backward, forward, service-tool, manufacturing, field-data, configuration, variant, diagnostic, update-package. Version matrix корисна лише тоді, коли записує migration contract: які source states можуть move, target states, state to preserve, unsupported paths to reject. Upgrade compatibility — це сума path promises. Support horizon називає, як довго product тримає paths alive.

Rollback потребує обережності. Він safe лише тоді, коли executable, що повертається, також повертає trustworthy product state. Якщо upgrade migrated configuration, changed calibration meaning, identity records, diagnostics або field data, rollback code може зберегти file і втратити trust. Retry, recovery і forward-fix — різні promises. Factory reset — last resort, бо він destroys evidence, identity, configuration, calibration або customer trust.

Change Radius масштабує release discipline. Local fix може потребувати targeted test; migration через firmware, service tools, manufacturing scripts, diagnostics, support notes, signing, gateway і variants потребує broad review. Discoverability не дає release стати усною історією: future engineer має знайти supported paths, unsupported paths, compatibility assumptions, release-critical owners, evidence, risks і review triggers.

Architecture Freeze — release tool, яким користуються обережно. Це temporary stabilization of named architectural decisions during high-risk phase, а не universal gate. У release moment supported upgrade paths, migration rules, diagnostic meanings, service-tool compatibility, release-critical APIs, boot/recovery behavior, manufacturing programming paths, support notes і risk decisions можуть потребувати зупинки руху, поки збирається evidence. Freeze має бути scoped, temporary і привʼязаним до exit criteria.

The Release We Should Have Delayed (`FAILURE-005`) — про перетворення known uncertainty на field cost, бо release здається близьким. Відповідь не в тому, щоб затримувати кожен release; відповідь — знати promises, evidence, unsupported paths і accepted risks.

## Інженерний принцип

Release-іть лише promises, які можете support, і upgrade-іть лише paths, які можете explain, recover і validate. Version не є release, якщо compatibility, state transitions, evidence і support obligations не відомі.

Запитуйте:

1. Які source versions можуть upgrade?
2. Які variants/configurations supported?
3. Який state має пережити upgrade?
4. Хто володіє release-critical state?
5. Що стається, якщо power/network відмовляє посеред upgrade?
6. Що можна roll back, retry, recover або forward-fix?
7. Які service tool versions compatible?
8. Яка evidence доводить цей path?
9. Які diagnostics побачить support, якщо path відмовить?
10. Що змінилося після freeze?
11. Який risk accepted, deferred або unsupported?
12. Що release notes мають зробити discoverable?

Мета не в тому, щоб сповільнювати release. Мета — honest commitment, який витримує field.

## Архітектурна вправа

### Trace One Upgrade Path

Оберіть real upgrade path: source version, target version, hardware revision, product variant, configuration schema і service-tool version.

Запишіть:

> Device на source version X, hardware revision Y, variant Z і configuration schema N оновлюється до target version T через supported path P.

Задокументуйте source, target, hardware revision, variant, schema, data/calibration, що мають зберегтися, release-critical state owner, compatibility promises, migration step, rollback/retry/recovery/forward-fix behavior, observability, service-tool compatibility, available/missing evidence, nearby unsupported paths, decision record і freeze/review trigger.

Завершіть одним supported path, одним unsupported/deferred path, одним release-critical owner і однією validation/recovery action.

## Нотатник Principal Engineer

- Release — це promise, а не file.
- Upgrade path включає state, який він має preserve.
- Rollback, що втрачає trust, не є recovery.

## ADR

### ADR розділу: Freeze Supported Upgrade Paths Before Field Release

Статус: прийнято для цього розділу.

Контекст:

- Product має multiple field versions, hardware revisions, configurations, variants і service-tool versions.
- Lab upgrade from latest build працює.
- Field release відкриває unsupported source versions і uncertain migration paths.
- Rollback/recovery не однаково safe для кожного path.

Рішення:

- Перелічити supported source-to-target upgrade paths перед field release.
- Явно відхиляти або відкладати unsupported paths.
- Заморозити release-critical state transitions, configuration migration, diagnostic meanings і service-tool compatibility перед final validation.
- Зберігати identity, calibration, configuration і variant meaning на supported paths.
- Вимагати evidence для кожного supported path.
- Записувати risks, limits, support notes і review triggers в ADR, RFC, Decision Journal, Architecture Ledger, Event Catalog, release notes або Mistake Ledger.
- Відкласти reference-project integration walkthrough до Chapter 25.

Наслідки:

Обіцянки support стають яснішими; field surprises зменшуються; validation йде за paths; rollback/retry/recovery/forward-fix розділені; product trust поліпшується. Validation work зростає; late changes сповільнюються, коли торкаються frozen surfaces; service-tool coordination стає release work.

Розглянуті альтернативи:

- Відправити image лише тому, що latest lab upgrade спрацював.
- Підтримувати кожну field version.
- Вимагати від усіх customers factory reset.
- Покладатися лише на rollback.
- Латати unsupported paths у support scripts.
- Відкласти визначення upgrade path до release.
- Заморозити всю architecture.

Відхилено, бо вони ховають field readiness, руйнують trust, створюють ризик Temporary Solution/Silent Coupling або заморожують надто широкий контур.

## Коментар редактора

Chapter 24 перетворює observable product evidence на supported release і upgrade commitments. Він не вводить primary PEAK concept. PEAK weight тримається на The Release We Should Have Delayed (`FAILURE-005`) і Architecture Freeze (`RITUAL-002`), з Architecture Freeze (`VOCAB-006`) як temporary scoped vocabulary.

Попередні chapters працюють як constraints: release-critical state потребує owners; released diagnostics є API promises; update tooling і service tools є dependency decisions; migration/support horizons залежать від time; confidence потребує evidence; Change Radius і Discoverability визначають ceremony; Event Catalog, ADR, RFC, Decision Journal, Architecture Ledger, release notes і Mistake Ledger тримають decisions findable.

Не запитуйте лише, чи image пройшов. Запитуйте, які paths обіцяє product, який state вони зберігають, яка evidence це доводить і що support може безпечно зробити, коли path відмовляє.
