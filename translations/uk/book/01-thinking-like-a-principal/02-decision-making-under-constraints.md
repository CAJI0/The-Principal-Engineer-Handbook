# Прийняття рішень в умовах обмежень

## Opening Quote

> Обмеження стає рішенням тоді, коли хтось приймає його ціну.

## Story

Release meeting почався з числа, яке ніхто не хотів захищати.

Пристрій наближався до hardware freeze. Enclosure був зафіксований. Battery budget уже узгодили з product team. Qualification plan запланували. Field service готував update procedure. Продукт був не новий, але наступний release мав значення, бо мав лишатися в полі роками.

Команді був потрібен validated і recoverable software update path. Це звучало просто, доки не прийшов memory report.

Поточний product image вміщувався. Recovery capability вміщувалася лише тоді, коли кілька planned diagnostics ставали optional. Diagnostic package вміщувався лише тоді, коли update mechanism лишався простим. Складніший update mechanism міг би повернути простір, але команда не перевірила його в field-like failure conditions. Speculative hooks для future variants теж займали місце: їх додали місяці тому, бо хтось очікував product-line expansion, але жоден variant не був approved.

Змінити hardware було technically possible, але не free. Більша memory part відкрила б qualification work, порушила supply plan і принесла ще один board review саме тоді, коли hardware team намагалася зупинити change. Ніхто не казав, що hardware змінити impossible. Казали, що cost now is high.

Release date мав реальне зовнішнє commitment: customer rollout, field training і manufacturing slots залежали від нього. Дата не була preference, але й не була law of physics.

Перші двадцять хвилин meeting трактував кожен тиск однаково:

«Ми не можемо змінити hardware.»

«Ми не можемо зсунути release.»

«Ми не можемо викинути diagnostics.»

«Ми не можемо shipping without recovery.»

«Ми не можемо прибрати variant hooks.»

«Ми не можемо так пізно будувати compressed updater.»

Одна й та сама фраза приховувала різні види обмежень. Одні були physical limits. Інші — safety and integrity requirements. Деякі були commitments to other groups. Деякі — assumptions, які ніхто не reviewed. Деякі — preferences, сказані з силою обмежень.

Principal Engineer попросив написати options без adjectives:

- Reopen hardware and delay qualification.
- Adopt the complex update mechanism with incomplete evidence.
- Defer lower-value diagnostics.
- Reduce or remove speculative variant flexibility.
- Accept a weaker recovery path.
- Delay the release.
- Keep everything and assume later optimization will recover enough space.

Список нікому не сподобався. Це було корисно.

Потім Principal Engineer запитав повільніше: «Яку ціну ми уникаємо назвати?»

Після паузи кожен вказав на свою cost: qualification delay, customer date, field recovery, брак доказів, service cost. Хтось тихо сказав про variant hooks: «Ми захищаємо option, потребу в якому не довели».

Meeting змінився. Команда більше не шукала option, яка не порушує жодного constraint. Вона вирішувала, який constraint можна challenged, яку cost можна accepted і який risk неприйнятно переносити в field.

Рішення ще не було прийняте.

## Discussion

Meeting змінився, коли команда перестала бачити constraint list як стіну.

Деякі стіни реальні. Memory part має capacity. Battery має limits. Watchdog window не переконується optimism. Update path, який не recover from interruption, не стає safe через confident meeting. Такі constraints заслуговують respect, бо їх порушення змінює system, а не тільки plan.

Інші constraints є commitments. Їх може бути дорого renegotiate, але вони не physical facts. Release date можна moved, якщо organization accepts cost. Feature promise можна narrowed, якщо product consequence understood. Qualification plan можна reopen, якщо alternative is worse. Називати це impossible занадто рано — значить не дати engineering judgment зробити свою роботу.

Третя група небезпечніша, бо звучить як knowledge. Assumptions часто входять у room dressed as facts: future variant will need hooks; compressed updater will be fine; service cannot operate without full diagnostics; customers will not tolerate a slip; later optimization will recover space. Будь-що з цього може бути true. Нічому не можна дозволяти harden without evidence.

Principal Engineer не покращив decision, просто ранжуючи concerns. Корисний рух був у тому, щоб розділити різні kinds of pressure.

Recoverable update path належав до hard part. Field device, який не recover from failed update, переносить cost у найгірше місце: customer environment. Cost — це не тільки repair time, а й trust, service capacity, support load і можливість deliver future fix safely.

