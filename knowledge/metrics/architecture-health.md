---
id: METRIC-005
type: metric
status: draft
canonical_name: Architecture Health
---

# Architecture Health

## Definition

The system's ability to support necessary change at acceptable cost.

## Why It Matters

It gives teams a shared way to discuss maintainability.

## Symptoms

- Changes are slow for reasons unrelated to feature size.
- Ownership is unclear.
- Old decisions block new work.

## Example

A product line cannot add a variant without touching shared startup, calibration, logging, and release tools.

## Related Concepts

- [Architecture Health](../vocabulary/architecture-health.md)
- [Architecture Health Review](../rituals/architecture-health-review.md)
- [Change Radius](change-radius.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Combine signals; do not reduce health to one score.

