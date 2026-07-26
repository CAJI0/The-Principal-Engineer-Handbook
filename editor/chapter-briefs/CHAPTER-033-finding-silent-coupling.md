# CHAPTER-033 Canonical Brief: Finding Silent Coupling

## 1. Metadata

- Stable ID: `CHAPTER-033`.
- Title: `Finding Silent Coupling`.
- Part: Part VI - Legacy.
- Chapter number: 33.
- Expected manuscript path: `book/06-legacy/33-finding-silent-coupling.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-033-finding-silent-coupling.md`.
- Branch: `chapter33`.
- Verified baseline `origin/main`: `1a0431bbea8fb7f4a1bfe27b43175753e5873331`.
- Baseline evidence: PR #34 Chapter 32 squash merge commit,
  `Chapter 32: Reading a Legacy System (#34)`.
- Chapter 32 feature Freeze commit handled through squash-merge evidence, not direct ancestry:
  `499fede053431e5a0544113199f22607816d3663`.
- Canonical predecessor: `CHAPTER-032` - Reading a Legacy System.
- Part position: second chapter of Part VI - Legacy.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 33 illustrates the existing `SMELL-001` Silent Coupling smell and references the
  existing `VOCAB-008` Silent Coupling vocabulary term; it must not add a `primary_concept` registry field.
- Central illustrated concept: `SMELL-001` - Silent Coupling.
- Central vocabulary term: `VOCAB-008` - Silent Coupling.
- Central chapter-local practice: making behavior that changes together visible before local edits are trusted.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `1a0431bbea8fb7f4a1bfe27b43175753e5873331`.
- That baseline is the PR #34 Chapter 32 squash merge commit,
  `Chapter 32: Reading a Legacy System (#34)`.
- The squash commit includes the Chapter 32 manuscript, canonical brief, editor log, and index updates.
- `CHAPTER-032` is registered as `canonical` in `knowledge/index.yaml`.
- Chapter 32 is the first Part VI chapter and is canonical on `origin/main`.
- The Chapter 32 feature Freeze commit `499fede053431e5a0544113199f22607816d3663` is not required as a direct ancestor
  because Chapter 32 reached `origin/main` through squash merge and was verified by canonical file and registry state.
- `CHAPTER-001` through `CHAPTER-032` are registered as `canonical` in `knowledge/index.yaml`.
- The table of contents places `Finding Silent Coupling` second in Part VI - Legacy.
- The remaining Part VI sequence is `Managing Utility Gravity`, `Reducing Boolean Explosion`, `Deleting Safely`, and
  `Refactoring Without Losing Product Trust`.