Hardware change був іншим: possible, but costly. Він міг бути right decision, якби software options були unsafe або dishonest. Але команда мала credible ways to reduce scope without weakening recovery.

Release date був commitment із owners outside engineering. Його не можна dismiss, але він не може сам вирішити technical risk. Deadline може пояснити, чому compromise considered. Він не erase compromise.

Complex update mechanism був tempting option, бо ніби зберігав release date, diagnostics, recovery, hardware plan і future flexibility. Саме тому він заслужив suspicion. Рішення, яке late in release задовольняє every constraint, часто переносить uncertainty з meeting у field.

Prototype update engineer мав значення. Це були докази, але не достатні докази для commitment. Його не interrupted during worst-case writes, не tested across oldest supported deployed images, не reviewed for partial transfer recovery, не exercised by field service. Команда мала confidence, що mechanism could be made to work, але ще не докази, що він should become release path for long-lived product.

Це Evidence Before Confidence (`LAW-005`) у практиці. Закон не каже чекати perfect proof. Він каже, що confidence має йти за доказами, а не замінювати їх.

Weaker recovery path був гіршим option. Він виглядав меншим, бо не disturb visible plan. Але його cost платили б field teams, support teams, customers і engineers наступного update.

Keep everything and hope for later optimization не був plan. Це transfer of decision cost to future engineer with less time. Optimization може бути real engineering work. Hope — ні. Якщо команда залежить від optimization, потрібні evidence, ownership і review trigger.

Лишилися чесні options: defer part of diagnostics, remove speculative variant hooks, preserve recovery path і keep update mechanism simple enough to validate. Це не робило release painless. Воно зменшувало scope, щоб захистити property, яку product найменше міг втратити.

Немає best option в abstract. Responsible choice залежить від обмежень, доказів, uncertainty, consequences і reversibility перед командою. Кожна option щось витрачає.

Обраний напрям витратив product scope і частину future optionality. Він захистив recovery, qualification evidence і release predictability. Він також створив cost для product і service teams, бо deferred diagnostics треба буде wait або narrow. Ця cost потребувала owner.

Команда challenged constraints, не вдаючи, що всі constraints можна removed. Memory limit, recovery requirement і external date лишилися real. Assumption про speculative variant hooks не пережило discussion. Assumption про готовність complex updater теж.

Simplicity mattered не тому, що simple designs morally superior. Simplicity Is a Feature (`LAW-004`), бо вона preserves reviewability, testability і explanation under pressure.

Flexibility mattered теж. Команда не видалила flexibility, бо flexibility погана. Вона прибрала flexibility, яка не protected against real evidenced uncertainty. Unused Flexibility Is Waste (`LAW-006`), коли вона consumes memory, test cases, review attention і release margin without committed reason.

Change Radius (`VOCAB-001`) допоміг описати consequence of being wrong. Помилка deferred diagnostics болюча, але bounded. Помилка recovery path торкнеться update tooling, field service, support, customer trust і possibly every deployed device that needs a fix.

Reversibility змінила evidence threshold. Deferring diagnostics more reversible than shipping fragile update path. Removing speculative hooks можна revisit when variant has evidence. Complex updater main release path hard to reverse after deployment. Що дорожче reversal, то більше доказів треба before committing.

Команда зрештою обрала narrower release:

- Preserve the recoverable update path.
- Keep the update mechanism simple enough to validate with current evidence.
- Defer a lower-value part of the diagnostic package.
- Remove speculative variant hooks that had no committed owner.
- Record a review trigger for the next hardware revision or stronger update-mechanism evidence.

Рішення не удавало, що uncertainty disappeared. Воно зробило uncertainty visible enough to own.

Compact Decision Journal (`ARTIFACT-003`) entry captured the reasoning:

```text
Date: 2026-07-04
Decision: Preserve recoverable updates by reducing release scope and removing unowned variant hooks.
Evidence: Current image and recovery capability fit after scope reduction; complex updater has only prototype evidence;
hardware change would reopen qualification; no approved variant currently depends on the hooks.
Confidence: Medium. Recovery behavior is supported by existing validation; diagnostic deferral carries product and service cost.
Review trigger: Revisit for the next hardware revision, an approved variant, or field-like evidence for the complex update mechanism.
```

Цей запис не ceremony. Це guardrail against future misremembering.

