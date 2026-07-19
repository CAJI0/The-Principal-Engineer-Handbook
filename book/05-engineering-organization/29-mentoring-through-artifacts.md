# Mentoring Through Artifacts

## Opening Quote

The best mentoring artifacts do not tell people what to think. They show how judgment was formed, what evidence
mattered, what trade-offs were accepted, and what would change the decision.

## Story

### The Answer That Did Not Teach

Mara noticed the pattern during Architecture Review, although the pattern was not in the diagram.

Three different engineers had asked her the same question in six weeks:

"What is the right retry pattern for this?"

The first time, the question came from the device team. A field sensor gateway could lose radio coverage while sending
telemetry from a remote installation. The engineer wanted to know whether firmware should retry locally, whether the
backend should retry the ingest call, or whether the system should accept a gap and rely on the next sample window.
Mara answered quickly and correctly. The firmware could retry local transient I/O, but once a command crossed into
product-visible state, the owner of that state had to define the retry budget, duplicate handling, and operator
consequence. Telemetry could tolerate delay; service commands could not pretend that replay was harmless.

The answer was correct. The change landed.

The second time, the question came from the service tools team. A field technician could press "apply configuration"
from a laptop in a noisy shop, lose connectivity, and press it again. The engineer had found an old ADR that said,
"Retry failed gateway requests three times with exponential delay." He asked if the same helper should be used. Mara
explained that the old decision had been about telemetry delivery from gateway to backend, not command submission by a
human-facing tool. The operation needed an owner, a visible command identifier, and a consequence for duplicate
execution. Three retries was not the lesson.

That answer was also correct. The change landed too.

The third time, the manufacturing systems team opened a pull request that reused the same retry helper for provisioning
packages sent to devices on the line. The code was neat. The tests passed. The review comment from a staff engineer was
short: "Use the existing retry helper so behavior matches the gateway path."

Mara stared at the comment longer than the code.

The engineer who opened the pull request had not asked a bad question. He had found a real precedent and followed it.
The problem was that the precedent did not teach him where it stopped being valid.

The repository had plenty of records. There was an ADR for retry strategy. It recorded the final decision but hid
alternatives and uncertainty: local transient failures at the gateway boundary could use bounded exponential retry,
while product-visible commands needed duplicate handling and explicit ownership. It had a status, a date, and a neat
consequences section. It did not show the alternatives the team rejected. It did not show which evidence made retries
acceptable for telemetry but risky for commands. It did not show the uncertainty the team still carried about low-signal
field networks.

There was an RFC thread. It had all the interesting reasoning, if a patient reader had forty minutes and excellent
memory. Buried inside comments were questions about radio dropouts, duplicate technician actions, backend queue
semantics, manufacturing station timeouts, and who would handle customer support if a command executed twice. The
thread showed people wrestling with the real decision. But it was long, unstructured, and closed. New engineers found
the ADR, not the reasoning that produced it.

There was a Mistake Ledger entry from the previous quarter. A technician command had been sent twice after a laptop
lost its connection during a site visit. The entry captured the field escape, the fix, and the customer impact. It did
not capture the changed mental model: retry strategy was not a loop-count question. It was an ownership, consequence,
and dependency question. The field failure had taught the team that retrying across a boundary could import obligations
from the device, backend, operator workflow, support process, and release train. The record preserved the scar but not
the lesson.

There were review comments too. Most said what to change. "Use command id." "Do not retry this path." "Add delay."
"Move retry to gateway boundary." They were useful in the moment. They were not useful six months later, because they
said what to change, but not why the change was responsible in that context.

By the time the manufacturing pull request appeared, the team had a working system of private interpretation. Engineers
could find artifacts, but only Mara could reliably translate them. The Architecture Ledger linked to the retry ADR and
marked it accepted, but the row did not tell a new engineer which example was safe to learn from or which examples had
become obsolete. The same question kept returning because the records preserved answers better than they preserved
judgment.

In review, someone said what everyone had been thinking.

"Can you document the correct approach?"

Mara almost opened a new page called `retry-best-practices.md`. It would have been faster. She could have written five
rules, linked the helper, and told teams to ask her before doing anything unusual.

Then she imagined the next engineer reading it and asking the same question in a different shape.

Instead she said, "What artifact would help someone practice the judgment, not just copy the answer?"

They chose one recurring decision type: retry behavior across a boundary where the operation might have side effects.
They did not try to turn every architecture record into training material. They chose this one because the Change
Radius was broad: firmware, backend ingest, service tools, manufacturing systems, support procedures, and field
operations could all inherit the consequences of one retry decision. The Bus Factor was also obvious. If Mara had to
explain the judgment every time, the architecture depended on her availability.

