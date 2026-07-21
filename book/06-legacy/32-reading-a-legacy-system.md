# Reading a Legacy System

## Opening Quote

> Legacy code is not code nobody understood. It is code whose promises outlived the records that explained them.

## Story

The System That Everyone Knew Differently began with a request that sounded too small to deserve a meeting.

A new hardware variant needed a slightly longer response window during startup. The product manager described it as a
compatibility tweak. The firmware lead called it a timeout adjustment. The backend team thought it was probably a
device-registration detail. Support said it might affect a field procedure. The tools engineer said the service tool
would not care, as long as the diagnostic text stayed the same.

Nobody was trying to be vague. They were each describing the system they knew.

The product had been in the field for years. It paired a controller, a replaceable peripheral module, a service tool, a
backend API, and a set of support procedures that had grown around real customer sites. The integration still worked.
It also carried old patches, sparse documentation, a few ADRs from a different product era, scripts nobody wanted to
touch, release notes that support used as operational guidance, and firmware assumptions that were older than some of
the engineers assigned to the change.

The first diagram looked reassuring.

It showed a controller speaking to the peripheral module, the controller posting status to the backend, and the service
tool reading diagnostics from the controller. The boxes were clean. The arrows were named. The document had a title,
an owner, and the confident tone of something that had once been true.

The diagram was six years old.

It did not show the fallback path added after a customer site lost connectivity during an upgrade. It did not show that
the backend accepted one odd firmware response as a valid compatibility signal. It did not show that the service tool
parsed a diagnostic string because an old support script looked for that exact phrase. It did not show the configuration
flag whose name suggested a lab-only escape hatch even though it now protected a field workflow.

The code did not make the missing picture obvious.

The timeout constant lived beside a state-machine transition. The fallback lived in a helper with a harmless name. The
configuration flag was global, written in one startup path, read in three runtime paths, and interpreted differently by
two product variants. The diagnostic string looked like a log message until the tools engineer mentioned the service
tool. The backend compatibility behavior looked like defensive parsing until the backend engineer said, "Do not remove
that. Some deployed firmware only reports readiness that way."

Tests passed.

They were mostly happy-path tests. They proved that the new module registered when it answered quickly, that the
controller rejected a module in an explicit failure state, and that the backend received a normal status payload. They
did not prove the startup window under slow peripheral response. They did not prove what happened when connectivity was
absent during the first boot after upgrade. They did not prove that support could still recover a site through the
service tool. They did not prove that an old firmware response was still a product promise rather than an accidental
tolerance.

The logs were plentiful and oddly unhelpful.

They showed retries. They showed state names. They showed the diagnostic string. They showed timestamps. They did not
show which clock was valid when the record was written. They did not show whether a retry came from peripheral delay,
backend delay, a service-tool action, or a local fallback. They did not show the owner of the state being changed. In a
field incident, the same failure could look like a packet loss, a late module, a stale backend response, or a technician
using the documented recovery path at the wrong moment.

The senior engineer remembered the strange rule.

"If the module says `pending-ready` after the first timeout, the controller waits once more before declaring failure.
That was for one large customer. Their sites rebooted the module slower after cold storage. We kept the wording because
the service tool recognized it."

Someone asked where that was recorded.

The room got quiet.

There was an ADR about the original module-registration flow. It did not mention the customer. There was a release note
that said, "Improved startup tolerance for selected field conditions." There was a support article that told
technicians to wait for "pending-ready" before power cycling. There was a script in the service-tool repository that
matched that text. There was a backend mapper that treated the same condition as compatible with a newer module family.
There was no current record saying which of those facts was the reason the fallback still existed.

The proposed cleanup suddenly looked less clean.

Removing the fallback would reduce code. It would also change a field recovery procedure, a diagnostic promise, a
backend interpretation, and possibly a release path. Increasing the timeout would keep the fallback but might hide a
slow startup that support needed to distinguish from a broken module. Renaming the diagnostic string would make the
logs clearer and break the service tool. Moving the configuration flag into the new product variant would look tidy and
could change behavior for an old customer whose workflow nobody wanted to rediscover during an outage.

The Principal Engineer did not ask the team to modernize the subsystem.

She asked them to read it.

Not line by line, at least not first. She asked for a reading map before the first change.

