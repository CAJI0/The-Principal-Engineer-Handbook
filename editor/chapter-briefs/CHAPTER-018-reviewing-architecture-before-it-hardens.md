# CHAPTER-018 Canonical Brief: Reviewing Architecture Before It Hardens

## 1. Metadata

- Stable ID: `CHAPTER-018`.
- Title: `Reviewing Architecture Before It Hardens`.
- Part: Part III - Architecture Playbook.
- Chapter number: 18.
- Expected manuscript path: `book/03-architecture-playbook/18-reviewing-architecture-before-it-hardens.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-018-reviewing-architecture-before-it-hardens.md`.
- Branch: `chapter18`.
- Verified baseline `origin/main`: `be9bf64b776b935bb5d94f240a91156a1b2e59f4`.
- Baseline evidence: PR #19 squash commit, `Chapter 17: Using ADRs and RFCs Well (#19)`.
- Chapter 17 feature Freeze commit checked for tree equivalence:
  `b72aba4d196c04fda1e4c2c728ffda60a3927ea9`.
- Canonical predecessor: `CHAPTER-017` - Using ADRs and RFCs Well.
- Part position: fifth chapter of Part III - Architecture Playbook.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 18 is a Part III practice chapter, and current repository convention does not require a
  primary PEAK concept for practice chapters.
- Central practice: `RITUAL-001` - Architecture Review.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `be9bf64b776b935bb5d94f240a91156a1b2e59f4`.
- That baseline is the PR #19 squash commit, `Chapter 17: Using ADRs and RFCs Well (#19)`.
- The Chapter 17 feature-branch Freeze commit `b72aba4d196c04fda1e4c2c728ffda60a3927ea9` remains tree-equivalent for
  the checked Chapter 17 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-017` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-017` is the fourth Part III chapter and is canonical.
- `editor/EDITOR_LOG.md` records Chapter 17 Editorial, Canon, Technical, and Freeze Review entries in order.
- The table of contents places `Reviewing Architecture Before It Hardens` immediately after Chapter 17 in Part III.
- `RITUAL-001` exists exactly once as `Architecture Review`.
- `ARTIFACT-001`, `ARTIFACT-002`, `ARTIFACT-003`, `ARTIFACT-006`, `LAW-001`, `LAW-002`, `LAW-005`, `LAW-007`,
  `VOCAB-001`, `METRIC-001`, `METRIC-003`, and `RITUAL-006` exist and are available as supporting concepts.
- `book/03-architecture-playbook/README.md` remains a placeholder and should not be expanded in this phase.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-018` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 18 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter18` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part III Role

Chapter 18 is the fifth Part III practice chapter. Chapter 14 taught boundary placement, Chapter 15 taught Change
Radius, Chapter 16 taught failure and recovery behavior, and Chapter 17 taught ADR and RFC practice. Chapter 18 teaches
the review practice that challenges consequential architecture decisions while change is still possible.

The chapter should move the reader from treating architecture review as approval, presentation, or committee ceremony
toward treating it as a structured challenge to a decision that is about to harden.

Chapter 18 must remain a practice chapter. It should not become an artifact-writing chapter, a governance-board chapter,
a meeting facilitation guide, a release gate, or the Architecture Freeze chapter.

## 4. Canonical Purpose

Prepare Chapter 18 to teach how to review architecture while meaningful change is still possible.

The chapter should move the reader from asking:

> Can we get this design approved?

to asking:

> What decision is about to harden, what evidence would change it, who is materially affected, and what must be resolved
> before the architecture becomes expensive to move?

The chapter must show that Architecture Review is not approval after implementation. It is a structured challenge to a
consequential architectural decision while evidence, alternatives, boundaries, risks, and consequences can still change
the outcome.

## 5. Primary-Concept Resolution

Chapter 18 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records, and Chapters 14 through
17 established that Part III practice chapters may be carried by a relationship set rather than by one primary concept.
Chapter 18 therefore records an explicit no-primary decision.

`RITUAL-001` - Architecture Review is the central practice and the concept Chapter 18 materially illustrates. The
chapter should not create a new Review Gate, Architecture Review Board, Review Packet, Review Readiness, Review Debt,
Architecture Approval, Decision Readiness, Challenge Map, Review Charter, or Architectural Risk Review concept.

## 6. Central Thesis

Architecture Review is useful when it challenges a consequential decision before code, tests, tools, release plans, and
organizational commitments make alternatives economically fake.

