---
id: ANTIPATTERN-002
type: anti_pattern
status: draft
canonical_name: HAL Everywhere
---

# HAL Everywhere

## Definition

Low-level hardware abstraction leaking through most of the product.

## Why It Matters

It makes hardware choices shape unrelated product behavior.

## Symptoms

- Product code depends directly on HAL calls.
- Porting requires broad edits.
- Driver quirks appear in business logic.

## Example

Feature code reads GPIO and timer details directly instead of depending on a product-level capability.

## Related Concepts

- [Platform Leakage](../smells/platform-leakage.md)
- [Every API Is a Promise](../laws/every-api-is-a-promise.md)
- [Change Radius](../vocabulary/change-radius.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

A HAL is useful only when its boundary protects product decisions.
