# CHAPTER-020 Canonical Brief: From Prototype to Product

## 1. Metadata

- Stable ID: `CHAPTER-020`.
- Title: `From Prototype to Product`.
- Part: Part IV - Building a Product.
- Chapter number: 20.
- Expected manuscript path: `book/04-building-a-product/20-from-prototype-to-product.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-020-from-prototype-to-product.md`.
- Branch: `chapter20`.
- Verified baseline `origin/main`: `c06c0143bc86c446815900e94508230414b0ff24`.
- Baseline evidence: PR #21 squash commit, `Chapter 19: Freezing Architecture Without Freezing Learning (#21)`.
- Chapter 19 feature Freeze commit checked for tree equivalence:
  `130e23d`.
- Canonical predecessor: `CHAPTER-019` - Freezing Architecture Without Freezing Learning.
- Part position: first chapter of Part IV - Building a Product.
- Reader-facing draft created: no.
- Primary concept: none. Chapter 20 opens a product-building part and should be carried by a relationship set rather
  than a new primary-concept field.
- Central anchor: `FAILURE-003` - The Successful Prototype.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `c06c0143bc86c446815900e94508230414b0ff24`.
- That baseline is the PR #21 squash commit, `Chapter 19: Freezing Architecture Without Freezing Learning (#21)`.
- The squash commit is an ancestor of current `origin/main` and has parent
  `63351df957acb62236ef5ff229cfed10718d4d0b`.
- The Chapter 19 feature-branch Freeze commit `130e23d` remains tree-equivalent for the checked Chapter 19 lifecycle
  files in the squash commit.
- `CHAPTER-001` through `CHAPTER-019` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-019` is the sixth and final Part III chapter and is canonical.
- The table of contents places `From Prototype to Product` first in Part IV - Building a Product.
- `book/04-building-a-product/README.md` exists and remains a placeholder.
- `editor/CHAPTER_ARCHITECTURE.md` remains the required manuscript architecture.
- `FAILURE-003` exists exactly once as `The Successful Prototype`.
- `ANTIPATTERN-006`, `LAW-001`, `LAW-002`, `LAW-004`, `LAW-005`, `LAW-006`, `LAW-007`, `VOCAB-001`,
  `METRIC-001`, `METRIC-003`, `ARTIFACT-001`, `ARTIFACT-003`, and `RITUAL-001` exist and are available as selected
  supporting concepts.
- `ARTIFACT-002`, `ARTIFACT-004`, `RITUAL-002`, `VOCAB-006`, `VOCAB-007`, `METRIC-005`, and `RITUAL-004` exist but
  are not selected as outgoing relationships for this chapter.
- `CHAPTER-020` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 20 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter20` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 3. Part IV Role

Chapter 20 opens Part IV by moving from architecture practices to product reality. Part III taught the reader how to
shape boundaries, manage Change Radius, design for recovery, use records, review architecture, and freeze selected
decisions. Chapter 20 applies that discipline to the moment a successful prototype is tempted to become the product.

The chapter should establish the posture for Part IV without teaching every later playbook. It should name the realities
that prototypes often ignore: manufacturing, service, field diagnosis, variants, update and recovery, release packaging,
support ownership, explicit dependencies, and long-term maintenance.

The chapter must not insult prototypes. A prototype is valuable because it creates evidence quickly. The failure begins
when the assumptions that made the prototype fast become invisible product architecture.

## 4. Canonical Purpose

Prepare Chapter 20 to teach the transition from a working prototype to a product architecture.

Candidate thesis for the future manuscript:

> A prototype proves that something can work once. A product architecture defines what must keep working across users,
> variants, manufacturing, service, release, support, and time.

The chapter should move the reader away from treating a successful prototype as production-ready because the demo
worked, the customer liked it, the hardware booted, the happy path passed, one lab configuration behaved correctly, the
team believes it can clean up later, or schedule pressure rewards shipping what already exists.

