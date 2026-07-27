# Refactoring Without Losing Product Trust

> A cleaner structure is not done until the product can still trust it.

## Story

### The Refactor That Was Technically Right and Operationally Wrong

The Refactor That Was Technically Right and Operationally Wrong began with a startup path everyone agreed was too hard
to change.

The controller had accumulated years of compatibility behavior. Old peripheral assemblies needed a longer cold-start
window. A service tool expected one diagnostic phrase before it offered a technician a recovery action. Manufacturing
used a final-test script that watched the same startup sequence. The backend translated a few controller reports into
fleet state. Support had procedures for mixed hardware during staged upgrades. Release validation had a matrix that
covered current hardware and a few known legacy combinations.

The code did not make that product surface obvious.

The startup path looked like a tangle of retries, helper calls, mode checks, diagnostic strings, and old fallbacks. One
branch handled current hardware. Another branch handled an older peripheral. A utility returned a default timeout. A
configuration flag changed the first diagnostic category. A backend mapper tolerated one old status field. The code had
tests, but they described the current happy path and a few explicit failures. They did not describe every product
promise that had grown around startup recovery.

The proposed refactor was technically sound.

The team wanted to move startup behavior behind a cleaner boundary. Instead of several call sites knowing about
peripheral timing, configuration flags, and diagnostic categories, a new startup coordinator would own the sequence.
The firmware would expose a smaller API. Retry policy would move out of a shared utility. State transitions would have
names. The old compatibility branch would stay for now, but its implementation would sit behind the new boundary.

The design review liked the direction.

The code would be easier to read. Dependency direction would improve. The state machine would be less scattered. The
new boundary would make later deletion and variant work more plausible. Characterization tests covered the firmware
behavior the team knew. The current hardware passed. The old peripheral test passed. No public API shape changed.

The release candidate exposed a failure the refactor had not been shaped to see.

Manufacturing reported inconclusive units on the rework station. The controllers started correctly, but the final-test
script watched for a diagnostic ordering the new coordinator no longer emitted. The script had not imported firmware
code. It had not been part of the unit test suite. It used the old sequence as evidence that a refurbished unit had
moved through recovery safely.

Support found the second break.

The service tool still connected to the controller. It still saw a recoverable condition. But it no longer showed the
technician the old guided flow because the diagnostic phrase had moved from an early message to a structured field the
tool did not read yet. The firmware team had preserved the product behavior in the controller. They had not preserved
the product behavior at the surface the technician used.

The backend team found the third break.

Their mapper accepted the new structured field. Their current contract tests passed. But a rollback expectation had
been missed. During staged upgrade, some customers could roll firmware back without rolling the service tool or backend
mapper back on the same day. The old diagnostic sequence had kept mixed versions understandable. The new sequence was
cleaner inside the controller and less trustworthy across release order.

The room reacted with understandable frustration.

"This is why we should stop touching startup."

"This is why we should rewrite the whole subsystem."

"This is why tools should not parse diagnostics."

"This is why manufacturing scripts need owners."

Each sentence contained a little truth. None of them was a plan.

Mara, the Principal Engineer, wrote a different sentence on the board:

> Refactor from the product promise inward.

She did not ban the refactor. She did not demand a rewrite. She did not let the team pretend that passing firmware
tests proved the product was safe. She asked them to rebuild the plan from the promises that had to remain trusted.

The first promise was startup recovery. A controller with a recoverable legacy peripheral condition should move through
one retry window, report a condition that tools and backend systems could interpret, and leave a technician with the
right next action.

The second promise was manufacturing confidence. A refurbished unit should give the station enough observable evidence
to distinguish a recoverable startup from an inconclusive unit.

The third promise was release compatibility. During a staged upgrade, old and new firmware, tools, backend mapping, and
support procedures should not require a perfect same-day rollout to remain understandable.

Naming those promises changed the refactor.

