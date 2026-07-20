# Architecture Health Reviews

## Opening Quote

> Architecture health is tested by the next change the system must carry.

## Story

### The Architecture That Looked Fine Until Every Change Was Expensive

The provisioning system looked healthy from far away.

The product had shipped four releases in a year. Incidents were low. Features still moved. Dashboards stayed green.
Support no longer escalated every provisioning case to engineering. Manufacturing knew the station flow. Firmware knew
the device states. Backend knew reservation and entitlement. Service tooling knew which screens technicians used in the
field.

The architecture had become familiar enough that people stopped seeing it.

Mara noticed the pattern because she was no longer being asked hard questions. She was being asked small questions that
should have been easy.

"Who owns this provisioning field now?"

"Can the service tool still treat backend reservation as readiness?"

"Do we still support the old compatibility layer?"

"Which upgrade path did Sam validate last release?"

"Why do we keep rejecting the same event-shape option in review?"

Each question was reasonable. None was an incident. Together they made the work feel heavier than the architecture
looked.

A firmware change that should have been local touched backend status mapping, service-tool labels, manufacturing
station output, release notes, and support language. The Change Radius was too large for the size of the change. No one
could name a single owner for the configuration field that moved through all of those surfaces. Manufacturing wrote it.
Firmware read it. Backend copied it into a provisioning summary. Support saw it in diagnostics. Release treated it as
part of the compatibility matrix.

The service-tool team found an undocumented API assumption. The old screen still treated a successful package write as
proof that a device was ready. That had been true enough before the newer backend reservation flow. It was no longer
true. The API promise had drifted, but the records had not.

The temporary compatibility layer had become permanent by silence. It was added for one upgrade window after the old
provisioning path was replaced. Two releases later, the adapter still existed. Its owner had changed teams. Its tests
passed because nobody wanted to break older devices accidentally. The expiration condition lived in memory, and memory
had started to disagree with itself.

Upgrade paths depended on Sam.

Sam was generous, patient, and tired. He knew which old firmware version could cross directly to the new package shape.
He knew which field units needed the intermediate service-tool version. He knew why one gateway model required a manual
step after recovery. He also knew the release where the team had almost removed the compatibility layer and decided not
to. The Architecture Ledger linked the old ADR, but the row still said "review after first field upgrade window." That
window had closed months ago.

Design reviews repeated the same rejected options. A backend engineer proposed combining reservation and readiness into
one status because the API would be easier. A service-tool engineer suggested using the station-written flag as the
operator source of truth. A firmware engineer suggested keeping both provisioning paths until "customers stop using the
old one." Each idea had been considered before. Each had been rejected for a reason. The reasons existed somewhere in
RFC comments, ADR consequences, and release notes, but not in a place people found before proposing them again.

The Event Catalog had drifted from support language. The system emitted `package_written`, `reservation_expired`,
`device_rejected`, and `accepted`. Support articles spoke about "provisioned," "failed provisioning," and "retry
needed." Technicians used a fourth vocabulary in service-tool notes. The Event Catalog existed, but it no longer kept
the product language, diagnostic language, and engineering language aligned.

Recovery logic had a Bus Factor problem. Sam and one firmware engineer understood the difference between package retry,
backend reservation retry, and device acceptance retry. The test suite covered the happy paths and a few field escapes,
but the reasoning behind the retry boundaries was still easier to get from people than from records.

Teams avoided one boundary. The product team wanted a small variant for a regional customer: one extra provisioning
constraint, one additional support warning, one manufacturing station option. Nobody said no. They said, "Let's wait
until after the release." The request was not dangerous by itself. The avoidance was the signal. Teams were routing
around the architecture because they no longer trusted the boundary to absorb a routine product change.

New engineers copied an old pattern without knowing why. A new backend engineer found an old compatibility adapter and
used it as the model for another variant. The code review caught the problem. The review comment said, "This path was
temporary." The engineer asked the obvious question:

