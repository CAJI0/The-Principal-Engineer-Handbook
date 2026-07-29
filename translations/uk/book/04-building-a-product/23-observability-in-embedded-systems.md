# Observability в embedded systems

## Вступна цитата

> Log корисний лише тоді, коли допомагає комусь вирішити, що сталося далі.

## Історія

### Пристрій, який не міг пояснити себе

Field trial мав довести, що product може leave the lab. Device уже мав manufacturing identity, supported firmware image, supported configurations, service tool, recovery path and documented product variants. Команда перестала treating every board as a snowflake, named supported product line, and made commitments manufacturing, support and product could share.

Then first field update went out.

Most devices updated and reported normally. Smaller group stopped reporting sometime after update. Not immediately, not always, not same variant, not same site. Support dashboard showed silence. Service tool said only `communication failed`. Returned lab unit with debug build produced useful logs, but field image did not include them. Reset reason overwritten by boot code. Configuration version invisible to support tool. Variant state stored but not reported. Update state disappeared after reboot. Radio, gateway, firmware, configuration, application and power failures collapsed into one product error code.

Support could not tell whether problem was firmware, configuration, gateway behavior, network coverage, power, variant selection, vendor dependency or recovery after update. Manufacturing identity existed but was not tied to diagnostics. Returned unit matched batch, but field evidence could not say which image, configuration, variant, update step, reset sequence or boundary outcome made it silent.

First proposal: add more logs. Verbose radio logs, update logs, gateway logs, power logs, application logs, temporary flag to turn everything on. Principal Engineer did not reject impulse, but volume was not missing architecture. She wrote:

> What decision must support or engineering make, and what evidence must the device preserve so that decision is possible?

Support needed decide whether retry communication, ask power-cycle, send replacement, escalate to engineering, or mark site issue. Engineering needed decide whether update mechanism failed, device rebooted during critical step, wrong variant configuration loaded, gateway protocol changed, radio dependency behaved differently, or application entered state it did not own cleanly.

Those decisions did not require every debug message. They required small set of preserved facts.

Team listed important transitions: update started, image verified, configuration migrated, variant selected, gateway session opened, first post-update report sent, recovery entered, recovery completed, normal operation resumed. Each transition got owner. Each boundary failure got name. Radio driver could report radio boundary outcomes, but not invent product meaning. Update component owned update state. Configuration component owned configuration version and migration result. Product identity owned manufacturing identity, hardware revision and supported variant identity.

They separated developer debug logs from product diagnostics. Developer logs could remain detailed, unstable and lab-useful. Product diagnostics had to be product promise. Service technician without debugger needed last meaningful product events, reset context, update/recovery context, firmware version, configuration version, supported variant, manufacturing identity and credible failure domain.

They resisted opposite failure too: every interesting line did not become event. Principal Engineer created Event Catalog and asked each candidate event: who owns it, what decision does it support, how long must it survive? Events without decisions removed. Events without owners sent back. Developer-log copies rejected. Mistake Ledger recorded false assumptions: reset reason available after boot; configuration version obvious from firmware image; gateway error code enough; manufacturing identity and diagnostics can be joined later.

Next field update did not remove every failure. It made failures explainable. One silent device said it verified image, migrated configuration, selected cellular variant, lost gateway handshake after reboot, and preserved brownout reset reason. Another said configuration migration failed because variant table lacked manufacturing option burned into unit. Third had no device failure; gateway rejected first report after dependency contract changed.

Product still had defects. Team no longer guessed which defect.

## Обговорення

Embedded observability is not printing everything firmware knows. It is preserving evidence that lets someone make product decision when device is far away, partially failed, power constrained, network constrained and no longer attached to debugger.

Field reality is harsher than lab. Developer can rebuild firmware, attach tools, raise logging, reproduce path. Support often has generic failure message, customer report, device identity and maybe one chance to ask device what happened. If product cannot answer with stable evidence, organization substitutes confidence, habit, escalation or blame.

Evidence Before Confidence (`LAW-005`) becomes concrete. Evidence must survive the event that makes people need it. Reset reason overwritten during boot is not field evidence. Update state disappearing after reboot is not field evidence. Configuration version known only to developer script is not field evidence. Variant bit is not field evidence if support surface cannot show it.

First architectural move is ownership. Every State Has One Owner (`LAW-001`) applies to diagnostics. If update state copied into three modules, none owns truth. If radio driver, gateway client and product service produce same «communication failed», product has hidden state disguised as simplicity. Device should name state transition or boundary outcome at level where meaning is owned.

This is API problem. Service tool is API to field organization. `communication failed` promises little. Last owned events, reset context, firmware/configuration versions, variant identity, update phase, recovery state, manufacturing identity and failure domain promise bounded support decisions.

Time is dependency. Failure may happen before reboot, during update, after migration, while waiting gateway response, after first report. Time Is a Dependency (`LAW-003`) does not require perfect wall-clock time; it requires useful order: sequence numbers, boot counters, monotonic ticks, install attempts, update phases, retained reset snapshots.

Every Dependency Is a Decision (`LAW-007`) appears when gateway behavior, radio coverage, vendor drivers, network policy, manufacturing data and configuration delivery participate in one field symptom. Observability should make boundary outcome plain enough to decide firmware fix, gateway fix, configuration correction, service action or dependency review.

Event Catalog (`ARTIFACT-005`) is central artifact. Good event entry records owner, name, trigger, payload, severity, retention, reset behavior, support visibility, privacy/security constraints, versioning, deprecation and decision supported. It gives Architecture Review (`RITUAL-001`) concrete surface and Architecture Freeze (`RITUAL-002`) diagnostic commitments to preserve.

