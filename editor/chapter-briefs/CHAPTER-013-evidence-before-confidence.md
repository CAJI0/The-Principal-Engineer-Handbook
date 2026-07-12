# CHAPTER-013 Canonical Brief: Evidence Before Confidence

## Metadata

- Stable ID: `CHAPTER-013`.
- Title: `Evidence Before Confidence`.
- Part: Part II - The Laws.
- Chapter number: 13.
- Expected manuscript path: `book/02-the-laws/13-evidence-before-confidence.md`.
- Expected canonical brief path: `editor/chapter-briefs/CHAPTER-013-evidence-before-confidence.md`.
- Branch: `chapter13`.
- Verified baseline `origin/main`: `5aaa875a39f0423f170ee59b88dc4bcc82cbb0eb`.
- Canonical predecessor: `CHAPTER-012` - Simplicity Is a Feature.
- Part position: final chapter of Part II - The Laws.
- Reader-facing draft created: no.
- Primary law: `LAW-005` - Evidence Before Confidence.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## Repository-Grounded Findings

- `origin/main` resolves to `5aaa875a39f0423f170ee59b88dc4bcc82cbb0eb`.
- That baseline is the PR #14 squash commit, `Chapter 12: Simplicity Is a Feature (#14)`.
- The Chapter 12 feature-branch Freeze commit `d9d3bcc78b12d56353e4e96259d15d992860f385` is not required to be an
  ancestor of `main` because PR #14 used squash merge.
- The final Chapter 12 lifecycle files in the PR #14 squash commit are tree-equivalent to the final feature-branch
  Freeze commit for the checked Chapter 12 paths.
- `CHAPTER-001` through `CHAPTER-012` are registered as `canonical` in `knowledge/index.yaml`.
- Chapter 12 exists at `book/02-the-laws/12-simplicity-is-a-feature.md`.
- `editor/EDITOR_LOG.md` records Chapter 12 Editorial, Canon, Technical, and Freeze Review entries in order.
- The repository table of contents places `Evidence Before Confidence` after `Simplicity Is a Feature` as the final
  chapter of Part II.
- `LAW-005` exists exactly once and is named `Evidence Before Confidence`.
- `LAW-005` states: "Confidence should follow evidence, not replace it."
- The `LAW-005` law file identifies the typical violation as accepting a timing margin because a prototype never failed
  on the bench.
- Chapter 5, `Technical Judgment and Evidence`, is already the Part I operational treatment of `LAW-005`.
- Chapter 5 uses the buffered flash-logging story, the evidence-bounded judgment exercise, and the staged flash-logging
  ADR.
- Chapters 7 through 12 each use evidence locally but leave evidence quality, confidence calibration, validation, proof
  standards, and confidence maintenance to Chapter 13.
- `CHAPTER-013` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 13 canonical brief or reader-facing manuscript existed before this registration.
- No local or remote branch named `chapter13` existed before the working branch was created.
- No tracked `site/` output existed before this registration.

## 1. Canonical Purpose

Prepare Chapter 13 to teach the final Part II law: architecture confidence must remain tied to evidence that still
supports the claim being carried forward.

The chapter should move the reader from treating confidence as a permanent property of an old decision toward treating
confidence as current, conditional, owned, bounded, and revisable. A design may have satisfied the previous Part II laws
when reviewed. That does not make the team's current confidence self-validating after products, versions, hardware,
tool chains, loads, environments, observability, or operating exposure change.

The chapter must not create a reader-facing draft during this task. It must constrain the later Author Draft.

## 2. Exact Law Statement

`LAW-005` states:

> Confidence should follow evidence, not replace it.

Chapter 13 must preserve that statement and apply it to architecture confidence over time.

## 3. Distinction From Chapter 5

Chapter 5 owns the Part I operating discipline for forming a defensible judgment for a current commitment. It teaches
claim identification, observation versus inference, evidence relevance, representativeness, independence, freshness,
measurement limitations, residual uncertainty, consequence, reversibility, the next evidence action, and sufficiency for
the next commitment.

Chapter 13 owns the lifecycle discipline for carrying architecture confidence forward after the original decision. It
asks whether the claim is still active, whether the evidence still transfers to the current product version and operating
conditions, what has changed since the evidence was collected, what weak signals or counter-evidence should lower
confidence, who owns revalidation, and what trigger should reopen the decision.

Both chapters are necessary:

- Chapter 5 prevents a team from making the current commitment with confidence that outruns the evidence.
- Chapter 13 prevents an old architecture confidence claim from surviving after the evidence envelope, product exposure,
  or operating assumptions have changed.

The future Chapter 13 manuscript must not reuse Chapter 5's buffered flash-logging story, evidence-bounded judgment
exercise, staged flash-logging ADR, discussion arc, or notebook observations.

