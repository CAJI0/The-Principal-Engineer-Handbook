---
id: SMELL-001
type: smell
status: draft
canonical_name: Silent Coupling
---

# Silent Coupling

## Definition

A hidden dependency that affects behavior but is not represented as an explicit contract.

## Why It Matters

It makes local changes unsafe because the real dependency graph is unknown.

## Symptoms

- Teams coordinate by memory.
- A change breaks another area without an obvious call path.
- Tests encode assumptions not present in product documentation.

## Example

A manufacturing script and firmware parser depend on identical field ordering without a shared schema.

## Related Concepts

- [Silent Coupling](../vocabulary/silent-coupling.md)
- [Every API Is a Promise](../laws/every-api-is-a-promise.md)
- [Change Radius](../vocabulary/change-radius.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Look for behavior that must change together but is reviewed separately.

