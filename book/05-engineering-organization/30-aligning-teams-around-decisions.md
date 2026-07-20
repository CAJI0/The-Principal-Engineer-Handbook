# Aligning Teams Around Decisions

## Opening Quote

> Agreement is only useful when every affected owner can act from the same decision.

## Story

### The Decision Everyone Agreed To Differently

The provisioning compatibility decision had already been accepted.

That was the strange part.

No one was waiting for an architecture verdict. The firmware lead, backend lead, service-tool owner, manufacturing
owner, support lead, test lead, release owner, and product architecture owner had all been through the RFC and
Architecture Review. The decision looked responsible. Older devices would continue to work. The next release would move
to a cleaner provisioning flow. The device would own final provisioning acceptance. The backend would own reservation
and entitlement. Manufacturing would write a bounded package. Support would get clearer diagnostics. Release would name
the supported combinations.

The ADR existed. The RFC was closed. The Architecture Ledger had links.

Then implementation began, and the agreement started to split.

Firmware treated the decision as a new default behavior with a temporary compatibility path. The old provisioning flow
would remain only for named older firmware and one service-tool version. The firmware team built the state model that
way: new devices moved through the new acceptance path, old devices entered the compatibility path, and that path had a
removal condition.

Backend treated the decision differently. To them, "keep older devices working" meant supporting both provisioning
modes indefinitely unless product explicitly removed one. Their API draft preserved the old activation behavior beside
the new reservation and entitlement behavior. They saw that as cautious. Firmware saw it as a permanent promise the team
had not accepted.

The service-tool team assumed the old provisioning sequence remained authoritative. The operator workflow still showed
the station-written package as the main source of readiness because that was what technicians already understood. The
tool could display new backend reservation information, but it did not change the old sequence labels. Support
diagnostics were being updated from those same labels.

Manufacturing scripts kept writing a manufacturing compatibility flag whose owner was unclear. The station owner
believed firmware owned the flag because the device consumed it. Firmware believed manufacturing owned it because the
station wrote it.
Backend believed it was an implementation detail. Release believed it was part of the compatibility matrix. Nobody was
lying. They were each carrying a different slice of the same decision.

Support diagnostics described behavior the new firmware would no longer guarantee. The draft support article said that
"provisioned" meant the package had been written and the device was ready for activation. In the new flow, the package
could be written while backend reservation had expired, or while the device had rejected the package after local
validation. Support wanted one visible phrase. Firmware and backend had deliberately separated the meanings.

The test team could not tell which release-critical test combinations mattered. Should they test old service tool with new
firmware and old backend behavior? New service tool with old firmware and new backend behavior? Manufacturing station
version N with backend reservation expiry? Field procedure after a failed package write? Every combination had a local
argument behind it. None had an owner saying, "This is required because this is the decision we accepted."

The release owner saw the problem before anyone else admitted it.

"Everyone says this is aligned," she said. "But I cannot tell what evidence is missing."

The Architecture Ledger had a row for the provisioning decision. It linked the RFC, the ADR, and the compatibility
matrix. It listed the product architecture owner. It did not list the affected-owner obligations. It did not say that
firmware owed a state model, backend owed API promise wording, manufacturing owed station flag ownership, service
tooling owed operator semantics, support owed product-safe diagnostic language, test owed supported combination
coverage, and release owed the gate for unsupported combinations.

Mara, the Principal Engineer, discovered the real failure in a set of private messages.

Firmware asked her whether backend was allowed to keep both modes forever.

Backend asked her whether firmware was allowed to remove the compatibility path after one release.

Service tooling asked her which screen should be treated as authoritative.

Manufacturing asked her who owned the station flag.

Support asked her whether the word "provisioned" was still safe.

Test asked her which matrix mattered.

Release asked her what evidence should block the date.

Every question was reasonable. Together, they meant the organization had not aligned around the decision. It had
aligned around the feeling that a decision had happened.

