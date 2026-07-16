# Release Discipline and Upgrade Paths

## Opening Quote

> A release is a promise made to devices that will not be in the room when the promise is broken.

## Story

### The Upgrade That Worked Only Once

The team had earned the feeling that the product was ready.

The embedded controller had survived the awkward transition from prototype to product. It had a manufacturing identity,
a calibration record, a supported configuration model, named variants, product-level diagnostics, a service tool, field
events, and an update path that no longer depended on one developer's laptop. The last field trial had been noisy, but
useful. Devices could now explain enough of their state for support to distinguish firmware, configuration, gateway,
radio, variant, and power failures.

That was why the next release felt straightforward.

The new firmware changed two things customers had asked for. It improved the recovery behavior after a gateway outage,
and it changed the configuration schema so licensed remote control could be enabled without replacing the unit. The
team had a release candidate. The package was signed. The service tool could install it. The latest engineering build
upgraded cleanly in the lab.

The release owner asked the ordinary question:

> Did the new image pass?

The answer was yes.

On the bench, a current unit running the previous engineering build accepted the package, verified the image, migrated
configuration, restarted, kept its identity, reported the new firmware version, and resumed normal operation. The
service tool showed progress. The Event Catalog entry for update completion matched the service-tool message. The
release notes listed the new recovery behavior and the remote-control configuration change.

The team planned to ship.

Then support asked which field versions could receive the update.

That question sounded administrative until the room tried to answer it.

Some field units were on the latest pilot version. Some were two releases behind because they had been installed at
sites with limited service windows. A small group still ran an early field build because the customer had delayed a
service visit. The product now had multiple older versions in the field. The lab test had covered only the latest
engineering build to the new release candidate. It had not covered older field versions with older configuration
records.

Manufacturing raised the next issue.

One hardware revision had a different nonvolatile layout for calibration backup. The new firmware could read it during
normal boot, but the recovery installer used a smaller compatibility path. In the lab, identity survived because the
test unit used the newest revision. On one older revision, the recovery path could preserve firmware and identity only
if calibration backup had already been compacted by an intermediate release.

The configuration owner noticed a third problem.

One customer variant still used a deprecated option. The new schema migrated supported options cleanly, but this
variant used a field that had been treated as obsolete in the latest package. The migration code did not reject it. It
kept the value and mapped it to a default that was legal for the firmware and wrong for the customer package.

The service-tool owner added a quieter concern.

The new release required service tool version 4.3 or later to show the new support-safe failure reasons. Older tools
could still install the image. They would report progress and success. But if configuration migration failed, they
would show `update failed` without the reason support needed. The update was observable, but the failure explanation
was not compatible with the tools still used in the field.

Rollback looked comforting for about ten minutes.

The firmware image could roll back. The migrated configuration could not always roll back without losing meaning. The
new schema merged two fields and moved one customer option behind a licensed capability. Returning to the old image
would not reconstruct the original configuration unless the installer preserved a source snapshot that the current
release package did not require.

Calibration ownership was also ambiguous during upgrade.

Firmware owned the calibration record during normal operation. Manufacturing owned the first calibration measurement.
The service tool could trigger recalibration under support guidance. The installer copied calibration through the update
path as bytes, because that had been enough before the schema changed. During recovery, the installer could decide
whether a calibration record was present, but not whether it was still valid for the restored image, hardware revision,
and variant.

Each issue had a local answer.

Support could warn customers on old versions. Manufacturing could flag the old hardware revision. Firmware could add a
special migration branch. The service-tool team could tell technicians to update the tool first. Release notes could
mention the deprecated option. QA could add a few more examples. The release owner could hold the package for one week.

None of those answers named the release promise.

The late change made the room finally stop.

A defect fix landed after validation had started. It changed the gateway retry window during the first report after
upgrade. The change was small in code. It affected the moment when a device proved it had completed upgrade, preserved
configuration, and returned to the service-visible reporting path. It also changed what support would see if the first
post-upgrade report failed.

The release owner repeated the question, now with less confidence:

> Did the new image pass?

Mara, the principal engineer, wrote a different question underneath it:

> Which upgrade paths are we promising, and what must remain true before, during, and after the upgrade?

