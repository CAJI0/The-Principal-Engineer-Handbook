---
id: VOCAB-008
type: vocabulary
status: draft
canonical_name: Silent Coupling
---

# Silent Coupling

## Definition

A dependency between parts of a system that exists in behavior but is not visible in code, contracts, or documentation.

## Why It Matters

Silent coupling makes change look local while its consequences are shared.

## Symptoms

- Two components must change together.
- A test station assumes firmware behavior not documented as an interface.
- Teams discover dependencies only after a failure.

## Example

A bootloader and update tool both assume the same packet ordering, but no protocol contract names it.

## Related Concepts

- [Silent Coupling Smell](../smells/silent-coupling.md)
- [Every API Is a Promise](../laws/every-api-is-a-promise.md)
- [Change Radius](change-radius.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Silent coupling should become either an explicit contract or a removed dependency.
