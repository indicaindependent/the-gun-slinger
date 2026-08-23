# THE IDEA

Why frame selection has to be mechanical.

---

## THE FAILURE THIS PREVENTS

Ask a general-purpose agent a cryptography question and it will answer. Ask it an
epidemiology question and it will answer that too. Both answers will be fluent,
well-organised, and confident.

Neither is anchored to what the discipline currently believes.

This is not a knowledge problem — the model has read the literature. It is a
**framing** problem. The agent has no mechanism for deciding *which kind of
practitioner it is being*, so it produces text with the surface features of a
discipline and none of its judgement. It reads like expertise because expertise is
mostly what it was trained on.

The dangerous part is not that an answer is wrong. It is that **nothing in the
output tells you which frame produced it.** A confident answer from the wrong frame
is indistinguishable from a correct one — including to the agent producing it.

## THE MOVE

Make frame selection explicit, mechanical, dated and logged.

- **Explicit** — the agent names which discipline it is operating in, before it
  answers. An unannounced frame cannot be audited.
- **Mechanical** — the choice comes from matching task signals against a roster,
  not from a vibe. Same task, same mount, every time.
- **Dated** — each discipline's brief carries the date it was researched, and
  expires. Expertise is a claim about the present.
- **Logged** — mount decisions are recorded with the alternates considered, so a
  wrong choice is corrected once instead of recurring.

## WHY TWENTY-FOUR

There is nothing magic about the number. It comes from a revolver metaphor that
turned out to be load-bearing rather than decorative:

| Term | Component |
| :--- | :--- |
| **The master** | The operator. Names the target; never has to name the tool |
| **The gunslinger** | The agent. Chooses the round and fires it |
| **The gun** | The router — a machine-readable roster plus a fixed procedure |
| **A chamber** | One granted discipline |
| **A bullet** | One live-researched, dated, cited working brief |
| **A fully formed bullet** | A brief that passes the conformance gate |
| **The journal** | Per-chamber research and expiry dates |
| **Maintenance** | The thirty-day refresh |

The metaphor earns its place because it forces the right question. Not "does the
agent know about X" but **"is there a round in the chamber, and was it made
recently enough to fire?"**

Use six chambers. Use forty. What matters is that the count is *granted*, and that
an empty chamber is never reported as a capability.

## WHAT THIS IS NOT

**Not a prompt library.** A prompt that says "you are an expert epidemiologist"
produces the exact failure described above, faster.

**Not fine-tuning.** No weights change. The capability is a researched document
the agent reads, which means it can be inspected, dated, corrected and expired.

**Not an agent swarm.** One agent, many frames, one at a time. Multiple agents can
be bound together — see [delegation](09-delegation-and-the-queue.md) — but that is
a separate concern from routing.

---

Next: [Layer 0 — the hand](01-layer-0-the-hand.md)