Approved supporting formulation for the future draft:

> Review architecture while the decision can still change. Name the decision, owner, evidence, alternatives, risks, and
> hardening point; then close the review into a decision, evidence request, accepted risk, or revised proposal.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. Architecture Review is an approval gate after design work is effectively complete.
2. A slide review is enough if senior people attend.
3. More reviewers automatically improve the decision.
4. Approval is the only successful review outcome.
5. Disagreement is a sign the team is not aligned.
6. RFC comments or code review can replace architecture review for consequential decisions.
7. Risks can be approved as follow-up tickets without owner, evidence, or decision effect.
8. A standing board owns architectural safety.

By the end of the chapter, the reader should be able to:

1. identify the decision that is about to harden;
2. distinguish too-early, useful, and too-late review timing;
3. name the decision owner, proposal owner, affected owners, facilitator, reviewers, and follow-up owners;
4. use affected architecture rather than hierarchy to choose participants;
5. review evidence, assumptions, alternatives, risks, Change Radius, and hardening points;
6. turn disagreement into evidence requests, decision changes, accepted risks, or escalation;
7. close review comments into explicit outcomes rather than durable ambiguity;
8. update ADRs, RFCs, Decision Journal entries, and Architecture Ledger links after the review.

## 8. Review Before Hardening

For this chapter, hardening means a decision is becoming expensive to move because code depends on it, data formats or
protocols are implemented, tests encode it, tooling assumes it, release plans depend on it, teams staff around it,
customer commitments reflect it, compatibility promises are made, rollback becomes costly, or alternatives become
politically or economically fake.

Architecture Review should happen when enough is known to review but before sunk cost turns rejection into theater.

Too early means the decision is vague, alternatives are not real, evidence is absent, and reviewers argue with guesses.
Too late means implementation has already made rejection expensive, comments become wording suggestions, and risks
become post-approval tickets.

There is no rigid calendar rule. The timing should follow the decision's hardening point.

## 9. In-Scope and Out-of-Scope

### In Scope

Chapter 18 covers:

- reviewing consequential architectural decisions before they harden;
- naming the review subject, owner, affected owners, evidence, alternatives, risks, and hardening point;
- choosing participants from affected architecture rather than hierarchy;
- using ADRs, RFCs, Decision Journal entries, and Architecture Ledger entries as inputs and outputs;
- using Change Radius to scope affected surface and review participants;
- examining ownership, boundary placement, API and protocol promises, state ownership, dependencies, failure and
  recovery behavior, compatibility, migration, tests, observability, rollout, and field consequences;
- turning disagreement into explicit outcomes;
- closing review comments into decision changes, evidence requests, accepted risks, split decisions, deferrals,
  rejection, escalation, or record updates;
- diagnosing review theater.

### Explicitly Out of Scope

Do not turn Chapter 18 into:

- Chapter 17's ADR and RFC mechanics;
- Chapter 19's Architecture Freeze, exception, and revalidation policy;
- a governance-board operating model;
- a meeting facilitation handbook;
- a generic design-review checklist;
- a code-review chapter;
- an approval-signature process;
- an organization-wide review-culture chapter;
- a release readiness gate;
- a product-line governance chapter;
- a new PEAK concept proposal.

## 10. Review Subject

The review subject is a consequential architectural decision, not a vague meeting agenda.

The future draft should require the subject to name:

- decision under review;
- decision owner;
- proposal owner if different;
- affected owners;
- current decision state;
- scope and non-goals;
- alternatives;
- evidence;
- assumptions;
- risks;
- Change Radius;
- expected consequences;
- unresolved questions;
- decision deadline;
- reversibility;
- records to update.

Avoid reviews titled only "review the design," "approve this project," or "look at slides." Split unrelated decisions
when they have different owners, consequences, or timelines.

## 11. Review Inputs

Chapter 18 may mention chapter-local review input, but it must not register a new PEAK artifact.

Valid inputs include:

- an RFC or ADR draft;
- decision statement;
- context;
- diagram;
- affected boundaries;
- Change Radius map;
- evidence summary;
- assumptions;
- alternatives;
- failure and recovery implications;
- compatibility or migration implications;
- risks;
- open questions;
- owner list;
- proposed outcome.

The chapter should use Chapter 17 artifacts as inputs and outputs without duplicating Chapter 17's artifact-choice,
status, closure, supersession, or discoverability teaching.

