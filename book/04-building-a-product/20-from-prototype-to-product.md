# From Prototype to Product

## Opening Quote

> A prototype proves that a thing can work. A product proves that it can keep working without the prototype team in the room.

## Story

The team called it the fastest path to the customer.

At first, that was true.

The product was an embedded controller for a field device that had been awkward to configure, slow to diagnose, and
expensive to service. The customer wanted a working demonstration before committing to a wider program. The team had
six weeks, one hardware spin, a vendor driver package, a bench fixture, and a sponsor who wanted to see the device move
from command to response without another architecture meeting.

The prototype did exactly what a good prototype should do.

It made the uncertain thing visible.

On the demo bench, the firmware booted quickly. The sensor path stabilized. The device accepted a configuration from a
small service tool. The motor profile applied without a reset. The customer could change one parameter, run the cycle,
and see the result on the screen. The team learned more in that week than it had learned from the previous month of
slides.

The prototype was not careless. It was focused.

It used one known board revision because that was the board they had. Calibration was manual because only three units
existed. Configuration was hard-coded for the customer path because variants would have slowed the demo. The service
tool was a debug application with a few product words in the UI. The driver for the sensor bus was the vendor example
driver with a thin wrapper around it. Firmware updated through a lab cable and a script that only the firmware lead knew
how to run. A diagnostic command exposed raw hardware state because that made bring-up faster. Manufacturing had an
ad-hoc script that copied a calibration value from the bench notebook into a fixture file. Field diagnostics were a
serial log and a developer who could read it.

None of those choices were surprising.

Most of them were right for the prototype.

The demo succeeded. The customer liked it. The sponsor liked it more. The product manager asked how quickly the team
could turn the prototype into the first product baseline. The release owner asked whether the firmware could be
packaged by the end of the month. The hardware owner said the second board revision was close enough. Manufacturing
said they could adapt the script later. Support said diagnostics could wait until the pilot units existed.

The phrase "clean it up after the pilot" appeared in three meetings.

No one meant harm by it.

But the prototype had started to carry product obligations before anyone had named the assumptions it depended on.

The first warning came from the second board revision.

The prototype had been calibrated on one board with one sensor lot. The new revision had the same schematic, but a
slightly different analog front end. The firmware still booted. The happy path still ran. But the manual calibration
value no longer produced the same operating range. The firmware lead knew how to adjust it, so the team did. The fix was
small enough to feel like a detail.

Then manufacturing tried to repeat the setup.

The station operator could run the fixture script, but the script assumed a bench file name, a USB device order, and a
calibration value copied from a developer note. It also assumed the device was already in the debug state. On the bench,
the firmware lead had put it there without thinking. On the manufacturing station, that step was invisible. The station
failed three units in a row before anyone realized that the "configuration process" was partly a person.

Support found the next gap.

A pilot unit failed to apply a configuration in the field. The service tool showed "write failed." The firmware log had
the real reason: the device rejected a profile because the board-revision field was missing. The customer did not have
the firmware log. The support engineer did not have the debug tool. The only person who could interpret the raw state
was on another call.

The team had diagnostics.

They did not have product diagnostics.

The configuration story also started to split. The original customer needed one motor profile. The second customer
needed the same controller with a different sensor option. The hardware team wanted to support both by keeping the
hard-coded default and adding a small override in the service tool. The service-tool owner wanted a configuration file.
Manufacturing wanted a station-owned value. Firmware wanted to keep the constant in code until the variant matrix was
clearer.

Every option looked simple from the place that proposed it.

Together, they meant nobody owned configuration state.

The update path was worse. The prototype updated through a lab-only script that erased the application, flashed a new
image, and restarted the device. It worked every time on the bench. It had never been interrupted. It had never been run
by support. It had never had to preserve a previous configuration. It had never had to explain what state the device was
in after failure.

When the release owner asked whether the pilot could be updated in the field, the room became careful.

"The update works," one engineer said.

"The update path works in the lab," the Principal Engineer said.

That was the moment the conversation changed.