"Temporary until what?"

No one answered quickly.

In the next leadership meeting, the product director looked at the incident chart and asked why architecture kept
coming up.

"Are we overreacting?" she asked. "The system is working."

Mara did not argue with the chart. The chart was true. The system was working.

She wrote one sentence on the whiteboard:

> Working today is not the same as healthy enough for the next necessary change.

Then she wrote the question underneath it:

> What evidence tells us whether this architecture can still carry the changes, failures, product obligations, and team
> boundaries we need it to carry?

That became the beginning of the architecture health review.

Mara did not invite every manager. She did not create a score. She did not ask senior engineers to rank the architecture
from red to green. She scoped the review to one product boundary: provisioning from manufacturing station through
backend reservation, device acceptance, service tooling, release upgrade, and support diagnosis.

The review had one purpose: decide whether the provisioning boundary was still healthy enough to support upcoming
change, and what the team would do about the evidence.

They started with recent changes.

The last three "small" provisioning changes had broad Change Radius. One label change touched firmware, backend,
service tooling, support, tests, and release notes. One regional variant required a manual station exception. One
upgrade fix required Sam to reconstruct the old compatibility promise. The team did not turn those examples into a
velocity complaint. They wrote down the evidence: small change, affected surfaces, owners, records touched, evidence
missing, and whether the same issue had appeared before.

Then they looked at ownership.

The configuration field had no single visible owner. Manufacturing owned the write. Firmware owned interpretation after
device read. Backend owned the summary API. Support owned customer-safe wording. Release owned the supported
combination. That was not automatically wrong. The unhealthy part was that no record explained the ownership split, so
every change rediscovered it.

They looked at API promises.

Backend reservation did not mean device readiness. The service tool still displayed a flow that implied it did. The
API was not broken, but the promise around it had drifted. The ADR recorded the newer boundary. The support article and
tool labels still taught the older one.

They looked at dependencies.

The compatibility layer depended on an old firmware behavior, one service-tool version, station package shape, and a
release note that customers rarely read. It was not just code. It was a dependency chain with product obligations at
the end.

They looked at records.

The accepted ADR was still useful. The RFC held old alternatives, but the rejected options were hard to find. The
Decision Journal had a release exception entry with no follow-up. The Architecture Ledger row was open past its review
trigger. The Event Catalog did not match support language. The Mistake Ledger had two field diagnosis failures, but
the lesson had not been connected back to provisioning. The Weak Signal Register had one entry: new engineers keep
copying the old adapter.

They looked at people.

Sam was not the owner of the architecture, but the upgrade path depended on him as if he were. That was the quiet form
of the Hero Engineer failure. No one was trying to be indispensable. The records had made him necessary.

The first instinct in the room was to fix everything.

That would have turned the health review into a refactoring program, and the team would have lost the point. Mara kept
pulling the discussion back to decisions.

"What do we keep?"

They kept device-owned final acceptance. The evidence still supported it. Field failures were easier to diagnose when
the device made the final acceptance decision locally and reported stable outcomes.

"What do we repair?"

They repaired the ownership record for the configuration field. Manufacturing would own writing and station evidence.
Firmware would own device interpretation. Backend would own summary wording. Support would own customer-safe language.
Release would own the supported matrix. The Architecture Ledger would show the split.

"What do we retire?"

They retired one unused compatibility option. No field unit had used it for two releases, and keeping it made the
service-tool flow harder to explain. The ADR would be updated with the removal decision and evidence.

"What do we review?"

They sent the service-tool readiness wording through Architecture Review because it crossed backend, firmware, support,
and release promises. The question was not whether the screen looked good. The question was what promise the screen
made to a technician.

"What do we freeze?"

They froze the release-critical acceptance-state names through the next validation window. Not the whole design. Not
every provisioning detail. Only the named product states whose meaning support, service tooling, tests, and release
needed to trust.

"What do we investigate?"

