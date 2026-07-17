# CHAPTER-026 Canonical Brief: Technical Leadership Without Authority

## 1. Metadata

- Stable ID: `CHAPTER-026`.
- Title: `Technical Leadership Without Authority`.
- Part: Part V - Engineering Organization.
- Chapter number: 26.
- Expected manuscript path: `book/05-engineering-organization/26-technical-leadership-without-authority.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-026-technical-leadership-without-authority.md`.
- Branch: `chapter26`.
- Verified baseline `origin/main`: `3e6f5126b6817c93c11571b6881fcea3ceead348`.
- Baseline evidence: PR #27 squash commit,
  `Chapter 25: Reference Project Walkthrough (#27)`.
- Chapter 25 feature Freeze commit checked for tree equivalence:
  `e4117e3597530cf90c66bddbb8a7a49ee21f0287`.
- Canonical predecessor: `CHAPTER-025` - Reference Project Walkthrough.
- Part position: first chapter of Part V - Engineering Organization.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 26 opens an organizational part by applying existing decision, evidence, ownership,
  and record concepts; it should be carried by a relationship set rather than a new primary-concept field.
- Central chapter-local practice: improving cross-team technical decision quality without taking decision ownership
  away from the accountable owners.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `3e6f5126b6817c93c11571b6881fcea3ceead348`.
- That baseline is the PR #27 squash commit,
  `Chapter 25: Reference Project Walkthrough (#27)`.
- The squash commit has parent `56c90ec7cfec4e7fe0d839b0f89d8ce8825d2268` and is an ancestor of current
  `origin/main`.
- The Chapter 25 feature-branch Freeze commit `e4117e3597530cf90c66bddbb8a7a49ee21f0287` remains tree-equivalent for
  the checked Chapter 25 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-025` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-025` is the sixth and final Part IV chapter and is canonical.
- The table of contents places `Technical Leadership Without Authority` first in Part V - Engineering Organization.
- `book/05-engineering-organization/README.md` exists and remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-026` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 26 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter26` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part V Role

Chapter 26 opens Part V by shifting the book from product architecture to engineering organization. The shift is not
from technical work to generic leadership advice. It is from making good architecture decisions to helping an
organization make, carry, challenge, and revisit those decisions when the Principal Engineer does not control the
people, roadmap, or reporting lines.

The chapter should establish the operating frame for Part V:

- Principal Engineers lead through decision quality, not command authority.
- Influence should make the right technical decision easier to see, trust, and carry.
- Trust grows when a Principal Engineer clarifies questions, evidence, trade-offs, ownership, and records.
- Technical authority must not become hidden control.
- Organizational leadership is strongest when the decision owner remains visible.

Chapter 26 should prepare later Part V chapters without writing them early.

## 4. Canonical Purpose

Prepare Chapter 26 to teach technical leadership without formal authority as organizational leverage over technical
decision quality.

Candidate thesis for the future manuscript:

> Technical leadership without authority is the practice of making the right decision easier for the organization to
> see, trust, and carry.

The chapter should move the reader away from treating leadership as title power, argument-winning, personality
performance, command-and-control, consensus at any cost, or heroic rescue.

The core question should become:

> How do I help the organization make and sustain better technical decisions when I do not control the people, roadmap,
> or reporting lines?

The chapter should use earlier canon as applied leadership tools. It should not repeat the teachings of Parts I through
IV.

## 5. Primary-Concept Resolution

Chapter 26 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Chapter 26 should be
carried by material relationships to existing concepts around ownership, evidence, Change Radius, decision records,
Architecture Review, discoverability, and hidden decision ownership.

Do not create PEAK concepts such as Technical Leadership, Influence Without Authority, Decision Owner, Hidden Owner,
Trust, Stewardship, Organizational Memory, Escalation, Facilitation, Alignment, or Decision System. These terms may
appear as chapter-local prose when needed, but they must not become new stable IDs.

## 6. Central Thesis

Technical leadership without formal authority means improving the decision before, during, and after the moment of
choice. The Principal Engineer helps the organization state the real decision, name who owns the consequences, surface
constraints and trade-offs, gather evidence, choose the right forum, recommend with precision, and leave behind records that
others can use.

