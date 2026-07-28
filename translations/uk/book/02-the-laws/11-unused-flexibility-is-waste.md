# Невикористана гнучкість — це марнування

## Вступна цитата

> Option не є безкоштовною після того, як system мусить її пам'ятати.

## Історія

Radio service був спроєктований так, ніби мав пережити продукти, яких ще не існувало.

Перший product потребував одного validated transport: one radio module, one board family, one packet format, one field service workflow. Release already needed service to wake radio, send command, receive response, retry safely, report diagnostics, and recover after reset.

Team knew product line might grow: lower-cost board, long-range transport, manufacturing service mode, second radio module, different packet-framing rule. These possibilities were not absurd. Hardware changes, customers ask for variants, and supply chains turn dependencies into release problems.

So team preserved options.

Service gained runtime mode selector, transport strategies, conditional compilation for unapproved boards, fallback for weak-link prototype, service-tool compatibility path, test-only configuration that later leaked, and dormant hardware transport. Code looked careful: interfaces, flags, runtime modes, tests, comments saying some modes were not used yet but might be needed later.

Only one combination shipped.

Production controller used validated radio module, production packet format, normal runtime mode, and supported service-tool flow. The rest stayed because "we may need it later" sounded cheaper than decision.

Field defect was narrow: after noisy gateway drop during command exchange, shipped transport received late response after retry. Production path should classify late response, keep retry bounded, and report diagnostic. Some units instead reported `radio unavailable` and stopped retrying.

Bug looked like radio work until review touched flexible service. Retry state depended on runtime mode. Error mapping depended on current radio, dormant long-range transport, or prototype fallback. Parser carried unused packet branch. Diagnostic path used generic mode names. Service tool exposed old prototype compatibility switch. CI built unsupported variants.

Defect was in shipped path, but team had to reason about everything around it.

Proposals kept discomfort alive: keep all modes, test every combination, mark paths legacy, hide unsupported docs, add production bypass flag, move selector to compile time, add abstraction layer, clean up later.

Principal Engineer asked team to list every mode, backend, build flag, fallback path, service-tool compatibility behavior, test-only switch, dormant implementation, and board branch without using word flexible. For each: who uses it, which product supports it, tests, tools, docs, uncertainty protected, owner, and retirement decision.

Most rows were quiet.

Production transport had evidence and owner. Prototype compatibility path had history but no owner: Temporary Solution (`ANTIPATTERN-006`). Dormant long-range transport had hope but no evidence; its error model already leaked: Platform Leakage (`SMELL-005`). Runtime selector created Boolean Explosion (`SMELL-003`). Board flags affected CI, release packaging, manufacturing scripts, and confidence.

Team measured Change Radius (`VOCAB-001` and `METRIC-001`): unit tests, integration tests, CI jobs, service-tool behavior, field diagnostics, release notes, security review, manufacturing scripts, support explanations.

"This is not a flexible service," Principal Engineer said. "It is a service with unowned options charging rent."

Team kept one narrow product-owned transport seam, but removed unsupported runtime modes from shipped builds, deleted exposed unsupported configuration, removed dormant implementation and prototype fallback, reduced CI to supported combinations plus seam tests, migrated service tests, updated diagnostics, and recorded evidence that old compatibility users had ended.

ADR captured the material decision. Smaller retained options went to Decision Journal (`ARTIFACT-003`). Discoverability (`METRIC-003`) improved: a new engineer could find supported variations, owner, why seam remained, and conditions for another implementation.

Radio service became less flexible visibly. It became more able to change.

## Обговорення

`LAW-006` states: Flexibility that is not used or justified becomes maintenance cost.

This is not complaint about abstraction. Engineers should preserve options when real uncertainty justifies cost. Problem is that options become system surface long before anyone uses them.

Flexibility has value only when it protects material uncertainty. Options without use, evidence, owner, or review trigger become maintenance cost.

Separate flexibility from variability. Variability is supported product/environment/operation difference with consumers, tests, docs, support expectations, and owners. Hypothetical future mode is different.

Separate flexibility from optionality. Optionality may preserve ability to decide later without shipping every possible implementation now. A team can preserve a narrow seam without carrying dormant transports, runtime modes, and public selector.

Flexibility is used when supported product, environment, workflow, customer, deployment, or test strategy actively depends on it. It may be justified before use if uncertainty is material, alternatives known, adding later expensive, seam small, owner exists, review trigger clear, evidence real.

Flexibility becomes waste when no supported user, no material uncertainty, no evidence, no owner, no review trigger, and unbounded continuing cost exist.

Runtime flexibility is easiest to feel in incidents: modes, runtime flags, selectable backends, fallback behavior, product configuration. Compile-time flexibility moves cost to CI, release packaging, manufacturing, service tools, and support. Architectural flexibility - seams, adapters, extension points, compatibility layers - can be valuable, but seam is not inventory of imagined changes.

Cost surface is wider than code: state combinations, tests, CI matrices, release packaging, configuration migration, docs, review, support, manufacturing, diagnostics, security review, compatibility, rollback, upgrade, deletion.

Boolean Explosion (`SMELL-003`) appears when independent flags create combinations nobody owns. Platform Leakage (`SMELL-005`) appears when dormant platform detail shapes product logic. Temporary Solution (`ANTIPATTERN-006`) survives when owner, trigger, and removal condition disappear.

