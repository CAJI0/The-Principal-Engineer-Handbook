# CHAPTER-006 Canonical Brief: Leaving Systems Better Than You Found Them

## Metadata

- Stable ID: `CHAPTER-006`.
- Title: `Leaving Systems Better Than You Found Them`.
- Expected manuscript path: `book/01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-006-leaving-systems-better-than-you-found-them.md`.
- Branch: `chapter6`.
- Canonical predecessor: `CHAPTER-005` - Technical Judgment and Evidence.
- Part position: final chapter of Part I - Thinking Like a Principal Engineer.
- Baseline `origin/main`: `749e6239c0561cf510bffc85f500261bdb287b0c`.
- Reader-facing draft created: no.
- Lifecycle status at brief-registration time: draft preparation.

## Repository-Grounded Findings

- `main` resolves to merge commit `749e6239c0561cf510bffc85f500261bdb287b0c`.
- The commit is the merge of PR #5, Chapter 5: Technical Judgment and Evidence.
- `CHAPTER-001` through `CHAPTER-005` are registered as `canonical` in `knowledge/index.yaml`.
- `editor/EDITOR_LOG.md` records Chapters 1-5 as Frozen.
- No `CHAPTER-006` manuscript or canonical brief exists on `main`.
- The repository contains canonical brief files for Chapters 4 and 5. Chapters 1-3 predate the current chapter-brief
  convention; their frozen manuscripts, PEAK records, and review history remain the available canon.
- Local branch `chapter6` was created from the verified `origin/main` baseline before this brief was registered.

## 1. Canonical Purpose

Prepare Chapter 6 to define stewardship as the discipline of completing a current engineering commitment while leaving
the system more capable of the next necessary change.

The chapter should show how a Principal Engineer notices structural cost created or exposed by ordinary delivery work
and includes a proportional improvement that reduces future cost without turning the task into an unbounded cleanup
initiative.

The chapter must reject two false choices:

1. deliver the feature and leave every surrounding weakness untouched;
2. use every feature as permission for a broad rewrite.

The canonical middle is bounded stewardship: deliver the product outcome, improve the system where the current work has
made the cost concrete, and stop when the justified improvement is complete.

## 2. Central Thesis

When a change exposes or creates structural cost, include the smallest justified improvement that reduces that cost
without displacing the product outcome.

Approved supporting formulation for the future draft:

> Leave the next necessary change cheaper, safer, or easier to understand.

This formulation is chapter-local language. Do not register it as a PEAK law, principle, maxim, metric, ritual, or
vocabulary concept.

## 3. Reader Transformation

The reader should move from treating "done" as either feature behavior delivered, or feature behavior delivered plus as
much cleanup as the engineer can justify, to a more disciplined question:

> What system cost did this work create or reveal, and what is the smallest evidence-backed improvement that should be
> completed with it?

By the end of the chapter, the reader should be able to:

1. name the current product commitment;
2. distinguish debt connected to the change from unrelated debt;
3. identify whether the work worsens a boundary, ownership model, decision record, failure visibility, or future change
   surface;
4. choose a proportional stewardship action;
5. state what remains intentionally out of scope;
6. define a stop condition;
7. show concrete evidence that the system was left easier to change, review, operate, or understand;
8. recognize when not to refactor.

## 4. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 6 covers:

- finishing the current commitment without worsening the surrounding system unnecessarily;
- noticing structural cost created or exposed by the current change;
- paying down only debt materially connected to that change;
- making one boundary clearer when the task crosses or leaks through it;
- localizing platform-specific behavior that the task would otherwise spread;
- narrowing or removing flexibility that current evidence no longer justifies;
- removing an obsolete path when its non-use and removal safety are sufficiently supported;
- preventing a helper, workaround, shared module, or temporary path from becoming architecture accidentally;
- replacing hidden decision context with a short discoverable record;
- making ownership visible where the current change reveals ambiguity;
- adding minimal diagnostic or operational feedback needed to make the changed behavior understandable;
- adding a seam for the next likely change only when the current task provides concrete evidence that the change is
  likely;