The team had been asking:

> How fast can we ship the prototype?

The Principal Engineer wrote a different question:

> Which prototype assumptions must be promoted, replaced, owned, tested, or intentionally accepted before this becomes
> the product?

The question did not slow the room because it was abstract.

It slowed the room because everyone could name an assumption.

The firmware lead named the hard-coded configuration. The hardware owner named the board revision and sensor lot. The
manufacturing engineer named the manual calibration step. The service-tool owner named the debug tool. Support named
the missing field diagnosis. Release named the lab-only update script. QA named the single customer path. The firmware
lead named the vendor example driver last, quietly, because everyone knew it had spread farther than planned.

The Principal Engineer did not call the prototype bad.

She did not ask for a rewrite.

She drew five columns on the whiteboard: product contract, implementation detail, temporary shortcut, evidence gap, and
removed shortcut. Then she asked the team to place each assumption somewhere.

The board revision was not an implementation detail anymore. It affected calibration, configuration, manufacturing
test, and support diagnosis. It became a product contract: a device would report its board revision, and configuration
would be validated against it.

The manual calibration step was not allowed to remain a person. The team did not need a full manufacturing chapter in
that meeting, but it did need an owner and a repeatable path. Manufacturing owned the station step. Firmware owned the
calibration state in the device. QA owned the evidence that a configured unit could be repeated across the first board
revision and the second.

The hard-coded customer path became two decisions. The algorithm stayed simple because it was still the right product
behavior. The hidden constant did not. The constant moved behind an owned configuration path with validation and a
default. The team explicitly refused to add a generic variant framework for every future product. One real variant was
evidence. A dozen imagined variants were not.

The debug service tool became a temporary shortcut. It could support the pilot only if it had an owner, an expiration
condition, and a visible list of unsupported actions. Product-level rejection reasons had to be stable enough for
support to use. Raw hardware state could remain diagnostic, but it could not be the only way to explain a field failure.

The vendor example driver became a dependency decision. The team did not replace it immediately. They named the surface
it was allowed to occupy, assigned update ownership, wrote down the assumptions it made about callbacks and error
meaning, and added a review trigger if the driver touched release packaging, diagnostics, or recovery behavior.

The lab-only update script became an evidence gap. It had proved that firmware could be flashed on a bench. It had not
proved a recoverable product update. The team accepted that full upgrade discipline belonged later, but the pilot still
needed a minimum answer: what happens if the update is interrupted, who can recover it, what state is visible to support,
and what configuration is preserved.

The temporary bypass was removed.

It had disabled one board-revision check during bring-up. Everyone remembered why it existed. That was not the same as
ownership. It had no pilot value, no evidence gap worth carrying, and too much Change Radius if it reached
manufacturing or support. Removing it was the simplest product decision in the room.

The whiteboard did not make the product ready.

It made the work honest.

The team could now separate the valuable prototype from the accidental product architecture hiding inside it. The
prototype had proved that the device behavior mattered to the customer. It had proved that the sensor path could be
stable enough. It had proved that the configuration idea was understandable. It had proved that the team could move
fast.

It had not proved manufacturing repeatability. It had not proved field diagnosis. It had not proved recoverable update.
It had not proved variant handling. It had not proved release packaging. It had not proved that a vendor example driver
was acceptable as a product dependency. It had not proved that a manual calibration step belonged in the product.

That distinction saved the pilot.

Not by making the team cautious about everything.

By making it precise about what the prototype had actually taught.

The pilot still shipped quickly. It shipped with fewer hidden promises. The team kept the simple control path. It kept
the small service interaction. It kept the narrow device behavior that had impressed the customer. But configuration
had an owner. Calibration had a repeatable minimum path. The service tool had product-level error meanings. The update
script had a recovery note and an explicit limit. The vendor driver had a named dependency surface. The remaining risks
were in a Decision Journal entry with review triggers instead of scattered through memory.

The product did not become perfect.

It became owned.

## Discussion

A prototype proves that something can work once. A product architecture defines what must keep working across users,
variants, manufacturing, service, release, support, and time.

