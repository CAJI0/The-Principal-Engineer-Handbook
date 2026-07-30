# Від прототипу до продукту

## Вступна цитата

> Прототип доводить, що річ може працювати. Продукт доводить, що вона може продовжувати працювати без команди прототипу в кімнаті.

## Історія

Команда називала це найшвидшим шляхом до клієнта. Спершу це було правдою.

Продукт був embedded controller для польового пристрою, який було незручно конфігурувати, повільно діагностувати й дорого обслуговувати. Клієнт хотів робочу демонстрацію перед ширшою програмою. Команда мала шість тижнів, одну ітерацію hardware, пакет vendor driver, стендовий fixture і спонсора, який хотів побачити, що пристрій відповідає на команду без ще однієї архітектурної зустрічі.

Прототип зробив саме те, що має робити добрий прототип: зробив невизначене видимим. На demo bench firmware швидко стартувала, sensor path стабілізувався, пристрій приймав конфігурацію з невеликого service tool, motor profile застосовувався без reset, а клієнт міг змінити один параметр, запустити цикл і побачити результат на екрані.

Прототип не був недбалим. Він був сфокусованим. Він використовував одну відому revision плати, бо саме вона була в команди. Калібрування було ручним, бо існувало лише три пристрої. Configuration була hard-coded під шлях клієнта, бо variants сповільнили б demo. Service tool був debug-додатком із кількома продуктовими словами в UI. Sensor bus driver був прикладом vendor driver із тонкою обгорткою. Firmware оновлювалася через лабораторний кабель і script, який умів запускати лише firmware lead. Diagnostic command відкривав raw hardware state, бо це прискорювало bring-up. Manufacturing мало ad-hoc script, який копіював calibration value зі стендового нотатника у fixture file. Field diagnostics були serial log і developer, який міг його прочитати.

Жоден із цих виборів не дивував. Більшість були правильними для прототипу.

Demo вдалося. Клієнту сподобалося. Спонсору сподобалося ще більше. Product manager запитав, як швидко команда перетворить прототип на перший product baseline. Release owner запитав, чи firmware можна запакувати до кінця місяця. Hardware owner сказав, що друга revision плати достатньо близька. Manufacturing сказало, що script можна адаптувати пізніше. Support сказав, що diagnostics зачекають до пілотних пристроїв.

Фраза «почистимо після pilot» прозвучала на трьох зустрічах. Ніхто не мав лихого наміру. Але прототип почав нести продуктові зобовʼязання до того, як команда назвала припущення, на яких він тримався.

Перше попередження прийшло від другої revision плати. Прототип був відкалібрований на одній платі з одним sensor lot. Нова revision мала ту саму schematic, але трохи інший analog front end. Firmware усе ще стартувала, happy path усе ще працював, але ручне calibration value більше не давало того самого робочого діапазону. Firmware lead знав, як це підкрутити, тож команда підкрутила. Виправлення було достатньо малим, щоб здаватися деталлю.

Потім manufacturing спробувало повторити setup. Station operator міг запустити fixture script, але script припускав стендове імʼя файла, порядок USB device і calibration value із developer note. Він також припускав, що device уже в debug state. На bench firmware lead переводив його туди не задумуючись. На manufacturing station цей крок був невидимим. Station провалила три пристрої поспіль, перш ніж хтось зрозумів: «процес configuration» частково був людиною.

Support знайшов наступний розрив. Пілотний пристрій у полі не застосував configuration. Service tool показав «write failed». Firmware log мав реальну причину: пристрій відхилив profile, бо бракувало board-revision field. Клієнт не мав firmware log. Support engineer не мав debug tool. Єдина людина, яка могла інтерпретувати raw state, була на іншому дзвінку.

Команда мала diagnostics. Вона не мала продуктової діагностики.

