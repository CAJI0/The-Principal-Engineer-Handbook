# Unused Flexibility Is Waste

## Opening Quote

> An option is not free after the system has to remember it.

## Story

The radio service had been designed to survive products that did not exist yet.

The first product needed one validated transport. It used one radio module, one board family, one packet format, and one
field service workflow. The release needed the communication service to wake the radio, send a command, receive a
response, retry safely, report diagnostics, and recover after reset. That was already enough work for one release.

The team also knew the product line might grow.

A lower-cost board was plausible. So was a long-range transport, a manufacturing service mode, a second radio module if
the first supplier became risky, or a product that needed a different packet-framing rule. None of those possibilities
was absurd. Hardware teams really do change parts. Customers really do ask for variants. Supply chains really do turn an
ordinary dependency into a release problem.

So the team preserved options.

The service gained a runtime mode selector. It gained transport strategies. It gained conditional compilation for two
boards that had not been approved. It gained fallback behavior for a weak-link prototype. It kept a service-tool
compatibility path that translated old prototype commands into the new service. It added a test-only configuration that
could force retry behavior and later leaked into release builds. It kept a dormant hardware transport because removing it
felt riskier than leaving it in place.

The code looked careful.

There was an interface around the transport. There were compile-time flags for board-specific details. There were
runtime flags for service mode, production mode, factory mode, diagnostic mode, and prototype compatibility. There were
tests for the current product. There were a few tests for older paths. There were comments explaining that some modes
were not used yet, but might be needed later.

Only one combination shipped.

The production controller used the validated radio module, the production packet format, the normal runtime mode, and
the supported service-tool flow. The rest stayed because the phrase "we may need it later" sounded cheaper than a
decision.

The field defect was narrow.

A small number of devices failed to reconnect after a noisy site gateway dropped the radio link during a command
exchange. The shipped transport received a late response from the peer after the service had already moved into retry.
The production path should have classified the response as late, kept the retry state bounded, and reported a clear
diagnostic. Instead, some units reported `radio unavailable` and stopped retrying until the next service session.

At first, the bug looked like ordinary radio work.

One engineer checked retry timing. Another traced the packet parser. A test engineer tried to reproduce the drop and late
response. A service engineer compared field logs. The fix seemed likely to live in the production transport.

Then the review touched the flexible service.

The retry state depended on runtime mode. The error mapping depended on whether the selected transport was the current
radio, the dormant long-range transport, or the prototype weak-link fallback. The parser carried a branch for a packet
format no approved product used. The diagnostic path used generic mode names because the service did not know which
combinations were supported. The service tool exposed an old prototype compatibility switch, so support could accidentally
start a session in a mode the product did not own. CI still built two board variants nobody shipped, and one of them had
not compiled cleanly since a register definition moved.

The defect was in the shipped path, but the team had to reason about everything around it.

Tests failed in combinations no product supported. Reviewers disagreed about whether a fallback branch was reachable. A
dormant transport changed one error from "late response" to "radio unavailable" because its retry model had once needed
that meaning. A service-tool test asserted old prototype behavior because support had used it during pilot units. A
security reviewer asked whether the dormant transport could be selected through configuration in the field. A release
engineer asked which build flags corresponded to supported products. Product owners could name the current product, but
not which options the product had agreed to own.

The team's first responses were understandable.

"Keep all modes until we are sure."

"Add tests for every combination."

"Mark the old paths as legacy."

"Hide unsupported options in the service documentation."

"Add another flag so the production path bypasses the dormant transport."

"Move the runtime selector to compile time."

"Add a second abstraction layer so the old modes cannot interfere."

"Clean it up after this release."

Each proposal reduced discomfort in one place while preserving the basic problem. The system still contained more
options than the product owned.

The Principal Engineer asked the team to make a list without using the word flexible.

The team wrote down every runtime mode, backend, build flag, fallback path, service-tool compatibility behavior,
test-only switch, dormant implementation, and board-specific branch. Beside each item they wrote who used it, which
product supported it, which tests proved it, which tools exposed it, which documentation mentioned it, what uncertainty
it protected against, and who would decide whether it stayed.

Most rows were quiet.

The production transport had evidence. One current product used it. The service tool used it. Tests and support
documents needed it. The owner was clear.

The old prototype compatibility path had a history, not an owner. It had helped pilot units, but those units had already
moved through their service window. The comment said temporary. There was no review trigger, no removal condition, and
no current consumer. It was a Temporary Solution (`ANTIPATTERN-006`) that had stopped looking temporary because nothing
forced the team to look at it again.