The core question should become:

> Which assumptions were acceptable in the prototype but must be made explicit, owned, tested, removed, or made ready
> before this becomes the product?

## 5. Primary-Concept Resolution

Chapter 20 has no primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. Chapters 14 through 19
established that practice chapters may be carried by a material relationship set rather than by one primary concept.
Chapter 20 follows that convention while opening Part IV.

`FAILURE-003` - The Successful Prototype is the central anchor. The chapter should materially illustrate the failure
mode where a useful prototype is treated as product architecture before its assumptions have owners, evidence, and
explicit product obligations.

The chapter should not create a named gap metric, Prototype Assumption, Product Readiness, Product Baseline, Production
Reality, Field Reality, Release Baseline, Service Contract, Manufacturing Contract, a ledger for prototype-to-product
work, or any other new PEAK concept. Such terms may remain chapter-local prose only where useful.

## 6. Central Thesis

A successful prototype is evidence, not architecture. Before it becomes the product, the Principal Engineer exposes the
assumptions that made the prototype work, keeps the simplicity that survives product reality, replaces or expires the
shortcuts that do not, and assigns owners to the product realities the prototype ignored.

Approved supporting formulation for the future draft:

> Treat a successful prototype as evidence, not architecture. Before it becomes the product, expose its assumptions,
> keep the simplicity that survives, replace the shortcuts that do not, and assign owners to the product realities the
> prototype ignored.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. A successful demo means the architecture is ready.
2. Prototype shortcuts are harmless because the team remembers them.
3. Product work mostly means cleaning up code.
4. Manual setup is acceptable if it worked in the lab.
5. Diagnostics can wait until support asks.
6. Manufacturing, variants, updates, and release packaging are later operational details.
7. Simplicity means keeping every prototype shortcut.
8. Turning a prototype into a product means rewriting everything or adding flexibility for every possible future
   variant.

By the end of the chapter, the reader should be able to:

1. state what the prototype actually proved;
2. list the assumptions hidden in people, scripts, wiring, fixtures, lab devices, and one customer path;
3. classify each assumption as product contract, implementation detail, temporary shortcut, risk, or evidence gap;
4. decide which shortcuts are harmless and which become product risk;
5. assign owners to configuration, manufacturing, service, diagnostics, variants, update, recovery, release, and support
   realities;
6. map the Change Radius of turning the prototype into a product baseline;
7. keep valuable simplicity without preserving accidental shortcuts;
8. record consequential choices in ADRs or Decision Journal entries.

## 8. Prototype Versus Product

The future manuscript should distinguish prototype and product without treating one as virtuous and the other as
bureaucratic.

A prototype:

- proves possibility;
- optimizes for learning speed;
- tolerates shortcuts;
- may rely on manual setup;
- may hide assumptions in people, scripts, wiring, fixtures, or one test unit;
- may lack support, update, manufacturing, diagnostics, variants, or long-term maintenance.

A product:

- preserves behavior across repeated use;
- supports manufacturing and test;
- survives configuration and variants;
- supports service and field diagnosis;
- handles update and recovery;
- has ownership boundaries;
- has explicit dependencies;
- has a supportable release path;
- has known limits and accepted residual risk.

The chapter should show that prototype success is a strong signal, but not the same thing as a product promise.

## 9. `Productization` Gap

Define the prototype-to-product gap as the distance between the prototype's hidden assumptions and the product's required
operating reality.

Typical gaps include:

- manual setup becomes production configuration;
- lab fixture becomes manufacturing process;
- debug log becomes field diagnostic need;
- one customer path becomes product variant matrix;
- direct dependency becomes support obligation;
- hard-coded value becomes calibration or configuration;
- local script becomes release process;
- happy-path update becomes recovery requirement;
- single board becomes tolerance, lot, and field variability;
- temporary wiring becomes interface contract.