In the next implementation review, someone asked the practical question:

> Can you send the decision around so everyone is aligned?

Mara did not open a new announcement.

She wrote the question at the top of the whiteboard, then wrote another beneath it:

> What must each affected team now do, own, verify, stop doing, or revisit because of this decision?

That second question was less comfortable.

It made the decision operational.

The team started with the decision owner. The product architecture owner still owned the accepted provisioning boundary.
Mara did not. The firmware lead did not. The backend lead did not. The release owner did not. Each of them owned an
affected surface, but the accepted architecture needed one owner who could explain the technical choice and reopen it
when evidence changed.

Then they named the affected owners.

Firmware owned device-side acceptance state and the temporary compatibility path inside firmware. Backend owned
reservation, entitlement, package expiry, and API status meanings. Manufacturing owned station package writing,
station evidence, and the compatibility flag at the point it was written. Service tooling owned operator workflow and
which product-level meanings appeared on screen. Support owned field procedure and customer-safe diagnostic language.
Test owned the release-critical matrix. Release owned the gate that would prevent unsupported version combinations from
shipping. Product owned customer communication and scope if the compatibility promise changed.

The room did not become simpler. It became less vague.

Mara asked the owners to state what changed and what must stay true.

Firmware said the device would become the final owner of operational acceptance for the new flow. What must stay true:
older supported devices must not be made unrecoverable by the new package shape.

Backend said reservation and entitlement would remain backend-owned, but backend status could no longer imply device
acceptance. What must stay true: support and service tooling must not treat reservation as readiness.

Manufacturing said the station would write a bounded package and record evidence, but it would not decide field
readiness. What must stay true: station throughput could not collapse, and the written flag needed one owner.

Service tooling said the operator workflow would show product-level states, not raw firmware detail. What must stay
true: technicians must be able to distinguish backend rejection, device rejection, package written, and unknown.

Support said the article would stop using "provisioned" as a single outcome. What must stay true: customer language
could not expose unstable implementation detail as a product promise.

Test said the release-critical matrix would include named firmware, service-tool, backend, and station versions. What
must stay true: untested combinations would be blocked rather than explained as supported.

Release said the date depended on evidence, not confidence. The new flow needed firmware acceptance tests, backend
expiry behavior tests, station package evidence, service-tool operator flow checks, support diagnostic review, and a
compatibility matrix with unsupported combinations named.

The decision had not changed.

The obligations had.

Mara asked the team to update the accepted RFC, not because an RFC was a magic container, but because the RFC already
held the proposal, scope, non-goals, risks, and open questions that had crossed ownership boundaries. The final ADR
would stay focused on the architectural decision and consequences. It would not become a task tracker. The RFC would
carry the alignment surface until implementation closed.

The RFC gained a new section called "Affected owner obligations." The title was not meant to create a new artifact. It
was a plain section in the existing record.

For each owner, the section stated:

- the affected surface;
- the changed promise;
- the promise that must remain stable;
- the dependency consequence;
- the sequencing constraint;
- the evidence already accepted;
- the evidence still missing;
- the open question;
- the temporary exception, if any;
- the review trigger.

The firmware entry said the compatibility path was temporary, owned by firmware, supported only for named older
firmware and one service-tool version, and reviewed after the first field upgrade window. The backend entry said both
modes were not an indefinite product promise; support for the old mode was tied to the compatibility window. The
manufacturing entry made the station flag ownership explicit: manufacturing owned writing and evidence, firmware owned
interpretation after device read, and no other component could infer readiness from the flag alone.

The service-tool entry changed the old workflow. The screen would no longer treat the old sequence as authoritative.
It would show stable product-level outcomes that matched the accepted API promises. The support entry removed the broad
"provisioned" wording and replaced it with customer-safe states. The test entry named the release-critical
combinations and the combinations release would block. The release entry named the evidence gaps that would prevent the
decision from being treated as ready.