The team used the reading map from Chapter 32 to list behavior, state, timing, diagnostics, release order, support
records, and stale assumptions. They used the silent-coupling findings from Chapter 33 to name hidden dependents:
service tools, backend mappers, manufacturing scripts, dashboards, support procedures, and release validation. They
used the utility map from Chapter 34 to move retry policy out of the shared helper without changing the helper's
trusted outputs all at once. They used the state-space work from Chapter 35 to classify valid, obsolete, unsupported,
temporary, and unknown startup combinations. They used the deletion evidence from Chapter 36 to decide which old
branches should stay, which should be frozen, and which could become later deletion candidates.

The refactor became staged.

First, the new startup coordinator ran behind a compatibility boundary. It produced the old diagnostic sequence and the
new structured fields at the same time. The service tool consumed the old phrase while adding coverage for the new
field. Backend accepted both reports and recorded when the old path appeared. Manufacturing updated the station script
in a separate step and ran it against refurbished units before the firmware release. Support updated the procedure to
name the product state rather than one fragile phrase. Release added a mixed-version check to prove rollback remained
understandable.

Then the team added observability.

The controller emitted a shadow event when the old compatibility path was used. The dashboard separated raw device
status from backend classification. Logs carried enough context to distinguish slow peripheral startup, service-tool
action, backend delay, and manufacturing rework. Support cases gained a tag for the legacy startup recovery path.
Release owners watched the shadow event during the compatibility window.

Then the team recorded the movement.

An ADR named the product promise, the new boundary, the compatibility behavior, the retirement trigger, and the
rollback and recovery criteria. An Architecture Ledger row named owners and consumers. The Event Catalog described the
new structured field without pretending the old diagnostic phrase had no consumers. A Decision Journal entry captured
why the team kept dual reporting for two releases instead of forcing all surfaces to move at once. Architecture Review
checked the movement before it hardened. Architecture Freeze named the stable boundary for the release. Architecture
Health Review kept the remaining startup risk visible.

The final refactor was smaller than the rewrite people wanted during the incident review.

It was also more complete than the original clean boundary.

The code became easier to change. Retry policy had a clearer owner. Product-state combinations were visible. The
service tool stopped depending on a fragile diagnostic phrase. Manufacturing had a more explicit check. Backend mapping
had a clearer contract. Support had a better procedure. Release had rollback evidence. The old compatibility behavior
was not deleted by wish or preserved by fear. It had an owner, a window, and a retirement trigger.

Nobody mistook the improved structure for success by itself.

The refactor was successful because the product still knew how to trust the system while the structure changed.

## Discussion

Refactoring is not only a code-structure exercise.

In a product system, refactoring changes the way trust moves through the organization. A boundary can become cleaner
while a technician loses the recovery path they expected. A dependency can point in a better direction while a backend
mapper loses an ordering assumption. A utility can shrink while manufacturing loses a signal it used as evidence. A
state model can become more explicit while support procedures keep naming the old state. A local test suite can pass
while a field upgrade becomes harder to understand.

The first question is therefore not:

> How do we make this code cleaner?

The better question is:

> Which product promises must remain trustworthy while the structure changes, and how will we prove that they did?

That question changes the shape of the work.

It does not make internal structure unimportant. Structure matters because it changes future cost. Poor boundaries make
each product change expensive. Scattered ownership makes recovery fragile. Hidden state makes diagnosis slow. Utility
gravity makes every small policy change non-local. Boolean Explosion makes the product state space too large to reason
about. Dead behavior makes the system bigger than its promises.

But structure is not the only surface the product trusts.

Users trust workflows. Support trusts diagnostics and procedures. Manufacturing trusts scripts and station evidence.
Operations trusts logs, dashboards, alerts, and rollback signals. Release owners trust sequencing and compatibility
windows. Downstream teams trust API meaning, event meaning, timing behavior, and field stability. Future maintainers
trust records, tests, and discoverable ownership.

A refactor that improves one surface by spending trust on the others is not done.

This is why legacy refactoring starts with a product trust surface. The surface is not a new artifact. It is a working
view of who can be surprised if the structure moves. It includes formal consumers and informal dependents:

- users and customer workflows;
- firmware, backend, service tools, and downstream systems;
- manufacturing scripts, station logs, and rework procedures;
- support articles, escalation paths, and diagnostic names;
- operations dashboards, alerts, logs, and telemetry;
- release sequencing, upgrade paths, rollback expectations, and recovery procedures;
- architecture records, tests, owners, and future maintainers.

