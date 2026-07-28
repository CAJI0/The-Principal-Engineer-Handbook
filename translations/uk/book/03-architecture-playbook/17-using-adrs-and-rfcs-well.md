# Як добре використовувати ADR і RFC

## Вступна цитата

> Record useful лише тоді, коли preserves reasoning, яке знадобиться після того, як room його забуде.

## Історія

ADR виглядав responsible. Team changing configuration updates for embedded controller: firmware image, gateway, service tool, manufacturing tests, release packaging and support workflow. Old command was simple: send profile, validate on device, store, show result.

Old command became too small. New variants needed schema versions, validation rules, compatibility markers and safe rejection for older firmware. Manufacturing wanted same profiles at end of test. Support wanted rejection reasons. Release needed old gateway behavior. Firmware wanted to start with plausible protocol without turning project into meeting.

Engineer opened ADR titled:

```text
Use Versioned Configuration Updates
```

Context said old command could not represent rules. Decision said add versioned update protocol. Consequences said firmware, gateway and tooling would change. It had headings, status and alternatives. It was not careless. It was too late to be first review artifact.

Implementation had begun: firmware branch with packet layout, gateway parser behind feature flag, service tool screen, manufacturing not reviewed, support not seen rejection reasons, release not checked old gateways, test team had one sample profile.

Reviewers commented. Questions touched profile/configuration vocabulary, field names, gateway validation, service-tool translation, manufacturing scope, support diagnostics and release compatibility. ADR grew into alternatives, implementation plan, migration plan, comments and responses. People stopped reading carefully.

Someone suggested renaming ADR to RFC. Principal Engineer asked: is this still proposal, or are we documenting a decision implementation already made?

For firmware decision felt almost made. For manufacturing it was open. For service tool semantics were unclear. For release assumptions missing. For support diagnostic promise unnamed. Same file tried to be two artifacts: RFC for people with evidence to add and ADR for choice firmware branch had started making.

Principal Engineer drew:

```text
Question -> Proposal -> Decision -> Record
```

Side paths:

```text
Smaller judgment -> Decision Journal
Active decision -> Architecture Ledger
```

Team split work. Existing ADR stopped pretending accepted. Live question moved into RFC with narrow proposal: change configuration-update protocol so profiles carry schema version, validation result and product-level rejection meaning across firmware, gateway, service tool, manufacturing and support.

RFC named non-goals: not redesign entire configuration system, not define every variant, not replace service tool, not decide rollout, not teach gateway to own configuration truth, not require station to understand private firmware layout.

Reviewers asked sharper questions. Firmware owned proposal; product architecture owner owned eventual decision. Required reviewers named by affected surface: firmware, gateway, service tool, manufacturing, test, support and release. RFC listed evidence and assumptions.

At RFC Friday (`RITUAL-006`), team walked open questions. Old gateway release inspected length field. Raw firmware errors leaked into exports. Station profiles came from different source. Compatibility tests needed old gateway and old firmware versions. RFC changed direction: device remained validation authority; gateway validated framing only; service tool translated product-level reasons; manufacturing used same package format, with station-only metadata outside payload.

Release compatibility risk went to Architecture Review. RFC did not become the ritual; it carried proposal and open question into right review.

After compatibility closed, ADR became useful. New ADR linked RFC and recorded accepted decision, evidence, rejected alternatives, consequences, owner, status and revisit trigger. Smaller choices went to Decision Journal (`ARTIFACT-003`). Architecture Ledger (`ARTIFACT-006`) got row for active protocol decision.

Future engineer could start at service-tool rejection message, find governing ADR, RFC, compatibility tests and owner. That was shared memory, not documentation for its own sake.

## Обговорення

ADRs and RFCs work when they make architectural reasoning reviewable before commitment and discoverable after commitment.

RFC is useful while meaningful change is still possible. It exposes motivation, scope, non-goals, proposal, risks and open questions so affected owners can add evidence before rejection becomes theater.

ADR is useful when material architectural decision has been accepted. It records what was decided, why, rejected alternatives and accepted consequences.

Decision state matters: question, proposal, evidence gathering, accepted, rejected, narrowed, deferred, split, reversible local judgment, superseded, retired. These are chapter-local words to stop template from making decision look more mature than it is.

Document type follows consequence, uncertainty, reversibility, affected ownership and future maintenance cost. Some choices need no artifact. Some need Decision Journal. Some need RFC. Some accepted decisions need ADR.

Artifact weight should follow lifetime of reasoning. Timing matters too: too early creates architecture fiction; too late creates defense. Write enough before commitment to improve decision; record enough at commitment to preserve why.

Scope and non-goals make review possible. One artifact should contain one coherent decision. Non-goals are not avoidance; they make question reviewable.

