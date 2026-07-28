# Ownership поза кодом

## Opening Quote

> Ownership завершується тоді, коли outcome може стояти без owner у кімнаті.

## Story

Diagnostic command почалася як manufacturing convenience.

Під час production fixture надсилав command to device, чекав response і вирішував, чи unit може перейти до next station. Command була small: status bits, counter і compact result code про calibration check.

Для першої product revision цього вистачало.

Потім product entered field.

Field service почав використовувати той самий diagnostic path через service tool. Support liked it, бо це зменшувало guesswork. Manufacturing already had command. Firmware had tests. Release engineering did not need new protocol. Tool team reused existing command.

Nothing looked reckless.

Diagnostic command moved from factory detail into product workflow.

Через два роки firmware change зробив command more precise. Old implementation returned «ready», коли calibration check had completed enough work for manufacturing fixture. New implementation returned «ready» only after longer internal verification. Change was reasonable: firmware team saw rare field cases where earlier result was too optimistic for service use.

Firmware ticket closed with tests. Service application updated for longer wait. Manufacturing kept older command sequence because fixture image had not moved to new service-tool library. Release packaged both firmware versions. Support updated troubleshooting page.

Each local owner did something sensible.

End-to-end workflow was still not owned.

Перший sign був release candidate, який ніхто не хотів sign. Service tool could not reliably determine diagnostic behavior. Response shape same in both firmware versions. Result code meant «manufacturing-ready» in one version and «service-ready» in another. Timeout sufficient for old fixture too short for new completion condition. Long timeout slowed older service sessions.

Meetings became familiar:

«Firmware owns the command.»

«Tools owns the service application.»

«Manufacturing owns the fixture.»

«Support owns the procedure.»

«Release owns packaging.»

All true. None answered release question:

«Who owns safe execution of the supported diagnostic workflow across manufacturing and field service?»

Principal Engineer became the person everyone asked. She knew history, shipped versions, fixture images, and why behavior had changed. For a while, that helped. She answered questions, reviewed tool changes, joined release meetings, approved exceptions, corrected old tickets.

Work moved again.

That was warning sign.

System looked safer because Principal Engineer stood at every crossing point. In reality ownership model became fragile. Local decisions waited for her interpretation. Tool, manufacturing, support, and release depended on her memory.

Team escaped one ownership gap by creating another.

Nobody owned complete outcome, so one expert became routing path.

By third release meeting, Principal Engineer stopped answering next compatibility question and wrote:

«The owned outcome is safe for the supported diagnostic workflow, versioned, and supportable across manufacturing and field service.»

Then asked:

«Who is responsible for making that outcome reach closure?»

Not who writes every patch. Not who approves every exception. Not who owns every component.

Who owns the closure?

The room did not become simpler. Firmware, tools, manufacturing, support, and release kept their component ownership. Але missing object finally had a name.

## Discussion

Local completion is not system closure.

Ticket can be closed, test pass, tool updated, procedure published, release packaged — and outcome still unowned.

Diagnostic story не failed because teams careless. Responsibilities were shaped around components while product consequence crossed components. Firmware completed command change. Tools updated application. Manufacturing kept fixture working. Support updated guidance. Release packaged valid images. Local work was real.

Workflow was not closed.

Closure означала supported behavior across firmware versions, understandable service tool, compatible manufacturing migration, explainable support, and release rules future engineers could find.

No component owner could produce that alone.

Component ownership necessary. Firmware behavior, fixture behavior, tool behavior, support procedure, and package rules each need owners. Mistake is assuming local owners automatically compose into complete outcome ownership.

Boundary that matters for ownership is not always org chart or repository layout. Diagnostic workflow lived in firmware, tooling, manufacturing, support, and release. Its risk lived between them.

Ownership starts by naming the thing owned.

«Firmware owns diagnostics» is too wide and too narrow. «Tools team owns it» also incomplete. «Support owns field use» cannot own firmware command semantics.

Bounded ownership statement looks different:

«Own safe execution of the supported diagnostic workflow across manufacturing and field service.»

It names an outcome and gives ownership shape. It also prevents ownership from becoming infinite.

Outcome ownership is not component ownership. Owner of closure does not replace firmware lead, tool lead, manufacturing engineer, support owner, or release engineer. A cross-domain workflow cannot safely depend on one universal implementer.

Outcome owner ensures closure happens. Component owners still own their parts.

Many ownership failures come from two bad options: every team owns only local component and outcome emerges by hope; or one expert becomes responsible for everything crossing boundary. First leaves gaps. Second creates bottleneck and hides missing contracts behind capable person.

Better model separates responsibility for closure from implementation. Outcome owner keeps bounded result visible. Component owners keep local correctness visible. Interface owners keep promises explicit. Risk owners keep accepted risk from fading.

Assignment and acceptance diverge. A handoff is not complete because ticket moved, note says «tools to handle», or org chart implies. Assignment says where work was sent. Acceptance says receiving owner understands bounded concern, current state, interface contract, uncertainty, consequences, closure condition, and ability to act or escalate.

Without acceptance, responsibility can be in transit for months.

Interfaces carry ownership across boundaries. Diagnostic command had command ID, response shape, result code, timing expectations. Real promise included what «ready» meant, which versions support which meaning, capability detection, error meaning, wait time, and when old behavior can be removed.

That is Every API Is a Promise (`LAW-002`) across teams.

Workflow also had state: whether device supported new semantics, fixture migrated, release package supported. Every State Has One Owner (`LAW-001`) applies because these states affect behavior. If no one owns capability truth, each consumer infers it. If no one owns migration state, release planning guesses.

Undocumented meanings create Silent Coupling (`SMELL-001`). Fixture, service tool, support procedure, and release gate all depend on same diagnostic meaning.

