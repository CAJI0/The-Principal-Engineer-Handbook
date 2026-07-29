# Прохід референсним проєктом

## Вступна цитата

> Продукт — це не одне рішення, зроблене добре. Це ланцюг рішень, які все ще можна знайти, коли поле питає чому.

## Історія

### Один продукт, пʼять точок тиску

Prototype був достатньо малим для одного bench і достатньо складним, щоб стати product.

Команда називала його Field Sensor Gateway. Він sampled one field sensor, stored local configuration, reported readings over low-power radio link and exposed simple service tool for setup and diagnosis. First customer wanted pilot. Prototype proved sensor reading useful, reporting path worked in lab, technician could change basic configuration without rebuilding firmware.

It was focused prototype: hard-coded reporting interval, manual calibration for five units, service tool showing developer logs, firmware update through lab cable/script, latest build updating to next build on bench, one hardware revision, one sensor offset, one radio module, one configuration shape, one customer package.

Prototype success created pressure. Sales wanted ten pilot units. Manufacturing wanted serial identity and calibration flow. Support wanted diagnose radio failures without firmware engineer reading raw logs. Product owner wanted regional package with longer reporting interval and another package with different radio option. Customer asked special timeout because gateway disappeared for minutes. Release wanted v1.1 with new configuration schema. Field units on v1.0 and v1.0.2 already existed.

Each pressure looked local. Firmware could replace hard-coded interval with setting. Manufacturing could add station file. Support could get richer log. Service-tool owner could add regional toggle. Release could add migration. Radio owner could tune retry. None wrong alone; together they would create product nobody could explain.

First argument: reporting interval. One engineer wanted global `reportingInterval` in non-volatile configuration. Manufacturing writes it, service tool edits it, firmware reads it, regional package sets default, special timeout another value. Simple until combinations appeared: standard every ten minutes; regional every thirty; battery package longer interval plus different retry; special customer timeout not reporting interval at all but gateway-absence tolerance. One broad value would look flexible while nobody owned promise.

Mara asked:

> Which difference are we promising to support, and which difference are we only tolerating for the pilot?

Regional reporting interval became supported variant promise. Battery package deferred because it changed measurement cadence, retry timing and field-support expectations. Special customer timeout became pilot exception with owner and review trigger. Global setting disappeared. Configuration became owned state, not hiding place for product difference.

Second argument: manufacturing. Station could write serial identity and calibration. Authority was problem. Manufacturing measured calibration; firmware used it; service tool could request recalibration; v1.1 migration needed preserve it; older hardware revision stored backup differently; recovery could restore firmware but not know calibration still matched hardware revision without owner. Team named state owners: manufacturing owns first measurement/evidence, firmware owns runtime calibration state and validation rules, service tool requests workflow but cannot write raw product truth, release owns migration evidence, support owns field procedure. Device reports serial identity, hardware revision, calibration version, active configuration fingerprint and firmware version in support-safe diagnostic snapshot.

Third argument: second board revision. Sensor offset changed. Happy path looked fine. Old calibration flow, service-tool label, event meaning and v1.0 update path now depended on hardware revision. Team almost added flag. Mara asked trace Change Radius. It touched firmware validation, station programming, service-tool display, field diagnostics, release notes, migration evidence, support scripts and Event Catalog. Not local flag; product promise. Team opened RFC for hardware-revision and configuration compatibility across firmware, manufacturing, service tooling, QA, support and release.

Fourth pressure: field. Three pilot units stopped reporting after v1.1 update. Two completed migration and lost radio contact during first report. One rejected configuration migration because regional package used old field name. Service tool showed same message: update failed. True but useless.

Support needed identity, active firmware, configuration fingerprint, variant, calibration validity and rejected boundary. Team wrote first Event Catalog entries:

- `upgrade_started`: accepted package and recorded source version, target version, hardware revision and variant.
- `configuration_migration_rejected`: firmware rejected migration and preserved source configuration.
- `first_report_not_acknowledged`: radio path missed expected acknowledgement within supported retry window.
- `recovery_ready`: device entered supportable recovery state with identity, calibration state, active version and configuration fingerprint.

