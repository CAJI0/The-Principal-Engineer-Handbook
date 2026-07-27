# Managing Utility Gravity

> A utility is small only until product behavior depends on it.

## Story

### The Helper That Became the Platform

The Helper That Became the Platform began with a request that sounded too small for architecture.

A firmware team wanted to add one device default to `device_utils`.

The module had started years earlier as a harmless helper. It converted device timestamps into fleet time. It normalized
serial numbers. It wrapped a retry helper used by two controller families. Nobody disliked it. Nobody owned it with any
seriousness either. It was the kind of file people mentioned with a shrug: "Put it in the utility."

That was how it grew.

One release added a default timeout for old sensors because the sensor driver could not be changed safely before a
field upgrade. Another added a configuration interpreter because the backend and firmware needed to agree on a compact
variant code. A service-tool team added a logging category so technicians could group startup failures by device type.
Manufacturing added a helper that translated test-station names into device families. Support asked for a fallback
that preserved an old recovery path while customers moved through staged upgrades. A product team added a feature flag
because the utility was already imported everywhere.

Each change had a reason.

Each change was reviewed locally.

None of the changes made `device_utils` look like a platform in a diagram.

By the time Mara, the Principal Engineer, saw the next pull request, the helper carried retry policy, time conversion,
device defaults, feature flags, configuration interpretation, logging categories, fallback behavior, and
product-specific decisions. It still had no named owner beyond "the firmware platform team usually reviews it." It had
tests, but the tests mostly checked helper outputs. It had consumers, but the import graph showed only code consumers,
not release paths, support procedures, manufacturing scripts, or the backend rules that had copied its meanings.

The proposed change looked safe.

A new controller variant needed a different startup grace period. The author added a branch to the utility: if the
device family was `MX-17` and the configuration included the new cold-start flag, the helper returned a longer retry
window and a new logging category. Firmware tests passed. The backend payload stayed the same. The service tool did not
call the changed function directly. Manufacturing did not import the utility at all.

The change failed in release validation.

The device started correctly. The backend accepted the status report. The firmware did not crash. But the service tool
classified the device as "field recovery required" because it grouped startup diagnostics by the old logging category.
The manufacturing script marked the same controller as inconclusive because the longer retry window pushed a readiness
event past the final-test expectation. Support saw the new category in a release candidate and asked whether existing
field instructions still applied. The backend team noticed that one customer-specific rule had been written using the
old default timeout as evidence that a module was late rather than still starting.

Nobody had changed the utility's signature.

They had changed what the utility promised.

The first reaction was to argue about whether the utility was bad.

"This is why shared helpers are dangerous."

"This is why teams should not add product behavior to utilities."

"This is why we should rewrite it."

"This is why we should extract a real library."

Mara let the complaints run for a few minutes and then put one sentence on the whiteboard:

> Before moving the utility, discover what it has become responsible for.

The team stopped debating whether `device_utils` was clean and started mapping what depended on it.

First they named the promises.

The utility promised normalized device time. It promised default retry windows. It promised interpretation of compact
configuration codes. It promised logging categories that support and service tools used as workflow cues. It promised
fallback behavior for staged upgrades. It promised a rough translation between product families and hardware behavior.

Those promises were not equal. Some were shared mechanism. Time normalization belonged in a common helper. Serial
number normalization probably did too. Some were product policy. A retry window for one controller variant did not
belong in a generic utility without an owner, tests, and review triggers. A support-facing logging category was not
just a string. A fallback that protected staged upgrades was not just dead-looking code.

Then they named the consumers.

Firmware consumed the helper directly. Backend code consumed its meanings indirectly through status mapping and variant
rules. The service tool consumed the logging categories. Manufacturing consumed the timing behavior through final-test
scripts. Support consumed the category names through field procedures. Release validation consumed all of it as a
compatibility surface. One senior engineer consumed it from memory: he knew which old customers still depended on the
fallback because he had helped them through the first upgrade.