## 4. Central Thesis

Architecture confidence is temporary and conditional. It must remain traceable to a specific claim, evidence provenance,
product version, operating conditions, residual uncertainty, and review trigger.

Approved supporting formulation for the future draft:

> Keep architecture confidence attached to a specific claim, evidence envelope, and review trigger. When the system or
> conditions change, revalidate the assumption before carrying the confidence forward.

This formulation is chapter-level language. Do not register it as a new PEAK law, maxim, principle, metric, artifact,
ritual, smell, anti-pattern, failure story, or vocabulary concept.

## 5. Reader Transformation

Before the chapter, the reader may think:

1. an old review means the architecture claim is still supported;
2. a successful prototype transfers naturally to production;
3. a passed test remains strong evidence after the system changes;
4. years without reported failure prove the design is reliable;
5. an unchanged ADR status means confidence is still current;
6. weak signals can be ignored until they prove a cause;
7. revalidation means rerunning the easiest old test;
8. a good outcome proves the original reasoning was sound.

By the end of the chapter, the reader should be able to:

1. name the current architecture claim being relied on;
2. identify which product versions, variants, hardware revisions, builds, loads, and environments the evidence covered;
3. distinguish valid historical evidence from evidence that no longer transfers;
4. explain why confidence can narrow without declaring the old decision irresponsible;
5. use weak signals and counter-evidence to adjust confidence before root cause is proven;
6. define proportional revalidation targeted at the changed assumption;
7. assign ownership for the claim, evidence record, confidence, and review trigger;
8. record confidence in existing artifacts without inventing a new evidence framework.

## 6. Semantic Definition of Architecture Confidence

Architecture confidence is the current degree of justified belief that an architecture claim remains true for a specified
product version, configuration, environment, exposure, and operating envelope.

Architecture confidence is not:

- certainty;
- consensus;
- seniority;
- lack of objections;
- repeated assertion;
- a successful release;
- a large test count;
- an unchanged ADR status;
- proof that the original decision was perfect;
- permission to stop watching for counter-evidence.

Confidence can rise, fall, narrow, or require revalidation as the system changes.

## 7. Exact In-Scope and Out-of-Scope

### In Scope

Chapter 13 covers:

- active architecture claims that remain in force after the original decision;
- evidence provenance and the conditions under which evidence was collected;
- confidence attached to a claim, version, hardware revision, build, load, environment, instrumentation, and exposure;
- evidence transfer across prototypes, production builds, product variants, hardware lots, laboratory setups, and field
  conditions;
- evidence freshness and confidence decay when assumptions change;
- weak signals, counter-evidence, absence of failure, and observability limits;
- proportional revalidation targeted at a changed assumption;
- ownership of the claim, evidence record, current confidence, and review trigger;
- decision quality versus outcome quality;
- Part II closure: the laws require evidence to remain useful after the review meeting ends.

### Explicitly Out of Scope

Do not turn Chapter 13 into:

- a duplicate of Chapter 5;
- a statistics textbook;
- a general test-strategy handbook;
- a formal verification tutorial;
- a timing architecture chapter;
- a benchmarking guide;
- a release-gating playbook;
- an observability implementation chapter;
- a complete Architecture Review procedure;
- an ADR or Decision Journal mechanics tutorial;
- a postmortem chapter;
- a philosophical essay about certainty;
- a Part II summary chapter with no new contribution;
- a Part III playbook written too early.

## 8. Claim, Evidence, Confidence, and Commitment

The future draft should use the Chapter 5 premise briefly: data becomes evidence only in relation to a claim. Chapter 13
should not reteach the full framework. It should apply the premise to architecture over time:

- Which claim is still active?
- Which evidence still supports it?
- Which version and conditions did that evidence cover?
- Did the system change enough to narrow or invalidate the inference?
- What confidence is sufficient for the next commitment?
- Who owns revalidation?

Confidence should remain weaker than or equal to what the current evidence supports. Commitment may still proceed under
uncertainty when exposure, reversibility, detectability, and consequence are bounded.

## 9. Evidence Provenance and Scope

Evidence provenance means enough context to know where evidence came from, when it was collected, which version produced
it, which conditions were present, which measurement path was used, what could not be observed, and whether the result
can be reproduced.

The future draft should attach confidence to:

- exact architecture claim;
- software version;
- hardware revision;
- component or vendor version;
- build configuration;
- tool chain;
- operating environment;
- load and timing conditions;
- observed states and boundaries;
- instrumentation and measurement path;
- product exposure;
- failure-detection capability.

This must not become a data-governance chapter. The point is architecture judgment, not record administration.

## 10. Evidence Transfer Across Versions and Conditions

Evidence from one context may support a later claim only when the similarity argument is explicit.

The future draft should cover transfer from:

