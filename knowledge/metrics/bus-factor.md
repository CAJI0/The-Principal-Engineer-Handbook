---
id: METRIC-002
type: metric
status: draft
canonical_name: Bus Factor
---

# Bus Factor

## Definition

The number of people whose absence would make a system area difficult to change safely.

## Why It Matters

Low bus factor means architecture depends on private memory.

## Symptoms

- Reviews wait for one person.
- Decision history is not written down.
- Teams avoid areas when the expert is unavailable.

## Example

Only one engineer knows why the firmware update protocol rejects certain packet sizes.

## Related Concepts

- [Documentation Is Shared Memory](../vocabulary/decision-journal.md)
- [ADR](../artifacts/adr.md)
- [Architecture Ledger](../artifacts/architecture-ledger.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Use bus factor to identify documentation and ownership risks.
