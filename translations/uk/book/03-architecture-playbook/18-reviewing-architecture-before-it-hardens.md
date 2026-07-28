# Перегляд архітектури до того, як вона затвердіє

## Вступна цитата

> Review useful лише тоді, коли decision can still change.

## Історія

Team later called it The Review That Could Only Approve. It had calendar invite, deck and answer.

Team changing configuration update path for long-lived embedded product. Profiles were no longer simple key/value files. New variants needed schema versions, product-level validation, rejection reasons and compatibility across firmware, gateway, service tool, manufacturing fixtures and field support.

Direction seemed obvious after Chapter 17 work. RFC existed: device owns configuration validation, gateway validates framing only, service tool translates device rejection reasons into product messages. ADR draft waited for decision to close.

Nobody thought review was skipped. Firmware branch compiled. Gateway adapter forwarded envelope behind feature flag. Service-tool screen existed. Manufacturing fixture was changing. Tests encoded device-owned validation. Release assumed path would land before field-service rehearsal.

Architecture Review was scheduled after concrete work existed. That was not laziness; it was sign that review timing and review subject had drifted apart.

First slides were tidy: approve versioned configuration protocol. Then questions arrived. Gateway ??????? asked about old gateways and historic length limit. Service-tool ??????? asked which rejection reasons were stable product messages. Manufacturing asked where station metadata belonged. Support asked how technician would distinguish incompatible firmware, invalid variant and temporary recovery state. Test asked old firmware/gateway matrix. Release asked why rollback looked small when Change Radius included tools and fixtures.

Each question was reasonable. None fit «open comments».

Decision was not only packet layout. It was validation authority, API promise, state ownership, dependency decision and failure/recovery decision. Review room discovered this after implementation made answers expensive.

First response was approve direction and track concerns as follow-up tickets. That sounded responsible, but tickets would start after decision crossed next ????? ???????????. Another response was more reviewers next time. But vague review subject would still be wrong object. Longer meeting would only negotiate around hardened decision.

Principal Engineer wrote:

> What is still changeable, what has already hardened, and what evidence must exist before the next irreversible step?

Team separated decision pieces. Packet envelope mostly changeable. Device-owned validation partly hardened because tests encoded it. Gateway framing unsettled because old gateway evidence weak. Service-tool vocabulary changeable before translation freeze. Manufacturing packaging changeable but needed answer soon. Release compatibility not reviewable because matrix unnamed.

Actual review subject became: whether configuration update protocol may harden around device-owned validation before old gateway forwarding, service-tool rejection semantics, manufacturing package ???? and recovery behavior have enough evidence.

Decision ??????? was product architecture ???????. Proposal ??????? remained firmware lead. Reviewers chosen by affected surface: firmware, gateway, service tool, manufacturing, test, support, release and future maintainer. Facilitator helped close review without becoming decision ???????.

Change Radius (`VOCAB-001` and `METRIC-001`) changed participant list. Decision touched code, tests, fixture scripts, release notes, support diagnostics, compatibility rehearsal and Architecture Ledger.

Evidence split into groups: strong enough (device parses/rejects happy path), missing but obtainable (old gateway forwarding, old firmware rejection, service-tool translation, fixture handling), and not blocker if owned (station-only metadata outside payload with Decision Journal trigger).

Outcome was not simply approved or blocked:

- proceed with envelope shape for firmware work that creates no compatibility promises;
- change service-tool ???? so product-level rejection reasons are stable and raw firmware diagnostics stay diagnostic;
- request old gateway and old firmware evidence before merging protocol ???? tests;
- keep station-only metadata outside device payload until manufacturing evidence exists;
- record recovery behavior before release rehearsal;
- update RFC with review outcome;
- write ADR only after compatibility evidence closes;
- add Architecture Ledger row with ???????, status, related RFC, pending evidence and review date.

Team left with more work and better decision: one that could still improve before it became expensive to move.

## Обговорення

Architecture Review is not approval after implementation. It is structured challenge to consequential decision while evidence, alternatives, ????, risks and consequences can still change outcome.

Decision hardens when system begins to depend on it: code, tests, formats, protocols, tools, release plans, staffing, customer commitments, compatibility promises and rollback cost. Alternatives may still exist in language but become economically fake.

Review becomes approval theater when questions arrive after movement is embarrassing or expensive. Comments become wording suggestions, missing evidence becomes ticket, risks are acknowledged but not owned.

First useful question is review subject. «Review the design» too vague. Subject should name decision, ???????, proposal ???????, affected ????????, decision state, scope, non-goals, alternatives, evidence, assumptions, risks, Change Radius, consequences, unresolved questions, deadline, reversibility and records to update.

Too early review argues with fog. Useful review sits between fog and hardened fact.

Participants follow affected architecture, not hierarchy. Decision ??????? accountable for outcome. Proposal ??????? carries proposal. Reviewers bring affected-surface ownership or relevant experience. Facilitator closes review without owning decision by accident.

Consensus can help, but is not proof. Disagreement is useful when it exposes missing evidence, hidden ????????, incompatible constraints or unpriced consequences.

