# Невикористана гнучкість — це марнування

## Вступна цитата

> Option не є безкоштовною після того, як system мусить її пам'ятати.

## Історія

Radio service був спроєктований так, ніби мав пережити продукти, яких ще не існувало.

Перший product потребував одного validated transport: one radio module, one board family, one packet format, one field service workflow. Release already needed service to wake radio, send command, receive response, retry safely, report diagnostics, and recover after reset.

Команда знала, що product line might grow: lower-cost board, long-range transport, manufacturing service mode, second radio module, different packet-framing rule. These possibilities were not absurd. Hardware changes, customers ask for variants, and supply chains turn dependencies into release problems.

Тому команда preserved options.

Service отримав runtime mode selector, transport strategies, conditional compilation for unapproved boards, fallback for weak-link prototype, service-tool compatibility path, test-only configuration that later leaked і dormant hardware transport. Code виглядав careful: interfaces, flags, runtime modes, tests, comments saying some modes were not used yet but might be needed later.

Shipped лише one combination.

Production controller used validated radio module, production packet format, normal runtime mode і supported service-tool flow. Решта лишилася, бо «we may need it later» звучало cheaper than decision.

Field defect був narrow: після noisy gateway drop during command exchange shipped transport received late response after retry. Production path мав classify late response, keep retry bounded і report diagnostic. Some units натомість reported `radio unavailable` and stopped retrying.

Bug виглядав як radio work, доки review не торкнувся flexible service. Retry state depended on runtime mode. Error mapping depended on current radio, dormant long-range transport або prototype fallback. Parser carried unused packet branch. Diagnostic path used generic mode names. Service tool exposed old prototype compatibility switch. CI built unsupported variants.

Defect був у shipped path, але team had to reason about everything around it.

Proposals залишали discomfort alive: keep all modes, test every combination, mark paths legacy, hide unsupported docs, add production bypass flag, move selector to compile time, add abstraction layer, clean up later.

Principal Engineer попросив team list every mode, backend, build flag, fallback path, service-tool compatibility behavior, test-only switch, dormant implementation і board branch без слова flexible. Для кожного: who uses it, which product supports it, tests, tools, docs, uncertainty protected, owner і retirement decision.

Більшість rows були quiet.

Production transport мав evidence і owner. Prototype compatibility path мав history, але no owner: Temporary Solution (`ANTIPATTERN-006`). Dormant long-range transport мав hope, але no evidence; його error model already leaked: Platform Leakage (`SMELL-005`). Runtime selector created Boolean Explosion (`SMELL-003`). Board flags affected CI, release packaging, manufacturing scripts і confidence.

Team виміряла Change Radius (`VOCAB-001` and `METRIC-001`): unit tests, integration tests, CI jobs, service-tool behavior, field diagnostics, release notes, security review, manufacturing scripts, support explanations.

"This is not a flexible service," Principal Engineer said. "It is a service with unowned options charging rent."

Команда kept one narrow product-owned transport seam, але removed unsupported runtime modes from shipped builds, deleted exposed unsupported configuration, removed dormant implementation and prototype fallback, reduced CI to supported combinations plus seam tests, migrated service tests, updated diagnostics, and recorded evidence that old compatibility users had ended.

ADR captured the material decision. Smaller retained options пішли до Decision Journal (`ARTIFACT-003`). Discoverability (`METRIC-003`) improved: new engineer міг знайти supported variations, owner, why seam remained і conditions for another implementation.

Radio service visibly став less flexible. Він став more able to change.

## Обговорення

`LAW-006` states: Flexibility that is not used or justified becomes maintenance cost.

Це не complaint about abstraction. Engineers should preserve options, коли real uncertainty justifies cost. Problem у тому, що options become system surface long before anyone uses them.

Flexibility має value лише тоді, коли protects material uncertainty. Options without use, evidence, owner або review trigger become maintenance cost.

Separate flexibility from variability. Variability — це supported product/environment/operation difference with consumers, tests, docs, support expectations і owners. Hypothetical future mode is different.

Separate flexibility from optionality. Optionality може preserve ability to decide later without shipping every possible implementation now. Team може preserve a narrow seam without carrying dormant transports, runtime modes і public selector.

Flexibility is used, коли supported product, environment, workflow, customer, deployment або test strategy actively depends on it. Вона може бути justified before use, якщо uncertainty material, alternatives known, adding later expensive, seam small, owner exists, review trigger clear, evidence real.

Flexibility becomes waste, коли no supported user, no material uncertainty, no evidence, no owner, no review trigger і unbounded continuing cost exist.

Runtime flexibility найлегше відчути в incidents: modes, runtime flags, selectable backends, fallback behavior, product configuration. Compile-time flexibility moves cost to CI, release packaging, manufacturing, service tools і support. Architectural flexibility — seams, adapters, extension points, compatibility layers — can be valuable, але seam is not inventory of imagined changes.