- `book/06-legacy/README.md` remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-033` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 33 canonical brief or reader-facing manuscript existed before this registration.
- No tracked `site/` output existed before this registration.
- The PEAK graph already contains `SMELL-001` Silent Coupling and `VOCAB-008` Silent Coupling, so no new coupling
  concept is required.

## 3. Part VI Role

Chapter 33 follows Chapter 32 by narrowing the legacy-reading practice to one dangerous class of discovery: behavior
that must change together but is not represented by an explicit contract, record, owner, schema, API, test, or review
path. Chapter 32 taught the reader to read a legacy system before changing it. Chapter 33 teaches the reader to find
the hidden behavioral ties that make local changes unsafe even when code ownership, tests, or diagrams appear local.

The chapter should stay concrete and diagnostic. It is not a generic dependency-mapping chapter, cleanup chapter,
utility-gravity chapter, Boolean Explosion chapter, deletion chapter, or refactoring-with-trust chapter. It should teach
how a Principal Engineer exposes silent coupling through evidence, shared behavior, shared timing, shared data shape,
shared state interpretation, shared diagnostic language, release paths, tools, tests, support workflows, and team
coordination.

## 4. Canonical Purpose

Prepare Chapter 33 to teach that silent coupling is found by looking for behavior that must remain aligned across
surfaces that do not name their relationship. The future manuscript should show how a Principal Engineer moves from
"the change is local" to "what else depends on this behavior even though the dependency is not explicit?"

Candidate thesis for the future manuscript:

> Silent coupling is found where behavior changes together but contracts, ownership, records, and review paths stay
> separate.

The chapter should move the reader away from asking:

> Which files call this code?

to asking:

> Which people, tools, tests, states, events, releases, and procedures assume this behavior will not change?

## 5. Primary-Concept Resolution

Chapter 33 has no new primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. The graph already
contains `SMELL-001` Silent Coupling and `VOCAB-008` Silent Coupling. Chapter 33 should illustrate the existing smell
and use the existing vocabulary term while referencing the laws, metrics, records, rituals, smells, anti-patterns, and
failure stories needed to find and surface hidden behavioral dependencies.

Coupling map, shared assumption, hidden contract, dependency trace, blast path, contract probe, evidence trace,
coupling ledger, and shared behavior map remain chapter-local prose. Do not create a new PEAK concept, ID,
artifact, ritual, metric, vocabulary term, smell, anti-pattern, failure story, primary-concept field, or relationship
verb for them.

## 6. Central Thesis

Silent coupling makes a change look local while its consequences are shared. Finding it means tracing behavior, data,
time, state, diagnostics, tools, tests, records, release paths, and human workflows until the team can decide whether
the dependency should become an explicit contract, receive an owner, gain evidence, or be removed later.

Approved supporting formulation for the future draft:

> A local change is only local after the hidden dependents have been named.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, artifact, ritual,
metric, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. dependency discovery means checking imports, call graphs, package boundaries, or service diagrams;
2. a change is local when the affected code has one owner;
3. tests reveal every consumer that matters;
4. a diagnostic string, named value, event name, file format, or timing gap is not an interface;
5. support procedures and service tools are outside the architecture;
6. if two teams do not coordinate formally, their systems are not coupled;
7. stale records are less important than current code;
8. hidden coupling is found only after a production break;
9. all discovered coupling should be removed immediately;
10. coupling is always a design failure by the previous team.

By the end of the chapter, the reader should be able to:

1. define silent coupling as behavior shared without an explicit contract;
2. find coupling candidates across code, data, events, diagnostics, tooling, support, release, manufacturing, tests, and
   human routines;
3. distinguish visible dependency from silent behavioral dependence;
4. use Change Radius, Discoverability, API Stability, and Bus Factor as evidence lenses;
5. test whether two surfaces must change together;
6. name the owner, promise, dependent, evidence source, and failure mode of a silent coupling;
7. decide whether to record, review, stabilize, probe, or later remove the coupling;
8. avoid turning discovery into blame or an immediate refactoring campaign.

## 8. Silent Coupling Scope

For Chapter 33, silent coupling means a dependency that affects behavior but is not represented as an explicit contract,
record, ownership boundary, schema, API, or review path.

The future manuscript may examine:

- diagnostic strings consumed by service tools or support scripts;
- event names, payload shapes, named values, and ordering assumptions;
- firmware behavior interpreted by backend services or manufacturing tools;
- backend responses interpreted by device code, tools, support procedures, or release scripts;
- shared configuration flags and variant behavior;
- state interpreted by multiple owners without a shared contract;
- tests that encode assumptions missing from product documentation;
- release notes, support articles, and field procedures that become operational interfaces;
- timing windows, retry behavior, startup order, upgrade order, and recovery order;
- human coordination habits that substitute for explicit contracts;
- ADR, RFC, Decision Journal, Event Catalog, and Architecture Ledger gaps that hide a dependency.

The chapter should make coupling discoverable and actionable. It should not require the team to remove every coupling
before making progress.

## 9. Finding Order and Evidence

The future manuscript should teach a finding order that starts from the requested change and asks what else would have
to change, fail, or coordinate if the behavior moved.

Useful finding layers:

1. What behavior is being changed?
2. Which product promise, diagnostic, event, state, data shape, or timing assumption carries that behavior?
3. Which code, tool, test, release path, support procedure, manufacturing step, or person assumes it?
4. Where is the assumption recorded, tested, reviewed, or owned?
5. What would break if the behavior changed while names and interfaces stayed the same?
6. Which teams would have to coordinate by memory?
7. Which records are missing, stale, or misleading?
8. What evidence proves the coupling is active rather than folklore?
9. Should the dependency become an explicit contract, get an owner, receive a test, enter a record, or be queued for
   later removal?

Do not turn this into a rigid checklist. The order should change the reader's attention from static structure to
behavior that has dependents.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 33 covers:

- finding silent coupling as hidden behavioral dependency;
- behavior that changes together without shared contracts;
- dependencies through diagnostics, events, state meanings, data shapes, timing, tools, support, manufacturing, tests,
  releases, upgrade paths, and team memory;
- evidence from code, tests, logs, runtime behavior, support notes, release records, tool repositories, incident
  reports, and senior memory;
- Change Radius when a local edit has non-local effects;
- Discoverability gaps when dependents cannot be found;
- API Stability when behavior, errors, timing, and meaning are trusted beyond formal signatures;
- Bus Factor risk when one person knows the hidden relation;
- ADRs, RFCs, Decision Journal entries, Event Catalog entries, Architecture Ledger rows, Architecture Review, and
  Architecture Health Review as ways to make discovered coupling visible;
- hidden state, platform leakage, global configuration, and temporary solutions as common sources of silent coupling;
- failure stories where timing, release, and single-expert memory exposed hidden dependence;
- non-blame treatment of legacy decisions.

### Explicitly Out of Scope

Do not turn Chapter 33 into:

- a general dependency management chapter;
- a code-graph or static-analysis tutorial;
- a microservices coupling essay;
- a platform or utility-gravity chapter;
- a Boolean Explosion chapter;
- a safe-deletion chapter;
- a broad refactoring chapter;
- a modernization or rewrite argument;
- a documentation-theater chapter;
- an incident postmortem chapter;
- a blame narrative about previous engineers;
- a new PEAK concept proposal.

## 11. Recommended Legacy-System Story

Use a story close to:

`The Change That Broke Nothing Locally`

A team changes a legacy device-registration behavior that appears local. The modified code belongs to one firmware
component, tests pass, and the visible API signature does not change. No import graph or service diagram suggests a
large risk.

After release validation, another surface fails:

- a service tool can no longer identify a recoverable startup state;
- a backend mapper treats a changed named value or diagnostic wording differently;
- a manufacturing script depends on field ordering or an event sequence;
- a support procedure tells technicians to wait for a phrase or state that no current contract names;
- an upgrade path depends on one retry window being longer than another;
- a test station accepts behavior the product docs never describe.

The system did not break locally. The hidden relationship broke somewhere the local team did not know to review.

The Principal Engineer frames the work again:

> We do not yet know the dependents of this behavior.

The intervention should trace behavior rather than files. The team compares the changed behavior against diagnostics,
events, tool code, backend mappings, manufacturing scripts, release notes, support procedures, tests, logs, and the
Architecture Ledger. They discover that two or three surfaces must change together despite having separate owners and
separate review paths.

The story should end with the coupling made explicit: an owned contract, a characterization test, an Event Catalog row,
an ADR or Decision Journal note, an Architecture Ledger entry, and a review or follow-up decision. It should not end
with a full refactor or deletion campaign.

## 12. Expected Discussion Arc

The future manuscript should move through this arc:

1. Define silent coupling as hidden behavioral dependency.
2. Show why static structure can make a change appear local while product behavior is shared.
3. Start from one requested change and trace who or what assumes the behavior.
4. Examine diagnostics, events, data shapes, state meanings, timing, tools, tests, releases, support, and memory.
5. Use Change Radius, Discoverability, API Stability, and Bus Factor as evidence lenses.
6. Distinguish active coupling from folklore by demanding evidence.
7. Decide whether the coupling should become an explicit contract, test, owner, record, review item, or later removal
   candidate.
8. Record the discovered relation without creating a new canonical artifact.
9. Hand off to later Part VI chapters by naming forces the discovery may reveal without teaching them early.

## 13. Boundaries With Later Part VI Chapters

Chapter 33 owns finding Silent Coupling. It must preserve later Part VI chapters:

- Chapter 34 owns Utility Gravity.
- Chapter 35 owns Boolean Explosion.
- Chapter 36 owns Deleting Safely.
- Chapter 37 owns Refactoring Without Losing Product Trust.

Chapter 33 may say that silent coupling can feed utility gravity, Boolean Explosion, deletion risk, and refactoring
trust risk. It must not teach how to manage utility gravity, reduce Boolean Explosion, delete safely, or refactor while
preserving product trust. Its job is to make hidden behavior-dependency visible and decide the next responsible action.

## 14. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating them:

- Chapter 32 supplies the legacy-reading handoff: find what the system protects before changing it.
- Part I supplies Principal Engineer judgment, better questions, ownership beyond code, evidence, and stewardship.
- Part II supplies laws used as finding lenses: state ownership, API promises, dependencies, timing, and evidence.
- Part III supplies Change Radius, ADRs, RFCs, Architecture Review, Architecture Freeze, and decision records.
- Part IV supplies product obligations: manufacturing, field reality, configuration, variants, observability, release
  discipline, upgrade paths, and support promises.
- Part V supplies review memory, rituals, mentoring through artifacts, alignment, and architecture health reviews.

Chapter 33 should apply these tools to hidden coupling. It must not summarize or re-teach their primary lessons.

## 15. Applicability

Chapter 33 is useful when:

- a local change affects firmware, backend, tooling, manufacturing, support, release, or field behavior;
- a diagnostic string, named value, event, file format, timeout, retry, or state meaning may be consumed elsewhere;
- two teams coordinate by memory instead of contract;
- tests pass but the product, service tool, backend, or support procedure might still depend on old behavior;
- ownership is clear in code but unclear in behavior;
- release notes or support articles describe behavior no current contract names;
- one senior engineer knows why two surfaces must move together;
- a small change needs many reviewers for reasons the architecture does not explain;
- a team wants to refactor or delete behavior before naming who depends on it.

Not every dependency is silent coupling. Use the practice when the dependency affects behavior and is missing from the
contract, record, owner, test, or review path that should make it discoverable.

## 16. Limits and Exceptions

Finding silent coupling should be proportionate.

- During an active incident, stabilize the incident first and use coupling discovery to support diagnosis.
- For a truly local low-risk change with clear contracts and strong tests, a lightweight check may be enough.
- If the coupling is intentional and already recorded, use the record instead of rediscovering it.
- If evidence is thin, name the uncertainty and choose a safe probe.
- If removal is attractive, preserve Chapter 36's boundary: first make the dependent behavior visible, then decide
  whether deletion is responsible.
- If the coupling crosses teams, avoid assigning blame; assign an owner, evidence source, and next decision.

The chapter should avoid both extremes: trusting local structure blindly and treating every possible consumer as a
blocker.

## 17. Violation Patterns

The future manuscript should warn against these patterns:

- relying only on import graphs or call graphs;
- treating API signatures as the whole promise;
- assuming diagnostic text, event names, named values, and timing windows are not interfaces;
- trusting tests without checking tools, release paths, support procedures, and field behavior;
- depending on senior memory without repairing the record;
- discovering coupling during release validation and calling it "surprising";
- recording the coupling without assigning an owner or decision path;
- removing coupling before understanding who depends on it;
- using discovered coupling as a reason to demand a rewrite;
- blaming prior engineers for a dependency that may have protected a real product promise.

## 18. Engineering Principle Target

Target meaning:

> Treat silent coupling as hidden shared behavior. Find it by tracing what must change together across code, data, time,
> tools, tests, releases, and people; then make the relationship explicit enough to own, test, review, or retire.

Potential questions:

1. What behavior is changing?
2. Who or what assumes that behavior?
3. Which diagnostic, event, named value, state, timing window, data shape, or support instruction carries it?
4. Where is the promise recorded or tested?
5. Which owner would know if it changed?
6. What would fail if the code changed but the name stayed the same?
7. Which team would discover the dependency only after release?
8. What evidence proves this is active coupling?
9. Should the relation become a contract, test, record, review item, or later deletion candidate?

The final manuscript may shorten this list for rhythm. It must not become an oversized checklist.

## 19. Architecture Exercise Target

Use:

`Trace a Hidden Coupling Before the Change`

Ask the reader to choose one planned or recent change and document:

- behavior being changed;
- visible owner;
- suspected hidden dependent;
- state, API, diagnostic, event, data shape, timing, or tool surface involved;
- evidence source;
- missing record or contract;
- likely Change Radius;
- failure mode if the relation is missed;
- owner to involve;
- record to update;
- test or safe probe to add;
- decision to make now;
- later cleanup, deletion, or refactoring question to defer.

End with:

1. one hidden dependent to verify;
2. one evidence source;
3. one owner;
4. one record or contract to repair;
5. one next decision.

Do not create a new canonical artifact.

## 20. Chapter-Local ADR Brief

Use a decision close to:

`Make Device Registration Diagnostics an Explicit Contract Before Changing Startup Behavior`

Context:

- a local firmware startup change modifies a diagnostic state, named value, or retry window;
- the service tool, backend mapper, support procedure, manufacturing script, and release validation may depend on the
  old behavior;
- tests cover the firmware path but not every dependent surface;
- no current record names the shared behavior as a contract.

Decision:

- do not treat the firmware change as local until the hidden dependents are named;
- trace the behavior through diagnostics, events, backend mappings, service tooling, manufacturing scripts, release
  notes, support procedures, tests, logs, and owners;
- add a characterization test or contract test for the shared behavior;
- update the Event Catalog, ADR, Decision Journal, or Architecture Ledger with owner, dependents, evidence, and revisit
  trigger;
- route the change through Architecture Review if the coupling crosses ownership or release boundaries;
- defer deletion or larger refactoring until the coupling is explicit and owned.

Alternatives:

- rely on import graphs and existing unit tests;
- change the diagnostic wording because it looks internal;
- ask the senior engineer and rely on memory;
- document the coupling without assigning an owner;
- remove the fallback as dead code;
- broaden the refactor before the coupling is understood.

Consequences should include slower first edit, fewer release surprises, clearer ownership, a better test surface,
updated records, and a path toward later simplification. The ADR must not reduce to "document before changing."

## 21. PEAK Concept Map

### Concepts Inspected

- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-005` - Evidence Before Confidence.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `VOCAB-008` - Silent Coupling.
- `VOCAB-009` - Utility Gravity.
- `VOCAB-010` - Boolean Explosion.
- `METRIC-001` - Change Radius.
- `METRIC-002` - Bus Factor.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-006` - Architecture Ledger.
- `RITUAL-001` - Architecture Review.
- `RITUAL-004` - Architecture Health Review.
- `SMELL-001` - Silent Coupling.
- `SMELL-002` - Utility Gravity.
- `SMELL-003` - Boolean Explosion.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-006` - Temporary Solution.
- `FAILURE-002` - One Lost Packet.
- `FAILURE-004` - The Hero Engineer.
- `FAILURE-005` - The Release We Should Have Delayed.

