# CHAPTER-032 Canonical Brief: Reading a Legacy System

## 1. Metadata

- Stable ID: `CHAPTER-032`.
- Title: `Reading a Legacy System`.
- Part: Part VI - Legacy.
- Chapter number: 32.
- Expected manuscript path: `book/06-legacy/32-reading-a-legacy-system.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-032-reading-a-legacy-system.md`.
- Branch: `chapter32`.
- Verified baseline `origin/main`: `489dc94e5c25c8e7b45b36a60b127cc67202fcc6`.
- Baseline evidence: PR #33 Chapter 31 squash merge commit,
  `Chapter 31: Architecture Health Reviews (#33)`.
- Chapter 31 feature Freeze commit checked for tree equivalence:
  `a0f1fb1`.
- Canonical predecessor: `CHAPTER-031` - Architecture Health Reviews.
- Part position: first chapter of Part VI - Legacy.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 32 applies existing laws, records, smells, metrics, and failure stories to the act of
  reading an existing system before change; it must not add a `primary_concept` registry field.
- Central chapter-local practice: building a reading map before the first change.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `489dc94e5c25c8e7b45b36a60b127cc67202fcc6`.
- That baseline is the PR #33 Chapter 31 squash merge commit,
  `Chapter 31: Architecture Health Reviews (#33)`.
- The squash commit has parent `8325145fc07aa9256d0af40819485815ceaa251d` and is an ancestor of current
  `origin/main`.
- The Chapter 31 feature-branch Freeze commit `a0f1fb1` remains tree-equivalent for the checked Chapter 31 lifecycle
  files in the squash commit.