- keeping improvement increments small enough to review, test, attribute, and reverse;
- defining a clear stop condition;
- deciding deliberately not to refactor when the improvement is speculative, weakly supported, too broad, or more costly
  than the product risk it removes;
- defining evidence that the system was actually left better.

### Evidence That the System Was Left Better

The future chapter may use concrete indicators such as:

- fewer unrelated modules touched by the same class of change;
- fewer platform checks outside the intended boundary;
- a smaller or clearer regression surface;
- an obsolete flag, fallback, branch, or compatibility path removed;
- one authoritative owner or contract made visible;
- a decision and review trigger made discoverable;
- reduced dependence on one engineer's private memory;
- a failure reason or selected configuration made observable;
- the next change no longer requiring rediscovery of the same decision;
- an explicit explanation of why no additional refactoring was justified.

These are indicators, not a scoring system.

### Explicitly Out of Scope

Do not turn Chapter 6 into:

- a general cleanup philosophy;
- a code-quality or craftsmanship chapter;
- a refactoring catalog;
- a safe-deletion procedure;
- a legacy-system archaeology chapter;
- a product-line architecture chapter;
- a boundary-design playbook;
- an observability architecture chapter;
- a release-readiness or production-gating chapter;
- an Architecture Health Review process;
- an ADR, RFC, or Architecture Ledger mechanics tutorial;
- an organization-wide debt-management program;
- a rule that every task must include refactoring;
- a justification for scope expansion, gold-plating, perfectionism, or heroics;
- a rewrite story;
- a review of all PEAK laws;
- Part II, Part III, Part IV, Part V, or Part VI material written early.

## 5. Boundaries With Chapters 1-5

### Chapter 1 - What Is a Principal Engineer?

Chapter 1 defines Principal Engineering as responsibility for the future cost of the system.

Chapter 6 operationalizes that responsibility in ordinary delivery work. It asks what condition the system is left in
after the immediate change.

Do not repeat the Principal Engineer role definition, architecture as a decision-making discipline, the career-level
distinction, or the general argument that decisions create future cost.

### Chapter 2 - Decision-Making Under Constraints

Chapter 2 asks:

> Given the constraints, consequences, uncertainty, and reversal cost, what should we commit to?

Chapter 6 asks:

> While fulfilling that commitment, what proportional improvement should prevent the work from making the next change
> harder?

Chapter 6 may use consequence, reversibility, scope, and accepted cost to bound stewardship. It must not repeat the
decision framework, option comparison, constraint classification, or commitment selection process.

### Chapter 3 - Asking Better Engineering Questions

Chapter 3 teaches how to expose assumptions and make an investigation answerable.

Chapter 6 may show that a well-stewarded change leaves the next engineer with a clearer boundary, a discoverable
decision, a visible owner, a more observable failure, or less hidden context.

It must not reteach inquiry framing, discriminating questions, root-cause investigation, or observation-versus-
interpretation.

### Chapter 4 - Ownership Beyond Code

Chapter 4 asks whether a bounded outcome has an owner and reaches visible closure.

Chapter 6 asks what condition the system and its future change capacity are left in after closure.

The distinction must remain explicit:

- Chapter 4: did the outcome reach durable closure?
- Chapter 6: did completing the outcome unnecessarily increase future cost, or did it leave a proportional improvement
  behind?

Chapter 6 may make ownership visible when the current change exposes ambiguity. It must not redefine ownership, handoff
acceptance, component ownership, outcome ownership, or closure.

### Chapter 5 - Technical Judgment and Evidence

Chapter 5 teaches claim-evidence alignment and confidence calibration.

Chapter 6 uses evidence as a guardrail to justify that an improvement is needed, avoid preference-driven cleanup,
support removal of an obsolete path, verify that the improvement reduced relevant cost, and decide when no refactoring
is justified.

