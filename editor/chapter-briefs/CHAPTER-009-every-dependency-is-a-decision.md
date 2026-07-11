# CHAPTER-009 Canonical Brief: Every Dependency Is a Decision

## Metadata

- Stable ID: `CHAPTER-009`
- Title: Every Dependency Is a Decision
- Part: Part II, The Laws
- Intended manuscript path: `book/02-the-laws/09-every-dependency-is-a-decision.md`
- Manuscript status: not created in this gate
- Knowledge status: `draft`
- Canonical law mapping: `LAW-007` - Every Dependency Is a Decision
- Branch baseline: `origin/main` at `e2fd0ce68338fb12df13d563d601a1f1495a19d0`
- Gate: Canon Resolution and Canonical Brief Registration
- Next gate after approval: Author Draft

## Repository-Grounded Findings

- `book/TOC.md` names Chapter 9 as "Every Dependency Is a Decision".
- `editor/ARCHITECTURE_VISION.md` lists "Every dependency is a decision" as part of the book's core philosophy.
- `editor/CANON.md` and `knowledge/index.yaml` previously listed laws `LAW-001` through `LAW-006` only.
- No existing PEAK law, vocabulary entry, smell, metric, ritual, artifact, or failure story was an equivalent concept.
- Chapter 7 and Chapter 8 canonical briefs already reserve Chapter 9 for dependency decisions.
- Chapters 1-8 remain frozen or canonical and must not be edited by this gate.
- `book/02-the-laws/09-every-dependency-is-a-decision.md` does not exist and must remain absent until Author Draft.

## 1. Canon Resolution

The canon mismatch is real. The book architecture and table of contents reserve a dedicated Part II law named "Every
Dependency Is a Decision", but the PEAK registry previously had no dedicated law for that title or meaning.

The approved resolution is to register a new law:

- ID: `LAW-007`
- Name: Every Dependency Is a Decision
- Path: `knowledge/laws/every-dependency-is-a-decision.md`
- Status: `draft`

Existing law IDs remain unchanged. In particular, `LAW-003` remains Time Is a Dependency, `LAW-004` remains Simplicity
Is a Feature, `LAW-005` remains Evidence Before Confidence, and `LAW-006` remains Unused Flexibility Is Waste.

No editorial ADR is required for this resolution. The decision follows the existing source-of-truth model: register the
missing PEAK concept, record the chapter brief, update the index, and log the gate outcome.

Author approval is not required before this registration because the prompt explicitly requests the canon resolution
gate and supplies the semantic test. The next author-facing step is the Author Draft gate.

## 2. Canonical Purpose

Chapter 9 teaches that dependency choice is an architectural decision.

The chapter should move the reader from a narrow idea of "dependency" as imported code toward a broader system view:
every dependency commits the system to behavior, change cost, failure modes, lifecycle constraints, ownership
boundaries, and replacement cost.

## 3. Central Thesis

Every dependency commits the system to behavior, change cost, failure modes, lifecycle constraints, ownership
boundaries, and replacement cost.

Dependency choice is therefore an architectural decision, not merely an implementation convenience.

## 4. Exact Law Statement

Use this law statement:

> Every dependency commits the system to behavior, failure modes, lifecycle constraints, ownership boundaries, and
> replacement cost.

The chapter may vary surrounding prose, but it must preserve this meaning.

## 5. Reader Transformation

The reader should stop treating dependencies as local convenience choices. By the end, the reader should ask:

- What behavior are we importing?
- What failure modes are we accepting?
- Who owns updates and compatibility?
- How far can this dependency spread?
- What would it cost to replace?

The chapter should make dependency review feel practical, not ceremonial.

## 6. Problem Frame

The problem is not that dependencies are bad. Modern systems need them.

The problem is that teams often accept dependencies without naming the architectural commitment. A library can shape
threading, memory ownership, error handling, observability, test strategy, build behavior, release cadence, service
operations, and field support long after the first use looked harmless.

