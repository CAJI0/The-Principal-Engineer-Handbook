# CHAPTER-012 Canonical Brief: Simplicity Is a Feature

## Metadata

- Stable ID: `CHAPTER-012`.
- Title: `Simplicity Is a Feature`.
- Part: Part II - The Laws.
- Chapter number: 12.
- Expected manuscript path: `book/02-the-laws/12-simplicity-is-a-feature.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-012-simplicity-is-a-feature.md`.
- Branch: `chapter12`.
- Canonical predecessor: `CHAPTER-011` - Unused Flexibility Is Waste.
- Part position: sixth chapter of Part II - The Laws.
- Verified baseline `origin/main`: `e00d5351488799949a873e605d6256b4e1e64940`.
- Reader-facing draft created: no.
- Primary law: `LAW-004` - Simplicity Is a Feature.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## Repository-Grounded Findings

- `origin/main` resolves to `e00d5351488799949a873e605d6256b4e1e64940`.
- That baseline is the PR #13 squash commit, `Chapter 11: Unused Flexibility Is Waste (#13)`.
- The Chapter 11 feature-branch Freeze commit `9dfc705946e452dbfb373a351593e8a866e43576` is not required to be an
  ancestor of `main` because PR #13 used squash merge.
- The final Chapter 11 lifecycle files in the PR #13 squash commit are tree-equivalent to the final feature-branch
  Freeze commit for the checked Chapter 11 paths.
- `CHAPTER-001` through `CHAPTER-011` are registered as `canonical` in `knowledge/index.yaml`.
- Chapter 11 exists at `book/02-the-laws/11-unused-flexibility-is-waste.md`.
- `editor/EDITOR_LOG.md` records Chapter 11 Editorial, Canon, Technical, and Freeze Review entries in order.
- The repository table of contents lives at `book/00-front-matter/table-of-contents.md` and places `Simplicity Is a
  Feature` after `Unused Flexibility Is Waste` in Part II.
