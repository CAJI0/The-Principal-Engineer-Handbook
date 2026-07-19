# CHAPTER-028 Canonical Brief: Building Engineering Rituals

## 1. Metadata

- Stable ID: `CHAPTER-028`.
- Title: `Building Engineering Rituals`.
- Part: Part V - Engineering Organization.
- Chapter number: 28.
- Expected manuscript path: `book/05-engineering-organization/28-building-engineering-rituals.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-028-building-engineering-rituals.md`.
- Branch: `chapter28`.
- Verified baseline `origin/main`: `e83ade929a78be2361b73da88a623f9f19ae14fb`.
- Baseline evidence: PR #29 Chapter 27 squash merge commit.
- Chapter 27 feature Freeze commit checked for tree equivalence:
  `f812ea7c6b8801929dbe98b3af327e0521753bcf`.
- Canonical predecessor: `CHAPTER-027` - Design Reviews as Shared Memory.
- Part position: third chapter of Part V - Engineering Organization.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 28 applies existing ritual, record, evidence, ownership, Change Radius, and
  Discoverability concepts to repeated engineering practices; it should be carried by relationships rather than by a
  new primary-concept field.
- Central chapter-local practice: designing and maintaining engineering rituals around technical behaviors rather than
  meetings, ceremonies, or calendar slots.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `e83ade929a78be2361b73da88a623f9f19ae14fb`.
- That baseline is the PR #29 Chapter 27 squash merge commit.
- The squash commit has parent `80332c17999d685e994e9bc8e1fa703ce4740231` and is an ancestor of current
  `origin/main`.
- The Chapter 27 feature-branch Freeze commit `f812ea7c6b8801929dbe98b3af327e0521753bcf` remains tree-equivalent for
  the checked Chapter 27 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-027` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-027` is the second Part V chapter and is canonical.
- The table of contents places `Building Engineering Rituals` third in Part V - Engineering Organization.
- `book/05-engineering-organization/README.md` remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-028` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 28 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter28` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part V Role

Chapter 28 follows Chapter 27 by generalizing from one design-review memory practice to broader repeated engineering
practices. Chapter 27 asked whether a design review left durable memory. Chapter 28 should ask how an organization
designs repeated structures so useful technical behavior keeps happening after urgency fades, teams rotate, calendars
fill, and original context disappears.

The chapter should keep Part V technical. It is not about generic meeting hygiene, agile ceremony, facilitation style,
or team operating manuals. It is about repeated engineering practices that protect decision quality, ownership,
learning, risk discovery, evidence, and architectural memory under organizational pressure.

## 4. Canonical Purpose

Prepare Chapter 28 to teach engineering rituals as intentionally designed repeated practices that protect a technical
behavior the organization cannot afford to rediscover accidentally.

Candidate thesis for the future manuscript:

> An engineering ritual is a repeated practice that preserves a technical judgment the organization cannot afford to
> rediscover accidentally.

The chapter should move the reader away from asking:

> What meeting should we schedule?

to asking:

> What technical behavior must keep happening after the original people, urgency, and context are gone?

## 5. Primary-Concept Resolution

Chapter 28 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Chapter 28 should be
carried by material relationships to existing rituals, artifacts, laws, metrics, smells, and anti-patterns.

Engineering ritual, ritual purpose, ritual trigger, ritual cadence, ritual owner, ritual health, ritual decay, review
cadence, meeting hygiene, approval theater, process debt, and ritual design remain chapter-local prose. Do not create a
new PEAK concept, ID, artifact, ritual, metric, vocabulary term, smell, anti-pattern, failure story, or relationship
verb for them.

## 6. Central Thesis

Engineering rituals are useful when they preserve or improve a specific technical behavior. A ritual is not a meeting
by default. It is a repeated structure with purpose, trigger or cadence, participants, inputs, outputs, owner, exit
criteria, feedback loop, failure mode, and a condition for redesign or retirement.

Approved supporting formulation for the future draft:

> Build rituals around behaviors, not meetings.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, ritual, metric,
artifact, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. a recurring meeting is the same thing as a ritual;
2. attendance proves the ritual matters;
3. mandatory attendance fixes ritual decay;
4. a checklist can replace judgment;
5. every decision should pass through the same ritual;
6. canceling a ritual means abandoning the behavior it once protected;
7. Principal Engineers should defend architecture rituals because they created them;
8. process load is a management problem rather than an architecture quality signal.

By the end of the chapter, the reader should be able to:

1. name the technical behavior a ritual protects;
2. distinguish trigger from cadence;
3. identify the ritual owner, participants, decision rights, inputs, and outputs;
4. choose ritual weight based on risk, reversibility, Change Radius, and decision maturity;
5. connect a ritual to the artifact or record it updates;
6. define follow-up ownership, health signals, decay signals, and feedback loops;
7. redesign or retire a ritual without losing the behavior;
8. spot when a ritual has become process theater, approval control, status reporting, or calendar load.

## 8. Engineering Ritual Scope

For Chapter 28, an engineering ritual is a repeated practice that preserves or improves a specific engineering
behavior.

Rituals may protect:

- review before hardening;
- decision memory;
- ownership clarity;
- cross-team alignment;
- release readiness;
- risk discovery;
- evidence gathering;
- weak-signal capture;
- mistake learning;
- dependency review;
- operational or field feedback loops;
- cleanup or simplification discipline.

A useful ritual should have:

- purpose;
- trigger or cadence;
- participants;
- inputs;
- output artifact or decision;
- owner;
- exit criteria;
- feedback loop;
- failure mode;
- redesign or retirement condition.

The future manuscript should avoid turning this into a long checklist. The list is a design lens. The core lesson is
that a ritual must protect a behavior the organization still needs.

## 9. Ritual Design and Ritual Decay

The future manuscript must distinguish:

- ritual purpose;
- ritual trigger;
- ritual cadence;
- ritual owner;
- participants;
- input artifacts;
- output artifacts;
- decision rights;
- review scope;
- exit criteria;
- signals of health;
- signals of decay;
- redesign or retirement condition.

Common ritual decay patterns:

- the meeting continues after the decision need disappears;
- attendance replaces accountability;
- templates replace judgment;
- reviews happen too late;
- records are not updated;
- nobody owns follow-up;
- teams attend to be safe rather than because the ritual helps;
- the ritual becomes a gate for unrelated work;
- the ritual captures status instead of decisions;
- people work around the ritual because it slows necessary change.

Chapter 28 should teach how Principal Engineers tune rituals rather than defend them blindly.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 28 covers:

- engineering rituals as repeated structures that protect technical behavior;
- ritual purpose, trigger, cadence, owner, participants, inputs, outputs, decision rights, and exit criteria;
- feedback loops, health signals, decay signals, redesign conditions, and retirement conditions;
- proportionality based on risk, reversibility, Change Radius, and decision maturity;
- Architecture Review and Architecture Freeze as existing PEAK rituals that can succeed or decay;
- ADRs, RFCs, Decision Journal entries, and Architecture Ledger rows as possible outputs or inputs;
- ownership, evidence, dependency visibility, decision memory, and Discoverability as protected behaviors;
- managers as legitimate partners in cadence, accountability, and organizational cost.

### Explicitly Out of Scope

Do not turn Chapter 28 into:

- a meeting-cadence cookbook;
- an agile ceremony or workflow-framework guide;
- a team operating manual;
- a process-compliance chapter;
- a facilitation tutorial;
- a calendar hygiene essay;
- a management handbook;
- generic productivity advice;
- Chapter 29's mentoring-through-artifacts chapter;
- Chapter 30's alignment-around-decisions chapter;
- Chapter 31's Architecture Health Review chapter;
- a new PEAK concept proposal.

## 11. Recommended Engineering-Organization Story

### Working Title

`The Ritual That Kept Running After It Stopped Helping`

### Starting System

After several cross-team architecture issues, a Principal Engineer helped introduce a weekly architecture review ritual.
At first it worked: teams brought risky designs early, reviewers found hidden dependencies, ADRs improved, and decisions
became easier to find.

