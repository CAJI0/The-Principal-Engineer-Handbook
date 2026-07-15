# Configuration, Variants, and Product Lines

## Opening Quote

> A flag is cheap until someone has to promise what it means.

## Story

The team called it the easy variant.

Later, support called it The Variant That Was Just a Flag.

It was the same industrial controller from the pilot build. The product now managed pumps in three environments that
looked similar from the outside and behaved differently once installed. The first package served standard industrial
sites. The second package added a cheaper radio module and a slightly different service-tool flow for a regional
customer. The third package request came from a customer who wanted the same controller, a different pressure range, a
licensed remote-control capability, and a longer protocol timeout because their gateway woke slowly after power loss.

No one wanted a product-line architecture project.

The team had just survived the prototype-to-product transition. Manufacturing and field reality had forced them to make
calibration, identity, diagnostics, recovery, and traceability more explicit. The product felt more honest than the
prototype had. The firmware team had stable board-revision handling. Manufacturing could provision a unit through a
defined path. Support could see product-level diagnostic reasons instead of raw developer states. Release had enough
packaging discipline to ship the pilot without private scripts.

So when the third package arrived, the first instinct was practical.

"Can we add one more flag?"

The question sounded reasonable because the first two packages had shipped that way.

There was a hardware revision flag for the newer board. There was a region behavior flag for one wireless rule. There
was a licensed feature flag for remote control. There was a customer-specific protocol timeout. There was a
manufacturing-mode flag that enabled station-only behavior. There was a hidden service-tool option that support used
when a unit arrived from the field with incomplete identity. There was a debug flag that had been left in production
because it helped one pilot customer. There was a build define for the cheaper radio module. There was a field override
stored in a configuration file. Recovery behavior also depended on which package had been built, because one package
could recover over the service link and the cheaper one needed a local cable.

Each flag had a story.

Each story made sense when it was added.

The hardware revision flag had protected the first board transition. The region flag had let the team comply with one
market rule without forking the whole firmware. The licensed feature flag had kept one capability out of the base
package. The protocol timeout had saved a customer trial. The manufacturing flag had made provisioning faster. The
service-tool option had helped support recover one awkward pilot unit. The debug flag had preserved evidence during a
field issue. The radio build define had kept the cheaper package small enough to fit. The field override had avoided an
urgent replacement visit.

None of those decisions looked reckless alone.

Together, they had become the product line.

The first warning came from manufacturing.

The station selected the regional package correctly, but it tested the wrong radio behavior because the cheaper module
was selected by build define, not by the product package record. The unit passed electrical test. It passed
provisioning. It failed the customer installation because the service tool expected the standard radio capability and
showed the technician an action the unit could never perform.

The manufacturing engineer said the station had used the package listed in the order.

The firmware engineer said the radio module was a build variant.

The support engineer asked which one was authoritative.

No one answered quickly.

The second warning came from an update package.

The update assumed the default configuration for the standard package. That default was right for the original
industrial sites and wrong for the regional package. The firmware accepted the update because the package identifier was
valid. The service tool reported success because the update completed. The unit restarted into a configuration that was
legal in firmware and unsupported for the customer. It did not fail loudly. It behaved just differently enough that
support could not reproduce the issue on the bench.

The configuration file said one thing.

The package label said another.

The service tool showed a third.

The support script assumed a fourth.

The third warning came from the licensed remote-control capability.

One flag enabled the feature in firmware. Another flag enabled the button in the service tool. The customer package
spreadsheet said the feature was included. The release package had been built without the firmware flag because it used
the cheaper module build profile. The field technician could see the button. The device rejected the command. The
service tool showed "unsupported operation," which was true but useless. Support could not tell whether the license was
missing, the package was wrong, the firmware image was wrong, the radio module was wrong, or the device was in a
recovery mode.

The API had changed without anyone naming the promise.

For one package, "remote control supported" meant service-tool button visible, firmware command accepted, radio module
capable, recovery compatible, and support trained. For another, it meant only that sales had checked a box and the tool
could display the button. The same phrase had two meanings.

The team was not careless.

It was overloaded by unclassified differences.

At the next architecture meeting, the request looked small on the agenda:

> Add third product package.