- `LAW-004` exists exactly once and is named `Simplicity Is a Feature`.
- `LAW-004` states that simplicity is a product capability because it makes future change safer.
- `LAW-004` already relates to Deletion Day, Utility Gravity, and Architecture Health in its law file.
- `CHAPTER-012` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 12 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter12` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 1. Canonical Purpose

Prepare Chapter 12 to teach the sixth Part II law: simplicity is a product capability, not an aesthetic preference.

The chapter should move the reader from judging simplicity by line count, familiarity, or local convenience toward a
system-level question: how many concepts must be understood together before the product behavior can be safely changed,
tested, operated, explained, and recovered?

The chapter must not create a reader-facing draft during this task. It must constrain the later Author Draft.

## 2. Exact Law Statement

`LAW-004` states:

> Simplicity is a product capability because it makes future change safer.

Chapter 12 should preserve that law while making "product capability" concrete: faster safe change, shorter diagnosis,
clearer ownership, better tests, more reliable releases, safer recovery, easier ramp-up, stronger review, and lower
support cost.

## 3. Central Thesis

A simple system makes important behavior visible, localizes decisions, reduces the number of concepts needed to reason
about change, and lowers the cost of operating, testing, explaining, recovering, and evolving the product.

Approved supporting formulation for the future draft:

> Prefer the design that makes product behavior, ownership, and consequences easiest to explain and safely change.
> Preserve essential complexity; remove accidental concepts.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 4. Reader Transformation

Before the chapter, the reader may think:

1. simplicity means fewer lines, fewer files, or fewer layers;
2. familiar code is simple because it is easy for the original author;
3. a generic manager or utility makes the system simpler because everyone calls one thing;
4. abstraction count measures simplicity;
5. explicit product decisions are messy compared with generic routing;
6. tests that mock every layer prove the product behavior;
7. diagrams or low file count prove a design is simple;
8. simplification usually means a rewrite.

By the end of the chapter, the reader should be able to:

1. define simplicity as an architectural property tied to safe future change;
2. distinguish easy now from simple over time;
3. distinguish simple from simplistic;
4. preserve essential complexity while removing accidental concepts;
5. evaluate local elegance against system-level reasoning cost;
6. identify product decisions hidden inside utilities, managers, callbacks, and configuration;
7. use Change Radius, Discoverability, and Architecture Health as signals of simplicity;
8. choose small, reviewable simplifications instead of heroic rewrites.

## 5. Semantic Definition of Simplicity

Simplicity is the property that lets the system's important behavior be explained, changed, tested, operated, diagnosed,
and recovered with a small, truthful set of concepts.

Architectural simplicity may appear as:

- few concepts required to explain behavior;
- explicit ownership;
- direct control flow for ordinary behavior;
- visible state transitions;
- bounded interfaces;
- limited coupling;
- discoverable decisions;
- local failure behavior;
- proportionate abstraction;
- one clear path for ordinary operation;
- intentional exceptional paths;
- product vocabulary instead of generic infrastructure vocabulary;
- ability to explain behavior during incidents and reviews.

Simplicity does not necessarily mean:

- small codebase;
- no abstraction;
- no layers;
- no configuration;
- one module;
- one process;
- one technology;
- duplicated logic;
- minimal up-front design;
- direct hardware access everywhere.

## 6. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 12 covers:

- simplicity as a product capability and architecture property;
- important behavior being visible, explainable, and safe to change;
- simple versus easy, simplistic, compact, concise, explicit, and verbose;
- essential versus accidental complexity;
- local simplicity versus system simplicity;
- proportionate abstraction and harmful indirection;
- utility areas, manager layers, event routing, callbacks, global context, and configuration that hide product decisions;
- product-level vocabulary and ownership;
- ordinary paths and intentional exceptional paths;
- Change Radius, Discoverability, and Architecture Health as signals;
- tests and diagnostics aligned with product behavior;
- deletion, narrowing, migration, and ownership as maintenance of simplicity;
- a scoped ADR for collapsing command routing into one product-owned decision path.

### Explicitly Out of Scope

Do not turn Chapter 12 into:

- a style guide;
- a fewer-lines argument;
- a ban on abstractions;
- a repetition of Chapter 11's unused-flexibility audit;
- a "clever code is bad" essay;
- a generic KISS or YAGNI article;
- a full state-ownership chapter;
- a full API-compatibility chapter;
- a full dependency-selection chapter;
- a full timing or event-ordering chapter;
- a full evidence-quality chapter;
- a Deletion Day playbook;
- an Architecture Health Review playbook;
- a legacy refactoring program;
- a product-configuration or manufacturing architecture chapter;
- a framework-design tutorial.

Those topics may appear only where they clarify simplicity as safe future change.

## 7. Simple, Easy, Simplistic, and Explicit

The future draft must distinguish:

- easy now: locally convenient, familiar, quick to call, or quick to patch;
- simple over time: few interacting concepts and clear consequences;
- simplistic: important distinctions removed until behavior becomes ambiguous or unsafe;
- explicit: visible product decisions, states, boundaries, and consequences;
- concise: few words or lines;
- compact: dense representation;
- understandable: explainable by the intended maintainers under real pressure.

A global helper may be easy to call and make the system less simple. A small boundary may require effort now and make
future behavior easier to reason about. One generic `status` value may be simplistic, while explicit states with clear
transitions may be simpler. Explicit code may be longer and still simpler.

Do not reward verbosity for its own sake. The point is truthful explanation, not maximal words.

## 8. Essential and Accidental Complexity

Essential complexity comes from real product behavior, hardware constraints, protocols, safety, timing, manufacturing,
field lifetime, recovery, support, or operations.

Accidental complexity comes from:

- duplicated concepts;
- indirect control flow;
- unnecessary frameworks;
- leaked platform details;
- hidden state;
- compatibility paths with no consumers;
- abstractions without a clear decision boundary;
- manager layers that only forward calls;
- callback chains that hide ordinary behavior;
- configuration that recreates code structure at runtime;
- utility modules that accumulate product decisions.

The chapter must not imply all complexity can be removed. A simple system preserves necessary distinctions while removing
accidental concepts.

## 9. Simplicity as Product Capability

The future draft must connect simplicity to product outcomes:

- faster safe change;
- fewer regression surfaces;
- shorter diagnosis;
- clearer support behavior;
- more reliable releases;
- easier variant reasoning;
- lower ramp-up cost;
- safer recovery;
- better review quality;
- clearer manufacturing and field behavior;
- less reliance on oral history.

Developer comfort may appear, but the chapter should not reduce the argument to developer happiness.

## 10. Local and System-Level Simplicity

A locally elegant abstraction may increase system-wide complexity. A locally repetitive implementation may reduce hidden
coupling. The chapter should teach readers to evaluate simplicity at the system level:

- Which product decision is being made?
- Which concepts must a reviewer hold together?
- Where is ownership?
- How many files, modules, services, modes, tools, or teams participate?
- How far does a change travel?
- Which failure paths exist?
- Which entry paths apply the decision?
- Can behavior be explained without implementation archaeology?

Local neatness is not enough. The product pays for the total reasoning surface.

## 11. Abstraction, Indirection, and Vocabulary

Abstraction is useful when it:

- names a stable concept;
- protects a meaningful boundary;
- reduces duplicated reasoning;
- narrows change radius;
- preserves dependency direction;
- makes testing or ownership clearer;
- keeps platform details behind a product-level edge.

Abstraction harms simplicity when it:

- hides ordinary control flow;
- generalizes one case without evidence;
- mirrors platform concepts;
- adds managers, registries, factories, callbacks, or event routing without reducing system concepts;
- spreads generic vocabulary into product logic;
- creates extension points no owned variation uses;
- makes diagnostics describe forwarding steps instead of product decisions.

Do not treat abstraction count as the measure of simplicity.

## 12. Ownership, Control Flow, and Decision Paths

The recommended chapter story should focus on a product command whose safe acceptance depends on calibration state.

The Principal Engineer should recast the design question from:

> Where should this condition go?

to:

> What product decision is being made, who owns it, and what is the shortest truthful path from input to consequence?

The future draft should show that simplicity improves when the decision owner, ordinary path, exceptional paths, platform
edge, tests, and diagnostics all name the same product behavior.

## 13. Change Radius, Testing, Diagnostics, and Recovery

Change Radius (`VOCAB-001` and `METRIC-001`) should make simplicity observable. A design is not simple if a small product
rule requires touching unrelated forwarding layers, mocks, configuration, utilities, logs, and support documentation.

Discoverability (`METRIC-003`) matters because simple systems let engineers find the decision, owner, and contract
behind behavior without archaeology.

Architecture Health (`VOCAB-007` and `METRIC-005`) matters because simplicity is part of the system's ability to absorb
necessary change at acceptable cost.

Tests should describe product behavior, not merely prove that layers forward calls. Diagnostics should explain why the
decision occurred, not only which infrastructure step emitted a message. Recovery behavior should remain explicit enough
that simplification does not erase necessary failure distinctions.

## 14. Simplicity Across the Product Lifecycle

A design may be simple at prototype stage and become complex as the product evolves. The chapter should cover how
simplicity is maintained through:

- review;
- deletion;
- narrowing;
- migration;
- ownership;
- documentation;
- health checks;
- refusal of accidental concepts;
- renaming generic vocabulary into product language;
- preserving records for decisions that still affect change.

Do not turn this into the complete Architecture Health Review, Deletion Day, or legacy refactoring playbook.

## 15. Boundaries With Chapters 1-11

### Chapters 1-5 - Principal Engineering Foundations

Chapter 12 may use role clarity, constrained decisions, better questions, ownership, and evidence as premises. It must
not repeat the Part I mindset chapters. Simplicity as safe future change is the subject.

### Chapter 6 - Leaving Systems Better Than You Found Them

Chapter 6 owns stewardship and incremental improvement. Chapter 12 may show simplification as product work, but it must
not repeat the general stewardship argument or teach every bounded-improvement tactic.

### Chapter 7 - Every State Has One Owner

Chapter 7 owns state authority. Chapter 12 may use explicit ownership and visible state transitions as simplicity
mechanisms, but it must not reteach one-owner semantics.

### Chapter 8 - Every API Is a Promise

Chapter 8 owns observable contracts. Chapter 12 may discuss narrower interfaces and product vocabulary, but it must not
retell compatibility, promise semantics, migration, or versioning.

### Chapter 9 - Every Dependency Is a Decision

Chapter 9 owns dependency commitments, imported behavior, lifecycle cost, and replacement cost. Chapter 12 may show that
dependency spread increases concepts and change radius, but it must not repeat dependency selection.

### Chapter 10 - Time Is a Dependency

Chapter 10 owns temporal semantics. Chapter 12 may mention callback ordering, deferred hardware completion, and recovery
only as part of the story's simplicity problem, not as a timing law.

### Chapter 11 - Unused Flexibility Is Waste

Chapter 11 owns unused options, unjustified optionality, unsupported modes, dormant paths, combinatorial variation, and
evidence and ownership for retained flexibility.

Chapter 12 owns the broader system property: comprehensibility, visible behavior, direct decision paths, bounded
concepts, easier operation, safer change, clearer recovery, and better review. It may refer to removing unused paths as
one simplification technique, but it must not become another flexibility audit.

## 16. Boundary With Evidence Before Confidence

Chapter 13 - `Evidence Before Confidence` will own evidence quality, confidence calibration, proof standards,
experiments, weak signals, and staged learning.

Chapter 12 may use change radius, tests, diagnostics, and the ability to explain behavior as evidence that a design is
simple enough to change safely. It must not define the complete evidence model or turn simplicity into a proof framework.

## 17. Boundaries With Later Parts

Part III should retain full boundary-drawing, change-radius management, failure and recovery design, ADR/RFC practice,
architecture review, and freeze playbooks.

Part IV should retain product configuration, variants, manufacturing architecture, observability, release discipline, and
reference-project implementation.

Part VI should retain utility-gravity recovery, Boolean Explosion reduction, broad deletion, and legacy refactoring
methods.

Chapter 12 may illustrate these concerns, not provide the complete remediation playbook.

## 18. Recommended Embedded-Systems Story

### Working Title

The Command Path That Looked Clean

### System

Use an embedded control subsystem that begins with a direct and understandable control path:

- input arrives;
- validation occurs;
- the state owner decides;
- a hardware command is issued;
- the result is reported.

As the product grows, reasonable local changes add:

- a global service locator;
- manager modules;
- generic command objects;
- callback registries;
- event forwarding;
- platform wrappers;
- configuration-driven routing;
- utility helpers;
- pass-through adapters;
- fallback paths;
- a shared context object.

Each addition solves a local problem. No single change appears absurd.

### Trigger

A field issue requires a small behavioral change:

> Reject one unsafe command while calibration is active, but preserve diagnostics and existing recovery behavior.

The change seems local. The engineer discovers that command acceptance depends on UI state, configuration, manager state,
an event callback, a global context flag, a utility helper, a platform wrapper, deferred hardware completion, and logging
side effects.

### Consequences

The story should show:

- no single component can explain the decision;
- several paths encode similar but different rules;
- tests mock layers instead of product behavior;
- reviewers cannot establish the real change radius;
- failure recovery differs by entry path;
- logs show forwarding steps rather than the product decision;
- the small patch touches many modules;
- safe behavior depends on hidden ordering.

### Tempting But Inadequate Response

The team initially proposes:

- add another manager;
- add a new callback;
- add a Boolean flag;
- add a generic policy interface;
- route everything through one central module;
- move logic into a utility;
- document the call sequence;
- add more mocks;
- rewrite everything in a new framework;
- duplicate the path for calibration mode.

Those responses may move complexity rather than remove it.

### Principal Engineer Intervention

The Principal Engineer maps the real decision path, identifies the state owner, removes pass-through abstractions,
collapses duplicated policies, replaces generic vocabulary with product language, and makes the command decision
explicit.

The solution should:

- keep platform details behind one bounded integration edge;
- define one ordinary path and intentional exceptional paths;
- align tests with product behavior;
- improve diagnostics around the decision;
- preserve essential hardware and recovery complexity;
- record a scoped ADR;
- schedule broader deletion only where evidence supports it.

The solution is not a heroic rewrite. The point is to reduce the concepts needed to explain and safely change the
behavior.

## 19. Expected Discussion Arc

1. Complexity accumulates through reasonable local decisions.
2. The product pays for all concepts that must be understood together.
3. Simple is not the same as short, familiar, compact, or easy.
4. Simplicity preserves necessary distinctions and removes accidental ones.
5. Local abstraction can increase system complexity.
6. Ownership and direct decision paths make behavior simpler.
7. Change Radius reveals whether simplicity is real.
8. Tests and diagnostics should describe product behavior, not forwarding layers.
9. Deletion and narrowing are design work.
10. Simplicity must be maintained as the product evolves.
11. Simplicity becomes a feature when it makes future change safer.

These are intellectual progression points, not mandatory manuscript headings.

## 20. Law Applicability

The law applies to:

- control flow;
- state transitions;
- service boundaries;
- module structure;
- manager layers;
- utility modules;
- event routing;
- callbacks;
- command handling;
- configuration;
- diagnostics;
- tests;
- platform isolation;
- error handling;
- recovery behavior;
- build and release understanding;
- support workflows;
- team ramp-up;
- architectural vocabulary.

The law is proportional. Not every indirection or long function is an architectural simplicity issue. Review depth should
match consequence of misunderstanding, change frequency, number of interacting concepts, cross-team ownership, field
lifetime, recovery difficulty, operational impact, safety implications, change radius, support involvement, and
manufacturing involvement.

## 21. Law Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- fewer lines are always simpler;
- fewer modules are always simpler;
- one layer is always better than several;
- all abstractions are harmful;
- all managers are anti-patterns;
- all global access is forbidden;
- duplication is always preferable to abstraction;
- explicit code should always be verbose;
- one module should own everything;
- complexity can be eliminated completely;
- a diagram proves simplicity;
- a low file count proves simplicity;
- a small binary is necessarily simple;
- rewrites are the normal path to simplicity;
- every system should optimize only for ramp-up;
- simplicity means avoiding advanced techniques;
- direct hardware access everywhere is simple;
- one unified interface is always simpler.

The law is satisfied when the system's important behavior is easier to explain and safely change without erasing
necessary product, hardware, recovery, or operational distinctions.

## 22. Violation Patterns

The future draft should make these violations visible:

- a small behavior change touches many forwarding layers;
- product decisions are encoded in utility functions;
- manager modules call other manager modules without clear ownership;
- event callbacks hide ordinary control flow;
- a global context object carries unrelated state;
- one generic status type erases meaningful distinctions;
- platform vocabulary leaks into product rules;
- tests mock architecture layers but do not prove product behavior;
- logs describe infrastructure steps rather than the decision;
- diagrams require more explanation than the behavior;
- configuration recreates control flow at runtime;
- wrappers rename APIs without reducing coupling;
- duplicated policies drift across entry paths;
- error recovery depends on hidden ordering;
- no engineer can explain the ordinary path end to end;
- simple means familiar only to the original author;
- simplification proposals are actually rewrites without scoped evidence.

## 23. Engineering Principle Target

Target principle for the future draft:

> Prefer the design that makes product behavior, ownership, and consequences easiest to explain and safely change.
> Preserve essential complexity; remove accidental concepts.

The principle should imply review questions:

1. What product decision is being made?
2. Who owns it?
3. What is the ordinary path from input to consequence?
4. Which concepts must be understood together?
5. Which layers change the decision, and which only forward it?
6. Where does platform vocabulary leak?
7. What is the real change radius?
8. Do tests describe product behavior or architecture mechanics?
9. Can diagnostics explain why the decision occurred?
10. Which complexity is essential?
11. Which concept can be deleted, narrowed, or renamed?
12. Would this still be understandable during an incident?

The final manuscript may shorten the list for reader rhythm.

## 24. Architecture Exercise Target

### Working Title

Explain One Behavior End to End

Ask the reader to choose one important product behavior and document:

1. trigger;
2. inputs;
3. decision owner;
4. required state;
5. ordinary control path;
6. exceptional paths;
7. hardware or platform boundary;
8. dependencies;
9. side effects;
10. completion semantics;
11. failure and recovery behavior;
12. diagnostics;
13. tests;
14. files, modules, or services involved;
15. vocabulary used;
16. change radius for one realistic modification;
17. layers that transform behavior;
18. layers that only forward;
19. duplicated policies;
20. hidden state;
21. concepts that can be removed, narrowed, or renamed;
22. ADR location for the proposed simplification.

End with one small, reviewable simplification decision.

Do not create a new canonical artifact such as Simplicity Score, Concept Budget, Explanation Map, Complexity Ledger,
Layer Tax, or Simplicity Register. A chapter-local worksheet is acceptable if it uses existing records such as ADRs.

## 25. Chapter-Local ADR Brief

### Working Title

Collapse Command Routing into One Product-Owned Decision Path

### Context

- A command passes through multiple managers, callbacks, utilities, and platform wrappers.
- Calibration state changes whether the command is safe.
- Different entry paths apply inconsistent rules.
- Tests verify forwarding but not the product decision.
- Diagnostics cannot explain acceptance or rejection.

### Decision

- Assign command acceptance to the product state owner.
- Define one product-level command vocabulary.
- Create one explicit decision function or boundary.
- Remove pass-through manager and callback layers.
- Keep hardware calls behind one bounded integration edge.
- Preserve distinct normal, rejected, and recovery outcomes.
- Align tests with product-level behavior.
- Emit diagnostics at the decision point.
- Migrate entry paths incrementally.
- Retain essential asynchronous completion where hardware requires it.

### Alternatives Considered

- Add another policy manager.
- Add a calibration Boolean to the global context.
- Route all commands through a generic event bus.
- Duplicate command logic per entry point.
- Rewrite the whole subsystem.
- Document current call chains without changing them.
- Make the platform driver responsible for product acceptance.
- Introduce a generic rules framework.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits:

- clearer ownership;
- smaller reasoning surface;
- consistent command behavior;
- lower change radius;
- tests aligned with product semantics;
- better diagnostics;
- easier ramp-up and incident response.

Costs:

- migration work;
- removal of familiar abstractions;
- temporary coexistence during transition;
- explicit product-specific code;
- careful preservation of asynchronous hardware behavior;
- risk of over-centralization if the boundary grows beyond the decision.

The ADR must make a genuine scoped decision. It must not reduce to "simplify the code."

## 26. PEAK Concept Map

### Concepts Inspected

- `LAW-004` - Simplicity Is a Feature.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-005` - Evidence Before Confidence.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-007` - Every Dependency Is a Decision.
- `SMELL-002` - Utility Gravity.
- `SMELL-001` - Silent Coupling.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `SMELL-003` - Boolean Explosion.
- `ANTIPATTERN-001` - God Module.
- `ANTIPATTERN-002` - HAL Everywhere.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-004` - Manager Mania.
- `ANTIPATTERN-005` - Callback Hell.
- `ANTIPATTERN-006` - Temporary Solution.
- `VOCAB-001` - Change Radius.
- `VOCAB-007` - Architecture Health.
- `VOCAB-009` - Utility Gravity.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `METRIC-005` - Architecture Health.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-006` - Architecture Ledger.
- `RITUAL-003` - Deletion Day.
- `RITUAL-004` - Architecture Health Review.
- `FAILURE-001` - Logger That Became a Platform.

### Selected Concepts

- `LAW-004` - Simplicity Is a Feature: the chapter directly illustrates this law as the sixth law of Part II.
- `SMELL-002` - Utility Gravity: material because convenience helpers can accumulate product decisions and hide
  ownership while appearing simple locally.
- `ANTIPATTERN-004` - Manager Mania: material because manager layers are central to the recommended story and obscure
  product decision ownership.
- `SMELL-001` - Silent Coupling: material because hidden dependencies between callbacks, configuration, utilities, and
  diagnostics make local change unsafe.
- `SMELL-005` - Platform Leakage: material because product acceptance rules should not depend on platform wrapper or
  driver vocabulary.
- `ANTIPATTERN-005` - Callback Hell: material because callback chains hide ordering, error handling, and the ordinary
  command decision path.
- `VOCAB-001` - Change Radius: material because simplicity is tested by how far a realistic product change travels.
- `VOCAB-007` - Architecture Health: material because simplicity contributes to the system's ability to absorb necessary
  change.
- `METRIC-001` - Change Radius: material because the exercise asks readers to identify affected modules, tests, tools,
  diagnostics, and support behavior.
- `METRIC-003` - Discoverability: material because a simple system lets maintainers find the decision, owner, and
  contract behind behavior.
- `METRIC-005` - Architecture Health: material because the chapter treats simplicity as a change-safety and maintenance
  capability, not a local code style.
- `ARTIFACT-001` - ADR: material because collapsing command routing into one product-owned decision path is an
  architectural decision with consequences and alternatives.

### Rejected Concepts

- `LAW-006` - Unused Flexibility Is Waste: directly adjacent, but Chapter 11 owns unused options and retained
  flexibility. Chapter 12 may mention unused paths as one simplification technique without registering a Chapter 12 edge.
- `LAW-005` - Evidence Before Confidence: evidence matters when validating simplification, but Chapter 13 owns evidence
  quality and confidence calibration.
- `LAW-001` - Every State Has One Owner: ownership matters, but Chapter 7 owns state authority.
- `LAW-002` - Every API Is a Promise: narrower interfaces matter, but Chapter 8 owns API promises.
- `LAW-003` - Time Is a Dependency: callback ordering may appear in the story, but Chapter 10 owns temporal semantics.
- `LAW-007` - Every Dependency Is a Decision: dependency spread can increase complexity, but Chapter 9 owns dependency
  commitment.
- `SMELL-004` - Hidden State: relevant to global context and hidden flags, but Silent Coupling and Manager Mania carry
  the selected story more directly.
- `SMELL-006` - Event Explosion: relevant to event forwarding, but Callback Hell and Silent Coupling are more material
  to the command-path story.
- `SMELL-003` - Boolean Explosion: relevant when flags multiply behavior, but Chapter 11 already uses it as a primary
  option-surface smell.
- `ANTIPATTERN-001` - God Module: relevant to over-centralization, but Manager Mania is more precise for the selected
  story and the ADR guardrail warns against growing one central owner.
- `ANTIPATTERN-002` - HAL Everywhere: relevant to platform details, but Platform Leakage covers the selected boundary
  without pulling the chapter into HAL design.
- `ANTIPATTERN-003` - Global Configuration: relevant to the shared context flag, but the selected graph avoids making
  Chapter 12 a configuration chapter.
- `ANTIPATTERN-006` - Temporary Solution: relevant to lifecycle cleanup, but Chapter 11 already owns temporary retained
  options.
- `VOCAB-009` - Utility Gravity: relevant, but `SMELL-002` already carries the selected Utility Gravity concept.
- `ARTIFACT-003` - Decision Journal: useful for smaller simplification decisions, but the selected ADR is the material
  artifact for this chapter.
- `ARTIFACT-006` - Architecture Ledger: useful for discoverability in larger systems, but not necessary for the chapter's
  central decision.
- `RITUAL-003` - Deletion Day: useful for removal, but Chapter 12 must not become the deletion ritual playbook.
- `RITUAL-004` - Architecture Health Review: useful for maintenance, but Chapter 12 should not teach the full review
  ritual.
- `FAILURE-001` - Logger That Became a Platform: related to utility growth, but the recommended story should be a command
  routing path rather than a logging platform story.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as reasoning surface, explanation cost, concept budget, decision path, simplicity debt, layer tax, and
complexity rent remain chapter-local prose unless a later Canon Review finds a stable reusable gap.

## 27. Exact Proposed PEAK Relationships

Register `CHAPTER-012` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-012
  type: illustrates
  to: LAW-004

- from: CHAPTER-012
  type: illustrates
  to: SMELL-002

- from: CHAPTER-012
  type: illustrates
  to: ANTIPATTERN-004

- from: CHAPTER-012
  type: references
  to: SMELL-001

- from: CHAPTER-012
  type: references
  to: SMELL-005

- from: CHAPTER-012
  type: references
  to: ANTIPATTERN-005

- from: CHAPTER-012
  type: references
  to: VOCAB-001

- from: CHAPTER-012
  type: references
  to: VOCAB-007

- from: CHAPTER-012
  type: references
  to: METRIC-001

- from: CHAPTER-012
  type: references
  to: METRIC-003

- from: CHAPTER-012
  type: references
  to: METRIC-005

- from: CHAPTER-012
  type: references
  to: ARTIFACT-001
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 28. Required Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

The `Principal's Notebook` must contain exactly three short observations and no explanations.

