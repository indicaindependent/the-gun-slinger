# FIRING SEQUENCE

**Eight steps, two mandatory stops**

![firing-sequence](../../assets/exports/firing-sequence.png)

| | |
| :--- | :--- |
| Vector | [`assets/vectors/diagrams/firing-sequence.svg`](../../assets/vectors/diagrams/firing-sequence.svg) |
| Raster | [`assets/exports/firing-sequence.png`](../../assets/exports/firing-sequence.png) |
| Canvas | 1180 x 900 |
| Type range | 12px - 36px |
| Text nodes | 28 |
| Solid background | yes |
| Blur filters | none |
| Accessible title + desc | yes |

## WHAT IT SHOWS

The ordered routing procedure. Steps 2 and 5 can end the sequence without producing an answer.

## DESIGN NOTE

Both stops carry an explicit badge rather than relying on colour alone, so the diagram survives greyscale printing and colour-vision differences.

---

Regenerate with `python3 lib/build_diagrams.py`. The generator refuses to write an
asset that overflows its canvas, uses an invalid text anchor, carries a blur filter,
or drops type below 12px.
