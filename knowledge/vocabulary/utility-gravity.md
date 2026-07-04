---
id: VOCAB-009
type: vocabulary
status: draft
canonical_name: Utility Gravity
---

# Utility Gravity

## Definition

The tendency for a generic utility area to attract unrelated responsibilities over time.

## Why It Matters

Utility gravity hides ownership and turns convenience into architecture.

## Symptoms

- A helper module grows unrelated functions.
- Many teams depend on code nobody owns.
- Changes to utilities become high-risk.

## Example

A small timing helper becomes the place for retries, logging, protocol parsing, and product constants.

## Related Concepts

- [Utility Gravity Smell](../smells/utility-gravity.md)
- [God Module](../anti-patterns/god-module.md)
- [Simplicity Is a Feature](../laws/simplicity-is-a-feature.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Watch for utility code with many reasons to change.