### Decay

Over time:

- attendance grows because everyone wants to be safe;
- small reversible decisions wait for the meeting;
- teams present status instead of decisions;
- reviewers ask the same checklist questions regardless of risk;
- follow-up owners are not tracked;
- Decision Journal and Architecture Ledger entries fall behind;
- high-risk changes still arrive too late;
- engineers see the ritual as approval bureaucracy;
- managers use the meeting as a confidence signal;
- the original purpose is no longer visible.

### Initial Question

> Should we cancel the ritual or make attendance mandatory?

### Principal Engineer Intervention

Frame the question again:

> What technical behavior was this ritual meant to protect, and is it still protecting it?

The Principal Engineer should recover the ritual's purpose, separate high-risk triggers from routine status, define
inputs and outputs, make ownership and follow-up visible, redirect small decisions to lighter records, keep Architecture
Review for broad Change Radius decisions, connect outcomes to the Architecture Ledger and Decision Journal, define
health and decay signals, and set a redesign or retirement condition.

The story should protect the behavior, not the meeting.

## 12. Expected Discussion Arc

1. A ritual can start useful and still decay.
2. A ritual is a repeated structure for preserving technical judgment, not a calendar slot.
3. The protected behavior must be named before the meeting format is defended.
4. Trigger and cadence are different: some rituals run on time, some run when risk appears.
5. Inputs and outputs are what make the ritual reviewable.
6. Ownership applies to the ritual itself and to follow-up work it creates.
7. Ritual weight should match risk, reversibility, Change Radius, and decision maturity.
8. Artifacts are not bureaucracy when they preserve the result the ritual exists to protect.
9. Health and decay signals should cause tuning, redesign, or retirement.
10. Retiring a ritual can be stewardship when the behavior is protected another way.

These are intellectual progression points, not mandatory manuscript headings.

## 13. Boundaries With Later Part V Chapters

Chapter 28 must not consume later Engineering Organization chapters.

- Chapter 29 owns mentoring through artifacts: how records teach engineers and transfer judgment.
- Chapter 30 owns aligning teams around decisions: coordination after decision paths and records exist.
- Chapter 31 owns architecture health reviews: recurring assessment of whether architecture still supports necessary
  change.

Chapter 28 may mention mentoring, alignment, and architecture health only as examples of behaviors rituals may support.
It must not teach those chapters early.

## 14. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating them:

- Part I supplies Principal Engineer judgment, better questions, evidence, ownership beyond code, and stewardship.
- Part II supplies the technical behaviors rituals keep visible: ownership, promises, dependency decisions, time,
  simplicity, evidence, and justified flexibility.
- Part III supplies ADRs, RFCs, Decision Journal entries, Architecture Review, and Architecture Freeze as decision
  structures that can become rituals when repeated deliberately.
- Part IV supplies product practices such as field feedback, release readiness, observability review, and upgrade-path
  validation that may need rituals.
- Chapter 26 supplies leadership without authority and shaping decision systems.
- Chapter 27 supplies design review as durable memory.

Chapter 28 should apply these tools to ritual design. It must not repeat their primary lessons.

## 15. Applicability

Chapter 28 is most useful when:

- teams keep repeating the same architecture issues;
- important decisions arrive too late for meaningful review;
- records fall behind meetings;
- follow-up owners disappear;
- recurring meetings accumulate without visible technical output;
- small reversible decisions wait for heavyweight review;
- broad Change Radius decisions bypass review because the ritual feels slow;
- managers rely on attendance as a confidence signal;
- engineers work around the process because the ritual no longer fits the decision.

Not every repeated practice needs to be a meeting. Not every meeting needs a durable artifact. The ritual should be as
light as possible while still protecting the behavior.

## 16. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- rituals are always good;
- rituals are bureaucracy by default;
- every practice needs a meeting;
- every meeting needs an artifact;
- every decision needs the same ritual;
- cadence alone creates quality;
- mandatory attendance fixes ritual decay;
- canceling a ritual abandons the behavior;
- Principal Engineers should own every ritual;
- asynchronous process is always better or always worse;
- ritual health can be inferred from attendance alone.