The surface may be large. That does not mean every refactor requires a giant program. It means the Principal Engineer
knows where trust can be spent accidentally.

Chapters 32 through 36 provide the inputs.

Chapter 32 gives the reading map. Before moving a boundary, read the behavior, owners, state, time, diagnostics,
records, evidence, and Change Radius. The reading map tells the team what the system is already protecting.

Chapter 33 gives the hidden dependents. Before calling a change local, trace the behavior through tools, scripts,
events, support, manufacturing, release, and people. Silent Coupling is the reason a refactor can break something that
never imported the code.

Chapter 34 gives the utility responsibility map. Before extracting or shrinking a helper, name what it has become
responsible for. Some shared mechanism can remain shared. Product policy needs owners, evidence, tests, and review.

Chapter 35 gives the product-state map. Before moving branches into a cleaner state model, classify the active,
invalid, unsupported, obsolete, temporary, and unknown combinations. A refactor that carries unknown combinations into a
new shape has not reduced the risk. It has made the risk look better organized.

Chapter 36 gives deletion evidence. Before removing old behavior as part of refactoring, prove whether the product
promise can disappear. Some old paths should be deleted. Some should be migrated. Some should be frozen. Some should be
left alone until evidence improves.

Together, those outputs can form a refactoring map.

The map starts with the product promise being preserved. It names the structural target: boundary, dependency
direction, ownership, API, state placement, configuration model, event flow, utility extraction, timing path, or
operational workflow. It lists the surfaces that can lose trust. It attaches evidence from reading, coupling, utility,
state-space, and deletion work. It chooses staged movement. It names rollback and recovery. It records what will change
outside the code. It defines how the team will know the system is easier to change afterward.

The map keeps the team from confusing movement with improvement.

Moving code behind a new interface may be useful. It may also preserve every old ambiguity behind a more modern name.
Extracting a component may reduce import cycles. It may also create a new API promise before consumers understand it.
Introducing branch-by-abstraction may let old and new paths coexist, but it can double the state space when the
retirement trigger is unclear. A shadow path may give evidence, but it can create false comfort when no one knows what
the shadow signal can and cannot see. Dual write may keep systems aligned during migration, but it can corrupt trust if
recovery after divergence is not defined.

Temporary compatibility is useful only when it has an owner and an exit.

`LAW-006`, Unused Flexibility Is Waste, applies to refactoring guardrails. A compatibility boundary, adapter, shadow
path, or dual report can protect trust during movement. It becomes waste when the team cannot say who owns it, what
promise it protects, what evidence retires it, or what review will revisit it.

The same is true of rollback.

Rollback proof is not the sentence "we can roll back." It is evidence that the old behavior can be restored quickly
enough, in the right version order, without confusing support, manufacturing, backend interpretation, service tools, or
customers. Recovery proof is broader. It says how the product will return to a trusted state after partial movement,
bad evidence, missed dependents, or a failed release path.

Some refactors should pause.

This is not cowardice. A pause can be the correct engineering decision when the product promise is not named, the owner
is unclear, the state space is unknown, the evidence cannot see the behavior, the rollback path restores code but not
trust, or the records are too stale for future maintainers to understand the movement.

Some refactors should continue despite discomfort.

This is also not heroism. Legacy systems do not become cheaper to change by waiting until every unknown is gone. The
Principal Engineer's job is to make the next movement proportionate to the evidence. A small observable slice may be
right. A compatibility boundary may be right. A temporary dual path may be right. A freeze point may be right. A later
deletion may be right. The point is to choose movement that preserves trust while improving structure.

Records are part of the refactor.

An ADR captures the consequential structural choice. An RFC helps when multiple teams must review the movement before
it hardens. A Decision Journal entry preserves smaller assumptions and trade-offs. A Mistake Ledger entry keeps prior
refactoring failures from becoming folklore. An Event Catalog row protects event and diagnostic meaning. An
Architecture Ledger row keeps owners, consumers, evidence, risks, and revisit triggers visible. Architecture Review
checks cross-boundary movement. Architecture Freeze names what becomes stable during the release. Architecture Health
Review tracks what remains expensive, fragile, or unclear.

