---
id: SMELL-002
type: smell
status: draft
canonical_name: Utility Gravity
---

# Utility Gravity

## Definition

A utility area accumulating unrelated behavior because it is easy to reuse.

## Why It Matters

It hides ownership and increases change radius.

## Symptoms

- Many modules depend on the same helper file.
- Utility changes require broad regression testing.
- New features add convenience functions instead of boundaries.

## Example

A common helper module becomes responsible for logging, parsing, retries, and product constants.

## Related Concepts

- [Utility Gravity](../vocabulary/utility-gravity.md)
- [God Module](../anti-patterns/god-module.md)
- [Simplicity Is a Feature](../laws/simplicity-is-a-feature.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Generic names often hide architectural decisions.

