# Review Process

## Purpose

The handbook uses review discipline similar to software projects because the book is an engineering system. Chapters, concepts, ADRs, templates, and knowledge records should be reviewed before they become difficult to change.

## Review Types

### Editorial Review

Checks clarity, structure, flow, and style.

### Canon Review

Checks consistency with laws, principles, vocabulary, and PEAK.

### Knowledge Review

Checks whether new concepts duplicate existing concepts or require stable IDs.

### Chapter Architecture Review

Checks whether the chapter follows the canonical chapter structure.

### Technical Review

Checks engineering correctness.

### Freeze Review

Final check before marking content as Freeze-ready.

## Chapter Lifecycle

The owner-approved Phase 2 chapter lifecycle is:

1. Draft
2. Editorial Review
3. Canon Review
4. Technical Review
5. Freeze

## Review Outcomes

- Approved
- Approved with minor changes
- Request changes
- Rework required
- Reject

## Chapter Review Checklist

- One main idea.
- Realistic engineering story.
- Trade-off.
- Practical exercise.
- ADR or decision artifact.
- Principal's Notebook.
- No undefined terminology.
- References PEAK concepts where needed.
- No unnecessary new terms.
- No repeated concept already covered elsewhere.

## Concept Review Checklist

- Does this concept need to exist?
- Does it duplicate another concept?
- Does it have a stable ID?
- Does it link to laws, smells, stories, artifacts, or chapters?
- Does it have recovery guidance if it is a smell or anti-pattern?

## ADR Review Checklist

- Clear context.
- Actual decision.
- Alternatives considered.
- Consequences.
- Review date if needed.

## Freeze Criteria

Content can be frozen only when:

- No major review issues remain.
- Terminology is consistent.
- Related concepts are linked.
- Style guide is followed.
- Chapter adds value to the whole handbook.

## Reviewer Roles

### Author

Creates or revises manuscript content and supplies intellectual content.

### Editor

Improves clarity, structure, flow, and consistency without inventing content.

### Technical Reviewer

Checks engineering correctness and practical credibility.

### Canon Reviewer

Checks consistency with canon, chapter architecture, and PEAK concepts.

### Repository Maintainer

Maintains structure, templates, links, process, and review hygiene.