- `CHAPTER-001` through `CHAPTER-031` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-031` is the final Part V chapter and is canonical.
- The table of contents places `Reading a Legacy System` first in Part VI - Legacy.
- The remaining Part VI sequence is `Finding Silent Coupling`, `Managing Utility Gravity`, `Reducing Boolean
  Explosion`, `Deleting Safely`, and `Refactoring Without Losing Product Trust`.
- `book/06-legacy/README.md` remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-032` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 32 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter32` existed before the working branch was created.
- No tracked `site/` output existed before this registration.
- The PEAK graph already contains laws, records, metrics, smells, anti-patterns, and failure stories needed for legacy
  reading; no new Legacy System, Reading Map, Safe Probe, Legacy Promise, Characterization, or Code Archaeology concept
  is required.

## 3. Part VI Role

Chapter 32 opens Part VI by moving from architecture that is actively governed to architecture that must first be
understood. Chapter 31 ended Part V by showing how organizations review whether architecture still supports necessary
change. Chapter 32 starts the legacy arc by teaching the entry practice: read the system as a living set of promises,
owners, states, dependencies, records, evidence, and risks before editing it.

The chapter should not blame prior engineers or treat age as failure. A legacy system may work in production precisely
because it protects promises that current readers have not named yet. The Principal Engineer's first act is not to
judge the code shape. It is to discover what the system already keeps true, who depends on it, where the real change
radius lies, and what small probe can reduce uncertainty without breaking hidden obligations.

## 4. Canonical Purpose

Prepare Chapter 32 to teach that reading a legacy system is an architectural act, not passive browsing or defect
hunting. The future manuscript should show how a Principal Engineer enters an existing system by discovering product
promises, state ownership, hidden state, API and protocol promises, dependencies, time assumptions, evidence, stale
records, and likely Change Radius before choosing a first change.

Candidate thesis for the future manuscript:

> Read a legacy system to discover the promises it already keeps, the ownership it hides, and the change paths it can
> safely tolerate.

The chapter should move the reader away from asking:

> Where should we start fixing this?

to asking:

> What must be true about this system before I can make a responsible change?

## 5. Primary-Concept Resolution

Chapter 32 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. The PEAK graph already
contains the concepts needed to carry this chapter: ownership, API promises, timing, evidence, dependencies, Change
Radius, Discoverability, API Stability, ADRs, Decision Journal entries, Mistake Ledger entries, Event Catalog entries,
Architecture Ledger entries, Architecture Health Review, Silent Coupling, Hidden State, Platform Leakage, Global
Configuration, Temporary Solution, and relevant failure stories.

Reading a legacy system, legacy reading, reading map, safe probe, characterization test, legacy promise, code
archaeology, unknown ownership, stale diagram, legacy boundary, and product promise map remain chapter-local prose. Do
not create a new PEAK law, artifact, ritual, metric, smell, anti-pattern, failure story, vocabulary term, relationship
verb, ID, or primary-concept field for them.

## 6. Central Thesis

Legacy reading is disciplined architectural discovery before change. It starts from product behavior and change risk,
then traces owners, states, boundaries, dependencies, time assumptions, evidence, records, and hidden promises until the
team can choose the smallest safe probe, question, test, or record update.

Approved supporting formulation for the future draft:

> Legacy code is often protecting something the organization stopped naming.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, artifact, ritual,
metric, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. reading legacy code means scanning files until the structure feels familiar;
2. old code is mostly a pile of defects waiting to be corrected;
3. obsolete diagrams and sparse documentation are useless;
4. senior memory is enough if the right expert is available;
5. tests reveal the full truth of the system;
6. unused-looking fallbacks are safe cleanup candidates;
7. names in code can be trusted more than observed behavior;
8. the easiest function to edit is the best place to start;
9. the responsible move is to understand everything before changing anything;
10. complexity proves prior incompetence.

By the end of the chapter, the reader should be able to:

1. read an existing subsystem by starting with product promises and change risk;
2. compare docs, code, runtime evidence, tests, logs, support notes, release records, and human memory;
3. identify state owners, hidden state, API promises, dependencies, and time assumptions;
4. distinguish real system promises from misleading names, stale diagrams, and folklore;
5. estimate likely Change Radius before editing;
6. find stale or missing ADRs, Decision Journal entries, Mistake Ledger entries, Event Catalog entries, and Architecture
   Ledger rows;
7. choose a small safe probe or characterization test that reduces uncertainty;
8. record discovered assumptions without creating a new canonical artifact or bureaucracy.

## 8. Legacy Reading Scope

For Chapter 32, legacy reading means a deliberate pass through a working system to form a change-safe model. It does
not require complete understanding. It requires enough understanding to decide the next safe probe, question, test,
record update, or change.

The future manuscript may examine:

- current product promises;
- real users, support workflows, field procedures, service tools, manufacturing, release, and operational context;
- state owners and hidden state;
- API, protocol, diagnostic, and compatibility promises;
- implicit dependencies across firmware, backend, service tooling, support, release, and field work;
- time, ordering, timeout, retry, and upgrade assumptions;
- configuration flags and variant behavior;
- release and upgrade constraints;
- failure and recovery paths;
- observability, logs, diagnostics, and evidence gaps;
- tests as evidence rather than full truth;
- stale diagrams, old ADRs, missing Decision Journal entries, and misleading records;
- change hot spots and likely Change Radius;
- undocumented rituals, scripts, and human workflows;
- senior memory as useful evidence that still needs records.

## 9. Reading Order and Evidence

The future manuscript should teach a reading order that starts from promises and risk, not from file hierarchy alone.

Useful reading layers:

1. What does the system promise externally?
2. Who or what depends on those promises?
3. What state exists, where is it stored, and who owns it?
4. Which boundaries, APIs, protocols, diagnostic strings, or service-tool screens carry meaning?
5. What dependencies import failure modes, lifecycle constraints, or ownership obligations?
6. What time, ordering, timeout, retry, release, or upgrade assumptions exist?
7. What evidence exists in tests, logs, metrics, events, incidents, release records, support notes, and field behavior?
8. Which decision records are absent, stale, or misleading?
9. What change is requested, and what is its likely Change Radius?
10. What small observation, characterization test, runtime probe, support-note check, or record repair would reduce
    uncertainty before editing?

Do not turn this into a rigid checklist. The reading order should transform the reader's attention from code shape to
system responsibility.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 32 covers:

- reading a legacy system as architecture discovery before change;
- product promises, hidden promises, state owners, hidden state, API promises, dependencies, and time assumptions;
- stale diagrams, misleading names, sparse documentation, old ADRs, missing records, and senior memory;
- evidence from source code, tests, logs, runtime behavior, support notes, release records, service tooling, incidents,
  manufacturing scripts, and field procedures;
- compatibility behavior, fallbacks, timeouts, configuration flags, diagnostic strings, backend APIs, and release
  support promises;
- estimating likely Change Radius for the requested change;
- choosing the smallest safe probe or characterization test;
- updating existing records such as ADRs, Decision Journal entries, Mistake Ledger entries, Event Catalog entries, or
  Architecture Ledger rows;
- non-blame treatment of systems and prior decisions.

### Explicitly Out of Scope

Do not turn Chapter 32 into:

- a generic refactoring chapter;
- a modernization roadmap;
- a rewrite argument;
- a code archaeology checklist;
- a static-analysis guide;
- a code-reading tutorial detached from product risk;
- a tool or vendor walkthrough;
- a legacy-blaming essay;
- a safe-deletion chapter;
- a utility-gravity chapter;
- a Boolean Explosion chapter;
- a silent-coupling chapter that teaches Chapter 33 early;
- a full documentation-before-change process;
- a new PEAK concept proposal.

## 11. Recommended Legacy-System Story

Use a story close to:

`The System That Everyone Knew Differently`

The system is a legacy service-and-device integration that works in production. It has years of patches, sparse docs,
old ADRs, scripts nobody wants to touch, a service tool, device firmware assumptions, backend APIs, field support
procedures, release notes, and a release path people do not fully trust.

A seemingly small change request arrives:

- add one compatibility behavior;
- adjust a timeout;
- remove an old fallback;
- simplify a configuration flag;
- support a new hardware revision or customer variant.

Symptoms:

- every team describes the system differently;
- the architecture diagram is obsolete;
- code names hide product meaning;
- a fallback nobody owns still protects a field behavior;
- a backend API treats a firmware quirk as a promise;
- a service tool depends on a diagnostic string;
- tests cover the happy path but not the legacy path;
- release notes imply support for versions nobody can reproduce;
- logs exist but do not explain the failure;
- a senior engineer remembers why a strange rule exists, but the record does not;
- the first proposed cleanup would break a hidden customer workflow.

The initial question is:

> Where should we start fixing this?

The Principal Engineer frames it again:

> Before we fix it, what must we read so we know what the system is already protecting?

The intervention should map product promises first, identify state owners and hidden state, trace boundaries and
dependencies, compare docs, code, runtime evidence, support notes, tests, and release records, name the requested
change and likely Change Radius, choose the smallest safe probe, repair records where needed, and defer refactoring
until the first safe model exists.

The story should end with a better first change, not a full modernization plan.

## 12. Expected Discussion Arc

The future manuscript should move through this arc:

1. Define legacy reading as disciplined architectural discovery before change.
2. Show why a working legacy system may protect promises that current engineers have stopped naming.
3. Explain why reading starts with product behavior, users, support obligations, and requested change risk.
4. Trace state ownership, hidden state, API promises, dependencies, and time assumptions.
5. Compare evidence sources: code, tests, logs, runtime behavior, support notes, release records, field reports, and
   senior memory.
6. Show how stale or missing records create Discoverability and Bus Factor risk.
7. Estimate likely Change Radius before editing.
8. Choose a small safe probe, characterization test, or record repair.
9. Record discovered assumptions in existing artifacts.
10. Hand off to later Part VI chapters by naming the legacy forces reading may reveal without teaching them early.

## 13. Boundaries With Later Part VI Chapters

Chapter 32 opens the legacy arc. It must preserve the later Part VI chapters:

- Chapter 33 owns finding Silent Coupling.
- Chapter 34 owns Utility Gravity.
- Chapter 35 owns Boolean Explosion.
- Chapter 36 owns Deleting Safely.
- Chapter 37 owns Refactoring Without Losing Product Trust.

Chapter 32 may say that reading can reveal silent coupling, utility gravity, Boolean Explosion, deletion candidates, and
refactoring paths. It must not teach how to find silent coupling systematically, manage utility gravity, reduce Boolean
Explosion, delete safely, or refactor while preserving product trust. Its job is the entry practice before those forces
are named and acted on.

## 14. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating them:

- Part I supplies Principal Engineer judgment, better questions, ownership beyond code, technical evidence, and
  stewardship.
- Part II supplies laws used as reading lenses: state ownership, API promises, dependencies, time assumptions,
  simplicity pressure, unused flexibility, and evidence.
- Part III supplies boundaries, Change Radius, failure and recovery, ADRs, RFCs, Architecture Review, Architecture
  Freeze, and decision records as ways to interpret what hardened.
- Part IV supplies product obligations: manufacturing, field reality, configuration, variants, observability, release
  discipline, upgrade paths, and support promises.
- Part V supplies leadership, review memory, rituals, mentoring through artifacts, alignment, and architecture health
  as ways legacy knowledge is shared or lost.

Chapter 32 should apply these tools as reading lenses. It must not summarize or re-teach their primary lessons.

## 15. Applicability

Chapter 32 is useful when:

- a working system is confusing but must be changed;
- docs, diagrams, code names, and team memory disagree;
- a seemingly small change touches compatibility, release, support, service tooling, manufacturing, or field behavior;
- an old fallback, timeout, configuration flag, diagnostic string, or service-tool path appears unused but may protect a
  customer workflow;
- tests cover happy paths while legacy behavior lives in release notes, support records, logs, or memory;
- a team wants to refactor before it understands the product promise;
- the likely Change Radius is unclear;
- the organization depends on one senior engineer to explain legacy behavior.

Not every edit needs a full reading map. Use the practice when the change crosses ownership boundaries, the system has
long-lived promises, or the cost of misunderstanding is high.

## 16. Limits and Exceptions

Legacy reading should be proportionate.

- During an active incident, stabilize the incident first and use reading to support diagnosis.
- For a truly local low-risk change with strong tests and clear ownership, a lightweight read may be enough.
- When a record is plainly stale and the correct owner is clear, update the record directly.
- When evidence is thin, do not pretend the reading map creates certainty; choose a safe probe.
- When a change is urgent, name the accepted risk, owner, evidence, and revisit trigger rather than blocking forever.
- When senior memory is available, use it as evidence and then repair the record it points to.

The chapter should avoid both extremes: editing blindly and demanding total understanding before any change.

## 17. Violation Patterns

The future manuscript should warn against these patterns:

- treating legacy code as bad because it is old;
- blaming previous engineers for constraints that may have protected real promises;
- starting from the easiest function to edit instead of the riskiest promise to understand;
- trusting file names, comments, diagrams, or senior memory without checking behavior;
- assuming unused-looking code is safe to remove;
- using tests as the only evidence;
- using static analysis as a substitute for product understanding;
- turning reading into a checklist detached from risk;
- documenting everything before choosing the next safe probe;
- rewriting mentally before understanding;
- creating a new permanent artifact when an existing record should be repaired.

## 18. Engineering Principle Target

Target meaning:

> Read legacy code as a system of promises before you read it as a pile of defects. Start with behavior, owners, state,
> boundaries, dependencies, evidence, and Change Radius; then choose the smallest safe probe that can improve your
> model.

Potential questions:

1. What product promise does this code protect?
2. Who depends on this behavior?
3. What state exists here, and who owns it?
4. Which name is lying or obsolete?
5. Which API, diagnostic string, timeout, or fallback has become a promise?
6. Which dependency imports failure modes?
7. Which behavior is only documented in tests, logs, support notes, release records, or memory?
8. What evidence contradicts the diagram?
9. What change is requested, and what is its likely Change Radius?
10. What safe probe would reduce uncertainty?
11. What record should be created or repaired before editing?

The final manuscript may shorten this list for rhythm. It must not become an oversized checklist.

## 19. Architecture Exercise Target

Use:

`Build a Reading Map Before the First Change`

Ask the reader to choose one legacy subsystem and document:

- requested change;
- visible product promise;
- suspected hidden promise;
- state owner;
- boundary or API involved;
- dependency involved;
- time or ordering assumption;
- evidence sources;
- evidence gaps;
- stale or missing records;
- likely Change Radius;
- smallest safe probe;
- record to update;
- risk if they edit first.

End with:

1. one promise the subsystem keeps;
2. one hidden assumption to verify;
3. one evidence source;
4. one safe probe;
5. one record to update.

Do not create a new canonical artifact.

## 20. Chapter-Local ADR Brief

Use a decision close to:

`Map Legacy Compatibility Behavior Before Removing the Fallback`

Context:

- a small cleanup or compatibility change touches a legacy fallback;
- docs are stale;
- tests cover only the happy path;
- service tooling, backend API behavior, release notes, and field support may depend on the fallback;
- no current record explains why the fallback exists.

Decision:

- do not remove or rewrite the fallback yet;
- create a reading map for the affected subsystem;
- identify product promise, state owner, boundary behavior, dependencies, test evidence, runtime evidence, release
  notes, and support assumptions;
- add a small safe probe or characterization test;
- update the Decision Journal or Architecture Ledger with discovered assumptions;
- revisit removal only after the real promise and Change Radius of the fallback are known.

Alternatives:

- remove the fallback because it looks unused;
- rewrite the subsystem first;
- trust the obsolete diagram;
- ask the senior engineer and rely on memory;
- add more logs but skip reading records;
- defer the change indefinitely.

Consequences should include slower first edit, reduced breakage risk, better shared understanding, a reusable reading
map, and a clearer path into Chapters 33-37. The ADR must not reduce to "document before changing."

## 21. PEAK Concept Map

### Concepts Inspected

- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `VOCAB-008` - Silent Coupling.
- `VOCAB-009` - Utility Gravity.
- `VOCAB-010` - Boolean Explosion.
- `VOCAB-007` - Architecture Health.
- `METRIC-001` - Change Radius.
- `METRIC-002` - Bus Factor.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `METRIC-005` - Architecture Health.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.
- `RITUAL-004` - Architecture Health Review.
- `SMELL-001` - Silent Coupling.
- `SMELL-002` - Utility Gravity.
- `SMELL-003` - Boolean Explosion.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-002` - HAL Everywhere.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-005` - Callback Hell.
- `ANTIPATTERN-006` - Temporary Solution.
- `FAILURE-001` - Logger That Became a Platform.
- `FAILURE-002` - One Lost Packet.
- `FAILURE-003` - The Successful Prototype.
- `FAILURE-004` - The Hero Engineer.
- `FAILURE-005` - The Release We Should Have Delayed.

### Selected Concepts

- `LAW-001` - Every State Has One Owner: material because legacy reading must discover state, storage, writers,
  interpreters, and ownership before changing behavior.
- `LAW-002` - Every API Is a Promise: material because backend APIs, protocols, diagnostic strings, service-tool
  screens, and compatibility behavior may carry promises beyond signatures.
- `LAW-003` - Time Is a Dependency: material because timeouts, retry windows, ordering, upgrade paths, and service-tool
  expectations are part of the legacy system's real contract.
- `LAW-005` - Evidence Before Confidence: material because the chapter compares code, docs, tests, logs, runtime
  behavior, support notes, release records, incidents, and memory before acting.
- `LAW-007` - Every Dependency Is a Decision: material because dependencies include libraries, firmware quirks,
  backend behavior, scripts, tools, procedures, release paths, and people.
- `VOCAB-001` - Change Radius: material vocabulary for the affected surface of the requested change.
- `METRIC-001` - Change Radius: material because the reading map estimates affected surfaces without false precision.
- `METRIC-002` - Bus Factor: material because senior memory may be the only source for why a fallback or upgrade path
  exists.
- `METRIC-003` - Discoverability: material because reading evaluates whether an engineer can find the owner, record,
  promise, and evidence behind behavior.
- `METRIC-004` - API Stability: material because legacy APIs may preserve behavior, errors, timing, and meaning that
  dependents trust.
- `ARTIFACT-001` - ADR: material because old ADRs may explain, mislead, or need update when a legacy promise is found.
- `ARTIFACT-003` - Decision Journal: material because discovered assumptions and small follow-up decisions may be too
  small for a full ADR.
- `ARTIFACT-004` - Mistake Ledger: material because escaped defects, delayed releases, and repeated failures can reveal
  legacy assumptions.
- `ARTIFACT-005` - Event Catalog: material because logs, events, diagnostic strings, and support language may disagree.
- `ARTIFACT-006` - Architecture Ledger: material because active legacy decisions, owners, debts, and review dates need
  a compact discoverable home.
- `RITUAL-004` - Architecture Health Review: material as the predecessor handoff; a health review may expose a legacy
  area that Chapter 32 then teaches the reader to read before changing.
- `SMELL-001` - Silent Coupling: material as something legacy reading may reveal, while Chapter 33 owns the systematic
  practice of finding and fixing it.
- `SMELL-004` - Hidden State: material because hidden state is a central reading target.
- `SMELL-005` - Platform Leakage: material because legacy product behavior may depend on platform details that escaped
  their boundary.
- `ANTIPATTERN-003` - Global Configuration: material because broad flags and configuration can hide product variants,
  state, and ownership.
- `ANTIPATTERN-006` - Temporary Solution: material because fallbacks and compatibility paths often outlive their owner,
  evidence, and expiry condition.
- `FAILURE-002` - One Lost Packet: material because protocol, retry, timing, and diagnostic evidence can be legacy
  promises.
- `FAILURE-004` - The Hero Engineer: material because relying on one senior engineer's memory is a legacy-reading risk.
- `FAILURE-005` - The Release We Should Have Delayed: material because release and upgrade promises are a key evidence
  source before changing legacy behavior.

### Rejected Concepts

- `LAW-004` - Simplicity Is a Feature: relevant background, but Chapter 32 should not judge shape before discovering
  promises.
- `LAW-006` - Unused Flexibility Is Waste: nearby to unused-looking fallbacks, but Chapter 32 stops before deletion or
  cleanup decisions.
- `VOCAB-008` - Silent Coupling: the chapter may preview silent coupling, but Chapter 33 owns the vocabulary-centered
  legacy chapter.
- `VOCAB-009` and `SMELL-002` - Utility Gravity: Chapter 34 owns utility gravity.
- `VOCAB-010` and `SMELL-003` - Boolean Explosion: Chapter 35 owns Boolean Explosion.
- `VOCAB-007` and `METRIC-005` - Architecture Health: Chapter 31 owns health review framing; Chapter 32 only uses the
  handoff from `RITUAL-004`.
- `ARTIFACT-002` - RFC: old proposals may be evidence, but the story-local record work is better carried by ADR,
  Decision Journal, Mistake Ledger, Event Catalog, and Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register: possible input from Chapter 31, but Chapter 32 should focus on reading and
  safe probes rather than weak-signal intake.
- `RITUAL-001` - Architecture Review: a later output if a promise needs review, but not material to the entry practice.
- `RITUAL-002` - Architecture Freeze: possible later release output, but not part of legacy reading itself.
- `ANTIPATTERN-002` - HAL Everywhere: possible implementation detail, but platform leakage is the stronger selected
  concept.
- `ANTIPATTERN-005` - Callback Hell: possible ordering detail, but `LAW-003`, `SMELL-006`, and Event Catalog evidence
  cover the material reading need without making this a callback chapter.
- `SMELL-006` - Event Explosion: relevant to noisy diagnostics, but the chapter should use Event Catalog as evidence
  without teaching event-model cleanup.
- `FAILURE-001` - Logger That Became a Platform: reserved for utility gravity and accidental-platform discussions.
- `FAILURE-003` - The Successful Prototype: background for how legacy forms, but Chapter 20 owns prototype-to-product.

### Exact Outgoing Relationships

```yaml
- from: CHAPTER-032
  type: references
  to: LAW-001
