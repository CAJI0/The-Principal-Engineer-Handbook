---
id: VOCAB-010
type: vocabulary
status: draft
canonical_name: Boolean Explosion
---

# Boolean Explosion

## Definition

The uncontrolled growth of flags and modes that multiply system behavior.

## Why It Matters

Boolean combinations create states that nobody reviews, tests, or owns.

## Symptoms

- Features require adding another flag.
- Test matrices become unclear.
- Engineers cannot name valid mode combinations.

## Example

A device has separate booleans for factory, debug, recovery, legacy, and safe modes, with no single state model.

## Related Concepts

- [Boolean Explosion Smell](../smells/boolean-explosion.md)
- [Every State Has One Owner](../laws/every-state-has-one-owner.md)
- [Hidden State](../smells/hidden-state.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Replace uncontrolled flags with named states and ownership.

