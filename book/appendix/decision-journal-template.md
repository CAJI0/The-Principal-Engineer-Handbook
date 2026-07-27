# Decision Journal Template

Use this template to track judgment over time: decision, confidence, evidence, assumptions, expected signals, review
date, result, and what changed.

## When to Use This

Use a Decision Journal (`ARTIFACT-003`) for a decision that matters enough to preserve, but does not need a full ADR.
It is useful for smaller assumptions, temporary choices, evidence gaps, or follow-ups created during review.

Do not use `METRIC-002` as Decision Quality. `METRIC-002` is Bus Factor.

## Template

### Decision

[decision]

### Decision Owner

[owner]

### Date

[date]

### Confidence Level

[low | medium | high] because [evidence and uncertainty]

### Evidence Available

- [evidence]
- [evidence]

This section supports Evidence Before Confidence (`LAW-005`).

### Assumptions

- [assumption]
- [assumption]

### Weak Signals

- [weak signal]
- [source]
- [what would make it stronger evidence]

Use Weak Signal (`VOCAB-002`) and the Weak Signal Register (`ARTIFACT-007`) when early signs need tracking before they
become confirmed failures.

### Expected Outcomes

- [expected outcome]
- [expected architecture or product signal]

### Expected Failure Signs

- [failure sign]
- [where it should be visible]

### Review Date

[review date]

### Actual Outcome

[what happened]

### What Changed

[new evidence, changed constraint, changed owner, changed product promise, or changed dependency]

### What the Team Learned

[lesson to preserve without blaming individuals]

### Follow-Up Links

- ADR: [link]
- RFC: [link]
- Architecture Ledger: [link]
- Architecture Health signal: [link]

## Review Prompts

- What evidence would change this decision?
- Which assumption is most likely to age badly?
- Which weak signal should be watched before the next review date?
- What is the Change Radius (`METRIC-001`) if this decision is wrong?
- Does this entry reveal a recurring Architecture Health (`METRIC-005`) concern?

## Completion Check

- [ ] The decision and owner are named.
- [ ] Confidence is tied to evidence.
- [ ] Assumptions and weak signals are visible.
- [ ] Expected outcomes and failure signs are testable.
- [ ] The review date is concrete.
- [ ] The actual outcome can be recorded later.
- [ ] Follow-up ADR, RFC, or Architecture Ledger links are included when needed.