- from: CHAPTER-032
  type: references
  to: LAW-002
- from: CHAPTER-032
  type: references
  to: LAW-003
- from: CHAPTER-032
  type: references
  to: LAW-005
- from: CHAPTER-032
  type: references
  to: LAW-007
- from: CHAPTER-032
  type: references
  to: VOCAB-001
- from: CHAPTER-032
  type: references
  to: METRIC-001
- from: CHAPTER-032
  type: references
  to: METRIC-002
- from: CHAPTER-032
  type: references
  to: METRIC-003
- from: CHAPTER-032
  type: references
  to: METRIC-004
- from: CHAPTER-032
  type: references
  to: ARTIFACT-001
- from: CHAPTER-032
  type: references
  to: ARTIFACT-003
- from: CHAPTER-032
  type: references
  to: ARTIFACT-004
- from: CHAPTER-032
  type: references
  to: ARTIFACT-005
- from: CHAPTER-032
  type: references
  to: ARTIFACT-006
- from: CHAPTER-032
  type: references
  to: RITUAL-004
- from: CHAPTER-032
  type: references
  to: SMELL-001
- from: CHAPTER-032
  type: references
  to: SMELL-004
- from: CHAPTER-032
  type: references
  to: SMELL-005
- from: CHAPTER-032
  type: references
  to: ANTIPATTERN-003