- prototype to production;
- one board revision to another;
- one hardware lot to another;
- one compiler configuration to another;
- one product variant to another;
- laboratory to field;
- simulation to hardware;
- unit test to system behavior;
- staged rollout to broad deployment.

Evidence transfer is neither automatic nor forbidden. The chapter should teach the reader to ask what matters to the
claim and what changed enough to require renewed evidence.

## 11. Evidence Freshness, Aging, and Revalidation

Evidence can age out when:

- code changes;
- compiler or optimization settings change;
- RTOS workload changes;
- hardware revision changes;
- component tolerance changes;
- dependency or vendor version changes;
- configuration changes;
- product variant changes;
- load changes;
- timing changes;
- environment changes;
- failure detection changes;
- operational use expands;
- old assumptions become hidden.

The chapter must not imply every change invalidates all evidence. Revalidation should be proportional to the material
change and the consequence of being wrong. The smallest useful evidence action should target the disputed assumption.

## 12. Weak Signals and Counter-evidence

Weak signals are early, low-confidence signs that a system decision may be aging badly. They do not prove a cause. They
can still lower confidence in a broad claim.

Counter-evidence is an observation that lowers confidence or supports an alternative explanation.

The future draft should treat examples such as:

- rare timeout reports;
- retries increasing in one product variant;
- a workaround added by another team;
- one board revision showing different latency;
- field reports outside the tested envelope;
- a regression after a compiler or dependency change;
- evidence that instrumentation changed behavior;
- inconsistent results across environments;
- an unexpected recovery path.

Do not require adversarial proof for every local decision. Do require confidence to respond when evidence changes.

## 13. Absence of Failure and Observability Limits

"No failures reported" may mean:

- failure did not occur;
- exposure was too low;
- instrumentation could not see it;
- users did not report it;
- logs were lost;
- the system recovered silently;
- classification was wrong;
- the affected version was rare.

The chapter should not become a full observability chapter. It should show that operational evidence matters only when
the system can observe the relevant failure, preserve useful context, and connect observations to versions and
conditions.

## 14. Confidence Ownership and Review Triggers

The future draft should clarify who owns:

- the active claim;
- the evidence record;
- current confidence;
- residual uncertainty;
- revalidation;
- review triggers;
- response to weak signals and counter-evidence.

Review triggers should be conditions, not merely dates. Valid triggers include architecture change, hardware revision,
tool chain change, new product variant, increased exposure, changed load, changed environment, new failure mode, recurring
weak signal, observability change, dependency upgrade, expiry of a support assumption, or inability to reproduce old
evidence.

Do not reteach Chapter 4 ownership or Chapter 7 state ownership. Use ownership only to keep confidence reviewable.

## 15. Decision Quality and Outcome Quality

A good outcome does not prove that the original reasoning was sound. A bad outcome does not automatically prove the
decision was negligent.

Chapter 13 should explain why architecture must preserve reasoning and evidence available at decision time. The team may
make a responsible bounded commitment under uncertainty. The team may also get lucky after unsupported confidence. The
future manuscript should distinguish those cases without becoming a postmortem chapter.

## 16. Part II Capstone Role

Chapter 13 closes Part II by showing that the laws are not self-validating.

The chapter should connect the preceding laws through evidence questions:

- What evidence shows state ownership is authoritative in the current system?
- What evidence shows API promises are observed across versions and failure paths?
- What evidence supports dependency behavior, lifecycle, failure modes, and replacement cost?
- What evidence supports timing margins, reset behavior, ordering, and timeout semantics?
- What evidence shows retained flexibility is justified and owned?
- What evidence shows simplification improved change safety rather than hiding distinctions?

This must not become a chapter-by-chapter summary. The point is that each law creates claims that need current evidence.

## 17. Boundaries With Chapters 1-12

### Chapters 1-4 - Principal Engineering Foundations

Chapter 13 may rely on role responsibility, constrained commitments, better questions, and ownership. It must not repeat
the general Principal Engineer role, the Chapter 2 commitment framework, the Chapter 3 inquiry framework, or Chapter 4
closure ownership.

### Chapter 5 - Technical Judgment and Evidence

Chapter 5 owns forming evidence-bounded judgment for a current commitment. Chapter 13 owns the lifecycle of confidence
after the architecture claim has been carried forward into later versions, variants, and operating conditions.

### Chapter 6 - Leaving Systems Better Than You Found Them

Chapter 6 owns stewardship and incremental improvement. Chapter 13 may show that confidence records are a way to avoid
leaving folklore, but it must not reteach the full stewardship argument.

### Chapter 7 - Every State Has One Owner

Chapter 7 owns state authority. Chapter 13 may ask what evidence proves the current owner still controls meaningful
transitions, but it must not reteach state ownership.

### Chapter 8 - Every API Is a Promise

