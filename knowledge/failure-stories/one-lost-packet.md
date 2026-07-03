---
id: FAILURE-002
type: failure_story
status: draft
canonical_name: One Lost Packet
---

# One Lost Packet

## Definition

A system failure triggered by one dropped or reordered packet.

## Why It Matters

Communication assumptions often hide in timing and retry behavior.

## Symptoms

- Recovery depends on perfect ordering.
- Logs show the symptom after the missing event.
- Retry behavior differs across components.

## Example

A firmware update stalls because one acknowledgment is lost and no component owns the recovery contract.

## Related Concepts

- [Time Is a Dependency](../laws/time-is-a-dependency.md)
- [Event Catalog](../artifacts/event-catalog.md)
- [Event Explosion](../smells/event-explosion.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Use this story when discussing protocol and event contracts.

