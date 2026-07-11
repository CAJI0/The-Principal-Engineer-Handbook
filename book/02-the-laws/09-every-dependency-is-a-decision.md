# Every Dependency Is a Decision

## Opening Quote

> A dependency is not free just because the first call compiled.

## Story

The radio decision looked like the practical one.

The product needed a new wireless module for the next controller revision. The hardware choice was already narrowing.
The first units had to reach the pilot line on a date that mattered. The team needed initialization, channel setup,
packet handling, power-state transitions, retries, diagnostics, and enough compliance behavior to make the selected
part usable without spending the whole release writing a radio stack.

The vendor provided a software kit for the radio.

It supported the selected hardware. It had example initialization code. It handled protocol details the team did not
want to rediscover. It came with a test application that had already moved packets on the evaluation board. The vendor
also had errata notes that looked painful but useful: timing around wake, a recommended retry sequence after channel
loss, and a narrow compiler version range the kit had been validated against.

Using it was not foolish.

Building the complete stack internally would have delayed the first product release and moved risk into an area where
the team had less evidence. Selecting another radio part would have reopened hardware work. Delaying the product until
every replacement risk was understood would have protected the architecture in theory while failing the product in
practice.

The firmware team made what seemed like the right compromise.

They put the vendor kit behind a thin wrapper. Product code called the wrapper. Only the radio driver directory included
the vendor headers. A short ADR said the team would use the kit for the first release and preserve the option to replace
it later. The review was brief because the boundary looked obvious.

For the first release, that was enough.

Then the dependency spread.

The vendor kit expected radio work to run from one task context. Its callbacks arrived from that context and carried
pointers to buffers owned by the kit until the callback returned. The first wrapper preserved that shape because it made
the integration simple. Product code learned to prepare buffers in the format the callback expected. A supervisory task
learned which vendor error meant "retry after wake" and which one meant "reset the radio." The logging path copied
vendor reason names because those names helped the first field reports. Manufacturing calibration scripts learned to
wait for the vendor's ready event. The service tool learned to display the same error categories because support needed
something understandable during pilot units.

The test harness followed. Unit tests mocked the wrapper but used vendor-style errors. Integration tests waited for
callback order the kit usually produced. A production fixture used the vendor diagnostic sequence because it was already
in the example application. Release engineering pinned a compiler version because the kit had only been validated there.
Firmware update planning had to keep the old radio behavior available because pilot units would not all move at once.

No one sat in a meeting and decided, "Let the vendor software kit define the product."

The product learned it anyway.

The trigger arrived with the next hardware revision. The original radio part became harder to source, and the newer
part came with a newer kit. The new kit had similar functions. It could initialize the radio, send packets, receive
callbacks, and report errors. The team still had a wrapper. The driver layer was still the only code that included the
vendor headers.

The first estimate was optimistic.

"It is behind the wrapper."

"We can swap the implementation."

"Only the driver layer uses it."

"The new kit has the same concepts."

"Tests will catch the differences."

Each sentence was partly true. Each sentence hid a different cost.

The wrapper isolated names and header files. It did not isolate callback context. The old kit called receive callbacks
from the radio task; the new kit sometimes delivered completion from a lower-level worker. The wrapper isolated the send
function. It did not isolate buffer ownership. The old kit required buffers to remain valid until callback return; the
new kit copied some payloads and retained others. The wrapper translated a few return codes. It did not own the error
model. Tests and service procedures had already learned vendor categories. The wrapper did not isolate tool chain
support. The new kit expected a newer compiler, which affected release images and qualification evidence. The wrapper
did not isolate manufacturing. The calibration fixture waited for a ready event whose meaning changed.

The replacement was not impossible. It was just not the work the estimate had described.

The Principal Engineer did not argue that the original dependency should have been rejected.

She asked the team to draw the real dependency surface.

Not the files that included the vendor headers. The behavior the system had come to rely on.

