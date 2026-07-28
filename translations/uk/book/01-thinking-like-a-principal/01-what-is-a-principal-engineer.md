# Що таке Principal Engineer?

## Opening Quote

> Корисне питання може змінити більше коду, ніж дотепна відповідь.

## Story

Відмова почалася як число на dashboard.

Виробнича лінія почала відбраковувати пристрої з темпом, який нікому не подобався, але ще не зупиняв фабрику. Пристрої завантажувалися. Більшість тестових станцій проходила. Польові логи не показували єдиного crash signature, очевидної регресії чи коміту, який виглядав винним.

Потім патерн змінився.

Одна партія проходила thermal test і падала на калібруванні. Інша поводилася інакше після firmware update. Третя працювала на bench, падала в chamber, а потім змінювала поведінку після power cycling. Кожен відкрив інструменти, яким довіряв: firmware engineers — IDE, test engineers — station logs, hardware engineers — останні board revisions. Хтось почав bisect firmware builds. Хтось порівнював compiler flags.

Principal Engineer приєднався до дзвінка на десять хвилин пізніше.

Він не попросив контроль над debugger. Не спитав, який engineer володіє підозрілим модулем. Не попросив найсвіжішу теорію.

Він запитав: «Що змінилося в системі, але не представлене у firmware diff?»

Дзвінок сповільнився.

Хтось згадав заміну fixture. Хтось інший — невелике оновлення script на calibration station. Manufacturing engineer сказав, що нова партія сенсорів прийшла від того самого vendor, але через інший distribution channel. Release engineer додав, що bootloader не змінювався, але update package format був заново згенерований новішим build container.

Principal Engineer написав на спільному екрані чотири колонки:

- Поведінка продукту
- Тестове середовище
- Supply chain
- Release process

Потім запитав: «Що з цього ми вважаємо частиною системи?»

Ніхто не відповів швидко.

Наступну годину команда не розвʼязувала відмову. Вона змінила форму розслідування. Firmware team перестала припускати, що дефект мусить бути в application. Test team перестала вважати station scripts фоновим шумом. Hardware team перестала вважати нову партію сенсорів еквівалентною лише тому, що part number збігався. Release engineer почав порівнювати generated artifacts, а не тільки source code.

Поворотним моментом був не прихований register і не рідкісний timing trick. Це був момент, коли команда перестала питати «Де bug?» і почала питати «Яке рішення зробило цю відмову можливою?»

Деякі спостереження були хибними слідами. Їхня цінність була в тому, що вони розширили межу розслідування.

Зрештою причина була буденною й дорогою. Калібрувальне припущення було продубльоване у двох місцях. Одна копія жила в station script. Інша — у firmware. Firmware-копію переглядали. Station-копію — ні. Обидві були розумними, коли їх написали. Жодна не була задокументована як shared contract. Невелика варіація постачальника розвела два припущення достатньо далеко, щоб частина пристроїв перетнула межу між acceptable і failing.

Виправлення було не лише зміною коду.

Команда замінила незалежні копії одним authoritative calibration contract. Додала check на divergence. Змінила ownership station script. Додала рішення в ADR, щоб наступний engineer знав, чому ця межа існує.

Principal Engineer майже не торкнувся implementation.

У цьому й був сенс.

## Discussion

Легко описати Principal Engineer як сильнішу версію Senior Engineer: більше досвіду, складніші проблеми, ширший вплив, краще debugging. Це не марні описи, але вони пропускають головну різницю.

Senior Engineers часто безпосередньо розвʼязують складні проблеми.

Principal Engineers теж розвʼязують складні проблеми, але їхній більший внесок — створювати середовище, де складні проблеми стає легше розвʼязувати.

Ця різниця проявляється під тиском. Коли система падає, сильний engineer часто може знайти зламаний рядок, погане припущення, race condition, відсутній timeout або небезпечний state transition. Ця глибина важлива. Розділ не сперечається з технічною силою.

Він ставить інше питання: чому відмову було важко зрозуміти з самого початку?

Чому команда не знала, які припущення були спільними? Чому release review сховав generated artifacts за source diffs? Чому test scripts стали частиною product behavior, але не розглядалися як product architecture? Чому supplier change перетнув межу, яку ніхто не назвав?

Це питання не про інтелект. Це питання про decision system навколо коду.

Більшість коду — це запис уже прийнятих рішень. Деякі рішення явні: protocol version, ownership boundary, retry policy, memory layout, timing budget. Інші неявні: цей module може викликати той; це calibration value означає те саме всюди; ця dependency лишиться стабільною; ця поведінка потрібна лише у manufacturing.

Явні рішення можна назвати, оскаржити, задокументувати й протестувати. Неявні рішення небезпечніші. Вони стають частиною системи, не потрапляючи в памʼять команди.

