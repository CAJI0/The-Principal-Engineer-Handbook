---
id: FAILURE-001
type: failure_story
status: draft
canonical_name: Logger That Became a Platform
---

# Logger That Became a Platform

## Definition

A logging utility gradually became a shared platform dependency.

## Why It Matters

Small utilities can become architecture without review.

## Symptoms

- Product behavior depends on logging side effects.
- Many modules import logging for non-logging helpers.
- Changing logs risks changing behavior.

## Example

An embedded logger starts carrying timestamps, retry counters, diagnostic routing, and feature flags.

## Related Concepts

- [Utility Gravity](../vocabulary/utility-gravity.md)
- [God Module](../anti-patterns/god-module.md)
- [Architecture Review](../rituals/architecture-review.md)

## Related Chapters

- [What Is a Principal Engineer?](../../book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md)

## Notes

Use this story when discussing accidental platforms.
