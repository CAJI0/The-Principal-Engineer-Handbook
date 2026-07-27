# CHAPTER-034 Canonical Brief: Managing Utility Gravity

## 1. Metadata

- Stable ID: `CHAPTER-034`.
- Title: `Managing Utility Gravity`.
- Part: Part VI - Legacy.
- Chapter number: 34.
- Expected manuscript path: `book/06-legacy/34-managing-utility-gravity.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-034-managing-utility-gravity.md`.
- Branch: `chapter34`.
- Verified baseline `origin/main`: `0d34780320928576dcedceed078a412f6176f256`.
- Baseline evidence: PR #35 Chapter 33 squash merge commit,
  `Chapter 33: Finding Silent Coupling (#35)`.
- Canonical predecessor: `CHAPTER-033` - Finding Silent Coupling.
- Part position: third chapter of Part VI - Legacy.
- Reader-facing draft created: no.
- Expected lifecycle status after registration: `draft`.
- Primary concept: none. Chapter 34 illustrates the existing `SMELL-002` Utility Gravity smell and references the
  existing `VOCAB-009` Utility Gravity vocabulary term; it must not add a `primary_concept` registry field.
- Central illustrated concept: `SMELL-002` - Utility Gravity.
- Central vocabulary term: `VOCAB-009` - Utility Gravity.
- Central chapter-local practice: mapping utility promises, owners, consumers, state, policies, and change radius before
  adding more behavior or extracting behavior away.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `0d34780320928576dcedceed078a412f6176f256`.
- That baseline is the PR #35 Chapter 33 squash merge commit,
  `Chapter 33: Finding Silent Coupling (#35)`.