They wrote down task context, callback ordering, buffer ownership, error meanings, retry policy, power-state behavior,
logging names, test harness assumptions, calibration sequence, service-tool messages, compiler support, release cadence,
and field compatibility. They marked which consumers depended on each item directly and which ones depended through
tests, fixtures, scripts, support procedures, or previous releases.

The diagram looked less like a driver boundary and more like a product decision.

The team changed the work from "swap the library" to "name and contain the commitments."

They kept the vendor kit. The new part still solved a real hardware and schedule problem. But the product boundary
changed. The integration layer now named product-owned outcomes: radio ready, send accepted, send completed, receive
available, radio unavailable, safe to retry, unsupported, and permanently failed. Vendor errors were translated into
those categories before they left the integration layer. Callback context was normalized so product consumers did not depend on where the vendor
called from. Buffer ownership was defined in product terms. Tests were rewritten around the product contract instead of
vendor behavior. The fixture waited for product-level calibration readiness, not a vendor event name. Service tooling
displayed product meanings and kept the vendor detail only as diagnostic context. The compiler and kit version became
an owned release assumption with an upgrade owner.

The ADR was rewritten too.

It no longer said only "use the vendor kit behind a wrapper." It said which commitments the team accepted, where the
dependency was allowed to appear, who owned updates, what evidence would prove the boundary, and what conditions would
trigger replacement.

The system did not become independent of the vendor kit.

It became honest about depending on it.

That honesty changed the architecture more than the wrapper had.

## Discussion

A dependency is any external or internal thing whose behavior the system relies on and cannot freely change alone.

That definition is wider than imported code. A dependency may be a library, a service, a protocol, a hardware part, a
file format, a build image, a compiler, a release tool, a production fixture, a test harness, a support procedure, or an
internal platform owned by another team. If the system relies on it and cannot change it freely, the decision carries
architectural cost.

The law statement is simple. Every dependency commits the system to behavior, failure modes, lifecycle constraints, ownership boundaries, and replacement cost.

This does not mean dependencies are bad. The radio software kit was useful. It reduced schedule risk, brought hardware
knowledge the team did not have, and helped the product reach its first release. Many good engineering decisions depend
on other people's work. Refusing all dependencies would produce worse systems: slower, less tested, less specialized,
and often less maintainable.

The law is not "avoid dependencies."

The law is "know what you are accepting."

The first mistake is treating dependency choice as an implementation detail because the first integration is local. In
the story, the wrapper lived in one driver directory, but the dependency's behavior moved through the product. Callback
context shaped task design. Error meanings shaped retry behavior. Logging names shaped support language. Compiler
support shaped release planning. Calibration events shaped manufacturing. Those commitments were not visible in the
include graph.

That is how Silent Coupling (`SMELL-001`) often appears. A hidden dependency affects behavior but is not represented as
an explicit contract. The team thinks the product depends on its wrapper. In practice, it depends on the vendor's timing,
error vocabulary, memory ownership, and lifecycle.

Dependency use and dependency spread are different.

Using a dependency means the system relies on it somewhere. That may be entirely reasonable. A product can use a radio
kit, a database, a compression library, an internal platform, a boot tool, or a test fixture without making every part of
the system think in that dependency's terms.

Dependency spread happens when the dependency's concepts escape the boundary that was supposed to contain them. Product
errors become vendor errors. Product state becomes vendor state. Tests assert vendor callback order. Manufacturing waits
for a vendor event. Support documentation uses vendor names. Release planning follows the dependency's version support
without naming the owner. At that point the dependency is no longer a local implementation choice. It is part of the
product architecture.

A wrapper can help. It is not proof.

Syntactic isolation is the easy part. A wrapper can hide function names, header files, types, and call shapes. That is
useful, but it is only the surface. Semantic isolation asks a harder question: do consumers depend on the product-owned
contract, or do they still depend on the underlying dependency's behavior?

The difference matters.

If a wrapper exposes every vendor error unchanged, product code still depends on the vendor error model. If a wrapper
passes through callback context, product code still depends on the vendor execution model. If a wrapper preserves buffer
ownership rules, product code still depends on vendor memory behavior. If tests wait for vendor ordering, the test suite
still depends on vendor timing. If service tools display vendor categories, support still depends on vendor vocabulary.

