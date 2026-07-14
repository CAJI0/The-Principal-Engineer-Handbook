# CHAPTER-017 Canonical Brief: Using ADRs and RFCs Well

## 1. Metadata

- Stable ID: `CHAPTER-017`.
- Title: `Using ADRs and RFCs Well`.
- Part: Part III - Architecture Playbook.
- Chapter number: 17.
- Expected manuscript path: `book/03-architecture-playbook/17-using-adrs-and-rfcs-well.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-017-using-adrs-and-rfcs-well.md`.
- Branch: `chapter17`.
- Verified baseline `origin/main`: `5f6e41751acf8bf184048a754254946bdae917a4`.
- Baseline evidence: PR #18 squash commit, `Chapter 16: Designing for Failure and Recovery (#18)`.
- Chapter 16 feature Freeze commit checked for tree equivalence:
  `1bfb6d540e85344dc568413e7c6cfda75189ca77`.
- Canonical predecessor: `CHAPTER-016` - Designing for Failure and Recovery.
- Part position: fourth chapter of Part III - Architecture Playbook.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 17 is a Part III practice chapter, and current repository convention does not require a
  primary PEAK concept for practice chapters.
- Central PEAK artifacts: `ARTIFACT-001` - ADR and `ARTIFACT-002` - RFC.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `5f6e41751acf8bf184048a754254946bdae917a4`.
- That baseline is the PR #18 squash commit, `Chapter 16: Designing for Failure and Recovery (#18)`.
- The Chapter 16 feature-branch Freeze commit `1bfb6d540e85344dc568413e7c6cfda75189ca77` remains tree-equivalent for the
  checked Chapter 16 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-016` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-016` is the third Part III chapter and is canonical.
- `editor/EDITOR_LOG.md` records Chapter 16 Editorial, Canon, Technical, and Freeze Review entries in order.
- The table of contents places `Using ADRs and RFCs Well` immediately after Chapter 16 in Part III.
- `ARTIFACT-001` exists exactly once as `ADR`.
- `ARTIFACT-002` exists exactly once as `RFC`.
- `ARTIFACT-003`, `ARTIFACT-006`, `LAW-005`, `RITUAL-001`, `RITUAL-006`, and `METRIC-003` exist and are available as
  supporting concepts.
- `book/03-architecture-playbook/README.md` remains a placeholder and should not be expanded in this phase.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-017` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 17 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter17` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part III Role

Chapter 17 is the fourth Part III practice chapter. Chapter 14 taught boundary placement, Chapter 15 taught affected
surface, and Chapter 16 taught failure and recovery behavior. Chapter 17 teaches how significant architecture proposals
and decisions become shared memory instead of private memory, meeting notes, or commit messages.

The chapter should move from designing architecture decisions to operating the artifacts that carry those decisions. It
should show that a Principal Engineer uses ADRs and RFCs to reduce ambiguity, invite useful review, preserve trade-offs,
and keep decisions findable after the immediate project has moved on.

Chapter 17 must remain a practice chapter. It should not become a documentation-style guide, a template catalog, a
process-compliance chapter, or the full Architecture Review chapter.

## 4. Canonical Purpose

Prepare Chapter 17 to teach a Principal Engineer how to choose, write, review, maintain, and retire ADRs and RFCs
without turning them into ceremony.

The chapter should move the reader from asking:

> Should we write an ADR or an RFC?

to asking:

> Which decision or proposal needs shared review, what evidence and trade-offs must be visible, who owns the outcome,
> and how will future engineers find, trust, and update the record?

The chapter must teach the difference between a decision artifact and a proposal artifact. A decision record without
evidence becomes an opinion archive. A proposal without a decision path becomes endless discussion.

## 5. Primary-Concept Resolution

Chapter 17 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records, and Chapters 14 through
16 established that Part III practice chapters may be carried by a relationship set rather than by one primary concept.
Chapter 17 therefore records an explicit no-primary decision.

`ARTIFACT-001` - ADR and `ARTIFACT-002` - RFC are the central paired artifacts. The ADR carries accepted or superseded
architecture decisions and their consequences. The RFC carries a proposal that needs review before the decision becomes
expensive to change.

Do not create a new PEAK law, vocabulary term, artifact, ritual, metric, smell, anti-pattern, or failure story for
decision records. Terms used in this chapter remain chapter-local unless a later Canon Review identifies an approved
repository-wide gap.