Do not treat those records as paperwork after the "real" refactor.

If the code changes and the records still describe the old promise, the product surface is inconsistent. If dashboards
still imply old behavior, support will trust the wrong signal. If release notes omit the compatibility window,
customers may choose the wrong upgrade order. If tests prove only the new internal design, future engineers may not
know which external promises were preserved.

Refactoring finishes when the product surface and the structure agree.

That agreement does not require perfection. It requires honest evidence. The team should be able to say what promise
was protected, which surfaces were checked, which old assumptions were preserved or changed, which records were
updated, which rollback or recovery path exists, which compatibility behavior remains, and what evidence shows the
system is easier to change.

The last proof matters.

Refactoring can preserve trust and still fail to lower future change cost. If every old branch remains, every adapter is
permanent, every owner is still ambiguous, and every future change still requires the same expert meeting, the system
may be safer than before but not meaningfully easier to change. The goal is both: preserve current trust and reduce
future cost.

That is the closing move of Part VI.

Read before changing. Name hidden dependents. Map shared responsibility. Reduce the state space. Delete only with
evidence. Then refactor from the product promise inward.

Make the system easier to change without making the product harder to trust.

## Engineering Principle

Refactor from the product promise inward.

A Principal Engineer names the promise before moving the structure. They ask what users, support, manufacturing,
operations, release owners, downstream teams, and future maintainers must still be able to trust after the refactor.
Then they name the owners, dependents, evidence, staged movement, rollback path, recovery path, records, and review
checkpoints before moving structure across a trusted boundary.

Use the principle as an order of work:

1. Name the product promise that must remain trustworthy.
2. Name the structural target: boundary, dependency direction, ownership, API, state placement, configuration model,
   event flow, utility extraction, timing path, or operational workflow.
3. Name the trust surfaces that can be surprised.
4. Bring forward evidence from reading maps, hidden dependents, utility responsibility, state-space classification, and
   deletion evidence.
5. Decide what to preserve, migrate, freeze, delete later, pause, or leave alone.
6. Stage movement through compatibility boundaries, observable slices, shadow paths, dual reporting, or other temporary
   guardrails only when they have owners and exit criteria.
7. Prove behavior with characterization tests, contract tests, integration tests, telemetry, logs, service-tool checks,
   manufacturing checks, support checks, release checks, rollback proof, and recovery proof.
8. Update ADRs, RFCs, Decision Journal entries, Mistake Ledger links, Event Catalog rows, Architecture Ledger rows,
   dashboards, alerts, release notes, and support procedures where the promise changes.
9. Use Architecture Review before the movement hardens, Architecture Freeze for the release boundary, and Architecture
   Health Review for remaining legacy risk.
10. Prove the system is easier to change afterward.

This principle prevents two opposite mistakes.

The first mistake is purity: move the code because the new shape is cleaner, then discover that the product no longer
trusts a workflow, diagnostic, script, timing path, or release sequence.

The second mistake is paralysis: preserve every old behavior because one hidden dependent might exist somewhere. That
keeps trust by spending all future change capacity.

Trust-preserving refactoring takes the harder middle path. It protects the promises that still matter, makes accidental
promises visible, retires temporary guardrails when evidence allows, and leaves the next engineer with a system whose
shape and records are easier to reason about.

## Architecture Exercise

### Plan a Trust-Preserving Refactor

Choose one legacy refactoring target. Prefer an area where internal structure is making product work expensive in a way
the team can show with evidence: a boundary that leaks hardware detail, a utility carrying product policy, a dependency
direction that blocks ownership, a state model hidden behind flags, a configuration model nobody can review, an event
flow with unclear consumers, a timing path that only one person understands, or an operational workflow that depends on
old code shape.

Do not perform the refactor as part of this exercise.

Use the exercise to make the refactor ready.

Start with the product promise.

Write one sentence:

> We want to change [structure] while preserving [product promise] for [surfaces that trust it].

If the sentence cannot name the promise or the trusting surfaces, the refactor is not ready.

