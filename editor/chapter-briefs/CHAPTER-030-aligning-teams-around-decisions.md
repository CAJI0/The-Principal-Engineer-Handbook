# CHAPTER-030 Canonical Brief: Aligning Teams Around Decisions

## 1. Metadata

- Stable ID: `CHAPTER-030`.
- Title: `Aligning Teams Around Decisions`.
- Part: Part V - Engineering Organization.
- Chapter number: 30.
- Expected manuscript path: `book/05-engineering-organization/30-aligning-teams-around-decisions.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-030-aligning-teams-around-decisions.md`.
- Branch: `chapter30`.
- Verified baseline `origin/main`: `73cc53d2afac40abcdd9ead33e9ea3885ec82163`.
- Baseline evidence: PR #31 Chapter 29 squash merge commit,
  `Chapter 29: Mentoring Through Artifacts (#31)`.
- Chapter 29 feature Freeze commit checked for tree equivalence:
  `610da9d8a71673d04b806b614f6aa37a76131f20`.
- Canonical predecessor: `CHAPTER-029` - Mentoring Through Artifacts.
- Part position: fifth chapter of Part V - Engineering Organization.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 30 applies existing decision, record, ownership, evidence, dependency, Change Radius,
  Discoverability, Bus Factor, and private-memory concepts to cross-team decision alignment; it should be carried by
  relationships rather than by a new primary-concept field.
- Central chapter-local practice: turning a recorded technical decision into explicit cross-team obligations,
  sequencing, owners, evidence, and review triggers.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `73cc53d2afac40abcdd9ead33e9ea3885ec82163`.
- That baseline is the PR #31 Chapter 29 squash merge commit,
  `Chapter 29: Mentoring Through Artifacts (#31)`.
- The squash commit has parent `0a757baf3e72bc21ef6c045dd3397b5532a7d33b` and is an ancestor of current
  `origin/main`.
- The Chapter 29 feature-branch Freeze commit `610da9d8a71673d04b806b614f6aa37a76131f20` remains tree-equivalent for
  the checked Chapter 29 lifecycle files in the squash commit.
- `CHAPTER-001` through `CHAPTER-029` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-029` is the fourth Part V chapter and is canonical.
- The table of contents places `Aligning Teams Around Decisions` fifth in Part V - Engineering Organization.
- `book/05-engineering-organization/README.md` remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `CHAPTER-030` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 30 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter30` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part V Role

Chapter 30 follows Chapter 29 by moving from artifacts as teaching surfaces to decisions as coordination surfaces.
Chapter 26 showed how a Principal Engineer can lead without owning every decision. Chapter 27 showed that reviews need
durable memory. Chapter 28 showed that repeated practices can protect technical behavior. Chapter 29 showed that
records can transfer judgment. Chapter 30 should show how those records help multiple teams act on the same decision
without relying on one person to translate it repeatedly.

The chapter should keep Part V technical. It is not a stakeholder-management chapter, consensus-building essay,
program-management chapter, release-readiness chapter, meeting facilitation guide, status-reporting process, roadmap
planning guide, or conflict-resolution chapter. It is about making the technical consequences of one decision explicit
enough that affected teams can coordinate implementation, tests, diagnostics, release notes, support behavior,
manufacturing or operational process, and follow-up ownership.

## 4. Canonical Purpose

Prepare Chapter 30 to teach that team alignment around a decision is not agreement in a meeting. Teams are aligned when
the same decision record tells each affected owner what changed, what did not change, what they own, what evidence is
required, what must happen first, what can proceed independently, what risk remains, and what would reopen the decision.

Candidate thesis for the future manuscript:

> A decision is aligned when every affected owner can name the same decision, consequence, obligation, sequence,
> evidence, and review trigger.

The chapter should move the reader away from asking:

> How do I get everyone to agree with the decision?

to asking:

> What must each affected team now do, own, verify, stop doing, or revisit because this decision exists?

## 5. Primary-Concept Resolution

Chapter 30 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Chapter 30 should be
carried by material relationships to existing artifacts, rituals, laws, metrics, smells, anti-patterns, and failure
stories.