## 12. Participants and Roles

Participants are determined by affected architecture, not hierarchy.

Potential roles include:

- decision owner;
- proposal author;
- affected component owners;
- API or protocol owners;
- state or data owners;
- support and operations;
- manufacturing, service, and test owners where relevant;
- security, safety, or compliance reviewers where relevant;
- future maintenance owner;
- facilitator;
- experienced architecture reviewer.

The chapter must distinguish reviewer, decision owner, facilitator, approver where governance uses one, and follow-up
owner. Consensus can help, but unanimity must not be required unless local governance explicitly says so.

Do not require a fixed committee.

## 13. What Architecture Review Examines

Architecture Review should examine the decision across:

- ownership and authority;
- boundary placement;
- API and protocol promises;
- state ownership and transitions;
- dependency commitments;
- Change Radius;
- failure and recovery behavior;
- evidence and confidence;
- compatibility;
- reversibility;
- observability needed to validate the decision;
- tests at correct boundaries;
- migration or rollout implications;
- operational and field consequences;
- alternatives and rejected options;
- risks and unresolved questions;
- decision-record updates.

Use earlier chapters as review lenses. Do not reteach them.

## 14. Review Questions

The future draft should keep the review questions compact and operational:

1. What decision is hardening?
2. Who owns the decision?
3. Who is materially affected?
4. What would make the team choose differently?
5. Which boundary, state, API, dependency, failure path, or Change Radius changes?
6. Which evidence supports the decision?
7. Which evidence is missing?
8. Which alternatives remain real?
9. What risk is accepted?
10. What must change before the next irreversible step?
11. What artifact preserves the outcome?

Avoid an oversized checklist.

## 15. Outcomes

Architecture Review must close into a clear outcome.

Possible outcomes include:

- proceed as proposed;
- proceed with explicit changes;
- narrow scope;
- split decision;
- request evidence;
- run an experiment or spike;
- change ownership;
- revise boundary or contract;
- defer;
- reject;
- escalate unresolved risk;
- record accepted risk;
- update ADR, RFC, Decision Journal, or Architecture Ledger records.

Approved is not the only successful outcome. A review that changes the decision or discovers missing evidence early is
useful.

## 16. Review Comments and Closure

Review comments are not the durable decision.

The chapter should require comments to close into explicit outcomes: accepted changes, rejected concerns with reason,
evidence requests, split decisions, deferrals, accepted risks, escalation, or updates to the governing record.

A concern without an owner becomes decoration. A risk without accepted ownership becomes background noise. A comment
thread without a final decision record becomes a shadow architecture.

## 17. Evidence and Disagreement

Use `LAW-005` - Evidence Before Confidence as the evidence posture.

Separate:

- evidence;
- assumption;
- preference;
- personal experience;
- product constraint;
- operational constraint;
- unresolved uncertainty;
- accepted risk.

Disagreement is useful when it exposes evidence gaps, hidden owners, different constraints, or consequences. The chapter
should show disagreement becoming review material, not personal conflict or consensus theater.

## 18. Review Theater

The future draft should make review theater visible:

- review happens after implementation is effectively committed;
- attendees cannot influence the outcome;
- slides hide the decision;
- only the chosen option is shown;
- missing evidence becomes action after approval;
- risks are acknowledged but not owned;
- approval signatures replace challenge;
- dissent disappears;
- decision owner is absent;
- unrelated decisions are bundled;
- outcome is not linked to ADR or RFC updates.

Do not create a new anti-pattern ID.

## 19. Boundary With Chapter 17

Chapter 17 owns ADR and RFC practice: artifact choice, content, status, closure, supersession, and discoverability.

Chapter 18 owns the review practice: timing before hardening, participants, challenge, disagreement, evidence requests,
outcomes, and closure of review comments.

Chapter 18 may use ADRs and RFCs as review inputs and outputs. It must not rewrite the artifact mechanics from Chapter
17 or turn Architecture Review into an RFC comment thread.

## 20. Boundary With Chapter 19

Chapter 19 owns Architecture Freeze, stability expectations, exception paths, revalidation, controlled learning after
Freeze, and how frozen architecture changes.

Chapter 18 may decide that a decision is not ready to freeze, must be reviewed again, needs more evidence, or should
not pass the next hardening point. It must not teach Freeze criteria, exception handling, revalidation policy, or
post-Freeze change control.

## 21. Boundaries With Earlier Chapters