They investigated Event Catalog drift. The team did not yet know whether the event names were wrong, the support
language was wrong, or the mapping was missing. The Weak Signal Register got an owner and a date.

"What do we document?"

They documented the upgrade path that had lived in Sam's memory. Sam helped, but he did not become the owner of the
record. The release owner owned the supported upgrade matrix. Firmware and service tooling owned their pieces.

"What risk do we accept?"

They accepted one temporary support workaround for older field units for one more release. It got an owner, evidence,
expiry condition, and review trigger. It did not get to stay because nobody wanted to touch it.

The review ended with fewer items than it began with.

That was a feature.

The Architecture Ledger gained one updated row for the provisioning boundary: current owner split, health notes,
decisions made, records to update, open weak signals, review date, and next trigger. The ADR gained a short update for
retiring the unused compatibility option. The RFC was linked as proposal history, with repeated rejected options pulled
into the ADR consequences. The Decision Journal captured the temporary support workaround and the service-tool review
trigger. The Mistake Ledger linked the field diagnosis failures to the Event Catalog drift. The Event Catalog owner got
a concrete mapping task. The Weak Signal Register tracked new-engineer pattern copying and repeated rejected options.

No one left with a health score.

They left with decisions.

Two months later, the regional variant arrived again. This time the conversation was different. Firmware could name the
state owner. Backend could say which API promise would change. Service tooling could say which technician wording was
stable. Support could find the Event Catalog mapping. Release could see whether the compatibility exception still
applied. Sam still had useful history, but the work did not depend on his memory.

The architecture had not become perfect.

It had become visible enough to review again.

## Discussion

Architecture health is the system's present ability to absorb necessary change without losing ownership, promises,
evidence, recovery paths, or trust.

That definition is deliberately practical. It does not ask whether the architecture is elegant. It does not ask whether
the diagram is current. It does not ask whether dashboards are green. Those things may matter, but they are not enough.
A system can be stable today and still be too fragile, unclear, or privately remembered to carry the next necessary
change.

Architecture health reviews exist for that gap.

An architecture health review is a repeated, evidence-based review of whether the architecture still supports necessary
change. The word "repeated" matters because health decays between decisions. The word "evidence" matters because taste
is not enough. The word "change" matters because architecture is not tested by stillness. It is tested by new
obligations: a product variant, a field failure, an upgrade path, a support promise, a manufacturing change, a
dependency replacement, a recovery case, or a team boundary shift.

The most common mistake is to confuse architecture health with operational calm.

Operational dashboards answer different questions. Are requests succeeding? Are devices reporting? Are incidents open?
Are latency and error rates inside expected ranges? These are important questions. They do not tell you whether a small
future change will require six teams, whether an API promise has drifted from support language, whether a compatibility
layer lost its expiration condition, or whether one engineer is carrying the upgrade path in memory.

Green dashboards can hide red architecture.

The opposite error is to treat architecture health as a scorecard. A score can be useful as a pointer, but it is a poor
substitute for judgment. If the review ends with "provisioning is yellow," the organization still has not decided what
to keep, repair, retire, review, freeze, investigate, document, or accept as risk. Architecture Health as a metric
warns against reducing the system to one number. The useful question is what evidence the organization has and what
decision that evidence now requires.

That is why architecture health reviews must be scoped.

"Review the architecture" is too broad to be useful. "Review the provisioning boundary before the next variant and
upgrade window" is a real review. A boundary gives the team something to inspect: owners, APIs, dependencies, records,
events, support language, release obligations, temporary solutions, recovery paths, and people. Scope keeps the review
from becoming an architecture board meeting where everyone reports the state of everything.

Architecture health review is not Architecture Review.

Architecture Review looks at a consequential design before it hardens. It asks whether the proposal, constraints,
alternatives, risks, evidence, and decision are ready enough to proceed. Architecture health review looks at an
architecture already in use. It asks whether the architecture remains fit for upcoming and ongoing change. The first is
often about a proposal. The second is about accumulated reality.