## 29. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- Simple is explainable under pressure.
- Easy now can be expensive later.
- Remove concepts, not truth.

These are semantic targets, not mandatory final wording.

## 30. Evidence and Technical Credibility Requirements

The future draft must be credible for embedded and long-lived systems. It should treat the following correctly:

- command acceptance and rejection;
- calibration state;
- deferred hardware completion;
- asynchronous callbacks;
- event routing and ordering assumptions;
- global context flags;
- manager layers and pass-through adapters;
- platform wrappers and driver vocabulary;
- diagnostics and support logs;
- tests that verify product behavior rather than forwarding;
- error handling and recovery behavior;
- migration from multiple entry paths;
- scoped deletion of accidental layers;
- preservation of essential hardware complexity.

The story should remain architecture-neutral unless a small illustrative detail is necessary. Do not require a specific
RTOS, MCU, hardware driver, UI framework, event bus, test framework, or vendor.

## 31. Terminology and Precision Guardrails

Use simplicity terms precisely:

- simple: few truthful concepts needed to explain and safely change important behavior;
- easy: locally convenient or familiar now;
- simplistic: necessary distinctions removed until behavior becomes ambiguous;
- explicit: visible ownership, state, boundary, decision, or consequence;
- concise: few words or lines;
- compact: dense representation;
- essential complexity: complexity required by real product, hardware, protocol, safety, timing, operations, or recovery
  needs;