Mara, the principal engineer, wrote the team's first question underneath it:

> Can we add one more flag?

Then she crossed out only two words:

> Is this a supported variant, a configuration value, an implementation detail, or an unsupported combination?

That did not make the work smaller.

It made the work visible.

The team listed every product difference they could find. Board revision. Radio module. Region behavior. Licensed
remote control. Protocol timeout. Manufacturing mode. Service-tool hidden option. Debug evidence flag. Field override.
Recovery path. Default configuration. Customer package. Update package. Diagnostic vocabulary. Support horizon.

Then they stopped calling all of them flags.

The protocol timeout was configuration. It selected behavior inside an existing product contract. It needed an owner,
a default, a validation rule, a migration rule, a source of truth, and a support meaning. It was not a product variant
by itself.

The cheaper radio module was a variant promise. It changed capability, diagnostics, recovery, manufacturing test, update
packaging, and support behavior. It could not hide behind the same software promise as the standard module.

The region behavior was also a variant promise, but narrower. It affected wireless behavior, manufacturing label,
release packaging, and support documentation. It did not need to reshape the pump-control algorithm.

The licensed remote-control capability was both configuration and a variant promise. The license value selected whether
the product would expose the capability, but the supported package had to promise the firmware command, radio module,
service-tool behavior, diagnostics, recovery compatibility, and support path that made the capability real.

The manufacturing-mode flag was not a product variant. It was a temporary implementation shortcut that had survived too
long. It changed station behavior, diagnostics, provisioning, and safety checks through one broad switch. That was
Global Configuration (`ANTIPATTERN-003`), not product-line architecture.

The debug flag was not a supported customer difference. It was a Temporary Solution (`ANTIPATTERN-006`) left active
after the field issue that justified it had closed. It needed an owner, an expiration condition, or removal.

The service-tool hidden option was a promise because support depended on it. If it stayed, it needed a stable meaning,
visible support rules, and compatibility behavior. If it was only an engineering escape hatch, it did not belong in a
customer package.

The field override was configuration, but it was also Hidden State (`SMELL-004`) because firmware, support, and release
could not all see or explain it.

The build define for the cheaper module was a dependency decision. It imported a module capability, memory profile,
radio stack behavior, update-package difference, manufacturing test path, and support limitation. It was not "just a
build setting" once customers could receive different behavior because of it.

Mara drew three columns.

The first was shared core.

The shared core was the pump-control behavior, the calibration record shape, identity lifecycle, product-level
diagnostic categories, configuration validation rules, and the update state model. Those parts had to stay stable
across supported packages unless the team intentionally changed the product line.

The second was variation points.

The team named the variation points it was willing to support: radio capability, region behavior, licensed remote
control, customer protocol timing, and recovery access. Each variation point needed an owner, validation, default,
supported combinations, unsupported combinations, and a record future engineers could find.

The third was unsupported combinations.

This column changed the room.

The cheaper radio module plus licensed remote control was unsupported for the next release because the module could not
meet the recovery promise. The regional package plus the old service-tool version was unsupported because the old tool
could not show the required diagnostic reason. The debug evidence flag was unsupported in customer builds. A
manufacturing-mode flag was unsupported outside the station flow. A field override without a Decision Journal entry and
review trigger was unsupported as a product-line practice.

The product manager worried that unsupported combinations sounded like losing options.

Mara answered carefully.

"They were not options," she said. "They were promises we could not explain."

That sentence did more than any diagram.

The team used Change Radius (`VOCAB-001` and `METRIC-001`) to decide which differences needed stronger review. Changing
the protocol timeout affected firmware validation, customer configuration, one service-tool message, and two tests. It
could be a Decision Journal entry. Supporting licensed remote control on the cheaper module affected firmware,
hardware, radio dependency, service-tool behavior, manufacturing test, update recovery, release packaging, support
training, and field diagnosis. That needed an RFC (`ARTIFACT-002`) and Architecture Review (`RITUAL-001`) before it
hardened.

They recorded the shared core and active variation points in the Architecture Ledger (`ARTIFACT-006`). They wrote an
ADR (`ARTIFACT-001`) for the product-line boundary before adding the third package. Smaller defaults and temporary
exceptions went into Decision Journal (`ARTIFACT-003`) entries with evidence and review triggers.