Each event had owner, producer, consumer, ordering assumption and failure meaning. Event Explosion was risk on one side; Hidden State on the other. Team chose fewer events with sharper meaning.

Fifth pressure: release. v1.1 changed configuration schema. Latest lab build upgraded cleanly, but field units existed on v1.0 and v1.0.2. Hardware revision needed different calibration migration. Regional variant had different reporting interval and radio option. Special timeout was pilot exception, not supported variant. Rollback could return executable but lose migrated configuration meaning unless source snapshot and calibration state preserved.

Release owner asked: «Can we ship v1.1?» Mara asked:

> Which product baseline are we promising, and what evidence keeps that promise true?

Team built decision chain instead of checklist. Prototype assumptions became owned product decisions. Hard-coded interval became regional variant default, not global setting. Manual calibration became manufacturing measurement with firmware ownership of runtime validity. Developer logs became support-safe diagnostics tied to event meanings. Lab-only update script became release path with supported source versions and recovery behavior.

Supported pilot baseline: hardware revisions A and B, standard and regional packages, configuration schema v2, service tool 4.3+, direct upgrade v1.0.2 to v1.1, upgrade v1.0 to v1.1 only through intermediate migration package. Special customer timeout remained pilot exception in Decision Journal with review trigger after thirty field days or second customer request. Battery package deferred. Older service tool rejected for v1.1 upgrade.

Unsupported combinations: revision A with unvalidated calibration backup cannot directly upgrade; regional package cannot use special timeout; battery package cannot be hidden flags; v1.0 cannot skip intermediate migration; service tool older than 4.3 cannot upgrade; factory reset not default recovery because it destroys identity, calibration evidence and trust.

Records: pilot baseline in ADR; compatibility proposal in RFC; special timeout in Decision Journal; event meanings in Event Catalog; active decisions in Architecture Ledger; escaped assumption «latest lab update proves field update readiness» in Mistake Ledger.

Review and freeze: Architecture Review for broad compatibility decision crossing firmware, manufacturing, service tooling, support, QA, release and field behavior. Architecture Freeze narrowly for v1.1 upgrade-path validation: supported paths, migration rules, service-tool compatibility, event meanings, release-critical state owners and recovery behavior. Bug fixes could continue if preserving decisions; changes required exception, owner review, record updates and evidence.

Pilot did not become perfect. It became supportable. When unit stopped reporting, support saw source version, target version, active variant, configuration fingerprint, hardware revision, calibration state, reset reason, migration result and first-report outcome. They knew difference between radio acknowledgement failure and rejected migration, when rollback safe, when retry enough, when forward-fix honest. Future engineers could find baseline decision, unsupported combinations, event meanings, review notes and reopen conditions.

That is walkthrough: not universal design or reference implementation, but chain of decisions that held together when product left bench.

## Обговорення

Reference project is useful when it connects decisions. If Field Sensor Gateway becomes product specification, it argues with real systems. If code walkthrough, it teaches mechanics. If recap, it repeats. Useful question:

> If we had to take one embedded product from prototype to supported release, which architecture decisions would we make, record, test, review, freeze, and revisit?

Answer is a chain.

Prototype proved useful behavior under prototype conditions. It did not prove manufacturing repeatability, field diagnosis, regional variants, release compatibility, calibration migration, support horizon or interrupted reporting recovery. That distinction is Chapter 20: successful prototype is evidence, not baseline.

First product move exposes assumptions and decides promises. Hard-coded interval may become regional variant promise, battery trade-off, support expectation, radio dependency and release compatibility concern. Manual calibration becomes identity, manufacturing evidence, firmware validation, support diagnosis and migration behavior. Developer logs help bring-up but support needs stable product meaning.

State ownership appears early. Identity, calibration, configuration, variant, event meaning, update state and recovery state decide what product may do and support can believe. Every State Has One Owner (`LAW-001`) separates explainable device from competing truths across firmware, station scripts, service tools, release packages and support notes.

