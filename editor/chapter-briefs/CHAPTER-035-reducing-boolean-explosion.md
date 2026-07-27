# CHAPTER-035 Canonical Brief: Reducing Boolean Explosion

## 1. Metadata

- Stable ID: `CHAPTER-035`.
- Title: `Reducing Boolean Explosion`.
- Part: Part VI - Legacy.
- Chapter number: 35.
- Expected manuscript path: `book/06-legacy/35-reducing-boolean-explosion.md`.
- Expected canonical brief path:
  `editor/chapter-briefs/CHAPTER-035-reducing-boolean-explosion.md`.
- Branch: `chapter35`.
- Verified baseline `origin/main`: `487507ebbd12fce8fde8f36633f9a21d5f40f4c8`.
- Baseline evidence: PR #36 Chapter 34 squash merge commit,
  `Chapter 34: Managing Utility Gravity (#36)`.
- Canonical predecessor: `CHAPTER-034` - Managing Utility Gravity.
- Part position: fourth chapter of Part VI - Legacy.
- Reader-facing draft created: no.
- Expected lifecycle status after registration: `draft`.
- Primary concept: none. Chapter 35 illustrates the existing `SMELL-003` Boolean Explosion smell and references the
  existing `VOCAB-010` Boolean Explosion vocabulary term; it must not add a `primary_concept` registry field.
- Central illustrated concept: `SMELL-003` - Boolean Explosion.
- Central vocabulary term: `VOCAB-010` - Boolean Explosion.
- Central chapter-local practice: mapping product states, valid combinations, owners, evidence, and review triggers
  before adding, removing, or refactoring flags and modes.
- Lifecycle status at brief-registration time: draft preparation.
- Preparation status: canonical brief registered.
- Next lifecycle stage: Author Draft after author approval.

## 2. Repository-Grounded Findings

- `origin/main` resolves to `487507ebbd12fce8fde8f36633f9a21d5f40f4c8`.
- That baseline is the PR #36 Chapter 34 squash merge commit,
  `Chapter 34: Managing Utility Gravity (#36)`.
- The baseline contains the Chapter 34 manuscript, canonical brief, editor log, and index updates.
- `CHAPTER-034` is registered as `canonical` in `knowledge/index.yaml`.
- Chapter 34 Freeze Review is recorded in `editor/EDITOR_LOG.md` with Frozen lifecycle status.
- `CHAPTER-001` through `CHAPTER-034` are registered as `canonical` in `knowledge/index.yaml`.
- `CHAPTER-035` was absent from `knowledge/index.yaml` before this registration.
- No Chapter 35 canonical brief or reader-facing manuscript existed before this registration.
- No Chapter 36 or Chapter 37 manuscript existed before this registration.
- The Part VI table of contents order is Reading a Legacy System, Finding Silent Coupling, Managing Utility Gravity,
  Reducing Boolean Explosion, Deleting Safely, and Refactoring Without Losing Product Trust.
- No tracked `site/` output existed before this registration.
- The PEAK graph already contains `SMELL-003` Boolean Explosion and `VOCAB-010` Boolean Explosion, so no new concept
  is required.

## 3. Part VI Role

Chapter 35 follows the first three Legacy chapters. Chapter 32 taught the reader to build a reading map before changing
a legacy system. Chapter 33 taught the reader to find hidden behavioral dependencies that make local changes non-local.
Chapter 34 taught the reader to manage shared utilities that have accumulated product responsibility. Chapter 35 narrows
the reader's attention to another common legacy force: uncontrolled combinations of flags, booleans, configuration
switches, compile-time options, compatibility toggles, product variants, customer exceptions, and mode bits.

The chapter should prepare the reader for later Legacy work without teaching it early. Chapter 36 owns deletion safety.
Chapter 37 owns trust-preserving refactoring. Chapter 35 should make the switch state space visible, named, owned,
tested, and recorded before the team decides whether to delete, migrate, or broadly refactor behavior.

## 4. Canonical Purpose

Prepare Chapter 35 to teach that Boolean Explosion is reduced by making the product state space explicit before changing
behavior. The chapter is not about tidying conditional code. It is about recovering control over combinations the team
can no longer reason about, test, own, document, or support.

Candidate thesis for the future manuscript:

> A Boolean is cheap to add but expensive to combine.

The chapter should move the reader away from asking:

> Can we add one more flag?

to asking:

> What product states, promises, owners, constraints, evidence, and review paths does this new combination create?

## 5. Primary-Concept Resolution