Use earlier chapters as review lenses:

- Chapter 2 - decision quality under constraints;
- Chapter 4 - outcome ownership and closure;
- Chapters 5 and 13 - evidence and confidence;
- Chapter 7 - state ownership;
- Chapter 8 - API promises;
- Chapter 9 - dependency commitments;
- Chapter 14 - boundary placement;
- Chapter 15 - Change Radius;
- Chapter 16 - failure and recovery semantics.

Do not reteach those chapters. Chapter 18 should ask whether the current decision survives those lenses before it
hardens.

## 22. Boundaries With Later Parts

Part IV should retain product-line architecture, manufacturing and field workflows, observability implementation,
release discipline, upgrade systems, and the reference project.

Part V should retain organization-wide review culture, recurring rituals, mentoring, alignment, leadership, and
Architecture Health Review operation.

Part VI should retain legacy discovery, silent-coupling recovery, utility gravity, deletion, refactoring, and product
trust in legacy systems.

Chapter 18 may use examples touching these areas, but it must not take over their future depth.

## 23. Story

### Working Title

The Review That Could Only Approve

### System

Use an embedded product team changing a cross-boundary configuration or update architecture. The decision affects
firmware, gateway or host behavior, service tooling, manufacturing and test fixtures, support diagnostics,
compatibility, and release.

An RFC and possibly an ADR draft exist from Chapter 17-style practice.

### Trigger

Implementation begins before Architecture Review because the direction feels obvious. By review time, the firmware
branch compiles, a gateway adapter exists, tests encode the chosen boundary, service tool UI assumes the behavior,
manufacturing fixture changes have started, and release dates depend on the path.

Reviewers discover ambiguous validation authority, an old consumer relying on previous behavior, missing failure and
recovery semantics, weak compatibility evidence, underestimated rollback cost, Change Radius reaching service and
manufacturing paths, and unclear follow-up ownership.

Rejecting the decision now feels impossible.

### Inadequate Response

Tempting responses include approving and tracking concerns as follow-up tickets, adding reviewers next time, extending
the meeting, collecting signatures, updating ADR wording, asking for more tests after merge, splitting responsibility
across components, creating a standing board, or canceling reviews because they happen too late.

### Principal Engineer Intervention

The Principal Engineer frames the review around:

> What is still changeable, what has already hardened, and what evidence must exist before the next irreversible step?

The intervention separates hardened from open decisions, names the actual decision, names decision and affected owners,
maps enough Change Radius to identify participants, identifies missing evidence and whether it blocks commitment,
identifies boundary or ownership corrections before continuing, converts risks into owners, evidence requests, or
accepted risk, updates RFC or ADR records, defines follow-up points if evidence arrives later, and avoids shifting
accountability to the review.

## 24. Discussion Arc

1. The team used responsible artifacts but reviewed too late.
2. Review after hardening becomes approval theater.
3. Architecture Review names decision, owner, evidence, alternatives, and hardening point.
4. Participants follow affected architecture, not hierarchy.
5. Good review questions can change the decision.
6. Evidence and disagreement are assets when explicit.
7. Outcomes are broader than approve or reject.
8. Comments close into decisions, evidence requests, accepted risks, or artifacts.
9. ADRs and RFCs carry the record; Architecture Review is the challenge practice.
10. Review succeeds when it improves or bounds the decision before movement becomes expensive.

These are intellectual progression points, not mandatory manuscript headings.

## 25. Applicability

Architecture Review is most useful when a decision has cross-boundary effect, high Change Radius, expensive reversal,
persistent data, API or protocol changes, state ownership changes, dependency commitments, failure and recovery
implications, manufacturing or service impact, security, safety, or availability consequences, product-line
implications, long support horizon, or uncertainty needing challenge.

Not every design choice needs Architecture Review. A local, reversible, low-impact choice may need only code review or
Decision Journal capture.

## 26. Limits

The future draft must avoid dogmatism. It should not claim:

- every architecture decision needs a formal review meeting;
- review guarantees correctness;
- review is approval;
- review replaces ownership;
- consensus is always required;
- seniority determines correctness;
- all reviewers have veto;
- every concern blocks progress;
- more participants improve review;
- every missing evidence item means stop;
- Architecture Review replaces RFCs or ADRs;
- comments preserve the final decision;
- late review is always useless;
- a standing board is always good or always bad;
- one format works for all teams.

## 27. Violations

The future draft should make these violations visible:

- architecture review held only after implementation has encoded the choice;
- agenda names a project instead of a decision;
- affected owners are missing;
- decision owner is absent;
- facilitator becomes accidental approver;
- only the preferred option is shown;
- Change Radius excludes service, manufacturing, support, tests, or release surfaces;
- evidence gaps are converted into follow-up tickets after approval;
- disagreement disappears without a recorded outcome;
- risks are accepted without owner or trigger;
- review comments are never reflected in the RFC, ADR, Decision Journal, or Architecture Ledger;
- a standing board absorbs accountability that belongs to the decision owner.

## 28. Engineering Principle

Target principle for the future draft:

> Review architecture while the decision can still change. Name the decision, owner, evidence, alternatives, risks, and
> hardening point; then close the review into a decision, evidence request, accepted risk, or revised proposal.

The principle should imply these review questions:

1. What decision is hardening?
2. Who owns it?
3. Who is materially affected?
4. What would make the team choose differently?
5. Which boundary, state, API, dependency, failure path, or Change Radius changes?
6. Which evidence supports it?
7. Which evidence is missing?
8. Which alternatives remain real?
9. What risk is accepted?
10. What must change before the next irreversible step?
11. What artifact preserves the outcome?

The final manuscript may shorten this list for reader rhythm.

## 29. Exercise

### Working Title

Review One Decision Before It Hardens

Ask the reader to choose one pending architecture decision and document:

- decision statement;
- current decision state;
- next hardening point;
- decision owner;
- affected owners;
- RFC, ADR, or Decision Journal link;
- affected boundaries;
- affected state;
- affected APIs or protocols;
- dependency commitments;
- Change Radius estimate;
- evidence available;
- evidence missing;
- alternatives;
- non-goals;
- failure and recovery implications;
- compatibility implications;
- review participants;
- questions that could change the decision;
- possible outcomes;
- closure artifact;
- follow-up owner.

The exercise must end with:

1. one reviewable decision statement;
2. one named decision owner;
3. one hardening point;
4. one review outcome or evidence request.

Do not create a new canonical artifact.

## 30. ADR

### Working Title

Hold Architecture Review Before Configuration Protocol Hardening

### Context

- A configuration or update protocol decision affects firmware, gateway, service tool, manufacturing, tests, support,
  compatibility, and release.
- An RFC exists and an ADR draft may exist.
- Implementation has begun.
- Tests and tooling are starting to encode the preferred boundary.
- Affected owners have unresolved concerns.
- Rejection will soon become expensive.

### Decision

- Hold Architecture Review before the next irreversible implementation step.
- Review the actual protocol and ownership decision, not the whole project.
- Name the decision owner and affected owners.
- Use the RFC as review input.
- Review evidence, assumptions, alternatives, Change Radius, compatibility, failure and recovery, and owner boundaries.
- Classify findings as accepted changes, evidence requests, accepted risks, split decisions, or blockers.
- Update the RFC and final ADR with the outcome.
- Proceed only for parts whose assumptions survived review.
- Record follow-up owners and review triggers.

### Alternatives Considered

- Continue implementation and review later.
- Use code review only.
- Require Architecture Review for every related decision.
- Ask for more sign-offs without changing the decision.
- Move the decision to a standing board.
- Let RFC Friday handle architecture risk.
- Freeze the decision immediately and handle issues as exceptions.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits include preserving real alternatives, correcting ownership or boundary problems before the next hardening
point, making evidence gaps visible, routing review to affected owners, and leaving a durable RFC or ADR outcome.

Costs include review preparation, possible delay, explicit ownership of follow-up evidence, and the discomfort of
exposing sunk cost before it becomes irreversible.

The ADR must make a real architecture-process decision. It must not reduce to "schedule an architecture review."

## 31. PEAK Concept Map

### Concepts Inspected

