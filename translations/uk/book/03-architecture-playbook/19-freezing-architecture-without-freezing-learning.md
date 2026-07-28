# Заморожування архітектури без заморожування навчання

## Вступна цитата

> Freeze має зупиняти uncontrolled movement, а не здатність system learning.

## Історія

Team later called it The Freeze That Froze the Wrong Thing. Product was close to release validation: firmware, gateway, service tool, manufacturing fixtures, QA validation, support diagnostics and release plan.

Configuration update protocol had become clear. RFC moved through review. Architecture Review challenged decision before hardening. Accepted direction: device owns validation, gateway validates framing only, service tool translates product-level rejection reasons, station-only metadata outside payload, recovery distinguishes accepted/rejected/partially applied/interrupted profiles.

Records were better: RFC with review outcome, ADR draft waiting for validation evidence, Architecture Ledger row, old gateway tests started, service-tool messages drafted, manufacturing fixture branch ready.

Release validation approached. Release ??????? said: architecture is frozen. Everyone wanted stability. Firmware wanted protocol to stop moving so tests mattered. Gateway wanted adapter stability. Manufacturing needed scripts stable. QA needed matrix steady. Support needed diagnostic wording. Release needed convergence.

Sentence felt responsible. It was too vague to be architecture.

Firmware interpreted freeze as no protocol changes. Gateway as no adapter API changes. Service tool kept changing validation logic because UI did not feel like architecture. Manufacturing treated fixture compatibility fix as allowed. Support held recovery wording issue for next release. QA found old gateway evidence and nobody knew whether it was bug, exception, release blocker or reason to reopen decision.

Same freeze had six meanings. Some people stopped learning; others kept changing architecture under safer names.

QA brought old gateway finding. Conversation became «can we break freeze?» versus «can we ignore evidence?». Principal Engineer asked:

> Which named decision is frozen, what evidence changed, and does this require an exception, implementation correction, or revalidation?

They had not frozen a decision. They had frozen a mood.

Team named stable decisions: configuration protocol ???? for release validation; service-tool promise about product-level rejection reasons; persistent profile format version; migration path for old service tools.

Then they named ?????????? ???. Firmware could fix defects inside accepted ????, add tests, improve diagnostics that did not change semantics, roll back unaccepted parser optimization. It could not change acceptance authority, format meaning, compatibility promise or recovery behavior without exception. Gateway could fix forwarding defects preserving framing-only role. Service tooling could improve presentation but not change product-level reasons. Manufacturing could fix scripts inside accepted package format but not invent station-only payload field.

QA, support and manufacturing could continue learning. Field evidence was not violation of freeze; it was reason freeze needed ???? ???????.

Exception had to name frozen decision affected, evidence, risk of changing, risk of not changing, affected ????????, validation required, rollback/containment, approving ???????, record updates and whether freeze scope changed.

Old gateway finding became first test. Evidence did not change device-owned validation. It showed one old gateway inspected length field before forwarding, violating release-compatible API promise assumption. Issue was larger than firmware bug and smaller than new architecture.

Exception proposal: allow gateway compatibility adapter for that release line, preserve device-owned validation ????, add compatibility test, update RFC and Architecture Ledger, require revalidation if another old gateway release showed same behavior.

Support finding took different path: unclear diagnostic phrase for partially applied profiles. Team allowed documentation/service-tool wording fix because it did not change frozen decision, and added Decision Journal entry.

Service-tool validation change changed product-level rejection meaning. Team stopped it until ??????? kept it inside current promise or requested exception.

By meeting end, release ??????? still had freeze, but not slogan. It had named decisions, ????????, ?????????? ???, evidence thresholds, exception authority, records and exit criteria.

Team did not make late change easy. It made necessary learning possible.

## Обговорення

Architecture Freeze is not ban on change. It is temporary stabilization of named architectural decisions during high-risk phase.

It is not code freeze, feature freeze, branch freeze or release freeze. Those stabilize different objects. The danger is phrase «architecture is frozen». Without named decision, people freeze different surfaces or keep moving structure under bug fixes.

`RITUAL-002`, Architecture Freeze, stabilizes architectural decisions during risky phase. `VOCAB-006` emphasizes temporary pause on architectural change while team stabilizes product or decision. Useful only with explicit exit criteria.

Temporary matters. Named decision matters. Exit criteria matter.

Start with decision being frozen. Bad subjects: freeze architecture, backend, protocol work, everything. Good subjects: accepted protocol ????, calibration data ownership, update recovery authority, persistent format version, compatibility behavior, dependency version assumption, migration path.

Next question: what remains allowed. ?????????? ??? may include bug fixes inside frozen ????, tests, diagnostics, docs, validation, rollback of unaccepted implementation detail or compatibility fixes preserving decision.

`LAW-001`, `LAW-002` and `LAW-007` become freeze lenses. If fix moves state authority, changes API promise or invalidates dependency assumption, it changes frozen decision.

Change Radius helps decide exception weight. Keep small exception small and broad exception honest.

Exceptions are part of freeze design. Treat exception as controlled answer to evidence, not moral failure. It names frozen decision, evidence, risks, ????????, validation, rollback/containment, approving ???????, record updates and scope change.