That is the transition this chapter cares about.

The prototype is not the villain. A good prototype is an act of engineering discipline. It narrows uncertainty. It gives
the team evidence. It lets customers react to behavior instead of intention. It exposes problems that planning could
only guess at.

The danger begins when prototype evidence is treated as product architecture.

Prototype success is usually conditional. It worked with this board, this fixture, this customer path, this operator,
this script, this firmware lead, this sensor lot, this service laptop, this configuration file, this update cable, and
this known failure mode. Those conditions do not make the prototype fake. They define what the prototype proved.

The Principal Engineer's job is to preserve that evidence without letting hidden assumptions become invisible product
promises.

A prototype optimizes for learning speed. It tolerates shortcuts because delay can be more expensive than temporary
roughness. Manual setup may be acceptable. Hard-coded values may be acceptable. A local script may be acceptable. A
debug tool may be acceptable. A direct dependency on a vendor example may be acceptable. A single board revision may be
enough to answer the question the prototype was built to answer.

A product optimizes for repeated trust.

It must preserve behavior across more than one use. It must be manufactured, tested, configured, updated, diagnosed,
released, and supported by people who did not build the prototype. It must survive variants. It must make ownership
visible. It must turn dependencies into decisions. It must state which limits are known and which risks are accepted.

The same design choice can be excellent in one world and dangerous in the other.

Hard-coding a configuration value may be the fastest way to learn whether the control loop behaves correctly. Keeping
that value hidden in product firmware may make manufacturing, service, variants, and release packaging all depend on a
developer memory.

A debug command that exposes raw hardware state may save a week during bring-up. If support depends on that command in
the field, it has become an API promise whether anyone named it or not.

A vendor example driver may be a good way to avoid premature abstraction during a prototype. If its callback model,
error meanings, memory ownership, and update cadence spread through product code, tests, tooling, and support
procedures, it is no longer just example code. It is a dependency decision.

The distance between those two worlds is the `productization` gap: the distance between the prototype's hidden
assumptions and the product's required operating reality.

The gap is not a new metric. Change Radius already gives the team the useful question: how much system surface must
change, be reviewed, or be retested when one decision changes? The prototype-to-product gap is a chapter-local way of
noticing where prototype assumptions will create that surface.

Manual setup becomes production configuration. A lab fixture becomes manufacturing process. A debug log becomes field
diagnostic need. One customer path becomes a variant matrix. A direct dependency becomes a support obligation. A
hard-coded value becomes calibration or configuration. A local script becomes release process. A happy-path update
becomes a recovery requirement. A single board becomes tolerance, lot, and field variability. Temporary wiring becomes
an interface contract. Developer memory becomes product documentation or a decision record.

The move is not to condemn each gap.

The move is to classify it.

Some prototype assumptions become product contracts. If the service tool returns a rejection reason that support will
use, that reason is not just UI text. It is a product promise. If a device reports board revision and configuration
validity, that state needs one owner. If a station process writes calibration state, the product must know who validates
and explains that state.

Some assumptions remain implementation details. A local helper function, a simple file format inside one owned tool, or
a narrow internal default may remain simple if it does not leak into manufacturing, service, update, variants, or
support. Simplicity is a feature when it reduces future change cost. The goal is not to make the prototype look more
architectural. The goal is to keep the simplicity that survives contact with product reality.

Some assumptions are temporary shortcuts. Temporary is not a problem by itself. Unowned temporary work is the
anti-pattern. A temporary shortcut needs an owner, an expiration condition, or an explicit decision to carry the risk.
Team memory is not an expiration condition. "Remove after pilot if no field unit requires the bypass" is closer.
"Firmware owner reviews before release baseline" is closer still.

Some assumptions are evidence gaps. The prototype showed a thing could work on the bench. It did not show that the
thing survives interruption, component variation, operator error, old service tools, station timing, or field support.
Evidence Before Confidence matters most when everyone wants the prototype to be enough. Confidence should follow the
evidence the prototype actually produced, not the relief everyone felt when the demo succeeded.