- `RITUAL-001` - Architecture Review.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-006` - Architecture Ledger.
- `RITUAL-006` - RFC Friday.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-005` - Evidence Before Confidence.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `ANTIPATTERN-006` - Temporary Solution.
- `VOCAB-002` - Weak Signal.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-002` - Architecture Freeze.
- `RITUAL-004` - Architecture Health Review.
- `FAILURE-003` - The Successful Prototype.
- `FAILURE-005` - The Release We Should Have Delayed.

### Selected Concepts

- `RITUAL-001` - Architecture Review: material because the chapter directly teaches the ritual as structured challenge
  before decisions become expensive to change.
- `ARTIFACT-001` - ADR: material because accepted review outcomes and final decisions must be recorded in ADRs where
  architectural cost and future maintenance justify them.
- `ARTIFACT-002` - RFC: material because RFCs are common review inputs while proposals are still open.
- `ARTIFACT-003` - Decision Journal: material because smaller decisions, evidence requests, and bounded judgments may
  need lightweight closure without a full ADR.
- `ARTIFACT-006` - Architecture Ledger: material because active reviewed decisions need owner, status, related artifact,
  and review-trigger visibility.
- `RITUAL-006` - RFC Friday: material because lightweight RFC review may feed or precede Architecture Review but does
  not replace it.
- `LAW-001` - Every State Has One Owner: material because Architecture Review examines state authority and transition
  ownership before the decision hardens.
- `LAW-002` - Every API Is a Promise: material because API and protocol promises are common review subjects and
  compatibility risks.
- `LAW-005` - Evidence Before Confidence: material because review separates evidence, assumptions, uncertainty, and
  accepted risk.
- `LAW-007` - Every Dependency Is a Decision: material because dependency commitments and replacement cost often define
  what is hardening.
- `VOCAB-001` - Change Radius: material because the review uses affected surface to find participants and consequences.
- `METRIC-001` - Change Radius: material because the review estimates how much system surface must change, be reviewed,
  or be retested.
- `METRIC-003` - Discoverability: material because the review outcome must be findable from the system surface, owner,
  or record it affects.

### Rejected Concepts

- `SMELL-001` - Silent Coupling: useful as a possible finding, but the chapter is about the review practice rather than
  diagnosing the smell.
- `SMELL-004` - Hidden State: useful as a possible review finding, but the state-ownership law is the stronger selected
  concept.
- `SMELL-005` - Platform Leakage: useful in embedded examples, but Chapter 14 owns the boundary-leakage practice.
- `ANTIPATTERN-006` - Temporary Solution: review may prevent unowned follow-up work from becoming permanent, but the
  anti-pattern is not central enough for an outgoing edge.
- `VOCAB-002` and `ARTIFACT-007` - Weak Signal and Weak Signal Register: review may use weak signals as evidence, but
  Chapters 5 and 13 own weak-signal treatment.
- `RITUAL-002` - Architecture Freeze: explicitly reserved for Chapter 19.
- `RITUAL-004` - Architecture Health Review: later parts own recurring health-review operation.
- `FAILURE-003` - The Successful Prototype: related to implementation hardening, but the Chapter 18 story is not the
  prototype failure story.
- `FAILURE-005` - The Release We Should Have Delayed: related to release risk, but Chapter 18 must not become a release
  readiness chapter.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as hardening point, review subject, review input, review theater, decision readiness, blocker, accepted risk,
and follow-up owner remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-018` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-018
  type: illustrates
  to: RITUAL-001

- from: CHAPTER-018
  type: references
  to: ARTIFACT-001

- from: CHAPTER-018
  type: references
  to: ARTIFACT-002

- from: CHAPTER-018
  type: references
  to: ARTIFACT-003

- from: CHAPTER-018
  type: references
  to: ARTIFACT-006

- from: CHAPTER-018
  type: references
  to: RITUAL-006

- from: CHAPTER-018
  type: references
  to: LAW-001

- from: CHAPTER-018
  type: references
  to: LAW-002

- from: CHAPTER-018
  type: references
  to: LAW-005

- from: CHAPTER-018
  type: references
  to: LAW-007

- from: CHAPTER-018
  type: references
  to: VOCAB-001

- from: CHAPTER-018
  type: references
  to: METRIC-001

- from: CHAPTER-018
  type: references
  to: METRIC-003
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 32. Reader-Facing Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 18 role:

- Opening Quote: establish that review is useful only while the decision can still change.
- Story: show a team reviewing a cross-boundary decision after implementation has begun to harden it.
- Discussion: teach hardening points, review subject, participants, evidence, disagreement, outcomes, closure, and
  review theater.
- Engineering Principle: anchor Architecture Review before hardening as a principal engineering practice.
- Architecture Exercise: review one decision before it hardens.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local decision to hold Architecture Review before configuration protocol hardening.
- Editor's Commentary: explain how Chapter 18 follows ADR/RFC practice and precedes Architecture Freeze.