The wrapper has isolated syntax. It has not isolated architecture.

This distinction is easy to miss because the build looks clean. The vendor header appears in one directory. The package
is behind an interface. The diagram has a box around the integration. But replacement cost is paid by behavior, not by
diagram shape.

Replacement cost includes more than swapping code.

It can include contract redesign, product migration, data migration, integration tests, system tests, fixture updates,
operational retraining, support documentation, shipped-version compatibility, confidence rebuilding, release
coordination, compiler updates, hardware qualification, and customer migration risk. A dependency that looks easy to
replace in source code may be hard to replace in the product because the product has learned its behavior.

The phrase "we can swap it later" deserves a follow-up question:

What exactly would have to change if we did?

If the answer names one file and one test, the dependency may be well contained. If the answer names product behavior,
field diagnostics, manufacturing scripts, service procedures, release images, and old device compatibility, the team has
accepted a larger decision.

Direct dependencies are the ones the team can see easily. They appear in imports, build files, service calls, protocol
choices, hardware selections, interface definitions, process handoffs, and recorded decisions.

Transitive dependencies arrive through other dependencies. They are easier to ignore because the team did not choose
them directly. They still matter when their behavior leaks into the product. A vendor kit may depend on a compiler
version. A service may depend on an identity provider. A test harness may depend on a fixture script. An internal
platform may depend on a storage format. If those transitive behaviors shape error handling, timing, storage, threading,
reset behavior, release constraints, or support horizon, they are part of the architecture.

Transitive does not mean another team owns the consequence.

It means the commitment is one step farther from the place where the team first sees it.

Dependency direction is another part of the decision. Useful dependency direction preserves architectural control.
Product code depends on a stable product contract. A narrow integration layer depends on the volatile vendor component.
The product owns its vocabulary, errors, states, and lifecycle. The vendor detail stays behind the boundary as much as
the real system allows.

Bad dependency direction lets the volatile component define the product. The vendor's vocabulary becomes the product's
vocabulary. The vendor's errors become product errors. The vendor's task model shapes unrelated components. Tests
encode the vendor's ordering. Service procedures depend on vendor names. The product cannot explain itself without the
dependency.

This is not a full boundary-design tutorial. It is a dependency decision habit. When a dependency is volatile, deep, or
hard to replace, ask which direction the concepts are flowing.

Failure behavior is part of what the dependency imports.

What happens when it is unavailable? What does latency look like? Which errors can be retried? What failures are permanent?
What state does it own? What resources can it exhaust? How does it behave during version skew? What happens when support
for the current version ends? What happens when the hardware degrades, the service changes, or the tool stops supporting
the old release?

Chapter 10 will give time its own law. Here, timing is one imported commitment among many. If correctness depends on a
dependency's ordering, delay, timeout, or cadence, that timing behavior should be named instead of discovered through
field failures.

Lifecycle is also part of the dependency.

Selection is only the first step. Adoption, integration, update, support, deprecation, replacement, and removal all need
owners when the dependency is material. A team that can adopt a dependency but cannot update it has accepted a future
maintenance problem. A team that can update it but cannot support old versions has accepted a compatibility problem. A
team that can deprecate it but never remove it has accepted a permanent cost.

Removal is not deleting an import.

Removal means consumers no longer depend on the behavior. Tests no longer encode it. Tools no longer assume it.
Manufacturing no longer waits for it. Support no longer explains it. Release planning no longer preserves it.

Not every dependency needs the same process.

A small isolated utility with obvious behavior, no product semantics, low failure impact, and cheap replacement does not
need the same review as a radio software kit, a persistent file format, a cloud service, a hardware part, a shared
platform, or a production fixture. Treating every dependency as a major ceremony wastes attention and teaches teams to
hide ordinary choices.

The Principal Engineer's job is to match review and containment effort to the size of the commitment.

