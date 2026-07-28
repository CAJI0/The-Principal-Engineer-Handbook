# Кожна залежність — це рішення

## Вступна цитата

> Dependency не стає безкоштовною лише тому, що перший call compiled.

## Історія

Radio decision виглядало практичним.

Product needed a new wireless module for next controller revision. Hardware choice was narrowing, pilot line date mattered, and team needed initialization, channel setup, packet handling, power-state transitions, retries, diagnostics, and enough compliance behavior without spending whole release writing radio stack.

Vendor provided software kit for radio. It supported hardware, had example initialization code, handled protocol details, moved packets on evaluation board, and included painful but useful errata: timing around wake, retry sequence after channel loss, and narrow compiler version range.

Using it was not foolish.

Building complete stack internally would delay release and move risk into area with less evidence. Selecting another part would reopen hardware work. Delaying product until every replacement risk was understood would protect architecture in theory while failing product in practice.

Firmware team made reasonable compromise: vendor kit behind thin wrapper. Product code called wrapper. Only radio driver directory included vendor headers. Short ADR said team would use kit for first release and preserve option to replace later. Review was brief because boundary looked obvious.

For first release, that was enough.

Then dependency spread.

Vendor kit expected radio work from one task context. Callbacks arrived from that context and carried buffers owned by kit until callback returned. Wrapper preserved that shape. Product code learned vendor buffer format. Supervisory task learned vendor errors. Logging copied vendor reason names. Manufacturing scripts waited for vendor ready event. Service tool displayed same error categories. Tests mocked wrapper but used vendor-style errors. Production fixture used vendor diagnostic sequence. Release engineering pinned compiler version.

No one decided "let vendor software kit define product." Product learned it anyway.

Next hardware revision exposed the real surface. New kit had similar functions, but callback context, buffer ownership, error model, tooling support, calibration readiness, compiler assumptions, tests, scripts, service messages, and field compatibility did not match old assumptions.

"It is behind the wrapper" was partly true. It hid headers and names. It did not isolate behavior.

Principal Engineer asked the team to draw the real dependency surface: task context, callback ordering, buffer ownership, error meanings, retry policy, power-state behavior, logging names, test harness assumptions, calibration sequence, service-tool messages, compiler support, release cadence, and field compatibility.

The diagram looked less like driver boundary and more like product decision.

Team changed work from "swap library" to "name and contain commitments." They kept vendor kit because it solved real risk. But product boundary changed. Integration layer now named product-owned outcomes: radio ready, send accepted, send completed, receive available, radio unavailable, safe to retry, unsupported, permanently failed. Vendor errors translated before leaving integration. Callback context normalized. Buffer ownership defined in product terms. Tests rewritten around product contract. Fixture waited for product-level calibration readiness. Service tooling displayed product meanings and kept vendor detail only as diagnostic context. Compiler and kit version became owned release assumption.

ADR was rewritten. It no longer said only "use vendor kit behind wrapper." It said which commitments team accepted, where dependency may appear, who owns updates, what evidence proves boundary, and what triggers replacement.

System did not become independent of vendor kit. It became honest about depending on it.

That honesty changed architecture more than wrapper had.

## Обговорення

A dependency is any external or internal thing whose behavior the system relies on and cannot freely change alone.

Це ширше за imported code: library, service, protocol, hardware part, file format, build image, compiler, release tool, production fixture, test harness, support procedure, internal platform. If system relies on it and cannot change it freely, decision carries architectural cost.

Every dependency commits system to behavior, failure modes, lifecycle constraints, ownership boundaries, and replacement cost.

This does not mean dependencies are bad. Radio kit reduced schedule risk and brought hardware knowledge. Many good decisions depend on other people's work. Law is not "avoid dependencies." Law is "know what you are accepting."

First mistake is treating dependency choice as implementation detail because first integration is local. Wrapper lived in one directory, but behavior moved through product: callback context, error meanings, logging language, compiler support, calibration events.

That is Silent Coupling (`SMELL-001`): hidden dependency affects behavior but is not explicit contract. Team thinks product depends on wrapper. In practice, it depends on vendor timing, error vocabulary, memory ownership, and lifecycle.

Dependency use and dependency spread are different.

Using dependency may be reasonable. Dependency spread happens when dependency concepts escape containment boundary: product errors become vendor errors, tests assert vendor callback order, manufacturing waits for vendor event, support docs use vendor names, release planning follows dependency support horizon without owner.

A wrapper can help. It is not proof.

Syntactic isolation hides names, headers, types, call shapes. Semantic isolation asks whether consumers depend on product-owned contract or underlying dependency behavior. If wrapper exposes vendor errors, callback context, memory rules, ordering, and categories, architecture remains dependent on vendor semantics.

Replacement cost includes more than swapping code: contract redesign, product migration, data migration, tests, fixture updates, operational retraining, support documentation, shipped-version compatibility, confidence rebuilding, release coordination, compiler updates, hardware qualification, customer migration risk.

"We can swap it later" deserves follow-up: what exactly would have to change if we did?

Direct dependencies are visible in imports, build files, service calls, protocol choices, hardware selections, interface definitions, process handoffs, and recorded decisions. Transitive dependencies arrive through other dependencies. Transitive does not mean another team owns consequence; it means commitment is one step farther from first choice.

Dependency direction preserves architectural control when product code depends on stable product contract, narrow integration layer depends on volatile vendor component, and product owns vocabulary, errors, states, and lifecycle. Bad direction lets volatile component define product.