Chapter 35 has no new primary PEAK concept at canonical-brief registration time.

Current repository convention does not add a primary-concept registry field to chapter records. The graph already
contains `SMELL-003` Boolean Explosion and `VOCAB-010` Boolean Explosion. Chapter 35 should illustrate the existing
smell and use the existing vocabulary term while referencing the laws, metrics, artifacts, rituals, smells,
anti-patterns, and failure stories needed to manage combinatorial product behavior responsibly.

Boolean state map, compatibility matrix, decision table, named mode boundary, flag inventory, combination budget,
state-space map, policy-bearing flag, mechanism switch, and compatibility promise remain chapter-local prose. Do not
create a new PEAK concept, ID, artifact, ritual, metric, vocabulary term, smell, anti-pattern, failure story,
primary-concept field, or relationship verb for them.

## 6. Central Thesis

Boolean Explosion happens when small local switches multiply into product behavior combinations that exceed the team's
ability to reason, test, own, document, and support them. In a legacy system, the responsible response is not immediate
cleanup, deletion, or a broad refactor. The responsible response is to name the real product states, classify valid and
invalid combinations, assign ownership, gather evidence, and create review triggers before behavior changes.

Approved supporting formulation for the future draft:

> Reduce the state space before changing behavior.

This formulation is chapter-level language. Do not register it as a PEAK law, maxim, principle, artifact, ritual,
metric, smell, anti-pattern, failure story, or vocabulary concept.

## 7. Reader Transformation

Before the chapter, the reader may think:

1. adding one switch is a small change because the diff is small;
2. Boolean Explosion means too many `if` statements;
3. flags, modes, product variants, and compatibility switches are local implementation details;
4. each customer exception can be handled as a special case;
5. unsupported combinations are obvious from code;
6. compile-time options and runtime flags are separate enough to reason about independently;
7. tests for the happy path prove the flag is safe;
8. the flag owner is whoever wrote the last conditional;
9. deletion or named-mode replacement should start as soon as the code looks messy;
10. legacy compatibility requires preserving every old combination forever.

By the end of the chapter, the reader should be able to:

1. recognize Boolean Explosion as uncontrolled product state growth rather than conditional style;
2. inventory booleans, flags, modes, compile-time options, customer exceptions, and compatibility toggles;
3. separate mechanism switches from product policy decisions;
4. name real product states hidden behind combinations;
5. identify valid, invalid, unsupported, obsolete, temporary, and unknown combinations;
6. assign owners for the state model and policy-bearing flags;
7. use characterization, contract, and integration tests around high-risk combinations;
8. record why combinations exist in ADRs, RFCs, Decision Journal entries, or Architecture Ledger rows;
9. create review triggers for new flags, modes, compatibility exceptions, and temporary paths;
10. defer deletion or broad refactoring until active combinations and promises are visible.

## 8. Boolean Explosion Scope

For Chapter 35, Boolean Explosion means the growth of product behavior combinations beyond what the team can reason
about, test, own, document, and support.

The future manuscript may examine:

- feature flags that combine into untested product variants;
- compatibility toggles that preserve old behavior without naming the promise;
- compile-time options that create firmware families with different field behavior;
- service-tool workflows that interpret the same device state differently from firmware;
- backend interpretations that drift from embedded mode bits;
- manufacturing scripts that depend on undocumented configuration combinations;
- support procedures that rely on local exceptions and tribal memory;
- release validation matrices that no longer cover active combinations;
- customer exceptions that survive after the original contract or migration window is gone;
- temporary flags that become permanent product modes.

The chapter should help the reader reduce and govern the state space. It should not treat every flag as bad or every
conditional as a design failure.

## 9. Managing Order and Evidence

The future manuscript should teach a managing order that starts with the product state space rather than the desired
cleanup.

Useful finding layers:

1. Which booleans, flags, modes, compile-time options, customer exceptions, and compatibility toggles exist?
2. Which combinations are active in firmware, backend systems, service tools, manufacturing, support, and release paths?
3. Which combinations represent real product states, operating modes, or contractual promises?
4. Which combinations are valid, invalid, unsupported, obsolete, temporary, or unknown?
5. Which switches are mechanism controls and which ones carry product policy?
6. Who owns the state model, each policy-bearing flag, and each compatibility promise?
7. Which combinations have characterization tests, contract tests, integration tests, release evidence, or field data?
8. Which combinations need an ADR, RFC, Decision Journal entry, Architecture Ledger row, Architecture Review, or
   Architecture Health Review?