Sometimes a ritual should be canceled. Sometimes it should be redesigned. Sometimes a manager must own cadence because
staffing, accountability, or coordination cost is part of the problem. Sometimes an asynchronous record is enough.
Sometimes broad risk deserves synchronous review.

## 17. Violation Patterns

The future draft should make these violations visible:

- attendance replaces accountability;
- the meeting continues after its decision need disappears;
- status reporting replaces decision review;
- templates replace judgment;
- small reversible changes wait for a heavyweight forum;
- high-risk changes still arrive after implementation hardens;
- follow-up owners are not tracked;
- Architecture Ledger and Decision Journal updates lag behind the ritual;
- teams attend to be safe rather than because the ritual helps;
- the ritual becomes an approval gate for unrelated work;
- people work around the ritual because it slows necessary change;
- nobody can name what would justify redesigning or retiring the ritual.

Do not create a new anti-pattern ID.

## 18. Engineering Principle Target

Target principle for the future draft:

> Build rituals around behaviors, not meetings. Name the technical judgment the organization must keep making, give it a
> trigger, owner, inputs, outputs, and feedback loop, and retire or redesign the ritual when it stops protecting that
> judgment.

The principle should imply these questions:

1. What behavior is this ritual meant to protect?
2. What decision, evidence, or ownership should it preserve?
3. What is the trigger or cadence?
4. Who owns the ritual?
5. Who must participate, and why?
6. What input must exist before the ritual starts?
7. What output must exist when it ends?
8. What artifact or record changes?
9. What follow-up owner is named?
10. What signal shows the ritual is healthy?
11. What signal shows it has decayed?
12. What would justify retiring or redesigning it?

The final manuscript may shorten this list for reader rhythm.

## 19. Architecture Exercise Target

### Working Title

`Repair One Engineering Ritual`

Ask the reader to choose one recurring engineering practice and document:

- current ritual;
- original purpose;
- technical behavior it should protect;
- current trigger or cadence;
- owner;
- participants;
- inputs;
- outputs;
- artifact or record updated;
- follow-up ownership;
- health signal;
- decay signal;
- redesign action;
- retirement condition.

End with five outputs:

1. one behavior the ritual protects;
2. one input;
3. one output;
4. one owner;
5. one health or decay signal.

Do not create a new canonical artifact.

## 20. Chapter-Local ADR Brief

### Working Title

Redesign the Weekly Architecture Review Ritual Around Change Radius

### Context

- Weekly architecture review started after cross-team architecture issues.
- It initially helped discover hidden dependencies and improve decision records.
- It has drifted into status reporting, approval theater, and waiting for small decisions.
- High-risk changes still arrive too late.
- Follow-up records are stale.

### Decision

- Keep Architecture Review as a ritual for broad Change Radius or high-risk decisions.
- Route small reversible decisions to Decision Journal entries or ADRs without waiting for the meeting.
- Require inputs before review: decision statement, owner, affected owners, options, evidence, and open risks.
- Require outputs after review: outcome, follow-up owner, artifact updates, revisit trigger, and Architecture Ledger
  status.
- Define health signals and decay signals.
- Review the ritual itself periodically.
- Retire or redesign the ritual when it stops protecting early review and decision memory.

### Alternatives Considered

- Cancel the review.
- Make attendance mandatory.
- Keep the ritual unchanged.
- Turn it into a status meeting.
- Require every design decision to pass through it.
- Replace it with asynchronous comments only.
- Escalate every disagreement to management.

### Consequences

Benefits include better fit between ritual weight and risk, fewer unnecessary delays, stronger review inputs, clearer
outputs, more visible follow-up, less approval theater, and stronger decision memory.

Costs include maintaining the ritual itself, making ownership explicit, checking health and decay signals, and resisting
the urge to route unrelated work through the same forum.

The ADR must make a real story-local architecture-process decision. It must not reduce to "hold better meetings."

