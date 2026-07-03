# Sprint 0 Review

## Summary

Sprint 0 created a coherent manuscript foundation for *The Principal Engineer Handbook*. The repository is ready for author-approved draft import and early manuscript development, with one structural decision still needing clarification: whether `book/` is the canonical manuscript source and `docs/` is only the publishing surface.

No new chapters were written during this review.

## What Is Good

- The required `book/`, `editor/`, `editor/decisions/`, `templates/`, `assets/`, and `tools/` areas exist.
- Every top-level project folder has a clear purpose.
- The README explains the title, subtitle, non-goals, current status, structure, contribution model, and decision documentation process.
- `editor/ARCHITECTURE_VISION.md` defines mission, non-goals, core philosophy, and long-term repository expectations.
- `editor/BOOK_BIBLE.md` records the working title, subtitle, book structure, editorial rules, and chapter lifecycle.
- `editor/CANON.md` has the required sections for laws, maxims, artifacts, rituals, metrics, smells, and anti-patterns.
- `editor/STYLE_GUIDE.md` is strict enough to prevent generic advice, filler, and unsupported principles.
- The initial ADRs use a consistent format: Status, Context, Decision, Consequences, and Alternatives Considered.
- Templates are practical and short enough to use during real editorial work.
- Empty major manuscript and asset directories have short README placeholders.
- No vague folder names such as `misc`, `common`, `stuff`, or `utils` were found.
- Markdown headings are consistently spaced and readable.

## What Needs Improvement

- Define the canonical manuscript source. The repository currently has both `book/` and `docs/manuscript/`.
- Replace broad `AUTHOR NOTE:` placeholders with author-approved decisions as soon as authors provide them.
- Decide how root pointer files such as `BOOK_BIBLE.md`, `ROADMAP.md`, and `STYLE_GUIDE.md` should stay aligned with `editor/`.
- Confirm whether generated documentation should be built directly from `book/` or mirrored into `docs/`.

## Missing Artifacts

- Author-approved draft import.
- Target audience definition.
- Reader promise.
- Tone constraints.
- Recurring chapter sections.
- Canonical metrics.
- Canonical anti-patterns.
- Release versioning rules.

## Structural Risks

- Parallel manuscript locations can drift if `book/` and `docs/manuscript/` both contain manuscript content.
- Root maintainer files that point to `editor/` can become stale if they grow beyond simple pointers.
- Build tooling exists from the earlier bootstrap, but the Sprint 0 manuscript structure does not yet define how publishing consumes `book/`.

## Editorial Risks

- Placeholders could be mistaken for approved editorial direction if they remain too long.
- The canon currently names required categories but does not yet distinguish approved concepts from future candidates beyond author notes.
- The style guide is strict, but chapter review will need examples of acceptable edits once real draft material exists.
- ADRs are useful, but maintainers may overuse them for minor editorial cleanups unless the threshold is clarified.

## Recommended Next Actions

1. Decide whether `book/` is the canonical manuscript source.
2. Import the existing author-approved draft into the chosen manuscript structure.
3. Replace high-priority `AUTHOR NOTE:` placeholders in `ARCHITECTURE_VISION.md` and `BOOK_BIBLE.md`.
4. Define recurring chapter sections before splitting full chapters.
5. Decide how MkDocs should consume manuscript files without creating duplicate content.
6. Add one ADR for the canonical manuscript source if the decision affects build and editorial workflow.