That memory was useful. It was also a Bus Factor risk.

If the safe path through a utility required one person in the room, the utility's real contract was not discoverable
enough.

The team checked evidence before making a movement plan.

They read the utility tests and found only direct function examples. They searched backend mappings and found two rules
using the old default timeout. They checked service-tool code and found logging categories displayed as technician
actions. They read manufacturing scripts and found a readiness window copied from an old release note. They checked the
Decision Journal and found a note that the fallback was temporary until upgrade data stabilized. They checked the
Architecture Ledger and found no current owner. They checked support procedures and found a phrase that treated one
logging category as a recovery boundary.

The import graph had been accurate. It had also been incomplete.

Mara did not ask for a rewrite.

She asked for containment.

The team split the immediate work into three decisions.

The time conversion and serial normalization stayed shared mechanism. They already had clear behavior, broad stable
use, and tests that matched the product promise.

The controller-specific retry rule moved behind a product-owned policy function. Firmware still called it through the
utility during the release, but the owner and review path changed. Any future change to that rule would involve the
controller team, backend mapping owner, service-tool owner, manufacturing representative, and release validation lead.

The logging category stayed stable for existing support behavior. The new variant gained a structured diagnostic field
instead of overloading the category. The service-tool team added a contract test around the category meaning. Support
updated the procedure to name the product state instead of relying on a phrase from the tool.

They recorded the boundary movement.

The ADR named `device_utils` as a utility with platform-like responsibilities until the split completed. The RFC listed
known consumers and the migration plan for product policy. The Architecture Ledger gained an owner, risk, evidence
links, and revisit trigger. The Decision Journal captured why the team was not deleting the fallback yet. Architecture
Review accepted the containment plan and required Architecture Health Review to watch for new product policy entering
the helper.

The change shipped one release later than the team had hoped.

It shipped with fewer surprises.

Nobody celebrated a cleanup. There was no heroic rewrite. The utility did not disappear. Some of it deserved to remain
shared. Some of it needed ownership. Some of it needed a later refactoring plan. Some of it might be deleted after
field evidence improved.

The important shift was simpler than the code movement.

The team stopped treating a convenient helper as a harmless place to put product behavior.

They treated it as an architectural boundary.

## Discussion

Utility Gravity is responsibility accumulation inside a shared helper.

It is not merely code reuse. It is not merely a file that grew too large. A utility develops gravity when it becomes the
easy place to put unrelated product decisions: one more flag, one more default, one more retry rule, one more fallback,
one more conversion, one more diagnostic string, one more configuration interpretation, one more logging category.

Each addition can be reasonable in isolation. The force appears over time.

A helper becomes a hidden platform when product behavior starts depending on it without the contract, owner, tests,
records, and review path that a platform would require. The name still says "utility." The architecture says something
else.

Smallness does not make a utility harmless.

A small function can carry a large promise. A five-line timeout helper may decide whether a controller is still
recoverable. A string-normalization function may decide which support workflow appears in a service tool. A default
configuration helper may decide whether a customer variant is treated as old, new, supported, or unknown. A utility can
be physically small and architecturally wide.

This is where `LAW-002`, Every API Is a Promise, becomes practical. Internal utility functions can become API promises
even when nobody designed them that way. If firmware, backend, service tools, manufacturing scripts, support
procedures, and release validation depend on the behavior, the utility has a contract. The contract may be unnamed. It
may be incomplete. It may be known only through tests and memory. It is still a contract because changing it changes
what other surfaces can trust.

Utility Gravity often grows through convenience.

The utility is already imported. The helper is already tested. The module already knows about device families. The
function already handles time. The file already has a switch over configuration. The team is under release pressure.
Putting one more behavior there feels cheaper than creating a new owner, policy boundary, or review path.

Sometimes that choice is responsible. Shared mechanism is real.