9. Which combinations should be protected for now, constrained, migrated, deleted later, or refactored later?
10. Which review trigger prevents the next flag from multiplying the hidden state space again?

Do not turn this into a rigid checklist. The order should change the reader's attention from local switch addition to
owned product-state management.

## 10. In-Scope and Out-of-Scope

### In Scope

Chapter 35 covers:

- Boolean Explosion as uncontrolled product behavior combinations;
- flags, booleans, configuration switches, compile-time options, compatibility toggles, product variants, customer
  exceptions, and mode bits;
- embedded and product-system combinations that cross firmware, backend services, service tools, manufacturing,
  support, field upgrades, and release validation;
- product state naming, valid-combination classification, ownership, evidence, and review triggers;
- mechanism switches versus product policy decisions;
- compatibility matrices, decision tables, explicit state models, and named mode boundaries where they reduce risk;
- characterization tests before behavior change;
- contract and integration tests for combinations crossing teams or release paths;
- ADRs, RFCs, Decision Journal entries, and Architecture Ledger rows that record why combinations exist;
- Architecture Review and Architecture Health Review as places to inspect state-space growth;
- Change Radius, Bus Factor, Discoverability, and API Stability as evidence lenses for flag risk.

### Explicitly Out of Scope

Do not turn Chapter 35 into:

- a code-style chapter about replacing switches with named modes;
- a generic feature-flag management chapter;
- a state-machine tutorial;
- a testing-only chapter;
- a product-management rollout chapter;
- a safe-deletion chapter;
- a broad refactoring chapter;
- a rewrite argument;
- a chapter about making every combination configurable;
- an argument for preserving all old behavior forever;
- a Utility Gravity chapter;
- a Silent Coupling chapter;
- a new PEAK concept proposal.

## 11. Recommended Legacy-System Story

Use a story close to:

`The Two Flags That Became Sixteen Products`

A legacy product begins with two local-looking flags: one for a compatibility mode and one for a customer exception.
Both changes appear safe in isolation. Over several releases, they interact with firmware behavior, service-tool
workflows, backend interpretation, manufacturing scripts, support procedures, field upgrade paths, and release
validation. The team discovers that a small flag change now creates sixteen practical product variants, many of which
no one can name, test, support, or confidently reject.

The Principal Engineer does not start by deleting flags or rewriting the state logic. They inventory the switches, name
the real product states, classify invalid and obsolete combinations, assign owners, add characterization and
cross-boundary tests, record compatibility promises, and create review triggers for future modes. The story should end
with a smaller, visible, owned state space, not a triumphant conditional cleanup.

## 12. Future Manuscript Moves

The future Author Draft should include these moves:

1. inventory booleans, flags, modes, compile-time options, customer exceptions, and compatibility toggles;
2. separate mechanism switches from product policy decisions;
3. name real product states and operating modes hidden behind combinations;
4. identify invalid, unsupported, obsolete, temporary, and unknown combinations;
5. assign owners for the state model and policy-bearing flags;
6. replace scattered checks with an explicit state model, compatibility matrix, decision table, or named mode boundary
   where appropriate;
7. add characterization tests before changing behavior;
8. add contract and integration tests around combinations crossing teams and release paths;
9. record why combinations exist in ADRs, RFCs, Decision Journal entries, or Architecture Ledger rows;
10. create review triggers for new flags, modes, compatibility exceptions, and temporary paths;
11. defer deletion until Chapter 36 evidence;
12. defer broad trust-sensitive refactoring until Chapter 37 migration planning.

## 13. Boundary With Neighboring Chapters

- Chapter 32 owns reading a legacy system before the first change. Chapter 35 may rely on reading maps but should not
  reteach them.
- Chapter 33 owns Silent Coupling. Chapter 35 may show flags crossing hidden dependency lines, but the central problem
  is combinatorial product behavior.
- Chapter 34 owns Utility Gravity. Chapter 35 may show product policy hiding inside utilities, but it must not become a
  shared-helper responsibility chapter.
- Chapter 36 owns Deleting Safely. Chapter 35 may mark obsolete or unsupported combinations as deletion candidates, but
  it must not teach deletion workflow.
- Chapter 37 owns Refactoring Without Losing Product Trust. Chapter 35 may prepare a state model for later migration,
  but it must not teach broad refactoring strategy.

## 14. Required PEAK Relationship Set

Register Chapter 35 with these outgoing relationships:

- `CHAPTER-035 illustrates SMELL-003`
- `CHAPTER-035 references VOCAB-010`
- `CHAPTER-035 references LAW-001`
- `CHAPTER-035 references LAW-002`
- `CHAPTER-035 references LAW-004`
- `CHAPTER-035 references LAW-005`
- `CHAPTER-035 references LAW-006`
- `CHAPTER-035 references LAW-007`
- `CHAPTER-035 references VOCAB-001`
- `CHAPTER-035 references METRIC-001`
- `CHAPTER-035 references METRIC-002`
- `CHAPTER-035 references METRIC-003`
- `CHAPTER-035 references METRIC-004`
- `CHAPTER-035 references ARTIFACT-001`
- `CHAPTER-035 references ARTIFACT-002`
- `CHAPTER-035 references ARTIFACT-003`
- `CHAPTER-035 references ARTIFACT-006`
- `CHAPTER-035 references RITUAL-001`
- `CHAPTER-035 references RITUAL-004`
- `CHAPTER-035 references SMELL-001`
- `CHAPTER-035 references SMELL-004`
- `CHAPTER-035 references SMELL-005`
- `CHAPTER-035 references SMELL-006`
- `CHAPTER-035 references ANTIPATTERN-003`
- `CHAPTER-035 references ANTIPATTERN-006`
- `CHAPTER-035 references FAILURE-004`
- `CHAPTER-035 references FAILURE-005`

## 15. Selected PEAK Concept Rationale

- `SMELL-003` is illustrated because Boolean Explosion is the chapter's central legacy-system smell.
- `VOCAB-010` is referenced because the chapter must use the existing Boolean Explosion vocabulary instead of inventing
  a new term.
- `LAW-001` is relevant because product states and policy-bearing flags need named owners.
- `LAW-002` is relevant because combinations crossing team boundaries require explicit decision records.
- `LAW-004` is relevant because unsupported or forgotten combinations create unstable architecture.
- `LAW-005` is relevant because flags that look internal can become product interfaces.
- `LAW-006` is relevant because invisible combinations create change risk when evidence is weak.
- `LAW-007` is relevant because aging compatibility paths and temporary modes can become structural drag.
- `VOCAB-001` is relevant because the Principal Engineer must reason from system responsibility, not local code style.
- `METRIC-001`, `METRIC-002`, `METRIC-003`, and `METRIC-004` are useful lenses for Change Radius, ownership memory,
  discoverability, and interface promises around combinations.
- `ARTIFACT-001`, `ARTIFACT-002`, `ARTIFACT-003`, and `ARTIFACT-006` are relevant because ADRs, RFCs, Decision Journal
  entries, and Architecture Ledger rows can record state-model decisions and compatibility promises.
- `RITUAL-001` and `RITUAL-004` are relevant because Architecture Review and Architecture Health Review can inspect
  state-space growth before it becomes field risk.
- `SMELL-001`, `SMELL-004`, `SMELL-005`, and `SMELL-006` are relevant related smells when combinations hide ownership,
  state, platform leakage, or global configuration.
- `ANTIPATTERN-003` and `ANTIPATTERN-006` are relevant because local special cases and scattered hardware or mode
  checks can multiply behavior.
- `FAILURE-004` and `FAILURE-005` are relevant because unmanaged combinations can surface as rollout failures and
  product trust failures.

## 16. Rejected and Avoided Concepts

Do not register or center these concepts unless the Author Draft uncovers a stronger, specific reason:

- `SMELL-002` and `VOCAB-009`: Chapter 34 owns Utility Gravity. Chapter 35 may mention utility-hosted flags only as one
  way Boolean Explosion appears.
- `ANTIPATTERN-001`, `ANTIPATTERN-002`, `ANTIPATTERN-004`, and `ANTIPATTERN-005`: these may appear as nearby forces in
  other chapters, but they are not needed for the core Boolean Explosion brief.
- `RITUAL-002`, `RITUAL-003`, `RITUAL-005`, and `RITUAL-006`: Chapter 35 should focus on review triggers and health
  review, not freeze, deletion, incident, or roadmap rituals.
- `ARTIFACT-004`, `ARTIFACT-005`, and `ARTIFACT-007`: operating guides, postmortems, and roadmap records are not the primary
  record shape for this chapter.
- `VOCAB-005`, `VOCAB-006`, `VOCAB-007`, `VOCAB-008`, and `VOCAB-009`: deletion, freeze, change surface, time debt, and
  Utility Gravity belong elsewhere unless used only as boundary language.
