---
id: SMELL-004
type: smell
status: draft
canonical_name: Hidden State
---

# Hidden State

## Definition

State that affects behavior but is not visible through a clear owner, interface, or model.

## Why It Matters

Hidden state makes debugging depend on guesswork.

## Symptoms

- Behavior changes after a sequence nobody documents.
- Reset fixes the problem without explaining it.
- Multiple components infer the same state differently.

## Example

A device behaves differently after factory calibration because a persistent flag is set outside the main state model.

## Related Concepts

- [Every State Has One Owner](../laws/every-state-has-one-owner.md)
- [Boolean Explosion](boolean-explosion.md)
- [Event Catalog](../artifacts/event-catalog.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Hidden state should be named, owned, or removed.
