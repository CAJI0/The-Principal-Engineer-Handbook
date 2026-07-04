---
id: LAW-001
type: law
status: draft
canonical_name: Every State Has One Owner
---

# Every State Has One Owner

## Statement

Every meaningful state in the system must have exactly one clear owner.

## Meaning

Ownership means one place is responsible for changing, validating, and explaining the state.

## Why It Matters

When ownership is unclear, state becomes duplicated, inferred, or corrected after the fact.

## Typical Violation

Firmware, a test fixture, and a mobile app each keep their own idea of device mode.

## Recovery

Name the state, assign ownership, remove duplicate writers, and document the contract.

## Related Concepts

- [Boolean Explosion](../vocabulary/boolean-explosion.md)
- [Hidden State](../smells/hidden-state.md)
- [ADR](../artifacts/adr.md)
