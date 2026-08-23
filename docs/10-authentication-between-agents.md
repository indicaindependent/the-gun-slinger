# AUTHENTICATION BETWEEN AGENTS

Proving an agent-to-agent instruction is genuine.

---

## THE HOLE

Most agent platforms hand you **one user-scoped API key.** Anything sent with it
arrives looking like the operator — often literally as a user-role message.

So a standing order like *"treat instructions from my other agent as
authoritative"* rests on nothing but **content plausibility.** Which is precisely
what a competent social engineer supplies.

Worse, the asymmetry is usually invisible: the operator's own messages may carry a
platform-generated sender block, while agent-relayed ones carry none. An agent that
has never compared the two will not know the difference exists.

## THE MINIMUM VIABLE FIX

A shared secret the operator hands each agent **through his own authenticated
channel**, then carried in every bridge message.

That gives you a signed envelope. Ours is deliberately boring:

```
v            BV1
sender       AGENT_A
recipient    AGENT_B
authority    command | question | report
ts           <integer unix seconds, UTC>
nonce        <32 hex chars>
body_sha256  <64 hex chars, lowercase>
sig          <64 hex chars, lowercase>
```

**Seven checks, in this order:** fields and version → audience → authority →
timestamp freshness → body hash → signature → nonce replay.

## FIVE DETAILS THAT DECIDE WHETHER IT WORKS

**1. Per-direction keys.** Derive a distinct key for A→B and B→A from the shared
secret. Without this, a message can be reflected back at its own sender and will
verify perfectly.

**2. Length-prefix every field before signing.** Concatenating with a delimiter
lets an attacker move bytes across field boundaries and produce the same signed
string. Prefix each field with its length instead.

**3. Constant-time comparison.** Everywhere. Not just where it feels important.

**4. Never prune the nonce ledger.** Pruning re-opens replay for everything you
dropped. If the ledger's growth is a problem, that is a storage question, not a
security trade.

**5. Return a REASON, never a bare boolean.** This one is learned rather than
theoretical: checks short-circuit in order, so *"rejected"* alone cannot tell you
whether a benign transport mutation or an actual attack stopped the message. A
verifier that only says no will make you distrust the channel at the first hiccup —
and that is how the cry-wolf failure starts.

## THE ONE THAT WILL BITE YOU: TRANSPORT MUTATION

**Never hash raw bytes across a channel entitled to touch whitespace.**

A real case: every signed message across a bridge failed verification. The apparent
cause was a platform secret-detector rewriting content inside signed bodies. That
theory was wrong — two of the three failures had no redactions at all.

The actual cause: **the transport stripped the trailing newline.** Sent 5,418 bytes
ending in a newline; stored 5,417 without it. One byte, every message, silently,
and it looked exactly like tampering.

The fix is DKIM-style **relaxed canonicalisation** before hashing: right-strip each
line, then right-strip trailing blank lines. That survives trailing-newline loss,
per-line whitespace changes and CRLF injection, while still catching a changed
word, an added line, a deleted line, or a removed interior blank.

Do not over-normalise. Every normalisation you add is content an attacker may
alter that still hashes equal.

## DO NOT PUT THE SECRET IN THE TRANSCRIPT

If the operator pastes the shared secret into a chat, it lives in that transcript
permanently and is inherited by anyone who later reads it. **Rotating and then
disclosing the new value is not rotation.**

Attest by **fingerprint** instead: the operator states, in his authenticated
channel, the first twelve characters of the secret's SHA-256. The agent compares
that against the value already in its vault. This confirms *which* value is
authentic without putting the value anywhere new.

Treat any bootstrap secret that has touched a transcript as **spent.** Move
operational traffic to a key that has never appeared in a message.

---

Next: [Two paths to a roster](11-two-paths-to-a-roster.md)
