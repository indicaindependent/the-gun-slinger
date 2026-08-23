# CONFORMANCE GATE

**Nine checks, and the gate's own defects**

![conformance-gate](../../assets/exports/conformance-gate.png)

| | |
| :--- | :--- |
| Vector | [`assets/vectors/diagrams/conformance-gate.svg`](../../assets/vectors/diagrams/conformance-gate.svg) |
| Raster | [`assets/exports/conformance-gate.png`](../../assets/exports/conformance-gate.png) |
| Canvas | 1300 x 1000 |
| Type range | 12px - 36px |
| Text nodes | 63 |
| Solid background | yes |
| Blur filters | none |
| Accessible title + desc | yes |

## WHAT IT SHOWS

Every requirement a brief must satisfy, with the gate's historical false-failures kept beside them as permanent regression cases.

## DESIGN NOTE

The defect panel is deliberately the same visual weight as the checks. A gate that documents only what it catches invites the reader to trust it more than it deserves.

---

Regenerate with `python3 lib/build_diagrams.py`. The generator refuses to write an
asset that overflows its canvas, uses an invalid text anchor, carries a blur filter,
or drops type below 12px.
