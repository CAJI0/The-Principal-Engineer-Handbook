# CHAPTER-031 Canonical Brief: Architecture Health Reviews

## 1. Metadata

- Stable ID: `CHAPTER-031`.
- Title: `Architecture Health Reviews`.
- Part: Part V - Engineering Organization.
- Chapter number: 31.
- Expected manuscript path: `book/05-engineering-organization/31-architecture-health-reviews.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-031-architecture-health-reviews.md`.
- Branch: `chapter31`.
- Verified baseline `origin/main`: `8325145fc07aa9256d0af40819485815ceaa251d`.
- Baseline evidence: PR #32 Chapter 30 squash merge commit,
  `Chapter 30: Aligning Teams Around Decisions (#32)`.
- Chapter 30 feature Freeze commit checked for tree equivalence:
  `092dc17`.
- Canonical predecessor: `CHAPTER-030` - Aligning Teams Around Decisions.
- Part position: sixth and final chapter of Part V - Engineering Organization.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 31 uses the existing `RITUAL-004` Architecture Health Review concept and existing
  Architecture Health vocabulary and metric entries; it must not add a primary-concept registry field.
- Central illustrated concept: `RITUAL-004` - Architecture Health Review.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `8325145fc07aa9256d0af40819485815ceaa251d`.
- That baseline is the PR #32 Chapter 30 squash merge commit,
  `Chapter 30: Aligning Teams Around Decisions (#32)`.
- The squash commit has parent `73cc53d2afac40abcdd9ead33e9ea3885ec82163` and is an ancestor of current
  `origin/main`.
- The Chapter 30 feature-branch Freeze commit `092dc17` remains tree-equivalent for the checked Chapter 30 lifecycle
  files in the squash commit.