Approved supporting formulation for the reader-facing draft:

> Lead by improving the decision, not by taking the decision away.

This formulation is chapter-level language. Do not register it as new canon.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. Technical leadership means being the most senior person in the room.
2. Influence means persuading people to accept the Principal Engineer's preferred answer.
3. A Principal Engineer should decide when teams disagree.
4. Avoiding formal authority means avoiding accountability.
5. A strong recommendation requires taking ownership of the decision.
6. Meetings, RFCs, ADRs, and reviews are process around the real work.
7. Escalation is either failure or the fastest way to make progress.

By the end of the chapter, the reader should be able to:

1. state the technical decision without taking it over;
2. distinguish recommendation, facilitation, decision ownership, formal approval, and escalation;
3. identify the accountable decision owner and affected owners;
4. separate evidence from preference;
5. map Change Radius for a cross-team technical decision;
6. choose whether an RFC, Architecture Review, ADR, Decision Journal entry, or Architecture Ledger row is appropriate;
7. recommend a direction while preserving ownership by the team that will carry the consequences;
8. escalate only when authority is genuinely required;
9. avoid becoming the hidden owner every decision waits for.

## 8. Technical Leadership Scope

Chapter 26 defines technical leadership as leverage over organizational decision quality.

It may include:

- clarifying the real technical question;
- surfacing constraints, trade-offs, and fixed requirements;
- asking better engineering questions;
- making evidence visible;
- naming owners and affected owners;
- mapping Change Radius;
- distinguishing reversible, hard-to-reverse, and authority-required decisions;
- creating records people can reuse;
- facilitating review without taking over;
- making risks and unknowns explicit;
- helping teams align around a decision after the owner decides;
- protecting long-term system health without becoming a gatekeeper.

It must remain technical. The chapter should not become a management handbook, promotion guide, politics chapter,
persuasion tricks chapter, meeting-facilitation tutorial, communication-skills essay, personality advice, or generic
leadership motivational chapter.

## 9. Authority Boundary

The reader-facing chapter must distinguish these ideas:

- formal authority: the role power to assign people, schedule work, approve scope, or make organizational trade-offs;
- technical authority: earned trust in technical judgment, evidence, and consequences;
- trust: confidence created by useful judgment and reliable follow-through;
- credibility: the right to be heard because prior recommendations were grounded and honest;
- ownership: accountability for carrying consequences after the decision;
- advisory influence: helping the owner see the decision with better precision;
- facilitation: improving the decision forum without becoming the owner;
- escalation: asking formal authority to decide or unblock what technical influence cannot own;
- veto power: an explicit organizational role, not a default property of seniority;
- stewardship: preserving long-term system health through clarity, evidence, and records.

Influence must not become hidden control. A Principal Engineer may recommend, challenge, clarify, and escalate. They
must not silently make decisions for teams that must own the outcome.

## 10. Decision Ownership and Influence

The chapter should make one distinction unavoidable:

> Influence is not ownership.

A Principal Engineer can improve the decision while another owner remains accountable for it. The manuscript should
show how to recommend strongly without making the accountable owner invisible.

Healthy influence should:

- clarify what decision is actually being made;
- name who owns consequences;
- identify who must be consulted because they inherit cost;
- expose which constraints are real;
- separate evidence, assumptions, preferences, and authority limits;
- make the recommendation explicit;
- name the record or forum that preserves the reasoning;
- define follow-up and revisit triggers.

Unhealthy influence should be shown as:

- making decisions for teams that must carry consequences;
- using architecture as a veto weapon;
- collecting informal power without responsibility;
- replacing management with technical seniority;
- avoiding conflict under the label of influence;
- escalating before the technical question is clear;
- delaying escalation when only formal authority can decide;
- becoming the person every decision waits for.

## 11. In-Scope and Out-of-Scope

### In Scope

Chapter 26 covers:

- technical leadership without direct reporting authority;
- cross-team architecture decisions;
- decision quality as the main leadership lever;
- ownership, accountability, evidence, constraints, trade-offs, Change Radius, and records;
- recommendation without hidden ownership;
- RFC and Architecture Review as forums for broad technical decisions;
- ADR, Decision Journal, and Architecture Ledger as records after ownership is clear;
- escalation as a bounded tool;
- trust created by clarity, evidence, service to the system, and reliable follow-through;
- risks of heroic rescue, gatekeeper behavior, and hidden decision ownership.

### Explicitly Out of Scope

Do not turn Chapter 26 into:

- a people-management chapter;
- a promotion or career-ladder guide;
- a politics chapter;
- a charisma, persuasion, or personality chapter;
- a meeting-facilitation tutorial;
- a generic communication-skills essay;
- a consensus-building recipe;
- an early design-review chapter;
- an early rituals chapter;
- an early mentoring chapter;
- an early alignment chapter;
- an early Architecture Health Review chapter;
- a new PEAK concept proposal.

## 12. Recommended Engineering-Organization Story

### Working Title

`The Decision Nobody Owned`

### Starting System

A product team is preparing a risky cross-team provisioning change. The change touches firmware, backend, manufacturing,
service tooling, support, and release. The Principal Engineer has no direct authority over those teams.

### Symptoms

- Product wants a date.
- Firmware wants a clean technical design.
- Backend wants stable API assumptions.
- Manufacturing wants provisioning clarity.
- Service tooling wants a predictable workflow.
- Support wants diagnostic meaning.
- Release wants a low-risk path.
- Managers want progress but do not own the full technical trade-off.
- Each team optimizes locally.
- Engineers ask the Principal Engineer to decide.
- The Principal Engineer is tempted to become the hidden decision-maker.

### Initial Question

> Can you tell everyone what architecture we should use?

### Principal Engineer Intervention

Frame the question again:

> What decision are we making, who owns it, what evidence would make it responsible, and what must stay true after we
> decide?

The Principal Engineer should:

- clarify the decision type and reversibility;
- map affected owners and Change Radius;
- identify constraints and fixed requirements;
- separate evidence from preference;
- surface risks and unknowns;
- recommend an RFC or Architecture Review for broad ownership;
- use an ADR or Decision Journal only after ownership is clear;
- make a recommendation without stealing decision ownership;
- define follow-up and revisit triggers;
- escalate only where formal authority is actually required.

The story should show influence through decision quality, not charisma.

## 13. Expected Discussion Arc

1. Part V starts where product decisions become organizational memory.
2. Technical leadership without authority is not weak leadership; it is leadership through decision quality.
3. Formal authority, technical authority, recommendation, facilitation, ownership, and escalation are different tools.
4. The Principal Engineer's first move is to clarify the decision, not to give an answer.
5. Cross-team decisions need visible owners, affected owners, evidence, and Change Radius.
6. Trust grows when recommendations are explicit, grounded, and do not erase the accountable owner.
7. Records and forums help the organization carry decisions without relying on one person.
8. Hidden ownership, heroic rescue, and gatekeeper behavior are leadership failures even when the technical answer is
   good.
9. Escalation is appropriate when the decision requires formal authority, not when the technical question is merely hard.
10. The chapter closes by leaving Part V's later practices visible but unwritten.

These are intellectual progression points, not mandatory manuscript headings.

## 14. Boundaries With Later Part V Chapters

Chapter 26 opens the organizational frame. It must not consume the later Part V chapters.

- Chapter 27 owns design reviews as shared memory.
- Chapter 28 owns building engineering rituals.
- Chapter 29 owns mentoring through artifacts.
- Chapter 30 owns aligning teams around decisions.
- Chapter 31 owns architecture health reviews.

Chapter 26 may preview reviews, rituals, mentoring, alignment, and health reviews as future supports for technical
leadership. It should not teach their full practice.

## 15. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating them:

- Part I supplies the Principal Engineer role, better questions, ownership beyond code, evidence, and leaving systems
  better.