Time conversion, byte-order normalization, serial formatting, checksum calculation, and small pure transformations can
deserve a shared utility. Reuse is not the enemy. A good shared helper reduces duplication without hiding product
policy. It has a clear promise, clear ownership, clear tests, and consumers that can understand what they are trusting.

The danger begins when shared mechanism and product policy blur.

Shared mechanism answers a stable technical question: how to convert this timestamp, parse this identifier, normalize
this value, or perform this common calculation. Product policy answers a product question: how long this controller may
wait, which fallback applies to this customer path, which diagnostic category sends a technician into recovery, which
variant is allowed to use which behavior, which release combination is still supported.

Those two kinds of decisions need different owners.

`LAW-001`, Every State Has One Owner, applies here because utility state is easy to smuggle past ownership. A cache, a
default table, a feature flag interpretation, a retry counter, a last-seen device mode, or a product-family map can
become state that several teams rely on while ownership of the meaning stays unclear. Hidden State (`SMELL-004`) makes
a utility feel simple from the outside while carrying decisions that should be explicit.

Global Configuration (`ANTIPATTERN-003`) increases gravity quickly. A global flag enters the utility as convenience.
Later it distinguishes product variants, customer exceptions, manufacturing modes, support workflows, or staged
upgrade behavior. Once that happens, a helper change is no longer a helper change. It is a product dependency decision.

HAL Everywhere (`ANTIPATTERN-002`) can create a similar pull from the other direction. Platform or hardware details
spread through convenience helpers until product code, service tools, and backend rules all depend on assumptions that
belong behind a clearer boundary. Platform Leakage (`SMELL-005`) is often visible in the utility's arguments and return
values: hardware timing, vendor error codes, board revisions, and low-level states appear in places that are supposed
to speak product language.

A utility can also become a disguised God Module (`ANTIPATTERN-001`). The code may not look like a classic giant class,
but the responsibility pattern is similar: unrelated decisions gather in one place because that place is convenient and
everyone is afraid to move it. The fear is not irrational. It usually means the utility's consumers are real but not
discoverable.

Temporary Solution (`ANTIPATTERN-006`) appears when a fallback, customer exception, or one-release helper becomes part of
normal product behavior. The temporary move may have been responsible when it was made. Utility Gravity begins when the
reason and owner disappear while the behavior remains trusted.

Import graphs help, but they do not settle the question.

An import graph can show direct code consumers. It cannot show every support procedure, manufacturing script, release
habit, backend meaning, technician workflow, or customer upgrade sequence that depends on the utility's behavior. It
cannot tell whether a logging category is displayed as an operator action. It cannot tell whether a default timeout has
become a backend interpretation rule. It cannot tell whether one senior engineer knows the customer exception that
keeps a fallback alive.

The consumer map needs several kinds of evidence.

Tests show expected behavior, but they may test only the helper and not the product path. Logs show runtime facts, but
only if the producer, consumer, timing, and meaning are understood. Release notes show what the organization promised.
Support articles show what technicians are told to do. Manufacturing scripts show what the factory uses as evidence.
Backend mappings show how device behavior becomes fleet state. ADRs, RFCs, Decision Journal entries, and Architecture
Ledger rows show what the organization decided, forgot, or deferred. Senior memory explains context that records may
have lost, but memory alone creates Bus Factor (`METRIC-002`) risk.

The Hero Engineer (`FAILURE-004`) is the warning sign when one person is the only reliable map of the utility.
The Release We Should Have Delayed (`FAILURE-005`) is the warning sign when release pressure exposes that the utility's
consumer map was smaller in the records than it was in the product.

Discoverability (`METRIC-003`) is the practical test. Could a future engineer find the utility's promises and consumers
without knowing whom to ask? If not, the utility may be carrying architecture invisibly.

