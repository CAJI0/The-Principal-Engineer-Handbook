---
id: ANTIPATTERN-006
type: anti_pattern
status: draft
canonical_name: Temporary Solution
---

# Temporary Solution

## Definition

A workaround with no owner, review trigger, or removal plan.

## Why It Matters

Temporary decisions become permanent when their context is forgotten.

## Symptoms

- Comments say "temporary" without a date or owner.
- Workarounds survive multiple releases.
- Nobody knows what would make removal safe.

## Example

A release adds a calibration bypass for one customer issue and leaves it active for all future products.

## Related Concepts

- [Decision Journal](../artifacts/decision-journal.md)
- [Deletion Day](../rituals/deletion-day.md)
- [Unused Flexibility Is Waste](../laws/unused-flexibility-is-waste.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

A temporary solution needs an expiration condition.
