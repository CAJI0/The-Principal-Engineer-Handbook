---
id: LAW-002
type: law
status: draft
canonical_name: Every API Is a Promise
---

# Every API Is a Promise

## Statement

Every API promises behavior that other code and people will trust.

## Meaning

An API is not only a function shape; it is a commitment about meaning, errors, timing, and ownership.

## Why It Matters

Changing a promise without naming it creates hidden system cost.

## Typical Violation

A firmware API changes retry behavior but callers still assume the old failure timing.

## Recovery

Document the promise, version the contract when needed, and review dependents.

## Related Concepts

- [Silent Coupling](../vocabulary/silent-coupling.md)
- [API Stability](../metrics/api-stability.md)
- [ADR](../artifacts/adr.md)