The map started with the requested change: add compatibility behavior for the new hardware variant without breaking
existing startup recovery. Then the team wrote the visible product promise: a controller must distinguish a slow module
from a failed module and keep support able to recover a site. They wrote the suspected hidden promise: the
`pending-ready` diagnostic and second wait may be part of a field procedure and backend compatibility rule.

They named the state.

The controller owned module-registration state. The peripheral module supplied readiness signals. The backend stored
fleet status. The service tool interpreted controller diagnostics for a technician. The support procedure interpreted
the same words as an operational instruction. That meant the controller was not merely changing an internal timeout. It
was keeping a promise at a boundary several consumers already trusted.

They traced the time assumption.

The first timeout was a runtime wait. The second wait was not just a delay; it was a compatibility behavior after a
specific diagnostic state. Release windows mattered because some sites upgraded controller firmware before module
firmware. Ordering mattered because the backend could see the controller's report before the module completed its local
startup. The old release path had taught customers a sequence that the new change could accidentally invalidate.

They traced dependencies.

The firmware depended on a peripheral quirk. The backend depended on a controller interpretation. The service tool
depended on diagnostic text. Support depended on release notes and a field procedure. The field procedure depended on
people remembering when to wait and when to power cycle. The build pipeline depended on a script nobody liked touching.
Those were not all code dependencies, but they were all decisions the change might disturb.

They compared evidence.

The code showed what could happen. The tests showed only normal startup and clear failure. The logs showed symptoms but
not enough cause. The old ADR explained the original clean model, not the later fallback. The release note proved that
someone had promised improved startup tolerance, but not exactly how. The support article proved that diagnostic words
had become operational. The backend mapper proved that a firmware quirk had become accepted behavior. The senior
engineer's memory explained why, but memory alone was a Bus Factor (`METRIC-002`) risk, not a durable record.

The first useful change was not the requested code change.

It was a small characterization test around the current fallback behavior. The test named the compatibility path:
when the module reports `pending-ready` after the first startup timeout, the controller waits once more, emits the
existing diagnostic, and reports a compatibility status the backend still accepts. The team also added one diagnostic
field to distinguish peripheral delay from backend delay without changing the message the service tool consumed.

They updated the Decision Journal with the active assumption. They added a note to the Architecture Ledger that the
fallback was a legacy promise pending review, not dead code. They linked the old ADR, the release note, the support
article, the backend mapper, and the new characterization test.

Only then did they make the product change.

It was smaller than the original cleanup and more precise than the original timeout tweak. The new hardware variant
received a bounded compatibility path. The existing diagnostic promise remained stable. The backend behavior remained
compatible. Support got a record that explained what to watch during rollout. The team still had work ahead: coupling
to find, utilities to unwind, flags to simplify, and code to delete.

The change did not make every slow startup wait longer. It preserved the legacy behavior only when the transitional
readiness signal appeared, because that was the promise the reading map had enough evidence to name.

But the first change no longer depended on everyone remembering the same system.

It depended on a map.

## Discussion

Legacy reading is the disciplined act of building a change-safe model of a system before editing it.

It is not passive browsing. It is not reverence for old code. It is not a modernization plan. It is an architectural
discovery practice for situations where the system still works, the records are incomplete, and the cost of being wrong
may appear outside the file you want to change.

The phrase code archaeology names part of the work, but only part of it. The reader is not digging through old commits
for nostalgia.
They are building a product promise map: a practical picture of the behaviors, boundaries, states, diagnostics, tools,
procedures, and release expectations the subsystem still keeps alive.

The usual first question is, "Where should we start fixing this?"

For a legacy system, the better first question is, "What must be true about this system before I can make a responsible
change?"

A working legacy system protects promises, even when nobody has recently named them. Some promises are obvious: an API
shape, a storage schema, a protocol response, a timeout, a release sequence. Others hide inside diagnostic strings,
service-tool screens, retry behavior, field procedures, default configuration, log names, backend tolerances, scripts,
operator habits, and senior memory.

Legacy code is often protecting something the organization stopped naming.

The code matters. It is not enough.

Code tells you what can execute. It does not automatically tell you which behaviors users rely on, which boundary
quirks have become compatibility promises, which records are stale, which tests are representative, which logs can be
trusted, which release paths constrain the next change, or which person is the only remaining interpreter of a strange
rule.

That is why Chapter 32 opens Part VI with reading rather than refactoring.

