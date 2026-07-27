"""Generate MkDocs manuscript pages from canonical book files.

Canonical manuscript text lives in ``book/``. This script creates derived
publishing pages under ``docs/manuscript/``. The generated pages are safe to
regenerate and must not be edited as manuscript source.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "book"
DOCS_MANUSCRIPT = ROOT / "docs" / "manuscript"

FRONT_MATTER = [
    ("Manifesto", "00-front-matter/manifesto.md"),
    ("Preface", "00-front-matter/preface.md"),
    ("Table of Contents", "00-front-matter/table-of-contents.md"),
]

PARTS = [
    (
        "Part I - Thinking Like a Principal Engineer",
        [
            ("What Is a Principal Engineer?", "01-thinking-like-a-principal/01-what-is-a-principal-engineer.md"),
            ("Decision-Making Under Constraints", "01-thinking-like-a-principal/02-decision-making-under-constraints.md"),
            ("Asking Better Engineering Questions", "01-thinking-like-a-principal/03-asking-better-engineering-questions.md"),
            ("Ownership Beyond Code", "01-thinking-like-a-principal/04-ownership-beyond-code.md"),
            ("Technical Judgment and Evidence", "01-thinking-like-a-principal/05-technical-judgment-and-evidence.md"),
            ("Leaving Systems Better Than You Found Them", "01-thinking-like-a-principal/06-leaving-systems-better-than-you-found-them.md"),
        ],
    ),
    (
        "Part II - The Laws",
        [
            ("Every State Has One Owner", "02-the-laws/07-every-state-has-one-owner.md"),
            ("Every API Is a Promise", "02-the-laws/08-every-api-is-a-promise.md"),
            ("Every Dependency Is a Decision", "02-the-laws/09-every-dependency-is-a-decision.md"),
            ("Time Is a Dependency", "02-the-laws/10-time-is-a-dependency.md"),
            ("Unused Flexibility Is Waste", "02-the-laws/11-unused-flexibility-is-waste.md"),
            ("Simplicity Is a Feature", "02-the-laws/12-simplicity-is-a-feature.md"),
            ("Evidence Before Confidence", "02-the-laws/13-evidence-before-confidence.md"),
        ],
    ),
    (
        "Part III - Architecture Playbook",
        [
            ("Drawing Boundaries That Survive Change", "03-architecture-playbook/14-drawing-boundaries-that-survive-change.md"),
            ("Managing Change Radius", "03-architecture-playbook/15-managing-change-radius.md"),
            ("Designing for Failure and Recovery", "03-architecture-playbook/16-designing-for-failure-and-recovery.md"),
            ("Using ADRs and RFCs Well", "03-architecture-playbook/17-using-adrs-and-rfcs-well.md"),
            ("Reviewing Architecture Before It Hardens", "03-architecture-playbook/18-reviewing-architecture-before-it-hardens.md"),
            ("Freezing Architecture Without Freezing Learning", "03-architecture-playbook/19-freezing-architecture-without-freezing-learning.md"),
        ],
    ),
    (
        "Part IV - Building a Product",
        [
            ("From Prototype to Product", "04-building-a-product/20-from-prototype-to-product.md"),
            ("Designing for Manufacturing and Field Reality", "04-building-a-product/21-designing-for-manufacturing-and-field-reality.md"),
            ("Configuration, Variants, and Product Lines", "04-building-a-product/22-configuration-variants-and-product-lines.md"),
            ("Observability in Embedded Systems", "04-building-a-product/23-observability-in-embedded-systems.md"),
            ("Release Discipline and Upgrade Paths", "04-building-a-product/24-release-discipline-and-upgrade-paths.md"),
            ("Reference Project Walkthrough", "04-building-a-product/25-reference-project-walkthrough.md"),
        ],
    ),
    (
        "Part V - Engineering Organization",
        [
            ("Technical Leadership Without Authority", "05-engineering-organization/26-technical-leadership-without-authority.md"),
            ("Design Reviews as Shared Memory", "05-engineering-organization/27-design-reviews-as-shared-memory.md"),
            ("Building Engineering Rituals", "05-engineering-organization/28-building-engineering-rituals.md"),
            ("Mentoring Through Artifacts", "05-engineering-organization/29-mentoring-through-artifacts.md"),
            ("Aligning Teams Around Decisions", "05-engineering-organization/30-aligning-teams-around-decisions.md"),
            ("Architecture Health Reviews", "05-engineering-organization/31-architecture-health-reviews.md"),
        ],
    ),
    (
        "Part VI - Legacy",
        [
            ("Reading a Legacy System", "06-legacy/32-reading-a-legacy-system.md"),
            ("Finding Silent Coupling", "06-legacy/33-finding-silent-coupling.md"),
            ("Managing Utility Gravity", "06-legacy/34-managing-utility-gravity.md"),
            ("Reducing Boolean Explosion", "06-legacy/35-reducing-boolean-explosion.md"),
            ("Deleting Safely", "06-legacy/36-deleting-safely.md"),
            ("Refactoring Without Losing Product Trust", "06-legacy/37-refactoring-without-losing-product-trust.md"),
        ],
    ),
]

APPENDIX = [
    ("Appendix Overview", "appendix/README.md"),
    ("ADR Template", "appendix/adr-template.md"),
    ("RFC Template", "appendix/rfc-template.md"),
    ("Decision Journal Template", "appendix/decision-journal-template.md"),
    ("Architecture Review Template", "appendix/architecture-review-template.md"),
    ("Chapter Review Checklist", "appendix/chapter-review-checklist.md"),
    ("Glossary", "appendix/glossary.md"),
]


def manuscript_page_for(book_rel: str) -> str:
    source = BOOK / book_rel
    return (
        "<!-- Generated by tools/generate_publishing_docs.py. Do not edit as canonical manuscript source. -->\n\n"
        + source.read_text(encoding="utf-8").rstrip()
        + "\n"
    )


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def title_list(items: list[tuple[str, str]]) -> str:
    return "\n".join(f"- {title}" for title, _ in items)


def main() -> None:
    generated = []

    all_items = FRONT_MATTER + [item for _, items in PARTS for item in items] + APPENDIX
    for _, book_rel in all_items:
        target = DOCS_MANUSCRIPT / book_rel
        write(target, manuscript_page_for(book_rel))
        generated.append(target)

    write(
        DOCS_MANUSCRIPT / "index.md",
        "# Manuscript\n\n"
        "This publishing section is generated from the canonical manuscript in `book/`.\n"
        "Edit `book/` first, then regenerate these wrappers with `python tools/generate_publishing_docs.py`.\n\n"
        "## Front Matter\n\n"
        f"{title_list(FRONT_MATTER)}\n\n"
        "## Chapters\n\n"
        "- Chapters 1-37\n\n"
        "## Appendix\n\n"
        "- Appendix templates and glossary\n",
    )

    write(
        DOCS_MANUSCRIPT / "front-matter.md",
        "# Front Matter\n\n"
        "Generated links to the canonical front matter.\n\n"
        f"{title_list(FRONT_MATTER)}\n",
    )

    chapter_sections = []
    for part_title, items in PARTS:
        chapter_sections.append(f"## {part_title}\n\n{title_list(items)}")
    write(
        DOCS_MANUSCRIPT / "chapters" / "index.md",
        "# Chapters\n\n"
        "Generated links to the canonical chapter wrappers.\n\n"
        + "\n\n".join(chapter_sections)
        + "\n",
    )

    write(
        DOCS_MANUSCRIPT / "appendices" / "index.md",
        "# Appendix\n\n"
        "Generated links to the canonical Appendix wrappers.\n\n"
        f"{title_list(APPENDIX)}\n",
    )

    print(f"Generated {len(generated) + 4} publishing pages under {DOCS_MANUSCRIPT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
