# Reducing Boolean Explosion

> A Boolean is cheap to add but expensive to combine.

## Story

### The Two Flags That Became Sixteen Products

The Two Flags That Became Sixteen Products began with two changes nobody wanted to call architecture.

The first flag was a compatibility mode.

A legacy controller needed to keep working with an older sensor board during a staged field upgrade. The new firmware
could speak the new startup protocol, but some customer sites would run mixed hardware for months. The team added
`legacy_sensor_mode`. When the flag was set, the controller waited longer during startup, accepted one older status
code, and reported a compatibility note to the backend.

The second flag was a customer exception.

One large customer used a service workflow that depended on a diagnostic phrase from the old controller. The service
tool had already been updated for new devices, but that customer's field technicians would not receive the tool update
until after the firmware release. The team added `customer_recovery_flow`. When the flag was set, the controller kept
the old phrase in the diagnostic stream and sent a supplemental status field for the backend.

Each change was defensible.

Each diff was small.

The compatibility mode protected mixed hardware. The customer exception protected a field workflow. The firmware tests
passed. The backend accepted the status report. The service-tool owner reviewed the diagnostic phrase. Manufacturing
said the provisioning script did not need to change because both flags were set from existing product codes. Release
validation added two cases: old sensor with compatibility mode, and customer recovery flow with the new controller.

The release shipped.

Then the flags started to combine with the rest of the product.

The next release added a compile-time option for a cost-reduced controller board. That board had a slower startup path
and reused part of the old sensor timing. The firmware team did not want to expose another product mode to the backend,
so the behavior lived behind a build option and a runtime check against `legacy_sensor_mode`.

Another release added a temporary mode for manufacturing.

Final test needed to provision devices before the backend had the full product record. The manufacturing script wrote a
short-lived flag into the device so the service tool would accept a partial configuration. The flag was supposed to be
cleared before shipment. Most of the time it was.

Support added a procedure for devices that arrived in the field with the flag still present.

Then a backend team added a tolerance around the supplemental status field. They did not own firmware flags, but they
had to interpret what came in from deployed devices. If `customer_recovery_flow` was true and the product code matched
one customer family, the backend preserved the old recovery classification. If the compatibility note also appeared,
the mapper treated the device as still upgradeable. If neither appeared, the new classification applied.

The service tool learned its own version of the rule.

For one product family, it showed the technician the old recovery instructions. For another, it showed the new guided
flow. For devices in manufacturing mode, it hid both flows because the unit was not ready for field action. For mixed
hardware, it displayed a warning that the startup delay might be expected.

The code did not look outrageous in any one repository.

Firmware had a few flags and build options. The backend had a mapper. The service tool had display rules.
Manufacturing had a provisioning script. Support had procedures. Release validation had a matrix that still fit on one
page if you used small type and did not ask too many questions.

The visible matrix was smaller than the state space.

Mara, the Principal Engineer, noticed it during review for a change that seemed unrelated. A new controller variant
needed to stop sending the old diagnostic phrase. The phrase confused a support workflow for new customers. The author
removed the phrase when `customer_recovery_flow` was false. The compatibility mode remained untouched. The manufacturing
flag remained untouched. The compile-time option remained untouched. The diff was small enough to review between
meetings.

Mara asked a simple question.

"Which products does this change affect?"

The answer came back too quickly.

"Only the new controller variant when the customer exception is off."

She wrote the known switches on the whiteboard:

- sensor protocol: old or new;
- customer recovery flow: on or off;
- controller board: standard or cost-reduced;
- manufacturing provisioning mode: present or absent.

"That is sixteen combinations before we talk about firmware version, backend mapper version, service-tool version, or
field upgrade order."

The arithmetic changed the review.

Nobody believed all sixteen combinations were supported. Nobody could say which ones were invalid. Nobody knew whether
manufacturing ever shipped a device with provisioning mode still present on the cost-reduced board. Nobody knew whether
support had field procedures for old sensors with the new service tool. Nobody knew whether release validation covered
the backend tolerance when firmware and backend versions were out of step.

The team opened the release matrix.

It had four rows.

Those four rows were not wrong. They were just not the product state space.

The first instinct was cleanup.

"We should delete the old mode."

"We should replace this with a state machine."

"We should move all of this into configuration."

"We should make the backend the source of truth."

Each idea might have a future. None of them answered the question in front of the release.

Mara drew a box and labeled it Product State, not Flag.

She asked the team to stop arguing about Booleans and start naming the product states the product actually had.

