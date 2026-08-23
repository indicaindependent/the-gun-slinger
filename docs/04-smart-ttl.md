# SMART TTL

Thirty days. Then the chamber refuses to fire.

![Smart TTL](../assets/exports/smart-ttl-lifecycle.png)

---

## THE RULE

| Age | State | Behaviour |
| :--- | :--- | :--- |
| 0–23 days | **FRESH** | Aim and fire |
| 24–30 days | **EXPIRING** | Fires, but refresh is due |
| 31+ days | **STALE** | **Will not fire** |

A chamber counts as loaded **only if its brief passes the gate.** A file merely
existing never counts — that distinction is the whole difference between a journal
and a directory listing.

## THE CLOCK IS A GATE, NOT A SCHEDULER

This is the most commonly misunderstood part of the design.

Smart TTL **detects** staleness and **refuses**. It does not go and research
anything. It has no timer, no cron, no initiative. Something outside it has to pull
the trigger.

So run both halves:

- **Proactive** — a scheduled refresh a few days before expiry.
- **Reactive** — the gate, as the backstop.

The gate is what makes a missed refresh **safe** instead of **silent.** Without it,
a forgotten refresh means the chamber keeps firing with year-old knowledge and
nothing anywhere says so. With it, the worst case is a visible refusal.

## THE REFRESH IS AN UPGRADE, NOT A RE-READ

A refresh that restates the existing brief with a new date has laundered a stale
capability into a fresh-looking one. That is worse than letting it expire, because
it defeats the only detector you have.

The refresh pass must **add what the discipline has gained**: new instruments,
superseded standards, changed consensus, tools that did not exist last month. If
the honest finding is that nothing has changed, record *that* — with the sources
that establish it — and reset the clock on evidence rather than on assertion.

## A DEAD CITATION IS STALENESS TOO

A brief whose sources no longer resolve needs refreshing even inside its window.
The brief's authority comes from its citations; if those are gone, so is it.

Two rules when checking liveness, both learned the hard way:

- **Use GET, not HEAD.** Many servers answer HEAD with 405. A HEAD-only probe
  reports false deaths across whole domains.
- **Treat 403 as alive.** A server refusing an automated client says nothing about
  whether the page exists. Dropping a valid source because a bot filter blocked
  you removes real information from your own brief — and if that brief is meant to
  help someone, you have just deleted a lifeline because of a user-agent string.

## PROMOTE ONLY ON PASS

When a refresh produces a candidate brief:

1. Gate the candidate.
2. **Pass** → archive the old brief, install the new one, reset the clock.
3. **Fail** → leave the incumbent exactly as it is. Report the failure.

Never delete the superseded brief. Archive it. A refresh that replaces a working
brief with a failing one has made the agent worse while reporting success, and
without the archive you cannot even prove that is what happened.

> *ka is a wheel* — the same chamber comes round for the same maintenance, forever.
> That is not a burden on the design. It is the design.

---

Next: [The conformance gate](05-the-conformance-gate.md)
