---
id: LAW-003
type: law
status: draft
canonical_name: Time Is a Dependency
---

# Time Is a Dependency

## Statement

Any code that depends on timing depends on architecture.

## Meaning

Delays, ordering, deadlines, and timeouts are system contracts, not incidental details.

## Why It Matters

Timing assumptions often fail only under load, temperature, manufacturing variation, or field conditions.

## Typical Violation

A task delay works on the bench but fails when another subsystem changes startup time.

## Recovery

Name timing contracts, test boundaries, and make ownership of time-sensitive behavior explicit.

## Related Concepts

- [Event Catalog](../artifacts/event-catalog.md)
- [Hidden State](../smells/hidden-state.md)
- [Architecture Review](../rituals/architecture-review.md)