They began with the active combinations.

The old sensor compatibility mode was active at customer sites still moving through the staged upgrade. The customer
recovery flow was active for one customer family until their service-tool rollout completed. The cost-reduced board was
active for new manufacturing lots only. Manufacturing provisioning mode was supposed to be absent from shipped devices,
but support records showed three field incidents where it had remained present after rework.

The team classified combinations.

New controller, new sensor, no customer exception, no provisioning mode: valid.

New controller, old sensor, compatibility mode on, no provisioning mode: valid during migration.

Cost-reduced board with old sensor and compatibility mode: supported only for manufacturing validation, not field
deployment.

Customer recovery flow on without the customer product family: invalid.

Provisioning mode present in field reports: unsupported, but real enough to need detection and support handling.

Old sensor compatibility with the new service-tool recovery flow: unknown until contract tests proved the diagnostic
meaning.

Several rows were not product states at all. They were mechanism controls. A compile-time option changed board timing.
A runtime flag preserved a customer workflow. A provisioning marker existed for manufacturing. A backend tolerance
protected upgrade order. Treating all of them as equivalent flags had hidden the ownership problem.

They assigned owners.

The firmware platform team owned the startup mechanism. The product team owned which controller and sensor
combinations were supported in the field. The service-tool owner owned technician workflow meanings. Manufacturing
owned provisioning mode and its exit criteria. Backend owned the mapper contract. Support owned field procedures. Release
validation owned the compatibility matrix, but not the product promise behind each row.

They added evidence.

Firmware added characterization tests around the existing startup behavior before changing the diagnostic phrase.
Backend added contract tests for the status fields consumed during mixed-version upgrades. The service tool added
integration tests for the diagnostic meanings it displayed to technicians. Manufacturing added a final-test assertion
that provisioning mode had been cleared before shipment. Support tagged field records where provisioning mode appeared
outside manufacturing. Release validation added a small compatibility matrix that named valid, invalid, unsupported,
obsolete, temporary, and unknown combinations instead of treating every flag as a free axis.

They recorded the promises.

An ADR named the product modes before accepting another compatibility flag. An RFC captured the migration window for
the old sensor protocol. The Decision Journal recorded why customer recovery behavior stayed stable until the tool
rollout completed. The Architecture Ledger gained owners, consumers, evidence links, and a revisit trigger for each
policy-bearing flag. Architecture Review became the place where new cross-boundary modes had to be named before they
were added. Architecture Health Review gained a recurring question: where is the state space growing faster than the
team's ability to prove it?

The immediate code change became smaller.

They did not delete the old diagnostic phrase everywhere. They did not rewrite the startup logic. They did not create a
grand state-machine project. They changed the diagnostic phrase only for the product states whose owners and tests were
known. They left compatibility behavior stable where customers and tools still depended on it. They marked two obsolete
combinations as candidates for later removal, but they did not remove them in this release.

The work felt slower than adding one more flag.

It was faster than discovering another product in the field.

By the next release, the team had fewer combinations than the arithmetic suggested. Some combinations were invalid.
Some were unsupported and detected. Some were temporary with owners and revisit dates. Some were real product states
with tests and records. Some were unknown, which was uncomfortable, but at least no longer invisible.

The team did not celebrate a conditional cleanup.

They celebrated a smaller, visible, owned state space.

## Discussion

Boolean Explosion is uncontrolled product state growth.

It is not merely a file with too many `if` statements. Messy conditionals can be a symptom, but the danger is larger:
small local switches multiply into behavior combinations the team can no longer reason about, test, own, document, or
support.

That is why a small diff can be misleading.

Adding one flag may look like a local branch. In the product, it can create a new state. If that flag combines with a
compatibility mode, customer exception, compile-time option, service-tool behavior, backend interpretation, manufacturing
script, support procedure, or field upgrade path, the team has not added one path. It has expanded the state space.

Some switches are legitimate.

A firmware mode bit may protect old hardware during a staged upgrade. A compile-time option may distinguish board
families. A service-tool flag may protect a technician workflow. A backend tolerance may preserve compatibility while
deployed devices move through versions. A customer exception may honor a real contract. The problem is not that these
switches exist. The problem is when their combinations become product behavior without names, owners, tests, records,
or review triggers.

This is where the smell becomes architecture.

A compatibility flag can become an API promise. It may not be public. It may not appear in generated documentation. But
if customers, tools, release procedures, support workflows, manufacturing scripts, or field upgrades depend on the
behavior, then changing it changes what someone can trust. `LAW-002`, Every API Is a Promise, applies even when the
promise began as an internal switch.