That means asking what the dependency can shape. Behavior? Failure? Lifecycle? Ownership? Release cadence? Replacement
cost? If the answer is no, keep the process light. If the answer is yes, record the decision, contain the spread, and
make the owner discoverable.

Discoverability (`METRIC-003`) matters because dependency decisions tend to age quietly. A future engineer may find the
adapter, but not the reason it exists. They may find the compiler pin, but not the vendor support assumption behind it.
They may find the test harness, but not the product contract it is supposed to prove. They may find the service-tool
message, but not the rule for updating it.

An ADR (`ARTIFACT-001`) is a good home for a material dependency decision. It does not make the decision safe. It makes
the commitment visible: why the dependency was chosen, what alternatives were considered, which behavior is imported,
who owns updates, what limitations are accepted, and what would trigger replacement.

That record is not bureaucracy when it prevents the next engineer from learning the decision through an incident.

The radio team did not need to reject the vendor kit. It needed to stop pretending the choice was only a driver detail.
Once the commitments were visible, the team could choose deliberately. It could accept the dependency where it bought
real value. It could own the parts that needed to be product behavior. It could prevent new direct use outside the
integration layer. It could test the product contract. It could define update and exit triggers.

That is the practical standard:

deliberate dependencies whose commitments are understood and proportionate to their value.

## Engineering Principle

Name the commitment before accepting the dependency. If it can shape behavior, failure, lifecycle, or replacement cost,
record the decision and contain the spread.

This principle keeps the law operational.

It does not ask teams to avoid useful dependencies. It asks them to decide at the right level. A dependency that only
saves a few lines of local code can be treated lightly. A dependency that shapes task model, failure behavior,
manufacturing, service, release cadence, or future replacement deserves architectural attention.

The review should answer enough of these questions to match the commitment:

1. What problem does the dependency solve?
2. What kind of dependency is it: code, service, protocol, hardware, tool, process, or platform?
3. Who consumes it directly?
4. Who consumes it transitively?
5. Which behavior are we importing?
6. Which failures enter our system?
7. Which vocabulary, errors, timing, ownership, or lifecycle assumptions might leak?
8. Which boundary keeps product semantics under product control?
9. Who owns versions, updates, support, and deprecation?
10. What would replacement actually require?
11. What evidence shows that replacement is plausible?
12. What event would trigger update, replacement, or removal?

The point is not to complete a form. The point is to prevent a local convenience from becoming architecture without
anyone noticing.

## Architecture Exercise

### Trace the Real Cost of One Dependency

Choose one real dependency from a system you work on.

Do not automatically choose the largest external package. Choose a dependency that could shape behavior: a library, a
service, a hardware part, a protocol, a build tool, a test fixture, a file format, a release process, or an internal
platform.

Write short answers to these prompts:

1. What is the dependency?
2. What category of dependency is it?
3. What problem does it solve?
4. Which components consume it directly?
5. Which components, tests, tools, fixtures, or procedures consume it transitively?
6. What behavior does it import?
7. What failures does it import?
8. What runtime assumptions does it bring?
9. What build, release, or support assumptions does it bring?
10. Which vocabulary or error meanings leak into the product?
11. Which data, protocol, storage, or manufacturing behavior depends on it?
12. Who owns updates?
13. Who owns compatibility with existing releases?
14. What support horizon matters?
15. What evidence shows the dependency is contained?
16. What would replacement require beyond code changes?
17. What would replacement cost in tests, tooling, operations, support, and confidence?
18. What condition would trigger update, replacement, or removal?
19. Where is the decision recorded?

End with this question:

What part of the system currently depends on this dependency's behavior while believing it depends only on your
boundary?

## Principal's Notebook

- A dependency is a decision about future change.
- A wrapper helps only when callers depend on the wrapper's contract.
- Replacement cost is real when someone can describe the path out.

## ADR

### Chapter ADR: Adopt the Vendor Radio Software Kit Behind a Bounded Integration Layer

### Context