The first responsibility is not to make the system beautiful. The first responsibility is to avoid breaking a promise
you have not yet discovered.

Start with behavior.

What does the subsystem do for users, operators, support, manufacturing, service tools, other services, firmware,
deployment, or recovery? Which visible behavior would someone notice if it changed? Which behavior is documented only
by an operations guide, a support article, a release note, a script, or a habit?

Then ask who owns state.

`LAW-001` does not become less important because the code is old. In legacy systems, state ownership is often exactly
what became unclear. A value may be written by startup code, corrected by a background job, interpreted by an API,
overridden by a service tool, and explained by a support procedure. If the owner is not visible, edits will tend to
move state by accident.

Reading should identify writers, readers, interpreters, and authority. Who can change the value? Who treats it as
truth? Who derives behavior from it? Who is allowed to repair it? Where is it persisted? Where is it cached? Where is
it copied? Where can it become Hidden State (`SMELL-004`) because the fact that matters is present only in a runtime
condition, a global flag, or a path-dependent sequence?

Boundaries deserve the same care.

`LAW-002` says every API is a promise. In legacy systems, APIs are often larger than their formal interfaces. A
diagnostic string can be an API if a service tool parses it. A status name can be an API if support tells customers to
wait for it. An error code can be an API if the backend maps it to compatibility behavior. A timeout can be an API if
callers schedule around it. A release note can turn a tolerance into a promise.

A legacy boundary is any place where old behavior is still trusted by a current consumer, even when the source code no
longer advertises that trust.

API Stability (`METRIC-004`) is therefore not only about signatures. It is about whether dependents can still trust the
meaning, timing, error behavior, compatibility behavior, and recovery behavior they have learned.

Read time and ordering explicitly.

`LAW-003` is easy to miss in legacy work because old timing behavior often looks arbitrary. The odd delay may protect a
slow peripheral. The retry order may match a field procedure. The release window may exist because customers upgrade
components in a particular sequence. A timeout may be less about patience and more about which state the product enters
after uncertainty.

Before changing a timeout, fallback, ordering rule, retry, migration, upgrade path, or release sequence, ask what time
means in that place. Is this elapsed runtime time, wall-clock time, ordering, freshness, compatibility, or support
guidance? What happens after reboot? What happens when old and new versions coexist? Which field procedure depends on
the sequence?

Dependencies are broader than imports.

`LAW-007` matters intensely in legacy systems because many dependencies have stopped looking technical. A library
version, firmware quirk, backend tolerance, release script, build job, service tool, lab fixture, support habit,
customer deployment sequence, and retired engineer's memory can all constrain change. They are dependencies because
they import behavior, replacement cost, coordination cost, and risk.

Platform Leakage (`SMELL-005`) often appears during this reading. The product may depend on details that were supposed
to stay behind the platform: driver timing, operating-system ordering, vendor error codes, build-machine paths, storage
layout, or backend retry behavior. Chapter 32 only asks you to notice that leakage when it affects the first change.
Later chapters can teach how to unwind specific structures.

Global Configuration (`ANTIPATTERN-003`) is another common discovery target. A global flag may look like convenience,
but in a legacy system it can hide ownership, product variants, field exceptions, and temporal assumptions. Do not
delete or localize it before you know which promise it carries.

Temporary Solution (`ANTIPATTERN-006`) requires equal humility.

Many temporary solutions are genuinely temporary and overdue for removal. Others became load-bearing because a product
promise formed around them. The point of reading is not to defend every old workaround. It is to discover which
workarounds are defects, which are compatibility behavior, and which are records of a real constraint the system no
longer documents.

Use evidence before confidence.

`LAW-005` is not a slogan for distrusting everyone. It is a way to keep old systems fair. Senior memory is evidence,
but it is fragile evidence. A passing test is evidence, but only for the path and conditions it covers. A log is
evidence only if it records the fact you need. An ADR is evidence of a decision, but not proof that the system still
matches the decision. A release note can be evidence of a promise. A support article can be evidence of operational
behavior. An incident can be evidence of what broke, what was misunderstood, or what could not be observed.

The reading map should compare these sources instead of letting one dominate.

Look at code, tests, logs, runtime behavior, old ADRs (`ARTIFACT-001`), Decision Journal entries (`ARTIFACT-003`),
Mistake Ledger entries (`ARTIFACT-004`), Event Catalog records (`ARTIFACT-005`), Architecture Ledger notes
(`ARTIFACT-006`), release notes, support tickets, service-tool behavior, field procedures, and senior memory. Each
source has a different failure mode. The useful question is not, "Which source is authoritative?" The useful question
is, "What claim does this source support, and where does it stop?"