Three smaller follow-ups did not belong in the ADR.

The old service tool could mislabel an expired backend package as a device rejection. That went into the Decision
Journal with evidence, confidence, owner, and review trigger. The manufacturing station needed one more proof run after
the flag ownership change. That also went into the Decision Journal. The support team needed to test whether technicians
could distinguish backend rejection from device rejection using the new wording. That was small enough for a journal
entry, but important enough not to leave in meeting memory.

The Architecture Ledger row changed too. It kept the active decision visible: decision owner, status, related RFC,
related ADR, related Decision Journal entries, affected owner list, and review date. A future engineer could search from
the service-tool screen, backend status, station flag, or support article and find the decision rather than asking Mara
why the system behaved that way.

At the end, Mara asked each affected owner to say the decision in one sentence and name their obligation.

Firmware said: "The device owns final provisioning acceptance; we own the new state model and the temporary
compatibility path."

Backend said: "Reservation and entitlement stay backend-owned; we will not let backend status imply device readiness."

Manufacturing said: "The station writes a bounded package and records evidence; it does not own field readiness."

Service tooling said: "The tool shows product-level provisioning outcomes that match the accepted promises."

Support said: "The field procedure names stable customer-safe outcomes and does not expose raw diagnostic detail as a
promise."

Test said: "The release-critical matrix follows the accepted decision and blocks unsupported combinations."

Release said: "The date depends on the named evidence and unsupported combinations are not hidden by confidence."

Product said: "Customer communication will describe the compatibility window, not an indefinite old-flow promise."

They still disagreed about details. Backend wanted a longer compatibility window. Support wanted one shorter label.
Manufacturing wanted to remove one station proof run. Those disagreements were no longer proof that the decision was
unclear. They were follow-up decisions with owners, evidence, and triggers.

Two weeks later, Mara noticed what had changed.

People still asked her questions, but they no longer asked her to be the live translator of the decision. They asked
whether the RFC obligation matched the ADR. They asked whether a Decision Journal entry had enough evidence. They asked
whether a new service-tool behavior changed the API promise. They asked whether the compatibility exception had reached
its review trigger.

That was alignment.

Not because everyone agreed with every consequence.

Because each team could act from the same decision.

## Discussion

Aligning teams around decisions means converting a technical choice into shared operational meaning.

That is narrower than organizational alignment in the usual sense. It is not a mood. It is not consensus. It is not
attendance. It is not a statement that everyone has been informed. A decision is aligned when every affected owner can
name the same decision, consequence, obligation, sequence, evidence, and review trigger.

A decision can be correct and still fail if teams implement different interpretations of it.

That is what happened in the story. The provisioning boundary had a responsible shape. The device owning final
acceptance was a responsible architecture choice. Backend reservation and entitlement ownership made sense.
Manufacturing station evidence was real. Service-tool workflow mattered. Support language mattered. Release risk
mattered. The failure was that each team turned the same decision into a different set of obligations.

Agreement is weaker than shared obligations.

Agreement says, "I accept the direction." An obligation says, "This is what my team must now do, own, verify, stop
doing, or revisit because the direction exists." The second sentence is more useful because architecture becomes real
through the work teams perform after the decision. The final decision may live in an ADR, but the system lives in API
behavior, state ownership, station scripts, diagnostic wording, tests, release gates, and support procedure.

Alignment starts after the question is framed and before implementation assumptions harden.

Too early, and the team is aligning around guesses. Too late, and each team has already turned private assumptions into
code, scripts, tests, and procedures. The useful window is when the decision has enough shape to coordinate work but
before the consequences have become expensive to change. That is why the RFC (`ARTIFACT-002`) is central in this
chapter. The RFC is already the place for proposals that need feedback across ownership boundaries. It carries summary,
motivation, scope, non-goals, proposal, risks, and open questions while implementation can still respond.

