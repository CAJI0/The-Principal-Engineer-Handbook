# Ukrainian Translation Validation Checklist

## Source Mapping

- Every source chapter has exactly one Ukrainian counterpart once translation begins.
- Every Appendix file has exactly one Ukrainian counterpart once Appendix translation begins.
- Ukrainian file paths mirror the English source structure unless a phase explicitly approves a publishing-only adjustment.
- English source files under `book/` are not modified during translation phases unless explicitly requested.

## ID Preservation

- IDs such as `CHAPTER-037`, `LAW-001`, `ARTIFACT-002`, `SMELL-001`, `METRIC-001`, `RITUAL-001`, and `FAILURE-001` remain unchanged.
- PEAK concept IDs remain unchanged.
- Chapter IDs, artifact IDs, law IDs, smell IDs, metric IDs, ritual IDs, and failure IDs remain unchanged.

## Content Quality

- Ukrainian prose follows `STYLE_GUIDE.md`.
- Glossary choices from `TERMINOLOGY_GLOSSARY.md` are applied consistently.
- No conceptual rewriting is introduced.
- No large accidental English prose blocks remain, except accepted technical terms and preserved identifiers.
- No `AUTHOR NOTE`, `TODO`, or placeholder text remains in Ukrainian release output.

## Links And Publishing

- Links are checked for each phase.
- Ukrainian MkDocs configuration will be built separately when added.
- Ukrainian PDF output must include all 37 chapters plus the Appendix before release.
- Generated output such as `site/` must not be tracked.

## Spell-Check Strategy

The current repository spelling tooling is English-oriented. Ukrainian translation phases must not mass-add Ukrainian words to the English dictionary.

Until Ukrainian-aware spelling tooling is selected, `translations/uk/**` is excluded from the English cspell pass. This is a scoped validation policy, not a waiver for Ukrainian editorial review.

Follow-up for translation phases:

- choose Ukrainian-aware spelling or proofreading tooling;
- document how it runs for `translations/uk/**`;
- keep English spelling checks active for the existing English manuscript and repository docs;
- record any accepted Ukrainian technical terms in this workstream, not in the global English dictionary.

## Phase Completion

A translation phase is complete only when:

- source-to-target mapping is complete for the declared scope;
- IDs and machine-readable text are preserved;
- terminology review is complete;
- Ukrainian editorial review is complete;
- publishing review is complete for the phase's current publishing surface;
- validation results and known follow-ups are recorded.