The room got quieter because the question was harder to dodge.

The team stopped treating the release as one image. They listed source versions on the left side of the board and the
target release on the right. They added hardware revision, product variant, configuration schema, service-tool version,
gateway compatibility, calibration layout, identity record, diagnostic event version, and recovery behavior to the
middle. The picture no longer looked like a file moving onto a device. It looked like a set of state transitions.

The first supported path was clear: latest field release to the new release candidate, newest hardware revision,
standard and regional variants, service tool 4.3 or later, current configuration schema, and no deprecated customer
option. That path had evidence, but it still needed one power-loss test during migration and one service-tool failure
case.

The second path was supportable with work: one release behind to the new release candidate, same hardware revision, same
variant set, with a compatibility migration for the previous configuration schema. The team assigned firmware ownership
for migration, service-tool ownership for failure wording, QA ownership for path evidence, and release ownership for the
support note.

The third path was deferred: early field build to the new release. It required an intermediate release because the old
configuration record did not contain enough information for safe direct migration. The team wrote that down as an
unsupported direct path, not as a support surprise.

The older hardware revision became a separate path. It could upgrade only if calibration backup had been compacted by
the intermediate release. If not, support had to use a recovery procedure that preserved firmware and identity but
required calibration validation before returning the unit to service. Factory reset was rejected as the default answer.
It was available only as a last resort because it would erase product trust along with product state.

The deprecated customer option became a release decision. The team would not silently map it to a default. The package
would reject the unsupported option with a support-safe diagnostic, preserve the original configuration, and require a
service decision. The release notes would state the unsupported path and the support horizon for that customer variant.

Rollback became narrower and more honest.

The team separated rollback, retry, recovery, and forward-fix. Retry meant the same package could attempt the same
stage again after a recoverable interruption. Recovery meant the device could return to a known supportable state after
partial upgrade. Rollback meant returning to the previous executable only when the configuration, calibration, identity,
and diagnostic meaning still matched that executable. Forward-fix meant moving to a corrected package when rollback
would preserve code but not trust.

That distinction changed the release plan more than the code diff did.

For the supported paths, the package would preserve identity, calibration, configuration snapshot, source version,
target version, variant identity, migration result, service-tool compatibility, and diagnostic event version. The Event
Catalog would record the event meanings for upgrade started, image verified, migration accepted, migration rejected,
recovery entered, rollback unavailable, retry allowed, and upgrade complete. Older diagnostic meanings would remain
compatible for the support horizon or be explicitly rejected.

The team opened an Architecture Review (`RITUAL-001`) for the broad compatibility decision because firmware, service
tools, manufacturing, support, QA, gateway owners, and release owners were all affected. The review did not approve the
release. It reviewed the upgrade paths, state ownership, compatibility promises, evidence gaps, and unsupported paths
before those choices hardened.

Then they froze a narrow set of release-critical decisions.

Architecture Freeze (`RITUAL-002`) did not freeze all code. It froze the supported source-to-target upgrade paths,
configuration migration rules, diagnostic event meanings, service-tool compatibility promise, release-critical state
owners, and the gateway retry behavior during first post-upgrade report. The vocabulary mattered: Architecture Freeze
(`VOCAB-006`) was temporary, scoped, and tied to exit criteria. Implementation fixes could continue when they preserved
those decisions. Any change to the frozen surfaces needed evidence, affected-owner review, record updates, and a new
validation decision.

The late gateway retry change became an exception request instead of a quiet fix. Its Change Radius (`VOCAB-001`,
`METRIC-001`) included firmware, gateway behavior, first-report diagnostics, service-tool wording, update validation,
support notes, and release evidence. The team accepted the change only after it preserved the frozen promise and added
targeted validation for the first post-upgrade report.

The records changed too.

The ADR captured the decision to freeze supported upgrade paths before field release. An RFC recorded the broader
service-tool compatibility and migration proposal. Decision Journal entries captured smaller path decisions and review
triggers. The Architecture Ledger listed active release-critical decisions, owners, freeze scope, and review date. The
release notes stopped being a list of features and became discoverable support evidence: supported source versions,
unsupported direct paths, service-tool requirements, known limits, migration behavior, and support horizon. The Mistake
Ledger received the assumption that almost escaped: "latest-build lab upgrade proves field upgrade readiness."

