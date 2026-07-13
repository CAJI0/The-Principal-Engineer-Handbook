# Managing Change Radius

## Opening Quote

> The diff is not the change. It is only the part of the change that made it into source control.

## Story

### The Calibration Record That Was Not One Change

The proposed work item looked harmless:

> Add one field to the configuration structure.

The team was building an industrial controller that shipped with a calibrated pressure sensor. Each unit left the
factory with a persistent calibration record. Firmware read the record during startup. The manufacturing station wrote
it after test. A service tool displayed it in the field. System tests loaded sample records into devices. Support could
ask a technician to export the record when a device behaved strangely.

The old record stored a signed offset and a gain. A new sensor lot needed one more idea: the calibrated range was no
longer implied by the product model. It had to be recorded with the calibration itself. The first estimate was honest
and incomplete. Add a range field, update the firmware structure, adjust the factory script, and ship.

No one was being careless. The visible edit was small. The product decision was not.

The Principal Engineer asked a different question:

> What decision is changing?

The answer was not "the structure has a new field." The answer was "the meaning of a valid calibration record now
includes a measured range, and every consumer that relies on calibration validity must either understand that range or
remain compatible with records that do not have it."

That sentence changed the plan.

The direct radius was still small: the persistent record definition, the firmware reader, the calibration writer, and a
few tests. The indirect radius was larger. The service tool displayed the old record and treated an unrecognized record
version as "unknown device." A host application cached the exported record for support cases. A packaging step included
sample records used by field diagnostics. A factory dashboard grouped failures by calibration result. None of those
paths were part of the initial source diff.

The latent radius was more interesting. A recovery image copied the calibration record during firmware update without
understanding its contents. It treated the record as bytes, not as an application schema. A product variant used the same
storage page but ignored calibration range. The system test fixtures contained binary records with padding that matched
the old layout. A supplier test bench had a script copied from an earlier manufacturing station. The team could not
prove that every external consumer had been found.

At first, several tempting plans appeared.

One plan appended the field and trusted structure layout. That assumed binary records would remain compatible even
though old readers did not know the new meaning. Another plan reset old records to defaults when the version changed.
That made the update easy but would erase valid field calibration. A third plan put one global compatibility setting in
configuration so firmware, tools, and tests could all switch behavior together. That made one flag responsible for
factory behavior, service behavior, product behavior, and support behavior. It would have turned a calibration decision
into Global Configuration (`ANTIPATTERN-003`). A fourth plan kept a temporary compatibility path with no retirement
trigger. That was a Temporary Solution (`ANTIPATTERN-006`) waiting to become permanent.

The Principal Engineer did not make the change bigger for drama. They made the affected surface visible.

The map separated required radius from accidental radius. Required radius included the record version, firmware
compatibility, manufacturing write behavior, service display behavior, migration behavior, upgrade and downgrade
semantics, diagnostics, and tests that proved old and new records behaved correctly. Those surfaces had to move because
the product meaning had changed.

Accidental radius came from duplicated knowledge. The service tool knew too much about the binary layout. Test fixtures
depended on padding rather than a named record builder. The factory dashboard interpreted raw firmware status values.
That was Platform Leakage (`SMELL-005`), and it created extra review and retest work that did not belong to the product
decision. Some consumers were hidden outside the obvious call graph. That was Silent Coupling (`SMELL-001`). Some state
existed in copies, caches, exported records, and recovery flows. That was Hidden State (`SMELL-004`).

The plan changed from "edit a structure" to "sequence a product decision."

First, the team named one authoritative product meaning and one versioned persistent representation for the calibration
record. That satisfied the state ownership question from Every State Has One Owner (`LAW-001`): the firmware team owned
the persisted meaning, and the manufacturing and service tools consumed that meaning through documented serialized and
export representations rather than through a shared in-memory layout.

Second, they made the contract explicit. Every API Is a Promise (`LAW-002`) applied even though no public web endpoint
was involved. The record format, export file, service-tool view, and diagnostic message were all contracts to someone.
The new reader had to accept old records. The new writer would create new records only after manufacturing and service
tools had been updated. Downgrade behavior was documented rather than assumed.

Third, they mapped time. Time Is a Dependency (`LAW-003`) showed up in startup ordering, update recovery, factory
transition, service-tool rollout, and the time between firmware release and field adoption. A correct record parser was
not enough if the writer arrived before the readers.

Fourth, they rechecked evidence. Evidence Before Confidence (`LAW-005`) meant the old calibration tests did not transfer
automatically. The team needed representation tests, migration tests, system tests, manufacturing station tests, service
tool compatibility tests, and one field-update rehearsal. Passing the old firmware suite would have proved less than it
used to prove.