- `CHAPTER-001` through `CHAPTER-030` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-030` is the fifth Part V chapter and is canonical.
- The table of contents places `Architecture Health Reviews` sixth and last in Part V - Engineering Organization.
- After Chapter 31, the table of contents begins Part VI with `Reading a Legacy System`.
- `book/05-engineering-organization/README.md` remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-031` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 31 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter31` existed before the working branch was created.
- No tracked `site/` output existed before this registration.
- The PEAK graph already contains `RITUAL-004` Architecture Health Review, `VOCAB-007` Architecture Health, and
  `METRIC-005` Architecture Health, so no new health concept is required.

## 3. Part V Role

Chapter 31 closes Part V by turning the prior organizational capabilities into a repeated way of noticing whether the
architecture still supports necessary work. Chapter 26 taught leadership without authority. Chapter 27 taught design
reviews as shared memory. Chapter 28 taught engineering rituals. Chapter 29 taught mentoring through artifacts.
Chapter 30 taught decision alignment. Chapter 31 should show how those practices become an ongoing ability to detect
architectural decay, repair weak ownership, update stale records, and choose the next decision before the architecture
becomes harder to change than the product can tolerate.

The chapter should stay technical and organizational. It is not a metrics dashboard chapter, audit process, compliance
checkpoint, management ritual, performance review, maturity model, or architecture board playbook. It should teach how
a Principal Engineer helps the organization ask whether the architecture can still carry the changes, failures,
product obligations, records, and team boundaries it now depends on.

## 4. Canonical Purpose

Prepare Chapter 31 to teach that architecture health is not a score, taste judgment, or annual inspection. Architecture
health is the present ability of the system to absorb necessary change without losing ownership, promises, evidence,
recovery paths, or trust.

Candidate thesis for the future manuscript:

> Architecture health is the system's present ability to absorb necessary change without losing ownership, promises,
> evidence, recovery paths, or trust.

The chapter should move the reader away from asking:

> Are our architecture metrics green?

to asking:

> What evidence tells us whether the architecture can still carry the decisions, changes, failures, product
> obligations, and team boundaries we need it to carry?

## 5. Primary-Concept Resolution

Chapter 31 has no new primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. The graph already
contains `RITUAL-004` Architecture Health Review, `VOCAB-007` Architecture Health, and `METRIC-005` Architecture
Health. Chapter 31 should illustrate the existing ritual and reference existing health, evidence, ownership, records,
Change Radius, Bus Factor, Discoverability, weak signal, and product-obligation concepts.

Health signal, architecture health check, quarterly review, review cadence, health finding, architecture repair list,
fitness review, architecture scorecard, decay map, and health dashboard remain chapter-local or rejected prose. Do not
create a new PEAK concept, ID, artifact, ritual, metric, vocabulary term, smell, anti-pattern, failure story, primary
concept field, or relationship verb for them.

## 6. Central Thesis

Architecture health reviews help an organization notice when a system that appears to work today is becoming too
expensive, risky, or unclear to change tomorrow. They review evidence from changes, owners, promises, records, support,
releases, failures, reviews, and people, then turn that evidence into decisions, owners, artifact updates, and revisit
triggers.

Approved supporting formulation for the future draft:

> Working today is not the same as healthy enough for the next necessary change.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, artifact, ritual,
metric, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. architecture health means operational dashboards are green;
2. low incident count means the architecture is fine;
3. health reviews are audits or architecture board meetings;
4. architecture health can be reduced to one score;
5. health problems are code quality problems;
6. health reviews are a Principal Engineer's opinion poll;
7. every health finding means refactor immediately;
8. repeated review questions are meeting friction, not architecture evidence;
9. stale ADRs and open ledger items are documentation debt only;
10. the organization should wait until delivery visibly slows.

By the end of the chapter, the reader should be able to:

1. run one focused architecture health review for a subsystem or product boundary;
2. collect evidence from change difficulty, ownership drift, API promises, support, release, records, and people;
3. distinguish green operational metrics from architectural health;
4. connect health signals to decisions instead of scores;
5. decide what to keep, repair, retire, review, freeze, investigate, document, or accept as risk;
6. update ADRs, RFCs, Decision Journal entries, Mistake Ledger entries, Event Catalog entries, the Architecture Ledger,
   or the Weak Signal Register as appropriate;
7. assign owners and revisit triggers;
8. keep the review lightweight enough to repeat without turning it into status reporting.

## 8. Architecture Health Review Scope

For Chapter 31, an architecture health review is a repeated, evidence-based review of whether architecture still
supports necessary change.

The future manuscript may examine:

- ownership clarity for state, APIs, configuration, release-critical decisions, and recovery behavior;
- API promises, compatibility, and support language;
- Change Radius for small or routine changes;
- silent coupling, hidden state, platform leakage, and event growth;
- dependency health and replacement difficulty;
- support, release, field, manufacturing, variant, upgrade, and recovery obligations;
- observability, diagnosis paths, and support ambiguity;
- stale ADRs, orphaned RFCs, open Architecture Ledger items, and Decision Journal gaps;
- Bus Factor risk around critical behavior;
- recurring field failures and weak signals;
- architectural debt backed by evidence;
- obsolete decisions and temporary solutions past their expiry condition;
- places where teams route work around the architecture because they no longer trust a boundary.

The review should produce decisions, owners, follow-up, records, and revisit triggers. It should not produce only a
score, dashboard, list of complaints, or preference ranking.

## 9. Health Review Boundaries

The future manuscript must distinguish architecture health review from:

- Architecture Review, which reviews a consequential design before it hardens;
- Architecture Freeze, which stabilizes named decisions during validation;
- design review of one proposal;
- operational incident review;
- security review;
- performance review;
- code-quality dashboard review;
- sprint retrospective;
- maturity assessment;
- compliance audit;
- architecture board meeting;
- team health survey.

Architecture health review asks whether the architecture remains fit for upcoming and ongoing change. It is not a
verdict on a team's competence.

## 10. Evidence for Architecture Health

Architecture health evidence may include:

- repeated high Change Radius for changes that should be small;
- unclear owners for state, APIs, configuration, dependencies, or release-critical decisions;
- API promises that changed without records;
- support ambiguity or diagnostic language that no longer matches system events;
- recurring release, upgrade, recovery, or compatibility exceptions;
- obsolete ADRs, orphaned RFCs, or Decision Journal entries without follow-up;
- Architecture Ledger items that stay open across reviews;
- Event Catalog drift or Event Explosion;
- rising Bus Factor risk around provisioning, recovery, configuration, upgrade, or support behavior;
- temporary solutions without owner, expiry condition, or review trigger;
- product variants that require private knowledge;
- field failures that cannot be diagnosed from current records;
- teams delaying changes because nobody trusts a boundary;
- engineers copying patterns without knowing constraints;
- weak signals from design reviews, support, new-engineer learning, incidents, release validation, and field feedback.

The review should connect signals to decisions: keep, repair, retire, review, freeze, investigate, document, or accept
risk.

## 11. In-Scope and Out-of-Scope

### In Scope

Chapter 31 covers:

- recurring architecture health review as an organizational practice;
- evidence-based architecture assessment;
- architecture health as the ability to absorb necessary change at acceptable cost;
- Change Radius, ownership drift, API promise drift, dependency risk, support ambiguity, release pressure, and weak
  signals;
- stale or missing records as architecture health evidence;
- Bus Factor as social and technical risk;
- product obligations from manufacturing, field, configuration, observability, releases, upgrades, and support;
- follow-up decisions, owners, artifact updates, and revisit triggers;
- lightweight repeatability and a non-blame framing;
- Part V closure and a light handoff to Part VI.

### Explicitly Out of Scope

Do not turn Chapter 31 into:

- a metrics dashboard chapter;
- an architecture scorecard checklist;
- a maturity model;
- a governance-board playbook;
- a compliance audit;
- a performance-review chapter;
- a security review;
- an incident-retrospective chapter;
- a status-reporting ritual;
- a generic management process;
- a tooling guide;
- a refactoring program plan;
- a legacy-system reading chapter repeated early from Chapter 32;
- a new PEAK concept proposal.

## 12. Recommended Engineering-Organization Story

Use a story close to:

`The Architecture That Looked Fine Until Every Change Was Expensive`

The organization has shipped several releases. Incidents are low, features ship, dashboards are green, and the teams
know the system. Mara notices that small cross-team changes now require unusual coordination. A provisioning field has
no visible owner. Service-tool behavior depends on an undocumented API assumption. A temporary compatibility layer has
become permanent. Upgrade paths depend on one engineer's memory. Design reviews repeat the same rejected options.
Event Catalog names do not match support language. Architecture Ledger items stay open. Recovery logic has rising Bus
Factor risk. Teams avoid one boundary. New engineers copy an old pattern without knowing why.

Leadership asks whether the team is overreacting because the system is working. Mara changes the question:

> Working today is not the same as healthy enough for the next necessary change.

The intervention should show a focused architecture health review. The team collects evidence across Change Radius,
ownership, discoverability, support ambiguity, release exceptions, review memory, Bus Factor, and weak signals. The
review avoids blame and taste. It produces a few decisions to keep, repair, retire, review, freeze, investigate,
document, or accept as risk. Owners and revisit triggers are assigned. Relevant artifacts are updated. The review stays
small enough to repeat.

## 13. Expected Discussion Arc

The future manuscript should move through this arc:

1. Define architecture health as the ability to support necessary change, not as beauty, coverage, or dashboard color.
2. Show why visible stability can hide rising change cost, ownership drift, and private memory.
3. Explain what makes architecture health review different from design review, Architecture Review, Architecture Freeze,
   audit, retrospective, and dashboard review.
4. Teach how to collect proportionate evidence from changes, records, owners, support, releases, weak signals, and
   people.
5. Translate evidence into decisions and follow-up rather than a broad complaint list.
6. Show artifact updates as memory repair, not documentation theater.
7. Tie the practice back to Part V: leadership, review memory, rituals, mentoring artifacts, and team alignment.
8. Close by naming Part VI's legacy boundary without starting legacy-system analysis.

## 14. Part V Closure and Forward Boundary

Chapter 31 closes Part V by showing how organizational practices keep architecture memory alive after individual
decisions are made. Technical leadership without authority, design reviews as shared memory, engineering rituals,
mentoring through artifacts, and decision alignment all become inputs to a recurring review of whether the architecture
still supports necessary change.

The chapter may preview that unhealthy, poorly remembered architecture often becomes tomorrow's legacy system. It must
not teach Part VI. Do not explain how to read a legacy system, map legacy behavior, recover lost intent, replace
obsolete components, or lead legacy modernization. Chapter 32 owns the first Part VI move: `Reading a Legacy System`.

## 15. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating their lessons:

- Part I supplies Principal Engineer judgment, better questions, ownership beyond code, evidence, and stewardship.
- Part II supplies laws that become health questions: state ownership, API promises, dependencies, time assumptions,
  simplicity, flexibility, and evidence.
- Part III supplies ADRs, RFCs, Architecture Review, Architecture Freeze, and decision records as review inputs and
  outputs.
- Part IV supplies product obligations that expose health under manufacturing, field, configuration, observability,
  release, upgrade, recovery, and support pressure.
- Earlier Part V chapters supply leadership, review memory, ritual design, mentoring through artifacts, and alignment
  around decisions.

The future manuscript should not summarize those chapters, re-teach their tools, or change their canon.

## 16. Applicability

Architecture health reviews are appropriate when:

- several releases have accumulated enough evidence to inspect the architecture in use;
- small changes are becoming more expensive than their feature size suggests;
- ownership, promise, dependency, or record drift is appearing across teams;
- support, release, field, or new-engineer learning pressure points to unclear architecture memory;
- repeated review questions suggest that old decisions are no longer discoverable;
- a boundary is avoided because teams no longer trust it;
- temporary solutions are outliving their review triggers;
- leaders see green operational metrics while engineers experience high coordination cost.

The review should be scoped to a subsystem, boundary, product area, or release path when possible. A broad review of the
whole company architecture should be rare and must still produce concrete decisions.

## 17. Limits and Exceptions

Architecture health review is not the first response to every problem.

- During an active incident, run incident response first.
- During release validation, use Architecture Freeze and release discipline where named decisions need temporary
  stability.
- For one consequential design that has not hardened yet, use Architecture Review or design review.
- For a known stale ADR or orphaned RFC, update the record directly when no cross-boundary health question is present.
- For one team-local refactor, do not create an organization-wide ritual.
- When evidence is too thin, investigate a weak signal before convening a broad review.

The chapter should teach proportion: lightweight, repeated, evidence-based review when the system's ability to carry
future change is in question.

## 18. Violation Patterns

The future manuscript should warn against these patterns:

- reducing health to one score;
- treating green dashboards as proof of architecture health;
- blaming teams for architecture decay;
- using the review to reopen every old decision;
- turning the review into an architecture board status meeting;
- using review cadence as a substitute for evidence;
- recording findings without decisions, owners, or revisit triggers;
- declaring every finding a refactoring project;
- letting the Principal Engineer become the private health oracle;
- ignoring support, release, field, new-engineer learning, and review weak signals;
- updating artifacts without changing ownership, promises, or follow-up.

## 19. Engineering Principle Target

Target meaning:

> Review architecture health by asking what the system can still carry. Use evidence from change, ownership, promises,
> support, releases, records, and people to decide what to keep, repair, retire, review, freeze, investigate, document,
> or accept as risk.

Potential questions:

- What small change recently had large Change Radius?
- Which state or API promise lacks a visible owner?
- Which dependency is harder to replace or understand than expected?
- Which temporary solution outlived its trigger?
- Which release or support issue repeated?
- Which rejected option keeps returning?
- Which boundary do teams avoid?
- Which record is stale, missing, or misleading?
- Where is Bus Factor rising?
- Which weak signal deserves investigation?
- What decision must be made after the review?
- What will we revisit next?

The future manuscript should not turn these questions into a large checklist. The questions should support judgment.

## 20. Architecture Exercise Target

Use:

`Run One Architecture Health Check`

Ask the reader to choose one subsystem or product boundary and document:

- recent change that was harder than expected;
- affected owners;
- state ownership issue;
- API or compatibility promise;
- dependency concern;
- evidence from support, release, field, or reviews;
- stale or missing record;
- temporary solution or workaround;
- Bus Factor risk;
- weak signal;
- decision to make;
- follow-up owner;
- artifact to update;
- revisit trigger.

End with:

1. one health signal;
2. one decision;
3. one owner;
4. one artifact update;
5. one revisit trigger.

Do not create a new canonical artifact.

## 21. Chapter-Local ADR Brief

Use a decision close to:

`Establish a Quarterly Architecture Health Review for the Provisioning Boundary`

Context:

- the cross-team provisioning boundary appears stable, but changes are increasingly expensive;
- ownership, support language, release assumptions, and recovery knowledge have drifted;
- leadership lacks visible evidence because incidents are low and dashboards are green;
- repeated review questions, stale ledger items, and Bus Factor risk indicate hidden architecture health problems.

Decision:

- run a quarterly architecture health review focused on the provisioning boundary;
- use evidence from Change Radius, support cases, release exceptions, design reviews, Architecture Ledger, ADR/RFC age,
  Event Catalog drift, Bus Factor risk, and weak signals;
- produce explicit decisions: keep, repair, retire, review, freeze, investigate, document, or accept risk;
- assign follow-up owners and revisit triggers;
- update relevant artifacts;
- keep the review lightweight and non-blame;
- preview Part VI legacy reading only as future application, not current scope.

Alternatives:

- wait until incidents rise;
- rely on dashboard metrics;
- hold a broad architecture board meeting;
- start a refactoring program immediately;
- ask senior engineers for opinions;
- run a maturity-model assessment;
- do nothing because the system currently works.

Consequences should include earlier detection of architectural decay, better ownership, fewer repeated arguments,
clearer follow-up, risk of process overhead, and the need to retire or redesign the review if it stops producing
decisions.

## 22. PEAK Concept Map

### Concepts Inspected

- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.
- `RITUAL-004` - Architecture Health Review.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `VOCAB-002` - Weak Signal.
- `VOCAB-007` - Architecture Health.
- `METRIC-001` - Change Radius.
- `METRIC-002` - Bus Factor.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `METRIC-005` - Architecture Health.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-006` - Temporary Solution.
- `FAILURE-004` - The Hero Engineer.
- `FAILURE-005` - Release and Upgrade Failure.