Some assumptions are residual risks. A team may decide to ship a pilot with a known limit. That can be responsible when
the risk is visible, owned, bounded, and tied to a review trigger. It is irresponsible when the risk is hidden in a
script, a comment, a chat thread, or a developer's memory.

Some assumptions should be removed. The fastest way to make a prototype more product-ready is sometimes to delete the
shortcut that no longer buys learning.

Classification prevents two common overreactions.

The first overreaction is shipping the prototype unchanged because the customer liked it.

That confuses evidence with readiness. The demo proved something, but usually not everything the product now has to
survive. It may have proved customer value without proving manufacturing repeatability. It may have proved firmware
behavior without proving service diagnosis. It may have proved update on a bench without proving recovery in the field.

The second overreaction is rewriting the prototype because it was "only a prototype."

That throws away evidence. It also often replaces real simplicity with speculative flexibility. The team imagines every
future product variant, builds hooks for them, expands the configuration surface, and increases the test matrix before
one real product has justified the cost. Unused flexibility is waste. Options are valuable when they protect against
real uncertainty. Options invented to feel safer become product debt wearing a responsible face.

The better path is narrower.

List the assumptions. Classify them. Assign owners. Decide what evidence is missing. Decide what must change before the
release baseline. Decide what can ship only with a review trigger. Record consequential choices where future engineers
will find them.

Ownership is the hinge.

Prototype work often hides ownership inside the people who built it. The firmware lead knows the update script. The
hardware owner knows which board revision behaves differently. The manufacturing engineer knows which fixture step was
manual. The support engineer knows which diagnostic message is not useful. The service-tool owner knows which error is
really raw firmware state. That knowledge is valuable, but it is not architecture until the system can survive without
private memory.

Every State Has One Owner becomes concrete during this transition. Calibration state, configuration state, board
revision, update state, service mode, and recovery status all need an owner that can change, validate, and explain the
state. If firmware, a station fixture, and a service tool each keep their own idea of the same state, the product has
already inherited a failure.

Every API Is a Promise becomes concrete too. Prototype interfaces are often born as convenience. A debug command, a
configuration file, a service-tool message, a fixture output, or a script argument may feel informal until another team
depends on it. Once manufacturing, support, QA, release, or a customer path trusts it, the API has made a promise about
meaning, errors, timing, and ownership.

Every Dependency Is a Decision is the third lens. Prototype dependencies rarely look architectural at first. A vendor
driver, a script language, a test harness, a flashing tool, a fixture behavior, a library version, or a manual process
can become part of the product's change radius. The question is not whether dependencies are bad. The question is who
owns the dependency surface, what behavior the product relies on, how failure propagates, and what would trigger
replacement.

Records keep the transition from becoming oral history.

Use an ADR when a prototype assumption becomes a long-lived product decision: configuration ownership, update recovery,
persistent data meaning, service-tool semantics, support-visible diagnostics, or dependency boundaries. Use a Decision
Journal entry for smaller assumption decisions, temporary risks, evidence gaps, and review triggers. Use Architecture
Review when the prototype-to-product move will harden across multiple teams and become expensive to change.

The point is not paperwork.

The point is discoverability. A future engineer should be able to find why a calibration value is owned by firmware
rather than the station, why a service tool shows one rejection reason instead of another, why a vendor driver is
wrapped only at one boundary, why a pilot shipped with a known update limitation, and when that limitation must be
reviewed again.

Chapter 20 can name manufacturing, service, diagnostics, variants, update, recovery, release, and support. It should
not teach all of them.

Those later chapters need room to do their work. Chapter 21 will go deeper into manufacturing and field reality.
Chapter 22 will own configuration, variants, and product lines. Chapter 23 will own observability in embedded systems.
Chapter 24 will own release discipline and upgrade paths. Chapter 25 will walk through the reference project.

Here, those concerns serve one question:

What did the prototype ignore that the product can no longer ignore?

That question is enough.

