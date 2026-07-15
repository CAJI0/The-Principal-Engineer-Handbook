# Designing for Manufacturing and Field Reality

## Opening Quote

> A product is not ready when it works for engineers. It is ready when it can be built and understood without them.

## Story

The team called the pilot unit "the one that finally felt real."

Later, the incident file would give the pilot a plainer name: The Product That Only Worked in Engineering.

It was a small industrial controller that managed a pump, two pressure sensors, a valve, and a wireless service link.
The earlier prototype had been impressive but fragile. It worked on the engineering bench because the same three people
who wrote the firmware also knew how to load it, adjust it, recover it, and explain its strange moments. Chapter 20's
work had helped them move beyond that. The update path was no longer a private developer ritual. Configuration had a
clearer shape. The service tool existed as a product surface instead of a debug console with a nicer icon. The
architecture review had removed several obvious prototype shortcuts.

By the time the team ordered the pilot build, the unit passed the lab test plan. It started cleanly. It controlled the
pump within the target band. It survived the update sequence. The service tool could connect, read state, and apply a
configuration file. The hardware team had a small stack of boards that behaved consistently enough for the demo room.
The product manager could show the unit to a customer without an engineer standing next to it with a cable.

Then the first manufacturing run began.

The contract manufacturer called on the second morning. The calibration step was taking too long. On the engineering
bench, calibration meant connecting the device, warming the sensor, running a script, waiting for the pressure fixture
to settle, nudging the offset, and rerunning the script if the first result looked odd. That was fine when an engineer
owned one unit at a time. It was not fine at line speed. The fixture operator had ninety seconds available for the step.
The script sometimes needed four minutes. Worse, it sometimes asked for a judgment call: "Does this slope look normal?"

The manufacturing lead tried to be helpful. He made a local instruction sheet. If the offset drifted by less than a
small value, operators accepted it and moved on. If the script hung, they power-cycled the unit and retried. If the
fixture could not reach the debug connector after the board was inside the enclosure, they calibrated before final
assembly and hoped nothing changed after the gasket compressed.

None of those choices looked like architecture. They looked like line-side pragmatism.

By Friday, they were architecture.

The first batch showed three different behaviors. Units from the original board revision calibrated in the expected
range. Units from the new board revision needed a slightly different timing window before the pressure reading was
stable. Units with a substitute sensor from the approved alternate supplier needed a different offset curve. The
firmware could handle all three cases if an engineer knew which case was present, loaded the right constants, and
validated the result manually. The product itself did not know. It had no owned model of manufacturing-visible
calibration state.

The serial numbers were worse. Device identity was assigned in a spreadsheet after the unit passed electrical test. The
service tool could read the identity if it had already been written, but there was no product contract that said when
identity became valid, who owned it, or what should happen if a unit left the line without it. The spreadsheet had become
a state owner. The station script had become another. The firmware had a third partial opinion because it cached the
identity after first boot. The warehouse labels had a fourth. When support later asked whether a returned unit had been
built with the substitute sensor, nobody could answer from the product record alone.

The team had seen this shape before, but in smaller forms. Every State Has One Owner (`LAW-001`) had already taught
them that meaningful state must have one clear owner. In the lab, device identity, calibration status, fixture result,
and board revision looked like setup details. In manufacturing, they were product state. Because nobody had assigned one
owner, each process invented a partial owner.

The first field trial made the same point with less patience.

The units were installed at three customer sites. One site had stable power and clean wiring. One site had long cable
runs beside noisy equipment. One site had a pump that pulled current close to the edge of the power budget during
startup. The engineering team expected some variation. They did not expect the service calls to be unreadable.

Support opened the service tool and saw raw developer states:

- `BOOT_WAIT_SENSOR`
- `CFG_PENDING`
- `CAL_DIRTY`
- `SAFE_HOLD_3`
- `UPD_RECOVERY_ARMED`