- Part II supplies state ownership, API promises, dependency decisions, and evidence discipline.
- Part III supplies Change Radius, ADRs, RFCs, Architecture Review, and freeze as decision tools.
- Part IV supplies the idea that product decisions become shared memory and obligations.

The future manuscript should show these tools becoming leadership without authority. It should not reteach Parts I
through IV.

## 16. Applicability

Chapter 26 is most useful when:

- a technical decision crosses team or ownership boundaries;
- no one person has authority over every affected surface;
- the team is asking the Principal Engineer to decide because seniority feels faster than ownership clarity;
- managers and product owners need technical framing but cannot supply it alone;
- decision records are scattered across memory, meetings, issue comments, and drafts;
- a recommendation is needed before all uncertainty is gone;
- escalation may be needed but the technical question is not yet clear enough.

Not every decision needs an RFC, Architecture Review, ADR, Decision Journal entry, or ledger row. The chapter should
teach proportionality.

## 17. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- formal authority is bad;
- managers are irrelevant;
- Principal Engineers should never decide;
- influence means consensus;
- influence means persuasion tricks;
- leadership without authority means avoiding accountability;
- technical correctness is enough;
- every decision needs a formal review;
- every disagreement needs escalation;
- a record replaces conversation;
- trust comes from charisma;
- the Principal Engineer must always remain neutral.

Sometimes the Principal Engineer is the explicit decision owner. Sometimes escalation is necessary. Sometimes a manager
or product owner must decide a priority or staffing trade-off. Sometimes speed requires a small reversible decision with
a Decision Journal entry instead of a full review. The chapter should teach how to tell those cases apart.

## 18. Violation Patterns

The future draft should make these violations visible:

- the Principal Engineer becomes the hidden owner of a cross-team decision;
- each team optimizes locally while the shared decision remains unnamed;
- product date pressure substitutes for a technical decision;
- recommendation is presented as neutral facilitation;
- authority is avoided when authority is actually required;
- escalation happens before the technical decision is clear;
- architecture review becomes a veto mechanism;
- an RFC is used as approval theater after the decision has hardened;
- an ADR records a decision before the accountable owner is known;
- a temporary workaround survives without owner, evidence, or revisit trigger;
- teams depend on private memory instead of shared records;
- future decisions wait for the same expert because the prior decision was never made discoverable.

Do not create a new anti-pattern ID.

## 19. Engineering Principle Target

Target principle for the future draft:

> Lead by improving the decision, not by taking the decision away. Clarify the question, name the owners, expose the
> trade-offs, gather the evidence, and leave behind a record the organization can carry.

The principle should imply these questions:

1. What decision is actually being made?
2. Who owns the consequences?
3. Who must be consulted because they will inherit the cost?
4. What evidence would make this decision responsible?
5. Which constraints are real?
6. Which preferences are being treated as facts?
7. What is reversible?
8. What is hard to reverse?
9. What is the Change Radius?
10. What record will help future teams?
11. What escalation is required, and what escalation would be avoidance?
12. How can I recommend without becoming the hidden owner?

The final manuscript may shorten the list for reader rhythm.

## 20. Architecture Exercise Target

### Working Title

`Lead One Decision Without Taking It Over`

Ask the reader to choose one current cross-team technical decision and document:

- actual decision;
- decision owner;
- affected owners;
- constraints;
- trade-offs;
- evidence available;
- evidence missing;
- reversibility;
- Change Radius;
- recommended forum or artifact;
- recommendation;
- what the Principal Engineer must not own;
- escalation condition;
- revisit trigger.

End with five outputs:

1. one clarified decision statement;
2. one decision owner;
3. one evidence gap;
4. one recommendation;
5. one record or forum.

Do not create a new canonical artifact for this exercise.

## 21. Chapter-Local ADR Brief

### Working Title

Use an RFC and Architecture Review for the Cross-Team Provisioning Change

### Context

- A risky cross-team provisioning change affects firmware, backend, manufacturing, service tooling, support, and
  release.
- No single team owns the entire technical consequence.
- The Principal Engineer has influence but not formal authority.
- Teams are optimizing locally and asking the Principal Engineer to decide.
- Managers and product owners need progress, but the technical ownership boundary is unclear.