### Selected Concepts

- `RITUAL-004` - Architecture Health Review: the central repeated practice illustrated by the chapter.
- `VOCAB-007` - Architecture Health: supplies the chapter's definition of health.
- `METRIC-005` - Architecture Health: supplies the evidence framing and warning against one-score reduction.
- `ARTIFACT-006` - Architecture Ledger: active memory for open items, health notes, stale decisions, and follow-up.
- `ARTIFACT-001` - ADR: records decisions kept, repaired, retired, or revisited after the review.
- `ARTIFACT-002` - RFC: supplies proposal memory and stale or orphaned review inputs.
- `ARTIFACT-003` - Decision Journal: captures follow-up decisions and revisit triggers.
- `ARTIFACT-004` - Mistake Ledger: captures repeated failures or patterns discovered by review.
- `ARTIFACT-005` - Event Catalog: reveals drift between system events and support language.
- `ARTIFACT-007` - Weak Signal Register: captures weak signals that need investigation before they harden.
- `RITUAL-001` - Architecture Review: boundary and input for designs before hardening.
- `RITUAL-002` - Architecture Freeze: possible follow-up when a named decision needs temporary stability.
- `LAW-001` - Every State Has One Owner: health question for ownership drift.
- `LAW-002` - Every API Is a Promise: health question for promise drift and compatibility.
- `LAW-005` - Evidence Before Confidence: governs review evidence.
- `LAW-006` - Unused Flexibility Is Waste: governs obsolete options and unnecessary flexibility.
- `LAW-007` - Every Dependency Is a Decision: health question for dependency drift.
- `VOCAB-001` - Change Radius: vocabulary for the cost of small changes.
- `METRIC-001` - Change Radius: measurement signal for architectural health.
- `METRIC-002` - Bus Factor: social and technical health signal for private memory.
- `METRIC-003` - Discoverability: health signal for records, owners, and constraints.
- `METRIC-004` - API Stability: health signal for promise drift.
- `VOCAB-002` - Weak Signal: language for early evidence.
- `SMELL-001` - Silent Coupling: architecture smell revealed by broad change cost.
- `SMELL-004` - Hidden State: architecture smell revealed by unclear ownership.
- `SMELL-005` - Platform Leakage: architecture smell revealed by boundary workarounds.
- `SMELL-006` - Event Explosion: architecture smell revealed by event catalog drift.
- `ANTIPATTERN-003` - Global Configuration: health risk when configuration ownership is unclear.
- `ANTIPATTERN-006` - Temporary Solution: health risk when workarounds lose expiry.
- `FAILURE-004` - The Hero Engineer: failure mode when one engineer holds recovery or upgrade memory.
- `FAILURE-005` - Release and Upgrade Failure: failure mode used for release and upgrade health evidence.