## 6. Central Thesis

ADRs and RFCs work when they make architectural reasoning reviewable before commitment and discoverable after
commitment.

Approved supporting formulation for the future draft:

> Use RFCs to test proposals before they harden; use ADRs to preserve decisions after they matter.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. ADRs are records to write after decisions are already obvious;
2. RFCs are documents used to get permission;
3. the template matters more than the decision;
4. every technical choice deserves the same artifact;
5. a meeting summary can replace a decision record;
6. accepted ADRs should never change;
7. review comments are noise once the decision is made;
8. documentation is complete when the file exists.

By the end of the chapter, the reader should be able to:

1. decide whether a choice needs no artifact, a Decision Journal entry, an RFC, or an ADR;
2. write an RFC that exposes motivation, scope, non-goals, proposal, risks, and open questions;
3. write an ADR that records context, decision, consequences, and alternatives;
4. separate proposal review from decision recording;
5. preserve evidence, uncertainty, dissent, and trade-offs without bloating the record;
6. link ADRs, RFCs, code, tests, owners, and Architecture Ledger entries;
7. supersede or retire records without erasing history;
8. improve Discoverability so future engineers can find the decision behind behavior.

## 8. Semantic Definition

For this chapter, using ADRs and RFCs well means choosing the smallest durable artifact that makes a significant
architecture proposal or decision understandable, reviewable, and maintainable across time.

Important questions are:

- what is being proposed or decided;
- why it matters now;
- what evidence supports the proposal or decision;
- which alternatives were considered;
- what is explicitly out of scope;
- who owns the decision after acceptance;
- which consequences and risks remain;
- when the record should be revisited;
- where future engineers can find it.

## 9. In-Scope and Out-of-Scope

### In Scope

Chapter 17 covers:

- choosing between no artifact, Decision Journal entry, RFC, and ADR;
- proposal versus decision semantics;
- context, scope, non-goals, evidence, alternatives, risks, consequences, owners, and review triggers;
- using RFCs before decisions harden;
- using ADRs after decisions matter;
- recording disagreement without turning the artifact into a transcript;
- linking artifacts to code, tests, incidents, releases, Architecture Ledger entries, and related decisions;
- superseding, retiring, and revisiting records;
- discoverability, naming, location, ownership, and status;
- an embedded architecture story where a cross-boundary proposal needs RFC review and an accepted decision becomes an
  ADR.

### Explicitly Out of Scope

Do not turn Chapter 17 into:

- a documentation-style handbook;
- a template catalog;
- a writing workshop;
- a process-compliance chapter;
- a tool survey;
- a code-review chapter;
- Chapter 14 boundary placement repeated;
- Chapter 15 Change Radius repeated;
- Chapter 16 failure and recovery repeated;
- Chapter 18 Architecture Review;
- Chapter 19 Architecture Freeze;
- a release-management chapter;
- a new PEAK concept proposal.

## 10. ADR Versus RFC

An RFC is a proposal artifact. It invites review before a consequential decision hardens. It should expose the problem,
motivation, scope, non-goals, proposal, risks, evidence, alternatives, and open questions.

An ADR is a decision artifact. It records an architectural decision, why it was made, what alternatives were rejected,
and what consequences the team accepts.

The same topic may move from RFC to ADR. The RFC gathers review and reduces uncertainty. The ADR preserves the accepted
decision and its consequences. They should not duplicate each other blindly.

## 11. Decision Scale

The chapter should teach proportionality.

Not every choice deserves an ADR or RFC. Small reversible implementation choices may need no record. Medium reversible
choices may fit a Decision Journal entry. Cross-boundary proposals with material uncertainty usually deserve an RFC.
Accepted architecture choices that affect ownership, cost, contracts, reversibility, or future maintenance usually
deserve an ADR.

Artifact weight should follow consequence, not seniority, personal preference, or organizational habit.

## 12. Proposal Before Decision

The future draft should show the value of review before commitment.

An RFC is useful when the team still has meaningful choices. It should name open questions and decision criteria rather
than asking reviewers to bless an already implemented plan. A good RFC can end as accepted, rejected, narrowed,
deferred, or converted into a deeper Architecture Review.

The chapter may mention `RITUAL-006` - RFC Friday as one review space, but it must not turn the ritual itself into the
main topic.

## 13. Decision After Commitment

An ADR should be written when the decision matters beyond the moment.

