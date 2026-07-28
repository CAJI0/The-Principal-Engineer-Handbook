# Залишати системи кращими, ніж ви їх знайшли

## Opening Quote

> Зміна не завершена, доки наступна зміна не бачить, що успадкувала.

## Story

New board revision виглядала modest on schedule.

Industrial controller already existed and shipped into factories, test stands, and service cabinets for years. Next production run needed board revision because one external power-monitor peripheral was no longer available. Replacement seemed close: same role, same bus, same startup sequence place, same responsibility for saying whether board healthy enough to continue.

It was not same part.

Replacement needed longer startup window before status reliable. It interpreted one status bit differently after reset. It reported one class of power failure through latched register instead of live pin. Its reset behavior cleared information old monitor kept. It exposed diagnostic capability old part never had: distinguishing slow rail from monitor-not-ready.

Product promise did not change. Controller still had to boot, reject unsafe power conditions, provide useful diagnostics, and keep manufacturing test flow boring. Date mattered. Board revision tied to production slot. Firmware work had to be real, bounded, and reviewable.

Support code had no clean place to absorb difference.

Years earlier startup code had grown shared board-support module. First it identified board revision and ran checks. Then it interpreted external power monitor. Then retry timing for cold chamber. Then fallback behavior for prototype board. Then diagnostic text, configuration flags, and monitor-selection option for possible second supplier never used by released product.

Module became convenient place for anything near boot. Board checks, peripheral-specific status, product startup policy, retry timing, diagnostics, configuration switches, and prototype detail lived together.

History understandable. Each addition solved real problem. Fallback helped hardware team. Retry timing avoided false failures. Selection option gave purchasing possible path. Diagnostic text helped manufacturing. None arrived with sign «future architecture problem». They arrived as helpful work.

Structural cost accumulates this way: sequence of locally reasonable choices without later moment asking which choices still carry their weight.

This was Utility Gravity (`SMELL-002`): shared module useful, reachable, already in startup path, so each addition cheaper than better boundary. Also Platform Leakage (`SMELL-005`): power-monitor details leaked into product startup decisions and diagnostics.

Fastest patch obvious: add condition for new board revision, wait longer, interpret latched bit, add diagnostic string, extend option, keep old fallback, add test. It would probably pass review. Small, one module, clear product reason.

It also made next board revision more expensive.

Reviewer would need board identity, monitor timing, reset semantics, product startup policy, fallback behavior, diagnostic wording. Test owner would need decide whether prototype fallback affects production board. Next engineer would learn which options real and which historical. Future monitor change would add another branch.

Firmware lead saw risk and opposite failure: «We cannot turn a part swap into a platform rewrite.» She was right. Broad startup redesign would displace product outcome. Team had evidence for one weak boundary, not rewrite whole boot path.

Principal Engineer framed differently:

«The board revision still ships. The question is whether this change also gives us enough evidence to remove one piece of structural cost.»

They split decision:

First, product-level boot orchestration stayed product-level. Startup path still decided whether controller could continue and reported product-level initialization failure. That was not monitor driver's job.

Second, monitor-specific timing and status interpretation moved behind owned platform boundary. Each supported board selected one monitor implementation. Startup asked for power-health result. It did not know whether status bit live, latched, delayed, or cleared by reset.

Third, obsolete flexibility challenged with evidence. Support policy, service records, and manufacturing records showed prototype boards with fallback outside supported scope. Release configuration showed no shipped product selected unused monitor option at runtime. Test evidence covered supported startup paths. Team removed prototype fallback and narrowed unused option.

That mattered because Unused Flexibility Is Waste (`LAW-006`). Fallback and option looked generous, but made every new monitor change harder to reason about and increased Change Radius (`VOCAB-001`) without real product capability.

Team did not clean up everything. They did not rename whole startup module, redesign diagnostics, or fix separate initialization issue. Those items went to backlog only with owner and reason. Board revision was not license to tidy every nearby corner.

They added two diagnostics: selected monitor implementation, and product-level reason startup rejected power health. Reason was stable category manufacturing and support tools could use: monitor not ready, power status invalid, reset-related power fault, unsupported board configuration.

Tests followed boundary. Monitor implementation tests covered part-specific timing, reset behavior, status translation. Product startup tests covered controller behavior with power-health result. Manufacturing tests checked diagnostic category and selected implementation, not private register semantics.