## 21. PEAK Concept Map

### Concepts Inspected

- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.
- `RITUAL-004` - Architecture Health Review.
- `RITUAL-006` - RFC Friday.
- `VOCAB-006` - Architecture Freeze.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `METRIC-002` - Bus Factor.
- `METRIC-003` - Discoverability.
- `METRIC-005` - Architecture Health.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-006` - Temporary Solution.
- `VOCAB-002` - Weak Signal.
- `VOCAB-007` - Architecture Health.

### Selected Concepts

- `RITUAL-001` - Architecture Review: material because the recommended story redesigns a weekly architecture review
  around the behavior it should protect.
- `RITUAL-002` - Architecture Freeze: material because it is an existing PEAK ritual whose value depends on explicit
  purpose, trigger, scope, output, exit criteria, and avoidance of permanence.
- `ARTIFACT-002` - RFC: material because risky designs need proposal inputs before a ritual can review them responsibly.
- `ARTIFACT-001` - ADR: material because accepted ritual outcomes and decisions need durable records.
- `ARTIFACT-003` - Decision Journal: material because small reversible decisions and follow-up judgments need lighter
  records than a full review meeting.
- `ARTIFACT-006` - Architecture Ledger: material because active ritual outcomes need owner, status, links, and review
  visibility.
- `LAW-001` - Every State Has One Owner: material because every useful ritual needs an owner and must name follow-up
  owners instead of leaving accountability in attendance.
- `LAW-005` - Evidence Before Confidence: material because rituals should require evidence inputs and not let cadence or
  attendance substitute for judgment.
- `LAW-006` - Unused Flexibility Is Waste: material because a ritual that no longer protects the intended behavior
  becomes avoidable process load and should be redesigned or retired.
- `LAW-007` - Every Dependency Is a Decision: material because rituals should expose cross-team dependencies and route
  broad decisions to proportionate review.
- `VOCAB-001` - Change Radius: material because Change Radius determines when the architecture review ritual is needed.
- `METRIC-001` - Change Radius: material because ritual weight should match the affected surface being changed,
  reviewed, or retested.
- `METRIC-003` - Discoverability: material because ritual outputs must be findable after the meeting, decision, or
  original people are gone.
- `SMELL-001` - Silent Coupling: material because decayed rituals let hidden dependencies survive review.
- `SMELL-004` - Hidden State: material because stale ritual outputs, unclear follow-up, and unrecorded decision status
  create invisible organizational state that affects technical behavior.
- `ANTIPATTERN-006` - Temporary Solution: material because temporary choices need owners and review triggers, and
  rituals themselves may need retirement conditions.

### Rejected Concepts

- `RITUAL-004`, `VOCAB-007`, and `METRIC-005`: Architecture Health and Architecture Health Review belong to Chapter 31.
- `RITUAL-006`: RFC Friday is a useful recurring proposal forum, but Chapter 17 owns RFC practice and Chapter 28's
  story is better carried by Architecture Review.
- `VOCAB-006`: Architecture Freeze may appear as an example through `RITUAL-002`, but Chapter 19 owns freeze semantics.
- `ARTIFACT-004`: Mistake Ledger may support mistake learning rituals, but the Chapter 28 story is not a post-failure
  learning chapter.
- `ARTIFACT-007` and `VOCAB-002`: weak signals may feed rituals, but Chapter 31 owns architecture health review and
  weak-signal operation.
- `LAW-002`: API promises may be protected by rituals in examples, but Chapter 28's material focus is ritual design
  around ownership, evidence, dependencies, Change Radius, and records.
- `METRIC-002`: the current concept is Bus Factor, not Decision Quality. It may appear as private-memory risk, but it is
  not the chapter's material metric.
- `SMELL-005`: Platform Leakage is a possible architecture-review concern, but Chapter 28's lesson is ritual decay and
  ritual design.
- `SMELL-006`: Event Explosion is a possible observability or output-noise concern, but the chapter does not need an
  event-design edge.
- `ANTIPATTERN-003`: Global Configuration is nearby when broad process settings hide ownership, but the story can show
  ritual decay without making global configuration material.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as engineering ritual, ritual decay, ritual health, ritual owner, review cadence, meeting hygiene, approval
theater, process debt, ritual design, and retirement condition remain chapter-local prose.

### Valid Relationship Verbs

The registered relationships use only `illustrates` and `references`, both valid PEAK relationship types in
`editor/KNOWLEDGE_MODEL.md`. `related_to` is intentionally avoided because the selected concepts are materially used
and can be named more precisely.

### Exact Proposed PEAK Relationships

Register `CHAPTER-028` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-028
  type: illustrates
  to: RITUAL-001

- from: CHAPTER-028
  type: references
  to: RITUAL-002

- from: CHAPTER-028
  type: references
  to: ARTIFACT-002

- from: CHAPTER-028
  type: references
  to: ARTIFACT-001

- from: CHAPTER-028
  type: references
  to: ARTIFACT-003

- from: CHAPTER-028
  type: references
  to: ARTIFACT-006

- from: CHAPTER-028
  type: references
  to: LAW-001

- from: CHAPTER-028
  type: references
  to: LAW-005

- from: CHAPTER-028
  type: references
  to: LAW-006

- from: CHAPTER-028
  type: references
  to: LAW-007

- from: CHAPTER-028
  type: references
  to: VOCAB-001

- from: CHAPTER-028
  type: references
  to: METRIC-001

- from: CHAPTER-028
  type: references
  to: METRIC-003

- from: CHAPTER-028
  type: references
  to: SMELL-001

- from: CHAPTER-028
  type: references
  to: SMELL-004

- from: CHAPTER-028
  type: references
  to: ANTIPATTERN-006
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 22. Required Reader-Facing Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 28 role:

- Opening Quote: establish that rituals protect behavior rather than time on a calendar.
- Story: show The Ritual That Kept Running After It Stopped Helping.
- Discussion: teach purpose, trigger, owner, inputs, outputs, feedback loop, decay, redesign, and retirement.
- Engineering Principle: build rituals around behaviors, not meetings.
- Architecture Exercise: repair one engineering ritual.
- Principal's Notebook: exactly three short observations, no explanations.
- ADR: record the story-local decision to redesign the weekly Architecture Review ritual around Change Radius.
- Editor's Commentary: explain how Chapter 28 follows Chapter 27 and prepares Chapters 29, 30, and 31 without writing
  them early.

## 23. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A ritual protects a behavior, not a calendar slot.
- A meeting without an output is only memory while people remember it.
- Retiring a ritual can be stewardship.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 24. Technical and Organizational Credibility Requirements

The future draft must treat the following accurately:

- recurring engineering practices in real teams;
- Principal Engineer influence over process without formal authority;
- differences among meeting, ritual, review, gate, status, record, and artifact;
- difference between trigger and cadence;
- proportionality based on risk, reversibility, Change Radius, and decision maturity;
- ownership of the ritual itself;
- inputs, outputs, follow-up owners, and record updates;
- ritual decay and ritual retirement;
- managers as legitimate partners in cadence and accountability;
- teams working around a ritual as a signal, not just resistance;
- asynchronous alternatives where appropriate;
- cost of process load and calendar load.

Avoid misleading claims:

- rituals are always good;
- rituals are bureaucracy;
- every practice needs a meeting;
- every meeting needs an artifact;
- every decision needs the same ritual;
- cadence alone creates quality;
- mandatory attendance fixes ritual decay;
- canceling a ritual means abandoning the behavior;
- Principal Engineers should own every ritual;
- a checklist can replace judgment;
- asynchronous process is always better or always worse;
- ritual health can be inferred from attendance alone.

## 25. Terminology and Precision Guardrails

Use terms precisely:

- Engineering ritual: chapter-local prose for a repeated practice that preserves or improves a specific engineering
  behavior.
- Meeting: a possible container for a ritual, not the ritual itself.
- Trigger: a condition that starts the ritual because risk, decision maturity, or evidence requires it.
- Cadence: a scheduled rhythm used only when repetition itself helps protect the behavior.
- Ritual owner: the person or role responsible for maintaining the ritual's purpose, inputs, outputs, and feedback loop.
- Output: the decision, artifact update, record change, owner, trigger, or follow-up the ritual exists to produce.
- Health signal: evidence that the ritual is still protecting the intended behavior.
- Decay signal: evidence that the ritual has become status, approval theater, approval control, or calendar load.
- Retirement condition: a condition showing that the behavior is no longer needed or is protected better another way.

Avoid misleading statements:

- ritual means meeting;
- attendance means accountability;
- managers are illegitimate owners of cadence;
- review ritual means approval gate;
- asynchronous comments are always lighter;
- every lightweight decision should wait for Architecture Review;
- ritual decay means people are lazy;
- deleting a ritual means abandoning stewardship.

## 26. Failure Modes to Avoid

The later draft must not become:

- a meeting-cadence cookbook;
- an agile ceremony guide;
- a workflow-framework chapter;
- a team operating manual;
- a process-compliance chapter;
- a facilitation tutorial;
- a calendar hygiene essay;
- a management handbook;
- generic productivity advice;
- Architecture Review repeated from Chapter 18;
- Architecture Freeze repeated from Chapter 19;
- Chapter 27 design-review memory repeated;
- a mentoring-through-artifacts chapter written before Chapter 29;
- an alignment-around-decisions chapter written before Chapter 30;
- an Architecture Health Review chapter written before Chapter 31;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 27. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story uses a weekly architecture review ritual that was once useful and has decayed or an equivalent credible
  repeated engineering practice;
- the initial ritual success is concrete: risky designs arrived early, dependencies were discovered, ADRs improved, and
  decisions became easier to find;
- the decay is concrete: attendance grows, status replaces decisions, small choices wait, reviewers reuse the same
  checklist, follow-up owners disappear, records fall behind, and high-risk decisions still arrive late;
- the Principal Engineer frames the question again around protected behavior rather than canceling or mandating
  attendance;
- the manuscript distinguishes meeting, ritual, review, gate, status, record, and artifact;
- trigger and cadence are distinct;
- ritual owner, participants, inputs, outputs, follow-up owners, health signals, decay signals, feedback loop, and
  retirement or redesign condition are visible;
- ritual weight follows risk, reversibility, Change Radius, and decision maturity;
- Architecture Review, Architecture Freeze, RFC, ADR, Decision Journal, and Architecture Ledger appear only where
  proportionate;
- selected PEAK concepts are materially present if the registered relationship set is kept;
- no primary PEAK concept is assigned unless a later editor decision changes repository convention;
- no new PEAK concept is implied accidentally;
- the exercise ends with one behavior, one input, one output, one owner, and one health or decay signal;
- the ADR makes a genuine story-local decision about redesigning the weekly Architecture Review ritual;
- exactly three Principal's Notebook observations are present;
- later Part V chapters are previewed only lightly and not written early.

## 28. Review Handoff Notes

Editorial Review should check whether the chapter stays alive as an engineering-organization story rather than becoming
a meeting advice essay. It should also check that ritual decay is visible through technical consequences, not merely
through annoyance with meetings.

Canon Review should verify that Chapter 28 remains no-primary, preserves only material outgoing relationships, avoids
new PEAK concepts, and keeps engineering ritual, ritual decay, ritual health, ritual owner, and retirement condition as
chapter-local prose carried by existing PEAK concepts.

Technical Review should focus on realistic recurring engineering practices: ownership, trigger versus cadence, inputs,
outputs, follow-up, artifacts, process load, asynchronous alternatives, manager partnership, and tuning or retiring
rituals without losing the protected behavior.

Freeze Review should confirm that Chapter 28 is the third Part V chapter, keeps the manuscript architecture intact,
uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and does not write Chapters
29, 30, or 31 early.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
ritual, team names, decay signals, redesign action, retirement condition, ADR wording, and notebook wording while
preserving the building-engineering-rituals thesis, PEAK map, and chapter boundaries.
