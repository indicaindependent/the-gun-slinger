# THE CONFORMANCE GATE

Nine mechanical checks. And a standing list of the times the gate itself was wrong
before the brief was.

![The gate](../assets/exports/conformance-gate.png)

---

## THE NINE CHECKS

| # | Requirement | Why mechanical |
| ---: | :--- | :--- |
| 1 | Document-type marker on line 1 | Machine-identifiable, or it is just prose |
| 2 | The mount pin, verbatim | With real dates substituted, not placeholders |
| 3 | A parseable research date | Parsed, never eyeballed |
| 4 | A maintenance-due date | Computed in code as research + 30 days |
| 5 | Routing tags | So the router can match a task to it |
| 6 | A trigger sentence | When this chamber, and not another |
| 7 | Five or more real source URLs | Each fetched. GET, never HEAD |
| 8 | Eight or more prioritised checklist items | Tagged P1/P2/P3 |
| 9 | A closing behavioural note | What changes in conduct, not in knowledge |

All nine, or the chamber is empty. There is no partial credit, because a
partially-loaded chamber fires exactly as confidently as a complete one.

## THE BRIEF IS THE SOURCE OF TRUTH

The journal is **derived** from the briefs and is fully regenerable.

So when the journal and a brief disagree: **regenerate the journal.** Never
hand-edit the journal to agree with the brief. Editing the derived artifact to
match the source converts a *detected* fault into a *hidden* one — the disagreement
was the only signal you had that something was wrong.

---

## THE GATE CAN BE WRONG BEFORE THE BRIEF IS

Every one of these is a real defect that fired against a correct brief. They are
kept as permanent regression cases.

| Defect | What it did |
| :--- | :--- |
| Counted only bullet lines | A checklist formatted as a table read as **zero items** |
| Counted box-drawing characters as emoji | Flagged clean ASCII diagrams as decorated |
| Failed to match a wrapped mount pin | A pin split across lines, or carrying a quote marker, read as absent |
| Counted markdown header rows as items | Inflated checklist counts by the width of the table |
| Counted nested sub-bullets separately | Same |

### The corollary

> **When a probe reports something broad and alarming, suspect the probe first.**

Broad simultaneous failure is nearly always instrumentation. A test that says
everything is broken is usually a broken test. A wrong-scoped credential returns
success with an *empty result set*, not an error — so "nothing found everywhere" is
a signature of a dead instrument, not a clean system.

This is not a licence to dismiss failures. It is an ordering rule: **verify the
instrument before you act on its verdict**, because acting on a false alarm can
destroy a working brief.

### And its inverse, which costs more

A gate that never fails is indistinguishable from a gate that always passes.

So test it with a **deliberately broken brief** and confirm it says no. If you have
never seen your gate refuse anything, you do not have a gate — you have a
formality that has never been exercised.

---

Next: [Never assume](06-never-assume.md)