They wrote Decision Journal (`ARTIFACT-003`) entry recording boundary: product startup owns orchestration and product failure categories; monitor implementations own timing, status interpretation, reset-specific behavior. It recorded evidence for removing fallback and narrowing option, out-of-scope work, and reopen signals: second active monitor supplier, new board family, or diagnostic requirement not expressible through current categories.

Change still shipped board revision. Controller shipped with new monitor support. Boot path not perfect. Shared module still had scars. But next necessary monitor change would not rediscover reset timing, status semantics, obsolete fallback, and diagnostic wording in same review.

System was better in a specific way: one product change reduced cost of next related change without pretending to solve every nearby problem.

## Discussion

Locally correct change can still raise future cost.

Patch can be small, tested, and justified while making system harder to change. Fast board-revision patch would work, but add another responsibility to overloaded place.

Architecture Health (`VOCAB-007`) is system ability to absorb necessary change without disproportionate cost. Chapter 1 introduced architecture as future cost of decisions. Chapter 6 turns that into daily question: when change exposes or creates structural cost, what is smallest justified improvement that reduces cost without displacing product outcome?

Stewardship is not cleanup.

Cleanup begins with discomfort of messy code. Stewardship begins with obligation of real change. Board revision created product obligation and evidence that existing boundary weak: monitor-specific knowledge leaked into product startup, obsolete flexibility affected review, shared utility became default home for unrelated concerns.

These facts made bounded improvement legitimate. They did not justify general rewrite.

Useful distinction is causal. Debt connected to change when task creates, worsens, or crosses weakness; provides evidence to remove/narrow old assumption; or next likely change would rediscover same surface. Debt is not connected merely because it is nearby, annoying, old, or aesthetically unpleasant.

This protects trust. Product partners can accept bounded stewardship when connection visible. They become rightly skeptical when «while we are here» expands into private engineering agenda.

Change Radius (`VOCAB-001`) becomes practical. Metric (`METRIC-001`) is not just file count. It is visible area of behavior, ownership, review, and test that must move for safe change. One more conditional looked small but expanded review radius. Bounded correction touched structure but reduced radius for next related monitor change.

Discoverability (`METRIC-003`) matters. Decision living only in memory is private context. Team improved discoverability by making selected monitor visible, reporting product-level failure categories, and recording boundary and reconsideration triggers in Decision Journal.

Three tempting responses:

First, narrow conditional. Preserves schedule and current diff. But Simplicity Is a Feature (`LAW-004`) can be misread as «touch as little as possible». Simplicity reduces necessary mental burden; small diff that hides more private rules is not necessarily simple.

Second, broad rewrite. Attractive because startup area accumulated compromises, but evidence did not support full redesign. It would increase schedule risk and blur review.

Third, bounded correction. Keeps board revision as center. Localizes monitor variation behind owned boundary. Removes Temporary Solution (`ANTIPATTERN-006`) after evidence. Narrows unused flexibility because Unused Flexibility Is Waste (`LAW-006`). Adds diagnostics that explain current product behavior.

Bounded correction not always available. Release risk may be too high, evidence too weak, area owned by another team, incident may require restore service and record debt. Principal Engineer can still leave system better by naming cost, preserving evidence, and creating path for later owner.

When not to refactor is part of judgment. Do not refactor because style irritates you, file is open, social cover exists, improvement cannot be reviewed as part of product change, boundary less clear after change, or you cannot say what future cost reduced.

Stop condition should be explicit: stop when product commitment met, structural cost exposed by change reduced, behavior and boundary reviewable/testable, decision or limitation discoverable, and further cleanup not causally tied to task.

Better does not mean certified complete. Improvement was reviewable and attributable. Before change, monitor timing, status interpretation, fallback behavior, and product startup policy tangled. After change, monitor variation had owner, obsolete fallback removed with evidence, unused selection narrowed, and startup exposed stable diagnostic reasons.

Attributable matters. Reviewer should tell which diff part delivers product outcome and which reduces exposed structural cost.

Leave next necessary change cheaper, safer, or easier to understand. That practical test is modest enough for real delivery and strong enough to resist moving cost into future.

That is enough.

Part I has been about mindset of principal engineering: decisions as future cost, constraints explicit, better questions, ownership beyond code, judgment tied to evidence. This chapter closes arc with stewardship. Principal Engineer does not merely complete todayʼs change or chase ideal system. Work is to make current outcome real while leaving next necessary change cheaper, safer, or easier to understand.