### Rejected Concepts

- `LAW-003` - Time Is a Dependency: relevant to timing assumptions, but release and upgrade health is covered through
  dependency, record, support, and `FAILURE-005` relationships.
- `ANTIPATTERN-004` - Manager Mania: not selected. The current graph names this ID as Manager Mania, not Hero Engineer,
  and Chapter 31 is not a management workaround chapter.
- `ANTIPATTERN-002` - HAL Everywhere: possible implementation smell, but not central to the health review story.
- `ANTIPATTERN-005` - Callback Hell: possible technical signal, but not needed for this chapter's organizing arc.
- `FAILURE-002` - One Lost Packet: nearby failure and recovery material, but Chapter 16 owns that failure story.
- `RITUAL-005` - Architecture Court: governance boundary only; Chapter 31 must avoid architecture-board framing.
- `RITUAL-006` - RFC Friday: possible forum, but Chapter 28 owns ritual design and Chapter 17 owns RFC mechanics.

### Exact Outgoing Relationships

```yaml
- from: CHAPTER-031
  type: illustrates
  to: RITUAL-004
- from: CHAPTER-031
  type: references
  to: VOCAB-007
- from: CHAPTER-031
  type: references
  to: METRIC-005
- from: CHAPTER-031
  type: references
  to: ARTIFACT-006
- from: CHAPTER-031
  type: references
  to: ARTIFACT-001
- from: CHAPTER-031
  type: references
  to: ARTIFACT-002
- from: CHAPTER-031
  type: references
  to: ARTIFACT-003
- from: CHAPTER-031
  type: references
  to: ARTIFACT-004
- from: CHAPTER-031
  type: references
  to: ARTIFACT-005
- from: CHAPTER-031
  type: references
  to: ARTIFACT-007
- from: CHAPTER-031
  type: references
  to: RITUAL-001
- from: CHAPTER-031
  type: references
  to: RITUAL-002
- from: CHAPTER-031
  type: references
  to: LAW-001
- from: CHAPTER-031
  type: references
  to: LAW-002
- from: CHAPTER-031
  type: references
  to: LAW-005
- from: CHAPTER-031
  type: references
  to: LAW-006
- from: CHAPTER-031
  type: references
  to: LAW-007
- from: CHAPTER-031
  type: references
  to: VOCAB-001
- from: CHAPTER-031
  type: references
  to: METRIC-001
- from: CHAPTER-031
  type: references
  to: METRIC-002
- from: CHAPTER-031
  type: references
  to: METRIC-003
- from: CHAPTER-031
  type: references
  to: METRIC-004
- from: CHAPTER-031
  type: references
  to: VOCAB-002
- from: CHAPTER-031
  type: references
  to: SMELL-001
- from: CHAPTER-031
  type: references
  to: SMELL-004
- from: CHAPTER-031
  type: references
  to: SMELL-005
- from: CHAPTER-031
  type: references
  to: SMELL-006
- from: CHAPTER-031
  type: references
  to: ANTIPATTERN-003
- from: CHAPTER-031
  type: references
  to: ANTIPATTERN-006
- from: CHAPTER-031
  type: references
  to: FAILURE-004
- from: CHAPTER-031
  type: references
  to: FAILURE-005
```