The future draft should teach that an ADR is not a victory note. It is a maintenance record. It tells a future engineer
which context was true, what evidence existed, which alternatives were rejected, which consequences were accepted, and
what would make the decision worth revisiting.

An accepted ADR may later be superseded. History remains useful even when the system moves on.

## 14. Evidence and Confidence

Use `LAW-005` - Evidence Before Confidence as the evidence posture.

The future draft should require records to separate claim, evidence, confidence, and residual uncertainty. Evidence may
come from tests, prototypes, incident data, field behavior, benchmarks, constraints, compatibility checks, operational
experience, or review findings.

Do not make Chapter 17 repeat Chapter 13's full evidence framework. Here, evidence matters because it changes the
quality of the artifact.

## 15. Context and Consequences

Decision records should make context and consequences explicit.

Context should include the forces that made the decision necessary: constraints, product promises, boundaries,
dependencies, failure modes, change surface, support cost, manufacturing realities, and evidence limits. Consequences
should include benefits, costs, obligations, test requirements, compatibility work, ownership, and revisit triggers.

A record that says only what the team chose is not enough.

## 16. Alternatives and Non-Goals

The future draft should treat alternatives and non-goals as design tools.

Alternatives show that the team made a choice, not a reflex. Non-goals protect the proposal from expanding until nobody
can review it. Rejected options should be represented fairly, including why they were attractive and why they were not
selected for this context.

The chapter should avoid straw-person alternatives and generic non-goals.

## 17. Ownership and Review

Every significant record needs an owner.

The owner is responsible for keeping the decision findable, updating status, coordinating review, and knowing when the
record needs to be superseded or retired. Reviewers should be chosen because they own affected boundaries, operations,
tests, tools, manufacturing paths, support paths, or future maintenance, not because they are nearby in the org chart.

Chapter 17 may describe review roles inside ADR/RFC practice. Chapter 18 owns the complete Architecture Review ritual.

## 18. Discoverability

Use `METRIC-003` - Discoverability as the visibility metric.

The future draft should show that an artifact is useful only if future engineers can find it from the behavior,
contract, module, test, incident, release, or owner it affects. Discoverability improves through stable names, clear
status, links, owners, dates, related artifacts, and Architecture Ledger entries.

The chapter should avoid claiming that a repository search alone proves discoverability.

## 19. Architecture Ledger and Decision Journal

Use `ARTIFACT-003` and `ARTIFACT-006` as supporting artifacts.

A Decision Journal entry is appropriate when the decision is important but smaller, more reversible, or not yet worth a
full ADR. An Architecture Ledger helps teams keep active decisions, owners, status, related artifacts, and review dates
visible when records are spread across files and teams.

Chapter 17 should not duplicate either artifact's whole template. It should explain how they fit the ADR/RFC lifecycle.

## 20. Status and Lifecycle

The future draft should teach status as part of meaning.

Useful statuses may include proposed, under review, accepted, rejected, superseded, retired, deferred, and withdrawn.
The exact vocabulary may vary by team, but status must make clear whether the artifact is a live proposal, an accepted
decision, historical context, or obsolete guidance.

Do not let status become bureaucracy. Status exists so engineers know whether they should follow, review, ignore, or
revisit the record.

## 21. Supersession and Retirement

The future draft should distinguish changing history from changing the current decision.

Do not rewrite an old ADR as if the original context never existed. Supersede it with a new record or a clear status
change. Retire a decision when it no longer affects architecture. Keep enough history to explain why the old path
existed and why it stopped being valid.

The chapter should make clear that stale records are dangerous when their status is ambiguous.

## 22. Linking Records to Reality

The future draft should require records to connect to the system.

Useful links may include code owners, modules, tests, diagrams, event catalogs, release notes, incident reports, RFCs,
ADRs, Decision Journal entries, Architecture Ledger rows, and follow-up tasks. Links should help future engineers find
the decision behind behavior. They should not become a dumping ground.

If a record cannot be found from the system surface it governs, the record is weaker than it looks.

## 23. Boundary With Chapter 14

Chapter 14 owns drawing boundaries that survive change: responsibility, authority, knowledge, vocabulary, dependency
direction, translation, integrity, back channels, and proportional boundary cost.

Chapter 17 may record a boundary decision in an ADR or propose a boundary change in an RFC. It must not reteach how to
draw the boundary. Its focus is how the decision or proposal is made reviewable, durable, and discoverable.