The release did not ship that week.

It shipped later with fewer surprises.

Support could tell which units needed an intermediate release. Manufacturing could explain which old hardware revision
needed calibration validation. The service tool refused unsupported paths instead of pretending every install was the
same. Firmware preserved the state it had promised to preserve. QA validated paths, not examples. Release notes told
future engineers where the promises ended.

The team had delayed the release.

This time, that was the engineering decision.

## Discussion

Release discipline is not a ceremony around a build artifact. It is architecture-aware judgment about what can ship,
what must be held, what evidence is required, what promises are being made, and how the product can be supported after
release.

An upgrade path is a supported transition from one product state to another. It is not only a firmware image.

That distinction is easy to miss because the release artifact is visible. A file has a name. A package has a hash. A
version has a label. A service tool can show success. A lab can prove that one unit accepted one image under one set of
conditions. Those facts matter, but they do not define the release promise by themselves.

A release is an architectural commitment.

It commits the product to behavior that other people, tools, devices, procedures, and future versions will rely on. It
commits support to explanations. It commits manufacturing and service to compatible paths. It commits customers to a
meaning of version, variant, configuration, diagnostic, and recovery state. It commits future engineers to the records
they will search when something fails after the people who made the release have moved on.

The most dangerous release question is the one from the story:

> Did the new image pass?

It is not a bad question. It is just too small. Image correctness is one part of release readiness. It says something
about artifact integrity, signing, ability to install, and behavior after installation. It does not say which source
versions can reach the image safely, which state must survive, which variants are supported, which service tools can
interpret failure, which diagnostics remain compatible, which rollback paths preserve trust, or what support can do if
the upgrade stops halfway.

That is why the better question is:

> Which upgrade paths are we promising, and what must remain true before, during, and after the upgrade?

Before the upgrade, the product has a source version, hardware revision, product variant, configuration schema,
calibration state, identity record, data shape, service-tool expectation, diagnostic vocabulary, dependency behavior,
and support horizon. During the upgrade, the product may pass through boot loader or installer states, migration steps,
power-loss windows, network interruptions, partial writes, retries, recovery decisions, and first-report handshakes.
After the upgrade, the product has to explain what happened and prove that the target state is supportable.

Every State Has One Owner (`LAW-001`) becomes concrete here. Release-critical state needs authority before the upgrade
can preserve it. Identity, calibration, configuration, variant meaning, migration state, data ownership, and recovery
state cannot be protected by a package that merely copies bytes. Someone must own what the state means, how it changes,
which transitions are valid, and what happens when the transition is interrupted.

Every API Is a Promise (`LAW-002`) becomes visible at release time too. The API may be a firmware command, a diagnostic
event, a service-tool protocol, a manufacturing programming path, a configuration schema, an update package format, or
a recovery behavior. Once released, other surfaces will trust its meaning. API Stability (`METRIC-004`) includes
behavior, errors, timing, and meaning. Keeping the same version shape or command name is not enough if the promise
changes.

Every Dependency Is a Decision (`LAW-007`) applies to release machinery even when the team does not want to talk about
release machinery. Boot loaders, installers, signing systems, distribution paths, gateways, service tools, and vendor
update libraries import lifecycle obligations. Their versions, failure modes, compatibility windows, and replacement
cost become part of the product architecture when the release depends on them.

Time Is a Dependency (`LAW-003`) because release promises live across time. Migration timing matters. Retry windows
matter. Support horizons matter. Deprecation dates matter. Staged exposure matters. A service tool that will be updated
"soon" is not compatible today. A gateway behavior that changes after field deployment can invalidate yesterday's
release evidence. A rollback path that works only before configuration migration finishes is not the same promise as a
rollback path that works after the device has served a customer for a week.

Evidence Before Confidence (`LAW-005`) is the release posture. A successful latest-build lab upgrade is evidence for
one path. It is not evidence for every source version, hardware revision, variant, configuration schema, service-tool
version, network condition, power-loss moment, or recovery branch. That does not mean every possible path must be
supported. It means unsupported paths should be named before the field discovers them.

Compatibility has more than one face.