They also froze a small set of promises before release validation: package identity, supported radio capability,
diagnostic meaning for unsupported operations, and recovery compatibility. Architecture Freeze (`RITUAL-002`) did not
freeze every configuration value. It stabilized the promises that manufacturing, release, support, and customers were
about to depend on.

The team removed two flags.

The debug flag came out of production builds. The broad manufacturing-mode flag was split into station-owned commands
with product-level API promises. The service-tool hidden option became either a supported recovery action with stable
meaning or disappeared from customer support flows.

The third package did not ship as fast as the flag-only version would have.

It shipped with fewer lies.

Manufacturing could select a package and know which radio behavior to test. Firmware could validate configuration
against supported combinations instead of accepting every legal-looking file. The service tool could display why a
capability was unsupported. Support could reproduce field reports because package identity, configuration version,
module capability, and recovery path were visible. Release could package updates against supported variants instead of
hoping defaults were harmless.

The product line was not grand.

It was understandable.

That was the architectural win.

## Discussion

Configuration and variants become dangerous when the team uses them to avoid naming product decisions.

A configuration value is not just a value. It is state. It affects behavior, and therefore it needs an owner. It needs a
scope. It needs a default. It needs validation. It needs a migration path. It needs a source of truth. It needs a
support meaning when someone has to explain a unit in the field.

A variant is not just a label. It is a promise. A supported variant says that some difference in hardware, firmware,
region, customer package, licensed capability, manufacturing flow, service-tool behavior, diagnostics, update recovery,
or support horizon is real enough for the product line to build, test, release, diagnose, and support.

A product line is not a spreadsheet. It is the architecture that lets related products share a core while differing
intentionally.

Those distinctions are not a taxonomy to memorize. They are a way to stop every product difference from becoming "one
more flag."

Flags are not the enemy. Compile-time defines are not the enemy. Configuration files are not the enemy. Build variants
are not the enemy. A spreadsheet may even be a useful planning tool. The problem begins when those mechanisms become
the only place where product promises live.

Every State Has One Owner (`LAW-001`) applies directly to configuration. If a value affects behavior, someone owns its
meaning. That owner may not be the person who stores it. Firmware may own validation. Manufacturing may write the first
value. A service tool may allow updates. Release may migrate it. Support may read it. Those surfaces can all participate
without all becoming owners of the same meaning.

The dangerous case is the familiar one: firmware has a default, manufacturing has a station value, the service tool has
a cached value, release has an update assumption, and support has a spreadsheet. The product seems configurable. In
reality, it has several partial owners and no authoritative state.

Configuration should answer ordinary questions.

Who may change this value? When may it change? What is the default? Is the default a product behavior, a manufacturing
convenience, or a migration fallback? How is the value validated? What happens when it is missing, stale, incompatible,
or from an older version? Where is the source of truth? How does support see it? Which manufacturing or service flow
depends on it?

If the team cannot answer those questions, the value is not harmless. It is hidden architecture.

Every API Is a Promise (`LAW-002`) applies to variants. A supported variant promises more than a name. It promises that
the product can behave, fail, recover, be manufactured, be updated, and be supported in a way someone can trust.

Consider a regional variant. It may require different radio behavior, label content, manufacturing checks, service-tool
warnings, release packaging, diagnostic wording, and support instructions. If the product calls that variant supported,
the promise extends across those surfaces. A flag that changes only firmware behavior does not fulfill the promise by
itself.

The same is true for hardware options. A cheaper module is not only a part substitution. It imports behavior,
capability limits, timing, failure modes, vendor lifecycle, test gaps, update packaging, and replacement cost. Every
Dependency Is a Decision (`LAW-007`) because the product line now relies on what that module can and cannot do.

This is why product-line boundaries matter.

The team needs to name the shared core: the behavior and contracts that should remain stable across supported variants.
It also needs to name variation points: the places where the product line intentionally allows differences. A variation
point is not a door to every possible combination. It is a bounded decision about where difference is allowed to enter.

Unsupported combinations are part of the architecture too.