Evidence Before Confidence (`LAW-005`) is review posture. Separate evidence from assumption, preference, product constraint, operational constraint, uncertainty and accepted risk.

Earlier laws become lenses: `LAW-001` asks about state authority; `LAW-002` asks what consumers may rely on; `LAW-007` asks what behavior system now depends on; Change Radius identifies affected surface; Chapter 16 failure/recovery asks what state is authoritative after interruption.

Review input can be lightweight: RFC (`ARTIFACT-002`), ADR draft (`ARTIFACT-001`), Decision Journal (`ARTIFACT-003`), diagram, evidence summary, Change Radius map, ??????? list and compatibility matrix. This chapter does not introduce new artifact; point is challenge.

Good outcomes include proceed, proceed with changes, narrow scope, split decision, request evidence, ask experiment, change ownership, revise ????/????????, defer, reject, escalate risk, record accepted risk or update records.

Comments are not closure. Closure turns conversation into owned change, evidence request, accepted risk, deferral, escalation or record update. Concern without ??????? is decoration.

Architecture Review differs from Chapter 17 artifacts and Chapter 19 freeze. RFC Friday can feed review; it does not replace review when broad Change Radius or expensive reversal must be challenged.

Not every choice needs ritual. Practice is proportional and useful because it protects moment when architecture can still learn.

## Інженерний принцип

Review architecture while decision can still change. Name decision, ???????, evidence, alternatives, risks and ????? ???????????; then close review into decision, evidence request, accepted risk or revised proposal.

Questions:

- What decision is hardening?
- Who owns it?
- Who is materially affected?
- What would make team choose differently?
- Which ????, state, API, dependency, failure path or Change Radius changes?
- Which evidence supports it?
- Which evidence is missing?
- Which alternatives remain real?
- What risk is accepted?
- What must change before next irreversible step?
- What artifact preserves outcome?

## Архітектурна вправа

### Review One Decision Before It Hardens

Choose one pending architecture decision whose direction is starting to shape code, tests, tools, data, release plans or commitments.

Document current decision state, next ????? ???????????, ???????, proposal ???????, affected ????????, RFC/ADR/Decision Journal link, affected ????/state/APIs/protocols/dependencies, Change Radius, evidence available/missing, assumptions, alternatives, non-goals, failure/recovery, compatibility, participants, questions that could change decision, possible outcomes, closure artifact and follow-up ???????.

End with one reviewable decision statement, one decision ???????, one ????? ??????????? and one review outcome or evidence request.

## Нотатник Principal Engineer

- Review useful only while decision can still change.
- Concern without ??????? is decoration.
- Approval is weaker than recorded outcome.

## ADR

### Chapter ADR: Hold Architecture Review Before Configuration Protocol Hardening

#### Status

Accepted.

#### Context

Configuration update protocol affects firmware, gateway, service tooling, manufacturing tests, support diagnostics, compatibility and release. RFC exists; ADR draft waits for accepted decision.

Implementation has begun. Firmware accepts new envelope. Gateway forwards behind feature flag. Service-tool UI and manufacturing fixtures assume preferred ????. Tests encode device-owned validation.

Affected ???????? still have unresolved concerns: old gateway forwarding, product-level rejection semantics, station package handling, old firmware/gateway matrix and diagnostic wording.

#### Decision

Hold Architecture Review before next irreversible implementation step. Review actual protocol and ownership decision, not whole project. Use RFC as input. Review evidence, assumptions, alternatives, Change Radius, compatibility, failure/recovery and ??????? ????.

Classify findings as accepted changes, evidence requests, accepted risks, split decisions or blockers. Update RFC. Write final ADR only after required evidence closes. Proceed only for parts whose assumptions survived review. Record follow-up ???????? and triggers in Architecture Ledger.

#### Consequences

Alternatives stay real longer. Ownership and ???? problems can be corrected before tests/tools/release plans harden them. Evidence gaps visible before compatibility promises. Cost is preparation, possible delay and follow-up ownership.

#### Alternatives Considered

- Continue implementation and review later. Hardens decision before review can change it.
- Use code review only. Too narrow for architecture risk.
- Require Architecture Review for every related decision. Overloads ritual.
- Ask for more sign-offs. Process without evidence.
- Move decision to standing board. May detach accountability.
- Let RFC Friday handle risk. Useful but not substitute for review.
- Freeze immediately. Decision not ready for freeze.

## Коментар редактора

Chapter 18 follows Chapter 17: records expose a decision that must face challenge before implementation turns it into fact. It is carried by Architecture Review (`RITUAL-001`) and supported by ADR (`ARTIFACT-001`), RFC (`ARTIFACT-002`), Decision Journal (`ARTIFACT-003`), Architecture Ledger (`ARTIFACT-006`), RFC Friday (`RITUAL-006`), `LAW-001`, `LAW-002`, `LAW-005`, `LAW-007`, Change Radius (`VOCAB-001`, `METRIC-001`) and Discoverability (`METRIC-003`).
