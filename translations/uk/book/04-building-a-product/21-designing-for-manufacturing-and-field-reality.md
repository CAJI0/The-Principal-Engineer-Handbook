# Проєктування для виробництва і польової реальності

## Вступна цитата

> Продукт готовий не тоді, коли він працює для інженерів. Він готовий тоді, коли його можна зібрати й зрозуміти без них.

## Історія

Команда називала pilot unit «тим, що нарешті відчувалося реальним». Пізніше incident file дасть йому простішу назву: The Product That Only Worked in Engineering.

Це був невеликий industrial controller для pump, двох pressure sensors, valve і wireless service link. Попередній prototype був impressive but fragile. Він працював на engineering bench, бо ті самі троє людей, які писали firmware, також знали, як load, adjust, recover і explain його дивні моменти. Робота Chapter 20 допомогла рухатися далі: update path уже не був private developer ritual, configuration мала яснішу shape, service tool був product surface, а architecture review прибрала obvious prototype shortcuts.

До pilot build unit проходив lab test plan: чистий startup, pump control у target band, update sequence, service tool connect/read/apply configuration, stack boards behaved consistently enough. Product manager міг показати unit customer без engineer із cable поруч.

Потім почався manufacturing run. Contract manufacturer подзвонив на другий ранок: calibration step тривав занадто довго. На engineering bench calibration означало connect device, warm sensor, run script, wait pressure fixture settle, nudge offset, rerun script if result looked odd. Це було нормально, коли engineer owns one unit at a time. На line speed - ні. Operator мав 90 seconds. Script sometimes needed four minutes і просив judgment call: «Does this slope look normal?»

Manufacturing lead зробив local instruction sheet: якщо offset drift small - accept; якщо script hung - power-cycle and retry; якщо fixture cannot reach debug connector after enclosure - calibrate before final assembly and hope gasket compression changes nothing. Це виглядало як line-side pragmatism, не architecture. До пʼятниці це було architecture.

Перший batch показав три behaviors. Original board revision calibrated in expected range. New board revision needed different timing window. Substitute sensor from approved alternate supplier needed different offset curve. Firmware could handle all three, if engineer knew which case was present, loaded right constants, and validated manually. Сам product цього не знав. Він не мав owned model of manufacturing-visible calibration state.

Device identity and provisioning були гірші. Identity assigned in spreadsheet після electrical test, provisioning depended on station script writing values, які product explicitly не model-ив. Service tool міг read identity, якщо її вже written, але не було product contract: when identity becomes valid, who owns it, what if unit leaves line without it. Spreadsheet стала state owner. Station script - another. Firmware мала third partial opinion через cache after first boot. Warehouse labels - fourth. Коли support later asked whether returned unit had substitute sensor, nobody could answer from product record alone.

Every State Has One Owner (`LAW-001`) уже навчила: meaningful state needs one clear owner. У lab device identity, calibration status, fixture result, board revision здавалися setup details. In manufacturing they were product state. Без owner кожен process invented partial owner.

First field trial сказав те саме різкіше. Units встановили на трьох customer sites: stable power, noisy long cable runs, pump close to power budget. Service calls стали unreadable. Support відкрив service tool і побачив raw developer states:

- `BOOT_WAIT_SENSOR`
- `CFG_PENDING`
- `CAL_DIRTY`
- `SAFE_HOLD_3`
- `UPD_RECOVERY_ARMED`

Ці names щось означали firmware team, але не support. Technician could see `SAFE_HOLD_3`, але не whether it meant pressure sensor mismatch, missing calibration record, update recovery guard або field wiring problem. Tool exposed internal states instead of support-safe diagnosis.

One unit reset during update. Update design був кращий за prototype path, але recovery still assumed developer laptop and private cable. Field technician не мав жодного з них. Support script сказав return the unit. Firmware engineer сказав: «It is recoverable. You just have to connect with the engineering tool and run the loader in manual mode.» Це завершило argument. Recoverable by developer in lab is not recoverable in field.

