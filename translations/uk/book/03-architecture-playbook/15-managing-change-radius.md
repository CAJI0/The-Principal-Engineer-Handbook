# Керування Change Radius

## Вступна цитата

> Diff — це не change. Це лише частина change, яка потрапила до source control.

## Історія

### Calibration Record, який не був однією change

Work item виглядав harmless:

> Add one field to the configuration structure.

Team будувала industrial controller із calibrated pressure sensor. Кожен unit leaving factory мав persistent calibration record. Firmware читав record during startup. Manufacturing station писала його after test. Service tool displayed it in field. System tests loaded sample records. Support could ask technician to export record.

Old record stored signed offset and gain. New sensor lot needed one more idea: calibrated range was no longer implied by product model. It had to be recorded with calibration itself. First estimate was honest and incomplete: add range field, update firmware structure, adjust factory script, ship.

Visible edit was small. Product decision was not.

Principal Engineer asked: what decision is changing? Answer was not «structure has new field». Answer: meaning of valid calibration record now includes measured range, and every consumer relying on calibration validity must either understand range or remain compatible with records that do not have it.

That sentence changed plan.

Direct radius was still small: persistent record definition, firmware reader, calibration writer and tests. Indirect radius was larger: service tool, host support app, packaging sample records, factory dashboard. Latent radius included recovery image copying record as bytes, product variant sharing page, binary fixtures with padding, supplier script copied from old station. Team could not prove every external consumer had been found.

Tempting plans appeared: append field and trust layout; reset old records to defaults; add one global compatibility setting; keep temporary compatibility path without retirement trigger. Those would create unsafe compatibility, erase field calibration, turn product/factory/service/support meaning into Global Configuration (`ANTIPATTERN-003`), or create Temporary Solution (`ANTIPATTERN-006`).

Principal Engineer made affected surface visible.

Map separated required radius from accidental radius. Required radius: record version, firmware compatibility, manufacturing write behavior, service display, migration, upgrade/downgrade, diagnostics and tests. Accidental radius came from duplicated knowledge: service tool knew binary layout, fixtures depended on padding, dashboard interpreted raw firmware statuses. Platform Leakage (`SMELL-005`), Silent Coupling (`SMELL-001`) and Hidden State (`SMELL-004`) made review and retest work larger than product decision required.

Plan changed from «edit structure» to «sequence product decision».

First, team named authoritative product meaning and versioned persistent representation. Firmware owned persisted meaning; manufacturing and service tools consumed documented serialized/export representations rather than shared in-memory layout. That honored Every State Has One Owner (`LAW-001`).

Second, Контракт став явним. Every API Is a Promise (`LAW-002`) applied to record format, export file, service-tool view and diagnostic message. New reader accepted old records. New writer created new records only after manufacturing and service tools were updated. Downgrade behavior documented.

Third, team mapped time. Time Is a Dependency (`LAW-003`) appeared in startup ordering, update recovery, factory transition, service-tool rollout and gap between firmware release and field adoption.

Fourth, they rechecked evidence. Evidence Before Confidence (`LAW-005`) meant old calibration tests did not automatically transfer. Needed representation, migration, system, manufacturing, service-tool compatibility and field-update rehearsal tests.

Fifth, they checked imported assumptions. Every Dependency Is a Decision (`LAW-007`) appeared in binary parser library, supplier script, packaging format and service tool runtime.

Final source diff remained modest. Real change was visible: what changes, what is reviewed, retested, migrated, kept compatible and accepted as uncertainty.

## Обговорення

Change Radius is amount of system surface that must change, be reviewed or retested when one decision changes.

This is intentionally larger than source diff. A one-file change can require contract review, migration, compatibility, factory validation, service-tool verification, release observation, support updates and new evidence. Many-file mechanical edits may have narrow semantic radius.

Cost and risk are determined by surfaces that must move, be reviewed, retested, migrated, remain compatible or observed because one decision changes. Surfaces include behavior, state, contracts, dependencies, timing, tests, tools, releases, owners and evidence.

### Map the Decision

Begin with decision in product/system language, not implementation language.

Weak statement:

> Add a range field to the calibration structure.

Stronger:

> A valid calibration record now includes a measured range, and consumers must preserve that meaning across firmware, tools, update behavior, support export and field service.

Ask:

1. What behavior is changing?
2. Which state authority owns new meaning?
3. Which APIs, protocols, schemas, events, records, files or diagnostics carry it?
4. Which consumers rely on old meaning, including tools and released versions?
5. Which lifecycle moments matter: startup, update, reset, retry, timeout, recovery, factory test, service or support?
6. Which tests and evidence supported old behavior?
7. Which owners and reviewers must participate?
8. Which surfaces must change, be reviewed, retested, migrated or remain compatible?
9. Which parts of radius are still unknown?

Use code search, call graphs, build targets, schema definitions, fixtures, CI, release notes, ADRs, Decision Journal entries, commits, incidents, telemetry, support notes and owner interviews.

### Separate Radius Types

Direct radius is surface intentionally edited. Indirect radius is known surface depending on changed decision. Latent radius is hidden or uncertain surface appearing through old releases, factory behavior, field conditions, copied scripts or team memory. Unknown radius labels what has not been proven. Residual radius is surface intentionally left for later or accepted for current commitment.

These phrases are local thinking tools, not new PEAK concepts.

