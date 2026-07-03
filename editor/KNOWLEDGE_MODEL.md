# Knowledge Model

## Purpose

PEAK gives *The Principal Engineer Handbook* a stable internal knowledge architecture. The handbook is not only a sequence of chapters; it is a reusable engineering knowledge system that can support the manuscript, website, workshops, reference project, checklists, and future architecture review workflows.

The model prevents duplicate concepts, preserves stable names, and gives future maintainers a way to connect chapters, stories, rituals, artifacts, and smells without rewriting the same ideas.

## Core Idea

The handbook is supported by a graph of engineering concepts.

The book is one rendering of that graph.

## Entity Types

- Law: a durable engineering rule with explicit consequences.
- Vocabulary: a named term used consistently across the handbook.
- Principle: a guiding idea used to reason about engineering trade-offs.
- Maxim: a short memorable statement that captures practical judgment.
- Story: a realistic engineering situation used to introduce or test an idea.
- Failure Story: a story centered on a failure and the system condition that made it possible.
- ADR: an architecture decision record.
- RFC: a proposal intended for review before a decision hardens.
- Artifact: a reusable engineering record, template, catalog, or ledger.
- Ritual: a repeated engineering practice that produces decisions or artifacts.
- Metric: a measurement used to discuss architecture with evidence.
- Smell: an early sign that architecture is becoming harder to change.
- Anti-pattern: a recurring structure that reliably creates long-term cost.
- Exercise: a reader activity that applies a concept.
- Checklist: a concise review aid.
- Diagram: a visual representation of concepts, relationships, or system structure.
- Chapter: a reader-facing manuscript unit.
- Reference Project Component: a concrete component from the reference project.

## Stable ID Scheme

Stable IDs identify concepts across Markdown files, chapters, tools, and future generated views.

- `LAW-001`
- `VOCAB-001`
- `PRINCIPLE-001`
- `MAXIM-001`
- `STORY-001`
- `FAILURE-001`
- `ADR-001`
- `RFC-001`
- `ARTIFACT-001`
- `RITUAL-001`
- `METRIC-001`
- `SMELL-001`
- `ANTIPATTERN-001`
- `EXERCISE-001`
- `CHECKLIST-001`
- `DIAGRAM-001`
- `CHAPTER-001`
- `REF-001`

IDs are stable. Do not reuse an ID after deletion, deprecation, or retirement.

## Source of Truth

- Markdown concept files are the human-readable source for concept explanation.
- `knowledge/index.yaml` is the machine-readable source for IDs, metadata, and relationships.
- `editor/CANON.md` is the editorial source for what belongs to the handbook's canon.
- These files must be kept consistent during Knowledge Review.

## Required Concept Front Matter

Every canonical concept Markdown file must start with YAML front matter:

```yaml
---
id: LAW-001
type: law
status: draft
canonical_name: Every State Has One Owner
---
```

Use the correct entity type and ID.

## Entity Metadata

Each entity should use the smallest metadata set that keeps it discoverable and reviewable.

### Vocabulary

```yaml
id: VOCAB-001
type: vocabulary
name: Change Radius
definition: The affected surface of one change.
status: draft
related:
  concepts: []
  chapters: []
```

### Law

```yaml
id: LAW-001
type: law
name: Every State Has One Owner
statement: Every mutable state must have exactly one authoritative owner.
status: draft
related:
  concepts: []
  chapters: []
  artifacts: []
  smells: []
```

### Principle

```yaml
id: PRINCIPLE-001
type: principle
name: Architecture is a decision-making discipline
statement: Architecture exists to make decisions explicit and future change less expensive.
status: draft
related:
  concepts: []
  chapters: []
```

### Maxim

```yaml
id: MAXIM-001
type: maxim
name: Decisions compound
statement: Small decisions accumulate into system behavior.
status: draft
related:
  concepts: []
  chapters: []
```

### Story

```yaml
id: STORY-001
type: story
name: Calibration Drift Investigation
summary: A realistic engineering situation that introduces a concept.
status: draft
related:
  concepts: []
  chapters: []
```

### Failure Story

```yaml
id: FAILURE-001
type: failure_story
name: Logger That Became a Platform
summary: A failure story showing how a small utility became architecture.
status: draft
related:
  concepts: []
  chapters: []
```