Those names meant something to the firmware team. They did not tell support whether the failure was configuration,
hardware, firmware, or environment. A technician could see that the unit was in `SAFE_HOLD_3`, but not whether that
meant a pressure sensor mismatch, a missing calibration record, an update recovery guard, or a field wiring problem.
The tool had exposed internal states instead of support-safe diagnosis.

One unit reset during an update. The update design was better than the prototype path, but recovery still assumed a
developer laptop and a private cable. The field technician had neither. The support script said to return the unit. The
firmware engineer who wrote the recovery command was confused: "It is recoverable. You just have to connect with the
engineering tool and run the loader in manual mode." That sentence ended the argument. Recoverable by a developer in the
lab was not recoverable in the field.

Another unit lost its field logs after reset. The team had treated logs as a convenience surface, useful when the unit
was alive and connected. In the field, logs were evidence. When a reset removed the last pressure readings, update
attempt, configuration version, and voltage warning, the team lost the only trace that could have separated environment
from firmware. Evidence Before Confidence (`LAW-005`) was not just a review posture. It was a product obligation when
engineers were absent.

By the next week, the product manager had a familiar question.

"Why did manufacturing and the field break the architecture?"

Mara, the principal engineer, did not answer immediately. She had been quiet through the incident review, writing the
same words in different columns:

- calibration
- identity
- fixture access
- service diagnosis
- update recovery
- traceability
- ownership
- evidence

"They did not break it," she said. "They revealed which realities were missing from the contract."

That changed the room.

The manufacturing lead had been defending the line instructions. Support had been defending the service script. Firmware
had been defending the state machine. Hardware had been defending the board revision. Everyone had a local reason for
the behavior. Mara moved the discussion away from blame and toward architecture obligations.

First, she separated process details from architectural promises. The manufacturing line could choose station layout,
operator steps, label placement, and fixture timing. The architecture still had to say what product state existed, who
owned it, how it was validated, what surfaces could write it, and what evidence proved it was correct.

Second, she named the assumptions the lab had hidden.

Calibration assumed developer judgment. Identity assumed the spreadsheet was always correct. Fixture access assumed the
debug connector was available after enclosure assembly. Board revision handling assumed an engineer knew the revision
before choosing timing and offset. Service diagnosis assumed support could translate firmware states. Update recovery
assumed a developer laptop. Field evidence assumed the device would stay alive long enough for someone to pull logs.
Component substitution assumed equivalent electrical behavior meant equivalent product behavior.

Third, she asked for owners.

The firmware team owned the product model for calibration status, not the station script. Manufacturing owned the
fixture process, but the fixture could write only through a product API with a defined promise. Hardware owned board
revision encoding and made it readable through a product-level interface rather than through platform-specific probing.
Support owned the service diagnosis vocabulary, but firmware owned the mapping from internal state to support-safe
reason. Release owned the field recovery path, but the product architecture had to make recovery possible without
developer-only tools.

Every API Is a Promise (`LAW-002`) became uncomfortable in a useful way. The calibration script was not "just a script"
if manufacturing depended on it. The service tool state view was not "just debug output" if support used it to decide
whether a customer could stay running. The recovery command was not "just engineering access" if the field plan relied
on it. Each surface promised meaning, timing, errors, and ownership to someone outside the lab.

Fourth, Mara looked for imported dependencies. Every Dependency Is a Decision (`LAW-007`) applied to more than
libraries. The pressure fixture, station script, approved alternate sensor, board revision encoding, label printer,
spreadsheet, service laptop, field cable, and update loader were dependencies now. Each one imported behavior, failure
modes, ownership boundaries, and replacement cost. The team did not need a large dependency program. It needed to name
which dependencies the product architecture had already accepted.

The first temptation was to add a broad manufacturing mode.

One engineer proposed a flag that would unlock calibration bypasses, raw state writes, fixture commands, serial number
changes, and extra logs. It sounded fast. It also sounded like Global Configuration (`ANTIPATTERN-003`) wearing a
factory badge. One setting would affect calibration, identity, logging, update behavior, safety holds, and support
diagnostics across the codebase. It would lower friction for the next two weeks and increase the Change Radius
(`VOCAB-001` and `METRIC-001`) of every future manufacturing and support change.