- accidental complexity: extra concepts created by implementation structure, indirection, hidden coupling, or stale
  design choices.

The chapter must avoid these misleading statements:

- "Short code is simple."
- "Abstraction is bad."
- "Managers are always wrong."
- "Duplication is always simpler."
- "A diagram proves simplicity."
- "Simplification means rewrite."
- "Direct hardware access everywhere is simple."
- "One unified interface is always simpler."
- "Verbose code is always explicit."
- "A product owner should own every implementation detail."

## 32. Failure Modes to Avoid

The later draft must not become:

- a style guide;
- a generic simplicity essay;
- a KISS/YAGNI article;
- an anti-abstraction rant;
- a fewer-lines argument;
- a retelling of Chapter 11 flexibility;
- a retelling of Chapter 13 evidence quality;
- a complete Architecture Health Review guide;
- a Deletion Day playbook;
- a legacy migration playbook;
- a framework-design tutorial;
- a shallow ADR that says only "simplify the code";
- a new PEAK artifact proposal;
- a worksheet with no real architectural decision;
- reader-facing draft prose inside the canonical brief.

## 33. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete embedded command-path simplicity failure;
- the Principal Engineer move recasts the work around product decision, owner, and shortest truthful path from input to
  consequence;
- `LAW-004` is explained beyond the slogan;
- simple, easy, simplistic, explicit, concise, compact, understandable, essential complexity, and accidental complexity
  are distinguished where relevant;