Do not create a new PEAK metric for this gap. The chapter can use the phrase to help the reader reason, while
`VOCAB-001` and `METRIC-001` remain the existing Change Radius concepts.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 20 covers:

- treating prototype success as evidence rather than a product promise;
- exposing prototype assumptions before the prototype becomes the product baseline;
- classifying assumptions as product contract, implementation detail, temporary shortcut, risk, or evidence gap;
- identifying owners for product realities the prototype ignored;
- deciding which simplicity should survive product reality;
- removing, expiring, or explicitly accepting shortcuts;
- mapping Change Radius across firmware, hardware, manufacturing, service, diagnostics, configuration, update,
  recovery, variants, release, and support;
- recording consequential choices in ADRs or Decision Journal entries;
- naming minimum readiness for manufacturing, service, update, recovery, diagnostics, variants, and release without
  teaching full playbooks.

### Explicitly Out of Scope

Do not turn Chapter 20 into:

- Chapter 21's manufacturing and field reality playbook;
- Chapter 22's configuration, variants, and product lines chapter;
- Chapter 23's embedded observability chapter;
- Chapter 24's release discipline and upgrade-path chapter;
- Chapter 25's reference project walkthrough;
- Chapter 15's Change Radius mapping chapter repeated;
- Chapter 17's ADR or RFC mechanics repeated;
- Chapter 18's Architecture Review practice repeated;
- Chapter 19's Architecture Freeze practice repeated;
- a project-management, product-management, QA, manufacturing-operations, or support-process chapter;
- a new PEAK artifact, metric, ritual, anti-pattern, or vocabulary proposal.

## 11. Recommended Embedded-Systems Story

### Working Title

The Demo That Became the Product

### System

An embedded team builds a prototype that impresses a customer or internal sponsor. It uses one known board revision,
manual calibration, a hard-coded configuration, a debug service tool, a vendor example driver, a lab-only update path,
direct access to hardware state, an ad-hoc manufacturing script, and developer-only diagnostics.

### Trigger

The demo succeeds. Schedule pressure turns the prototype into the product baseline.

### Product Reality

The second board revision behaves differently. Manufacturing cannot repeat manual calibration. Field support cannot
diagnose failures. Configuration variants multiply. Update recovery is undefined. Release packaging depends on
developer scripts. One temporary bypass survives. Nobody knows which prototype assumptions are still valid.

### Principal Engineer Intervention

The Principal Engineer restates the pressure:

> How fast can we ship the prototype?

as:

> Which prototype assumptions must be promoted, replaced, owned, tested, or intentionally accepted before this becomes
> the product?

The intervention should:

- list prototype assumptions;
- classify them as product contract, implementation detail, temporary shortcut, risk, or evidence gap;
- identify owners;
- map Change Radius of turning the prototype into a product baseline;
- preserve valuable simplicity;
- remove or expire temporary shortcuts;
- add minimum manufacturing, service, update, recovery, diagnostic, variant, and release readiness;
- record consequential decisions in ADRs or Decision Journal entries;
- decide what can ship with explicit risk and review trigger.

## 12. Expected Discussion Arc

1. Prototype success proves something valuable, but usually only under prototype conditions.
2. Product architecture must keep behavior working across repeated use and product realities.
3. The prototype-to-product gap is where hidden assumptions become product risk.
4. Assumptions must be listed before they can be owned, tested, removed, or accepted.
5. Some prototype simplicity should be preserved because it remains intentional and stable.
6. Some shortcuts become temporary solutions once they affect users, manufacturing, service, variants, release, or
   support.
7. Product work starts by assigning owners and evidence needs, not by rewriting everything.
8. ADRs and Decision Journal entries keep consequential choices discoverable.
9. The chapter opens Part IV by naming later product realities without teaching their full playbooks.

These are intellectual progression points, not mandatory manuscript headings.

## 13. Boundaries With Later Part IV Chapters

Chapter 20 may identify later Part IV realities but must not teach their detailed playbooks.