The first product baseline does not need to be perfect. It does need to stop pretending that a successful demo answered
questions it never asked.

## Engineering Principle

Treat a successful prototype as evidence, not architecture. Before it becomes the product, expose its assumptions, keep
the simplicity that survives, replace the shortcuts that do not, and assign owners to the product realities the
prototype ignored.

Ask a focused set of questions:

- What did the prototype actually prove?
- Which assumptions were hidden in people, scripts, wiring, fixtures, or one test unit?
- Which shortcuts are harmless implementation details?
- Which shortcuts become product risk?
- Which behavior becomes a product promise?
- Which manual steps must become repeatable?
- Which diagnostics are needed outside the lab?
- What changes for manufacturing, service, updates, variants, and release?
- Which dependency becomes a support obligation?
- Which temporary solution needs owner and expiration?
- Which risk can ship with an explicit review trigger?

The goal is not to punish prototype speed. The goal is to keep prototype learning while removing the invisible promises
that would make the product fragile.

## Architecture Exercise

### `Productize One Prototype Assumption`

Choose one prototype assumption. Do not choose the whole prototype. Choose one assumption that would hurt someone if it
became product behavior without being named.

Write one sentence that states the assumption.

Then document:

1. where the assumption lives;
2. why it was acceptable in the prototype;
3. which product reality it affects;
4. owner;
5. evidence available;
6. evidence missing;
7. classification: product contract, implementation detail, temporary risk, evidence gap, or removed shortcut;
8. affected surfaces;
9. test or validation needed;
10. manufacturing, service, update, variant, or release implication;
11. decision record needed;
12. review trigger or expiration condition.

End with four outputs:

1. one assumption promoted, removed, or explicitly accepted;
2. one owner;
3. one evidence gap;
4. one prototype-to-product action.

If the exercise ends with "clean up later," keep going. Later is not an owner.

## Principal's Notebook

- A prototype is evidence, not a product promise.
- Keep the simplicity that survives product reality.
- Every shortcut needs an owner, an expiration, or a decision.

## ADR

### Chapter ADR: `Productize the Prototype Configuration Path Before Release Baseline`

#### Status

Accepted.

#### Context

The prototype configuration path worked in the lab through manual steps and developer scripts. A firmware lead could
put the device into the right state, copy a calibration value from a bench note, run the flashing script, apply the
hard-coded customer configuration, and read the debug log when something failed.

That was acceptable for the prototype. The prototype needed fast evidence that the device behavior mattered and that the
configuration idea could work.

The product will need more than that. Manufacturing needs a repeatable configuration and calibration path. Service needs
stable product-level rejection reasons and enough diagnostic visibility to help a field unit. Variants need a way to
express real differences without turning every future possibility into a configuration framework. Update and recovery
need a visible state when configuration changes are interrupted. Release needs packaging that does not depend on one
developer's local script.

Keeping the prototype path unchanged would preserve short-term speed, but it would hide product risk inside manual
steps, scripts, comments, and developer memory.

#### Decision

Make the prototype configuration path product-ready before accepting it as the release baseline.

Keep the parts of the prototype that are intentionally simple and stable: the narrow device behavior, the small
configuration surface for the first product, and the customer-visible flow that the demo proved valuable.

Replace manual configuration with an owned product configuration path. Firmware owns device configuration validation
and stored configuration state. Manufacturing owns the station step that writes or verifies production configuration.
The service-tool owner owns product-level messages and operator flow. QA owns the evidence that the path repeats across
the first supported board revisions and customer configuration paths.

Remove temporary bypasses that no longer produce learning. Temporary shortcuts that remain for the pilot must have an
owner, expiration condition, and review trigger.

Record the consequential choices in an ADR. Use Decision Journal entries for smaller accepted risks, evidence gaps, and
review triggers.

Add minimum diagnostics, validation, and service visibility before release baseline. The service tool must distinguish
configuration rejected, unsupported board revision, invalid calibration, interrupted update, and unknown device state at
the product level. Raw debug logs may remain available to engineering, but they are not the support contract.

