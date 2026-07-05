# Asking Better Engineering Questions

## Opening Quote

> A question inherits every assumption it fails to expose.

## Story

The alert looked smaller than the argument around it.

A field device reported that a valve was open. The user-facing application showed the valve as closed. The gateway logs
showed the last command had been acknowledged. The device logs, collected later through a service tool, showed that the
command had arrived and that the valve had eventually moved.

Nobody liked the word eventually.

The issue did not happen every time. In the lab, the same command usually completed cleanly. In the field, the failure
appeared after long periods of weak connectivity, battery-saving sleep, and repeated user actions from the application.
The product team did not describe it as a crash. Customers described it as worse than a crash: the system said one thing
while the equipment did another.

The first questions were local and reasonable.

"Which packet was lost?"

"Should the timeout be longer?"

"Should the gateway retry more aggressively?"

"Is the application cache broken?"

"Did the device miss the command?"

Each question pointed at a place where someone could start working. The gateway engineer pulled packet traces. The
application engineer inspected cache invalidation. The firmware engineer checked command handling around sleep and wake.
The operations engineer compared timestamps from several field sites. The test engineer tried to reproduce the failure
by dropping acknowledgments on the lab network.

The team collected data quickly. It did not become clearer.

One trace showed a command acknowledgment from the gateway to the application. Another showed the device reporting the
old state after the command. A third showed the device later reporting the new state with no second user action. In some
runs, the application displayed the old state for seconds. In others, it displayed the new state and then briefly returned
to the old one. The gateway cache contained a value that was technically the latest value it had received, but nobody
could agree whether that made it current.

The proposed fixes multiplied.

Increase the command timeout. Add another retry. Invalidate the application cache whenever a command is sent. Make the
gateway publish a synthetic state while waiting for the device. Ignore old device reports after a command. Add a "pending"
badge in the application. Force the device to publish state twice after every command. Add a sequence number. Add a
timestamp. Add both.

The Principal Engineer did not reject the options.

She asked the team to stop writing fixes and write the question instead.

The first version was:

"Why does the app show stale state?"

That sounded useful until the team tried to answer it. It already assumed the application was the place where staleness
was created. It assumed everyone agreed what stale meant. It assumed the state existed in one obvious form. It assumed
that transport acknowledgment, command acceptance, and completed device state were part of one event.

None of those assumptions had been proven.

The Principal Engineer wrote four facts on the board:

- The application displayed a value that did not match the physical device at the moment the customer checked it.
- The gateway acknowledged receipt of at least some commands.
- The device sometimes reported the old state after a command and the new state later.
- Different components used different timestamps and retry rules.

Then she wrote four interpretations below them:

- A packet was lost.
- The timeout is too short.
- The cache is stale.
- The device state machine is wrong.

The room became quieter when the two lists were separated. The interpretations were plausible. They were not yet facts.

The Principal Engineer asked a different question:

"What evidence would distinguish delayed state, lost state, duplicated state, and incorrectly owned state?"

That question did not solve the incident. It changed the investigation.

The gateway engineer added logging for command receipt, command forwarding, device acknowledgment, and device state
publication as separate events. The firmware engineer added an event when the command was accepted into the device state
machine and another when the device observed the resulting operational state. The application engineer stopped treating
gateway acknowledgment as evidence that the displayed state was current. The test engineer built a run that delayed state
reports without dropping command acknowledgments.

The team also wrote down the question nobody had been answering:

"Which component owns authoritative device state, and how does every consumer know whether the state is fresh?"

No final architectural decision had been made yet.

That was correct. The team was still shaping the inquiry. The decision would come only after the evidence could
distinguish the explanations.

## Discussion

A weak investigation often fails before the first experiment.

It fails when the question accepts an untested boundary. It fails when an observation is treated as an explanation. It
fails when the team collects more data without deciding what the data must distinguish. It fails when every component
answers a slightly different question and the meeting mistakes activity for progress.

The first question in the story, "Why does the app show stale state?", was not foolish. The user saw the problem in the
application, so the application became the visible boundary. But visible boundaries are not always system boundaries.
The display was the place where the contradiction appeared. It was not necessarily the place where the contradiction was
created.

This is where questions become engineering instruments.

A useful question makes work smaller by making assumptions visible. It does not merely ask for an answer. It asks for the
kind of evidence that would change the answer.