- Chapter 21 owns manufacturing and field reality details.
- Chapter 22 owns configuration, variants, and product lines.
- Chapter 23 owns observability in embedded systems.
- Chapter 24 owns release discipline and upgrade paths.
- Chapter 25 owns the reference project walkthrough.

Chapter 20 can ask whether manufacturing, field service, variants, observability, update, recovery, release packaging,
and support ownership have been considered. It should not provide manufacturing workflow design, variant architecture,
observability platform design, release discipline, upgrade-system design, or reference-project implementation.

## 14. Boundaries With Earlier Parts

Use earlier chapters as support without reteaching them:

- Chapters 5 and 13 - evidence, assumptions, and confidence.
- Chapter 6 - leaving systems better than you found them.
- Chapters 11 and 12 - unused flexibility and simplicity.
- Chapters 14 and 15 - boundaries and Change Radius.
- Chapter 16 - failure and recovery behavior.
- Chapter 17 - ADRs, RFCs, and Decision Journal entries.
- Chapter 18 - review before architecture hardens.
- Chapter 19 - freeze decisions through high-risk phases.

Chapter 20 applies those ideas to the move from prototype to product. It should not repeat the Part III architecture
playbook or treat Part IV as a recap of Part III.

## 15. Applicability

Chapter 20 is most useful when:

- a working prototype is being proposed as the product baseline;
- a customer, executive, sponsor, or schedule is rewarding the successful demo;
- one board, one configuration, one fixture, or one customer path has hidden assumptions;
- a prototype shortcut touches manufacturing, service, diagnostics, update, recovery, variants, release, or support;
- the team needs to decide what ships now, what must be replaced, and what risk is explicitly accepted;
- a simple design should be preserved without preserving accidental shortcuts.

Not every prototype needs heavy process. Local, reversible decisions with low Change Radius may need a note and an owner
rather than an ADR. The chapter should teach judgment, not a universal gate.

## 16. Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- prototypes are bad;
- moving from prototype to product always means a rewrite;
- shipping fast is always irresponsible;
- product work means adding flexibility for every possible future variant;
- every prototype assumption needs a formal ADR;
- manufacturing concerns must be fully solved in Chapter 20;
- observability, release, and variant playbooks belong in Chapter 20;
- a successful demo proves product readiness;
- comments are sufficient ownership;
- temporary shortcuts are harmless if everyone remembers them.

Some shortcuts can ship when they have an owner, visible risk, evidence bounds, and a review trigger. Some simplicity
should be preserved because it is a real product feature.

## 17. Violation Patterns

The future draft should make these violations visible:

- the demo is treated as proof of product readiness;
- manual setup becomes an undocumented production step;
- developer scripts become the release process;
- a lab fixture becomes an assumed manufacturing process;
- hard-coded values become hidden calibration behavior;
- one board revision is treated as enough evidence for product behavior;
- direct hardware access becomes a support obligation without an owner;
- developer-only diagnostics are expected to serve field support;
- update works only on the happy path;
- temporary bypasses survive without owner, expiration, or decision;
- variants multiply around assumptions nobody recorded;
- the team preserves all shortcuts in the name of simplicity;
- the team rewrites everything in the name of product work.

Do not create a new anti-pattern ID.

## 18. Engineering Principle Target

Target principle for the future draft:

> Treat a successful prototype as evidence, not architecture. Before it becomes the product, expose its assumptions,
> keep the simplicity that survives, replace the shortcuts that do not, and assign owners to the product realities the
> prototype ignored.

The principle should imply these questions:

1. What did the prototype actually prove?
2. Which assumptions were hidden?
3. Which shortcuts are harmless implementation detail?
4. Which shortcuts become product risk?
5. Which behavior becomes a product promise?
6. Which manual steps must become repeatable?
7. Which diagnostics are needed outside the lab?
8. What changes for manufacturing, service, updates, variants, and release?
9. Which dependency becomes support obligation?
10. Which temporary solution needs owner and expiration?
11. Which risk can ship with explicit review trigger?

