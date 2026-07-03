---
id: RITUAL-003
type: ritual
status: draft
canonical_name: Deletion Day
---

# Deletion Day

## Purpose

Remove unused architecture before it becomes permanent cost.

## Cadence

Schedule during maintenance windows, before major releases, or after feature retirement.

## Participants

Owners of affected modules, test owners, and release reviewers.

## Process

Identify candidates, verify usage, remove safely, and update contracts.

## Output

Deleted code, updated documentation, and reduced test or review surface.

## Failure Modes

Deletion happens without evidence, or the ritual becomes cosmetic cleanup only.

## Related Concepts

- [Deletion Day](../vocabulary/deletion-day.md)
- [Unused Flexibility Is Waste](../laws/unused-flexibility-is-waste.md)
- [Simplicity Is a Feature](../laws/simplicity-is-a-feature.md)