API promises appear next. Service-tool command, diagnostic event, configuration file, regional package, update package, station record or support note may feel informal until another surface depends on it. Every API Is a Promise (`LAW-002`) and API Stability (`METRIC-004`) mean promise must survive change without surprising dependents.

Dependencies become visible off bench. Radio link brings retry behavior, timing assumptions, acknowledgements, gateway compatibility, field failure modes and support cost. Service tool decides what technicians see/install/recover. Manufacturing fixture creates identity and calibration evidence. Every Dependency Is a Decision (`LAW-007`).

Time becomes product concern: reporting intervals, gateway absence tolerance, update windows, retry timing, event ordering, support horizons and revisit triggers. Time Is a Dependency (`LAW-003`) because bench behavior can fail when device sleeps, misses acknowledgement, updates during service window or waits for support.

Manufacturing and field reality make baseline honest. Product needs serial identity, calibration ownership, fixture/service boundaries. Configuration and variants force deliberate difference. Regional interval is supported variant; special timeout is pilot exception; battery package deferred. Simplicity Is a Feature (`LAW-004`) keeps baseline understandable. Unused Flexibility Is Waste (`LAW-006`) avoids perfect product-line architecture for imagined variants.

Global Configuration is tempting shortcut: one broad flag blurs regional behavior, hardware revision, migration, diagnostics and support. Recovery: name supported/unsupported combinations, keep defaults owned, give values scope/lifecycle.

Observability turns field behavior into usable evidence. Useful Field Sensor Gateway evidence: reset reason, active/source/target firmware, hardware revision, configuration fingerprint, variant, calibration state, migration result, radio boundary outcome, first-report result, service-tool compatibility and recovery state. Event Catalog keeps meanings stable. Hidden State, Silent Coupling, Platform Leakage and Event Explosion are risks. Answer is not more events, but owned events with product meaning.

Release and upgrade paths turn chain into promise. Supported baseline names direct path v1.0.2 to v1.1 with hardware revisions, regional packages, schema v2, service tool 4.3+, and preserved identity/calibration/configuration/event/recovery state. Deferred v1.0 path requires intermediate package. Rejected paths include old service tools, hidden variants and factory reset as default. One Lost Packet (`FAILURE-002`), The Release We Should Have Delayed (`FAILURE-005`) and The Successful Prototype (`FAILURE-003`) all matter because missing facts and release pressure expose hidden assumptions.

Records keep chain discoverable: ADR for baseline, RFC for compatibility proposal, Decision Journal for bounded exception, Mistake Ledger for escaped assumption, Event Catalog for event meanings, Architecture Ledger for active decisions. Discoverability (`METRIC-003`) is how future engineers avoid treating same assumptions as new.

Review and freeze are scoped. Architecture Review (`RITUAL-001`) when Change Radius crosses owners. Architecture Freeze (`RITUAL-002`) when selected decisions need stability for validation. Freeze named release-critical decisions, not whole product, and keeps exception path.

Temporary Solution (`ANTIPATTERN-006`) appears throughout: prototype shortcut, pilot timeout, support script, calibration bypass, manual recovery note. Temporary work is not shameful; it needs path out.

Product becomes supportable when decisions connect: promises, owners, evidence, records and revisit triggers form chain. Part IV ends here because product is no longer only design problem. It is shared memory, bridge into technical leadership.

## Інженерний принцип

Build product as chain of explicit decisions. Each decision names promise, owner, evidence and revisit condition.

Ask:

1. What did prototype actually prove?
2. Which product reality changed architecture?
3. Which state needs owner?
4. Which interface became promise?
5. Which dependency became support obligation?
6. Which configuration difference is supported variant?
7. Which unsupported combination must be stated?
8. Which field failure must explain itself?
9. Which upgrade path is promised?
10. Which evidence supports release?
11. Which decision needs review, freeze or ledger entry?

Мета не apply every Part IV practice equally. Мета — connect decisions that must stay true after product leaves prototype bench.

## Архітектурна вправа

### Walk One Product Decision Chain

Оберіть small product or subsystem, ideally starting from real prototype assumption.

