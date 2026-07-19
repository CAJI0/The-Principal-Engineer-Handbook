# CHAPTER-029 Canonical Brief: Mentoring Through Artifacts

## 1. Metadata

- Stable ID: `CHAPTER-029`.
- Title: `Mentoring Through Artifacts`.
- Part: Part V - Engineering Organization.
- Chapter number: 29.
- Expected manuscript path: `book/05-engineering-organization/29-mentoring-through-artifacts.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-029-mentoring-through-artifacts.md`.
- Branch: `chapter29`.
- Verified baseline `origin/main`: `0a757baf3e72bc21ef6c045dd3397b5532a7d33b`.
- Baseline evidence: PR #30 Chapter 28 squash merge commit.
- Chapter 28 feature Freeze commit checked for tree equivalence:
  `604d4583882d6b69633196e81c3dda0a7f9520b1`.
- Canonical predecessor: `CHAPTER-028` - Building Engineering Rituals.
- Part position: fourth chapter of Part V - Engineering Organization.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 29 applies existing artifacts, records, evidence, ownership, Change Radius,
  Discoverability, Bus Factor, and private-memory concepts to mentoring through durable engineering records; it should
  be carried by relationships rather than by a new primary-concept field.
- Central chapter-local practice: using existing engineering artifacts as mentoring surfaces that teach how judgment is
  formed, revised, and carried.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `0a757baf3e72bc21ef6c045dd3397b5532a7d33b`.
- That baseline is the PR #30 Chapter 28 squash merge commit,
  `Chapter 28: Building Engineering Rituals (#30)`.
- The squash commit has parent `e83ade929a78be2361b73da88a623f9f19ae14fb` and is an ancestor of current
  `origin/main`.
- The Chapter 28 feature-branch Freeze commit `604d4583882d6b69633196e81c3dda0a7f9520b1` remains tree-equivalent for
  the checked Chapter 28 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-028` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-028` is the third Part V chapter and is canonical.
- The table of contents places `Mentoring Through Artifacts` fourth in Part V - Engineering Organization.
- `book/05-engineering-organization/README.md` remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-029` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 29 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter29` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part V Role

Chapter 29 follows Chapter 28 by showing what durable records from decisions, reviews, and rituals can do for people
who are learning to make better technical judgments. Chapter 26 made decision ownership and influence visible. Chapter
27 showed reviews as shared memory. Chapter 28 showed rituals as repeated protection for technical behavior. Chapter
29 should show how those records become mentoring surfaces.

The chapter should keep Part V technical. It is not a career-coaching chapter, performance-management chapter,
promotion-packet guide, ramp-up checklist, documentation tutorial, knowledge-base process, code-review etiquette
chapter, or personal advice essay. It is about using engineering artifacts to help engineers practice judgment by
seeing real questions, evidence, constraints, alternatives, trade-offs, rejected options, owners, consequences,
uncertainty, and revisit triggers.

## 4. Canonical Purpose

Prepare Chapter 29 to teach that Principal Engineer mentoring is not mainly giving private advice. It is creating and
using artifacts that let other engineers see how technical judgment was formed and safely inherit more responsibility.

Candidate thesis for the future manuscript:

> The best mentoring artifacts do not tell people what to think. They show how judgment was formed, what evidence
> mattered, what trade-offs were accepted, and what would change the decision.

The chapter should move the reader away from asking:

> How do I document the correct approach so people stop asking me?

to asking:

> What artifact would help another engineer make a better technical decision next time without needing me in the room?

## 5. Primary-Concept Resolution

Chapter 29 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Chapter 29 should be
carried by material relationships to existing artifacts, rituals, laws, metrics, smells, anti-patterns, and failure
stories.