Cost surface ширша за code: state combinations, tests, CI matrices, release packaging, configuration migration, docs, review, support, manufacturing, diagnostics, security review, compatibility, rollback, upgrade, deletion.

Boolean Explosion (`SMELL-003`) appears, коли independent flags create combinations nobody owns. Platform Leakage (`SMELL-005`) appears, коли dormant platform detail shapes product logic. Temporary Solution (`ANTIPATTERN-006`) survives, коли owner, trigger і removal condition disappear.

Remedy — не deletion by search result. Removing flexibility — architecture decision, коли code, tests, tools, docs, workflows або shipped versions may depend on it. Prove use/non-use, identify consumers, migrate tools/tests, delete configuration, reduce CI, update docs, check manufacturing and field workflows, define rollback boundaries і preserve evidence.

Retained flexibility needs evidence, ownership і review trigger. ADR (`ARTIFACT-001`) fits large decisions. Decision Journal (`ARTIFACT-003`) fits smaller retained options. Discoverability matters, бо unused flexibility hides in plain sight.

Practical test: якщо option protects real uncertainty або supports owned variation, pay deliberately. Otherwise remove option або preserve only smallest seam justified by evidence.

## Інженерний принцип

Keep flexibility only when it protects real uncertainty або supports owned variation. Otherwise remove option і preserve only smallest seam justified by evidence.

Питання:

1. Хто uses this option today?
2. Від якої real uncertainty вона захищає?
3. Скільки коштувало б add later?
4. Які products, tools, tests або workflows support it?
5. Хто owns it?
6. Які tests prove supported combinations?
7. Яка documentation і tools expose it?
8. Які compatibility obligations exist?
9. Яка condition trigger review або retirement?
10. Яка seam може лишитися, якщо option removed?

## Архітектурна вправа

### Перевірте одну точку гнучкості

Оберіть одну flexibility point: mode, flag, backend, interface, fallback, build option, compatibility layer або extension point.

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

Завершіть одним decision:

- keep and own;
- narrow;
- defer;
- remove;
- preserve only the seam;
- create a review trigger with a date or condition.

Не створюйте нового artifact для цієї вправи. Використайте records, які system already has.

## Нотатник Principal Engineer

- Options charge rent.
- A seam is not every path.
- Temporary needs a trigger.

## ADR

### Chapter ADR: Remove Unsupported Runtime Modes and Preserve One Transport Seam

### Context

One shipped product використовує one validated communication path. Radio service також contains dormant runtime modes, transport candidates, conditional build paths, prototype compatibility behavior, test-only configuration і fallback branches.

Unsupported combinations affect tests, review, diagnostics, service tools, release packaging і security review. Future transport variation plausible, але no current product owns dormant implementations.

### Decision

Define single supported runtime mode для current product. Remove unsupported runtime modes from shipped builds. Delete configuration exposing unsupported behavior. Remove dormant implementations і old prototype fallback. Reduce CI and release packaging to supported combinations plus focused seam tests.

Preserve one narrow product-owned transport seam із product meanings: send accepted, response received, late response, retry allowed, radio unavailable, unsupported transport, permanent failure. Assign owner і review trigger. Document compatibility obligations. Use Decision Journal for smaller retained options.

### Consequences

Supported behavior becomes clearer. State space і test combinations shrink. Review, diagnosis, service tools, diagnostics, Boolean Explosion і unsupported behavior reduce. Product keeps future change seam without shipping every imagined transport.

Migration work remains. Tests і tools using prototype behavior must change. Evidence retained. Removed path may need rebuilding, якщо future product makes it real. Retained seam requires discipline.

### Alternatives Considered

Keep all modes until future product appears. Maximum apparent flexibility, але ongoing cost.

Test every combination. Expands cost замість deciding supported combinations.

Hide unsupported options in documentation while retaining behavior. Keeps runtime і diagnostic ambiguity.

Replace runtime options with compile-time flags. Helps only if unsupported combinations removed from CI, packaging, tools і support.

Remove all abstraction and call hardware APIs directly. Це discards justified seam.

Duplicate subsystem per product. Це creates parallel behavior before variation exists.

Build broader plug-in framework. Це formalizes speculative surface.

Postpone cleanup. Це leaves next defect to rediscover same unowned options.

## Коментар редактора

Chapter 11 focuses on option surface. Він не переказує state authority, API promises, dependency selection або time. Він робить вужче твердження: unused flexibility is maintenance cost, якщо evidence, ownership і review triggers не виправдовують цю плату.

PEAK concepts цього chapter: Unused Flexibility Is Waste (`LAW-006`), Boolean Explosion (`SMELL-003`), Platform Leakage (`SMELL-005`), Temporary Solution (`ANTIPATTERN-006`), Change Radius (`VOCAB-001` and `METRIC-001`), Discoverability (`METRIC-003`), ADR (`ARTIFACT-001`) і Decision Journal (`ARTIFACT-003`).
