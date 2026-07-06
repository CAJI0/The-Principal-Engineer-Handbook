# Leaving Systems Better Than You Found Them

## Opening Quote

> A change is not finished until the next change can see what it inherited.

## Story

The new board revision looked modest on the schedule.

The industrial controller already existed. It had shipped into factories, test
stands, and service cabinets for years. The next production run needed a board
revision because one external power-monitor peripheral was no longer available
on the purchasing timeline. The replacement part was close enough to feel
ordinary: same general role, same bus, same place in the startup sequence, same
responsibility for saying whether the board was healthy enough to continue.

It was not the same part.

The replacement needed a longer startup window before its status was reliable.
It interpreted one status bit differently after reset. It reported one class of
power failure through a latched register instead of a live pin. Its reset
behavior cleared information the old monitor had kept. It also exposed one
diagnostic capability the old part never had: it could distinguish between a
slow rail and a monitor-not-ready condition.

None of those differences changed the product promise. The controller still had
to boot, reject unsafe power conditions, provide useful diagnostics, and keep the
manufacturing test flow boring. The date mattered. The board revision was tied
to a production slot. The firmware work had to be real, bounded, and reviewable.

The support code, however, did not have a clean place to absorb the difference.

Years earlier, the startup code had grown a shared board-support module. At
first it identified the board revision and ran a few checks before the
application initialized. Then it learned how to interpret the external power
monitor. Then it gained retry timing because one early batch came up slowly in a
cold chamber. Then it gained fallback behavior for a prototype board that could
not reliably see the monitor during early hardware work. Then it gained
diagnostic text, configuration flags, and a monitor-selection option that had
been added for a possible second supplier but never used by a released product.

The module had become a convenient place for anything that happened near boot.
Board checks lived beside peripheral-specific status interpretation. Product
startup policy lived beside retry timing for a particular monitor. Diagnostic
strings lived beside configuration switches. A private detail from a prototype
had survived long after the prototype stopped mattering.

The history was understandable. Each addition had solved a real problem at the
time. The first fallback helped the hardware team get through early board
testing. The retry timing avoided false failures in a cold chamber. The
monitor-selection option gave purchasing a possible path if the second supplier
became real. The diagnostic text helped manufacturing separate a power problem
from an application crash. None of those changes had arrived wearing a sign that
said "future architecture problem." They had arrived as helpful work.

That is how structural cost usually accumulates. It does not require neglect or
carelessness. It only requires a sequence of locally reasonable choices without
a later moment where the team asks which choices are still carrying their own
weight.

This was Utility Gravity (`SMELL-002`) in a familiar form. The shared module was
useful, reachable, and already included in the right startup path, so each small
addition had felt cheaper than creating a better boundary. It was also showing
Platform Leakage (`SMELL-005`): details that belonged to a power-monitor
implementation had leaked into product-level startup decisions and diagnostics.

The fastest patch was obvious. Add a condition for the new board revision. If
the new monitor was present, wait longer before the first read. Interpret the
latched status bit differently. Add one more diagnostic string. Extend the
monitor-selection option. Keep the old prototype fallback. Add a test case for
the new board.

That patch would probably pass review. It was small. It touched one module. It
had a clear product reason. No one had to pretend it was reckless.

It also made the next board revision more expensive.

The reviewer would have to understand board identity, monitor timing, reset
semantics, product startup policy, fallback behavior, and diagnostic wording in
one place. The test owner would have to decide whether an old prototype fallback
could affect a new production board. The next engineer would have to learn which
configuration options were real and which were historical. A future monitor
change would rediscover the same surface and add another branch to the same
shared module.

Even the release note would become less clear. Was the change a board-revision
update, a startup timing change, a diagnostic change, or a configuration
behavior change? The answer would be "all of them, but only for one board, and
only through a path that also knows about old boards." That kind of answer makes
review slow because it forces people to reconstruct intent from placement.

The firmware lead saw the risk but was wary of the opposite failure.

"We cannot turn a part swap into a platform rewrite," she said.

She was right. A broad startup redesign would have displaced the product
outcome. The team did not have evidence for rewriting the whole boot path. They
had evidence that one boundary was carrying too many kinds of knowledge.

The principal engineer framed the work differently.

"The board revision still ships," he said. "The question is whether this change
also gives us enough evidence to remove one piece of structural cost."

They split the decision into three parts.

First, product-level boot orchestration stayed product-level. The startup path
would still decide whether the controller could continue. It would still report
a product-level initialization failure when power health was not acceptable.
That was not the monitor driver's job.

