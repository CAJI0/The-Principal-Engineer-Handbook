# The Principal Engineer Handbook

Building Embedded Systems That Survive Change

This is a professional long-term book project about how Principal Engineers think, design, document, review, and evolve long-living embedded systems.

This is not a C tutorial. This is not an STM32 tutorial. This is a handbook about engineering thinking, architecture, decision-making, and long-living embedded systems.

Current status: early draft / PEAK knowledge model foundation.

The repository itself must demonstrate the engineering practices described in the book.

## Repository Structure

- `book/` - manuscript structure.
- `book/00-front-matter/` - front matter.
- `book/01-thinking-like-a-principal/` - part or chapter workspace.
- `book/02-the-laws/` - part or chapter workspace.
- `book/03-architecture-playbook/` - part or chapter workspace.
- `book/04-building-a-product/` - part or chapter workspace.
- `book/05-engineering-organization/` - part or chapter workspace.
- `book/06-legacy/` - part or chapter workspace.
- `book/appendix/` - appendix workspace.
- `editor/` - editorial operating system for the book.
- `editor/decisions/` - ADRs for major editorial and architectural decisions in the book project.
- `knowledge/` - PEAK knowledge base for reusable concepts.
- `templates/` - reusable editorial and review templates.
- `assets/` - diagrams, images, cover assets, examples, and reference-project material.
- `tools/` - helper scripts and automation, when needed.
- `docs/` - MkDocs source files for the web edition.
- `.github/` - GitHub issue templates, pull request template, and repository metadata.
- `.vale/` - Vale style rules.

## Contributing

Maintainers may organize, refactor, format, cross-reference, and improve maintainability. Maintainers must not invent manuscript content.

Use issues and pull requests for non-trivial work. Mark author decisions with `AUTHOR NOTE:` or track them in `editor/OPEN_QUESTIONS.md`.

## Decision Documentation

Major editorial and structural decisions are documented as ADRs in `editor/decisions/`.

Use `templates/adr-template.md` for new ADRs.

## Reader-Facing Manuscript

- [Manifesto](book/00-front-matter/manifesto.md)
- [Preface](book/00-front-matter/preface.md)
- [Table of Contents](book/00-front-matter/table-of-contents.md)

## Editorial Reference

- [Architecture Vision](editor/ARCHITECTURE_VISION.md)
- [Book Bible](editor/BOOK_BIBLE.md)
- [Canon](editor/CANON.md)
- [Style Guide](editor/STYLE_GUIDE.md)

## Knowledge Base

This repository includes a structured knowledge base under [knowledge/](knowledge/README.md).

It defines the vocabulary, laws, artifacts, rituals, smells, metrics, and failure stories used throughout the handbook.

The PEAK domain model is documented in [Knowledge Model](editor/KNOWLEDGE_MODEL.md), and the first machine-readable index lives at [knowledge/index.yaml](knowledge/index.yaml).

The first repository architecture review is documented in [Architecture Review 0](editor/ARCHITECTURE_REVIEW_0.md), and the review workflow is defined in [Review Process](editor/REVIEW_PROCESS.md).

## Source of Truth

Canonical manuscript content lives in [book/](book/README.md).

[docs/](docs/index.md) is reserved for generated or published documentation support. Canonical chapter text must not be duplicated in `docs/`.

Repository ownership rules are documented in [Source of Truth Policy](editor/SOURCE_OF_TRUTH.md).

## Local Preview

Install the documentation dependencies:

```powershell
pip install -r requirements.txt
```

Run the local site:

```powershell
mkdocs serve
```

Build the site:

```powershell
mkdocs build --strict
```

Build the PDF:

```powershell
ENABLE_PDF_EXPORT=1 mkdocs build --config-file mkdocs-pdf.yml
```

On Windows PowerShell:

```powershell
$env:ENABLE_PDF_EXPORT="1"; mkdocs build --config-file mkdocs-pdf.yml
```

Run Markdown and spelling checks after installing Node dependencies:

```powershell
npm install
npm run lint
```

Run Vale after installing Vale:

```powershell
vale sync
vale .
```

## Manuscript Policy

Do not invent content. If a section needs author input, add a clear `AUTHOR NOTE:` or open an issue.
