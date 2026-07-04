---
id: METRIC-003
type: metric
status: draft
canonical_name: Discoverability
---

# Discoverability

## Definition

How easily an engineer can find the decision, owner, and contract behind system behavior.

## Why It Matters

Poor discoverability turns maintenance into archaeology.

## Symptoms

- Engineers rely on oral history.
- Important decisions are scattered.
- Search finds code but not intent.

## Example

A new maintainer finds the retry code but cannot find why the retry limit is three.

## Related Concepts

- [ADR](../artifacts/adr.md)
- [Architecture Ledger](../artifacts/architecture-ledger.md)
- [Decision Journal](../artifacts/decision-journal.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Discoverability is improved by names, links, ownership, and short records.