Evidence belongs in artifact, not as decoration. `LAW-005` means records separate evidence, assumptions, preferences, forecasts, open questions and accepted risk. RFC exposes gaps while decision can change. ADR preserves evidence that made accepted decision reasonable and review trigger for evidence aging.

Alternatives deserve fair treatment. Useful ADR explains why rejected option was attractive and why not selected in this context. Consequences deserve honesty about costs.

Ownership keeps artifacts alive. Proposal owner, decision owner, reviewers, release owners and future maintenance owner may differ. Comments need closure: accepted, rejected, narrowed, deferred, split, experiment/evidence requested or escalated to Architecture Review.

Status is part of meaning. Do not rewrite history silently. Supersede or retire records with links.

Discoverability (`METRIC-003`) tests shared memory. Future engineers should move from module, test, rejection message, release note, incident or owner to governing decision.

Architecture Ledger (`ARTIFACT-006`) is compact inventory of active decisions and known debts, not second ADR. Decision Journal (`ARTIFACT-003`) captures smaller or reversible decisions with evidence/confidence/trigger.

## Інженерний принцип

Use the smallest durable artifact that makes consequential proposal or decision reviewable now and discoverable later.

Questions:

- Is this proposal, accepted decision or smaller judgment?
- Is meaningful change still possible?
- Who owns proposal?
- Who owns decision after acceptance?
- Who is materially affected?
- What evidence exists?
- What remains uncertain?
- Which alternatives are real?
- What is out of scope?
- Which consequences are accepted?
- What closes RFC?
- What preserves accepted decision?
- What triggers review, supersession or retirement?
- How will future engineer find record from affected surface?

Answer may be no artifact, Decision Journal, RFC, ADR, or linked RFC and ADR.

## Архітектурна вправа

### Choose the Right Decision Artifact

Choose one current or recent architecture choice. State the choice in one sentence. Then answer decision state, affected surfaces, reversibility, Change Radius, evidence, assumptions, uncertainty, alternatives, non-goals, risks, owners, reviewers, closure, status, links, trigger and Architecture Ledger pointer.

Choose artifact weight: no artifact, Decision Journal entry, RFC, ADR, linked RFC and ADR.

End with artifact choice and why sufficient, named owner, evidence statement and discoverability action.

## Нотатник Principal Engineer

- An RFC preserves choice; an ADR preserves commitment.
- A record without evidence is an opinion with filename.
- A decision nobody can find is not shared memory.

## ADR

### Chapter ADR: Adopt RFC-First Review for the Configuration Update Protocol

#### Status

Accepted.

#### Context

Configuration-update protocol affects firmware, gateway, service tooling, manufacturing tests, support diagnostics, release compatibility and field operation. Implementation began before affected owners had shared proposal. First ADR draft recorded preferred direction but hid unresolved questions about scope, old gateway behavior, service-tool translation, manufacturing loading and support-visible rejection reasons.

#### Decision

Convert live protocol proposal into RFC before accepting architecture decision. RFC records motivation, scope, non-goals, proposal, risks, evidence, assumptions, alternatives, affected owners and open questions. It names proposal owner and decision owner. Affected owners review.

Use RFC Friday for lightweight review while alternatives remain open. Escalate unresolved cross-boundary risk to Architecture Review. Close RFC clearly. After acceptance, write ADR with context, decision, consequences, alternatives, owner, status and revisit trigger. Link ADR to RFC, implementation, compatibility tests, release notes, support diagnostics and Architecture Ledger.

Use Decision Journal for smaller reversible choices. Preserve superseded ADRs and link successors.

#### Consequences

Review happens while protocol can change. Evidence and uncertainty remain visible. Accepted rationale stays discoverable. Proposal state and decision state remain distinct. Cost: writing, review, status maintenance, links and abandoned proposal cleanup.

#### Alternatives Considered

- Keep ADR and request approval. Makes open decision look closed.
- Finish implementation and document later. Treats sunk cost as evidence.
- Use only ticket. Not enough for architectural reasoning.
- Use meeting notes. Hard to find and weak as accepted decision.
- Require Architecture Review before any proposal. Too heavy.
- Skip ADR because RFC exists. Proposal review is not concise accepted record.
- Mix proposal and accepted decision in one large document. Blurs state.
- Require RFCs or ADRs for all changes. Artifact weight should follow consequence.

## Коментар редактора

Chapter 17 makes reasoning reviewable before commitment and legible after conversation disappears. It is carried by ADR (`ARTIFACT-001`) and RFC (`ARTIFACT-002`), supported by Decision Journal (`ARTIFACT-003`), Architecture Ledger (`ARTIFACT-006`), Evidence Before Confidence (`LAW-005`), Architecture Review (`RITUAL-001`), RFC Friday (`RITUAL-006`) and Discoverability (`METRIC-003`).
