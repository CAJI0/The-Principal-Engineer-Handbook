# Release-дисципліна і шляхи оновлення

## Вступна цитата

> Release — це обіцянка пристроям, які не будуть у кімнаті, коли ця обіцянка зламається.

## Історія

### Оновлення, яке спрацювало лише один раз

Команда заслужила відчуття, що product готовий. Embedded controller пройшов шлях від prototype to product: manufacturing identity, calibration record, supported configuration model, named variants, product-level diagnostics, service tool, field events and update path no longer depending on one developer laptop. Field trial був noisy but useful; devices could explain enough state for support to distinguish firmware, configuration, gateway, radio, variant and power failures.

Next release felt straightforward. New firmware improved recovery after gateway outage and changed configuration schema so licensed remote control could be enabled without replacing unit. Release candidate existed, package signed, service tool could install it, latest engineering build upgraded cleanly in lab.

Release owner asked: «Did the new image pass?» Answer: yes. Current unit on previous engineering build accepted package, verified image, migrated configuration, restarted, kept identity, reported new firmware, resumed normal operation. Service tool showed progress. Event Catalog update completion matched tool message. Release notes listed features.

Team planned to ship. Then support asked which field versions could receive update.

That administrative-looking question was hard. Some field units on latest pilot, some two releases behind, small group on early field build. Lab test covered only latest engineering build to release candidate, not older field versions with older configuration records.

Manufacturing raised hardware revision issue: one revision had different nonvolatile layout for calibration backup. New firmware could read it during normal boot, but recovery installer used smaller compatibility path. On older revision recovery path could preserve firmware and identity only if calibration backup had been compacted by intermediate release.

Configuration owner noticed deprecated option. New schema migrated supported options, but customer variant used obsolete field. Migration kept value and mapped to default legal for firmware but wrong for customer package.

Service-tool owner noted that new release required service tool 4.3+ to show new support-safe failure reasons. Older tools could install image and report success, but if migration failed they would show `update failed` without reason support needed.

Rollback looked comforting briefly. Firmware image could roll back. Migrated configuration could not always roll back without losing meaning. New schema merged fields and moved one customer option behind licensed capability. Returning to old image could not reconstruct original configuration unless installer preserved source snapshot, which package did not require.

Calibration ownership ambiguous during upgrade. Firmware owned calibration record in normal operation; manufacturing owned first measurement; service tool could trigger recalibration; installer copied calibration as bytes, because enough before. During recovery installer could know record present, not whether still valid for restored image, hardware revision and variant.

Each issue had local answer: warn customers, flag hardware revision, special migration branch, update service tool first, release notes, more examples, hold package one week. None named release promise.

Late defect fix changed gateway retry window during first report after upgrade. Small code diff, but affected moment when device proved upgrade complete, configuration preserved and service-visible reporting returned. Release owner asked again: «Did the new image pass?» Mara wrote:

> Which upgrade paths are we promising, and what must remain true before, during, and after the upgrade?

Team stopped treating release as one image. They listed source versions and target release, then hardware revision, product variant, configuration schema, service-tool version, gateway compatibility, calibration layout, identity record, diagnostic event version and recovery behavior. It looked like state transitions, not file moving onto device.

First supported path: latest field release to release candidate, newest hardware revision, standard/regional variants, service tool 4.3+, current configuration schema, no deprecated option. Evidence existed, with power-loss migration test and service-tool failure case still needed.

Second path supportable with work: one release behind to release candidate, same hardware revision/variants, compatibility migration for previous schema. Firmware owns migration, service tool owns failure wording, QA owns path evidence, release owns support note.

Third path deferred: early field build to new release required intermediate release because old configuration record lacked enough information for safe direct migration. Written as unsupported direct path, not support surprise.

Older hardware revision became separate path: upgrade only if calibration backup compacted by intermediate release; otherwise support recovery procedure preserves firmware/identity but requires calibration validation before return to service. Factory reset rejected as default because it erases product trust with product state.

Deprecated customer option: package rejects unsupported option with support-safe diagnostic, preserves original configuration and requires service decision. Release notes state unsupported path and support horizon.

Rollback became narrower. Team separated rollback, retry, recovery and forward-fix. Retry means same package can attempt same stage after recoverable interruption. Recovery means known supportable state after partial upgrade. Rollback means returning to previous executable only when configuration, calibration, identity and diagnostic meaning match it. Forward-fix means corrected package when rollback preserves code but not trust.