## 7. Primary Dependency Definition

A dependency is any external or internal thing whose behavior the system relies on and cannot freely change alone.

Examples include:

- product libraries and shared modules;
- vendor components;
- cloud services;
- protocols;
- hardware parts;
- file formats and persisted schemas;
- build tools and release tools;
- test stations and manufacturing fixtures;
- operational procedures;
- team-owned services.

The chapter should avoid reducing the topic to package managers.

## 8. Scope In

The chapter should cover:

- dependency surface area;
- direct and transitive dependency cost;
- behavioral commitments;
- failure propagation;
- ownership and update responsibility;
- lifecycle and release cadence;
- replacement cost;
- where wrappers help and where they do not;
- how an ADR can record dependency choice.

## 9. Scope Out

The chapter should not become:

- a package management tutorial;
- a vendor selection checklist;
- a procurement chapter;
- a license compliance chapter;
- a security dependency scanning chapter;
- a generic "avoid dependencies" argument;
- a full Part III boundary-design chapter.

The chapter may mention these concerns when they serve the law, but it should not teach them as the main subject.

## 10. Dependency Categories

The author draft should show that dependencies take several forms:

- code dependency: a library, shared module, or internal package;
- service dependency: an API, database, queue, identity provider, or cloud capability;
- protocol dependency: a wire format, handshake, message contract, or version negotiation;
- hardware dependency: a part, driver, timing property, bus behavior, or manufacturing constraint;
- tool dependency: compiler, build image, test fixture, release packager, or observability pipeline;
- process dependency: operational procedure, support procedure, supplier process, or release schedule.

The point is not to list everything. The point is to teach the reader to notice imported commitments.

## 11. Direct and Transitive Dependencies

A direct dependency is visible in a decision, import, build file, interface, service call, or process handoff.

A transitive dependency is brought in by another dependency. It still affects the system, even when the team did not
choose it directly.

The chapter should show that transitive dependencies matter most when they leak behavior into product assumptions:
error codes, timing, storage formats, thread models, retry rules, hardware reset behavior, or release constraints.

## 12. Replacement Cost

Replacement cost is not only the effort to swap code.

It includes:

- contract redesign;
- data migration;
- test changes;
- fixture updates;
- operational training;
- support documentation;
- compatibility with already shipped versions;
- confidence rebuilding;
- customer-facing migration risk.

The reader should understand that a wrapper can reduce replacement cost only if the system actually depends on the
wrapper's contract instead of the underlying dependency's behavior.

## 13. Failure and Lifecycle Commitments

Every dependency imports failure behavior:

- how it times out;
- how it retries;
- how it reports errors;
- what happens during partial outage;
- what state it owns;
- which versions it supports;
- how quickly it changes;
- how long it is maintained.

The chapter should connect these commitments to ownership. Somebody must know who decides upgrades, compatibility,
fallbacks, deprecation, and removal.

## 14. Direction of Dependency

The chapter should distinguish useful dependency direction from accidental dependency direction.

Good dependency direction preserves architectural control. Product code can depend on a stable domain contract while
only a narrow adapter depends on a volatile vendor component.

Bad dependency direction lets the volatile dependency define product behavior, vocabulary, error handling, and tests.

## 15. Boundary With Chapter 7

Chapter 7 teaches that every state has one owner.

Chapter 9 may reuse state ownership as one consequence of dependency choice, but it must not reteach Chapter 7. The
boundary is:

- Chapter 7 asks who owns state.
- Chapter 9 asks what commitments enter the system when we depend on something.

## 16. Boundary With Chapter 8

Chapter 8 teaches that every API is a promise.

Chapter 9 may use APIs as one dependency form, but it must not reteach Chapter 8. The boundary is:

- Chapter 8 asks what observable behavior a boundary promises.
- Chapter 9 asks whether choosing that boundary imports lifecycle, failure, ownership, and replacement cost.

An API can be the mechanism through which a dependency is expressed, but the dependency decision is broader than the
API signature.

