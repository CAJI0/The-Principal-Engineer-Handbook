---
id: SMELL-006
type: smell
status: draft
canonical_name: Event Explosion
---

# Event Explosion

## Definition

The uncontrolled growth of events without clear meaning, ownership, or lifecycle.

## Why It Matters

Event-heavy systems become hard to trace and harder to change safely.

## Symptoms

- Similar events mean slightly different things.
- Consumers depend on event ordering that is not documented.
- Removing one event breaks unexpected behavior.

## Example

A device emits separate connected, ready, configured, and active events, but teams disagree on their order.

## Related Concepts

- [Event Catalog](../artifacts/event-catalog.md)
- [Time Is a Dependency](../laws/time-is-a-dependency.md)
- [Silent Coupling](silent-coupling.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Catalog events before adding more of them.