Chapter 8 owns observable contracts. Chapter 13 may ask what evidence shows the promise still holds across versions and
failure paths, but it must not reteach API promise semantics.

### Chapter 9 - Every Dependency Is a Decision

Chapter 9 owns dependency commitments and replacement cost. Chapter 13 may ask whether dependency evidence still
transfers after upgrades or vendor changes, but it must not repeat dependency selection.

### Chapter 10 - Time Is a Dependency

Chapter 10 owns temporal semantics. Chapter 13 may use a timing-margin story because `LAW-005` itself names that typical
violation, but the subject is evidence lifecycle, not timer design.

### Chapter 11 - Unused Flexibility Is Waste

Chapter 11 owns unused options, unjustified flexibility, and evidence for retained options. Chapter 13 owns evidence
quality, freshness, transfer, confidence, and revalidation for active architecture claims.

### Chapter 12 - Simplicity Is a Feature

Chapter 12 owns simplicity as safe future change. Chapter 13 may ask what evidence supports simplicity claims, but it
must not reteach simple versus easy, product decision paths, or simplification tactics.

## 18. Boundaries With Later Parts

Part III should retain full boundary-drawing, change-radius management, failure and recovery design, ADR/RFC practice,
Architecture Review, and Architecture Freeze playbooks.

Part IV should retain product configuration, manufacturing, observability implementation, release discipline, upgrade
paths, and the reference project.

Part V should retain organizational rituals, mentoring, alignment, and Architecture Health Review operation.

Part VI should retain legacy recovery, utility-gravity reduction, Boolean Explosion reduction, and broad refactoring
programs.

Chapter 13 may point toward these practices as the places where evidence becomes durable, but it must not teach the
playbooks.

## 19. Recommended Embedded-Systems Story

### Working Title

The Timing Margin That Aged Out

### System

Use an embedded communications or control product that depends on a command-response timing margin.

The original team measured the path on one prototype board, one hardware revision, one component lot, room temperature,
stable supply, one firmware build, one traffic pattern, debug instrumentation, and a limited number of runs. The measured
result showed comfortable margin, and the decision was reasonable for the tested conditions.

### Architecture Evolution

Over releases, the system changed:

- compiler or optimization settings changed;
- an RTOS workload grew;
- diagnostic logging was added;
- another interrupt source appeared;
- hardware revision or component tolerance changed;
- radio or peripheral firmware changed;
- product load expanded;
- power-management behavior changed;
- failure diagnostics changed.

The old timing claim survived in memory or an ADR. The evidence conditions became invisible.

### Trigger

Weak signals appear:

- rare timeout reports;
- retries increasing in one product variant;
- failures only under low temperature or high load;
- one board revision showing different latency;
- a support note that cannot reproduce the issue;
- an intermittent lab failure dismissed as noise.

No single signal proves the root cause. Together they should lower confidence in the old margin claim.

### Tempting But Inadequate Response

The team proposes:

- increase the timeout;
- rerun the original test once;
- cite years without a major incident;
- trust the original senior engineer;
- add retries;
- classify reports as environmental;
- keep the old ADR because no replacement design exists;
- run a long test without targeting the disputed boundary;
- demand proof of failure before reopening the decision.

Those responses defend confidence without examining whether the supporting evidence still transfers.

### Principal Engineer Intervention

The Principal Engineer recasts the issue from:

> Is the old design proven wrong?

to:

> Which current architecture claim are we relying on, what evidence still supports it, and what changed since that
> evidence was collected?

The solution should:

- state the exact timing claim;
- identify products and versions relying on it;
- recover evidence provenance;
- compare original and current conditions;
- classify material changes;
- preserve valid evidence;
- identify weak signals and counter-evidence;
- define the smallest targeted revalidation;
- use production-equivalent configurations;
- improve measurement where the system is blind;
- bound exposure until confidence supports the broader claim;
- record current confidence and residual uncertainty;
- assign revalidation ownership;
- define review triggers.

The story must not become a timer tutorial, a repeat of Chapter 10, a statistics chapter, an exhaustive test plan, or a
guarantee of certainty.

## 20. Expected Discussion Arc

1. The original decision may have been responsible.
2. Confidence outlived the conditions that created it.
3. Architecture claims remain active after reviews end.
4. Evidence belongs to a claim, version, and operating envelope.
5. Change can narrow or invalidate evidence transfer.
6. A good outcome does not retroactively improve weak reasoning.
7. Weak signals can lower confidence without proving a cause.
8. Revalidation should target the changed assumption, not repeat every test.
9. Operational evidence matters only when failures are observable.
10. Confidence must be owned, reviewable, and revisable.
11. Part II laws require evidence, not ceremonial compliance.
12. Part III provides practices for making those decisions durable.

Do not mechanically create twelve top-level headings in the manuscript.