Then produce nine outputs:

1. The product promise that must remain trustworthy.
2. The structural target: boundary, dependency direction, ownership, API, state placement, configuration model, event
   flow, utility extraction, timing path, or operational workflow.
3. The surfaces that can lose trust: users, support, manufacturing, operations, release, downstream teams, service
   tools, dashboards, logs, customer workflows, or future maintainers.
4. Evidence from reading, coupling, utility, state-space, and deletion work. Separate what the evidence proves from
   what it cannot see.
5. The tests, telemetry, logs, service-tool checks, manufacturing checks, release checks, and support checks that prove
   behavior still holds.
6. The staged movement plan, including compatibility boundary, migration slice, observable signal, rollback path, and
   recovery path.
7. The records and dashboards to update: ADR, RFC, Decision Journal, Mistake Ledger, Event Catalog, Architecture Ledger,
   release notes, support procedures, alerts, or operational dashboards.
8. The review checkpoint and freeze point. Name who must review before the movement hardens and what becomes stable for
   the release.
9. The evidence that proves the system is easier to change afterward: reduced Change Radius, clearer ownership, lower
   Bus Factor risk, better Discoverability, stronger API Stability, simpler state space, retired temporary behavior, or
   improved Architecture Health.

End by choosing one of five dispositions:

- preserve for now because the promise is active;
- migrate through a staged compatibility path;
- freeze during the current release and revisit with evidence;
- delete later after Chapter 36-style evidence exists;
- pause because the promise, owner, dependent, or recovery path is not known.

The exercise is successful when a future pull request can be reviewed against product trust, not just against code
shape.

## Principal's Notebook

- A cleaner structure is not done until the product still trusts it.
- Refactor from the promise inward.
- The best legacy refactor lowers future change cost without spending current trust.

## ADR

### Refactor the Legacy Startup Path Behind a Compatibility Boundary

#### Status

Accepted for the next staged refactor of the legacy startup area.

#### Context

The controller startup path is difficult to change. Peripheral timing, retry policy, diagnostic categories,
configuration flags, backend classification, service-tool behavior, manufacturing rework, support procedures, release
sequencing, and field rollback expectations have grown around the same behavior.

The current structure is too expensive and risky to change because responsibility is scattered. Firmware owns the
state machine, a shared utility owns some retry defaults, backend mapping owns fleet interpretation, service tools own
technician workflow, manufacturing owns station evidence, support owns procedures, and release owns mixed-version
sequencing. Several old assumptions are active only because prior chapters' evidence found them: a reading map exposed
the startup promise, silent-coupling work found diagnostics and scripts as hidden dependents, utility mapping found
retry policy inside a shared helper, state-space work found temporary and unknown combinations, and deletion evidence
showed that old compatibility behavior is not yet safe to remove.

The product promise being preserved is: a controller with a recoverable legacy peripheral startup condition must remain
diagnosable, serviceable, usable in manufacturing, supportable, and recoverable during staged upgrade while the internal
startup structure changes.

#### Decision

Refactor the legacy startup path behind a compatibility boundary.

The new boundary will own startup sequencing, state transition naming, retry policy entry points, and structured
diagnostic output. Existing consumers will not be forced to move in the first release. The boundary will produce both
the old trusted diagnostic behavior and the new structured signal during a compatibility window.

Firmware will add characterization tests for current startup recovery behavior before moving code. Backend will add
contract tests for old and new startup reports. Service tools will add integration checks for technician recovery.
Manufacturing will run station checks against refurbished units and mixed hardware. Support will validate procedures
against the old diagnostic phrase and the new product-state wording. Release will validate mixed-version sequencing,
rollback, and recovery. Observability will include raw device status, backend classification, service-tool action,
manufacturing result, support-case tag, and compatibility-window dashboard views.

The compatibility boundary will have a retirement trigger. It can be removed only after shadow observations show no
active use outside the approved window, service tools and backend mapping consume the new structured signal, support
procedures no longer depend on the old phrase, manufacturing stations no longer use the old sequence as evidence, and
release can roll forward or recover without restoring the old diagnostic behavior.