- The baseline contains the Chapter 33 manuscript, canonical brief, editor log, and index updates.
- `CHAPTER-033` is registered as `canonical` in `knowledge/index.yaml`.
- Chapter 33 Freeze Review is recorded in `editor/EDITOR_LOG.md` with PR readiness and Frozen lifecycle status.
- `CHAPTER-001` through `CHAPTER-033` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-034` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 34 canonical brief or reader-facing manuscript existed before this registration.
- No Chapter 35, Chapter 36, or Chapter 37 manuscript existed before this registration.
- No tracked `site/` output existed before this registration.
- The PEAK graph already contains `SMELL-002` Utility Gravity and `VOCAB-009` Utility Gravity, so no new concept is
  required.

## 3. Part VI Role

Chapter 34 follows the first two Legacy chapters. Chapter 32 taught the reader to build a reading map before changing a
legacy system. Chapter 33 taught the reader to find hidden behavioral dependencies that make local changes non-local.
Chapter 34 narrows that attention to a common legacy force: a convenient utility becoming the place where unrelated
product decisions, policies, platform assumptions, hidden state, and cross-team dependencies accumulate.

The chapter should prepare the reader for later Legacy work without teaching it early. Chapter 35 owns Boolean
Explosion, Chapter 36 owns deletion, and Chapter 37 owns trust-preserving refactoring. Chapter 34 should make utility
gravity visible and governable before the team decides whether to split, delete, or refactor anything.

## 4. Canonical Purpose

Prepare Chapter 34 to teach that utility gravity is managed by making the utility's promises, owners, consumers, state,
policies, and change radius visible before adding more behavior to it or extracting behavior away from it.

Candidate thesis for the future manuscript:

> A utility becomes architecture when unrelated product behavior starts depending on it.

The chapter should move the reader away from asking:

> Is this code shared?

to asking:

> What promises, policies, state, owners, consumers, and product paths now depend on this shared code?

## 5. Primary-Concept Resolution

Chapter 34 has no new primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. The graph already
contains `SMELL-002` Utility Gravity and `VOCAB-009` Utility Gravity. Chapter 34 should illustrate the existing smell
and use the existing vocabulary term while referencing the laws, metrics, artifacts, rituals, smells, anti-patterns, and
failure stories needed to manage the force responsibly.

Utility promise map, utility boundary map, consumer inventory, responsibility gravity, shared mechanism, product policy
split, and extraction candidate remain chapter-local prose. Do not create a new PEAK concept, ID, artifact, ritual,
metric, vocabulary term, smell, anti-pattern, failure story, primary-concept field, or relationship verb for them.

## 6. Central Thesis

Utility gravity grows when a helper becomes the easiest place to put unrelated decisions. In a legacy system, the
responsible move is not to add another option, rewrite the helper, or extract a library on instinct. The responsible
move is to name what the utility promises, who owns it, who consumes it, what state and policy it carries, and how far a
change can travel.

Approved supporting formulation for the future draft:

> Before moving a utility, discover what it has become responsible for.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, artifact, ritual,
metric, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. a shared utility is harmless because it is small;
2. utility cleanup is mostly about code tidiness;
3. reuse is automatically cheaper than local duplication;
4. product policy inside a helper is an implementation detail;
5. a utility has no real API because it is internal;
6. the team can split or rewrite a utility when the code shape looks bad;
7. consumers are easy to find from imports alone;
8. shared defaults, retries, flags, time conversion, and logging categories are minor details;
9. the right response to an overgrown helper is deletion or broad refactoring;
10. nobody owns a utility because everybody uses it.

By the end of the chapter, the reader should be able to:

1. recognize when a helper has become a hidden platform;
2. distinguish shared mechanism from centralized product policy;
3. identify utility promises, owners, consumers, state, configuration, policy, and review paths;
4. use Change Radius, Discoverability, and Bus Factor as evidence lenses for utility risk;
5. decide whether to contain, split, document, review, or leave a utility alone;
6. avoid treating utility movement as cosmetic cleanup;
7. route consequential boundary movement through records and review instead of memory;
8. preserve compatibility while preparing later deletion or refactoring decisions.

## 8. Utility Gravity Scope

For Chapter 34, Utility Gravity means the structural pull by which a convenient shared utility accumulates responsibility
from unrelated product paths until changing it affects more behavior than its name, owner, tests, or review path reveal.

The future manuscript may examine:

- retry policy and fallback behavior added to a helper because it was already imported everywhere;
- time conversion, device defaults, and variant interpretation hidden behind utility calls;
- feature flags and configuration interpretation that centralize product policy in a utility;
- diagnostic strings, logging categories, and error handling that become operational interfaces;
- hidden state cached inside a helper without an owner;
- platform assumptions leaking into product code through a convenience boundary;
- broad consumers that make one utility change a wide Change Radius;
- senior memory as the only reliable map of who depends on the utility;
- ADR, RFC, Decision Journal, and Architecture Ledger records used to make boundary movement visible;
- Architecture Review and Architecture Health Review as places to examine utility responsibility.

The chapter should help the reader contain and redirect gravity. It should not treat every utility as bad or every
shared helper as a platform.

## 9. Managing Order and Evidence

The future manuscript should teach a managing order that starts with the utility's current role rather than the desired
refactor.

Useful finding layers:

1. What behavior does the utility actually promise today?
2. Which consumers depend on that behavior, including tools, tests, release paths, support, and manufacturing?
3. Which state, defaults, flags, retries, conversions, logging categories, or policies does it carry?
4. Who owns the utility, who owns the product policy inside it, and who reviews changes?
5. What changes when the utility changes?
6. Which parts are shared mechanism and which parts are product-specific policy?
7. What evidence proves a dependency is active rather than historical?
8. Which boundary needs a record, test, owner, review trigger, or later split?
9. Which movement should be deferred to Chapter 36 deletion or Chapter 37 refactoring work?

Do not turn this into a rigid checklist. The order should change the reader's attention from code tidiness to system
responsibility.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 34 covers:

- managing Utility Gravity as responsibility accumulation inside shared utilities;
- recognizing a helper that has become a hidden platform;
- utility promises, owners, consumers, state, policies, review triggers, and Change Radius;
- shared mechanism versus product-specific policy;
- evidence from imports, tests, logs, release paths, support tools, manufacturing scripts, records, and team memory;
- Bus Factor and Discoverability risk around utility ownership and consumer knowledge;
- ADRs, RFCs, Decision Journal entries, Architecture Ledger rows, Architecture Review, and Architecture Health Review as
  ways to make utility boundaries visible;
- Silent Coupling, Hidden State, Platform Leakage, Global Configuration, HAL Everywhere, God Module, and Temporary
  Solution as related forces;
- failure stories where a helper or shared component became a platform through convenience.

### Explicitly Out of Scope

Do not turn Chapter 34 into:

- a generic cleanup chapter;
- a reusable-code enthusiasm chapter;
- a framework design chapter;
- a library extraction tutorial;
- a Dependency Injection chapter;
- a static analysis tutorial;
- a Boolean Explosion chapter;
- a safe-deletion chapter;
- a broad refactoring chapter;
- a platform architecture tutorial;
- a rewrite argument;
- a new PEAK concept proposal.

## 11. Recommended Legacy-System Story

Use a story close to:

`The Helper That Became the Platform`

A small utility module begins as a harmless helper used by several teams. Over time it absorbs retry policy, time
conversion, device defaults, feature flags, configuration interpretation, logging categories, fallback behavior, and
product-specific decisions. Because it is "just a utility," no team treats it as a real interface with owners,
consumers, tests, review triggers, or architecture health signals.

A later change appears local but breaks another product path because the utility has become a hidden platform. The
Principal Engineer does not start by rewriting or deleting it. They first map its promises, owners, consumers, state,
policies, and change radius, then split product policy from shared mechanism and create review boundaries for future
movement.

The story should end with visible ownership and decision paths, not a triumphant cleanup campaign.

## 12. Expected Discussion Arc

The future manuscript should move through this arc:

1. Define Utility Gravity as responsibility accumulation around convenient shared helpers.
2. Show how local convenience becomes cross-system policy.
3. Distinguish legitimate shared mechanism from hidden platform behavior.
4. Map promises, owners, consumers, state, policies, and Change Radius.
5. Use evidence before moving or splitting utility behavior.
6. Separate product policy from shared mechanism.
7. Decide whether to contain, split, document, review, or leave the utility alone.
8. Record consequential boundary decisions without creating a new canonical artifact.
9. Hand off deletion and trust-preserving refactoring to later chapters.

## 13. Boundaries With Part VI Chapters

Chapter 34 owns managing Utility Gravity. It must preserve neighboring Legacy chapters:

- Chapter 32 owns the first pass of understanding a legacy system and building a reading map before change. Chapter 34
  may reference reading maps, consumers, state, and ownership discovery, but must not reteach the full legacy-reading
  method.
- Chapter 33 owns detecting hidden behavioral dependencies and making Silent Coupling visible. Chapter 34 may use Silent
  Coupling as a supporting smell because utility gravity often hides coupling inside shared helpers, but Chapter 34's
  center is the gravitational accumulation of unrelated responsibility inside a utility boundary.
- Chapter 35 owns Boolean Explosion and flag or branch complexity. Chapter 34 may mention flags or configuration only
  when they are being pulled into a utility and increasing its gravity. It must not teach Boolean Explosion reduction.
- Chapter 36 owns deletion, retirement, fallback removal, and Deletion Day. Chapter 34 may identify dead or obsolete
  utility behavior as a signal, but it must not teach safe deletion, removal sequencing, or deletion rituals.
- Chapter 37 owns trust-preserving refactoring across product boundaries. Chapter 34 may prepare later refactoring by
  making utility responsibility visible, but it must not become the broad refactoring chapter.

## 14. Boundaries With Earlier Parts

Use earlier chapters as applied tools without repeating them:

- Chapter 7 and `LAW-001` own state ownership. Chapter 34 uses ownership to ask who owns utility state and policy, not
  to reteach the law.
- Chapter 8 and `LAW-002` own API promises. Chapter 34 uses API promise thinking to treat utility functions as real
  contracts, not to reteach API design.
- Chapter 9 and `LAW-007` own dependency decisions. Chapter 34 uses dependency thinking to make utility consumers
  visible, not to reteach dependency theory.
- Chapter 12 and `LAW-004` own simplicity. Chapter 34 uses simplicity to distinguish useful shared mechanism from
  overgrown convenience, not to argue that every utility should be simpler.
- Chapter 13 and `LAW-005` own evidence. Chapter 34 requires evidence before moving or splitting utility behavior, not
  confidence from code shape alone.
- Chapter 15 owns Change Radius. Chapter 34 uses Change Radius to evaluate utility centrality, not to reteach the
  metric.
- Chapter 17 owns ADRs and RFCs. Chapter 34 uses ADR and RFC records for boundary movement, not to teach those
  artifacts.
- Chapter 18 owns Architecture Review. Chapter 34 may send utility-boundary changes to Architecture Review but does not
  reteach the ritual.
- Chapter 31 owns Architecture Health Reviews. Chapter 34 may use Architecture Health Review as a place where utility
  gravity is surfaced, not as the ritual's main tutorial.

## 15. Applicability

Chapter 34 is useful when:

- a shared helper attracts flags, defaults, retries, logging, conversions, or fallback policy;
- changing one utility requires reviewers from unrelated product paths;
- utility policy ownership is unclear;
- imports show consumers but not product consequences;
- utility tests pass while product paths can still break;
- a helper's name hides platform behavior;
- a utility is proposed for extraction, rewrite, or deletion before its consumers are named;
- release, support, manufacturing, or service-tool behavior depends on a shared helper;
- one senior engineer knows which utility changes are dangerous.

Not every shared helper has utility gravity. Use the practice when unrelated responsibility, unclear ownership, hidden
policy, or wide change impact has gathered around a utility boundary.

## 16. Limits and Exceptions

Managing utility gravity should be proportionate.

- For a narrow helper with clear ownership, tests, and a small consumer set, normal review may be enough.
- During an active incident, stabilize the incident before boundary redesign.
- If a utility is intentionally a platform, name the platform contract, owners, and consumers instead of pretending it is
  "just a helper."
- If evidence is thin, use a safe probe before moving behavior.
- If deletion is attractive, preserve Chapter 36's boundary.
- If refactoring is attractive, preserve Chapter 37's trust-preserving boundary.

The chapter should avoid both extremes: allowing every team to keep adding behavior to the helper and demanding a broad
rewrite before the utility's real promises are known.

## 17. Violation Patterns

The future manuscript should warn against these patterns:

- treating a utility as having no owner because it is shared;
- adding one more flag, retry, default, or fallback because the helper is convenient;
- centralizing product policy while calling it reuse;
- extracting a library before naming consumers and promises;
- relying only on import graphs;
- splitting a utility without preserving product compatibility;
- documenting the helper without assigning review boundaries;
- letting senior memory remain the only map;
- turning Utility Gravity into a blame story;
- teaching Boolean Explosion, deletion, or broad refactoring early.

## 18. Engineering Principle Target

Target meaning:

> Treat an overgrown utility as an architectural boundary. Before adding, extracting, or moving behavior, name its
> promises, owners, consumers, state, policies, evidence, and change radius.

Potential questions:

1. What does this utility promise today?
2. Which product paths consume it?
3. Which state, defaults, flags, retries, conversions, logging categories, or fallback policies does it carry?
4. Who owns the mechanism and who owns the product policy?
5. What would break if the utility changed while its name stayed the same?
6. Which consumers are visible only through tests, tools, release paths, support, manufacturing, or memory?
7. What evidence proves the dependency is active?
8. Which responsibility should remain shared, move behind a contract, split into product policy, or wait?
9. Which record or review path must be repaired before movement?

The final manuscript may shorten this list for rhythm. It must not become an oversized checklist.

## 19. Architecture Exercise Target

Use:

`Map the Utility Before Moving It`

Ask the reader to choose one shared helper or utility and document:

- utility name and visible owner;
- current promise;
- known consumers;
- suspected hidden consumers;
- state, defaults, flags, retries, conversions, logging categories, or fallback behavior inside it;
- product policy mixed with shared mechanism;
- evidence sources;
- likely Change Radius;
- Bus Factor and Discoverability risk;
- review boundary;
- record to update;
- decision to make now;
- deletion or refactoring question to defer.

End with:

1. one utility promise to name;
2. one consumer to verify;
3. one owner or reviewer to assign;
4. one record to repair;
5. one movement to defer until evidence exists.

Do not create a new canonical artifact.

## 20. Chapter-Local ADR Brief

Use a decision close to:

`Split Product Policy From the Shared Device Utility Before Adding More Behavior`

Context:

- a shared device utility now carries retry policy, time conversion, defaults, flags, logging categories, fallback
  behavior, and product-specific decisions;
- firmware, backend, service tools, manufacturing scripts, support procedures, release validation, and tests may depend
  on the current behavior;
- no current record names the utility as a platform-like interface;
- adding one more branch would increase utility gravity and make later movement harder.

Decision:

- do not add new behavior until the utility's promises, owners, consumers, state, policies, and Change Radius are mapped;
- separate shared mechanism from product-specific policy where evidence supports the split;
- add characterization or contract tests around active utility promises;
- update the ADR, RFC, Decision Journal, or Architecture Ledger with owner, consumers, evidence, risk, and revisit
  trigger;
- route cross-boundary utility movement through Architecture Review;
- surface recurring utility gravity in Architecture Health Review;
- defer deletion or broad refactoring until compatibility and product trust can be preserved.

Alternatives:

- add another flag because the utility is already shared;
- rewrite the utility before naming consumers;
- extract a library from the current shape;
- rely on import graphs alone;
- ask the senior engineer and keep the knowledge in memory;
- remove obsolete-looking branches before dependent behavior is understood.

Consequences should include slower first movement, clearer ownership, reduced surprise, better tests and records, and a
path toward later simplification. The ADR must not reduce to "clean up the helper."

## 21. PEAK Concept Map

### Concepts Inspected

- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-005` - Evidence Before Confidence.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `VOCAB-005` - Deletion Day.
- `VOCAB-009` - Utility Gravity.
- `VOCAB-010` - Boolean Explosion.
- `METRIC-001` - Change Radius.
- `METRIC-002` - Bus Factor.
- `METRIC-003` - Discoverability.
- `METRIC-004` - API Stability.
- `METRIC-005` - Architecture Health.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-002` - RFC.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-004` - Mistake Ledger.
- `ARTIFACT-005` - Event Catalog.
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-001` - Architecture Review.
- `RITUAL-002` - Architecture Freeze.
- `RITUAL-003` - Deletion Day.
- `RITUAL-004` - Architecture Health Review.
- `RITUAL-005` - Architecture Court.
- `RITUAL-006` - RFC Friday.
- `SMELL-001` - Silent Coupling.
- `SMELL-002` - Utility Gravity.
- `SMELL-003` - Boolean Explosion.
- `SMELL-004` - Hidden State.
- `SMELL-005` - Platform Leakage.
- `SMELL-006` - Event Explosion.
- `ANTIPATTERN-001` - God Module.
- `ANTIPATTERN-002` - HAL Everywhere.
- `ANTIPATTERN-003` - Global Configuration.
- `ANTIPATTERN-006` - Temporary Solution.
- `FAILURE-001` - Logger That Became a Platform.
- `FAILURE-004` - The Hero Engineer.
- `FAILURE-005` - The Release We Should Have Delayed.

### Selected Concepts

- `SMELL-002` - Utility Gravity: central illustrated smell because Chapter 34 teaches how an over-convenient shared
  helper accumulates unrelated responsibility.
- `VOCAB-009` - Utility Gravity: material vocabulary because the chapter gives the reader a precise name for this
  structural force.
- `LAW-001` - Every State Has One Owner: material because utility state and policy need visible ownership.
- `LAW-002` - Every API Is a Promise: material because internal utility functions can become real contracts.
- `LAW-004` - Simplicity Is a Feature: material because the chapter distinguishes useful shared mechanism from
  overgrown convenience.
- `LAW-005` - Evidence Before Confidence: material because utility movement should follow evidence, not code-shape
  confidence.
- `LAW-007` - Every Dependency Is a Decision: material because utility consumers and shared behavior make dependency
  decisions visible.
- `VOCAB-001` - Change Radius: material vocabulary for the affected surface behind a supposedly small utility change.
- `METRIC-001` - Change Radius: material because utility gravity widens the real affected surface of one change.
- `METRIC-002` - Bus Factor: material because one person often knows which utility behavior is dangerous to change.
- `METRIC-003` - Discoverability: material because future engineers need to find utility promises and consumers.
- `ARTIFACT-001` - ADR: material because consequential utility boundary decisions may need a durable record.
- `ARTIFACT-002` - RFC: material because cross-team utility movement may need proposal review.
- `ARTIFACT-003` - Decision Journal: material because smaller containment choices need lightweight memory.
- `ARTIFACT-006` - Architecture Ledger: material because utility responsibility, owner, risk, and revisit triggers need
  visibility.
- `RITUAL-001` - Architecture Review: material because cross-boundary utility movement may need review.
- `RITUAL-004` - Architecture Health Review: material because utility gravity can be surfaced as a recurring health
  signal.
- `SMELL-001` - Silent Coupling: material because utility gravity often hides coupling inside shared helpers.
- `SMELL-004` - Hidden State: material because utility caches and defaults can hide state ownership.
- `SMELL-005` - Platform Leakage: material because platform assumptions can leak through a convenience utility.
- `ANTIPATTERN-001` - God Module: material because an overgrown utility can become a disguised God Module.
- `ANTIPATTERN-002` - HAL Everywhere: material because platform convenience can spread hardware or platform assumptions.
- `ANTIPATTERN-003` - Global Configuration: material because utility gravity often pulls configuration policy inward.
- `ANTIPATTERN-006` - Temporary Solution: material because temporary helper behavior can become product promise.
- `FAILURE-001` - Logger That Became a Platform: material because it is the direct failure-story analogue for accidental
  platform gravity.
- `FAILURE-004` - The Hero Engineer: material because single-person memory often protects utility boundaries.
- `FAILURE-005` - The Release We Should Have Delayed: material because release pressure exposes broad utility impact.

### Rejected or Background Concepts

- `VOCAB-010` and `SMELL-003` - Boolean Explosion: Chapter 35 owns Boolean Explosion.
- `VOCAB-005` and `RITUAL-003` - Deletion Day: Chapter 36 owns deletion and removal rituals.
- `LAW-006` - Unused Flexibility Is Waste: nearby when unused utility hooks accumulate, but Chapter 36 owns deletion and
  Chapter 37 owns trust-preserving refactoring.
- `SMELL-006` - Event Explosion: may appear in product systems but is not the center of Utility Gravity.
- `ARTIFACT-004` - Mistake Ledger: useful after incidents, but not central to the Chapter 34 teaching frame.
- `ARTIFACT-005` - Event Catalog: useful when utility gravity manifests through event semantics, but not generally
  central.
- `ARTIFACT-007` - Weak Signal Register: Chapter 31 owns health review signal gathering; Chapter 34 focuses on
  utility-boundary mapping.
- `METRIC-004` - API Stability: related to utility APIs, but Chapter 34 is about responsibility gravity and change
  radius rather than API stability measurement.
- `METRIC-005` - Architecture Health: background through Architecture Health Review, but Chapter 31 owns the metric.
- `RITUAL-002` - Architecture Freeze: release and freeze governance belongs earlier Part IV and Part V material, not
  this chapter.
- `RITUAL-005` - Architecture Court and `RITUAL-006` - RFC Friday: existing rituals, but not central to this chapter.

### Exact Outgoing Relationships

```yaml
- from: CHAPTER-034
  type: illustrates
  to: SMELL-002