Backward compatibility asks whether new code can handle old state, old packages, old tools, or old assumptions.
Forward compatibility asks whether old surfaces can survive or reject future meanings safely. Service-tool
compatibility asks whether technicians can install, diagnose, recover, and explain the product with supported tools.
Manufacturing compatibility asks whether station programming, identity, calibration, and traceability paths remain
valid. Field-data compatibility asks whether data recorded before the release still means what the product thinks it
means. Configuration compatibility asks whether old schemas migrate or reject safely. Variant compatibility asks whether
supported packages still carry the same promises. Diagnostic compatibility asks whether event meanings remain
support-safe and discoverable. Update-package compatibility asks whether package metadata, signing, source-version
rules, target-version rules, and dependency assumptions match the devices that will receive the package. A version
matrix is useful only when it records the migration contract: which source states may move, which target states they may
reach, which state must survive, and which unsupported paths must be rejected. Upgrade compatibility is the sum of
those path promises. Support horizon names how long the product promises to keep those paths alive.

Version numbers can help readers navigate those promises. They cannot replace the promises.

Release notes have a similar boundary. They are not architecture records by themselves, but they can make architecture
promises discoverable. A useful release note for an embedded product may say which source versions are supported, which
service-tool versions are required, which variants are included, which paths are unsupported, which diagnostics changed
meaning, what support should do after a failed migration, and where the governing ADR, RFC, Event Catalog, or
Architecture Ledger entry lives. A feature list is not enough when the release changes the path by which a field unit
survives.

Rollback deserves special care because it feels safer than it often is.

Rollback is safe only when returning to the earlier executable also returns to a trustworthy product state. If the
upgrade has already migrated configuration, changed calibration meaning, altered identity records, updated diagnostic
event versions, or changed field data, rolling back code may leave the product in a state the old code cannot explain.
In that case, rollback preserves a file and loses trust.

Retry, recovery, and forward-fix are different promises.

Retry means trying the same supported step again after a recoverable interruption. Recovery means reaching a known
supportable state after the original path fails or stops halfway. Forward-fix means moving to a corrected target when
returning backward would be unsafe or incomplete. Factory reset is another path, but it should be a last resort because
it often destroys the evidence, identity, configuration, calibration, or customer trust the product needed to preserve.

Change Radius (`VOCAB-001`, `METRIC-001`) helps the team scale release discipline. A small defect fix inside one owned
boundary may need a targeted test and a Decision Journal entry. A migration that touches firmware, service tools,
manufacturing scripts, diagnostics, support notes, package signing, gateway behavior, and customer variants needs
broader review. The goal is not to make every release heavy. The goal is to match release discipline to the affected
surface.

Discoverability (`METRIC-003`) keeps the release from becoming oral history. A future engineer should be able to find
the supported paths, unsupported paths, compatibility assumptions, release-critical owners, evidence, known risks, and
review triggers. ADRs (`ARTIFACT-001`) record consequential release and upgrade decisions. RFCs (`ARTIFACT-002`) invite
review when upgrade behavior crosses ownership boundaries. Decision Journal entries (`ARTIFACT-003`) capture smaller
risks, deferred paths, confidence judgments, and review triggers. Mistake Ledger entries (`ARTIFACT-004`) preserve
escaped release assumptions. Event Catalog entries (`ARTIFACT-005`) keep upgrade progress and failure meanings stable.
Architecture Ledger rows (`ARTIFACT-006`) make active release-critical decisions, freeze scope, owners, and review
dates findable.

The common smells are familiar because earlier chapters prepared them.

Hidden State (`SMELL-004`) breaks upgrades when configuration, calibration, identity, migration, or recovery state
exists but cannot be inspected or owned. Silent Coupling (`SMELL-001`) appears when firmware, service tools,
manufacturing scripts, release packages, diagnostics, and support records all depend on the same promise without a
shared contract. Platform Leakage (`SMELL-005`) appears when low-level driver, hardware, or vendor details leak into
product release and support promises without translation. Event Explosion (`SMELL-006`) appears when upgrade
diagnostics become noisy or incompatible because event meanings are not owned, versioned, and tied to decisions.