Supported paths preserve identity, calibration, configuration snapshot, source version, target version, variant identity, migration result, service-tool compatibility and diagnostic event version. Event Catalog records upgrade started, image verified, migration accepted/rejected, recovery entered, rollback unavailable, retry allowed and upgrade complete.

Architecture Review (`RITUAL-001`) reviewed upgrade paths, state ownership, compatibility promises, evidence gaps and unsupported paths across firmware, service tools, manufacturing, support, QA, gateway and release owners. Architecture Freeze (`RITUAL-002`) froze supported source-to-target upgrade paths, migration rules, diagnostic event meanings, service-tool compatibility promise, release-critical state owners and gateway retry behavior during first post-upgrade report. Implementation fixes could continue if they preserved decisions.

Late gateway retry change became exception request. Its Change Radius included firmware, gateway behavior, first-report diagnostics, service-tool wording, update validation, support notes and release evidence. Accepted only after preserving frozen promise and adding targeted validation.

Records changed: ADR captured supported upgrade path freeze, RFC recorded service-tool compatibility/migration proposal, Decision Journal captured smaller path decisions, Architecture Ledger listed active release-critical decisions, release notes became support evidence, Mistake Ledger captured assumption: «latest-build lab upgrade proves field upgrade readiness.»

Release did not ship that week. It shipped later with fewer surprises. Support knew units needing intermediate release. Manufacturing explained old hardware revision calibration validation. Service tool refused unsupported paths. Firmware preserved promised state. QA validated paths, not examples. Release notes told future engineers where promises ended. Delay was engineering decision.

## Обговорення

Release discipline is not ceremony around build artifact. It is architecture-aware judgment about what can ship, what must be held, what evidence is required, what promises are made and how product can be supported after release.

Upgrade path is supported transition from one product state to another, not only firmware image.

Release artifact is visible: file, hash, version label, service-tool success, lab install. These matter but do not define promise alone. Release commits product to behavior other people, tools, devices, procedures and future versions will rely on. It commits support to explanations, manufacturing/service to compatible paths, customers to meaning of version/variant/configuration/diagnostic/recovery state, future engineers to records.

«Did the new image pass?» is not bad, just too small. Better: which upgrade paths are we promising, and what must remain true before, during and after upgrade?

Before upgrade: source version, hardware revision, product variant, configuration schema, calibration state, identity record, data shape, service-tool expectation, diagnostic vocabulary, dependency behavior, support horizon. During: bootloader/installer states, migration, power-loss windows, network interruptions, partial writes, retries, recovery decisions, first-report handshakes. After: product explains what happened and proves target state supportable.

Every State Has One Owner (`LAW-001`) means release-critical state has authority before upgrade can preserve it. Every API Is a Promise (`LAW-002`) means firmware command, diagnostic event, service-tool protocol, manufacturing programming path, configuration schema, update package format or recovery behavior become promises after release. API Stability (`METRIC-004`) includes behavior, errors, timing and meaning.

Every Dependency Is a Decision (`LAW-007`) applies to boot loaders, installers, signing, distribution paths, gateways, service tools and vendor update libraries. Time Is a Dependency (`LAW-003`) because migration timing, retry windows, support horizons, deprecation dates and staged exposure matter. Evidence Before Confidence (`LAW-005`) means latest-build lab upgrade is evidence for one path, not all source versions, hardware revisions, variants, tools, power-loss moments or recovery branches.

Compatibility has many faces: backward, forward, service-tool, manufacturing, field-data, configuration, variant, diagnostic, update-package. Version matrix is useful only when it records migration contract: which source states may move, target states, state to preserve, unsupported paths to reject. Upgrade compatibility is sum of path promises. Support horizon names how long product keeps paths alive.

Rollback deserves care. It is safe only when returning executable also returns trustworthy product state. If upgrade migrated configuration, changed calibration meaning, identity records, diagnostics or field data, rollback code may preserve file and lose trust. Retry, recovery and forward-fix are different promises. Factory reset is last resort because it destroys evidence, identity, configuration, calibration or customer trust.

Change Radius scales release discipline. Local fix may need targeted test; migration across firmware, service tools, manufacturing scripts, diagnostics, support notes, signing, gateway and variants needs broad review. Discoverability keeps release from oral history: future engineer should find supported paths, unsupported paths, compatibility assumptions, release-critical owners, evidence, risks and review triggers.

