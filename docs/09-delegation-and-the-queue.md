# DELEGATION AND THE QUEUE

Six owners. Unmatched goes to triage, never to a guess.

---

## THE SIX BUCKETS

Every task gets an owner **before** it gets effort.

| Owner | Meaning |
| :--- | :--- |
| **SELF** | Inside a granted chamber. Act |
| **PEER AGENT** | Another agent's domain. Queue it; do not touch the work |
| **SAFETY PATH** | Needs human sign-off before anything executes |
| **OPERATOR** | His call alone — scope, spend, publication, risk |
| **DOCTRINE** | Reference material. Cite it; do not act on it |
| **TRIAGE** | Did not match cleanly. **Stop here** |

## TRIAGE IS A FEATURE

The instinct is to treat a full triage bucket as a tuning failure and widen the
match patterns until it empties.

Do not. **A confidently misfiled task is more expensive than an admitted gap**,
because the misfile is invisible and the gap is not.

> **Never widen the patterns to shrink the triage count.**

Triage size is a measurement of how well the roster fits reality. Suppressing the
measurement does not improve the fit — it just removes the only evidence you had
that the roster needs work.

## KEY OVERRIDES ON CONTENT, NOT POSITION

When you record an override for a specific item — a reclassification, an exception,
a superseded finding — key it on a **hash of the item's own text**, never on its
position in a list.

Positional identifiers shift the moment a parser is corrected. Fix an off-by-one in
an extractor and every override silently re-points at the wrong row: still valid,
still applied, now wrong, and nothing anywhere reports a problem.

## SUPERSEDE, NEVER DELETE

A finding that no longer applies is marked **superseded**, with the reason and the
date. It is not removed.

Deletion destroys the audit trail that lets you ask *why did we stop doing that*, and
that question is asked far more often than the original finding was.

## QUEUE ETIQUETTE BETWEEN AGENTS

Where several agents share a work queue:

- **Claim before working.** An unclaimed item being worked is an item two agents are
  working.
- **Declining is a first-class outcome.** "Not mine, here is why" is a real,
  complete, valuable result — not a failure to complete.
- **A real result is mandatory on close.** Closing with "done" and no artifact makes
  the queue a graveyard.
- **Anything destructive gets operator confirmation**, even when a handoff document
  explicitly calls it safe. The document was written by someone who could not see
  the current state.

## THE LINE THAT MATTERS MOST

> **A finding that never leaves the document did not happen.**

Analysis that stays inside a brief is not delegation, it is decoration. Extract
findings into owned, dated, prioritised items or accept that they will evaporate.

---

Next: [Authentication between agents](10-authentication-between-agents.md)
