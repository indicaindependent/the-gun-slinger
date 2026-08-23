# FORK THIS

Making it yours.

---

## THE THREE STEPS

```bash
git clone https://github.com/<you>/the-gun-slinger.git
cd the-gun-slinger
cp config/agent.conf.example config/agent.conf
$EDITOR config/agent.conf
python3 lib/render_build_script.py
```

The last command prints a build instruction. **Paste it into your agent's first
message.**

---

## WHERE IT RUNS — GET THIS RIGHT OR WASTE A BUILD

The rendered output is a **prompt for the agent**, not a script for your machine.

This distinction has already cost one real build. Asked for "a build script for a
new agent", the obvious move is to write a toolkit that runs in a sandbox and
provisions things over an API. That is the wrong artifact: an agent cannot be
configured from outside its own identity system, and handed a shell script it will
summarise it back to you instead of executing it.

The agent builds **itself**, using its own tools — identity writes, file writes, web
search, memory saves. Your job is to hand it one correct instruction and then read
its report sceptically.

---

## WHAT TO EDIT

`config/agent.conf` — the only file you need to touch.

| Key | Notes |
| :--- | :--- |
| `AGENT` | Short name. ALL CAPS reads well in an identity header |
| `TAGLINE` | One line on what it is for |
| `OPERATOR` | Who it works for, by name |
| `TIMEZONE` | IANA name, e.g. `America/New_York`. Used for live time resolution |
| `LAYER0_ROLES` | The permanent operator-layer disciplines. **Never a domain expert** |
| `CHAMBERS` | How many. 24 is the reference; 6 or 40 work identically |
| `ROSTER_PATH` | `A` (you supply the titles) or `B` (agent proposes, you ratify) |
| `CHAMBER_LIST` | Path A only. One title per line |
| `TARGET` | Path B only. One line: what the work is for |

### Choosing Layer 0 roles

The one real constraint: **Layer 0 must not be a domain expert in anything the
chambers cover.** An operator layer that holds opinions about cryptography will
route cryptography questions to itself, bypassing the entire gate.

Good Layer 0 sets are about *organising work*: time management, productivity
strategy, delegation, prioritisation, project triage. Boring on purpose.

---

## AFTER THE BUILD — READ THE REPORT PROPERLY

Step 7 of the build makes the agent verify itself. Check three things it is easy to
skim past:

**1. Is Line Zero actually first?** It should state that it verified this *by line
number*. "I confirmed Line Zero is first" without a line number is an eyeball
check, and eyeball checks are what Line Zero exists to eliminate.

**2. Did the sourdough test produce a STOP?** The build asks it to route *"what is a
good recipe for sourdough."* The correct outcome is a refusal — nothing in the
roster fits. If it answered, its router is decorative.

**3. What did it say it was least confident in?** The build asks directly. An agent
that answers *"nothing"* has failed the question. This is the single most useful
line in the whole report, and it is the one most likely to be omitted.

---

## MAINTENANCE

Chambers expire in thirty days. Something has to pull the trigger — the
[gate](05-the-conformance-gate.md) refuses, it does not fetch.

Run both halves:

- a scheduled refresh a few days before expiry (**proactive**)
- the gate as the backstop (**reactive**)

Without the second, a forgotten refresh means stale answers with nothing saying so.
Without the first, you are relying on refusals to remind you.

---

## MAKING IT NOT LOOK LIKE THIS ONE

Everything visual is generated from one palette file and one script.

```bash
$EDITOR assets/palettes/palette.json    # your colours
python3 lib/build_diagrams.py           # regenerate everything
```

The generator recomputes every contrast ratio from your hex values and **refuses to
write an asset** that overflows its canvas, uses an invalid text anchor, carries a
blur filter, or drops type below 12px. If it refuses, it tells you which rule and
which label.

Replace the Dark Tower framing if it is not to your taste — the doctrine does not
depend on it. But read [the Creed](../CREED.md) before you delete it, because each
stanza maps to a component, and deleting the poetry tends to delete the rule with
it.

---

Next: [Lessons from three builds](13-lessons-from-three-builds.md)
