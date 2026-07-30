# Проєктування для виробництва і польової реальності

## Вступна цитата

> Продукт готовий не тоді, коли він працює для інженерів. Він готовий тоді, коли його можна зібрати й зрозуміти без них.

## Історія

Команда називала pilot unit «тим, що нарешті відчувалося реальним». Пізніше incident file дасть йому простішу назву: «продукт, який працював лише в engineering».

Це був невеликий industrial controller для pump, двох pressure sensors, valve і wireless service link. Попередній prototype був вражаючим, але крихким. Він працював на engineering bench, бо ті самі троє людей, які писали firmware, також знали, як його завантажити, налаштувати, відновити й пояснити його дивні моменти. Робота Chapter 20 допомогла рухатися далі: update path уже не був приватним developer ritual, configuration мала яснішу форму, service tool був product surface, а architecture review прибрала очевидні prototype shortcuts.

До pilot build unit проходив lab test plan: чистий startup, pump control у target band, update sequence, service tool міг підʼєднатися, прочитати й застосувати configuration, а stack boards поводилися достатньо послідовно. Product manager міг показати unit customer без engineer із cable поруч.

Потім почався manufacturing run. Contract manufacturer подзвонив на другий ранок: calibration step тривав занадто довго. На engineering bench calibration означало підʼєднати device, прогріти sensor, запустити script, зачекати, доки pressure fixture стабілізується, підправити offset і перезапустити script, якщо результат виглядав дивно. Це було нормально, коли engineer володіє одним unit за раз. На швидкості line — ні. Operator мав 90 seconds. Script іноді потребував чотири хвилини і просив judgment call: «Чи нормально виглядає цей нахил?»

Manufacturing lead зробив local instruction sheet: якщо offset drift малий — прийняти; якщо script завис — перезапустити живлення і спробувати ще раз; якщо fixture не може дістатися debug connector після enclosure — калібрувати перед final assembly і сподіватися, що стиск gasket нічого не змінить. Це виглядало як line-side pragmatism, не architecture. До пʼятниці це було architecture.

Перший batch показав три behaviors. Original board revision калібрувалася в очікуваному діапазоні. New board revision потребувала іншого timing window. Substitute sensor from approved alternate supplier потребував іншої offset curve. Firmware могла обробити всі три, якщо engineer знав, який case присутній, завантажив правильні constants і перевірив усе вручну. Сам product цього не знав. Він не мав моделі manufacturing-visible calibration state із власником.

Device identity і provisioning були гірші. Identity призначалася у spreadsheet після electrical test, provisioning залежав від того, що station script записує values, які product явно не моделював. Service tool міг прочитати identity, якщо її вже записали, але не було product contract: коли identity стає valid, хто нею володіє, що робити, якщо unit залишає line без неї. Spreadsheet стала state owner. Station script — ще одним. Firmware мала третю часткову думку через cache після first boot. Warehouse labels — четверту. Коли support пізніше запитав, чи returned unit мав substitute sensor, ніхто не міг відповісти лише з product record.

Every State Has One Owner (`LAW-001`) уже навчила: meaningful state потребує одного чіткого owner. У lab device identity, calibration status, fixture result, board revision здавалися setup details. У manufacturing вони були product state. Без owner кожен process вигадував часткового owner.

First field trial сказав те саме різкіше. Units встановили на трьох customer sites: stable power, noisy long cable runs, pump close to power budget. Service calls стали нечитабельними. Support відкрив service tool і побачив raw developer states:

- `BOOT_WAIT_SENSOR`
- `CFG_PENDING`
- `CAL_DIRTY`
- `SAFE_HOLD_3`
- `UPD_RECOVERY_ARMED`

Ці names щось означали firmware team, але не support. Technician бачив `SAFE_HOLD_3`, але не розумів, що саме це означає: mismatch pressure sensor, missing calibration record, update recovery guard або проблему польової проводки. Tool показував internal states замість support-safe diagnosis.

Один unit перезапустився під час update. Update design був кращий за prototype path, але recovery досі припускало developer laptop і private cable. Field technician не мав жодного з них. Support script сказав повернути unit. Firmware engineer сказав: «Його можна відновити. Треба лише підʼєднатися engineering tool і запустити loader у manual mode.» Це завершило argument. Те, що може відновити developer у lab, не є відновленням у field.

Інший unit втратив field logs після reset. Team ставилася до logs як до convenience surface. У field logs були evidence. Reset прибрав pressure readings, update attempt, configuration version і voltage warning. Evidence Before Confidence (`LAW-005`) стало product obligation, коли engineers були відсутні.

