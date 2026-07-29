# Конфігурація, варіанти і продуктові лінійки

## Вступна цитата

> Flag дешевий, доки комусь не треба пообіцяти, що він означає.

## Історія

Команда називала це easy variant. Support пізніше назвав це The Variant That Was Just a Flag.

Це був той самий industrial controller з pilot build. Продукт уже керував pumps у трьох environments, які виглядали схоже, але поводилися інакше після installation. First package served standard industrial sites. Second package added cheaper radio module and slightly different service-tool flow. Third package request asked for same controller, different pressure range, licensed remote-control capability and longer protocol timeout because gateway woke slowly after power loss.

Ніхто не хотів product-line architecture project. Команда щойно пережила prototype-to-product transition і manufacturing/field reality. Product felt more honest: board-revision handling stable, manufacturing provisioning defined, support saw product-level diagnostics, release had enough packaging discipline.

Тому перший instinct був practical: «Can we add one more flag?»

Перші два packages справді shipped that way. Hardware revision flag, region behavior flag, licensed feature flag, customer protocol timeout, manufacturing-mode flag, hidden service-tool option, debug flag left in production, build define for cheaper radio, field override in configuration file. Recovery behavior також depended on package: one could recover over service link, cheaper one needed local cable.

Кожен flag мав story і виглядав розумно сам по собі. Разом вони стали product line.

Manufacturing дало перше warning: station selected regional package, але tested wrong radio behavior because cheaper module selected by build define, not product package record. Unit passed electrical test and provisioning, failed customer installation because service tool expected standard radio capability. Manufacturing engineer said station used package in order. Firmware engineer said radio module was build variant. Support asked which one was authoritative. No quick answer.

Second warning came from update package. Update assumed default configuration for standard package. It was wrong for regional package. Firmware accepted valid package id. Service tool reported success. Unit restarted into legal firmware configuration unsupported for customer. Configuration file said one thing. Package label another. Service tool third. Support script fourth.

Third warning came from licensed remote-control capability. Firmware flag, service-tool button, customer package spreadsheet and release package disagreed. Technician could see button; device rejected command. «unsupported operation» was true but useless. Support could not tell whether license missing, package wrong, firmware image wrong, radio module wrong or recovery mode active. API changed without named promise.

Tests passed examples, not product line. They covered standard package, one regional package, one happy-path update, but not combinations customers, manufacturing, service tooling, release packaging and support had started treating as possible.

Agenda item looked small: Add third product package. Mara wrote first question: «Can we add one more flag?» Then crossed out two words and asked:

> Is this a supported variant, a configuration value, an implementation detail, a temporary exception, or an unsupported combination?

The team listed every difference: board revision, radio module, region behavior, licensed remote control, protocol timeout, manufacturing mode, hidden service-tool option, debug flag, field override, recovery path, default configuration, customer package, update package, diagnostic vocabulary, support horizon.

Then they stopped calling all of them flags.

Protocol timeout was configuration. It selected behavior inside existing product contract and needed owner, default, validation, migration rule, source of truth and support meaning. Cheaper radio module was variant promise: capability, diagnostics, recovery, manufacturing test, update packaging, support behavior. Region behavior was narrower variant promise. Licensed remote control was both configuration and variant promise: license selected exposure, but supported package had to promise firmware command, radio capability, service-tool behavior, diagnostics, recovery compatibility and support path.

Manufacturing-mode flag was not product variant. It was Temporary Solution/Global Configuration: broad switch changing calibration, identity, logging, provisioning and safety checks. Debug flag was not supported customer difference. Hidden service-tool option was promise if support depended on it; otherwise engineering escape hatch. Field override was configuration and Hidden State (`SMELL-004`) because firmware, support and release could not all see or explain it. Build define was dependency decision, not «just build setting».

Mara drew three columns: shared core, variation points, unsupported combinations.

Shared core: pump-control behavior, calibration record shape, identity lifecycle, product-level diagnostic categories, configuration validation rules and update state model. These remain stable across supported packages unless product line intentionally changes.

Variation points team was willing to support: radio capability, region behavior, licensed remote control, customer protocol timing and recovery access. Each needed owner, validation, default, supported combinations, unsupported combinations and discoverable record.

Unsupported combinations changed the room. Cheaper radio plus licensed remote control unsupported for next release because module could not meet recovery promise. Regional package plus old service-tool version unsupported because tool could not show required diagnostic reason. Debug evidence flag unsupported in customer builds. Manufacturing-mode flag unsupported outside station flow. Field override without Decision Journal entry and review trigger unsupported as product-line practice.