Decision alignment, alignment around decisions, alignment contract, alignment note, affected-owner map, obligation map,
implementation promise, rollout map, decision broadcast, coordination surface, shared commitment, and same-decision
test remain chapter-local prose. Do not create a new PEAK concept, ID, artifact, ritual, metric, vocabulary term, smell,
anti-pattern, failure story, or relationship verb for them.

## 6. Central Thesis

Aligning teams around decisions means converting a technical choice into shared operational meaning. The decision record
must name who owns the decision, who is affected by it, what promises change, what dependencies are created, what
temporary exceptions exist, what evidence is needed, and what review trigger will reopen the choice.

Approved supporting formulation for the future draft:

> Align teams by turning decisions into shared obligations, not shared opinions.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, artifact, ritual,
metric, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. alignment means everyone attended the meeting;
2. agreement on the chosen option is enough;
3. a decision owner can coordinate by answering questions as they appear;
4. RFC approval means implementation details are aligned;
5. ADR publication means affected teams understand their obligations;
6. the release plan will expose any missed coordination;
7. affected teams only need the final answer;
8. disagreement is the main alignment failure;
9. temporary exceptions can be handled informally;
10. the Principal Engineer staying available is a sufficient translation mechanism.

By the end of the chapter, the reader should be able to:

1. identify one cross-team decision whose consequences are being interpreted differently;
2. name the decision owner and affected owners;
3. separate decision agreement from implementation alignment;
4. update the RFC, ADR, Decision Journal entry, or Architecture Ledger so obligations are visible;
5. make changed and unchanged promises explicit;
6. identify sequencing constraints and independent work;
7. record evidence, open questions, assumptions, residual risks, and review triggers;
8. reduce reliance on one Principal Engineer as the decision interpreter.

## 8. Decision Alignment Scope

For Chapter 30, aligning teams around decisions means making a technical decision actionable across ownership
boundaries.

The future manuscript should show that an aligned decision includes:

- decision statement;
- decision owner;
- affected owners;
- affected system surfaces;
- changed promises;
- unchanged promises;
- dependency consequences;
- sequencing constraints;
- evidence already accepted;
- evidence still required;
- open questions;
- explicit non-goals;
- temporary exceptions with owner and expiration condition;
- follow-up actions and owners;
- review trigger;
- links to RFC, ADR, Decision Journal, Architecture Ledger, tests, diagnostics, release note, support procedure, or
  manufacturing or operational process where appropriate.

The point is not heavier process. The point is to prevent each team from implementing a different interpretation of the
same decision.

## 9. Alignment Boundary

The future manuscript must distinguish:

- alignment around a decision;
- consensus;
- approval;
- review attendance;
- decision ownership;
- implementation ownership;
- program coordination;
- release readiness;
- Architecture Review;
- RFC mechanics;
- ADR writing;
- mentoring through artifacts;
- recurring engineering rituals;
- architecture health review.

Alignment should not mean everyone gets equal decision rights, every concern blocks progress, every affected team must
approve every detail, or the Principal Engineer becomes the owner of all cross-team consequences. The chapter should
teach enough structure for teams to act together while preserving clear decision ownership.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 30 covers:

- cross-team decision alignment after a decision has enough shape to coordinate work;
- decision owner and affected-owner clarity;
- translating the same decision into team obligations;
- changed and unchanged API, behavior, diagnostic, manufacturing, release, or support promises;
- dependency consequences and sequencing;
- RFC, ADR, Decision Journal, Architecture Ledger, and Architecture Review use as alignment surfaces;
- evidence and open-question tracking;
- temporary compatibility exceptions with owners and review triggers;
- discoverability of the decision, owner, contract, and obligations;
- private-memory and Bus Factor risk when one Principal Engineer becomes the only interpreter.

### Explicitly Out of Scope

Do not turn Chapter 30 into:

- a generic leadership alignment chapter;
- a stakeholder-management chapter;
- a consensus-building essay;
- a meeting facilitation guide;
- a program-management guide;
- a release-readiness chapter repeated from Chapter 24;
- an Architecture Freeze chapter repeated from Chapter 19;
- an RFC or ADR tutorial repeated from Chapter 17;
- a design-review chapter repeated from Chapter 27;
- an engineering-rituals chapter repeated from Chapter 28;
- a mentoring-through-artifacts chapter repeated from Chapter 29;
- Chapter 31's Architecture Health Review chapter;
- a new PEAK concept proposal.

