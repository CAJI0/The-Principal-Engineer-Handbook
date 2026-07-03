---
id: VOCAB-001
type: vocabulary
status: draft
canonical_name: Change Radius
---

# Change Radius

## Definition

The amount of system surface that must change, be reviewed, or be retested when one decision changes.

## Why It Matters

Small change radius keeps work understandable and reduces release risk.

## Symptoms

- A small feature touches many unrelated modules.
- Tests fail far from the changed code.
- Reviewers cannot identify the real boundary of a change.

## Example

A sensor calibration update requires firmware, station scripts, release packaging, and documentation changes because the contract was never isolated.

## Related Concepts

- [Every API Is a Promise](../laws/every-api-is-a-promise.md)
- [Silent Coupling](../smells/silent-coupling.md)
- [Change Radius Metric](../metrics/change-radius.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Track change radius when reviewing architecture and release risk.