### Selected Concepts

- `SMELL-001` - Silent Coupling: central illustrated smell because Chapter 33 teaches how to find hidden behavioral
  dependencies that make local changes unsafe.
- `VOCAB-008` - Silent Coupling: material vocabulary because the chapter gives the reader a precise name for behavior
  that changes together without visible contract.
- `LAW-002` - Every API Is a Promise: material because diagnostics, events, named values, tool screens, backend responses,
  and compatibility behavior may be promises even when they look internal.
- `LAW-007` - Every Dependency Is a Decision: material because silent coupling often arrives through tools, scripts,
  data formats, procedures, vendor behavior, release paths, and people, not only code imports.
- `LAW-001` - Every State Has One Owner: material because hidden coupling often appears when multiple surfaces
  interpret or mutate state without a shared owner.
- `LAW-003` - Time Is a Dependency: material because retry windows, startup order, event ordering, upgrade sequence,
  and timeout behavior frequently carry hidden dependents.
- `LAW-005` - Evidence Before Confidence: material because the chapter requires proof from tests, logs, tools, release
  records, support notes, runtime behavior, and memory before treating a coupling as active.
- `VOCAB-001` - Change Radius: material vocabulary for the affected surface behind a supposedly local change.
- `METRIC-001` - Change Radius: material because silent coupling increases the real affected surface of one change.
- `METRIC-002` - Bus Factor: material because a hidden dependency known only through one senior engineer is a core
  silent-coupling risk.