- from: CHAPTER-034
  type: references
  to: VOCAB-009
- from: CHAPTER-034
  type: references
  to: LAW-001
- from: CHAPTER-034
  type: references
  to: LAW-002
- from: CHAPTER-034
  type: references
  to: LAW-004
- from: CHAPTER-034
  type: references
  to: LAW-005
- from: CHAPTER-034
  type: references
  to: LAW-007
- from: CHAPTER-034
  type: references
  to: VOCAB-001
- from: CHAPTER-034
  type: references
  to: METRIC-001
- from: CHAPTER-034
  type: references
  to: METRIC-002
- from: CHAPTER-034
  type: references
  to: METRIC-003
- from: CHAPTER-034
  type: references
  to: ARTIFACT-001
- from: CHAPTER-034
  type: references
  to: ARTIFACT-002
- from: CHAPTER-034
  type: references
  to: ARTIFACT-003
- from: CHAPTER-034
  type: references
  to: ARTIFACT-006
- from: CHAPTER-034
  type: references
  to: RITUAL-001
- from: CHAPTER-034
  type: references
  to: RITUAL-004
- from: CHAPTER-034
  type: references
  to: SMELL-001
- from: CHAPTER-034
  type: references
  to: SMELL-004
- from: CHAPTER-034
  type: references
  to: SMELL-005
