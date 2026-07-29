# Release-дисципліна і шляхи оновлення

## Вступна цитата

> Release - це обіцянка пристроям, які не будуть у кімнаті, коли ця обіцянка зламається.

## Історія

### Оновлення, яке спрацювало лише один раз

Команда заслужила відчуття, що product готовий. Embedded controller пройшов шлях from prototype to product: manufacturing identity, calibration record, supported configuration model, named variants, product-level diagnostics, service tool, field events і update path більше не залежали від одного developer laptop. Field trial був noisy but useful; devices могли пояснити достатньо state, щоб support відрізняв firmware, configuration, gateway, radio, variant і power failures.

Next release здавався прямолінійним. New firmware поліпшила recovery після gateway outage і змінила configuration schema, щоб licensed remote control можна було ввімкнути без заміни unit. Release candidate існував, package був signed, service tool міг його install, latest engineering build чисто upgrade-ився в lab.

Release owner запитав: «Did the new image pass?» Відповідь: так. Current unit на previous engineering build прийняв package, verified image, migrated configuration, restarted, kept identity, reported new firmware і resumed normal operation. Service tool показував progress. Event Catalog update completion збігався з tool message. Release notes перелічували features.

Команда планувала ship. Потім support запитав, які field versions можуть отримати update.

Це адміністративне на вигляд питання було важким. Деякі field units були на latest pilot, деякі - на два releases позаду, невелика група - на early field build. Lab test покривав лише latest engineering build to release candidate, а не older field versions зі старішими configuration records.

Manufacturing підняло hardware revision issue: одна revision мала інший nonvolatile layout для calibration backup. New firmware могла читати його під час normal boot, але recovery installer використовував менший compatibility path. На older revision recovery path міг зберегти firmware і identity лише якщо calibration backup був compacted intermediate release.

Configuration owner помітив deprecated option. New schema мігрувала supported options, але customer variant використовував obsolete field. Migration зберігала value і мапила його на default, легальний для firmware, але неправильний для customer package.

Service-tool owner зауважив, що new release потребує service tool 4.3+, щоб показувати new support-safe failure reasons. Старіші tools могли install image і report success, але якщо migration failed, вони показали б `update failed` без reason, потрібної support.

Rollback ненадовго виглядав заспокійливо. Firmware image можна було roll back. Migrated configuration не завжди можна було roll back без втрати meaning. New schema merged fields і перенесла одну customer option за licensed capability. Повернення до old image не могло reconstruct original configuration, якщо installer не зберіг source snapshot, а package цього не вимагав.

Calibration ownership під час upgrade була ambiguous. Firmware володіла calibration record у normal operation; manufacturing володіло first measurement; service tool міг trigger recalibration; installer копіював calibration як bytes, бо раніше цього вистачало. Під час recovery installer міг знати, що record present, але не чи він досі valid для restored image, hardware revision і variant.

Кожна issue мала local answer: попередити customers, flag hardware revision, special migration branch, update service tool first, release notes, more examples, hold package one week. Жодна відповідь не називала release promise.

Late defect fix змінив gateway retry window під час first report after upgrade. Diff був малий, але зачіпав момент, коли device доводив upgrade complete, configuration preserved і service-visible reporting returned. Release owner знову запитав: «Did the new image pass?» Mara написала:

> Які upgrade paths ми обіцяємо, і що має лишатися true before, during, and after the upgrade?

Команда перестала ставитися до release як до одного image. Вони перелічили source versions і target release, потім hardware revision, product variant, configuration schema, service-tool version, gateway compatibility, calibration layout, identity record, diagnostic event version і recovery behavior. Це виглядало як state transitions, а не переміщення файла на device.

Перший supported path: latest field release to release candidate, newest hardware revision, standard/regional variants, service tool 4.3+, current configuration schema, no deprecated option. Evidence існувала, але ще потрібні були power-loss migration test і service-tool failure case.

Другий path був supportable with work: one release behind to release candidate, та сама hardware revision/variants, compatibility migration for previous schema. Firmware owns migration, service tool owns failure wording, QA owns path evidence, release owns support note.

Третій path deferred: early field build to new release вимагав intermediate release, бо old configuration record не мав достатньо information для safe direct migration. Його записали як unsupported direct path, а не support surprise.

Older hardware revision стала окремим path: upgrade лише якщо calibration backup compacted by intermediate release; інакше support recovery procedure зберігає firmware/identity, але вимагає calibration validation before return to service. Factory reset відхилили як default, бо він стирає product trust разом із product state.

Deprecated customer option: package rejects unsupported option with support-safe diagnostic, preserves original configuration і requires service decision. Release notes називають unsupported path і support horizon.