Architecture health review is not Architecture Freeze.

Architecture Freeze stabilizes named decisions during validation, release hardening, or another high-risk window. A
health review may produce a freeze decision for one set of names, promises, or behaviors, as the story did with
acceptance-state names. But the review itself is not a freeze. It can also produce repair, retirement, investigation,
documentation, or accepted risk.

Architecture health review is not an incident review.

Incidents deserve incident response and learning. A health review may use repeated incidents or field diagnosis failures
as evidence, but it is not trying to assign root cause for one event. It is asking whether the architecture around the
boundary still supports the work the organization now needs.

It is also not a retrospective, status meeting, compliance audit, security review, performance review, maturity model,
or code-quality dashboard review. Those practices may expose useful evidence. They do not replace the architectural
judgment: can this system still carry necessary change without losing ownership, promises, evidence, recovery paths, or
trust?

Evidence for architecture health often appears first as friction.

High Change Radius is one signal. When a small change touches many modules, teams, tests, release notes, diagnostic
phrases, and support procedures, the system is telling you something. Broad Change Radius is not always bad. Some
product changes are genuinely broad. The health signal appears when the radius is surprising, repeated, or poorly
owned.

Ownership drift is another signal. Every State Has One Owner is easy to say and hard to preserve as systems evolve. A
configuration field that is written by manufacturing, interpreted by firmware, summarized by backend, displayed by
service tooling, and explained by support may be legitimate. It becomes unhealthy when no record names the ownership
split and every change has to rediscover it.

API promise drift is a signal. Every API Is a Promise means the promise includes the meanings other teams act on. If
backend reservation no longer means device readiness, service tooling and support language must stop teaching that it
does. API Stability is not only whether the endpoint still responds. It is whether the promise remains discoverable,
compatible, and true for its consumers.

Dependency drift is a signal. Every Dependency Is a Decision applies to compatibility layers, station scripts,
service-tool versions, support procedures, field workflows, release gates, and people. A dependency becomes unhealthy
when the organization no longer knows who owns it, why it remains, what would replace it, or what failure it imports.

Unused flexibility and temporary solutions are signals. Flexibility that no longer has a user still creates test cost,
branching cost, support ambiguity, and review confusion. A temporary solution without an owner, expiry condition, and
review trigger is not temporary. It is a permanent obligation the organization has stopped admitting.

Discoverability is a signal. Can an engineer move from behavior to owner, decision, record, and promise? Can support
find the event meaning? Can release find the supported upgrade matrix? Can a new engineer find why an old pattern should
not be copied? If the answer is "ask Sam" or "ask Mara," the architecture has a Bus Factor problem even while the code
continues to run.

Smells show up as health evidence too. Silent Coupling appears when backend, service tooling, and support each trust a
different meaning for the same provisioning state. Hidden State appears when a configuration field affects behavior
without visible ownership. Platform Leakage appears when a product boundary forces teams to understand platform detail
that should be contained. Event Explosion appears when events multiply or drift until support, diagnostics, and
engineering no longer speak the same language. Global Configuration appears when configuration is shared broadly but
owned nowhere.

Weak signals deserve a place in the review because architecture often fails socially before it fails operationally.
Repeated rejected options, new engineers copying obsolete patterns, review questions that return every month, teams
avoiding one boundary, and support phrases that do not match system behavior are not proof by themselves. They are
signals worth investigating before they harden into failures.

The review should connect every signal to a decision or investigation.

That discipline prevents two failure modes. The first is the complaint list: everyone names pain, the list grows, and
nothing changes. The second is the refactoring reflex: every pain becomes a project before the team understands the
decision. A health review is useful when it says: keep this decision because evidence still supports it; repair this
record because ownership is unclear; retire this option because it no longer has users; review this design because the
promise crosses owners; freeze this behavior during validation; investigate this weak signal; document this upgrade
path; accept this risk for one release with owner and trigger.