Another unit lost field logs after reset. Team ставилася до logs як до convenience surface. In field logs were evidence. Reset прибрав pressure readings, update attempt, configuration version і voltage warning. Evidence Before Confidence (`LAW-005`) стало product obligation, коли engineers були absent.

Product manager запитав: «Why did manufacturing and the field break the architecture?» Mara, principal engineer, відповіла: «They did not break it. They revealed which realities were missing from the contract.»

Вона відокремила process details від architectural promises. Manufacturing line може вибирати station layout, operator steps, label placement і fixture timing. Architecture still must say what product state exists, who owns it, which surfaces can write it, and what evidence proves it correct.

Вона назвала assumptions, які lab ховав: calibration assumed developer judgment; identity/provisioning assumed spreadsheet and script correct; fixture access assumed debug connector after enclosure; board revision handling assumed engineer knew revision; service diagnosis assumed support could translate firmware states; update recovery assumed developer laptop; field evidence assumed device alive long enough to pull logs; component substitution assumed equivalent electrical behavior meant equivalent product behavior.

Потім вона попросила owners. Firmware owned product model for calibration status, not station script. Manufacturing owned fixture process, but fixture writes only through product API with defined promise. Hardware owned board revision encoding and exposed it via product-level interface. Support owned service diagnosis vocabulary; firmware owned mapping from internal state to support-safe reason. Release owned field recovery path; product architecture had to make recovery possible without developer-only tools.

Every API Is a Promise (`LAW-002`) стало uncomfortable usefully: calibration script was not `just a script`, якщо manufacturing depended on it; service tool state view was not `just debug output`, якщо support used it; recovery command was not `just engineering access`, якщо field plan relied on it.

Every Dependency Is a Decision (`LAW-007`) applied to pressure fixture, station script, alternate sensor, board revision encoding, label printer, spreadsheet, service laptop, field cable і update loader. Кожна dependency imported behavior, failure modes, ownership boundaries і replacement cost.

First temptation: broad manufacturing mode. One flag unlocking calibration bypasses, raw state writes, fixture commands, serial number changes і extra logs. Це звучало швидко; насправді це була Global Configuration (`ANTIPATTERN-003`) wearing a factory badge. One setting would affect calibration, identity, logging, update behavior, safety holds і support diagnostics, increasing Change Radius (`VOCAB-001`, `METRIC-001`).

Mara pushed for smaller surfaces. Calibration needed product-owned record with status, version, source, evidence і validation result. Station could request calibration, write measurements і receive product-level pass/fail reason, але not create hidden state model. Identity needed lifecycle: unassigned, assigned, verified, retired. Fixture access needed surface available at assembly point. Board revision needed product-level capability description. Service diagnosis needed stable vocabulary. Update recovery needed field path without developer laptop. Logs needed enough persistence to preserve last useful evidence after reset.

Highest-consequence choices пішли в ADR. Smaller evidence gaps - у Decision Journal entries. First field escape створив Mistake Ledger entry: «If recovery works on a developer laptop, it is field recovery.» False.

Architecture Review (`RITUAL-001`) reviewed architecture surfaces manufacturing and support would depend on: calibration ownership, identity lifecycle, fixture contract, diagnostic vocabulary, update recovery, traceability record. Before pilot build, Architecture Freeze (`RITUAL-002`) froze only a few decisions: calibration record shape, service diagnosis vocabulary, identity lifecycle, recovery contract. Temporary and named; it did not freeze learning from line or field.

Result був not glamorous. Unit виглядав так само. Pump still turned on. Enclosure barely changed. Але product survived places where engineers were absent. Manufacturing no longer inferred calibration validity. Fixture received product-level errors. Board revision carried capability description without HAL Everywhere (`ANTIPATTERN-002`). Service tool showed support reasons tied to configuration, calibration, hardware, firmware, environment evidence. Logs preserved last trace across reset. Component substitution became decision with evidence. Line workaround міг still happen, але якщо він changed product behavior, йому були потрібні owner, review trigger і removal condition; інакше Temporary Solution (`ANTIPATTERN-006`) would become permanent.

