---
id: METRIC-001
type: metric
status: draft
canonical_name: Change Radius
---

# Change Radius

## Definition

How much system surface is affected by one change.

## Why It Matters

It helps teams compare architectural cost with evidence.

## Symptoms

- Small changes need many reviewers.
- Regression scope is unclear.
- A feature crosses unexpected boundaries.

## Example

Changing a timeout requires firmware, test station, release note, and support-tool updates.

## Related Concepts

- [Change Radius](../vocabulary/change-radius.md)
- [Silent Coupling](../smells/silent-coupling.md)
- [Architecture Health](architecture-health.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Measure approximate affected surface; do not chase false precision.