The final manuscript may shorten this list for reader rhythm.

## 19. Architecture Exercise Target

### Working Title

`Productize One Prototype Assumption`

Ask the reader to choose one prototype assumption and document:

- assumption;
- where it lives;
- why it was acceptable in the prototype;
- product reality it affects;
- owner;
- evidence available;
- evidence missing;
- whether it becomes contract, implementation detail, temporary risk, or removed shortcut;
- affected surfaces;
- test or validation needed;
- manufacturing, service, update, variant, or release implication;
- decision record needed;
- review trigger or expiration condition.

The exercise must end with:

1. one assumption promoted, removed, or explicitly accepted;
2. one owner;
3. one evidence gap;
4. one prototype-to-product action.

Do not create a new canonical artifact.

## 20. Chapter-Local ADR Brief

### Working Title

`Productize the Prototype Configuration Path Before Release Baseline`

### Context

- Prototype configuration worked in the lab through manual steps and developer scripts.
- The product will need repeatable manufacturing, service, variants, update and recovery, and release support.
- Keeping the prototype path unchanged would preserve speed but hide product risk.

### Decision

- Keep the parts of the prototype that are intentionally simple and stable.
- Replace manual configuration with an owned product configuration path.
- Remove or expire temporary bypasses.
- Record assumptions and residual risks.
- Add minimum diagnostics, validation, and service visibility.
- Create ADR or Decision Journal entries for consequential choices.
- Defer deeper manufacturing, observability, and release playbooks to later chapters.

### Alternatives Considered

- Ship the prototype unchanged.
- Rewrite the entire architecture before the prototype-to-product transition.
- Add flexibility for every possible future variant.
- Defer manufacturing, service, and update concerns until after first release.
- Document assumptions only in comments.
- Freeze prototype behavior immediately.

The ADR should explain why these alternatives are not selected for the story system without claiming they can never be
valid elsewhere.

### Consequences

Benefits include retained delivery speed, clearer ownership, reduced hidden product risk, and a repeatable path from
prototype evidence to product behavior.

Costs include extra prototype-to-product work, explicit risk handling, record updates, and some residual assumptions that may
still need review triggers.

The ADR must make a real story-local architecture decision. It must not reduce to "clean up the prototype."

## 21. PEAK Concept Map

### Concepts Inspected

- `FAILURE-003` - The Successful Prototype.
- `ANTIPATTERN-006` - Temporary Solution.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-005` - Evidence Before Confidence.
- `VOCAB-001` - Change Radius.
- `METRIC-001` - Change Radius.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.
- `METRIC-003` - Discoverability.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-006` - Architecture Freeze.
- `VOCAB-007` - Architecture Health.
- `METRIC-005` - Architecture Health.
- `RITUAL-004` - Architecture Health Review.

### Selected Concepts

- `FAILURE-003` - The Successful Prototype: material because the chapter directly teaches how prototype success can
  become product architecture before assumptions are exposed.
- `ANTIPATTERN-006` - Temporary Solution: material because prototype shortcuts need an owner, expiration, removal, or
  explicit risk decision.
- `LAW-004` - Simplicity Is a Feature: material because the chapter must preserve simple prototype choices that remain
  intentional product design.
- `LAW-006` - Unused Flexibility Is Waste: material because prototype-to-product work should not become speculative flexibility
  for every future variant.
- `LAW-005` - Evidence Before Confidence: material because prototype evidence must be separated from product evidence.
- `VOCAB-001` - Change Radius: material because converting prototype assumptions into product behavior affects multiple
  surfaces.
- `METRIC-001` - Change Radius: material because the chapter estimates the surface affected by each assumption or
  shortcut.
- `ARTIFACT-001` - ADR: material because consequential prototype-to-product decisions may need durable decision records.
- `ARTIFACT-003` - Decision Journal: material because smaller assumption decisions and accepted risks may need
  lightweight closure.