## 17. Boundary With Chapter 10

Chapter 10 is reserved for Time Is a Dependency.

Chapter 9 may mention timing, timeouts, cadence, and release schedules as imported dependency commitments, but it must
not make time the main subject. Chapter 10 owns the deeper law about clocks, ordering, delays, schedules, freshness,
and temporal assumptions.

## 18. Boundary With Chapters 11-13

Chapter 11, Unused Flexibility Is Waste, owns speculative extension and premature generality.

Chapter 12, Simplicity Is a Feature, owns simplicity as a system property.

Chapter 13, Evidence Before Confidence, owns proof, validation, and justified belief.

Chapter 9 may reference these laws only as consequences:

- dependency abstraction should not become unused flexibility;
- a dependency can increase or reduce simplicity;
- replacement cost and failure behavior should be tested when confidence matters.

## 19. Boundary With Later Parts

Later parts may teach architecture reviews, modularity, platform boundaries, migration planning, and governance in more
detail.

Chapter 9 should stay at law level. It should name the architectural commitment and give the reader enough practice to
recognize it, without becoming a full playbook for dependency governance.

## 20. Primary Story Requirement

Use one durable story. It should be specific enough to feel real, but not tied to a named vendor, cloud provider,
protocol, framework, or current industry trend.

Recommended story shape:

1. A team adopts a vendor library or internal platform component because it solves a real problem quickly.
2. The integration appears isolated behind a thin wrapper.
3. Over time, the dependency's behavior spreads into product code, tests, manufacturing, release, or support.
4. A change, upgrade, outage, part replacement, or deprecation reveals that the dependency had become architecture.
5. The principal engineer changes the frame from "swap the implementation" to "name and contain the commitments".

The story must not make the dependency choice look foolish in hindsight. The original decision should be understandable.

## 21. Discussion Arc

The author draft should follow this arc:

1. Show a dependency chosen for good local reasons.
2. Reveal the imported behavior that was not named.
3. Show the cost when change arrives.
4. Distinguish dependency use from dependency spread.
5. Explain why wrappers are not enough unless they define the real contract.
6. Teach a practical dependency decision frame.
7. Close with an Engineering Principle and exercise.

## 22. Law Applicability

The law should apply across:

- embedded systems;
- backend systems;
- internal platforms;
- cloud services;
- data systems;
- hardware and manufacturing;
- release engineering;
- operational tooling.

Keep examples grounded in durable system behavior, not fashionable tools.

## 23. Legitimate Exceptions

The chapter must not imply that every dependency requires a heavy review.

Lightweight dependencies can be acceptable when:

- they are isolated;
- behavior is obvious and low-risk;
- replacement is cheap;
- the dependency does not shape product semantics;
- failure modes are contained;
- ownership is clear.

The principal engineer's job is not to block dependencies. It is to match review effort to commitment size.

## 24. Violation Patterns

The chapter should make these violations visible:

- a dependency's vocabulary becomes product vocabulary;
- tests assert vendor behavior instead of product behavior;
- a wrapper exposes all underlying concepts unchanged;
- release cadence follows an external component without a named owner;
- failures are handled according to undocumented assumptions;
- transitive dependencies define runtime behavior;
- replacement is claimed to be easy without evidence;
- a dependency is treated as local while its effects cross team boundaries.

## 25. Engineering Principle Target

The Engineering Principle should be concise and operational.

Target meaning:

Name the commitment before accepting the dependency. If the dependency can shape behavior, failure, lifecycle, or
replacement cost, record the decision and contain the spread.

The final wording can change during Author Draft, but it must preserve this meaning.

## 26. Exercise Target

The exercise should ask the reader to audit one dependency in their own system.

It should lead them to identify:

- the imported behavior;
- the owner;
- the failure mode;
- the update path;
- the replacement trigger;
- the boundary that contains it;
- the evidence that replacement would be possible.

The exercise should be practical enough for a team meeting or architecture review.