Pilot still found problems. Good pilots do. One sensor lot had narrower stable range. One support message was vague. One recovery instruction was hard under pressure. Але problems були visible, owned, evidenced і recorded.

Product crossed a boundary, яку lab не міг simulate: він став architecture for people who were not in the room when architecture was designed.

## Обговорення

Manufacturing reality and field reality - не late-stage cleanup. Це design inputs.

Lab дає unusual advantages: knowledgeable engineers, direct board access, private tools, flexible timing, forgiving setup, people who remember why strange behavior is acceptable. Manufacturing and field use прибирають ці advantages. Вони питають, чи product can be built repeatedly, configured correctly, calibrated safely, identified reliably, recovered without developers, diagnosed by support і explained from evidence.

Architecture не має contain every manufacturing procedure. Manufacturing process decides how line runs. Product architecture decides what state exists, who owns it, which surfaces can change it, and what evidence proves it. Field service process decides how support works with customers. Product architecture decides which diagnosis, recovery, traceability and configuration promises that process can trust.

Repeatability - first pressure. Prototype often succeeds through skilled repetition. Manufacturing needs ordinary repetition: shift changes, fixture variation, component lots, board revisions, enclosure constraints, line timing. If step requires judgment, architecture should say which judgment belongs to person and which becomes product decision with clear result.

Calibration example: dangerous question is not «Can unit be calibrated?» Better: what does product know after calibration, who owns that state, how is it validated, what does system promise? Без answer calibration becomes Hidden State (`SMELL-004`).

Identity, provisioning and traceability create similar pressure. Serial number is not only label. It connects hardware revision, component lot, firmware version, configuration, calibration, field history and support action. If identity is assigned by spreadsheet, label printer, station script and firmware cache without one product contract, product has Silent Coupling (`SMELL-001`).

Fixture access is architecture when product relies on it. A debug connector hidden inside enclosure is not manufacturing detail if calibration, identity or recovery depends on it after assembly. Architecture defines product-level contract fixture uses, where in assembly flow it is available, and what evidence fixture returns.

Diagnostics matter because field makes ambiguity expensive. Developer states are precise in wrong language. Support-safe diagnostic surface should separate configuration, hardware, firmware, environment, update and calibration causes, preserve evidence and avoid requiring support to remember private firmware meanings.

Update recovery is same promise. Product is recoverable when intended support/field path can recover it under realistic access, tooling, time, power and network constraints. Private tools are not field recovery.

Architecture should resist broad catch-all modes. Single manufacturing flag or field-service flag often creates Global Configuration. Smaller owned surfaces are easier to reason about.

Evidence Before Confidence matters here: lab success is evidence for lab conditions. Pilot manufacturing, component substitution, enclosure assembly, field wiring, customer configuration and support use need their own evidence.

Discoverability (`METRIC-003`) becomes product quality. Future maintainer should find decision, owner and contract behind calibration ownership, identity lifecycle, diagnostic vocabulary, recovery path and traceability record. ADRs, Decision Journal and Mistake Ledger entries keep reality attached to architecture.

This chapter is not a manufacturing handbook, field-service manual, fixture-design guide, observability chapter or release-process chapter. Він makes manufacturing and field assumptions explicit before pilot use depends on them.

## Інженерний принцип

Проєктуйте продукт для місць, де інженерів немає. Manufacturing and field reality require architecture to make identity, calibration, configuration, diagnostics, recovery, traceability і ownership explicit before the product depends on them.

Запитуйте:

1. На який state покладатимуться manufacturing або support?
2. Хто owns that state?
3. Яка surface може create, change, validate або retire it?
4. Що product promises about calibration, identity, configuration and recovery?
5. Які assumptions live in scripts, spreadsheets, private tools або team memory?
6. Яка field evidence має survive reset, update failure або loss of connection?
7. Чи може support separate configuration, hardware, firmware, environment і calibration causes?
8. Яка dependency has manufacturing or field path quietly imported?
9. Який Change Radius, якщо assumption wrong?
10. Яка evidence exists outside lab?
11. Де future engineer знайде owner, contract, decision і review trigger?