Artifact updates are memory repair.

An ADR records decisions kept, repaired, retired, or revisited. An RFC preserves proposal memory and repeated rejected
options. A Decision Journal captures smaller follow-up decisions and review triggers. A Mistake Ledger connects
repeated failures to changed thinking. An Event Catalog keeps system events, diagnostic meanings, and support language
from drifting apart. An Architecture Ledger keeps active ownership, status, health notes, and review dates visible. A
Weak Signal Register holds early evidence that should not yet become a decision.

The point is not to update artifacts for their own sake. The point is that architecture memory either lives in records
or in people. When it lives only in people, the system quietly recreates the Hero Engineer failure.

Cadence helps only after purpose is clear.

A quarterly review may be useful for the provisioning boundary because release windows, field feedback, support cases,
and product variants create enough evidence each quarter. That does not mean every architecture needs a quarterly
meeting. Cadence without evidence becomes status. Evidence without decisions becomes theater. Decisions without owners
become wishes. Owners without revisit triggers become permanent drift.

This is the Part V closure.

Technical leadership without authority helps the Principal Engineer convene the right owners without taking their work
away. Design reviews as shared memory provide review evidence. Engineering rituals provide repeatable triggers and
outputs. Mentoring through artifacts reduces private interpretation. Aligning teams around decisions makes obligations
visible. Architecture health review asks whether all of that memory and ownership still lets the system support the
next necessary change.

The next part of the book will begin with legacy systems. Chapter 31 stops before that. It only names the bridge:
unhealthy architecture is often not a dramatic collapse. It is architecture whose intent, ownership, promises, and
change paths are no longer easy to recover. If the organization does not review health while the system still works, a
future engineer will inherit the same facts as legacy mystery.

## Engineering Principle

Review architecture health by asking what the system can still carry. Use evidence from change, ownership, promises,
support, releases, records, and people to decide what to keep, repair, retire, review, freeze, investigate, document, or
accept as risk.

Use this principle when a system appears stable but changes are becoming expensive, ownership is drifting, records are
stale, or important behavior depends on private memory.

Ask:

1. What small change recently had large Change Radius?
2. Which state or API promise lacks a visible owner?
3. Which dependency is harder to replace or understand than expected?
4. Which temporary solution outlived its trigger?
5. Which release, upgrade, recovery, or support issue repeated?
6. Which rejected option keeps returning?
7. Which boundary do teams avoid?
8. Which record is stale, missing, or misleading?
9. Where is Bus Factor rising?
10. Which weak signal deserves investigation?
11. What decision must be made after the review?
12. What will we revisit next?

The goal is not an architecture score. The goal is a better next decision.

## Architecture Exercise

### Run One Architecture Health Check

Choose one subsystem or product boundary. Prefer an area that appears stable but has started to make small changes feel
surprisingly expensive.

Do not create a new canonical artifact. Update the existing ADR, RFC, Decision Journal entry, Mistake Ledger entry,
Event Catalog entry, Architecture Ledger row, Weak Signal Register entry, test record, support note, or release note
that already carries the relevant memory.

Document:

- a recent change that was harder than expected;
- affected owners;
- one state ownership issue;
- one API or compatibility promise;
- one dependency concern;
- evidence from support, release, field, validation, or reviews;
- one stale or missing record;
- one temporary solution or workaround;
- one Bus Factor risk;
- one weak signal;
- the decision to make next;
- the follow-up owner;
- the artifact to update;
- the revisit trigger.

Then choose the smallest useful action. Keep a decision that still has evidence. Repair one owner record. Retire one
obsolete option. Send one cross-boundary promise through Architecture Review. Freeze one named behavior during
validation. Investigate one weak signal. Document one path that currently lives in memory. Accept one risk with an
owner and trigger.

End with:

1. one health signal;
2. one decision;
3. one owner;
4. one artifact update;
5. one revisit trigger.