## 11. Recommended Engineering-Organization Story

### Working Title

`The Decision Everyone Agreed To Differently`

### Starting System

A cross-team provisioning compatibility decision has been accepted after an RFC and review. The team believes the hard
part is finished because everyone agreed to keep older devices working while changing the provisioning flow for the next
release. The decision touches firmware behavior, backend assumptions, service tooling, manufacturing scripts, support
diagnostics, test coverage, release notes, and field procedures.

### Symptoms

- firmware treats the decision as a new default behavior with a temporary compatibility path;
- backend treats the decision as support for both modes indefinitely;
- service tooling assumes the old provisioning sequence remains authoritative;
- manufacturing scripts keep writing a flag whose owner is unclear;
- support diagnostics describe behavior that the new firmware will no longer guarantee;
- test owners cannot tell which combinations are release-critical;
- the release owner sees agreement but not remaining evidence gaps;
- the Architecture Ledger has links but no affected-owner obligations;
- the Principal Engineer becomes the person translating the decision for every team;
- everyone says they are aligned, but each team is preparing a different system.

### Initial Question

> Can you send the decision around so everyone is aligned?

### Principal Engineer Intervention

Frame the question again:

> What must each affected team now do, own, verify, stop doing, or revisit because of this decision?

The Principal Engineer should update the RFC or linked alignment note to name the decision owner, affected owners,
changed and unchanged promises, dependency consequences, sequence, evidence, open questions, temporary exceptions,
follow-up owners, and review trigger. The final ADR records the architectural decision. Decision Journal entries capture
smaller follow-ups. The Architecture Ledger tracks active ownership, status, related artifacts, and review date.

The story should show alignment as shared technical obligations, not agreement theater.

## 12. Expected Discussion Arc

1. A decision can be correct and still fail when teams interpret it differently.
2. Alignment starts after the question is framed and before implementation assumptions harden.
3. Agreement is weaker than shared obligations.
4. The decision owner is not automatically the owner of every affected change.
5. Affected owners need to know what changed, what stayed stable, and what they must verify.
6. RFCs are useful alignment surfaces when they expose scope, non-goals, risks, open questions, and affected owners.
7. ADRs preserve the final decision, but they should link to implementation obligations instead of hiding them.
8. Decision Journal entries and the Architecture Ledger keep smaller commitments discoverable.
9. Temporary exceptions need owners, evidence, and expiration conditions.
10. The chapter closes by connecting alignment to future architecture health without running a health review early.

These are intellectual progression points, not mandatory manuscript headings.

## 13. Boundaries With Later Part V Chapters

Chapter 30 must not consume the remaining Engineering Organization chapter.

- Chapter 31 owns architecture health reviews: recurring assessment of whether architecture still supports necessary
  change.

Chapter 30 may mention architecture health only as a downstream reason to keep decision obligations visible. It must not
teach architecture-health signals, health-review cadence, periodic health assessment, weak-signal intake, or health
review operation.

## 14. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating them:

- Part I supplies Principal Engineer role, better questions, evidence, ownership beyond code, judgment, and stewardship.
- Part II supplies laws that constrain aligned decisions: state ownership, API promises, dependencies, time, evidence,
  simplicity, and justified flexibility.
- Part III supplies ADRs, RFCs, Decision Journal entries, Architecture Ledgers, Architecture Review, and Architecture
  Freeze as durable decision tools.
- Part IV supplies product examples where alignment matters across manufacturing, configuration, observability, release,
  upgrade, field support, and reference-project memory.
- Chapter 26 supplies leadership without formal authority.
- Chapter 27 supplies design reviews as shared memory.
- Chapter 28 supplies rituals that can protect repeated alignment behavior.
- Chapter 29 supplies mentoring through artifacts and judgment transfer.

Chapter 30 should apply these tools to cross-team decision alignment. It must not repeat their primary lessons.

## 15. Applicability

Chapter 30 is most useful when:

- a technical decision crosses team or ownership boundaries;
- everyone agreed in a meeting, but implementation plans diverge;
- an RFC was approved before affected-owner obligations were explicit;
- an ADR records the final decision but not who must change behavior;
- a compatibility exception has no owner or expiration condition;
- API or diagnostic promises changed across teams;
- manufacturing, service tooling, support, or release work depends on engineering interpretation;
- test owners cannot tell which combinations are critical;
- the Architecture Ledger has links but not active obligations;
- the Principal Engineer is repeatedly asked to translate the same decision.