Second, monitor-specific timing and status interpretation moved behind an owned
platform boundary. Each supported board selected one monitor implementation.
The startup path asked for a power-health result. It did not know whether a
particular status bit was live, latched, delayed, or cleared by reset. It did not
know which retry window belonged to which monitor.

Third, the obsolete flexibility was challenged with evidence. Manufacturing
records showed that the prototype boards using the fallback were no longer in
supported service. Release configuration showed that no shipped product selected
the unused monitor-selection option at runtime. Test coverage showed that the
fallback path had no current product owner. The team removed the prototype
fallback and narrowed the unused option to the supported board configurations.

That last part mattered because Unused Flexibility Is Waste (`LAW-006`). The
fallback and selection option looked generous, but in practice they made every
new monitor change harder to reason about. They increased Change Radius
(`VOCAB-001`) without buying an actual product capability.

The team did not clean up everything. They did not rename the entire startup
module. They did not redesign diagnostics across the product. They did not fix a
separate initialization ordering issue that everyone disliked but this change
did not touch. Those items went into the backlog only if they had an owner and a
reason. The board revision was not a license to tidy every nearby corner.

They added two diagnostics because the new boundary made them cheap and useful:
which monitor implementation had been selected for the board, and the
product-level reason startup had rejected power health. The reason was not a raw
register dump. It was a stable category the manufacturing and support tools
could use: monitor not ready, power status invalid, reset-related power fault,
or unsupported board configuration.

The tests followed the same boundary. Monitor implementation tests covered
part-specific timing, reset behavior, and status translation. Product startup
tests covered what the controller did with a power-health result. Manufacturing
tests checked the diagnostic category and the selected implementation, not the
private register semantics of the part. The split did not create a grand new
testing strategy. It made the current behavior easier to review in the shape it
would be changed next time.

They also wrote a short Decision Journal (`ARTIFACT-003`) entry. It recorded the
boundary: product startup owns orchestration and product failure categories;
monitor implementations own timing, status interpretation, and reset-specific
behavior. It recorded the evidence used to remove the prototype fallback and
narrow the unused option. It recorded what stayed out of scope and what signal
would justify reopening the decision: a second active monitor supplier, a new
board family with different power-health semantics, or a diagnostic requirement
that could not be expressed through the current categories.

The change was still a board-revision change. The production date was still the
forcing function. The controller shipped with the new monitor support. The boot
path was not perfect, and the shared module still had some old scars. But the
next necessary monitor change would not have to rediscover reset timing, status
semantics, obsolete fallback behavior, and diagnostic wording in the same
review.

The system was better in a specific way: one product change had reduced the cost
of the next related change without pretending to solve every nearby problem.

## Discussion

A locally correct change can still raise future cost.

That is one of the uncomfortable truths of senior engineering. A patch can be
small, well tested, and justified by the current request while also making the
system harder to change. The fast board-revision patch would have worked because
it matched the immediate symptom: a new monitor needed different timing and
status handling. Its weakness was not that it was careless. Its weakness was
that it added another responsibility to a place already carrying board identity,
startup policy, monitor interpretation, diagnostics, fallback behavior, and
configuration history.

Architecture Health (`VOCAB-007`) is the system's ability to absorb necessary
change without disproportionate cost. Chapter 1 introduced architecture as the
future cost of decisions. Chapter 6 turns that idea into a daily question: when
a change exposes or creates structural cost, what is the smallest justified
improvement that reduces that cost without displacing the product outcome?

Stewardship is not cleanup.

Cleanup begins with the discomfort of messy code. Stewardship begins with the
obligation of a real change. The board revision created a product obligation:
support the new monitor and preserve safe startup behavior. It also supplied
evidence that the existing boundary was weak. Monitor-specific knowledge had
leaked into product startup. Obsolete flexibility still affected review. A
shared utility had become the default home for unrelated concerns.

Those facts made a bounded improvement legitimate. They did not justify a
general rewrite.

The useful distinction is causal. Debt is connected to the change when the task
creates, worsens, or crosses the weakness; when the task provides evidence to
remove or narrow an old assumption; or when the next likely change would
rediscover the same surface. Debt is not connected merely because it is nearby,
annoying, old, or aesthetically unpleasant.

That distinction also protects trust. Product partners can accept a bounded
stewardship action when they can see why it belongs to the change. They become
rightly skeptical when "while we are here" expands into a private engineering
agenda. Principal engineers earn room for improvement by making the connection
visible: this structural weakness is on the path of the requested change, this
evidence comes from the requested change, and this smaller boundary reduces the
next related cost.

