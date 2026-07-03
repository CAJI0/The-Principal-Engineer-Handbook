# Contributing

Thanks for helping maintain *The Principal Engineer Handbook*.

## Maintainer Boundary

Maintainers may:

- Organize files and sections.
- Refactor headings and navigation.
- Improve formatting and consistency.
- Add cross-references.
- Add build, lint, review, and release infrastructure.
- Mark unclear areas for author review.

Maintainers must not:

- Invent new manuscript arguments, examples, frameworks, stories, or conclusions.
- Rewrite author intent without review.
- Add unverified claims.
- Add third-party text without license review.

## Workflow

1. Open or reference an issue for non-trivial work.
2. Keep pull requests focused.
3. Document major editorial or structural decisions as ADRs in `editor/decisions/`.
4. Run the quality checks that apply to the changed files.
5. Mark any author decisions clearly in the pull request.

## Author Notes

Use this format when the manuscript needs author input:

```markdown
> AUTHOR NOTE: Describe the missing decision or source needed here.
```

## Templates

Use the templates in `templates/` for ADRs, RFCs, decision journals, architecture reviews, and chapters.