- `METRIC-003` - Discoverability: material because the chapter asks whether a future engineer can find the hidden
  dependent without folklore.
- `METRIC-004` - API Stability: material because silent coupling often depends on stable behavior, errors, timing, and
  meanings that were never named as contract.
- `ARTIFACT-001` - ADR: material because consequential discovered coupling may need a durable architectural decision.
- `ARTIFACT-002` - RFC: material because cross-team changes that reveal silent coupling may need proposal review before
  the relation hardens.
- `ARTIFACT-003` - Decision Journal: material because some discovered couplings need lightweight decision memory rather
  than a full ADR.
- `ARTIFACT-005` - Event Catalog: material because event meanings, ordering, producers, and consumers are common places
  where silent coupling hides.
- `ARTIFACT-006` - Architecture Ledger: material because active coupling needs owner, status, risk, and revisit
  visibility.
- `RITUAL-001` - Architecture Review: material because a discovered cross-boundary coupling may need review before a
  local change is shipped.
- `RITUAL-004` - Architecture Health Review: material as a source of weak coupling signals and as a predecessor handoff
  from Chapter 31 and Chapter 32.
- `SMELL-004` - Hidden State: material because hidden state can create hidden behavior dependencies.
- `SMELL-005` - Platform Leakage: material because platform details escaping their boundary can silently couple product
  code, tools, and support.