Teams often avoid writing them down because unsupported combinations sound negative. That avoidance is expensive. If the
product line does not say what it does not support, the field will eventually discover combinations by accident. A
customer tries a package with the wrong module. A service tool accepts a configuration it cannot diagnose. An update
package assumes a default that does not belong to the installed variant. A test passes one example and quietly leaves the
rest undefined.

An unsupported combination is not a failure when it is explicit. It is a boundary.

Good variation is intentional. It has owner, scope, default, validation, compatibility meaning, support meaning, visible
records, and tests. It does not make every combination possible by accident.

Bad variation is accidental. It hides in global flags, copied defaults, build defines, service-tool options, customer
exceptions, and field overrides. It changes behavior without one owner. It makes firmware, manufacturing, service,
release, tests, and support depend on the same difference without a shared contract. That is Silent Coupling
(`SMELL-001`).

Global Configuration (`ANTIPATTERN-003`) is the common trap. One setting starts small and then controls logging,
calibration, connectivity, diagnostics, safety behavior, recovery, and service-tool options. The value becomes powerful
because nobody wants to split the decisions. It feels efficient until every change needs broad regression testing and no
one can state what the flag promises.

Hidden State (`SMELL-004`) appears when variant state affects behavior but is not visible through a clear owner,
interface, or model. A field override that support cannot see is hidden state. A default that changes during migration
without a record is hidden state. A build define that selects a hardware capability but leaves no product-level evidence
is hidden state.

Platform Leakage (`SMELL-005`) appears when low-level hardware or vendor details escape into product variation logic. A
radio module may matter to the product, but product behavior should not force service tools and feature code to learn
private driver vocabulary. HAL Everywhere (`ANTIPATTERN-002`) is the harder version: hardware abstraction details spread
so widely that each hardware option shapes unrelated product behavior. The better boundary exposes product-level
capabilities and reasons.

Simplicity Is a Feature (`LAW-004`) is especially important in a product line. A product line that supports fewer
combinations but explains them directly may be healthier than one that offers flexibility everywhere. The cheapest
product line is often the one the team can still understand.

Unused Flexibility Is Waste (`LAW-006`) keeps the team honest. A generic variation framework, broad feature-flag
system, or every-possible-combination design creates test space, review cost, migration burden, and support confusion.
Options are valuable when they protect against real uncertainty. Options invented to avoid a decision become product
debt.

Evidence Before Confidence (`LAW-005`) decides what becomes supported. A supported variant should be backed by evidence:
prototype behavior, manufacturing runs, field feedback, service-tool use, compatibility tests, customer need, recovery
tests, or release rehearsal. Evidence does not have to be perfect. It does have to match the promise being made.

One customer asking for a behavior is evidence of demand. It is not evidence that every module, region, recovery path,
and service-tool version can support that behavior. One build passing a bench test is evidence for that build. It is not
evidence for the product line.

Change Radius helps decide how much ceremony a variation deserves. A local default inside one owned tool may need only
a small record and tests. A new variation point that crosses firmware, hardware, manufacturing, service tooling, update
packaging, support, and release deserves stronger review. The point is not to count files. The point is to see the
surface that must change, be reviewed, or be retested when one product difference changes.

Records keep the product line from becoming oral history.

Use an ADR when the team defines product-line boundaries, shared core, supported variants, unsupported combinations,
or a long-lived variation point. Use an RFC when a broad variation point needs review before implementation hardens.
Use a Decision Journal entry for smaller configuration choices, temporary exceptions, evidence gaps, and review
triggers. Use an Architecture Ledger when active product-line decisions need a compact inventory with owners and review
dates.

Discoverability (`METRIC-003`) is not paperwork here. It is the ability for a future engineer to find why a package is
supported, why another combination is unsupported, who owns a default, which module capability is promised, which
service-tool behavior is stable, and what evidence would reopen the decision.

Architecture Review (`RITUAL-001`) belongs where a new variation point would harden across ownership boundaries.
Architecture Freeze (`RITUAL-002`) may belong when selected product-line promises need temporary stability for
manufacturing, field trial, release validation, or customer shipment. Freezing every configuration value would be too
heavy. Freezing package identity, diagnostic meaning, recovery compatibility, or supported module capability may be
exactly right.

