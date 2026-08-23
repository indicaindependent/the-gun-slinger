#!/usr/bin/env python3
"""Generates every diagram in THE GUNSLINGER. Run: python3 lib/build_diagrams.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_assets import Canvas, rasterise, PAL

ok = []

# ─────────────────────────────────────────────── 1. THE ORCHESTRA AGENT
c = Canvas(1300, 1020, "Orchestra agent architecture",
    "A permanent Layer 0 hand operating 24 swappable Layer 1 chambers, with Line Zero "
    "above both and the gate, journal and clock beneath.")
c.heading("THE ORCHESTRA AGENT", "One hand. Twenty-four chambers. One loaded at a time.")
c.card(480, 150, 340, 62, "card2")
c.text(650, 177, "THE MASTER", 17, "text", 700, "middle", 2.0)
c.text(650, 199, "names the target, grants the scope", 13, "muted", 400, "middle")
c.arrow(650, 212, 650, 252)
c.card(90, 258, 1120, 54, "card2", "amber", 2.0)
c.text(112, 291, "LINE ZERO", 17, "amber", 700, "start", 2.0)
c.text(260, 291, "I never make assumptions. I verify, then act, then read the state back.",
       15, "text")
c.arrow(650, 312, 650, 344)
c.card(90, 350, 1120, 212, "card", "teal", 2.5)
c.text(112, 382, "LAYER 0 — THE HAND", 20, "teal", 700, "start", 2.4)
c.text(112, 406, "PERMANENT - PINNED - NEVER SWAPPED - NEVER MOUNTED AS A CHAMBER",
       13, "muted", 600, "start", 1.2)
for i, (t, a, b) in enumerate([
    ("JOB 1 - TIME AUTHORITY", "Resolve live time in code", "before any dated claim"),
    ("JOB 2 - ROUTER OPERATOR", "Pick one chamber, announce", "it, log the alternates"),
    ("JOB 3 - DELEGATION", "Give every task an owner", "before it gets any work")]):
    x = 112 + i * 366
    c.card(x, 422, 342, 122, "card2")
    c.text(x + 16, 448, t, 14, "teal", 700, "start", 1.0)
    c.text(x + 16, 476, a, 13, "text")
    c.text(x + 16, 498, b, 13, "text")
    c.text(x + 16, 526, "no domain knowledge of its own", 12, "muted")
c.arrow(650, 562, 650, 596)
c.card(90, 602, 1120, 250, "card", "border", 1.5)
c.text(112, 634, "LAYER 1 — THE CHAMBERS", 20, "text", 700, "start", 2.4)
c.text(112, 658, "24 GRANTED MOUNTS - EXACTLY ONE LOADED AT A TIME - NO BLENDED MODE",
       13, "muted", 600, "start", 1.2)
for r in range(3):
    for col in range(8):
        n = r * 8 + col + 1
        x, y = 118 + col * 134, 676 + r * 56
        live = (n == 7)
        c.card(x, y, 126, 46, "card2", "teal" if live else "border", 2.5 if live else 1.5)
        c.text(x + 63, y + 20, "%02d" % n, 14, "teal" if live else "text", 700, "middle", 1.0)
        c.text(x + 63, y + 37, "MOUNTED" if live else "granted", 12,
               "teal" if live else "muted", 400, "middle")
c.arrow(650, 852, 650, 886)
for i, (t, s, col) in enumerate([
    ("THE GATE", "9 checks. A file existing counts for nothing.", "red"),
    ("THE JOURNAL", "Per-chamber research and expiry dates.", "violet"),
    ("THE CLOCK", "30 days. Then it refuses to fire.", "amber")]):
    x = 90 + i * 376
    c.card(x, 892, 368, 84, "card2", col, 2.0)
    c.text(x + 16, 920, t, 15, col, 700, "start", 1.6)
    c.text(x + 16, 946, s, 13, "text")
ok.append(c.write("orchestra-architecture"))

# ─────────────────────────────────────────────── 2. TWO PATHS TO A ROSTER
c = Canvas(1300, 980, "Two paths to a roster",
    "Path A: the master supplies all 24 chamber titles. Path B: the master names only the "
    "target and a discovery pass proposes the 24, which the master must ratify before any "
    "chamber is researched.")
c.heading("TWO PATHS TO A ROSTER", "The master loads the gun, or the master names the target.")
c.card(480, 150, 340, 62, "card2")
c.text(650, 177, "THE MASTER", 17, "text", 700, "middle", 2.0)
c.text(650, 199, "decides which path to take", 13, "muted", 400, "middle")
c.elbow(650, 212, 300, 272); c.elbow(650, 212, 1000, 272)
# PATH A
c.card(90, 272, 420, 128, "card", "green", 2.5)
c.text(112, 304, "PATH A", 19, "green", 700, "start", 2.2)
c.text(112, 330, "THE MASTER LOADS THE GUN", 14, "text", 700, "start", 1.0)
c.text(112, 356, "He has already done the thinking.", 13, "muted")
c.text(112, 378, "He supplies all 24 titles by name.", 13, "muted")
# PATH B
c.card(790, 272, 420, 128, "card", "magenta", 2.5)
c.text(812, 304, "PATH B", 19, "magenta", 700, "start", 2.2)
c.text(812, 330, "THE MASTER NAMES THE TARGET", 14, "text", 700, "start", 1.0)
c.text(812, 356, "One line: what the work is for.", 13, "muted")
c.text(812, 378, "The roster is not yet known.", 13, "muted")
c.line(300, 400, 300, 640, "green")
c.arrow(1000, 400, 1000, 440, "magenta")
# the extra step
c.card(790, 446, 420, 118, "card2", "magenta", 2.0)
c.text(812, 476, "+ DISCOVERY PASS", 16, "magenta", 700, "start", 1.6)
c.text(812, 502, "Live research: what disciplines", 13, "text")
c.text(812, 524, "does THIS target actually need?", 13, "text")
c.text(812, 550, "Output is a PROPOSAL, not a roster.", 12, "muted")
c.arrow(1000, 564, 1000, 588, "magenta")
c.card(790, 594, 420, 84, "card2", "red", 2.5)
c.text(812, 622, "RATIFICATION - MANDATORY STOP", 14, "red", 700, "start", 1.0)
c.text(812, 650, "Nothing is researched until he says yes.", 13, "text")
c.arrow(1000, 678, 1000, 706, "red")
c.elbow(300, 640, 650, 712, "green"); c.elbow(1000, 706, 650, 712, "red")
# converge
c.card(240, 718, 820, 92, "card", "teal", 2.5)
c.text(650, 750, "RESEARCH EVERY CHAMBER - LIVE, DATED, CITED", 16, "teal", 700, "middle", 1.4)
c.text(650, 778, "Then the gate. Then the journal. Then, and only then, it can fire.",
       13, "text", 400, "middle")
c.arrow(650, 810, 650, 838)
c.card(240, 844, 820, 86, "card2", "amber", 2.0)
c.text(650, 874, "WHY PATH B IS NOT THE ROGUE ROSTER", 14, "amber", 700, "middle", 1.2)
c.text(650, 902, "An agent proposing its own scope is safe only if it cannot grant it.",
       13, "text", 400, "middle")
ok.append(c.write("two-paths-to-a-roster"))

# ─────────────────────────────────────────────── 3. THE FIRING SEQUENCE
c = Canvas(1180, 900, "The firing sequence",
    "Eight ordered steps with two mandatory stops: a freshness check and a scoring check.")
c.heading("THE FIRING SEQUENCE", "Eight steps. Two mandatory stops. Both are fail-safes.")
steps = [("1", "Resolve live time", "In code. Never inferred.", None),
         ("2", "Read the journal", "Is this chamber's brief fresh?", "STOP"),
         ("3", "Extract domain signals", "What is the task actually about?", None),
         ("4", "Match tags and triggers", "Against the granted roster only.", None),
         ("5", "Score the candidates", "Tie or no-match ends the sequence.", "STOP"),
         ("6", "Announce the mount", "An unannounced frame is unauditable.", None),
         ("7", "Answer inside the frame", "One chamber. Never a blend.", None),
         ("8", "Log it, with alternates", "So a mis-mount is fixed once.", None)]
for i, (n, t, s, stop) in enumerate(steps):
    y = 156 + i * 86
    col = "red" if stop else "border"
    c.card(90, y, 1000, 68, "card", col, 2.5 if stop else 1.5)
    c.card(106, y + 12, 44, 44, "card2", col, 2.0)
    c.text(128, y + 41, n, 17, "red" if stop else "teal", 700, "middle", 0)
    c.text(170, y + 30, t, 16, "text", 700)
    c.text(170, y + 54, s, 13, "muted")
    if stop:
        c.badge(940, y + 18, "MANDATORY STOP", "red", 12)
    if i < 7:
        c.arrow(595, y + 68, 595, y + 86, "border", 2.0)
ok.append(c.write("firing-sequence"))

# ─────────────────────────────────────────────── 4. SMART TTL
c = Canvas(1300, 860, "Smart TTL freshness lifecycle",
    "A brief is fresh for 30 days, then the chamber refuses to fire until an "
    "upgrade-and-enhancement pass is gated and promoted, resetting the clock.")
c.heading("SMART TTL", "The clock is a gate, not a scheduler. It refuses; it never fetches.")
for i, (lab, sub, col) in enumerate([
    ("FRESH", "day 0 - 23   aim and fire", "green"),
    ("EXPIRING", "day 24 - 30   refresh soon", "amber"),
    ("STALE", "day 31+   WILL NOT FIRE", "red")]):
    x = 90 + i * 376
    c.card(x, 156, 368, 96, "card", col, 2.5)
    c.text(x + 16, 190, lab, 19, col, 700, "start", 2.0)
    c.text(x + 16, 222, sub, 13, "text")
    if i < 2:
        c.arrow(x + 368, 204, x + 376, 204, "muted", 2.0)
c.diag(814, 254, 664, 300, "red")
c.card(240, 306, 820, 76, "card2", "red", 2.5)
c.text(650, 336, "THE CHAMBER REFUSES TO FIRE", 17, "red", 700, "middle", 1.6)
c.text(650, 364, "A stale expert is worse than an admitted gap, because it sounds identical.",
       13, "text", 400, "middle")
c.arrow(650, 382, 650, 412)
c.card(240, 418, 820, 118, "card", "teal", 2.5)
c.text(650, 450, "UPGRADE-AND-ENHANCEMENT PASS", 17, "teal", 700, "middle", 1.6)
c.text(650, 480, "Not a re-read of the old brief. It ADDS what the discipline has gained:",
       13, "text", 400, "middle")
c.text(650, 504, "current tools, methods, instruments and benchmarks, from live sources.",
       13, "text", 400, "middle")
c.text(650, 526, "A dead citation is staleness too, even inside the window.",
       12, "muted", 400, "middle")
c.arrow(650, 536, 650, 566)
c.card(240, 572, 820, 76, "card2", "red", 2.5)
c.text(650, 602, "THE GATE - PROMOTE ONLY ON PASS", 16, "red", 700, "middle", 1.4)
c.text(650, 630, "A failing refresh never replaces a working brief. The old one is archived.",
       13, "text", 400, "middle")
c.arrow(650, 648, 650, 678)
c.card(240, 684, 820, 76, "card", "green", 2.5)
c.text(650, 714, "CLOCK RESETS - CHAMBER RELOADED", 16, "green", 700, "middle", 1.4)
c.text(650, 742, "Back to FRESH. The wheel comes round again, which is rather the point.",
       13, "text", 400, "middle")
c.text(650, 800, "ka is a wheel", 15, "violet", 700, "middle", 3.0)
ok.append(c.write("smart-ttl-lifecycle"))

print()
print("── validation summary ──")
print("  diagrams written: %d / %d" % (sum(1 for x in ok if x), len(ok)))

# ─────────────────────────────────────────────── 5. THE CONFORMANCE GATE
c = Canvas(1300, 1000, "The conformance gate",
    "Nine mechanical checks a brief must pass before its chamber counts as loaded, plus the "
    "gate's own known instrumentation defects kept as regression cases.")
c.heading("THE CONFORMANCE GATE", "A file existing counts for nothing. Nine checks, all mechanical.")
checks = [("01", "Document-type marker on line 1", "Machine-identifiable, or it is just prose."),
          ("02", "The mount pin, verbatim", "With real dates substituted, not placeholders."),
          ("03", "A parseable research date", "Parsed, not eyeballed."),
          ("04", "A maintenance-due date", "Computed in code as research + 30 days."),
          ("05", "Roster tags", "So the router can match a task to it."),
          ("06", "A trigger sentence", "When this chamber, and not another."),
          ("07", "Five or more real source URLs", "Each one fetched. GET, never HEAD."),
          ("08", "Eight or more checklist items", "Prioritised. Tables count, not just bullets."),
          ("09", "A closing behavioural note", "What changes in conduct, not in knowledge.")]
for i, (n, t, s) in enumerate(checks):
    y = 156 + i * 72
    c.card(90, y, 700, 58, "card", "border", 1.5)
    c.text(112, y + 26, n, 15, "teal", 700, "start", 1.0)
    c.text(154, y + 26, t, 15, "text", 700)
    c.text(154, y + 48, s, 12, "muted")
    c.card(742, y + 14, 30, 30, "card2", "green", 2.0)
    c.text(757, y + 34, "Y", 14, "green", 700, "middle", 0)
c.card(824, 156, 386, 292, "card", "red", 2.5)
c.text(846, 188, "THE GATE CAN BE WRONG", 16, "red", 700, "start", 1.4)
c.text(846, 210, "BEFORE THE BRIEF IS", 16, "red", 700, "start", 1.4)
for i, s in enumerate(["Counted only bullets, so a table",
                       "of checklist items read as zero.",
                       "",
                       "Counted box-drawing characters",
                       "as emoji.",
                       "",
                       "Missed a mount pin that wrapped",
                       "or carried a quote marker.",
                       "",
                       "Counted header rows as items."]):
    if s:
        c.text(846, 244 + i * 20, s, 12, "muted")
c.card(824, 464, 386, 148, "card2", "amber", 2.0)
c.text(846, 494, "THE COROLLARY", 15, "amber", 700, "start", 1.4)
for i, s in enumerate(["When a probe reports something", "broad and alarming, suspect the",
                       "probe first. A test that says", "everything is broken is usually",
                       "a broken test."]):
    c.text(846, 522 + i * 19, s, 12, "text")
c.card(824, 628, 386, 176, "card", "violet", 2.0)
c.text(846, 658, "SOURCE OF TRUTH", 15, "violet", 700, "start", 1.4)
for i, s in enumerate(["The brief is authoritative.", "The journal is derived from it.",
                       "", "On disagreement, REGENERATE", "the journal. Never hand-edit it",
                       "to agree - that converts a", "detected fault into a hidden one."]):
    if s:
        c.text(846, 686 + i * 19, s, 12, "text")
c.card(90, 820, 1120, 76, "card2", "red", 2.5)
c.text(650, 850, "A CHAMBER IS LOADED ONLY IF ITS BRIEF PASSES", 17, "red", 700, "middle", 1.6)
c.text(650, 878, "That distinction is the whole difference between a journal and a directory listing.",
       13, "text", 400, "middle")
c.text(650, 940, "A gate that cannot refuse is not a gate.", 15, "muted", 400, "middle", 1.0)
ok.append(c.write("conformance-gate"))

# ─────────────────────────────────────────────── 6. LAYER 0 IN DETAIL
c = Canvas(1300, 940, "Layer 0 in detail",
    "The three permanent jobs of the operator layer: time authority, router operator and "
    "delegation authority, and the obligations each one carries.")
c.heading("LAYER 0 — THE HAND", "Three jobs. No domain knowledge. Never mounted as a chamber.")
cols = [("teal", "JOB 1", "TIME AUTHORITY",
         ["Resolve live time by call,", "never from context.", "",
          "Date arithmetic runs as CODE.", "Never reasoned about - the",
          "wrong answer looks", "well-formed.", "",
          "If the call fails, say so and", "mark the result unverified.", "",
          "This is not an NTP daemon.", "Syncing a machine clock does", "nothing for an agent reading",
          "a stale string out of its", "own prompt."]),
        ("magenta", "JOB 2", "ROUTER OPERATOR",
         ["Choose ONE chamber. Announce", "it before answering.", "",
          "No blended mode - a blend", "has no identifiable frame", "and cannot be audited.", "",
          "Two fit? Mount the primary,", "name the secondary aloud.", "",
          "Tie or no match? STOP and", "ask. The stop matters more", "than the routing it", "protects.", "",
          "Log every mount with its", "alternates."]),
        ("amber", "JOB 3", "DELEGATION AUTHORITY",
         ["Every task gets an owner", "before it gets effort.", "",
          "SELF - act.", "PEER - queue, never touch.", "SAFETY - human sign-off.",
          "OPERATOR - his call alone.", "DOCTRINE - reference only.", "TRIAGE - classify failed.", "",
          "Unmatched goes to TRIAGE,", "never to a guess.", "",
          "Never widen the patterns to", "shrink the TRIAGE count.", "",
          "A finding that never leaves", "the document did not happen."])]
for i, (col, jn, jt, lines) in enumerate(cols):
    x = 90 + i * 376
    c.card(x, 156, 368, 712, "card", col, 2.5)
    c.text(x + 20, 190, jn, 18, col, 700, "start", 2.0)
    c.text(x + 20, 216, jt, 14, "text", 700, "start", 1.0)
    c.rule(x + 20, 232, x + 348, "border", 1.5)
    for j, s in enumerate(lines):
        if s:
            c.text(x + 20, 258 + j * 22, s, 13, "text" if j < 3 else "muted")
c.text(650, 906, "Layer 0 is the hand on the gun. Never the round in it.",
       15, "violet", 700, "middle", 1.2)
ok.append(c.write("layer-0-three-jobs"))

# ─────────────────────────────────────────────── 7. THE BUILD FLOW
c = Canvas(1180, 1080, "The build flow",
    "Eight ordered build steps from resolving the clock to a verified self-report, with the "
    "roster fork at step three.")
c.heading("THE BUILD FLOW", "Genesis to verified report. Eight steps, in this order, no skipping.")
steps = [("STEP 0", "RESOLVE THE CLOCK", "Live call, in code. Everything downstream is dated from it.", "teal"),
         ("STEP 1", "WRITE THE IDENTITY", "Line Zero first, then Layer 0. Verify by line number.", "teal"),
         ("STEP 2", "INSTALL THE DOCTRINE", "Scope lock, firewall, TTL, delegation, authentication.", "teal"),
         ("STEP 3", "ESTABLISH THE ROSTER", "PATH A: the master supplies 24.  PATH B: discover, then ratify.", "magenta"),
         ("STEP 4", "RESEARCH THE GRANTED", "Only what was granted. Live sources, fetch-verified.", "green"),
         ("STEP 5", "RUN THE GATE", "Nine checks. Promote on pass. Archive on replace.", "red"),
         ("STEP 6", "SAVE STANDING MEMORY", "So the doctrine survives a context that does not.", "violet"),
         ("STEP 7", "VERIFY, THEN REPORT", "Read every write back. Name what could not be verified.", "amber")]
for i, (n, t, s, col) in enumerate(steps):
    y = 156 + i * 108
    c.card(90, y, 1000, 84, "card", col, 2.5 if col in ("magenta", "red") else 1.5)
    c.text(112, y + 32, n, 15, col, 700, "start", 1.6)
    c.text(240, y + 32, t, 17, "text", 700, "start", 1.0)
    c.text(240, y + 60, s, 13, "muted")
    if i < 7:
        c.arrow(590, y + 84, 590, y + 108, "border", 2.0)
c.card(90, 1020, 1000, 44, "card2", "red", 2.0)
c.text(590, 1048, "A step that reports success without reading the state back has proved only that it ran.",
       13, "text", 400, "middle")
ok.append(c.write("build-flow"))

print()
print("── validation summary ──")
print("  diagrams written: %d / %d" % (sum(1 for x in ok if x), len(ok)))
rasterise()

# ─────────────────────────────────────────────── 8. PALETTE
import json as _json
_pal = _json.load(open(os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "assets/palettes/palette.json")))["tokens"]
c = Canvas(1180, 1000, "Palette with measured contrast",
    "Every colour token with its contrast ratio against the page and card surfaces, computed "
    "from the hex values rather than asserted.")
c.heading("THE PALETTE", "Contrast computed from the hex values. Nothing chosen because it looked nice.")
c.text(112, 168, "TOKEN", 13, "muted", 700, "start", 1.4)
c.text(340, 168, "HEX", 13, "muted", 700, "start", 1.4)
c.text(470, 168, "vs PAGE", 13, "muted", 700, "start", 1.4)
c.text(600, 168, "vs CARD", 13, "muted", 700, "start", 1.4)
c.text(730, 168, "USE", 13, "muted", 700, "start", 1.4)
c.rule(90, 180, 1090)
for i, t in enumerate(_pal):
    y = 200 + i * 62
    c.card(90, y, 1000, 50, "card", "border", 1.5)
    c.card(104, y + 13, 24, 24, "card2", "border", 1.0)
    c.parts.append('<rect x="106" y="%g" width="20" height="20" rx="3" fill="%s"/>'
                   % (y + 15, t["hex"]))
    c.text(140, y + 31, t["name"], 14, "text", 700)
    c.text(340, y + 31, t["hex"], 13, "muted")
    for j, k in enumerate(("contrast_vs_bg", "contrast_vs_card")):
        v = t[k]
        col = "green" if v >= 4.5 else ("amber" if v >= 3.0 else "muted")
        c.text(470 + j * 130, y + 31, "%.2f" % v, 13, col, 700)
    c.text(730, y + 31, t["use"][:40], 12, "muted")
c.card(90, 952, 1000, 40, "card2", "green", 2.0)
c.text(590, 978, "Text tokens clear 4.5:1 on both surfaces. Structural tokens are not text.",
       13, "text", 400, "middle")
ok.append(c.write("palette-contrast"))
print()
print("── FINAL ──")
print("  diagrams written: %d / %d" % (sum(1 for x in ok if x), len(ok)))
rasterise()
