# Від прототипу до продукту

## Вступна цитата

> Прототип доводить, що річ може працювати. Продукт доводить, що вона може продовжувати працювати без команди прототипу в кімнаті.

## Історія

Команда називала це найшвидшим шляхом до клієнта. Спершу це було правдою.

Продукт був embedded controller для польового пристрою, який було незручно конфігурувати, повільно діагностувати й дорого обслуговувати. Клієнт хотів робочу демонстрацію перед ширшою програмою. Команда мала шість тижнів, одну hardware spin, vendor driver package, bench fixture і спонсора, який хотів побачити, що пристрій відповідає на команду без ще однієї архітектурної зустрічі.

Прототип зробив саме те, що має робити добрий прототип: зробив невизначене видимим. На demo bench firmware швидко стартувала, sensor path стабілізувався, пристрій приймав конфігурацію з невеликого service tool, motor profile застосовувався без reset, а клієнт міг змінити один параметр, запустити цикл і побачити результат на екрані.

Прототип не був недбалим. Він був сфокусованим. Він використовував одну відому revision плати, бо саме вона була в команди. Калібрування було ручним, бо існувало лише три пристрої. Configuration була hard-coded під шлях клієнта, бо variants сповільнили б demo. Service tool був debug application із кількома продуктовими словами в UI. Sensor bus driver був vendor example driver із тонким wrapper. Firmware оновлювалася через lab cable і script, який умів запускати лише firmware lead. Diagnostic command відкривав raw hardware state, бо це прискорювало bring-up. Manufacturing мало ad-hoc script, який копіював calibration value з bench notebook у fixture file. Field diagnostics були serial log і developer, який міг його прочитати.

Жоден із цих виборів не дивував. Більшість були правильними для прототипу.

Demo вдалося. Клієнту сподобалося. Спонсору сподобалося ще більше. Product manager запитав, як швидко команда перетворить прототип на перший product baseline. Release owner запитав, чи firmware можна запакувати до кінця місяця. Hardware owner сказав, що друга revision плати достатньо близька. Manufacturing сказало, що script можна адаптувати пізніше. Support сказав, що diagnostics зачекають до pilot units.

Фраза «clean it up after the pilot» прозвучала на трьох зустрічах. Ніхто не мав лихого наміру. Але прототип почав нести продуктові зобовʼязання до того, як команда назвала assumptions, на яких він тримався.

Перше попередження прийшло від другої revision плати. Прототип був відкалібрований на одній платі з одним sensor lot. Нова revision мала ту саму schematic, але трохи інший analog front end. Firmware усе ще стартувала, happy path усе ще працював, але manual calibration value більше не давав того самого operating range. Firmware lead знав, як це підкрутити, тож команда підкрутила. Fix був достатньо малим, щоб здаватися detail.

Потім manufacturing спробувало повторити setup. Station operator міг запустити fixture script, але script припускав bench file name, USB device order і calibration value із developer note. Він також припускав, що device уже в debug state. На bench firmware lead переводив його туди не задумуючись. На manufacturing station цей крок був невидимим. Station провалила три пристрої поспіль, перш ніж хтось зрозумів: «configuration process» частково був людиною.

Support знайшов наступний розрив. Pilot unit у полі не застосував configuration. Service tool показав «write failed». Firmware log мав реальну причину: пристрій відхилив profile, бо не було board-revision field. Клієнт не мав firmware log. Support engineer не мав debug tool. Єдина людина, яка могла інтерпретувати raw state, була на іншому дзвінку.

Команда мала diagnostics. Вона не мала product diagnostics.

Configuration story теж почала розщеплюватися. Першому клієнту був потрібен один motor profile. Другому потрібен був той самий controller з іншою sensor option. Hardware team хотіла підтримати обидва через hard-coded default і маленький override у service tool. Service-tool owner хотів configuration file. Manufacturing хотіло station-owned value. Firmware хотіла залишити constant у code, доки variant matrix не стане яснішою. Кожна опція виглядала просто з місця, яке її запропонувало. Разом вони означали, що configuration state не мав власника.

Update path був гіршим. Прототип оновлювався lab-only script, який стирав application, flash-ив новий image і restart-ив device. На bench це завжди працювало. Його ніколи не переривали, не запускали support-люди, він ніколи не мав зберігати попередню configuration і ніколи не мав пояснювати, в якому state device після failure.

Коли release owner запитав, чи pilot можна оновити в полі, кімната стала обережною.

«The update works», сказав один engineer.

«The update path works in the lab», сказала Principal Engineer.

Тоді розмова змінилася. Команда питала: «How fast can we ship the prototype?» Principal Engineer написала інше питання:

> Які prototype assumptions треба promoted, replaced, owned, tested або intentionally accepted, перш ніж це стане product?

Питання сповільнило кімнату не тому, що було абстрактним, а тому, що кожен міг назвати assumption. Firmware lead назвав hard-coded configuration. Hardware owner — board revision і sensor lot. Manufacturing engineer — manual calibration step. Service-tool owner — debug tool. Support — missing field diagnosis. Release — lab-only update script. QA — single customer path. Firmware lead останнім і тихо назвав vendor example driver, бо всі знали, що він розповзся далі, ніж планувалося.

Principal Engineer не назвала прототип поганим і не попросила rewrite. Вона намалювала пʼять колонок: product contract, implementation detail, temporary shortcut, evidence gap, removed shortcut. Потім попросила команду розкласти кожне assumption.

Board revision уже не була implementation detail. Вона впливала на calibration, configuration, manufacturing test і support diagnosis. Вона стала product contract: device report-ить board revision, а configuration validation враховує її.

Manual calibration step не міг залишатися людиною. Manufacturing стало owner station step. Firmware стало owner calibration state у device. QA стало owner evidence, що configured unit повторюється на першій і другій board revision.

Hard-coded customer path розділився на два decisions. Algorithm залишився simple, бо це досі була правильна product behavior. Hidden constant — ні. Constant перейшов за owned configuration path з validation і default. Команда відмовилася будувати generic variant framework для кожного майбутнього product: один реальний variant був evidence, дюжина уявних variants — ні.

Debug service tool став temporary shortcut. Він міг підтримати pilot лише з owner, expiration condition і visible list unsupported actions. Product-level rejection reasons мали бути достатньо stable для support. Raw hardware state міг лишитися diagnostic, але не міг бути єдиним поясненням field failure.

Vendor example driver став dependency decision. Команда не замінила його одразу. Вона назвала surface, де він дозволений, призначила update ownership, записала assumptions про callbacks і error meaning, і додала review trigger, якщо driver торкнеться release packaging, diagnostics або recovery behavior.

Lab-only update script став evidence gap. Він довів, що firmware можна flash-ити на bench. Він не довів recoverable product update. Pilot усе ще потребував мінімальної відповіді: що буде, якщо update перерветься, хто може його recover, який state бачить support і яка configuration зберігається.

Temporary bypass було видалено. Він вимикав один board-revision check during bring-up. Усі памʼятали, чому він існував. Але памʼять не була ownership. Bypass не мав pilot value, не ніс evidence gap, який варто carry, і мав завеликий Change Radius, якщо потрапить у manufacturing або support.

Whiteboard не зробив продукт готовим. Він зробив роботу чесною. Команда відділила цінний prototype від accidental product architecture, що ховалася всередині. Prototype довів customer value, sensor path, configuration idea і здатність команди рухатися швидко. Він не довів manufacturing repeatability, field diagnosis, recoverable update, variant handling, release packaging, vendor example driver як product dependency або manual calibration як частину продукту.

Pilot усе ще shipped швидко. Але з меншою кількістю hidden promises. Simple control path залишився. Small service interaction залишився. Narrow device behavior, який вразив клієнта, залишився. Але configuration отримала owner. Calibration мала repeatable minimum path. Service tool мав product-level error meanings. Update script мав recovery note і explicit limit. Vendor driver мав named dependency surface. Remaining risks жили в Decision Journal entry з review triggers, а не в розкиданій памʼяті.

Продукт не став ідеальним. Він став owned.

## Обговорення

Прототип доводить, що щось може спрацювати один раз. Product architecture визначає, що має продовжувати працювати across users, variants, manufacturing, service, release, support і time.

Prototype не є villain. Добрий prototype — це engineering discipline: він звужує uncertainty, дає evidence, дозволяє customers реагувати на behavior, а не intention, і виявляє problems, які planning міг лише вгадувати. Небезпека починається, коли prototype evidence трактують як product architecture.

Prototype success зазвичай conditional. Він працював з цією board, цим fixture, цим customer path, цим operator, цим script, цим firmware lead, цим sensor lot, цим service laptop, цим configuration file, цим update cable і цим known failure mode. Ці умови не роблять prototype fake. Вони визначають, що саме prototype довів.

Робота Principal Engineer — зберегти це evidence і не дати hidden assumptions стати invisible product promises.