Mara pushed for smaller surfaces.

Calibration needed a product-owned record with status, version, source, evidence, and validation result. The station
could request calibration, write measurements, and receive a pass or fail reason, but it could not silently create a new
state model. Identity needed an explicit lifecycle: unassigned, assigned, verified, retired. Fixture access needed a
surface available at the point in assembly where the fixture actually ran. Board revision needed a product-level
capability description, not scattered driver checks. Service diagnosis needed a stable vocabulary that mapped internal
state to support-safe reasons. Update recovery needed a field path that did not require a developer laptop. Logs needed
enough persistence to preserve the last useful evidence after reset.

The team recorded the highest consequence choices in an ADR. The smaller evidence gaps went into Decision Journal
entries with review triggers. The first field escape created a Mistake Ledger entry, not to shame anyone, but to preserve
the failed assumption: "If recovery works on a developer laptop, it is field recovery." It was false. They wanted the
next team to find that lesson before repeating it.

They also used Architecture Review (`RITUAL-001`) differently. The review was not a meeting to approve all
manufacturing procedures. It reviewed the architecture surfaces manufacturing and support would depend on: calibration
ownership, identity lifecycle, fixture contract, diagnostic vocabulary, update recovery, and traceability record. When
the pilot build approached, they used Architecture Freeze (`RITUAL-002`) on only a few decisions: the calibration record
shape, service diagnosis vocabulary, identity lifecycle, and recovery contract. The freeze was temporary and named. It
did not freeze learning from the line or the field.

The result was not glamorous. The unit still looked the same. The pump still turned on. The enclosure did not change
much. But the product started to survive places where engineers were absent.

Manufacturing no longer needed to infer whether calibration was valid. The fixture received product-level errors instead
of raw driver codes. A board revision could carry its capability description without leaking HAL Everywhere
(`ANTIPATTERN-002`) through feature code. The service tool no longer displayed only internal states. It showed support
reasons with links to configuration, calibration, hardware, firmware, and environment evidence. Field logs preserved the
last useful trace across reset. Component substitution became a decision with evidence, not a silent assumption. A line
workaround could still happen, but if it changed product behavior it needed an owner, a review trigger, and a removal
condition. Otherwise it was a Temporary Solution (`ANTIPATTERN-006`) becoming permanent in quiet daylight.

The pilot still found problems. Good pilots do. One sensor lot had a narrower stable range than the supplier data sheet
suggested. One support message was too vague. One recovery instruction was hard to follow under time pressure. But those
problems were now visible. They had owners. They had evidence. They had records a future engineer could find.

The product had crossed a boundary the lab could not simulate: it had become architecture for people who were not in the
room when the architecture was designed.

## Discussion

Manufacturing reality and field reality are not late-stage inconvenience. They are design inputs.

A team can build a product that is clean in the lab and still incomplete as architecture. The lab supplies unusual
advantages: knowledgeable engineers, direct access to boards, private tools, flexible timing, forgiving setup, and
people who remember why a strange behavior is acceptable. Manufacturing and field use remove those advantages. They ask
whether the product can be built repeatedly, configured correctly, calibrated safely, identified reliably, recovered
without developers, diagnosed by support, and explained from evidence.

This does not mean the architecture must contain every manufacturing procedure. A principal engineer should not turn the
product design into a factory handbook. The distinction is important:

- Manufacturing process decides how the line runs.
- Product architecture decides what state exists, who owns it, which surfaces can change it, and what evidence proves it.
- Field service process decides how support works with customers.
- Product architecture decides what diagnosis, recovery, traceability, and configuration promises the support process can
  trust.

Designing for manufacturing and field reality means making those architectural obligations explicit before the product
depends on them.