## 21. Law Applicability

`LAW-005` applies when a team relies on a claim whose evidence may be incomplete, stale, narrow, unobservable, or
transferred from one context to another.

It is especially relevant when:

- the decision affects many components or teams;
- the result is difficult to reverse;
- failure is hard to detect;
- product exposure is broadening;
- hardware, software, environment, or load changed;
- old tests are being cited after architecture changed;
- the supporting evidence is remembered but not traceable;
- weak signals are recurring;
- the next commitment depends on confidence in a previous decision.

The law does not require impossible proof before every action. It requires confidence to remain bounded by evidence.

## 22. Law Limits and Exceptions

The future draft must avoid dogmatism. It should not claim:

- every architectural claim must be formally proven;
- confidence is bad;
- expert judgment has no value;
- tests are the only evidence;
- field data is always stronger than lab data;
- more data always means stronger evidence;
- repeated results are independent evidence;
- no failures reported proves reliability;
- every code change invalidates all prior evidence;
- old evidence is useless;
- all evidence needs a fixed expiry date;
- weak signals prove defects;
- a Decision Journal makes a decision correct;
- an ADR is an evidence repository;
- staged rollout substitutes for validation;
- instrumentation is neutral;
- a successful outcome proves a good decision;
- a failed outcome proves a negligent decision;
- certainty is required before commitment;
- quantitative confidence percentages are always useful;
- architecture reviews produce truth by consensus.

The law is satisfied when confidence is traceable, bounded, current enough for the commitment, and responsive to changed
conditions.

## 23. Violation Patterns

The future draft should make these violations visible:

- an old benchmark cited after the system changed;
- one prototype result treated as a product property;
- a debug build used to justify release timing;
- a lab test transferred to field conditions without argument;
- an ADR that records a decision but not its evidence limits;
- a test count cited without the claim it supports;
- "no customer complaints" used despite weak observability;
- repeated results from one path treated as independent confirmation;
- a senior engineer's memory replacing evidence provenance;
- weak signals dismissed because they do not prove a cause;
- confidence remaining unchanged after counter-evidence;
- evidence copied across product variants;
- a hardware revision inheriting old margins without revalidation;
- a dependency upgrade accepted under old compatibility evidence;
- a successful rollout retroactively described as proof;
- revalidation repeating easy tests instead of targeting the changed assumption;
- evidence ownership disappearing after the original decision owner leaves.

## 24. Engineering Principle Target

Target principle for the future draft:

> Keep architecture confidence attached to a specific claim, evidence envelope, and review trigger. When the system or
> conditions change, revalidate the assumption before carrying the confidence forward.

The principle should imply review questions:

1. What exact architecture claim are we relying on?
2. What evidence supports it now?
3. Which version, hardware, build, load, and environment did that evidence cover?
4. What changed since it was collected?
5. Why should the evidence transfer?
6. What can the measurement not observe?
7. What would lower our confidence?
8. Which weak signals exist?
9. Who owns revalidation?
10. What is the smallest evidence action that targets the changed assumption?
11. What confidence is sufficient for the next commitment?
12. What trigger will reopen the decision?

The final manuscript may shorten the list for reader rhythm.

## 25. Architecture Exercise Target

### Working Title

Revalidate One Architecture Claim

Ask the reader to choose one active architecture claim and document:

1. exact claim;
2. products, versions, and variants relying on it;
3. original decision and artifact;
4. original evidence;
5. original evidence conditions;
6. current evidence;
7. changes since collection;
8. assumptions required for evidence transfer;
9. evidence that remains valid;
10. evidence that no longer transfers;
11. blind spots;
12. weak signals;
13. counter-evidence;
14. current confidence and scope;
15. consequence if wrong;
16. reversibility;
17. detectability;
18. smallest targeted revalidation;
19. owner;
20. review trigger;
21. ADR, Decision Journal, or Weak Signal Register update required.

End with one of these decisions:

- confidence remains justified;
- confidence narrows;
- revalidation is required;
- commitment must be bounded;
- architecture decision must reopen;
- observability must improve before confidence can rise.

Do not create a new canonical artifact such as Evidence Ledger, Confidence Register, Evidence Envelope, Confidence Map,
Validation Passport, or Architecture Proof Record.

## 26. Chapter-Local ADR Brief

### Working Title

Revalidate the Communication Timing Margin Before Broadening Product Exposure

### Context

- An original timing margin was measured on a prototype.
- The original result was valid for its tested conditions.
- Software, hardware, load, or tool chain conditions changed.
- Current products still rely on the margin.
- Evidence provenance is incomplete.
- Weak signals exist but do not prove one cause.
- Current observability cannot see all deadline misses or recovery behavior.

### Decision