The team updated the retry ADR, but they did not make it longer just to look complete. They changed its shape.

At the top, they added the decision question:

"Where should retry responsibility live when a request may cross a boundary, cause side effects, or be observed by a
human workflow?"

Under context, they separated three cases:

- gateway telemetry delivery, where duplicate samples were tolerable if the backend could identify them;
- service-tool commands, where duplicate execution could change product state and confuse the technician;
- manufacturing provisioning, where retries could hide a station, device, or release-package ownership problem.

Under evidence, they linked the radio-loss data from field logs, the support ticket from the duplicate technician
command, the manufacturing station timeout report, and the test evidence showing which failures were transient. Under
alternatives, they restored the options that had disappeared from the final ADR: retry everywhere with one helper,
retry only at clients, retry only at the backend, reject automatic retry for command paths, and require an explicit
operation identifier for any side effect that could be retried.

The accepted trade-off became visible. The team would allow bounded retry for transport failures only where the owner
of the resulting state had defined duplicate handling. They would not let a generic retry helper make an operation look
safe merely because it was convenient. Where a temporary workaround was still in use, the artifact named the owner, the
expiry condition, and the review date. Old examples that had taught "three retries is our pattern" were marked
obsolete, with a link to the updated ADR.

Mara added two short learner cues.

What to notice: the retry count was less important than the owner of the consequence.

What not to generalize: the gateway telemetry example did not make retries safe for every boundary or every command.

They linked the old RFC thread as proposal history, but they also summarized the decision-shaping questions so a reader
did not have to excavate them. They added a Decision Journal entry for the manufacturing case because it was smaller
than a full ADR but worth revisiting after the next pilot line run. They updated the Mistake Ledger entry with the
changed mental model from the field escape. They changed the Architecture Ledger row so an engineer searching from
"retry helper," "service command," or "manufacturing provisioning" could find the ADR, the owner, the status, the
review date, and the related examples.

At the next Architecture Review, Mara did not present the ADR as doctrine. She used it as a teaching surface. She
asked the engineer who had copied the gateway pattern to walk through the decision question, then identify which parts
of the old example applied and which did not. The conversation took longer than a direct answer. It also changed who
could answer the next question.

Two weeks later, a different engineer opened an RFC for retrying a backend job that reconciled delayed telemetry. The
first paragraph did not ask for the right pattern. It named the decision:

"This is a retry decision across a boundary with delayed observations but no user-visible command side effect."

The RFC linked to the retry ADR, named the owner of the resulting state, described the evidence, and called out what
would change the decision. Mara still reviewed it. She had useful questions. But for the first time in months, she was
not the artifact the team had to query.

## Discussion

Chapter 28 showed that rituals protect technical behavior by making it repeatable. Chapter 29 turns to the records
those rituals leave behind. A review, decision, field lesson, or release choice can either become stale evidence that a
senior engineer must interpret later, or it can become a mentoring surface that helps another engineer practice the
judgment behind the decision.

Mentoring at Principal Engineer level is rarely only a private conversation. Private conversation matters. It lets a
person ask the unfinished question, admit confusion, and borrow the judgment of someone who has seen the system fail in
more ways. But if every meaningful lesson stays in private conversation, the organization recreates the Hero Engineer
failure in a softer form. The system depends on one person's memory, patience, and calendar. That is a Bus Factor
problem even when everyone involved is generous.

The goal is not to replace mentoring with documents. Artifacts are poor substitutes for attention. A pile of ADRs handed
to a new engineer without context is not mentoring; it is artifact dumping. A review comment that says "use the existing
pattern" may be efficient, but it teaches obedience more readily than judgment. A knowledge base that records every
decision without exposing context can make the system look more mature while preserving the same private bottleneck.

The useful question is narrower: where does an existing artifact already contain judgment that other engineers need to
learn?

That boundary matters. Direct advice helps in the moment. Coaching helps a person inspect their own reasoning. Ramp-up
documentation helps someone find the system. Code review and design review improve a specific change. Process records
and architecture records preserve organizational memory. Mentoring through artifacts is different: it uses a real
engineering record to show how a technical judgment was formed, where it applies, and where copying it would become
dangerous.

An ADR can teach the shape of a decision when it names the question, owner, evidence, rejected options, accepted
trade-offs, consequences, uncertainty, and revisit trigger. An ADR that only records the final answer may be valuable
for governance, but it is a weak mentoring artifact. It tells a reader what the team chose. It does not teach how to
make the adjacent decision when one constraint changes.