- No new PEAK concept, relationship verb, primary-concept field, artifact, ritual, metric, smell, anti-pattern,
  vocabulary term, law, or failure story should be introduced.

## 17. Required Framing Constraints

The future manuscript must preserve these constraints:

- Boolean Explosion is not "too many if statements."
- It is growth of product behavior combinations beyond what the team can reason about, test, own, document, and
  support.
- It is especially dangerous in embedded and product systems because combinations cross firmware, backend systems,
  service tools, manufacturing, support, and field upgrade paths.
- Adding one flag can multiply the product state space.
- The responsible response is not immediate cleanup.
- First name the state space, constraints, owners, evidence, and review path.
- Future simplification becomes safer only after active combinations and promises are visible.

## 18. Engineering Principle Target

The future chapter should include a principle close to:

> Reduce the state space before changing behavior.

The principle should emphasize that a Principal Engineer treats a new switch as a product-state decision when it
combines with existing modes, compatibility promises, release paths, or customer exceptions.

## 19. Exercise Target

Use an exercise close to:

`Map the Boolean State Space`

The exercise should ask the reader to choose a legacy area with several flags or modes and produce:

1. an inventory of switches and where they are read;
2. a table of known valid, invalid, obsolete, temporary, and unknown combinations;
3. a list of real product states hidden behind the combinations;
4. owners for policy-bearing flags and compatibility promises;
5. evidence for active combinations;
6. characterization, contract, or integration tests needed before behavior changes;
7. records and review triggers needed before another flag is added.

The exercise should not ask the reader to delete flags immediately.

## 20. Chapter-Local ADR/RFC Target

Use a record close to:

`Name the Product Modes Before Adding Another Compatibility Flag`

The record should capture:

- the current flags, modes, and compatibility toggles;
- the product states they imply;
- the supported, unsupported, obsolete, and unknown combinations;
- owners and reviewers for policy-bearing flags;
- the tests and release evidence that guard active combinations;
- the reason another compatibility flag is accepted, rejected, or deferred;
- the review trigger for future state-space changes.

## 21. Notebook Targets

The future draft should end with exactly three chapter-specific observations close to:

1. `A Boolean is cheap to add but expensive to combine.`
2. `Flags become product states when customers depend on them.`
3. `Reduce the state space before changing behavior.`

These remain chapter prose, not registered PEAK concepts.

## 22. Author Draft Acceptance Constraints

The Author Draft should be accepted only if it:

1. creates `book/06-legacy/35-reducing-boolean-explosion.md`;
2. preserves this canonical brief unchanged unless a later prompt explicitly authorizes brief revision;
3. keeps `CHAPTER-035` as `draft` until freeze;
4. does not add a `primary_concept` field;
5. does not create new PEAK concepts or relationship verbs;
6. includes the story target, engineering principle, exercise, ADR/RFC target, and three Notebook observations;
7. frames Boolean Explosion as uncontrolled product behavior combinations, not conditional style;
8. covers embedded and product-system crossings across firmware, backend, tools, manufacturing, support, upgrades, and
   release validation;
9. defers deletion to Chapter 36 and broad trust-sensitive refactoring to Chapter 37;
10. keeps Chapters 1-34 canonical and untouched.

## 23. Validation Checklist for This Registration

- Repository synchronized with `origin/main` before branch creation.
- `origin/main` contains Chapter 34 canonical state and manuscript.
- Working tree clean before editing.
- Branch `chapter35` created from `origin/main`.
- `editor/chapter-briefs/CHAPTER-035-reducing-boolean-explosion.md` created.
- `CHAPTER-035` registered exactly once as `draft` in `knowledge/index.yaml`.
- No `primary_concept` field added to `CHAPTER-035`.
- Required `CHAPTER-035` relationship set registered.
- No Chapter 35 manuscript created.
- No Chapter 36 or Chapter 37 files or registrations created.
- `editor/EDITOR_LOG.md` updated with Chapter 35 Canonical Brief Registration.
- Validation commands completed and recorded in the editor log.
- Commit subject: `docs(chapter-35): register canonical brief`.
- Next expected phase: Author Draft.

## 24. Review Handoff

Next expected phase: Chapter 35 Author Draft.

The next prompt should create the reader-facing manuscript only after this brief is committed and pushed. It should not
reopen Chapter 34 freeze work, revise Chapters 1-34, create Chapter 36 or Chapter 37 files, introduce a new PEAK concept,
or add a `primary_concept` field.