Rollback criteria are product-facing. Roll back or pause if manufacturing inconclusive results rise, service-tool
recovery becomes ambiguous, backend classification diverges, support cases increase around legacy startup recovery,
customers inside the compatibility window lose upgrade confidence, or logs cannot distinguish slow startup from failed
startup.

Recovery criteria are also product-facing. The team must be able to restore the old trusted behavior or guide affected
surfaces to a known safe state, update records, communicate with support and release, and preserve evidence for the
next decision.

Update the ADR, Decision Journal, Event Catalog, Architecture Ledger, dashboards, alerts, release notes, support
procedures, manufacturing checks, and service-tool guidance as part of the refactor. Route the movement through
Architecture Review before it hardens. Use Architecture Freeze to name the stable release boundary. Surface unresolved
startup risk in Architecture Health Review.

#### Alternatives Considered

Refactor the startup path in one change because the internal design is easier to explain. This improves structure
quickly but spends product trust before manufacturing, support, service tools, backend mapping, and release sequencing
have evidence.

Rewrite the startup subsystem. This may eventually be attractive, but it expands Change Radius before the product
promise, dependents, rollback path, and recovery path are clear.

Keep the old structure indefinitely because it still works. This preserves current trust while continuing to spend
future change capacity, Bus Factor, Discoverability, and Architecture Health.

Move retry policy out of the shared utility without a compatibility boundary. This reduces Utility Gravity but risks
changing product policy hidden inside the helper.

Delete the old compatibility behavior as part of the refactor. Chapter 36-style evidence shows it is not safe yet.
Deletion remains a later decision with a retirement trigger.

Rely on rollback alone. Rollback may restore firmware code, but it may not restore manufacturing station confidence,
service-tool guidance, backend interpretation, support procedures, dashboards, or customer upgrade trust quickly enough.

#### Consequences

The refactor takes more than one pull request. The first movement creates a boundary and preserves trusted behavior.
The next movements migrate consumers, improve records, retire temporary compatibility, and reduce the remaining state
space when evidence allows.

The product stays trustworthy during the change. Manufacturing, support, service tools, backend owners, release owners,
and future maintainers can see what is moving and what must remain stable.

The system becomes easier to change for specific reasons: startup sequencing has an owner, retry policy is no longer
hidden inside an overgrown utility, diagnostics have explicit meaning, product states are classified, compatibility has
a retirement trigger, records point to the current promise, and later deletion can proceed with evidence instead of
hope.

The decision does not make the legacy area perfect. It makes the next structural movement reviewable.

## Editor's Commentary

Chapter 37 closes Part VI by refusing two tempting endings.

The first tempting ending is cleanup romance: read the legacy system, find its hidden dependents, map its utilities,
reduce its flags, delete some old behavior, and then finally make the code beautiful. That story flatters engineering
taste but misses product reality. A Principal Engineer cannot judge a refactor only by the elegance of the new shape.

The second tempting ending is legacy fatalism: old systems are too dangerous, so preserve every odd path, every
compatibility behavior, every global flag, every shared helper, and every support habit forever. That story protects
today by spending tomorrow. It turns past uncertainty into permanent architecture.

This chapter takes the middle path the book has been building toward.

Part I taught judgment, ownership, better questions, evidence, and stewardship. Part II named laws about state,
promises, time, simplicity, evidence, flexibility, and dependencies. Part III gave boundaries, Change Radius, recovery,
ADRs, RFCs, reviews, and freeze discipline. Part IV grounded the work in product reality: manufacturing, field
constraints, configuration, observability, releases, upgrades, diagnostics, and supportability. Part V made the work
organizational through leadership, rituals, shared memory, team alignment, and architecture health. Part VI applied all
of that to legacy systems.

Chapter 37 does not add a final framework. It gathers the existing discipline into one closing standard.

Read what the system promises. Name who trusts it. Make hidden dependents visible. Separate shared mechanism from
product policy. Reduce the state space. Delete only with evidence. Refactor from the product promise inward.

The final chapter before the Appendix should leave the reader with a practical measure, not a slogan:

Make the system easier to change without making the product harder to trust.
