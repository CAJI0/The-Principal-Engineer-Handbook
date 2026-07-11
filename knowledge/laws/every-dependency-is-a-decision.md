---
id: LAW-007
type: law
status: draft
canonical_name: Every Dependency Is a Decision
---

# Every Dependency Is a Decision

## Statement

Every dependency commits the system to behavior, failure modes, lifecycle constraints, ownership boundaries, and
replacement cost.

## Meaning

A dependency is not merely code the system calls. It can be a library, service, protocol, tool chain, hardware part,
data format, vendor component, build step, manufacturing fixture, test harness, or operational process whose behavior
the system now relies on.

## Why It Matters

Dependencies import change radius. They bring update cadence, failure propagation, ownership questions, compatibility
work, and exit cost into the architecture even when the first use feels small.

## Typical Violation

A team wraps a vendor library thinly but still lets the library's callback model, memory ownership, error meanings,
and release cadence spread through product code, tests, tooling, and support procedures.

## Recovery

Name the dependency surface, constrain where it can spread, assign update ownership, test the contract, and record the
conditions that would trigger replacement.

## Related Concepts

- [Change Radius](../vocabulary/change-radius.md)
- [Silent Coupling](../smells/silent-coupling.md)
- [ADR](../artifacts/adr.md)
