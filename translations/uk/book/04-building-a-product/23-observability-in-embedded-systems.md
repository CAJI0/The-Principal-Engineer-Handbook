# Observability в embedded systems

## Вступна цитата

> Log корисний лише тоді, коли допомагає комусь вирішити, що сталося далі.

## Історія

### Пристрій, який не міг пояснити себе

Field trial мав довести, що product може вийти з лабораторії. Device уже мав manufacturing identity, supported firmware image, supported configurations, service tool, recovery path і documented product variants. Команда перестала ставитися до кожної плати як до винятку, назвала supported product line і зробила commitments, які могли поділяти manufacturing, support і product.

Потім вийшов перший field update.

Більшість devices оновилися і звітували нормально. Менша група перестала звітувати через певний час після update. Не одразу, не завжди, не на тому самому variant і не на тому самому site. Support dashboard показував тишу. Service tool казав лише `communication failed`. Повернений lab unit із debug build давав корисні logs, але field image їх не містив. Reset reason перезаписувався boot code. Configuration version була невидима для support tool. Variant state зберігався, але не звітувався. Update state зникав після reboot. Radio, gateway, firmware, configuration, application і power failures зливалися в один product error code.

Support не міг сказати, чи проблема була у firmware, configuration, gateway behavior, network coverage, power, variant selection, vendor dependency або recovery після update. Manufacturing identity існувала, але не була повʼязана з diagnostics. Повернений unit збігався з batch, але field evidence не могла сказати, який image, configuration, variant, update step, reset sequence або boundary outcome зробив його silent.

Перша пропозиція була простою: додати більше logs. Verbose radio logs, update logs, gateway logs, power logs, application logs, temporary flag, щоб увімкнути все. Principal Engineer не відкинула імпульс, але бракувало не обсягу, а архітектури. Вона написала:

> Яке рішення мають ухвалити support або engineering, і які докази device має зберегти, щоб це рішення було можливим?

Support мав вирішити, чи повторити communication, попросити power-cycle, надіслати replacement, ескалювати до engineering або позначити site issue. Engineering мав вирішити, чи зламався update mechanism, чи device reboot-нувся під час critical step, чи завантажилася wrong variant configuration, чи змінився gateway protocol, чи radio dependency повелася інакше, або чи application увійшла у state, яким не володіла чисто.

Ці рішення не потребували кожного debug message. Вони потребували малого набору збережених фактів.

Команда перелічила важливі transitions: update started, image verified, configuration migrated, variant selected, gateway session opened, first post-update report sent, recovery entered, recovery completed, normal operation resumed. Кожен transition отримав owner. Кожен boundary failure отримав name. Radio driver міг звітувати radio boundary outcomes, але не вигадувати product meaning. Update component володів update state. Configuration component володів configuration version і migration result. Product identity володіла manufacturing identity, hardware revision і supported variant identity.

Вони відділили developer debug logs від product diagnostics. Developer logs могли залишатися детальними, нестабільними й корисними в lab. Product diagnostics мали бути product promise. Service technician без debugger потребував last meaningful product events, reset context, update/recovery context, firmware version, configuration version, supported variant, manufacturing identity і credible failure domain.

Вони опиралися й протилежній помилці: не кожен цікавий рядок стає event. Principal Engineer створила Event Catalog і питала про кожен candidate event: хто ним володіє, яке рішення він підтримує, як довго має зберігатися? Events без decisions прибрали. Events без owners повернули на доопрацювання. Копії developer logs відхилили. Mistake Ledger записав хибні assumptions: reset reason доступний після boot; configuration version очевидна з firmware image; gateway error code достатній; manufacturing identity і diagnostics можна зʼєднати пізніше.

Наступний field update не прибрав кожну failure. Він зробив failures пояснюваними. Один silent device сказав, що verify-нув image, migrated configuration, selected cellular variant, втратив gateway handshake після reboot і зберіг brownout reset reason. Інший сказав, що configuration migration failed, бо variant table не мала manufacturing option, burned into unit. Третій не мав device failure: gateway відхилив first report після зміни dependency contract.

Product усе ще мав defects. Команда більше не вгадувала, який саме defect.

## Обговорення

