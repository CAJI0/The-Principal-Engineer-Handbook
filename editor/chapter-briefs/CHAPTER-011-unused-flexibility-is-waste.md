# CHAPTER-011 Canonical Brief: Unused Flexibility Is Waste

## Metadata

- Stable ID: `CHAPTER-011`.
- Title: `Unused Flexibility Is Waste`.
- Part: Part II - The Laws.
- Chapter number: 11.
- Expected manuscript path: `book/02-the-laws/11-unused-flexibility-is-waste.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-011-unused-flexibility-is-waste.md`.
- Branch: `chapter11`.
- Canonical predecessor: `CHAPTER-010` - Time Is a Dependency.
- Part position: fifth chapter of Part II - The Laws.
- Verified baseline `origin/main`: `96aeb1a6f2dca7d0cd3639a2298d3ba4ae05e4a6`.
- Reader-facing draft created: no.
- Primary law: `LAW-006` - Unused Flexibility Is Waste.
- Lifecycle status at brief-registration time: draft preparation.
- Next lifecycle stage: Author Draft after author approval.

## Repository-Grounded Findings

- `origin/main` resolves to `96aeb1a6f2dca7d0cd3639a2298d3ba4ae05e4a6`.
- That baseline is the PR #12 squash commit, `Chapter 10: Time Is a Dependency (#12)`.
- The Chapter 10 feature-branch Freeze commit `e088cb9db2a3d4c1e774bc9c4793ced363505e15` is not required to be an
  ancestor of `main` because PR #12 used squash merge.
- The final Chapter 10 lifecycle files in the PR #12 squash commit are tree-equivalent to the final feature-branch
  Freeze commit for the checked Chapter 10 paths.
- `CHAPTER-001` through `CHAPTER-010` are registered as `canonical` in `knowledge/index.yaml`.
- Chapter 10 exists at `book/02-the-laws/10-time-is-a-dependency.md`.
- `editor/EDITOR_LOG.md` records Chapter 10 Editorial, Canon, Technical, and Freeze Review entries in order.
- The repository table of contents lives at `book/00-front-matter/table-of-contents.md` and places `Unused Flexibility Is
  Waste` after `Time Is a Dependency` in Part II.