Repeatability is the first pressure. A prototype often succeeds through skilled repetition: the same engineer performs
the same steps until the unit behaves. Manufacturing needs ordinary repetition. The path must tolerate shift changes,
fixture variation, component lots, board revisions, enclosure constraints, and line timing. If a step requires judgment,
the architecture should say which judgment belongs to a person and which should become a product decision with a clear
result.

Calibration is a common example. The dangerous question is not "Can the unit be calibrated?" The better question is
"What does the product know after calibration, who owns that state, how is it validated, and what does the rest of the
system promise about it?" Without that answer, calibration becomes Hidden State (`SMELL-004`). The unit behaves
differently after a sequence that no product model explains.

Identity and traceability create similar pressure. A serial number is not only a label. It connects hardware revision,
component lot, firmware version, configuration, calibration, field history, and support action. If identity is assigned
by spreadsheet, label printer, station script, and firmware cache without one product contract, the product has Silent
Coupling (`SMELL-001`) between surfaces that must change together but are reviewed separately.

Fixture access is also architecture when the product relies on it. A debug connector hidden inside the enclosure is not
a manufacturing detail if calibration, identity, or recovery depends on it after assembly. The architecture does not
need to prescribe the fixture mechanics. It does need to define the product-level contract the fixture uses, where in the
assembly flow that contract is available, and what evidence the fixture must return.

Diagnostics matter because the field is where ambiguity becomes expensive. Developer states are often precise in the
wrong language. They describe implementation, not support action. A support-safe diagnostic surface should help separate
configuration, hardware, firmware, environment, update, and calibration causes. It should preserve enough evidence to
support that separation. It should not require support to remember private firmware meanings.

Update recovery is the same kind of promise. A product is not recoverable because an engineer can recover it. It is
recoverable when the intended support or field path can recover it under realistic access, tooling, time, power, and
network constraints. If recovery requires private tools, direct board access, or undocumented command order, the
architecture has not yet made recovery a product responsibility.

The architecture should resist broad catch-all modes. A single manufacturing flag or field-service flag can look
efficient, but it often creates Global Configuration. It gives one setting too much authority and lets unrelated behavior
change together. That makes Change Radius larger: one adjustment touches calibration, logging, safety, update behavior,
diagnostics, and support scripts. Smaller owned surfaces are usually easier to reason about.

The same restraint applies to platform boundaries. Some low-level details must be visible to manufacturing. Board
revision, sensor capability, timing limits, and fixture access can matter. But if feature code, service tools, and
manufacturing scripts all learn driver vocabulary, Platform Leakage (`SMELL-005`) spreads. If hardware abstraction calls
appear everywhere because "the factory needs them," HAL Everywhere follows. A better design exposes product-level
capabilities and reasons while keeping low-level mechanisms behind the boundary that owns them.

Evidence Before Confidence is especially important here. Lab success is evidence, but it is evidence for lab conditions.
Pilot manufacturing, component substitution, enclosure assembly, field wiring, customer configuration, and support use
need their own evidence. The question is not whether the team is confident. The question is what confidence is based on,
what it does not cover, and what signal will reopen the decision.

Discoverability (`METRIC-003`) becomes a product quality attribute. Manufacturing and support failures are harder when
engineers can find code but not intent. A future maintainer should be able to find the decision, owner, and contract
behind calibration ownership, identity lifecycle, diagnostic vocabulary, recovery path, and traceability record. ADRs,
Decision Journal entries, and Mistake Ledger entries are not paperwork here. They are how the product remains
understandable when the people who improvised the pilot are no longer nearby.

Use an ADR for decisions that affect future architecture, ownership, cost, or reversibility. Use a Decision Journal for
smaller or more reversible choices that still need evidence and review triggers. Use a Mistake Ledger when manufacturing
or field escape reveals a wrong assumption. These artifacts should stay short, linked, and findable. Their purpose is
not to celebrate process. Their purpose is to keep reality attached to architecture.

This chapter also has boundaries. Chapter 22 will go deeper on configuration, variants, and product lines. Chapter 23
will own embedded observability. Chapter 24 will own release discipline and upgrade paths. Chapter 25 will walk through
the reference project. Here the job is narrower: expose the manufacturing and field assumptions the architecture must
make explicit before pilot use depends on them.