Історія configuration теж почала розщеплюватися. Першому клієнту був потрібен один motor profile. Другому потрібен був той самий controller з іншою sensor option. Hardware team хотіла підтримати обидва через hard-coded default і маленький override у service tool. Service-tool owner хотів configuration file. Manufacturing хотіло значення, яким володіє station. Firmware хотіла залишити constant у code, доки variant matrix не стане яснішою. Кожна опція виглядала просто з місця, яке її запропонувало. Разом вони означали, що configuration state не мав власника.

Update path був гіршим. Прототип оновлювався script, призначеним лише для лабораторії: він стирав application, flash-ив новий image і перезапускав device. На bench це завжди працювало. Його ніколи не переривали, не запускали люди з support, він ніколи не мав зберігати попередню configuration і ніколи не мав пояснювати, в якому state device після failure.

Коли release owner запитав, чи pilot можна оновити в полі, кімната стала обережною.

«Оновлення працює», сказав один engineer.

«Шлях оновлення працює в лабораторії», сказала Principal Engineer.

Тоді розмова змінилася. Команда питала: «Як швидко ми можемо відправити прототип?» Principal Engineer написала інше питання:

> Які припущення прототипу треба підняти до продуктового рівня, замінити, передати власнику, перевірити або свідомо прийняти, перш ніж це стане продуктом?

Питання сповільнило кімнату не тому, що було абстрактним, а тому, що кожен міг назвати припущення. Firmware lead назвав hard-coded configuration. Hardware owner — board revision і sensor lot. Manufacturing engineer — ручний calibration step. Service-tool owner — debug tool. Support — браку польової діагностики. Release — script оновлення лише для лабораторії. QA — шлях одного клієнта. Firmware lead останнім і тихо назвав vendor example driver, бо всі знали, що він розповзся далі, ніж планувалося.

Principal Engineer не назвала прототип поганим і не попросила переписування. Вона намалювала пʼять колонок: продуктовий contract, implementation detail, temporary shortcut, evidence gap, removed shortcut. Потім попросила команду розкласти кожне припущення.

Board revision уже не була implementation detail. Вона впливала на calibration, configuration, manufacturing test і support diagnosis. Вона стала продуктовим contract: device повідомляє board revision, а configuration validation враховує її.

Ручний calibration step не міг залишатися людиною. Manufacturing стало власником station step. Firmware стало власником calibration state у device. QA стало власником доказів, що configured unit повторюється на першій і другій board revision.

Hard-coded customer path розділився на два рішення. Algorithm залишився простим, бо це досі була правильна product behavior. Прихована constant — ні. Constant перейшов за configuration path із власником, validation і default. Команда відмовилася будувати generic variant framework для кожного майбутнього product: один реальний variant був evidence, дюжина уявних variants — ні.

Debug service tool став temporary shortcut. Він міг підтримати pilot лише з owner, expiration condition і видимим списком unsupported actions. Product-level rejection reasons мали бути достатньо stable для support. Raw hardware state міг лишитися diagnostic, але не міг бути єдиним поясненням польової відмови.

Vendor example driver став dependency decision. Команда не замінила його одразу. Вона назвала surface, де він дозволений, призначила ownership для оновлень, записала припущення про callbacks і error meaning, і додала review trigger, якщо driver торкнеться release packaging, diagnostics або recovery behavior.

Script оновлення лише для лабораторії став evidence gap. Він довів, що firmware можна flash-ити на bench. Він не довів, що продуктове оновлення можна відновити. Pilot усе ще потребував мінімальної відповіді: що буде, якщо update перерветься, хто може його відновити, який state бачить support і яка configuration зберігається.

Temporary bypass було видалено. Він вимикав один board-revision check під час bring-up. Усі памʼятали, чому він існував. Але памʼять не була ownership. Bypass не мав pilot value, не ніс evidence gap, який варто було зберігати, і мав завеликий Change Radius, якщо потрапить у manufacturing або support.

