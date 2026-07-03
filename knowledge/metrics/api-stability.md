---
id: METRIC-004
type: metric
status: draft
canonical_name: API Stability
---

# API Stability

## Definition

How reliably an API preserves the behavior its dependents trust.

## Why It Matters

API instability spreads cost across teams and releases.

## Symptoms

- Callers add defensive workarounds.
- Minor API changes cause broad regressions.
- Behavior changes without versioning or review.

## Example

A sensor API keeps the same signature but changes when it reports invalid readings.

## Related Concepts

- [Every API Is a Promise](../laws/every-api-is-a-promise.md)
- [Silent Coupling](../smells/silent-coupling.md)
- [Change Radius](change-radius.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Stability includes behavior, errors, timing, and meaning.