Unsupported combinations are rarely obvious from code alone.

The code can tell you that two switches can be true at the same time. It may not tell you whether that combination ever
ships, whether support has seen it in the field, whether manufacturing creates it temporarily, whether backend rules
interpret it differently, or whether one customer depends on it during upgrade. Static structure shows possible paths.
Product evidence shows active paths.

Embedded and product systems make the problem sharper.

The same state can be interpreted by firmware, backend systems, service tools, manufacturing stations, support
procedures, release validation, and field upgrade workflows. Each surface may have a different version, owner, and
release cadence. Firmware may report a mode bit. The backend may translate it into fleet state. The service tool may
display it as a technician action. Manufacturing may treat it as a provisioning condition. Support may describe it as a
known recovery path. Field upgrades may temporarily combine old hardware, new firmware, old tools, and new backend
rules.

No single repository contains the whole truth.

Chapter 32 taught reading the system before changing it. Chapter 33 showed how behavior can have hidden dependents.
Chapter 34 showed how shared utilities can accumulate responsibility. Chapter 35 adds a different question: what
product states are implied by the switches we already have?

That question changes the shape of the work.

The first move is not deletion. Deletion belongs to later evidence. The first move is not a broad refactor. Refactoring
that changes trusted product behavior needs a migration plan and a trust plan. The first move is naming the state space
so the team can see what it is trying to preserve, constrain, or change.

Start by separating mechanism switches from product policy decisions.

A mechanism switch controls how something is done: use this board timing, enable this transport detail, choose this
startup protocol, compile this driver family. A product policy decision says what behavior the product promises: this
customer remains compatible, this field workflow remains valid, this variant is supported, this upgrade order is safe,
this temporary mode must not leave manufacturing.

Mechanism switches can still matter, but they need different ownership from policy-bearing flags. If a build option
silently decides which customer workflows are valid, a technical switch is carrying product policy. If a compatibility
toggle changes what the backend promises to customers, it is not just a firmware convenience. If a temporary flag
changes support behavior in the field, it is no longer temporary in the only sense that matters.

Ownership is the constraint that makes state space governable.

`LAW-001`, Every State Has One Owner, becomes very practical here. The state model needs an owner. Policy-bearing flags
need owners and reviewers. Compatibility promises need owners who can say whether a combination is valid, unsupported,
obsolete, temporary, or unknown. When nobody owns the combination, everybody treats it as dangerous and nobody can
change it safely.

The evidence is distributed.

Characterization tests show what the current system does before you change it. Contract tests show what one surface has
promised another. Integration tests show how combinations behave across firmware, backend, service tools, and release
paths. Release evidence shows what the organization actually validates. Logs and field data show what has appeared
outside the lab. Support procedures show what humans have been taught to trust. Manufacturing scripts show temporary
states that may never appear in product diagrams. Team memory can explain why a strange combination exists, but if the
only map lives in one engineer's head, the Bus Factor is part of the risk.

Use metrics as evidence lenses, not as theater.

Change Radius asks how far a flag change travels. Bus Factor asks how many people can explain a combination and its
promise. Discoverability asks whether the next reviewer can find the rule without a lucky conversation. API Stability
asks whether a switch has become part of a contract that other surfaces rely on. None of these measures gives a magic
number. They give better questions.

Hidden State often sits under Boolean Explosion.

A device may carry a provisioning marker nobody expects in the field. A service tool may cache a recovery classification
after one mode transition. A backend mapper may infer product family from a status field that firmware treats as
diagnostic detail. Global Configuration can make combinations appear everywhere and belong nowhere. Platform Leakage
can expose hardware assumptions as product choices. HAL Everywhere can scatter mode checks across places that should
not know board details. Temporary Solution can keep one release's workaround alive long after the owner has moved on.

These related smells and anti-patterns matter because Boolean Explosion is rarely isolated. But they should not distract
from the central work: name, classify, own, prove, and review the state space.

Do not turn the response into a giant checklist.

The order matters because it changes attention. Inventory switches, but do not stop at the inventory. Name product
states, but do not pretend naming is enough. Classify combinations, but do not confuse "unsupported" with "impossible."
Assign owners, but do not rely on ownership without tests and records. Add tests, but do not pretend happy-path unit
tests prove cross-boundary behavior. Record decisions, but do not use documentation as a substitute for review.