Whiteboard не зробив продукт готовим. Він зробив роботу чесною. Команда відділила цінний prototype від випадкової product architecture, що ховалася всередині. Prototype довів customer value, sensor path, ідею configuration і здатність команди рухатися швидко. Він не довів повторюваність manufacturing, польову діагностику, відновлюване оновлення, роботу з variants, release packaging, vendor example driver як product dependency або ручне калібрування як частину продукту.

Pilot усе ще вийшов швидко. Але з меншою кількістю прихованих promises. Простий control path залишився. Невелика service interaction залишилася. Вузька device behavior, яка вразила клієнта, залишилася. Але configuration отримала owner. Calibration мала repeatable minimum path. Service tool мав product-level error meanings. Update script мав recovery note і явну межу. Vendor driver мав named dependency surface. Залишкові risks жили в Decision Journal entry з review triggers, а не в розкиданій памʼяті.

Продукт не став ідеальним. Він отримав власників.

## Обговорення

Прототип доводить, що щось може спрацювати один раз. Product architecture визначає, що має продовжувати працювати для різних users, variants, manufacturing, service, release, support і з плином часу.

Prototype не є лиходієм. Добрий prototype — це engineering discipline: він звужує uncertainty, дає evidence, дозволяє customers реагувати на behavior, а не на намір, і виявляє problems, які planning міг лише вгадувати. Небезпека починається, коли prototype evidence трактують як product architecture.

Prototype success зазвичай умовний. Він працював з цією board, цим fixture, цим customer path, цим operator, цим script, цим firmware lead, цим sensor lot, цим service laptop, цим configuration file, цим update cable і цим відомим failure mode. Ці умови не роблять prototype фальшивим. Вони визначають, що саме prototype довів.

Робота Principal Engineer — зберегти це evidence і не дати прихованим assumptions стати невидимими product promises.

Prototype оптимізує швидкість навчання. Product оптимізує повторювану довіру. Один і той самий design choice може бути чудовим у світі prototype і небезпечним у світі product. Hard-coded value може швидко довести control loop; у product firmware він може зробити manufacturing, service, variants і release packaging залежними від памʼяті developer. Debug command може зекономити тиждень bring-up; якщо support покладається на нього в полі, він уже став API promise. Vendor example driver може уникнути premature abstraction; якщо його callback model, error meanings і update cadence розповзлися через product code, tests, tooling і support procedures, це dependency decision.

Відстань між цими світами — `productization` gap: відстань між прихованими assumptions прототипу і required operating reality продукту. Це не нова metric. Change Radius уже дає корисне питання: скільки system surface має змінитися, пройти review або повторне test, коли змінюється одне decision?

Ручний setup стає production configuration. Lab fixture стає manufacturing process. Debug log стає потребою польової діагностики. Один customer path стає variant matrix. Direct dependency стає support obligation. Hard-coded value стає calibration або configuration. Local script стає release process. Happy-path update стає recovery requirement. Single board стає tolerance, lot і field variability. Temporary wiring стає interface contract. Developer memory стає documentation або decision record.

Рух не в тому, щоб засудити кожен gap. Рух у тому, щоб його класифікувати.

Деякі prototype assumptions стають product contracts. Деякі залишаються implementation details. Деякі є temporary shortcuts і потребують owner, expiration або explicit decision. Деякі є evidence gaps. Деякі — residual risks, які можна ship-ити лише коли вони видимі, мають власника, обмежені й привʼязані до review trigger. Деякі треба видалити.

Класифікація запобігає двом overreactions: відправити prototype без змін, бо він сподобався customer, або переписати prototype, бо це «лише prototype». Перше плутає evidence з readiness. Друге викидає evidence і часто замінює working simplicity на speculative flexibility. Unused flexibility is waste.

Кращий шлях вужчий: перелічити assumptions, класифікувати їх, призначити owners, визначити missing evidence, вирішити, що має змінитися до release baseline, що можна ship-ити лише з review trigger, і записати consequential choices.