## Engineering Principle

Design the product for the places where engineers are absent. Manufacturing and field reality require architecture to
make identity, calibration, configuration, diagnostics, recovery, traceability, and ownership explicit before the product
depends on them.

Use this principle when a design looks ready because it works in engineering but has not yet been tested against repeat
builds, constrained access, support handoff, field recovery, or component variation.

Ask:

1. What state will manufacturing or support depend on?
2. Who owns that state?
3. Which surface is allowed to create, change, validate, or retire it?
4. What does the product promise about calibration, identity, configuration, and recovery?
5. Which assumptions currently live in scripts, spreadsheets, private tools, or team memory?
6. Which field evidence must survive reset, update failure, or loss of connection?
7. Can support separate configuration, hardware, firmware, environment, and calibration causes?
8. What dependency has the manufacturing or field path quietly imported?
9. What is the Change Radius if the assumption is wrong?
10. What evidence exists outside the lab?
11. Where will a future engineer find the owner, contract, decision, and review trigger?

The goal is not to make every edge case perfect before pilot manufacturing. The goal is to prevent the product from
depending on invisible engineering presence.

## Architecture Exercise

### `Expose One Manufacturing or Field Assumption`

Choose one product behavior that currently works in the lab and will matter in manufacturing or the field.

Good candidates:

- calibration or tuning;
- device identity or traceability;
- fixture access;
- service diagnostics;
- update recovery;
- configuration assignment;
- field logs after reset;
- component substitution;
- board revision handling.

Work through the assumption:

1. Describe the lab behavior in one sentence.
2. Name the manufacturing or field condition that changes the behavior.
3. Identify the current hidden assumption.
4. Name the state, dependency, API promise, or evidence gap involved.
5. Decide who owns it.
6. Decide which architectural surface must be added, changed, or made explicit.
7. Define one validation action that would provide evidence outside the lab.
8. Record whether the decision belongs in an ADR, Decision Journal, or Mistake Ledger.

End with:

1. one manufacturing or field assumption;
2. one owner;
3. one architectural surface to add or change;
4. one evidence or validation action.

## Principal's Notebook

- The lab is not the environment.
- Diagnostics matter most when developers are absent.
- A workaround becomes architecture when no one owns it.

## ADR

### Chapter ADR: `Make Calibration and Recovery Product Responsibilities Before Pilot Manufacturing`

#### Status

Accepted for the chapter.

#### Context

The product works in the lab after the prototype-to-product transition. Configuration has a clearer path. The service
tool exists. Updates can be tested by the engineering team. The pilot build is approaching.

The remaining risk is that several product obligations still assume engineering presence. Calibration is performed with
developer-assisted scripts. Update recovery works when a developer laptop and private cable are available. Device
identity is assigned through a spreadsheet and station script. Fixture access relies on a debug connector that may not be
available after enclosure assembly. Service diagnostics expose raw developer states. Field logs may be lost after reset.

Pilot manufacturing and field trial require repeatable calibration, usable fixture access, valid device identity,
support-safe diagnostics, recoverable update paths, and traceability that can be understood away from the lab.

#### Decision

Make calibration ownership explicit in the product architecture. The firmware-owned calibration record will include
status, version, source, validation result, and enough evidence for manufacturing and support to understand whether the
unit is usable.

Provide a manufacturing-safe calibration and setup path. The line fixture may request calibration, submit measurements,
and receive product-level pass or fail reasons through a defined API promise. It may not create a separate hidden state
model.

Define a minimum service-visible diagnostic vocabulary. The service tool will map internal states to support-safe
reasons that distinguish configuration, hardware, firmware, environment, update, and calibration causes.

Make update recovery possible without developer tools. The supported recovery path must work with the intended field or
support access model, not only with private engineering equipment.