Product manager worried unsupported combinations sounded like losing options. Mara answered: «They were not options. They were promises we could not explain.»

Change Radius (`VOCAB-001`, `METRIC-001`) decided ceremony. Protocol timeout affected firmware validation, customer configuration, one service-tool message and tests: Decision Journal enough. Licensed remote control on cheaper module affected firmware, hardware, radio dependency, service-tool behavior, manufacturing test, update recovery, release packaging, support training and field diagnosis: RFC (`ARTIFACT-002`) and Architecture Review (`RITUAL-001`) before hardening.

Shared core and variation points went into Architecture Ledger (`ARTIFACT-006`). ADR (`ARTIFACT-001`) defined product-line boundary before third package. Smaller defaults and temporary exceptions went into Decision Journal (`ARTIFACT-003`). Architecture Freeze (`RITUAL-002`) froze package identity, supported radio capability, diagnostic meaning for unsupported operations and recovery compatibility before release validation.

Team removed two flags: debug flag from production builds and broad manufacturing-mode flag, split into station-owned commands with product-level API promises. Hidden service-tool option either became supported recovery action with stable meaning or disappeared from customer support flows.

Third package shipped slower than flag-only version. It shipped with fewer lies. Manufacturing knew which radio behavior to test. Firmware validated configuration against supported combinations. Service tool explained unsupported capability. Support reproduced field reports because package identity, configuration version, module capability and recovery path were visible. Product line was not grand. It was understandable.

## Обговорення

Configuration and variants become dangerous when the team uses them to avoid naming product decisions.

Thesis: configuration is owned product state. Supported variant is product promise.

A configuration value affects behavior; therefore it needs owner, scope, default, validation, migration path, source of truth and support meaning. A variant is a promise: product can behave, fail, recover, be manufactured, updated and supported in a way someone can trust. Product line is not spreadsheet; it is architecture that lets related products share a core while differing intentionally.

Flags, compile-time defines, configuration files, build variants and spreadsheets are mechanisms. Problem begins when mechanisms are only place where product promises live.

Every State Has One Owner (`LAW-001`) applies to configuration. Firmware may own validation, manufacturing may write first value, service tool may update, release may migrate, support may read. They can participate without all becoming owners of same meaning. Dangerous case: firmware default, manufacturing station value, service tool cache, release assumption and support spreadsheet all carry partial truth.

Every API Is a Promise (`LAW-002`) applies to variants. Regional variant promises radio behavior, label content, manufacturing checks, service-tool warnings, release packaging, diagnostic wording and support instructions. A flag in firmware alone does not fulfill that promise.

Hardware options bring dependencies. Cheaper module imports behavior, capability limits, timing, failure modes, vendor lifecycle, test gaps, update packaging and replacement cost. Every Dependency Is a Decision (`LAW-007`) because product line now relies on what module can and cannot do.

Product-line boundaries name shared core and variation points. Variation point is bounded decision about where difference may enter, not door to every combination. Unsupported combinations are architecture too. If not named, field discovers them by accident.

Good variation is intentional: owner, scope, default, validation, compatibility meaning, support meaning, records and tests. Bad variation hides in global flags, copied defaults, build defines, service-tool options, customer exceptions and field overrides. That is Silent Coupling (`SMELL-001`).

Global Configuration (`ANTIPATTERN-003`) is common trap: one setting controls logging, calibration, connectivity, diagnostics, safety behavior, recovery and service-tool options. Hidden State appears when variant state affects behavior but is not visible through clear owner/interface/model. Platform Leakage appears when hardware/vendor details escape into product variation logic. HAL Everywhere follows when hardware abstraction details shape unrelated product behavior.

Simplicity Is a Feature (`LAW-004`) matters: product line with fewer combinations but direct explanation may be healthier than flexibility everywhere. Unused Flexibility Is Waste (`LAW-006`) keeps generic variation framework from expanding test space before evidence justifies it. Evidence Before Confidence (`LAW-005`) decides what becomes supported.

Records keep product line from oral history. Use ADR for boundaries, shared core, supported/unsupported combinations or long-lived variation point. Use RFC when broad variation point needs review. Use Decision Journal for smaller configuration choices, temporary exceptions, evidence gaps and review triggers. Use Architecture Ledger for active decisions, owners and review dates. Discoverability (`METRIC-003`) is ability to find why a package is supported or unsupported.