## Principal's Notebook

- Green dashboards can hide red architecture.
- Health shows up in the next change.
- No decision means no review happened.

## ADR

### Establish a Quarterly Architecture Health Review for the Provisioning Boundary

#### Status

Accepted for the team in the story.

#### Context

The cross-team provisioning boundary appears stable. Incidents are low, dashboards are green, and the product has
completed several releases. Under that visible calm, changes are becoming more expensive. Ownership of a provisioning
configuration field has drifted across manufacturing, firmware, backend, support, and release. Service-tool behavior
depends on an undocumented API assumption. Release upgrade paths depend on one engineer's memory. The temporary
compatibility layer has outlived its original trigger. Design reviews repeat rejected options. Architecture Ledger
items remain open after their review date. Event Catalog names no longer match support language. Bus Factor risk is
rising around recovery and upgrade behavior.

Leadership lacks visible evidence because the system is working. The organization needs a lightweight way to inspect
whether the provisioning architecture still supports upcoming product variants, upgrade windows, support obligations,
release validation, and team ownership.

#### Decision

Run a quarterly architecture health review focused on the provisioning boundary.

The review will inspect evidence from:

- Change Radius of recent provisioning changes;
- support cases and field diagnosis failures;
- release, upgrade, recovery, and compatibility exceptions;
- design reviews and repeated rejected options;
- Architecture Ledger status and stale review triggers;
- ADR and RFC age, accuracy, and discoverability;
- Decision Journal follow-ups;
- Mistake Ledger patterns;
- Event Catalog drift from support and service-tool language;
- Bus Factor risk around upgrade and recovery paths;
- weak signals from new-engineer learning, support, reviews, release validation, and field feedback.

The review will produce explicit decisions: keep, repair, retire, review, freeze, investigate, document, or accept risk.
Each decision must name an owner, artifact update, and revisit trigger. The review will update existing records rather
than create a new canonical artifact. It will stay scoped to the provisioning boundary and will not become a broad
architecture board meeting.

The review avoids blame. It judges whether the architecture can carry necessary change, not whether a team is
competent.

#### Consequences

The organization should detect architectural decay earlier. Ownership splits become visible. API promises and support
language are more likely to stay aligned. Repeated arguments can move from memory into records. Temporary compatibility
paths gain owners, evidence, expiry conditions, and review triggers. Bus Factor risk around upgrade and recovery logic
should fall as records improve. Release and support obligations become easier to inspect before they become late risk.

The organization accepts maintenance cost. The review must stay lightweight. If it produces no decisions, it should be
redesigned or retired. If it becomes a status meeting, scorecard, audit, or refactoring wish list, it has failed. If the
review only records findings without owners and revisit triggers, it has created more memory to maintain without
improving architecture health.

The review may reveal that one named behavior should enter Architecture Freeze during validation, that one proposal
needs Architecture Review before it hardens, or that one weak signal needs investigation before a decision is possible.
Those are outputs of the health review, not replacements for it.

#### Alternatives Considered

Wait until incidents rise.

This would treat operational failure as the first acceptable evidence. It ignores rising Change Radius, ownership
drift, stale records, and private memory while the system still has time to repair them.

Rely on dashboard metrics.

Dashboards are useful for operational health. They do not show whether a small change now crosses six teams, whether an
API promise has drifted, or whether upgrade knowledge lives in one engineer's head.

Hold a broad architecture board meeting.

This would increase visibility but blur ownership and scope. The provisioning boundary needs concrete decisions, not a
forum where every architecture topic competes for attention.

Start a refactoring program immediately.

This assumes the decision before reviewing the evidence. Some findings may need record repair, owner clarification,
Architecture Review, Architecture Freeze, investigation, or accepted risk rather than refactoring.

Ask senior engineers for opinions.

Expert judgment matters, but unsupported opinion would make architecture health a taste contest. The review must use
evidence and records so the organization is not dependent on private interpretation.