Mentoring through artifacts, mentoring artifact, teaching artifact, artifact-based mentoring, judgment transfer,
learning record, decision example, pattern library, ramp-up record, tribal knowledge, what to notice, what not to
generalize, and teaching surface remain chapter-local prose. Do not create a new PEAK concept, ID, artifact, ritual,
metric, vocabulary term, smell, anti-pattern, failure story, or relationship verb for them.

## 6. Central Thesis

Mentoring through artifacts is the intentional use of durable engineering records to transfer judgment. A useful
mentoring artifact does not merely preserve an answer. It exposes the reasoning that made the answer responsible in its
context, and it warns the learner where the example should not be copied.

Approved supporting formulation for the future draft:

> Mentor by preserving judgment, not just answers.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, artifact, ritual,
metric, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. mentoring is mostly private advice from a senior engineer;
2. a correct answer teaches as well as an explained decision;
3. documentation volume solves repeated questions;
4. code review comments are enough if they say what to change;
5. an ADR teaches by recording the final decision;
6. RFC threads teach even when reasoning is scattered;
7. new engineers should copy proven patterns;
8. uncertainty should be hidden so the artifact looks authoritative;
9. obsolete examples are harmless if they are historically accurate;
10. the Principal Engineer staying available is a mentoring strategy.

By the end of the chapter, the reader should be able to:

1. choose one recurring decision type worth teaching;
2. identify the artifact that already contains useful judgment;
3. expose hidden reasoning: question, context, constraints, evidence, alternatives, rejected options, trade-offs,
   uncertainty, owner, consequence, and revisit trigger;
4. distinguish a teaching artifact from ramp-up documentation, code review, design review, training material,
   promotion evidence, process compliance, and tribal knowledge;
5. add learner cues such as what to notice and what not to generalize;
6. use the artifact in mentoring and review conversations without replacing conversation;
7. improve discoverability so engineers can find the example from the affected behavior;
8. retire or mark obsolete examples that teach the wrong lesson.

## 8. Mentoring-Through-Artifacts Scope

For Chapter 29, mentoring through artifacts means intentional use of durable engineering records to transfer technical
judgment.

Artifacts may include:

- ADRs;
- RFCs;
- Decision Journal entries;
- Mistake Ledger entries;
- Architecture Ledger rows;
- Event Catalog examples;
- design review notes;
- review comments that explain reasoning;
- incident or field-learning summaries;
- examples of rejected options;
- migration notes;
- test evidence summaries;
- architecture exercises;
- annotated examples of good and bad decisions.

A good mentoring artifact should make visible:

- the question being answered;
- context and constraints;
- evidence;
- trade-offs;
- rejected options;
- confidence and uncertainty;
- owner;
- consequences;
- follow-up;
- revisit trigger;
- what a less experienced engineer should notice;
- what not to generalize from this example.

The future manuscript should avoid turning this into a documentation inventory. The point is not artifact volume. The
point is to expose the reasoning process behind technical judgment.

## 9. Mentoring Boundary

The future manuscript must distinguish:

- mentoring through artifacts;
- direct mentoring conversation;
- ramp-up documentation;
- code review;
- design review;
- training material;
- promotion evidence;
- process compliance;
- tribal knowledge;
- architecture record;
- team memory.

Artifacts should not replace conversation. They should make conversation better, repeatable, and less dependent on one
senior engineer's availability. A Principal Engineer should use records to help engineers practice judgment, ask better
questions, and inherit responsibility safely, not to hand them a homework pile or an unquestionable precedent.

Chapter 29 should warn against:

- artifact dumping;
- using records as homework without context;
- presenting decisions as timeless precedent;
- hiding uncertainty to appear authoritative;
- turning mentorship into bureaucracy;
- writing for reviewers instead of learners;
- using artifacts to avoid responsibility for teaching;
- making engineers copy patterns without understanding constraints.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 29 covers:

- artifacts as mentoring surfaces for technical judgment;
- ADRs, RFCs, Decision Journal entries, Mistake Ledger entries, Architecture Ledger rows, review notes, and selected
  field-learning records as teaching sources;