Мета не perfection before pilot manufacturing. Мета - не дати product залежати від invisible engineering presence.

## Архітектурна вправа

### `Expose One Manufacturing or Field Assumption`

Оберіть product behavior, яка works in lab and matters in manufacturing or field: calibration, identity, fixture access, service diagnostics, update recovery, configuration assignment, field logs after reset, component substitution або board revision handling.

Опрацюйте assumption:

1. Describe lab behavior in one sentence.
2. Name manufacturing or field condition that changes behavior.
3. Identify current hidden assumption.
4. Name state, dependency, API promise or evidence gap.
5. Decide owner.
6. Decide architectural surface to add/change/make explicit.
7. Define validation action outside lab.
8. Record ADR, Decision Journal or Mistake Ledger.

End with one assumption, one owner, one architectural surface, one evidence or validation action.

## Нотатник Principal Engineer

- Lab is not the environment.
- Diagnostics matter most when developers are absent.
- Workaround becomes architecture when no one owns it.

## ADR

### Chapter ADR: `Make Calibration and Recovery Product Responsibilities Before Pilot Manufacturing`

#### Status

Accepted for the chapter.

#### Context

Product works in lab after prototype-to-product transition. Configuration clearer, service tool exists, updates can be tested by engineering. Pilot build approaches. Remaining risk: product obligations still assume engineering presence: developer-assisted calibration scripts, recovery through developer laptop/private cable, identity via spreadsheet/station script, fixture access through debug connector, raw developer states in service diagnostics, field logs lost after reset.

#### Decision

Make calibration ownership explicit. Firmware-owned calibration record includes status, version, source, validation result and enough evidence for manufacturing/support. Provide manufacturing-safe calibration/provisioning path: fixture requests calibration, submits measurements, provisions required identity/setup values through product contract, receives product-level pass/fail reasons. It cannot create separate hidden state model.

Define minimum service-visible diagnostic vocabulary separating configuration, hardware, firmware, environment, update and calibration causes. Make update recovery possible without developer tools. Treat identity and traceability as architecture contracts: lifecycle, ownership, validation and fields connecting board revision, component substitution, firmware, configuration, calibration and field evidence.

Record residual assumptions and review triggers in ADR, Decision Journal and Mistake Ledger as appropriate. Defer deeper variants, observability, release discipline and reference-project examples to later Part IV chapters.

#### Consequences

Manufacturing can build repeatable units without private engineering judgment. Support can diagnose through product-level reasons. Calibration, identity, recovery and traceability have owners. Cost: more integration work before pilot, cross-owner agreement, evidence outside lab and constraints on future variants.

#### Alternatives Considered

- Let manufacturing own the workaround.
- Keep developer scripts and train the line.
- Add broad manufacturing mode.
- Postpone service diagnostics until after field trial.
- Rely on release notes and support training.
- Rework full architecture before pilot.

All were rejected because they either hide ownership, depend on engineering presence, create Global Configuration, weaken field learning, or are broader than current evidence.

## Коментар редактора

Chapter 21 asks whether product decisions survive manufacturing and field reality when engineers are absent. It introduces no new PEAK concept. It applies Every State Has One Owner (`LAW-001`), Every API Is a Promise (`LAW-002`), Evidence Before Confidence (`LAW-005`), Every Dependency Is a Decision (`LAW-007`), Change Radius, Discoverability, ADR, Decision Journal, Mistake Ledger, Architecture Review, Architecture Freeze, Temporary Solution, Hidden State, Silent Coupling, Platform Leakage, HAL Everywhere and Global Configuration.

Boundary is deliberate: not a manufacturing handbook or service manual, but an architecture chapter about explicit manufacturing and field assumptions. Chapter 22 can now take configuration and product lines; Chapter 23 observability; Chapter 24 release; Chapter 25 reference project.