Run a maturity-model assessment.

This would create broad categories without necessarily producing decisions for the provisioning boundary. The team
needs owners, artifact updates, and revisit triggers.

Do nothing because the system currently works.

This preserves visible calm while hidden change cost rises. Working today is not the same as healthy enough for the
next necessary change.

## Editor's Commentary

Chapter 31 closes Part V by turning organizational memory into an operating habit. Chapter 26 showed leadership without
formal authority. Chapter 27 showed reviews as shared memory. Chapter 28 showed rituals that preserve technical
behavior. Chapter 29 showed artifacts that teach judgment. Chapter 30 showed how decisions become cross-team
obligations. Chapter 31 asks whether those decisions, records, rituals, owners, and obligations still let the
architecture support necessary change.

The chapter illustrates Architecture Health Review (`RITUAL-004`) and uses the existing Architecture Health vocabulary
and metric concepts (`VOCAB-007` and `METRIC-005`). It does not introduce a new health artifact, score, dashboard,
cadence, or maturity model. Architecture health remains the ability to support necessary change at acceptable cost, and
the review remains evidence-based.

The registered concepts are active throughout the chapter. Ownership drift applies Every State Has One Owner
(`LAW-001`). API promise drift applies Every API Is a Promise (`LAW-002`) and API Stability (`METRIC-004`). Evidence
Before Confidence (`LAW-005`) keeps the review from becoming opinion. Unused Flexibility Is Waste (`LAW-006`) and
Temporary Solution (`ANTIPATTERN-006`) explain obsolete options and compatibility paths without expiry. Every
Dependency Is a Decision (`LAW-007`) broadens the review beyond code libraries into support, release, station scripts,
service tools, and people. Change Radius (`VOCAB-001` and `METRIC-001`), Bus Factor (`METRIC-002`), Discoverability
(`METRIC-003`), and Weak Signal (`VOCAB-002`) provide evidence.

The records matter because health is partly memory. ADRs (`ARTIFACT-001`) preserve decisions kept, repaired, retired,
or revisited. RFCs (`ARTIFACT-002`) preserve proposal history and repeated rejected options. Decision Journal entries
(`ARTIFACT-003`) preserve smaller follow-ups. Mistake Ledger entries (`ARTIFACT-004`) preserve repeated failures and
changed thinking. Event Catalog entries (`ARTIFACT-005`) keep system events and support language aligned. Architecture
Ledger rows (`ARTIFACT-006`) keep active ownership, status, health notes, and review dates visible. Weak Signal
Register entries (`ARTIFACT-007`) hold early evidence until the organization knows what decision it should make.

The smells and failures are not decorative. Silent Coupling (`SMELL-001`) appears when teams act on different meanings
for the same state. Hidden State (`SMELL-004`) appears when ownership is invisible. Platform Leakage (`SMELL-005`)
appears when boundary workarounds force product teams to know platform detail they should not need. Event Explosion
(`SMELL-006`) appears when events multiply or drift away from product and support meaning. Global Configuration
(`ANTIPATTERN-003`) appears when shared configuration has no clear owner. The Hero Engineer (`FAILURE-004`) appears
when upgrade and recovery memory depends on one person. Release and Upgrade Failure (`FAILURE-005`) supplies the
pressure that makes health evidence matter before validation discovers it late.

Architecture Review (`RITUAL-001`) and Architecture Freeze (`RITUAL-002`) remain boundaries and possible outputs, not
duplicates. A health review may send one proposal to Architecture Review or freeze one named behavior during
validation, but it does not replace either practice.

The Part VI boundary is deliberate. This chapter may say that unhealthy, poorly remembered architecture becomes future
legacy work. It does not teach how to read legacy systems, recover lost intent, or lead modernization. Chapter 32 owns
that turn. Chapter 31's job is to end Part V with a practice: inspect health while the architecture still works, and
turn evidence into decisions before the next necessary change becomes unnecessarily hard.