- from: CHAPTER-034
  type: references
  to: ANTIPATTERN-001
- from: CHAPTER-034
  type: references
  to: ANTIPATTERN-002
- from: CHAPTER-034
  type: references
  to: ANTIPATTERN-003
- from: CHAPTER-034
  type: references
  to: ANTIPATTERN-006
- from: CHAPTER-034
  type: references
  to: FAILURE-001
- from: CHAPTER-034
  type: references
  to: FAILURE-004
- from: CHAPTER-034
  type: references
  to: FAILURE-005
```

### Valid Relationship Verbs

The registered relationships use only `illustrates` and `references`, valid PEAK relationship types in
`editor/KNOWLEDGE_MODEL.md` and the existing chapter graph.

### No-New-Concept Result

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, vocabulary concept, ID,
relationship verb, or primary-concept field is required.

## 22. Required Reader-Facing Chapter Architecture

The future manuscript must preserve the standard architecture:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Do not modify `editor/CHAPTER_ARCHITECTURE.md`.

## 23. Principal's Notebook Shape

The future manuscript must include exactly three short observations, no explanations.

Semantic targets:

- Utility gravity turns convenience into responsibility.
- Shared helpers need named promises and owners.
- Do not move the utility before mapping its consumers.

Possible house-style lines:

- A shared helper can become a hidden platform.
- Utility promises need owners.
- Map the consumers before moving the code.

## 24. Technical Credibility Requirements

The future manuscript must treat accurately:

- utility gravity as responsibility accumulation, not merely code reuse;
- legitimate helpers versus hidden platforms;
- embedded, backend, service-tool, manufacturing, support, release, and field workflows;
- state, defaults, retries, flags, configuration, logging, diagnostics, fallback behavior, and product policy as possible
  utility promises;
- import graphs as useful but insufficient consumer evidence;
- tests and logs as evidence but not a complete map;
- senior memory as useful but insufficient;
- containment, boundary records, and review triggers as first responses before deletion or broad refactoring;
- active dependencies versus historical fear.

## 25. Terminology and Precision Guardrails

Use terms precisely:

- `Utility Gravity`: existing PEAK smell and vocabulary term for responsibility accumulating inside a utility boundary.
- `hidden platform`: prose term for a shared helper that now carries product promises and cross-team dependencies.
- `shared mechanism`: prose term for behavior that can responsibly remain common.
- `product policy`: prose term for product-specific decisions that should not hide inside a generic helper.
- `utility promise map`: chapter-local prose for a compact trace of promises, owners, consumers, state, policies,
  evidence, and next decision.

Avoid implying:

- all utilities are bad;
- reuse is always wrong;
- every overgrown utility should be deleted;
- every utility should become a platform;
- import graphs reveal the full consumer set;
- static analysis is sufficient;
- documentation alone fixes utility gravity;
- Chapter 34 owns Boolean Explosion, deletion, or trust-preserving refactoring.

## 26. Failure Modes to Avoid

Avoid these draft failures:

- writing a generic cleanup or refactoring chapter;
- teaching Chapter 35, 36, or 37 early;
- treating utility gravity as only file size or function count;
- making the solution a rewrite;
- making the solution deletion;
- using library extraction as the default answer;
- losing the embedded/product context;
- creating a new PEAK concept, artifact, metric, ritual, vocabulary term, smell, anti-pattern, failure story, or ID;
- over-connecting the graph to background concepts that only appear as previews.

## 27. Author Draft Acceptance Criteria

The Author Draft should pass when:

- it creates `book/06-legacy/34-managing-utility-gravity.md`;
- it preserves the required reader-facing chapter architecture;
- it keeps `CHAPTER-034` as `draft` in `knowledge/index.yaml`;
- it preserves the exact registered Chapter 34 relationship set;
- it keeps no-primary resolution and creates no new PEAK concept;
- it illustrates `SMELL-002` and materially uses `VOCAB-009`;
- it teaches utility promises, owners, consumers, state, policies, evidence, and Change Radius;
- it uses the recommended story or an equivalent credible legacy utility story;
- it ends with containment and visible decision paths, not a full rewrite or deletion campaign;
- it includes exactly three Principal's Notebook observations;
- it does not create later Part VI chapters early;
- it does not modify Chapters 1-33, Part VI README, table of contents, `editor/CHAPTER_ARCHITECTURE.md`,
  `editor/CANON.md`, or PEAK concept files.

## 28. Validation Notes

This brief registration must validate that:

- `CHAPTER-034` exists exactly once in `knowledge/index.yaml`;
- `CHAPTER-034` has status `draft`;
- `CHAPTER-034` has no `primary_concept`;
- every target in the Chapter 34 relationship set exists as an entity;
- relationship verbs are only `illustrates` and `references`;
- no duplicate Chapter 34 relationships exist;
- no self-edge exists;
- Chapters 1-33 remain canonical;
- Chapter 35, Chapter 36, and Chapter 37 are not registered;
- the Chapter 34 manuscript remains absent;
- no tracked `site/` output exists.

## 29. Review Handoff Notes

For the Author Draft:

- write the manuscript only after this canonical brief is committed and pushed;
- keep the story centered on a working legacy system where a utility became a hidden platform through convenience;
- make the Principal Engineer's first move mapping promises, owners, consumers, state, policies, and Change Radius;
- use utility promise map and product policy split as chapter-local prose only;
- ensure selected PEAK concepts are materially present if the registered relationship set is kept;
- keep Chapter 35 Boolean Explosion, Chapter 36 Deleting Safely, and Chapter 37 Refactoring Without Losing Product Trust
  as future boundaries;
- do not open a pull request or begin review gates during the Author Draft prompt.