- exposing question, context, constraints, evidence, rejected options, trade-offs, uncertainty, owner, consequences,
  follow-up, and revisit trigger;
- learner cues such as what to notice and what not to generalize;
- artifact use in review, ramp-up, and mentoring conversations;
- discoverability from code, behavior, tools, diagnostics, tests, or product surfaces;
- retiring, correcting, or marking obsolete examples;
- Principal Engineer bottleneck and private-memory risk.

### Explicitly Out of Scope

Do not turn Chapter 29 into:

- a generic mentoring handbook;
- a career-coaching guide;
- a performance-management chapter;
- a promotion-packet guide;
- a ramp-up checklist;
- a documentation tutorial;
- a knowledge-base process;
- a code-review etiquette chapter;
- a design-review chapter repeated from Chapter 27;
- an engineering-rituals chapter repeated from Chapter 28;
- a training-deck chapter;
- a pattern-library catalog;
- Chapter 30's alignment-around-decisions chapter;
- Chapter 31's Architecture Health Review chapter;
- a new PEAK concept proposal.

## 11. Recommended Engineering-Organization Story

### Working Title

`The Answer That Did Not Teach`

### Starting System

A Principal Engineer is repeatedly asked the same architecture questions by several engineers. The product has
accumulated ADRs, RFCs, review notes, release decisions, and field-learning records, but they are hard to learn from.
The records preserve decisions, yet the reasoning that would help another engineer make a similar decision is scattered,
hidden, obsolete, or too implicit.

### Symptoms

- engineers ask for "the right pattern" instead of framing the decision;
- the Principal Engineer answers quickly and correctly, but the same question returns later;
- an ADR records the final decision but hides alternatives and uncertainty;
- an RFC thread contains useful reasoning but is too long and unstructured;
- a Mistake Ledger entry captures a field escape but not the changed mental model;
- review comments say what to change, but not why;
- a new engineer cargo-cults a previous design into the wrong context;
- the Architecture Ledger points to decisions but not to examples that teach;
- obsolete examples keep teaching a pattern that no longer matches the system;
- the Principal Engineer becomes a bottleneck for judgment.

### Initial Question

> Can you document the correct approach?

### Principal Engineer Intervention

Frame the question again:

> What artifact would help someone practice the judgment, not just copy the answer?

The Principal Engineer should choose one recurring decision type, turn a prior decision into a teaching artifact, expose
question, context, constraints, evidence, rejected options, trade-offs, uncertainty, owner, consequence, and revisit
trigger, annotate what to notice and what not to generalize, connect related ADR, RFC, Decision Journal, Mistake Ledger,
and Architecture Ledger records where appropriate, use the artifact in review and mentoring conversations, improve
discoverability, retire misleading examples, and make the next engineer less dependent on the Principal Engineer.

The story should show artifacts as mentoring surfaces, not documents as substitutes for teaching.

## 12. Expected Discussion Arc

1. A correct answer can solve the immediate question and still fail to teach judgment.
2. Mentoring at Principal Engineer level often means improving the decision environment, not staying available for
   every decision.
3. A teaching artifact exposes how judgment was formed, not just what was decided.
4. Existing artifacts have different teaching roles: proposal, decision, lightweight judgment, mistake learning, active
   inventory, and review memory.
5. Learners need context, constraints, evidence, alternatives, rejected options, trade-offs, uncertainty, and triggers.
6. The artifact should name what to notice and what not to generalize.
7. Discoverability matters because the artifact must be found when a similar decision appears.
8. Obsolete examples need correction, retirement, or warnings so they do not teach stale patterns.
9. Artifacts make mentoring conversations better; they do not replace conversation.
10. The chapter closes by connecting artifact-based mentoring to later alignment and architecture health without
    writing those chapters early.

These are intellectual progression points, not mandatory manuscript headings.

## 13. Boundaries With Later Part V Chapters