## 27. ADR Target

The chapter should include or point toward a small ADR-shaped decision record.

The ADR should not be a bureaucratic artifact. It should capture:

- dependency chosen;
- problem it solves;
- alternatives considered;
- imported commitments;
- ownership;
- update plan;
- exit trigger;
- known risks.

Use `ARTIFACT-001` ADR as the PEAK artifact. Do not introduce a new dependency-decision artifact in this gate.

## 28. PEAK Concept Map

Primary concept:

- `LAW-007` - Every Dependency Is a Decision

Selected supporting concepts:

- `VOCAB-001` - Change Radius
- `SMELL-001` - Silent Coupling
- `ARTIFACT-001` - ADR
- `METRIC-003` - Discoverability

Considered but not registered as outgoing Chapter 9 relationships:

- `ARTIFACT-003` - Decision Journal: useful, but Chapter 9 should use ADR as the main dependency decision artifact.
- `RITUAL-001` - Architecture Review: useful later, but not required as a primary relationship for this brief.
- `METRIC-004` - API Stability: relevant to service dependencies, but Chapter 8 owns the main API stability teaching.
- `FAILURE-001` - Logger That Became a Platform: related, but not the primary story for Chapter 9.
- `FAILURE-002` - One Lost Packet: reserved for time and recovery contracts.
- `LAW-002` - Every API Is a Promise: boundary relation is textual, not a registered Chapter 9 outgoing edge.
- `LAW-003` - Time Is a Dependency: boundary relation is textual, not a registered Chapter 9 outgoing edge.

No additional PEAK concepts should be created during Author Draft unless a later gate explicitly approves them.

## 29. Exact Outgoing Relationships

Register these exact outgoing relationships for `CHAPTER-009`:

- `CHAPTER-009 illustrates LAW-007`
- `CHAPTER-009 illustrates SMELL-001`
- `CHAPTER-009 references VOCAB-001`
- `CHAPTER-009 references ARTIFACT-001`
- `CHAPTER-009 references METRIC-003`

Do not add broad `related_to` relationships from the chapter.

## 30. Required Chapter Architecture

The manuscript must follow the current chapter architecture:

1. opening quote;
2. chapter title;
3. story opening;
4. "The Principle";
5. explanatory middle;
6. "The Practice";
7. "The Tradeoff";
8. "The Failure Mode";
9. "The Principal Engineer's Job";
10. "Questions to Ask";
11. "Principle";
12. "Exercise";
13. "Summary";
14. "Principal's Notebook".

The Author Draft gate must verify the exact H2 sequence against `editor/CHAPTER_ARCHITECTURE.md`.

## 31. Principal's Notebook Candidates

Use exactly three notebook observations in the manuscript. Candidate meanings:

- A dependency is a decision about future change.
- A wrapper is only useful when callers depend on the wrapper's contract.
- Replacement cost is not real until someone can explain the path out.

The final notebook wording can change, but the observations should remain short and distinct.

## 32. Technical Requirements

The chapter must be technically credible:

- do not claim that wrappers automatically make dependencies replaceable;
- do not claim that internal dependencies are harmless;
- do not claim that all vendor dependencies are dangerous;
- do not claim that replacing code replaces operational behavior;
- do not claim that transitive dependencies matter only at build time;
- do not claim that an ADR eliminates risk;
- do not claim that every dependency requires a formal review.

## 33. Review Handoff Notes

Author Draft should create only the Chapter 9 manuscript and any explicitly required log entry for that gate.

Author Draft must preserve this brief's law mapping, outgoing relationships, and no-renumbering decision. It should not
edit Chapters 1-8.

Reviewers should pay special attention to whether the chapter teaches the law rather than drifting into package
management, vendor management, or generic abstraction advice.

## Final Scope Statement

Chapter 9 exists to teach dependency choice as architecture. It should leave the reader with a concrete habit: before a
dependency spreads, name the commitment, contain the surface, assign ownership, and know what replacement would cost.
