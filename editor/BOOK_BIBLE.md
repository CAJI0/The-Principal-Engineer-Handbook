# Book Bible

## Working Title

The Principal Engineer Handbook

## Subtitle

Building Embedded Systems That Survive Change

## Tone

> AUTHOR NOTE: Authors to define tone constraints.

## Target Reader

> AUTHOR NOTE: Authors to define the target reader.

## Book Structure

Canonical manuscript source lives in `book/`.

`docs/` is reserved for generated or published documentation support and must not duplicate canonical chapter text.

- `00-front-matter`
- `01-thinking-like-a-principal`
- `02-the-laws`
- `03-architecture-playbook`
- `04-building-a-product`
- `05-engineering-organization`
- `06-legacy`
- `appendix`

## Recurring Sections

> AUTHOR NOTE: Authors to define recurring sections.

## Terminology Rules

> AUTHOR NOTE: Authors to define canonical terminology.

## Editorial Rules

- Do not invent manuscript content.
- Preserve author intent.
- Mark unresolved content decisions with `AUTHOR NOTE:`.
- Reference PEAK knowledge concepts from `knowledge/` where appropriate.
- Reuse existing knowledge concepts instead of redefining them in chapters.

## Knowledge References

Chapters should reference PEAK concepts by name and stable ID where appropriate.

New terminology should first be checked against the knowledge model.

Human-readable concept explanations live in `knowledge/<category>/<concept>.md`. Machine-readable IDs, metadata, and relationships live in `knowledge/index.yaml`.

## Chapter Lifecycle

1. Draft
2. Editorial Review
3. Canon Review
4. Technical Review
5. Freeze