### No-New-Concept Result

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, vocabulary concept, ID,
relationship verb, or primary-concept field is required.

## 23. Required Reader-Facing Chapter Architecture

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

## 24. Principal's Notebook Shape

The future manuscript must include exactly three short observations, no explanations.

Semantic targets:

- Green dashboards can hide red architecture.
- Architecture health is measured by the next change.
- A health review that produces no decision is only a status report.

Possible house-style lines:

- Green dashboards can hide red architecture.
- Health shows up in the next change.
- No decision means no review happened.

## 25. Technical and Organizational Credibility Requirements

The future manuscript must treat accurately:

- recurring architecture health review as an organizational practice;
- differences among health review, design review, Architecture Review, Architecture Freeze, audit, retrospective,
  status meeting, and dashboard review;
- evidence-based architecture assessment;
- Change Radius as a health signal;
- ownership and API promise drift;
- release, support, field, upgrade, manufacturing, variant, diagnosis, and recovery pressure as health evidence;
- Architecture Ledger as active memory;
- stale ADRs and RFCs;
- repeated rejected options;
- Bus Factor as social and technical risk;
- weak signals from support, reviews, new-engineer learning, field failures, and release validation;
- follow-up decisions and owners;
- lightweight repeatability and non-blame framing;
- Part V closure and Part VI preview.