Not every decision requires broad alignment work. The chapter should teach proportionality: use this approach when the
Change Radius crosses ownership boundaries, the cost of divergent interpretation is high, or one person's private memory
is carrying the coordination.

## 16. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- every decision needs a cross-team alignment process;
- consensus is required for technical progress;
- every affected team has veto power;
- a longer RFC creates better alignment;
- an ADR by itself aligns implementation work;
- release planning will reveal all decision drift;
- the Principal Engineer should own every cross-team follow-up;
- all temporary exceptions are bad;
- alignment removes disagreement;
- every alignment gap is a management failure;
- the architecture ledger should duplicate every artifact;
- meetings are always worse or better than asynchronous review.

Sometimes a short owner-to-owner conversation is enough. Sometimes the decision has low Change Radius. Sometimes one
affected team can proceed independently after reading the ADR. Sometimes the right answer is to pause implementation and
gather evidence before asking teams to align around a decision that is not ready.

## 17. Violation Patterns

The future draft should make these violations visible:

- teams say they agreed but describe different consequences;
- the decision owner is clear, but affected-owner obligations are not;
- RFC approval happens without scope, non-goals, and open questions being updated;
- an ADR records the final option but not changed and unchanged promises;
- release plans depend on assumptions that no owner has accepted;
- temporary compatibility paths lack expiration conditions;
- support, manufacturing, service tooling, and tests each infer different behavior;
- the Architecture Ledger links to records but omits owner, status, or review date;
- one Principal Engineer becomes the live translator of the decision;
- disagreement is hidden until late integration or release hardening.

Do not create a new anti-pattern ID.

## 18. Engineering Principle Target

Target principle for the future draft:

> Align teams by turning decisions into shared obligations, not shared opinions. Name the decision owner, affected
> owners, changed and unchanged promises, sequencing constraints, evidence, open questions, temporary exceptions, and
> review trigger so each team can act on the same technical choice.

The principle should imply these questions:

1. What decision are teams interpreting differently?
2. Who owns the decision?
3. Who is affected by the decision?
4. What changed?
5. What must stay true?
6. What does each affected owner now owe?
7. What must happen before what?
8. What evidence is accepted and what evidence is still missing?
9. What temporary exception needs an owner and expiration condition?
10. What would reopen or revise the decision?

The final manuscript may shorten this list for reader rhythm.

## 19. Architecture Exercise Target

### Working Title

`Align One Cross-Team Decision`

Ask the reader to choose one decision that affects more than one team and document:

- decision statement;
- decision owner;
- affected owners;
- affected surfaces;
- changed promise;
- unchanged promise;
- dependency consequence;
- sequencing constraint;
- accepted evidence;
- missing evidence;
- open question;
- temporary exception;
- follow-up owner;
- review trigger;
- artifact to update.

End with five outputs:

1. one decision statement;
2. one affected-owner obligation;
3. one changed or unchanged promise;
4. one sequencing constraint or evidence gap;
5. one artifact update.

Do not create a new canonical artifact.

## 20. Chapter-Local ADR Brief

### Working Title

Use the Provisioning RFC as the Alignment Contract

### Context

- A provisioning compatibility decision has been accepted after RFC discussion and Architecture Review.
- The final ADR records the selected technical direction, but teams are interpreting obligations differently.
- Firmware, backend, service tooling, manufacturing scripts, support diagnostics, tests, and release notes are affected.
- Some teams assume the compatibility path is temporary; others assume it is a long-term promise.
- The Principal Engineer is becoming the translator for the same decision across teams.

### Decision

- Treat the accepted RFC, plus a short linked update if needed, as the alignment surface until implementation closes.
- Update the RFC with decision owner, affected owners, changed and unchanged promises, sequencing constraints, evidence,
  open questions, temporary exceptions, follow-up owners, and review trigger.
- Keep the ADR focused on the final architectural decision and consequences.
- Use Decision Journal entries for small follow-ups and evidence gaps.
- Add or update the Architecture Ledger row with owner, status, related artifacts, and review date.
- Require each affected owner to confirm the obligation they own, not to approve every detail.