Remedy is not deletion by search result. Removing flexibility is architecture decision when code, tests, tools, docs, workflows, or shipped versions may depend on it. Prove use/non-use, identify consumers, migrate tools/tests, delete configuration, reduce CI, update docs, check manufacturing and field workflows, define rollback boundaries, and preserve evidence.

Retained flexibility needs evidence, ownership, and review trigger. ADR (`ARTIFACT-001`) fits large decisions. Decision Journal (`ARTIFACT-003`) fits smaller retained options. Discoverability matters because unused flexibility hides in plain sight.

The practical test: if option protects real uncertainty or supports owned variation, pay deliberately. Otherwise remove option or preserve only smallest seam justified by evidence.

## Інженерний принцип

Keep flexibility only when it protects real uncertainty or supports owned variation. Otherwise remove option and preserve only smallest seam justified by evidence.

Questions:

1. Who uses this option today?
2. Which real uncertainty does it protect against?
3. What would it cost to add later?
4. Which products, tools, tests, or workflows support it?
5. Who owns it?
6. Which tests prove supported combinations?
7. What documentation and tools expose it?
8. Which compatibility obligations exist?
9. What condition will trigger review or retirement?
10. Which seam can remain if option removed?

## Архітектурна вправа

### Перевірте одну точку гнучкості

Choose one flexibility point: mode, flag, backend, interface, fallback, build option, compatibility layer, extension point.

1. What is exact option name?
2. Which products, customers, tools, tests, or workflows use it today?
3. What evidence shows use?
4. What uncertainty does it protect?
5. What would it cost to add later if removed now?
6. Runtime, compile time, or architecture boundary?
7. Which state combinations does it create?
8. Which tests required because it exists?
9. What does it add to CI/release matrix?
10. What documentation mentions it?
11. Which service-tool, manufacturing, or field-support behavior exposes it?
12. What failure or security-review surface does it create?
13. Which compatibility obligations depend on it?
14. Who owns option?
15. What condition triggers review or retirement?
16. What evidence proves it can be removed?
17. Which consumers need migration?
18. What is smallest seam worth preserving?
19. Where should decision live: ADR or Decision Journal?

End with one decision:

- keep and own;
- narrow;
- defer;
- remove;
- preserve only the seam;
- create a review trigger with a date or condition.

Do not create new artifact for exercise. Use records system already has.

## Нотатник Principal Engineer

- Options charge rent.
- A seam is not every path.
- Temporary needs a trigger.

## ADR

### Chapter ADR: Remove Unsupported Runtime Modes and Preserve One Transport Seam

### Context

One shipped product uses one validated communication path. Radio service also contains dormant runtime modes, transport candidates, conditional build paths, prototype compatibility behavior, test-only configuration, and fallback branches.

Unsupported combinations affect tests, review, diagnostics, service tools, release packaging, and security review. Future transport variation is plausible, but no current product owns dormant implementations.

### Decision

Define single supported runtime mode for current product. Remove unsupported runtime modes from shipped builds. Delete configuration exposing unsupported behavior. Remove dormant implementations and old prototype fallback. Reduce CI and release packaging to supported combinations plus focused seam tests.

Preserve one narrow product-owned transport seam with product meanings: send accepted, response received, late response, retry allowed, radio unavailable, unsupported transport, permanent failure. Assign owner and review trigger. Document compatibility obligations. Use Decision Journal for smaller retained options.

### Consequences

Supported behavior becomes clearer. State space and test combinations shrink. Review, diagnosis, service tools, diagnostics, Boolean Explosion, and unsupported behavior reduce. Product keeps future change seam without shipping every imagined transport.

Migration work remains. Tests and tools using prototype behavior must change. Evidence retained. Removed path may need rebuilding if future product makes it real. Retained seam requires discipline.

### Alternatives Considered

Keep all modes until future product appears. Maximum apparent flexibility, ongoing cost.

Test every combination. Expands cost instead of deciding supported combinations.

Hide unsupported options in documentation while retaining behavior. Keeps runtime and diagnostic ambiguity.

Replace runtime options with compile-time flags. Helps only if unsupported combinations removed from CI, packaging, tools, support.

Remove all abstraction and call hardware APIs directly. Discards justified seam.

Duplicate subsystem per product. Creates parallel behavior before variation exists.

Build broader plug-in framework. Formalizes speculative surface.

Postpone cleanup. Leaves next defect to rediscover same unowned options.

## Коментар редактора

Chapter 11 focuses on option surface. It does not reteach state authority, API promises, dependency selection, or time. It makes one narrower claim: unused flexibility is maintenance cost unless evidence, ownership, and review triggers justify paying for it.

The PEAK concepts carrying this chapter are Unused Flexibility Is Waste (`LAW-006`), Boolean Explosion (`SMELL-003`), Platform Leakage (`SMELL-005`), Temporary Solution (`ANTIPATTERN-006`), Change Radius (`VOCAB-001` and `METRIC-001`), Discoverability (`METRIC-003`), ADR (`ARTIFACT-001`), and Decision Journal (`ARTIFACT-003`).