The product needs radio support for the selected hardware in the next controller revision. The vendor radio software kit
provides working initialization, protocol handling, diagnostics, and hardware-specific guidance that reduce delivery and
integration risk for the first release.

The kit also imports commitments. Its callback model, memory ownership, error meanings, retry behavior, compiler
support, release cadence, and diagnostic assumptions can spread into product code, tests, manufacturing, service tools,
and support procedures if the product boundary is too thin.

A wrapper that merely hides headers and function names does not guarantee replacement. If consumers learn vendor
semantics, replacement cost will spread beyond the driver layer.

### Decision

Adopt the vendor radio software kit, but constrain direct use to one bounded radio integration layer.

Define a product-owned radio contract for readiness, send acceptance, send completion, receive behavior, unavailable
states, failures that can be retried, unsupported states, and permanent failures. Normalize vendor errors into product meanings
before they leave the integration layer. Normalize callback context and buffer ownership into product terms. Prohibit
new direct vendor kit use outside the integration boundary.

Add contract tests around the product-owned behavior and integration tests around the actual kit. Keep manufacturing,
service tooling, logging, and support procedures aligned to product meanings rather than vendor vocabulary. Record
supported kit versions, compiler assumptions, update ownership, support horizon, and exit triggers in the ADR.

Accept that the product still depends on the kit for hardware-specific behavior. The decision contains the spread; it
does not pretend the dependency disappears.

### Consequences

The product can use the vendor kit without letting vendor semantics become the product model by accident. Delivery risk
is reduced because the team reuses working hardware support. Replacement thinking becomes more realistic because the
team can distinguish product behavior from vendor behavior. Tests become more useful because they check the product
contract first and the vendor integration second. Upgrade decisions have owners.

The decision creates work. The integration layer must be maintained. Error and lifecycle translation can hide useful
detail if the product contract is too vague. Contract tests and integration tests both need care. Some deep hardware
behavior cannot be fully insulated. If the exit trigger occurs, replacement will still require migration, validation,
release coordination, and support work.

### Alternatives Considered

Build the complete radio stack internally. This would increase product control, but it would delay the release and move
risk into an area where the team has less evidence.

Use the vendor kit directly throughout the product. This would be fastest at first, but it would let vendor vocabulary,
errors, callback context, memory ownership, and lifecycle define product behavior.

Delay the product until all replacement risks are solved. This would protect optionality in theory, but it would ignore
the current product commitment and may not produce better evidence.

Select another radio vendor. This might reduce one set of risks, but it would reopen hardware and qualification work and
would still introduce another dependency decision.

Create a fully generic radio abstraction. This could be useful after the product has evidence of multiple supported
radio families. At this stage it would likely create unused flexibility before the real variation is known.

Avoid integration until every exit path is cheap. This would make replacement easy only by not shipping the product.

## Editor's Commentary

Chapter 9 continues the Part II laws by widening the boundary created in Chapters 7 and 8.

Chapter 7 asked who owns meaningful state. Chapter 8 asked what behavior an API promises. Chapter 9 asks what broader
commitment enters the architecture when the system chooses to rely on something it cannot freely change alone.

That boundary matters because dependency decisions are easy to misclassify as implementation choices. A dependency may
enter through code, but its cost can show up in failure behavior, release cadence, test design, manufacturing, service,
support, hardware qualification, and replacement planning.

The chapter deliberately does not become a package-management tutorial, a vendor-selection guide, a license discussion,
or a security-scanning checklist. Those concerns can matter, but they are not the law. The law is about commitment.

The PEAK concepts carrying this chapter are Every Dependency Is a Decision (`LAW-007`), Silent Coupling (`SMELL-001`),
Change Radius (`VOCAB-001`), ADR (`ARTIFACT-001`), and Discoverability (`METRIC-003`). They are enough. The chapter does
not need a new dependency ledger, dependency owner concept, replacement budget, or exit-contract artifact to teach the
idea.

Chapter 10 will take one imported commitment, time, and give it its own law. This chapter only prepares that move by
showing that timing is one of the things a dependency can import.