An RFC can teach proposal judgment. It shows what people were worried about before the decision hardened: affected
owners, alternative designs, migration concerns, dependency obligations, and unresolved questions. But RFC threads
often hide their best material in comment history. If the final decision does not carry forward the important reasoning,
future readers will either ignore the RFC or treat the loudest comment as the lesson.

A Decision Journal entry can teach smaller judgment moves. It can preserve confidence, uncertainty, evidence gaps, and
the condition that would cause the team to revisit the choice. That is especially useful for mentoring because many
engineering decisions are too small for a full ADR and too important to leave as memory.

A Mistake Ledger entry can teach changed thinking. A field escape or failed assumption should not only say what broke
and what was fixed. It should say what the team learned to see differently. Without that changed mental model, the same
failure becomes a story people retell instead of a lesson people can apply.

An Architecture Ledger row can teach by making decisions discoverable. Discoverability is not the existence of a file
somewhere. It is the ability for an engineer to move from the affected behavior to the decision, owner, status, related
records, and reasoning. If a developer can find a helper function but not the reason it exists, the code becomes the
teacher. Sometimes that teacher is misleading.

Review notes can also teach, but only when they explain the judgment behind the requested change. "Use command id" is
useful instruction. "Use command id because this path crosses an operator-visible boundary and duplicate execution
changes product state" is mentoring. The second version names ownership, consequence, and context. It lets the learner
recognize a similar decision later.

Artifacts fail as mentoring surfaces when they hide uncertainty. Teams often hide uncertainty because they want records
to look authoritative. The effect is backwards. A decision without uncertainty looks more general than it is. A reader
cannot tell why the team rejected an option. That hidden state invites copying. The copied pattern silently couples a
new team to context it never understood.

This is Hidden State in organizational form: the record exists, but the reasoning that makes it safe to use is still
somewhere else. A Temporary Solution has the same mentoring risk when the artifact keeps the workaround visible but
loses the owner, expiry condition, or reason it was allowed.

This is where Change Radius becomes practical. The broader the affected surface of a decision, the more important it is
to make the reasoning teachable. A local implementation choice may need only a review comment and a test. A retry
strategy that affects firmware, backend behavior, field tools, support expectations, manufacturing stations, and
release operations deserves a record that teaches. The point is not ceremony. The point is that many people will inherit
the consequences.

Teaching artifacts also need boundaries. The phrase "what to notice" tells the learner where the judgment lives. In the
retry story, the judgment was not "three retries." It was "who owns the consequence if the operation happens twice?"
The phrase "what not to generalize" protects the artifact from becoming a pattern library by accident. A valid example
in telemetry delivery may be dangerous when copied into human-triggered commands.

Obsolete examples require the same discipline. Unused flexibility can masquerade as wisdom when old artifacts keep
teaching options the system no longer supports. A temporary workaround can look like an approved pattern if the owner,
expiry condition, and review trigger are missing. Leaving those examples discoverable without warnings teaches the
wrong lesson with the authority of history.

Good artifact-based mentoring is therefore selective. Not every ADR needs learner annotations. Not every review comment
needs a paragraph of teaching. Not every mistake needs to become a curriculum. Choose decisions that recur, decisions
with broad consequence, decisions that are often copied, and decisions where the old record hides the reasoning needed
to make the next call.

The artifact should still be used with people. Bring it into Architecture Review. Ask a staff engineer to compare two
contexts before recommending a pattern. Use it in a mentoring conversation when someone asks for the right answer. Ask
the learner to identify the owner, evidence, trade-off, dependency, uncertainty, and revisit trigger. The artifact makes
the conversation repeatable. It does not make the conversation unnecessary.

This is also how a Principal Engineer avoids becoming the default interpreter of the system. The work is not to encode
all personal judgment into templates. It is to preserve enough real reasoning that others can practice the decision
without needing the same person in the room every time. The measure is not document volume. The measure is whether the
next engineer asks a better question.

## Engineering Principle

Mentor by preserving judgment, not just answers. Use artifacts to show the question, constraints, evidence,
alternatives, trade-offs, owner, consequences, and revisit triggers so another engineer can practice the decision, not
merely copy the result.

When choosing where to invest, ask:

- What recurring decision are engineers struggling to make?
- Which artifact already contains useful judgment?
- What reasoning is hidden from the current record?
- What uncertainty or rejected option should be visible?
- What should the learner notice?
- What should they not generalize?
- What context makes this example valid?
- What would change the decision?
- Where will this artifact be used in review, ramp-up, or mentoring?
- Which obsolete example should be marked or retired?