Accepted risk also needs ownership. Writing «known risk» in release note is not enough. Useful accepted risk has statement, reason, owner, consequences, and trigger for review or expiry.

Closure should be named before work fragments. For diagnostic workflow closure might include agreed command semantics, explicit behavior for old and new firmware, service-tool capability handling, manufacturing migration, support procedure alignment, release compatibility checks, named residual risks, accepted handoffs, and evidence across supported combinations.

Closure must be observable. Outcome owner should not declare closure because room feels aligned. Closure needs tests, compatibility table, fixture migration record, release gates, support procedure tied to firmware behavior, and maintained Architecture Ledger (`ARTIFACT-006`) or another discoverable record.

The Hero Engineer (`FAILURE-004`) is failed ownership architecture. It looks useful: senior person helps every team and keeps release moving. Sometimes necessary. It becomes debt when system only works through that person's memory.

Private memory replaces explicit contracts. Intervention replaces owned interfaces. Availability replaces Discoverability (`METRIC-003`). Bus Factor (`METRIC-002`) falls.

Answer is not caring less. It is moving care into system.

Principal Engineer in story did useful work by naming outcome and ownership gap, then stepping out of permanent routing path. She helped assign one owner for closure, kept component owners in place, made interface semantics, capability behavior, migration state, accepted risks, handoffs, and closure evidence explicit.

Own the closure, not all the work.

## Engineering Principle

Ownership is responsibility for making a bounded outcome reach visible closure across boundaries.

Thing owned is not every task near outcome. It is the outcome itself: diagnostic workflow, release property, compatibility promise, migration, supportability condition, or another consequential bounded concern.

Closure means concern reached a state that can be observed and explained. Work is done or intentionally deferred. Remaining risks named. Handoffs accepted. States and interface promises have owners. Evidence exists. Record is discoverable.

Implementation remains distributed. Outcome owner does not absorb component responsibilities. Outcome owner ensures they compose into result product can support.

Ownership survives beyond one person when future engineers can find owner, contract, decision, risk, handoff, and evidence without reconstructing them from old meetings.

That is ownership beyond code.

## Architecture Exercise

Map an ownership gap from your current or recent work.

Choose concern crossing at least two boundaries: firmware and tools, product and manufacturing, release and support, hardware and software, platform and application, or similar.

Write short answers:

1. The exact bounded outcome.
2. Where responsibility currently fragments.
3. The relevant component owners.
4. The owner of authoritative state.
5. The owners of interface promises.
6. Unresolved decisions and their decision paths.
7. Accepted risks.
8. Risk owners.
9. Handoffs that are assumed but not accepted.
10. Observable closure evidence.
11. Where ownership, decisions, contracts, and risks are recorded.
12. Whose absence currently blocks safe progress.
13. Who should ensure closure without absorbing all implementation work.

End with:

What is currently assigned, but not truly owned?

## Principal's Notebook

- Assignment is not acceptance.
- Closure without evidence is only a claim.
- Private memory is not an ownership model.

## ADR

### Chapter ADR: Assign End-to-End Ownership for the Diagnostic Workflow

### Context

Diagnostic workflow crosses firmware, manufacturing, service tooling, support, release packaging, and compatibility rules. Each component has local owner, but no one owns supported behavior, compatibility, migration, supportability, and closure of complete workflow.

Command semantics differ across firmware versions. Service tool cannot reliably determine capability in all cases. Manufacturing depends on older sequence. Support lacks complete compatibility rule. Deprecation and residual risk are scattered. Principal Engineer became informal source of truth for decisions that should be owned by system.

### Decision

Assign one owner responsible for end-to-end closure of diagnostic workflow.

This owner maintains bounded product-level outcome, coordinates closure criteria, ensures command and compatibility semantics have explicit owners, keeps remaining risks visible, ensures handoffs accepted, makes decisions and contracts discoverable, and verifies agreed closure evidence exists and remains current.

Component teams retain implementation responsibility for firmware, tools, manufacturing fixtures, support procedure, and release packaging.

### Consequences

- Product-level responsibility becomes explicit.
- Component ownership remains distributed.
- Compatibility and lifecycle commitments become visible.
- Cross-boundary gaps can be found before release approval.
- Dependence on private memory is reduced.
- Bus Factor and Discoverability improve.
- Outcome owner takes on coordination and record-maintenance work.
- Boundaries may require negotiation.
- Outcome owner can become approval bottleneck if role replaces component judgment.
- Ownership should be revisited when product, lifecycle, or organizational boundaries change.

### Alternatives Considered

- Leave ownership distributed only by component.
- Make Principal Engineer approve or implement every cross-boundary change.
- Treat ticket assignment as sufficient ownership.
- Add coordinator without changing technical ownership.
- Wait for integration or field failure to expose gap.

## Editor's Commentary

Chapter 3 showed how better questions expose assumptions, boundaries, evidence needs, and ownership gaps before team commits to wrong explanation. Chapter 4 begins after gap visible. It asks how bounded concern reaches durable closure without pretending one person should do or remember everything.

Chapter avoids general management or org-chart advice because handbook concerns engineering decisions and architecture. Ownership here is not status. It is system property: right people can find outcome, owners, contracts, accepted risks, handoffs, and evidence.

Evidence appears because closure should be observable. Next chapter asks whether evidence is strong enough.

Chapter uses existing PEAK concepts rather than creating new ownership law. Every State Has One Owner (`LAW-001`), Every API Is a Promise (`LAW-002`), Silent Coupling (`SMELL-001`), The Hero Engineer (`FAILURE-004`), Bus Factor (`METRIC-002`), Discoverability (`METRIC-003`), and Architecture Ledger (`ARTIFACT-006`) carry the canon.