## Engineering Principle

When a change exposes or creates structural cost, include the smallest justified improvement that reduces that cost without displacing product outcome.

This principle depends on Simplicity Is a Feature (`LAW-004`) and Unused Flexibility Is Waste (`LAW-006`). Simplicity does not preserve smallest diff at any cost; it reduces burden of understanding and changing system. Unused flexibility imposes review, test, and diagnostic cost without evidence.

Practical move: disciplined stewardship. Use current change as evidence. Improve only boundary or behavior the change crosses. Remove/narrow obsolete flexibility only with enough evidence. Record decision so next engineer can find it. Then stop.

## Architecture Exercise

### Define a Bounded Stewardship Action

Choose a change you are making or recently reviewed.

1. What product outcome must this change deliver?
2. What part of system resists the change?
3. What structural cost does the change expose or create?
4. What evidence shows cost is real rather than preference?
5. What is smallest improvement that directly reduces cost?
6. How should it affect boundary clarity, Change Radius, Discoverability, ownership, or failure visibility?
7. What debt remains deliberately out of scope?
8. What existing behavior must not change?
9. What validation is needed for product outcome?
10. What validation is needed for stewardship action?
11. Where will decision, limitation, or review trigger be discoverable?
12. What is stop condition?

> What is the smallest improvement you can include now that leaves the next
> necessary change cheaper without turning this task into a rewrite?

## Principal's Notebook

- Leave a cheaper path for the next related change.
- Improve the boundary the change actually crosses.
- Stop when the product outcome and the bounded stewardship outcome are both met.

## ADR

### Chapter ADR: Localize Power-Monitor Variation While Delivering the New Board Revision

### Context

New industrial controller board revision replaces external power-monitor peripheral. Replacement changes startup timing, status interpretation, reset behavior, error reporting, and one diagnostic capability. Existing shared startup-support module mixes product boot orchestration, board checks, monitor-specific interpretation, retry timing, fallback behavior, diagnostic text, and unused configuration flexibility.

### Decision

Keep product-level boot orchestration in startup path, but localize monitor-specific timing, status interpretation, and reset behavior behind owned platform boundary. Select one supported monitor implementation per board configuration. Remove obsolete prototype fallback and narrow unused monitor-selection option using product support, service, manufacturing, release, configuration, and test evidence. Add minimal diagnostics for selected monitor implementation and product-level power-health failure reason. Record boundary, evidence, out-of-scope work, and reconsideration triggers in Decision Journal.

### Consequences

Board revision can ship without platform rewrite. Next related monitor change has smaller review/test surface because monitor variation no longer leaks through product startup policy. Obsolete fallback and unused flexibility no longer impose review cost. Startup path still not fully redesigned; unrelated initialization debt remains out of scope.

### Alternatives Considered

Add another conditional to shared startup-support module. Fast, but increases Change Radius and preserves private knowledge.

Rewrite startup path broadly. Addresses more debt, but current board revision lacks evidence and schedule room.

Introduce generic plug-in framework for future monitors. Turns bounded variation into speculative architecture before evidence.

Deliver only feature and defer every structural correction. Protects narrow schedule story but preserves same leakage and unsupported option.

Keep obsolete fallback and unused option. Avoids removal risk, but evidence shows they no longer support current product or service scope.

## Editor's Commentary

Chapter 6 follows Chapter 5 by turning evidence-based judgment into bounded stewardship. Chapter 5 asks how much confidence claim deserves; this chapter asks what current evidence justifies changing in system itself.

It operationalizes Chapter 1ʼs idea that architecture is future cost of decisions. It does not repeat Chapter 2ʼs constraint framing, Chapter 3ʼs question discipline, Chapter 4ʼs ownership model, or Chapter 5ʼs evidence ladder. It shows how those habits combine when real product change exposes structural cost.

This closes Part I because principal-engineer mindset is complete enough to move from posture to laws. Part II can name forces that make systems easier or harder to change without introducing new PEAK concept here.

Concepts carrying this chapter are Architecture Health, Change Radius, Discoverability, Utility Gravity, Platform Leakage, Temporary Solution, Decision Journal, Simplicity Is a Feature, and Unused Flexibility Is Waste.