This chapter can mention diagnostics, release packaging, update compatibility, recovery, and support because variants
create promises there. It should not solve observability or release discipline in full. Chapter 23 will go deeper on
observability in embedded systems. Chapter 24 will own release discipline and upgrade paths. Chapter 25 will make the
reference project concrete.

Here the job is narrower.

Name the difference. Classify it. Own it. Bound it. Record it. Test the promise it creates.

That is how configuration and variants stay architecture instead of becoming folklore.

## Engineering Principle

Treat configuration as owned state and variants as product promises. Keep the product line small enough to understand,
explicit enough to test, and discoverable enough to support.

Ask a focused set of questions:

- Is this difference configuration, a variant, an implementation detail, or unsupported?
- Who owns this value or variation point?
- Who may change it?
- What is the default?
- How is it validated?
- How does it migrate?
- Which combinations are supported?
- Which combinations are intentionally unsupported?
- Which promise does this variant make to customers, manufacturing, service, release, or support?
- What is the Change Radius of adding this variant?
- What must be recorded, reviewed, tested, or frozen?

The goal is not to prevent product differences. The goal is to make every supported difference explicit enough that the
product line can keep its promises.

## Architecture Exercise

### `Classify One Product Difference`

Choose one product difference. Do not choose the whole product line. Choose one difference that changes behavior,
manufacturing, service, release, support, update, recovery, or customer promise.

Write one sentence that names the difference.

Then document:

1. classification: configuration, variant, implementation detail, temporary exception, or unsupported combination;
2. owner;
3. who may change it;
4. default;
5. validation rule;
6. migration rule;
7. storage or source of truth;
8. affected state, API, dependency, test, manufacturing, service, release, and support surfaces;
9. supported combinations;
10. unsupported combinations;
11. evidence available;
12. decision record needed;
13. review or freeze trigger;
14. expiration or removal trigger if temporary.

End with four outputs:

1. one classification;
2. one owner;
3. one supported or unsupported boundary;
4. one validation or decision action.

If the answer is "just add a flag," keep going. A flag is a mechanism, not a decision.

## Principal's Notebook

- A flag without an owner is hidden state.
- Every supported variant is a promise.
- The cheapest product line is the one you can still understand.

## ADR

### Chapter ADR: `Define Supported Variant Boundaries Before Adding the Third Product Package`

#### Status

Accepted for the chapter.

#### Context

The first product package shipped with small configuration differences. The second package added a cheaper hardware
module and service-tool differences. Both packages reached customers, manufacturing, support, and release through a mix
of configuration files, build defines, package labels, service-tool options, and temporary flags.

A third product package is now requested. It would add a different pressure range, a licensed remote-control capability,
customer-specific protocol timing, and recovery behavior that depends on module capability.

The current variation model is not explicit enough. Support cannot see or validate every combination. Manufacturing can
select a package while testing the wrong module behavior. Release packaging can assume defaults that do not belong to
the installed variant. Service tooling can expose capabilities the firmware or hardware package does not promise.
Temporary flags are starting to become product-line behavior.

Adding another flag would make the next package possible quickly, but it would turn unowned variation into customer,
manufacturing, service, release, and support promises.

#### Decision

Define supported variant boundaries before adding the third product package.

Separate configuration values from supported variants. Configuration values select behavior inside an existing product
contract and must have owner, default, validation, migration rule, source of truth, and support meaning. Supported
variants are product promises and must name the behavior, compatibility, manufacturing, service, release, update,
recovery, and support implications they create.

Define the shared core for the product line: pump-control behavior, calibration record shape, identity lifecycle,
product-level diagnostic categories, configuration validation rules, and update state model. Changes to shared core
require explicit review because they affect every supported package.

Define variation points for radio capability, region behavior, licensed remote control, customer protocol timing, and
recovery access. Each variation point must have an owner, supported combinations, unsupported combinations, validation
evidence, and a discoverable record.

Remove or expire temporary flags that are not supported product behavior. Split broad manufacturing or service flags
into smaller product-level surfaces with owners and clear promises.

Record consequential product-line decisions in an ADR. Use RFCs for proposed variation points with broad Change Radius.
Use Decision Journal entries for smaller configuration choices and temporary exceptions. Keep active product-line
decisions visible in the Architecture Ledger.