The dormant long-range transport had a hope, not evidence. A future product might need it, but no product had committed
to the module, packet behavior, diagnostics, certification work, or support plan. Its error model had already leaked into
the production path. That was Platform Leakage (`SMELL-005`): low-level transport behavior escaping into product logic
without an explicit boundary the product owned.

The runtime mode selector had created Boolean Explosion (`SMELL-003`). Factory, diagnostic, prototype, production,
fallback, and transport-selection flags combined into behavior no one could list. Each flag looked small. Together they
created state combinations that reviewers, tests, and tools treated as possible even when no product supported them.

The board flags were not free because they were compile-time. They affected CI, release packaging, manufacturing
scripts, and confidence in which behavior belonged to which product. One stale combination did not enter the production
binary, but it still delayed the release because the build matrix claimed it mattered.

The team measured Change Radius (`VOCAB-001` and `METRIC-001`) in practical terms. Keeping an option touched more than
the implementation. It touched unit tests, integration tests, CI jobs, service-tool behavior, field diagnostics, release
notes, security review, manufacturing scripts, and support explanations. The cost of the option was the surface that had
to change, be reviewed, or be retested whenever the communication service changed.

The Principal Engineer recast the subsystem.

"This is not a flexible service," she said. "It is a service with unowned options charging rent."

That changed the decision.

The team did not delete the transport interface. There was real uncertainty around future radio hardware, and adding a
transport seam later would be expensive if the product boundary disappeared entirely. But the team no longer treated the
interface as a reason to keep every dormant implementation behind it.

They defined one supported runtime mode for the shipped product. They removed unsupported runtime modes from shipped
builds. They deleted configuration that exposed unsupported behavior. They removed the dormant long-range implementation
and the old prototype fallback. They kept one narrow product-owned transport seam with a small set of product meanings:
send accepted, response received, late response, retry allowed, radio unavailable, unsupported transport, and permanent
failure.

They reduced CI to supported combinations and one focused seam test. They migrated service-tool tests away from prototype
behavior. They updated diagnostics so logs reported the supported product mode and transport decision rather than a
generic selector value. They recorded which service and manufacturing tools had ever used the old compatibility path and
what migration evidence proved those uses had ended.

The material decision became an ADR.

Smaller retained options went into a Decision Journal (`ARTIFACT-003`): why the seam stayed, what evidence justified it,
how confident the team was, and what would trigger another review. Discoverability (`METRIC-003`) improved because a new
engineer could find which variations were supported, who owned them, why one seam remained, and what conditions would
allow another implementation to return.

The field defect still had to be fixed.

After the option surface was narrowed, the fix became easier to reason about. A late response in the supported transport
mapped to a bounded retry state. The dormant transport no longer changed error semantics. The service tool no longer
exposed unsupported behavior. The test matrix no longer pretended every historical combination was a product promise.

The radio service became less flexible in the visible sense.

It became more able to change.

## Discussion

`LAW-006` states: Flexibility that is not used or justified becomes maintenance cost.

That law is easy to misread as a complaint about abstraction. It is not. The problem is not that engineers preserve
options. The problem is that options become real system surface long before anyone uses them.

Flexibility has value only when it protects against real, material uncertainty. Options that are not used, justified, or
deliberately owned become permanent maintenance cost. Pay for flexibility only when the uncertainty it protects against
is real enough to justify the ongoing cost.

The first discipline is to separate flexibility from variability.

Flexibility is a deliberately retained option for future variation. Variability is supported product, environment, or
operational difference that the system truly owns. A product with two approved radio modules, two certified markets, or
two supported manufacturing flows is not waste merely because one branch is active at a time. That variability has
consumers, tests, documentation, support expectations, and owners.

A hypothetical future mode is different. It may be plausible. It may even be likely. It is not justified merely because
the code can support it.

The second discipline is to separate flexibility from optionality.

Optionality may mean preserving the ability to decide later. It does not require shipping every possible implementation
now. A team can preserve a narrow seam around a volatile transport boundary without carrying three dormant transports,
five runtime modes, and a public selector that promises all of them. A reversible decision preserves a path for later
change. It does not automatically require multiple live paths today.

This distinction matters because engineers often defend implementation inventory as if it were optionality. "We can
change transports later" is not the same as "we must ship every transport candidate now." The first may be a useful
architecture decision. The second may be an unpaid maintenance bill.

Flexibility is used when a supported product, environment, workflow, customer, deployment, or test strategy actively
depends on it. If a service tool, manufacturing line, field workflow, supported hardware variant, or customer commitment
uses the option, the option is part of the product surface.