- `RITUAL-001` - Architecture Review: material because turning a prototype into a product baseline may require review
  before hardening.
- `METRIC-003` - Discoverability: material because product assumptions, owners, records, and residual risks must be
  findable.
- `LAW-001` - Every State Has One Owner: material because prototype hardware state, calibration state, and
  configuration state need ownership before product release.
- `LAW-002` - Every API Is a Promise: material because prototype interfaces, service tools, and configuration paths can
  become product promises.
- `LAW-007` - Every Dependency Is a Decision: material because vendor examples, scripts, tools, fixtures, and direct
  dependencies become support obligations when made ready for product use.

### Rejected Concepts

- `ARTIFACT-002` - RFC: relevant to proposals, but Chapter 20 only needs ADR and Decision Journal support for the
  chapter-local decision and assumption closure.
- `ARTIFACT-004` - Mistake Ledger: useful after a prototype-to-product failure, but this chapter should act before the failure
  becomes retrospective material.
- `RITUAL-002` and `VOCAB-006` - Architecture Freeze: freeze can appear as a rejected move, but Chapter 19 already owns
  freeze semantics.
- `VOCAB-007`, `METRIC-005`, and `RITUAL-004` - Architecture Health: later health review may revisit product-ready
  assumptions, but Chapter 20 should not become a recurring health operating model.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as prototype-to-product gap, product baseline, product reality, prototype assumption, field reality, release
baseline, service contract, manufacturing contract, and prototype-to-product action remain chapter-local prose.

### Exact Proposed PEAK Relationships

Register `CHAPTER-020` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-020
  type: illustrates
  to: FAILURE-003

- from: CHAPTER-020
  type: references
  to: ANTIPATTERN-006

- from: CHAPTER-020
  type: references
  to: LAW-004

- from: CHAPTER-020
  type: references
  to: LAW-006

- from: CHAPTER-020
  type: references
  to: LAW-005

- from: CHAPTER-020
  type: references
  to: VOCAB-001

- from: CHAPTER-020
  type: references
  to: METRIC-001

- from: CHAPTER-020
  type: references
  to: ARTIFACT-001

- from: CHAPTER-020
  type: references
  to: ARTIFACT-003

- from: CHAPTER-020
  type: references
  to: RITUAL-001

- from: CHAPTER-020
  type: references
  to: METRIC-003

- from: CHAPTER-020
  type: references
  to: LAW-001

- from: CHAPTER-020
  type: references
  to: LAW-002

- from: CHAPTER-020
  type: references
  to: LAW-007
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

Each section should serve the Chapter 20 role:

- Opening Quote: establish that prototype success is evidence, not a product promise.
- Story: show a successful embedded demo becoming the product baseline with hidden assumptions.
- Discussion: teach prototype versus product, the prototype-to-product gap, assumption classification, ownership, shortcuts,
  evidence, and minimum product realities.
- Engineering Principle: anchor the move from successful prototype to product architecture.
- Architecture Exercise: make one prototype assumption ready for product use.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the story-local decision to make the prototype configuration path ready before release baseline.
- Editor's Commentary: explain how Chapter 20 opens Part IV without teaching later Part IV chapters early.

## 23. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- A prototype is evidence, not a product promise.
- Keep the simplicity that survives contact with product reality.
- Every shortcut needs either an owner, an expiration, or a decision.

These are semantic targets, not mandatory final wording. Do not register them as new canon.

## 24. Technical Credibility Requirements

The future draft must treat the following accurately:

- prototype firmware and hardware assumptions;
- manual calibration and configuration;
- board revisions and component variability;
- service tools and diagnostics;
- update and recovery assumptions;
- manufacturing repeatability;
- supportability;
- release packaging;
- variants;
- dependencies;
- field conditions;
- test evidence;
- temporary workarounds;
- product baseline decisions.