- `ANTIPATTERN-003` - Global Configuration: material because broad flags often silently couple variants, startup paths,
  tools, and owners.
- `ANTIPATTERN-006` - Temporary Solution: material because temporary fallbacks often become unnamed product promises.
- `FAILURE-002` - One Lost Packet: material because packet loss, retry timing, and diagnostic evidence show hidden
  timing and protocol coupling.
- `FAILURE-004` - The Hero Engineer: material because single-person memory can be the only place a coupling is known.
- `FAILURE-005` - The Release We Should Have Delayed: material because release validation often exposes hidden
  coupling after local tests pass.

### Rejected Concepts

- `LAW-004` - Simplicity Is a Feature: relevant background, but Chapter 33 finds hidden coupling before arguing for
  simplification.
- `LAW-006` - Unused Flexibility Is Waste: nearby when a fallback looks unused, but Chapter 36 owns deletion and Chapter
  37 owns trust-preserving refactoring.
- `VOCAB-009` and `SMELL-002` - Utility Gravity: Chapter 34 owns utility gravity.
- `VOCAB-010` and `SMELL-003` - Boolean Explosion: Chapter 35 owns Boolean Explosion.
- `VOCAB-007` and `METRIC-005` - Architecture Health: Chapter 31 owns the health frame; Chapter 33 only uses health
  review as a source of signals.