Architecture Freeze is release tool used carefully. It is temporary stabilization of named architectural decisions during high-risk phase, not universal gate. For release moment, supported upgrade paths, migration rules, diagnostic meanings, service-tool compatibility, release-critical APIs, boot/recovery behavior, manufacturing programming paths, support notes and risk decisions may need to stop moving while evidence is gathered. Freeze must be scoped, temporary and exit-criteria-bound.

The Release We Should Have Delayed (`FAILURE-005`) is about converting known uncertainty into field cost because release feels close. Answer is not delay every release; answer is know promises, evidence, unsupported paths and accepted risks.

## Інженерний принцип

Release only the promises you can support, and upgrade only along paths you can explain, recover and validate. Version is not release unless compatibility, state transitions, evidence and support obligations are known.

Ask:

1. Which source versions can upgrade?
2. Which variants/configurations are supported?
3. What state must survive?
4. Who owns release-critical state?
5. What happens if power/network fails mid-upgrade?
6. What can be rolled back, retried, recovered or forward-fixed?
7. Which service tool versions are compatible?
8. What evidence proves this path?
9. What diagnostics will support see if it fails?
10. What changed after freeze?
11. What risk is accepted, deferred or unsupported?
12. What must release notes make discoverable?

Мета не slow release. Мета — honest commitment that survives field.

## Архітектурна вправа

### Trace One Upgrade Path

Оберіть real upgrade path: source version, target version, hardware revision, product variant, configuration schema and service-tool version.

Write:

> Device on source version X, hardware revision Y, variant Z, and configuration schema N upgrades to target version T through supported path P.

Document source, target, hardware revision, variant, schema, data/calibration to survive, release-critical state owner, compatibility promises, migration step, rollback/retry/recovery/forward-fix behavior, observability, service-tool compatibility, evidence available/missing, nearby unsupported paths, decision record and freeze/review trigger.

End with one supported path, one unsupported/deferred path, one release-critical owner, one validation/recovery action.

## Нотатник Principal Engineer

- Release is a promise, not a file.
- Upgrade path includes state it must preserve.
- Rollback that loses trust is not recovery.

## ADR

### Chapter ADR: Freeze Supported Upgrade Paths Before Field Release

Status: Accepted for this chapter.

Context:

- Product has multiple field versions, hardware revisions, configurations, variants and service-tool versions.
- Lab upgrade from latest build works.
- Field release would expose unsupported source versions and uncertain migration paths.
- Rollback/recovery not equally safe for every path.

Decision:

- Enumerate supported source-to-target upgrade paths before field release.
- Explicitly reject/defer unsupported paths.
- Freeze release-critical state transitions, configuration migration, diagnostic meanings and service-tool compatibility before final validation.
- Preserve identity, calibration, configuration and variant meaning across supported paths.
- Require evidence for each supported path.
- Record risks, limits, support notes and review triggers in ADR, RFC, Decision Journal, Architecture Ledger, Event Catalog, release notes or Mistake Ledger.
- Defer reference-project integration walkthrough to Chapter 25.

Consequences:

Support promises clearer; field surprises reduced; validation follows paths; rollback/retry/recovery/forward-fix separated; product trust improves. Validation work increases; late changes slower when touching frozen surfaces; service-tool coordination becomes release work.

Alternatives Considered:

- Ship image because latest lab upgrade worked.
- Support every field version.
- Require all customers to factory reset.
- Rely on rollback only.
- Patch unsupported paths in support scripts.
- Defer upgrade-path definition until after release.
- Freeze whole architecture.

Rejected because they hide field readiness, destroy trust, create Temporary Solution/Silent Coupling risk, or freeze too broadly.

## Коментар редактора

Chapter 24 turns observable product evidence into supported release and upgrade commitments. It introduces no primary PEAK concept. PEAK weight sits on The Release We Should Have Delayed (`FAILURE-005`) and Architecture Freeze (`RITUAL-002`), with Architecture Freeze (`VOCAB-006`) as temporary scoped vocabulary.

Earlier chapters act as constraints: release-critical state needs owners; released diagnostics are API promises; update tooling and service tools are dependency decisions; migration/support horizons depend on time; confidence needs evidence; Change Radius and Discoverability determine ceremony; Event Catalog, ADR, RFC, Decision Journal, Architecture Ledger, release notes and Mistake Ledger keep decisions findable.

Do not ask only whether image passed. Ask which paths product promises, what state they preserve, what evidence proves them and what support can safely do when path fails.