Stale records are not useless.

A stale diagram can tell you what the system used to promise. An old ADR can explain a decision that later drifted. A
release note can reveal a promise nobody put into code comments. A support article can show how users actually recover.
A Mistake Ledger entry can explain why a path became cautious. The danger is treating stale records as current truth
without comparing them to runtime behavior and current dependents.

Discoverability (`METRIC-003`) is one of the first risks legacy reading measures.

Can an engineer find the owner of the state? Can they find the record explaining the fallback? Can they find who depends
on a diagnostic string? Can they find the test that characterizes the behavior? Can they find the release path? Can
they find the reason a timeout exists? If not, the system may be working, but it is expensive to change responsibly.

Bus Factor (`METRIC-002`) is the companion risk.

When the only explanation lives in one person's memory, the system has evidence, but not durable evidence. The answer
is not to ignore that person. The answer is to interview them as part of reading, compare their memory with other
sources, and repair the record enough that the next engineer does not need the same conversation to make a safe change.

Estimate Change Radius before editing.

Change Radius (`VOCAB-001` and `METRIC-001`) is not just the number of files you expect to touch. In legacy work, the
radius includes direct code changes, indirect dependents, latent product promises, support paths, release sequences,
diagnostic consumers, data migration, field procedures, and unknowns. A small diff can have a large Change Radius when
the behavior is observable at a trusted boundary.

The estimate will be imperfect. That is fine. The purpose is to decide how cautiously to probe.

A safe probe is the smallest change or observation that improves your model without spending the system's trust.

Sometimes the safe probe is a characterization test around current behavior. Sometimes it is an added diagnostic field
that does not change existing output. Sometimes it is a read-only trace in a staging environment. Sometimes it is a
small record repair: linking an old ADR to a release note, adding an Architecture Ledger note, or recording an
assumption in the Decision Journal. Sometimes it is a limited runtime experiment with a clear rollback. Sometimes it is
verification that a supposed dependent no longer exists.

The probe should answer a question the reading map has exposed.

Does this diagnostic string have consumers? Does this fallback protect a field workflow? Does this state have one
owner? Does this old ADR still describe the runtime behavior? Does this timeout decide state or merely wait? Does this
backend tolerance represent compatibility? Does support rely on the release sequence? Does the log distinguish the
failure modes the change could create?

Characterization tests are especially useful when the current behavior is messy but relied on.

A characterization test does not declare the behavior elegant. It records what the system currently does at a boundary
that matters. That record can protect a legacy promise while the team decides whether to preserve, revise, or remove it
later. The test is not the modernization. It is evidence for the next responsible step.

Record assumptions as you learn.

Legacy reading that lives only in a meeting recreates the same problem it found. Use existing records. If the finding
explains why a decision exists or why it should not be changed yet, update the Decision Journal or ADR. If it repairs
knowledge about a subsystem boundary, update the Architecture Ledger. If it clarifies event meaning or diagnostic
consumers, update the Event Catalog. If it captures a past mistake that explains present caution, link the Mistake
Ledger. The chapter does not need a new artifact. It needs the old system to become readable through records the team
already recognizes.

An Architecture Health Review (`RITUAL-004`) may be one place where legacy reading starts or hands off. Chapter 31 owns
that ritual. Chapter 32 uses the handoff: health reviews can reveal stale records, unknown ownership, low
discoverability, and fragile memory. The first legacy chapter turns those signals into a reading practice for the next
change.

Chapter 32 also points forward without taking over the rest of Part VI.

Reading may reveal Silent Coupling (`SMELL-001`). Chapter 33 teaches the focused practice of finding it. Reading may
reveal utility pull, configuration flags, and deletion candidates. Chapters 34, 35, 36, and 37 own those deeper moves.
Here, the task is simpler and earlier: build enough understanding to choose the first responsible probe.

The legacy system is not guilty because it is old.

It is dangerous only when its promises are invisible, its evidence is stale, and its first change is made before anyone
knows what the system is still protecting.

## Engineering Principle

Read legacy code as a system of promises before you read it as a pile of defects. Start with behavior, owners, state,
boundaries, dependencies, evidence, and Change Radius; then choose the smallest safe probe that can improve your model.