Embedded constraints still matter: RAM, flash, CPU, power, radio bandwidth, service access, privacy, security, flash wear. Small retained ring buffer, counters, boot counter, reset snapshot or bounded crash snapshot may be better evidence than huge debug stream that disappears or drains battery.

Opposing smell is Event Explosion (`SMELL-006`): many events, few easier decisions. Every callback, retry and branch emits event; field receives noise, storage pressure, battery cost, privacy questions and unclear ownership. Discoverability worsens. Change Radius grows because behavior changes touch logs, tools, dashboards, support procedures and tests.

Avoiding Event Explosion does not mean stingy evidence. It means evidence around decisions. If event cannot change support action, engineering triage, recovery behavior, release validation or product learning, it belongs in developer debug log, not product diagnostic surface.

Common smells appear: Hidden State for reset reasons/update phases/config versions; Silent Coupling for gateway/tool/manufacturing assumptions; Platform Leakage for raw driver concepts in support surface; HAL Everywhere when hardware meaning spreads; Global Configuration when every component reads configuration directly; Callback Hell when event order is unreadable; Temporary Solution when quick diagnostic flag becomes support promise.

One Lost Packet (`FAILURE-002`) reminds that one missing fact can dominate investigation. Here missing fact may be whether first post-update report was attempted, which configuration was active, whether recovery ran, or whether reset happened before migration.

Observability creates shared memory. ADRs record architectural diagnostic commitments; Decision Journal records field decisions from incomplete evidence; Mistake Ledger records assumptions that escaped; Weak Signal Register (`ARTIFACT-007`) and Weak Signal (`VOCAB-002`) help notice patterns before confirmed failures.

Product does not need perfect observability platform. It needs enough durable, owned, support-safe evidence to make decisions less speculative.

## Інженерний принцип

Design observability around decisions, not volume. Name state transitions, boundary outcomes, versions, variants, reset context and failure evidence product must preserve so people without debugger can decide what happened and what to do next.

Useful questions:

- What field decision will this evidence support?
- Which component owns the fact?
- What boundary outcome or state transition does it name?
- What context must survive reset, update, recovery and service access?
- Who can safely see it, and how will they validate it?

## Архітектурна вправа

### Make One Failure Explain Itself

Оберіть ambiguous field failure or support case: device stops reporting, failed update, confusing configuration issue, manufacturing option, service-tool message hiding too much.

Write the decision someone must make from field evidence. Identify missing evidence forcing guesswork. Map state transition or boundary outcome. Name owner. Draft one event or diagnostic record with stable name, payload, severity, retention rule, reset behavior, time/sequence, version, configuration, variant and manufacturing identity fields. Decide support-safety, privacy/security constraint, where decision is recorded, and how validation proves evidence survives failure path.

Outputs:

1. one decision evidence must support;
2. one owned event or diagnostic;
3. one retained context requirement;
4. one validation action.

## Нотатник Principal Engineer

- Logs are not evidence until someone can use them.
- Event without owner becomes noise.
- Device should explain enough to be helped.

## ADR

### Chapter ADR: Adopt Decision-Oriented Field Events for Update and Recovery Failures

Status: Accepted for this chapter.

Context:

- Field devices can fail after update, reset, configuration migration, variant selection, gateway interaction, radio communication or recovery.
- Developer debug logs are lab-useful but not stable product promise for support.
- Current service surface can collapse many failure domains into one generic message.
- Manufacturing identity, firmware/configuration versions, variant state, reset context and update state matter only if preserved and visible.
- Embedded constraints limit evidence.
- Logging everything would create Event Explosion.

Decision:

- Maintain Event Catalog for product diagnostics: owner, name, trigger, payload, severity, retention, reset behavior, support visibility, privacy/security, validation and supported decision.
- Treat update, recovery, reset, configuration, variant, gateway, radio and reporting outcomes as owned product events when they affect field decisions.
- Keep developer debug logs separate from support-safe diagnostics.
- Preserve enough context across reset/recovery to distinguish firmware, configuration, gateway, network, power, variant, dependency and recovery causes.
- Record false diagnostic assumptions and field escapes in Mistake Ledger.

Consequences:

- Support can make bounded decisions without developer tools for every issue.
- Engineering can triage from retained evidence.
- Diagnostic events become product API and require ownership, review, tests and compatibility care.
- Event versions/deprecation become support promises.
- Team must reject noisy events and design around storage, power, privacy, security and service-tool constraints.

Alternatives Considered:

- Add verbose logging everywhere.
- Keep diagnostics developer-only.
- Add one generic field error code.
- Defer diagnostics until after field trial.

Rejected because they add noise, hide evidence from support or delay exactly the evidence field trial needs.

## Коментар редактора

Chapter 23 follows Chapter 22: once product has configurations, variants, manufacturing identity, update paths, recovery paths and service tools, it needs to say which reality shaped a failure.

Observability remains chapter-local prose term. No new PEAK concept. Weight stays on Event Catalog (`ARTIFACT-005`) and Event Explosion (`SMELL-006`), supported by state ownership, API promises, time, evidence, dependency decisions, Change Radius, Discoverability, ADR, Decision Journal, Mistake Ledger, weak signals, Architecture Review and Architecture Freeze.

Chapter 24 will take these product promises into release discipline and upgrade paths. Chapter 25 will show them in reference project.