## 26. Terminology and Precision Guardrails

Use precise language:

- say `architecture health review` when referring to the repeated practice;
- say `Architecture Review` only for `RITUAL-001`, review before hardening;
- say `Architecture Freeze` only for `RITUAL-002`, temporary stability for named decisions;
- say `Architecture Health` when referring to the existing vocabulary or metric concept;
- describe evidence, signals, owners, records, and decisions before mentioning cadence;
- describe health as the ability to support necessary change, not as one number;
- use `FAILURE-004` for The Hero Engineer because `ANTIPATTERN-004` is Manager Mania in the current graph.

Avoid implying:

- architecture health is the Principal Engineer's private taste;
- dashboards replace review;
- every finding becomes refactoring;
- green operations prove healthy architecture;
- health review judges team competence;
- a quarterly meeting fixes architecture by existing.

## 27. Failure Modes to Avoid

Avoid these draft failures:

- writing a dashboard or scorecard chapter;
- creating a new health artifact, metric, ritual, smell, anti-pattern, failure story, vocabulary term, or primary concept;
- making the review heavy enough to become bureaucracy;
- teaching Architecture Review, Architecture Freeze, ADR, RFC, or release discipline again;
- turning Part V closure into a summary chapter without a usable practice;
- starting Part VI by teaching legacy-system reading early;
- over-connecting the graph to concepts that appear only as background;
- treating `ANTIPATTERN-004` as Hero Engineer despite the current graph naming it Manager Mania;
- leaving the review without decisions, owners, artifact updates, and revisit triggers.