It must not repeat evidence-quality dimensions, confidence calibration, weak-signal reasoning, experimental design, or
staged-commitment logic.

## 6. Boundary With Part II and Later Parts

### Part II - The Laws

Chapter 6 closes Part I by showing why stable engineering laws are needed in daily work.

It may apply `LAW-004` - Simplicity Is a Feature, `LAW-006` - Unused Flexibility Is Waste, and existing ownership, API,
dependency, time, and evidence laws where naturally relevant.

It must not summarize or systematically teach Part II. The transition should be:

1. Part I establishes how a Principal Engineer thinks and acts.
2. Chapter 6 shows what those habits should leave behind in the system.
3. Part II names the durable laws that repeatedly support those choices.

### Part III - Architecture Playbook

Leave detailed treatment of boundary design, formal Change Radius analysis, failure and recovery architecture, ADR and
RFC mechanics, Architecture Review, and Architecture Freeze to Part III.

Chapter 6 may show a small boundary correction but must focus on proportional stewardship scope, not boundary-design
technique.

### Part IV - Building a Product

Leave prototype-to-product transition, product-line and variant architecture, manufacturing and field reality, embedded
observability, release discipline, and upgrade paths to Part IV.

The Chapter 6 story may use a board revision or peripheral variant as context. It must not become a product-line design
chapter.

### Part V - Engineering Organization

Leave leadership without authority, design reviews as shared memory, recurring engineering rituals, mentoring through
artifacts, team alignment, and organization-level Architecture Health Reviews to Part V.

Chapter 6 should remain focused on the state of the engineering system after a bounded change.

### Part VI - Legacy

Leave reading legacy systems, Silent Coupling, Utility Gravity as a broad legacy pattern, Boolean Explosion, safe
deletion, and trust-preserving refactoring to Part VI.

Chapter 6 may use Utility Gravity or Platform Leakage in one current-change story. It must not teach the full legacy
recovery method.

## 7. Recommended Embedded-Systems Story

### Working Title

One More Board Revision

### System

An industrial controller gains a new board revision because the existing external power-monitor device is unavailable or
no longer preferred for the next production run.

The replacement device reports similar product-level information but differs in startup timing, status interpretation,
reset behavior, error reporting, and one diagnostic capability.

### Existing Condition

A shared support module has gradually accumulated:

- board-ID checks;
- power-good interpretation;
- retry timing;
- fallback behavior;
- diagnostic text;
- feature flags;
- product-specific conditionals.

The module was once a convenient helper. It now exhibits Utility Gravity, Platform Leakage, growing Change Radius, one
obsolete prototype fallback, and a configuration option no shipped product uses.

### Fast Local Path

The feature can be delivered by adding another board-revision conditional, another platform-specific status check,
another configuration flag, and another fallback branch.

The patch is small in line count and likely passes current tests. It also makes the next board revision harder, spreads
platform behavior further into shared product code, and preserves unused flexibility.

### Wrong Opposite Reaction

A broad rewrite of startup, diagnostics, board detection, and platform abstraction would exceed the product need,
disturb validated behavior, and convert stewardship into an architecture initiative.

### Principal Engineer Intervention

The Principal Engineer keeps the product commitment intact and defines one proportional improvement:

1. keep shared boot orchestration expressed in product-level terms;
2. localize device-specific power-monitor behavior behind one owned boundary;
3. remove the obsolete prototype fallback after verifying it is unused;
4. remove or narrow the unused configuration option;
5. record why the boundary exists and what would trigger revisiting it;
6. add minimal boot diagnostics that expose the selected monitor path and a product-level failure reason;
7. leave unrelated cleanup in the shared module out of scope.

### Outcome

The new board revision is delivered.

The system is not "clean" or "finished," but it is observably better:

- the new platform check is not duplicated across product code;
- one obsolete path and one unjustified option are gone;
- the selected implementation and failure reason are visible;
- the decision is discoverable;
- the next similar peripheral change has a clearer location and smaller expected review surface;
- unrelated utility debt remains visible but intentionally out of scope.

### Why This Story Fits

The story is distinct from Chapter 2's constrained update-memory decision, Chapter 3's stale-state investigation,
Chapter 4's cross-team diagnostic ownership, and Chapter 5's flash-logging evidence judgment.

It also avoids consuming the later product-line, observability, boundary-design, safe-deletion, and legacy-refactoring
chapters because the technical correction stays deliberately small.

## 8. Expected Discussion Arc

1. **The task can be locally correct and systemically expensive.**
   Introduce the tempting conditional patch and show the future cost it creates.
2. **Stewardship is not cleanup.**
   Separate product delivery, necessary structural correction, and unrelated debt.
3. **Use the current change as evidence.**
   The task has made a specific weakness concrete: platform behavior has leaked, the shared module has attracted another
   responsibility, and unused flexibility is consuming attention.
4. **Choose the smallest leverage point.**
   Compare another local patch, a full rewrite, and one bounded correction.
5. **Improve only the surface connected to the commitment.**
   Localize the platform behavior, remove one supported deletion candidate, narrow one unused option, and record intent.
6. **Make the improvement reviewable and attributable.**
   Keep feature behavior and stewardship action visible in the same change without mixing unrelated cleanup.
7. **Define the stop condition.**
   Stop when the product commitment is met, the exposed structural cost is reduced, evidence exists, and further cleanup
   is no longer causally connected to the task.
8. **Recognize when not to refactor.**
   Do not generalize for hypothetical variants, rewrite validated paths, or remove behavior without sufficient evidence.
9. **Prove "better" with concrete indicators.**
   Use Change Radius, Discoverability, removed branches/options, explicit ownership, and failure visibility without
   inventing a composite score.
10. **Close Part I.**
    Connect role, constraints, questions, ownership, evidence, and stewardship into one operating model, then transition
    to the Laws.

## 9. Engineering Principle Target

Target chapter-local principle:

> When a change exposes or creates structural cost, include the smallest justified improvement that reduces that cost
> without displacing the product outcome.

Supporting formulation:

> Leave the next necessary change cheaper, safer, or easier to understand.

Required trade-off:

- Too little stewardship externalizes avoidable cost to future engineers.
- Too much stewardship hides scope expansion behind architectural language.
- Proportional stewardship improves a concrete future cost and then stops.

Do not register these formulations as new PEAK entities.

## 10. Architecture Exercise Target

### Working Title

Define a Bounded Stewardship Action

Ask the reader to choose one current or recent engineering change and record:

1. the product commitment;
2. the system surface the change touches;
3. structural cost created or exposed by the change;
4. evidence that the cost is real rather than a personal preference;
5. the smallest improvement that would reduce that cost;
6. expected effect on boundary clarity, Change Radius, Discoverability, ownership, or failure visibility;
7. debt deliberately left out of scope;
8. behavior that must not change;
9. validation needed for the product outcome;
10. validation needed for the stewardship action;
11. the stop condition;
12. the decision record or review trigger that preserves intent.

Required final question:

> What is the smallest improvement you can include now that leaves the next necessary change cheaper without turning
> this task into a rewrite?

The exercise is chapter-local. Do not create a canonical artifact named Stewardship Plan, Better-System Review,
Improvement Budget, or similar.

## 11. Chapter-Local ADR Brief

### Working Title

Localize Power-Monitor Variation While Delivering the New Board Revision

### Context

- A new board revision uses a different external power-monitor device.
- Existing shared boot code contains board checks, device quirks, retry timing, diagnostic text, fallback behavior, and
  unused configuration.
- Another conditional patch would deliver the feature but increase platform leakage and future review surface.
- A broad startup-system rewrite would exceed the commitment and disturb validated behavior.

### Decision