Decision quality не дорівнює outcome quality. Narrowed release може still cause pain, а careless decision може get lucky. Responsible decision оцінюють за тим, що team did with what it could know: exposed assumptions, separated evidence from confidence, examined alternatives, named consequence, assigned ownership і defined revisit trigger.

Constraints are not excuses. They are part of the decision.

Deadline не absolve team from field risk. Memory limit не absolve from product scope consequences. Qualification plan не absolve from revisiting hardware if software options unsafe. Constraints explain why compromise exists. Вони не make cost disappear.

Саме тому constrained decision-making central to principal engineering. Робота не в тому, щоб знайти pure option. Її може не бути. Робота — make accepted cost explicit before the system hides it.

## Engineering Principle

Sound engineering decision робить обмеження, докази, uncertainty, consequences і cost of reversal explicit before committing.

Цей principle не remove інженерне судження і не guarantee success. Він змінює quality of commitment.

Коли constraints visible, їх можна honestly challenged. Коли evidence named, confidence calibrated. Коли uncertainty recorded, future engineers know what to revisit. Коли consequences мають owners, risk stops drifting silently. Коли reversal cost understood, team can decide how much evidence decision deserves.

Goal не remove all risk. Goal — знати, який risk team accepts, why, і when decision must be opened again.

## Architecture Exercise

Оберіть current або recent engineering decision, де жодна option не задовольняла every demand.

Дайте короткі відповіді:

- What decision is being made?
- What outcome are you trying to protect?
- Which constraints are genuinely hard?
- Which commitments might be renegotiated?
- Which assumptions are being treated as facts?
- What remains unknown?
- What evidence is available?
- What is the cost of being wrong?
- What is its Change Radius?
- How reversible is the decision?
- Who owns the accepted risk?
- What review trigger would reopen the decision?

Потім останнє питання:

Що б ви обрали, якби goal був не remove all risk, а make accepted risk explicit and recoverable?

## Principal's Notebook

- Constraints must be visible before they can be challenged.
- Reversibility buys learning, not safety.
- Deadlines transfer risk; they do not erase it.

## ADR

### Chapter ADR: Preserve Recovery by Reducing Scope

### Context

Команда наближається до hardware and release freeze для long-lived field device. Поточний memory budget не підтримує комфортно product image, recovery capability, усі planned diagnostics і speculative flexibility для possible future variants.

Changing hardware would reopen qualification. More complex update mechanism lacks sufficient field-like evidence. Weaker recovery path would transfer risk into deployed devices. Keeping all planned functionality would depend on unsupported optimism about later optimization.

### Decision

Preserve the recoverable update path and keep the update mechanism simple enough to validate with current evidence. Reduce release scope by deferring lower-value diagnostics and removing speculative variant flexibility that has no committed owner.

Record remaining uncertainty and revisit decision when future hardware revision, approved variant, or stronger update-mechanism evidence changes constraints.

### Consequences

- Field recovery remains a protected product property.
- Release avoids adopting insufficiently evidenced complex update mechanism.
- Qualification evidence already earned by hardware team remains useful.
- Product and service teams absorb cost of reduced or deferred diagnostics.
- Future variant work may need to reintroduce flexibility with clearer evidence and ownership.
- Decision requires review trigger so temporary scope reduction does not become forgotten architecture.

### Alternatives Considered

- Reopen the hardware design and delay qualification.
- Adopt the complex update mechanism based on prototype evidence.
- Accept a weaker recovery path to preserve diagnostics and flexibility.
- Delay the release until every planned capability fits comfortably.
- Keep speculative flexibility and assume later optimization will recover enough space.

## Editor's Commentary

Chapter 1 established principal engineering as responsibility for future system cost. Chapter 2 показує, як це виглядає, коли every available option spends something the team would rather keep.

Constrained decisions — це місце, де engineering judgment стає visible. Легко говорити прямо, коли одна option safe, cheap, simple і reversible. Real systems рідко дають таку доброту near release, hardware freeze, field deployment або product commitment.

Chapter не teaches decision algorithm. Він просить reader slow decision down enough to see what kind of constraint is being discussed, what evidence exists, what uncertainty remains, what cost accepted, and who owns that cost later.

Це готує наступний chapter, Asking Better Engineering Questions. Chapter 2 робить constrained commitment legible. Наступний крок — learn how better questions expose shape of commitment before system hardens around it.