Product manager запитав: «Чому manufacturing і field зламали architecture?» Mara, principal engineer, відповіла: «Вони її не зламали. Вони показали, яких realities бракувало в contract.»

Вона відокремила process details від architectural promises. Manufacturing line може вибирати station layout, operator steps, label placement і fixture timing. Architecture все одно має сказати, який product state існує, хто ним володіє, які surfaces можуть його записувати і яка evidence доводить його правильність.

Вона назвала assumptions, які lab ховав: calibration припускала developer judgment; identity/provisioning припускали правильні spreadsheet і script; fixture access припускав debug connector після enclosure; board revision handling припускав, що engineer знає revision; service diagnosis припускала, що support може перекласти firmware states; update recovery припускав developer laptop; field evidence припускала, що device живий достатньо довго, щоб витягнути logs; component substitution припускала, що equivalent electrical behavior означає equivalent product behavior.

Потім вона попросила owners. Firmware володіла product model для calibration status, а не station script. Manufacturing володіло fixture process, але fixture записував лише через product API з визначеною promise. Hardware володіло board revision encoding і показувало його через product-level interface. Support володів service diagnosis vocabulary; firmware володіла mapping від internal state до support-safe reason. Release володів field recovery path; product architecture мала зробити recovery можливим без developer-only tools.

Every API Is a Promise (`LAW-002`) стало корисно незручним: calibration script був не `just a script`, якщо manufacturing від нього залежало; service tool state view був не `just debug output`, якщо support його використовував; recovery command був не `just engineering access`, якщо field plan на нього покладався.

Every Dependency Is a Decision (`LAW-007`) застосовувався до pressure fixture, station script, alternate sensor, board revision encoding, label printer, spreadsheet, service laptop, field cable і update loader. Кожна dependency приносила behavior, failure modes, ownership boundaries і replacement cost.

Перша спокуса: broad manufacturing mode. Один flag відкривав calibration bypasses, raw state writes, fixture commands, serial number changes і extra logs. Це звучало швидко; насправді це була Global Configuration (`ANTIPATTERN-003`) з factory badge. Один setting впливав би на calibration, identity, logging, update behavior, safety holds і support diagnostics, збільшуючи Change Radius (`VOCAB-001`, `METRIC-001`).

Mara наполягла на менших surfaces. Для calibration потрібен був product-owned record зі status, version, source, evidence і validation result. Station могла запитувати calibration, записувати measurements і отримувати product-level pass/fail reason, але не створювати hidden state model. Для identity потрібен lifecycle: unassigned, assigned, verified, retired. Fixture access потребував surface, доступної в assembly point. Board revision мав давати product-level capability description. Service diagnosis потребувала stable vocabulary. Update recovery мав мати field path без developer laptop. Logs потребували достатньої persistence, щоб зберігати last useful evidence після reset.

Найнаслідковіші choices пішли в ADR. Менші evidence gaps — у Decision Journal entries. First field escape створив Mistake Ledger entry: «Якщо recovery працює на developer laptop, це field recovery». Хибно.

Architecture Review (`RITUAL-001`) переглянув architecture surfaces, від яких залежали manufacturing і support: calibration ownership, identity lifecycle, fixture contract, diagnostic vocabulary, update recovery, traceability record. Перед pilot build Architecture Freeze (`RITUAL-002`) заморозив лише кілька decisions: calibration record shape, service diagnosis vocabulary, identity lifecycle, recovery contract. Freeze був тимчасовим і названим; він не зупиняв learning від line або field.

Результат не був ефектним. Unit виглядав так само. Pump усе ще вмикалася. Enclosure майже не змінився. Але product виживав у місцях, де engineers були відсутні. Manufacturing більше не виводило calibration validity здогадкою. Fixture отримував product-level errors. Board revision несла capability description без HAL Everywhere (`ANTIPATTERN-002`). Service tool показував support reasons, привʼязані до configuration, calibration, hardware, firmware і environment evidence. Logs зберігали останній trace через reset. Component substitution стала decision з evidence. Line workaround усе ще міг трапитися, але якщо він змінював product behavior, йому були потрібні owner, review trigger і removal condition; інакше Temporary Solution (`ANTIPATTERN-006`) стала б постійною.

Pilot усе одно знайшов problems. Так працюють добрі pilots. One sensor lot мав вужчий stable range. One support message був нечітким. One recovery instruction було важко виконати під тиском. Але problems були visible, мали owners, evidence і records.