Evidence Before Confidence (`LAW-005`) is freeze posture. Validation, compatibility, manufacturing findings, support observations, security findings, measurements, diagnostics and field feedback are learning channels that tell whether freeze is still true.

Learning during freeze may lead to implementation correction, Decision Journal entry, exception/revalidation, changed exit criteria or record update. Useful freeze does not collapse all into allowed/forbidden.

Freeze differs from Architecture Review. Review challenges decision before hardening. Freeze begins after selected decisions need stability. Review approval does not automatically create freeze.

Records keep freeze discoverable: RFC (`ARTIFACT-002`), ADR (`ARTIFACT-001`), Decision Journal (`ARTIFACT-003`) and Architecture Ledger (`ARTIFACT-006`). Discoverability (`METRIC-003`) matters because freeze hidden in chat is not shared architecture.

Exit criteria keep freeze from becoming architecture by neglect. Revalidation is scoped check that frozen decision, assumptions and criteria still hold.

Use Architecture Freeze when instability itself has become system risk: protocols, persistent formats, APIs, dependencies, ownership decisions, compatibility commitments, ????, recovery assumptions and long support costs. Freeze the decision, not curiosity.

## Інженерний принцип

Freeze named architectural decisions, not learning. Define scope, ???????, ?????????? ???, ???? ???????, evidence threshold and exit criteria so stability protects next phase without hiding evidence.

Questions:

- Which decision is frozen?
- Why does it need stability now?
- Who owns freeze?
- What can still change?
- What evidence justifies exception?
- Who approves exception?
- Which records must be updated?
- What is exit condition?
- Which learning channels remain open?
- What happens if evidence invalidates decision?

## Архітектурна вправа

### Freeze One Decision Without Freezing Learning

Choose one architectural decision approaching high-risk phase. State frozen decision. Document governing record, freeze ???????, affected ????????, reason for stability, start/exit conditions, allowed implementation changes, disallowed architecture changes, ???? ???????, evidence threshold, validation, learning channels, communication surface, artifact updates, revalidation trigger and residual risk.

End with named frozen decision, ???????, allowed-change rule and exception/revalidation trigger.

## Нотатник Principal Engineer

- Freeze decisions, not curiosity.
- ???? ??????? is part of freeze.
- Vague freeze creates hidden architecture changes.

## ADR

### Chapter ADR: Freeze the Configuration Protocol ???? Through Release Validation

#### Status

Accepted.

#### Context

Configuration update protocol ???? has been reviewed. Firmware, gateway behavior, service tooling, manufacturing fixtures, QA validation, support diagnostics and release planning depend on it.

Accepted direction: device owns configuration acceptance, gateway validates framing only, service tool presents product-level rejection reasons, station-only metadata stays outside payload, and recovery distinguishes accepted, rejected, partially applied and interrupted profiles.

Validation and compatibility testing underway. Uncontrolled protocol or ownership change would invalidate tests/tooling. Field evidence may still reveal defects or invalid assumptions.

#### Decision

Freeze named configuration protocol ???? and ownership decision through release validation.

Implementation fixes may continue when they preserve frozen decision. Tests, diagnostics, compatibility evidence, presentation improvements, fixture fixes inside accepted format and docs corrections remain allowed.

Require exception for changes to protocol semantics, validation ownership, persistent format meaning, release-compatible API promise, migration path, dependency assumption in compatibility matrix or recovery-policy behavior.

Product architecture ??????? owns freeze. Exceptions require evidence, risk of changing/not changing, affected ????????, validation, rollback/containment, approving ??????? and record updates. Update RFC, ADR, Decision Journal or Architecture Ledger as appropriate. Keep learning channels active.

Freeze exits when release validation completes, compatibility evidence closes, manufacturing rehearsal passes, recovery behavior is validated and product architecture ??????? accepts final ADR or records revised freeze.

#### Consequences

Team gains stable validation and clearer compatibility promises. Affected teams know ?????????? ??? and ???? ???????. Evidence-driven correction remains visible. Cost is explicit exception handling and repeated record updates.

#### Alternatives Considered

- Do not freeze. Validation chases moving architecture.
- Freeze all code. Blocks useful fixes and evidence.
- Freeze only branch/release artifacts. Does not name architecture decision.
- Route every change through Architecture Review. Too heavy for ?????????? ???.
- Allow team-local exceptions. Dangerous across broad Change Radius.
- Postpone freeze until after validation. Evidence would measure several architectures.
- Treat field findings as post-release work. Invalidating evidence must trigger exception or revalidation.

## Коментар редактора

Chapter 19 closes Part III by turning reviewed architecture into controlled stability without closing learning. It illustrates Architecture Freeze (`RITUAL-002`) and `VOCAB-006`, with Architecture Review (`RITUAL-001`) as predecessor. ADR (`ARTIFACT-001`), RFC (`ARTIFACT-002`), Decision Journal (`ARTIFACT-003`) and Architecture Ledger (`ARTIFACT-006`) keep freeze scope and exceptions discoverable. Laws and metrics keep it concrete: `LAW-001`, `LAW-002`, `LAW-005`, `LAW-007`, Change Radius (`VOCAB-001`, `METRIC-001`) and Discoverability (`METRIC-003`).
