---
id: ANTIPATTERN-004
type: anti_pattern
status: draft
canonical_name: Manager Mania
---

# Manager Mania

## Definition

Adding manager objects that coordinate behavior without clear domain ownership.

## Why It Matters

Managers often centralize decisions while hiding why those decisions belong together.

## Symptoms

- Many classes or modules end with "manager."
- Control flow passes through generic coordinators.
- Ownership debates move into manager code.

## Example

A DeviceManager owns connectivity, storage, firmware update, and factory-mode behavior.

## Related Concepts

- [God Module](god-module.md)
- [Utility Gravity](../vocabulary/utility-gravity.md)
- [Every State Has One Owner](../laws/every-state-has-one-owner.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Rename is not enough; ownership must become clearer.