An accepted RFC can also become an alignment surface.

That does not mean inventing a new permanent artifact. It means using the existing proposal record to close the gap
between "we chose this direction" and "each affected owner knows what the choice now requires." The RFC should expose
the decision owner, affected owners, changed promises, unchanged promises, sequencing constraints, evidence, open
questions, temporary exceptions, follow-up owners, and review trigger. If the RFC does that work, the team can align
without relying on one Principal Engineer to answer the same question from every direction.

The decision owner is not automatically the owner of every affected change.

This distinction protects both accountability and autonomy. The product architecture owner may own the accepted
provisioning boundary. Firmware still owns device acceptance state. Backend still owns reservation and entitlement
behavior. Manufacturing still owns station writes and station evidence. Support still owns field procedure. Release
still owns the gate. Affected owners do not need veto power over every detail, but they do need obligations they can
accept, challenge, and execute.

Every State Has One Owner (`LAW-001`) matters here because alignment often fails around state that no one owns cleanly.
The station flag in the story was not only a variable. It was a decision state. Manufacturing wrote it. Firmware
interpreted it. Backend ignored it until support asked questions. Release treated it as part of compatibility. Without
explicit ownership, the flag became Hidden State (`SMELL-004`): it affected behavior, but the model and responsibility
were not visible.

Every API Is a Promise (`LAW-002`) matters because team obligations often appear as words other teams trust.

"Reserved" is a promise. "Accepted" is a promise. "Provisioned" is a promise if support, service tooling, or customers
act on it. "Backend rejected" and "device rejected" are promises about meaning, not only strings in a response. When a
decision changes those promises, alignment must state what changed and what stayed stable. Otherwise teams create
Silent Coupling (`SMELL-001`) through private assumptions. The backend assumes one meaning. The service tool displays
another. Support writes a third. Tests bless whichever one they saw first.

Evidence separates alignment from optimism.

Evidence Before Confidence (`LAW-005`) is uncomfortable in alignment work because agreement can feel like evidence.
It is not. The release owner in the story did not need another statement that everyone supported the decision. She
needed to know which evidence had been accepted and which evidence was missing. Firmware acceptance tests, backend
expiry behavior, station proof runs, service-tool operator checks, support wording review, and compatibility matrix
coverage each supported different claims. If those claims are not separated, confidence gets spread across the whole
decision like paint.

Every Dependency Is a Decision (`LAW-007`) widens the view.

The provisioning decision depended on backend behavior, firmware state, service-tool versions, manufacturing scripts,
station evidence, support procedure, release notes, and field procedure. Those are dependencies even when they are not
libraries. They carry lifecycle constraints, failure modes, ownership boundaries, and replacement cost. Alignment makes
those consequences explicit enough that teams can sequence work. The station proof run must happen before release treats
the flag as trustworthy. Support wording must wait for stable product-level states. The old service-tool path must be
tested before it is promised.

Change Radius (`VOCAB-001` and `METRIC-001`) tells the Principal Engineer how much alignment work is justified.

Not every decision deserves this weight. A narrow, reversible choice inside one owned boundary may need only a code
review or a short Decision Journal entry. A decision that touches firmware, backend, manufacturing, service tooling,
support, tests, release notes, and field procedure has broad Change Radius. The affected surface is the reason to name
affected owners. The goal is not false precision. The goal is to avoid pretending that a cross-team decision is local
because the first code change appears in one repository.

The ADR (`ARTIFACT-001`) still matters, but it should not carry every obligation.

An ADR records the architectural decision, why it was made, alternatives, consequences, and revisit trigger. It should
link to the RFC section that carries implementation obligations when those obligations are too active or detailed for
the ADR. If every follow-up task goes into the ADR, the ADR becomes a stale project plan. If no obligation is linked
from the ADR, the ADR becomes a final answer without operational meaning.