## Architecture Exercise

### Turn One Decision Into a Teaching Artifact

Choose one existing decision record that people keep copying, questioning, or misapplying. Prefer a decision with real
Change Radius: multiple teams, an external dependency, field consequence, manufacturing effect, support burden, or
future migration cost.

Do not create a new canonical artifact for this exercise. Improve one record that already exists, or add a linked
companion note if the original record should remain concise.

Document:

- the decision question;
- the learner audience;
- the context that made the decision valid;
- the constraints that shaped the choice;
- the evidence the team trusted;
- the alternatives considered;
- one rejected option and why it was rejected;
- the accepted trade-off;
- the owner of the decision and its consequences;
- the consequence inherited by future engineers;
- the uncertainty the team still carries;
- the revisit trigger;
- the lesson the learner should notice;
- the warning about what not to overgeneralize;
- the record that will be updated;
- the conversation or review where the artifact will be used.

End with:

1. one decision question;
2. one hidden reasoning element to expose;
3. one lesson to notice;
4. one warning not to generalize;
5. one artifact update.

## Principal's Notebook

- A good artifact teaches the shape of a decision.
- Mentoring fails when records hide uncertainty.
- The goal is better judgment without you in the room.

## ADR

### Turn the Retry Strategy ADR Into a Mentoring Artifact

#### Status

Accepted for the team in the story.

#### Context

Several engineers keep asking the same architecture question about retry strategy across device, backend, service-tool,
and manufacturing boundaries. The existing retry ADR states the final decision, but it does not teach the judgment that
made the decision responsible. Relevant RFC discussion, review notes, a Decision Journal entry, a Mistake Ledger entry,
and the Architecture Ledger row are scattered. A field issue changed the team's mental model about retrying operations
with side effects, but that lesson is hard to find. Mara is becoming the default explainer.

#### Decision

Update the retry ADR, or add a linked companion note if the ADR must stay concise, so the record exposes the decision
question, context, constraints, evidence, rejected options, accepted trade-offs, uncertainty, owner, consequences, and
revisit trigger.

Link the related RFC, Decision Journal entry, Mistake Ledger entry, and Architecture Ledger row. Add a short "what to
notice / what not to generalize" section. Use the artifact in future Architecture Review and mentoring conversations.
Mark obsolete examples that teach "three retries is the pattern" without showing the boundary, owner, and consequence
that make retry safe.

#### Consequences

Engineers can learn the retry judgment from a real decision instead of asking Mara for the answer every time. The retry
helper becomes less likely to create Silent Coupling because the artifact explains where the example applies and where
it does not. Reasoning becomes more discoverable from the affected behavior, the owner is clearer, and uncertainty is
visible enough to guide future review. The team also accepts maintenance cost: the artifact must stay linked, obsolete
examples must be marked, and temporary exceptions must keep owner, expiry condition, and revisit trigger.

#### Alternatives Considered

- Write a generic best-practices page.
- Answer engineers individually.
- Require everyone to read the ADR as-is.
- Create a training deck detached from real decisions.
- Rely on code comments.
- Make the senior engineer approve every similar decision.

## Editor's Commentary

Chapter 29 follows Chapter 28 by taking the outputs of durable engineering practice and asking whether they teach.
Chapter 28 was about rituals that keep valuable behavior alive. This chapter is about the artifacts those rituals and
decisions leave behind: ADRs, RFCs, Decision Journal entries, Mistake Ledger entries, Architecture Ledger rows, and
review notes that can either preserve judgment or bury it.

The chapter keeps `ARTIFACT-001` - ADR - as the illustrated center. The retry ADR is not presented as better
documentation in the abstract. It becomes a place where ownership, evidence, dependency consequences, Change Radius,
Bus Factor, Discoverability, uncertainty, and revisit triggers can be practiced by another engineer. RFCs preserve
proposal reasoning, Decision Journals preserve smaller judgments, Mistake Ledgers preserve changed mental models, and
Architecture Review gives the team a place to use the record in conversation.

The boundaries are intentional. This is not a chapter about career coaching, ramp-up, performance management,
documentation systems, or review etiquette. It does not repeat Chapter 17's ADR/RFC mechanics, Chapter 27's design
review memory, or Chapter 28's ritual design. It also leaves Chapter 30's alignment work and Chapter 31's architecture
health review work for later. Better artifacts can support those later concerns, but this chapter's job is narrower:
show how a Principal Engineer helps others practice technical judgment without making the Principal Engineer the only
interpreter of the system.