### ADR

```yaml
id: ADR-001
type: adr
name: Use ADRs for Book Decisions
status: accepted
related:
  concepts: []
  chapters: []
```

### RFC

```yaml
id: RFC-001
type: rfc
name: Proposal Title
status: proposed
related:
  concepts: []
  chapters: []
```

### Artifact

```yaml
id: ARTIFACT-001
type: artifact
name: ADR
purpose: Record a decision and its consequences.
status: draft
related:
  concepts: []
  chapters: []
```

### Ritual

```yaml
id: RITUAL-001
type: ritual
name: Architecture Review
purpose: Review decisions before they become expensive to change.
status: draft
related:
  concepts: []
  artifacts: []
```

### Metric

```yaml
id: METRIC-001
type: metric
name: Change Radius
definition: The affected surface of one change.
status: draft
related:
  concepts: []
  rituals: []
```

### Smell

```yaml
id: SMELL-001
type: smell
name: Silent Coupling
definition: A hidden behavioral dependency.
status: draft
related:
  laws: []
  artifacts: []
```

### Anti-pattern

```yaml
id: ANTIPATTERN-001
type: anti_pattern
name: God Module
definition: A module with too many unrelated responsibilities.
status: draft
related:
  smells: []
  laws: []
```

### Exercise

```yaml
id: EXERCISE-001
type: exercise
name: Recent Decision Review
purpose: Help the reader inspect decision cost.
status: draft
related:
  chapters: []
  concepts: []
```

### Checklist

```yaml
id: CHECKLIST-001
type: checklist
name: Architecture Review Checklist
purpose: Guide review without replacing judgment.
status: draft
related:
  rituals: []
  artifacts: []
```

### Diagram

```yaml
id: DIAGRAM-001
type: diagram
name: Knowledge Model Overview
purpose: Show relationships between PEAK entities.
status: draft
related:
  concepts: []
  chapters: []
```

### Chapter

```yaml
id: CHAPTER-001
type: chapter
name: What Is a Principal Engineer?
path: book/01-thinking-like-a-principal/01-what-is-a-principal-engineer.md
status: draft
related:
  concepts: []
```

### Reference Project Component

```yaml
id: REF-001
type: reference_project_component
name: Component Name
purpose: Demonstrate a concept in the reference project.
status: proposed
related:
  concepts: []
  chapters: []
```

## Relationship Types

- `references`: one entity points readers to another.
- `explains`: one entity explains another.
- `illustrates`: a story, failure, diagram, or chapter makes a concept concrete.
- `violates`: an anti-pattern, smell, or failure breaks a law or principle.
- `mitigates`: an artifact, ritual, or practice reduces the risk of another entity.
- `depends_on`: one entity requires another to be understood or used.
- `related_to`: a loose relationship without stronger semantics.
- `appears_in`: an entity appears in a chapter, story, or artifact.
- `produces`: a ritual creates an artifact or decision.
- `replaces`: one entity replaces another.
- `supersedes`: one entity formally takes the place of an older one.
- `conflicts_with`: two entities are in tension and require trade-off discussion.

Use the strongest accurate relationship type. Use `related_to` only when a more precise type would be misleading.

## Lifecycle

Entities move through this lifecycle:

1. proposed
2. draft
3. reviewed
4. canonical
5. deprecated
6. retired

Deprecated and retired entities keep their IDs.

## Canon Rules

- One concept must have one canonical name.
- Do not introduce a new term if an existing term already covers it.
- Every new law must be linked to at least one story, smell, or failure.
- Every new artifact must have a template or example.
- Every smell must have recovery guidance.
- Every chapter should reference existing concepts instead of redefining them.

## Review Process

Ask these questions before adding or changing knowledge entities:

- Is this a new concept or a duplicate?
- Does it need a stable ID?
- What concepts does it depend on?
- What chapters will reference it?
- What failure story proves its value?
- What artifact or ritual operationalizes it?

## AI Navigation

The knowledge model should eventually support AI-assisted search and review.

Examples:

- Show all failure stories related to Change Radius.
- Show all ADRs connected to Every API Is a Promise.
- Find chapters that introduce concepts without canon entries.