Require Architecture Review before adding a new variation point that affects firmware, hardware, manufacturing, service
tooling, update packaging, release, support, or recovery. Temporarily freeze selected variant promises before release
validation when manufacturing, field support, or customer shipment depends on stable meaning.

Defer observability details to Chapter 23 and release-discipline details to Chapter 24.

#### Consequences

The product line becomes easier to reason about. Configuration values have owners. Supported variants have explicit
promises. Unsupported combinations are named instead of discovered in the field. Manufacturing, release, support, and
service tooling can align on the same product-line boundaries.

The accidental test space shrinks because every possible combination is not treated as supported. Supportability
improves because package identity, defaults, module capability, diagnostic meaning, and recovery behavior are visible.
Silent coupling is reduced because firmware, manufacturing, service tools, update packages, tests, and support records
share explicit contracts.

The cost is slower feature addition for unsupported combinations. Some customer-specific behavior will require review
before it becomes a product promise. Some flexibility will be removed because it lacks evidence or ownership. The team
must maintain product-line records as the product evolves.

The trade-off is accepted because unbounded variation creates larger cost later, when customers already depend on
promises the architecture cannot explain.

#### Alternatives Considered

Add another flag.

This is fastest locally, but it keeps product-line behavior hidden in scattered switches and increases Change Radius for
future changes.

Create separate firmware for each customer.

This can isolate behavior, but it duplicates shared core, increases release and support cost, and hides common product
promises behind separate builds.

Make everything configurable.

This sounds flexible, but it turns product-line design into a configuration problem and makes every combination seem
possible unless the architecture says otherwise.

Freeze the current variant model immediately.

This creates stability too early. The model has not yet defined shared core, variation points, supported combinations,
unsupported combinations, or owners well enough to freeze.

Support every combination discovered in the field.

This mistakes accidental behavior for a product promise. Field discovery is evidence, not automatic support scope.

Postpone variant modeling until after the next customer ships.

This preserves short-term delivery but lets temporary flags, build defines, defaults, and service-tool behavior harden
into the product line without review.

## Editor's Commentary

Chapter 22 turns the product outward again.

Chapter 20 asked what prototype assumptions must become product decisions. Chapter 21 asked whether those decisions
survive manufacturing and field reality. Chapter 22 asks what happens when the product is no longer one product in one
shape. The pressure is not only to build the device. It is to support intentional differences without letting accidental
differences become the product line.

The chapter intentionally has no primary PEAK concept and introduces no new concept. Configuration, variant, product
line, supported combination, and unsupported combination are chapter-local working terms. The force of the chapter comes
from applying the existing relationship set to product-line growth: Every State Has One Owner (`LAW-001`), Every API Is
a Promise (`LAW-002`), Simplicity Is a Feature (`LAW-004`), Evidence Before Confidence (`LAW-005`), Unused Flexibility
Is Waste (`LAW-006`), Every Dependency Is a Decision (`LAW-007`), Change Radius (`VOCAB-001` and `METRIC-001`),
Discoverability (`METRIC-003`), ADR (`ARTIFACT-001`), RFC (`ARTIFACT-002`), Decision Journal (`ARTIFACT-003`),
Architecture Ledger (`ARTIFACT-006`), Architecture Review (`RITUAL-001`), Architecture Freeze (`RITUAL-002`), Hidden
State (`SMELL-004`), Silent Coupling (`SMELL-001`), Platform Leakage (`SMELL-005`), Global Configuration
(`ANTIPATTERN-003`), Temporary Solution (`ANTIPATTERN-006`), and HAL Everywhere (`ANTIPATTERN-002`).

The boundary is deliberate. This is not a product-management chapter, feature-flag operations guide, SKU tutorial,
configuration database design, build-system guide, release-train process, product-line engineering methodology, or
test-matrix tutorial. It is an architecture chapter about product differences becoming promises.

Chapter 23 can now take up observability in embedded systems with a clearer question: what must the product make visible
once configuration and variants create different supported realities? Chapter 24 can handle release discipline and
upgrade paths. Chapter 25 can bring the reference project together.