Do not require a specific MCU, RTOS, manufacturing system, release tool, test framework, cloud platform, issue tracker,
or organization structure.

## 25. Terminology and Precision Guardrails

Use terms precisely:

- Prototype: an implementation optimized for fast evidence and learning.
- Product architecture: the decisions and ownership needed for behavior to keep working across product realities.
- Prototype-to-product gap: the distance between prototype assumptions and required operating reality.
- Prototype assumption: a belief, manual step, fixture behavior, script, configuration, wiring, or dependency that made
  the prototype work.
- Shortcut: a deliberate or accidental simplification that may be harmless, temporary, risky, or no longer acceptable.
- Product baseline: the version of behavior, configuration, interfaces, and ownership treated as the product starting
  point.
- Product reality: repeated use, manufacturing, service, field diagnosis, variants, update, recovery, release, support,
  and time.

Avoid misleading statements:

- A successful demo proves readiness.
- Prototype code is always bad.
- Production means rewrite.
- Moving from prototype to product means adding flexibility.
- A comment is ownership.
- A manual script is a release process.
- Temporary shortcuts are safe if everyone remembers them.
- Later chapters' playbooks belong in Chapter 20.

## 26. Failure Modes to Avoid

The later draft must not become:

- a generic checklist;
- a manufacturing process chapter;
- a field-service operations chapter;
- an observability platform chapter;
- a release-management chapter;
- a product-line architecture chapter;
- a project-management or product-management chapter;
- a criticism of prototypes;
- a rewrite manifesto;
- a speculative flexibility chapter;
- Chapter 15, 17, 18, or 19 repeated;
- a new PEAK concept proposal;
- reader-facing draft prose inside the canonical brief.

## 27. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the story contains a concrete embedded prototype that became the product baseline under schedule pressure;
- the prototype includes hidden assumptions across board revision, calibration, configuration, service tooling, vendor
  code, update path, hardware state, manufacturing script, and diagnostics;
- the later product reality reveals credible manufacturing, service, field diagnosis, variant, update, recovery,
  release, and support pressure without teaching those later chapters in full;
- the Principal Engineer move restates the issue from shipping the prototype to exposing, owning, testing, removing, or
  accepting prototype assumptions;
- no primary PEAK concept is assigned unless a later editor decision changes repository convention;
- `FAILURE-003` is materially present as the central anchor;
- prototype success is treated as valuable evidence, not as product readiness;
- simplicity is preserved only when it survives product reality;
- temporary shortcuts have owner, expiration, removal, or explicit decision;
- Change Radius is used without reteaching Chapter 15;
- ADR and Decision Journal use is present without repeating Chapter 17 mechanics;
- Architecture Review is present only where turning the prototype into a baseline needs review before hardening;
- later Part IV playbooks remain out of scope;
- the exercise ends with one assumption promoted, removed, or explicitly accepted; one owner; one evidence gap; and one
  prototype-to-product action;
- the ADR makes a genuine story-local decision about the prototype configuration path;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 28. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach
one idea without drifting into a manufacturing playbook, variant architecture, observability chapter, release process,
or generic product-management advice.

Canon Review should verify that Chapter 20 remains a no-primary Part IV opener, materially illustrates `FAILURE-003`,
preserves the registered relationship set, does not imply a new gap metric or prototype-to-product ledger artifact, and
preserves boundaries with Chapters 21 through 25.

Technical Review should focus on realistic embedded assumptions: board revisions, manual calibration, product
configuration, service tools, vendor examples, hardware state access, manufacturing scripts, diagnostics, update and
recovery, release packaging, variants, support ownership, dependencies, evidence, and temporary workarounds.

Freeze Review should confirm that Chapter 20 remains the first Part IV chapter, keeps the manuscript architecture
intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the
reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
prototype device, board revision issue, calibration path, configuration mechanism, service-tool details, update path,
release packaging, and final notebook wording while preserving the prototype-to-product thesis, PEAK map, and chapter
boundaries.