Rollback став вужчим. Команда розділила rollback, retry, recovery і forward-fix. Retry означає, що той самий package може attempt same stage після recoverable interruption. Recovery означає known supportable state after partial upgrade. Rollback означає повернення до previous executable лише тоді, коли configuration, calibration, identity і diagnostic meaning йому відповідають. Forward-fix означає corrected package, коли rollback preserves code but not trust.

Supported paths зберігають identity, calibration, configuration snapshot, source version, target version, variant identity, migration result, service-tool compatibility і diagnostic event version. Event Catalog records upgrade started, image verified, migration accepted/rejected, recovery entered, rollback unavailable, retry allowed і upgrade complete.

Architecture Review (`RITUAL-001`) reviewed upgrade paths, state ownership, compatibility promises, evidence gaps і unsupported paths across firmware, service tools, manufacturing, support, QA, gateway і release owners. Architecture Freeze (`RITUAL-002`) froze supported source-to-target upgrade paths, migration rules, diagnostic event meanings, service-tool compatibility promise, release-critical state owners і gateway retry behavior during first post-upgrade report. Implementation fixes могли продовжуватися, якщо вони зберігали decisions.

Late gateway retry change став exception request. Його Change Radius включав firmware, gateway behavior, first-report diagnostics, service-tool wording, update validation, support notes і release evidence. Його прийняли лише після preserving frozen promise і adding targeted validation.

Records змінилися: ADR captured supported upgrade path freeze, RFC recorded service-tool compatibility/migration proposal, Decision Journal captured smaller path decisions, Architecture Ledger listed active release-critical decisions, release notes became support evidence, Mistake Ledger captured assumption: «latest-build lab upgrade proves field upgrade readiness.»

Release не ship-нувся того тижня. Він вийшов пізніше з меншою кількістю surprises. Support знав units, яким потрібен intermediate release. Manufacturing пояснювало old hardware revision calibration validation. Service tool refused unsupported paths. Firmware preserved promised state. QA validated paths, not examples. Release notes told future engineers where promises ended. Delay був engineering decision.

## Обговорення

Release discipline - це не ceremony навколо build artifact. Це architecture-aware judgment про те, що можна ship, що треба hold, яка evidence потрібна, які promises зроблені і як product можна support after release.

Upgrade path - це supported transition from one product state to another, а не лише firmware image.

Release artifact видимий: file, hash, version label, service-tool success, lab install. Це важливо, але саме по собі не визначає promise. Release commits product to behavior, на який покладатимуться other people, tools, devices, procedures і future versions. Він commits support to explanations, manufacturing/service to compatible paths, customers to meaning of version/variant/configuration/diagnostic/recovery state, future engineers to records.

«Did the new image pass?» - не погане питання, просто замале. Краще: які upgrade paths ми обіцяємо, і що має лишатися true before, during and after upgrade?

Before upgrade: source version, hardware revision, product variant, configuration schema, calibration state, identity record, data shape, service-tool expectation, diagnostic vocabulary, dependency behavior, support horizon. During: bootloader/installer states, migration, power-loss windows, network interruptions, partial writes, retries, recovery decisions, first-report handshakes. After: product explains what happened і proves target state supportable.

Every State Has One Owner (`LAW-001`) означає, що release-critical state має authority, перш ніж upgrade може його preserve. Every API Is a Promise (`LAW-002`) означає, що firmware command, diagnostic event, service-tool protocol, manufacturing programming path, configuration schema, update package format або recovery behavior стають promises after release. API Stability (`METRIC-004`) включає behavior, errors, timing і meaning.

Every Dependency Is a Decision (`LAW-007`) застосовується до boot loaders, installers, signing, distribution paths, gateways, service tools і vendor update libraries. Time Is a Dependency (`LAW-003`), бо migration timing, retry windows, support horizons, deprecation dates і staged exposure мають значення. Evidence Before Confidence (`LAW-005`) означає, що latest-build lab upgrade є evidence для одного path, а не для всіх source versions, hardware revisions, variants, tools, power-loss moments або recovery branches.

Compatibility має багато облич: backward, forward, service-tool, manufacturing, field-data, configuration, variant, diagnostic, update-package. Version matrix корисна лише тоді, коли записує migration contract: які source states можуть move, target states, state to preserve, unsupported paths to reject. Upgrade compatibility - це сума path promises. Support horizon називає, як довго product тримає paths alive.

Rollback потребує обережності. Він safe лише тоді, коли returning executable також returns trustworthy product state. Якщо upgrade migrated configuration, changed calibration meaning, identity records, diagnostics або field data, rollback code може зберегти file і втратити trust. Retry, recovery і forward-fix - різні promises. Factory reset - last resort, бо він destroys evidence, identity, configuration, calibration або customer trust.

Change Radius масштабує release discipline. Local fix може потребувати targeted test; migration across firmware, service tools, manufacturing scripts, diagnostics, support notes, signing, gateway і variants потребує broad review. Discoverability не дає release стати oral history: future engineer має знайти supported paths, unsupported paths, compatibility assumptions, release-critical owners, evidence, risks і review triggers.

