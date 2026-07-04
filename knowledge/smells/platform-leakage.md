---
id: SMELL-005
type: smell
status: draft
canonical_name: Platform Leakage
---

# Platform Leakage

## Definition

Platform details escaping into product code without an explicit boundary.

## Why It Matters

Leakage makes product behavior depend on low-level choices that should be replaceable.

## Symptoms

- Product logic knows driver quirks.
- Hardware-specific constants appear in feature code.
- Porting requires touching unrelated behavior.

## Example

Application code checks a vendor-specific error value instead of receiving a product-level failure reason.

## Related Concepts

- [HAL Everywhere](../anti-patterns/hal-everywhere.md)
- [Every API Is a Promise](../laws/every-api-is-a-promise.md)
- [Change Radius](../vocabulary/change-radius.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Not every platform detail needs hiding, but every leak should be intentional.