Ownership є шарніром. Prototype work часто ховає ownership усередині людей. Firmware lead знає update script. Hardware owner знає board revision. Manufacturing engineer знає ручний fixture step. Support engineer знає diagnostic message. Це цінне знання, але це не architecture, доки system не може вижити без приватної памʼяті.

Every State Has One Owner стає конкретним: calibration state, configuration state, board revision, update state, service mode і recovery status потребують owner. Every API Is a Promise стає конкретним: debug command, configuration file, service-tool message, fixture output або script argument можуть бути неформальними лише доти, доки manufacturing, support, QA, release або customer path не починають їм довіряти. Every Dependency Is a Decision теж стає видимим: vendor driver, script language, test harness, flashing tool, fixture behavior, library version або manual process можуть стати частиною product Change Radius.

Records не дають transition стати усною історією. Використовуйте ADR для long-lived product decisions, Decision Journal для менших assumptions, evidence gaps і review triggers, Architecture Review, коли рух від prototype до product твердішає через кілька teams.

Chapter 20 може назвати manufacturing, service, diagnostics, variants, update, recovery, release і support, але не має навчати їх усіх. Chapter 21 піде глибше у виробництво і польову реальність. Chapter 22 — у configuration, variants і product lines. Chapter 23 — в observability. Chapter 24 — у release discipline і upgrade paths. Chapter 25 — у reference project.

Тут достатньо одного питання: що прототип ігнорував, а продукт більше не може ігнорувати?

## Інженерний принцип

Сприймайте successful prototype як evidence, а не architecture. Перед тим як він стане product, відкрийте його assumptions, збережіть simplicity, яка витримує продуктову реальність, замініть shortcuts, які її не витримують, і призначте owners для product realities, які prototype ігнорував.

Запитуйте:

- Що prototype насправді довів?
- Які assumptions жили в людях, scripts, wiring, fixtures або одному test unit?
- Які shortcuts є безпечними implementation details?
- Які shortcuts стають product risk?
- Яка behavior стає product promise?
- Які manual steps мають стати repeatable?
- Які diagnostics потрібні поза лабораторією?
- Що змінюється для manufacturing, service, updates, variants і release?
- Яка dependency стає support obligation?
- Яка temporary solution потребує owner і expiration?
- Який risk можна ship-ити з explicit review trigger?

Мета не в тому, щоб карати prototype speed. Мета — зберегти prototype learning і прибрати invisible promises, які зробили б product крихким.

## Архітектурна вправа

### `Productize One Prototype Assumption`

Оберіть одне prototype assumption. Не беріть увесь prototype. Візьміть assumption, яке зашкодить комусь, якщо стане product behavior без назви.

Запишіть одним реченням assumption. Потім задокументуйте:

1. де assumption живе;
2. чому воно було прийнятним у prototype;
3. яку product reality воно зачіпає;
4. owner;
5. наявні evidence;
6. missing evidence;
7. класифікація: product contract, implementation detail, temporary risk, evidence gap або removed shortcut;
8. affected surfaces;
9. потрібні test або validation;
10. наслідок для manufacturing, service, update, variant або release;
11. потрібний decision record;
12. review trigger або expiration condition.

Завершіть чотирма результатами:

1. одне assumption, підняте до продуктового рівня, видалене або explicitly accepted;
2. один owner;
3. один evidence gap;
4. одна дія переходу від prototype до product.

Якщо exercise завершується фразою «почистимо пізніше», продовжуйте. «Пізніше» — не owner.

## Нотатник Principal Engineer

- Prototype — це evidence, а не product promise.
- Зберігайте simplicity, яка витримує product reality.
- Кожен shortcut потребує owner, expiration або decision.

## ADR

### ADR розділу: `Productize the Prototype Configuration Path Before Release Baseline`

#### Статус

Прийнято.

#### Контекст

