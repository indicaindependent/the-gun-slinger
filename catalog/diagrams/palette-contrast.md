# PALETTE CONTRAST

**Measured contrast for every token**

![palette-contrast](../../assets/exports/palette-contrast.png)

| | |
| :--- | :--- |
| Vector | [`assets/vectors/diagrams/palette-contrast.svg`](../../assets/vectors/diagrams/palette-contrast.svg) |
| Raster | [`assets/exports/palette-contrast.png`](../../assets/exports/palette-contrast.png) |
| Canvas | 1180 x 1000 |
| Type range | 12px - 36px |
| Text nodes | 68 |
| Solid background | yes |
| Blur filters | none |
| Accessible title + desc | yes |

## WHAT IT SHOWS

All twelve design tokens with their contrast ratios against the page and card surfaces.

## DESIGN NOTE

Ratios are recomputed from the hex values at generation time, not read from a stored field. The generator re-verified all twelve on import and found zero mismatches against the inherited values.

---

Regenerate with `python3 lib/build_diagrams.py`. The generator refuses to write an
asset that overflows its canvas, uses an invalid text anchor, carries a blur filter,
or drops type below 12px.