Flexibility may also be justified before current use. The uncertainty may be material. Likely alternatives may be known.
Adding the option later may be expensive or risky. The seam may be small and contained. An owner may exist. A review
trigger may say when to keep, change, or remove it. Evidence may come from a roadmap, signed customer need, regulatory
requirement, repeated change history, field-support obligation, shipped compatibility promise, or testing constraint
better served by a seam than a full product option.

That is a real engineering judgment. It should not become a bureaucracy-heavy approval framework.

Flexibility becomes waste when it has no supported user, no material uncertainty, no evidence, no owner, no review
trigger, and unbounded continuing cost. The system keeps paying because nobody wants to make the decision visible.

Runtime flexibility is the easiest to feel in incidents.

Modes, runtime flags, strategy selection, selectable backends, service discovery, fallback behavior, and product
configuration all create live behavior. They affect state space, diagnostics, field support, configuration migration,
security review, and recovery. A defaulted-off flag may still need to be parsed, migrated, secured, documented, tested,
and explained. A fallback path may still change error behavior. A dormant mode may still influence initialization or
diagnostics.

Compile-time flexibility moves cost. It does not erase it.

Conditional compilation, build flags, generated-code options, target variants, optional drivers, and release matrices may
keep unused paths out of one binary. They still affect CI, release packaging, manufacturing, service tools, and the
ability to know which product contains which behavior. A stale build variant can delay a release even when no customer
runs it. A board flag no one owns can confuse support because the repository still claims the combination exists.

Architectural flexibility is subtler.

Seams, interfaces, adapters, extension points, compatibility layers, plug-in designs, and framework-like abstractions can
be valuable. An interface with one production implementation may be justified by testability, platform isolation, known
volatility, clear ownership, or constrained dependency direction. A compatibility layer may be justified when shipped
consumers still depend on old behavior. A seam can protect future change without making product code know a vendor's
details.

The mistake is treating the seam as permission to keep every possible implementation.

A seam is a narrow place where a future change can be introduced. It is not an inventory of all imagined changes. When
the seam starts exposing unsupported backends, generic error models, unowned configuration, and dormant modes, it is no
longer only preserving optionality. It is creating promises.

Chapter 8 owns the full API promise argument. Chapter 11 uses only the part it needs: extension points, optional fields,
runtime selectors, and compatibility layers can become behavior other code and people trust. If those promises are not
owned, they will still have to be honored, migrated, or removed later.

Chapter 9 owns dependency choice. Chapter 11 uses only the part it needs: generic wrappers and multiple backends can
import dependency behavior into the system even when the product does not own those variations. A wrapper around three
backends does not make all three cheap. It may only make the cost harder to see.

Chapter 10 owns time. Chapter 11 may use review triggers, but it should not become a scheduling law. A trigger is not a
calendar decoration. It is the condition that forces reconsideration: product launch, variant retirement, compatibility
window end, customer migration completion, no measured usage, test matrix growth, a defect in a dormant path, hardware
selection, or release-train change.

The cost surface is wider than code.

Unused flexibility creates implementation branches. It creates state combinations. It multiplies tests. It grows CI
matrices. It complicates release packaging. It adds configuration migration. It increases documentation burden, review
effort, code search, field support, manufacturing behavior, service-tool behavior, diagnostics, security review,
compatibility obligations, failure modes, rollback paths, upgrade paths, and future deletion cost.

Boolean Explosion (`SMELL-003`) is one common symptom. Several independent flags create behavior combinations no one can
reason about. The team may know the intended default. It may not know every legal combination, every illegal combination,
or every combination that tests accidentally exercise. Bugs then appear in rare mixes that no product owner recognizes.

Platform Leakage (`SMELL-005`) is another symptom. A dormant hardware transport or speculative board hook starts
shaping product logic. Vendor errors, register timing, retry quirks, or low-level failure meanings leak into the product
because the platform boundary was built for imagined variation rather than owned behavior. Not every platform detail
needs hiding, but every leak should be intentional.

Temporary Solution (`ANTIPATTERN-006`) is how unused flexibility often survives. A prototype fallback, customer bypass,
calibration shortcut, or service compatibility path is added for a real reason. Then the owner, review trigger, and
removal condition disappear. The temporary path becomes permanent because its context is forgotten.

The remedy is not immediate deletion by search result.

Removing flexibility is an architectural decision when other code, tests, tools, documents, field workflows, or shipped
versions may depend on it. The team must prove current use or non-use, identify direct and indirect consumers, migrate
tools and tests, delete configuration, reduce the CI matrix, remove compatibility behavior, update documentation, check
manufacturing and field workflows, define rollback boundaries, and preserve enough evidence for future engineers to
understand why the option disappeared.