- Define the exact current timing claim.
- Identify products and versions relying on it.
- Preserve valid original evidence.
- Compare original and current evidence conditions.
- Run targeted production-equivalent measurements around the disputed boundary.
- Include relevant hardware, load, voltage, and temperature variation only where material.
- Add the minimum diagnostics required to observe misses.
- Bound exposure until evidence supports the broader claim.
- Record current confidence and residual uncertainty.
- Assign revalidation ownership.
- Define review triggers for material changes.

### Alternatives Considered

- Retain confidence because the product has mostly worked.
- Increase the timeout.
- Add retries.
- Repeat the original bench test.
- Demand proof of field failure.
- Redesign immediately without revalidation.
- Run an exhaustive qualification program.
- Ignore weak signals until they become reproducible.
- Keep the old ADR unchanged.

The ADR should explain why these alternatives are not selected for this system without claiming they can never be valid
elsewhere.

### Consequences

Benefits:

- current confidence becomes traceable;
- valid historical evidence is preserved;
- changed assumptions receive targeted testing;
- exposure remains proportionate;
- weak signals become actionable without being overstated;
- future changes gain explicit triggers.

Costs:

- measurement and instrumentation work;
- temporary release or exposure constraints;
- uncertainty remains;
- some original evidence may be difficult to reproduce;
- additional ownership and record maintenance;
- possible redesign if the margin is not supported.

The ADR must make a real scoped decision. It must not reduce to "test more."

## 27. PEAK Concept Map

### Concepts Inspected

- `LAW-005` - Evidence Before Confidence.
- `LAW-001` - Every State Has One Owner.
- `LAW-002` - Every API Is a Promise.
- `LAW-003` - Time Is a Dependency.
- `LAW-004` - Simplicity Is a Feature.
- `LAW-006` - Unused Flexibility Is Waste.
- `LAW-007` - Every Dependency Is a Decision.
- `VOCAB-001` - Change Radius.
- `VOCAB-002` - Weak Signal.
- `VOCAB-003` - Decision Journal.
- `VOCAB-007` - Architecture Health.
- `METRIC-001` - Change Radius.
- `METRIC-003` - Discoverability.
- `METRIC-005` - Architecture Health.
- `ARTIFACT-001` - ADR.
- `ARTIFACT-003` - Decision Journal.
- `ARTIFACT-006` - Architecture Ledger.
- `ARTIFACT-007` - Weak Signal Register.
- `RITUAL-001` - Architecture Review.
- `RITUAL-004` - Architecture Health Review.
- `FAILURE-003` - The Successful Prototype.
- `FAILURE-005` - The Release We Should Have Delayed.

### Selected Concepts

- `LAW-005` - Evidence Before Confidence: the chapter directly illustrates the final Part II law.
- `VOCAB-002` - Weak Signal: material because the story turns rare timeouts, retries, and inconsistent reports into
  confidence-lowering signals without overstating proof.
- `ARTIFACT-007` - Weak Signal Register: material because weak signals need a place to survive until evidence matures.
- `VOCAB-003` - Decision Journal: material because smaller confidence judgments can record claim, evidence, confidence,
  uncertainty, and review trigger without a full ADR.
- `ARTIFACT-003` - Decision Journal: material because the exercise may update a decision record when confidence narrows
  or revalidation is required.
- `ARTIFACT-001` - ADR: material because the chapter-local ADR records a scoped revalidation and exposure decision.
- `RITUAL-001` - Architecture Review: material because architecture claims should reopen when triggers show the old
  evidence may no longer support current confidence.
- `VOCAB-001` - Change Radius: material because evidence strength should scale with affected system surface and the
  consequence of carrying unsupported confidence.
- `METRIC-001` - Change Radius: material because the exercise asks readers to identify affected products, tests,
  tooling, support, diagnostics, and release surfaces.
- `VOCAB-007` - Architecture Health: material because stale confidence and unowned evidence records are health signals
  for a long-lived architecture.
- `METRIC-005` - Architecture Health: material because current confidence is part of the system's ability to support
  necessary change at acceptable cost.
- `FAILURE-003` - The Successful Prototype: material because the recommended story shows prototype evidence being
  carried beyond its tested conditions.

### Rejected Concepts

- `LAW-001` - Every State Has One Owner: Chapter 13 may ask for evidence of state ownership, but Chapter 7 owns the law.
- `LAW-002` - Every API Is a Promise: Chapter 13 may ask for evidence of API behavior, but Chapter 8 owns promises.
- `LAW-003` - Time Is a Dependency: the story uses timing, but Chapter 10 owns temporal semantics.
- `LAW-004` - Simplicity Is a Feature: Chapter 13 may ask for evidence that simplification worked, but Chapter 12 owns
  simplicity.
- `LAW-006` - Unused Flexibility Is Waste: Chapter 13 may ask for evidence that retained options remain justified, but
  Chapter 11 owns flexibility.