У термінах PEAK калібрувальна відмова є формою Silent Coupling (`SMELL-001`): поведінкова залежність існувала, але явний contract не робив її видимою.

Саме тому рішення живуть довше за код.

Функцію можуть переписати тричі, поки первинне припущення лишається недоторканим. Модуль можуть перейменувати, поки ownership лишається нечітким. Build system можуть замінити, поки release promises лишаються незадокументованими. Продукт може перейти від prototype до production, поки команда поводиться так, ніби кожне рішення дешеве для зміни.

Principal engineering починається, коли engineer бачить ці приховані безперервності.

Architecture часто описують як структуру: layers, components, dependencies, interfaces, diagrams. Структура важлива, але diagram може показати лише те, що один module залежить від іншого. Він не покаже, чому dependency прийняли, які alternatives відхилили, яку майбутню ціну створили або яке припущення зламає design.

Architecture — це не лише boxes and arrows.

Architecture — це набір рішень, які роблять одні майбутні зміни дешевими, а інші дорогими.

Тому architecture включає рішення про те, коли саме рішення мають бути прийняті. Корисна architecture не відповідає сьогодні на кожне майбутнє питання. Вона створює систему, у якій майбутні питання можна відповісти з меншою шкодою. Вона тримає options відкритими там, де ціна помилки висока. Вона закриває options там, де uncertainty вже розвʼязана. І вона записує різницю.

Ця остання частина важлива. Незадокументоване judgment не масштабується.

Досвідчений engineer може тримати в памʼяті дивовижно багато контексту: чому boot sequence має незручну затримку, чому driver відкриває дивний callback, чому manufacturing test bypass існує, яка dependency стабільна, а яка лише терпиться, бо її заміна затримала б release.

Система працює, поки ця памʼять поруч.

Потім engineer переходить в іншу команду. Або продукт входить у maintenance. Або зʼявляється новий variant. Або customer просить feature, якої ніхто не очікував. Старі рішення лишаються, а reasoning зникає. Команда далі платить ціну, але більше не памʼятає, що купила.

Це unmanaged technical debt у найдорожчій формі.

Technical debt може бути deliberate або accidental. Він зʼявляється, коли команда приймає future remediation cost в обмін на shipping, learning або зменшення поточної складності. Реальна інженерія повна компромісів, і не кожен компроміс шкідливий. Небезпека зростає, коли ціна незадокументована, owner нечіткий, review trigger відсутній або команда забуває, що компроміс був компромісом.

Principal Engineer не усуває компроміс. Principal Engineer робить компроміс достатньо видимим, щоб ним керувати.

Те саме стосується abstraction.

Кожна abstraction створює майбутнє зобовʼязання, але не кожна має однакову вагу. Локальна implementation aid відрізняється від interface, на який покладаються через ownership boundaries, і обидві відрізняються від published або long-lived contract. Якщо abstraction корисна, вона зменшує кількість речей, які reader має тримати в голові одночасно. Якщо вона premature, вона створює ще одне місце, де intent може загубитися.

Питання не в тому: «Чи можемо ми це абстрагувати?»

Краще питання: «Яку майбутню ціну ми приймаємо, якщо ця abstraction стане promise?»

Такі питання є архітектурними інструментами.

Хто owns this state? Що зламається, якщо ця dependency зміниться? Яке припущення спільне для firmware, hardware, manufacturing і release? Яке рішення ми приймаємо, нічого не роблячи? Як наступний engineer дізнається, що це було intentional?

Ці питання не мʼякші за implementation. Вони формують середовище, у якому implementation відбувається.

Команда може витратити тижні, покращуючи не те, якщо перше питання надто вузьке. «Чому це завдання падає?» може привести до local fix. «Чому це завдання може впасти, не залишивши evidence?» вказує на observability. «Чому дві частини системи можуть не погодитися про calibration?» вказує на ownership. «Чому release review це пропустив?» вказує на process.

Один incident може породити patch, test, contract або змінене review rule — залежно від питання, яке веде роботу.

Це не про clever questions у meetings. Це про використання питань, щоб виявити cost до того, як system його сховає. Слабке питання приймає поточну межу проблеми. Краще питання перевіряє, чи ця межа реальна.

В embedded systems хибні межі часті. Firmware вважають окремою від manufacturing. Test scripts — окремими від product behavior. Hardware variation — окремою від software assumptions. Release tooling — окремим від architecture.

Ці розділення можуть бути корисними, але вони є рішеннями. Коли їх не названо, failures можуть переходити з одного domain в інший, не належачи жодному.

Саме тому Principal Engineer на початку incident може виглядати повільнішим. Він не уникає technical work. Він шукає рішення, яке ще матиме значення після immediate defect fix.

