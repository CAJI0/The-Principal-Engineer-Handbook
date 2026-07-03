---
id: SMELL-003
type: smell
status: draft
canonical_name: Boolean Explosion
---

# Boolean Explosion

## Definition

Too many flags creating behavior combinations no one can reason about.

## Why It Matters

Each flag multiplies test, review, and ownership cost.

## Symptoms

- Mode behavior depends on several independent booleans.
- No one can list valid combinations.
- Bugs appear only under rare flag mixes.

## Example

Factory, debug, safe, recovery, and legacy flags combine into states that were never designed.

## Related Concepts

- [Boolean Explosion](../vocabulary/boolean-explosion.md)
- [Every State Has One Owner](../laws/every-state-has-one-owner.md)
- [Hidden State](hidden-state.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Replace flag combinations with named states when behavior matters.