- `ARTIFACT-004` - Mistake Ledger: possible evidence, but Chapter 33's active record work is better carried by ADR,
  RFC, Decision Journal, Event Catalog, and Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register: possible input from Chapter 31, but not material enough for the registered
  graph.
- `RITUAL-002` - Architecture Freeze: possible later release output, but not part of finding the coupling.
- `ANTIPATTERN-002` - HAL Everywhere and `ANTIPATTERN-005` - Callback Hell: possible local sources, but not material
  enough for outgoing edges.
- `SMELL-006` - Event Explosion: related to event cleanup, but Chapter 33 only needs Event Catalog evidence for hidden
  coupling.
- `FAILURE-001` - Logger That Became a Platform: reserved for utility gravity and accidental-platform discussions.
- `FAILURE-003` - The Successful Prototype: background for how legacy forms, but not central to finding silent
  coupling.

### Exact Outgoing Relationships

```yaml
- from: CHAPTER-033
  type: illustrates
  to: SMELL-001
- from: CHAPTER-033
  type: references
  to: VOCAB-008
- from: CHAPTER-033
  type: references
  to: LAW-002
- from: CHAPTER-033
  type: references
  to: LAW-007
- from: CHAPTER-033
  type: references
  to: LAW-001
- from: CHAPTER-033
  type: references
  to: LAW-003
- from: CHAPTER-033
  type: references
  to: LAW-005
- from: CHAPTER-033
  type: references
  to: VOCAB-001
- from: CHAPTER-033
  type: references
  to: METRIC-001
- from: CHAPTER-033
  type: references
  to: METRIC-002
- from: CHAPTER-033
  type: references
  to: METRIC-003
- from: CHAPTER-033
  type: references
  to: METRIC-004
- from: CHAPTER-033
  type: references
  to: ARTIFACT-001
- from: CHAPTER-033
  type: references
  to: ARTIFACT-002
- from: CHAPTER-033
  type: references
  to: ARTIFACT-003
- from: CHAPTER-033
  type: references
  to: ARTIFACT-005
- from: CHAPTER-033
  type: references
  to: ARTIFACT-006
- from: CHAPTER-033
  type: references
  to: RITUAL-001
- from: CHAPTER-033
  type: references
  to: RITUAL-004
- from: CHAPTER-033
  type: references
  to: SMELL-004
- from: CHAPTER-033
  type: references
  to: SMELL-005
- from: CHAPTER-033
  type: references
  to: ANTIPATTERN-003
- from: CHAPTER-033
  type: references
  to: ANTIPATTERN-006
- from: CHAPTER-033
  type: references
  to: FAILURE-002
- from: CHAPTER-033
  type: references
  to: FAILURE-004
- from: CHAPTER-033
  type: references
  to: FAILURE-005
```