Defer deeper manufacturing, observability, variants, and release playbooks to later chapters. This decision creates a
minimum owned path; it does not solve every future product-line or upgrade problem.

#### Consequences

The team keeps a faster path from prototype to product baseline because it preserves the behavior the prototype proved.
It avoids a rewrite and avoids speculative flexibility for variants the product has not justified.

The team also gains explicit ownership of product assumptions. Configuration state has an owner. Calibration has a
repeatable minimum path. Service messages have product meaning. Temporary shortcuts have expiration or removal. The
vendor and tool dependencies have named surfaces. Manufacturing, support, QA, and release can see which parts of the
prototype are product decisions and which remain risks.

The cost is visible product work before visible feature progress. Some schedule pressure increases because the team
must validate assumptions that the prototype skipped. Some residual risks remain and need review triggers. Some
prototype decisions may still be revisited after pilot evidence arrives.

The decision makes the product baseline more honest. It does not make it final.

#### Alternatives Considered

Ship the prototype unchanged.

This preserves short-term speed, but it lets manual calibration, hard-coded configuration, developer scripts, lab-only
update behavior, and debug-only diagnosis become product architecture without owners.

Rewrite the entire architecture before the product baseline.

This may feel cleaner, but it discards useful prototype evidence and delays the pilot without proving that the rewrite
addresses real product uncertainty. It also risks replacing simple working behavior with untested abstractions.

Add flexibility for every possible future variant.

This protects against imagined futures while increasing the test matrix, configuration surface, review cost, and
support burden now. The first product needs a path for real variants, not a framework for every possible product.

Defer manufacturing, service, and update concerns until after first release.

Some depth belongs later, but the release baseline cannot depend on invisible manual steps, unsupported diagnostics, or
a happy-path update script. Minimum ownership and evidence are required before the prototype becomes the product.

Document assumptions only in comments.

Comments may help local code, but they do not create ownership, review triggers, or discoverability across firmware,
manufacturing, service, QA, support, and release.

Freeze prototype behavior immediately.

Freezing may be useful after the team has named the product decision and evidence threshold. Freezing the prototype too
early protects hidden assumptions instead of product architecture.

## Editor's Commentary

Chapter 20 opens Part IV by changing the source of architectural pressure.

Part III taught how to shape decisions: draw boundaries, understand Change Radius, design for failure and recovery,
record ADRs and Decision Journal entries, review architecture before it hardens, and freeze selected decisions during a
high-risk phase. Chapter 20 asks what happens when a working prototype starts carrying product obligations.

The answer is not "slow down." It is not "rewrite." It is not "add a process." The answer is to expose the assumptions
that made the prototype succeed and decide which of them can survive as product architecture.

This chapter has no primary PEAK concept. It is anchored by The Successful Prototype (`FAILURE-003`), the failure mode
where useful prototype decisions become production architecture without review. Temporary Solution (`ANTIPATTERN-006`)
names the risk of shortcuts without owner or expiration. Simplicity Is a Feature (`LAW-004`) protects the parts of the
prototype that remain intentionally simple. Unused Flexibility Is Waste (`LAW-006`) keeps the team from replacing one
problem with speculative variant machinery. Evidence Before Confidence (`LAW-005`) keeps the demo from becoming proof
of readiness.

The supporting laws make the transition concrete. State needs ownership. APIs become promises. Dependencies become
decisions. Change Radius shows how far one prototype assumption can spread. ADRs, Decision Journal entries,
Architecture Review, and Discoverability keep the resulting choices findable after the prototype team is no longer in
the room.

The later Part IV chapters will go deeper. Chapter 21 owns manufacturing and field reality. Chapter 22 owns
configuration, variants, and product lines. Chapter 23 owns observability. Chapter 24 owns release discipline and
upgrade paths. Chapter 25 walks the reference project.

Chapter 20 does not write those chapters early. It creates the doorway into them: product reality is architecture
pressure, and the first place that pressure appears is in the gap between a successful prototype and the product it is
now expected to become.