### Alternatives Considered

- Send a decision announcement and rely on teams to infer their work.
- Reopen the whole decision until every team agrees on all details.
- Make the Principal Engineer coordinate every follow-up manually.
- Put every obligation into the ADR.
- Wait for release planning or integration testing to expose mismatches.
- Create a new permanent alignment artifact.

### Consequences

Benefits include less divergent implementation, clearer ownership, better evidence tracking, clearer temporary
exceptions, better Discoverability, lower Bus Factor risk around one Principal Engineer, and less late release drift.

Costs include maintaining the RFC update, making affected-owner obligations explicit, revisiting open questions, and
resisting the urge to turn the record into duplicated project planning.

The ADR must make a real story-local architecture-process decision. It must not reduce to "communicate better."

## 21. PEAK Concept Map

### Concepts Inspected

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
- `FAILURE-004` - The Hero Engineer.
- `FAILURE-005` - The Release We Should Have Delayed.
- `VOCAB-002` - Weak Signal.
- `VOCAB-007` - Architecture Health.

### Selected Concepts

- `ARTIFACT-002` - RFC: material because RFCs are the existing PEAK artifact for proposals that need feedback across
  ownership boundaries, and the chapter uses the accepted RFC as the central alignment surface.
- `ARTIFACT-001` - ADR: material because the final architectural decision and consequences still need a durable record.
- `ARTIFACT-003` - Decision Journal: material because smaller follow-ups, evidence gaps, confidence, and review triggers
  may be too small for a full ADR.
- `ARTIFACT-006` - Architecture Ledger: material because active decisions need owner, status, related artifact, and
  review date so affected teams can find current obligations.
- `RITUAL-001` - Architecture Review: material because the decision crosses ownership boundaries and the review can
  surface affected owners, constraints, alternatives, risks, evidence, and open questions.
- `LAW-001` - Every State Has One Owner: material because alignment requires naming who owns affected state and who can
  change, validate, and explain it.
- `LAW-002` - Every API Is a Promise: material because the story turns on changed and unchanged behavior, error,
  diagnostic, or timing promises trusted by other teams.
- `LAW-005` - Evidence Before Confidence: material because aligned work should distinguish accepted evidence, missing
  evidence, assumptions, confidence, and review triggers.
- `LAW-007` - Every Dependency Is a Decision: material because cross-team alignment must expose dependency
  consequences, lifecycle constraints, ownership boundaries, and replacement cost.
- `VOCAB-001` - Change Radius: material because the affected system surface determines who must be aligned.
- `METRIC-001` - Change Radius: material because the chapter can use affected surface to scale alignment work without
  false precision.
- `METRIC-002` - Bus Factor: material because the Principal Engineer becoming the only decision interpreter means the
  organization depends on private memory. The current canon names `METRIC-002` as Bus Factor, not Decision Quality.
- `METRIC-003` - Discoverability: material because affected teams must find the decision, owner, contract, obligations,
  and review trigger from the system behavior they are changing.
- `SMELL-001` - Silent Coupling: material because divergent team interpretations reveal hidden dependencies not
  represented as explicit contracts.
- `SMELL-004` - Hidden State: material because hidden decision state, compatibility mode state, or ownership state makes
  alignment depend on oral history.
- `ANTIPATTERN-006` - Temporary Solution: material because compatibility paths and release exceptions require owner,
  review trigger, and expiration condition.
- `FAILURE-004` - The Hero Engineer: material because the story reduces dependence on one senior engineer's private
  memory and repeated intervention.

### Rejected Concepts

- `ARTIFACT-004` - Mistake Ledger: prior mistakes may motivate alignment, but Chapter 30 is not a failure-learning
  record chapter.
- `ARTIFACT-007`, `VOCAB-002`, `VOCAB-007`, `METRIC-005`, and `RITUAL-004`: weak signals, Architecture Health, and
  Architecture Health Review belong to Chapter 31.
- `RITUAL-002` - Architecture Freeze: release hardening may appear in the story, but Chapter 19 and Chapter 24 own
  freeze and release-readiness discipline.