### Valid Relationship Verbs

The registered relationships use only `illustrates` and `references`, valid PEAK relationship types in
`editor/KNOWLEDGE_MODEL.md` and the existing chapter graph.

### No-New-Concept Result

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, vocabulary concept, ID,
relationship verb, or primary-concept field is required.

## 22. Required Reader-Facing Chapter Architecture

The future manuscript must preserve the standard architecture:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Do not modify `editor/CHAPTER_ARCHITECTURE.md`.

## 23. Principal's Notebook Shape

The future manuscript must include exactly three short observations, no explanations.

Semantic targets:

- Hidden coupling makes local changes non-local.
- If behavior must change together, the relationship needs a name.
- The first fix is visibility.

Possible house-style lines:

- Silent coupling makes local changes non-local.
- Shared behavior needs a named relationship.
- The first fix is visibility.

## 24. Technical Credibility Requirements

The future manuscript must treat accurately:

- coupling that exists through behavior rather than static calls;
- firmware, backend, service-tool, manufacturing, support, release, and field workflows;
- diagnostic strings, events, named values, data shapes, file formats, timing windows, retries, and upgrade order as possible
  interfaces;
- tests as evidence but not a complete dependent list;
- logs as evidence only when producer, consumer, timing, and meaning are understood;
- service-tool and support behavior as part of product architecture;
- senior memory as useful but insufficient;
- active coupling versus folklore;
- turning discovered coupling into explicit contracts, tests, owners, records, review paths, or later removal decisions.

