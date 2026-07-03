---
id: ARTIFACT-005
type: artifact
status: draft
canonical_name: Event Catalog
---

# Event Catalog

## Purpose

Record important system events, their meanings, and ownership.

## When To Use

Use it when firmware, tools, tests, or products communicate through events.

## Template

- Event name
- Meaning
- Producer
- Consumer
- Ordering or timing assumptions
- Failure behavior

## Common Mistakes

- Treating event names as self-documenting.
- Ignoring timing assumptions.
- Allowing multiple meanings for one event.

## Related Concepts

- [Time Is a Dependency](../laws/time-is-a-dependency.md)
- [Event Explosion](../smells/event-explosion.md)
- [Every State Has One Owner](../laws/every-state-has-one-owner.md)