Chapter 29 must not consume later Engineering Organization chapters.

- Chapter 30 owns aligning teams around decisions: cross-team coordination after decision paths and records exist.
- Chapter 31 owns architecture health reviews: recurring assessment of whether architecture still supports necessary
  change.

Chapter 29 may mention alignment and architecture health only as downstream benefits of better artifact-based learning.
It must not teach team-alignment operating models, decision rollout, architecture-health signals, health-review cadence,
or recurring architecture-health review operation.

## 14. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating them:

- Part I supplies Principal Engineer role, better questions, evidence, ownership beyond code, judgment, and stewardship.
- Part II supplies laws that artifacts can teach through concrete decisions: ownership, API promises, dependencies,
  time, evidence, simplicity, and justified flexibility.
- Part III supplies ADRs, RFCs, Decision Journal entries, Mistake Ledgers, Architecture Ledgers, Architecture Review,
  and Architecture Freeze as durable judgment traces.
- Part IV supplies product-building examples where artifact-based mentoring matters: manufacturing, configuration,
  observability, release, upgrade, field learning, and reference-project memory.
- Chapter 26 supplies leadership without authority through better decision systems.
- Chapter 27 supplies design reviews as shared memory.
- Chapter 28 supplies rituals that can keep artifact-based mentoring alive.

Chapter 29 should apply these tools to mentoring. It must not repeat their primary lessons.

## 15. Applicability

Chapter 29 is most useful when:

- engineers repeatedly ask the same architecture question;
- a Principal Engineer is becoming the default explainer;
- existing records state decisions but hide reasoning;
- RFC comments contain useful judgment that never became easy to learn from;
- ADRs omit uncertainty, alternatives, rejected options, owner, or revisit trigger;
- Mistake Ledger entries capture failures but not the changed mental model;
- review comments say what to do without explaining why;
- new engineers copy a pattern into the wrong context;
- obsolete examples are still discoverable and persuasive;
- teams need mentoring that scales beyond private availability.

Not every artifact should be turned into a teaching artifact. The chapter should teach how to choose examples that
matter because the decision recurs, the consequence is high, the pattern is often copied, or the old reasoning is easy
to misunderstand.

## 16. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- documents replace mentoring;
- every artifact should teach every audience;
- every decision needs a teaching artifact;
- longer records are more educational;
- engineers only need examples;
- senior engineers should encode all judgment into templates;
- one pattern library prevents bad decisions;
- mentoring through artifacts is only ramp-up;
- code review comments are enough;
- artifacts should hide uncertainty to avoid confusion;
- artifact-based mentoring removes the need for team ownership;
- every obsolete artifact must be deleted immediately.

Sometimes a short conversation is the right mentoring moment. Sometimes a code comment is enough. Sometimes an ADR
should stay concise and link to a companion note rather than becoming a tutorial. Sometimes an obsolete example should
remain for history, but it needs a visible warning. Sometimes a decision is too context-specific to become a reusable
teaching example.

## 17. Violation Patterns

The future draft should make these violations visible:

- repeated questions route through the Principal Engineer because records do not teach;
- engineers ask for the right pattern without framing the decision;
- ADRs record the final answer but not the reasoning that made it responsible;
- RFC threads bury useful trade-offs inside long comment history;
- Mistake Ledger entries record the fix but not the changed mental model;
- review comments prescribe changes without naming the judgment behind them;
- examples hide uncertainty and become false precedent;
- rejected options are forgotten and rediscovered as new ideas;
- artifacts are assigned as homework without conversation;
- new engineers copy an old design outside the context that made it valid;
- the Architecture Ledger points to records that are technically present but hard to learn from;
- obsolete examples stay discoverable without warning.

Do not create a new anti-pattern ID.

## 18. Engineering Principle Target

Target principle for the future draft:

> Mentor by preserving judgment, not just answers. Use artifacts to show the question, constraints, evidence,
> alternatives, trade-offs, owner, consequences, and revisit triggers so another engineer can practice the decision,
> not merely copy the result.

The principle should imply these questions:

1. What recurring decision are engineers struggling to make?
2. Which artifact already contains useful judgment?
3. What reasoning is hidden from the current record?
4. What uncertainty or rejected option should be visible?
5. What should the learner notice?
6. What should they not generalize?
7. What context makes this example valid?
8. What would change the decision?
9. How will the artifact be used in review, ramp-up, or mentoring?
10. How will obsolete examples be retired or marked?

The final manuscript may shorten this list for reader rhythm.

## 19. Architecture Exercise Target

### Working Title

`Turn One Decision Into a Teaching Artifact`

Ask the reader to choose one existing decision record and document:

- decision question;
- learner audience;
- context;
- constraints;
- evidence;
- alternatives;
- rejected option;
- accepted trade-off;
- owner;
- consequence;
- uncertainty;
- revisit trigger;
- lesson to notice;
- warning not to overgeneralize;
- record to update;
- conversation or review where it will be used.

End with five outputs:

1. one decision question;
2. one hidden reasoning element to expose;
3. one lesson to notice;
4. one warning not to generalize;
5. one artifact update.

Do not create a new canonical artifact.

## 20. Chapter-Local ADR Brief

### Working Title

Turn the Retry Strategy ADR Into a Mentoring Artifact

### Context

- Several engineers keep asking the same architecture question about retry strategy or service boundary behavior.
- The existing ADR states the final decision but does not teach the judgment.
- Relevant RFC discussion, review notes, Decision Journal entries, Mistake Ledger entries, and Architecture Ledger rows
  are scattered.
- A prior field issue changed the team's mental model, but the lesson is hard to find.
- The Principal Engineer is becoming the default explainer.

### Decision

- Update the ADR or linked companion note to expose context, constraints, evidence, rejected options, accepted
  trade-offs, uncertainty, owner, consequences, and revisit trigger.
- Link the related RFC, Decision Journal entry, Mistake Ledger entry, and Architecture Ledger row where appropriate.
- Add a short `what to notice / what not to generalize` section if repository style permits.
- Use the artifact in future review and mentoring conversations.
- Retire or mark obsolete examples that teach the wrong lesson.

### Alternatives Considered

- Write a generic best-practices page.
- Answer engineers individually.
- Require everyone to read the ADR as-is.
- Create a training deck detached from real decisions.
- Rely on code comments.
- Make the senior engineer approve every similar decision.

### Consequences

Benefits include better judgment transfer, less repeated explanation, more discoverable reasoning, safer reuse of
patterns, clearer uncertainty, clearer ownership, and a lower private-memory bottleneck around one Principal Engineer.

Costs include maintaining the teaching surface, keeping links current, choosing what not to teach, and retiring
examples when the system changes.

The ADR must make a real story-local architecture-process decision. It must not reduce to "write better docs."

## 21. PEAK Concept Map

### Concepts Inspected

- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `METRIC-002` - Bus Factor.
- `METRIC-003` - Discoverability.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-006` - Temporary Solution.
- `FAILURE-004` - The Hero Engineer.
- `VOCAB-002` - Weak Signal.
- `VOCAB-007` - Architecture Health.
- `METRIC-005` - Architecture Health.
- `RITUAL-004` - Architecture Health Review.

### Selected Concepts

- `ARTIFACT-001` - ADR: material because the recommended story and chapter-local ADR turn a final decision record into
  a teaching surface.
- `ARTIFACT-002` - RFC: material because proposal history and review questions often contain the reasoning a learner
  needs before a decision closes.
- `ARTIFACT-003` - Decision Journal: material because smaller judgments, evidence gaps, confidence, and review triggers
  can teach without a full ADR.
- `ARTIFACT-004` - Mistake Ledger: material because field escapes and repeated mistakes should teach the changed
  mental model, not merely the fix.
- `ARTIFACT-006` - Architecture Ledger: material because active decisions need owner, status, links, and review dates so
  teaching examples remain findable.
- `RITUAL-001` - Architecture Review: material because artifacts become mentoring surfaces in review conversations and
  review outcomes can produce examples worth teaching.
- `LAW-001` - Every State Has One Owner: material because teaching artifacts must name the owner of the decision and the
  responsibility being inherited.
- `LAW-005` - Evidence Before Confidence: material because the chapter teaches artifacts to expose evidence,
  assumptions, confidence, uncertainty, and revisit triggers.
- `LAW-006` - Unused Flexibility Is Waste: material because obsolete or misleading examples should be removed, marked,
  or retired when they no longer teach justified flexibility.
- `LAW-007` - Every Dependency Is a Decision: material because teaching artifacts should make dependency consequences,
  lifecycle constraints, and replacement costs visible to learners.
- `VOCAB-001` - Change Radius: material because the reach of a recurring decision helps choose whether it deserves a
  teaching artifact and which audience should learn from it.
- `METRIC-001` - Change Radius: material because the chapter can use affected surface to judge consequence and teaching
  priority without false precision.
- `METRIC-002` - Bus Factor: material because repeated private explanation by one Principal Engineer means the
  architecture depends on private memory and low judgment redundancy. The current canon names `METRIC-002` as Bus
  Factor, not Decision Quality.
- `METRIC-003` - Discoverability: material because a teaching artifact succeeds only when engineers can find the
  decision, owner, contract, and reasoning from the affected behavior.
- `SMELL-001` - Silent Coupling: material because copied patterns and hidden dependencies become unsafe when artifacts
  fail to explain the contract behind behavior.
- `SMELL-004` - Hidden State: material because hidden decision state and hidden reasoning force engineers back to oral
  history.
- `ANTIPATTERN-006` - Temporary Solution: material because temporary decisions need owners and review triggers, and
  obsolete examples can become permanent teaching mistakes.
- `FAILURE-004` - The Hero Engineer: material because the story centers on reducing dependence on one senior engineer's
  private memory and intervention.

### Rejected Concepts

- `ARTIFACT-005` - Event Catalog: event examples may appear as possible teaching material, but Chapter 23 owns Event
  Catalog operation and Chapter 29 does not need an event-design edge.
- `ARTIFACT-007` and `VOCAB-002` - Weak Signal Register and Weak Signal: weak signals may feed examples, but Chapter 31
  owns recurring architecture-health operation.
- `RITUAL-002` - Architecture Freeze: freeze can be an example of a prior decision, but Chapter 19 and Chapter 28 own
  freeze semantics and ritual design.
- `LAW-002` - Every API Is a Promise: retry or service-boundary behavior may appear in the story, but Chapter 29's
  material lesson is artifact-based mentoring rather than API promise semantics.
- `SMELL-005` - Platform Leakage: possible example domain, but the chapter does not need platform-boundary leakage as a
  material edge.
- `SMELL-006` - Event Explosion: possible example domain, but the chapter does not teach event-model design.
- `ANTIPATTERN-003` - Global Configuration: possible example domain, but the chapter's failure is hidden reasoning and
  copied precedent rather than global configuration.
- `VOCAB-007`, `METRIC-005`, and `RITUAL-004`: Architecture Health and Architecture Health Review belong to Chapter 31.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as mentoring through artifacts, mentoring artifact, teaching artifact, artifact-based mentoring, judgment
transfer, learning record, decision example, pattern library, ramp-up record, tribal knowledge, what to notice, what
not to generalize, and teaching surface remain chapter-local prose.

### Valid Relationship Verbs

The registered relationships use only `illustrates` and `references`, both valid PEAK relationship types in
`editor/KNOWLEDGE_MODEL.md`. `related_to` is intentionally avoided because the selected concepts are materially used
and can be named more precisely.

### Exact Proposed PEAK Relationships

Register `CHAPTER-029` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-029
  type: illustrates
  to: ARTIFACT-001

- from: CHAPTER-029
  type: references
  to: ARTIFACT-002

- from: CHAPTER-029
  type: references
  to: ARTIFACT-003

- from: CHAPTER-029
  type: references
  to: ARTIFACT-004

- from: CHAPTER-029
  type: references
  to: ARTIFACT-006

- from: CHAPTER-029
  type: references
  to: RITUAL-001

- from: CHAPTER-029
  type: references
  to: LAW-001

- from: CHAPTER-029
  type: references
  to: LAW-005

- from: CHAPTER-029
  type: references
  to: LAW-006

- from: CHAPTER-029
  type: references
  to: LAW-007

- from: CHAPTER-029
  type: references
  to: VOCAB-001

- from: CHAPTER-029
  type: references
  to: METRIC-001

- from: CHAPTER-029
  type: references
  to: METRIC-002

- from: CHAPTER-029
  type: references
  to: METRIC-003

- from: CHAPTER-029
  type: references
  to: SMELL-001

- from: CHAPTER-029
  type: references
  to: SMELL-004

- from: CHAPTER-029
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-029
  type: references
  to: FAILURE-004
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

Each section should serve the Chapter 29 role:

- Opening Quote: establish that useful mentoring preserves judgment, not just answers.
- Story: show The Answer That Did Not Teach.
- Discussion: teach how engineering artifacts expose reasoning and become mentoring surfaces.
- Engineering Principle: mentor by preserving judgment, not just answers.
- Architecture Exercise: turn one decision into a teaching artifact.
- Principal's Notebook: exactly three short observations, no explanations.
- ADR: record the story-local decision to turn the retry strategy ADR into a mentoring artifact.
- Editor's Commentary: explain how Chapter 29 follows Chapters 26-28 and prepares Chapters 30-31 without writing them
  early.

## 23. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A good artifact teaches the shape of a decision.
- Mentoring fails when records hide uncertainty.
- The goal is better judgment without you in the room.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 24. Technical and Organizational Credibility Requirements

The future draft must treat the following accurately:

- mentoring experienced and less experienced engineers through real engineering records;
- distinction among advice, coaching, ramp-up, code review, documentation, and artifact-based mentoring;
- how ADRs, RFCs, Decision Journal entries, Mistake Ledger entries, Architecture Ledger rows, and review notes can
  teach judgment;
- risk of copying patterns without context;
- risk of hiding uncertainty in final decisions;
- discoverability of teaching examples;
- maintenance and retirement of obsolete examples;
- Principal Engineer bottleneck and Bus Factor risk;
- mentoring as repeated practice, not one document;
- artifacts as conversation aids, not replacements;
- realistic use of field-learning records without turning the chapter into incident process.

Avoid misleading claims:

- documents replace mentoring;
- every artifact should teach every audience;
- every decision needs a teaching artifact;
- engineers only need examples;
- senior engineers should encode all judgment into templates;
- one pattern library prevents bad decisions;
- mentoring through artifacts is only ramp-up;
- code review comments are enough;
- making records longer makes them more educational;
- artifacts should hide uncertainty to avoid confusion;
- artifact-based mentoring removes the need for team ownership.

## 25. Terminology and Precision Guardrails

Use terms precisely:

- Mentoring through artifacts: chapter-local prose for intentionally using durable engineering records to transfer
  judgment.
- Teaching artifact: chapter-local prose for an existing or lightly annotated record used to teach how a decision was
  made.
- Artifact dumping: assigning documents without context, discussion, or learner cues.
- What to notice: the specific judgment move the learner should see.
- What not to generalize: the context boundary that prevents cargo-cult reuse.
- Obsolete example: an artifact whose old lesson no longer matches the current system or constraints.
- Judgment transfer: chapter-local prose for helping another engineer practice reasoning, not merely copy a result.

Avoid misleading statements:

- mentoring equals documentation;
- artifacts are self-teaching by default;
- final decisions are better examples when uncertainty is hidden;
- every previous decision is a reusable pattern;
- a Principal Engineer should approve every similar decision;
- code review is the only or best mentoring surface;
- ramp-up is the same as artifact-based mentoring;
- discoverability means a record exists somewhere.

## 26. Failure Modes to Avoid

The later draft must not become:

- a generic mentoring handbook;
- a career advice essay;
- a performance-management chapter;
- a promotion evidence guide;
- a ramp-up checklist;
- a documentation tutorial;
- a knowledge-base process;
- a code-review etiquette chapter;
- a design-review chapter repeated from Chapter 27;
- an engineering-rituals chapter repeated from Chapter 28;
- an ADR/RFC tutorial repeated from Chapter 17;
- a pattern-library catalog;
- an incident-postmortem chapter;
- an alignment-around-decisions chapter written before Chapter 30;
- an Architecture Health Review chapter written before Chapter 31;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 27. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story uses a recurring architecture question about retry strategy, service boundary behavior, or an equivalent
  credible decision type;
- the Principal Engineer initially answers correctly, but the same question returns because the answer did not teach;
- existing ADRs, RFCs, review notes, release decisions, and field-learning records are present but hard to learn from;
- the story shows an ADR hiding alternatives and uncertainty, an RFC thread burying reasoning, a Mistake Ledger entry
  missing the changed mental model, review comments missing why, and a copied pattern used in the wrong context;
- the intervention frames documentation again as a teaching artifact that lets engineers practice judgment;
- the manuscript distinguishes mentoring through artifacts from advice, coaching, ramp-up documentation, code
  review, design review, training material, promotion evidence, process compliance, tribal knowledge, architecture
  record, and team memory;
- artifact roles are proportionate: ADR, RFC, Decision Journal, Mistake Ledger, Architecture Ledger, and review notes
  appear only where they carry real judgment;
- learner cues include what to notice and what not to generalize;
- selected PEAK concepts are materially present if the registered relationship set is kept;
- no primary PEAK concept is assigned unless a later editor decision changes repository convention;
- no new PEAK concept is implied accidentally;
- the exercise ends with one decision question, one hidden reasoning element to expose, one lesson to notice, one
  warning not to generalize, and one artifact update;
- the ADR makes a genuine story-local decision about turning the retry strategy ADR into a mentoring artifact;
- exactly three Principal's Notebook observations are present;
- later Part V chapters are previewed only lightly and not written early.

## 28. Review Handoff Notes

Editorial Review should check whether the chapter stays alive as an engineering-organization story rather than becoming
a documentation or career-mentoring essay. It should also check that the story shows a correct answer failing to teach
judgment, not merely bad documentation being improved.

Canon Review should verify that Chapter 29 remains no-primary, preserves only material outgoing relationships, avoids
new PEAK concepts, and keeps mentoring through artifacts, teaching artifact, judgment transfer, what to notice, what
not to generalize, and artifact dumping as chapter-local prose carried by existing PEAK concepts.

Technical Review should focus on realistic artifact use: ADR/RFC/Decision Journal/Mistake Ledger/Architecture Ledger
boundaries, review-note credibility, field-learning summaries, cargo-cult risk, uncertainty visibility, discoverability,
obsolete example retirement, and Principal Engineer bottleneck risk.

Freeze Review should confirm that Chapter 29 is the fourth Part V chapter, keeps the manuscript architecture intact,
uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and does not write Chapters
30 or 31 early.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
retry strategy, service-boundary example, learner audience, artifact links, teaching annotations, obsolete example,
ADR wording, and notebook wording while preserving the mentoring-through-artifacts thesis, PEAK map, and chapter
boundaries.
