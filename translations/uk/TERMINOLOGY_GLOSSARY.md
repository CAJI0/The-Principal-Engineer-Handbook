# Ukrainian Terminology Glossary

| English term | Ukrainian rendering | Rule / context | Notes |
| --- | --- | --- | --- |
| Principal Engineer | Principal Engineer | Usually keep in English. | Do not translate as «головний інженер». |
| ownership | володіння відповідальністю; відповідальність за контур; власник | Translate by context. | Avoid literal «власність» for engineering responsibility. |
| evidence | докази; інженерні докази | Use for proof, validation, and decision support. | Use «свідчення» only for signals or observations. |
| judgment | інженерне судження | Use for professional technical judgment. | Avoid reducing it to opinion. |
| constraints | обмеження | Use for time, budget, system, product, and organizational constraints. | Keep concrete. |
| trade-off | trade-off; компроміс | Prefer `trade-off` when the engineering nuance matters. | Use «компроміс» only when it does not flatten the meaning. |
| accountability | підзвітність; відповідальність за результат | Use when someone is answerable for an outcome. | Distinguish from task ownership. |
| responsibility | відповідальність | General responsibility for work, behavior, or scope. | May combine with «за контур». |
| boundary | межа; архітектурна межа | Use for architecture, ownership, and system boundaries. | Preserve canonical meaning. |
| interface | інтерфейс | Use for software, API, module, and team interfaces. | Do not over-translate. |
| state | стан | Use for system, component, and product state. | Preserve technical meaning. |
| risk | ризик | Use directly. | Keep risk statements concrete. |
| assumption | припущення | Use for explicit assumptions in decisions and reviews. | Prefer documenting over hiding. |
| confidence | впевненість | Use for confidence level in evidence-backed decisions. | Avoid implying certainty. |
| decision record | запис рішення | Use for a record of a decision. | For ADR, preserve `ADR`. |
| ADR | ADR | Keep acronym in English. | Can explain as «запис архітектурного рішення» on first mention. |
| RFC | RFC | Keep acronym in English. | Can explain as «запит на обговорення» if needed. |
| Decision Journal | Decision Journal | Usually keep artifact name in English. | Optionally explain as «журнал рішень». |
| Architecture Ledger | Architecture Ledger | Usually keep artifact name in English. | Optionally explain as «архітектурний реєстр». |
| Architecture Review | Architecture Review | Usually keep artifact name in English. | Optionally explain as «архітектурний перегляд». |
| Architecture Health Review | Architecture Health Review | Usually keep artifact name in English. | Optionally explain as «перегляд архітектурного здоровʼя». |
| Change Radius | радіус зміни | Preserve `Change Radius` on first mention. | Use consistently after first mention. |
| Bus Factor | Bus Factor | Keep in English. | Optionally explain as «ризик концентрації знань». |
| Discoverability | discoverability; виявлюваність | Prefer English if used as a metric name. | Use Ukrainian explanation in prose. |
| API Stability | API Stability | Preserve as metric or concept name. | Explain as «стабільність API» when needed. |
| Architecture Health | Architecture Health | Preserve as concept or metric name. | Explain as «архітектурне здоровʼя» when needed. |
| Silent Coupling | мовчазна звʼязаність | Preserve English on first mention if used as a smell name. | Avoid «тиха» unless context requires it. |
| Utility Gravity | гравітація utility-коду | Chosen rendering for consistency. | Avoid alternating with «утилітний код» unless review approves. |
| Boolean Explosion | вибух булевих прапорців | Chosen rendering for consistency. | Preserve English on first mention if used as a smell name. |
| Deletion Day | День видалення | Use for the ritual or practice name. | Capitalize when used as the canonical name. |
| Temporary Solution | тимчасове рішення | Use for the smell or pattern. | Preserve English on first mention if it is a canonical label. |
| Hero Engineer | Hero Engineer | Usually keep in English. | Explain as a risky role pattern, not praise. |
| Failure Story | Failure Story | Usually keep in English. | Explain as «історія відмови» when needed. |

| Architecture Playbook | Архітектурний playbook | Preserve `playbook` as the recognizable practice term. | Introduced in Phase 3. |
| Review habit | звичка перегляду | Use for repeated practice questions after an engineering principle. | Avoid leaving the phrase as standalone English outside canonical labels. |
| hardening point | точка затвердіння | Use for the moment after which a decision becomes expensive to change. | Introduced in Phase 3 review practice. |
| allowed movement | дозволений рух | Use in Architecture Freeze context. | Means changes permitted inside a frozen decision. |
| exception path | шлях винятку | Use in Architecture Freeze context. | Means the controlled path for changing or revalidating a frozen decision. |
| contract | контракт | Use for behavioral/API/architecture promises. | Keep `API` and canonical artifact names in English. |
| owner | власник | Use for a responsible authority in architecture decisions. | Prefer contextual responsibility language where Ukrainian flow requires it. |
| firmware | firmware | Preserve in English. | Common embedded term; translate surrounding prose. |
| gateway | gateway | Preserve in English. | Common product/integration term in Part III examples. |
| service tool | service tool | Preserve in English. | Common field/support tooling term in Part III examples. |
| runtime | runtime | Preserve in English when used technically. | Translate surrounding prose. |

When a term is ambiguous, record the ambiguity in the phase notes instead of forcing a poor translation.