### Separate Required and Accidental Radius

Broad Change Radius is not automatically bad architecture. Required radius must move to preserve coherent decision. Accidental radius comes from leaked or duplicated knowledge. Goal is not always minimizing radius; goal is making it truthful, planning required radius and shrinking accidental radius.

### Use Dimensions Lightly

Consider behavioral, state, contract, dependency, temporal, test, tool, release, organizational and evidence surfaces. Do not force every change through every dimension. Map should change decision, not become ceremony.

### Manage the Radius

Mapping is useful only if it changes plan. Contain accidental spread by moving translation to boundary, naming authority, making contract explicit, replacing copied schema knowledge, removing back channel or moving platform detail out of product logic.

Sequence required spread deliberately: compatible reader before new writer, migration before behavior change, diagnostics before rollout, manufacturing tool before factory transition, service tool before field support, cleanup after old versions retire.

Manage uncertainty with bounded discovery and staged commitment. Approximate measurement is enough. Change Radius as `METRIC-001` asks for affected surface, not fake precision.

## Інженерний принцип

Map the decision, not the diff. Identify surfaces that must change, be reviewed, retested, migrated or remain compatible; then contain accidental spread and sequence required spread deliberately.

Ask:

1. What decision is changing?
2. Which behavior changes?
3. Who owns authoritative meaning?
4. Which contracts and representations carry it?
5. Which consumers rely on old meaning?
6. Which surfaces change, require review, need retest, migrate or remain compatible?
7. Which radius is required?
8. Which radius is accidental?
9. What remains unknown?
10. Which evidence no longer transfers?
11. What sequence preserves compatibility?
12. Which boundaryboundary accepts residual radius?

## Архітектурна вправа

### Map One Change Before You Implement It

Choose one upcoming change that looks smaller than it feels: configuration, record format, protocol, dependency update, product rule, test fixture or tool behavior.

Write one sentence for changing decision. Then map visible behavior, owner, representation, APIs/protocols/schemas/events/storage/diagnostics/export, consumers, variants, released versions, migration, timing, tests/evidence, manufacturing/service/support/release paths, owners, implementation/review/retest/migration/observation surfaces, required/accidental/unknown radius, containment action, compatibility sequence, reversible first step and ADR or Decision Journal update.

End with four outputs: explicit radius map, sequencing decision, containment action, and accepted residual uncertainty with owner.

## Нотатник Principal Engineer

- The diff is not the change.
- Plan required radius; contain accidental radius.
- Unknown consumers are part of risk.

## ADR

### Chapter ADR: Version and Migrate the Calibration Record Across Product and Tooling boundary

#### Context

Calibration record now needs measured range as part of validity. Old record stored offset and gain. Firmware, boot support, manufacturing stations, service tools, fixtures, exports, diagnostics, packaging, released devices and variants depend on old representation in different ways.

Visible source edit is small, but product decision changes valid record meaning. Resetting old records would lose valid field state. Writer before readers would create release/service risk. Some external consumers may be copied scripts or old workflows.

#### Decision

Introduce versioned calibration record with one authoritative product meaning owned by firmware. Persistent record, service export and tool views are documented representations, not shared C structure layouts.

Firmware reads old and new records before any tool writes new version. Manufacturing station and service tool updated before factory transition. Migration preserves valid old calibration data, populates new range only with evidence and reports version/migration outcome through diagnostics. Downgrade behavior documented.

Service tool and fixtures stop depending on binary padding/private layout. Factory dashboard consumes product diagnostic meanings. Unknown external consumers recorded in Decision Journal (`ARTIFACT-003`) with owner, discovery action and trigger. Temporary old-record compatibility path remains only until supported old firmware and factory image retire.

#### Consequences

Required radius explicit: firmware parsing, persistent schema, boot support, manufacturing write behavior, service-tool behavior, migration/downgrade, diagnostics, release artifacts and targeted tests.

Accidental radius reduced: duplicated layout knowledge removed from tools/fixtures, platform status stops leaking, record version becomes named contract.

Costs: version logic, migration tests, compatibility behavior, diagnostics, tool coordination and cleanup. Residual radius remains for unknown external consumers.

#### Alternatives Considered

- Append field and rely on layout. Unsafe for alignment, old readers and copied parsers.
- Reset old records. Loses valid field calibration.
- Update firmware first and tools later. Bad sequence for factory/service.
- Keep duplicated schemas synchronized manually. Preserves Silent Coupling (`SMELL-001`) and Hidden State (`SMELL-004`).
- Use one global compatibility setting. Creates Global Configuration (`ANTIPATTERN-003`).
- Keep temporary path without trigger. Creates Temporary Solution (`ANTIPATTERN-006`).
- Redesign whole configuration subsystem first. Too broad for scoped decision.

## Коментар редактора

Chapter 15 asks what must move when one decision changes. It is carried by Change Radius (`VOCAB-001`, `METRIC-001`) and lenses from `LAW-001`, `LAW-002`, `LAW-003`, `LAW-005`, `LAW-007`, `SMELL-001`, `SMELL-004`, `SMELL-005`, `ANTIPATTERN-003`, `ANTIPATTERN-006`, ADR (`ARTIFACT-001`) and Decision Journal (`ARTIFACT-003`). It teaches a Principal Engineer habit: make real affected surface visible early enough that architecture can still change the plan.