Chapter 23 will take observability; Chapter 24 release discipline; Chapter 25 reference project. Here job is narrower: name difference, classify it, own it, bound it, record it, test the promise.

## Інженерний принцип

Treat configuration as owned state and variants as product promises. Keep product line small enough to understand, explicit enough to test, and discoverable enough to support.

Ask:

- Is this difference configuration, supported variant, implementation detail, temporary exception or unsupported?
- Who owns this value or variation point?
- Who may change it?
- What is default?
- How is it validated?
- How does it migrate?
- Which combinations are supported?
- Which are intentionally unsupported?
- Which promise does this variant make to customers, manufacturing, service, release or support?
- What is Change Radius?
- What must be recorded, reviewed, tested or frozen?

Мета не prevent product differences. Мета — make every supported difference explicit enough that product line can keep promises.

## Архітектурна вправа

### `Classify One Product Difference`

Оберіть одну product difference, яка changes behavior, manufacturing, service, release, support, update, recovery або customer promise.

Document:

1. classification: configuration, variant, implementation detail, temporary exception or unsupported combination;
2. owner;
3. who may change it;
4. default;
5. validation rule;
6. migration rule;
7. storage/source of truth;
8. affected state, API, dependency, test, manufacturing, service, release and support surfaces;
9. supported combinations;
10. unsupported combinations;
11. evidence available;
12. decision record needed;
13. review or freeze trigger;
14. expiration/removal trigger if temporary.

End with one classification, one owner, one supported/unsupported boundary, one validation or decision action. If answer is «just add a flag», keep going. Flag is mechanism, not decision.

## Нотатник Principal Engineer

- Flag without owner is hidden state.
- Every supported variant is a promise.
- Cheapest product line is the one you can still understand.

## ADR

### Chapter ADR: `Define Supported Variant Boundaries Before Adding the Third Product Package`

#### Status

Accepted for the chapter.

#### Context

First product package shipped with small configuration differences. Second added cheaper hardware module and service-tool differences. Both reached customers through configuration files, build defines, package labels, service-tool options and temporary flags. Third package adds pressure range, licensed remote-control capability, customer-specific protocol timing and recovery behavior depending on module capability. Current variation model is not explicit enough.

#### Decision

Define supported variant boundaries before third package. Separate configuration values from supported variants. Configuration values need owner, default, validation, migration rule, source of truth and support meaning. Supported variants name behavior, compatibility, manufacturing, service, release, update, recovery and support implications.

Define shared core: pump-control behavior, calibration record shape, identity lifecycle, product-level diagnostic categories, configuration validation rules and update state model. Define variation points: radio capability, region behavior, licensed remote control, customer protocol timing and recovery access. Each has owner, supported/unsupported combinations, validation evidence and discoverable record.

Remove/expire temporary flags that are not supported product behavior. Record consequential product-line decisions in ADR; use RFCs for broad variation points, Decision Journal for smaller choices, Architecture Ledger for active decisions. Require Architecture Review before new variation point with broad Change Radius. Freeze selected variant promises before release validation when needed.

#### Consequences

Product line becomes easier to reason about. Configuration values have owners; supported variants have explicit promises; unsupported combinations are named. Accidental test space shrinks. Supportability improves. Cost: slower feature addition for unsupported combinations, review for customer-specific behavior, maintenance of records, removal of flexibility without evidence.

#### Alternatives Considered

- Add another flag.
- Create separate firmware for each customer.
- Make everything configurable.
- Freeze current variant model immediately.
- Support every combination discovered in field.
- Postpone variant modeling until after next customer ships.

Rejected because they hide promises, duplicate shared core, expand accidental combinations or freeze/ship unowned variation.

## Коментар редактора

Chapter 22 asks what happens when product is no longer one product in one shape. It introduces no primary PEAK concept; configuration, variant, product line, supported combination and unsupported combination are chapter-local working terms. It applies state ownership, API promises, simplicity, evidence, unused flexibility, dependency decisions, Change Radius, Discoverability, ADR, RFC, Decision Journal, Architecture Ledger, Architecture Review, Architecture Freeze, Hidden State, Silent Coupling, Platform Leakage, Global Configuration, Temporary Solution and HAL Everywhere.

This is not a product-management chapter, feature-flag guide, SKU tutorial or build-system guide. It is an architecture chapter about product differences becoming promises.