Change Radius (`VOCAB-001`, `METRIC-001`) makes the cost visible. A utility's real Change Radius is not the number of
files it touches. It is the set of product paths that may change when the utility's behavior changes. In embedded and
product systems that radius can include firmware, backend services, service tools, manufacturing, support, release
validation, field procedures, and compatibility paths.

Utility Gravity and Silent Coupling often travel together.

Silent Coupling (`SMELL-001`) asks what behavior must change together without an explicit relationship. Utility Gravity
answers where many of those unnamed relationships can accumulate. A helper pulls in responsibility. The responsibilities
quietly connect teams. A local change becomes non-local because too many product surfaces now orbit the same utility.

This is the same force behind Logger That Became a Platform (`FAILURE-001`). A shared component can start as a narrow
mechanism and become a product surface because other teams build behavior around its categories, timing, retention,
or meaning.

The first response should usually be containment, not deletion.

Deletion may be right later. Refactoring may be right later. But if the utility is already a hidden platform, deleting
or moving it before naming its promises and consumers just relocates risk. Chapter 36 owns deletion. Chapter 37 owns
trust-preserving refactoring. Chapter 34 earns those later moves by making the boundary visible first.

Containment means several practical things.

Name the utility's current promises. Assign owners for shared mechanism and product policy. Add characterization or
contract tests around active behavior. Record consequential decisions in an ADR. Use an RFC when cross-team movement
needs proposal review. Use a Decision Journal entry when the decision is smaller but still worth remembering. Put active
utility responsibilities into the Architecture Ledger with owners, evidence, risk, and revisit triggers. Route
cross-boundary movement through Architecture Review. Surface repeated utility gravity in Architecture Health Review.

Some utilities should remain shared.

The goal is not to punish reuse. The goal is to stop pretending every shared helper is merely a helper. If a utility is
intentionally a platform, name the platform contract, owners, consumers, review path, tests, and records. If it is not a
platform, keep product policy from gathering there by default.

Utility Gravity is managed when the team can answer a calm question before the next change:

What has this utility become responsible for?

## Engineering Principle

Treat an overgrown utility as an architectural boundary.

Before adding, extracting, or moving behavior, name its promises, owners, consumers, state, policies, evidence, and
Change Radius. Do this before the team debates whether the utility is clean, ugly, reusable, obsolete, or ready for
extraction.

Start with the promise. What does the utility actually guarantee today? It may guarantee a conversion, a retry window, a
fallback, a logging category, a default, a configuration meaning, or a compatibility behavior. If other product paths
depend on it, the promise is real even when the name says "helper."

Then name the consumers. Direct imports matter, but so do tests, tools, release paths, support procedures,
manufacturing scripts, backend mappings, field workflows, and senior memory. The consumer list does not have to be
perfect. It has to be honest enough to prevent a local-looking change from surprising the product.

Separate mechanism from policy. Shared mechanism can remain shared. Product policy needs an owner, evidence, review
path, and record. When those two are mixed, a utility becomes the easiest place to make decisions that no one later knows
how to review.

Choose the smallest responsible movement. Sometimes the answer is to leave the utility alone and add tests. Sometimes
it is to assign an owner. Sometimes it is to split one policy function away from shared mechanism. Sometimes it is to
route future changes through Architecture Review. Sometimes it is to write an ADR or RFC before the boundary moves.

The important discipline is order:

> Map the responsibility before moving the code.

A utility becomes safer when its promises are visible enough to own, test, review, and eventually simplify.

## Architecture Exercise

Map the Utility Before Moving It.

Choose one shared helper or utility that people are tempted to extend, extract, rewrite, or delete. Prefer one used by
more than one team, product path, tool, script, or release workflow.

Document the current boundary:

1. utility name and visible owner;
2. current promise;
3. known consumers;
4. suspected hidden consumers;
5. state, defaults, flags, retries, conversions, logging categories, diagnostics, or fallback behavior inside it;
6. product policy mixed with shared mechanism;
7. evidence sources;
8. likely Change Radius;
9. Bus Factor and Discoverability risk;
10. review boundary;
11. record to update;
12. decision to make now;
13. deletion or refactoring question to defer.