Виробнича історія почалася з failure, але failure була не лише у firmware. Вона була в system memory. Команда прийняла рішення про calibration ownership, не назвавши його. Code, scripts, process і people поводилися так, ніби рішення очевидне. Воно не було очевидним. Воно було лише знайоме людям, які були поруч, коли це сталося.

Principal Engineers зменшують future cost, перетворюючи familiarity на structure.

Ця structure може мати багато форм: API boundary, checklist, review ritual, ADR, build rule, test, який падає, коли assumption drift happens, diagram, що називає ownership, або deletion unused option.

Жодна з цих речей сама по собі не вражає.

Їхня цінність зʼявляється пізніше, коли команда може змінити систему, не відкриваючи її історію з нуля.

## Engineering Principle

Architecture — це дисципліна прийняття рішень.

Це engineering principle відкриває handbook, бо змінює те, на що ми звертаємо увагу.

Якщо architecture — лише structure, тоді робота полягає в тому, щоб створити чисту форму. Якщо architecture — decision-making, тоді робота полягає в тому, щоб зробити future change менш дорогою через уважний вибір, відкладання, запис і перегляд рішень.

Деякі рішення треба приймати рано, бо вони створюють stability. Ownership boundaries, safety constraints, update guarantees і product promises часто мають бути explicit до того, як решта system може рухатися безпечно.

Деякі рішення треба відкладати, бо команда ще не має достатньо evidence. Занадто раннє freezing створює false certainty. Воно перетворює guesses на architecture.

Деякі рішення треба документувати, бо їхні consequences переживуть людей у кімнаті.

Деякі commitments, options і constraints треба переглядати й retiring, коли вони вже не купують достатньо value, щоб виправдати cost. Decision record має лишатися discoverable, коли пояснює history system.

Principal Engineer — не людина, яка приймає кожне важливе рішення. Це зробило б system слабшою. Principal Engineer допомагає будувати conditions, у яких important decisions мають visible reasoning, explicit ownership і durable context.

Саме тому роль не можна звести до career badge. Це відповідальність за future cost system.

## Architecture Exercise

Оберіть одне недавнє technical decision зі своєї поточної або недавньої роботи.

Не обирайте найбільше рішення. Оберіть те, що тоді здавалося ordinary: dependency, API shape, timeout, state owner, build rule, test strategy, hardware assumption або release shortcut.

Запишіть короткі відповіді:

- Хто підтримуватиме це через три роки?
- Які припущення воно робить?
- Яку future cost воно створило?
- Чи була ця cost задокументована?

Потім додайте ще два питання:

- Що зробило б це рішення неправильним?
- Як наступний engineer дізнається, чому його прийняли?

Якщо відповіді нечіткі, а рішення має long lifetime, high reversal cost, cross-boundary impact, ownership або compatibility consequences чи впливає на later decisions, воно, ймовірно, є частиною architecture.

## Principal's Notebook

- Питання — архітектурні інструменти.
- Рішення накопичуються.
- Простота потребує безперервної роботи.

## ADR

### Chapter ADR: Why This Handbook Begins With Thinking Instead of Technology

### Context

Handbook міг би початися з embedded technology: C, STM32, RTOS APIs, drivers, scheduling, memory, interrupts або build systems.

Ці теми важливі, але вони не є першою відмінністю, яку handbook має встановити.

Перший розділ представляє Principal Engineer як людину, що проєктує decision system навколо software, а не лише саме software. Книзі потрібна ця основа до обговорення конкретних technical tools.

### Decision

Почати handbook з мислення, якості рішень і architectural judgment замість technology.

### Consequences

- Читач зустрічає роль Principal Engineer через відповідальність за future system cost.
- Пізніші technical chapters можна повʼязати з decision-making, а не трактувати як isolated techniques.
- Книга уникає плутанини з C tutorial, STM32 guide, RTOS reference або career ladder document.
- Перший розділ задає очікування, що stories, ADRs, reviews і exercises є частиною engineering content.

### Alternatives Considered

- Почати з definition ролі Principal Engineer.
- Почати з порівняння Senior Engineer і Principal Engineer.
- Почати з embedded architecture patterns.
- Почати з reference project.

## Editor's Commentary

Цей розділ навмисно уникає technology.

Це не знецінення technical depth. Це sequencing decision. Handbook починається зі способу прийняття рішень, бо technology choices мають сенс лише всередині decision system. Driver boundary, RTOS primitive, hardware abstraction або release process можуть бути добрими чи поганими залежно від assumptions навколо них.

Embedded systems використовуються в handbook, бо вони роблять architectural consequences видимими. Constraints фізичні. Updates можуть бути дорогими. Failures виходять за межі lab. Product lifetimes довгі. Ціна vague decision може жити роками.

Цей розділ встановлює центр ваги handbook: Principal Engineering — це не бути найкмітливішою людиною біля code. Це покращувати conditions, у яких буде розвʼязана наступна важка проблема.