Deletion without evidence can be as irresponsible as keeping everything.

The right outcome may be one supported implementation, one narrow product-owned boundary, no unsupported runtime
selector, and explicit evidence for adding another implementation later. It may preserve a seam. It may retain a
compatibility promise for a bounded window. It may defer a choice until a product decision arrives. It may remove the
dormant implementation but keep focused tests around the boundary where another implementation could return.

Retained flexibility needs three things: evidence, ownership, and a review trigger.

Evidence answers why the system is paying for the option. Ownership identifies who decides whether it remains supported,
which products use it, which tests prove it, which documents and tools expose it, when it can be removed, and who reviews
the trigger. The review trigger names the condition that reopens the decision.

An ADR (`ARTIFACT-001`) is appropriate when the flexibility decision affects architecture, ownership, cost, or
reversibility. Removing unsupported runtime modes while preserving one transport seam is that kind of decision. A
Decision Journal (`ARTIFACT-003`) is useful for smaller retained options: a reversible build flag, a test seam, a
temporary compatibility setting, or a deferred variant hook that still needs evidence, confidence, and a review trigger.

Discoverability (`METRIC-003`) matters because unused flexibility hides in plain sight. Engineers can find the code but
not the intent. They can find the flag but not the product that supports it. They can find the fallback but not the
condition that would remove it. Poor discoverability turns maintenance into archaeology.

This chapter sits near Chapter 12, but it is not Chapter 12.

Simplicity Is a Feature (`LAW-004`) will make the broader argument that simple systems are easier to review, operate,
test, explain, and change. Chapter 11 is narrower. It says that unused options are one specific way complexity becomes
permanent cost. The point is not to prefer simple-looking code in every case. The point is to refuse option surface that
no product, evidence, owner, or trigger justifies.

The law also sits near Chapter 13, but it is not Chapter 13.

Evidence Before Confidence (`LAW-005`) will own evidence quality, confidence calibration, and proof standards. Chapter 11
uses evidence for a narrower purpose: deciding whether the system should keep paying for an option.

The practical test is direct.

If the option protects real uncertainty or supports an owned variation, pay for it deliberately. If it does not, remove
the option or preserve only the smallest seam justified by evidence.

## Engineering Principle

Keep flexibility only when it protects real uncertainty or supports an owned variation. Otherwise, remove the option and
preserve only the smallest seam justified by evidence.

Use a focused review around questions like these:

1. Who uses this option today?
2. Which real uncertainty does it protect against?
3. What would it cost to add later?
4. Which products, tools, tests, or workflows support it?
5. Who owns it?
6. Which tests prove the supported combinations?
7. What documentation and tools expose it?
8. Which compatibility obligations exist?
9. What condition will trigger review or retirement?
10. Which seam can remain if the option is removed?

The goal is not to punish engineers for thinking ahead. The goal is to make the cost of thinking ahead visible enough
that the team can decide whether the option is worth carrying.

## Architecture Exercise

### Audit One Flexibility Point

Choose one real flexibility point from a system you know: a mode, flag, backend, interface, fallback, build option,
compatibility layer, or extension point.

Write short answers to these prompts:

1. What is the exact option name?
2. Which products, customers, tools, tests, or workflows use it today?
3. What evidence shows that use?
4. What uncertainty does it protect against?
5. What would it cost to add later if removed now?
6. Is it exposed at runtime, compile time, or architecture boundary?
7. Which state combinations does it create?
8. Which tests are required because it exists?
9. What does it add to CI or the release matrix?
10. What documentation mentions it?
11. Which service-tool, manufacturing, or field-support behavior exposes it?
12. What failure or security-review surface does it create?
13. Which compatibility obligations depend on it?
14. Who owns the option?
15. What condition triggers review or retirement?
16. What evidence would prove it can be removed?
17. Which consumers would need migration?
18. What is the smallest seam worth preserving?
19. Where should the decision live: ADR or Decision Journal?

End with one decision:

- keep and own;
- narrow;
- defer;
- remove;
- preserve only the seam;
- create a review trigger with a date or condition.

Do not create a new artifact to manage this exercise. Use the records the system already has.

## Principal's Notebook

- Options charge rent.
- A seam is not every path.
- Temporary needs a trigger.

## ADR

### Chapter ADR: Remove Unsupported Runtime Modes and Preserve One Transport Seam

### Context

One shipped product uses one validated communication path. The radio service also contains multiple dormant runtime
modes, transport candidates, conditional build paths, prototype compatibility behavior, test-only configuration, and
fallback branches.

