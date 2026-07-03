# Source of Truth Policy

## Purpose

The repository needs explicit source-of-truth rules because it contains a manuscript, editorial policy, reusable templates, a knowledge base, and publishing support. Without ownership rules, the same information can drift across files.

## Manuscript

Canonical manuscript content lives in:

`book/`

`docs/` must not contain duplicate canonical manuscript content.

## Published Documentation

`docs/` is reserved for generated site content, publishing support, or documentation derived from the manuscript and knowledge base.

If manual content is placed in `docs/`, it must clearly explain why it is not part of `book/`.

## Knowledge Concepts

Human-readable concept explanations live in:

`knowledge/<category>/<concept>.md`

Machine-readable metadata and relationships live in:

`knowledge/index.yaml`

## Canon

`editor/CANON.md` defines editorial canon and high-level conceptual boundaries.

It must not duplicate full concept definitions from `knowledge/`.

## Book Architecture

`editor/BOOK_BIBLE.md`, `editor/ARCHITECTURE_VISION.md`, and related editor documents define how the book is written and governed.

They must not duplicate manuscript content.

## Templates

Reusable process templates live in:

`templates/`

## Rule

If two files appear to own the same information, create or update an ADR before expanding either one.