## 25. Terminology and Precision Guardrails

Use terms precisely:

- `silent coupling`: existing PEAK smell and vocabulary term for hidden behavioral dependency.
- `hidden dependency`: prose term for a dependency that affects behavior but is not represented where reviewers would
  expect.
- `explicit contract`: prose term for an API, schema, event definition, test, artifact, or owner-visible record that
  makes the relation discoverable.
- `coupling map`: chapter-local prose for a compact trace of behavior, dependents, owners, evidence, records, and next
  decision.
- `contract probe`: chapter-local prose for a small test, runtime observation, or record comparison that proves whether
  a suspected coupling is active.

Avoid implying:

- all coupling is bad;
- every hidden dependency must be removed immediately;
- import graphs reveal the true dependency graph;
- tests alone reveal all dependents;
- support procedures and service tools are outside architecture;
- static analysis is enough;
- every surprising dependency proves incompetence;
- documentation by itself fixes coupling;
- Chapter 33 owns utility gravity, Boolean Explosion, deletion, or trust-preserving refactoring.

## 26. Failure Modes to Avoid

Avoid these draft failures:

- writing a broad dependency-management or refactoring chapter;
- teaching Chapter 34, 35, 36, or 37 early;
- treating silent coupling as only code-level coupling;
- over-indexing on microservices examples and losing the embedded/product context;
- using a story where the local change immediately breaks local tests instead of hidden dependents;
- making the solution "write docs" instead of assigning contracts, owners, evidence, review paths, or next decisions;
- blaming previous engineers;
- creating a new coupling artifact, metric, ritual, vocabulary term, smell, anti-pattern, failure story, or PEAK ID;
- over-connecting the graph to later Part VI concepts that only appear as previews.

## 27. Author Draft Acceptance Criteria

The Author Draft should pass when:

- it creates `book/06-legacy/33-finding-silent-coupling.md`;
- it preserves the required reader-facing chapter architecture;
- it keeps `CHAPTER-033` as `draft` in `knowledge/index.yaml`;
- it preserves the exact registered Chapter 33 relationship set;
- it keeps no-primary resolution and creates no new PEAK concept;
- it illustrates `SMELL-001` and materially uses `VOCAB-008`;
- it teaches finding hidden behavioral dependency across code, tools, tests, data, time, releases, support, and people;
- it uses the recommended story or an equivalent credible system-and-device integration story;
- it ends with coupling made explicit and owned, not a full refactor;
- it includes exactly three Principal's Notebook observations;
- it does not create the later Part VI chapters early;
- it does not modify Chapters 1-32, Part VI README, table of contents, `editor/CHAPTER_ARCHITECTURE.md`,
  `editor/CANON.md`, or PEAK concept files.

## 28. Review Handoff Notes

For the Author Draft:

- write the manuscript only after this canonical brief is committed and pushed;
- keep the story centered on a working legacy system where the change broke nothing locally but exposed a hidden
  dependent elsewhere;
- make the Principal Engineer's move a shift from static dependency search to behavior-dependency discovery;
- use coupling map and contract probe as chapter-local prose only;
- ensure selected PEAK concepts are materially present if the registered relationship set is kept;
- keep Chapter 34 Utility Gravity, Chapter 35 Boolean Explosion, Chapter 36 Deleting Safely, and Chapter 37 Refactoring
  Without Losing Product Trust as future boundaries;
- do not open a pull request or begin review gates during the Author Draft prompt.