Decision Journal entries (`ARTIFACT-003`) are useful for the smaller commitments that alignment creates.

The old service-tool mislabel risk did not need a full ADR. The manufacturing proof run did not need to reopen the
architecture decision. The support wording check was not a new architecture choice. Each still needed evidence,
confidence, owner, and review trigger. A Decision Journal entry gives those small commitments enough memory without
making the main decision record heavier.

The Architecture Ledger (`ARTIFACT-006`) is the discoverability test.

Discoverability (`METRIC-003`) asks whether an engineer can find the decision, owner, and contract behind system
behavior. For aligned decisions, extend that mental test: can a firmware engineer find the backend promise? Can support
find why a diagnostic phrase changed? Can manufacturing find who owns the station flag? Can release find which
combination is unsupported? If the answer is "ask Mara," the system has a Bus Factor (`METRIC-002`) problem. It depends
on private memory, even if the private memory belongs to someone helpful.

This is The Hero Engineer (`FAILURE-004`) in a quiet form.

No incident waits at the door. No one is celebrating heroics. The failure is softer: every affected team needs the same
senior engineer to translate the accepted decision into local meaning. That is not alignment. It is live interpretation.
The Principal Engineer should help the organization write the translation down in the right records so the next
question routes through evidence, ownership, and artifacts rather than through memory.

Temporary compatibility deserves particular care.

Temporary Solution (`ANTIPATTERN-006`) appears whenever a compatibility path, backend adapter, manual support rule, or
station exception has no owner, evidence, review trigger, or expiration condition. A temporary path can be the right
trade-off. Older devices may need support. A release may need one bounded adapter. A service tool may need a bridge
version. The danger is leaving "temporary" as a shared hope. Alignment turns it into an owned commitment: who owns it,
what evidence keeps it, what condition removes it, and what date or event forces review.

Alignment is also not consensus.

The backend team may prefer longer compatibility support. Support may prefer one label. Manufacturing may prefer fewer
proof runs. Those disagreements do not automatically reopen the decision. They become useful when each disagreement is
attached to an owner, evidence, consequence, and review trigger. Alignment preserves room for dissent while making the
accepted decision executable.

Nor is alignment program management.

A program plan can track dates and tasks. It cannot decide what "accepted" means, who owns a state, which API promise
changed, which diagnostic phrase is safe, which dependency consequence matters, or which evidence is enough. Technical
alignment gives program coordination something accurate to coordinate. Release planning can then sequence real work
rather than discover hidden interpretations late.

The practice is deliberately modest.

Use the RFC while the decision is still becoming operational. Use the ADR for the final decision. Use the Decision
Journal for smaller follow-ups. Use the Architecture Ledger so active decisions stay findable. Use Architecture Review
(`RITUAL-001`) when broad Change Radius, hard-to-reverse consequences, or cross-owner evidence require structured
challenge.

The point is not heavier process.

The point is that one decision should not become seven different systems.

Chapter 31 will later ask whether the architecture as a whole still supports necessary change. Chapter 30 stops before
that. It stays with one accepted decision and the practical question that follows it: what must each affected owner do
now because this decision exists?

## Engineering Principle

Align teams by turning decisions into shared obligations, not shared opinions. Name the decision owner, affected
owners, changed and unchanged promises, sequencing constraints, evidence, open questions, temporary exceptions, and
review trigger so each team can act on the same technical choice.

Use this principle when a cross-team decision has been accepted but teams are turning it into different work.

Ask:

1. What decision are teams interpreting differently?
2. Who owns the accepted decision?
3. Who is affected by the decision?
4. What changed?
5. What must stay true?
6. What does each affected owner now owe?
7. What must happen before what?
8. What evidence is accepted, and what evidence is still missing?
9. What temporary exception needs an owner and expiration condition?
10. What would reopen or revise the decision?

The goal is not universal agreement. The goal is compatible action from the same technical choice.

## Architecture Exercise

