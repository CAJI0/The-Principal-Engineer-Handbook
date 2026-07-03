---
id: ANTIPATTERN-003
type: anti_pattern
status: draft
canonical_name: Global Configuration
---

# Global Configuration

## Definition

Configuration shared broadly without ownership, scope, or lifecycle.

## Why It Matters

Global configuration turns product variation into hidden coupling.

## Symptoms

- One setting affects many unrelated modules.
- Configuration changes need broad regression testing.
- Defaults are copied instead of owned.

## Example

A product mode flag changes logging, calibration, connectivity, and power behavior across the codebase.

## Related Concepts

- [Hidden State](../smells/hidden-state.md)
- [Every State Has One Owner](../laws/every-state-has-one-owner.md)
- [Boolean Explosion](../vocabulary/boolean-explosion.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Configuration should have scope, owner, and validation.