The anti-patterns are release-risk amplifiers. HAL Everywhere (`ANTIPATTERN-002`) spreads hardware-revision details into
places that should reason in product language. Global Configuration (`ANTIPATTERN-003`) turns one broad migration or
release flag into a switch that changes unrelated behavior across variants, diagnostics, recovery, and service tools.
Callback Hell (`ANTIPATTERN-005`) can hide installer, gateway, service-tool, and recovery ordering so no one can
explain which step failed. Temporary Solution (`ANTIPATTERN-006`) appears when a release workaround, support script, or
upgrade bypass ships without owner, expiration, or support decision.

The failure story One Lost Packet (`FAILURE-002`) matters here because upgrade paths often fail on one missing,
reordered, or late message. A lost acknowledgement, interrupted gateway handshake, or missing first report may reveal
whether retry, recovery, and diagnostics are real promises or hopeful assumptions.

Architecture Freeze is the release tool that must be used carefully.

Architecture Freeze (`RITUAL-002`) is not a universal release gate. It is a temporary stabilization of named
architectural decisions during a high-risk phase. Chapter 19 already taught the practice. Chapter 24 uses it for a
narrow release moment: supported upgrade paths, migration rules, diagnostic meanings, service-tool compatibility,
release-critical APIs, boot and recovery behavior, manufacturing programming paths, support notes, and known risk
decisions may need to stop moving while evidence is gathered.

The freeze should be scoped, temporary, and exit-criteria-bound. It should say what can still change, who approves an
exception, what evidence justifies movement, which records must be updated, and when the freeze ends. The point is not
bureaucracy. The point is to prevent late uncontrolled architectural change from invalidating release evidence while
still allowing learning to correct wrong assumptions.

The Release We Should Have Delayed (`FAILURE-005`) is not a story about timid teams. It is a story about teams that
convert known uncertainty into field cost because the release feels close. Chapter 24's answer is not "delay every
release." The answer is to know what is being promised, what evidence supports the promise, what paths are unsupported,
and which risks are accepted.

That is release discipline.

Not a checklist.

A promise with evidence, boundaries, records, and a way to recover trust.

## Engineering Principle

Release only the promises you can support, and upgrade only along paths you can explain, recover, and validate. A
version is not a release unless its compatibility, state transitions, evidence, and support obligations are known.

Use this principle when a release looks ready because the image passed, the package installs, or the latest lab path
works.

Ask:

1. Which source versions can upgrade to this release?
2. Which variants and configurations are supported?
3. What state must survive the upgrade?
4. Who owns release-critical state?
5. What happens if power or network fails mid-upgrade?
6. What can be rolled back, retried, recovered, or forward-fixed?
7. Which service tool versions are compatible?
8. What evidence proves this path works?
9. What diagnostic evidence will support see if it fails?
10. What changed after freeze?
11. What risk is accepted, deferred, or unsupported?
12. What must release notes make discoverable?

The goal is not to make release slow. The goal is to make the commitment honest enough to survive the field.

## Architecture Exercise

### Trace One Upgrade Path

Choose one product upgrade path that your system currently assumes is safe. Pick a real path if possible: one source
version, one target version, one hardware revision, one product variant, one configuration schema, and one service-tool
version.

Write the path in one sentence:

> Device on source version X, hardware revision Y, variant Z, and configuration schema N upgrades to target version T
> through supported path P.

Then document:

1. source version;
2. target version;
3. hardware revision;
4. product variant;
5. configuration schema;
6. data or calibration that must survive;
7. release-critical state owner;
8. compatibility promises;
9. migration step;
10. rollback, retry, recovery, or forward-fix behavior;
11. observability needed during and after upgrade;
12. service-tool compatibility;
13. evidence available;
14. evidence missing;
15. unsupported paths nearby;
16. decision record needed;
17. freeze or review trigger.

End with four outputs:

1. one supported upgrade path;
2. one unsupported or deferred path;
3. one release-critical state owner;
4. one validation or recovery action.

Do not create a new artifact for this exercise. Use the records your system already has: ADR, RFC, Decision Journal,
Architecture Ledger, Event Catalog, release notes, or Mistake Ledger.

## Principal's Notebook

- A release is a promise, not a file.
- An upgrade path includes the state it must preserve.
- A rollback that loses trust is not recovery.