Failure behavior is imported too: unavailable states, latency, errors safe to retry, permanent failures, resources exhausted, version skew, support horizon, hardware degradation, service changes, tool support end.

Lifecycle is part of dependency. Selection, adoption, integration, update, support, deprecation, replacement, and removal need owners when dependency is material. Removal means consumers no longer depend on behavior, tests no longer encode it, tools no longer assume it, manufacturing no longer waits for it, support no longer explains it.

Not every dependency needs same process. Small isolated utility with obvious behavior and cheap replacement needs little ceremony. Material dependencies need decision record, containment, and discoverable owner.

Discoverability (`METRIC-003`) matters because dependency decisions age quietly. ADR (`ARTIFACT-001`) is a good home for material dependency decision: why chosen, alternatives, imported behavior, update owner, limitations, replacement trigger.

Practical standard: deliberate dependencies whose commitments are understood and proportionate to their value.

## Інженерний принцип

Name the commitment before accepting the dependency. If it can shape behavior, failure, lifecycle, or replacement cost, record the decision and contain the spread.

Review questions:

1. What problem does dependency solve?
2. What kind: code, service, protocol, hardware, tool, process, or platform?
3. Who consumes it directly?
4. Who consumes it transitively?
5. Which behavior are we importing?
6. Which failures enter our system?
7. Which vocabulary, errors, timing, ownership, or lifecycle assumptions might leak?
8. Which boundary keeps product semantics under product control?
9. Who owns versions, updates, support, and deprecation?
10. What would replacement actually require?
11. What evidence shows replacement is plausible?
12. What event would trigger update, replacement, or removal?

Point is not a form. Point is to prevent local convenience from becoming architecture unnoticed.

## Архітектурна вправа

### Простежте реальну вартість однієї залежності

Оберіть real dependency: library, service, hardware part, protocol, build tool, test fixture, file format, release process, or internal platform.

1. What is dependency?
2. What category is it?
3. What problem does it solve?
4. Which components consume it directly?
5. Which components, tests, tools, fixtures, or procedures consume it transitively?
6. What behavior does it import?
7. What failures does it import?
8. What runtime assumptions does it bring?
9. What build, release, or support assumptions does it bring?
10. Which vocabulary or error meanings leak into product?
11. Which data, protocol, storage, or manufacturing behavior depends on it?
12. Who owns updates?
13. Who owns compatibility with existing releases?
14. What support horizon matters?
15. What evidence shows dependency is contained?
16. What would replacement require beyond code?
17. What would replacement cost in tests, tooling, operations, support, and confidence?
18. What condition would trigger update, replacement, or removal?
19. Where is decision recorded?

End with:

What part of the system currently depends on this dependency's behavior while believing it depends only on your boundary?

## Нотатник Principal Engineer

- A dependency is a decision about future change.
- A wrapper helps only when callers depend on wrapper's contract.
- Replacement cost is real when someone can describe path out.

## ADR

### Chapter ADR: Adopt the Vendor Radio Software Kit Behind a Bounded Integration Layer

### Context

Product needs radio support for selected hardware in next controller revision. Vendor radio software kit provides working initialization, protocol handling, diagnostics, and hardware-specific guidance that reduce delivery and integration risk for first release.

Kit imports commitments: callback model, memory ownership, error meanings, retry behavior, compiler support, release cadence, and diagnostic assumptions can spread into product code, tests, manufacturing, service tools, and support procedures if boundary is too thin.

### Decision

Adopt vendor radio software kit, but constrain direct use to one bounded radio integration layer.

Define product-owned radio contract for readiness, send acceptance, send completion, receive behavior, unavailable states, failures safe to retry, unsupported states, and permanent failures. Normalize vendor errors into product meanings before leaving integration layer. Normalize callback context and buffer ownership into product terms. Prohibit new direct vendor kit use outside integration boundary.

Add contract tests around product-owned behavior and integration tests around actual kit. Keep manufacturing, service tooling, logging, and support procedures aligned to product meanings. Record supported kit versions, compiler assumptions, update ownership, support horizon, and exit triggers.

### Consequences

Product can use vendor kit without letting vendor semantics become product model by accident. Delivery risk reduced. Replacement thinking more realistic. Tests check product contract first and vendor integration second. Upgrade decisions have owners.

Work remains: integration layer maintenance, careful translation of errors/lifecycle, contract and integration tests, and unavoidable deep hardware behavior.

### Alternatives Considered

Build complete radio stack internally. More control, delayed release.

Use vendor kit directly throughout product. Fastest at first, but vendor vocabulary and lifecycle define product behavior.

Delay product until all replacement risks solved. Protects optionality in theory while ignoring current product commitment.

Select another radio vendor. Reopens hardware and qualification and introduces another dependency decision.

Create fully generic radio abstraction. Likely unused flexibility before real variation known.

Avoid integration until every exit path cheap. Makes replacement easy only by not shipping product.

## Коментар редактора

Chapter 9 widens the boundary from Chapters 7 and 8. Dependency decisions are easy to misclassify as implementation choices; cost can appear in failure behavior, release cadence, tests, manufacturing, service, support, hardware qualification, and replacement planning.

The PEAK concepts carrying this chapter are Every Dependency Is a Decision (`LAW-007`), Silent Coupling (`SMELL-001`), Change Radius (`VOCAB-001`), ADR (`ARTIFACT-001`), and Discoverability (`METRIC-003`). They are enough. Chapter 10 will take one imported commitment, time, and give it its own law.
