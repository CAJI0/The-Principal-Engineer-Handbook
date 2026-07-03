# The Principal Engineer Handbook

Repository for maintaining the manuscript and publishing pipeline for *The Principal Engineer Handbook*.

This repository is maintained with a strict authorship boundary: maintainers may organize, refactor, format, cross-reference, and improve the manuscript infrastructure, but the intellectual content belongs to the authors.

## Repository Map

- `docs/` - MkDocs source files for the web edition.
- `docs/manuscript/` - manuscript chapters and appendices.
- `docs/assets/` - images, diagrams, and other static assets.
- `.github/` - GitHub issue templates, pull request template, and repository metadata.
- `.vale/` - Vale style rules.

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
ENABLE_PDF_EXPORT=1 mkdocs build --strict
```

On Windows PowerShell:

```powershell
$env:ENABLE_PDF_EXPORT="1"; mkdocs build --strict
```

Run Markdown and spelling checks after installing Node dependencies:

```powershell
npm install
npm run lint
```

Run Vale after installing Vale:

```powershell
vale sync
vale docs
```

## Manuscript Policy

Do not invent content. If a section needs author input, add a clear `AUTHOR NOTE:` or open an issue.