## 33. Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- Review is useful only while the decision can still change.
- A concern without an owner becomes decoration.
- Approval is weaker than a recorded outcome.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 34. Technical Requirements

The future draft must treat the following accurately:

- architecture decisions hardening through code, tests, tools, data formats, release plans, and organizational
  commitments;
- review timing;
- decision owner versus facilitator versus reviewer;
- affected owners across firmware, gateway, service tool, manufacturing, test, support, and release;
- RFC and ADR inputs without duplicating Chapter 17;
- evidence versus assumptions;
- real alternatives;
- compatibility and migration concerns;
- failure and recovery concerns;
- Change Radius enough to scope participants;
- review outcomes;
- accepted risk;
- follow-up ownership;
- links to decision records.

Do not require a specific meeting format, board, Git platform, issue tracker, template, organization size, approval
system, MCU, RTOS, protocol, cloud service, or process tool.

## 35. Terminology

Use terms precisely:

- Architecture Review: a structured challenge to a consequential architectural decision before it becomes expensive to
  change;
- hardening: the point where code, tests, tools, data, release commitments, compatibility promises, or sunk cost make
  alternatives expensive or fake;
- review subject: the actual decision under review, not the project or meeting topic;
- decision owner: the person accountable for the decision outcome and its record;
- proposal owner: the person carrying the proposal through review, if different;
- reviewer: a participant selected because they own affected surface or relevant expertise;
- facilitator: a person helping the review close without becoming the decision owner by accident;
- accepted risk: a named risk the decision owner accepts with owner, evidence, and review trigger;
- blocker: an unresolved issue that prevents the next hardening step;
- evidence request: a review outcome asking for specific evidence that could change the decision;
- review theater: a review that performs challenge after the decision can no longer meaningfully change.

The chapter must avoid these misleading statements:

- Architecture Review means approval;
- a senior committee guarantees architecture quality;
- consensus proves correctness;
- more reviewers automatically improve review;
- missing evidence always blocks progress;
- code review is always enough;
- RFC Friday is the same as Architecture Review;
- a signed review replaces ownership;
- comments are the final record;
- late review is always useless.

## 36. Failure Modes to Avoid

The later draft must not become:

- Chapter 17 repeated;
- Chapter 19 written early;
- a governance-board chapter;
- a meeting facilitation guide;
- a generic checklist;
- a slide-review critique with no architecture substance;
- an approval workflow;
- a release-gate chapter;
- a code-review chapter;
- an organization design chapter;
- a new PEAK artifact proposal;
- reader-facing draft prose inside the canonical brief.

## 37. Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete embedded architecture decision reviewed after implementation begins to harden it;
- the Principal Engineer move frames the issue from approval to "what is still changeable before the next irreversible
  step";
- no primary PEAK concept is assigned unless a later author/editor decision changes repository convention;
- `RITUAL-001` is materially present as the central practice;
- review is not treated as approval, committee ceremony, slide review, or replacement for ownership;
- the manuscript distinguishes too-early, useful, and too-late review timing;
- review participants follow affected architecture, not hierarchy;
- evidence, assumptions, alternatives, risks, accepted risks, blockers, and follow-up owners are distinct;
- outcomes are broader than approve or reject;
- review comments close into decisions, evidence requests, accepted risks, or artifacts;
- Chapter 17 remains the ADR/RFC practice chapter;
- Chapter 19 remains the Architecture Freeze chapter;
- the exercise ends with one reviewable decision statement, one named decision owner, one hardening point, and one
  review outcome or evidence request;
- the ADR makes a genuine story-local architecture-process decision;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 38. Review Handoff

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into artifact mechanics, generic meeting process, governance theater, release gates, or
Architecture Freeze.

Canon Review should verify that Chapter 18 remains a Part III practice chapter with no forced primary concept,
materially illustrates `RITUAL-001`, preserves the registered relationship set, does not imply a new review artifact or
board concept, and preserves the boundaries with Chapters 17 and 19.

Technical Review should focus on realistic hardening points, affected owners, evidence gaps, compatibility and migration
concerns, failure and recovery implications, Change Radius, accepted risks, decision ownership, and credible review
outcomes.

Freeze Review should confirm that Chapter 18 remains the fifth Part III practice chapter, keeps the manuscript
architecture intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and
leaves the reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
configuration protocol, affected owners, review sequence, hardening point, and final notebook wording while preserving
the Architecture Review thesis, story shape, PEAK map, and chapter boundaries.