Prototype optimizes for learning speed. Product optimizes for repeated trust. Один і той самий design choice може бути чудовим у prototype world і небезпечним у product world. Hard-coded value може швидко довести control loop; у product firmware він може зробити manufacturing, service, variants і release packaging залежними від developer memory. Debug command може зекономити тиждень bring-up; якщо support покладається на нього в полі, він уже став API promise. Vendor example driver може уникнути premature abstraction; якщо його callback model, error meanings і update cadence розповзлися через product code, tests, tooling і support procedures, це dependency decision.

Відстань між цими світами — `productization` gap: відстань між hidden assumptions прототипу і required operating reality продукту. Це не нова metric. Change Radius уже дає корисне питання: скільки system surface має змінитися, бути reviewed або retested, коли змінюється одне decision?

Manual setup стає production configuration. Lab fixture стає manufacturing process. Debug log стає field diagnostic need. One customer path стає variant matrix. Direct dependency стає support obligation. Hard-coded value стає calibration або configuration. Local script стає release process. Happy-path update стає recovery requirement. Single board стає tolerance, lot і field variability. Temporary wiring стає interface contract. Developer memory стає documentation або decision record.

Рух не в тому, щоб засудити кожен gap. Рух у тому, щоб його класифікувати.

Деякі prototype assumptions стають product contracts. Деякі залишаються implementation details. Деякі є temporary shortcuts і потребують owner, expiration або explicit decision. Деякі є evidence gaps. Деякі — residual risks, які можна ship-ити лише коли вони visible, owned, bounded і tied to review trigger. Деякі треба видалити.

Classification запобігає двом overreactions: ship prototype unchanged, бо customer liked it, або rewrite prototype, бо це «only a prototype». Перше плутає evidence з readiness. Друге викидає evidence і часто замінює working simplicity speculative flexibility. Unused flexibility is waste.

Кращий шлях вужчий: перелічити assumptions, класифікувати їх, призначити owners, визначити missing evidence, вирішити, що має змінитися before release baseline, що може ship only with review trigger, і записати consequential choices.

Ownership є hinge. Prototype work often hides ownership inside people. Firmware lead знає update script. Hardware owner знає board revision. Manufacturing engineer знає manual fixture step. Support engineer знає diagnostic message. Це valuable knowledge, але це не architecture, доки system не може survive without private memory.

Every State Has One Owner стає concrete: calibration state, configuration state, board revision, update state, service mode і recovery status потребують owner. Every API Is a Promise стає concrete: debug command, configuration file, service-tool message, fixture output або script argument можуть бути informal лише доти, доки manufacturing, support, QA, release або customer path не починають їм довіряти. Every Dependency Is a Decision теж visible: vendor driver, script language, test harness, flashing tool, fixture behavior, library version або manual process можуть стати частиною product Change Radius.

Records не дають transition стати oral history. Використовуйте ADR для long-lived product decisions, Decision Journal для менших assumptions, evidence gaps і review triggers, Architecture Review коли prototype-to-product move harden-иться через multiple teams.

Chapter 20 може назвати manufacturing, service, diagnostics, variants, update, recovery, release і support, але не має навчати їх усіх. Chapter 21 піде глибше в manufacturing and field reality. Chapter 22 — configuration, variants, product lines. Chapter 23 — observability. Chapter 24 — release discipline and upgrade paths. Chapter 25 — reference project.

Тут достатньо одного питання: що прототип ігнорував, а продукт більше не може ігнорувати?

## Інженерний принцип

Сприймайте successful prototype як evidence, а не architecture. Перед тим як він стане product, відкрийте його assumptions, збережіть simplicity, яка survives, замініть shortcuts, які не survive, і призначте owners для product realities, які prototype ігнорував.

Запитуйте:

- Що prototype насправді довів?
- Які assumptions жили в people, scripts, wiring, fixtures або одному test unit?
- Які shortcuts є harmless implementation details?
- Які shortcuts стають product risk?
- Яка behavior стає product promise?
- Які manual steps мають стати repeatable?
- Які diagnostics потрібні outside the lab?
- Що змінюється для manufacturing, service, updates, variants і release?
- Яка dependency стає support obligation?
- Яка temporary solution потребує owner і expiration?
- Який risk може ship-итися з explicit review trigger?

Мета не в тому, щоб карати prototype speed. Мета — зберегти prototype learning і прибрати invisible promises, які зробили б product fragile.

## Архітектурна вправа

### `Productize One Prototype Assumption`

Оберіть одне prototype assumption. Не беріть увесь prototype. Візьміть assumption, яке зашкодить комусь, якщо стане product behavior без назви.

Запишіть одним реченням assumption. Потім задокументуйте:

1. де assumption живе;
2. чому воно було acceptable у prototype;
3. яку product reality воно зачіпає;
4. owner;
5. available evidence;
6. missing evidence;
7. classification: product contract, implementation detail, temporary risk, evidence gap або removed shortcut;
8. affected surfaces;
9. test або validation needed;
10. manufacturing, service, update, variant або release implication;
11. decision record needed;
12. review trigger або expiration condition.

Завершіть чотирма outputs:

1. одне assumption promoted, removed або explicitly accepted;
2. один owner;
3. один evidence gap;
4. одна prototype-to-product action.

Якщо exercise завершується «clean up later», продовжуйте. Later — не owner.

## Нотатник Principal Engineer

- Prototype — це evidence, а не product promise.
- Зберігайте simplicity, яка survives product reality.
- Кожен shortcut потребує owner, expiration або decision.

## ADR

### Chapter ADR: `Productize the Prototype Configuration Path Before Release Baseline`

#### Status

Accepted.

#### Context

Prototype configuration path працював у lab через manual steps і developer scripts. Firmware lead міг перевести device у правильний state, скопіювати calibration value з bench note, запустити flashing script, застосувати hard-coded customer configuration і прочитати debug log після failure. Для prototype це було acceptable: потрібне було fast evidence, що device behavior має value і configuration idea може працювати.

Product потребує більше. Manufacturing потребує repeatable configuration і calibration path. Service потребує stable product-level rejection reasons і diagnostic visibility для field unit. Variants потребують способу виразити real differences без framework for every future possibility. Update and recovery потребують visible state, коли configuration changes interrupted. Release потребує packaging, який не залежить від local script одного developer.

#### Decision

Зробити prototype configuration path product-ready перед тим, як прийняти його як release baseline. Зберегти intentionally simple and stable частини: narrow device behavior, small configuration surface для першого product, customer-visible flow, який demo довело valuable.

Замінити manual configuration на owned product configuration path. Firmware owns device configuration validation and stored configuration state. Manufacturing owns station step. Service-tool owner owns product-level messages and operator flow. QA owns evidence, що path repeats across supported board revisions and customer configuration paths.

Temporary shortcuts, які залишаються для pilot, мусять мати owner, expiration condition and review trigger. Product-level diagnostics and validation мають розрізняти configuration rejected, unsupported board revision, invalid calibration, interrupted update and unknown device state. Raw debug logs можуть лишатися engineering diagnostics, але не support contract.

#### Consequences

Команда зберігає швидший шлях від prototype до product baseline, бо не переписує доведений behavior і не додає speculative flexibility. Вона отримує explicit ownership для product assumptions: configuration state, calibration path, service messages, temporary shortcuts, vendor/tool dependency surfaces. Cost — видима product work до видимого feature progress, validation assumptions, residual risks and review triggers.

#### Alternatives Considered

- Ship prototype unchanged. Fast, але manual calibration, hard-coded configuration, developer scripts, lab-only update behavior і debug-only diagnosis стають product architecture without owners.
- Rewrite entire architecture before baseline. Cleaner на вигляд, але викидає prototype evidence і створює untested abstractions.
- Add flexibility for every possible future variant. Розширює test matrix, configuration surface, review cost і support burden.
- Defer manufacturing, service and update concerns until after first release. Release baseline не може залежати від invisible manual steps.
- Document assumptions only in comments. Comments не створюють ownership, review triggers або discoverability.
- Freeze prototype behavior immediately. Freeze too early protects hidden assumptions, а не product architecture.

## Коментар редактора

Chapter 20 відкриває Part IV і змінює джерело архітектурного тиску. Part III навчила shape decisions: boundaries, Change Radius, failure and recovery, ADRs, Decision Journal, Architecture Review and Architecture Freeze. Chapter 20 питає, що стається, коли working prototype починає carry product obligations.

Відповідь не «slow down», не «rewrite», не «add process». Відповідь — expose assumptions, які зробили prototype successful, і вирішити, які з них можуть survive as product architecture.

Chapter не має primary PEAK concept. Він anchored by The Successful Prototype (`FAILURE-003`) і Temporary Solution (`ANTIPATTERN-006`), with Simplicity Is a Feature (`LAW-004`), Unused Flexibility Is Waste (`LAW-006`), Evidence Before Confidence (`LAW-005`), state ownership, API promises, dependency decisions, Change Radius, ADRs, Decision Journal, Architecture Review і Discoverability.

Later Part IV chapters ідуть глибше: Chapter 21 - manufacturing and field reality, Chapter 22 - configuration and variants, Chapter 23 - observability, Chapter 24 - release discipline, Chapter 25 - reference project. Chapter 20 creates the doorway: product reality is architecture pressure, and it first appears in the gap between a successful prototype and the product it is expected to become.