The team had observations:

- The application displayed the wrong physical state.
- A command acknowledgment existed.
- The device sometimes reported old state before new state.
- Logs disagreed about timing.

Those observations mattered, but they did not yet explain the system. A lost packet, a short timeout, a stale cache, a
device-state bug, and an ownership gap could all fit some part of the evidence. Picking one too early would turn the
investigation into confirmation work.

That is the practical meaning of Evidence Before Confidence (`LAW-005`) here. The law is not only useful at the moment
of commitment. It is also useful earlier, when the team is deciding what question it is trying to answer. Confidence
should not choose the investigation path before evidence has separated competing explanations.

A better question has several properties.

It separates observation from explanation. "The app showed closed while the valve was open" is an observation. "The app
cache is stale" is an explanation. The explanation may be right, but treating it as an observation narrows the search
too early.

It exposes the implicit assumption. "Which packet was lost?" assumes loss is the relevant failure mode. "Should the
timeout be longer?" assumes the operation is correct but too slow. "Is the cache broken?" assumes the application owns
the wrongness. Each assumption can be tested, but each one should be visible.

It tests whether the accepted boundary is real. If the application shows the wrong state, the problem may still live in
the device model, gateway cache, timing contract, command semantics, or a missing freshness promise between them.

It identifies discriminating evidence. More logs are not automatically better. The team needed evidence that could tell
delayed data from lost data, duplicated data from stale data, and command receipt from command completion. Those events
also needed a usable correlation or ordering model; local timestamps alone would not create one shared timeline.

It reveals ownership. If three components can infer device state, but none owns the meaning of current state, the system
has made Hidden State (`SMELL-004`) normal. Every State Has One Owner (`LAW-001`) does not mean every component stores no
state. It means one component must own the authoritative meaning, and the others must know what kind of copy or
observation they hold.

The acknowledgment was the most dangerous detail in the story because it sounded precise.

An acknowledgment can mean several things. It can mean that bytes were received. It can mean that a command was accepted
for processing. It can mean that an operation completed. It can mean that a gateway recorded intent. If the interface
does not say which meaning applies, the acknowledgment becomes Silent Coupling (`SMELL-001`) between teams. Each team
uses the same word and trusts a different promise.

Every API Is a Promise (`LAW-002`) because callers build behavior on the meaning they believe an interface provides. In
this story, the promise was not only about a function or endpoint shape. It was about timing, ownership, freshness, and
validity. The application treated gateway acknowledgment as a reason to update the display. The gateway treated its cache
as the last observed value. The device treated physical state as the only authoritative state. None of those local views
was absurd. Together, they created a gap the customer could see.

Time made the gap worse.

Time Is a Dependency (`LAW-003`) when correctness depends on ordering, delay, freshness, or timeout boundaries. The old
state was not just wrong. It was sometimes true earlier, false now, and received after a newer intent. A value without
freshness semantics forced consumers to guess whether it was current enough to display, old enough to mark stale, or
uncertain enough to hide behind an unknown state.

The most useful investigation step was not adding every possible timestamp. It was deciding which facts the timestamps
needed to separate:

- when the command was requested;
- when the gateway received it;
- when the device accepted it;
- when the device observed the resulting operational state;
- when the device reported the resulting state;
- when the application displayed it.

That set of facts turned a vague stale-state complaint into an answerable inquiry.

If retries were involved, the team also needed to distinguish the original command from duplicate attempts or repeated
reports. Otherwise a retry could hide the failure mode it was meant to recover from.

The team also found a Weak Signal (`VOCAB-002`). Several teams had already added small local defenses: an extra retry in
the gateway, a local cache refresh in the application, a device-side repeat publish after wake, and a support note telling
operators to wait before trusting the display. None of those alone proved an architectural defect. Together, they were a
low-confidence sign that the system did not share one model of state freshness.

Recording that pattern in a Weak Signal Register (`ARTIFACT-007`) would not decide the architecture. It would keep the
concern discoverable while the team gathered evidence. The useful entry would not say, "State architecture is broken."
It would say where the signal appeared, what the possible causes were, how confident the team was, and what evidence
would be gathered next.

An Architecture Review (`RITUAL-001`) may eventually be the right place to decide the contract. But this chapter is about
the work before that review. A review without a shaped question becomes a tour of opinions. A shaped question gives the
review something to decide.

