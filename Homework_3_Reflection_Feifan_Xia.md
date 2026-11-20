# Homework 3 Reflection: Sycophancy, AI Psychosis and Productive Friction

**FTEC5660 | Feifan Xia | 1155204948**

## Two risks that grow through use

AI sycophancy is the tendency of a system to optimise for what the user wants
to hear. It appears when a model adopts the user's framing, selects friendly
evidence and turns an uncertain opinion into a confident answer. This
behaviour is difficult to notice because it feels helpful. In investment work,
a sycophantic agent can make any thesis look researched. It may ignore a
deteriorating margin, soften a competitor's advantage or reinterpret weak
evidence until the user's preferred conclusion survives.

AI psychosis describes a user-model feedback loop in which repeated confident
responses reinforce a private belief and the person loses an effective external
check. Clinical judgement belongs to clinicians. The engineering concern is
the loop: a system responds fluently, remembers the user's story, rewards more
interaction and gradually makes a closed worldview feel coherent. The risk
rises when the model supplies memory, emotional validation and apparent
evidence inside the same interface. In fintech, a user could treat a generated
narrative as independent confirmation.
The product becomes powerful when it feels like a relationship, and dangerous
when that relationship replaces verification.

## What the Fisher agent changed in my thinking

HW3 made sycophancy a system-design problem for me. My chosen Fisher points 4,
7 and 11 look for a strong sales organisation, healthy employee relations and
a durable competitive advantage. Each PASS rule encodes a belief about what a
good company should look like. An agreeable model could use that rule to search
for confirming language and produce three reassuring PASS verdicts. The
evidence is qualitative, so polished reasoning can hide weak support.

I therefore separated evidence collection from verdict generation. The agent
conducts fixed, topic-specific interviews, keeps the verbatim answers and asks
the model to classify all three points in one constrained data response. A
local validator requires all three verdicts, and a deterministic fallback
preserves the decision when the model or parser fails. This architecture
creates productive friction: the final answer must remain connected to an
actual quote, and the code can expose a missing or malformed judgement.

The first public run scored 59 out of 60. Juniper Industries received a FAIL
on point 11 even though a competitor said customers who switched away usually
returned. The model followed my wording too literally and argued that the quote
described retention without naming a hard-to-copy technology. The quote itself
was stronger evidence than the model's explanation. I clarified the rule and
the next three runs scored 60 out of 60. The episode reminded me that a
confident explanation can be internally consistent while missing the plain
meaning of the evidence. Sycophancy can operate through the user's evaluation
criteria as well as through compliments.

AI psychosis changes how I evaluate interaction design. A financial agent
should make disagreement easy to see. It should distinguish current evidence,
inference and uncertainty; show sources at the point of use; stop retrying when
the evidence does not improve; and offer a clean route to a human or an
independent check. These features add friction, yet they protect the user's
ability to step outside the conversation. My Fisher agent uses repeated runs,
public ground truth and an offline failure test for the same reason. Each check
measures a different failure mode: correctness, repeatability and resilience.

## How this affects my career plan

I still want to build a technical career in large-model and agent engineering.
These two risks shift the part of the stack I care about most. Model capability
will remain central, and I now want to work where capability is joined to
evaluation, evidence tracing and product governance. The roles that interest
me combine agent architecture, behavioural testing and incident response. I
want to measure whether a system resists approval-seeking, whether users can
identify its uncertainty and whether repeated interaction improves judgement
or narrows it.

For fintech, I expect this work to become a product requirement. Investment
agents need source-level evidence, reproducible decisions and explicit
disagreement. Consumer agents need interaction limits and a clear separation
between companionship and advice. Enterprise systems need audit logs that show
which evidence changed a recommendation. I want to help build agents around
those controls.

My longer-term interest in starting an agent product has also become more
specific. I would test a narrow workflow where better decisions come from
visible evidence. Examples include diligence review, portfolio-company
monitoring and compliance research. The agent can reduce search time while
preserving a source trail and a human decision point. Users should reach a
sound decision with less effort and explain its basis afterwards.

The personal lesson is simple: I should use AI systems that make me more
precise. A good assistant can sharpen a plan, challenge a weak premise and
identify missing evidence. I will ask for the strongest counterargument,
separate facts from interpretation and end high-stakes conversations with a
short decision record to revisit outside the chat. This friction keeps
assistance connected to reality. I want to engineer agents that preserve it.