Product перетнув boundary, яку lab не міг simulate: він став architecture для людей, яких не було в кімнаті, коли architecture проєктували.

## Обговорення

Manufacturing reality і field reality — не cleanup наприкінці роботи. Це вхідні дані для design.

Лабораторія дає незвичні переваги: обізнаних інженерів, прямий доступ до плати, приватні інструменти, гнучкий час, поблажливе налаштування і людей, які памʼятають, чому дивна поведінка прийнятна. Виробниче й польове використання прибирають ці переваги. Вони питають, чи продукт можна будувати повторювано, налаштовувати правильно, калібрувати безпечно, ідентифікувати надійно, відновлювати без розробників, діагностувати силами підтримки і пояснювати на основі доказів.

Architecture не має містити кожну manufacturing procedure. Manufacturing process вирішує, як працює line. Product architecture вирішує, який state існує, хто ним володіє, які surfaces можуть його змінювати і яка evidence це доводить. Field service process вирішує, як support працює з customers. Product architecture вирішує, яким diagnosis, recovery, traceability і configuration promises цей process може довіряти.

Repeatability — перший pressure. Prototype часто succeeds through skilled repetition. Manufacturing потребує ordinary repetition: shift changes, fixture variation, component lots, board revisions, enclosure constraints, line timing. Якщо step потребує judgment, architecture має сказати, яке judgment належить людині, а яке стає product decision з чітким результатом.

Calibration example: небезпечне питання — не «Чи можна відкалібрувати unit?» Краще питати: що product знає після calibration, хто володіє цим state, як його validate і що system promises? Без відповіді calibration стає Hidden State (`SMELL-004`).

Identity, provisioning і traceability створюють схожий pressure. Serial number — не лише label. Він поєднує hardware revision, component lot, firmware version, configuration, calibration, field history і support action. Якщо identity призначають spreadsheet, label printer, station script і firmware cache без одного product contract, product має Silent Coupling (`SMELL-001`).

Fixture access є architecture, коли product на нього покладається. Debug connector, hidden inside enclosure, не є manufacturing detail, якщо calibration, identity або recovery залежать від нього після assembly. Architecture визначає product-level contract, який використовує fixture, де в assembly flow він доступний і яку evidence fixture повертає.

Diagnostics має значення, бо field робить ambiguity дорогою. Developer states точні, але неправильною мовою. Support-safe diagnostic surface має розділяти configuration, hardware, firmware, environment, update і calibration causes, зберігати evidence і не змушувати support памʼятати приватні firmware meanings.

Update recovery — та сама promise. Product є recoverable, коли intended support/field path може його відновити за реалістичних access, tooling, time, power і network constraints. Private tools не є field recovery.

Architecture має чинити опір broad catch-all modes. Single manufacturing flag або field-service flag часто створює Global Configuration. Про smaller owned surfaces легше reasoning.

Evidence Before Confidence має тут значення: лабораторний успіх є доказом для лабораторних умов. Пілотне виробництво, заміна компонента, складання enclosure, польова проводка, клієнтська конфігурація і використання підтримкою потребують власних доказів.

Discoverability (`METRIC-003`) стає product quality. Future maintainer має знайти decision, owner і contract за calibration ownership, identity lifecycle, diagnostic vocabulary, recovery path і traceability record. ADRs, Decision Journal і Mistake Ledger entries тримають reality привʼязаною до architecture.

Цей розділ не є довідником з виробництва, польовим сервісним посібником, інструкцією з проєктування fixture, розділом про спостережуваність або описом release process. Він робить виробничі й польові припущення явними, перш ніж пілотне використання почне від них залежати.

## Інженерний принцип

Проєктуйте продукт для місць, де інженерів немає. Manufacturing і field reality вимагають від architecture зробити identity, calibration, configuration, diagnostics, recovery, traceability і ownership явними до того, як product почне від них залежати.

Запитуйте:

1. На який state покладатимуться manufacturing або support?
2. Хто володіє цим state?
3. Яка surface може його створити, змінити, validate або retire?
4. Що продукт обіцяє щодо калібрування, ідентичності, конфігурації і відновлення?
5. Які assumptions живуть у scripts, spreadsheets, private tools або памʼяті team?
6. Яка field evidence має пережити reset, update failure або loss of connection?
7. Чи може support розділити configuration, hardware, firmware, environment і calibration causes?
8. Яку dependency manufacturing або field path тихо імпортував?
9. Який Change Radius, якщо assumption хибне?
10. Яка evidence існує поза lab?
11. Де future engineer знайде owner, contract, decision і review trigger?