This is where Change Radius (`VOCAB-001`) becomes practical. The Change Radius
metric (`METRIC-001`) is not just a count of files touched. It is the visible
area of behavior, ownership, review, and test that must move for a change to be
safe. Adding one more conditional to the shared startup module looked small as a
diff, but it expanded the review radius. The reviewer needed to understand more
board-specific history and more monitor-specific semantics to judge a product
startup decision. The bounded correction touched a bit more structure, but it
reduced the radius for the next related monitor change.

Discoverability (`METRIC-003`) matters for the same reason. A decision that only
lives in the memory of the people present is not architecture; it is private
context. The team improved discoverability by making the selected monitor
implementation visible, by reporting product-level failure categories instead of
raw part details, and by recording the boundary and reconsideration triggers in a
Decision Journal (`ARTIFACT-003`). The next engineer should not have to infer
the boundary from a chain of conditionals.

The three tempting responses were all understandable.

The first was the narrow conditional. It preserved schedule and minimized the
current diff. It was attractive because Simplicity Is a Feature (`LAW-004`) can
be misread as "touch as little as possible." But simplicity is about reducing
the system's necessary mental burden, not hiding more meaning inside an already
overloaded place. A small diff that increases the number of private rules in one
module is not necessarily simple.

The second was the broad rewrite. It was attractive because the startup area had
accumulated years of compromises. But the current evidence did not support a
full redesign. Rewriting the startup path would have increased schedule risk,
blurred the review, and made the board revision compete with a platform project.
That would have failed the product obligation.

The third was the bounded correction. It kept the board revision as the work's
center. It localized monitor-specific timing and interpretation behind an owned
boundary. It removed a Temporary Solution (`ANTIPATTERN-006`) only after the
team had evidence that the prototype fallback no longer served a supported
product. It narrowed unused flexibility because Unused Flexibility Is Waste
(`LAW-006`). It added diagnostics that explained the current product behavior
instead of expanding the scope into a general diagnostics redesign.

The bounded correction is not always available. Sometimes the release risk is
too high. Sometimes the evidence is too weak. Sometimes the area is already
owned by another team and the correct action is to make the cost visible, not
quietly change the boundary. Sometimes the current task is a production incident
where the only responsible move is to restore service and record the debt with a
specific owner. Sometimes a structural improvement would require test coverage
the team does not yet have.

In those cases, doing less can be the more responsible choice. A principal
engineer can still leave the system better by naming the cost, preserving the
evidence, and creating a path for a later owner. The improvement may be a
diagnostic, a Decision Journal entry, a removed false option, or a test that
captures the boundary. It does not have to be a redesign to matter.

When not to refactor is part of the judgment.

Do not refactor because you are irritated by style. Do not refactor because the
file was open. Do not refactor because the change gives you social cover to fix
everything nearby. Do not refactor when the improvement cannot be reviewed as
part of the product change. Do not refactor when the behavior boundary will be
less clear after the change than before it. Do not refactor when you cannot say
what future cost is being reduced.

The stop condition should be explicit.

Stop when the product commitment is met, the structural cost exposed by the
change has been reduced, the behavior and boundary are reviewable and testable,
the decision or limitation is discoverable, and further cleanup is not causally
tied to the task. That stop condition protects both sides of the work. It
prevents the "just one more cleanup" drift that threatens delivery. It also
prevents the "just one more conditional" drift that quietly lowers Architecture
Health (`VOCAB-007`).

Better does not mean scored, certified, or declared complete. The team did not
need a new rating system to prove the module was improved. The improvement was
reviewable and attributable. Before the change, monitor timing, status
interpretation, fallback behavior, and product startup policy were tangled in a
shared module. After the change, monitor-specific variation had an owner,
obsolete fallback behavior had been removed with evidence, unused selection had
been narrowed, and the product startup path exposed stable diagnostic reasons.

Attributable matters. If a reviewer cannot tell which part of the diff delivers
the product outcome and which part reduces the exposed structural cost, the work
is too muddy. In the board-revision change, the product outcome was the new
monitor support. The stewardship outcome was the localized variation, removed
fallback, narrowed option, and discoverable boundary. Those outcomes were close
enough to belong together and distinct enough to review separately.

Leave the next necessary change cheaper, safer, or easier to understand. That is
the practical test. It is modest enough to fit inside real delivery work and
strong enough to resist changes that only move cost into the future.

That is enough.

Part I has been about the mindset of principal engineering: seeing decisions as
future cost, making constraints explicit, asking better questions, owning beyond
the code you personally write, and tying judgment to evidence. This chapter
closes that arc by adding stewardship. A principal engineer does not merely
complete today's change or chase an abstract ideal system. The work is to make
the current outcome real while leaving the next necessary change cheaper, safer,
or easier to understand.

## Engineering Principle

When a change exposes or creates structural cost, include the smallest justified
improvement that reduces that cost without displacing the product outcome.