- `LAW-007` - Every Dependency Is a Decision: Chapter 13 may ask whether dependency evidence transfers after upgrades,
  but Chapter 9 owns dependency commitment.
- `METRIC-003` - Discoverability: provenance and records improve discoverability, but selected artifacts carry the
  chapter's record-keeping need more directly.
- `ARTIFACT-006` - Architecture Ledger: useful for large systems, but not required for the chapter's central claim.
- `RITUAL-004` - Architecture Health Review: relevant to future practice, but the chapter should not teach the full
  health-review ritual.
- `FAILURE-005` - The Release We Should Have Delayed: relevant to release pressure, but the selected story is about
  confidence transfer from a successful prototype rather than release readiness.

### New PEAK Concept Decision

No new PEAK law, maxim, artifact, ritual, metric, smell, anti-pattern, failure story, or vocabulary concept is required.
Terms such as evidence envelope, confidence expiry, evidence decay, confidence boundary, revalidation debt, evidence
owner, and validation passport remain chapter-local prose unless a later Canon Review finds a stable reusable gap.

## 28. Exact Proposed PEAK Relationships

Register `CHAPTER-013` as a `draft` chapter and add exactly these outgoing relationships during brief registration:

```yaml
- from: CHAPTER-013
  type: illustrates
  to: LAW-005

- from: CHAPTER-013
  type: illustrates
  to: FAILURE-003

- from: CHAPTER-013
  type: references
  to: VOCAB-002

- from: CHAPTER-013
  type: references
  to: ARTIFACT-007

- from: CHAPTER-013
  type: references
  to: VOCAB-003

- from: CHAPTER-013
  type: references
  to: ARTIFACT-003

- from: CHAPTER-013
  type: references
  to: ARTIFACT-001

- from: CHAPTER-013
  type: references
  to: RITUAL-001

- from: CHAPTER-013
  type: references
  to: VOCAB-001

- from: CHAPTER-013
  type: references
  to: METRIC-001

- from: CHAPTER-013
  type: references
  to: VOCAB-007

- from: CHAPTER-013
  type: references
  to: METRIC-005
```

Canon Review should remove any edge whose concept is not materially present in the final manuscript. Do not add broad
`related_to` edges.

## 29. Required Chapter Architecture

The eventual manuscript must use the required chapter sequence from `editor/CHAPTER_ARCHITECTURE.md`:

1. Opening Quote
2. Story
3. Discussion
4. Engineering Principle
5. Architecture Exercise
6. Principal's Notebook
7. ADR
8. Editor's Commentary

Each section should serve the Chapter 13 role:

- Opening Quote: establish that confidence needs a current evidence basis.
- Story: show a timing margin whose original evidence was reasonable but no longer transfers cleanly.
- Discussion: explain evidence provenance, transfer, weak signals, revalidation, and ownership without repeating Chapter
  5.
- Engineering Principle: anchor the law as current, conditional confidence.
- Architecture Exercise: revalidate one active architecture claim.
- Principal's Notebook: three short observations, no explanations.
- ADR: record the scoped timing-margin revalidation and exposure decision.
- Editor's Commentary: explain the Chapter 5 distinction, close Part II, and point toward Part III practices without
  teaching them.

## 30. Principal's Notebook Shape

The future notebook should contain exactly three short observations. Candidate semantic targets:

- Confidence expires when its conditions change.
- A successful outcome does not repair weak reasoning.
- Weak signals lower confidence before they prove a cause.

These are semantic targets, not mandatory final wording. Do not reuse Chapter 5's exact notebook observations.

## 31. Evidence and Technical Credibility Requirements

The future draft must be credible for embedded and long-lived systems. It should treat the following correctly:

- timing measurements;
- hardware and software version context;
- compiler and build differences;
- RTOS workload and interrupt effects;
- hardware revision and component tolerance;
- temperature, voltage, and load;
- measurement instrumentation effects;
- weak signals;
- timeout and retry observations;
- production-equivalent configuration;
- evidence transfer;
- targeted revalidation;
- observability blind spots;
- staged or bounded exposure;
- counter-evidence;
- current confidence versus historical confidence.

The story should remain architecture-neutral unless a small illustrative detail is necessary. Do not require a specific
MCU, RTOS, bus, radio, timer width, synchronization protocol, test framework, statistical method, or vendor.

## 32. Terminology and Precision Guardrails

Use these terms precisely:

- claim: a statement the architecture relies on;
- evidence: an observation or result relevant to that claim;
- confidence: current degree of belief justified by available evidence;
- evidence provenance: origin, version, conditions, and measurement path of evidence;
- evidence transfer: reason evidence collected in one context supports a claim in another;
- revalidation: targeted evidence gathering after material assumptions or conditions change;
- weak signal: an early low-confidence observation that should affect investigation or confidence without being treated
  as proof;