- from: CHAPTER-032
  type: references
  to: ANTIPATTERN-006
- from: CHAPTER-032
  type: references
  to: FAILURE-002
- from: CHAPTER-032
  type: references
  to: FAILURE-004
- from: CHAPTER-032
  type: references
  to: FAILURE-005
```

### Valid Relationship Verbs

The registered relationships use only `references`, a valid PEAK relationship type in `editor/KNOWLEDGE_MODEL.md` and
the existing chapter graph. `illustrates` is intentionally avoided because Chapter 32 does not introduce or centrally
illustrate one existing PEAK ritual, artifact, smell, or failure story.

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

- Legacy code is often protecting something nobody named.
- The first job is not to judge the shape; it is to discover the promise.
- A safe change starts with a better reading of reality.

Possible house-style lines:

- Legacy code often protects an unnamed promise.
- Read the promise before judging the shape.
- A safe change starts with a better reading.

## 24. Technical Credibility Requirements

The future manuscript must treat accurately:

- legacy systems that work in production despite confusing code;
- obsolete diagrams and partial documentation;
- code names that no longer match product meaning;
- fallbacks, compatibility behavior, timeouts, configuration flags, service-tool assumptions, backend APIs, release
  notes, and field support procedures;
- tests as evidence but not full truth;
- logs and diagnostics as evidence only when their meaning is understood;
- runtime behavior versus source-level intent;
- senior engineer memory as useful but insufficient;
- small safe probes, characterization tests, and reading maps;
- risk of breaking hidden customer workflows;
- incremental knowledge-building before refactoring.

## 25. Terminology and Precision Guardrails

Use terms precisely:

- `legacy system`: prose term for an existing system whose behavior, records, owners, and promises must be understood
  before safe change; do not register it as PEAK.
- `reading map`: chapter-local prose for the compact map of promises, owners, evidence, gaps, Change Radius, and safe
  probe.
- `safe probe`: chapter-local prose for a small observation, test, runtime check, support-record comparison, or record
  repair that reduces uncertainty before editing.
- `characterization test`: allowed as local engineering language when used as one possible safe probe, not a new
  canonical artifact.
- `legacy promise`: chapter-local prose for an existing behavior that dependents trust even if no record names it.

Avoid implying:

- legacy code is bad because it is old;
- rewrite is the default answer;
- all unknown code must be documented before any change;
- full understanding is required before every edit;
- tests alone reveal the truth;
- diagrams are useless;
- senior memory should be ignored;
- static analysis is enough;
- code reading is separate from product behavior;
- reading maps must become permanent bureaucracy;
- every odd behavior is accidental.

## 26. Failure Modes to Avoid

Avoid these draft failures:

- writing a refactoring, deletion, modernization, static-analysis, or rewrite chapter;
- teaching Chapter 33, 34, 35, 36, or 37 early;
- creating a new legacy artifact, metric, ritual, smell, anti-pattern, vocabulary term, or failure story;
- blaming prior engineers or treating complexity as incompetence;
- turning the reading order into a rigid checklist;
- making the story end with a full modernization plan instead of a better first change;
- confusing reading with documentation theater;
- reducing safe probes to "add logs";
- treating obsolete docs as useless instead of evidence to compare;
- over-connecting the graph to later Part VI concepts that only appear as previews.

## 27. Author Draft Acceptance Criteria

The Author Draft should pass when:

- it creates `book/06-legacy/32-reading-a-legacy-system.md`;
- it preserves the required reader-facing chapter architecture;
- it keeps `CHAPTER-032` as `draft` in `knowledge/index.yaml`;
- it preserves the exact registered Chapter 32 relationship set;
- it keeps no-primary resolution and creates no new PEAK concept;
- it teaches legacy reading as architectural discovery before change;
- it starts from product promises and change risk, not file hierarchy alone;
- it includes state owners, hidden state, API promises, dependencies, time assumptions, evidence, stale records, Change
  Radius, and safe probes;
- it uses the recommended legacy story or an equivalent credible system-and-device integration story;
- it ends the story with a better first change, not a modernization roadmap;
- it includes exactly three Principal's Notebook observations;
- it does not create the later Part VI chapters early;
- it does not modify Chapters 1-31, Part VI README, table of contents, `editor/CHAPTER_ARCHITECTURE.md`,
  `editor/CANON.md`, or PEAK concept files.

## 28. Review Handoff Notes

For the Author Draft:

- write the manuscript only after this canonical brief is committed and pushed;
- keep the story centered on a working legacy service-and-device integration;
- make the Principal Engineer's move a shift from fixing to reading what the system protects;
- use reading map and safe probe as chapter-local prose only;
- ensure selected PEAK concepts are materially present if the registered relationship set is kept;
- keep Chapter 33 Silent Coupling, Chapter 34 Utility Gravity, Chapter 35 Boolean Explosion, Chapter 36 Deleting Safely,
  and Chapter 37 Refactoring Without Losing Product Trust as future boundaries;
- do not open a pull request or begin review gates during the Author Draft prompt.