Some combinations should remain.

Some are active product promises. Some protect customers during migration. Some keep manufacturing safe. Some preserve
support confidence while tools and firmware move at different speeds. Reducing Boolean Explosion does not mean flattening
all behavior into one path. It means making the supported state space smaller than the possible state space and making
the remaining promises visible.

Some combinations should be constrained.

An invalid combination should fail early or be prevented. An unsupported combination should be detected and routed to a
clear behavior. An obsolete combination should have evidence attached before it becomes a deletion candidate. A temporary
combination should have an owner and a revisit trigger. An unknown combination should stay visible until evidence moves
it into a known category.

That is the practical reduction.

You reduce the state space first by making it explicit. Then you reduce it by refusing new hidden combinations, closing
evidence gaps, preventing invalid states, retiring unsupported paths when deletion evidence exists, and preparing
trust-preserving refactoring when product promises need migration.

The code may improve later.

It may become a state model, a compatibility matrix, a decision table, or a named mode boundary. It may lose scattered
checks. It may gain clearer APIs. It may delete old paths. But those are later moves. If the team changes structure
before it understands active combinations and promises, it risks turning uncertainty into regression.

Boolean Explosion is not solved by being clever with conditionals.

It is reduced by making product states visible enough for the team to own them.

## Engineering Principle

Treat every new switch as a product-state decision when it combines with existing modes, compatibility promises, release
paths, or customer exceptions.

Reduce the state space before changing behavior.

That principle does not mean every flag deserves a ceremony. It means a Principal Engineer notices when a local switch
changes what the product can become.

Before approving another flag, ask what it combines with. Which runtime flags, mode bits, configuration switches,
compile-time options, customer exceptions, temporary modes, and compatibility toggles already exist? Which combinations
are active in firmware, backend systems, service tools, manufacturing, support, release validation, and field upgrade
paths? Which combinations represent real product states or contractual promises?

Then separate possible from supported.

Possible combinations are what arithmetic gives you. Supported combinations are what the product is willing to own.
Active combinations are what evidence shows in code, tests, logs, manufacturing, support, release data, and the field.
Unknown combinations need evidence before the team treats them as safe.

The useful categories are plain:

- valid;
- invalid;
- unsupported;
- obsolete;
- temporary;
- unknown.

Those categories are not final truth. They are a way to make the next review honest.

A valid combination needs tests, owners, and release evidence. An invalid combination needs prevention or explicit
failure. An unsupported combination needs detection and safe handling. An obsolete combination needs evidence before
removal. A temporary combination needs an owner and revisit trigger. An unknown combination needs investigation before it
becomes the quiet reason nobody changes anything.

Finally, put a review path around growth.

If a switch changes a product promise, route it through Architecture Review. If a state-space area keeps growing, surface
it in Architecture Health Review. If a compatibility promise affects several teams, record it in an ADR, RFC, Decision
Journal entry, or Architecture Ledger row. The record should name the owner, consumers, evidence, risk, and trigger for
revisit.

The principle is not "never add flags."

The principle is: do not add invisible product states.

## Architecture Exercise

Map the Boolean State Space.

Choose one legacy area with several flags or modes. Prefer an area where firmware behavior, backend interpretation,
service tools, manufacturing scripts, support procedures, release validation, or field upgrades interact. Do not choose
an area only because the code looks messy. Choose an area where a small switch change could alter product behavior.

Use the first pass for reading, not changing.

Find the switches. Include runtime flags, mode bits, configuration switches, compile-time options, compatibility
toggles, temporary paths, product variants, and customer exceptions. For each switch, write where it is set, where it is
read, which releases or product families use it, and which team usually reviews it.

Then name the product states hidden behind the combinations.

Do not list every theoretical row if the list becomes noise. Start with active and plausible combinations. Mark each
known combination as valid, invalid, unsupported, obsolete, temporary, or unknown. If a combination is impossible only
because "we never do that," treat it as unknown until evidence proves the constraint.

Look for evidence in different places:

- characterization tests for current behavior;
- contract tests between surfaces;
- integration tests across release paths;
- release validation records;
- manufacturing scripts and station logs;
- service-tool behavior;
- support procedures and field data;
- ADRs, RFCs, Decision Journal entries, and Architecture Ledger rows;
- team memory, especially when no record exists.

The exercise ends with exactly seven outputs:

1. one switch inventory;
2. one valid-combination table;
3. one list of hidden product states;
4. one owner or reviewer assignment;
5. one evidence gap to close;
6. one test to add before behavior change;
7. one review trigger for future flags.