## 24. Boundary With Chapter 15

Chapter 15 owns Change Radius: mapping affected surface, separating required from accidental spread, and sequencing
change.

Chapter 17 may use Change Radius to decide review scope and artifact need. It must not teach the full Change Radius
method. Its focus is how that scope and reasoning enter an RFC or ADR.

## 25. Boundary With Chapter 16

Chapter 16 owns failure and recovery design: operation outcomes, retry, partial completion, duplicate handling,
recovery to known state, and escalation.

Chapter 17 may record a recovery decision in an ADR or propose recovery behavior in an RFC. It must not reteach failure
semantics or recovery design.

## 26. Boundary With Chapters 18 and 19

Chapter 18 owns Architecture Review: the ritual for reviewing architecture before it hardens.

Chapter 17 may show that ADRs and RFCs feed review and capture outcomes, but it must not become a full review process.

Chapter 19 owns Architecture Freeze: stabilizing architecture without stopping learning.

Chapter 17 may mention freeze readiness and decision status, but it must not teach freeze criteria, exception handling,
or revalidation.

## 27. Boundaries With Chapters 1-13

### Chapters 1-6 - Principal Engineering Foundations

Chapter 17 may use principal thinking, constraints, questions, ownership, evidence, and stewardship as premises. It
must not repeat the Part I mindset chapters.

### Chapter 7 - Every State Has One Owner

Chapter 17 may require decision ownership. It must not reteach state ownership.

### Chapter 8 - Every API Is a Promise

Chapter 17 may record API promises in ADRs and RFCs. It must not become the API-contract chapter.

### Chapter 9 - Every Dependency Is a Decision

Chapter 17 may record dependency decisions. It must not reteach dependency selection, update surface, or replacement
cost.

### Chapter 10 - Time Is a Dependency

Chapter 17 may record temporal assumptions and deadlines. It must not reteach time semantics.

### Chapter 11 - Unused Flexibility Is Waste

Chapter 17 may reject speculative options in alternatives. It must not become an optionality audit.

### Chapter 12 - Simplicity Is a Feature

Chapter 17 may ask whether the artifact increases or reduces future complexity. It must not become a general simplicity
chapter.

### Chapter 13 - Evidence Before Confidence

Chapter 17 may require evidence in records. It must not repeat Chapter 13's full law and judgment method.

## 28. Boundaries With Later Parts

Part IV should retain product-line architecture, manufacturing and field workflows, observability implementation,
release discipline, upgrade systems, and the reference project.

Part V should retain organizational rituals, mentoring, alignment, and Architecture Health Review operation.

Part VI should retain legacy discovery, silent-coupling recovery, utility gravity, deletion, refactoring, and product
trust in legacy systems.

Chapter 17 may use examples that touch these areas, but it must not take over their future depth.

## 29. Recommended Embedded-Systems Story

### Working Title

The RFC That Saved the ADR

### System

Use an embedded product with firmware, a gateway, a service tool, manufacturing tests, and a cloud or host application.
The team needs to change how configuration updates are represented and validated across the device and service tool.

### Trigger

An engineer starts writing an ADR for a new configuration-update protocol after implementation has already begun. The
record says which protocol the team wants, but it does not expose who is affected, which assumptions are untested, or
what alternatives were rejected.

### Inadequate Response

The team treats the ADR as a permission slip. Reviewers comment on wording instead of architecture. Manufacturing,
service, and field-support implications appear late. The decision looks documented but remains poorly reviewed.

### Principal Engineer Intervention

The Principal Engineer pauses the ADR, converts the live question into an RFC, names scope and non-goals, lists open
questions, gathers evidence, routes review to affected owners, and then writes an ADR only after the decision is ready.

The ADR links back to the RFC, records alternatives and consequences, names owners and revisit triggers, and updates the
Architecture Ledger.

## 30. Discussion Arc

1. **The artifact is not the decision.** A file can exist while the reasoning remains invisible.
2. **Choose the artifact by consequence.** Record weight should follow impact, uncertainty, and future cost.
3. **RFCs preserve choice.** Use them while review can still change direction.
4. **ADRs preserve commitment.** Use them when future engineers must understand the accepted decision.
5. **Evidence belongs in the record.** Claims should show what supports them and what remains uncertain.
6. **Alternatives deserve fair treatment.** Rejected options teach future maintainers what the team already considered.
7. **Status prevents stale guidance.** Records need clear live, historical, superseded, or retired meaning.
8. **Discoverability is part of quality.** A good record can be found from the behavior it governs.
9. **Records need owners.** Without ownership, artifacts drift into folklore.
10. **Review and freeze are later steps.** ADRs and RFCs feed those practices without replacing them.