Use this principle as a reading sequence:

1. Name the requested change.
2. Name the visible product promise that must keep working.
3. Name any suspected hidden promise.
4. Identify state writers, readers, interpreters, and owners.
5. Identify boundaries that may have API, diagnostic, timing, or compatibility promises.
6. Identify dependencies beyond imports: tools, scripts, firmware, backend behavior, release paths, support, and people.
7. Identify time, ordering, retry, timeout, upgrade, and field-procedure assumptions.
8. Compare evidence from code, tests, logs, runtime behavior, records, release notes, support, incidents, and memory.
9. Mark stale or missing records.
10. Estimate likely Change Radius, including unknowns.
11. Choose the smallest safe probe.
12. Update the record that would have helped you start.

The goal is not full certainty before action. The goal is to make the first action proportionate to what the system can
currently prove.

## Architecture Exercise

### Build a Reading Map Before the First Change

Choose one legacy subsystem and one requested change. Prefer a change that sounds small: remove a fallback, adjust a
timeout, simplify a configuration flag, add a compatibility behavior, rename a diagnostic, change an upgrade sequence,
or support a new hardware or customer variant.

Write short answers to these prompts:

1. What exact change has been requested?
2. What visible product promise must continue to hold?
3. What hidden promise might exist?
4. Which state is involved?
5. Who writes that state?
6. Who reads it?
7. Who interprets it as truth?
8. Who appears to own it?
9. Which boundary or API could observe the change?
10. Which diagnostic string, status, error, screen, or service-tool behavior might be a promise?
11. Which dependency could be affected: library, firmware quirk, backend behavior, script, tool, procedure, release path,
    or person?
12. Which time, ordering, retry, timeout, upgrade, or field-procedure assumption might matter?
13. Which tests describe current behavior?
14. Which logs or events expose the behavior?
15. Which ADR, Decision Journal, Mistake Ledger, Event Catalog, or Architecture Ledger entry explains it?
16. Which release notes, support articles, tickets, incidents, or senior memories are evidence?
17. Which records are stale, missing, contradictory, or too hard to find?
18. What is the likely Change Radius?
19. Which part of the radius is unknown?
20. What is the smallest safe probe that would improve the model?
21. What characterization test, diagnostic observation, read-only trace, or record repair should happen before editing?
22. Which existing record should be updated after the probe?
23. What could go wrong if you edit first?

End with five statements:

1. One promise the subsystem keeps is ______.
2. One hidden assumption to verify is ______.
3. One evidence source is ______.
4. One safe probe is ______.
5. One record to update is ______.

Do not create a new canonical artifact for this exercise. Use the records the system already has.

## Principal's Notebook

- Old code often protects current promises.
- Senior memory is evidence, not storage.
- The first safe change is often a better map.

## ADR

### Chapter ADR: Map Legacy Compatibility Behavior Before Removing the Fallback

### Context

The controller has a legacy startup fallback for a replaceable peripheral module. The fallback waits once more when the
module reports a transitional readiness state after the first startup timeout. The behavior was added years ago and is
now poorly documented.

A new hardware variant needs compatibility behavior in the same area. The proposed cleanup would remove or rewrite the
fallback while adjusting the timeout path. The current diagram does not show the fallback. The original ADR explains the
clean module-registration design, but not the later compatibility behavior. Existing tests cover normal startup and
clear failure, not the transitional fallback path.

Several possible dependents exist. The service tool may parse the diagnostic string emitted by the fallback. The
backend API may treat the transitional firmware response as compatible behavior. Release notes and support procedures
may tell technicians to wait for that state before power cycling a site. No current record explains whether the
fallback is dead code, a field workaround, or a product promise.

### Decision

Do not remove or rewrite the fallback yet.

Create a reading map for the compatibility behavior before making the code change. The map will identify the visible
product promise, suspected hidden promise, state owner, boundary behavior, diagnostic consumer, backend interpretation,
firmware dependency, service-tool dependency, release sequence, support procedure, and time or ordering assumptions.

Compare evidence from code, happy-path tests, runtime logs, the old ADR, release notes, support articles, backend
mapping behavior, service-tool behavior, incident history, and senior memory. Treat senior memory as useful evidence but
not as the final record.