- `RITUAL-006` - RFC Friday: a possible forum, but Chapter 17 owns RFC practice and Chapter 28 owns ritual design.
- `LAW-006` - Unused Flexibility Is Waste: temporary compatibility may have flexibility cost, but Chapter 30's material
  lesson is ownership and alignment around decisions.
- `SMELL-005` - Platform Leakage: possible embedded example detail, but the chapter does not teach platform-boundary
  design.
- `SMELL-006` - Event Explosion: possible diagnostic example detail, but the chapter does not teach event-model design.
- `ANTIPATTERN-003` - Global Configuration: possible compatibility-mode example detail, but Chapter 30's failure is
  divergent decision interpretation rather than broad configuration ownership.
- `FAILURE-005` - The Release We Should Have Delayed: release pressure may appear, but Chapter 30 is not a
  release-readiness or delayed-release chapter.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as decision alignment, alignment around decisions, alignment contract, alignment note, affected-owner map,
obligation map, implementation promise, rollout map, decision broadcast, coordination surface, shared commitment, and
same-decision test remain chapter-local prose.

### Valid Relationship Verbs

The registered relationships use only `illustrates` and `references`, both valid PEAK relationship types in
`editor/KNOWLEDGE_MODEL.md`. `related_to` is intentionally avoided because the selected concepts are materially used
and can be named more precisely.

### Exact Proposed PEAK Relationships

Register `CHAPTER-030` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-030
  type: illustrates
  to: ARTIFACT-002

- from: CHAPTER-030
  type: references
  to: ARTIFACT-001

- from: CHAPTER-030
  type: references
  to: ARTIFACT-003

- from: CHAPTER-030
  type: references
  to: ARTIFACT-006

- from: CHAPTER-030
  type: references
  to: RITUAL-001

- from: CHAPTER-030
  type: references
  to: LAW-001

- from: CHAPTER-030
  type: references
  to: LAW-002

- from: CHAPTER-030
  type: references
  to: LAW-005

- from: CHAPTER-030
  type: references
  to: LAW-007

- from: CHAPTER-030
  type: references
  to: VOCAB-001

- from: CHAPTER-030
  type: references
  to: METRIC-001

- from: CHAPTER-030
  type: references
  to: METRIC-002

- from: CHAPTER-030
  type: references
  to: METRIC-003

- from: CHAPTER-030
  type: references
  to: SMELL-001

- from: CHAPTER-030
  type: references
  to: SMELL-004

- from: CHAPTER-030
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-030
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

Each section should serve the Chapter 30 role:

- Opening Quote: establish that alignment is shared obligation, not shared opinion.
- Story: show The Decision Everyone Agreed To Differently.
- Discussion: teach how records turn one decision into compatible work across teams.
- Engineering Principle: align teams by turning decisions into shared obligations.
- Architecture Exercise: align one cross-team decision.
- Principal's Notebook: exactly three short observations, no explanations.
- ADR: record the story-local decision to use the provisioning RFC as the alignment contract.
- Editor's Commentary: explain how Chapter 30 follows Chapters 26-29 and prepares Chapter 31 without writing it early.

## 23. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- Agreement is not alignment.
- Affected owners need obligations, not rumors.
- A decision that only you can explain is not aligned.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 24. Technical and Organizational Credibility Requirements

The future draft must treat the following accurately:

- cross-team technical decisions across firmware, backend, service tooling, manufacturing, support, tests, and release;
- distinction among decision owner, affected owner, approver, reviewer, facilitator, and implementer;
- RFC, ADR, Decision Journal, Architecture Ledger, and Architecture Review boundaries;
- API, diagnostic, timing, compatibility, and support promises;
- state ownership and compatibility-mode ownership;
- dependency consequences and sequencing constraints;
- accepted evidence, missing evidence, assumptions, confidence, and review triggers;
- proportional alignment by Change Radius;
- Discoverability of decision, owner, contract, and obligations;
- Bus Factor risk when one Principal Engineer translates the decision;
- temporary exceptions with owner and expiration condition.

Avoid misleading claims:

- alignment equals agreement;
- a meeting creates alignment by default;
- RFC approval closes all implementation questions;
- an ADR should contain every follow-up task;
- every affected team must approve every detail;
- release planning substitutes for technical alignment;
- the Principal Engineer should become the coordinator of all consequences;
- temporary exceptions are safe without review triggers.

