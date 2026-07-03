# PEAK Knowledge Model

PEAK means Principal Engineering Architecture Knowledge.

PEAK is the internal knowledge architecture behind *The Principal Engineer Handbook*. It organizes concepts that can be reused by the book manuscript, future website, workshops, reference project, architecture reviews, checklists, and long-term handbook evolution.

The domain model is defined in [`editor/KNOWLEDGE_MODEL.md`](../editor/KNOWLEDGE_MODEL.md).

The first machine-readable index is [`knowledge/index.yaml`](index.yaml).

The architecture review process is documented in [`editor/REVIEW_PROCESS.md`](../editor/REVIEW_PROCESS.md), and the first foundation review is recorded in [`editor/ARCHITECTURE_REVIEW_0.md`](../editor/ARCHITECTURE_REVIEW_0.md).

## Areas

- [Vocabulary](vocabulary/README.md)
- [Laws](laws/README.md)
- [Artifacts](artifacts/README.md)
- [Rituals](rituals/README.md)
- [Smells](smells/README.md)
- [Anti-patterns](anti-patterns/README.md)
- [Metrics](metrics/README.md)
- [Failure Stories](failure-stories/README.md)

## How It Relates to the Book

The book is one rendering of PEAK. Chapters should reference existing PEAK concepts instead of redefining them.

## Adding New Concepts

Before adding a concept:

1. Check whether an existing concept already covers it.
2. Assign a stable ID if the concept belongs in the knowledge graph.
3. Add or update the Markdown concept file.
4. Add the entity to `index.yaml`.
5. Add useful relationships to other entities.

## Stable IDs

Stable IDs let chapters, tools, workshops, and future AI-assisted reviews refer to the same concept over time.

IDs are never reused after deletion, deprecation, or retirement.

## Maintaining the YAML Index

Keep `index.yaml` readable. Add only canonical or intentionally tracked draft entities. Use approved relationship types from the knowledge model.