Add a small safe probe before editing the fallback. The first probe is a characterization test for the current
transitional startup behavior: when the module reports the transitional readiness state after the first timeout, the
controller waits once more, preserves the diagnostic behavior consumed by tools, and reports compatibility status the
backend accepts. Add diagnostic context only where it improves cause distinction without changing existing diagnostic
promises.

Keep the probe scoped to the transitional readiness path. It should not turn all slow starts into successful
compatibility cases or make one hardware variant's startup tolerance a global timing rule.

Update the Decision Journal or Architecture Ledger with the active assumption, evidence links, likely Change Radius,
and the condition that would allow later removal. Revisit fallback removal only after the legacy promise and Change
Radius are known.

### Consequences

The team avoids turning an apparently small cleanup into an accidental product break. The fallback becomes explainable:
either a promise to preserve, behavior to revise, or dead code to remove later with evidence. The new hardware variant
can receive a narrower compatibility change because the existing promise is visible.

This adds a short discovery step before the requested change. It may reveal that more consumers depend on the behavior
than expected. It may delay deletion. It may require updating records that were previously stale. It may also show that
the fallback is no longer needed, but that conclusion will rest on evidence rather than hope.

### Alternatives Considered

Remove the fallback immediately. This reduces code but risks breaking service tooling, backend compatibility, release
expectations, or field recovery behavior that the current records do not expose.

Increase the timeout and keep the fallback unchanged. This may preserve behavior, but it can hide the distinction
between slow startup, failed startup, backend delay, and support action.

Rename diagnostics while cleaning the path. This may improve readability for engineers, but diagnostic text may already
be part of a service-tool or support promise.

Rely on the original ADR. The ADR is valuable historical evidence, but it predates the fallback and does not describe
current runtime behavior.

Trust the senior engineer's memory. The memory is useful and should be captured, but it creates Bus Factor risk until
it is compared with evidence and recorded.

Modernize the whole integration first. That may become appropriate later, but the current need is a safe first change,
not a broad modernization plan.

## Editor's Commentary

Chapter 32 opens Part VI by changing the reader's posture toward legacy work.

Parts I through V taught better questions, laws, decision records, product obligations, team alignment, and architecture
health. This chapter uses those ideas as reading lenses. It does not repeat their playbooks. It asks the reader to apply
them before touching an old subsystem whose promises are not fully visible.

The chapter deliberately starts with a working legacy integration rather than a broken system. That matters. Legacy risk
often hides in successful behavior whose explanation has drifted out of code, records, and team memory. The system may
still be serving customers while becoming hard to change responsibly.

The PEAK concepts carrying the chapter are Every State Has One Owner (`LAW-001`), Every API Is a Promise (`LAW-002`),
Time Is a Dependency (`LAW-003`), Evidence Before Confidence (`LAW-005`), Every Dependency Is a Decision (`LAW-007`),
Change Radius (`VOCAB-001` and `METRIC-001`), Bus Factor (`METRIC-002`), Discoverability (`METRIC-003`), API Stability
(`METRIC-004`), ADR (`ARTIFACT-001`), Decision Journal (`ARTIFACT-003`), Mistake Ledger (`ARTIFACT-004`), Event Catalog
(`ARTIFACT-005`), Architecture Ledger (`ARTIFACT-006`), Architecture Health Review (`RITUAL-004`), Hidden State
(`SMELL-004`), Platform Leakage (`SMELL-005`), Global Configuration (`ANTIPATTERN-003`), Temporary Solution
(`ANTIPATTERN-006`), One Lost Packet (`FAILURE-002`), The Hero Engineer (`FAILURE-004`), and The Release We Should Have
Delayed (`FAILURE-005`). Silent Coupling (`SMELL-001`) is present as something reading may reveal, but Chapter 33 owns
the focused practice of finding it.

The chapter avoids creating a new PEAK artifact. The reading map is a chapter-local practice, not a canonical record.
Its output should repair existing records: ADRs, Decision Journal entries, Mistake Ledger links, Event Catalog entries,
and Architecture Ledger notes.

Later Part VI chapters own the deeper work this reading may uncover: Silent Coupling, Utility Gravity, Boolean
Explosion, Deleting Safely, and Refactoring Without Losing Product Trust. Chapter 32's job is earlier and narrower:
build enough understanding to choose the first safe probe.

The reader-facing move is simple: before asking how to fix the legacy system, ask what promise the system is still
keeping.