- Deliver support for the new board revision.
- Keep shared boot orchestration expressed in product-level power-health terms.
- Place device-specific interpretation and timing behind one owned platform boundary.
- Remove the verified-unused prototype fallback.
- Remove or narrow the unused monitor-selection option.
- Record the decision, owner, remaining limitation, and review trigger.
- Expose the selected implementation and product-level initialization failure reason.
- Do not refactor unrelated startup, logging, or diagnostic responsibilities in this change.

### Alternatives Considered

- Add another board-revision conditional to the shared module.
- Introduce a generic plug-in framework for possible future monitors.
- Rewrite the complete startup and diagnostic subsystem.
- Deliver only the feature and defer every structural correction.
- Keep the obsolete fallback and unused option "for safety."

### Consequences

Benefits:

- the product commitment remains deliverable;
- platform-specific behavior has a clearer location;
- one obsolete path and one unjustified option are removed;
- future review and test scope become easier to identify;
- the selected path and failure reason are observable;
- decision intent is discoverable.

Costs:

- the change is larger than the minimum feature patch;
- the new boundary requires focused tests;
- some shared-module debt remains;
- the boundary may need revision if future devices differ materially from the current product-level contract.

The ADR is story-local and reader-facing. It must not become a repository-level ADR or a tutorial on ADR mechanics.

## 12. PEAK Concept Map

### Primary Concepts

- `VOCAB-007` - Architecture Health: defines "better" as improved ability to absorb necessary change without
  disproportionate cost.
- `LAW-004` - Simplicity Is a Feature: supports removing unnecessary behavior and keeping future work reviewable.
- `LAW-006` - Unused Flexibility Is Waste: supports narrowing or removing options not justified by real uncertainty.
- `VOCAB-001` - Change Radius: provides shared language for the future surface affected by similar changes.
- `METRIC-001` - Change Radius: provides an approximate, non-precise indicator that the improvement changed the review
  or retest surface.
- `METRIC-003` - Discoverability: supports recording the decision, owner, boundary, and review trigger so the next
  engineer does not repeat the investigation.
- `SMELL-002` - Utility Gravity: describes the shared helper accumulating unrelated behavior.
- `SMELL-005` - Platform Leakage: describes device-specific behavior escaping into product-level code.
- `ANTIPATTERN-006` - Temporary Solution: provides the guardrail that a workaround needs an owner, review trigger, and
  removal condition.
- `ARTIFACT-003` - Decision Journal: provides a lightweight record when the bounded improvement does not require a full
  architecture-governance process.

### Supporting Concepts Only If Materially Used

- `ARTIFACT-001` - ADR.
- `ARTIFACT-006` - Architecture Ledger.
- `METRIC-002` - Bus Factor.
- `METRIC-005` - Architecture Health.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `RITUAL-003` - Deletion Day.
- `RITUAL-004` - Architecture Health Review.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `FAILURE-001` - Logger That Became a Platform.
- `FAILURE-003` - The Successful Prototype.
- `FAILURE-004` - The Hero Engineer.
- `FAILURE-005` - The Release We Should Have Delayed.
- `LAW-005` - Evidence Before Confidence.

Do not force supporting concepts into the manuscript merely to increase relationship count.

## 13. Exact Proposed PEAK Relationships

Register `CHAPTER-006` as a `draft` chapter and propose exactly these relationships during brief registration:

```yaml
- from: CHAPTER-006
  type: references
  to: VOCAB-007

- from: CHAPTER-006
  type: illustrates
  to: LAW-004

- from: CHAPTER-006
  type: illustrates
  to: LAW-006

- from: CHAPTER-006
  type: references
  to: VOCAB-001

- from: CHAPTER-006
  type: references
  to: METRIC-001

- from: CHAPTER-006
  type: references
  to: METRIC-003

- from: CHAPTER-006
  type: illustrates
  to: SMELL-002

- from: CHAPTER-006
  type: illustrates
  to: SMELL-005

- from: CHAPTER-006
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-006
  type: references
  to: ARTIFACT-003
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 14. Decision on New PEAK Concepts

No new PEAK concept is required.

The current graph already provides:

- the desired outcome through Architecture Health;
- future-change surface through Change Radius;
- knowledge accessibility through Discoverability;
- simplification and option cost through `LAW-004` and `LAW-006`;
- the primary structural smells through Utility Gravity and Platform Leakage;
- temporary-work guardrails through `ANTIPATTERN-006`;
- lightweight system memory through the Decision Journal.

A new Stewardship concept is not yet justified because:

1. the chapter can define stewardship by combining existing concepts;
2. the proposed names overlap existing Architecture Health, Change Radius, Decision Journal, and review-trigger
   semantics;
3. no stable cross-book usage has yet demonstrated a semantic gap;
4. no separate artifact, ritual, or metric is required to make the chapter usable;
5. allocating a stable ID now would encode chapter-local wording before repeated use proves it canonical.

## 15. How Chapter 6 Closes Part I

Part I should end with a complete operating sequence:

1. Chapter 1 - accept responsibility for the future cost of the system.
2. Chapter 2 - make constrained commitments explicit.
3. Chapter 3 - ask questions that expose hidden assumptions.
4. Chapter 4 - ensure bounded outcomes have ownership and reach closure.
5. Chapter 5 - calibrate confidence to evidence.
6. Chapter 6 - complete the work in a way that leaves the next necessary change cheaper, safer, or easier to understand.

The final movement should not say that a Principal Engineer keeps every system clean.

It should say that principal-level thinking changes what remains after the work:

- decisions are more visible;
- boundaries are less accidental;
- unused options are less likely to survive by inertia;
- failures are easier to interpret;
- ownership is easier to find;
- future work requires less rediscovery.

The transition to Part II should explain that these outcomes are not produced by taste alone. They depend on durable laws
that can be applied repeatedly across systems and teams.

## 16. Canon Review Acceptance Criteria

Canon Review should ask:

> Does the chapter teach proportional stewardship while preserving product delivery and avoiding cleanup theatre,
> gold-plating, and a premature legacy-refactoring chapter?

Acceptance criteria:

- The chapter teaches one central idea.
- The product commitment remains visible and is actually delivered.
- The stewardship action is tied to structural cost created or exposed by the current change.
- The improvement is proportional, bounded, reviewable, and attributable.
- Unrelated cleanup remains explicitly out of scope.
- A clear stop condition exists.
- The chapter explains when not to refactor.
- The story does not present a broad rewrite as principal-level behavior.
- The story does not present another local conditional as harmless.
- Platform Leakage and Utility Gravity are materially illustrated, not merely named.
- Simplicity and removal of unused flexibility are connected to future product capability, not aesthetic preference.
- "Better" is supported by concrete indicators rather than a composite score.
- Change Radius is used without false precision.
- Discoverability is improved through a short decision record, not duplicated documentation.
- Operational feedback remains minimal and does not become an observability chapter.
- Deletion remains narrow and evidence-supported and does not become a safe-deletion tutorial.
- The chapter-local ADR records a real bounded decision, alternatives, and consequences.
- The exercise can be applied to ordinary engineering work.
- The Principal's Notebook contains exactly three short observations.
- No new PEAK concept is introduced.
- The exact relationship set contains only concepts materially used by the final manuscript.
- Chapters 1-5 remain Frozen and unchanged.
- Existing PEAK concept files and `editor/CANON.md` remain unchanged.
- No canonical manuscript is duplicated under `docs/`.
- The chapter closes Part I and creates a natural transition to Part II without teaching Part II early.

## Concepts Considered but Rejected From the Primary Map

- `RITUAL-003` - Deletion Day: deletion may appear as one bounded action, but the ritual and safe-deletion process
  belong later.
- `RITUAL-004` - Architecture Health Review: organization-level recurring review belongs to Part V.
- `ARTIFACT-004` - Mistake Ledger: the recommended story is not incident or failure-learning centered.
- `ARTIFACT-006` - Architecture Ledger: useful for larger decision inventories, but unnecessary for one bounded story.
- `ARTIFACT-007` - Weak Signal Register: Chapter 5 already owns weak-signal evidence treatment.
- `SMELL-001` - Silent Coupling: potentially relevant, but not required for the recommended story and heavily reserved
  for Part VI.
- `SMELL-004` - Hidden State: not central to the recommended peripheral-variation problem.
- `METRIC-002` - Bus Factor: Chapter 4 already gives it a primary role.
- `METRIC-005` - Architecture Health: considered as a metric edge, but concrete Change Radius and Discoverability
  indicators are more useful here and avoid implying one health score.
- `FAILURE-001` - Logger That Became a Platform: relevant to accidental platforms, but another logger story would repeat
  Chapter 5's domain.
- `FAILURE-003` - The Successful Prototype: already central to Chapter 5 and belongs more fully to Part IV.
- `FAILURE-004` - The Hero Engineer: already central to Chapter 4.
- `FAILURE-005` - The Release We Should Have Delayed: would shift the chapter toward release discipline.
- `LAW-005` - Evidence Before Confidence: remains a prerequisite and guardrail, but Chapter 6 should not repeat Chapter
  5 or add an edge unless the final manuscript materially teaches the law again.
- `ARTIFACT-001` - ADR: the chapter contains the required story-local ADR, but ADR mechanics are not a teaching target.
  Add an edge only if the Discussion materially uses ADRs as system memory beyond the required chapter section.

## Chapter-Local Formulations

Keep these as ordinary prose unless a later cross-book Canon Review proves stable reuse:

- stewardship;
- bounded stewardship;
- proportional stewardship;
- proportional improvement;
- bounded cleanup;
- stewardship action;
- stewardship budget;
- better-system rule;
- improvement radius;
- change dividend;
- future-cost ledger;
- leave-it-better check;
- local stewardship;
- system improvement score;
- next-change cost;
- exposed debt;
- change-connected debt.

Do not allocate stable IDs for these terms during Chapter 6 preparation or Draft.

## Largest Duplication Risks

1. **Chapter 4:** turning stewardship into another ownership-and-closure chapter.
2. **Chapter 5:** reteaching evidence quality instead of using evidence as a guardrail.
3. **Part III:** expanding the small boundary correction into a boundary-design playbook.
4. **Part IV:** turning the board-revision story into product-line architecture or embedded observability.
5. **Part V:** turning system memory into organization-wide review rituals.
6. **Part VI:** turning proportional improvement into a legacy refactoring or safe-deletion chapter.
7. **Part II:** summarizing all laws instead of preparing the reader to receive them.

## Author Decisions

No blocking author decision is required before brief registration.

The recommended story, scope, principle, exercise, ADR, and PEAK map are sufficiently resolved from repository canon.

During Author Draft, the author may adjust:

- exact product and peripheral names;
- whether the new board revision is driven by supply, qualification, or product need;
- the precise obsolete fallback removed;
- final quote and Principal's Notebook wording.

Any alternative story must preserve:

- current product delivery;
- one concrete structural cost exposed by the task;
- a bounded correction rather than a rewrite;
- evidence of improved future change capacity;
- the same adjacent-chapter and later-part boundaries.

## Final Scope Statement

Chapter 6 should define stewardship as completing today's commitment while making a proportional, evidence-backed
reduction in the future cost that the change creates or exposes.

The chapter should show a Principal Engineer delivering a new embedded-system variant without adding another accidental
architectural path, making one boundary clearer, removing one unsupported option or obsolete path, preserving decision
context, adding only the minimum useful feedback, and stopping before the work becomes an unrelated refactoring
initiative.

The system does not need to become perfect.

It must become easier for the next necessary change.