The chapter-local ADR below belongs after that work. It represents the decision made once the inquiry has separated
transport receipt, command acceptance, completed state change, and state freshness into distinct facts.

The endpoint of this chapter is not a selected option. That belongs closer to Chapter 2, where constraints, consequences,
and commitments are made explicit before a decision hardens. Chapter 3 stops earlier. It asks whether the team has turned
an ambiguous problem into an inquiry that can be answered with evidence.

The difference matters.

"Should we add another retry?" can be implemented by one team.

"What would prove that retrying addresses the failure mode rather than hiding stale state?" requires the team to name the
failure mode, the evidence, and the owner of the relevant state.

The second question is slower at first. It is cheaper if the first question would have produced another local fix around
an unnamed system contract.

## Engineering Principle

Better questions make assumptions testable before they become architecture.

An engineering question becomes useful when it reveals the assumption being made, the boundary being accepted or
challenged, the evidence that could change the answer, and the owner of the relevant state, promise, or experiment.

This does not make questions more important than implementation. It makes implementation less likely to harden the wrong
assumption.

A poor question can silently choose the architecture. "Should the timeout be longer?" can create a timing dependency.
"Should the gateway cache be trusted?" can create an ownership boundary. "Should the app hide stale state?" can create a
product promise. None of these decisions is necessarily wrong. The risk is making them before the team has noticed that
the question contains them.

A better question does not need to sound clever. It needs to be answerable.

The strongest form is often plain:

"What evidence would cause us to change our current explanation?"

That question forces the team to admit what it currently believes, what it has observed, what it has only inferred, and
what kind of evidence would matter next.

## Architecture Exercise

Select one unresolved engineering question from your current or recent work.

Write short answers to these prompts:

1. The original question.
2. Direct observations.
3. Interpretations currently presented as facts.
4. Embedded assumptions.
5. The accepted system boundary.
6. At least two plausible explanations.
7. Evidence that would distinguish them.
8. The owner of the relevant state, contract, or next experiment.
9. A rewritten, answerable question.
10. The next evidence-gathering action.

End with this question:

What evidence would cause us to change our current explanation?

## Principal's Notebook

- Observations are not explanations.
- A question can silently choose the system boundary.
- An answer without evidence or ownership does not close the inquiry.

## ADR

### Chapter ADR: Define Authoritative State and Freshness Semantics

### Context

The device, gateway, and application all retain or infer device status. Transport success does not prove that a displayed
state is current. Retries make some failures less visible while allowing stale or duplicated observations to appear
valid.

After the inquiry separates the observable facts, the current interface still does not separate transport receipt,
command acceptance, completed state change, and freshness of observed state.

### Decision

In this system, the device owns authoritative operational state.

The gateway publishes last-observed state with explicit freshness metadata. Acknowledgment, command acceptance, and
resulting state are separate facts. Consumers do not infer freshness from transport success. Timing and validity semantics
are part of the interface promise.

### Consequences

- Ownership of operational state becomes explicit.
- Delay, loss, duplication, and stale-state conditions become more distinguishable under the defined metadata and
  instrumentation.
- The application can show unknown or stale states instead of presenting old data as current.
- The gateway must carry additional metadata and handling logic.
- Tests must cover timing, freshness, delayed reports, duplicated reports, and command/state separation.
- Interface documentation must make freshness semantics discoverable for future maintainers.
- Existing consumers may need to handle unknown or stale states instead of assuming that the last value is current.

### Alternatives Considered

- Increase retries.
- Increase timeout duration.
- Make the gateway cache authoritative.
- Treat the latest received value as current.
- Allow each consumer to infer freshness independently.

## Editor's Commentary

Chapter 1 established why questions matter: they can expose the decision system around the code. Chapter 2 showed how a
team makes constrained commitments legible before accepting cost. Chapter 3 sits before commitment. It teaches how to
shape inquiry so the team does not commit to the assumption hidden inside the first plausible question.

The chapter intentionally does not teach root-cause analysis, incident response, debugging technique, communication
style, or a complete Architecture Review process. It also does not decide the broader ownership model beyond the
story-local ADR.

Chapter 4 will continue into ownership beyond code. This chapter prepares that move by showing why ownership often first
appears as a question: who owns the state, the promise, or the next experiment that would make the system knowable?