## 28. Author Draft Acceptance Criteria

The Author Draft should pass when:

- it creates `book/05-engineering-organization/31-architecture-health-reviews.md`;
- it preserves the required reader-facing chapter architecture;
- it keeps `CHAPTER-031` as `draft` in `knowledge/index.yaml`;
- it preserves the exact registered Chapter 31 relationship set;
- it illustrates `RITUAL-004` without creating a new concept;
- it defines architecture health as the ability to support necessary change;
- it distinguishes health review from Architecture Review, Architecture Freeze, audit, retrospective, dashboard review,
  and management process;
- it uses evidence from Change Radius, ownership, API promises, support, release, records, Bus Factor, weak signals,
  product obligations, and team learning;
- it produces decisions, owners, follow-up, artifact updates, and revisit triggers;
- it closes Part V and only lightly previews Part VI;
- it includes exactly three Principal's Notebook observations;
- it does not modify Chapters 1-30, Part V README, TOC, `editor/CHAPTER_ARCHITECTURE.md`, `editor/CANON.md`, or PEAK
  concept files.

## 29. Review Handoff Notes

For the Author Draft:

- write the manuscript only after this canonical brief is committed and pushed;
- keep the story centered on a working system whose next changes are becoming expensive;
- make the review evidence-based and non-blame;
- ensure every health signal leads to a possible decision or investigation;
- update artifacts in the story without inventing a new canonical artifact;
- preserve the selected/rejected concept decisions above;
- keep Part VI to a brief forward boundary;
- do not open a pull request or begin review gates during the Author Draft prompt.
