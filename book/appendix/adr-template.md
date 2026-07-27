# ADR Template

Use this template to record an architecture-significant decision, the evidence behind it, rejected options, ownership
implications, API promises, dependency decisions, risks, and review triggers.

## When to Use This

Use an ADR (`ARTIFACT-001`) when a decision will affect future architecture, ownership, cost, reversibility, product
promises, or cross-team coordination. If meaningful alternatives are still open, start with an RFC instead.

Keep the record short enough to be read later. Chapter 17 teaches ADR and RFC usage; this file is only the copyable form.

## Template

### Title

[decision name]

### Status

[proposed | accepted | superseded | retired]

### Date

[date]

### Owner

[owner]

### Context

[What problem, product promise, system boundary, or legacy condition created the decision?]

### Decision

[What has been decided?]

### Evidence

[tests, telemetry, field data, manufacturing checks, support cases, review findings, or other evidence]

This section supports Evidence Before Confidence (`LAW-005`). Separate observed evidence from assumptions.

### Constraints

- [technical constraint]
- [product or release constraint]
- [operational or manufacturing constraint]

### Options Considered

- Option A: [trade-off]
- Option B: [trade-off]
- Option C: [trade-off]

### Rejected Options

- [rejected option]: [why it was rejected and what would need to change before reconsidering it]

### State Ownership Impact

[Which meaningful state is affected, and who owns changing, validating, and explaining it?]

This section supports Every State Has One Owner (`LAW-001`).

### API Promises Affected

[Which interfaces, events, diagnostics, files, protocols, dashboards, or human procedures will others trust after this
decision?]

This section supports Every API Is a Promise (`LAW-002`).

### Dependencies Introduced, Removed, or Accepted

- Introduced: [dependency and owner]
- Removed: [dependency and retirement evidence]
- Accepted: [dependency, reason, risk, and review trigger]

This section supports Every Dependency Is a Decision (`LAW-007`).

### Change Radius

[Which code, teams, tests, release paths, manufacturing steps, service tools, support procedures, and records must change
or be reviewed?]

Use Change Radius (`METRIC-001`) to keep review weight proportionate.

### Rollout and Recovery

- Rollout plan: [sequence, compatibility window, owner, and evidence]
- Rollback trigger: [signal that stops or reverses the change]
- Recovery path: [how the product, users, support, and records recover if the decision is wrong]

### Risks and Responses

- Risk: [risk]
  Response: [response]
- Risk: [risk]
  Response: [response]

### Review Trigger

[date, event, metric, release, evidence threshold, or Architecture Health Review trigger]

Use Architecture Review (`RITUAL-001`) before hardening consequential cross-boundary decisions. Use Architecture Health
Review (`RITUAL-004`) when repeated drift or unresolved risk needs recurring attention.

### Related Records

- RFCs: [links]
- Decision Journal entries: [links]
- Architecture Ledger entries: [links]
- Tests, dashboards, release notes, or support records: [links]

## Review Prompts

- Is there one owner for each meaningful state affected by this decision?
- Which API promises, including informal promises, will people trust after this decision?
- What evidence supports the decision, and what remains an assumption?
- Which dependencies are being accepted, and what replacement cost do they create?
- Can a future engineer discover the decision, owner, and contract from the affected behavior (`METRIC-003`)?
- What would cause the team to revisit, supersede, or retire this ADR?

## Completion Check

- [ ] The decision is explicit.
- [ ] The owner is named.
- [ ] Evidence is separated from confidence.
- [ ] Rejected options are recorded.
- [ ] State ownership and API promises are named.
- [ ] Dependencies and Change Radius are visible.
- [ ] Rollout, rollback, and recovery are defined.
- [ ] Related records are linked.
- [ ] The review trigger is concrete.