Fifth, they looked at imported assumptions. Every Dependency Is a Decision (`LAW-007`) showed up in a binary parser
library, a supplier script, a packaging format, and the service tool runtime. Those dependencies imported update cadence,
support horizon, and compatibility obligations into the change.

The final source diff was still modest. The real change was no longer hidden. The team could explain which surfaces
would change, which would be reviewed, which would be retested, which would be migrated, which would remain compatible,
and which uncertainty they were accepting.

## Discussion

Change Radius is the amount of system surface that must change, be reviewed, or be retested when one decision changes.

That definition is intentionally larger than a source diff. A change may touch one file and still require contract
review, migration planning, old-version compatibility, factory validation, service-tool verification, release
observation, support procedure updates, and new evidence. Another change may edit many files mechanically while keeping
the semantic radius narrow.

The cost and risk of a change are determined by the system surfaces that must move, be reviewed, be retested, be
migrated, remain compatible, or be observed because one decision changes - not by the number of edited files. The
surfaces may include behavior, state, contracts, dependencies, timing, tests, tools, releases, owners, and evidence. Not
every change crosses every surface. The point is to notice which ones matter before implementation has already made the
architecture choice for you.

### Map the Decision

Begin by stating the decision that is changing. Do this in product or system language, not implementation language.

Weak statement:

> Add a range field to the calibration structure.

Stronger statement:

> A valid calibration record now includes a measured range, and consumers must preserve that meaning across firmware,
> tools, update behavior, support export, and field service.

The stronger statement exposes affected surface. It lets you ask who owns the authoritative meaning, which contracts
carry it, which old assumptions stop being valid, and which evidence no longer transfers.

A practical map usually asks:

1. What behavior is changing?
2. Which state authority owns the new meaning?
3. Which APIs, protocols, schemas, events, records, files, or diagnostic messages carry it?
4. Which consumers rely on the old meaning, including tools and released versions?
5. Which lifecycle moments matter: startup, update, reset, retry, timeout, recovery, factory test, service, or support?
6. Which tests and evidence supported the old behavior?
7. Which owners and reviewers must participate?
8. Which surfaces must change, be reviewed, be retested, migrated, or remain compatible?
9. Which parts of the radius are still unknown?

Incomplete documentation is normal. Use code search, call graphs, build targets, schema definitions, test fixtures,
continuous integration, release notes, ADRs, Decision Journal entries, commit history, incident reports, field
telemetry, support notes, and interviews with owners. No source is complete by itself. Static analysis misses human
workflows. Team memory misses old automation. Tests miss tools they never run.

### Separate Direct, Indirect, Latent, Unknown, and Residual Radius

Direct radius is the surface you intentionally edit. In the calibration story, that included the record definition, the
firmware parser, and the manufacturing writer.

Indirect radius is the known surface that depends on the changed decision without necessarily being edited. A service
tool, export format, product variant, or diagnostic workflow may rely on the old meaning even when its source files do
not change.

Latent radius is the hidden or uncertain surface that may only appear through failures, old releases, factory behavior,
field conditions, copied scripts, or team memory. Latent radius is where Silent Coupling (`SMELL-001`) and Hidden State
(`SMELL-004`) often appear.

Unknown radius is not a confession of incompetence. It is a truthful label for surfaces the team has not proven. Unknown
radius should change commitment, review depth, test scope, release exposure, observation, and reversibility. It should
not automatically stop the work.

Residual radius is the surface intentionally left for later or accepted for the current commitment. A temporary reader
for old records, an external script that will be retired after a factory date, or an unknown third-party consumer may be
residual radius. Record it. Give it an owner. Give it a trigger for review or removal.

These phrases are local tools for thinking. They are not new PEAK concepts.

### Separate Required and Accidental Radius

A broad Change Radius is not automatically bad architecture.

Required radius is affected surface that must move to preserve one coherent decision. If a persistent record changes
meaning, migration and compatibility are real work. If a safety rule changes, behavior, diagnostics, tests, release
notes, and support expectations may all need to move. Pretending the radius is smaller only moves risk to integration,
field service, or customers.

Accidental radius is affected surface created by leaked or duplicated knowledge. If a service tool reads internal
storage layout, if a UI interprets platform status values, if manufacturing scripts duplicate firmware validation, or
if a broad setting changes unrelated modules, the radius is larger than the product decision requires. That is the part
you contain.

The goal is not always to minimize Change Radius. The goal is to make it truthful, plan the required radius, and shrink
the accidental radius.

### Use Dimensions Without Turning Them Into Ceremony

A useful Change Radius map is multi-dimensional, but it should remain lightweight. For a specific change, consider:

- behavioral surface: externally or internally observable behavior;
- state surface: authorities, transitions, persistence, caches, copies, and migration paths;
- contract surface: APIs, protocols, schemas, events, commands, records, and compatibility promises;
- dependency surface: imported libraries, platforms, tools, suppliers, and support horizons;
- temporal surface: ordering, startup, timeout, retry, reset, update, recovery, and lifecycle assumptions;
- test surface: unit, integration, system, manufacturing, compatibility, field, and hardware-in-the-loop tests;
- tool surface: build, calibration, service, packaging, deployment, diagnostics, and support tools;
- release surface: shipped versions, upgrade paths, downgrade paths, staged exposure, and release artifacts;
- organizational surface: owners, reviewers, teams, suppliers, and operational roles;
- evidence surface: old evidence that no longer transfers and new evidence that must be gathered.

Do not force every change through every dimension. The map should help the decision. When the map becomes a ritual
performed after the decision is already locked, it has stopped doing architecture work.

### Manage the Radius

Mapping is only useful if it changes the plan.

Contain accidental spread by moving translation to a boundary, naming one authority, making an implicit contract
explicit, replacing copied schema knowledge with a shared representation, removing a back channel, or moving platform
detail out of product logic. A smaller accidental radius should be visible in review and test work, not merely in a
diagram.

Sequence required spread deliberately. Sometimes the compatible reader must ship before the new writer. Sometimes a
schema migration must precede a behavior change. Sometimes diagnostics should ship before a staged rollout. Sometimes a
manufacturing tool must move before the factory transition. Sometimes service tools must be updated before field
support can accept the new record. Sometimes cleanup waits until old versions retire.

Manage uncertainty with bounded discovery and staged commitment. You can proceed while naming unknown consumers, but
the plan should reflect them. A reversible first step, a narrower release exposure, targeted observation, or a Decision
Journal entry can be more honest than a confident plan built on silence.

Approximate measurement is enough. Change Radius as `METRIC-001` asks for affected surface, not fake precision. Compare
one design option with another. Compare expected affected surface with what the work actually revealed. Compare a
boundary improvement before and after. A map that exposes five owners, three contracts, two old releases, one factory
tool, and missing evidence is more useful than a number that pretends those surfaces are interchangeable.

### Keep the Chapter Boundaries Clear

Chapter 14 taught how to draw boundaries around responsibility, authority, knowledge, vocabulary, dependency direction,
translation, and integrity. This chapter assumes those ideas and asks what must move when a decision crosses or tests
those boundaries.

Chapter 16 will teach failure and recovery design. This chapter may notice rollback, recovery, and observation surfaces,
but it does not design the full failure model.

Chapter 17 will teach ADR and RFC practice. This chapter uses an ADR and may use a Decision Journal (`ARTIFACT-003`),
but it does not teach artifact lifecycle.

Chapter 18 will teach Architecture Review. This chapter identifies review surface, but it does not run the ritual.

Chapter 19 will teach Architecture Freeze. This chapter records residual radius and uncertainty, but it does not define
freeze policy.

## Engineering Principle

Map the decision, not the diff. Identify the surfaces that must change, be reviewed, be retested, migrated, or remain compatible; then contain accidental spread and sequence the required spread deliberately.

Use the principle before a change hardens into tickets or scattered pull requests. Ask:

1. What decision is changing?
2. Which behavior changes?
3. Who owns the authoritative meaning?
4. Which contracts and representations carry it?
5. Which consumers rely on the old meaning?
6. Which surfaces change, require review, need retest, migrate, or remain compatible?
7. Which radius is required?
8. Which radius is accidental?
9. What remains unknown?
10. Which evidence no longer transfers?
11. What sequence preserves compatibility?
12. Which owner accepts the residual radius?

The answers do not need to be perfect. They need to be truthful enough to change the architecture plan.

## Architecture Exercise

### Map One Change Before You Implement It

Choose one upcoming change that looks smaller than it feels. It can be a configuration change, a record-format change,
a protocol change, a dependency update, a product-rule change, a test-fixture change, or a tool behavior change.

Write one sentence for the decision that is changing. Avoid file names unless they are part of the decision.

Then map:

1. visible behavior affected;
2. authoritative owner;
3. current representation;
4. APIs, protocols, schemas, events, storage, diagnostics, and export formats;
5. direct consumers;
6. indirect consumers;
7. uncertain or historical consumers;
8. hardware and software variants;
9. released versions and compatibility obligations;
10. state and migration implications;
11. timing and lifecycle assumptions;
12. tests and evidence that supported the old behavior;
13. manufacturing, calibration, service, support, packaging, and release paths;
14. owners and reviewers;
15. implementation surface;
16. review surface;
17. retest surface;
18. migration surface;
19. release-observation surface;
20. required radius;
21. accidental radius;
22. unknown radius;
23. containment action;
24. compatibility sequence;
25. reversible first step;
26. ADR or Decision Journal update.

End the exercise with four outputs:

1. one explicit radius map;
2. one sequencing decision;
3. one containment action;
4. one accepted residual uncertainty with an owner.