Embedded observability - це не друкувати все, що знає firmware. Це зберігати evidence, яка дозволяє комусь ухвалити product decision, коли device далеко, частково відмовив, обмежений power, обмежений network і вже не підʼєднаний до debugger.

Field reality жорсткіша за lab. Developer може rebuild firmware, підʼєднати tools, підняти logging, відтворити path. Support часто має generic failure message, customer report, device identity і, можливо, один шанс запитати device, що сталося. Якщо product не може відповісти stable evidence, organization підставляє confidence, habit, escalation або blame.

Evidence Before Confidence (`LAW-005`) стає конкретним. Evidence має пережити event, через який вона стала потрібною. Reset reason, перезаписаний під час boot, не є field evidence. Update state, що зникає після reboot, не є field evidence. Configuration version, відома лише developer script, не є field evidence. Variant bit не є field evidence, якщо support surface не може його показати.

Перший архітектурний рух - ownership. Every State Has One Owner (`LAW-001`) застосовується до diagnostics. Якщо update state скопійований у три modules, truth не належить нікому. Якщо radio driver, gateway client і product service виробляють той самий `communication failed`, product має hidden state, замаскований під simplicity. Device має називати state transition або boundary outcome на тому рівні, де meaning має owner.

Це API problem. Service tool — API для field organization. `communication failed` обіцяє мало. Last owned events, reset context, firmware/configuration versions, variant identity, update phase, recovery state, manufacturing identity і failure domain дають support обмежені, придатні для дії decisions.

Time — dependency. Failure може статися before reboot, during update, after migration, while waiting gateway response, after first report. Time Is a Dependency (`LAW-003`) не вимагає perfect wall-clock time; вона вимагає useful order: sequence numbers, boot counters, monotonic ticks, install attempts, update phases, retained reset snapshots.

Every Dependency Is a Decision (`LAW-007`) зʼявляється, коли gateway behavior, radio coverage, vendor drivers, network policy, manufacturing data і configuration delivery беруть участь в одному field symptom. Observability має зробити boundary outcome достатньо явним, щоб вирішити: firmware fix, gateway fix, configuration correction, service action або dependency review.

Event Catalog (`ARTIFACT-005`) - центральний artifact. Добрий event entry записує owner, name, trigger, payload, severity, retention, reset behavior, support visibility, privacy/security constraints, versioning, deprecation і supported decision. Він дає Architecture Review (`RITUAL-001`) concrete surface, а Architecture Freeze (`RITUAL-002`) - diagnostic commitments, які треба зберегти.

Embedded constraints усе ще важливі: RAM, flash, CPU, power, radio bandwidth, service access, privacy, security, flash wear. Малий retained ring buffer, counters, boot counter, reset snapshot або bounded crash snapshot можуть бути кращою evidence, ніж huge debug stream, який зникає або розряджає battery.

Протилежний smell - Event Explosion (`SMELL-006`): багато events, мало простіших decisions. Кожен callback, retry і branch emit-ить event; field отримує noise, storage pressure, battery cost, privacy questions і unclear ownership. Discoverability погіршується. Change Radius росте, бо behavior changes торкаються logs, tools, dashboards, support procedures і tests.

Уникати Event Explosion не означає скупитися на evidence. Це означає будувати evidence навколо decisions. Якщо event не може змінити support action, engineering triage, recovery behavior, release validation або product learning, йому місце в developer debug log, а не на product diagnostic surface.

Зʼявляються common smells: Hidden State для reset reasons/update phases/config versions; Silent Coupling для gateway/tool/manufacturing assumptions; Platform Leakage для raw driver concepts на support surface; HAL Everywhere, коли hardware meaning розповзається; Global Configuration, коли кожен component читає configuration напряму; Callback Hell, коли event order нечитабельний; Temporary Solution, коли quick diagnostic flag стає support promise.

One Lost Packet (`FAILURE-002`) нагадує: один missing fact може визначати все investigation. Тут missing fact може бути те, чи first post-update report був attempted, яка configuration була active, чи recovery ran, або чи reset стався before migration.

Observability створює shared memory. ADRs записують architectural diagnostic commitments; Decision Journal записує field decisions from incomplete evidence; Mistake Ledger записує assumptions, які escaped; Weak Signal Register (`ARTIFACT-007`) і Weak Signal (`VOCAB-002`) допомагають помічати patterns before confirmed failures.

