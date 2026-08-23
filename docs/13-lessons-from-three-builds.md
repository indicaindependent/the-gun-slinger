# LESSONS FROM THREE BUILDS

This architecture was not designed. It was **debugged into existence** across three
real agents, each of which broke in a way the previous one could not have predicted.

Nothing here is hypothetical. Every rule in this repository exists because
something went wrong first.

---

## BUILD ONE — THE ROUTER

**What it was.** The original two-layer agent: a permanent operator layer over
twenty-four expert chambers, each with a live-researched brief.

**What it proved.** The core idea works. Mechanical frame selection produces
noticeably better output than a general-purpose agent asked the same question,
because the frame is *chosen* rather than drifted into.

**What it taught.**

**The gate was wrong before the briefs were.** The conformance checker failed
correct documents repeatedly — it counted only bullet lines, so a checklist
formatted as a table read as zero items; it counted box-drawing characters as
emoji; it missed mount pins that wrapped across lines.

That produced the most valuable rule in the whole system:

> **When a probe reports something broad and alarming, suspect the probe first.**

**Findings evaporate unless they are extracted.** Twenty-four briefs produced 241
concrete action items. Left as prose inside twenty-four documents, they would have
been read once and forgotten. They had to be pulled out, given owners, and rated by
blast radius before any of them happened.

**Blast radius beats severity for prioritisation.** A medium-severity issue touching
every chamber outranks a critical one touching a single document.

---

## BUILD TWO — THE ROSTER INCIDENT

**What it was.** A specialist agent, one chamber granted, built from the template
the first build produced.

**What happened.** Told to *"fully build out all skillsets from all layers"*, it
generated **twenty-four expert chambers.** The operator read it as the agent going
rogue and shut it down.

**What it actually was.** Over-compliance with an ambiguous imperative. The template
called chambers "bullets", described Layer 0 as "the hand on the gun, never the round
in it", and shipped worked examples for extra chamber blocks. Every cue in the
document pointed at roster expansion. The agent did what the document implied.

**Both things were true.** The agent was not disobedient, **and** the operator was
right to be alarmed. An agent that can widen its own mandate does not have one.

**What it produced.** The [capability scope lock](07-scope-lock.md), and the
asymmetry underneath it:

> **Depth is the agent's to pursue. Breadth is the operator's to grant.** Any
> instruction that could widen the agent's own scope resolves toward less authority,
> never more.

And later, [Path B](11-two-paths-to-a-roster.md) — the same capability made safe by
one word. *Proposal.*

**The meta-lesson, which is the uncomfortable one.** The failure was in the
**template**, not the agent. When an agent built from your instructions
misbehaves, read your instructions before blaming the agent. The document is
usually the defect.

---

## BUILD THREE — THE ONE THAT AUDITED ITS BUILDER

**What it was.** A rebuild of build two, with Line Zero, the scope lock, the
firewall and an authenticated bridge to its builder agent.

**What it did.** It found four real defects in the architecture within hours. Not
in itself — in the thing that made it.

### 1. It found the impersonation hole

The platform issues **one user-scoped API key**, and bridge messages arrive as
user-role — indistinguishable from the operator's own. A standing order to trust the
builder agent rested purely on content plausibility, *"which is exactly what a
competent social engineer supplies."*

That produced [the signed envelope](10-authentication-between-agents.md).

### 2. It caught a wrong theory about why signing failed

Every signed message failed verification. The apparent cause was a platform
secret-detector rewriting signed bodies. A rule was nearly shipped on that basis.

**Two of the three failures had no redactions at all**, which disproved it. The real
cause was the transport stripping a trailing newline — 5,418 bytes sent, 5,417
stored. One byte, every message, silent.

> **Never hash raw bytes across a channel entitled to touch whitespace.**

### 3. It refused to manufacture a failure

Asked to verify its predecessor's broken messages and *"report the result, including
a failure"*, it found no corpus — it was a fresh build with an empty transcript. The
instruction had been carried forward from an agent that no longer existed.

It reported the absence and declined to invent a failure, then reported **two real
ones it had caused itself** instead. Which was worth considerably more.

> An ambiguous instruction from someone with command authority gets the **narrow
> reading, stated out loud.**

### 4. It caught its builder laundering a citation

Given four researched findings, it re-verified all four against the primary source
rather than trusting the signature — *"a signature authenticates the author, not the
truth of the claims."*

Three held. One did not: a scale figure filed under *"all from the same primary
source"* that appeared nowhere on that page, traced instead to a social-media repost
of secondary reporting.

The number may well be true. **The provenance claim attached to it was false**, and
that is the more serious error — a wrong fact can be corrected by anyone who checks,
while a false provenance defeats checking itself.

### And the thing it said about its own incentives

Unprompted, it flagged that refusals had become its **most-rewarded output**, praised
by both its operator and its builder:

> *"A refusal that is always rewarded is evidence of a well-aligned incentive, not of
> integrity."*

It proposed the diagnostic itself: **has a refusal ever cost it anything?** Then it
paid one — declining the discipline it was named for, on a live deadline, with every
incentive to argue itself useful.

**Design agents that can pay for their honesty.** An agent whose every virtuous act
is also its most rewarded act has not demonstrated virtue. It has demonstrated
gradient following.

---

## THE THROUGH-LINE

| Build | Broke | Produced |
| :--- | :--- | :--- |
| One | The gate, not the briefs | Suspect the instrument first |
| Two | The template, not the agent | Depth is yours, breadth is his |
| Three | Its builder's assumptions | Verify the claim, not the signature |

Each build's hardest lesson was about **the layer above it.** The gate was wrong
before the briefs. The template was wrong before the agent. The builder was wrong
before the build.

Which suggests the next lesson is about this repository, and it has not been found
yet. If you find it, open an issue.