Keep the exercise concrete. Use one utility and one proposed movement. Do not try to map every shared helper in the
system.

End with exactly five outputs:

1. one utility promise to name;
2. one consumer to verify;
3. one owner or reviewer to assign;
4. one record to repair;
5. one movement to defer until evidence exists.

Use the records the system already trusts. Do not create a new canonical artifact for the exercise.

## Principal's Notebook

- A shared helper can become a hidden platform.
- Utility promises need owners.
- Map the consumers before moving the code.

## ADR

### Split Product Policy From the Shared Device Utility Before Adding More Behavior

### Status

Accepted for the next utility-boundary change.

### Context

A shared device utility now carries retry policy, time conversion, defaults, flags, logging categories, fallback
behavior, and product-specific decisions.

Firmware, backend services, service tools, manufacturing scripts, support procedures, release validation, and tests may
depend on the current behavior. The import graph shows direct callers, but it does not show every product path that
trusts the utility's meanings.

No current record names the utility as a platform-like interface. The Architecture Ledger does not identify a current
owner for several product policies inside the helper. Adding one more branch would increase Utility Gravity and make
later movement harder.

### Decision

Do not add new behavior until the utility's promises, owners, consumers, state, policies, evidence, and Change Radius
are mapped.

Separate shared mechanism from product-specific policy where evidence supports the split.

Add characterization or contract tests around active utility promises.

Update the ADR, RFC, Decision Journal, or Architecture Ledger with the owner, consumers, evidence, risk, and revisit
trigger.

Route cross-boundary utility movement through Architecture Review.

Surface recurring utility gravity in Architecture Health Review.

Defer deletion or broad refactoring until compatibility and product trust can be preserved.

### Alternatives

Add another flag because the utility is already shared.

Rewrite the utility before naming consumers.

Extract a library from the current shape.

Rely on import graphs alone.

Ask the senior engineer and keep the knowledge in memory.

Remove obsolete-looking branches before dependent behavior is understood.

### Consequences

The first movement takes longer because the team must trace responsibility before changing the boundary.

Ownership becomes clearer. Shared mechanism can stay shared, while product policy gains owners, tests, and review
paths.

Release surprises become less likely because firmware, backend, service tools, manufacturing, support, and validation
paths are visible before the utility changes again.

Records improve. The utility's active promises can be found in ADRs, RFCs, the Decision Journal, or the Architecture
Ledger instead of living only in memory.

The team keeps a future path toward simplification, deletion, or refactoring without pretending those moves are safe
before the product trust surface is known.

## Editor's Commentary

This chapter exists because legacy systems often hide architecture in places that sound too modest to review.

Chapter 32 taught the reader to read the system before changing it. Chapter 33 taught the reader to find silent
behavioral dependencies. Chapter 34 shows where many of those dependencies gather: the shared helper that became
convenient enough to attract policy, state, defaults, fallbacks, diagnostics, and cross-team assumptions.

The chapter is careful not to make utilities the villain. Shared mechanism is valuable. A well-owned helper with clear
promises can make a system simpler. The danger is not reuse. The danger is product responsibility gathering in a place
that has no matching contract, owner, evidence, or review path.

That is why the Principal Engineer's move is not theatrical. They do not demand a rewrite. They do not delete the
helper. They do not extract a library because the shape looks reusable. They slow the first movement enough to discover
what the utility has become responsible for.

This preserves the rest of Part VI. Boolean Explosion, deletion, and trust-preserving refactoring may all appear after
utility gravity is visible. They are not this chapter's work. This chapter gives those later decisions a safer starting
point: named promises, named owners, known consumers, evidence, records, and review boundaries.

A utility becomes architecture when the product depends on it.

Treat it accordingly.
