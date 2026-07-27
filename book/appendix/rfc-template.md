# RFC Template

Use this template to expose a proposed change before it hardens: context, problem, constraints, options, affected teams,
product promises, operational consequences, rollout plan, and open questions.

## When to Use This

Use an RFC (`ARTIFACT-002`) when a proposal needs review across ownership boundaries while meaningful alternatives still
exist. If the decision is already accepted, write or update the ADR and use the RFC as proposal history.

Keep the RFC focused on decision quality, ownership, evidence, dependencies, and Change Radius.

## Template

### Title

[proposal name]

### Author and Owner

- Author: [author]
- Proposal owner: [owner]
- Expected decision owner: [owner]

### Reviewers and Affected Teams

- Required reviewers: [reviewers]
- Affected teams: [firmware, backend, manufacturing, service tooling, support, release, test, product, or other teams]

### Problem Statement

[What problem should this proposal solve?]

### Context

[What system behavior, product promise, constraint, or prior decision makes this proposal necessary?]

### Non-Goals

- [thing this RFC will not solve]
- [thing that should stay unchanged]

### Constraints

- [technical constraint]
- [time, release, manufacturing, support, operational, or safety constraint]

### Options

- Option A: [description, evidence, trade-off]
- Option B: [description, evidence, trade-off]
- Option C: [description, evidence, trade-off]

### Recommended Direction

[recommended direction and why it is currently favored]

### Decision State

- Decision not yet made: [yes/no]
- Decision already made: [yes/no]
- If already made, link the ADR or decision record: [link]

### Ownership Impact

[Which state, behavior, boundary, or product promise changes owner or creates affected-owner obligations?]

### API Promises

[Which interfaces, events, diagnostics, schemas, tools, procedures, or timing behaviors may become promises?]

### Dependencies

[What libraries, services, protocols, hardware, tools, vendors, manufacturing fixtures, test harnesses, or operational
processes will the system rely on?]

This section supports Every Dependency Is a Decision (`LAW-007`).

### Operational Consequences

[What changes for deployment, observability, support, manufacturing, service tools, release validation, rollback, or
field recovery?]

### Migration or Rollout Plan

- Stage 1: [scope, owner, evidence, rollback trigger]
- Stage 2: [scope, owner, evidence, rollback trigger]
- Compatibility window: [window and retirement trigger]

### Observability and Evidence Plan

[What tests, telemetry, logs, dashboards, manufacturing checks, support checks, or field signals will prove the proposal
is safe enough?]

This section supports Evidence Before Confidence (`LAW-005`).

### Open Questions

- [question, owner, needed evidence, decision deadline]

### Decision Deadline

[date or event by which the decision must close]

### Expected Follow-Up Artifacts

- ADR (`ARTIFACT-001`): [needed/not needed/link]
- Decision Journal (`ARTIFACT-003`): [needed/not needed/link]
- Architecture Ledger (`ARTIFACT-006`): [needed/not needed/link]
- Architecture Review (`RITUAL-001`): [needed/not needed/date]

## Review Prompts

- Is the proposal still reviewable, or has implementation already hardened the decision?
- Which affected owners must be able to act on the result?
- What API promises could this proposal create or change (`LAW-002`)?
- What evidence exists now, and what evidence must be gathered before confidence rises?
- Which dependencies does the proposal accept, and who owns their lifecycle?
- Is the Change Radius broad enough to require Architecture Review?

## Completion Check

- [ ] The problem and context are clear.
- [ ] Non-goals prevent scope drift.
- [ ] Affected teams and reviewers are named.
- [ ] Options and trade-offs are visible.
- [ ] Ownership impact, API promises, and dependencies are explicit.
- [ ] Evidence and open questions have owners.
- [ ] Rollout, observability, and follow-up artifacts are named.
- [ ] The decision deadline is concrete.