### Decision

- Do not let the Principal Engineer become the hidden owner.
- Identify the accountable decision owner and affected owners.
- Run an RFC to surface constraints, options, evidence, non-goals, and open questions.
- Hold Architecture Review because the Change Radius crosses several ownership boundaries.
- Record the final architecture decision in an ADR when ownership is clear.
- Use Decision Journal entries for smaller follow-ups, evidence gaps, and revisit triggers.
- Add an Architecture Ledger row if the decision remains active and discoverability matters.
- Escalate only if organizational authority is required to resolve scope, staffing, priority, or accountability.

### Alternatives Considered

- Principal Engineer decides informally.
- Manager decides by date pressure.
- Each team proceeds locally.
- Defer until consensus emerges.
- Hold repeated meetings without a record.
- Escalate immediately without clarifying the technical decision.

### Consequences

Benefits include stronger ownership, clearer accountability, better evidence, reduced hidden authority, a better review
forum, and records future teams can trust.

Costs include slower initial framing, visible disagreement, more explicit ownership work, and the discipline to keep
the Principal Engineer's recommendation from becoming hidden approval.

The ADR must make a real story-local architecture decision. It must not reduce to "be a better leader" or "use an RFC
for everything."

## 22. PEAK Concept Map

### Concepts Inspected

- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `VOCAB-003` - Decision Journal.
- `VOCAB-006` - Architecture Freeze.
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
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.
- `RITUAL-004` - Architecture Health Review.
- `RITUAL-006` - RFC Friday.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-004` - Manager Mania.
- `ANTIPATTERN-006` - Temporary Solution.
- `FAILURE-004` - The Hero Engineer.

### Selected Concepts

- `FAILURE-004` - The Hero Engineer: material because the chapter warns against making the Principal Engineer the
  person every difficult decision waits for.
- `LAW-001` - Every State Has One Owner: material because the story turns on naming the owner of the decision and the
  consequences rather than letting ownership drift into seniority.
- `LAW-002` - Every API Is a Promise: material because the cross-team provisioning change includes backend and service
  assumptions whose observable behavior becomes a promise.
- `LAW-005` - Evidence Before Confidence: material because influence should separate evidence from preference and make
  responsible confidence visible.
- `LAW-007` - Every Dependency Is a Decision: material because the cross-team change imports dependencies across
  firmware, backend, manufacturing, support, and release.
- `VOCAB-001` - Change Radius: material because the Principal Engineer maps affected surface before selecting forum,
  owners, and evidence.
- `METRIC-001` - Change Radius: material because the decision should estimate affected firmware, backend,
  manufacturing, service, support, and release surfaces.
- `METRIC-002` - Bus Factor: material because hidden authority and private memory make the organization depend on one
  expert.
- `METRIC-003` - Discoverability: material because leadership leaves records that future teams can find without
  needing the original Principal Engineer in the room.
- `ARTIFACT-001` - ADR: material because the final accepted cross-team architecture decision needs durable reasoning
  after ownership is clear.
- `ARTIFACT-002` - RFC: material because the proposal needs review before broad ownership hardens.
- `ARTIFACT-003` - Decision Journal: material because smaller follow-ups, evidence gaps, and revisit triggers need
  lightweight records.
- `ARTIFACT-006` - Architecture Ledger: material because active decisions, owners, related records, and review dates
  should remain findable.
- `RITUAL-001` - Architecture Review: material because the broad Change Radius requires structured challenge before
  implementation hardens the decision.
- `SMELL-001` - Silent Coupling: material because local team assumptions can create hidden dependencies when no shared
  decision is named.
- `SMELL-004` - Hidden State: material because hidden decision ownership affects behavior without a clear owner,
  interface, or model.
- `ANTIPATTERN-006` - Temporary Solution: material because local workarounds and informal decisions need owners,
  expiration conditions, or explicit records.

### Rejected Concepts

- `LAW-003`: time may matter to release sequencing, but Chapter 26 is not a timing-dependency chapter.
- `LAW-004` and `LAW-006`: simplicity and unused flexibility may appear as background judgment, but they are not the
  organizing leadership mechanism.
- `VOCAB-003`: relevant through `ARTIFACT-003`, but the vocabulary edge is unnecessary when the artifact is the material
  record.
- `VOCAB-006` and `RITUAL-002`: Architecture Freeze is a later stability tool, not central to Chapter 26.
- `VOCAB-007`, `METRIC-005`, and `RITUAL-004`: Architecture Health and Architecture Health Review belong to Chapter
  31.
- `METRIC-004`: API Stability is relevant to backend assumptions, but Chapter 8 owns the metric and Chapter 26 should
  not over-connect to it.
- `ARTIFACT-004` and `ARTIFACT-007`: Mistake Ledger and Weak Signal Register are useful in later evidence or learning
  cases, but the Chapter 26 story does not require them.
- `RITUAL-006`: RFC Friday may be a useful lightweight forum, but Chapter 28 owns rituals and Chapter 26 should not
  teach ritual design early.
- `SMELL-005`: platform leakage may appear in the technical change, but the organizational lesson is ownership and
  decision quality, not platform vocabulary.
- `ANTIPATTERN-003`: global configuration is nearby if provisioning becomes a broad flag, but it is not the main
  failure mode.
- `ANTIPATTERN-004`: Manager Mania is about generic technical manager objects, not formal management authority.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as technical leadership, influence without authority, hidden owner, stewardship, escalation, facilitation,
alignment, trust, organizational memory, and decision system remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-026` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-026
  type: illustrates
  to: FAILURE-004