Do not delete flags as part of this exercise.

The goal is to make the state space visible enough that deletion, migration, or refactoring can happen later without
guessing what the product still promises.

## Principal's Notebook

- A Boolean is cheap to add but expensive to combine.
- Flags become product states when customers depend on them.
- Reduce the state space before changing behavior.

## ADR

### Name the Product Modes Before Adding Another Compatibility Flag

#### Status

Accepted for the next change in this legacy area.

#### Context

The system already has runtime flags, mode bits, compatibility toggles, customer exceptions, compile-time options, and
temporary paths around controller startup and recovery behavior.

Firmware behavior, backend interpretation, service tools, manufacturing scripts, support procedures, release validation,
and tests may depend on active combinations. Some combinations are valid. Some are invalid. Some are unsupported but
possible. Some are obsolete. Some are temporary. Some are unknown.

No current record names the product states, owners, promises, evidence, or review trigger. Adding one more compatibility
flag would multiply the state space and make later deletion or refactoring less trustworthy.

#### Decision

We will not add another compatibility flag until the active product state space is named.

We will inventory switches and where they are read. We will classify known combinations as valid, invalid, unsupported,
obsolete, temporary, or unknown. We will separate mechanism switches from product-policy decisions. We will assign
owners and reviewers for the state model and policy-bearing flags.

We will add characterization tests around current behavior before changing it. We will add contract or integration tests
around active promises that cross firmware, backend, service tools, manufacturing, support, release validation, or field
upgrade paths.

We will update the ADR, RFC, Decision Journal, or Architecture Ledger with owner, consumers, evidence, risk, and revisit
trigger. Cross-boundary state-space changes will go through Architecture Review. Recurring Boolean Explosion in this
area will be surfaced in Architecture Health Review.

Deletion and broad refactoring are deferred until compatibility and product trust can be preserved.

#### Alternatives Considered

We could add one more flag because the diff is small. That would optimize for the review in front of us while hiding the
new product state it creates.

We could preserve every historical combination forever. That would avoid immediate risk while turning old uncertainty
into permanent architecture.

We could delete obsolete-looking flags before dependent behavior is understood. That would make the code smaller before
we know which customers, tools, or release paths still trust the behavior.

We could replace all flags with a state model before naming active product states. That would make the design look
cleaner while carrying the same unknown promises into a new shape.

We could rely only on unit tests or happy-path release validation. That would miss combinations that appear across
versions, tools, manufacturing, support, and field workflows.

We could ask the senior engineer and keep the combination rules in memory. That would answer today's question while
leaving tomorrow's Bus Factor and Discoverability risk unchanged.

We could move the problem into configuration. That would make combinations easier to express without reducing the state
space the product must own.

#### Consequences

The first movement is slower. The team must read the state space before adding another compatibility path.

Product-state ownership becomes clearer. Policy-bearing flags gain owners and reviewers. Unsupported and invalid
combinations become visible instead of surprising the release. Tests and records improve around active promises.

Later deletion becomes safer because obsolete combinations have evidence. Later refactoring becomes more trustworthy
because the migration starts from named product states rather than scattered conditionals.

The decision does not clean up every branch. It makes the next branch harder to add invisibly.

## Editor's Commentary

This chapter sits after reading a legacy system, finding silent coupling, and managing utility gravity because Boolean
Explosion needs all three instincts.

The reader first needs the patience to read before changing. Then they need the habit of tracing behavior across
surfaces, not only imports. Then they need to recognize when product policy hides inside convenient shared places. Only
then can they see why a small switch may be a product-state decision rather than a small conditional.

Chapter 35 deliberately does not teach deletion. It may mark obsolete or unsupported combinations as candidates, but
Chapter 36 owns the discipline of removing behavior safely. This chapter also does not teach broad refactoring. It may
prepare a state model, compatibility matrix, or decision table, but Chapter 37 owns the work of preserving product trust
while structure changes.

The chapter's job is narrower and earlier: make the state space visible.

That visibility changes the team's posture. Instead of asking whether one more flag is easy, the team asks which product
states, promises, owners, constraints, evidence, and review paths the flag creates. Sometimes the answer is that the
flag is legitimate. Sometimes the answer is that the combination is invalid. Sometimes the answer is that the team does
not know enough yet.

That last answer is useful.

In a legacy system, knowing where the unknown combinations are is often the first honest architecture improvement.