Мета не в perfection до pilot manufacturing. Мета — не дати product залежати від invisible engineering presence.

## Архітектурна вправа

### `Expose One Manufacturing or Field Assumption`

Оберіть поведінку продукту, яка працює в лабораторії і має значення у виробництві або в полі: калібрування, ідентичність, доступ до fixture, сервісна діагностика, відновлення після оновлення, призначення конфігурації, польові логи після скидання, заміна компонента або обробка ревізії плати.

Опрацюйте assumption:

1. Опишіть лабораторну поведінку одним реченням.
2. Назвіть manufacturing або field condition, яка змінює behavior.
3. Визначте поточне приховане припущення.
4. Назвіть state, dependency, API promise або evidence gap.
5. Визначте власника.
6. Вирішіть, яку architectural surface треба додати, змінити або зробити explicit.
7. Визначте дію перевірки поза лабораторією.
8. Запишіть ADR, Decision Journal або Mistake Ledger.

Завершіть одним assumption, одним owner, однією architectural surface і однією дією evidence або validation.

## Нотатник Principal Engineer

- Lab — це не environment.
- Diagnostics найважливіші, коли developers відсутні.
- Workaround стає architecture, коли ним ніхто не володіє.

## ADR

### ADR розділу: `Make Calibration and Recovery Product Responsibilities Before Pilot Manufacturing`

#### Статус

Прийнято для цього розділу.

#### Контекст

Продукт працює в лабораторії після переходу від прототипу до продукту. Конфігурація стала яснішою, service tool уже існує, оновлення може перевіряти інженерна команда. Pilot build наближається. Залишковий ризик: продуктові зобовʼязання досі припускають присутність інженерів - скрипти калібрування за участі розробника, відновлення через developer laptop/private cable, ідентичність через spreadsheet/station script, доступ до fixture через debug connector, сирі стани розробників у сервісній діагностиці і втрачені польові логи після скидання.

#### Рішення

Зробити calibration ownership explicit. Firmware-owned calibration record містить status, version, source, validation result і enough evidence для manufacturing/support. Надати manufacturing-safe calibration/provisioning path: fixture запитує calibration, подає measurements, provisions required identity/setup values через product contract і отримує product-level pass/fail reasons. Він не може створювати separate hidden state model.

Визначити мінімальний сервісно видимий діагностичний словник, який розділяє причини, повʼязані з configuration, hardware, firmware, environment, update і calibration. Зробити відновлення після update можливим без інструментів лише для розробників. Ставитися до identity і traceability як до архітектурних контрактів: lifecycle, ownership, validation і fields, що поєднують board revision, component substitution, firmware, configuration, calibration і field evidence.

Записати залишкові припущення і тригери перегляду в ADR, Decision Journal і Mistake Ledger там, де це доречно. Глибші variants, observability, release discipline і reference-project examples відкласти до наступних розділів Part IV.

#### Наслідки

Manufacturing може будувати repeatable units без private engineering judgment. Support може діагностувати через product-level reasons. Calibration, identity, recovery і traceability мають owners. Ціна: більше integration work до pilot, cross-owner agreement, evidence поза lab і constraints on future variants.

#### Розглянуті альтернативи

- Дати manufacturing володіти workaround.
- Залишити developer scripts і навчити line.
- Додати broad manufacturing mode.
- Відкласти service diagnostics до field trial.
- Покластися на release notes і support training.
- Переробити всю architecture перед pilot.

Усі варіанти відхилено, бо вони або ховають ownership, або залежать від engineering presence, або створюють Global Configuration, або послаблюють field learning, або ширші за поточне evidence.

## Коментар редактора

Chapter 21 питає, чи виживають продуктові рішення у виробничій і польовій реальності, коли інженерів немає поруч. Він не вводить нового PEAK concept. Він застосовує Every State Has One Owner (`LAW-001`), Every API Is a Promise (`LAW-002`), Evidence Before Confidence (`LAW-005`), Every Dependency Is a Decision (`LAW-007`), Change Radius, Discoverability, ADR, Decision Journal, Mistake Ledger, Architecture Review, Architecture Freeze, Temporary Solution, Hidden State, Silent Coupling, Platform Leakage, HAL Everywhere і Global Configuration.

Межа навмисна: це не manufacturing handbook і не service manual, а архітектурний розділ про явні виробничі й польові припущення. Chapter 22 тепер може перейти до configuration і product lines; Chapter 23 - до observability; Chapter 24 - до release; Chapter 25 - до reference project.