Unsupported combinations affect tests, review, diagnostics, service tools, release packaging, and security review. A
field defect in the shipped transport exposed unclear supported behavior because dormant paths changed error semantics
and service tooling could still expose old options.

Future transport variation is plausible. A new radio module or board family may appear. However, no current product owns
the dormant implementations, and the existing option surface is larger than the uncertainty justifies.

### Decision

Define the single supported runtime mode for the current product.

Remove unsupported runtime modes from shipped builds. Delete configuration that exposes unsupported behavior. Remove
dormant implementations and old prototype fallback behavior. Reduce CI and release packaging to supported combinations
plus focused tests around the retained seam.

Preserve one narrow product-owned transport seam. The seam exposes product meanings such as send accepted, response
received, late response, retry allowed, radio unavailable, unsupported transport, and permanent failure. It does not
promise every backend capability in advance.

Assign an owner and review trigger for the retained seam. Document compatibility obligations for any service,
manufacturing, or field-support workflow that used old behavior. Keep focused tests around the supported product path and
the seam. Use the Decision Journal for smaller retained options whose evidence or review triggers do not require a full
ADR.

### Consequences

The supported behavior becomes clearer. State space and test combinations shrink. Review and diagnosis cost fall because
unsupported paths no longer participate in production reasoning. Service tools and diagnostics can report product-owned
meanings instead of generic selector values. Boolean Explosion is reduced. The product keeps a future change seam without
shipping every imagined transport.

The decision creates migration work. Tests and tools that used prototype behavior must change. Compatibility obligations
must be checked before removal. Evidence must be retained so future engineers know why the old paths disappeared. Some
short-term delivery time is spent reducing the option surface. A removed path may need to be rebuilt if a future
product makes it real. The retained seam requires discipline so it does not grow into another unowned framework.

### Alternatives Considered

Keep all modes until a future product appears. This preserves maximum apparent flexibility, but it keeps charging every
release, review, test, diagnostic, and support path for options no product owns.

Test every combination. This treats the current option surface as legitimate product surface and expands cost instead of
deciding which combinations are supported.

Hide unsupported options in documentation while retaining behavior. This reduces visible confusion but keeps runtime,
security, service-tool, and diagnostic ambiguity.

Replace runtime options with compile-time flags. This may be useful for supported variants, but it does not reduce cost
unless the unsupported combinations are actually removed from CI, packaging, tools, and support expectations.

Remove all abstraction and call hardware APIs directly. This would reduce indirection now, but it would discard a
justified seam around likely future transport variation and increase Platform Leakage into product code.

Duplicate the subsystem per product. This can be appropriate for truly separate product lines, but here it would create
parallel behavior before the product variation exists.

Build a broader plug-in framework. This would formalize the speculative surface and make unsupported extension feel more
official.

Postpone cleanup. This keeps the release moving in the short term, but it leaves the next defect to rediscover the same
unowned options with less time.

## Editor's Commentary

Chapter 11 follows the first four Part II laws by focusing on option surface.

Chapter 7 asked who owns meaningful state. Chapter 11 may show that modes and flags multiply state combinations, but it
does not reteach state authority. Chapter 8 asked what an API promises. Chapter 11 may show that extension points and
compatibility behavior create promises, but it does not retell API evolution. Chapter 9 asked what commitments enter
through dependencies. Chapter 11 may show that multiple backends and generic wrappers create cost, but it does not
repeat dependency selection. Chapter 10 asked which time a system depends on. Chapter 11 uses review triggers without
becoming a time chapter.

The boundary with Chapter 12 is deliberate. This chapter does not argue that all simplicity is good or that all
abstraction is suspicious. It makes one narrower claim: unused flexibility is maintenance cost unless evidence,
ownership, and review triggers justify paying for it. Chapter 12 can make the broader case for simplicity as a product
capability.

The boundary with Chapter 13 is also deliberate. This chapter asks for enough evidence to justify carrying or removing an
option. It does not teach the full discipline of evidence quality, confidence, experiments, or proof.

The PEAK concepts carrying this chapter are Unused Flexibility Is Waste (`LAW-006`), Boolean Explosion (`SMELL-003`),
Platform Leakage (`SMELL-005`), Temporary Solution (`ANTIPATTERN-006`), Change Radius (`VOCAB-001` and `METRIC-001`),
Discoverability (`METRIC-003`), ADR (`ARTIFACT-001`), and Decision Journal (`ARTIFACT-003`). They are enough. The
chapter does not need a new option ledger, variant map, seam catalog, or flexibility budget to teach the law.

The reader-facing move is modest and durable: keep the seam when the uncertainty is real, but stop carrying every path
the seam could someday contain.