Architecture Freeze - release tool, яким користуються обережно. Це temporary stabilization of named architectural decisions during high-risk phase, а не universal gate. На release moment supported upgrade paths, migration rules, diagnostic meanings, service-tool compatibility, release-critical APIs, boot/recovery behavior, manufacturing programming paths, support notes і risk decisions можуть потребувати зупинки руху, поки збирається evidence. Freeze має бути scoped, temporary і привʼязаним до exit criteria.

The Release We Should Have Delayed (`FAILURE-005`) - про перетворення known uncertainty на field cost, бо release здається близьким. Відповідь не в тому, щоб delay every release; відповідь - знати promises, evidence, unsupported paths і accepted risks.

## Інженерний принцип

Release-іть лише promises, які можете support, і upgrade-іть лише paths, які можете explain, recover і validate. Version не є release, якщо compatibility, state transitions, evidence і support obligations не відомі.

Запитуйте:

1. Які source versions можуть upgrade?
2. Які variants/configurations supported?
3. Який state має survive?
4. Хто owns release-critical state?
5. Що стається, якщо power/network fails mid-upgrade?
6. Що можна roll back, retry, recover або forward-fix?
7. Які service tool versions compatible?
8. Яка evidence доводить цей path?
9. Які diagnostics побачить support, якщо він failed?
10. Що changed after freeze?
11. Який risk accepted, deferred або unsupported?
12. Що release notes мають зробити discoverable?

Мета не slow release. Мета - honest commitment, який survives field.

## Архітектурна вправа

### Trace One Upgrade Path

Оберіть real upgrade path: source version, target version, hardware revision, product variant, configuration schema і service-tool version.

Запишіть:

> Device on source version X, hardware revision Y, variant Z, and configuration schema N upgrades to target version T through supported path P.

Задокументуйте source, target, hardware revision, variant, schema, data/calibration to survive, release-critical state owner, compatibility promises, migration step, rollback/retry/recovery/forward-fix behavior, observability, service-tool compatibility, evidence available/missing, nearby unsupported paths, decision record і freeze/review trigger.

Завершіть одним supported path, одним unsupported/deferred path, одним release-critical owner і однією validation/recovery action.

## Нотатник Principal Engineer

- Release - це promise, а не file.
- Upgrade path включає state, який він має preserve.
- Rollback, що втрачає trust, не є recovery.

## ADR

### Chapter ADR: Freeze Supported Upgrade Paths Before Field Release

Status: Accepted for this chapter.

Context:

- Product має multiple field versions, hardware revisions, configurations, variants і service-tool versions.
- Lab upgrade from latest build works.
- Field release expose-ить unsupported source versions і uncertain migration paths.
- Rollback/recovery не однаково safe для кожного path.

Decision:

- Enumerate supported source-to-target upgrade paths before field release.
- Explicitly reject/defer unsupported paths.
- Freeze release-critical state transitions, configuration migration, diagnostic meanings і service-tool compatibility before final validation.
- Preserve identity, calibration, configuration і variant meaning across supported paths.
- Require evidence for each supported path.
- Record risks, limits, support notes і review triggers in ADR, RFC, Decision Journal, Architecture Ledger, Event Catalog, release notes або Mistake Ledger.
- Defer reference-project integration walkthrough to Chapter 25.

Consequences:

Support promises clearer; field surprises reduced; validation follows paths; rollback/retry/recovery/forward-fix separated; product trust improves. Validation work increases; late changes slower when touching frozen surfaces; service-tool coordination becomes release work.

Alternatives Considered:

- Ship image because latest lab upgrade worked.
- Support every field version.
- Require all customers to factory reset.
- Rely on rollback only.
- Patch unsupported paths in support scripts.
- Defer upgrade-path definition until after release.
- Freeze whole architecture.

Rejected because they hide field readiness, destroy trust, create Temporary Solution/Silent Coupling risk, or freeze too broadly.

## Коментар редактора

Chapter 24 перетворює observable product evidence на supported release and upgrade commitments. Він не вводить primary PEAK concept. PEAK weight тримається на The Release We Should Have Delayed (`FAILURE-005`) і Architecture Freeze (`RITUAL-002`), з Architecture Freeze (`VOCAB-006`) як temporary scoped vocabulary.

Earlier chapters працюють як constraints: release-critical state needs owners; released diagnostics are API promises; update tooling and service tools are dependency decisions; migration/support horizons depend on time; confidence needs evidence; Change Radius and Discoverability determine ceremony; Event Catalog, ADR, RFC, Decision Journal, Architecture Ledger, release notes і Mistake Ledger keep decisions findable.

Не запитуйте лише, чи image passed. Запитуйте, які paths product promises, який state вони preserve, яка evidence це proves і що support can safely do, коли path fails.