## ADR

### Chapter ADR: Freeze Supported Upgrade Paths Before Field Release

Status: Accepted for this chapter.

Context:

- The product has multiple field versions, hardware revisions, configurations, variants, and service-tool versions.
- A lab upgrade from the latest build works.
- Field release would expose unsupported source versions and uncertain migration paths.
- Rollback and recovery behavior are not equally safe for every path.

Decision:

- Enumerate supported source-to-target upgrade paths before field release.
- Explicitly reject or defer unsupported paths instead of leaving them for support to discover.
- Freeze release-critical state transitions, configuration migration, diagnostic meanings, and service-tool
  compatibility before final validation.
- Preserve identity, calibration, configuration, and variant meaning across supported paths.
- Require evidence for each supported path.
- Record release risks, known limits, support notes, and review triggers in the appropriate ADR, RFC, Decision Journal,
  Architecture Ledger, Event Catalog, release notes, or Mistake Ledger.
- Defer reference-project integration walkthrough to Chapter 25.

Consequences:

- Support promises become clearer.
- Field surprises are reduced because unsupported paths are visible before release.
- Compatibility evidence becomes stronger because validation follows source-to-target paths instead of examples.
- Recovery decisions improve because rollback, retry, recovery, and forward-fix are separated.
- Product trust improves because identity, calibration, configuration, and variant meaning are preserved deliberately.
- Validation work increases.
- Late changes become slower when they touch frozen release-critical surfaces.
- Service-tool coordination and compatibility records become part of release work.
- The team must maintain extra discipline around release-critical state.

Alternatives Considered:

- Ship the image because the latest lab upgrade worked. Rejected because one passing path does not prove field upgrade
  readiness.
- Support every field version. Rejected because unsupported paths should be explicit, not hidden behind unrealistic
  promises.
- Require all customers to factory reset. Rejected because reset may destroy identity, calibration, configuration,
  evidence, and trust.
- Rely on rollback only. Rejected because rollback is not safe when migrated state cannot return with the executable.
- Patch unsupported paths in support scripts. Rejected because private support scripts create Temporary Solution risk
  and Silent Coupling.
- Defer upgrade-path definition until after release. Rejected because the field would then define the unsupported
  paths through failure.
- Freeze the whole architecture instead of release-critical surfaces. Rejected because the team needs scoped stability,
  not a broad ban on learning.

## Editor's Commentary

Chapter 24 follows Chapter 23 by turning observable product evidence into supported release and upgrade commitments.
Chapter 23 asked what the device can explain when it fails away from engineering. Chapter 24 asks which release and
upgrade promises that evidence must support before the product changes in the field.

The chapter deliberately keeps release discipline, upgrade path, rollback, retry, forward-fix, firmware image, release
candidate, version matrix, migration contract, upgrade compatibility, support horizon, release gate, release notes, and
release evidence as chapter-local terms. It introduces no primary PEAK concept. The PEAK weight sits on The Release We
Should Have Delayed (`FAILURE-005`) and Architecture Freeze (`RITUAL-002`), supported by the temporary, scoped meaning
of Architecture Freeze (`VOCAB-006`).

The earlier chapters are constraints, not material to repeat. Release-critical state needs owners. Released behavior and
diagnostics become API promises. Update tooling and service tools are dependency decisions. Migration and support
horizons depend on time. Confidence needs evidence. Change Radius and Discoverability determine how much release
discipline the work deserves. Event Catalog entries, ADRs, RFCs, Decision Journal entries, Architecture Ledger rows,
release notes, and Mistake Ledger entries keep release decisions findable after the release pressure has passed.

This chapter also preserves the Part IV boundary. Chapter 20 owns the prototype-to-product transition. Chapter 21 owns
manufacturing and field reality. Chapter 22 owns configuration, variants, and product lines. Chapter 23 owns embedded
observability. Chapter 24 owns release discipline and upgrade paths. Chapter 25 can now walk through the reference
project with these promises available, but this chapter does not write that walkthrough early.

The closing move is intentionally practical: do not ask only whether the image passed. Ask which paths the product is
promising, what state those paths must preserve, what evidence proves them, and what support can safely do when the path
does not hold.