Treat device identity and traceability as architecture contracts. The product will define identity lifecycle, ownership,
validation, and the traceability fields needed to connect board revision, component substitution, firmware version,
configuration, calibration, and field evidence.

Record residual assumptions and review triggers. Consequential choices belong in this ADR. Smaller evidence gaps belong
in Decision Journal entries. Manufacturing misses or field escapes caused by wrong assumptions belong in the Mistake
Ledger.

Defer deeper variant management, embedded observability, release discipline, and reference-project examples to later
Part IV chapters.

#### Consequences

Manufacturing can build repeatable units without relying on private engineering judgment. Support can diagnose failures
through product-level reasons instead of raw developer states. Calibration, identity, recovery, and traceability have
owners. Discoverability improves because the decision, contracts, and review triggers are recorded.

The design costs more integration work before pilot manufacturing. Firmware, manufacturing, hardware, support, and
release owners must agree on contracts. The team must gather evidence outside the lab. Some future variant choices will
be constrained by the product-level calibration, identity, diagnostic, and recovery surfaces chosen here.

The trade-off is accepted because hidden manufacturing and field assumptions create larger Change Radius later, when
units are already in customer environments and the cost of ambiguity is higher.

#### Alternatives Considered

Let manufacturing own the workaround.

This is fast locally, but it makes line behavior part of the product without a product owner. It risks Hidden State,
Silent Coupling, and Temporary Solution behavior that survives the pilot.

Keep developer scripts and train the line.

This preserves the lab path but depends on engineering judgment at manufacturing speed. It does not create a product API
promise, support-safe diagnosis, or durable evidence.

Add a broad manufacturing mode.

This reduces immediate friction but concentrates authority in one global flag. It risks Global Configuration, larger
Change Radius, and unrelated behavior changing together.

Postpone service diagnostics until after field trial.

This lets the team ship the pilot faster but makes field learning weaker. Support may be unable to separate
configuration, hardware, firmware, environment, update, and calibration causes.

Rely on release notes and support training.

This helps people, but it cannot replace product-level diagnosis, recovery, identity, calibration ownership, or
traceability. It also depends on memory when the product needs discoverable contracts.

Rework the full architecture before pilot.

This may reduce risk, but it is too broad for the current evidence. The better decision is to make the manufacturing and
field obligations explicit now, freeze only the high-risk contracts needed for pilot, and keep learning from the line
and field.

## Editor's Commentary

This chapter begins the second movement of Part IV. Chapter 20 moved the reader from prototype to product by turning
prototype assumptions into owned product decisions. Chapter 21 asks what happens next: whether those decisions survive
manufacturing and field reality when engineers are no longer present.

The chapter intentionally has no primary PEAK concept and introduces no new concept. Its force comes from applying the
existing relationship set to a product moment: Every State Has One Owner (`LAW-001`), Every API Is a Promise
(`LAW-002`), Evidence Before Confidence (`LAW-005`), Every Dependency Is a Decision (`LAW-007`), Change Radius
(`VOCAB-001` and `METRIC-001`), Discoverability (`METRIC-003`), ADR (`ARTIFACT-001`), Decision Journal
(`ARTIFACT-003`), Mistake Ledger (`ARTIFACT-004`), Architecture Review (`RITUAL-001`), Architecture Freeze
(`RITUAL-002`), Temporary Solution (`ANTIPATTERN-006`), Hidden State (`SMELL-004`), Silent Coupling (`SMELL-001`),
Platform Leakage (`SMELL-005`), HAL Everywhere (`ANTIPATTERN-002`), and Global Configuration (`ANTIPATTERN-003`).

The boundary is deliberate. This is not a manufacturing handbook, field-service manual, fixture-design guide,
observability chapter, or release-process chapter. It is an architecture chapter about making manufacturing and field
assumptions explicit before the product depends on them. Chapter 22 can now take up configuration, variants, and product
lines with a grounded product context. Chapter 23 can go deeper on embedded observability. Chapter 24 can handle release
discipline and upgrade paths. Chapter 25 can bring the reference project together.