Write:

> Because prototype assumption A became product promise P, owner O must preserve evidence E until revisit trigger T.

Trace prototype assumption, manufacturing/field reality, configuration/variant decision, observable event/diagnostic, release/upgrade path, owner, promise, evidence, record, review/freeze trigger and revisit condition.

End with:

1. one product promise;
2. one owner;
3. one evidence requirement;
4. one record to update;
5. one revisit trigger.

If exercise produces long checklist, narrow it. If only local fix, widen until next product surface appears.

## Нотатник Principal Engineer

- Product is a chain of promises.
- Baseline is useful only when assumptions are findable.
- Good walkthrough leaves decisions people can reuse.

## ADR

### Chapter ADR: Set the Field Sensor Gateway Product Baseline for Pilot Release

#### Status

Accepted for this chapter.

#### Context

Field Sensor Gateway prototype works: reports sensor readings over radio path, stores local configuration, has simple service tool and can be updated in lab. Manufacturing needs serial identity and calibration flow. Field support needs diagnostic evidence beyond developer logs. Regional and hardware variants exist. Firmware v1.1 changes configuration schema. Field units exist on v1.0 and v1.0.2. Support and future engineers need discoverable baseline: supported, deferred, evidence.

#### Decision

Accept limited supported baseline for pilot release.

Pilot baseline supports hardware revisions A and B, standard and regional packages, configuration schema v2, service tool 4.3+, direct upgrade from v1.0.2 to v1.1. Upgrade from v1.0 to v1.1 requires intermediate migration package. Battery package, unsupported regional timeout combinations and old service-tool upgrade path are deferred or rejected.

Assign owners for serial identity, calibration state, configuration schema, regional variant promises, event meanings, release artifact identity, migration behavior, update state and recovery state. Preserve identity, calibration, configuration fingerprint, hardware revision, variant, source version, target version, migration result, reset reason and first-report outcome as support-safe evidence.

Record pilot baseline in ADR; keep hardware-revision/service-tool compatibility proposal in RFC; use Decision Journal for pilot exceptions/evidence gaps; Event Catalog for event meanings; Architecture Ledger for active baseline decisions; Mistake Ledger for escaped assumptions. Run Architecture Review for broad Change Radius decisions. Apply Architecture Freeze narrowly to v1.1 upgrade-path validation.

#### Consequences

Pilot baseline becomes supportable. Ownership clearer, hidden promises reduced, unsupported paths stated before support discovers them. Field diagnosis improves, future engineers can find product memory. Cost: more validation, visible deferrals, cross-team coordination, delayed customer requests, records to maintain.

#### Alternatives Considered

- Ship prototype baseline.
- Wait for perfect product-line architecture.
- Support every requested configuration.
- Defer observability and upgrade evidence until after pilot.
- Split every customer into separate firmware.
- Freeze entire architecture until all unknowns resolved.

Rejected because they hide assumptions, add speculative flexibility, expand support surface or freeze too broadly.

## Коментар редактора

Chapter 25 closes Part IV by making product-building chapters meet inside one reference product. It does not repeat previous chapters; it shows how Field Sensor Gateway decision chain touches prototype evidence, manufacturing/field reality, variants, observability and release paths.

Reference project, Field Sensor Gateway, product baseline, product decision chain, pilot release and walkthrough remain chapter-local language. No new PEAK concept. Relationship set includes successful prototype pressure, release risk, communication/recovery failure, state ownership, API promises, time, simplicity, evidence, unused flexibility, dependency decisions, Change Radius, Discoverability, API Stability, ADR, RFC, Decision Journal, Mistake Ledger, Event Catalog, Architecture Ledger, Architecture Review, Architecture Freeze, Hidden State, Silent Coupling, Platform Leakage, Event Explosion, Temporary Solution and Global Configuration.

This is not MCU guide, RTOS design, boot loader pattern, radio protocol comparison, service-tool spec or manufacturing-process manual. Embedded details keep walkthrough credible. Transition to Part V is quiet: product decisions that can be found become shared memory strong enough for leadership to work through it.
