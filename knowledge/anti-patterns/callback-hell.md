---
id: ANTIPATTERN-005
type: anti_pattern
status: draft
canonical_name: Callback Hell
---

# Callback Hell

## Definition

Control flow spread across callbacks so behavior is hard to trace or own.

## Why It Matters

It hides ordering, error handling, and state transitions.

## Symptoms

- Engineers cannot explain full execution order.
- Error handling is duplicated or skipped.
- Timing bugs depend on callback sequence.

## Example

Firmware startup depends on nested callbacks from storage, radio, calibration, and cloud subsystems.

## Related Concepts

- [Time Is a Dependency](../laws/time-is-a-dependency.md)
- [Event Explosion](../smells/event-explosion.md)
- [Hidden State](../smells/hidden-state.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Make ordering and failure behavior explicit.