Prototype configuration path працював у lab через manual steps і developer scripts. Firmware lead міг перевести device у правильний state, скопіювати calibration value з bench note, запустити flashing script, застосувати hard-coded customer configuration і прочитати debug log після failure. Для prototype це було прийнятно: потрібне було швидке evidence, що device behavior має value і configuration idea може працювати.

Product потребує більше. Manufacturing потребує repeatable configuration і calibration path. Service потребує stable product-level rejection reasons і diagnostic visibility для field unit. Variants потребують способу виразити real differences без framework для кожної майбутньої можливості. Update і recovery потребують visible state, коли configuration changes перервані. Release потребує packaging, який не залежить від local script одного developer.

#### Рішення

Зробити prototype configuration path готовим до product перед тим, як прийняти його як release baseline. Зберегти свідомо прості й stable частини: narrow device behavior, small configuration surface для першого product, customer-visible flow, цінність якого довело demo.

Замінити manual configuration на product configuration path із власником. Firmware володіє device configuration validation і stored configuration state. Manufacturing володіє station step. Service-tool owner володіє product-level messages і operator flow. QA володіє evidence, що path повторюється на supported board revisions і customer configuration paths.

Temporary shortcuts, які залишаються для pilot, мусять мати owner, expiration condition і review trigger. Product-level diagnostics і validation мають розрізняти configuration rejected, unsupported board revision, invalid calibration, interrupted update і unknown device state. Raw debug logs можуть лишатися engineering diagnostics, але не support contract.

#### Наслідки

Команда зберігає швидший шлях від prototype до product baseline, бо не переписує доведений behavior і не додає speculative flexibility. Вона отримує explicit ownership для product assumptions: configuration state, calibration path, service messages, temporary shortcuts, vendor/tool dependency surfaces. Ціна — видима product work до видимого feature progress, validation assumptions, residual risks і review triggers.

#### Розглянуті альтернативи

- Відправити prototype без змін. Це швидко, але manual calibration, hard-coded configuration, developer scripts, lab-only update behavior і debug-only diagnosis стають product architecture без owners.
- Переписати всю architecture перед baseline. Виглядає чистіше, але викидає prototype evidence і створює untested abstractions.
- Додати flexibility для кожного можливого майбутнього variant. Це розширює test matrix, configuration surface, review cost і support burden.
- Відкласти manufacturing, service і update concerns до першого release. Release baseline не може залежати від invisible manual steps.
- Документувати припущення лише в коментарях. Коментарі не створюють ownership, review triggers або discoverability.
- Негайно заморозити prototype behavior. Надто ранній freeze захищає hidden assumptions, а не product architecture.

## Коментар редактора

Chapter 20 відкриває Part IV і змінює джерело архітектурного тиску. Part III навчила формувати decisions: boundaries, Change Radius, failure and recovery, ADRs, Decision Journal, Architecture Review і Architecture Freeze. Chapter 20 питає, що стається, коли working prototype починає нести product obligations.

Відповідь не «сповільнитись», не «переписати», не «додати process». Відповідь — expose assumptions, які зробили prototype successful, і вирішити, які з них можуть вижити як product architecture.

Chapter не має primary PEAK concept. Він тримається на The Successful Prototype (`FAILURE-003`) і Temporary Solution (`ANTIPATTERN-006`), із Simplicity Is a Feature (`LAW-004`), Unused Flexibility Is Waste (`LAW-006`), Evidence Before Confidence (`LAW-005`), володінням станом, API promises, dependency decisions, Change Radius, ADRs, Decision Journal, Architecture Review і Discoverability.

Пізніші chapters Part IV ідуть глибше: Chapter 21 — у manufacturing and field reality, Chapter 22 — у configuration and variants, Chapter 23 — в observability, Chapter 24 — у release discipline, Chapter 25 — у reference project. Chapter 20 створює doorway: product reality є архітектурним pressure, і вперше він проявляється у gap між successful prototype та product, яким він має стати.