This principle depends on two laws introduced earlier in the handbook.
Simplicity Is a Feature (`LAW-004`) does not ask engineers to preserve the
smallest diff at any cost. It asks them to reduce the burden of understanding
and changing the system. Unused Flexibility Is Waste (`LAW-006`) reminds us that
options without current evidence still impose review, test, and diagnostic cost.

The practical move is disciplined stewardship. Use the current change as
evidence. Improve only the boundary or behavior the change actually crosses.
Remove or narrow obsolete flexibility only when the evidence is strong enough.
Record the decision so the next engineer can find it. Then stop.

## Architecture Exercise

### Define a Bounded Stewardship Action

Choose a change you are currently making or recently reviewed.

1. What product outcome must this change deliver?
2. What part of the system resists the change?
3. What structural cost does the change expose or create?
4. What evidence shows that cost is real rather than a personal preference?
5. What is the smallest improvement that directly reduces that cost?
6. How should it affect boundary clarity, Change Radius, Discoverability,
   ownership, or failure visibility?
7. What debt remains deliberately out of scope?
8. What existing behavior must not change?
9. What validation is needed for the product outcome?
10. What validation is needed for the stewardship action?
11. Where will the decision, limitation, or review trigger be made discoverable?
12. What is your stop condition?

> What is the smallest improvement you can include now that leaves the next
> necessary change cheaper without turning this task into a rewrite?

## Principal's Notebook

- Leave a cheaper path for the next related change.
- Improve the boundary the change actually crosses.
- Stop when the product outcome and the bounded stewardship outcome are both met.

## ADR

### Chapter ADR: Localize Power-Monitor Variation While Delivering the New Board Revision

### Context

A new industrial controller board revision replaces an external power-monitor
peripheral. The replacement changes startup timing, status interpretation, reset
behavior, error reporting, and one diagnostic capability. The existing shared
startup-support module mixes product boot orchestration, board checks,
monitor-specific interpretation, retry timing, fallback behavior, diagnostic
text, and unused configuration flexibility.

### Decision

Keep product-level boot orchestration in the startup path, but localize
monitor-specific timing, status interpretation, and reset behavior behind an
owned platform boundary. Select one supported monitor implementation per board
configuration. Remove the obsolete prototype fallback and narrow the unused
monitor-selection option using release, manufacturing, and test evidence. Add
minimal diagnostics for selected monitor implementation and product-level
power-health failure reason. Record the boundary, evidence, out-of-scope work,
and reconsideration triggers in the Decision Journal.

### Consequences

The board revision can ship without turning the work into a platform rewrite.
The next related monitor change has a smaller review and test surface because
monitor variation no longer leaks through product startup policy. Obsolete
fallback behavior and unused flexibility no longer impose review cost. The
startup path is still not fully redesigned, and unrelated initialization debt
remains outside this change.

### Alternatives Considered

Add another conditional to the shared startup-support module. This would be
fast, but it would increase Change Radius and preserve private knowledge about
monitor behavior, fallback paths, and diagnostic meaning.

Rewrite the startup path broadly. This would address more accumulated debt, but
the current board revision does not provide enough evidence or schedule room to
justify a platform redesign.

Introduce a generic plug-in framework for possible future monitors. This would
turn a bounded variation into speculative architecture before the team has
evidence that multiple active monitor families need that shape.

Deliver only the feature and defer every structural correction. This would
protect the narrowest schedule story, but it would knowingly preserve the same
leakage, obsolete fallback, and unsupported option that the change has made
visible.

Keep the obsolete fallback and unused monitor-selection option. This would avoid
removal risk, but the available evidence shows they no longer support released
products and would continue to tax review, test, and diagnosis.

## Editor's Commentary

Chapter 6 follows Chapter 5 by turning evidence-based judgment into bounded
stewardship. Chapter 5 asks how much confidence a claim deserves; this chapter
asks what the current evidence justifies changing in the system itself.

It operationalizes Chapter 1's idea that architecture is the future cost of
decisions. The chapter does not repeat Chapter 2's constraint framing, Chapter
3's question discipline, Chapter 4's ownership model, or Chapter 5's evidence
ladder. Instead, it shows how those habits combine when a real product change
exposes structural cost.

This closes Part I because the principal-engineer mindset is now complete enough
to move from posture to laws. Part II can name the forces that make systems
easier or harder to change without introducing a new PEAK concept here.
The concepts carrying this chapter are Architecture Health, Change Radius,
Discoverability, Utility Gravity, Platform Leakage, Temporary Solution, Decision
Journal, Simplicity Is a Feature, and Unused Flexibility Is Waste. Later parts
can build on those concepts without reopening the authoring scope of this
chapter.
