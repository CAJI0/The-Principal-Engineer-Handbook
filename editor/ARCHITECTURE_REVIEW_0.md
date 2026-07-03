# Architecture Review 0

## Status

Review Completed

## Scope

What was reviewed:

- Repository structure
- Manuscript structure
- Editor documents
- PEAK knowledge model
- `knowledge/index.yaml`
- Templates
- Contribution process

## Review Summary

The repository has a strong foundation for a long-term handbook project. The manuscript, editorial system, chapter architecture, and PEAK knowledge model are coherent enough to continue, but the foundation should not be frozen yet.

The main issue is not missing content. The main issue is source-of-truth clarity. The repository now has several useful representations of the same concepts: `editor/CANON.md`, concept Markdown files, and `knowledge/index.yaml`. That is acceptable at this stage, but it will become expensive unless ownership rules and synchronization rules are defined before the knowledge base grows.

Review decision: approved with actions.

## Strengths

- The repository separates manuscript, editor process, templates, assets, tools, and knowledge base.
- The `book/` structure is clear and ready for more manuscript work.
- The canonical chapter architecture gives future chapters a repeatable rhythm.
- PEAK gives the project a scalable model for concepts, relationships, stable IDs, and future navigation.
- The first chapter already uses the chapter architecture and demonstrates the intended editorial direction.
- Templates are practical and short.
- ADRs exist for early editorial decisions.
- The README gives a new contributor a reasonable first map of the project.

## Major Risks

- Source of truth is not yet defined for PEAK metadata. `editor/CANON.md`, concept Markdown files, and `knowledge/index.yaml` can drift.
- The relationship between `book/` and `docs/manuscript/` remains unresolved. Two manuscript trees will become a serious maintenance problem if both hold real content.
- `knowledge/index.yaml` is manually maintained and has no repository-level validation command yet.
- Stable IDs exist in YAML but are not embedded in the concept Markdown files, so humans browsing Markdown cannot see canonical IDs without checking the index.
- Lifecycle states are defined for PEAK entities, but there is no process for moving concepts from draft to reviewed to canonical.

## Medium Risks

- `editor/CANON.md` still duplicates some concept lists that now live in `knowledge/`.
- `BOOK_BIBLE.md` and `ARCHITECTURE_VISION.md` overlap in purpose and should remain clearly scoped.
- `STYLE_GUIDE.md` and `CHAPTER_ARCHITECTURE.md` are consistent now, but both may grow into competing instruction documents.
- The review process was implicit before this sprint; future contributions need explicit reviewer roles.
- Failure stories are currently concept records, not narrative assets. That is fine, but the distinction should remain clear.

## Minor Issues

- The root pointer files `BOOK_BIBLE.md`, `ROADMAP.md`, and `STYLE_GUIDE.md` are useful for discoverability but add another place to keep aligned.
- Some knowledge categories have both vocabulary entries and category entries with the same name, such as Change Radius and Architecture Health.
- The README points to the right areas, but it will need a shorter contributor path once the repository grows.
- There is no generated index yet for concepts grouped by stable ID.

## Scalability Review

Can this structure scale to 100 concepts?

Yes, if `knowledge/index.yaml` becomes governed by a clear source-of-truth rule and validation check.

Can this structure scale to 500 pages?

Yes, if `book/` is confirmed as the canonical manuscript source and `docs/` is treated as publishing output or generated documentation source.

Can this structure scale to 50 ADRs?

Yes. `editor/decisions/` is simple and clear. A future ADR index will be needed.

Can this structure scale to multiple formats?

Probably. MkDocs exists, but the manuscript-to-site relationship is not resolved.

Can this structure scale to a future website?

Yes, but the project needs a policy for generated navigation and duplicated docs content.

## Discoverability Review

A new contributor can find the book structure from README and `book/`.

A new contributor can find the canon from README and `editor/CANON.md`.

A new contributor can find knowledge concepts from README and `knowledge/README.md`.

A new contributor can find templates from `templates/`.

A new contributor can find decision records from `editor/decisions/`.

A new contributor can find contribution rules from `CONTRIBUTING.md`.

The main discoverability gap is knowing which file is authoritative when files overlap.

## Duplication Review

`CANON.md` vs `knowledge/index.yaml`:

Both list canonical concepts. `CANON.md` is readable; `index.yaml` is machine-readable. The project needs a rule for which one owns canonical metadata.

Concept Markdown files vs YAML index:

Markdown files own explanation. YAML owns IDs and graph relationships. This should be documented and validated.

`BOOK_BIBLE.md` vs `ARCHITECTURE_VISION.md`:

Both define direction. `ARCHITECTURE_VISION.md` should explain why the project exists. `BOOK_BIBLE.md` should record book-specific editorial rules.

`STYLE_GUIDE.md` vs `CHAPTER_ARCHITECTURE.md`:

The style guide should govern prose and editorial constraints. Chapter architecture should govern chapter structure.

## Naming Review

No vague folder names such as `misc`, `common`, `stuff`, or `utils` were found.

Naming is generally clear. PEAK entity names are readable and consistent.

The main naming risk is duplicate names across categories. For example, Change Radius exists as vocabulary and metric. That may be intentional, but it should be governed.

Capitalization is mostly consistent. Stable IDs provide a stronger naming anchor for future automation.

## Relationship Review

Relationship types are clear enough for the current graph.

The current relationships in `knowledge/index.yaml` are meaningful but sparse. That is appropriate for a first index.

Missing relationship rules:

- Whether relationships should be bidirectional.
- Whether every chapter must have at least one `references` relationship.
- Whether every smell must link to a recovery artifact or ritual.
- Whether every failure story must illustrate a law, smell, or anti-pattern.

Potential duplicate meanings:

- `references` and `appears_in` may overlap unless used carefully.
- `replaces` and `supersedes` need a clear distinction in practice.

## Lifecycle Review

Chapters:

Chapter lifecycle exists in `BOOK_BIBLE.md`, but review gates are not yet operationalized.

Concepts:

Concept lifecycle exists in `KNOWLEDGE_MODEL.md`, but concept files do not show lifecycle status.

ADRs:

ADRs have status sections and a consistent format.

Templates:

Templates are practical, but template lifecycle is not defined.

Failure stories:

Failure stories are tracked as PEAK entities, but the distinction between concept record and future manuscript story should remain explicit.

## AI Readiness Review

Stable IDs are usable.

`knowledge/index.yaml` is readable enough for future machine use.

Relationships are explicit but currently sparse.

Concept files are structured consistently enough for future parsing.

The main AI-readiness gap is validation. A future check should verify IDs, paths, relationship endpoints, approved relationship types, and drift between Markdown headings and YAML names.

## Recommended Actions

### Must Fix

- Decide the source-of-truth rule for PEAK metadata.
- Decide whether `book/` is the canonical manuscript source and what role `docs/manuscript/` plays.
- Define how `knowledge/index.yaml` is validated before the knowledge base grows.

### Should Fix

- Add stable IDs to concept Markdown files or document why IDs live only in YAML.
- Create a lightweight ADR index before ADR count grows.
- Clarify the difference between `references` and `appears_in`.
- Clarify whether duplicate names across PEAK categories are allowed.
- Define lifecycle movement for concepts and chapters.

### Could Fix

- Add a generated or manually maintained concept index by stable ID.
- Add a short contributor path to README.
- Add review labels or templates for canon review and knowledge review.
- Add a future validation script when build tooling is allowed.

## Review Decision

Approved with actions

## Next Step Recommendation

Perform cleanup before returning to manuscript writing.

The next sprint should focus on foundation freeze or cleanup. The foundation is strong, but it should not be frozen until source-of-truth decisions are made for manuscript structure and PEAK metadata.

## Sprint 6 Follow-up

Addressed actions:

- Created `editor/SOURCE_OF_TRUTH.md`.
- Clarified that `book/` is the canonical manuscript source.
- Clarified that `docs/` is reserved for generated or published documentation support.
- Defined ownership between Markdown concept files and `knowledge/index.yaml`.
- Added stable IDs as YAML front matter in existing knowledge concept files.
- Added missing index entries for existing vocabulary, artifact, and ritual concept files.
- Updated category README files to mention front matter and YAML relationships.

Remaining open actions:

- Decide how existing starter content in `docs/manuscript/` should evolve.
- Decide when validation tooling for `knowledge/index.yaml` should be introduced.
- Decide whether duplicate names across PEAK categories require an ADR.
- Decide when the foundation is ready for Freeze 0.