## Principal's Notebook

- The diff is not the change.
- Plan required radius; contain accidental radius.
- Unknown consumers are part of the risk.

## ADR

### Chapter ADR: Version and Migrate the Calibration Record Across Product and Tooling Boundaries

#### Context

The product calibration record now needs to store a measured range as part of calibration validity. The old persistent
record stored offset and gain only. Firmware, boot support, manufacturing stations, service tools, test fixtures,
export files, diagnostics, packaging artifacts, released devices, and product variants depend on the old representation
in different ways.

The visible source edit is small, but the product decision changes the meaning of a valid record. Resetting old records
to defaults would lose valid field state. Updating the writer before compatible readers exist would create avoidable
release and service risk. Some external consumers may be copied scripts or old support workflows that are not visible
in the main repository.

#### Decision

We will introduce a versioned calibration record with one authoritative product meaning owned by firmware. The
persistent record, service export, and tool-facing views will be documented representations of that meaning, not shared
C structure layouts.

Firmware will read old and new records before any tool writes the new version. The manufacturing station and service
tool will be updated and verified before the factory transition. The migration will preserve valid old calibration
data, populate the new range only when evidence exists, and report record version and migration outcome through
diagnostics. Downgrade behavior will be documented for supported releases.

The service tool and test fixtures will stop depending on binary padding or private layout assumptions. They will use
named record builders or documented export formats. The factory dashboard will consume product diagnostic meanings
rather than raw platform status values.

Unknown external consumers will be recorded in the Decision Journal (`ARTIFACT-003`) with an owner, discovery action,
and review trigger. The temporary old-record compatibility path will remain only until the last supported old firmware
and factory image retire.

#### Consequences

The required radius is explicit: firmware parsing, persistent schema, boot support, manufacturing write behavior,
service-tool display and edit behavior, migration and downgrade behavior, diagnostics, release artifacts, and targeted
tests move together.

The accidental radius is reduced: duplicated layout knowledge is removed from tools and fixtures, platform status stops
leaking into product workflows, and the record version becomes a named contract rather than a structure accident.

The costs are real. The team adds version logic, migration tests, compatibility behavior, diagnostics, tool
coordination, and cleanup work. Some residual radius remains because unknown external consumers cannot be proven away
before implementation. That uncertainty is accepted with an owner and a review trigger.

#### Alternatives Considered

Append a field and rely on structure layout. Rejected because alignment, old readers, exported records, and copied
parsers make this compatibility claim unsafe.

Reset old records to defaults. Rejected because valid field calibration would be lost.

Update firmware first and tools later. Rejected because the writer and readers would be out of sequence for factory and
service workflows.

Keep duplicated schemas synchronized manually. Rejected because it preserves Silent Coupling (`SMELL-001`) and Hidden
State (`SMELL-004`) across tools and tests.

Use one global compatibility setting. Rejected because it would turn product, factory, service, and support meanings
into Global Configuration (`ANTIPATTERN-003`).

Keep a temporary compatibility path with no retirement trigger. Rejected because it would become a Temporary Solution
(`ANTIPATTERN-006`) with unowned residual radius.

Redesign the entire configuration subsystem first. Rejected because the current decision can be handled with a scoped
versioning and migration plan.

## Editor's Commentary

Chapter 15 is the second practice chapter in Part III. Chapter 14 asked where responsibility, authority, vocabulary,
and translation belong. This chapter asks what must move when one of those decisions changes.

The chapter is carried by a relationship set rather than by a primary PEAK concept. Change Radius (`VOCAB-001`) supplies
the definition. Change Radius as a metric (`METRIC-001`) supplies the approximate affected-surface posture. The chapter
uses Every State Has One Owner (`LAW-001`), Every API Is a Promise (`LAW-002`), Time Is a Dependency (`LAW-003`),
Evidence Before Confidence (`LAW-005`), and Every Dependency Is a Decision (`LAW-007`) as lenses on affected surface.
It also uses Silent Coupling (`SMELL-001`), Hidden State (`SMELL-004`), Platform Leakage (`SMELL-005`), Global
Configuration (`ANTIPATTERN-003`), Temporary Solution (`ANTIPATTERN-006`), ADR (`ARTIFACT-001`), and Decision Journal
(`ARTIFACT-003`) without creating new canon.

The chapter avoids turning Change Radius into project planning, a static-analysis survey, a schema-migration tutorial,
or release management. It teaches a Principal Engineer habit: make the real affected surface visible early enough that
architecture can still change the plan.

The handoff is deliberate. Chapter 16 can now take failure and recovery design further. Chapter 17 can teach ADR and RFC
practice in full. Chapter 18 can turn identified review surface into Architecture Review. Chapter 19 can handle freeze,
exceptions, and validated learning without pretending every residual radius disappeared.