- `LAW-006` exists exactly once and is named `Unused Flexibility Is Waste`.
- `LAW-006` states that flexibility not used or justified becomes maintenance cost.
- `LAW-006` already relates to Deletion Day, Simplicity Is a Feature, and Temporary Solution in its law file.
- `CHAPTER-011` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 11 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter11` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 1. Canonical Purpose

Prepare Chapter 11 to teach the fifth Part II law: flexibility is not free just because it is technically possible.

The chapter should move the reader from admiring options, modes, plug-in points, generic interfaces, and dormant code as
default signs of good design toward a reviewable architecture question: what uncertainty does this option protect
against, who owns it, and what cost does it impose while it remains available?

The chapter must not create a reader-facing draft during this task. It must constrain the later Author Draft.

## 2. Exact Law Statement

`LAW-006` states:

> Flexibility that is not used or justified becomes maintenance cost.

Chapter 11 should preserve that law while making "maintenance cost" concrete: code paths, state space, test combinations,
configuration surface, documentation, review effort, operational ambiguity, migration obligations, compatibility,
cognitive load, incident diagnosis, field support, and future deletion cost.

## 3. Central Thesis

Flexibility has value only when it protects against real, material uncertainty. Options that are not used, justified, or
deliberately owned become permanent maintenance cost.

Approved supporting formulation for the future draft:

> Pay for flexibility only when the uncertainty it protects against is real enough to justify the ongoing cost.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact, ritual,
smell, anti-pattern, failure story, or vocabulary concept.

## 4. Reader Transformation

Before the chapter, the reader may think:

1. flexible architecture is inherently better architecture;
2. adding a mode, flag, interface, fallback, or strategy costs little if it is not used;
3. unused options can remain harmless until needed;
4. configuration is safer than choosing;
5. an abstraction around hypothetical change is prudent engineering;
6. compatibility layers and dormant implementations are cheap insurance;
7. deleting an unused option is riskier than keeping it.

By the end of the chapter, the reader should be able to:

1. distinguish owned product variability from speculative flexibility;
2. identify the full cost surface created by one option;
3. decide whether an option is used, justified, or waste;
4. preserve a small seam without shipping every path;
5. assign an owner and review trigger to retained flexibility;
6. record large flexibility decisions in an ADR or smaller ones in a Decision Journal;
7. remove unsupported paths with evidence and rollback boundaries;
8. avoid turning the law into a blanket attack on abstraction.

## 5. Semantic Definition of Flexibility

Flexibility is a deliberate option preserved in the system so it can support more than one future behavior, variation,
implementation, deployment shape, or operating mode.

Flexibility may appear as:

- optional configuration;
- feature flags;
- multiple active modes;
- plug-in points;
- generic interfaces;
- multiple backends or transports;
- protocol extension points;
- conditional compilation;
- build matrices;
- fallback modes;
- compatibility layers;
- dormant implementations;
- speculative hardware support;
- runtime strategy selection;
- product variants;
- framework-building;
- abstraction around hypothetical change.

The chapter should separate valuable optionality from waste. A reversible decision can be valuable without shipping all
possible paths. A small seam can be justified without carrying every implementation behind it.

## 6. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 11 covers:

- unused and unjustified flexibility as maintenance cost;
- the difference between product variability, near-term variation, and speculative options;
- runtime, compile-time, and architectural flexibility;
- code paths, state space, test combinations, configuration, documentation, review, operations, migration, and support
  burden;
- ownership, evidence, and review triggers for retained options;
- preserving the smallest justified seam;
- removing unsupported modes and dormant paths;
- compatibility cost when options have escaped into tests, tools, field procedures, or customer expectations;
- local abstraction that improves readability or testability without creating broad variability;
- recording material flexibility decisions in existing PEAK artifacts.

### Explicitly Out of Scope

Do not turn Chapter 11 into:

- a blanket "abstraction is waste" argument;
- a generic simplicity essay;
- a full Deletion Day playbook;
- a legacy-code migration manual;
- a configuration-management chapter;
- a product-line engineering handbook;
- a compiler-flag or build-system tutorial;
- a plug-in architecture tutorial;
- a framework-design chapter;
- a test-matrix management chapter;
- a broad evidence-quality chapter;
- a Part III boundary-design playbook;
- a Part IV product-configuration or field-operations chapter;
- a Part VI legacy deletion program.

Those topics may appear only where they clarify the cost of retained options.

## 7. Flexibility, Variability, and Optionality

The future draft must distinguish:

- actual product variability: supported variations that customers, markets, hardware, regulation, or operations require;
- near-term variation: likely alternatives with known owners, dates, or decision triggers;
- seams around proven volatility: narrow boundaries where repeated change has shown a stable uncertainty;
- hypothetical possibilities: "we might need it someday" options with no evidence, owner, or trigger;
- compatibility obligations: behavior kept because shipped consumers already rely on it;
- unused configuration: switches, modes, or flags that no supported product needs;
- generic design without evidence: abstraction built around imagined variation rather than observed pressure.

Product variability is not waste when it is owned, tested, documented, and supported. Speculative flexibility becomes
waste when it creates permanent surface without a justified uncertainty.

## 8. Used and Justified Flexibility

Flexibility is used when a supported product, environment, workflow, customer, deployment, or test strategy actively
depends on it.

Flexibility is justified when all or most of these are true:

- the uncertainty is material, not imaginary;
- likely alternatives are known;
- adding the option later would be expensive or risky;
- the seam is small and contained;
- the retained option has an owner;
- a review trigger says when to keep, change, or delete it;
- tests and documentation match the supported surface;
- evidence exists in an ADR, Decision Journal, roadmap, field need, product constraint, or repeated change pattern.

Flexibility is waste when it has no supported user, no evidence, no owner, no review trigger, and no bounded cost.

## 9. Runtime, Compile-Time, and Architectural Flexibility

Runtime flexibility appears as modes, strategy selection, optional backends, runtime flags, service discovery, fallback
behavior, and product configuration. Its cost appears in state space, operational ambiguity, diagnostics, field support,
security review, and live failure modes.

Compile-time flexibility appears as build flags, conditional compilation, target variants, generated code options,
optional drivers, and build matrices. Its cost appears in CI, release packaging, test coverage, manufacturing, support
tools, and the ability to know which product actually contains which behavior.

Architectural flexibility appears as seams, interfaces, adapters, extension points, compatibility layers, and
framework-like designs. Its cost appears in indirection, review effort, discoverability, owner ambiguity, and the
temptation to support variation that the product does not own.

The chapter should not rank one form as always better. It should ask whether the option protects real uncertainty and
whether its cost is visible.

## 10. Cost Surface and Combinatorial Growth

Unused flexibility costs more than code size.

The future draft should make the cost surface concrete:

- implementation branches;
- state combinations;
- test combinations;
- CI matrix size;
- configuration migration;
- documentation burden;
- review effort;
- code search and comprehension;
- operational ambiguity;
- field support;
- manufacturing behavior;
- service-tool behavior;
- observability and diagnostics;
- security review;
- compatibility obligations;
- failure modes;
- incident diagnosis;
- rollback and upgrade paths;
- ownership questions.

The chapter should use `SMELL-003` - Boolean Explosion where optional modes and flags multiply behavior combinations
until no one can list what is valid.

## 11. Evidence, Ownership, and Review Triggers

Retained flexibility needs evidence, ownership, and a review trigger.

Evidence may include:

- active product requirement;
- known hardware variant;
- signed customer or regulatory requirement;
- repeated change history;
- expensive later migration;
- planned near-term alternative with a decision date;
- field-support obligation;
- shipped compatibility promise;
- testing constraint better served by a seam than by a full product option.

Ownership should identify who decides whether the option remains supported, which products use it, what tests prove it,
and when it can be removed.

Review triggers may include:

- product launch;
- variant retirement;
- end of compatibility window;
- customer migration completion;
- no usage over a measured period;
- test matrix growth above a threshold;
- field defect in a dormant path;
- new hardware selection;
- release train change.

Large decisions belong in an ADR. Smaller or reversible decisions may belong in a Decision Journal with evidence,
confidence, and review trigger.

## 12. Removal and Seam Preservation

Removing flexibility is not just deleting code.

The future draft should cover:

- proving the path is unused or unsupported;
- identifying consumers;
- deleting configuration;
- reducing tests;
- removing compatibility layers;
- updating documentation;
- simplifying support tools;
- deciding whether to preserve a seam;
- setting rollback boundaries;
- keeping enough evidence to explain the removal later.

The chapter should not become a full legacy deletion playbook. The law-level point is that unsupported options must be
paid for until they are removed or intentionally owned.

Seam preservation matters. Sometimes the right move is not to keep five modes. It is to keep one narrow boundary where a
future mode could be added when evidence appears.

## 13. Local Abstraction and System Flexibility

The future draft must avoid the false lesson that every abstraction is waste.

Local abstraction can improve readability, testability, substitution in tests, or separation of volatile details without
creating broad product variability. The cost becomes waste when the abstraction claims to support modes, implementations,
or products that no one owns.

The chapter should distinguish:

- a small helper that clarifies code;
- an interface used by tests and one production implementation;
- an adapter that isolates a volatile platform detail;
- a framework that invites unsupported extension;
- a strategy surface that carries untested modes;
- a compatibility layer whose retirement condition has disappeared.

## 14. Boundaries With Chapters 1-10

### Chapters 1-6 - Principal Engineering Foundations

Chapter 11 may use decision quality, constraints, questions, ownership, evidence, and stewardship as premises. It must
not repeat the Part I mindset chapters. The cost of options is the subject.

### Chapter 7 - Every State Has One Owner

Chapter 7 owns state authority. Chapter 11 may show that extra modes and flags multiply state ownership questions, but it
must not reteach one-owner semantics.

### Chapter 8 - Every API Is a Promise

Chapter 8 owns API promises. Chapter 11 may show that extension points, optional fields, and compatibility layers create
promises, but it must not become another API-contract chapter.

### Chapter 9 - Every Dependency Is a Decision

Chapter 9 owns dependency commitment. Chapter 11 may show that generic wrappers and multiple backends create option
cost, but it must not retell dependency selection or replacement cost.

### Chapter 10 - Time Is a Dependency

Chapter 10 owns temporal semantics. Chapter 11 may mention review triggers and scheduled retirement, but it must not
become a clock, timeout, or freshness chapter.

## 15. Boundary With Simplicity Is a Feature

Chapter 12 - `Simplicity Is a Feature` will own simplicity as a product capability and system property.

Chapter 11 should remain narrower: unused flexibility is one way complexity becomes permanent cost. It should show why
unused options harm change safety without trying to teach all of simplicity, readability, product focus, or design
minimalism.

Use `LAW-004` as a boundary, not as a registered outgoing Chapter 11 relationship.

## 16. Boundaries With Later Part II Laws

- Chapter 12 - `Simplicity Is a Feature`: Chapter 11 may prepare the reader to value less optional surface, but Chapter
  12 owns the broader simplicity argument.
- Chapter 13 - `Evidence Before Confidence`: Chapter 11 may require evidence for retained options, but Chapter 13 owns
  the full evidence-quality law.

Do not consume the later laws by making Chapter 11 a general simplicity or evidence chapter.

## 17. Boundaries With Later Parts

Later parts should retain detailed architecture reviews, RFC operations, product configuration strategy, manufacturing
and field workflows, release and upgrade orchestration, telemetry, platform governance, legacy migration, and deletion
programs.

Chapter 11 should stay at law level. It names the cost of retained options and gives the reader enough practice to
recognize, justify, own, or remove one flexibility point.

## 18. Recommended Embedded-Systems Story

### Working Title

The Radio Service That Could Be Anything

### System

Use an embedded radio or communications service originally built for one shipped product and one validated transport.
The team anticipates several future products and adds flexibility early:

- multiple transports;
- several runtime modes;
- conditional compilation for boards not yet selected;
- generic packet strategy interfaces;
- optional fallback paths;
- test-only configuration that leaks into release builds;
- compatibility behavior for a prototype tool;
- dormant hardware support.

Only one mode ships. The rest remains present because "we may need it later."

### Incident Shape

A field defect appears in the shipped mode. The team tries to reason about the fix but must account for dormant modes,
untested fallbacks, old prototype behavior, build flags, and service-tool configuration.

The defect may show:

- tests failing in combinations no product supports;
- reviewers unsure which modes are valid;
- diagnostics reporting generic mode names with no owner;
- support tools exposing unsupported options;
- a dormant transport changing error handling;
- a prototype compatibility path blocking cleanup;
- a security review considering code no customer can use;
- product owners unable to say which flexibility the product owns.

### Tempting But Inadequate Response

The team initially proposes:

- leave all modes because deleting them is risky;
- add more tests for every combination;
- mark old paths as "legacy";
- hide options in documentation;
- add another runtime flag;
- add a second abstraction layer;
- promise cleanup after the next release;
- keep dormant code because a future product might need it.

Those responses keep the cost while avoiding the decision.

### Principal Engineer Intervention

The Principal Engineer recasts the issue from "flexible service" to "unowned options charging rent."

The corrective model:

- list every mode, backend, flag, build option, fallback, and compatibility path;
- identify active products and consumers;
- identify unsupported or dormant paths;
- preserve only the smallest seam justified by real uncertainty;
- remove unsupported runtime modes;
- delete configuration that exposes unsupported behavior;
- reduce test matrix size to supported combinations;
- record compatibility obligations and retirement triggers;
- assign ownership for retained variation;
- write an ADR for material removal and seam preservation;
- use a Decision Journal for smaller options with evidence and review triggers.

The point is not that a radio service should never be reusable. The point is that reuse must be owned and paid for.

## 19. Expected Discussion Arc

1. **Flexibility feels prudent because it preserves choices.**
   The chapter should begin by honoring why engineers add options.
2. **Options become real surface even when no product uses them.**
   Code, tests, docs, tools, operations, and support must still carry them.
3. **Variability is valuable when it is owned.**
   Product variants and compatibility duties are not waste when they have evidence and support.
4. **Speculative flexibility differs from reversible decisions.**
   A team can postpone commitment without shipping every possible path.
5. **Modes and flags multiply behavior.**
   The cost is often combinatorial, not additive.
6. **Dormant paths decay invisibly.**
   Untested and unsupported paths still shape review and incident response.
7. **Small seams are often enough.**
   Preserve the boundary when uncertainty is real; avoid carrying all implementations early.
8. **Retained flexibility needs an owner and trigger.**
   Without review conditions, "temporary" becomes permanent.
9. **Removal has an architecture path.**
   Prove usage, identify consumers, update tests and docs, and preserve evidence.
10. **The Principal Engineer protects future change by refusing unpaid options.**
    Flexibility should be designed, not accumulated.

These are intellectual progression points, not mandatory manuscript headings.

## 20. Law Applicability

The law applies when a system keeps:

- optional configuration;
- unused flags;
- plug-in points;
- generic interfaces;
- multiple backends;
- protocol extension points;
- conditional compilation;
- build matrices;
- fallback modes;
- compatibility layers;
- dormant implementations;
- speculative hardware support;
- runtime strategy selection;
- product variants;
- framework-building;
- abstraction around hypothetical change.

The law is proportional. Not every local helper or test seam deserves an ADR. Review depth should grow with product
surface, test matrix size, field exposure, compatibility cost, operational ambiguity, security exposure, and future
deletion cost.

## 21. Law Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- all abstraction is waste;
- all unused code must be deleted immediately;
- every option needs a formal review;
- every product variant is speculative;
- every compatibility layer is wrong;
- configuration is inherently bad;
- runtime selection is always worse than compile-time selection;
- compile-time selection is always safer than runtime selection;
- test seams are suspicious by default;
- platform isolation is over-engineering;
- future reuse is never real;
- deletion is safe without evidence;
- simplicity means choosing the first implementation forever.

The law is satisfied when retained flexibility has evidence, ownership, bounded cost, and a review trigger.

## 22. Violation Patterns

The future draft should make these violations visible:

- `future_product_enabled` flags with no product owner;
- multiple runtime modes where only one is supported;
- optional configuration not exercised in CI;
- build flags that create untested releases;
- fallback paths with unclear failure semantics;
- generic interfaces that expose every backend detail;
- plug-in points with no plug-ins;
- compatibility layers with no retirement trigger;
- prototype behavior kept for field tools by accident;
- dormant hardware support affecting product logic;
- test-only paths leaking into supported builds;
- documentation that lists options support cannot explain;
- security review covering unreachable but shipped code;
- deleting an option blocked by oral history rather than evidence.

## 23. Engineering Principle Target

Target principle for the future draft:

> Keep flexibility only when it protects against real uncertainty or supports an owned variation. Otherwise remove the
> option and preserve only the smallest seam justified by evidence.

The principle should imply review questions:

1. Who uses this option today?
2. What uncertainty does it protect against?
3. What would it cost to add later?
4. Which products or workflows support it?
5. Who owns the retained variation?
6. Which tests prove the supported combinations?
7. What documentation and tools expose it?
8. What compatibility obligations exist?
9. What is the review trigger?
10. What seam can remain if the option is removed?

## 24. Architecture Exercise Target

### Working Title

Audit One Flexibility Point

Ask the reader to choose one optional mode, flag, backend, interface, fallback, build option, or compatibility layer and
document:

1. exact option name;
2. supported products or consumers;
3. evidence that the option is used;
4. uncertainty it protects against;
5. cost of adding the option later;
6. runtime or build-time exposure;
7. state combinations it creates;
8. tests required;
9. CI or release matrix impact;
10. documentation impact;
11. service-tool or field-support impact;
12. security or failure-mode impact;
13. owner;
14. review trigger;
15. deletion evidence needed;
16. consumers to migrate;
17. smallest seam worth preserving;
18. ADR or Decision Journal location.

The exercise must not create a new canonical PEAK artifact such as Flexibility Ledger, Option Register, Variant Map, or
Seam Catalog. A chapter-local worksheet is acceptable if it uses existing records such as ADRs and Decision Journals.

## 25. Chapter-Local ADR Brief

### Working Title

Remove Unsupported Runtime Modes and Preserve One Transport Seam

### Context

- The communication service supports several modes and transports, but only one shipped product uses one validated path.
- Dormant modes affect tests, review, diagnostics, support tools, and security review.
- A field defect in the shipped mode is harder to diagnose because unsupported combinations still exist.
- Future product uncertainty is real, but no product owns the dormant implementations.

### Decision

- Remove unsupported runtime modes from shipped builds.
- Delete configuration that exposes unsupported modes.
- Reduce CI to supported combinations.
- Preserve one narrow transport seam where evidence shows future hardware variation is likely.
- Assign an owner and review trigger for the retained seam.
- Record compatibility obligations for any service or manufacturing tool that used old behavior.
- Use the Decision Journal for smaller retained options with evidence and review dates.

### Alternatives Considered

- Keep all modes until a future product decides.
- Add tests for every existing combination.
- Hide unsupported options from documentation but keep runtime behavior.
- Replace runtime modes with compile-time flags without reducing the supported surface.
- Delete the entire abstraction and hard-code the current transport.
- Build a broader plug-in framework.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits:

- smaller test matrix;
- clearer supported behavior;
- lower review and diagnosis cost;
- fewer exposed configuration paths;
- visible ownership for retained variation;
- easier future addition behind a narrow seam.

Costs:

- migration for tests and tools using old options;
- possible compatibility work for prototype or service workflows;
- evidence gathering before deletion;
- risk of needing to re-add a removed path later;
- discipline to keep the preserved seam small.

The ADR is story-local and reader-facing. It must not become a repository-level ADR or a tutorial on ADR mechanics.

## 26. PEAK Concept Map

### Concepts Inspected

- `LAW-006` - Unused Flexibility Is Waste.
- `SMELL-003` - Boolean Explosion.
- `SMELL-005` - Platform Leakage.
- `ANTIPATTERN-006` - Temporary Solution.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-003` - Decision Journal.
- `VOCAB-005` - Deletion Day.
- `RITUAL-003` - Deletion Day.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-005` - Evidence Before Confidence.
- `FAILURE-001` - Logger That Became a Platform.
- `SMELL-002` - Utility Gravity.
- `SMELL-001` - Silent Coupling.

### Selected Concepts

- `LAW-006` - Unused Flexibility Is Waste: the chapter directly illustrates this law as the fifth law of Part II.
- `SMELL-003` - Boolean Explosion: material because unused modes and flags multiply behavior combinations, test space,
  and review burden.
- `SMELL-005` - Platform Leakage: material because speculative hardware and platform hooks can leak into product logic
  when a boundary is broader than the product owns.
- `ANTIPATTERN-006` - Temporary Solution: material because temporary fallbacks, prototype paths, and compatibility modes
  become permanent without an owner, trigger, or removal plan.
- `VOCAB-001` - Change Radius: material because each option expands the surface that must change, be reviewed, or be
  retested.
- `METRIC-001` - Change Radius: material because the exercise asks readers to estimate affected implementation, test,
  documentation, tooling, and support surface.
- `METRIC-003` - Discoverability: material because future engineers must be able to find which variations are supported,
  who owns them, and why retained options exist.
- `ARTIFACT-001` - ADR: material because removing unsupported runtime modes while preserving one seam is an architectural
  decision with consequences and alternatives.
- `ARTIFACT-003` - Decision Journal: material because smaller retained options need evidence, confidence, and review
  triggers without requiring a full ADR.

### Rejected Concepts

- `VOCAB-005` - Deletion Day: relevant to removing unused options, but Chapter 11 should not teach the ritual as its
  primary mechanism.
- `RITUAL-003` - Deletion Day: useful later for organized cleanup, but the chapter should stay at law level and avoid a
  deletion-process playbook.
- `LAW-004` - Simplicity Is a Feature: directly adjacent, but Chapter 12 owns simplicity as the broader system property.
- `LAW-005` - Evidence Before Confidence: evidence matters for retained options, but Chapter 13 owns evidence quality.
- `FAILURE-001` - Logger That Became a Platform: related to flexibility becoming platform cost, but the recommended story
  should be centered on unused runtime modes in a communication service.
- `SMELL-002` - Utility Gravity: relevant when a helper grows into a platform, but the selected story is better supported
  by Boolean Explosion and Platform Leakage.
- `SMELL-001` - Silent Coupling: optional cost can create hidden coupling, but the selected relationship set should stay
  focused on option multiplication, platform leakage, and discoverability.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as flexibility point, option surface, option owner, variant owner, seam preservation, dormant path, and
supported variation remain chapter-local prose unless a later Canon Review finds a stable reusable gap.

## 27. Exact Proposed PEAK Relationships

Register `CHAPTER-011` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-011
  type: illustrates
  to: LAW-006

- from: CHAPTER-011
  type: illustrates
  to: SMELL-003

- from: CHAPTER-011
  type: illustrates
  to: SMELL-005

- from: CHAPTER-011
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-011
  type: references
  to: VOCAB-001

- from: CHAPTER-011
  type: references
  to: METRIC-001

- from: CHAPTER-011
  type: references
  to: METRIC-003

- from: CHAPTER-011
  type: references
  to: ARTIFACT-001

- from: CHAPTER-011
  type: references
  to: ARTIFACT-003
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

- Options charge rent.
- A seam is not every path.
- Temporary needs a trigger.

These are semantic targets, not mandatory final wording.

## 30. Evidence and Technical Credibility Requirements

The future draft must be credible for embedded and long-lived systems. It should treat the following correctly:

- shipped versus unsupported modes;
- runtime flags and build flags;
- conditional compilation;
- test matrix growth;
- CI and release-packaging cost;
- service-tool and manufacturing exposure;
- field diagnostics;
- compatibility paths;
- dormant hardware or transport support;
- fallback semantics;
- security review for exposed options;
- configuration migration;
- preserving a narrow seam without retaining all paths;
- deletion evidence and rollback boundaries.

The story should remain architecture-neutral unless a small illustrative detail is necessary. Do not require a specific
RTOS, MCU, radio chip, transport, cloud platform, build system, test framework, or vendor.

## 31. Terminology and Precision Guardrails

Use flexibility terms precisely:

- flexibility: a deliberate retained option for future variation;
- variability: supported product, environment, or operational variation;
- optionality: the ability to defer or preserve a choice;
- reversible decision: a choice that can be changed later without shipping all paths now;
- seam: a narrow boundary where change can be introduced later;
- dormant path: shipped or retained behavior with no active supported use;
- compatibility layer: behavior retained because existing consumers rely on it;
- review trigger: the condition that forces a retained option to be re-evaluated.

The chapter must avoid these misleading statements:

- "Abstractions are waste."
- "Delete anything unused immediately."
- "A single current product proves no future variation is real."
- "All configuration is bad."
- "A seam must include every possible implementation."
- "A future product is never valid evidence."
- "Test-only paths do not matter."
- "Build flags are cheaper than runtime modes by definition."
- "Compatibility code is only technical debt."
- "Deletion is safe because search found no callers."

## 32. Failure Modes to Avoid

The later draft must not become:

- a broad simplicity chapter;
- an anti-abstraction rant;
- a configuration tutorial;
- a framework-design tutorial;
- a Deletion Day process guide;
- a legacy migration playbook;
- a full product-line architecture chapter;
- a retelling of Chapter 8 compatibility;
- a retelling of Chapter 9 dependency choice;
- a retelling of Chapter 10 review-trigger timing;
- a new PEAK artifact proposal;
- a shallow ADR that says only "delete unused code";
- a worksheet with no real architectural decision;
- reader-facing draft prose inside the canonical brief.

## 33. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete unused-flexibility failure in an embedded communication service;
- the Principal Engineer move recasts flexibility as owned or unowned options with ongoing cost;
- the law is explained beyond the slogan;
- flexibility, variability, optionality, reversible decisions, seams, and dormant paths are distinguished;
- runtime, compile-time, and architectural flexibility are covered where relevant;
- the cost surface includes code, state, tests, CI, docs, tools, operations, support, compatibility, and diagnosis;
- retained flexibility requires evidence, ownership, and a review trigger;
- removal covers usage proof, consumers, configuration, tests, documentation, compatibility, seam preservation, evidence,
  and rollback boundaries;
- the chapter avoids claiming that all abstraction is waste;
- the exercise can be applied to one real flexibility point;
- the ADR makes a genuine decision and acknowledges benefits and costs;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally;
- boundaries with Chapters 1-10, later Part II laws, and later parts are respected;
- claims are technically credible and reviewable.

## 34. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach one
idea without drifting into a broad simplicity essay, deletion program, configuration guide, or anti-abstraction argument.

Canon Review should verify that the chapter illustrates `LAW-006`, materially uses the registered supporting concepts,
does not imply a new PEAK artifact or vocabulary term, and preserves boundaries with Chapters 7 through 10 and later
Part II laws.

Technical Review should focus on runtime modes, build flags, test matrix cost, dormant paths, service-tool exposure,
field diagnostics, compatibility behavior, platform boundaries, deletion evidence, rollback boundaries, and whether the
preserved seam is smaller than the removed option surface.

Freeze Review should confirm that Chapter 11 continues Part II, keeps the manuscript architecture intact, uses exactly
three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the reader-facing manuscript in
canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
radio service details, mode names, transport examples, compatibility paths, and final notebook wording while preserving
the unused-flexibility thesis, story shape, PEAK map, and chapter boundaries.

## 35. Final Scope Statement

Chapter 11 should define unused flexibility as retained option surface that lacks use, evidence, ownership, or review
triggers. It should show an embedded communication service whose speculative modes make a real field defect harder to
diagnose, then guide the reader toward owned variability, small seams, removal evidence, reduced test and support
surface, and an ADR that removes unsupported runtime modes while preserving one justified transport seam.