### Align One Cross-Team Decision

Choose one decision that affects more than one team. Prefer a decision where people already say they agree, but where
implementation plans, tests, support language, release assumptions, tooling behavior, or ownership responsibilities are
starting to diverge.

Do not create a new canonical artifact. Update the RFC, ADR, Decision Journal entry, Architecture Ledger row, test
record, support note, release note, or linked companion note that already carries the decision.

Document:

- the decision statement;
- the decision owner;
- the affected owners;
- the affected surfaces;
- one changed promise;
- one unchanged promise;
- one dependency consequence;
- one sequencing constraint;
- accepted evidence;
- missing evidence;
- one open question;
- one temporary exception;
- one follow-up owner;
- one review trigger;
- the artifact to update.

Then ask each affected owner to state the decision and their obligation in one sentence. If those sentences describe
different decisions, the alignment work is not done yet.

End with:

1. one decision statement;
2. one affected-owner obligation;
3. one changed or unchanged promise;
4. one sequencing constraint or evidence gap;
5. one artifact update.

## Principal's Notebook

- Agreement is not alignment.
- Affected owners need obligations, not rumors.
- A decision that only you can explain is not aligned.

## ADR

### Use the Provisioning RFC as the Alignment Contract

#### Status

Accepted for the team in the story.

#### Context

A provisioning compatibility decision has been accepted after RFC discussion and Architecture Review. The final ADR
records the selected technical direction: device-owned final provisioning acceptance, backend-owned reservation and
entitlement, bounded manufacturing package writing, product-level service-tool outcomes, named compatibility support,
and release gating for unsupported combinations.

Teams are interpreting the obligations differently. Firmware treats the compatibility path as temporary. Backend treats
both modes as an indefinite promise. Service tooling assumes the old provisioning sequence remains authoritative.
Manufacturing scripts write a compatibility flag whose owner is unclear. Support diagnostics describe behavior the new
firmware will no longer guarantee. Test owners cannot tell which combinations are release-critical.

Mara, the Principal Engineer, is becoming the translator for the same decision across teams. If that continues, the
decision will depend on private memory. The Bus Factor will fall, and the organization will repeat The Hero Engineer
failure in a quieter form.

#### Decision

Treat the accepted RFC, plus a short linked update if needed, as the alignment surface until implementation closes.

Update the RFC with:

- decision owner;
- affected owners;
- changed and unchanged promises;
- sequencing constraints;
- accepted evidence;
- missing evidence;
- open questions;
- temporary exceptions with owners and expiration conditions;
- follow-up owners;
- review trigger.

Keep the ADR focused on the final architectural decision, alternatives, consequences, and revisit trigger. Do not turn
the ADR into a project plan.

Use Decision Journal entries for small follow-ups and evidence gaps: old service-tool mislabel risk, manufacturing
station proof run, support wording review, and any temporary compatibility judgment that needs confidence and a review
trigger.

Add or update the Architecture Ledger row with owner, status, related RFC, related ADR, related Decision Journal
entries, affected-owner obligations, and review date.

Require each affected owner to confirm the obligation they own. Do not require each affected owner to approve every
detail.

#### Consequences

The decision becomes harder to misinterpret. Firmware, backend, service tooling, manufacturing, support, test, release,
and product can act from the same technical choice while still owning their surfaces. Changed and unchanged promises
are visible. Temporary compatibility paths have owners, evidence, review triggers, and expiration conditions. Smaller
follow-ups are discoverable without overloading the ADR. The Architecture Ledger can lead future engineers to the
current owner, contract, status, and review date.

The team accepts a maintenance cost. The RFC update must stay current until implementation closes. The ledger row must
not become duplicate documentation. Follow-up owners must close or revise their Decision Journal entries. The practice
must remain proportionate to Change Radius rather than becoming a new approval ceremony.