## 25. Terminology and Precision Guardrails

Use terms precisely:

- Decision alignment: chapter-local prose for making one technical decision actionable across ownership boundaries.
- Alignment surface: chapter-local prose for the RFC, ADR, ledger row, or linked update that lets teams act from the
  same decision.
- Decision owner: the owner accountable for the technical choice and its consequences.
- Affected owner: an owner whose system surface, promise, test, process, or support behavior must change or remain
  stable because of the decision.
- Shared obligation: chapter-local prose for the work, evidence, promise, or review trigger an affected owner accepts.
- Same-decision test: chapter-local prose for asking affected teams to state the decision and their obligation in
  compatible terms.
- Temporary exception: a compatibility or release path that needs owner, evidence, review trigger, and expiration
  condition.

Avoid misleading statements:

- alignment means consensus;
- alignment means no disagreement remains;
- decision owner and implementation owner are always the same person;
- affected owners only need notification;
- every disagreement should reopen the decision;
- Discoverability means the RFC exists somewhere;
- Bus Factor is a judgment-quality metric;
- temporary compatibility can be left to team memory.

## 26. Failure Modes to Avoid

The later draft must not become:

- a generic leadership alignment essay;
- a stakeholder-management chapter;
- a meeting facilitation guide;
- a program-management checklist;
- a release-readiness chapter;
- an Architecture Freeze chapter;
- an RFC or ADR tutorial;
- a design-review chapter repeated from Chapter 27;
- an engineering-rituals chapter repeated from Chapter 28;
- a mentoring-through-artifacts chapter repeated from Chapter 29;
- an Architecture Health Review chapter written before Chapter 31;
- a platform-boundary chapter;
- an event-model chapter;
- a configuration-management chapter;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 27. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story uses a cross-team provisioning compatibility decision or an equivalent credible technical decision;
- the decision has been accepted, but teams interpret obligations differently;
- firmware, backend, service tooling, manufacturing, support diagnostics, tests, and release or field procedure impacts
  are materially visible;
- the Principal Engineer turns "send the decision around" into "what must each affected owner do, own, verify, stop,
  or revisit";
- the manuscript distinguishes alignment from consensus, approval, review attendance, release planning, program
  management, RFC mechanics, ADR writing, mentoring, rituals, and architecture health review;
- selected PEAK concepts are materially present if the registered relationship set is kept;
- `METRIC-002` is used only as Bus Factor, not Decision Quality;
- no primary PEAK concept is assigned unless a later editor decision changes repository convention;
- no new PEAK concept is implied accidentally;
- temporary exceptions have owner, evidence, review trigger, and expiration condition;
- the exercise ends with one decision statement, one affected-owner obligation, one changed or unchanged promise, one
  sequencing constraint or evidence gap, and one artifact update;
- the ADR makes a genuine story-local decision about using the provisioning RFC as the alignment surface;
- exactly three Principal's Notebook observations are present;
- Chapter 31 is previewed only lightly and not written early.

## 28. Review Handoff Notes

Editorial Review should check whether the chapter stays alive as an engineering-organization story rather than becoming
a generic alignment or communication essay. It should also check that the story shows a technically accepted decision
failing through divergent interpretation, not merely poor meeting notes.

Canon Review should verify that Chapter 30 remains no-primary, preserves only material outgoing relationships, avoids
new PEAK concepts, and keeps decision alignment, alignment surface, alignment contract, affected-owner map, obligation
map, shared obligation, and same-decision test as chapter-local prose carried by existing PEAK concepts.

Technical Review should focus on realistic cross-team decision execution: owner boundaries, API promises, compatibility
state, dependency consequences, evidence gaps, tests, support diagnostics, manufacturing or operational process, release
timing, temporary exceptions, RFC/ADR/Decision Journal/Architecture Ledger boundaries, and private-memory risk.

Freeze Review should confirm that Chapter 30 is the fifth Part V chapter, keeps the manuscript architecture intact, uses
exactly three Principal's Notebook observations, preserves the registered PEAK graph, and does not write Chapter 31
early.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
provisioning decision, affected teams, compatibility path, artifact links, ADR wording, exercise wording, and notebook
wording while preserving the aligning-teams-around-decisions thesis, PEAK map, and chapter boundaries.
