---
id: ANTIPATTERN-001
type: anti_pattern
status: draft
canonical_name: God Module
---

# God Module

## Definition

A module that owns too many unrelated responsibilities.

## Why It Matters

It becomes a coordination bottleneck and a high-risk change point.

## Symptoms

- Many features require editing the same module.
- Ownership is unclear.
- Tests are broad because behavior is tangled.

## Example

A system manager module handles startup, logging, retries, calibration, and product modes.

## Related Concepts

- [Utility Gravity](../vocabulary/utility-gravity.md)
- [Change Radius](../vocabulary/change-radius.md)
- [Simplicity Is a Feature](../laws/simplicity-is-a-feature.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Split by ownership and reason to change, not by file size alone.