- the chapter connects simplicity to product outcomes such as change safety, diagnosis, recovery, release confidence,
  support, ramp-up, and review quality;
- local and system-level simplicity are distinguished;
- abstraction is treated proportionately rather than counted or condemned;
- Utility Gravity, Manager Mania, Silent Coupling, Platform Leakage, Callback Hell, Change Radius, Discoverability,
  Architecture Health, and ADR are materially present if their relationships remain registered;
- the exercise can be applied to one real behavior end to end and ends in a small, reviewable simplification decision;
- the ADR makes a genuine scoped decision and acknowledges benefits and costs;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally;
- boundaries with Chapters 1-11, Chapter 13, and later parts are respected;
- claims are technically credible and reviewable.

## 34. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach one
idea without drifting into a style guide, rewrite story, anti-abstraction essay, or generic simplicity article.

Canon Review should verify that the chapter illustrates `LAW-004`, materially uses the registered supporting concepts,
does not imply a new PEAK artifact or vocabulary term, and preserves the boundary with Chapter 11 and Chapter 13.

Technical Review should focus on command acceptance, calibration state, callback and event ordering, product-level
ownership, platform boundaries, diagnostics, recovery behavior, tests aligned with product semantics, and whether the
proposed simplification removes accidental concepts without erasing essential hardware or recovery complexity.

Freeze Review should confirm that Chapter 12 continues Part II, keeps the manuscript architecture intact, uses exactly
three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the reader-facing manuscript in
canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
control subsystem details, command names, callback shape, manager names, and final notebook wording while preserving the
simplicity thesis, story shape, PEAK map, and chapter boundaries.

## 35. Final Scope Statement

Chapter 12 should define simplicity as the system property that makes product behavior, ownership, and consequences easy
to explain and safely change. It should show an embedded command path whose locally reasonable layers hide a product
decision, then guide the reader toward product vocabulary, explicit ownership, direct decision paths, lower change
radius, better diagnostics, product-level tests, and a scoped ADR that collapses command routing without erasing
essential hardware and recovery complexity.