These are intellectual progression points, not mandatory manuscript headings.

## 31. Applicability

The chapter applies when a decision or proposal affects architecture, ownership, product behavior, APIs, protocols,
state, persistence, timing, failure behavior, dependencies, manufacturing, service tools, tests, releases, support, or
future maintenance.

It is especially relevant when the decision crosses ownership boundaries, has material uncertainty, affects long-lived
product commitments, or will be questioned by engineers who were not present for the original discussion.

## 32. Limits

The future draft must avoid dogmatism. It should not claim:

- every decision needs an ADR;
- every proposal needs an RFC;
- writing the artifact proves the decision is good;
- a longer template creates better reasoning;
- accepted ADRs are immutable law;
- all disagreement must be preserved;
- a meeting transcript is a good decision record;
- an RFC is a vote;
- an ADR is an approval form;
- discoverability is solved by storing files in one folder;
- a record can replace ownership;
- status changes can replace review.

## 33. Violations

The future draft should make these violations visible:

- ADR written after implementation only to justify the result;
- RFC used when no meaningful alternative remains;
- proposal with no non-goals;
- alternatives listed without trade-offs;
- evidence replaced by senior opinion;
- decision owner missing;
- status unclear after the system changes;
- old ADR contradicting current code with no superseding record;
- RFC review limited to the author's team despite affected boundaries;
- decision scattered across chat, tickets, slides, and memory;
- Architecture Ledger not updated for an active decision;
- record that future engineers cannot find from the affected module or behavior.

## 34. Engineering Principle

Target principle for the future draft:

> Use the smallest durable artifact that makes a consequential proposal or decision reviewable now and discoverable
> later.

The principle should imply review questions:

1. Is this a proposal, a decision, or a smaller judgment?
2. Who is affected?
3. What evidence exists?
4. What remains uncertain?
5. Which alternatives were considered?
6. What is out of scope?
7. Who owns the outcome?
8. What consequences are accepted?
9. What would cause the record to be revisited?
10. Where will future engineers find it?

The final manuscript may shorten this list for reader rhythm.

## 35. Exercise

### Working Title

Choose the Right Decision Artifact

Ask the reader to choose one current or recent architecture choice and document:

1. decision or proposal statement;
2. affected owners and boundaries;
3. current evidence;
4. uncertainty and open questions;
5. alternatives considered;
6. risks and consequences;
7. artifact choice: no artifact, Decision Journal entry, RFC, or ADR;
8. why the chosen artifact is sufficient;
9. review path or decision owner;
10. status;
11. links to code, tests, release notes, incidents, or related records;
12. revisit trigger;
13. Architecture Ledger update if the decision remains active.

The exercise must end with one artifact choice, one owner, one evidence statement, and one discoverability action. Do
not create a new canonical artifact.

## 36. ADR

### Working Title

Adopt RFC-First Review for the Configuration Update Protocol

### Context

- A configuration-update protocol affects firmware, gateway behavior, service tools, manufacturing tests, support
  workflows, and field compatibility.
- Implementation started before affected owners had a shared proposal.
- The first ADR draft records a preferred approach but hides unresolved questions.
- Manufacturing and support owners need to review non-goals, migration, validation, and rollback expectations before
  the decision hardens.
- Future maintainers will need one place to find the accepted decision and why rejected options were not chosen.

### Decision

- Convert the live proposal into an RFC before accepting the protocol decision.
- Use the RFC to record motivation, scope, non-goals, proposal, risks, evidence, alternatives, and open questions.
- Route review to firmware, gateway, service-tool, manufacturing, test, and support owners.
- Use RFC Friday for lightweight proposal review and escalate unresolved architecture risk to Architecture Review.
- After the decision is accepted, write an ADR that records the decision, context, consequences, alternatives, owner,
  status, and revisit trigger.
- Link the ADR to the RFC, tests, affected modules, release notes, and Architecture Ledger entry.

### Alternatives Considered