- counter-evidence: observation that lowers confidence or supports an alternative explanation;
- review trigger: a condition that requires the judgment to be reopened;
- residual uncertainty: what remains unknown after the current evidence.

The chapter must avoid these misleading statements:

- "One timing capture establishes worst case."
- "A long test proves all state boundaries."
- "Debug instrumentation is behavior-neutral."
- "Passing at room temperature proves tolerance coverage."
- "Higher timeout always increases safety."
- "Retries validate timing assumptions."
- "No logs means no failure."
- "Production behavior transfers from a prototype automatically."
- "All old evidence becomes invalid after any change."
- "Field reports are independent by default."
- "Targeted revalidation guarantees correctness."
- "A confidence percentage is objective because it is numeric."

## 33. Failure Modes to Avoid

The later draft must not become:

- a duplicate of Chapter 5;
- a statistics textbook;
- a test-strategy handbook;
- a formal verification tutorial;
- a timing chapter;
- a benchmarking guide;
- a release-gating playbook;
- an observability implementation chapter;
- an Architecture Review procedure;
- an ADR mechanics tutorial;
- a postmortem chapter;
- a philosophical essay about certainty;
- an argument that evidence eliminates judgment;
- an argument that experts cannot use intuition;
- an argument that every decision requires exhaustive proof;
- a Part II summary chapter with no new contribution;
- a Part III playbook written too early;
- a new PEAK artifact proposal;
- reader-facing draft prose inside the canonical brief.

## 34. Author Draft Acceptance Criteria

Author Draft acceptance criteria:

- the standard chapter architecture is complete and ordered correctly;
- the opening story contains a concrete embedded timing-margin confidence failure;
- the original decision is treated as possibly responsible for its tested conditions;
- the Principal Engineer move recasts the work around current claim, current evidence, changed conditions, and
  revalidation;
- `LAW-005` is explained beyond the slogan without duplicating Chapter 5;
- Chapter 5's flash-logging story, exercise, ADR, discussion arc, and notebook observations are not reused;
- claim, evidence, confidence, commitment, provenance, transfer, revalidation, weak signal, counter-evidence, review
  trigger, and residual uncertainty are used precisely;
- absence of failure is handled with observability limits;
- evidence freshness and proportional revalidation are treated without dogmatism;
- decision quality and outcome quality are distinguished;
- Part II laws are synthesized through evidence questions rather than summarized one by one;
- Part III is previewed as the place where practices make decisions durable, without teaching those playbooks;
- `LAW-005`, Weak Signal, Decision Journal, Weak Signal Register, ADR, Architecture Review, Change Radius, Architecture
  Health, and The Successful Prototype are materially present if their relationships remain registered;
- the exercise ends in a decision about confidence, revalidation, bounded commitment, reopening, or observability;
- the ADR makes a genuine scoped decision and acknowledges benefits and costs;
- exactly three Principal's Notebook observations are present;
- all referenced PEAK concepts already exist;
- no new canonical concept is implied accidentally.

## 35. Review Handoff Notes

Editorial Review should check whether the story, discussion, principle, exercise, notebook, ADR, and commentary teach one
idea without drifting into a duplicate of Chapter 5, a timing tutorial, a release-gate chapter, or a generic evidence
essay.

Canon Review should verify that the chapter illustrates `LAW-005`, materially uses the registered supporting concepts,
does not imply a new PEAK artifact or vocabulary term, preserves the boundary with Chapter 5, and closes Part II without
becoming a summary chapter.

Technical Review should focus on timing measurement credibility, hardware and software version context, build and
instrumentation effects, interrupt/load variation, temperature/voltage considerations, timeout and retry interpretation,
evidence transfer, observability blind spots, targeted revalidation, and bounded exposure.

Freeze Review should confirm that Chapter 13 remains the final Part II law chapter, keeps the manuscript architecture
intact, uses exactly three Principal's Notebook observations, preserves the registered PEAK graph, and leaves the
reader-facing manuscript in canonical-ready shape.

No blocking author decision is required before brief registration. During Author Draft, the author may adjust the exact
communication subsystem, timing path, weak signals, product variants, and final notebook wording while preserving the
evidence-lifecycle thesis, story shape, PEAK map, and chapter boundaries.

## 36. Final Scope Statement

Chapter 13 should define architecture confidence as a current, conditional belief tied to a specific claim and evidence
that still transfers to the product, version, and operating conditions being relied on. It should show an embedded timing
margin whose original evidence was reasonable but aged out as the system changed, then guide the reader toward evidence
provenance, weak signals, counter-evidence, proportional revalidation, owned review triggers, and existing artifacts that
keep confidence reviewable as Part II hands off to Part III.