The benefit is lower late release drift, clearer ownership, better evidence tracking, better Discoverability, and lower
Bus Factor risk around one Principal Engineer.

#### Alternatives Considered

Send a decision announcement and rely on teams to infer their work.

This is fast, but it repeats the failure. Teams already agree with the headline while interpreting obligations
differently.

Reopen the whole decision until every team agrees on all details.

This confuses alignment with consensus. Some disagreements are follow-up decisions. They need owners and evidence, not a
new vote on the accepted architecture.

Make the Principal Engineer coordinate every follow-up manually.

This may work for one release, but it turns Mara into the live interpreter of the decision and increases private-memory
risk.

Put every obligation into the ADR.

The ADR should record the final architectural decision and consequences. Active implementation obligations are better
kept in the RFC update, Decision Journal entries, and Architecture Ledger links.

Wait for release planning or integration testing to expose mismatches.

This discovers divergent interpretation after assumptions have hardened. It turns alignment work into late risk
management.

Create a new permanent alignment artifact.

The existing RFC, ADR, Decision Journal, and Architecture Ledger are enough. The problem is not a missing container. The
problem is failing to turn the decision into visible obligations.

## Editor's Commentary

Chapter 30 follows Chapter 29 by moving from artifacts as teaching surfaces to decisions as coordination surfaces.
Chapter 26 showed how a Principal Engineer can lead without taking ownership away from accountable owners. Chapter 27
showed that reviews need durable memory. Chapter 28 showed how rituals preserve technical behavior. Chapter 29 showed
how artifacts can transfer judgment. Chapter 30 asks what happens after the record exists and several teams must act on
the same decision.

The chapter illustrates RFC (`ARTIFACT-002`) because the accepted RFC is the strongest existing surface for
cross-boundary alignment before implementation closes. ADRs (`ARTIFACT-001`) preserve the final decision and
consequences. Decision Journal entries (`ARTIFACT-003`) preserve smaller follow-ups, evidence gaps, confidence, and
review triggers. Architecture Ledger rows (`ARTIFACT-006`) keep active ownership, status, related artifacts, and review
dates findable.

The registered laws and signals remain material. Every State Has One Owner (`LAW-001`) keeps affected state and
compatibility-mode state from becoming shared confusion. Every API Is a Promise (`LAW-002`) makes backend statuses,
service-tool labels, diagnostic meanings, and timing behavior reviewable as promises. Evidence Before Confidence
(`LAW-005`) keeps release confidence tied to accepted and missing evidence. Every Dependency Is a Decision (`LAW-007`)
makes tooling, station scripts, backend behavior, support procedure, release gates, and field procedure part of the
architecture conversation. Change Radius (`VOCAB-001` and `METRIC-001`) determines who must be aligned and how much
alignment work is justified.

Discoverability (`METRIC-003`) is the practical test: can an engineer find the decision, owner, contract, obligation,
and review trigger from the affected behavior? Bus Factor (`METRIC-002`) is used only in its current canon meaning. If
one Principal Engineer is the only person who can explain the decision across teams, the system depends on private
memory. Silent Coupling (`SMELL-001`) and Hidden State (`SMELL-004`) describe the drift that appears when teams act on
unwritten assumptions. Temporary Solution (`ANTIPATTERN-006`) describes compatibility paths and exceptions that lack
owner, evidence, review trigger, or expiration condition. The Hero Engineer (`FAILURE-004`) is the failure Chapter 30 is
trying to avoid.

The boundary with Chapter 31 is deliberate. This chapter does not run architecture health reviews, define health
signals, set health-review cadence, or create a recurring assessment process. It only notes that future health work
depends on decisions whose owners, obligations, evidence, and review triggers are visible. Chapter 31 will take up that
broader review loop later.

Chapter 30 is therefore not a generic alignment chapter. It is a technical chapter about making one accepted decision
actionable across ownership boundaries without turning the Principal Engineer into the decision translator for
everyone.