- Keep the ADR and ask reviewers to approve it.
- Finish implementation and document the result later.
- Use only a ticket or meeting notes.
- Require a full Architecture Review before any written proposal.
- Skip the ADR because the RFC already exists.
- Create one large document that mixes proposal discussion and accepted decision.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits include earlier review, clearer non-goals, visible evidence, fair alternatives, a durable accepted decision,
and better discoverability for future maintainers.

Costs include time to write and review the RFC, explicit ownership of record status, and maintenance work when the
decision is superseded or retired.

The ADR must make a real architecture-process decision for the story. It must not reduce to "write better docs."

## 37. PEAK Concept Map

### Concepts Inspected

- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-006` - Architecture Ledger.
- `LAW-005` - Evidence Before Confidence.
- `RITUAL-001` - Architecture Review.
- `RITUAL-006` - RFC Friday.
- `METRIC-003` - Discoverability.
- `VOCAB-003` - Decision Journal.
- `LAW-002` - Every API Is a Promise.
- `LAW-007` - Every Dependency Is a Decision.
- `SMELL-001` - Silent Coupling.
- `ANTIPATTERN-006` - Temporary Solution.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `VOCAB-007` - Architecture Health.
- `METRIC-005` - Architecture Health.
- `RITUAL-004` - Architecture Health Review.

### Selected Concepts

- `ARTIFACT-001` - ADR: material because the chapter directly teaches decision records and the accepted decision
  lifecycle.
- `ARTIFACT-002` - RFC: material because the chapter directly teaches proposal review before decisions harden.
- `ARTIFACT-003` - Decision Journal: material because the chapter must distinguish smaller decision records from full
  ADRs and RFCs.
- `ARTIFACT-006` - Architecture Ledger: material because active decisions need owner, status, related artifact, and
  review-date visibility.
- `LAW-005` - Evidence Before Confidence: material because records must separate evidence, confidence, and uncertainty.
- `RITUAL-001` - Architecture Review: material because ADRs and RFCs can feed review or capture review outcomes, while
  Chapter 18 retains the full ritual.
- `RITUAL-006` - RFC Friday: material because it is the named lightweight ritual for reviewing active RFCs.
- `METRIC-003` - Discoverability: material because a good ADR or RFC must be findable from the behavior, owner, and
  contract it affects.

### Rejected Concepts

- `VOCAB-003` - Decision Journal: the artifact edge is sufficient because Chapter 17 concerns artifact choice and
  lifecycle, not vocabulary definition.
- `LAW-002` - Every API Is a Promise: many records may describe API promises, but Chapter 8 owns the law.
- `LAW-007` - Every Dependency Is a Decision: many records may describe dependency decisions, but Chapter 9 owns the
  law.
- `SMELL-001` - Silent Coupling: poor records may hide coupling, but the chapter is about artifact practice rather than
  diagnosing the smell.
- `ANTIPATTERN-006` - Temporary Solution: supersession and retirement help prevent stale temporary choices, but Chapter
  11 and Chapter 15 carry the broader temporary-solution risk.
- `VOCAB-001` and `METRIC-001` - Change Radius: affected surface can guide artifact choice, but Chapter 15 owns the
  method and metric.
- `VOCAB-007`, `METRIC-005`, and `RITUAL-004` - Architecture Health: decision records support long-term health, but
  later chapters and parts own health review operation.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as proposal artifact, decision artifact, superseded, retired, record owner, record status, and artifact
choice remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-017` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-017
  type: illustrates
  to: ARTIFACT-001

- from: CHAPTER-017
  type: illustrates
  to: ARTIFACT-002

- from: CHAPTER-017
  type: references
  to: ARTIFACT-003

- from: CHAPTER-017
  type: references
  to: ARTIFACT-006

- from: CHAPTER-017
  type: references
  to: LAW-005

- from: CHAPTER-017
  type: references
  to: RITUAL-001

- from: CHAPTER-017
  type: references
  to: RITUAL-006

- from: CHAPTER-017
  type: references
  to: METRIC-003
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 38. Reader-Facing Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 17 role:

- Opening Quote: establish that records are useful only when they preserve reasoning.
- Story: show a team moving from after-the-fact ADR to RFC-backed review and accepted ADR.
- Discussion: teach artifact choice, proposal versus decision, evidence, alternatives, status, ownership,
  discoverability, and lifecycle.
- Engineering Principle: anchor proportional durable artifacts as an architecture habit.
- Architecture Exercise: choose the right decision artifact for one real choice.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local choice to use RFC-first review and ADR capture.
- Editor's Commentary: explain how Chapter 17 advances Part III after boundary, radius, and recovery chapters and before
  review and freeze chapters.