Product не потребує perfect observability platform. Йому потрібна достатня durable, owned, support-safe evidence, щоб decisions були менш speculative.

## Інженерний принцип

Проєктуйте observability навколо decisions, а не volume. Називайте state transitions, boundary outcomes, versions, variants, reset context і failure evidence, які product має зберегти, щоб люди без debugger могли вирішити, що сталося і що робити далі.

Корисні питання:

- Яке field decision ця evidence підтримуватиме?
- Який component володіє цим fact?
- Який boundary outcome або state transition він називає?
- Який context має пережити reset, update, recovery і service access?
- Хто може безпечно це бачити, і як вони це validate?

## Архітектурна вправа

### Make One Failure Explain Itself

Оберіть ambiguous field failure або support case: device stops reporting, failed update, confusing configuration issue, manufacturing option, service-tool message, що приховує забагато.

Запишіть decision, яке хтось має ухвалити з field evidence. Визначте missing evidence, що змушує guessing. Зіставте state transition або boundary outcome. Назвіть owner. Чернетково опишіть один event або diagnostic record зі stable name, payload, severity, retention rule, reset behavior, time/sequence, version, configuration, variant і manufacturing identity fields. Вирішіть support-safety, privacy/security constraint, де записується decision, і як validation доводить, що evidence survives failure path.

Outputs:

1. one decision evidence must support;
2. one owned event or diagnostic;
3. one retained context requirement;
4. one validation action.

## Нотатник Principal Engineer

- Logs не є evidence, доки хтось не може їх використати.
- Event без owner стає noise.
- Device має пояснювати достатньо, щоб йому могли допомогти.

## ADR

### ADR розділу: Adopt Decision-Oriented Field Events for Update and Recovery Failures

Status: Accepted for this chapter.

Context:

- Field devices можуть відмовити після update, reset, configuration migration, variant selection, gateway interaction, radio communication або recovery.
- Developer debug logs корисні в lab, але не є stable product promise для support.
- Current service surface може зводити багато failure domains до одного generic message.
- Manufacturing identity, firmware/configuration versions, variant state, reset context і update state мають значення лише тоді, коли preserved і visible.
- Embedded constraints обмежують evidence.
- Logging everything створив би Event Explosion.

Decision:

- Maintain Event Catalog для product diagnostics: owner, name, trigger, payload, severity, retention, reset behavior, support visibility, privacy/security, validation і supported decision.
- Treat update, recovery, reset, configuration, variant, gateway, radio і reporting outcomes як owned product events, коли вони впливають на field decisions.
- Keep developer debug logs окремо від support-safe diagnostics.
- Preserve enough context across reset/recovery, щоб розрізняти firmware, configuration, gateway, network, power, variant, dependency і recovery causes.
- Record false diagnostic assumptions і field escapes у Mistake Ledger.

Consequences:

- Support може ухвалювати bounded decisions без developer tools для кожної issue.
- Engineering може triage from retained evidence.
- Diagnostic events стають product API і потребують ownership, review, tests і compatibility care.
- Event versions/deprecation стають support promises.
- Team має відкидати noisy events і проєктувати з урахуванням storage, power, privacy, security і service-tool constraints.

Alternatives Considered:

- Add verbose logging everywhere.
- Keep diagnostics developer-only.
- Add one generic field error code.
- Defer diagnostics until after field trial.

Відхилено, бо ці варіанти додають noise, ховають evidence від support або відкладають саме ту evidence, яка потрібна field trial.

## Коментар редактора

Chapter 23 іде після Chapter 22: коли product має configurations, variants, manufacturing identity, update paths, recovery paths і service tools, він мусить сказати, яка reality сформувала failure.

Observability лишається chapter-local prose term. Нового PEAK concept немає. Вага лишається на Event Catalog (`ARTIFACT-005`) і Event Explosion (`SMELL-006`), за підтримки state ownership, API promises, time, evidence, dependency decisions, Change Radius, Discoverability, ADR, Decision Journal, Mistake Ledger, weak signals, Architecture Review і Architecture Freeze.

Chapter 24 перенесе ці product promises у release discipline і upgrade paths. Chapter 25 покаже їх у reference project.