- from: CHAPTER-026
  type: references
  to: LAW-001

- from: CHAPTER-026
  type: references
  to: LAW-002

- from: CHAPTER-026
  type: references
  to: LAW-005

- from: CHAPTER-026
  type: references
  to: LAW-007

- from: CHAPTER-026
  type: references
  to: VOCAB-001

- from: CHAPTER-026
  type: references
  to: METRIC-001

- from: CHAPTER-026
  type: references
  to: METRIC-002

- from: CHAPTER-026
  type: references
  to: METRIC-003

- from: CHAPTER-026
  type: references
  to: ARTIFACT-001

- from: CHAPTER-026
  type: references
  to: ARTIFACT-002

- from: CHAPTER-026
  type: references
  to: ARTIFACT-003

- from: CHAPTER-026
  type: references
  to: ARTIFACT-006

- from: CHAPTER-026
  type: references
  to: RITUAL-001

- from: CHAPTER-026
  type: references
  to: SMELL-001

- from: CHAPTER-026
  type: references
  to: SMELL-004

- from: CHAPTER-026
  type: references
  to: ANTIPATTERN-006
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 23. Required Reader-Facing Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 26 role:

- Opening Quote: establish that influence should improve the decision system, not hide ownership.
- Story: show The Decision Nobody Owned and the Principal Engineer's intervention.
- Discussion: distinguish authority, influence, ownership, evidence, records, and escalation.
- Engineering Principle: lead by improving the decision without taking it away.
- Architecture Exercise: lead one decision without taking it over.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local cross-team provisioning decision process.
- Editor's Commentary: explain how Chapter 26 opens Part V and uses earlier canon as organizational practice.

## 24. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- Influence is not ownership.
- The best technical leaders improve the decision system.
- A recommendation is stronger when the owner remains visible.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 25. Technical and Organizational Credibility Requirements

The future draft must treat the following accurately:

- Principal Engineer influence without direct management authority;
- distinction between recommendation, facilitation, decision ownership, and formal approval;
- cross-team technical decisions with real ownership consequences;
- managers and product owners as legitimate partners;
- technical credibility based on evidence, clarity, and follow-through;
- disagreement as expected engineering work;
- trust as earned through useful judgment and reliable records;
- RFCs, ADRs, Decision Journal entries, Architecture Review, and Architecture Ledger as aids, not paperwork;
- escalation as a tool, not a habit;
- risks of hidden ownership, gatekeeper behavior, veto behavior, and heroic rescue.

Avoid misleading claims:

- authority is bad;
- technical correctness is enough;
- every decision needs a formal review;
- every disagreement needs escalation;
- a record replaces conversation;
- charisma is the leadership mechanism.

## 26. Terminology and Precision Guardrails

Use terms precisely:

- Technical leadership: improving technical decision quality and system stewardship, not managing people by another
  name.
- Formal authority: explicit organizational decision power.
- Technical authority: earned trust in technical judgment and evidence.
- Decision owner: the accountable owner of consequences after the decision.
- Affected owner: a team or role that inherits cost, constraints, or operational consequences.
- Recommendation: a clear technical judgment offered to the owner, not hidden approval.
- Facilitation: improving the decision forum, not controlling the outcome invisibly.
- Escalation: bringing in formal authority when the decision requires it.
- Hidden owner: chapter-local prose for an unofficial decision-maker; do not register it as a PEAK concept.

Avoid misleading statements:

- influence means consensus;
- leadership without authority means staying neutral;
- seniority grants veto power;
- the loudest expert owns the architecture;
- RFCs and reviews make ownership unnecessary;
- managers are obstacles to technical leadership;
- teams should outsource hard decisions to the Principal Engineer.

## 27. Failure Modes to Avoid

The later draft must not become:

- a management handbook chapter;
- a promotion or career-ladder chapter;
- a persuasion or politics chapter;
- a motivational leadership essay;
- a generic communication-skills chapter;
- a design-review chapter written early;
- an engineering-rituals chapter written early;
- a mentoring-through-artifacts chapter written early;
- an alignment-around-decisions chapter written early;
- an Architecture Health Review chapter written early;
- a retelling of Parts I through IV;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 28. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the chapter opens Part V and keeps the subject technical;
- the story uses a risky cross-team technical decision involving firmware, backend, manufacturing, service tooling,
  support, and release or an equivalent credible system;
- the Principal Engineer has influence but no direct authority over the teams;
- the story shows local optimization, unclear ownership, evidence gaps, and pressure for the Principal Engineer to
  decide;
- the Principal Engineer improves the decision by clarifying the question, owner, evidence, constraints, Change Radius,
  forum, record, follow-up, revisit trigger, and escalation condition;
- the Principal Engineer makes a recommendation without becoming hidden owner;
- the chapter distinguishes formal authority, technical authority, trust, ownership, recommendation, facilitation,
  escalation, veto power, and stewardship;
- RFC, Architecture Review, ADR, Decision Journal, and Architecture Ledger appear only where proportionate;
- managers and product owners are treated as legitimate partners;
- escalation is neither demonized nor used as a reflex;
- selected PEAK concepts are materially present if the registered relationship set is kept;
- no primary PEAK concept is assigned unless a later editor decision changes repository convention;
- no new PEAK concept is implied accidentally;
- the exercise ends with one clarified decision statement, one decision owner, one evidence gap, one recommendation, and
  one record or forum;
- the ADR makes a genuine story-local decision about the cross-team provisioning change;
- exactly three Principal's Notebook observations are present;
- later Part V chapters are previewed only lightly and not written early.

## 29. Review Handoff Notes

Editorial Review should check whether the chapter stays alive as a technical leadership story rather than becoming a
generic leadership essay. It should also check that the Principal Engineer's recommendation is strong, specific, and not
hidden ownership.

Canon Review should verify that Chapter 26 remains no-primary, preserves only material outgoing relationships, avoids
new PEAK concepts, and keeps technical leadership without authority as chapter-local prose carried by existing PEAK
concepts.

Technical Review should focus on realistic cross-team engineering organization dynamics: authority boundaries,
decision ownership, evidence, Change Radius, API and dependency assumptions, RFC/ADR/review usage, escalation, trust,
and avoidance of hidden owners.

Freeze Review should confirm that Chapter 26 is the first Part V chapter, keeps the manuscript architecture intact,
uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and does not write later Part
V chapters early.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
cross-team change, team names, recommendation, forum choice, record choice, escalation condition, ADR wording, and
notebook wording while preserving the Part V opening role, PEAK map, and chapter boundaries.