## 39. Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- An RFC preserves choice; an ADR preserves commitment.
- A record without evidence is only an opinion with a filename.
- A decision nobody can find is not shared memory.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 40. Technical Requirements

The future draft must treat the following accurately:

- embedded firmware, gateway, service-tool, manufacturing, support, and release stakeholders;
- proposal review before implementation hardens;
- accepted decision record after review;
- evidence from tests, prototypes, compatibility checks, incidents, and field behavior;
- scope and non-goal boundaries;
- alternatives and trade-offs;
- decision ownership;
- status vocabulary;
- links between RFC, ADR, code, tests, releases, and Architecture Ledger;
- superseded and retired records;
- discoverability from affected behavior;
- proportional artifact weight.

Do not require a specific repository layout, issue tracker, document tool, review platform, template system, firmware
stack, MCU, RTOS, gateway architecture, or cloud service.

## 41. Terminology

Use terms precisely:

- ADR: an artifact that records an architectural decision, why it was made, and what consequences it creates;
- RFC: an artifact that invites review before a decision becomes hard to change;
- Decision Journal: a lightweight record for decisions where a full ADR would be too heavy;
- Architecture Ledger: a compact inventory of active architectural decisions and known debts;
- proposal: a suggested direction still open to review;
- decision: an accepted direction with ownership and consequences;
- non-goal: an explicit boundary that narrows review and protects scope;
- alternative: a plausible option considered and rejected or deferred;
- status: the current meaning of a record;
- superseded: replaced by a later decision while history remains useful;
- retired: no longer active because the decision no longer affects architecture.

The chapter must avoid these misleading statements:

- ADR means approved;
- RFC means consensus;
- a template creates good reasoning;
- writing the record after the fact is equivalent to review;
- accepted ADRs cannot be superseded;
- all decisions need the same record weight;
- links are sufficient without ownership;
- meeting notes are durable architecture memory;
- Architecture Review is the same as an RFC comment thread.

## 42. Failure Modes to Avoid

The later draft must not become:

- a documentation-style chapter;
- a template catalog;
- a writing-style tutorial;
- a tool survey;
- a process-compliance chapter;
- a code-review chapter;
- Chapter 14 repeated;
- Chapter 15 repeated;
- Chapter 16 repeated;
- Chapter 18 written early;
- Chapter 19 written early;
- a claim that every decision needs an ADR or RFC;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 43. Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete embedded architecture proposal crossing affected owners;
- the Principal Engineer move recasts the problem from "write an ADR" to "review the proposal before recording the
  accepted decision";
- no primary PEAK concept is assigned unless a later author/editor decision changes repository convention;
- `ARTIFACT-001` and `ARTIFACT-002` are materially present as the central paired artifacts;
- the manuscript distinguishes proposal, decision, Decision Journal entry, RFC, and ADR;
- evidence, alternatives, non-goals, risks, consequences, ownership, status, and revisit triggers are materially present;
- RFC Friday appears only as a lightweight supporting ritual;
- Architecture Review remains a boundary for Chapter 18;
- Architecture Freeze remains a boundary for Chapter 19;
- Discoverability is treated as artifact quality, not only file location;
- stale, superseded, and retired records are handled without rewriting history;
- the exercise ends with one artifact choice, one owner, one evidence statement, and one discoverability action;
- the ADR makes a genuine story-local architecture-process decision;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 44. Review Handoff

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into documentation style, process compliance, tool choice, Architecture Review, or Architecture
Freeze.

Canon Review should verify that Chapter 17 remains a Part III practice chapter with no forced primary concept,
materially uses ADR and RFC as the central paired artifacts, preserves the registered relationship set, and does not
imply a new PEAK artifact, ritual, metric, or vocabulary term.

Technical Review should focus on artifact choice, cross-boundary review timing, evidence quality, accepted-decision
semantics, owner and status clarity, supersession and retirement, links to affected system surfaces, and realistic
embedded stakeholders.

Freeze Review should confirm that Chapter 17 remains the fourth Part III practice chapter, keeps the manuscript
architecture intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and
leaves the reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
configuration protocol, affected owners, review path, artifact names, and final notebook wording while preserving the
ADR/RFC thesis, story shape, PEAK map, and chapter boundaries.
